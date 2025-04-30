<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2a7aaeb42235207ba74581473b305581",
  "translation_date": "2025-04-03T07:04:43+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "zh"
}
-->
# **使用 llama.cpp 对 Phi 系列进行量化**

## **什么是 llama.cpp**

llama.cpp 是一个主要使用 C++ 编写的开源软件库，用于对各种大型语言模型（LLM）进行推理，例如 Llama。其主要目标是在广泛的硬件上实现最先进的 LLM 推理性能，同时简化设置过程。此外，该库还提供了 Python 绑定，提供用于文本补全的高级 API，以及一个兼容 OpenAI 的网络服务器。

llama.cpp 的主要目标是以最小的设置和先进的性能支持本地和云端的多种硬件进行 LLM 推理。

- 纯 C/C++ 实现，无需任何依赖
- Apple Silicon 是一级支持对象 - 通过 ARM NEON、Accelerate 和 Metal 框架进行优化
- 支持 x86 架构的 AVX、AVX2 和 AVX512
- 支持 1.5 位、2 位、3 位、4 位、5 位、6 位和 8 位整数量化，以加速推理并减少内存使用
- 针对 NVIDIA GPU 的自定义 CUDA 内核（支持 AMD GPU 通过 HIP）
- Vulkan 和 SYCL 后端支持
- CPU+GPU 混合推理，用于加速大于总显存容量的模型

## **使用 llama.cpp 对 Phi-3.5 进行量化**

Phi-3.5-Instruct 模型可以通过 llama.cpp 进行量化，但 Phi-3.5-Vision 和 Phi-3.5-MoE 目前尚不支持。llama.cpp 转换的格式为 gguf，这也是目前最广泛使用的量化格式。

在 Hugging Face 上有大量量化的 GGUF 格式模型。AI Foundry、Ollama 和 LlamaEdge 都依赖于 llama.cpp，因此 GGUF 模型也被频繁使用。

### **什么是 GGUF**

GGUF 是一种二进制格式，专为快速加载和保存模型而优化，非常适合推理使用。GGUF 设计用于 GGML 和其他执行器。GGUF 由 @ggerganov 开发，他也是 llama.cpp 的开发者，这是一个广受欢迎的 C/C++ LLM 推理框架。最初在 PyTorch 等框架中开发的模型可以转换为 GGUF 格式，以便在这些引擎中使用。

### **ONNX 与 GGUF**

ONNX 是一种传统的机器学习/深度学习格式，在不同的 AI 框架中得到了良好的支持，并且在边缘设备中有很好的使用场景。至于 GGUF，它基于 llama.cpp，可以说是在生成式 AI 时代中诞生的。两者用途相似。如果您希望在嵌入式硬件和应用层中获得更好的性能，ONNX 可能是您的选择。如果您使用 llama.cpp 的衍生框架和技术，那么 GGUF 可能更适合。

### **使用 llama.cpp 对 Phi-3.5-Instruct 进行量化**

**1. 环境配置**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. 量化**

使用 llama.cpp 将 Phi-3.5-Instruct 转换为 FP16 GGUF

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

将 Phi-3.5 量化为 INT4

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. 测试**

安装 llama-cpp-python

```bash

pip install llama-cpp-python -U

```

***注意***

如果您使用的是 Apple Silicon，请按照以下方式安装 llama-cpp-python

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

测试

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **资源**

1. 了解更多关于 llama.cpp 的信息 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. 了解更多关于 GGUF 的信息 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免责声明**：  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们不承担责任。