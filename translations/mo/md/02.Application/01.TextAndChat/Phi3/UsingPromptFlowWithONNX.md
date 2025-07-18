<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:57:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "mo"
}
-->
# 使用 Windows GPU 建立基於 Phi-3.5-Instruct ONNX 的 Prompt flow 解決方案

以下文件示範如何使用 PromptFlow 搭配 ONNX（Open Neural Network Exchange）來開發基於 Phi-3 模型的 AI 應用程式。

PromptFlow 是一套開發工具，旨在簡化基於 LLM（大型語言模型）的 AI 應用程式從構思、原型設計到測試與評估的完整開發流程。

透過整合 PromptFlow 與 ONNX，開發者可以：

- 優化模型效能：利用 ONNX 進行高效的模型推論與部署。
- 簡化開發流程：使用 PromptFlow 管理工作流程並自動化重複性任務。
- 強化團隊協作：提供統一的開發環境，促進團隊成員間的合作。

**Prompt flow** 是一套開發工具，設計用來簡化基於 LLM 的 AI 應用程式從構思、原型設計、測試、評估到生產部署與監控的完整開發週期。它讓 prompt 工程變得更加輕鬆，並幫助你打造具備生產品質的 LLM 應用。

Prompt flow 可連接 OpenAI、Azure OpenAI Service 以及可自訂的模型（Huggingface、本地 LLM/SLM）。我們希望將 Phi-3.5 的量化 ONNX 模型部署到本地應用。Prompt flow 能協助我們更好地規劃業務，並完成基於 Phi-3.5 的本地解決方案。在此範例中，我們將結合 ONNX Runtime GenAI Library，完成基於 Windows GPU 的 Prompt flow 解決方案。

## **安裝**

### **Windows GPU 版 ONNX Runtime GenAI**

請參考此指南設定 Windows GPU 版 ONNX Runtime GenAI [點此查看](./ORTWindowGPUGuideline.md)

### **在 VSCode 中設定 Prompt flow**

1. 安裝 Prompt flow VS Code 擴充功能

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.mo.png)

2. 安裝完 Prompt flow VS Code 擴充功能後，點選該擴充功能，選擇 **Installation dependencies**，依照指引在你的環境中安裝 Prompt flow SDK

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.mo.png)

3. 下載 [範例程式碼](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf)，並使用 VS Code 開啟此範例

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.mo.png)

4. 開啟 **flow.dag.yaml** 選擇你的 Python 環境

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.mo.png)

   開啟 **chat_phi3_ort.py** 修改你的 Phi-3.5-instruct ONNX 模型路徑

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.mo.png)

5. 執行你的 prompt flow 進行測試

開啟 **flow.dag.yaml**，點選視覺化編輯器

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.mo.png)

點擊後執行測試

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.mo.png)

1. 你也可以在終端機批次執行以查看更多結果


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

你可以在預設瀏覽器中查看結果


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.mo.png)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。