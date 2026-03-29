## 微調場景

![FineTuning with MS Services](../../../../translated_images/zh-MO/FinetuningwithMS.3d0cec8ae693e094.webp)

本節概述了 Microsoft Foundry 及 Azure 環境中的微調場景，包括部署模型、基礎設施層及常用優化技術。

<strong>平台</strong>  
包括 Microsoft Foundry（前稱 Microsoft Foundry）和 Azure 機器學習等管理型服務，提供模型管理、編排、實驗追蹤及部署工作流程。

<strong>基礎設施</strong>  
微調需要可擴充的計算資源。在 Azure 環境中，通常包括基於 GPU 的虛擬機和用於輕量工作負載的 CPU 資源，及用於資料集和檢查點的可擴充存儲。

<strong>工具與框架</strong>  
微調工作流程常依賴框架和優化庫，如 Hugging Face Transformers、DeepSpeed 和 PEFT（參數高效微調）。

利用 Microsoft 技術的微調過程涵蓋平台服務、計算基礎設施和訓練框架。透過瞭解這些元件如何協同工作，開發人員能有效地將基礎模型調整至特定任務和生產場景。

## 以模型為服務

使用託管微調來微調模型，無需建立和管理計算資源。

![MaaS Fine Tuning](../../../../translated_images/zh-MO/MaaSfinetune.3eee4630607aff0d.webp)

無伺服器微調現在支援 Phi-3、Phi-3.5 和 Phi-4 模型系列，使開發者能快速且輕鬆地針對雲端和邊緣場景定制模型，無需安排計算資源。

## 以模型為平台

使用者自行管理計算資源以微調自己的模型。

![Maap Fine Tuning](../../../../translated_images/zh-MO/MaaPFinetune.fd3829c1122f5d1c.webp)

[微調範例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 微調技術比較

|場景|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|將預訓練 LLM 調整至特定任務或領域|是|是|是|是|是|是|
|用於文本分類、命名實體識別和機器翻譯等 NLP 任務的微調|是|是|是|是|是|是|
|問答任務的微調|是|是|是|是|是|是|
|為聊天機器人生成類人回應的微調|是|是|是|是|是|是|
|生成音樂、藝術或其他形式創作的微調|是|是|是|是|是|是|
|降低計算和財務成本|是|是|是|是|是|是|
|降低記憶體使用|是|是|是|是|是|是|
|使用更少參數以實現高效微調|是|是|是|否|否|是|
|以記憶體高效的資料並行形式訪問所有GPU設備的總GPU記憶體|否|否|否|是|是|否|

> [!NOTE]
> LoRA、QLoRA、PEFT 和 DoRA 是參數高效的微調方法，而 DeepSpeed 和 ZeRO 著重於分散式訓練及記憶體優化。

## 微調效能範例

![Finetuning Performance](../../../../translated_images/zh-MO/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯而成。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或曲解概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->