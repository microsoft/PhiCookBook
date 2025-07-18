<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:02:54+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "pa"
}
-->
# Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਤੁਸੀਂ Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ:

1. ਇੱਕ LoRA ਐਡਾਪਟਰ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ ਤਾਂ ਜੋ ਵਾਕਾਂ ਨੂੰ Sad, Joy, Fear, Surprise ਵਿੱਚ ਵਰਗੀਕ੍ਰਿਤ ਕੀਤਾ ਜਾ ਸਕੇ।
1. ਐਡਾਪਟਰ ਦੇ ਵਜ਼ਨ ਬੇਸ ਮਾਡਲ ਵਿੱਚ ਮਿਲਾਓ।
1. ਮਾਡਲ ਨੂੰ `int4` ਵਿੱਚ Optimize ਅਤੇ Quantize ਕਰੋ।

ਅਸੀਂ ਤੁਹਾਨੂੰ ਦਿਖਾਵਾਂਗੇ ਕਿ ਕਿਵੇਂ ONNX Runtime (ORT) Generate API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਇੰਫਰੈਂਸ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

> **⚠️ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ, ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਯੋਗ GPU ਹੋਣਾ ਜਰੂਰੀ ਹੈ - ਉਦਾਹਰਨ ਵਜੋਂ, A10, V100, A100।**

## 💾 ਇੰਸਟਾਲ ਕਰੋ

ਨਵਾਂ Python ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ (ਉਦਾਹਰਨ ਵਜੋਂ, `conda` ਦੀ ਵਰਤੋਂ ਕਰਕੇ):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, Olive ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਰਕਫਲੋ ਲਈ ਲੋੜੀਂਦੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ
[Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ਵਿੱਚ ਇੱਕ *workflow* ਹੈ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ *passes* ਹਨ:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ਉੱਚ-ਸਤਰ 'ਤੇ, ਇਹ workflow ਇਹ ਕਰੇਗਾ:

1. Phi3 ਨੂੰ (150 ਕਦਮਾਂ ਲਈ, ਜਿਸਨੂੰ ਤੁਸੀਂ ਬਦਲ ਸਕਦੇ ਹੋ) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) ਡੇਟਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ।
1. LoRA ਐਡਾਪਟਰ ਦੇ ਵਜ਼ਨ ਬੇਸ ਮਾਡਲ ਵਿੱਚ ਮਿਲਾਓ। ਇਸ ਨਾਲ ਤੁਹਾਡੇ ਕੋਲ ONNX ਫਾਰਮੈਟ ਵਿੱਚ ਇੱਕ ਇਕੱਲਾ ਮਾਡਲ ਆਰਟੀਫੈਕਟ ਹੋਵੇਗਾ।
1. Model Builder ਮਾਡਲ ਨੂੰ ONNX ਰਨਟਾਈਮ ਲਈ Optimize ਕਰੇਗਾ ਅਤੇ ਮਾਡਲ ਨੂੰ `int4` ਵਿੱਚ Quantize ਕਰੇਗਾ।

ਵਰਕਫਲੋ ਚਲਾਉਣ ਲਈ, ਇਹ ਕਮਾਂਡ ਦਿਓ:

```bash
olive run --config phrase-classification.json
```

ਜਦੋਂ Olive ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ, ਤੁਹਾਡਾ Optimize ਕੀਤਾ ਹੋਇਆ `int4` ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ Phi3 ਮਾਡਲ ਇਸ ਥਾਂ ਉਪਲਬਧ ਹੋਵੇਗਾ: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`।

## 🧑‍💻 ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ Phi3 ਸ਼ਾਮਿਲ ਕਰੋ

ਐਪ ਚਲਾਉਣ ਲਈ:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ਇਸ ਦਾ ਜਵਾਬ ਵਾਕ ਦਾ ਇੱਕ ਸ਼ਬਦ ਵਰਗੀਕਰਨ ਹੋਵੇਗਾ (Sad/Joy/Fear/Surprise)।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।