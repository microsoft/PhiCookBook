# **Generative AI एक्सटेंਸ਼ਨਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ onnxruntime ਲਈ Phi ਫੈਮਿਲੀ ਦਾ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ**

## **onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ ਕੀ ਹਨ**

ਇਹ ਐਕਸਟੈਂਸ਼ਨਜ਼ ਤੁਹਾਨੂੰ ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) ਨਾਲ Generative AI ਚਲਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਇਹ ONNX ਮਾਡਲਾਂ ਲਈ generative AI ਲੂਪ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ, ਜਿਸ ਵਿੱਚ ONNX Runtime ਨਾਲ ਇਨਫਰੰਸ, ਲੋਗਿਟ ਪ੍ਰੋਸੈਸਿੰਗ, ਖੋਜ ਅਤੇ ਸੈਂਪਲਿੰਗ, ਅਤੇ KV ਕੈਸ਼ ਪ੍ਰਬੰਧਨ ਸ਼ਾਮਲ ਹੈ। ਡਿਵੈਲਪਰ ਇੱਕ ਹਾਈ-ਲੇਵਲ generate() ਮੈਥਡ ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਂ ਮਾਡਲ ਦੇ ਹਰ ਇਟਰੈਸ਼ਨ ਨੂੰ ਲੂਪ ਵਿੱਚ ਚਲਾ ਕੇ ਇਕ ਸਮੇਂ ਵਿੱਚ ਇੱਕ ਟੋਕਨ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹਨ, ਅਤੇ ਵਿਕਲਪਕ ਤੌਰ 'ਤੇ ਲੂਪ ਦੇ ਅੰਦਰ ਜਨਰੇਸ਼ਨ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਅੱਪਡੇਟ ਵੀ ਕਰ ਸਕਦੇ ਹਨ। ਇਹ greedy/beam ਖੋਜ ਅਤੇ TopP, TopK ਸੈਂਪਲਿੰਗ ਲਈ ਸਹਾਇਕਤਾ ਰੱਖਦਾ ਹੈ ਟੋਕਨ ਸੀਕਵੈਂਸ ਪ੍ਰਸਾਰਿਤ ਕਰਨ ਲਈ ਅਤੇ ਦੁਹਰਾਅ ਸਜ਼ਾਵਾਂ ਵਰਗੇ ਬਿਲਟ-ਇਨ ਲੋਗਿਟ ਪ੍ਰੋਸੈਸਿੰਗ ਵੀ ਰੱਖਦਾ ਹੈ। ਤੁਸੀਂ ਅਸਾਨੀ ਨਾਲ ਕਸਟਮ ਸਕੋਰਿੰਗ ਵੀ ਜੋੜ ਸਕਦੇ ਹੋ।

ਐਪਲੀਕੇਸ਼ਨ ਲੈਵਲ 'ਤੇ, ਤੁਸੀਂ C++/ C# / Python ਦੀ ਵਰਤੋਂ ਕਰਕੇ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ ਵਰਤ ਕੇ ਐਪ ਬਣਾਉ ਸਕਦੇ ਹੋ। ਮਾਡਲ ਲੈਵਲ 'ਤੇ, ਤੁਸੀਂ ਇਸਦੀ ਵਰਤੋਂ ਫਾਈਨ-ਟੂਨਡ ਮਾਡਲਾਂ ਨੂੰ ਮਰਜ ਕਰਕੇ ਸੰਬੰਧਿਤ ਕੁਆਂਟਿਟੇਟਿਵ ਡਿਪਲੋਯਮੈਂਟ ਕੰਮ ਕਰਨ ਲਈ ਕਰ ਸਕਦੇ ਹੋ।


## **Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ ਨਾਲ Phi-3.5 ਦੀ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ**

### **ਸਹਾਇਕ ਮਾਡਲ**

onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ Microsoft Phi, Google Gemma, Mistral ਅਤੇ Meta LLaMA ਦੀ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ।


### **onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ ਵਿੱਚ ਮਾਡਲ ਬਿਲਡਰ**

ਮਾਡਲ ਬਿਲਡਰ ਅਨੁਕੂਲਿਤ ਅਤੇ ਕੁਆਂਟਾਈਜ਼ਡ ONNX ਮਾਡਲ ਬਣਾਉਣ ਦੇ ਕੰਮ ਨੂੰ ਬਹੁਤ ਤੇਜ਼ ਕਰਦਾ ਹੈ ਜੋ ONNX Runtime generate() API ਨਾਲ ਚਲਦੇ ਹਨ।

ਮਾਡਲ ਬਿਲਡਰ ਰਾਹੀਂ, ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ INT4, INT8, FP16, FP32 ਵਿੱਚ ਕੁਆਂਟਾਈਜ਼ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ CPU, CUDA, DirectML, Mobile ਆਦਿ ਵਰਗੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਤੇਜ਼ੀ ਦੇ ਤਰੀਕਿਆਂ ਨੂੰ ਮਿਲਾ ਸਕਦੇ ਹੋ।

ਮਾਡਲ ਬਿਲਡਰ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਤੁਹਾਨੂੰ ਇੰਸਟਾਲ ਕਰਨਾ ਪਵੇਗਾ

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ਇੰਸਟਾਲੇਸ਼ਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਮਾਡਲ ਬਿਲਡਰ ਸਕ੍ਰਿਪਟ ਨੂੰ ਟਰਮੀਨਲ ਤੋਂ ਚਲਾ ਕੇ ਮਾਡਲ ਫਾਰਮੈਟ ਅਤੇ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਕਨਵਰਜ਼ਨ ਕਰ ਸਕਦੇ ਹੋ।


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

ਸੰਬੰਧਿਤ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸਮਝੋ

1. **model_name** ਇਹ Hugging face 'ਤੇ ਮੌਜੂਦ ਮਾਡਲ ਹੈ, ਜਿਵੇਂ microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct ਆਦਿ। ਇਹ ਮਾਡਲ ਸਟੋਰ ਕਰਨ ਵਾਲੀ ਰਾਹ ਵੀ ਹੋ ਸਕਦੀ ਹੈ

2. **path_to_output_folder** ਕੁਆਂਟਾਈਜ਼ਡ ਕਨਵਰਜ਼ਨ ਸੇਵ ਕਰਣ ਵਾਲੀ ਰਾਹ

3. **execution_provider** ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਤੇਜ਼ੀ ਸਹਾਇਕਤਾ, ਜਿਵੇਂ cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** ਅਸੀਂ Hugging face ਤੋਂ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਕੈਸ਼ ਕਰਦੇ ਹਾਂ




***ਨੋਟ：*** <ul>ਜਦੋਂ ਕਿ onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ ਪ੍ਰੀਵਿਊ ਵਿੱਚ ਹਨ, ਉਹ Microsoft Olive ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤੇ ਗਏ ਹਨ, ਅਤੇ ਤੁਸੀਂ Microsoft Olive ਰਾਹੀਂ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ Model Builder ਫੰਕਸ਼ਨਜ਼ ਨੂੰ ਵੀ ਕਾਲ ਕਰ ਸਕਦੇ ਹੋ।</ul>

## **ਮਾਡਲ ਬਿਲਡਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 ਦੀ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਕਿਵੇਂ ਕਰੀਏ**

ਮਾਡਲ ਬਿਲਡਰ ਹੁਣ Phi-3.5 Instruct ਅਤੇ Phi-3.5-Vision ਲਈ ONNX ਮਾਡਲ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਸਮਰਥਨ ਦਿੰਦਾ ਹੈ

### **Phi-3.5-Instruct**


**ਕੁਆਂਟਾਈਜ਼ਡ INT 4 ਦਾ CPU ਤੇਜ਼ੀ ਵਾਲਾ ਕਨਵਰਜ਼ਨ**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**ਕੁਆਂਟਾਈਜ਼ਡ INT 4 ਦਾ CUDA ਤੇਜ਼ੀ ਵਾਲਾ ਕਨਵਰਜ਼ਨ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ਟਰਮੀਨਲ ਵਿੱਚ ਮਾਹੌਲ ਸੈੱਟ ਕਰੋ

```bash

mkdir models

cd models 

```

2. ਮਾਡਲ ਫੋਲਡਰ ਵਿੱਚ microsoft/Phi-3.5-vision-instruct ਡਾਊਨਲੋਡ ਕਰੋ
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਫਾਇਲਾਂ ਆਪਣੇ Phi-3.5-vision-instruct ਫੋਲਡਰ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕਰੋ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ਮਾਡਲ ਫੋਲਡਰ ਵਿੱਚ ਇਹ ਫਾਇਲ ਡਾਊਨਲੋਡ ਕਰੋ
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ਟਰਮੀਨਲ 'ਤੇ ਜਾਓ

ONNX ਲਈ FP32 ਸਮਰਥਿਤ ਕਨਵਰਜ਼ਨ ਕਰੋ


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **ਨੋਟ：**

1. ਮਾਡਲ ਬਿਲਡਰ ਇਸ ਵੇਲੇ Phi-3.5-Instruct ਅਤੇ Phi-3.5-Vision ਦੇ ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਮਰਥਨ ਦਿੰਦਾ ਹੈ, ਪਰ Phi-3.5-MoE ਨੂੰ ਨਹੀਂ

2. ਤੁਸੀਂ ONNX ਦੇ ਕੁਆਂਟਾਈਜ਼ਡ ਮਾਡਲ ਨੂੰ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ for onnxruntime SDK ਰਾਹੀਂ ਵਰਤ ਸਕਦੇ ਹੋ

3. ਸਾਨੂੰ ਜ਼ਿੰਮੇਵਾਰ AI ਬਾਰੇ ਵਧੇਰੇ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸ ਕਰਕੇ ਮਾਡਲ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਤੋਂ ਬਾਅਦ ਵਧੇਰੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਨਤੀਜੇ ਦੀ ਜਾਂਚ ਕਰਨ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ

4. CPU INT4 ਮਾਡਲ ਦੀ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਦੇ ਨਾਲ, ਅਸੀਂ ਇਸਨੂੰ Edge ਡਿਵਾਈਸ 'ਤੇ ਡਿਪਲੌਇ ਕਰ ਸਕਦੇ ਹਾਂ, ਜਿਸਦੇ ਬਿਹਤਰ ਐਪਲੀਕੇਸ਼ਨ ਸਨੀਹ ਹਨ, ਇਸ ਲਈ ਅਸੀਂ Phi-3.5-Instruct ਨੂੰ INT 4 ਦੇ ਆਸ-ਪਾਸ ਮੁਕੰਮਲ ਕੀਤਾ ਹੈ


## **ਸੰਸਾਧਨ**

1. onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨਜ਼ GitHub ਰਿਪੋ [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->