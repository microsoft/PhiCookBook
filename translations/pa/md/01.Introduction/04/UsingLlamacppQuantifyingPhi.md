<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:08:16+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "pa"
}
-->
# **llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi ਪਰਿਵਾਰ ਦਾ Quantizing**

## **llama.cpp ਕੀ ਹੈ**

llama.cpp ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਸੌਫਟਵੇਅਰ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ ਮੁੱਖ ਤੌਰ 'ਤੇ C++ ਵਿੱਚ ਲਿਖੀ ਗਈ ਹੈ ਅਤੇ ਵੱਖ-ਵੱਖ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਜਿਵੇਂ ਕਿ Llama 'ਤੇ ਇਨਫਰੰਸ ਕਰਦੀ ਹੈ। ਇਸਦਾ ਮੁੱਖ ਮਕਸਦ ਘੱਟ ਤੋਂ ਘੱਟ ਸੈਟਅਪ ਨਾਲ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ 'ਤੇ LLM ਇਨਫਰੰਸ ਲਈ ਅਧੁਨਿਕ ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਨਾ ਹੈ। ਇਸਦੇ ਨਾਲ-ਨਾਲ, ਇਸ ਲਾਇਬ੍ਰੇਰੀ ਲਈ Python ਬਾਈਂਡਿੰਗਜ਼ ਵੀ ਉਪਲਬਧ ਹਨ, ਜੋ ਟੈਕਸਟ ਪੂਰਨਤਾ ਲਈ ਉੱਚ-ਸਤਰ ਦਾ API ਅਤੇ OpenAI ਅਨੁਕੂਲ ਵੈੱਬ ਸਰਵਰ ਦਿੰਦੇ ਹਨ।

llama.cpp ਦਾ ਮੁੱਖ ਮਕਸਦ ਘੱਟ ਤੋਂ ਘੱਟ ਸੈਟਅਪ ਅਤੇ ਅਧੁਨਿਕ ਪ੍ਰਦਰਸ਼ਨ ਨਾਲ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ 'ਤੇ LLM ਇਨਫਰੰਸ ਨੂੰ ਸਥਾਨਕ ਅਤੇ ਕਲਾਉਡ ਦੋਹਾਂ ਵਿੱਚ ਯੋਗ ਬਣਾਉਣਾ ਹੈ।

- ਕਿਸੇ ਵੀ ਡਿਪੈਂਡੈਂਸੀ ਤੋਂ ਬਿਨਾਂ ਸਾਫ਼ C/C++ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ  
- Apple silicon ਨੂੰ ਪਹਿਲ ਦਰਜੇ ਦਾ ਸਮਾਨ ਮਿਲਦਾ ਹੈ - ARM NEON, Accelerate ਅਤੇ Metal ਫਰੇਮਵਰਕਾਂ ਰਾਹੀਂ ਅਪਟੀਮਾਈਜ਼ਡ  
- x86 ਆਰਕੀਟੈਕਚਰਾਂ ਲਈ AVX, AVX2 ਅਤੇ AVX512 ਸਹਾਇਤਾ  
- ਤੇਜ਼ ਇਨਫਰੰਸ ਅਤੇ ਘੱਟ ਮੈਮੋਰੀ ਖਪਤ ਲਈ 1.5-ਬਿਟ, 2-ਬਿਟ, 3-ਬਿਟ, 4-ਬਿਟ, 5-ਬਿਟ, 6-ਬਿਟ ਅਤੇ 8-ਬਿਟ ਇੰਟੀਜਰ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ  
- NVIDIA GPUs 'ਤੇ LLM ਚਲਾਉਣ ਲਈ ਕਸਟਮ CUDA ਕਰਨਲ (AMD GPUs ਲਈ HIP ਸਹਾਇਤਾ)  
- Vulkan ਅਤੇ SYCL ਬੈਕਐਂਡ ਸਹਾਇਤਾ  
- ਕੁੱਲ VRAM ਸਮਰੱਥਾ ਤੋਂ ਵੱਡੇ ਮਾਡਲਾਂ ਲਈ CPU+GPU ਹਾਈਬ੍ਰਿਡ ਇਨਫਰੰਸ ਜੋ ਹਿੱਸੇਦਾਰ ਤੌਰ 'ਤੇ ਤੇਜ਼ੀ ਲਿਆਉਂਦਾ ਹੈ  

## **llama.cpp ਨਾਲ Phi-3.5 ਦਾ Quantizing**

Phi-3.5-Instruct ਮਾਡਲ ਨੂੰ llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਵਾਂਟਾਈਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਪਰ Phi-3.5-Vision ਅਤੇ Phi-3.5-MoE ਹਾਲੇ ਤੱਕ ਸਹਾਇਤਿਤ ਨਹੀਂ ਹਨ। llama.cpp ਦੁਆਰਾ ਬਦਲਿਆ ਗਿਆ ਫਾਰਮੈਟ gguf ਹੈ, ਜੋ ਸਭ ਤੋਂ ਵਿਆਪਕ ਤੌਰ 'ਤੇ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਫਾਰਮੈਟ ਵੀ ਹੈ।

Hugging face 'ਤੇ quantized GGUF ਫਾਰਮੈਟ ਦੇ ਬਹੁਤ ਸਾਰੇ ਮਾਡਲ ਮੌਜੂਦ ਹਨ। AI Foundry, Ollama, ਅਤੇ LlamaEdge llama.cpp 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ GGUF ਮਾਡਲ ਵੀ ਅਕਸਰ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

### **GGUF ਕੀ ਹੈ**

GGUF ਇੱਕ ਬਾਈਨਰੀ ਫਾਰਮੈਟ ਹੈ ਜੋ ਮਾਡਲਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਲੋਡ ਅਤੇ ਸੇਵ ਕਰਨ ਲਈ ਅਪਟੀਮਾਈਜ਼ਡ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਇਨਫਰੰਸ ਲਈ ਬਹੁਤ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਬਣ ਜਾਂਦਾ ਹੈ। GGUF GGML ਅਤੇ ਹੋਰ ਐਗਜ਼ਿਕਿਊਟਰਾਂ ਨਾਲ ਵਰਤੋਂ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। GGUF ਨੂੰ @ggerganov ਨੇ ਵਿਕਸਿਤ ਕੀਤਾ ਸੀ, ਜੋ llama.cpp ਦੇ ਵਿਕਾਸਕਾਰ ਵੀ ਹਨ, ਜੋ ਇੱਕ ਪ੍ਰਸਿੱਧ C/C++ LLM ਇਨਫਰੰਸ ਫਰੇਮਵਰਕ ਹੈ। PyTorch ਵਰਗੇ ਫਰੇਮਵਰਕਾਂ ਵਿੱਚ ਬਣਾਏ ਗਏ ਮਾਡਲਾਂ ਨੂੰ GGUF ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ ਤਾਂ ਜੋ ਉਹਨਾਂ ਇੰਜਨਾਂ ਨਾਲ ਵਰਤੇ ਜਾ ਸਕਣ।

### **ONNX ਅਤੇ GGUF ਵਿੱਚ ਫਰਕ**

ONNX ਇੱਕ ਪਰੰਪਰਾਗਤ ਮਸ਼ੀਨ ਲਰਨਿੰਗ/ਡੀਪ ਲਰਨਿੰਗ ਫਾਰਮੈਟ ਹੈ, ਜੋ ਵੱਖ-ਵੱਖ AI ਫਰੇਮਵਰਕਾਂ ਵਿੱਚ ਚੰਗੀ ਤਰ੍ਹਾਂ ਸਹਾਇਤਿਤ ਹੈ ਅਤੇ ਐਜ ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਇਸਦਾ ਵਧੀਆ ਉਪਯੋਗ ਹੈ। GGUF, ਜੋ llama.cpp 'ਤੇ ਆਧਾਰਿਤ ਹੈ, GenAI ਯੁੱਗ ਵਿੱਚ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਦੋਹਾਂ ਦੇ ਵਰਤੋਂ ਦੇ ਮਾਮਲੇ ਮਿਲਦੇ-ਜੁਲਦੇ ਹਨ। ਜੇ ਤੁਸੀਂ ਐਂਬੈਡਡ ਹਾਰਡਵੇਅਰ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਲੇਅਰਾਂ ਵਿੱਚ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ONNX ਤੁਹਾਡੀ ਚੋਣ ਹੋ ਸਕਦੀ ਹੈ। ਜੇ ਤੁਸੀਂ llama.cpp ਦੇ ਡੈਰੀਵੇਟਿਵ ਫਰੇਮਵਰਕ ਅਤੇ ਤਕਨਾਲੋਜੀ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ, ਤਾਂ GGUF ਬਿਹਤਰ ਹੋ ਸਕਦਾ ਹੈ।

### **llama.cpp ਨਾਲ Phi-3.5-Instruct ਦਾ Quantization**

**1. ਵਾਤਾਵਰਣ ਸੰਰਚਨਾ**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-Instruct ਨੂੰ FP16 GGUF ਵਿੱਚ ਬਦਲੋ


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 ਨੂੰ INT4 ਵਿੱਚ Quantize ਕਰਨਾ


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. ਟੈਸਟਿੰਗ**

llama-cpp-python ਇੰਸਟਾਲ ਕਰੋ


```bash

pip install llama-cpp-python -U

```

***Note*** 

ਜੇ ਤੁਸੀਂ Apple Silicon ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਇਸ ਤਰ੍ਹਾਂ llama-cpp-python ਇੰਸਟਾਲ ਕਰੋ


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

ਟੈਸਟਿੰਗ 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **ਸੰਸਾਧਨ**

1. llama.cpp ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. onnxruntime ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. GGUF ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।