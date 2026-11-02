# **在 Android 上進行 Phi-3 推論**

讓我們來探討如何在 Android 裝置上使用 Phi-3-mini 進行推論。Phi-3-mini 是微軟推出的新一系列模型，可實現在邊緣裝置與物聯網設備上部署大型語言模型（LLMs）。

## 語意核心與推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用框架，允許你創建兼容 Azure OpenAI 服務、OpenAI 模型甚至本地模型的應用。如果你是 Semantic Kernel 新手，我們建議你參考 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 存取 Phi-3-mini

你可以將其與 Semantic Kernel 的 Hugging Face 連接器結合使用。請參考此 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

預設情況下，它對應於 Hugging Face 上的模型 ID。不過，你也可以連接本地建置的 Phi-3-mini 模型服務器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶偏好使用量化模型以便在本地運行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允許個人用戶調用不同的量化模型：

#### Ollama

你可以直接運行 `ollama run Phi-3`，或透過建立包含 `.gguf` 檔案路徑的 `Modelfile` ，離線配置它。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你想同時在雲端和邊緣裝置使用 `.gguf` 檔案，LlamaEdge 是不錯的選擇。你可以參考此 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) 開始使用。

### 在 Android 手機上安裝與運行

1. **下載 MLC Chat 應用程式**（免費）用於 Android 手機。
2. 下載 APK 檔案（148MB），並安裝至你的裝置。
3. 啟動 MLC Chat 應用程式。你會看到包含 Phi-3-mini 在內的 AI 模型列表。

### 使用 LiteRT-LM 運行 Phi-4-mini-reasoning

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) 以社群轉換的 int4 `.litertlm` 套件形式提供，適用於 Google 的 [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) 裝置端執行環境。在 Android 上，它可透過 [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) 應用程式 (從應用程式內部 Hugging Face 匯入套件) 或 LiteRT-LM Kotlin API 在 CPU 或 GPU 上運行；同一套件也可在 iOS、macOS、Linux 和 Windows 上運行。模型卡列出了測試速度及運行指令。

總結來說，Phi-3-mini 為邊緣設備上的生成式 AI 開啟了令人振奮的可能性，而您可以開始在 Android 上探索它的功能。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->