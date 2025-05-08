<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-05-08T05:17:44+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "hk"
}
-->
# **介紹 Azure Machine Learning Service**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) 是一個雲端服務，幫助加速及管理機器學習（ML）項目全生命周期。

機器學習專業人士、數據科學家及工程師可以在日常工作流程中使用它來：

- 訓練及部署模型。
- 管理機器學習運營（MLOps）。
- 你可以在 Azure Machine Learning 裡建立模型，或使用來自開源平台如 PyTorch、TensorFlow 或 scikit-learn 建立的模型。
- MLOps 工具協助你監控、重新訓練及重新部署模型。

## Azure Machine Learning 適合邊個？

**數據科學家及 ML 工程師**

佢哋可以用工具加快及自動化日常工作流程。
Azure ML 提供公平性、可解釋性、追蹤及審計功能。

**應用程式開發者**

可以無縫地將模型整合到應用程式或服務中。

**平台開發者**

擁有強大工具集，背後支援穩定嘅 Azure Resource Manager APIs。
呢啲工具令佢哋可以建立先進嘅 ML 工具。

**企業**

使用 Microsoft Azure 雲端，企業享受熟悉嘅安全性及基於角色嘅存取控制。
可以設定項目，控制對受保護數據及特定操作嘅存取權限。

## 團隊每個人嘅生產力
ML 項目通常需要多元技能嘅團隊去建立及維護。

Azure ML 提供嘅工具令你可以：
- 通過共享筆記本、計算資源、無伺服器計算、數據及環境，與團隊協作。
- 開發具公平性、可解釋性、追蹤及審計功能嘅模型，以符合血統及審計合規要求。
- 快速且輕鬆地大規模部署 ML 模型，並用 MLOps 有效管理及治理。
- 隨時隨地運行機器學習工作負載，同時內置治理、安全及合規。

## 跨平台相容工具

ML 團隊中任何人都可以用自己慣用嘅工具完成工作。
無論你係做快速實驗、超參數調優、建立流程線，或者管理推論，都可以使用熟悉嘅介面，包括：
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

隨著你優化模型及整個開發週期中協作，可以在 Azure Machine Learning studio UI 裡分享及尋找資產、資源及指標。

## **Azure ML 裡嘅 LLM/SLM**

Azure ML 加入咗好多 LLM/SLM 相關功能，結合 LLMOps 同 SLMOps，打造企業級生成式人工智能技術平台。

### **模型目錄**

企業用戶可以根據唔同商業場景透過模型目錄部署不同模型，並以模型即服務（Model as Service）形式為企業開發者或用戶提供服務。

![models](../../../../translated_images/models.e6c7ff50a51806fd0bfd398477e3db3d5c3dc545cd7308344e448e0b8d8295a1.hk.png)

Azure Machine Learning studio 裡嘅模型目錄係發掘及使用多款模型嘅中心，助你建立生成式 AI 應用。模型目錄包含數百款來自 Azure OpenAI service、Mistral、Meta、Cohere、Nvidia、Hugging Face 等模型供應商嘅模型，包括 Microsoft 自家訓練嘅模型。非 Microsoft 供應商嘅模型屬於非 Microsoft 產品，根據 Microsoft 產品條款，受相應條款約束。

### **工作流程管道**

機器學習管道嘅核心係將完整嘅機器學習任務拆分成多步工作流程。每一步係可管理嘅組件，可以獨立開發、優化、配置及自動化。步驟之間透過明確界面連接。Azure Machine Learning 管道服務會自動協調所有步驟之間嘅依賴。

喺微調 SLM / LLM 嘅過程中，我哋可以透過 Pipeline 管理數據、訓練及生成流程。

![finetuning](../../../../translated_images/finetuning.6559da198851fa523d94d6f0b9f271fa6e1bbac13db0024ebda43cb5348a4633.hk.png)

### **Prompt flow**

使用 Azure Machine Learning prompt flow 嘅好處  
Azure Machine Learning prompt flow 提供多項優勢，幫助用戶由構思到實驗，最終推出生產級基於 LLM 嘅應用：

**Prompt 工程靈活性**

互動式創作體驗：Azure Machine Learning prompt flow 以視覺化方式展示流程結構，方便用戶理解及導航項目。亦提供類似筆記本嘅編碼體驗，提升流程開發及除錯效率。  
Prompt 調校變體：用戶可以建立及比較多個 prompt 變體，促進迭代優化。

評估：內置評估流程使用戶能評估 prompt 及流程嘅質素及效果。

全面資源：Azure Machine Learning prompt flow 包含內置工具庫、範例及模板，為開發提供起點，激發創意並加速流程。

**企業級 LLM 應用準備**

協作：Azure Machine Learning prompt flow 支援團隊協作，讓多個用戶共同參與 prompt 工程項目，分享知識及維護版本控制。

一站式平台：Azure Machine Learning prompt flow 簡化整個 prompt 工程流程，從開發、評估到部署及監控。用戶可輕鬆將流程部署為 Azure Machine Learning 端點，並實時監控表現，確保最佳運行及持續優化。

Azure Machine Learning 企業級準備方案：Prompt flow 利用 Azure Machine Learning 強大嘅企業級方案，提供安全、可擴展及可靠嘅基礎，支持流程嘅開發、實驗及部署。

用 Azure Machine Learning prompt flow，用戶可以釋放 prompt 工程嘅靈活性，有效協作，並利用企業級方案，成功開發及部署基於 LLM 嘅應用。

結合 Azure ML 嘅計算能力、數據及不同組件，企業開發者可以輕鬆建立自己嘅人工智能應用。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件嘅母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。