<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f2577190cbe70305b9de13df37e1c9a",
  "translation_date": "2025-04-03T06:10:45+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# Phi 使用手册：Microsoft Phi 模型实践示例

[![在 GitHub Codespaces 中打开并使用示例](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![在 Dev Containers 中打开](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub 贡献者](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 问题](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 拉取请求](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![欢迎提交 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub 关注者](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 派生](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 星标](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI 社区 Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi 是由 Microsoft 开发的一系列开源 AI 模型。

Phi 目前是性能最强、性价比最高的小型语言模型（SLM），在多语言、推理、文本/聊天生成、代码生成、图像、音频及其他场景中表现优异。

您可以将 Phi 部署到云端或边缘设备，并且可以轻松利用有限的计算资源构建生成式 AI 应用。

按照以下步骤开始使用这些资源：
1. **Fork 仓库**：点击 [![GitHub 派生](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **克隆仓库**：   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**加入 Microsoft AI Discord 社区，与专家和开发者交流**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![封面](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.zh.png)

## 🌐 多语言支持
[法语](../fr/README.md) | [西班牙语](../es/README.md) | [德语](../de/README.md) | [俄语](../ru/README.md) | [阿拉伯语](../ar/README.md) | [波斯语 (法尔西语)](../fa/README.md) | [乌尔都语](../ur/README.md) | [中文（简体）](./README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，台湾）](../tw/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) | [印地语](../hi/README.md) | [孟加拉语](../bn/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [旁遮普语 (古木基语)](../pa/README.md) | [葡萄牙语（葡萄牙）](../pt/README.md) | [葡萄牙语（巴西）](../br/README.md) | [意大利语](../it/README.md) | [波兰语](../pl/README.md) | [土耳其语](../tr/README.md) | [希腊语](../el/README.md) | [泰语](../th/README.md) | [瑞典语](../sv/README.md) | [丹麦语](../da/README.md) | [挪威语](../no/README.md) | [芬兰语](../fi/README.md) | [荷兰语](../nl/README.md) | [希伯来语](../he/README.md) | [越南语](../vi/README.md) | [印尼语](../id/README.md) | [马来语](../ms/README.md) | [他加禄语 (菲律宾语)](../tl/README.md) | [斯瓦希里语](../sw/README.md) | [匈牙利语](../hu/README.md) | [捷克语](../cs/README.md) | [斯洛伐克语](../sk/README.md) | [罗马尼亚语](../ro/README.md) | [保加利亚语](../bg/README.md) | [塞尔维亚语（西里尔文）](../sr/README.md) | [克罗地亚语](../hr/README.md) | [斯洛文尼亚语](../sl/README.md)
## 目录

- 简介
  - [欢迎加入Phi家族](./md/01.Introduction/01/01.PhiFamily.md)
  - [设置您的环境](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [了解关键技术](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi模型的AI安全性](./md/01.Introduction/01/01.AISafety.md)
  - [Phi硬件支持](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi模型及跨平台可用性](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [使用Guidance-ai和Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace模型](https://github.com/marketplace/models)
  - [Azure AI模型目录](https://ai.azure.com)

- 在不同环境中推理Phi
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub模型](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry模型目录](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phi家族推理
    - [在iOS中推理Phi](./md/01.Introduction/03/iOS_Inference.md)
    - [在Android中推理Phi](./md/01.Introduction/03/Android_Inference.md)
    - [在Jetson中推理Phi](./md/01.Introduction/03/Jetson_Inference.md)
    - [在AI PC中推理Phi](./md/01.Introduction/03/AIPC_Inference.md)
    - [使用Apple MLX框架推理Phi](./md/01.Introduction/03/MLX_Inference.md)
    - [在本地服务器中推理Phi](./md/01.Introduction/03/Local_Server_Inference.md)
    - [使用AI工具包在远程服务器中推理Phi](./md/01.Introduction/03/Remote_Interence.md)
    - [使用Rust推理Phi](./md/01.Introduction/03/Rust_Inference.md)
    - [在本地推理Phi--Vision](./md/01.Introduction/03/Vision_Inference.md)
    - [使用Kaito AKS和Azure容器（官方支持）推理Phi](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi家族量化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [使用llama.cpp量化Phi-3.5 / 4](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [使用onnxruntime的生成式AI扩展量化Phi-3.5 / 4](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [使用Intel OpenVINO量化Phi-3.5 / 4](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [使用Apple MLX框架量化Phi-3.5 / 4](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- 评估Phi
- [负责任的AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [用于评估的Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [使用Promptflow进行评估](./md/01.Introduction/05/Promptflow.md)
 
- 使用Azure AI Search的RAG
    - [如何使用Phi-4-mini和Phi-4-multimodal（RAG）结合Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi应用开发样例
  - 文本与聊天应用
    - Phi-4 样例 🆕
      - [📓] [使用Phi-4-mini ONNX模型进行聊天](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [使用Phi-4本地ONNX模型的.NET聊天](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [使用Phi-4 ONNX和语义内核的.NET控制台聊天应用](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 样例
      - [使用Phi3、ONNX Runtime Web和WebGPU在浏览器中运行本地聊天机器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino聊天](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [多模型 - Phi-3-mini与OpenAI Whisper交互](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - 构建封装并使用Phi-3与MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [模型优化 - 如何使用Olive优化Phi-3-mini模型以适配ONNX Runtime Web](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3应用与Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3多模型AI驱动的笔记应用样例](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [使用Prompt flow微调并集成自定义Phi-3模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [在Azure AI Foundry中使用Prompt flow微调并集成自定义Phi-3模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [在Azure AI Foundry中评估微调后的Phi-3 / Phi-3.5模型，重点关注微软的负责任AI原则](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct语言预测样例（中文/英文）](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG聊天机器人](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [使用Windows GPU创建Prompt flow解决方案并结合Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [使用Microsoft Phi-3.5 tflite创建安卓应用](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [使用Microsoft.ML.OnnxRuntime结合本地ONNX Phi-3模型的问答.NET样例](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [结合语义内核和Phi-3的.NET控制台聊天应用](../../md/04.HOL/dotnet/src/LabsPhi302)

  - 基于Azure AI推理SDK的代码样例 
    - Phi-4 样例 🆕
      - [📓] [使用Phi-4-multimodal生成项目代码](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 样例
      - [使用Microsoft Phi-3系列构建自己的Visual Studio Code GitHub Copilot聊天扩展](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [使用Phi-3.5结合GitHub模型创建自己的Visual Studio Code聊天助手](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - 高级推理样例
    - Phi-4 样例 🆕
      - [📓] [Phi-4-mini推理样例](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
  
  - 演示
      - [Phi-4-mini演示托管于Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal演示托管于Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - 视觉样例
    - Phi-4 样例 🆕
      - [📓] [使用Phi-4-multimodal读取图像并生成代码](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 样例
- [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
  - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
  - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
  - [Phi-3-vision - 视觉语言助手 - 使用 Phi3-Vision 和 OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
  - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
  - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
  - [📓][Phi-3.5 Vision 多帧或多图像示例](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
  - [Phi-3 Vision 使用 Microsoft.ML.OnnxRuntime .NET 的本地 ONNX 模型](../../md/04.HOL/dotnet/src/LabsPhi303)  
  - [基于菜单的 Phi-3 Vision 使用 Microsoft.ML.OnnxRuntime .NET 的本地 ONNX 模型](../../md/04.HOL/dotnet/src/LabsPhi304)  

- 音频样例  
  - Phi-4 样例 🆕  
    - [📓] [使用 Phi-4-multimodal 提取音频转录](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal 音频样例](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal 语音翻译样例](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET 控制台应用程序使用 Phi-4-multimodal 分析音频文件并生成转录](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE 样例  
  - Phi-3 / 3.5 样例  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) 社交媒体样例](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [使用 NVIDIA NIM Phi-3 MOE、Azure AI Search 和 LlamaIndex 构建检索增强生成 (RAG) 管道](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- 函数调用样例  
  - Phi-4 样例 🆕  
    - [📓] [使用 Phi-4-mini 进行函数调用](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [使用函数调用创建多代理，使用 Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [使用 Ollama 进行函数调用](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  

- 多模态混合样例  
  - Phi-4 样例 🆕  
    - [📓] [作为技术记者使用 Phi-4-multimodal](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET 控制台应用程序使用 Phi-4-multimodal 分析图像](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi 样例微调  
  - [微调场景](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [微调与 RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [微调让 Phi-3 成为行业专家](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [使用 AI 工具包为 VS Code 微调 Phi-3](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [使用 Azure 机器学习服务微调 Phi-3](./md/03.FineTuning/Introduce_AzureML.md)  
  - [使用 Lora 微调 Phi-3](./md/03.FineTuning/FineTuning_Lora.md)  
  - [使用 QLora 微调 Phi-3](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [使用 Azure AI Foundry 微调 Phi-3](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [使用 Azure ML CLI/SDK 微调 Phi-3](./md/03.FineTuning/FineTuning_MLSDK.md)  
- [使用 Microsoft Olive 进行微调](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive 微调实践实验](./md/03.FineTuning/olive-lab/readme.md)
  - [使用 Weights and Bias 微调 Phi-3-vision](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [使用 Apple MLX 框架微调 Phi-3](./md/03.FineTuning/FineTuning_MLX.md)
  - [微调 Phi-3-vision（官方支持）](./md/03.FineTuning/FineTuning_Vision.md)
  - [使用 Kaito AKS 和 Azure Containers 微调 Phi-3（官方支持）](./md/03.FineTuning/FineTuning_Kaito.md)
  - [微调 Phi-3 和 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- 实践实验
  - [探索前沿模型：LLM、SLM、本地开发等](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [解锁 NLP 潜力：使用 Microsoft Olive 进行微调](https://github.com/azure/Ignite_FineTuning_workshop)

- 学术研究论文和出版物
  - [教科书是你唯一需要的 II：phi-1.5 技术报告](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技术报告：在手机本地运行的高能力语言模型](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技术报告](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技术报告：通过 Mixture-of-LoRAs 实现紧凑但强大的多模态语言模型](https://arxiv.org/abs/2503.01743)
  - [优化小型语言模型用于车载功能调用](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) 微调 PHI-3 以回答多项选择题：方法、结果与挑战](https://arxiv.org/abs/2501.01588)

## 使用 Phi 模型

### 在 Azure AI Foundry 上使用 Phi

您可以学习如何使用 Microsoft Phi，并在不同的硬件设备上构建端到端解决方案。要亲自体验 Phi，可以通过 [Azure AI Foundry Azure AI 模型目录](https://aka.ms/phi3-azure-ai) 开始试用模型并根据您的场景自定义 Phi。您还可以通过 [Azure AI Foundry 快速入门](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) 获取更多信息。

**Playground**
每个模型都有专属的 Playground 用于测试模型：[Azure AI Playground](https://aka.ms/try-phi3)。

### 在 GitHub 模型上使用 Phi

您可以学习如何使用 Microsoft Phi，并在不同的硬件设备上构建端到端解决方案。要亲自体验 Phi，可以通过 [GitHub 模型目录](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 开始试用模型并根据您的场景自定义 Phi。您还可以通过 [GitHub 模型目录快速入门](/md/02.QuickStart/GitHubModel_QuickStart.md) 获取更多信息。

**Playground**
每个模型都有专属的 [Playground 用于测试模型](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### 在 Hugging Face 上使用 Phi

您也可以在 [Hugging Face](https://huggingface.co/microsoft) 上找到该模型。

**Playground**
[Hugging Chat Playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 负责任的 AI

Microsoft 致力于帮助客户负责任地使用我们的 AI 产品，分享我们的经验，并通过工具（如透明性说明和影响评估）建立基于信任的合作伙伴关系。这些资源中的许多可以在 [https://aka.ms/RAI](https://aka.ms/RAI) 找到。  
Microsoft 的负责任 AI 方法基于我们的 AI 原则：公平性、可靠性和安全性、隐私和安全性、包容性、透明性和问责制。

大规模的自然语言、图像和语音模型（如本示例中使用的模型）可能会以不公平、不可靠或冒犯的方式表现，从而造成伤害。请查阅 [Azure OpenAI 服务透明性说明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) 了解相关风险和限制。

推荐的风险缓解方法是在您的架构中包含一个安全系统，以检测和防止有害行为。[Azure AI 内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview) 提供了一个独立的保护层，能够检测应用程序和服务中的用户生成和 AI 生成的有害内容。Azure AI 内容安全包括文本和图像 API，允许您检测有害内容。在 Azure AI Foundry 中，内容安全服务允许您查看、探索和试用检测不同模态有害内容的示例代码。以下 [快速入门文档](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) 指导您如何向该服务发送请求。

另一个需要考虑的方面是整体应用程序性能。在多模态和多模型应用程序中，我们认为性能意味着系统按照您和您的用户的预期运行，包括不生成有害输出。评估整体应用程序性能的重要性可以通过使用 [性能与质量以及风险与安全评估器](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) 来实现。您还可以创建和评估 [自定义评估器](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)。
您可以在开发环境中使用 [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) 来评估您的 AI 应用程序。无论是给定测试数据集还是目标，您的生成式 AI 应用程序的生成结果都可以通过内置评估器或您选择的自定义评估器进行定量测量。要开始使用 Azure AI Evaluation SDK 评估您的系统，可以参考[快速入门指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。执行评估运行后，您可以在 [Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) 中可视化结果。

## 商标

此项目可能包含项目、产品或服务的商标或标识。经授权使用 Microsoft 商标或标识必须遵守并符合 [Microsoft 商标和品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。在修改版本中使用 Microsoft 商标或标识不得引起混淆或暗示 Microsoft 赞助。任何使用第三方商标或标识的行为必须遵守这些第三方的政策。

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议寻求专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。