"""Deductive and abductive reasoning evaluation for Phi models.

Works with any OpenAI-compatible chat endpoint: Foundry Local, Ollama,
vLLM, GitHub Models or a Microsoft Foundry deployment.

Datasets (both MIT licensed, pulled from their public sources at runtime):
  * PARARULE-Plus  - deductive reasoning, depth 2-5   (Bao et al., 2022)
  * AbductionRules - abductive reasoning              (Young, Bao et al., 2022)
"""

from __future__ import annotations

import json
import random
import re
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

PARARULE_URL = (
    "https://huggingface.co/datasets/qbao775/PARARULE-Plus/resolve/main/"
    "Depth{d}/PARARULE_Plus_Depth{d}_shuffled_test_huggingface.jsonl"
)
ABDUCTION_URL = (
    "https://raw.githubusercontent.com/Strong-AI-Lab/AbductionRules/main/"
    "datasets/Abduction-{domain}-Simple/test.jsonl"
)

DEDUCTIVE_PROMPT = """You are given a set of facts and rules about some entities, followed by a statement.
Decide whether the statement is True or False based only on the facts and rules.
Use the closed-world assumption: anything that is not stated and cannot be derived from the rules is false.
So a condition such as "someone is not big" holds whenever "big" cannot be derived for that person.

Facts and rules:
{context}

Statement: {question}

Reason step by step, then finish with a single line of the form
Final answer: True
or
Final answer: False"""

ABDUCTIVE_PROMPT = """You are given a set of facts and rules about some entities, followed by an observation.
The observation does NOT follow from the facts and rules as given: exactly one fact is missing.
Find the single missing fact that, once added to the facts, makes the observation follow from the rules.

Facts and rules:
{context}

Observation: {question}

Reason step by step, then finish with a single line of the form
Missing fact: <one short sentence in the same style as the facts, e.g. "The cat is big.">"""


# --------------------------------------------------------------------------- data

@dataclass
class Example:
    id: str
    task: str  # "deductive" | "abductive"
    context: str
    question: str
    answer: str  # "True"/"False" for deductive, the missing fact for abductive
    meta: dict = field(default_factory=dict)


def _fetch_jsonl(url: str, cache_dir: Path) -> list[dict]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / re.sub(r"[^A-Za-z0-9_.-]", "_", url.split("://", 1)[1])
    if not path.exists():
        urllib.request.urlretrieve(url, path)
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_deductive(per_depth: int = 25, depths=(2, 3, 4, 5), seed: int = 42,
                   cache_dir: str | Path = "data") -> list[Example]:
    """Sample a label-balanced subset of PARARULE-Plus for each reasoning depth."""
    rng = random.Random(seed)
    out: list[Example] = []
    for d in depths:
        rows = _fetch_jsonl(PARARULE_URL.format(d=d), Path(cache_dir))
        for label in (0, 1):
            pool = [r for r in rows if r["label"] == label]
            for r in rng.sample(pool, per_depth // 2 + (label == 1) * (per_depth % 2)):
                out.append(Example(
                    id=r["id"], task="deductive", context=r["context"], question=r["question"],
                    answer="True" if r["label"] == 1 else "False",
                    meta={"depth": d, "negation": r["id"].startswith("NegationRule")},
                ))
    rng.shuffle(out)
    return out


def load_abductive(per_domain: int = 50, domains=("Animal", "Person"), seed: int = 42,
                   cache_dir: str | Path = "data") -> list[Example]:
    """Sample positive observations from AbductionRules (Simple = one valid explanation)."""
    rng = random.Random(seed)
    out: list[Example] = []
    for dom in domains:
        rows = _fetch_jsonl(ABDUCTION_URL.format(domain=dom), Path(cache_dir))
        # one positive observation (QCat "0") per context keeps the sample diverse
        cands = []
        for r in rows:
            qs = [q for q in r["questions"] if q["QCat"] == "0"]
            if qs:
                cands.append((r, rng.choice(qs)))
        for r, q in rng.sample(cands, per_domain):
            out.append(Example(
                id=q["id"], task="abductive", context=r["context"], question=q["text"],
                answer=q["label"], meta={"domain": dom},
            ))
    rng.shuffle(out)
    return out


# ---------------------------------------------------------------------- parsing

def strip_thinking(text: str) -> str:
    """Return the visible answer after the reasoning block.

    Some servers return the opening <think> tag and some put it in the prompt, so we
    keep whatever follows the last </think>. Without a closing tag (the model
    occasionally writes a malformed one such as "</roll") the whole text is kept and
    the parsers look for the last answer line; truncation is judged by finish_reason.
    """
    text = text or ""
    if "</think>" in text:
        return text.rsplit("</think>", 1)[1].strip()
    return text.strip()


def parse_deductive(text: str, allow_fallback: bool = True) -> str | None:
    body = strip_thinking(text)
    m = re.findall(r"final answer\s*[:：]?\s*\**\s*(?:\\boxed\{)?\s*(true|false)", body, re.I)
    if not m:
        m = re.findall(r"\\boxed\{\s*(?:\\text\{)?\s*(true|false)", body, re.I)
    if not m and allow_fallback:
        # last resort: last bare True/False in the visible answer
        m = re.findall(r"\b(true|false)\b", body, re.I)
    return m[-1].capitalize() if m else None


def parse_abductive(text: str) -> str | None:
    body = strip_thinking(text)
    m = re.findall(r"missing fact\s*[:：]\s*\**\s*(?:\\boxed\{)?(.+)", body, re.I)
    if not m:
        return None
    ans = m[-1].strip().strip("*`\"'}").strip()
    ans = re.sub(r"\\text\{([^}]*)\}", r"\1", ans)
    return ans or None


def normalize_fact(s: str | None) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ------------------------------------------------------------------------ eval

@dataclass
class Result:
    example: Example
    raw: str
    prediction: str | None
    correct: bool
    finish_reason: str | None
    completion_tokens: int | None
    error_type: str | None = None


def build_prompt(ex: Example) -> str:
    tmpl = DEDUCTIVE_PROMPT if ex.task == "deductive" else ABDUCTIVE_PROMPT
    return tmpl.format(context=ex.context, question=ex.question)


def classify_abductive_error(ex: Example, pred: str | None, finish_reason: str | None) -> str | None:
    gold, p = normalize_fact(ex.answer), normalize_fact(pred)
    if p == gold:
        return None
    if pred is None:
        return "truncated" if finish_reason == "length" else "no_answer"
    if re.match(r"(none|no missing|no additional|nothing)\b", p):
        return "denied_missing_fact"  # claims the observation already follows
    if p in {normalize_fact(s) for s in re.split(r"(?<=\.)\s+", ex.context)}:
        return "restated_known_fact"
    gold_subj = " ".join(gold.split()[:2])  # "the dog" / "charlie is"
    if not p.startswith(gold_subj.split()[0]) or gold_subj not in p:
        return "wrong_entity"
    return "wrong_attribute"


def score(ex: Example, raw: str, finish_reason: str | None, tokens: int | None) -> Result:
    if ex.task == "deductive":
        # a response cut off at max_tokens only counts if it already gave the final line
        pred = parse_deductive(raw, allow_fallback=finish_reason != "length")
        ok = pred == ex.answer
        err = None if ok else ("truncated" if pred is None and finish_reason == "length"
                               else "no_answer" if pred is None else
                               "false_positive" if pred == "True" else "false_negative")
    else:
        pred = parse_abductive(raw)
        ok = normalize_fact(pred) == normalize_fact(ex.answer)
        err = classify_abductive_error(ex, pred, finish_reason)
    return Result(ex, raw, pred, ok, finish_reason, tokens, err)


def run_eval(client, model: str, examples: list[Example], *, max_tokens: int = 8192,
             temperature: float = 0.0, top_p: float = 1.0, workers: int = 16,
             system_prompt: str | None = None) -> list[Result]:
    """Query the endpoint for every example (in parallel) and score the answers."""

    def one(ex: Example) -> Result:
        messages = ([{"role": "system", "content": system_prompt}] if system_prompt else [])
        messages.append({"role": "user", "content": build_prompt(ex)})
        try:
            resp = client.chat.completions.create(
                model=model, messages=messages, max_tokens=max_tokens,
                temperature=temperature, top_p=top_p,
            )
            choice = resp.choices[0]
            msg = choice.message
            # some servers return the chain of thought in a separate field
            reasoning = getattr(msg, "reasoning_content", None) or getattr(msg, "reasoning", None)
            text = msg.content or ""
            if reasoning and "<think>" not in text:
                text = f"<think>{reasoning}</think>{text}"
            tokens = resp.usage.completion_tokens if resp.usage else None
            return score(ex, text, choice.finish_reason, tokens)
        except Exception as e:  # keep going; record the failure
            return Result(ex, f"[request error] {e}", None, False, None, None, "request_error")

    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(one, examples))


# --------------------------------------------------------------------- reports

def summarize(results: list[Result]) -> dict:
    """Accuracy overall, per task and per slice, plus error-type counts."""
    groups: dict[str, list[bool]] = defaultdict(list)
    errors: dict[str, Counter] = defaultdict(Counter)
    for r in results:
        ex = r.example
        groups[ex.task].append(r.correct)
        if ex.task == "deductive":
            groups[f"deductive/depth={ex.meta['depth']}"].append(r.correct)
            groups[f"deductive/{'negation' if ex.meta['negation'] else 'no-negation'}"].append(r.correct)
        else:
            groups[f"abductive/{ex.meta['domain']}"].append(r.correct)
        if r.error_type:
            errors[ex.task][r.error_type] += 1
    acc = {k: {"n": len(v), "accuracy": round(sum(v) / len(v), 3)} for k, v in sorted(groups.items())}
    toks = [r.completion_tokens for r in results if r.completion_tokens]
    return {
        "accuracy": acc,
        "errors": {k: dict(v.most_common()) for k, v in errors.items()},
        "truncated": sum(r.finish_reason == "length" for r in results),
        "mean_completion_tokens": round(sum(toks) / len(toks)) if toks else None,
    }


def save_results(results: list[Result], path: str | Path) -> None:
    with Path(path).open("w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps({
                "id": r.example.id, "task": r.example.task, "meta": r.example.meta,
                "question": r.example.question, "gold": r.example.answer,
                "prediction": r.prediction, "correct": r.correct, "error_type": r.error_type,
                "finish_reason": r.finish_reason, "completion_tokens": r.completion_tokens,
                "response": r.raw,
            }, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    import argparse
    import os

    from openai import OpenAI

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", required=True)
    ap.add_argument("--base-url", default=os.getenv("OPENAI_BASE_URL", "http://localhost:8000/v1"))
    ap.add_argument("--api-key", default=os.getenv("OPENAI_API_KEY", "not-needed"))
    ap.add_argument("--per-depth", type=int, default=25)
    ap.add_argument("--per-domain", type=int, default=50)
    ap.add_argument("--max-tokens", type=int, default=8192)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--top-p", type=float, default=1.0)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--out", default="results.jsonl")
    a = ap.parse_args()

    client = OpenAI(base_url=a.base_url, api_key=a.api_key)
    exs = load_deductive(a.per_depth) + load_abductive(a.per_domain)
    res = run_eval(client, a.model, exs, max_tokens=a.max_tokens, temperature=a.temperature,
                   top_p=a.top_p, workers=a.workers)
    save_results(res, a.out)
    print(json.dumps(summarize(res), indent=2))
