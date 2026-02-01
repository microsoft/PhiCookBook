# **Quantizing Phi Family using llama.cpp**

## **What's llama.cpp**

llama.cpp is an open-source software library mainly written in C++ that performs inference on various Large Language Models (LLMs), such as Llama. Its primary goal is to deliver state-of-the-art performance for LLM inference across a wide range of hardware with minimal setup. Additionally, Python bindings are available for this library, providing a high-level API for text completion and an OpenAI-compatible web server.

The main objective of llama.cpp is to enable LLM inference with minimal setup and top-tier performance on a wide variety of hardware—both locally and in the cloud.

- Pure C/C++ implementation with no dependencies
- Apple silicon is fully supported—optimized using ARM NEON, Accelerate, and Metal frameworks
- AVX, AVX2, and AVX512 support for x86 architectures
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory usage
- Custom CUDA kernels for running LLMs on NVIDIA GPUs (AMD GPU support via HIP)
- Vulkan and SYCL backend support
- CPU+GPU hybrid inference to partially accelerate models larger than total VRAM capacity

## **Quantizing Phi-3.5 with llama.cpp**

The Phi-3.5-Instruct model can be quantized using llama.cpp, but Phi-3.5-Vision and Phi-3.5-MoE are not supported yet. The format converted by llama.cpp is gguf, which is also the most widely used quantization format.

There are many quantized GGUF format models available on Hugging Face. AI Foundry, Ollama, and LlamaEdge rely on llama.cpp, so GGUF models are commonly used.

### **What's GGUF**

GGUF is a binary format optimized for fast loading and saving of models, making it highly efficient for inference. GGUF is designed for use with GGML and other executors. GGUF was developed by @ggerganov, who is also the creator of llama.cpp, a popular C/C++ LLM inference framework. Models originally developed in frameworks like PyTorch can be converted to GGUF format for use with these engines.

### **ONNX vs GGUF**

ONNX is a traditional machine learning/deep learning format, well supported across various AI frameworks and widely used in edge devices. GGUF, on the other hand, is based on llama.cpp and can be considered a product of the GenAI era. Both have similar applications. If you want better performance on embedded hardware and application layers, ONNX might be your choice. If you are using the derivative framework and technology of llama.cpp, then GGUF could be a better fit.

### **Quantizing Phi-3.5-Instruct using llama.cpp**

**1. Environment Configuration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

Convert Phi-3.5-Instruct to FP16 GGUF using llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantizing Phi-3.5 to INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testing**

Install llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Note*** 

If you are using Apple Silicon, please install llama-cpp-python like this


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testing 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resources**

1. Learn more about llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Learn more about onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Learn more about GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.