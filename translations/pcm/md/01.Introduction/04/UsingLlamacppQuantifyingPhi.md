<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-12-22T01:56:00+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "pcm"
}
-->
# **How to quantize Phi Family wit llama.cpp**

## **Wetin be llama.cpp**

llama.cpp na open-source software library wey dem mainly write for C++ wey dey do inference on different Large Language Models (LLMs), like Llama. Im main goal na to provide state-of-the-art performance for LLM inference across plenty hardware with minimal setup. Plus, dem get Python bindings for this library wey dey offer high-level API for text completion and an OpenAI-compatible web server.

Di main goal of llama.cpp na to enable LLM inference with minimal setup and state-of-the-art performance on plenty different hardware - locally and for the cloud.

- Plain C/C++ implementation wey no get any dependencies
- Apple silicon na first-class citizen - optimized via ARM NEON, Accelerate and Metal frameworks
- AVX, AVX2 and AVX512 support for x86 architectures
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization to make inference faster and reduce memory use
- Custom CUDA kernels for running LLMs on NVIDIA GPUs (support for AMD GPUs via HIP)
- Vulkan and SYCL backend support
- CPU+GPU hybrid inference to partially accelerate models wey big pass the total VRAM capacity

## **Quantizing Phi-3.5 with llama.cpp**

The Phi-3.5-Instruct model fit dey quantized using llama.cpp, but Phi-3.5-Vision and Phi-3.5-MoE no dey supported yet. The format wey llama.cpp convert to na gguf, wey be the most widely used quantization format.

Plenty quantized GGUF format models dey for Hugging Face. AI Foundry, Ollama, and LlamaEdge dey rely on llama.cpp, so GGUF models dey used often too.

### **Wetin be GGUF**

GGUF na binary format wey dem optimize for quick loading and saving of models, so e dey very efficient for inference purposes. GGUF design na to work with GGML and other executors. GGUF na @ggerganov develop am — na him too be developer of llama.cpp, the popular C/C++ LLM inference framework. Models wey dem first build for frameworks like PyTorch fit convert to GGUF format make dem run for those engines.

### **ONNX vs GGUF**

ONNX na traditional machine learning/deep learning format wey get solid support for different AI frameworks and get fine use cases for edge devices. As for GGUF, e base on llama.cpp and you fit talk say dem build am for the GenAI era. Di two dey get similar uses. If you want better performance for embedded hardware and application layers, ONNX fit be your choice. If you dey use derivative framework and technology wey base on llama.cpp, then GGUF fit better.

### **Quantization Phi-3.5-Instruct using llama.cpp**

**1. Environment Configuration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

Make you use llama.cpp convert Phi-3.5-Instruct to FP16 GGUF


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

If you dey use Apple Silicon, make you install llama-cpp-python like dis


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testing 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resources**

1. Find out more about llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Learn mode about onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. Find out more about GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Abeg note:
Dis document dem translate with AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make everything correct, abeg sabi say automated translation fit get errors or no too correct. The original document for im own language na the official/authoritative source. If na serious information, better make person wey sabi translate am humanly do am. We no go responsible for any misunderstanding or wrong interpretation wey fit arise from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->