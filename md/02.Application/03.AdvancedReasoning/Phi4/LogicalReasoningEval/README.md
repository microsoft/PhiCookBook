# Evaluating deductive and abductive reasoning with Phi-4-mini-reasoning

This sample measures how well Phi-4-mini-reasoning handles **logical** reasoning, as opposed to math, and shows how to find out *where* it fails. It uses two small, open benchmarks built from synthetic facts and rules:

| Task | Question | Dataset |
|---|---|---|
| **Deductive** | Given facts and rules, is a statement True or False? | [PARARULE-Plus](https://huggingface.co/datasets/qbao775/PARARULE-Plus), depth 2-5 (MIT) |
| **Abductive** | Given facts, rules and an observation that does not follow, which single missing fact explains it? | [AbductionRules](https://github.com/Strong-AI-Lab/AbductionRules), *Simple* split (MIT) |

The evaluation code talks to any **OpenAI-compatible endpoint**, so it runs unchanged against [Foundry Local](https://github.com/microsoft/Foundry-Local), Ollama, vLLM, GitHub Models or a Microsoft Foundry deployment.

## Files

| File | What it does |
|---|---|
| [phi4_logical_reasoning_eval.ipynb](./phi4_logical_reasoning_eval.ipynb) | 📓 Step-by-step walkthrough: pick an endpoint, load data, run, read the accuracy breakdown and errors (80 items, a few minutes on one GPU) |
| [reasoning_eval.py](./reasoning_eval.py) | Data loading, prompts, answer parsing, scoring and error classification. Also a command-line tool for larger runs |
| [requirements.txt](./requirements.txt) | `openai`, `pandas` |

## Quick start

```bash
pip install -r requirements.txt

# 1. Start an OpenAI-compatible server, for example with vLLM
vllm serve microsoft/Phi-4-mini-reasoning --max-model-len 16384 --served-model-name phi-4-mini-reasoning

# 2. Run the full evaluation (200 deductive + 200 abductive items)
python reasoning_eval.py --model phi-4-mini-reasoning --base-url http://localhost:8000/v1 \
    --temperature 0.8 --top-p 0.95 --max-tokens 12288 --out results.jsonl
```

For Foundry Local or Ollama, see the first cell of the notebook. Test files are downloaded once from the sources above and cached in `./data`. Samples are drawn with a fixed seed, so every model sees the same items.

## Results

Full run: 200 deductive items (50 per depth, balanced True/False) and 200 abductive items (100 Animal, 100 Person), served with vLLM on one A100.

* **Phi-4-mini-reasoning**: sampling settings from the model card (temperature 0.8, top-p 0.95), `max_tokens` 12288, mean ± std over 3 runs.
* **Phi-4-mini-instruct**: same prompts, greedy decoding, `max_tokens` 4096, 1 run, included as a non-reasoning baseline.

| Slice | n | Phi-4-mini-reasoning | Phi-4-mini-instruct |
|---|---:|---:|---:|
| **Abductive (all)** | 200 | **88.2 ± 3.3** | 64.0 |
| Abductive / Animal | 100 | 87.3 ± 7.2 | 66.0 |
| Abductive / Person | 100 | 89.0 ± 1.7 | 62.0 |
| **Deductive (all)** | 200 | 74.0 ± 2.8 | **78.5** |
| Deductive / depth 2 | 50 | 82.0 ± 2.0 | 80.0 |
| Deductive / depth 3 | 50 | 78.0 ± 6.0 | 74.0 |
| Deductive / depth 4 | 50 | 66.0 ± 4.0 | 84.0 |
| Deductive / depth 5 | 50 | 70.0 ± 4.0 | 76.0 |
| Deductive / rules **with negation** | 93 | **56.3 ± 3.8** | 64.5 |
| Deductive / rules without negation | 107 | 89.4 ± 1.9 | 90.7 |

These are small samples (n = 50 per depth), so treat differences of a few points as noise.

### What the numbers show

1. **Abduction is where the reasoning model clearly helps** (+24 points). The instruct model's main failure is not a wrong guess. In 52 of 200 cases it answers `None`, insisting the observation already follows and refusing the premise of the task. Phi-4-mini-reasoning almost never does this.
2. **Negation is the weak spot for deduction.** Without negation, both models are near 90%. With rules like `If someone is not big then they are poor`, which must be read under the closed-world assumption (*not derivable* means *false*), Phi-4-mini-reasoning falls to 56%, close to chance. The traces show it mixing closed- and open-world reading ("the cat might be not powerful") within one chain.
3. **More thinking is a warning sign.** Across the three runs, the median completion length of *wrong* answers is 2.6× that of correct ones on deductive items (3,912 vs 1,516 tokens) and 4.2× on abductive items (7,076 vs 1,667). A token budget is a cheap confidence signal: long traces are worth a second look or a retry.
4. **Truncation is rare at 12k tokens** (4-8 of 400 per run). With a smaller `max_tokens` budget, it becomes a real source of errors, so check `finish_reason` before blaming the model. A response cut off at `max_tokens` only counts if it had already written its final answer line.
5. **Parse defensively.** In 2-5% of responses, Phi-4-mini-reasoning closes its reasoning with a malformed tag (for example `</roll`) and then gives a normal `Final answer:` line. The parsers read the last answer line instead of relying on a well-formed `</think>`, and they work whether or not the server returns the opening `<think>` tag.

## Error types

`reasoning_eval.py` labels every wrong answer, so you can count failure modes rather than read 400 traces:

| Task | Error type | Meaning |
|---|---|---|
| deductive | `false_positive` / `false_negative` | answered True for a False statement / False for a True one |
| abductive | `wrong_attribute` | right entity, wrong property |
| abductive | `wrong_entity` | a fact about a different entity |
| abductive | `restated_known_fact` | "explained" the observation with a fact already in the context |
| abductive | `denied_missing_fact` | answered "None", claiming the observation already follows |
| both | `truncated` / `no_answer` | stopped at `max_tokens`, or no parsable final line |

## Adapting the sample

* **Another model**: change `MODEL` (or `--model`). Phi-4-reasoning, Phi-4-reasoning-plus and fine-tuned checkpoints work as long as they are served behind an OpenAI-compatible API.
* **Your own data**: write a loader that returns `Example` objects (`context`, `question`, `answer`). The prompts, parsers and reports stay the same.
* **Bigger runs**: raise `per_depth` / `per_domain`. Each PARARULE-Plus depth has about 2,700 test items and each AbductionRules domain about 600 contexts.

## Limitations

* Synthetic rule-based data checks rule following, not world knowledge. Do not read the scores as general reasoning ability.
* Abductive scoring is exact match after normalisation. The *Simple* split has a single valid explanation per observation, which keeps this fair, but the confounded splits would need a checker that verifies whether a predicted fact actually entails the observation.
* Results above come from one prompt template. Prompt wording affects both models, especially how the closed-world assumption is explained.

## References

* Qiming Bao, Alex Yuxuan Peng, Tim Hartill, Neset Tan, Zhenyun Deng, Michael Witbrock and Jiamou Liu. 2022. *Multi-Step Deductive Reasoning Over Natural Language: An Empirical Study on Out-of-Distribution Generalisation.* IJCLR-NeSy 2022. (PARARULE-Plus)
* Nathan Young, Qiming Bao, Joshua Bensemann and Michael Witbrock. 2022. *AbductionRules: Training Transformers to Explain Unexpected Inputs.* Findings of ACL 2022.
* [Phi-4-mini-reasoning model card](https://huggingface.co/microsoft/Phi-4-mini-reasoning) and [technical report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
