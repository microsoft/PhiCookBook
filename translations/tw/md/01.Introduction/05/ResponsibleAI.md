<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "805b96b20152936d8f4c587d90d6e06e",
  "translation_date": "2025-07-16T22:49:10+00:00",
  "source_file": "md/01.Introduction/05/ResponsibleAI.md",
  "language_code": "tw"
}
-->
# **介紹負責任的 AI**

[Microsoft Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=aiml-138114-kinfeylo) 是一項旨在協助開發者和組織打造透明、值得信賴且具問責性的 AI 系統的計畫。該計畫提供指導和資源，幫助開發符合隱私、公平性和透明度等倫理原則的負責任 AI 解決方案。我們也將探討建構負責任 AI 系統時所面臨的挑戰與最佳實踐。

## Microsoft Responsible AI 概覽

![RAIPrinciples](../../../../../translated_images/tw/RAIPrinciples.bf9c9bc6ca160d33.png)

**倫理原則**

Microsoft Responsible AI 以一套倫理原則為指導，包括隱私、公平性、透明度、問責性與安全性。這些原則旨在確保 AI 系統的開發符合道德且負責任的標準。

**透明的 AI**

Microsoft Responsible AI 強調 AI 系統透明度的重要性，包含清楚說明 AI 模型的運作方式，並確保資料來源與演算法公開可查。

**具問責性的 AI**

[Microsoft Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=aiml-138114-kinfeylo) 推動開發具問責性的 AI 系統，能夠提供 AI 模型決策過程的洞見，幫助使用者理解並信任 AI 系統的輸出結果。

**包容性**

AI 系統應設計為惠及所有人。Microsoft 致力打造包容性的 AI，考量多元觀點，避免偏見或歧視。

**可靠性與安全性**

確保 AI 系統的可靠性與安全性至關重要。Microsoft 專注於建構穩健的模型，確保其表現穩定且避免造成有害後果。

**AI 的公平性**

Microsoft Responsible AI 認識到若 AI 系統訓練於有偏見的資料或演算法，可能會延續偏見。該計畫提供指導，協助開發不因種族、性別或年齡等因素而歧視的公平 AI 系統。

**隱私與安全**

Microsoft Responsible AI 強調保護使用者隱私與資料安全的重要性，包含實施強化的資料加密與存取控制，並定期審核 AI 系統的安全漏洞。

**問責與責任**

Microsoft Responsible AI 推動 AI 開發與部署過程中的問責與責任，確保開發者與組織了解 AI 系統潛在風險，並採取措施降低這些風險。

## 建立負責任 AI 系統的最佳實踐

**使用多元資料集開發 AI 模型**

為避免 AI 系統產生偏見，重要的是使用能代表多元觀點與經驗的多元資料集。

**採用可解釋的 AI 技術**

可解釋的 AI 技術能幫助使用者理解 AI 模型的決策過程，提升對系統的信任度。

**定期審核 AI 系統的安全漏洞**

定期審核 AI 系統有助於發現需解決的潛在風險與漏洞。

**實施強化的資料加密與存取控制**

資料加密與存取控制能有效保護 AI 系統中的使用者隱私與安全。

**遵循 AI 開發的倫理原則**

遵守公平、透明與問責等倫理原則，有助於建立對 AI 系統的信任，並確保其負責任地開發。

## 使用 AI Foundry 推動負責任 AI

[Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 是一個強大的平台，讓開發者和組織能快速打造智能、先進、市場就緒且負責任的應用程式。以下是 Azure AI Foundry 的一些主要功能與特色：

**現成的 API 與模型**

Azure AI Foundry 提供預建且可自訂的 API 與模型，涵蓋多種 AI 任務，包括生成式 AI、對話式自然語言處理、搜尋、監控、翻譯、語音、視覺與決策等。

**Prompt Flow**

Azure AI Foundry 的 Prompt Flow 讓您能創建對話式 AI 體驗，設計並管理對話流程，輕鬆打造聊天機器人、虛擬助理及其他互動應用。

**檢索增強生成（RAG）**

RAG 是結合檢索式與生成式方法的技術，透過同時利用既有知識（檢索）與創造性生成（生成），提升回應品質。

**生成式 AI 的評估與監控指標**

Azure AI Foundry 提供評估與監控生成式 AI 模型的工具，能評估其效能、公平性及其他重要指標，確保負責任的部署。此外，若您已建立儀表板，可使用 Azure Machine Learning Studio 的無程式碼介面，根據 [Repsonsible AI Toolbox](https://responsibleaitoolbox.ai/?WT.mc_id=aiml-138114-kinfeylo) Python 函式庫自訂並產生負責任 AI 儀表板及相關評分卡。此評分卡有助於與技術及非技術利害關係人分享公平性、特徵重要性及其他負責任部署的關鍵洞見。

使用 AI Foundry 推動負責任 AI 時，可遵循以下最佳實踐：

**明確定義 AI 系統的問題與目標**

在開發前，清楚定義 AI 系統欲解決的問題或目標，有助於識別所需的資料、演算法與資源，打造有效模型。

**收集並預處理相關資料**

訓練 AI 系統所用資料的品質與數量，對其效能有重大影響。因此，需收集相關資料，進行清理與預處理，並確保資料能代表目標族群或問題。

**選擇適當的評估方法**

市面上有多種評估演算法，需根據資料與問題選擇最合適的演算法。

**評估並解釋模型**

建立 AI 模型後，應使用適當指標評估其效能，並以透明方式解釋結果，協助識別模型中的偏見或限制，並在必要時進行改進。

**確保透明度與可解釋性**

AI 系統應具備透明與可解釋性，讓使用者了解其運作原理及決策過程。這對於對人類生活有重大影響的應用（如醫療、金融及法律系統）尤其重要。

**持續監控並更新模型**

AI 系統需持續監控與更新，確保其長期保持準確與有效，這需要持續的維護、測試與再訓練。

總結來說，Microsoft Responsible AI 是一項協助開發者與組織打造透明、值得信賴且具問責性 AI 系統的計畫。負責任的 AI 實踐至關重要，而 Azure AI Foundry 致力於讓組織能實際落實。透過遵循倫理原則與最佳實踐，我們能確保 AI 系統以負責任的方式開發與部署，造福整個社會。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。