<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-07T14:42:03+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "zh"
}
-->
在 Phi-3-mini 的背景下，推理指的是使用模型根据输入数据进行预测或生成输出的过程。让我为你详细介绍一下 Phi-3-mini 及其推理能力。

Phi-3-mini 是微软发布的 Phi-3 系列模型的一部分。这些模型旨在重新定义小型语言模型（SLMs）的可能性。

以下是关于 Phi-3-mini 及其推理能力的一些关键点：

## **Phi-3-mini 概述：**
- Phi-3-mini 拥有 38 亿参数。
- 它不仅能运行在传统计算设备上，还能在移动设备和物联网设备等边缘设备上运行。
- Phi-3-mini 的发布使个人和企业能够在不同硬件设备上部署 SLM，尤其是在资源受限的环境中。
- 它支持多种模型格式，包括传统的 PyTorch 格式、量化的 gguf 格式，以及基于 ONNX 的量化版本。

## **访问 Phi-3-mini：**
你可以在 Copilot 应用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) 来访问 Phi-3-mini。Semantic Kernel 通常兼容 Azure OpenAI 服务、Hugging Face 上的开源模型以及本地模型。  
你还可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 来调用量化模型。Ollama 允许个人用户调用不同的量化模型，而 LlamaEdge 则为 GGUF 模型提供跨平台支持。

## **量化模型：**
许多用户更倾向于使用量化模型进行本地推理。例如，你可以直接使用 Ollama 运行 Phi-3，或通过 Modelfile 离线配置。Modelfile 指定了 GGUF 文件路径和提示格式。

## **生成式 AI 的可能性：**
结合像 Phi-3-mini 这样的 SLM，开启了生成式 AI 的新可能。推理只是第一步；这些模型可以应用于资源受限、延迟要求高和成本受限的各种场景。

## **用 Phi-3-mini 解锁生成式 AI：推理与部署指南**  
学习如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 访问并推理 Phi-3-mini 模型，探索生成式 AI 在多种应用场景中的潜力。

**功能**  
在以下平台推理 phi3-mini 模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

总之，Phi-3-mini 让开发者能够探索不同的模型格式，并在多种应用场景中利用生成式 AI。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力保证翻译的准确性，但请注意，自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。