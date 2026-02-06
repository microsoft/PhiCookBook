# **使用 llama.cpp 对 Phi 系列进行量化**

## **什么是 llama.cpp**

llama.cpp 是一个主要用 C++ 编写的开源软件库，能够对各种大型语言模型（LLM），如 Llama，进行推理。它的主要目标是在各种硬件上以最少的配置实现最先进的 LLM 推理性能。此外，该库还提供了 Python 绑定，支持文本补全的高级 API 以及兼容 OpenAI 的 Web 服务器。

llama.cpp 的核心目标是实现 LLM 推理的最小配置和最先进性能，适用于本地和云端的多种硬件环境。

- 纯 C/C++ 实现，无任何依赖
- Apple Silicon 支持优先，利用 ARM NEON、Accelerate 和 Metal 框架进行优化
- 支持 x86 架构的 AVX、AVX2 和 AVX512
- 支持 1.5-bit、2-bit、3-bit、4-bit、5-bit、6-bit 和 8-bit 整数量化，实现更快推理和更低内存占用
- 针对 NVIDIA GPU 的自定义 CUDA 内核（通过 HIP 支持 AMD GPU）
- 支持 Vulkan 和 SYCL 后端
- CPU+GPU 混合推理，可部分加速超出显存容量的模型

## **使用 llama.cpp 对 Phi-3.5 进行量化**

Phi-3.5-Instruct 模型可以通过 llama.cpp 进行量化，但 Phi-3.5-Vision 和 Phi-3.5-MoE 目前尚不支持。llama.cpp 转换的格式是 gguf，这也是目前最广泛使用的量化格式。

Hugging Face 上有大量量化的 GGUF 格式模型。AI Foundry、Ollama 和 LlamaEdge 都依赖于 llama.cpp，因此 GGUF 模型也被广泛使用。

### **什么是 GGUF**

GGUF 是一种二进制格式，针对模型的快速加载和保存进行了优化，非常适合推理使用。GGUF 设计用于 GGML 及其他执行器。GGUF 由 @ggerganov 开发，他也是 llama.cpp 的开发者，llama.cpp 是一个流行的 C/C++ LLM 推理框架。最初在 PyTorch 等框架中开发的模型可以转换为 GGUF 格式，以便在这些引擎中使用。

### **ONNX 与 GGUF 的对比**

ONNX 是一种传统的机器学习/深度学习格式，得到了多种 AI 框架的良好支持，并且在边缘设备中有广泛的应用场景。GGUF 则基于 llama.cpp，可以说是生成式 AI 时代的产物。两者用途相似。如果你需要在嵌入式硬件和应用层获得更好的性能，ONNX 可能是更好的选择；如果你使用 llama.cpp 的衍生框架和技术，那么 GGUF 可能更合适。

### **使用 llama.cpp 量化 Phi-3.5-Instruct**

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

如果你使用 Apple Silicon，请按如下方式安装 llama-cpp-python


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

测试


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **资源**

1. 了解更多关于 llama.cpp 的信息 [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. 了解更多关于 onnxruntime 的信息 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. 了解更多关于 GGUF 的信息 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。