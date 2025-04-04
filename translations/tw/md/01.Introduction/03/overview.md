<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d570fac7029d6697ad8ab1c963b43811",
  "translation_date": "2025-04-04T06:00:45+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "tw"
}
-->
在 Phi-3-mini 的背景下，推理是指利用模型基於輸入數據進行預測或生成輸出的過程。以下是關於 Phi-3-mini 及其推理能力的詳細說明。

Phi-3-mini 是 Microsoft 發布的 Phi-3 系列模型之一。這些模型旨在重新定義小型語言模型（SLMs）的可能性。

以下是 Phi-3-mini 及其推理能力的一些關鍵點：

## **Phi-3-mini 概述：**
- Phi-3-mini 擁有 38 億個參數。
- 它不僅可以在傳統計算設備上運行，還可以在移動設備和物聯網設備等邊緣設備上運行。
- Phi-3-mini 的發布使個人和企業能夠在不同硬件設備上部署 SLMs，尤其是在資源有限的環境中。
- 它支持多種模型格式，包括傳統的 PyTorch 格式、量化版本的 gguf 格式，以及基於 ONNX 的量化版本。

## **訪問 Phi-3-mini：**
要訪問 Phi-3-mini，可以在 Copilot 應用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常與 Azure OpenAI Service、Hugging Face 上的開源模型以及本地模型兼容。
你也可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 來調用量化模型。Ollama 允許個人用戶調用不同的量化模型，而 LlamaEdge 則為 GGUF 模型提供跨平台支持。

## **量化模型：**
許多用戶更傾向於使用量化模型進行本地推理。例如，你可以直接運行 Ollama run Phi-3，或者通過 Modelfile 進行離線配置。Modelfile 會指定 GGUF 文件的路徑以及提示格式。

## **生成式 AI 的可能性：**
結合像 Phi-3-mini 這樣的 SLMs，開啟了生成式 AI 的新可能性。推理只是第一步，這些模型可以用於資源受限、延遲要求高以及成本受限的各種任務場景。

## **解鎖 Phi-3-mini 的生成式 AI：推理與部署指南**
了解如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 訪問並推理 Phi-3-mini 模型，探索生成式 AI 在各種應用場景中的可能性。

**功能**
在以下平台進行 Phi-3-mini 模型推理：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

總結來說，Phi-3-mini 讓開發者能夠探索不同的模型格式，並在各種應用場景中充分利用生成式 AI。

**免責聲明**：  
本文檔是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。我們努力確保翻譯的準確性，但請注意，機器翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤解不承擔責任。