<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:07:06+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "pa"
}
-->
# **llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi ਪਰਿਵਾਰ ਦਾ ਕੁਆਂਟਾਈਜ਼ਿੰਗ**

## **llama.cpp ਕੀ ਹੈ**

llama.cpp ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਸਾਫਟਵੇਅਰ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ ਮੁੱਖ ਤੌਰ 'ਤੇ C++ ਵਿੱਚ ਲਿਖੀ ਗਈ ਹੈ ਅਤੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs) ਜਿਵੇਂ ਕਿ Llama 'ਤੇ ਇਨਫਰੈਂਸ ਕਰਦੀ ਹੈ। ਇਸ ਦਾ ਮੁੱਖ ਮਕਸਦ ਘੱਟ ਤੋਂ ਘੱਟ ਸੈਟਅਪ ਨਾਲ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ 'ਤੇ LLM ਇਨਫਰੈਂਸ ਲਈ ਅਧੁਨਿਕ ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਨਾ ਹੈ। ਇਸ ਲਾਇਬ੍ਰੇਰੀ ਲਈ Python ਬਾਈਂਡਿੰਗ ਵੀ ਉਪਲਬਧ ਹੈ, ਜੋ ਟੈਕਸਟ ਕੰਪਲੀਸ਼ਨ ਲਈ ਉੱਚ-ਸਤਰ ਦਾ API ਅਤੇ OpenAI ਅਨੁਕੂਲ ਵੈੱਬ ਸਰਵਰ ਦਿੰਦੀ ਹੈ।

llama.cpp ਦਾ ਮੁੱਖ ਮਕਸਦ ਘੱਟ ਸੈਟਅਪ ਅਤੇ ਵਿਆਪਕ ਹਾਰਡਵੇਅਰ 'ਤੇ ਅਧੁਨਿਕ ਪ੍ਰਦਰਸ਼ਨ ਨਾਲ LLM ਇਨਫਰੈਂਸ ਨੂੰ ਯੋਗ ਬਣਾਉਣਾ ਹੈ - ਸਥਾਨਕ ਅਤੇ ਕਲਾਉਡ ਦੋਹਾਂ ਵਿੱਚ।

- ਕਿਸੇ ਵੀ ਡੀਪੈਂਡੈਂਸੀ ਤੋਂ ਬਿਨਾਂ ਸਧਾਰਣ C/C++ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ  
- Apple silicon ਨੂੰ ਪਹਿਲ ਦਰਜੇ ਦਾ ਸਮਝਿਆ ਗਿਆ ਹੈ - ARM NEON, Accelerate ਅਤੇ Metal ਫਰੇਮਵਰਕਾਂ ਰਾਹੀਂ ਅਪਟਿਮਾਈਜ਼ਡ  
- x86 ਆਰਕੀਟੈਕਚਰ ਲਈ AVX, AVX2 ਅਤੇ AVX512 ਸਹਾਇਤਾ  
- ਤੇਜ਼ ਇਨਫਰੈਂਸ ਅਤੇ ਘੱਟ ਮੈਮੋਰੀ ਖਪਤ ਲਈ 1.5-ਬਿਟ, 2-ਬਿਟ, 3-ਬਿਟ, 4-ਬਿਟ, 5-ਬਿਟ, 6-ਬਿਟ ਅਤੇ 8-ਬਿਟ ਇੰਟੀਜਰ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ  
- NVIDIA GPUs 'ਤੇ LLM ਚਲਾਉਣ ਲਈ ਕਸਟਮ CUDA ਕਰਨਲ (AMD GPUs ਲਈ HIP ਸਹਾਇਤਾ)  
- Vulkan ਅਤੇ SYCL ਬੈਕਐਂਡ ਸਹਾਇਤਾ  
- ਕੁੱਲ VRAM ਸਮਰੱਥਾ ਤੋਂ ਵੱਡੇ ਮਾਡਲਾਂ ਨੂੰ ਅਧਿਕ ਤੀਵਰ ਕਰਨ ਲਈ CPU+GPU ਹਾਈਬ੍ਰਿਡ ਇਨਫਰੈਂਸ  

## **llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 ਦਾ ਕੁਆਂਟਾਈਜ਼ਿੰਗ**

Phi-3.5-Instruct ਮਾਡਲ ਨੂੰ llama.cpp ਨਾਲ ਕੁਆਂਟਾਈਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਪਰ Phi-3.5-Vision ਅਤੇ Phi-3.5-MoE ਨੂੰ ਅਜੇ ਤੱਕ ਸਹਾਇਤਾ ਨਹੀਂ ਮਿਲੀ। llama.cpp ਦੁਆਰਾ ਬਦਲਾ ਗਿਆ ਫਾਰਮੈਟ gguf ਹੈ, ਜੋ ਸਭ ਤੋਂ ਵਿਆਪਕ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ ਫਾਰਮੈਟ ਵੀ ਹੈ।

Hugging Face 'ਤੇ ਬਹੁਤ ਸਾਰੇ ਕੁਆਂਟਾਈਜ਼ਡ GGUF ਫਾਰਮੈਟ ਮਾਡਲ ਉਪਲਬਧ ਹਨ। AI Foundry, Ollama, ਅਤੇ LlamaEdge llama.cpp 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ GGUF ਮਾਡਲ ਵੀ ਆਮ ਤੌਰ 'ਤੇ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

### **GGUF ਕੀ ਹੈ**

GGUF ਇੱਕ ਬਾਈਨਰੀ ਫਾਰਮੈਟ ਹੈ ਜੋ ਮਾਡਲਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਲੋਡ ਅਤੇ ਸੇਵ ਕਰਨ ਲਈ ਅਪਟਿਮਾਈਜ਼ਡ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਇਨਫਰੈਂਸ ਲਈ ਬਹੁਤ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਬਣ ਜਾਂਦਾ ਹੈ। GGUF GGML ਅਤੇ ਹੋਰ ਐਗਜ਼ਿਕਿਊਟਰਾਂ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। GGUF ਨੂੰ @ggerganov ਨੇ ਵਿਕਸਤ ਕੀਤਾ ਸੀ ਜੋ llama.cpp ਦਾ ਵੀ ਵਿਕਾਸਕਾਰ ਹੈ, ਜੋ ਇੱਕ ਲੋਕਪ੍ਰਿਯ C/C++ LLM ਇਨਫਰੈਂਸ ਫਰੇਮਵਰਕ ਹੈ। PyTorch ਵਰਗੇ ਫਰੇਮਵਰਕ ਵਿੱਚ ਬਣਾਏ ਮਾਡਲਾਂ ਨੂੰ GGUF ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲ ਕੇ ਉਹਨਾਂ ਇੰਜਣਾਂ ਨਾਲ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

### **ONNX ਅਤੇ GGUF ਵਿੱਚ ਤਫਾਵਤ**

ONNX ਇੱਕ ਰਵਾਇਤੀ ਮਸ਼ੀਨ ਲਰਨਿੰਗ/ਡੀਪ ਲਰਨਿੰਗ ਫਾਰਮੈਟ ਹੈ, ਜੋ ਵੱਖ-ਵੱਖ AI ਫਰੇਮਵਰਕਾਂ ਵਿੱਚ ਵਧੀਆ ਸਹਾਇਤਾ ਨਾਲ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਐਜ ਡਿਵਾਈਸز ਵਿੱਚ ਵੀ ਇਸਦਾ ਚੰਗਾ ਵਰਤੋਂ ਮੌਜੂਦ ਹੈ। GGUF llama.cpp 'ਤੇ ਆਧਾਰਿਤ ਹੈ ਅਤੇ ਕਿਹਾ ਜਾ ਸਕਦਾ ਹੈ ਕਿ ਇਹ GenAI ਯੁੱਗ ਵਿੱਚ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਦੋਹਾਂ ਦੇ ਵਰਤੋਂ ਦੇ ਕੇਸ ਮਿਲਦੇ-ਜੁਲਦੇ ਹਨ। ਜੇ ਤੁਸੀਂ ਐਮਬੈੱਡਡ ਹਾਰਡਵੇਅਰ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਲੇਅਰਾਂ ਵਿੱਚ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ONNX ਤੁਹਾਡੀ ਚੋਣ ਹੋ ਸਕਦੀ ਹੈ। ਜੇ ਤੁਸੀਂ llama.cpp ਦੇ ਡੈਰੀਵੇਟਿਵ ਫਰੇਮਵਰਕ ਅਤੇ ਤਕਨਾਲੋਜੀ ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ GGUF ਵਧੀਆ ਰਹੇਗਾ।

### **llama.cpp ਨਾਲ Phi-3.5-Instruct ਦਾ ਕੁਆਂਟਾਈਜ਼ਿੰਗ**

**1. ਵਾਤਾਵਰਣ ਸੰਰਚਨਾ**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. ਕੁਆਂਟਾਈਜ਼ਿੰਗ**

llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-Instruct ਨੂੰ FP16 GGUF ਵਿੱਚ ਬਦਲੋ


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 ਨੂੰ INT4 ਵਿੱਚ ਕੁਆਂਟਾਈਜ਼ ਕਰਨਾ


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. ਟੈਸਟਿੰਗ**

llama-cpp-python ਇੰਸਟਾਲ ਕਰੋ


```bash

pip install llama-cpp-python -U

```

***ਨੋਟ*** 

ਜੇ ਤੁਸੀਂ Apple Silicon ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ ਇਹ ਤਰੀਕੇ ਨਾਲ llama-cpp-python ਇੰਸਟਾਲ ਕਰੋ


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

**ਅਸਵੀਕਾਰੋਧ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।