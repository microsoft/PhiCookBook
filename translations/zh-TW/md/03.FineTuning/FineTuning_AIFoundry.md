# 使用 Microsoft Foundry 微調 Phi-3

讓我們探索如何使用 Microsoft Foundry 微調 Microsoft 的 Phi-3 Mini 語言模型。微調可讓您將 Phi-3 Mini 調整為特定任務，使其更強大且具備上下文感知能力。

## 考量

- **能力：** 哪些模型可以微調？基礎模型可以微調成什麼用途？
- **成本：** 微調的定價模型是什麼？
- **可客製化程度：** 我能修改基礎模型多少？以什麼方式？
- **便利性：** 微調實際如何進行？我需要撰寫自訂程式碼嗎？需要自行準備運算資源嗎？
- **安全性：** 微調模型有已知安全風險嗎？有沒有防護措施避免無意的傷害？

![AIFoundry Models](../../../../translated_images/zh-TW/AIFoundryModels.0e1b16f7d0b09b73.webp)

## 微調準備

### 先決條件

> [!NOTE]
> 對於 Phi-3 系列模型，按使用付費模式的微調服務僅在 **East US 2** 區域建立的集線器可用。

- 一個 Azure 訂閱。如果您還沒有 Azure 訂閱，請建立一個 [付費 Azure 帳戶](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go)。

- 一個 [AI Foundry 專案](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)。
- Microsoft Foundry 使用 Azure 角色型存取控制 (Azure RBAC) 授權操作。執行本指南步驟的使用者帳戶必須在資源群組上被指派 __Azure AI Developer 角色__。

### 訂閱提供者註冊

確認訂閱已註冊 `Microsoft.Network` 資源提供者。

1. 登入 [Azure 入口網站](https://portal.azure.com)。
1. 從左側選單選擇 <strong>訂閱</strong>。
1. 選擇您要使用的訂閱。
1. 從左側選單選擇 **AI 專案設定** > <strong>資源提供者</strong>。
1. 確認清單中有 **Microsoft.Network**，如果沒有，請新增。

### 資料準備

準備您的訓練與驗證資料，以微調您的模型。訓練資料和驗證資料應包括您期望模型執行的輸入與輸出範例。

確保您的所有訓練範例符合推論的預期格式。為有效微調模型，確保資料集平衡且多樣。

這包括維持資料平衡、納入各種情境，並定期優化訓練資料，使其符合真實世界期望，最終達成更準確且平衡的模型回應。

不同型態的模型需不同格式的訓練資料。

### 聊天完成

所使用的訓練與驗證資料<strong>必須</strong>格式為 JSON Lines (JSONL) 檔案。針對 `Phi-3-mini-128k-instruct`，微調資料集必須以 Chat completion API 使用的對話格式呈現。

### 範例檔案格式

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

支援的檔案類型是 JSON Lines。檔案將上傳至預設資料庫並在您的專案中提供。

## 使用 Microsoft Foundry 微調 Phi-3

Microsoft Foundry 讓您可透過微調流程，針對個人資料集定制大型語言模型。微調能大幅提升針對特定任務與應用的客製化與優化效果，進而改善效能、降低成本與延遲，並輸出更貼合需求的結果。

![Finetune AI Foundry](../../../../translated_images/zh-TW/AIFoundryfinetune.193aaddce48d553c.webp)

### 建立新專案

1. 登入 [Microsoft Foundry](https://ai.azure.com)。

1. 選擇 **+New project** 以在 Microsoft Foundry 建立新專案。

    ![FineTuneSelect](../../../../translated_images/zh-TW/select-new-project.cd31c0404088d7a3.webp)

1. 執行以下操作：

    - 專案 <strong>集線器名稱</strong>，必須唯一。
    - 選擇要使用的 <strong>集線器</strong>（如需要，可建立新集線器）。

    ![FineTuneSelect](../../../../translated_images/zh-TW/create-project.ca3b71298b90e420.webp)

1. 執行以下步驟以建立新集線器：

    - 輸入 <strong>集線器名稱</strong>，必須唯一。
    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如需要，可建立新資源群組）。
    - 選擇您想使用的 <strong>地區</strong>。
    - 選擇要連接的 **Azure AI Services**（如需要，可建立新連接）。
    - 選擇 **連接 Azure AI Search** 並選擇 <strong>跳過連接</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-TW/create-hub.49e53d235e80779e.webp)

1. 選擇 **Next**。
1. 選擇 **Create a project**。

### 資料準備

微調前，蒐集或建立與任務相關的資料集，例如聊天指令、問答對，或其他相關文字資料。清理並前處理資料，包含去除雜訊、處理缺失值及標記化文字。

### 在 Microsoft Foundry 微調 Phi-3 模型

> [!NOTE]
> Phi-3 模型微調目前僅支援位於 East US 2 的專案。

1. 從左側分頁選擇 **Model catalog**。

1. 在 <strong>搜尋列</strong> 輸入 *phi-3*，並選取您要使用的 phi-3 模型。

    ![FineTuneSelect](../../../../translated_images/zh-TW/select-model.60ef2d4a6a3cec57.webp)

1. 選擇 **Fine-tune**。

    ![FineTuneSelect](../../../../translated_images/zh-TW/select-finetune.a976213b543dd9d8.webp)

1. 輸入 <strong>微調後的模型名稱</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-TW/finetune1.c2b39463f0d34148.webp)

1. 選擇 **Next**。

1. 執行以下作業：

    - 選擇 <strong>任務類型</strong> 為 **Chat completion**。
    - 選擇您想要使用的 <strong>訓練資料</strong>。您可以透過 Microsoft Foundry 的資料或本地端環境上傳。

    ![FineTuneSelect](../../../../translated_images/zh-TW/finetune2.43cb099b1a94442d.webp)

1. 選擇 **Next**。

1. 上傳您想要使用的 <strong>驗證資料</strong>，或者選擇 <strong>自動切分訓練資料</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-TW/finetune3.fd96121b67dcdd92.webp)

1. 選擇 **Next**。

1. 執行以下操作：

    - 選擇您要使用的 <strong>批次大小乘數</strong>。
    - 選擇您要使用的 <strong>學習率</strong>。
    - 選擇您要使用的 <strong>訓練週期數</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-TW/finetune4.e18b80ffccb5834a.webp)

1. 選擇 **Submit** 開始微調過程。

    ![FineTuneSelect](../../../../translated_images/zh-TW/select-submit.0a3802d581bac271.webp)


1. 模型微調完成後，狀態會顯示為 **Completed**，如下圖所示。您現在可以部署模型，並在自用應用程式、操場或提示流程中使用。詳細資訊，請參閱 [如何使用 Microsoft Foundry 部署 Phi-3 系列小型語言模型](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)。

    ![FineTuneSelect](../../../../translated_images/zh-TW/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> 如需更詳細的 Phi-3 微調資訊，請參考 [在 Microsoft Foundry 微調 Phi-3 模型](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)。

## 清理您的微調模型

您可以從 [Microsoft Foundry](https://ai.azure.com) 的微調模型清單或模型詳細資料頁面刪除微調模型。在微調頁面選擇要刪除的微調模型，然後選擇刪除按鈕。

> [!NOTE]
> 若自訂模型已有部署，無法刪除。您必須先刪除模型部署，才能刪除自訂模型。

## 成本與配額

### Phi-3 模型以服務方式微調的成本與配額考量

Phi 模型以服務方式微調由 Microsoft 提供，並與 Microsoft Foundry 整合使用。您可於部署或微調模型時，參閱部署精靈中「定價與條款」索引標籤的價格資訊。

## 內容過濾

以按使用付費方式部署的服務模型受 Azure AI Content Safety 保護。部署到即時端點時可選擇退出此功能。啟用 Azure AI Content Safety 時，提示詞與完成詞均會通過多種分類模型組合，旨在偵測並防止有害內容輸出。內容過濾系統會偵測並對輸入提示詞與輸出完成詞中可能有害的特定類別內容採取行動。了解更多 [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)。

<strong>微調設定</strong>

定義超參數，如學習率、批次大小及訓練週期數。

<strong>損失函數</strong>

為您的任務選擇合適的損失函數（例如交叉熵）。

<strong>優化器</strong>

選擇優化器（例如 Adam）以進行訓練期間的梯度更新。

<strong>微調流程</strong>

- 載入預訓練模型：載入 Phi-3 Mini 檢查點。
- 新增自訂層：新增任務專用層（例如聊天指令的分類頭）。

<strong>訓練模型</strong>

使用您準備好的資料集微調模型。監控訓練進度並必要時調整超參數。

<strong>評估與驗證</strong>

驗證集：將資料拆分為訓練集與驗證集。

<strong>評估效能</strong>

使用準確率、F1 分數或困惑度等指標評估模型表現。

## 儲存微調模型

<strong>檢查點</strong>

儲存微調後的模型檢查點以供日後使用。

## 部署

- 作為網路服務部署：將微調模型部署為 Microsoft Foundry 中的網路服務。
- 測試端點：傳送測試查詢至部署的端點，以驗證功能。

## 反覆優化與改進

反覆調整：若效能不理想，可透過調整超參數、增加資料或增加訓練週期數進行反覆微調。

## 監控與精進

持續監控模型行為並視需要進行調整。

## 客製化與擴充

自訂任務：Phi-3 Mini 可微調用於聊天指令外的各種任務。探索其他用例！
實驗：嘗試不同架構、層的組合與技術，以提升效能。

> [!NOTE]
> 微調是一個反覆進行的流程。透過實驗、學習並調整模型，為您的特定任務達成最佳成果！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們對因使用此翻譯所產生的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->