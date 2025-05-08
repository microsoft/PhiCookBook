<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-08T06:04:21+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "tw"
}
-->
在 Phi-3-mini 的背景下，推論指的是使用模型根據輸入資料進行預測或產生輸出結果的過程。讓我為你介紹更多關於 Phi-3-mini 及其推論能力的細節。

Phi-3-mini 是微軟發布的 Phi-3 系列模型之一。這些模型旨在重新定義小型語言模型（SLM）的可能性。

以下是關於 Phi-3-mini 及其推論能力的一些重點：

## **Phi-3-mini 概覽：**
- Phi-3-mini 擁有 38 億參數。
- 它不僅能在傳統計算設備上運行，也能在邊緣設備，如行動裝置和物聯網設備上執行。
- Phi-3-mini 的發布使個人和企業能夠在不同硬體設備上部署 SLM，尤其是在資源有限的環境中。
- 支援多種模型格式，包括傳統的 PyTorch 格式、量化版的 gguf 格式，以及基於 ONNX 的量化版本。

## **如何存取 Phi-3-mini：**
你可以在 Copilot 應用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) 來存取 Phi-3-mini。Semantic Kernel 通常與 Azure OpenAI 服務、Hugging Face 上的開源模型，以及本地模型相容。
你也可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 來調用量化模型。Ollama 允許個人用戶呼叫不同的量化模型，而 LlamaEdge 則提供 GGUF 模型的跨平台支援。

## **量化模型：**
許多使用者偏好使用量化模型進行本地推論。例如，你可以直接用 Ollama 執行 Phi-3，或使用 Modelfile 離線配置。Modelfile 指定了 GGUF 檔案路徑和提示格式。

## **生成式 AI 的可能性：**
結合像 Phi-3-mini 這樣的 SLM，開啟了生成式 AI 的新可能性。推論只是第一步；這些模型可用於資源有限、延遲敏感及成本受限的各種任務。

## **利用 Phi-3-mini 解鎖生成式 AI：推論與部署指南**  
學習如何使用 Semantic Kernel、Ollama/LlamaEdge 與 ONNX Runtime 來存取及推論 Phi-3-mini 模型，並探索生成式 AI 在各種應用場景中的可能性。

**功能**  
在以下平台推論 phi3-mini 模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

總結來說，Phi-3-mini 讓開發者能夠探索不同的模型格式，並在多種應用場景中運用生成式 AI。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威依據。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤譯負責。