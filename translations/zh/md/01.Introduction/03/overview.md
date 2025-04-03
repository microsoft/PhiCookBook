<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d570fac7029d6697ad8ab1c963b43811",
  "translation_date": "2025-04-03T06:57:10+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "zh"
}
-->
在 Phi-3-mini 的上下文中，推理指的是使用模型根据输入数据进行预测或生成输出的过程。以下是关于 Phi-3-mini 及其推理能力的更多详细信息。

Phi-3-mini 是微软发布的 Phi-3 系列模型的一部分。这些模型旨在重新定义小型语言模型（SLMs）的潜力。

以下是关于 Phi-3-mini 及其推理能力的一些关键点：

## **Phi-3-mini 概述：**
- Phi-3-mini 拥有 38 亿参数。
- 它不仅可以运行在传统计算设备上，还能运行在边缘设备上，例如移动设备和物联网设备。
- Phi-3-mini 的发布使个人和企业能够在不同硬件设备上部署 SLMs，特别是在资源受限的环境中。
- 它支持多种模型格式，包括传统的 PyTorch 格式、量化后的 gguf 格式以及基于 ONNX 的量化版本。

## **访问 Phi-3-mini：**
要访问 Phi-3-mini，可以在 Copilot 应用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常兼容 Azure OpenAI 服务、Hugging Face 上的开源模型以及本地模型。
您还可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 调用量化模型。Ollama 允许个人用户调用不同的量化模型，而 LlamaEdge 为 GGUF 模型提供跨平台的可用性。

## **量化模型：**
许多用户更倾向于使用量化模型进行本地推理。例如，您可以直接运行 Ollama run Phi-3 或使用 Modelfile 离线配置。Modelfile 指定了 GGUF 文件路径和提示格式。

## **生成式 AI 的可能性：**
结合像 Phi-3-mini 这样的 SLMs，开启了生成式 AI 的新可能性。推理只是第一步；这些模型可以在资源受限、延迟敏感和成本受限的场景中完成多种任务。

## **解锁 Phi-3-mini 的生成式 AI：推理与部署指南**  
了解如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 访问和推理 Phi-3-mini 模型，并探索生成式 AI 在各种应用场景中的可能性。

**功能**
在以下平台上进行 Phi-3-mini 模型推理：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

总而言之，Phi-3-mini 使开发者能够探索不同的模型格式，并在多种应用场景中利用生成式 AI。

**免责声明**:  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。