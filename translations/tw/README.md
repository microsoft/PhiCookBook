<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f133aeb5a2b33942b50a761d56389d91",
  "translation_date": "2025-07-09T16:23:23+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
# Phi Cookbook：Microsoft Phi 模型的實作範例

[![在 GitHub Codespaces 開啟並使用範例](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![在 Dev Containers 開啟](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub 觀察者](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub 分支](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub 星標](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi 是由 Microsoft 開發的一系列開源 AI 模型。

Phi 目前是最強大且具成本效益的小型語言模型（SLM），在多語言、推理、文本/聊天生成、程式碼、影像、音訊及其他場景中都有優異的基準表現。

你可以將 Phi 部署到雲端或邊緣裝置，並且能輕鬆地在有限的運算資源下構建生成式 AI 應用。

請依照以下步驟開始使用這些資源：  
1. **Fork 此倉庫**：點擊 [![GitHub 分支](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Clone 倉庫**：`git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**加入 Microsoft AI Discord 社群，與專家及開發者交流**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.tw.png)

## 🌐 多語言支援

### 透過 GitHub Action 支援（自動且持續更新）

[法文](../fr/README.md) | [西班牙文](../es/README.md) | [德文](../de/README.md) | [俄文](../ru/README.md) | [阿拉伯文](../ar/README.md) | [波斯文 (Farsi)](../fa/README.md) | [烏爾都語](../ur/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，香港）](../hk/README.md) | [中文（繁體，台灣）](./README.md) | [日文](../ja/README.md) | [韓文](../ko/README.md) | [印地語](../hi/README.md)

### 透過 CLI 支援

[孟加拉文](../bn/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [旁遮普語 (Gurmukhi)](../pa/README.md) | [葡萄牙語（葡萄牙）](../pt/README.md) | [葡萄牙語（巴西）](../br/README.md) | [義大利語](../it/README.md) | [波蘭語](../pl/README.md) | [土耳其語](../tr/README.md) | [希臘語](../el/README.md) | [泰語](../th/README.md) | [瑞典語](../sv/README.md) | [丹麥語](../da/README.md) | [挪威語](../no/README.md) | [芬蘭語](../fi/README.md) | [荷蘭語](../nl/README.md) | [希伯來語](../he/README.md) | [越南語](../vi/README.md) | [印尼語](../id/README.md) | [馬來語](../ms/README.md) | [他加祿語（菲律賓語）](../tl/README.md) | [斯瓦希里語](../sw/README.md) | [匈牙利語](../hu/README.md) | [捷克語](../cs/README.md) | [斯洛伐克語](../sk/README.md) | [羅馬尼亞語](../ro/README.md) | [保加利亞語](../bg/README.md) | [塞爾維亞語（西里爾字母）](../sr/README.md) | [克羅埃西亞語](../hr/README.md) | [斯洛維尼亞語](../sl/README.md)

## 目錄

- 介紹  
  - [歡迎加入 Phi 家族](./md/01.Introduction/01/01.PhiFamily.md)  
  - [環境設定](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [關鍵技術解析](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Phi 模型的 AI 安全性](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi 硬體支援](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi 模型與跨平台可用性](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [使用 Guidance-ai 與 Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub Marketplace 模型](https://github.com/marketplace/models)  
  - [Azure AI 模型目錄](https://ai.azure.com)

- 在不同環境中推論 Phi  
  - [Hugging face](./md/01.Introduction/02/01.HF.md)  
  - [GitHub 模型](./md/01.Introduction/02/02.GitHubModel.md)  
  - [Azure AI Foundry 模型目錄](./md/01.Introduction/02/03.AzureAIFoundry.md)  
  - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
  - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
  - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
  - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi 家族推論  
  - [iOS 上的 Phi 推論](./md/01.Introduction/03/iOS_Inference.md)  
  - [Android 上的 Phi 推論](./md/01.Introduction/03/Android_Inference.md)  
  - [Jetson 上的 Phi 推論](./md/01.Introduction/03/Jetson_Inference.md)  
  - [AI PC 上的 Phi 推論](./md/01.Introduction/03/AIPC_Inference.md)  
  - [使用 Apple MLX Framework 的 Phi 推論](./md/01.Introduction/03/MLX_Inference.md)  
  - [本地伺服器上的 Phi 推論](./md/01.Introduction/03/Local_Server_Inference.md)  
  - [使用 AI Toolkit 在遠端伺服器上推論 Phi](./md/01.Introduction/03/Remote_Interence.md)  
  - [使用 Rust 推論 Phi](./md/01.Introduction/03/Rust_Inference.md)  
  - [本地端 Phi--Vision 推論](./md/01.Introduction/03/Vision_Inference.md)  
  - [使用 Kaito AKS、Azure Containers（官方支援）推論 Phi](./md/01.Introduction/03/Kaito_Inference.md)

- Phi 家族量化  
  - [使用 llama.cpp 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
  - [使用 onnxruntime 的生成式 AI 擴充功能量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
  - [使用 Intel OpenVINO 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
  - [使用 Apple MLX Framework 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi 評估  
  - [負責任的 AI](./md/01.Introduction/05/ResponsibleAI.md)  
  - [使用 Azure AI Foundry 進行評估](./md/01.Introduction/05/AIFoundry.md)  
  - [使用 Promptflow 進行評估](./md/01.Introduction/05/Promptflow.md)

- 使用 Azure AI Search 的 RAG  
  - [如何使用 Phi-4-mini 和 Phi-4-multimodal (RAG) 搭配 Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi 應用開發範例  
  - 文字與聊天應用  
    - Phi-4 範例 🆕  
      - [📓] [與 Phi-4-mini ONNX 模型聊天](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [使用 Phi-4 本地 ONNX 模型的聊天 .NET 範例](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [使用 Semantic Kernel 的 Phi-4 ONNX 聊天 .NET 主控台應用](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 範例  
      - [使用 Phi3、ONNX Runtime Web 和 WebGPU 在瀏覽器中本地聊天機器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino 聊天](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [多模型 - 互動式 Phi-3-mini 與 OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - 建立包裝器並使用 Phi-3 與 MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [模型優化 - 如何使用 Olive 優化 Phi-3-mini 模型以適用於 ONNX Runtime Web](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [使用 Phi-3 mini-4k-instruct-onnx 的 WinUI3 應用](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 多模型 AI 助力筆記應用範例](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [使用 Prompt flow 微調並整合自訂 Phi-3 模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [在 Azure AI Foundry 中使用 Prompt flow 微調並整合自訂 Phi-3 模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [在 Azure AI Foundry 中評估微調後的 Phi-3 / Phi-3.5 模型，聚焦於微軟的負責任 AI 原則](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct 語言預測範例（中/英文）](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG 聊天機器人](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [使用 Windows GPU 與 Phi-3.5-Instruct ONNX 建立 Prompt flow 解決方案](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [使用 Microsoft Phi-3.5 tflite 建立 Android 應用程式](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [使用 Microsoft.ML.OnnxRuntime 的本地 ONNX Phi-3 模型 .NET 問答範例](../../md/04.HOL/dotnet/src/LabsPhi301)
- [結合 Semantic Kernel 與 Phi-3 的 .NET 主控台聊天應用程式](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI 推論 SDK 程式碼範例  
  - Phi-4 範例 🆕  
    - [📓] [使用 Phi-4-multimodal 產生專案程式碼](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 範例  
    - [使用 Microsoft Phi-3 系列打造自己的 Visual Studio Code GitHub Copilot Chat](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [使用 GitHub 模型與 Phi-3.5 建立自己的 Visual Studio Code Chat Copilot 代理人](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- 進階推理範例  
  - Phi-4 範例 🆕  
    - [📓] [Phi-4-mini-reasoning 或 Phi-4-reasoning 範例](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [使用 Microsoft Olive 微調 Phi-4-mini-reasoning](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [使用 Apple MLX 微調 Phi-4-mini-reasoning](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [使用 GitHub 模型的 Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [使用 Azure AI Foundry 模型的 Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- 示範  
    - [Phi-4-mini 示範，託管於 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal 示範，託管於 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- 視覺範例  
  - Phi-4 範例 🆕  
    - [📓] [使用 Phi-4-multimodal 讀取影像並產生程式碼](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 範例  
    - [📓][Phi-3-vision-影像文字轉文字](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP 嵌入](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [示範：Phi-3 回收](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - 視覺語言助理 - 結合 Phi3-Vision 與 OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision 多幀或多影像範例](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [使用 Microsoft.ML.OnnxRuntime .NET 的 Phi-3 Vision 本地 ONNX 模型](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [基於選單的 Phi-3 Vision 本地 ONNX 模型，使用 Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- 數學範例  
  - Phi-4-Mini-Flash-Reasoning-Instruct 範例 🆕 [使用 Phi-4-Mini-Flash-Reasoning-Instruct 的數學示範](../../md/02.Application/09.Math/MathDemo.ipynb)  

- 音訊範例  
  - Phi-4 範例 🆕  
    - [📓] [使用 Phi-4-multimodal 擷取音訊文字稿](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal 音訊範例](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal 語音翻譯範例](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [使用 Phi-4-multimodal 的 .NET 主控台應用程式，分析音訊檔並產生文字稿](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE 範例  
  - Phi-3 / 3.5 範例  
    - [📓] [Phi-3.5 專家混合模型 (MoEs) 社群媒體範例](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [使用 NVIDIA NIM Phi-3 MOE、Azure AI Search 與 LlamaIndex 建立檢索增強生成 (RAG) 流程](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- 函式呼叫範例  
  - Phi-4 範例 🆕  
    - [📓] [使用 Phi-4-mini 的函式呼叫](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [使用函式呼叫建立多代理人系統，搭配 Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [使用函式呼叫搭配 Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [使用函式呼叫搭配 ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- 多模態混合範例  
  - Phi-4 範例 🆕  
    - [📓] [使用 Phi-4-multimodal 擔任科技記者](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [使用 Phi-4-multimodal 的 .NET 主控台應用程式分析影像](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi 微調範例  
  - [微調情境](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [微調與 RAG 比較](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [微調讓 Phi-3 成為產業專家](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [使用 AI Toolkit for VS Code 微調 Phi-3](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [使用 Azure Machine Learning Service 微調 Phi-3](./md/03.FineTuning/Introduce_AzureML.md)  
  - [使用 Lora 微調 Phi-3](./md/03.FineTuning/FineTuning_Lora.md)  
  - [使用 QLora 微調 Phi-3](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [使用 Azure AI Foundry 微調 Phi-3](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [使用 Azure ML CLI/SDK 微調 Phi-3](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [使用 Microsoft Olive 微調](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive 實作實驗室](./md/03.FineTuning/olive-lab/readme.md)  
  - [使用 Weights and Bias 微調 Phi-3-vision](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [使用 Apple MLX Framework 微調 Phi-3](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision 微調（官方支援）](./md/03.FineTuning/FineTuning_Vision.md)  
  - [使用 Kaito AKS、Azure Containers 微調 Phi-3（官方支援）](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 與 3.5 Vision 微調](https://github.com/2U1/Phi3-Vision-Finetune)  

- 實作實驗室  
  - [探索尖端模型：LLMs、SLMs、本地開發等](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [釋放 NLP 潛力：使用 Microsoft Olive 進行微調](https://github.com/azure/Ignite_FineTuning_workshop)  

- 學術研究論文與出版物  
  - [Textbooks Are All You Need II: phi-1.5 技術報告](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 技術報告：在手機上運行的高效能語言模型](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 技術報告](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini 技術報告：透過 LoRA 混合打造緊湊且強大的多模態語言模型](https://arxiv.org/abs/2503.01743)  
  - [優化車載功能呼叫用小型語言模型](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) 微調 PHI-3 用於多選題問答：方法、結果與挑戰](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning 技術報告](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning 技術報告](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## 使用 Phi 模型

### 在 Azure AI Foundry 上使用 Phi

您可以學習如何使用 Microsoft Phi 以及如何在不同硬體設備上構建端到端解決方案。想親自體驗 Phi，請先透過 [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 試玩模型並根據您的場景自訂 Phi。更多資訊請參考 [Azure AI Foundry 快速入門](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)。

**Playground**  
每個模型都有專屬的測試平台，您可以在 [Azure AI Playground](https://aka.ms/try-phi3) 試用模型。

### 在 GitHub Models 上使用 Phi

您可以學習如何使用 Microsoft Phi 以及如何在不同硬體設備上構建端到端解決方案。想親自體驗 Phi，請先透過 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 試玩模型並根據您的場景自訂 Phi。更多資訊請參考 [GitHub Model Catalog 快速入門](/md/02.QuickStart/GitHubModel_QuickStart.md)。

**Playground**  
每個模型都有專屬的[測試平台](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### 在 Hugging Face 上使用 Phi

您也可以在 [Hugging Face](https://huggingface.co/microsoft) 找到這些模型。

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 負責任的 AI

Microsoft 致力於協助客戶負責任地使用我們的 AI 產品，分享我們的經驗，並透過 Transparency Notes 和 Impact Assessments 等工具建立基於信任的合作關係。許多相關資源可在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。  
Microsoft 的負責任 AI 方法基於我們的 AI 原則：公平性、可靠性與安全性、隱私與安全、包容性、透明度及問責制。

大型自然語言、影像和語音模型——如本範例中使用的模型——可能會出現不公平、不可靠或冒犯性的行為，進而造成傷害。請參考 [Azure OpenAI 服務 Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解相關風險與限制。

建議的風險緩解方法是在架構中加入安全系統，能夠偵測並防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立的保護層，能偵測應用程式和服務中使用者生成及 AI 生成的有害內容。Azure AI Content Safety 包含文字和影像 API，讓您能偵測有害素材。在 Azure AI Foundry 中，Content Safety 服務讓您能查看、探索並試用跨不同模態偵測有害內容的範例程式碼。以下的[快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)將引導您如何向該服務發送請求。

另一個需要考慮的面向是整體應用程式的效能。對於多模態和多模型應用，我們認為效能是指系統能如您和使用者所期望地運作，包括不產生有害輸出。評估整體應用程式效能時，建議使用[效能與品質以及風險與安全評估工具](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。您也可以使用[自訂評估工具](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)來建立和評估。

您可以在開發環境中使用 [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) 評估您的 AI 應用。無論是測試資料集或目標，您的生成式 AI 應用產出都能透過內建或自訂評估工具進行量化評估。想開始使用 Azure AI Evaluation SDK 評估系統，請參考[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，您可以在 [Azure AI Foundry 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。授權使用 Microsoft 商標或標誌須遵守並遵循 [Microsoft 商標與品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。  
在本專案的修改版本中使用 Microsoft 商標或標誌，不得造成混淆或暗示 Microsoft 贊助。任何第三方商標或標誌的使用均須遵守該第三方的相關政策。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。