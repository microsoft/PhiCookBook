## 微調場景

![FineTuning with MS Services](../../../../translated_images/zh-TW/FinetuningwithMS.3d0cec8ae693e094.webp)

本節概述在 Microsoft Foundry 和 Azure 環境中的微調場景，包括部署模型、基礎架構層以及常用的優化技術。

<strong>平台</strong>  
包括像 Microsoft Foundry（前稱 Microsoft Foundry）和 Azure Machine Learning 等受管理的服務，提供模型管理、編排、實驗追蹤及部署工作流程。

<strong>基礎架構</strong>  
微調需要可擴展的運算資源。在 Azure 環境中，通常包括基於 GPU 的虛擬機和用於輕量工作負載的 CPU 資源，以及可擴展的存儲空間用於資料集和檢查點。

<strong>工具與框架</strong>  
微調工作流程通常依賴於 Hugging Face Transformers、DeepSpeed 和 PEFT（參數效能微調）等框架和優化庫。

使用 Microsoft 技術的微調過程涵蓋平台服務、運算基礎架構與訓練框架。通過理解這些元件如何協同工作，開發人員能有效地將基礎模型調整至特定任務和生產場景。

## 模型即服務

使用託管微調進行模型微調，無需自行建立和管理運算資源。

![MaaS Fine Tuning](../../../../translated_images/zh-TW/MaaSfinetune.3eee4630607aff0d.webp)

無伺服器微調現在支援 Phi-3、Phi-3.5 和 Phi-4 模型系列，讓開發者能快速且輕鬆地為雲端與邊緣場景定制模型，無需自行安排運算資源。

## 模型即平台

用戶自行管理運算資源來微調他們的模型。

![Maap Fine Tuning](../../../../translated_images/zh-TW/MaaPFinetune.fd3829c1122f5d1c.webp)

[微調範例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 微調技術比較

|場景|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|將已預訓練的 LLM 調整至特定任務或領域|是|是|是|是|是|是|
|針對 NLP 任務如文本分類、命名實體識別及機器翻譯的微調|是|是|是|是|是|是|
|針對問答任務的微調|是|是|是|是|是|是|
|針對聊天機器人生成類人回應的微調|是|是|是|是|是|是|
|針對創作音樂、藝術或其他創意形式的微調|是|是|是|是|是|是|
|降低計算和經濟成本|是|是|是|是|是|是|
|降低記憶體使用量|是|是|是|是|是|是|
|使用更少參數進行有效微調|是|是|是|否|否|是|
|記憶體有效的資料並行形式，可使用所有 GPU 裝置之累積 GPU 記憶體|否|否|否|是|是|否|

> [!NOTE]
> LoRA、QLoRA、PEFT 和 DoRA 是參數效能微調方法，而 DeepSpeed 和 ZeRO 著重於分散式訓練與記憶體優化。

## 微調效能範例

![Finetuning Performance](../../../../translated_images/zh-TW/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本文件應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->