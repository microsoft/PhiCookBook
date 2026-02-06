## **ਮਾਡਲ ਬਿਲਡਰ ਨਾਲ Phi-3.5 ਨੂੰ ਕਿਵੇਂ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ ਹੈ**

ਮਾਡਲ ਬਿਲਡਰ ਹੁਣ Phi-3.5 Instruct ਅਤੇ Phi-3.5-Vision ਲਈ ONNX ਮਾਡਲ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ।

### **Phi-3.5-Instruct**

**ਕਵਾਂਟਾਈਜ਼ਡ INT4 ਦੀ CPU ਤੇ ਤੇਜ਼ ਕੀਤੀ ਗਈ ਕਨਵਰਜ਼ਨ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**ਕਵਾਂਟਾਈਜ਼ਡ INT4 ਦੀ CUDA ਤੇ ਤੇਜ਼ ਕੀਤੀ ਗਈ ਕਨਵਰਜ਼ਨ**

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

2. models ਫੋਲਡਰ ਵਿੱਚ microsoft/Phi-3.5-vision-instruct ਡਾਊਨਲੋਡ ਕਰੋ  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਫਾਈਲਾਂ ਆਪਣੇ Phi-3.5-vision-instruct ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ਇਹ ਫਾਈਲ models ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ਟਰਮੀਨਲ 'ਤੇ ਜਾਓ

    FP32 ਨਾਲ ONNX ਸਹਿਯੋਗੀ ਕਨਵਰਜ਼ਨ ਕਰੋ

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ਨੋਟ：**

1. ਮਾਡਲ ਬਿਲਡਰ ਇਸ ਸਮੇਂ Phi-3.5-Instruct ਅਤੇ Phi-3.5-Vision ਦੀ ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ, ਪਰ Phi-3.5-MoE ਲਈ ਨਹੀਂ।

2. ONNX ਦੇ ਕਵਾਂਟਾਈਜ਼ਡ ਮਾਡਲ ਨੂੰ ਵਰਤਣ ਲਈ, ਤੁਸੀਂ ਇਸਨੂੰ Generative AI extensions for onnxruntime SDK ਰਾਹੀਂ ਵਰਤ ਸਕਦੇ ਹੋ।

3. ਸਾਨੂੰ ਜ਼ਿਆਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਬਾਰੇ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸ ਲਈ ਮਾਡਲ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਕਨਵਰਜ਼ਨ ਤੋਂ ਬਾਅਦ, ਵਧੇਰੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਨਤੀਜੇ ਦੀ ਜਾਂਚ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

4. CPU INT4 ਮਾਡਲ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਕੇ, ਅਸੀਂ ਇਸਨੂੰ Edge Device 'ਤੇ ਡਿਪਲੋਇ ਕਰ ਸਕਦੇ ਹਾਂ, ਜਿਸ ਨਾਲ ਬਿਹਤਰ ਐਪਲੀਕੇਸ਼ਨ ਸਥਿਤੀਆਂ ਬਣਦੀਆਂ ਹਨ, ਇਸ ਲਈ ਅਸੀਂ Phi-3.5-Instruct ਨੂੰ INT4 ਦੇ ਆਲੇ-ਦੁਆਲੇ ਪੂਰਾ ਕਰ ਲਿਆ ਹੈ।

## **ਸੰਸਾਧਨ**

1. Generative AI extensions for onnxruntime ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime ਦਾ GitHub ਰਿਪੋ [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।