# 使用 Microsoft Foundry 微調 Phi-3

讓我們探索如何使用 Microsoft Foundry 微調 Microsoft 的 Phi-3 Mini 語言模型。微調可讓您將 Phi-3 Mini 適應於特定任務，使其更強大且更具上下文感知能力。

## 注意事項

- **能力：** 哪些模型可以微調？基礎模型可以微調至什麼功能？
- **成本：** 微調的定價模式是什麼？
- **可定制性：** 我能在多大程度上修改基礎模型 — 以及以哪些方式？
- **便利性：** 微調實際如何進行 — 我需要撰寫自訂程式碼嗎？我需要自備運算資源嗎？
- **安全性：** 微調後的模型存在安全風險 — 是否有任何防護措施以避免意外傷害？

![AIFoundry Models](../../../../translated_images/zh-MO/AIFoundryModels.0e1b16f7d0b09b73.webp)

## 微調準備

### 前置條件

> [!NOTE]
> 對於 Phi-3 系列模型，即用即付（pay-as-you-go）模式的微調服務僅在 **East US 2** 區域所建立的 hubs 可用。

- 一個 Azure 訂閱。如果尚未擁有 Azure 訂閱，請建立一個[付費 Azure 帳戶](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go)。

- 一個 [AI Foundry 專案](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)。
- Microsoft Foundry 使用 Azure 角色型存取控制 (Azure RBAC) 來授權操作。您必須被指派在資源群組上的 __Azure AI Developer 角色__，才能執行本文中的步驟。

### 訂閱提供者註冊

確認訂閱已向 `Microsoft.Network` 雲端資源提供者登記。

1. 登入 [Azure 入口網站](https://portal.azure.com)。
1. 從左側選單選擇 <strong>訂閱</strong>。
1. 選擇您要使用的訂閱。
1. 從左側選單選擇 **AI 專案設定** > <strong>資源提供者</strong>。
1. 確認列表中有 **Microsoft.Network**，若無請新增。

### 資料準備

準備訓練及驗證資料以微調您的模型。訓練資料與驗證資料包含模型執行方式的輸入與輸出範例。

確保所有訓練範例皆符合推論期望格式。為有效微調模型，請使用平衡且多樣的資料集。

這涉及資料平衡維護、涵蓋多種場景，並周期性調整訓練資料以符合真實世界預期，最終達成更準確且均衡的模型回答。

不同類型的模型需要不同格式的訓練資料。

### Chat Completion

您使用的訓練與驗證資料<strong>必須</strong>是 JSON Lines (JSONL) 格式文件。對於 `Phi-3-mini-128k-instruct`，微調資料集必須使用 Chat 完成 API 採用的對話格式。

### 範例文件格式

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

支援的檔案類型是 JSON Lines。檔案會上傳至預設資料存放區，並於您的專案中可供使用。

## 使用 Microsoft Foundry 微調 Phi-3

Microsoft Foundry 讓您可通過微調程序，自訂大型語言模型以符合個人資料集。微調提供重大價值，能為特定任務和應用實現定制化和優化，提升效能、降低成本和延遲，並產生量身打造的輸出。

![Finetune AI Foundry](../../../../translated_images/zh-MO/AIFoundryfinetune.193aaddce48d553c.webp)

### 建立新專案

1. 登入 [Microsoft Foundry](https://ai.azure.com)。
1. 選擇 **+New project** 來建立新的 Microsoft Foundry 專案。

    ![FineTuneSelect](../../../../translated_images/zh-MO/select-new-project.cd31c0404088d7a3.webp)

1. 執行以下操作：

    - 專案 **Hub 名稱**，需為唯一值。
    - 選擇使用的 **Hub**（如需可建立新 hub）。

    ![FineTuneSelect](../../../../translated_images/zh-MO/create-project.ca3b71298b90e420.webp)

1. 執行以下操作以建立新 hub：

    - 輸入 **Hub 名稱**，需為唯一值。
    - 選擇 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如需可建立新群組）。
    - 選擇您想使用的 <strong>地點</strong>。
    - 選擇 **連接 Azure AI 服務**（如需可建立新服務）。
    - 選擇 **連接 Azure AI 搜尋** 並選擇 <strong>略過連結</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-MO/create-hub.49e53d235e80779e.webp)

1. 選擇 <strong>下一步</strong>。
1. 選擇 <strong>建立專案</strong>。

### 資料準備

微調前，收集或建立與您任務相關的資料集，例如聊天指令、問答對或其他相關文本資料。清理及預處理資料，移除噪音、處理缺失值並標記文本。

### 在 Microsoft Foundry 微調 Phi-3 模型

> [!NOTE]
> Phi-3 模型微調目前僅支持於 East US 2 地區的專案中使用。

1. 從左側分頁選擇 <strong>模型目錄</strong>。
1. 在 <strong>搜尋列</strong> 輸入 *phi-3*，然後選擇您想使用的 phi-3 模型。

    ![FineTuneSelect](../../../../translated_images/zh-MO/select-model.60ef2d4a6a3cec57.webp)

1. 選擇 <strong>微調</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-MO/select-finetune.a976213b543dd9d8.webp)

1. 輸入 <strong>微調後的模型名稱</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-MO/finetune1.c2b39463f0d34148.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行以下操作：

    - 選擇 <strong>任務類型</strong> 為 <strong>聊天補全</strong>。
    - 選擇您要使用的 <strong>訓練資料</strong>。可透過 Microsoft Foundry 的資料或本機環境上傳。

    ![FineTuneSelect](../../../../translated_images/zh-MO/finetune2.43cb099b1a94442d.webp)

1. 選擇 <strong>下一步</strong>。

1. 上傳您要使用的 <strong>驗證資料</strong>，或者選擇 <strong>自動拆分訓練資料</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-MO/finetune3.fd96121b67dcdd92.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行以下操作：

    - 選擇您想使用的 <strong>批次大小乘數</strong>。
    - 選擇您想使用的 <strong>學習率</strong>。
    - 選擇您想使用的 <strong>訓練周期</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-MO/finetune4.e18b80ffccb5834a.webp)

1. 選擇 <strong>提交</strong> 開始微調程序。

    ![FineTuneSelect](../../../../translated_images/zh-MO/select-submit.0a3802d581bac271.webp)

1. 適當微調完成後，狀態會顯示為 <strong>已完成</strong>，如以下圖片所示。您現在可以部署此模型，並在您的應用程式、遊樂場或提示流程中使用。更多資訊請參考 [如何使用 Microsoft Foundry 部署 Phi-3 系列小型語言模型](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)。

    ![FineTuneSelect](../../../../translated_images/zh-MO/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> 有關 Phi-3 微調的詳細資訊，請造訪 [在 Microsoft Foundry 微調 Phi-3 模型](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)。

## 清理您的微調模型

您可以從 [Microsoft Foundry](https://ai.azure.com) 的微調模型清單或模型詳細頁刪除微調模型。在「微調」頁面中選擇欲刪除的微調模型，然後選擇刪除按鈕以刪除該模型。

> [!NOTE]
> 如果自訂模型有已存在的部署，您無法刪除該模型。必須先刪除模型部署，才可刪除自訂模型。

## 成本與配額

### Phi-3 服務化微調模型的成本與配額考量

Phi 模型以服務化方式由 Microsoft 提供並整合至 Microsoft Foundry。您可以在[部署](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)或微調模型時，在部署嚮導的「價格與條款」頁籤中找到定價資訊。

## 內容過濾

以即用即付模式服務化部署的模型受到 Azure AI 內容安全保護。部署到即時端點時，您可選擇關閉此功能。啟用 Azure AI 內容安全後，提示詞與完成結果都會通過分類模型組合，偵測並阻止可能有害內容的產出。內容過濾系統會偵測並處理輸入提示詞與輸出完成中某些特定類別的潛在有害內容。閱讀更多 [Azure AI 內容安全](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)。

<strong>微調配置</strong>

超參數：定義學習率、批次大小及訓練周期數等超參數。

<strong>損失函數</strong>

選擇適用於任務的損失函數（例如，交叉熵）。

<strong>優化器</strong>

選擇優化器（例如 Adam）以於訓練期間更新梯度。

<strong>微調流程</strong>

- 載入預訓練模型：載入 Phi-3 Mini 的檢查點。
- 新增自訂層：新增任務專用層（例如用於聊天指令的分類頭）。

<strong>訓練模型</strong>  
使用您準備的資料集微調模型，監控訓練進度並根據需要調整超參數。

<strong>評估與驗證</strong>

驗證集：將資料拆分為訓練集與驗證集。

<strong>評估效能</strong>

使用準確率、F1 分數或困惑度等指標評估模型效能。

## 保存微調模型

<strong>檢查點</strong>  
保存微調後的模型檢查點以供未來使用。

## 部署

- 作為 Web 服務部署：將微調模型部署為 Microsoft Foundry 的 Web 服務。
- 測試端點：送出測試查詢以驗證端點功能。

## 反覆優化

反覆調整：若性能不佳，可透過調整超參數、增添資料或延長微調周期來反覆優化。

## 監控與調整

持續監控模型行為，並根據需要進行調整。

## 客製與擴展

自定任務：Phi-3 Mini 可微調用於聊天指令以外的各種任務，探索更多用例吧！  
實驗探索：嘗試不同架構、層組合與技術以提升效能。

> [!NOTE]
> 微調是一個反覆的過程。持續實驗、學習並調整您的模型，以達成特定任務的最佳成果！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
此文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用本翻譯而產生的任何誤解或誤譯，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->