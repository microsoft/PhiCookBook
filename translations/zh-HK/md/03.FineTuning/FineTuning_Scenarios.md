## 微調場景

![FineTuning with MS Services](../../../../translated_images/zh-HK/FinetuningwithMS.3d0cec8ae693e094.webp)

本節概述 Microsoft Foundry 和 Azure 環境中的微調場景，包括部署模型、基礎設施層級及常用的優化技術。

<strong>平台</strong>  
包含 Microsoft Foundry（前稱 Microsoft Foundry）和 Azure Machine Learning 等託管服務，提供模型管理、協調、實驗追蹤及部署工作流程。

<strong>基礎設施</strong>  
微調需要可擴展的計算資源。在 Azure 環境中，這通常包括基於 GPU 的虛擬機器以及用於輕量工作負載的 CPU 資源，並配備可擴展的存儲來存放數據集和檢查點。

<strong>工具與框架</strong>  
微調工作流程通常依賴 Hugging Face Transformers、DeepSpeed 及 PEFT（參數高效微調）等框架和優化庫。

微調流程涵蓋 Microsoft 技術的平臺服務、計算基礎設施及訓練框架。理解這些組件如何協同運作，可幫助開發者有效地將基礎模型調整為特定任務及生產場景。

## 模型即服務

使用托管微調來微調模型，無需自行建立和管理計算資源。

![MaaS Fine Tuning](../../../../translated_images/zh-HK/MaaSfinetune.3eee4630607aff0d.webp)

Serverless 微調現已支援 Phi-3、Phi-3.5 及 Phi-4 模型系列，讓開發者能快速輕鬆地為雲端和邊緣場景自訂模型，無需安排計算資源。

## 模型即平台

用戶自主管理計算資源以微調模型。

![Maap Fine Tuning](../../../../translated_images/zh-HK/MaaPFinetune.fd3829c1122f5d1c.webp)

[微調範例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 微調技術比較

|場景|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|將預訓練大型語言模型適應於特定任務或領域|是|是|是|是|是|是|
|針對 NLP 任務如文本分類、命名實體識別和機器翻譯的微調|是|是|是|是|是|是|
|問答任務微調|是|是|是|是|是|是|
|聊天機器人生成類人回應的微調|是|是|是|是|是|是|
|生成音樂、藝術或其他創意形式的微調|是|是|是|是|是|是|
|降低計算和財務成本|是|是|是|是|是|是|
|降低記憶體使用量|是|是|是|是|是|是|
|使用較少參數以實現高效微調|是|是|是|否|否|是|
|一種記憶體高效的數據並行形式，能使用所有 GPU 裝置的匯總 GPU 記憶體|否|否|否|是|是|否|

> [!NOTE]
> LoRA、QLoRA、PEFT 與 DoRA 是參數高效微調方法，而 DeepSpeed 與 ZeRO 則專注於分散式訓練和記憶體優化。

## 微調效能範例

![Finetuning Performance](../../../../translated_images/zh-HK/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。儘管我們力求精確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯所引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->