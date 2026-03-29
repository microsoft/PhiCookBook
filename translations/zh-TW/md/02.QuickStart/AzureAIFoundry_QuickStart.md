# **在 Microsoft Foundry 使用 Phi-3**

隨著生成式 AI 的發展，我們希望使用統一平台來管理不同的 LLM 和 SLM、企業數據整合、微調/RAG 操作，以及整合 LLM 和 SLM 後對不同企業業務的評估等，讓生成式 AI 更好地實現智慧應用。[Microsoft Foundry](https://ai.azure.com) 是一個企業級的生成式 AI 應用平台。

![aistudo](../../../../translated_images/zh-TW/aifoundry_home.f28a8127c96c7d93.webp)

透過 Microsoft Foundry，你可以評估大型語言模型（LLM）的回應，並用 prompt flow 編排提示應用元件，以提升效能。該平台支援從概念驗證輕鬆轉換為完整生產的可擴展性。持續監控與精進，支援長期成功。

我們可以透過簡單步驟快速在 Microsoft Foundry 部署 Phi-3 模型，接著使用 Microsoft Foundry 完成 Phi-3 相關的 Playground/Chat、微調、評估及其他相關工作。

## **1. 準備工作**

如果你已經在電腦上安裝了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)，使用此範本只需在一個新目錄中執行這個指令。

## 手動建立

創建一個 Microsoft Foundry 項目和中心是組織和管理你的 AI 工作的好方式。以下是開始的逐步指南：

### 在 Microsoft Foundry 建立項目

1. **前往 Microsoft Foundry**：登入 Microsoft Foundry 入口網站。
2. <strong>建立項目</strong>：
   - 如果你身處某個項目，點選頁面左上角的「Microsoft Foundry」回到首頁。
   - 選擇「+ Create project」。
   - 輸入項目名稱。
   - 如果你已有中心，它將是預設被選擇。若你擁有多個中心存取權，可以從下拉選單選擇不同中心。若想建立新中心，選擇「Create new hub」並輸入名稱。
   - 點選「Create」。

### 在 Microsoft Foundry 建立中心

1. **前往 Microsoft Foundry**：使用你的 Azure 帳號登入。
2. <strong>建立中心</strong>：
   - 從左側選單選擇管理中心。
   - 選擇「所有資源」，接著點選「+ 新專案」旁的下拉箭頭選擇「+ 新中心」。
   - 在「建立新中心」對話框中，輸入中心名稱（例如 contoso-hub）並根據需求修改其他欄位。
   - 選擇「下一步」，檢查資訊，然後選擇「建立」。

更多詳細說明，可參考官方 [Microsoft 文件](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)。

建立成功後，可透過 [ai.azure.com](https://ai.azure.com/) 進入你建立的工作室。

一個 AI Foundry 可以有多個項目。在 AI Foundry 建立一個項目來準備。

建立 Microsoft Foundry [快速入門](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. 在 Microsoft Foundry 部署 Phi 模型**

點選項目中的 Explore 選項，進入模型目錄並選擇 Phi-3。

選擇 Phi-3-mini-4k-instruct。

點擊「Deploy」部署 Phi-3-mini-4k-instruct 模型。

> [!NOTE]
>
> 部署時可選擇運算資源。

## **3. 在 Microsoft Foundry 的 Playground 與 Phi 聊天**

前往部署頁面，選擇 Playground，與 Microsoft Foundry 的 Phi-3 進行聊天。

## **4. 從 Microsoft Foundry 部署模型**

若想從 Azure 模型目錄部署模型，可以依照以下步驟：

- 登入 Microsoft Foundry。
- 從 Microsoft Foundry 模型目錄中選擇想要部署的模型。
- 在模型詳細頁面選擇「Deploy」，接著選擇「無伺服器 API 並含 Azure AI 內容安全」。
- 選擇想部署模型的項目。要使用無伺服器 API，工作區必須屬於 East US 2 或 Sweden Central 區域。你也可以自訂部署名稱。
- 在部署嚮導中，選擇定價與條款，以了解相關價格和使用條款。
- 選擇「Deploy」。等待部署完成並跳轉到部署頁面。
- 選擇「Open in playground」來開始與模型互動。
- 你可以返回部署頁面，選擇該部署並記下終端的目標 URL 及 Secret Key，用來呼叫部署並產生回應。
- 你隨時可以在「Build」標籤下，從「元件」區域選擇「Deployments」，找到終端詳細資訊、URL 和存取金鑰。

> [!NOTE]
> 請注意，執行這些操作的帳號必須對資源群組擁有 Azure AI Developer 角色權限。

## **5. 在 Microsoft Foundry 使用 Phi API**

你可以透過 Postman 透過 GET 存取 https://{Your project name}.region.inference.ml.azure.com/swagger.json，結合金鑰來瞭解提供的介面。

你可以非常方便地獲取請求參數以及回應參數。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->