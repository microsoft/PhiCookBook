<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-03T06:49:37+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "zh"
}
-->
# **在安卓设备上进行Phi-3推理**

让我们来探讨如何在安卓设备上使用Phi-3-mini进行推理。Phi-3-mini是微软推出的一系列新模型，能够在边缘设备和物联网设备上部署大型语言模型（LLMs）。

## Semantic Kernel与推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一个应用框架，允许您创建与Azure OpenAI Service、OpenAI模型甚至本地模型兼容的应用程序。如果您是Semantic Kernel的新手，我们建议您查看[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用Semantic Kernel访问Phi-3-mini

您可以将它与Semantic Kernel中的Hugging Face Connector结合使用。请参考此[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

默认情况下，它对应于Hugging Face上的模型ID。不过，您也可以连接到本地构建的Phi-3-mini模型服务器。

### 使用Ollama或LlamaEdge调用量化模型

许多用户更喜欢使用量化模型来本地运行模型。[Ollama](https://ollama.com/)和[LlamaEdge](https://llamaedge.com)允许用户调用不同的量化模型：

#### Ollama

您可以直接运行`ollama run Phi-3`，或者通过创建一个`Modelfile`文件并指定`.gguf`文件路径来离线配置。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果您希望同时在云端和边缘设备上使用`.gguf`文件，LlamaEdge是一个很好的选择。您可以参考此[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)开始使用。

### 在安卓手机上安装和运行

1. **下载MLC Chat应用**（免费）用于安卓手机。
2. 下载APK文件（148MB），并安装到您的设备上。
3. 打开MLC Chat应用。您会看到包括Phi-3-mini在内的AI模型列表。

总而言之，Phi-3-mini为边缘设备上的生成式AI带来了令人兴奋的可能性，您可以开始在安卓设备上探索它的功能。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本的文档应被视为权威来源。对于重要信息，建议使用专业的人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。