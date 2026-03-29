# **在 Microsoft Foundry 使用 Phi-3**

隨著生成式 AI 的發展，我們希望使用統一的平台來管理不同的 LLM 和 SLM、企業數據整合、微調/RAG 操作，以及整合 LLM 和 SLM 後對不同企業業務的評估等，從而更好地實現生成式 AI 的智慧應用。[Microsoft Foundry](https://ai.azure.com) 是一個企業級的生成式 AI 應用平台。

![aistudo](../../../../translated_images/zh-HK/aifoundry_home.f28a8127c96c7d93.webp)

借助 Microsoft Foundry，您可以評估大型語言模型（LLM）的回應，並使用 prompt flow 編排提示應用組件，以獲得更佳的性能。該平台促進擴展性，輕鬆將概念驗證轉化為成熟的生產環境。持續監控和優化支持長期成功。

我們可以通過簡單的步驟，快速在 Microsoft Foundry 上部署 Phi-3 模型，然後使用 Microsoft Foundry 完成與 Phi-3 相關的 Playground/Chat、微調、評估等相關工作。

## **1. 準備**

如果您已經在您的機器上安裝了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)，使用此範本只需在新目錄下運行此命令即可。

## 手動創建

創建 Microsoft Foundry 項目和中樞是組織和管理您 AI 工作的好方法。以下是入門的逐步指南：

### 在 Microsoft Foundry 創建項目

1. **前往 Microsoft Foundry**：登錄 Microsoft Foundry 入口網站。
2. <strong>創建項目</strong>：
   - 如果您已在某項目中，請選擇頁面左上方的「Microsoft Foundry」以返回首頁。
   - 選擇「+ Create project」。
   - 輸入項目名稱。
   - 如果您已有中樞，系統會預設選擇它。如果您有多於一個中樞，可以從下拉選單選擇其他中樞。如果您想創建新中樞，選擇「Create new hub」並提供名稱。
   - 選擇「Create」。

### 在 Microsoft Foundry 創建中樞

1. **前往 Microsoft Foundry**：用您的 Azure 帳戶登入。
2. <strong>創建中樞</strong>：
   - 從左側菜單選擇管理中心。
   - 選擇「All resources」，然後點擊「+ New project」旁的向下箭頭，選擇「+ New hub」。
   - 在「Create a new hub」對話框中，輸入您的中樞名稱（例如 contoso-hub），並按需修改其他欄位。
   - 選擇「Next」，檢查資訊，然後選擇「Create」。

更多詳細說明，您可參考官方的 [Microsoft 文件](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)。

成功創建後，您可以通過 [ai.azure.com](https://ai.azure.com/) 訪問您建立的工作室。

一個 AI Foundry 中可有多個項目。請先在 AI Foundry 內建立項目以備用。

建立 Microsoft Foundry [快速入門](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. 在 Microsoft Foundry 部署 Phi 模型**

點擊項目中的 Explore 選項進入模型目錄，選擇 Phi-3。

選擇 Phi-3-mini-4k-instruct。

點擊「Deploy」部署 Phi-3-mini-4k-instruct 模型。

> [!NOTE]
>
> 部署時您可以選擇計算資源。

## **3. 在 Microsoft Foundry 的 Playground 與 Phi 聊天**

前往部署頁面，選擇 Playground，開始與 Microsoft Foundry 的 Phi-3 聊天。

## **4. 從 Microsoft Foundry 部署模型**

若要從 Azure 模型目錄部署模型，您可以遵循以下步驟：

- 登入 Microsoft Foundry。
- 從 Microsoft Foundry 模型目錄中選擇您想部署的模型。
- 在模型詳細頁面，選擇 Deploy，然後選擇帶有 Azure AI 內容安全的 Serverless API。
- 選擇您想部署模型的項目。要使用 Serverless API，您的工作區必須屬於 East US 2 或 Sweden Central 地區。您可以自訂部署名稱。
- 在部署精靈中，選擇定價和條款以了解價格和使用條款。
- 點擊 Deploy。等待部署完成並且系統自動跳轉到部署頁面。
- 選擇「Open in playground」開始與模型互動。
- 您可以返回部署頁面，選擇部署，並記下端點的目標 URL 和秘密金鑰，用於調用部署並生成回應。
- 您隨時可以通過導覽至「Build」標籤，並從「Components」區段選擇「Deployments」來查找端點詳情、URL 和訪問金鑰。

> [!NOTE]
>
> 請注意，您的帳號必須在該資源組具有 Azure AI Developer 角色權限，才能執行這些步驟。

## **5. 在 Microsoft Foundry 使用 Phi API**

您可以通過 Postman 使用 GET 請求存取 https://{Your project name}.region.inference.ml.azure.com/swagger.json，結合金鑰了解所提供的接口。

您可以非常方便地獲取請求參數以及回應參數。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引致的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->