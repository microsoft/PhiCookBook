# **建立您自己的 Visual Studio Code GitHub Copilot Chat，結合 Microsoft Phi-3 系列**

您是否使用過 GitHub Copilot Chat 的工作區代理？您想打造自己的團隊代碼代理嗎？本實作實驗希望結合開源模型，打造企業級的代碼業務代理。

## <strong>基礎</strong>

### **為什麼選擇 Microsoft Phi-3**

Phi-3 是一個系列，包括基於不同訓練參數用於文本生成、對話完成和代碼生成的 phi-3-mini、phi-3-small 和 phi-3-medium。還有基於 Vision 的 phi-3-vision。它適合企業或不同團隊構建離線生成式 AI 解決方案。

建議閱讀此連結 [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 擴充功能為您提供一個聊天介面，讓您能直接在 VS Code 內與 GitHub Copilot 互動，並接收有關編碼問題的答案，無需瀏覽文件或在線論壇搜尋。

Copilot Chat 可能使用語法高亮、縮排及其他格式功能，使生成的回應更易理解。依用戶提問類型，結果可能包含 Copilot 用作生成回應的上下文連結，如原始碼文件或文件說明，或語法按鈕以存取 VS Code 功能。

- Copilot Chat 融入您的開發流程，並在您需要時提供協助：

- 從編輯器或終端機直接啟動內聯聊天對話，在編碼時獲得協助

- 使用聊天視圖隨時擁有 AI 助手協助您

- 啟動快速聊天，快速提問並繼續您的工作

您可在多種場景中使用 GitHub Copilot Chat，例如：

- 回答解決問題的最佳編碼方案問題

- 解釋他人代碼並提出改進建議

- 建議代碼修正

- 生成單元測試案例

- 生成代碼文件說明

建議閱讀此連結 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat 中的 **@workspace** 讓您可以詢問整個代碼庫的問題。根據問題，Copilot 智能檢索相關檔案和符號，並在回答中以連結和代碼示例引用它們。

為了回答您的問題，**@workspace** 會搜尋 VS Code 開發者瀏覽代碼庫時會用的相同來源：

- 工作區內的所有檔案，但不包括 .gitignore 忽略的檔案

- 嵌套的資料夾和檔案名的目錄結構

- 如果工作區為 GitHub 儲存庫且受代碼搜尋索引，則使用 GitHub 的代碼搜尋索引

- 工作區的符號及定義

- 在活動編輯器中目前選取或可見的文字

注意：如果您開啟了被忽略的檔案或者在該檔案中選取文字，.gitignore 會被忽略。

建議閱讀此連結 [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## <strong>了解更多本實驗</strong>

GitHub Copilot 大幅提升企業編程效率，每間企業都希望能自訂 GitHub Copilot 的相關功能。許多企業根據自身業務場景和開源模型定制了類似 GitHub Copilot 的擴充功能。對企業來說，自訂的擴充功能更易控制，但也會影響用戶體驗。畢竟，GitHub Copilot 在處理通用場景和專業性方面功能更強。如果體驗能保持一致，定制企業自有的擴充功能會更理想。GitHub Copilot Chat 為企業提供擴展聊天體驗的相關 API。維持一致體驗並擁有自訂功能，是更好的用戶體驗。

本實驗主要使用 Phi-3 模型結合本地 NPU 及 Azure 混合，建立 GitHub Copilot Chat 自訂 Agent ***@PHI3***，協助企業開發者完成代碼生成<strong><em>(@PHI3 /gen)</em></strong>，以及基於影像生成代碼 ***(@PHI3 /img)***。

![PHI3](../../../../../../../translated_images/zh-HK/cover.1017ebc9a7c46d09.webp)

### ***注意：*** 

本實驗目前實作於 Intel CPU 與 Apple Silicon 的 AIPC 上。我們會持續更新 Qualcomm 版本的 NPU 支援。


## <strong>實驗</strong>


| 名稱 | 說明 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - 安裝(✅) | 配置並安裝相關環境及安裝工具 | [前往](./HOL/AIPC/01.Installations.md) |[前往](./HOL/Apple/01.Installations.md) |
| Lab1 - 使用 Phi-3-mini 進行 Prompt 流 (✅) | 結合 AIPC / Apple Silicon，使用本地 NPU 通過 Phi-3-mini 創建代碼生成 | [前往](./HOL/AIPC/02.PromptflowWithNPU.md) |  [前往](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - 在 Azure 機器學習服務上部署 Phi-3-vision(✅) | 通過部署 Azure 機器學習服務的模型目錄 - Phi-3-vision 影像來生成代碼 | [前往](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[前往](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - 建立 GitHub Copilot Chat 中的 @phi-3 代理(✅)  | 在 GitHub Copilot Chat 中創建自訂 Phi-3 代理以完成代碼生成、圖生成代碼、RAG 等 | [前往](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [前往](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| 範例程式碼 (✅)  | 下載範例程式碼 | [前往](../../../../../../../code/07.Lab/01/AIPC) | [前往](../../../../../../../code/07.Lab/01/Apple) |


## <strong>資源</strong>

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. 了解更多關於 GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. 了解更多關於 GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. 了解更多關於 GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. 了解更多關於 Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. 了解更多關於 Microsoft Foundry 的模型目錄 [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->