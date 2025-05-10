<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:44:29+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "pa"
}
-->
# Olive ਨਾਲ Phi3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਤੁਸੀਂ Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ:

1. ਇੱਕ LoRA ਐਡਾਪਟਰ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ ਤਾਂ ਜੋ ਵਾਕਾਂ ਨੂੰ Sad, Joy, Fear, Surprise ਵਿੱਚ ਵਰਗੀਕ੍ਰਿਤ ਕੀਤਾ ਜਾ ਸਕੇ।
1. ਐਡਾਪਟਰ ਦੇ ਵਜ਼ਨ ਨੂੰ ਬੇਸ ਮਾਡਲ ਵਿੱਚ ਮਰਜ ਕਰੋ।
1. ਮਾਡਲ ਨੂੰ `int4` ਵਿੱਚ Optimize ਅਤੇ Quantize ਕਰੋ।

ਅਸੀਂ ਤੁਹਾਨੂੰ ਦਿਖਾਵਾਂਗੇ ਕਿ ONNX Runtime (ORT) Generate API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਕਿਵੇਂ ਇਨਫਰੰਸ ਕਰਨਾ ਹੈ।

> **⚠️ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ, ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਯੋਗ GPU ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ - ਉਦਾਹਰਨ ਵਜੋਂ, A10, V100, A100।**

## 💾 ਇੰਸਟਾਲ ਕਰੋ

ਨਵਾਂ Python ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਓ (ਉਦਾਹਰਨ ਵਜੋਂ, `conda` ਦੀ ਵਰਤੋਂ ਕਰਕੇ):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

ਅਗਲੇ ਕਦਮ ਵਿੱਚ, Olive ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਰਕਫਲੋ ਲਈ ਲੋੜੀਂਦੇ dependencies ਇੰਸਟਾਲ ਕਰੋ:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ਨਾਲ Phi3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ
[Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) ਵਿੱਚ ਇੱਕ *workflow* ਹੈ ਜਿਸ ਵਿੱਚ ਇਹ *passes* ਹਨ:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ਉੱਚ-ਸਤਰ 'ਤੇ, ਇਹ workflow ਇਹ ਕਰੇਗਾ:

1. Phi3 ਨੂੰ 150 ਸਟੈਪ ਲਈ (ਜਿਹੜੇ ਤੁਸੀਂ ਬਦਲ ਸਕਦੇ ਹੋ) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) ਡੇਟਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟਿਊਨ ਕਰੇਗਾ।
1. LoRA ਐਡਾਪਟਰ ਦੇ ਵਜ਼ਨ ਬੇਸ ਮਾਡਲ ਵਿੱਚ ਮਰਜ ਕਰੇਗਾ। ਇਸ ਨਾਲ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ONNX ਫਾਰਮੈਟ ਵਿੱਚ ਇਕੱਲਾ ਮਾਡਲ ਆਰਟੀਫੈਕਟ ਹੋਵੇਗਾ।
1. Model Builder ਮਾਡਲ ਨੂੰ ONNX ਰਨਟਾਈਮ ਲਈ Optimize ਅਤੇ ਮਾਡਲ ਨੂੰ `int4` ਵਿੱਚ Quantize ਕਰੇਗਾ।

Workflow ਚਲਾਉਣ ਲਈ, ਇਹ ਚਲਾਓ:

```bash
olive run --config phrase-classification.json
```

ਜਦੋਂ Olive ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ, ਤਾਂ ਤੁਹਾਡਾ Optimize ਕੀਤਾ ਹੋਇਆ `int4` ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ Phi3 ਮਾਡਲ ਇਥੇ ਮਿਲੇਗਾ: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ਆਪਣੇ ਐਪ ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ Phi3 ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ

ਐਪ ਚਲਾਉਣ ਲਈ:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ਇਸ ਦਾ ਜਵਾਬ ਇੱਕ ਸਿਰਫ਼ ਇੱਕ ਸ਼ਬਦ ਦਾ ਵਰਗੀਕਰਨ ਹੋਵੇਗਾ (Sad/Joy/Fear/Surprise)।

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।