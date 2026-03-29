# **使用 Microsoft Phi-3 系列打造您自己的 Visual Studio Code GitHub Copilot Chat**

您是否使用過 GitHub Copilot Chat 中的 workspace agent？您是否想打造您自己團隊的程式碼代理人？本動手實驗希望結合開源模型來打造一個企業級的程式碼商務代理人。

## <strong>基礎</strong>

### **為何選擇 Microsoft Phi-3**

Phi-3 是一個系列家族，包括基於不同訓練參數的 phi-3-mini、phi-3-small 及 phi-3-medium，適用於文本生成、對話完成及程式碼生成。此外也有基於 Vision 的 phi-3-vision。它適合企業或不同團隊打造離線產生式 AI 解決方案。

建議閱讀此連結 [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 擴充功能提供了聊天介面，讓您能與 GitHub Copilot 互動，並直接在 VS Code 中針對程式相關問題收到回答，無需瀏覽文件或線上論壇。

Copilot Chat 可能會使用語法高亮、縮排和其他格式功能來增加生成回應的清晰度。根據使用者問題類型，回應中可能包含 Copilot 用於生成回答的上下文連結，例如原始程式碼檔案或文件，或是存取 VS Code 功能的按鈕。

- Copilot Chat 整合您的開發流程，在您需要的地方提供協助：

- 直接從編輯器或終端機啟動內嵌聊天對話，在您編寫程式時獲得幫助

- 使用聊天視圖讓 AI 助手隨時在側邊協助您

- 啟動快速聊天以快速提出問題，並迅速回到您所做的事情

您可以在多種情境下使用 GitHub Copilot Chat，例如：

- 回答如何最佳解決問題的程式相關問題

- 解釋他人程式碼並提出改進建議

- 提議程式碼修正

- 產生單元測試案例

- 產生程式碼文件說明

建議閱讀此連結 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

在 Copilot Chat 中引用 **@workspace** 讓您能就整個程式碼庫提出問題。根據問題，Copilot 智能檢索相關檔案和符號，並在回答中引用這些連結和程式碼範例。

為了回答您的問題，**@workspace** 會搜尋與開發人員在 VS Code 導覽程式碼庫時相同的資源：

- 工作區中所有檔案，除了被 .gitignore 檔案忽略的檔案

- 目錄結構，包含巢狀資料夾和檔案名稱

- GitHub 的程式碼搜尋索引（如果工作區是 GitHub 倉庫且已被程式碼搜尋索引）

- 工作區中的符號和定義

- 當前選中的文字或在啟動編輯器中可見的文字

注意：如果您已開啟被忽略的檔案或在其中選取文字，.gitignore 將被忽略。

建議閱讀此連結 [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## <strong>進一步了解本實驗</strong>

GitHub Copilot 已大幅提升企業的程式開發效率，每家企業都希望客製化 GitHub Copilot 的相關功能。許多企業根據自身業務場景與開源模型，客製化了類似 GitHub Copilot 的擴充功能。對企業而言，客製化擴充功能更易於控管，但這也影響使用者體驗。畢竟 GitHub Copilot 在處理通用場景與專業度方面功能更強。如果能保持體驗一致，便能打造出更佳的企業自有擴充功能。GitHub Copilot Chat 提供企業相關 API 以擴展聊天體驗。維持一致的體驗且擁有客製化功能，將帶來更好的使用者體驗。

本實驗主要使用 Phi-3 模型結合本地 NPU 與 Azure 混合，打造 GitHub Copilot Chat 中的自訂代理人 ***@PHI3***，協助企業開發者完成程式碼生成 ***(@PHI3 /gen)*** 與基於圖片生成程式碼 ***(@PHI3 /img)***。

![PHI3](../../../../../../../translated_images/zh-TW/cover.1017ebc9a7c46d09.webp)

### ***注意：***

本實驗目前已於 Intel CPU 與 Apple Silicon 的 AIPC 上實作，後續將持續更新 Qualcomm 版本的 NPU。

## <strong>實驗內容</strong>


| 名稱 | 說明 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - 安裝(✅) | 配置並安裝相關環境與安裝工具 | [前往](./HOL/AIPC/01.Installations.md) |[前往](./HOL/Apple/01.Installations.md) |
| Lab1 - 使用 Phi-3-mini 執行 Prompt flow (✅) | 結合 AIPC / Apple Silicon，使用本地 NPU 透過 Phi-3-mini 建立程式碼生成 | [前往](./HOL/AIPC/02.PromptflowWithNPU.md) |  [前往](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - 在 Azure Machine Learning Service 部署 Phi-3-vision(✅) | 透過部署 Azure Machine Learning Service 的 Model Catalog - Phi-3-vision 影像以生成程式碼 | [前往](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[前往](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - 在 GitHub Copilot Chat 建立 @phi-3 代理人(✅)  | 在 GitHub Copilot Chat 建立自訂 Phi-3 代理人，完成程式碼生成、圖形生成程式碼、RAG 等 | [前往](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [前往](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| 範例程式碼 (✅)  | 下載範例程式碼 | [前往](../../../../../../../code/07.Lab/01/AIPC) | [前往](../../../../../../../code/07.Lab/01/Apple) |


## <strong>資源</strong>

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. 進一步了解 GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. 進一步了解 GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. 進一步了解 GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. 進一步了解 Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. 進一步了解 Microsoft Foundry 的 Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->