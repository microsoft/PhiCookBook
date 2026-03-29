# **使用 Microsoft Foundry 進行評估**

![aistudo](../../../../../translated_images/zh-MO/AIFoundry.9e0b513e999a1c5a.webp)

如何使用 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 評估您的生成式 AI 應用程式。無論您是在評估單輪還是多輪對話，Microsoft Foundry 都提供工具來評估模型的性能及安全性。

![aistudo](../../../../../translated_images/zh-MO/AIPortfolio.69da59a8e1eaa70f.webp)

## 如何使用 Microsoft Foundry 評估生成式 AI 應用程式
更多詳細指引請參考 [Microsoft Foundry 文件](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

以下是開始使用的步驟：

## 在 Microsoft Foundry 評估生成式 AI 模型

<strong>先決條件</strong>

- 以 CSV 或 JSON 格式的測試資料集。
- 已部署的生成式 AI 模型（例如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一個可執行評估的運行時與計算實例。

## 內建的評估指標

Microsoft Foundry 允許您評估單輪及複雜多輪對話。
對於基於特定資料的檢索增強生成（RAG）場景，您可以使用內建評估指標來評估性能。
此外，您還可評估一般的單輪問答場景（非 RAG）。

## 建立評估執行

在 Microsoft Foundry 使用介面中，前往 Evaluate 頁面或 Prompt Flow 頁面。
按照評估建立精靈設定評估執行，並可為您的評估設定可選名稱。
選擇與您應用程式目標對應的場景。
選擇一個或多個評估指標來評估模型輸出。

## 自訂評估流程（可選）

為了更大彈性，您可建立自訂評估流程。依據您的具體需求自訂評估過程。

## 查看結果

執行評估後，在 Microsoft Foundry 中記錄、查看及分析詳細的評估指標，深入了解您的應用程式能力與限制。



**Note** Microsoft Foundry 目前處於公開預覽階段，請用於試驗及開發。至於生產工作負載，建議使用其他選項。欲獲更多詳細資訊及逐步指南，請參考官方 [AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。儘管我們致力於確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。文件原文應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->