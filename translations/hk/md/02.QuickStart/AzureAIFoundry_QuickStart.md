<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:20:18+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "hk"
}
-->
# **在 Azure AI Foundry 使用 Phi-3**

隨著生成式 AI 的發展，我們希望能透過一個統一的平台來管理不同的 LLM 和 SLM、企業數據整合、微調/RAG 操作，以及整合 LLM 和 SLM 後對不同企業業務的評估等，讓生成式 AI 能更好地應用於智慧化場景。[Azure AI Foundry](https://ai.azure.com) 是一個企業級的生成式 AI 應用平台。

![aistudo](../../../../translated_images/hk/aifoundry_home.f28a8127c96c7d93.png)

利用 Azure AI Foundry，你可以評估大型語言模型（LLM）的回應，並透過 prompt flow 編排提示應用元件，以提升效能。此平台支援從概念驗證到完整生產的擴展，並提供持續監控與優化，助你長期成功。

我們可以透過簡單步驟，快速在 Azure AI Foundry 部署 Phi-3 模型，並利用 Azure AI Foundry 完成 Phi-3 相關的 Playground/Chat、微調、評估等工作。

## **1. 準備工作**

如果你已在電腦上安裝了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)，使用此範本只需在新目錄下執行指令即可。

## 手動建立

建立 Microsoft Azure AI Foundry 專案與 hub 是組織和管理 AI 工作的好方法。以下是逐步教學，幫助你開始：

### 在 Azure AI Foundry 建立專案

1. **前往 Azure AI Foundry**：登入 Azure AI Foundry 入口網站。
2. **建立專案**：
   - 若你已在某專案中，點選頁面左上角的「Azure AI Foundry」回到首頁。
   - 選擇「+ Create project」。
   - 輸入專案名稱。
   - 若已有 hub，系統會預設選擇；若你有多個 hub 權限，可從下拉選單選擇其他 hub。若要建立新 hub，選擇「Create new hub」並輸入名稱。
   - 點選「Create」。

### 在 Azure AI Foundry 建立 Hub

1. **前往 Azure AI Foundry**：使用你的 Azure 帳號登入。
2. **建立 Hub**：
   - 從左側選單選擇管理中心（Management center）。
   - 選擇「All resources」，點擊「+ New project」旁的下拉箭頭，選擇「+ New hub」。
   - 在「Create a new hub」對話框中，輸入 hub 名稱（例如 contoso-hub），並依需求修改其他欄位。
   - 點選「Next」，確認資訊後點選「Create」。

更多詳細說明可參考官方 [Microsoft 文件](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)。

建立成功後，可透過 [ai.azure.com](https://ai.azure.com/) 進入你建立的 studio。

一個 AI Foundry 可有多個專案，先在 AI Foundry 建立專案做準備。

建立 Azure AI Foundry [快速入門](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. 在 Azure AI Foundry 部署 Phi 模型**

點選專案的 Explore 選項，進入模型目錄並選擇 Phi-3。

選擇 Phi-3-mini-4k-instruct。

點擊「Deploy」部署 Phi-3-mini-4k-instruct 模型。

> [!NOTE]
>
> 部署時可選擇運算資源。

## **3. 在 Azure AI Foundry Playground 與 Phi 聊天**

前往部署頁面，選擇 Playground，與 Azure AI Foundry 的 Phi-3 進行對話。

## **4. 從 Azure AI Foundry 部署模型**

若要從 Azure 模型目錄部署模型，可依照以下步驟：

- 登入 Azure AI Foundry。
- 從 Azure AI Foundry 模型目錄中選擇想部署的模型。
- 在模型詳細頁面，選擇 Deploy，接著選擇帶有 Azure AI Content Safety 的 Serverless API。
- 選擇要部署模型的專案。使用 Serverless API 服務時，工作區必須位於 East US 2 或 Sweden Central 區域。你也可以自訂部署名稱。
- 在部署精靈中，選擇 Pricing and terms 了解價格與使用條款。
- 點選 Deploy，等待部署完成並自動導向 Deployments 頁面。
- 選擇 Open in playground 開始與模型互動。
- 你可以回到 Deployments 頁面，選擇該部署，查看端點的 Target URL 和 Secret Key，這些可用來呼叫部署並產生回應。
- 你也可以在 Build 標籤下，從 Components 區段選擇 Deployments，隨時查看端點詳細資訊、URL 和存取金鑰。

> [!NOTE]
> 請注意，你的帳號必須在資源群組擁有 Azure AI Developer 角色權限，才能執行上述步驟。

## **5. 在 Azure AI Foundry 使用 Phi API**

你可以透過 Postman 使用 GET 請求存取 https://{Your project name}.region.inference.ml.azure.com/swagger.json，並結合 Key 了解提供的介面。

你可以非常方便地取得請求參數及回應參數。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。