# **使用 Microsoft Foundry 作評估**

![aistudo](../../../../../translated_images/zh-HK/AIFoundry.9e0b513e999a1c5a.webp)

如何使用 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 評估你的生成式 AI 應用。無論你是在評估單輪還是多輪對話，Microsoft Foundry 都提供用於評估模型表現及安全性的工具。

![aistudo](../../../../../translated_images/zh-HK/AIPortfolio.69da59a8e1eaa70f.webp)

## 如何使用 Microsoft Foundry 評估生成式 AI 應用
有關詳細說明，請參閱 [Microsoft Foundry 文件](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

以下是開始步驟：

## 在 Microsoft Foundry 中評估生成式 AI 模型

<strong>先決條件</strong>

- 一個 CSV 或 JSON 格式的測試資料集。
- 一個已部署的生成式 AI 模型（如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一個可運行評估的運算實例。

## 內建評估指標

Microsoft Foundry 可評估單輪及複雜的多輪對話。  
針對檢索增強生成（RAG）場景，模型基於特定資料，你可以使用內建評估指標來評估表現。  
此外，你也可以評估一般的單輪問答場景（非 RAG）。

## 建立評估執行

從 Microsoft Foundry UI，前往 Evaluate 頁面或 Prompt Flow 頁面。  
依照評估建立精靈設定評估執行。可為評估提供選填的名稱。  
選擇符合應用目標的場景。  
選擇一個或多個評估指標來評估模型輸出。

## 自訂評估流程（可選）

若需更大彈性，你可以建立自訂評估流程。根據具體需求自訂評估過程。

## 查看結果

執行評估後，在 Microsoft Foundry 中記錄、查看及分析詳細評估指標。獲取應用程式能力與限制的見解。



<strong>注意</strong> Microsoft Foundry 目前為公開預覽，請用於實驗和開發用途。針對生產工作負載，請考慮其他方案。  
探索官方的 [AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) 以了解更多細節及分步說明。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威資料來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->