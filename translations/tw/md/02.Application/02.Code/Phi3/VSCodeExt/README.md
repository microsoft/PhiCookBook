<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:35:15+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "tw"
}
-->
# **使用 Microsoft Phi-3 系列打造專屬的 Visual Studio Code GitHub Copilot Chat**

你有使用過 GitHub Copilot Chat 中的 workspace agent 嗎？想打造自己團隊的程式碼助理嗎？這個實作實驗室希望結合開源模型，打造企業級的程式碼商務助理。

## **基礎介紹**

### **為什麼選擇 Microsoft Phi-3**

Phi-3 是一個系列家族，包含 phi-3-mini、phi-3-small 和 phi-3-medium，根據不同的訓練參數，適用於文字生成、對話完成和程式碼生成。還有基於 Vision 的 phi-3-vision。非常適合企業或不同團隊打造離線的生成式 AI 解決方案。

建議閱讀此連結 [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 擴充功能提供一個聊天介面，讓你能直接在 VS Code 中與 GitHub Copilot 互動，並獲得程式碼相關問題的解答，無需翻閱文件或搜尋線上論壇。

Copilot Chat 可能會使用語法高亮、縮排及其他格式化功能，讓生成的回應更清晰。根據使用者提問的類型，結果可能包含 Copilot 用來生成回應的上下文連結，如原始碼檔案或文件，或是用於存取 VS Code 功能的按鈕。

- Copilot Chat 整合在你的開發流程中，隨時提供協助：

- 可直接從編輯器或終端機啟動內嵌聊天，讓你在編碼時獲得幫助

- 使用 Chat 視圖，隨時有 AI 助理在旁協助

- 啟動快速聊天，快速提問後繼續工作

你可以在多種情境下使用 GitHub Copilot Chat，例如：

- 回答如何最佳解決問題的程式碼問題

- 解釋他人程式碼並提出改進建議

- 建議程式碼修正

- 生成單元測試案例

- 生成程式碼文件說明

建議閱讀此連結 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

在 Copilot Chat 中使用 **@workspace**，可以讓你針對整個程式碼庫提問。根據問題，Copilot 會智能檢索相關檔案和符號，並在回答中以連結和程式碼範例呈現。

為了回答你的問題，**@workspace** 會搜尋開發者在 VS Code 中瀏覽程式碼庫時會用到的資源：

- 工作區中的所有檔案，除了被 .gitignore 忽略的檔案

- 目錄結構，包括巢狀資料夾和檔案名稱

- 如果工作區是 GitHub 倉庫且已被代碼搜尋索引，則會使用 GitHub 的代碼搜尋索引

- 工作區中的符號和定義

- 目前選取的文字或在活動編輯器中可見的文字

注意：如果你已開啟或選取了被忽略檔案中的文字，.gitignore 將被忽略。

建議閱讀此連結 [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **進一步了解本實驗室**

GitHub Copilot 大幅提升企業的程式開發效率，每個企業都希望能客製化 GitHub Copilot 的相關功能。許多企業根據自身業務場景和開源模型，打造了類似 GitHub Copilot 的客製化擴充功能。對企業來說，客製化擴充功能更容易掌控，但這也會影響使用者體驗。畢竟 GitHub Copilot 在處理通用場景和專業性上功能更強大。如果能保持體驗一致，客製化企業自己的擴充功能會更理想。GitHub Copilot Chat 提供相關 API，讓企業能在聊天體驗上擴展。維持一致的體驗並擁有客製化功能，能帶來更佳的使用者體驗。

本實驗室主要結合 Phi-3 模型與本地 NPU 及 Azure 混合架構，打造 GitHub Copilot Chat 中的自訂 Agent ***@PHI3***，協助企業開發者完成程式碼生成***(@PHI3 /gen)***及基於圖片生成程式碼***(@PHI3 /img)***。

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d095fe0b942687287803c03933d2d1d439d14e10fa1442a864d.tw.png)

### ***注意：***

本實驗室目前在 Intel CPU 和 Apple Silicon 的 AIPC 上實作，我們將持續更新 Qualcomm 版本的 NPU。

## **實驗室內容**

| 名稱 | 說明 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - 安裝(✅) | 配置並安裝相關環境與安裝工具 | [前往](./HOL/AIPC/01.Installations.md) |[前往](./HOL/Apple/01.Installations.md) |
| Lab1 - 使用 Phi-3-mini 執行 Prompt flow (✅) | 結合 AIPC / Apple Silicon，使用本地 NPU 透過 Phi-3-mini 進行程式碼生成 | [前往](./HOL/AIPC/02.PromptflowWithNPU.md) |  [前往](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - 在 Azure Machine Learning Service 部署 Phi-3-vision(✅) | 透過部署 Azure Machine Learning Service 的模型目錄 - Phi-3-vision 影像來生成程式碼 | [前往](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[前往](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - 在 GitHub Copilot Chat 中建立 @phi-3 agent(✅)  | 在 GitHub Copilot Chat 中建立自訂 Phi-3 agent，完成程式碼生成、圖形生成程式碼、RAG 等功能 | [前往](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [前往](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| 範例程式碼 (✅)  | 下載範例程式碼 | [前往](../../../../../../../code/07.Lab/01/AIPC) | [前往](../../../../../../../code/07.Lab/01/Apple) |

## **資源**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. 進一步了解 GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. 進一步了解 GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. 進一步了解 GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. 進一步了解 Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. 進一步了解 Azure AI Foundry 的模型目錄 [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。