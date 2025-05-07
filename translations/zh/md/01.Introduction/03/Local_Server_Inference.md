<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-05-07T14:30:49+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "zh"
}
-->
# **在本地服务器上推理 Phi-3**

我们可以将 Phi-3 部署在本地服务器上。用户可以选择 [Ollama](https://ollama.com) 或 [LM Studio](https://llamaedge.com) 解决方案，或者编写自己的代码。你可以通过 [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) 或 [Langchain](https://www.langchain.com/) 连接 Phi-3 的本地服务，来构建 Copilot 应用。

## **使用 Semantic Kernel 访问 Phi-3-mini**

在 Copilot 应用中，我们通过 Semantic Kernel / LangChain 创建应用。这类应用框架通常兼容 Azure OpenAI Service / OpenAI 模型，也能支持 Hugging Face 上的开源模型和本地模型。如果想用 Semantic Kernel 访问 Phi-3-mini，该怎么做？以 .NET 为例，我们可以将其与 Semantic Kernel 中的 Hugging Face Connector 结合使用。默认情况下，它会对应 Hugging Face 上的模型 id（首次使用时，模型会从 Hugging Face 下载，耗时较长）。你也可以连接到已构建的本地服务。相比之下，我们推荐使用后者，因为它具有更高的自主性，尤其适合企业级应用。

![sk](../../../../../translated_images/sk.d03785c25edc6d445a2e9ae037979e544e0b0c482f43c7617b0324e717b9af62.zh.png)

从图中可以看出，通过 Semantic Kernel 访问本地服务，可以轻松连接到自建的 Phi-3-mini 模型服务器。以下是运行结果：

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca2020eefcaeaaee184d29bb0cf1c37b00fd9c79acc23a6dc8d2.zh.png)

***示例代码*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力保证准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。