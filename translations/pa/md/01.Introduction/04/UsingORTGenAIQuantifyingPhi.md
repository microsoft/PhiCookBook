<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:24:49+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "pa"
}
-->
## **Model Builder ਨਾਲ Phi-3.5 ਨੂੰ Quantize ਕਰਨ ਦਾ ਤਰੀਕਾ**

ਹੁਣ Model Builder Phi-3.5 Instruct ਅਤੇ Phi-3.5-Vision ਲਈ ONNX ਮਾਡਲ ਦੀ quantization ਨੂੰ ਸਮਰਥਨ ਦਿੰਦਾ ਹੈ।

### **Phi-3.5-Instruct**

**CPU ਤੇ ਤੇਜ਼ ਕੀਤਾ ਗਿਆ quantized INT 4 ਦਾ ਕਨਵਰਜ਼ਨ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ਤੇ ਤੇਜ਼ ਕੀਤਾ ਗਿਆ quantized INT 4 ਦਾ ਕਨਵਰਜ਼ਨ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ਟਰਮੀਨਲ ਵਿੱਚ ਵਾਤਾਵਰਣ ਸੈੱਟ ਕਰੋ

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct ਨੂੰ models ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਫਾਈਲਾਂ ਆਪਣੇ Phi-3.5-vision-instruct ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ਇਹ ਫਾਈਲ models ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ਟਰਮੀਨਲ ਵਿੱਚ ਜਾਓ

    FP32 ਨਾਲ ONNX ਸਹਾਇਤਾ ਵਾਲਾ ਕਨਵਰਜ਼ਨ ਕਰੋ

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ਨੋਟ:**

1. Model Builder ਇਸ ਵੇਲੇ Phi-3.5-Instruct ਅਤੇ Phi-3.5-Vision ਦੇ ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਮਰਥਨ ਦਿੰਦਾ ਹੈ, ਪਰ Phi-3.5-MoE ਲਈ ਨਹੀਂ।

2. ONNX ਦੇ quantized ਮਾਡਲ ਨੂੰ ਵਰਤਣ ਲਈ, ਤੁਸੀਂ ਇਸਨੂੰ Generative AI extensions for onnxruntime SDK ਰਾਹੀਂ ਵਰਤ ਸਕਦੇ ਹੋ।

3. ਸਾਨੂੰ ਜ਼ਿਆਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਬਾਰੇ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸ ਲਈ ਮਾਡਲ ਦੀ quantization ਕਨਵਰਜ਼ਨ ਤੋਂ ਬਾਅਦ, ਵਧੀਆ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਟੈਸਟਿੰਗ ਕਰਨਾ ਸੁਝਾਇਆ ਜਾਂਦਾ ਹੈ।

4. CPU INT4 ਮਾਡਲ ਨੂੰ quantize ਕਰਕੇ, ਅਸੀਂ ਇਸਨੂੰ Edge ਡਿਵਾਈਸ ਤੇ ਤਾਇਨਾਤ ਕਰ ਸਕਦੇ ਹਾਂ, ਜਿਸ ਨਾਲ ਬਿਹਤਰ ਐਪਲੀਕੇਸ਼ਨ ਸਿਨਾਰੀਓ ਬਣਦੇ ਹਨ, ਇਸ ਲਈ ਅਸੀਂ Phi-3.5-Instruct ਨੂੰ INT 4 ਦੇ ਆਲੇ-ਦੁਆਲੇ ਪੂਰਾ ਕਰ ਲਿਆ ਹੈ।

## **ਸੰਸਾਧਨ**

1. Generative AI extensions for onnxruntime ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub ਰਿਪੋ [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**ਅਸਵੀਕਾਰੋਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।