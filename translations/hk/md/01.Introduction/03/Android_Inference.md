<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-04T17:44:20+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "hk"
}
-->
# **在 Android 上推理 Phi-3**

讓我們看看如何在 Android 設備上使用 Phi-3-mini 進行推理。Phi-3-mini 是 Microsoft 推出的一系列新模型，能夠在邊緣設備和物聯網設備上部署大型語言模型（LLMs）。

## Semantic Kernel 和推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用框架，能讓你創建兼容 Azure OpenAI Service、OpenAI 模型甚至本地模型的應用。如果你是 Semantic Kernel 的新手，我們建議你查看 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 訪問 Phi-3-mini

你可以將其與 Semantic Kernel 中的 Hugging Face Connector 結合使用。參考這段 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

默認情況下，它對應 Hugging Face 上的模型 ID。不過，你也可以連接到本地搭建的 Phi-3-mini 模型服務器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶更喜歡使用量化模型來本地運行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允許用戶調用不同的量化模型：

#### Ollama

你可以直接運行 `ollama run Phi-3`，或者通過創建一個 `Modelfile` 並配置 `.gguf` 文件的路徑來離線運行。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你想在雲端和邊緣設備上同時使用 `.gguf` 文件，LlamaEdge 是一個很好的選擇。你可以參考這段 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) 開始使用。

### 在 Android 手機上安裝和運行

1. **下載 MLC Chat 應用**（免費）適用於 Android 手機。
2. 下載 APK 文件（148MB），並安裝到你的設備上。
3. 啟動 MLC Chat 應用。你會看到一系列 AI 模型，包括 Phi-3-mini。

總而言之，Phi-3-mini 為邊緣設備上的生成式 AI 開啟了令人興奮的可能性，你可以開始在 Android 設備上探索它的功能。

**免責聲明**：  
此文件已使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或錯誤負責。