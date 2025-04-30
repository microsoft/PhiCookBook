# **Quantizing Phi Family using llama.cpp**

## **What's llama.cpp**

llama.cpp is an open-source software library primarily written in C++ that performs inference on various Large Language Models (LLMs), such as Llama. Its main goal is to provide state-of-the-art performance for LLM inference across a wide range of hardware with minimal setup. Additionally, there are Python bindings available for this library, which offer a high-level API for text completion and an OpenAI compatible web server.

The main goal of llama.cpp is to enable LLM inference with minimal setup and state-of-the-art performance on a wide variety of hardware - locally and in the cloud.

- Plain C/C++ implementation without any dependencies
- Apple silicon is a first-class citizen - optimized via ARM NEON, Accelerate and Metal frameworks
- AVX, AVX2 and AVX512 support for x86 architectures
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory use
- Custom CUDA kernels for running LLMs on NVIDIA GPUs (support for AMD GPUs via HIP)
- Vulkan and SYCL backend support
- CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity

## **Quantizing Phi-3.5 with llama.cpp**

The Phi-3.5-Instruct model can be quantized using llama.cpp, but Phi-3.5-Vision and Phi-3.5-MoE are not supported yet. The format converted by llama.cpp is gguf, which is also the most widely used quantization format.

There are a large number of quantized GGUF format models on Hugging face. AI Foundry, Ollama, and LlamaEdge rely on llama.cpp, so GGUF models are also often used.

### **What's GGUF**

GGUF is a binary format that is optimized for quick loading and saving of models, making it highly efficient for inference purposes. GGUF is designed for use with GGML and other executors. GGUF was developed by @ggerganov who is also the developer of llama.cpp, a popular C/C++ LLM inference framework. Models initially developed in frameworks like PyTorch can be converted to GGUF format for use with those engines.

### **ONNX vs GGUF**

ONNX is a traditional machine learning/deep learning format, which is well supported in different AI Frameworks and has good usage scenarios in edge devices. As for GGUF, it is based on llama.cpp and can be said to be produced in the GenAI era. The two have similar uses. If you want better performance in embedded hardware and application layers, ONNX may be your choice. If you use the derivative framework and technology of llama.cpp, then GGUF may be better.

### **Quantization Phi-3.5-Instruct using llama.cpp**

**1. Environment Configuration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

Using llama.cpp convert Phi-3.5-Instruct to FP16 GGUF


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

If you use Apple Silicon , please install llama-cpp-python like this


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testing 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resources**

1. Learn more about llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Learn mode about onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Learn more about GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)



