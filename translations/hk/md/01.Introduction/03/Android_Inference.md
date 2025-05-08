<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-08T05:57:09+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "hk"
}
-->
# **Android 上使用 Phi-3 進行推理**

讓我們來看看如何在 Android 裝置上使用 Phi-3-mini 進行推理。Phi-3-mini 是 Microsoft 推出的新一代模型系列，能夠讓大型語言模型（LLMs）部署在邊緣設備和物聯網裝置上。

## Semantic Kernel 與推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用框架，讓你能夠建立與 Azure OpenAI Service、OpenAI 模型，甚至本地模型相容的應用程式。如果你是 Semantic Kernel 新手，建議先參考 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 訪問 Phi-3-mini

你可以將它與 Semantic Kernel 裡的 Hugging Face Connector 結合使用。詳情請參考這個[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

預設情況下，它會對應到 Hugging Face 上的模型 ID，不過你也可以連接到本地架設的 Phi-3-mini 模型伺服器。

### 使用 Ollama 或 LlamaEdge 呼叫量化模型

很多用戶喜歡使用量化模型在本地執行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 讓個人用戶可以呼叫不同的量化模型：

#### Ollama

你可以直接運行 `ollama run Phi-3`，或者透過建立一個 `Modelfile`，並指定 `.gguf` 檔案路徑來離線配置。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你想同時在雲端和邊緣裝置上使用 `.gguf` 檔案，LlamaEdge 是個不錯的選擇。你可以參考這個[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)開始使用。

### 在 Android 手機上安裝並運行

1. **下載 MLC Chat app**（免費）給 Android 手機使用。
2. 下載 APK 檔案（148MB）並安裝到你的裝置。
3. 啟動 MLC Chat app，你會看到包括 Phi-3-mini 在內的 AI 模型列表。

總結來說，Phi-3-mini 為邊緣裝置上的生成式 AI 開啟了更多可能，你也可以開始在 Android 上探索它的功能。

**免責聲明**：  
本文件係用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我哋盡力確保準確性，但請注意自動翻譯可能會有錯誤或不準確之處。原文文件嘅母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。