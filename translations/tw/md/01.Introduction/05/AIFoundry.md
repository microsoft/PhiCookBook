<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:29:26+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "tw"
}
-->
# **使用 Azure AI Foundry 進行評估**

![aistudo](../../../../../translated_images/AIFoundry.9e0b513e999a1c5aa227e4c7028b5ff9a6cb712e6613c696705445ee4ca8f35d.tw.png)

如何使用 [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 評估您的生成式 AI 應用程式。無論您是在評估單輪還是多輪對話，Azure AI Foundry 都提供了評估模型效能與安全性的工具。

![aistudo](../../../../../translated_images/AIPortfolio.69da59a8e1eaa70f2bab1836c11a69fc97e59f1b1b4154ce5e58bc589d278047.tw.png)

## 如何使用 Azure AI Foundry 評估生成式 AI 應用程式
更多詳細說明請參考 [Azure AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

以下是開始的步驟：

## 在 Azure AI Foundry 中評估生成式 AI 模型

**先決條件**

- 一份 CSV 或 JSON 格式的測試資料集。
- 已部署的生成式 AI 模型（例如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一個具備運算實例的執行環境，用於執行評估。

## 內建評估指標

Azure AI Foundry 支援評估單輪及複雜的多輪對話。
針對 Retrieval Augmented Generation (RAG) 場景，模型基於特定資料，您可以使用內建評估指標來評估效能。
此外，也能評估一般的單輪問答場景（非 RAG）。

## 建立評估執行

從 Azure AI Foundry 介面，前往 Evaluate 頁面或 Prompt Flow 頁面。
依照評估建立精靈設定評估執行，並可選擇為評估命名。
選擇符合您應用目標的場景。
挑選一個或多個評估指標來評估模型輸出。

## 自訂評估流程（選用）

若需更高彈性，您可以建立自訂評估流程，根據您的需求調整評估過程。

## 查看結果

執行評估後，您可以在 Azure AI Foundry 中記錄、查看並分析詳細的評估指標，深入了解應用的能力與限制。

**Note** Azure AI Foundry 目前處於公開預覽階段，建議用於實驗和開發用途。若用於正式生產工作負載，請考慮其他方案。更多細節與操作步驟，請參考官方 [AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。