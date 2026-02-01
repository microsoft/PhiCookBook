在Phi-3-mini的背景下，推理指的是使用模型根据输入数据进行预测或生成输出的过程。下面我将为您详细介绍Phi-3-mini及其推理能力。

Phi-3-mini是微软发布的Phi-3系列模型的一部分。这些模型旨在重新定义小型语言模型（SLMs）的可能性。

以下是关于Phi-3-mini及其推理能力的一些关键点：

## **Phi-3-mini 概述：**
- Phi-3-mini拥有38亿参数规模。
- 它不仅可以在传统计算设备上运行，还能在移动设备和物联网设备等边缘设备上运行。
- Phi-3-mini的发布使个人和企业能够在不同硬件设备上部署SLMs，特别是在资源受限的环境中。
- 支持多种模型格式，包括传统的PyTorch格式、量化后的gguf格式以及基于ONNX的量化版本。

## **访问Phi-3-mini：**
要访问Phi-3-mini，您可以在Copilot应用中使用[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel通常兼容Azure OpenAI服务、Hugging Face上的开源模型以及本地模型。
您还可以使用[Ollama](https://ollama.com)或[LlamaEdge](https://llamaedge.com)调用量化模型。Ollama允许个人用户调用不同的量化模型，而LlamaEdge则为GGUF模型提供跨平台支持。

## **量化模型：**
许多用户更喜欢使用量化模型进行本地推理。例如，您可以直接使用Ollama运行Phi-3，或者通过Modelfile离线配置。Modelfile指定了GGUF文件路径和提示格式。

## **生成式AI的可能性：**
结合像Phi-3-mini这样的SLMs，为生成式AI开辟了新的可能性。推理只是第一步；这些模型可以用于资源受限、延迟敏感和成本受限的各种任务。

## **使用Phi-3-mini解锁生成式AI：推理与部署指南**  
了解如何使用Semantic Kernel、Ollama/LlamaEdge和ONNX Runtime访问并推理Phi-3-mini模型，探索生成式AI在各种应用场景中的潜力。

**功能**  
在以下平台推理phi3-mini模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

总之，Phi-3-mini使开发者能够探索不同的模型格式，并在各种应用场景中利用生成式AI的潜力。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。