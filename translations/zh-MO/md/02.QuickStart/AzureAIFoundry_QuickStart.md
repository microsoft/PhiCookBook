# **在 Microsoft Foundry 中使用 Phi-3**

隨著生成式 AI 的發展，我們希望使用一個統一平台來管理不同的 LLM 和 SLM、企業數據整合、微調/RAG 操作，以及整合 LLM 和 SLM 後對不同企業業務的評估，從而更好地實現生成式 AI 的智慧應用。[Microsoft Foundry](https://ai.azure.com) 是一個企業級的生成式 AI 應用平台。

![aistudo](../../../../translated_images/zh-MO/aifoundry_home.f28a8127c96c7d93.webp)

使用 Microsoft Foundry，您可以評估大型語言模型 (LLM) 的回應，並使用提示流程協調提示應用組件，以獲得更佳性能。該平台便於將概念驗證輕鬆轉變為完整生產，並支持持續監控與優化，助力長期成功。

我們可以通過簡單步驟快速在 Microsoft Foundry 上部署 Phi-3 模型，然後利用 Microsoft Foundry 完成與 Phi-3 相關的 Playground/聊天、微調、評估等工作。

## **1. 準備工作**

如果您已在機器上安裝了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)，使用此模板只需在新目錄中運行此命令即可。

## 手動創建

創建 Microsoft Foundry 專案和集線器是組織和管理您的 AI 工作的好方法。以下是開始使用的步驟指南：

### 在 Microsoft Foundry 中創建一個專案

1. **前往 Microsoft Foundry**：登入 Microsoft Foundry 入口網站。
2. <strong>創建專案</strong>：
   - 如果您已在某專案內，請點選頁面左上角的「Microsoft Foundry」回到主頁。
   - 選擇「+ 創建專案」。
   - 輸入專案名稱。
   - 如果已有集線器，則會預設選中。如果您有權限訪問多個集線器，可以從下拉選單中選擇不同集線器。若要創建新集線器，請選擇「創建新集線器」並輸入名稱。
   - 選擇「創建」。

### 在 Microsoft Foundry 中創建一個集線器

1. **前往 Microsoft Foundry**：使用您的 Azure 帳戶登入。
2. <strong>創建集線器</strong>：
   - 從左側選單中選擇管理中心。
   - 選擇「所有資源」，然後在「+ 新專案」旁的下拉箭頭中選擇「+ 新集線器」。
   - 在「創建新集線器」對話框中輸入集線器名稱（例如 contoso-hub），並根據需要修改其他欄位。
   - 選擇「下一步」，檢查資訊後選擇「創建」。

更多詳細說明，您可參考官方 [Microsoft 文件](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)。

成功創建後，您可以通過 [ai.azure.com](https://ai.azure.com/) 訪問您創建的 Studio。

一個 AI Foundry 可以擁有多個專案，請在 AI Foundry 中創建專案以便準備。

創建 Microsoft Foundry [快速入門](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. 在 Microsoft Foundry 部署 Phi 模型**

點選專案的 Explore 選項進入模型目錄，並選擇 Phi-3。

選擇 Phi-3-mini-4k-instruct。

點擊「部署」來部署 Phi-3-mini-4k-instruct 模型。

> [!NOTE]
>
> 部署時可以選擇計算能力。

## **3. 在 Microsoft Foundry Playground 與 Phi 聊天**

前往部署頁面，選擇 Playground，並與 Microsoft Foundry 的 Phi-3 聊天。

## **4. 從 Microsoft Foundry 部署模型**

從 Azure 模型目錄部署模型可按以下步驟操作：

- 登入 Microsoft Foundry。
- 從 Microsoft Foundry 模型目錄選擇您要部署的模型。
- 在模型詳情頁，選擇部署，然後選擇「使用 Azure AI 內容安全的無伺服器 API」。
- 選擇要部署模型的專案。使用無伺服器 API 服務，您的工作區必須屬於 East US 2 或 Sweden Central 區域。您可以自訂部署名稱。
- 在部署嚮導中，選擇「價格與條款」以了解價格及使用條款。
- 選擇「部署」。等待部署完成，並會自動轉至部署頁面。
- 選擇「在 playground 中開啟」以開始與模型互動。
- 您可以返回部署頁面，選擇部署，並查看端點的目標 URL 與密鑰，這些可用於調用部署並生成回應。
- 您可隨時在「建置」標籤中，於元件區段選擇「部署」，找到端點詳情、URL 與訪問鑰匙。

> [!NOTE]
> 請注意，您的帳戶必須在資源群組上擁有 Azure AI 開發者角色權限，以執行這些步驟。

## **5. 在 Microsoft Foundry 使用 Phi API**

您可以透過 Postman GET 連接 https://{Your project name}.region.inference.ml.azure.com/swagger.json，並結合密鑰了解所提供的介面。

您可以非常方便地取得請求參數及回應參數。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言文件應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->