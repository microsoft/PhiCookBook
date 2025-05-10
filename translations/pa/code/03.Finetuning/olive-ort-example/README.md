<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:31:27+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "pa"
}
-->
# Olive ਨਾਲ Phi3 ਨੂੰ Fine-tune ਕਰੋ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਤੁਸੀਂ Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ:

1. ਇੱਕ LoRA adapter ਨੂੰ fine-tune ਕਰੋ ਜੋ phrases ਨੂੰ Sad, Joy, Fear, Surprise ਵਿੱਚ classify ਕਰੇ।
1. adapter ਦੇ weights ਨੂੰ base model ਵਿੱਚ merge ਕਰੋ।
1. ਮਾਡਲ ਨੂੰ optimize ਅਤੇ quantize ਕਰੋ `int4` ਵਿੱਚ।

ਅਸੀਂ ਤੁਹਾਨੂੰ ONNX Runtime (ORT) Generate API ਦੀ ਵਰਤੋਂ ਕਰਕੇ fine-tuned ਮਾਡਲ ਨੂੰ inference ਕਰਨ ਦਾ ਤਰੀਕਾ ਵੀ ਦਿਖਾਵਾਂਗੇ।

> **⚠️ Fine-tuning ਲਈ, ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ suitable GPU ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ - ਉਦਾਹਰਨ ਵਜੋਂ, A10, V100, A100।**

## 💾 Install

ਨਵਾਂ Python virtual environment ਬਣਾਓ (ਉਦਾਹਰਨ ਵਜੋਂ, `conda` ਦੀ ਵਰਤੋਂ ਕਰਕੇ):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

ਫਿਰ, Olive ਅਤੇ fine-tuning workflow ਲਈ dependencies install ਕਰੋ:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ਨਾਲ Phi3 ਨੂੰ Fine-tune ਕਰੋ
[Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ਵਿੱਚ ਇੱਕ *workflow* ਹੈ ਜਿਸ ਵਿੱਚ ਇਹ *passes* ਹਨ:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ਉੱਚ ਸਤਰ 'ਤੇ, ਇਹ workflow ਇਹ ਕਰੇਗਾ:

1. Phi3 ਨੂੰ fine-tune ਕਰੇਗਾ (150 steps ਲਈ, ਜਿਸਨੂੰ ਤੁਸੀਂ ਬਦਲ ਸਕਦੇ ਹੋ) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) ਡੇਟਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ।
1. LoRA adapter ਦੇ weights ਨੂੰ base model ਵਿੱਚ merge ਕਰੇਗਾ। ਇਸ ਨਾਲ ਤੁਹਾਡੇ ਕੋਲ ONNX ਫਾਰਮੈਟ ਵਿੱਚ ਇੱਕ single ਮਾਡਲ artifact ਹੋਵੇਗਾ।
1. Model Builder ਮਾਡਲ ਨੂੰ ONNX runtime ਲਈ optimize ਅਤੇ `int4` ਵਿੱਚ quantize ਕਰੇਗਾ।

Workflow ਚਲਾਉਣ ਲਈ, ਇਹ ਚਲਾਓ:

```bash
olive run --config phrase-classification.json
```

ਜਦੋਂ Olive ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ, ਤਾਂ ਤੁਹਾਡਾ optimized `int4` fine-tuned Phi3 ਮਾਡਲ ਇਸ ਥਾਂ ਉਪਲਬਧ ਹੋਵੇਗਾ: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Fine-tuned Phi3 ਨੂੰ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ

ਐਪ ਚਲਾਉਣ ਲਈ:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ਇਸ ਦਾ ਜਵਾਬ phrase ਦੀ single word classification ਹੋਵੇਗੀ (Sad/Joy/Fear/Surprise)।

**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਉੱਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।