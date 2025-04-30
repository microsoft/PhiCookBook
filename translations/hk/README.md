<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f2577190cbe70305b9de13df37e1c9a",
  "translation_date": "2025-04-04T17:05:38+00:00",
  "source_file": "README.md",
  "language_code": "hk"
}
-->
# Phi Cookbook: 微軟 Phi 模型實戰範例

Phi 是微軟開發的一系列開源 AI 模型。

Phi 目前是最強大且具成本效益的小型語言模型 (SLM)，在多語言、推理、文本/聊天生成、程式碼、圖像、音頻及其他場景中都有非常優秀的基準表現。

你可以將 Phi 部署到雲端或邊緣設備，並且可以在有限的計算資源下輕鬆建立生成式 AI 應用。

按照以下步驟開始使用這些資源：
1. **Fork 儲存庫**：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clone 儲存庫**：   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**加入微軟 AI Discord 社群，與專家及其他開發者交流**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![封面](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.hk.png)

## 🌐 多語言支援
[法文](../fr/README.md) | [西班牙文](../es/README.md) | [德文](../de/README.md) | [俄文](../ru/README.md) | [阿拉伯文](../ar/README.md) | [波斯文（法文）](../fa/README.md) | [烏爾都文](../ur/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，香港）](./README.md) | [中文（繁體，台灣）](../tw/README.md) | [日文](../ja/README.md) | [韓文](../ko/README.md) | [印地文](../hi/README.md) | [孟加拉文](../bn/README.md) | [馬拉地文](../mr/README.md) | [尼泊爾文](../ne/README.md) | [旁遮普文（古木基文）](../pa/README.md) | [葡萄牙文（葡萄牙）](../pt/README.md) | [葡萄牙文（巴西）](../br/README.md) | [意大利文](../it/README.md) | [波蘭文](../pl/README.md) | [土耳其文](../tr/README.md) | [希臘文](../el/README.md) | [泰文](../th/README.md) | [瑞典文](../sv/README.md) | [丹麥文](../da/README.md) | [挪威文](../no/README.md) | [芬蘭文](../fi/README.md) | [荷蘭文](../nl/README.md) | [希伯來文](../he/README.md) | [越南文](../vi/README.md) | [印尼文](../id/README.md) | [馬來文](../ms/README.md) | [塔加洛文（菲律賓文）](../tl/README.md) | [斯瓦希里文](../sw/README.md) | [匈牙利文](../hu/README.md) | [捷克文](../cs/README.md) | [斯洛伐克文](../sk/README.md) | [羅馬尼亞文](../ro/README.md) | [保加利亞文](../bg/README.md) | [塞爾維亞文（西里爾文）](../sr/README.md) | [克羅地亞文](../hr/README.md) | [斯洛文尼亞文](../sl/README.md)
## 目錄

- 簡介
  - [歡迎加入 Phi 家族](./md/01.Introduction/01/01.PhiFamily.md)
  - [設置您的環境](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [了解關鍵技術](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi 模型的 AI 安全性](./md/01.Introduction/01/01.AISafety.md)
  - [Phi 硬件支持](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi 模型及其跨平台的可用性](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [使用 Guidance-ai 和 Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace 模型](https://github.com/marketplace/models)
  - [Azure AI 模型目錄](https://ai.azure.com)

- 在不同環境中推理 Phi
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub 模型](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry 模型目錄](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phi 家族推理
    - [在 iOS 中推理 Phi](./md/01.Introduction/03/iOS_Inference.md)
    - [在 Android 中推理 Phi](./md/01.Introduction/03/Android_Inference.md)
    - [在 Jetson 中推理 Phi](./md/01.Introduction/03/Jetson_Inference.md)
    - [在 AI PC 中推理 Phi](./md/01.Introduction/03/AIPC_Inference.md)
    - [使用 Apple MLX Framework 推理 Phi](./md/01.Introduction/03/MLX_Inference.md)
    - [在本地服務器中推理 Phi](./md/01.Introduction/03/Local_Server_Inference.md)
    - [使用 AI Toolkit 在遠程服務器中推理 Phi](./md/01.Introduction/03/Remote_Interence.md)
    - [使用 Rust 推理 Phi](./md/01.Introduction/03/Rust_Inference.md)
    - [在本地推理 Phi--Vision](./md/01.Introduction/03/Vision_Inference.md)
    - [使用 Kaito AKS 和 Azure Containers（官方支持）推理 Phi](./md/01.Introduction/03/Kaito_Inference.md)

-  [Phi 家族量化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [使用 llama.cpp 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [使用 onnxruntime 的生成式 AI 擴展量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [使用 Intel OpenVINO 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [使用 Apple MLX Framework 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  評估 Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry 用於評估](./md/01.Introduction/05/AIFoundry.md)  
    - [使用 Promptflow 進行評估](./md/01.Introduction/05/Promptflow.md)  

- RAG 與 Azure AI Search  
    - [如何使用 Phi-4-mini 和 Phi-4-multimodal(RAG) 配合 Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Phi 應用開發範例  
  - 文本與聊天應用  
    - Phi-4 範例 🆕  
      - [📓] [使用 Phi-4-mini ONNX 模型進行聊天](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [使用 Phi-4 本地 ONNX 模型 .NET 進行聊天](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [使用 Semantic Kernel 和 Phi-4 ONNX 的聊天 .NET 控制台應用](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 範例  
      - [使用 Phi3、ONNX Runtime Web 和 WebGPU 在瀏覽器中創建本地聊天機器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino 聊天](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [多模型 - 交互式 Phi-3-mini 和 OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - 構建封裝並使用 Phi-3 配合 MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [模型優化 - 如何使用 Olive 優化 Phi-3-mini 模型以配合 ONNX Runtime Web](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 應用使用 Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 多模型 AI 驅動筆記應用範例](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [微調並整合自定義 Phi-3 模型配合 Promptflow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [微調並整合自定義 Phi-3 模型配合 Azure AI Foundry 的 Promptflow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [在 Azure AI Foundry 中評估微調的 Phi-3 / Phi-3.5 模型，專注於 Microsoft 的負責任 AI 原則](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
      - [📓] [Phi-3.5-mini-instruct 語言預測範例（中文/英文）](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
      - [Phi-3.5-Instruct WebGPU RAG 聊天機器人](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
      - [使用 Windows GPU 創建 Phi-3.5-Instruct ONNX 的 Promptflow 解決方案](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
      - [使用 Microsoft Phi-3.5 tflite 創建 Android 應用](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
      - [使用本地 ONNX Phi-3 模型和 Microsoft.ML.OnnxRuntime 的 Q&A .NET 範例](../../md/04.HOL/dotnet/src/LabsPhi301)  
      - [使用 Semantic Kernel 和 Phi-3 的聊天 .NET 控制台應用](../../md/04.HOL/dotnet/src/LabsPhi302)  

  - Azure AI Inference SDK 基於代碼的範例  
    - Phi-4 範例 🆕  
      - [📓] [使用 Phi-4-multimodal 生成項目代碼](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
    - Phi-3 / 3.5 範例  
      - [使用 Microsoft Phi-3 系列創建自己的 Visual Studio Code GitHub Copilot 聊天](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
      - [使用 Phi-3.5 和 GitHub 模型創建自己的 Visual Studio Code 聊天 Copilot 代理](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

  - 高級推理範例  
    - Phi-4 範例 🆕  
      - [📓] [Phi-4-mini 推理範例](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  

  - 演示  
      - [Phi-4-mini 演示託管於 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
      - [Phi-4-multimodal 演示託管於 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
  - 視覺範例  
    - Phi-4 範例 🆕  
      - [📓] [使用 Phi-4-multimodal 讀取圖像並生成代碼](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
    - Phi-3 / 3.5 範例  
-  [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - 視覺語言助手 - 使用 Phi3-Vision 同 OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision 多幀或者多圖片示例](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision 本地 ONNX 模型，使用 Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [基於選單嘅 Phi-3 Vision 本地 ONNX 模型，使用 Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - 音頻示例
    - Phi-4 示例 🆕
      - [📓] [使用 Phi-4-multimodal 提取音頻文本](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal 音頻示例](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal 語音翻譯示例](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET 控制台應用，使用 Phi-4-multimodal 分析音頻文件並生成文本](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE 示例
    - Phi-3 / 3.5 示例
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) 社交媒體示例](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [用 NVIDIA NIM Phi-3 MOE、Azure AI Search 同 LlamaIndex 構建檢索增強生成 (RAG) 流程](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - 函數調用示例
    - Phi-4 示例 🆕
      -  [📓] [使用 Phi-4-mini 進行函數調用](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [使用函數調用創建多代理人，使用 Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [使用函數調用同 Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - 多模態混合示例
    - Phi-4 示例 🆕
      -  [📓] [使用 Phi-4-multimodal 作為科技記者](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET 控制台應用，使用 Phi-4-multimodal 分析圖片](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi 微調示例
  - [微調場景](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [微調 vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [微調 Phi-3 成為行業專家](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [使用 AI Toolkit for VS Code 微調 Phi-3](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [使用 Azure Machine Learning Service 微調 Phi-3](./md/03.FineTuning/Introduce_AzureML.md)
  - [使用 Lora 微調 Phi-3](./md/03.FineTuning/FineTuning_Lora.md)
  - [使用 QLora 微調 Phi-3](./md/03.FineTuning/FineTuning_Qlora.md)
  - [使用 Azure AI Foundry 微調 Phi-3](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [使用 Azure ML CLI/SDK 微調 Phi-3](./md/03.FineTuning/FineTuning_MLSDK.md)
- [使用 Microsoft Olive 進行微調](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive 微調實操實驗室](./md/03.FineTuning/olive-lab/readme.md)
  - [使用 Weights and Bias 微調 Phi-3-vision](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [使用 Apple MLX 框架微調 Phi-3](./md/03.FineTuning/FineTuning_MLX.md)
  - [微調 Phi-3-vision（官方支持）](./md/03.FineTuning/FineTuning_Vision.md)
  - [使用 Kaito AKS 和 Azure Containers 微調 Phi-3（官方支持）](./md/03.FineTuning/FineTuning_Kaito.md)
  - [微調 Phi-3 和 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- 實操實驗室
  - [探索前沿模型：LLMs、SLMs、本地開發等](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [解鎖 NLP 潛力：使用 Microsoft Olive 進行微調](https://github.com/azure/Ignite_FineTuning_workshop)

- 學術研究論文及出版物
  - [Textbooks Are All You Need II: phi-1.5 技術報告](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技術報告：高效的語言模型可在手機本地運行](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技術報告](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技術報告：通過 LoRA 混合構建緊湊但強大的多模態語言模型](https://arxiv.org/abs/2503.01743)
  - [優化小型語言模型以支持車內功能調用](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) 微調 PHI-3 以應對多選題回答：方法論、結果及挑戰](https://arxiv.org/abs/2501.01588)

## 使用 Phi 模型

### Phi 在 Azure AI Foundry

您可以學習如何使用 Microsoft Phi，並在不同硬件設備上構建端到端解決方案。若要親身體驗 Phi，請從測試模型並根據您的場景定制 Phi 開始，使用 [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)。您可以在 [Azure AI Foundry 快速入門](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) 中了解更多。

**Playground**
每個模型都有專屬的 Playground 來測試模型 [Azure AI Playground](https://aka.ms/try-phi3)。

### Phi 在 GitHub 模型

您可以學習如何使用 Microsoft Phi，並在不同硬件設備上構建端到端解決方案。若要親身體驗 Phi，請從測試模型並根據您的場景定制 Phi 開始，使用 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)。您可以在 [GitHub Model Catalog 快速入門](/md/02.QuickStart/GitHubModel_QuickStart.md) 中了解更多。

**Playground**
每個模型都有專屬的 [Playground 測試模型](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Phi 在 Hugging Face

您也可以在 [Hugging Face](https://huggingface.co/microsoft) 上找到模型。

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 負責任的 AI 

Microsoft 致力於幫助客戶負責任地使用我們的 AI 產品，分享我們的經驗，並通過透明性說明和影響評估等工具建立基於信任的合作關係。許多資源可以在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。
Microsoft 的負責任 AI 方法基於我們的 AI 原則：公平性、可靠性和安全性、隱私和安全性、包容性、透明性以及問責制。

大型自然語言、圖像和語音模型（例如此示例中使用的模型）可能會以不公平、不可靠或冒犯的方式表現，進而導致傷害。請參考 [Azure OpenAI 服務透明性說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 了解相關風險和限制。

建議的風險緩解方法是在您的架構中加入安全系統，該系統能檢測並防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供了獨立的保護層，可以檢測應用和服務中的用戶生成內容及 AI 生成內容是否有害。Azure AI Content Safety 包括文本和圖像 API，能幫助您檢測有害材料。在 Azure AI Foundry 中，Content Safety 服務允許您查看、探索和試用示例代碼以檢測不同模式下的有害內容。以下 [快速入門文檔](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 將指導您如何向服務發送請求。

另一個需要考慮的方面是整體應用性能。對於多模態和多模型應用，我們認為性能是指系統能如您和您的用戶所期望地運行，包括不生成有害輸出。評估整體應用性能時，請使用 [Performance and Quality 和 Risk and Safety 評估工具](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。此外，您還可以創建和使用 [自定義評估工具](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)。
你可以在你的開發環境中使用 [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) 來評估你的 AI 應用程式。無論是測試數據集還是目標，你的生成式 AI 應用程式的生成結果都可以通過內建的評估器或你選擇的自訂評估器進行量化測量。要開始使用 Azure AI Evaluation SDK 來評估你的系統，可以參考 [快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。執行評估後，你可以在 [Azure AI Foundry 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

這個專案可能包含與專案、產品或服務相關的商標或標誌。授權使用 Microsoft 商標或標誌必須遵守並符合 [Microsoft 的商標與品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。在修改版本的專案中使用 Microsoft 商標或標誌不得造成混淆或暗示 Microsoft 的贊助。任何第三方商標或標誌的使用需遵守該第三方的政策。

**免責聲明**：  
本文檔已使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。