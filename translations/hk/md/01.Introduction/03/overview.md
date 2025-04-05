<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d570fac7029d6697ad8ab1c963b43811",
  "translation_date": "2025-04-04T17:51:39+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "hk"
}
-->
在 Phi-3-mini 的背景下，推理指的是利用模型根據輸入數據進行預測或生成輸出。以下是關於 Phi-3-mini 及其推理能力的更多詳細信息。

Phi-3-mini 是微軟推出的 Phi-3 系列模型之一。這些模型旨在重新定義小型語言模型（SLMs）的可能性。

以下是 Phi-3-mini 及其推理能力的一些關鍵點：

## **Phi-3-mini 概述：**
- Phi-3-mini 擁有 38 億參數規模。
- 它不僅可以在傳統計算設備上運行，還能在邊緣設備（例如移動設備和物聯網設備）上運行。
- Phi-3-mini 的發布使個人和企業能夠在不同的硬件設備上部署 SLMs，特別是在資源有限的環境中。
- 它支持多種模型格式，包括傳統的 PyTorch 格式、量化的 gguf 格式以及基於 ONNX 的量化版本。

## **訪問 Phi-3-mini：**
要訪問 Phi-3-mini，您可以在 Copilot 應用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常兼容 Azure OpenAI Service、Hugging Face 的開源模型以及本地模型。
您還可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 調用量化模型。Ollama 允許個人用戶調用不同的量化模型，而 LlamaEdge 則提供 GGUF 模型的跨平台支持。

## **量化模型：**
許多用戶更喜歡使用量化模型進行本地推理。例如，您可以直接運行 Ollama run Phi-3，或者使用 Modelfile 進行離線配置。Modelfile 指定 GGUF 文件路徑和提示格式。

## **生成式 AI 的可能性：**
結合像 Phi-3-mini 這樣的小型語言模型，生成式 AI 的新可能性被開啟。推理僅僅是第一步，這些模型可以用於資源受限、延遲敏感和成本受限的各種任務。

## **利用 Phi-3-mini 解鎖生成式 AI：推理與部署指南**  
學習如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 訪問和推理 Phi-3-mini 模型，並探索生成式 AI 在各種應用場景中的可能性。

**功能**
在以下平台進行 Phi-3-mini 模型推理：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

總結來說，Phi-3-mini 使開發者能夠探索不同的模型格式，並在各種應用場景中利用生成式 AI 的能力。

**免責聲明**:  
此文件已使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原文檔的母語版本應被視為最具權威性的來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。