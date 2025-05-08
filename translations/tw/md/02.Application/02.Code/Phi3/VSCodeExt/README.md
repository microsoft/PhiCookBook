<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-05-08T05:29:16+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "tw"
}
-->
# **打造你自己的 Visual Studio Code GitHub Copilot Chat，搭配 Microsoft Phi-3 系列**

你有使用過 GitHub Copilot Chat 裡的 workspace agent 嗎？想打造你們團隊專屬的程式碼助理嗎？這個實作實驗室希望結合開源模型，打造企業級的程式碼商務助理。

## **基礎介紹**

### **為什麼選擇 Microsoft Phi-3**

Phi-3 是一個系列家族，包括 phi-3-mini、phi-3-small 和 phi-3-medium，根據不同的訓練參數，適用於文字生成、對話完成和程式碼生成。還有基於視覺的 phi-3-vision。適合企業或不同團隊打造離線生成式 AI 解決方案。

建議閱讀此連結 [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 擴充功能提供一個聊天介面，讓你能直接在 VS Code 裡與 GitHub Copilot 互動，針對程式相關問題獲得解答，無需跳轉文件或上網搜尋論壇。

Copilot Chat 會利用語法高亮、縮排等格式化功能，讓回覆更清楚。根據使用者提問的類型，結果可能包含 Copilot 用來生成回答的上下文連結，例如原始碼檔案或文件，或是呼叫 VS Code 功能的按鈕。

- Copilot Chat 整合在你的開發流程中，隨時提供協助：

- 可直接從編輯器或終端機啟動內嵌聊天，邊寫程式邊求助

- 使用聊天視窗，隨時有 AI 助手在旁協助

- 啟動快速聊天，快速提問後回到工作

你可以在多種情境下使用 GitHub Copilot Chat，例如：

- 回答程式問題，協助最佳解法

- 解釋他人程式碼並提出改進建議

- 建議程式碼修正

- 產生單元測試案例

- 產生程式碼文件說明

建議閱讀此連結 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

在 Copilot Chat 中使用 **@workspace**，可以針對整個程式碼庫提問。Copilot 會根據問題，智能檢索相關檔案和符號，並在回答中以連結和程式碼範例引用。

為了回答你的問題，**@workspace** 會搜尋開發者在 VS Code 瀏覽程式碼庫時會用到的資源：

- 工作區內所有檔案，但排除被 .gitignore 忽略的檔案

- 目錄結構，包括巢狀資料夾與檔名

- 如果工作區是 GitHub 倉庫且被程式碼搜尋索引，則會用到 GitHub 的程式碼搜尋索引

- 工作區中的符號與定義

- 編輯器中目前選取的文字或可見文字

注意：若你已開啟被忽略的檔案或選取其中文字，.gitignore 將不會生效。

建議閱讀此連結 [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **深入了解本實驗室**

GitHub Copilot 大幅提升企業的程式開發效率，每家企業都希望客製化 GitHub Copilot 的相關功能。許多企業根據自身商業場景和開源模型，客製化了類似 GitHub Copilot 的擴充功能。對企業來說，客製化擴充功能較易控管，但同時也影響使用體驗。畢竟 GitHub Copilot 在處理通用場景和專業度上功能更強。如果能保持一致的體驗，再加上客製化功能，會是更好的使用體驗。GitHub Copilot Chat 提供相關 API，方便企業擴展聊天體驗。維持一致體驗同時具備客製功能，是更佳的用戶體驗。

本實驗室主要使用 Phi-3 模型，結合本地 NPU 與 Azure 混合架構，在 GitHub Copilot Chat 裡打造自訂 Agent ***@PHI3***，協助企業開發者完成程式碼生成 ***(@PHI3 /gen)*** 及基於影像生成程式碼 ***(@PHI3 /img)***。

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d095fe0b942687287803c03933d2d1d439d14e10fa1442a864d.tw.png)

### ***注意:*** 

本實驗室目前在 Intel CPU 和 Apple Silicon 的 AIPC 平台實作，未來會持續更新 Qualcomm 版本的 NPU。


## **實驗室內容**


| 名稱 | 說明 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | 設定並安裝相關環境與安裝工具 | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | 結合 AIPC / Apple Silicon，使用本地 NPU 透過 Phi-3-mini 建立程式碼生成 | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | 部署 Azure Machine Learning Service 的模型目錄 - Phi-3-vision 影像，生成程式碼 | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | 在 GitHub Copilot Chat 裡建立自訂 Phi-3 agent，完成程式碼生成、圖形生成程式碼、RAG 等 | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | 下載範例程式碼 | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **資源**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. 了解更多 GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. 了解更多 GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. 了解更多 GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. 了解更多 Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. 了解更多 Azure AI Foundry 的模型目錄 [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能會包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。本公司不對因使用本翻譯所引起之任何誤解或誤譯負責。