<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-08T06:04:01+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "hk"
}
-->
喺Phi-3-mini嘅背景下，inference指用模型根據輸入數據作出預測或生成輸出嘅過程。等我詳細講下Phi-3-mini同佢嘅inference能力。

Phi-3-mini係Microsoft發佈嘅Phi-3系列模型之一。呢啲模型係為咗重新定義小型語言模型（SLMs）嘅可能性而設計。

以下係關於Phi-3-mini同佢inference能力嘅重點：

## **Phi-3-mini 簡介：**
- Phi-3-mini有38億個參數。
- 除咗可以喺傳統計算設備運行，仲可以喺邊緣設備，例如手機同物聯網設備運行。
- Phi-3-mini嘅發佈令個人同企業可以喺唔同硬件設備部署SLMs，特別係喺資源有限嘅環境。
- 支援多種模型格式，包括傳統PyTorch格式、量化版嘅gguf格式同基於ONNX嘅量化版本。

## **點樣使用Phi-3-mini：**
想用Phi-3-mini，可以喺Copilot應用程式入面用[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel一般兼容Azure OpenAI Service、Hugging Face嘅開源模型同本地模型。
你亦可以用[Ollama](https://ollama.com)或者[LlamaEdge](https://llamaedge.com)去調用量化模型。Ollama方便個人用戶調用唔同嘅量化模型，而LlamaEdge提供跨平台嘅GGUF模型支援。

## **量化模型：**
好多用戶鍾意用量化模型嚟做本地inference。例如，你可以直接用Ollama跑Phi-3，或者用Modelfile離線配置。Modelfile會指定GGUF文件路徑同prompt格式。

## **生成式AI嘅可能性：**
將Phi-3-mini呢啲SLMs結合起嚟，為生成式AI帶嚟新嘅可能性。inference只係第一步；呢啲模型可以用喺資源有限、延遲要求高同成本受限嘅場景做唔同任務。

## **用Phi-3-mini解鎖生成式AI：Inference同部署指南**  
學識點用Semantic Kernel、Ollama/LlamaEdge同ONNX Runtime去存取同推理Phi-3-mini模型，探索生成式AI喺唔同應用場景嘅可能性。

**功能**
喺以下平台推理phi3-mini模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

總括嚟講，Phi-3-mini令開發者可以探索唔同模型格式，並喺唔同應用場景利用生成式AI。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不會對因使用此翻譯而引起的任何誤解或誤釋負責。