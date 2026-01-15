<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-07-16T22:36:48+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "hk"
}
-->
# **介紹 Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) 是一款視覺化工作流程自動化工具，讓用戶能夠利用預建範本和自訂連接器來創建自動化工作流程。它旨在幫助開發人員和業務分析師快速建立自動化流程，應用於資料管理、協作及流程優化等任務。透過 Prompt Flow，用戶可以輕鬆連接不同的服務、應用程式和系統，並自動化複雜的業務流程。

Microsoft Prompt Flow 專為簡化由大型語言模型（LLMs）驅動的 AI 應用程式的端到端開發週期而設計。無論你是在構思、原型設計、測試、評估還是部署基於 LLM 的應用程式，Prompt Flow 都能簡化流程，幫助你打造具備生產品質的 LLM 應用。

## 使用 Microsoft Prompt Flow 的主要功能與優勢：

**互動式創作體驗**

Prompt Flow 提供工作流程結構的視覺化呈現，讓你輕鬆理解並瀏覽專案。
它提供類似筆記本的編碼體驗，提升工作流程開發與除錯的效率。

**提示變體與調整**

建立並比較多個提示變體，促進反覆優化的過程。評估不同提示的表現，選擇最有效的版本。

**內建評估流程**

利用內建的評估工具，評估你的提示和工作流程的品質與效能。
了解你的基於 LLM 的應用程式表現如何。

**豐富資源**

Prompt Flow 包含內建工具庫、範例和範本，這些資源可作為開發起點，激發創意並加速流程。

**協作與企業級準備**

支援團隊協作，允許多位用戶共同參與提示工程專案。
維護版本控制並有效分享知識。簡化整個提示工程流程，從開發、評估到部署與監控。

## Prompt Flow 中的評估

在 Microsoft Prompt Flow 中，評估在判斷 AI 模型表現上扮演關鍵角色。讓我們來看看如何在 Prompt Flow 中自訂評估流程和指標：

![PFVizualise](../../../../../translated_images/hk/pfvisualize.c1d9ca75baa2a222.png)

**理解 Prompt Flow 中的評估**

在 Prompt Flow 裡，工作流程代表一連串節點，負責處理輸入並產生輸出。評估流程是專門用來根據特定標準和目標評估執行結果表現的特殊流程。

**評估流程的主要特點**

通常會在被測試的流程執行後運行，使用其輸出結果。
計算分數或指標來衡量被測流程的表現。指標可以包括準確率、相關性分數或其他相關衡量標準。

### 自訂評估流程

**定義輸入**

評估流程需要接收被測流程的輸出。輸入定義方式與一般流程相同。
例如，若你在評估 QnA 流程，輸入可命名為「answer」。若評估分類流程，輸入可命名為「category」。有時也需要真實標籤（ground truth）作為輸入。

**輸出與指標**

評估流程會產生衡量被測流程表現的結果。指標可透過 Python 或 LLM 計算。使用 log_metric() 函數來記錄相關指標。

**使用自訂評估流程**

開發符合你特定任務和目標的自訂評估流程。
根據評估目標調整指標。
將此自訂評估流程應用於批次執行，以進行大規模測試。

## 內建評估方法

Prompt Flow 也提供內建的評估方法。
你可以提交批次執行，並使用這些方法評估工作流程在大型資料集上的表現。
查看評估結果、比較指標，並根據需要反覆優化。
請記得，評估對確保 AI 模型達到預期標準和目標至關重要。詳細的開發與使用評估流程說明，請參考官方文件。

總結來說，Microsoft Prompt Flow 透過簡化提示工程並提供強大的開發環境，賦能開發者打造高品質的 LLM 應用程式。如果你正在使用 LLM，Prompt Flow 是值得探索的利器。詳情請參考 [Prompt Flow 評估文件](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo)。

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。