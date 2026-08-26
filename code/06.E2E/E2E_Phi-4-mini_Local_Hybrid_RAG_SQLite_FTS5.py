"""
Hybrid Retrieval-Augmented Generation (RAG) with Microsoft phi-4-mini & SQLite FTS5
===================================================================================
A standalone, reference cookbook demonstrating:
1. Deterministic local embeddings (feature-hashing) with Cosine Similarity, or
   real embeddings from Microsoft Foundry Local (phi-4-mini) when installed/available
2. Sparse Full-Text Search (SQLite FTS5 BM25)
3. Reciprocal Rank Fusion (RRF, k=60) Hybrid Merging [Cormack, Clarke & Buettcher, 2009]
4. Grounded Prompt Engineering with In-Text Citations ([1], [2])
5. Optional local SLM generation via Microsoft Foundry Local SDK (phi-4-mini),
   with a transparent fallback when the Foundry Local runtime/model isn't available.

References:
- Cormack, G.V., Clarke, C.L.A., Buettcher, S. "Reciprocal Rank Fusion outperforms
  Condorcet and Individual Rank Learning Methods." SIGIR 2009.
  https://dl.acm.org/doi/10.1145/1571941.1572114
- Robertson, S., Zaragoza, H. "The Probabilistic Relevance Framework: BM25 and Beyond."
  Foundations and Trends in Information Retrieval, 2009.
- SQLite FTS5 Extension: https://www.sqlite.org/fts5.html
- Microsoft Foundry Local: https://github.com/microsoft/Foundry-Local
- Phi-4-mini model card: https://huggingface.co/microsoft/Phi-4-mini-instruct

Note on benchmarks: this reference implementation does not ship a formal
faithfulness/accuracy benchmark. Retrieval quality on your own corpus should
be measured independently (e.g. Recall@k, citation-coverage) before quoting
any accuracy figure in downstream documentation.

Author: Çağrı Giray Keşan (@Cagrik34)
License: MIT
"""

import hashlib
import logging
import os
import sqlite3
import sys

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import numpy as np
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

# Configuration Constants
DB_PATH = ":memory:"          # In-memory SQLite for high-speed demonstration
RRF_K = 60                    # Standard Reciprocal Rank Fusion smoothing constant
TOP_K = 3                     # Number of hybrid chunks to retrieve
EMBEDDING_DIM = 256            # Dimensionality for the local fallback embedding
FOUNDRY_MODEL_ALIAS = "phi-4-mini"


def hash_embedding(text: str, dim: int = EMBEDDING_DIM) -> List[float]:
    """Deterministic, dependency-free local embedding via feature hashing.

    This is a real (if simple) embedding technique -- not a mock -- commonly
    used as a lightweight baseline (e.g. Vowpal Wabbit style hashing trick).
    It has no external/model dependency, so this recipe is fully reproducible
    offline. For production-quality semantic retrieval, replace this with
    embeddings from an actual model (see `try_get_foundry_embedding` below).
    """
    vec = np.zeros(dim, dtype=np.float32)
    tokens = text.lower().split()
    for token in tokens:
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        bucket = int.from_bytes(digest[:4], "big") % dim
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vec[bucket] += sign
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec.tolist()


class FoundryLocalUnavailable(Exception):
    """Raised when the Foundry Local SDK/runtime cannot service a request."""


def try_get_foundry_embedding(text: str, alias: str = FOUNDRY_MODEL_ALIAS) -> List[float]:
    """Attempts to compute a real embedding via Microsoft Foundry Local (phi-4-mini).

    Requires the `foundry-local-sdk` package AND the Foundry Local runtime/app
    installed locally with the model downloaded. Raises FoundryLocalUnavailable
    if either the SDK or the running service is not present, so callers can
    fall back to `hash_embedding`.
    """
    try:
        from foundry_local_sdk import Configuration, FoundryLocalManager
    except ImportError as exc:
        raise FoundryLocalUnavailable(f"foundry-local-sdk is not installed: {exc}") from exc

    try:
        config = Configuration(app_name="phi-cookbook-hybrid-rag")
        if FoundryLocalManager.instance is None:
            FoundryLocalManager.initialize(config)
        manager = FoundryLocalManager.instance
        model = manager.catalog.get_model(alias)
        if model is None:
            raise FoundryLocalUnavailable(f"Model alias '{alias}' not found in local catalog.")
        model.load()
        embedding_client = model.get_embedding_client()
        response = embedding_client.generate_embedding(text)
        return list(response.data[0].embedding)
    except FoundryLocalUnavailable:
        raise
    except Exception as exc:  # native runtime missing, model not cached, etc.
        raise FoundryLocalUnavailable(f"Foundry Local runtime unavailable: {exc}") from exc


def try_generate_with_foundry(prompt: str, alias: str = FOUNDRY_MODEL_ALIAS) -> str:
    """Attempts a real phi-4-mini generation call via Microsoft Foundry Local.

    Raises FoundryLocalUnavailable if the SDK/runtime/model isn't available so
    callers can fall back to returning the constructed prompt for manual use.
    """
    try:
        from foundry_local_sdk import Configuration, FoundryLocalManager
    except ImportError as exc:
        raise FoundryLocalUnavailable(f"foundry-local-sdk is not installed: {exc}") from exc

    try:
        config = Configuration(app_name="phi-cookbook-hybrid-rag")
        if FoundryLocalManager.instance is None:
            FoundryLocalManager.initialize(config)
        manager = FoundryLocalManager.instance
        model = manager.catalog.get_model(alias)
        if model is None:
            raise FoundryLocalUnavailable(f"Model alias '{alias}' not found in local catalog.")
        model.load()
        chat_client = model.get_chat_client()
        completion = chat_client.complete_chat([{"role": "user", "content": prompt}])
        return completion.choices[0].message.content
    except FoundryLocalUnavailable:
        raise
    except Exception as exc:
        raise FoundryLocalUnavailable(f"Foundry Local runtime unavailable: {exc}") from exc


class LocalHybridRAGStore:
    """Lightweight SQLite-backed store combining Vector Cosine Similarity and FTS5 BM25."""

    def __init__(self, db_path: str = DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self._init_schema()

    def _init_schema(self) -> None:
        """Initializes both dense document storage and virtual FTS5 full-text table."""
        with self.conn:
            # Dense Vector Table
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS document_chunks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_file TEXT NOT NULL,
                    chunk_index INTEGER NOT NULL,
                    content TEXT NOT NULL,
                    embedding BLOB NOT NULL
                )
            """)
            # Sparse FTS5 Virtual Table for BM25 Token Search
            self.conn.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS document_chunks_fts USING fts5(
                    content,
                    source_file UNINDEXED,
                    chunk_index UNINDEXED,
                    tokenize='unicode61'
                )
            """)

    def insert_chunk(self, source_file: str, chunk_index: int, content: str, embedding: List[float]) -> None:
        """Stores a chunk and its normalized embedding vector into both indices."""
        vec = np.array(embedding, dtype=np.float32)
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm

        with self.conn:
            self.conn.execute(
                "INSERT INTO document_chunks (source_file, chunk_index, content, embedding) VALUES (?, ?, ?, ?)",
                (source_file, chunk_index, content, vec.tobytes())
            )
            self.conn.execute(
                "INSERT INTO document_chunks_fts (content, source_file, chunk_index) VALUES (?, ?, ?)",
                (content, source_file, str(chunk_index))
            )

    def search_dense(self, query_embedding: List[float], top_k: int = 5) -> List[Tuple[int, str, str, float]]:
        """Performs Cosine Similarity search over normalized vector blobs."""
        q_vec = np.array(query_embedding, dtype=np.float32)
        q_norm = np.linalg.norm(q_vec)
        if q_norm > 0:
            q_vec = q_vec / q_norm

        cursor = self.conn.execute("SELECT id, source_file, content, embedding FROM document_chunks")
        results = []
        for doc_id, src, content, blob in cursor.fetchall():
            doc_vec = np.frombuffer(blob, dtype=np.float32)
            similarity = float(np.dot(q_vec, doc_vec))
            results.append((doc_id, src, content, similarity))

        results.sort(key=lambda x: x[3], reverse=True)
        return results[:top_k]

    def search_sparse_bm25(self, query_text: str, top_k: int = 5) -> List[Tuple[int, str, str, float]]:
        """Performs BM25 token matching via SQLite FTS5 match queries."""
        # Sanitize query for FTS5 syntax
        clean_tokens = [t for t in query_text.replace("'", "").replace('"', '').split() if len(t) > 1]
        if not clean_tokens:
            return []

        fts_query = " OR ".join(f'"{t}"' for t in clean_tokens)
        cursor = self.conn.execute(
            """
            SELECT rowid, source_file, content, rank
            FROM document_chunks_fts
            WHERE document_chunks_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (fts_query, top_k)
        )
        results = []
        for doc_id, src, content, bm25_rank in cursor.fetchall():
            # In SQLite FTS5, lower rank value means higher BM25 relevance
            bm25_score = 1.0 / (1.0 + abs(float(bm25_rank)))
            results.append((doc_id, src, content, bm25_score))
        return results

    def hybrid_search(self, query_text: str, query_embedding: List[float], top_k: int = TOP_K) -> List[Dict[str, Any]]:
        """
        Fuses Dense and Sparse results using Reciprocal Rank Fusion (RRF).
        Formula: RRF_score(d) = sum(1 / (k + rank_dense(d)), 1 / (k + rank_sparse(d)))
        Reference: Cormack, Clarke & Buettcher, SIGIR 2009.
        """
        dense_hits = self.search_dense(query_embedding, top_k=10)
        sparse_hits = self.search_sparse_bm25(query_text, top_k=10)

        fused_scores: Dict[str, float] = {}
        chunk_map: Dict[str, Tuple[str, str, str]] = {}

        # 1. Score Dense Ranks
        for rank, (doc_id, src, content, sim) in enumerate(dense_hits, start=1):
            key = f"{src}::{content[:50]}"
            chunk_map[key] = (src, content, "vector")
            fused_scores[key] = fused_scores.get(key, 0.0) + (1.0 / (RRF_K + rank))

        # 2. Score Sparse Ranks
        for rank, (doc_id, src, content, bm25) in enumerate(sparse_hits, start=1):
            key = f"{src}::{content[:50]}"
            if key not in chunk_map:
                chunk_map[key] = (src, content, "bm25")
            else:
                chunk_map[key] = (src, content, "hybrid")
            fused_scores[key] = fused_scores.get(key, 0.0) + (1.0 / (RRF_K + rank))

        # 3. Sort by aggregated RRF score
        sorted_keys = sorted(fused_scores.keys(), key=lambda k: fused_scores[k], reverse=True)[:top_k]

        output = []
        for citation_idx, key in enumerate(sorted_keys, start=1):
            src, content, match_type = chunk_map[key]
            output.append({
                "citation_index": citation_idx,
                "source_file": src,
                "content": content,
                "rrf_score": fused_scores[key],
                "match_type": match_type
            })
        return output


def construct_grounded_prompt(query: str, retrieved_chunks: List[Dict[str, Any]]) -> str:
    """Builds a hallucination-resistant prompt with explicit citation requirements."""
    context_blocks = []
    for chunk in retrieved_chunks:
        context_blocks.append(f"[{chunk['citation_index']}] (Source: {chunk['source_file']})\n{chunk['content']}")

    context_str = "\n\n".join(context_blocks)

    prompt = f"""You are Zenith AI, an enterprise-grade local assistant.
Answer the user query strictly based on the provided context below.
Every factual claim must cite its source index like [1] or [2].
If the context does not contain the answer, respond: 'This information is not present in the indexed documents.'

--- CONTEXT ---
{context_str}
--- END CONTEXT ---

User Query: {query}
Answer:"""
    return prompt


def embed(text: str) -> List[float]:
    """Returns a real embedding for `text`: Foundry Local (phi-4-mini) if available,
    otherwise the deterministic local hashing fallback (always available offline)."""
    try:
        return try_get_foundry_embedding(text)
    except FoundryLocalUnavailable as exc:
        logger.info("Falling back to local hash embedding (%s)", exc)
        return hash_embedding(text)


# =============================================================================
# Demonstration / Execution Example
# =============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("  🚀 MICROSOFT PHI-4-MINI + SQLITE FTS5 HYBRID RAG COOKBOOK")
    print("=" * 70)

    store = LocalHybridRAGStore()

    # Sample Corpus. Embeddings are computed from the actual chunk text (via
    # `embed`), not hand-picked constants, so retrieval genuinely reflects
    # the content and is reproducible from scratch.
    sample_docs = [
        ("q3_financial_report.pdf", 0, "CodePulse engineering project total Q3 budget was allocated at 2,340,000 TL with 15 active developers."),
        ("architecture_specs.md", 0, "Zenith AI leverages Microsoft phi-4-mini (3.8B parameters) for local zero-cloud inference."),
        ("hr_policy_2026.docx", 0, "Remote work expense allowance is capped at 15,000 TL per employee quarterly."),
    ]

    print("\n📦 Ingesting sample documents into SQLite Vector + FTS5 tables...")
    for src, idx, content in sample_docs:
        store.insert_chunk(src, idx, content, embed(content))
    print("✅ Ingestion complete.")

    # Test Query
    query = "What is the total allocated budget for the CodePulse project?"
    query_vector = embed(query)

    print(f"\n🔍 Query: '{query}'")
    hits = store.hybrid_search(query, query_vector, top_k=2)

    print("\n📊 Retrieved Hybrid Results (Reciprocal Rank Fusion):")
    for hit in hits:
        print(f"  [{hit['citation_index']}] {hit['source_file']} ({hit['match_type'].upper()}) -> RRF Score: {hit['rrf_score']:.4f}")
        print(f"      \"{hit['content']}\"")

    prompt = construct_grounded_prompt(query, hits)
    print("\n📝 Constructed Grounded Prompt for phi-4-mini:\n")
    print(prompt)

    print("\n🤖 Attempting local generation via Microsoft Foundry Local (phi-4-mini)...")
    try:
        answer = try_generate_with_foundry(prompt)
        print("\n✅ phi-4-mini response:\n")
        print(answer)
    except FoundryLocalUnavailable as exc:
        reason = str(exc).splitlines()[0]
        print(f"\n⚠️  Foundry Local generation unavailable in this environment: {reason}")
        print("    Install `foundry-local-sdk`, install the Foundry Local app, and run")
        print("    `foundry model run phi-4-mini` to enable real generation. Falling back")
        print("    to displaying the constructed prompt only (see above).")

    print("\n" + "=" * 70)
    print("✅ Reference Hybrid RAG Cookbook Executed Successfully!")
    print("=" * 70)
