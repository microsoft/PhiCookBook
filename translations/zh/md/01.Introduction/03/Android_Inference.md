<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:11:22+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "zh"
}
-->
# **在 Android 上进行 Phi-3 推理**

让我们来看看如何在 Android 设备上使用 Phi-3-mini 进行推理。Phi-3-mini 是微软推出的一系列新模型，支持在边缘设备和物联网设备上部署大型语言模型（LLM）。

## Semantic Kernel 与推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一个应用框架，允许你创建兼容 Azure OpenAI 服务、OpenAI 模型，甚至本地模型的应用程序。如果你是 Semantic Kernel 新手，建议先查看[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 访问 Phi-3-mini

你可以将其与 Semantic Kernel 中的 Hugging Face Connector 结合使用。请参考这份[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

默认情况下，它对应 Hugging Face 上的模型 ID，但你也可以连接到本地搭建的 Phi-3-mini 模型服务器。

### 使用 Ollama 或 LlamaEdge 调用量化模型

许多用户更喜欢使用量化模型在本地运行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允许个人用户调用不同的量化模型：

#### Ollama

你可以直接运行 `ollama run Phi-3`，或者通过创建包含 `.gguf` 文件路径的 `Modelfile` 离线配置。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你想同时在云端和边缘设备上使用 `.gguf` 文件，LlamaEdge 是一个不错的选择。你可以参考这份[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)开始使用。

### 在 Android 手机上安装和运行

1. **下载 MLC Chat 应用**（免费）适用于 Android 手机。  
2. 下载 APK 文件（148MB）并安装到你的设备上。  
3. 启动 MLC Chat 应用，你会看到包括 Phi-3-mini 在内的 AI 模型列表。

总之，Phi-3-mini 为边缘设备上的生成式 AI 带来了令人兴奋的可能性，你可以开始在 Android 上探索它的功能。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。