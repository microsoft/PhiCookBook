# **使用 Microsoft Foundry 進行評估**

![aistudo](../../../../../translated_images/zh-TW/AIFoundry.9e0b513e999a1c5a.webp)

如何使用 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 評估您的生成式 AI 應用。不管您是在評估單輪還是多輪對話，Microsoft Foundry 提供了評估模型表現和安全性的工具。

![aistudo](../../../../../translated_images/zh-TW/AIPortfolio.69da59a8e1eaa70f.webp)

## 如何使用 Microsoft Foundry 評估生成式 AI 應用
更多詳細說明請參考 [Microsoft Foundry 文件](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

以下是開始的步驟：

## 在 Microsoft Foundry 中評估生成式 AI 模型

<strong>先決條件</strong>

- 以 CSV 或 JSON 格式的測試資料集。
- 已部署的生成式 AI 模型（例如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 可運行評估的計算實例運行時環境。

## 內建評估指標

Microsoft Foundry 支援評估單輪及複雜多輪對話。
在檢索增強生成（RAG）場景中，模型基於特定資料，可以使用內建評估指標來衡量表現。
另外，也能評估一般的單輪問答場景（非 RAG）。

## 建立評估執行

從 Microsoft Foundry 介面，前往 Evaluate 頁面或 Prompt Flow 頁面。
跟隨評估建立導引設定評估執行。可為您的評估提供選填名稱。
選擇與應用目標相符的場景。
選擇一個或多個評估指標以評估模型輸出。

## 自訂評估流程（選用）

若需要更高彈性，可建立自訂評估流程。依您的需求自訂評估執行程序。

## 查看結果

評估執行完成後，在 Microsoft Foundry 中記錄、查看並分析詳細評估指標。深入了解您的應用能力與限制。

<strong>注意</strong> Microsoft Foundry 目前處於公開預覽階段，因此建議用於實驗與開發用途。生產環境工作負載請考慮其他方案。詳情和逐步說明請參考官方 [AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言文件應視為權威來源。對於重要資訊，建議聘請專業人工翻譯。對於因使用本翻譯而產生的任何誤解或誤譯，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->