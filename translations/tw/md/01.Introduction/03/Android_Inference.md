<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-04T05:53:37+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "tw"
}
-->
# **在 Android 上進行 Phi-3 推論**

讓我們來看看如何在 Android 設備上使用 Phi-3-mini 進行推論。Phi-3-mini 是 Microsoft 推出的一系列新模型，能夠讓大型語言模型（LLMs）部署在邊緣設備和物聯網設備上。

## Semantic Kernel 與推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用框架，允許你創建兼容 Azure OpenAI Service、OpenAI 模型，甚至本地模型的應用。如果你是 Semantic Kernel 的新手，我們建議你查看 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 訪問 Phi-3-mini

你可以將它與 Semantic Kernel 中的 Hugging Face Connector 結合使用。請參考這份 [範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

預設情況下，它對應於 Hugging Face 上的模型 ID。不過，你也可以連接到本地部署的 Phi-3-mini 模型伺服器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶更喜歡使用量化模型來本地運行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允許用戶調用不同的量化模型：

#### Ollama

你可以直接運行 `ollama run Phi-3` 或透過建立一個 `Modelfile`，並配置 `.gguf` 檔案的路徑以離線方式使用。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你希望同時在雲端和邊緣設備上使用 `.gguf` 檔案，LlamaEdge 是一個很好的選擇。你可以參考這份 [範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) 開始使用。

### 在 Android 手機上安裝和運行

1. **下載 MLC Chat 應用程式**（免費）適用於 Android 手機。
2. 下載 APK 檔案（148MB），並安裝到你的設備上。
3. 啟動 MLC Chat 應用程式。你會看到包括 Phi-3-mini 在內的 AI 模型列表。

總而言之，Phi-3-mini 為邊緣設備上的生成式 AI 開啟了令人興奮的可能性，你可以立即在 Android 設備上探索它的功能。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能會包含錯誤或不精確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或錯誤解釋負責。