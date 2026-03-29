# 使用 Microsoft Foundry 微調 Phi-3

讓我們探索如何使用 Microsoft Foundry 微調 Microsoft 的 Phi-3 Mini 語言模型。微調允許你針對特定任務調整 Phi-3 Mini，令它變得更強大且更具上下文感知能力。

## 注意事項

- <strong>能力：</strong>哪些模型可進行微調？基礎模型可以被微調來完成什麼？
- <strong>成本：</strong>微調的定價模式是什麼？
- <strong>可定制性：</strong>我能多大程度修改基礎模型——以及以什麼方式修改？
- <strong>便利性：</strong>微調實際怎麼進行——我需要編寫自訂代碼嗎？需要帶來自己的運算資源嗎？
- <strong>安全性：</strong>微調後的模型存在安全風險——是否有防護機制防止意外傷害？

![AIFoundry Models](../../../../translated_images/zh-HK/AIFoundryModels.0e1b16f7d0b09b73.webp)

## 微調準備

### 先決條件

> [!NOTE]
> 對於 Phi-3 系列模型，付費即用的微調服務僅支援位於 **East US 2** 地區創建的集線器。

- 一個 Azure 訂閱。如果你沒有 Azure 訂閱，請建立一個[付費 Azure 帳戶](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go)開始。

- 一個 [AI Foundry 專案](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)。
- Microsoft Foundry 中使用 Azure 基於角色的存取控制 (Azure RBAC) 來授權操作。要進行本文的步驟，您的使用者帳戶必須在資源組上被指派為 __Azure AI Developer 角色__。

### 訂閱提供者註冊

確認訂閱已註冊 `Microsoft.Network` 資源提供者。

1. 登入 [Azure 入口網站](https://portal.azure.com)。
1. 從左側選單選擇 <strong>訂閱</strong>。
1. 選擇你想使用的訂閱。
1. 從左側選單選擇 **AI 專案設定** > <strong>資源提供者</strong>。
1. 確認列表中有 **Microsoft.Network**。否則請新增它。

### 數據準備

準備你的訓練和驗證數據來微調你的模型。你的訓練數據和驗證數據集應包含希望模型完成的輸入和輸出範例。

確保所有訓練範例均符合推論的預期格式。為有效微調模型，請確保數據集平衡且多樣化。

這包括維持數據平衡，包含各種場景，以及定期優化訓練資料以與現實世界期望對齊，最終產生更精確且平衡的模型回應。

不同模型類型需要不同格式的訓練數據。

### 聊天完成

你使用的訓練和驗證數據<strong>必須</strong>格式為 JSON Lines (JSONL) 文檔。對於 `Phi-3-mini-128k-instruct`，微調數據集必須採用由 Chat completions API 使用的對話格式。

### 示例檔案格式

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

支援的檔案類型是 JSON Lines。檔案會上傳到預設的資料存儲並在你的專案中可用。

## 使用 Microsoft Foundry 微調 Phi-3

Microsoft Foundry 允許你通過稱為微調的流程，將大型語言模型客製化為你的個人數據集。微調具有重大價值，能針對特定任務和應用進行定制和優化，帶來更佳表現、成本效率、降低延遲及客製化輸出。

![Finetune AI Foundry](../../../../translated_images/zh-HK/AIFoundryfinetune.193aaddce48d553c.webp)

### 建立新專案

1. 登入 [Microsoft Foundry](https://ai.azure.com)。

1. 選擇 **+New project** 以在 Microsoft Foundry 中建立新專案。

    ![FineTuneSelect](../../../../translated_images/zh-HK/select-new-project.cd31c0404088d7a3.webp)

1. 執行以下任務：

    - 專案 **Hub name**。必須是唯一值。
    - 選擇要使用的 **Hub**（如果需要，請新建）。

    ![FineTuneSelect](../../../../translated_images/zh-HK/create-project.ca3b71298b90e420.webp)

1. 執行以下任務以建立新集線器（Hub）：

    - 輸入 **Hub name**。必須是唯一值。
    - 選擇你的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源組</strong>（如果需要，請新建）。
    - 選擇你想使用的 <strong>位置</strong>。
    - 選擇<strong>連接 Azure AI 服務</strong>（需要可新建）。
    - 選擇 **連接 Azure AI 搜索** 為 <strong>跳過連接</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-HK/create-hub.49e53d235e80779e.webp)

1. 選取 <strong>下一步</strong>。
1. 選取 <strong>建立專案</strong>。

### 數據準備

微調前，收集或建立與你的任務相關的資料集，例如聊天指令、問答對或其他相關文字資料。清理並預處理資料，包括去除雜訊、處理缺失值以及文字斷詞。

### 在 Microsoft Foundry 微調 Phi-3 模型

> [!NOTE]
> Phi-3 模型的微調目前僅支援位於 East US 2 的專案。

1. 從左側標籤選擇 <strong>模型目錄</strong>。

1. 在 <strong>搜尋欄</strong> 輸入 *phi-3* 選擇你想使用的 phi-3 模型。

    ![FineTuneSelect](../../../../translated_images/zh-HK/select-model.60ef2d4a6a3cec57.webp)

1. 選擇 <strong>微調</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-HK/select-finetune.a976213b543dd9d8.webp)

1. 輸入 <strong>微調模型名稱</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-HK/finetune1.c2b39463f0d34148.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行以下任務：

    - 選擇 <strong>任務類型</strong> 至 <strong>聊天完成</strong>。
    - 選擇你想使用的 <strong>訓練數據</strong>。可以透過 Microsoft Foundry 上傳資料，或從本機環境導入。

    ![FineTuneSelect](../../../../translated_images/zh-HK/finetune2.43cb099b1a94442d.webp)

1. 選擇 <strong>下一步</strong>。

1. 上傳你想使用的 <strong>驗證數據</strong>，或選擇 <strong>自動拆分訓練數據</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-HK/finetune3.fd96121b67dcdd92.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行以下任務：

    - 選擇你想使用的 <strong>批次大小倍數</strong>。
    - 選擇你想使用的 <strong>學習率</strong>。
    - 選擇你想使用的 <strong>訓練輪數</strong>。

    ![FineTuneSelect](../../../../translated_images/zh-HK/finetune4.e18b80ffccb5834a.webp)

1. 選擇 <strong>提交</strong> 開始微調程序。

    ![FineTuneSelect](../../../../translated_images/zh-HK/select-submit.0a3802d581bac271.webp)


1. 一旦你的模型微調完成，狀態會顯示為 <strong>已完成</strong>，如下圖所示。現在你可以部署模型，並在你自己的應用程式、遊樂場或提示流程中使用它。詳情請參閱[如何使用 Microsoft Foundry 部署 Phi-3 系列小型語言模型](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)。

    ![FineTuneSelect](../../../../translated_images/zh-HK/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> 有關 Phi-3 微調的更詳細資訊，請參閱[在 Microsoft Foundry 中微調 Phi-3 模型](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)。

## 清理你的微調模型

你可以從 [Microsoft Foundry](https://ai.azure.com) 的微調模型列表或模型詳細頁刪除微調模型。在微調頁面選擇欲刪除的微調模型，再選擇刪除按鈕以刪除該微調模型。

> [!NOTE]
> 若自訂模型已有部署，則不能刪除。必須先刪除模型部署，才能刪除自訂模型。

## 成本與配額

### Phi-3 模型作為服務微調的成本與配額考量

Phi 系列模型作為服務進行微調，由 Microsoft 提供並整合在 Microsoft Foundry 中使用。你可以在[部署](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)或微調模型時，在部署精靈的「定價及條款」標籤頁中查詢價格。

## 內容過濾

作為付費即用服務部署的模型受到 Azure AI 內容安全保護。部署至即時端點時，你可選擇退出此功能。啟用 Azure AI 內容安全後，提示和生成回答皆會通過一組分類模型，用於偵測和阻止有害內容輸出。內容過濾系統會偵測並對輸入提示和輸出完成中具潛在危害的特定類別內容採取行動。詳情請參閱[Azure AI 內容安全](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)。

<strong>微調配置</strong>

定義如學習率、批次大小及訓練迭代次數等超參數。

<strong>損失函數</strong>

根據任務選擇適合的損失函數（例如交叉熵）。

<strong>優化器</strong>

選擇優化器（例如 Adam）以更新訓練時的梯度。

<strong>微調過程</strong>

- 載入預訓練模型：載入 Phi-3 Mini 檢查點。
- 增加自訂層：添加特定任務的層（如聊天指令分類頭）。

<strong>訓練模型</strong>
使用準備好的資料集對模型進行微調。監控訓練進度並根據需要調整超參數。

<strong>評估與驗證</strong>

驗證集：將資料拆分為訓練和驗證集。

<strong>效能評估</strong>

使用準確率、F1 分數或困惑度等衡量指標評估模型效能。

## 保存微調模型

<strong>檢查點</strong>
保存微調後的模型檢查點以備未來使用。

## 部署

- 作為網路服務部署：在 Microsoft Foundry 部署你的微調模型作為網路服務。
- 測試端點：向已部署端點送出測試詢問以驗證功能。

## 迭代和改進

反覆調整：若效能不理想，透過調整超參數、新增資料或增加訓練輪數迭代改進。

## 監控和優化

持續監控模型表現並視需要進行優化。

## 自訂與擴展

自訂任務：Phi-3 Mini 可針對多種任務進行微調，超越聊天指令。探索其他應用範例！
實驗嘗試：嘗試不同架構、層組合與技巧以提升性能。

> [!NOTE]
> 微調是一個反覆的過程。實驗、學習並調整你的模型以達成特定任務的最佳效果！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於保持準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。如需關鍵資訊，建議聘請專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->