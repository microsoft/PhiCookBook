# Phi Cookbook: 使用 Microsoft Phi 模型的實作範例

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi 是由 Microsoft 開發的一系列開源 AI 模型。

Phi 目前是最強大且具成本效益的小型語言模型（SLM），在多語言、推理、文本/聊天生成、程式碼、圖像、音訊及其他應用場景中表現非常優異。

您可以將 Phi 部署到雲端或邊緣設備，並且輕鬆使用有限的運算能力來構建生成式 AI 應用程式。

請按照以下步驟開始使用這些資源：
1. <strong>複製儲存庫分支</strong>：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. <strong>克隆儲存庫</strong>：   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**加入 Microsoft AI Discord 社區，認識專家與開發者夥伴**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/zh-HK/cover.eb18d1b9605d754b.webp)

### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動且持續更新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](./README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **想本地克隆？**
>
> 此儲存庫包含超過 50 種語言翻譯，會大幅增加下載大小。若要不帶翻譯克隆，請用稀疏檢出：
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 這樣可以讓您以更快速度取得完成課程所需的所有內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 目錄
- 簡介 - [歡迎來到Phi家族](./md/01.Introduction/01/01.PhiFamily.md) - [設置您的環境](./md/01.Introduction/01/01.EnvironmentSetup.md) - [了解關鍵技術](./md/01.Introduction/01/01.Understandingtech.md) - [Phi模型的AI安全](./md/01.Introduction/01/01.AISafety.md) - [Phi硬件支援](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi模型及跨平台可用性](./md/01.Introduction/01/01.Edgeandcloud.md) - [使用Guidance-ai和Phi](./md/01.Introduction/01/01.Guidance.md) - [GitHub市場模型](https://github.com/marketplace/models) - [Azure AI模型目錄](https://ai.azure.com) - 在不同環境中推理Phi - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub模型](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry模型目錄](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI工具包VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - Phi家族的推理 - [iOS上的Phi推理](./md/01.Introduction/03/iOS_Inference.md) - [Android上的Phi推理](./md/01.Introduction/03/Android_Inference.md) - [Jetson上的Phi推理](./md/01.Introduction/03/Jetson_Inference.md) - [AI PC上的Phi推理](./md/01.Introduction/03/AIPC_Inference.md) - [使用Apple MLX框架進行Phi推理](./md/01.Introduction/03/MLX_Inference.md) - [本地服務器上的Phi推理](./md/01.Introduction/03/Local_Server_Inference.md) - [使用AI工具包在遠端服務器上推理Phi](./md/01.Introduction/03/Remote_Interence.md) - [使用Rust推理Phi](./md/01.Introduction/03/Rust_Inference.md) - [在本地進行Phi視覺推理](./md/01.Introduction/03/Vision_Inference.md) - [使用Kaito AKS、Azure容器進行Phi推理（官方支援）](./md/01.Introduction/03/Kaito_Inference.md) - [Phi家族的量化](./md/01.Introduction/04/QuantifyingPhi.md) - [使用llama.cpp量化Phi-3.5 / 4](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [使用onnxruntime生成式AI擴展量化Phi-3.5 / 4](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [使用Intel OpenVINO量化Phi-3.5 / 4](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [使用Apple MLX框架量化Phi-3.5 / 4](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Phi的評估 - [負責任的AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry的評估](./md/01.Introduction/05/AIFoundry.md) - [使用Promptflow進行評估](./md/01.Introduction/05/Promptflow.md) - Azure AI搜索的RAG - [如何使用Phi-4-mini和Phi-4-multimodal(RAG)與Azure AI搜索](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi應用開發範例 - 文字和聊天應用程式 - Phi-4範例 - [📓] [與Phi-4-mini ONNX模型聊天](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [使用Phi-4本地ONNX模型 .NET聊天](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [使用Semantic Kernel和Phi-4的.NET控制台聊天應用程式](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5範例 - [使用Phi3、ONNX Runtime Web和WebGPU在瀏覽器本地聊天機器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino聊天](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [多模型 - 互動式Phi-3-mini與OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - 建立包裝器並使用Phi-3與MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [模型優化 - 如何使用Olive優化Phi-3-mini模型以適用於ONNX Runtime Web](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [使用Phi-3 mini-4k-instruct-onnx的WinUI3應用程式](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[WinUI3多模型AI驅動筆記應用範例](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [使用Prompt flow微調並整合自訂Phi-3模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [使用Microsoft Foundry中的Prompt flow微調並整合自訂Phi-3模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [在Microsoft Foundry評估微調的Phi-3 / Phi-3.5模型，聚焦Microsoft的負責任AI原則](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct語言預測範例（中文/英文）](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG聊天機器人](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [使用Windows GPU及Phi-3.5-Instruct ONNX創建Prompt flow解決方案](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [使用Microsoft Phi-3.5 tflite創建Android應用程式](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [使用本地ONNX Phi-3模型與Microsoft.ML.OnnxRuntime的問答.NET範例](../../md/04.HOL/dotnet/src/LabsPhi301) - [使用Semantic Kernel和Phi-3的.NET控制台聊天應用程式](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI推理SDK基於代碼的範例 - Phi-4範例 - [📓] [使用Phi-4-multimodal生成專案代碼](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5範例 - [使用Microsoft Phi-3家族打造您自己的Visual Studio Code GitHub Copilot聊天](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [用GitHub模型用Phi-3.5為Visual Studio Code創建聊天Copilot代理](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - 進階推理範例 - Phi-4範例 - [📓] [Phi-4-mini推理或Phi-4推理範例](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [使用Microsoft Olive微調Phi-4-mini推理](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [使用Apple MLX微調Phi-4-mini推理](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini推理與GitHub模型](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini推理與Microsoft Foundry模型](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
示範 - [Phi-4-mini 示範託管於 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodal 示範託管於 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - 視覺範例 - Phi-4 範例 - [📓] [使用 Phi-4-multimodal 讀取圖片並生成代碼](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 範例 - [📓][Phi-3-vision-圖像文字轉文字](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP 嵌入](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [示範：Phi-3 回收](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - 視覺語言助手 - 結合 Phi3-Vision 及 OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision 多幀或多圖像範例](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision 本地 ONNX 模型 使用 Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [基於選單的 Phi-3 Vision 本地 ONNX 模型 使用 Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - 推理與視覺範例 - Phi-4-Reasoning-Vision-15B - [📓] [使用 Phi-4-Reasoning-Vision-15B 檢測闖紅燈行人](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [使用 Phi-4-Reasoning-Vision-15B 進行數學運算](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [使用 Phi-4-Reasoning-Vision-15B 偵測使用者介面](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - 數學範例 - Phi-4-Mini-Flash-Reasoning-Instruct 範例 [Phi-4-Mini-Flash-Reasoning-Instruct 數學示範](./md/02.Application/09.Math/MathDemo.ipynb) - 音訊範例 - Phi-4 範例 - [📓] [使用 Phi-4-multimodal 擷取音訊文字稿](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodal 音訊示範](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodal 語音翻譯示範](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET 控制台應用程序 使用 Phi-4-multimodal 音訊分析音訊文件並生成文字稿](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MoE 範例 - Phi-3 / 3.5 範例 - [📓] [Phi-3.5 多專家模型 (MoEs) 社交媒體示範](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [使用 NVIDIA NIM Phi-3 MOE、Azure AI 搜尋及 LlamaIndex 建立檢索增強生成功能 (RAG) 管道](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - 功能呼叫範例 - Phi-4 範例 🆕 - [📓] [使用 Phi-4-mini 進行功能呼叫](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [使用功能呼叫建立多代理與 Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [與 Ollama 一起使用功能呼叫](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [使用 ONNX 進行功能呼叫](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - 多模態混合範例 - Phi-4 範例 🆕 - [📓] [使用 Phi-4-multimodal 擔任科技記者](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET 控制台應用程序 使用 Phi-4-multimodal 分析圖片](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - 微調 Phi 範例 - [微調情境](./md/03.FineTuning/FineTuning_Scenarios.md) - [微調與 RAG 比較](./md/03.FineTuning/FineTuning_vs_RAG.md) - [微調讓 Phi-3 成為產業專家](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [使用 AI 工具包於 VS Code 微調 Phi-3](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [使用 Azure 機器學習服務微調 Phi-3](./md/03.FineTuning/Introduce_AzureML.md) - [用 Lora 微調 Phi-3](./md/03.FineTuning/FineTuning_Lora.md) - [用 QLora 微調 Phi-3](./md/03.FineTuning/FineTuning_Qlora.md) - [用 Microsoft Foundry 微調 Phi-3](./md/03.FineTuning/FineTuning_AIFoundry.md) - [使用 Azure ML CLI/SDK 微調 Phi-3](./md/03.FineTuning/FineTuning_MLSDK.md) - [用 Microsoft Olive 微調](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Microsoft Olive 實驗室操作](./md/03.FineTuning/olive-lab/readme.md) - [使用 Weights and Bias 微調 Phi-3-vision](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [用 Apple MLX 框架微調 Phi-3](./md/03.FineTuning/FineTuning_MLX.md) - [官方支援的 Phi-3-vision 微調](./md/03.FineTuning/FineTuning_Vision.md) - [Kaito AKS、Azure 容器官方支援的 Phi-3 微調](./md/03.FineTuning/FineTuning_Kaito.md) - [Phi-3 與 3.5 Vision 微調](https://github.com/2U1/Phi3-Vision-Finetune) - 實驗室操作 - [探索尖端模型：大型語言模型 (LLMs)、小型語言模型 (SLMs)、本地開發等等](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [解鎖自然語言處理潛力：使用 Microsoft Olive 進行微調](https://github.com/azure/Ignite_FineTuning_workshop) - 學術研究論文與出版物 - [Textbooks Are All You Need II: phi-1.5 技術報告](https://arxiv.org/abs/2309.05463) - [Phi-3 技術報告：本地手機上的高能力語言模型](https://arxiv.org/abs/2404.14219) - [Phi-4 技術報告](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini 技術報告：透過混合 LoRAs 的緊湊而強大的多模態語言模型](https://arxiv.org/abs/2503.01743) - [優化車載功能呼叫的小型語言模型](https://arxiv.org/abs/2501.02342) - [(WhyPHI) 微調 PHI-3 用於多選題問答：方法論、結果與挑戰](https://arxiv.org/abs/2501.01588) - [Phi-4推理技術報告](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini推理技術報告](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: Microsoft Phi 模型實作範例

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi 是微軟開發的一系列開源 AI 模型。

Phi 目前是最強大又具成本效益的小型語言模型 (SLM)，在多語言、推理、文本/聊天生成、編碼、圖像、音頻等多種場景中表現卓越。

你可以將 Phi 部署在雲端或邊緣設備上，並且能夠輕鬆使用有限的計算能力建構生成式 AI 應用。

請依照以下步驟開始使用這些資源：
1. **Fork 本儲存庫**：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. <strong>克隆儲存庫</strong>： `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**加入 Microsoft AI Discord 社群，認識專家與開發者夥伴**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/zh-HK/cover.eb18d1b9605d754b.webp)

### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動化且持續更新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [中文 (簡體)](../zh-CN/README.md) | [中文 (繁體，香港)](./README.md) | [中文 (繁體，澳門)](../zh-MO/README.md) | [中文 (繁體，台灣)](../zh-TW/README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [卡納達語](../kn/README.md) | [高棉語](../km/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (Farsi)](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語 (巴西)](../pt-BR/README.md) | [葡萄牙語 (葡萄牙)](../pt-PT/README.md) | [旁遮普語 (Gurmukhi)](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語 (西里爾文)](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [塔加洛語 (菲律賓語)](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **想要本地克隆？**
>
> 此儲存庫包含 50 多種語言的翻譯，會大幅增加下載大小。若想下載不含翻譯的版本，請使用稀疏簽出：
>
> **Bash / macOS / Linux：**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows)：**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 這樣可讓你以更快的速度完成課程所需的所有內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 目錄

## 使用 Phi 模型

### Microsoft Foundry上的 Phi

你可以學習如何使用 Microsoft Phi，並在不同硬體設備上建立端到端解決方案。若想親身體驗 Phi，請先試玩模型並利用 [Microsoft Foundry Azure AI 模型目錄](https://aka.ms/phi3-azure-ai) 針對你的場景自訂 Phi，詳細資訊請見從 [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) 快速入門。

<strong>遊樂場</strong>
每個模型都有專屬的遊樂場供測試模型用 [Azure AI Playground](https://aka.ms/try-phi3)。

### GitHub 模型上的 Phi

你可以學習如何使用 Microsoft Phi，並在不同硬體設備上建立端到端解決方案。若想親身體驗 Phi，請先試玩模型並利用 [GitHub 模型目錄](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 針對你的場景自訂 Phi，詳細資訊請見從 [GitHub 模型目錄](/md/02.QuickStart/GitHubModel_QuickStart.md) 快速入門。

<strong>遊樂場</strong>
每個模型都有專屬的[遊樂場供測試模型用](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Hugging Face上的 Phi

你也可以在 [Hugging Face](https://huggingface.co/microsoft) 找到該模型。

<strong>遊樂場</strong>
 [Hugging Chat 遊樂場](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 其他課程

我們團隊提供其他課程！請參考：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 負責任的人工智能

微軟致力於協助我們的客戶負責任地使用我們的人工智能產品，分享我們的經驗，並透過如 Transparency Notes 和 Impact Assessments 等工具建立基於信任的合作夥伴關係。許多這些資源可於 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。  
微軟對負責任人工智能的做法基於我們的AI原則：公平性、可靠性與安全性、隱私與安全、包容性、透明度及問責制。

大型自然語言、影像及語音模型——例如本範例所用的模型——可能會表現出不公平、不可靠或冒犯性的行為，進而造成傷害。請參考 [Azure OpenAI 服務透明度說明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 以了解風險及限制。

減輕這些風險的建議方法是於您的架構加入安全系統，能檢測並防止有害行為。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供獨立保護層，能在應用程式與服務中檢測使用者與 AI 產生的有害內容。Azure AI Content Safety 包含可檢測有害材質的文字與影像 API。在 Microsoft Foundry 中，Content Safety 服務允許您查看、瀏覽及試用不同模式有害內容檢測的範例程式碼。以下的 [快速入門文件](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 導引您如何向服務提交請求。

另一個要考慮的層面是整體應用程式效能。對於多模態及多模型的應用，我們認為效能指系統如您及使用者所期望地運作，包括不產生有害輸出。評估您整體應用程式效能時，可使用 [效能與品質，以及風險和安全評估器](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。您也可以創建並使用 [自訂評估器](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)進行評估。

您可以在開發環境中使用 [Azure AI 評估 SDK](https://microsoft.github.io/promptflow/index.html) 評估您的 AI 應用程式。給定測試資料集或目標，您生成的 AI 輸出會被內建或自訂評估器以數據方式衡量。開始使用 Azure AI 評估 SDK 評估系統請遵循[快速入門指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。完成評估執行後，您可以在 [Microsoft Foundry 中視覺化結果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

本專案可能包含專案、產品或服務的商標或標誌。授權使用微軟商標或標誌，須依據且遵守 [微軟商標及品牌使用指引](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。  
於本專案修改版本中使用微軟商標或標誌，不得造成混淆或暗示微軟贊助。任何第三方商標或標誌使用，均須遵守該第三方相關政策。

## 尋求協助

若您遇到困難或對構建 AI 應用有任何疑問，歡迎加入：

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

若您在開發過程中有產品反饋或錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威資料來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用此翻譯所引起的任何誤解或錯誤解釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->