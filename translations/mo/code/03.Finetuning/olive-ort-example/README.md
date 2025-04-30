<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T11:25:40+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "mo"
}
-->
# Fine-tune Phi3 ye Olive laa kɔrɛ

Esi yɛ example la, wo yɛ Olive la kpɔkɛ:

1. Fine-tune LoRA adapter la kɛ phrases ye kpɔ Sad, Joy, Fear, Surprise.
1. Merge adapter weights kɔ base model me.
1. Optimize kɛ Quantize model la wɔ `int4`.

Dɔ ko wo yɛ nɔ sɛɛ fine-tuned model la inference wɔ ONNX Runtime (ORT) Generate API kpɔ.

> **⚠️ Fine-tuning wɔ yɛ, wo yɛ GPU la kɛ wɔ yɛ - nɔ yɛ A10, V100, A100.**

## 💾 Install

Yɛ Python virtual environment fofo (nɔ yɛ `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Esi yɛ Olive kɛ dependencies wɔ fine-tuning workflow yɛ:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 ye Olive
[Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) la yɛ *workflow* wɔ *passes* nɔ kpɔ:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Yɛ high-level la, workflow la yɛ:

1. Fine-tune Phi3 (150 steps la, wo yɛ modify) wɔ [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) data la kpɔ.
1. Merge LoRA adapter weights kɔ base model me. Nɔ yɛ single model artifact wɔ ONNX format.
1. Model Builder yɛ model la optimize wɔ ONNX runtime *kɛ* quantize model la wɔ `int4`.

Wɔ yɛ workflow la execute, yɛ:

```bash
olive run --config phrase-classification.json
```

Esi Olive yɛ complete, optimized `int4` fine-tuned Phi3 model la wɔ: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrate fine-tuned Phi3 wɔ wo application me 

Wɔ app la run:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Response la yɛ single word classification wɔ phrase (Sad/Joy/Fear/Surprise).

It seems like "mo" might refer to a language or abbreviation, but it's not clear which specific language or context you're referring to. Could you clarify what "mo" means? For example, are you asking for a translation into Maori, Mongolian, or another language?