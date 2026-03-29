# **建立你自己的 Visual Studio Code GitHub Copilot Chat 及 Microsoft Phi-3 系列**

你用過 GitHub Copilot Chat 中的工作區智能代理嗎？你想建立自己團隊的程式碼智能代理嗎？這個實作實驗旨在結合開源模型，打造企業級的程式碼業務代理。

## <strong>基礎知識</strong>

### **為什麼選擇 Microsoft Phi-3**

Phi-3 是一個系列，包括基於不同訓練參數的 phi-3-mini、phi-3-small 和 phi-3-medium，適用於文本生成、對話完成和程式碼生成。還有基於視覺的 phi-3-vision。它適合企業或不同團隊建立離線生成式 AI 解決方案。

建議閱讀此連結 [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 擴展提供一個聊天界面，讓你可以與 GitHub Copilot 互動，並直接在 VS Code 內獲得與編程相關的問題答案，無需瀏覽文件或線上論壇。

Copilot Chat 可能會使用語法高亮、縮排和其他格式化功能，為生成的回應增添清晰度。根據用戶問題的不同，結果可能包含 Copilot 用於生成回應的上下文連結（如源碼文件或文件檔案），或訪問 VS Code 功能的按鈕。

- Copilot Chat 整合在你的開發流程中，並在你需要的地方提供協助：

- 直接從編輯器或終端啟動內聯聊天對話，助你編碼時獲得幫助

- 使用 Chat 視圖讓 AI 助手隨時在旁支援

- 啟動快速聊天 (Quick Chat) 即問即答，迅速回到你的工作

你可以在多種場景中使用 GitHub Copilot Chat，例如：

- 解答關於解決問題的編程問題

- 解釋其他人的程式碼並提出改進建議

- 提議程式碼修正

- 生成單元測試案例

- 生成程式碼文件

建議閱讀此連結 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

在 Copilot Chat 中引用 **@workspace**，讓你可以針對整個程式碼庫提問。根據問題，Copilot 智能檢索相關檔案和符號，並在回答中以連結和程式碼範例引用它們。

為了回應你的問題，**@workspace** 會搜索與開發者在 VS Code 導覽程式碼庫時同樣的資源：

- 工作區中的所有檔案，忽略 .gitignore 文件中忽略的檔案

- 包含嵌套資料夾和檔名的目錄結構

- GitHub 的程式碼搜尋索引（如果工作區為 GitHub 儲存庫且已被程式碼搜尋編入索引）

- 工作區中的符號和定義

- 編輯器中當前選取的文字或可見文字

注意：如果你打開或選取了忽略文件中的文字，.gitignore 將被繞過。

建議閱讀此連結 [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## <strong>深入了解此實驗</strong>

GitHub Copilot 已大幅提升企業的程式設計效率，且每間企業都希望定制 GitHub Copilot 的相關功能。許多企業基於自身業務場景和開源模型，定制了類似 GitHub Copilot 的擴展 (Extensions)。對企業來說，定制的擴展更易於控制，但這也影響使用者體驗。畢竟 GitHub Copilot 在處理通用場景及專業度上功能更強。如果能保持一致體驗，定制企業的專屬擴展會更理想。GitHub Copilot Chat 提供企業擴展聊天體驗的相關 API，維持一致體驗並結合定制功能，才能有更佳使用者體驗。

本實驗主要利用 Phi-3 型號，結合本地 NPU 與 Azure 混合部署，打造 GitHub Copilot Chat 中的自訂代理 ***@PHI3***，協助企業開發者完成程式碼生成 ***(@PHI3 /gen)*** 及基於影像生成程式碼 ***(@PHI3 /img)***。

![PHI3](../../../../../../../translated_images/zh-MO/cover.1017ebc9a7c46d09.webp)

### ***注意：*** 

本實驗目前於 Intel CPU 及 Apple Silicon 的 AIPC 實施，我們將持續更新 Qualcomm 版本的 NPU。


## <strong>實驗室</strong>


| 名稱 | 描述 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - 安裝(✅) | 配置及安裝相關環境和安裝工具 | [前往](./HOL/AIPC/01.Installations.md) |[前往](./HOL/Apple/01.Installations.md) |
| Lab1 - 使用 Phi-3-mini 執行 Prompt flow (✅) | 結合 AIPC / Apple Silicon，使用本地 NPU 透過 Phi-3-mini 建立程式碼生成 | [前往](./HOL/AIPC/02.PromptflowWithNPU.md) |  [前往](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - 在 Azure Machine Learning Service 部署 Phi-3-vision(✅) | 部署 Azure Machine Learning Service 的模型目錄 - Phi-3-vision 影像進行程式碼生成 | [前往](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[前往](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - 在 GitHub Copilot Chat 中建立 @phi-3 代理(✅)  | 在 GitHub Copilot Chat 中建立自訂 Phi-3 代理，完成程式碼生成、圖形生成程式碼、RAG 等 | [前往](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [前往](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| 範例程式碼 (✅)  | 下載範例程式碼 | [前往](../../../../../../../code/07.Lab/01/AIPC) | [前往](../../../../../../../code/07.Lab/01/Apple) |


## <strong>資源</strong>

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. 了解更多 GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. 了解更多 GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. 了解更多 GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. 了解更多 Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. 了解更多 Microsoft Foundry 的模型目錄 [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。如因使用本翻譯而產生任何誤解或誤釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->