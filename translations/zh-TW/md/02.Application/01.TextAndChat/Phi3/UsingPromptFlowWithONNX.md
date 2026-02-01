# 使用 Windows GPU 建立 Phi-3.5-Instruct ONNX 的 Prompt flow 解決方案

以下文件示範如何使用 PromptFlow 搭配 ONNX（Open Neural Network Exchange）來開發基於 Phi-3 模型的 AI 應用程式。

PromptFlow 是一套開發工具，旨在簡化基於大型語言模型（LLM）的 AI 應用程式從構思、原型設計到測試與評估的完整開發流程。

透過整合 PromptFlow 與 ONNX，開發者可以：

- 優化模型效能：利用 ONNX 進行高效的模型推論與部署。
- 簡化開發流程：使用 PromptFlow 管理工作流程並自動化重複性任務。
- 強化團隊協作：提供統一的開發環境，促進團隊成員間的合作。

**Prompt flow** 是一套開發工具，設計用來簡化基於 LLM 的 AI 應用程式從構思、原型設計、測試、評估到生產部署與監控的完整開發週期。它讓提示工程變得更加輕鬆，並幫助你打造具備生產品質的 LLM 應用。

Prompt flow 可連接 OpenAI、Azure OpenAI 服務，以及可自訂的模型（Huggingface、本地 LLM/SLM）。我們希望將 Phi-3.5 的量化 ONNX 模型部署到本地應用。Prompt flow 能協助我們更好地規劃業務，並完成基於 Phi-3.5 的本地解決方案。在此範例中，我們將結合 ONNX Runtime GenAI 函式庫，完成基於 Windows GPU 的 Prompt flow 解決方案。

## **安裝**

### **Windows GPU 的 ONNX Runtime GenAI**

請參考此指南設定 Windows GPU 的 ONNX Runtime GenAI [點此](./ORTWindowGPUGuideline.md)

### **在 VSCode 中設定 Prompt flow**

1. 安裝 Prompt flow VS Code 擴充功能

![pfvscode](../../../../../../translated_images/zh-TW/pfvscode.eff93dfc66a42cbe.webp)

2. 安裝完 Prompt flow VS Code 擴充功能後，點選該擴充功能，選擇 **Installation dependencies**，依照指引在你的環境中安裝 Prompt flow SDK

![pfsetup](../../../../../../translated_images/zh-TW/pfsetup.b46e93096f5a254f.webp)

3. 下載 [範例程式碼](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf)，並使用 VS Code 開啟此範例

![pfsample](../../../../../../translated_images/zh-TW/pfsample.8d89e70584ffe7c4.webp)

4. 開啟 **flow.dag.yaml** 選擇你的 Python 環境

![pfdag](../../../../../../translated_images/zh-TW/pfdag.264a77f7366458ff.webp)

   開啟 **chat_phi3_ort.py** 修改你的 Phi-3.5-instruct ONNX 模型路徑

![pfphi](../../../../../../translated_images/zh-TW/pfphi.72da81d74244b45f.webp)

5. 執行你的 prompt flow 進行測試

開啟 **flow.dag.yaml**，點選視覺化編輯器

![pfv](../../../../../../translated_images/zh-TW/pfv.ba8a81f34b20f603.webp)

點擊後執行以進行測試

![pfflow](../../../../../../translated_images/zh-TW/pfflow.4e1135a089b1ce1b.webp)

1. 你也可以在終端機中批次執行以查看更多結果

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

你可以在預設瀏覽器中查看結果

![pfresult](../../../../../../translated_images/zh-TW/pfresult.c22c826f8062d7cb.webp)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。