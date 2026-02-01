在 Phi-3-mini 的背景下，推論指的是使用模型根據輸入資料進行預測或產生輸出結果的過程。讓我為你介紹更多關於 Phi-3-mini 及其推論能力的細節。

Phi-3-mini 是微軟推出的 Phi-3 系列模型之一。這些模型旨在重新定義小型語言模型（SLMs）的可能性。

以下是關於 Phi-3-mini 及其推論能力的一些重點：

## **Phi-3-mini 概述：**
- Phi-3-mini 擁有 38 億個參數。
- 它不僅能在傳統計算設備上運行，也能在邊緣設備如行動裝置和物聯網設備上運作。
- Phi-3-mini 的發布使個人和企業能夠在不同硬體設備上部署 SLM，特別是在資源有限的環境中。
- 支援多種模型格式，包括傳統的 PyTorch 格式、量化後的 gguf 格式，以及基於 ONNX 的量化版本。

## **存取 Phi-3-mini：**
要使用 Phi-3-mini，你可以在 Copilot 應用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常與 Azure OpenAI 服務、Hugging Face 上的開源模型以及本地模型相容。
你也可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 來調用量化模型。Ollama 允許個人用戶調用不同的量化模型，而 LlamaEdge 則提供 GGUF 模型的跨平台支援。

## **量化模型：**
許多用戶偏好使用量化模型進行本地推論。例如，你可以直接使用 Ollama 執行 Phi-3，或透過 Modelfile 離線配置。Modelfile 指定 GGUF 檔案路徑及提示格式。

## **生成式 AI 的可能性：**
結合像 Phi-3-mini 這樣的 SLM，為生成式 AI 開啟了新的可能性。推論只是第一步；這些模型可用於資源受限、延遲要求高及成本限制的多種任務。

## **使用 Phi-3-mini 解鎖生成式 AI：推論與部署指南**  
學習如何使用 Semantic Kernel、Ollama/LlamaEdge 及 ONNX Runtime 存取並推論 Phi-3-mini 模型，並探索生成式 AI 在各種應用場景中的潛力。

**功能**  
在以下平台推論 phi3-mini 模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

總結來說，Phi-3-mini 讓開發者能探索不同的模型格式，並在多種應用場景中善用生成式 AI。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。