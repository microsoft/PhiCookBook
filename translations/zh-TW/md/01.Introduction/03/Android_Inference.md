# **在 Android 上使用 Phi-3 進行推論**

讓我們來看看如何在 Android 裝置上使用 Phi-3-mini 進行推論。Phi-3-mini 是微軟推出的新一代模型系列，能夠在邊緣裝置和物聯網設備上部署大型語言模型（LLM）。

## Semantic Kernel 與推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用框架，讓你能夠建立與 Azure OpenAI 服務、OpenAI 模型，甚至本地模型相容的應用程式。如果你是 Semantic Kernel 新手，建議先參考 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 存取 Phi-3-mini

你可以將它與 Semantic Kernel 中的 Hugging Face Connector 結合使用。請參考這個[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

預設情況下，它會對應到 Hugging Face 上的模型 ID，但你也可以連接到本地建置的 Phi-3-mini 模型伺服器。

### 使用 Ollama 或 LlamaEdge 呼叫量化模型

許多用戶偏好使用量化模型來本地執行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允許個人用戶呼叫不同的量化模型：

#### Ollama

你可以直接執行 `ollama run Phi-3`，或透過建立一個指向 `.gguf` 檔案路徑的 `Modelfile` 來離線設定。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你想同時在雲端和邊緣裝置使用 `.gguf` 檔案，LlamaEdge 是個不錯的選擇。你可以參考這個[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)開始使用。

### 在 Android 手機上安裝與執行

1. **下載 MLC Chat 應用程式**（免費）到 Android 手機。
2. 下載 APK 檔案（148MB）並安裝到你的裝置。
3. 啟動 MLC Chat 應用程式，你會看到包含 Phi-3-mini 在內的 AI 模型列表。

總結來說，Phi-3-mini 為邊緣裝置上的生成式 AI 帶來了令人興奮的可能性，你可以開始在 Android 上探索它的功能。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。