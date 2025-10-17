<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:08:45+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
# Phi 烹饪手册：微软 Phi 模型的实践示例

[![在 GitHub Codespaces 中打开并使用示例](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![在 Dev Containers 中打开](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub 贡献者](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 问题](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 拉取请求](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![欢迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub 关注者](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 分叉](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 星标](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi 是微软开发的一系列开源 AI 模型。

Phi 是目前最强大且性价比最高的小型语言模型（SLM），在多语言、推理、文本/聊天生成、编程、图像、音频及其他场景中表现优异。

您可以将 Phi 部署到云端或边缘设备，并且可以轻松利用有限的计算资源构建生成式 AI 应用。

按照以下步骤开始使用这些资源：
1. **分叉仓库**：点击 [![GitHub 分叉](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **克隆仓库**：`git clone https://github.com/microsoft/PhiCookBook.git`
3. [**加入 Microsoft AI Discord 社区，与专家和开发者交流**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![封面](../../imgs/cover.png)

### 🌐 多语言支持

#### 通过 GitHub Action 支持（自动化且始终保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯语](../ar/README.md) | [孟加拉语](../bn/README.md) | [保加利亚语](../bg/README.md) | [缅甸语](../my/README.md) | [中文（简体）](./README.md) | [中文（繁体，香港）](../hk/README.md) | [中文（繁体，澳门）](../mo/README.md) | [中文（繁体，台湾）](../tw/README.md) | [克罗地亚语](../hr/README.md) | [捷克语](../cs/README.md) | [丹麦语](../da/README.md) | [荷兰语](../nl/README.md) | [爱沙尼亚语](../et/README.md) | [芬兰语](../fi/README.md) | [法语](../fr/README.md) | [德语](../de/README.md) | [希腊语](../el/README.md) | [希伯来语](../he/README.md) | [印地语](../hi/README.md) | [匈牙利语](../hu/README.md) | [印尼语](../id/README.md) | [意大利语](../it/README.md) | [日语](../ja/README.md) | [韩语](../ko/README.md) | [立陶宛语](../lt/README.md) | [马来语](../ms/README.md) | [马拉地语](../mr/README.md) | [尼泊尔语](../ne/README.md) | [挪威语](../no/README.md) | [波斯语（法尔西语）](../fa/README.md) | [波兰语](../pl/README.md) | [葡萄牙语（巴西）](../br/README.md) | [葡萄牙语（葡萄牙）](../pt/README.md) | [旁遮普语（古木基文）](../pa/README.md) | [罗马尼亚语](../ro/README.md) | [俄语](../ru/README.md) | [塞尔维亚语（西里尔文）](../sr/README.md) | [斯洛伐克语](../sk/README.md) | [斯洛文尼亚语](../sl/README.md) | [西班牙语](../es/README.md) | [斯瓦希里语](../sw/README.md) | [瑞典语](../sv/README.md) | [他加禄语（菲律宾语）](../tl/README.md) | [泰米尔语](../ta/README.md) | [泰语](../th/README.md) | [土耳其语](../tr/README.md) | [乌克兰语](../uk/README.md) | [乌尔都语](../ur/README.md) | [越南语](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 目录

- 介绍
  - [欢迎加入 Phi 家族](./md/01.Introduction/01/01.PhiFamily.md)
  - [设置您的环境](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [了解关键技术](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi 模型的 AI 安全性](./md/01.Introduction/01/01.AISafety.md)
  - [Phi 硬件支持](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi 模型及跨平台可用性](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [使用 Guidance-ai 和 Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace 模型](https://github.com/marketplace/models)
  - [Azure AI 模型目录](https://ai.azure.com)

- 在不同环境中推理 Phi
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub 模型](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry 模型目录](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- 推理 Phi 家族
    - [在 iOS 中推理 Phi](./md/01.Introduction/03/iOS_Inference.md)
    - [在 Android 中推理 Phi](./md/01.Introduction/03/Android_Inference.md)
    - [在 Jetson 中推理 Phi](./md/01.Introduction/03/Jetson_Inference.md)
    - [在 AI PC 中推理 Phi](./md/01.Introduction/03/AIPC_Inference.md)
    - [使用 Apple MLX 框架推理 Phi](./md/01.Introduction/03/MLX_Inference.md)
    - [在本地服务器中推理 Phi](./md/01.Introduction/03/Local_Server_Inference.md)
    - [使用 AI Toolkit 在远程服务器中推理 Phi](./md/01.Introduction/03/Remote_Interence.md)
    - [使用 Rust 推理 Phi](./md/01.Introduction/03/Rust_Inference.md)
    - [在本地推理 Phi--Vision](./md/01.Introduction/03/Vision_Inference.md)
    - [使用 Kaito AKS 和 Azure 容器（官方支持）推理 Phi](./md/01.Introduction/03/Kaito_Inference.md)
-  [量化 Phi 家族](./md/01.Introduction/04/QuantifyingPhi.md)
    - [使用 llama.cpp 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [使用 onnxruntime 的生成式 AI 扩展量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [使用 Intel OpenVINO 量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [使用 Apple MLX 框架量化 Phi-3.5 / 4](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  评估 Phi
    - [负责任的 AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [使用 Azure AI Foundry 进行评估](./md/01.Introduction/05/AIFoundry.md)
    - [使用 Promptflow 进行评估](./md/01.Introduction/05/Promptflow.md)
 
- 使用 Azure AI 搜索进行 RAG
    - [如何使用 Phi-4-mini 和 Phi-4-multimodal（RAG）与 Azure AI 搜索](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi 应用开发示例
  - 文本与聊天应用
    - Phi-4 示例 🆕
      - [📓] [使用 Phi-4-mini ONNX 模型聊天](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [使用 Phi-4 本地 ONNX 模型聊天 .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [使用语义内核的 Phi-4 ONNX 聊天 .NET 控制台应用](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 示例
      - [使用 Phi3、ONNX Runtime Web 和 WebGPU 在浏览器中构建本地聊天机器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino 聊天](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [多模型 - 交互式 Phi-3-mini 和 OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - 构建包装器并使用 Phi-3 与 MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [模型优化 - 如何使用 Olive 优化 Phi-3-min 模型以适配 ONNX Runtime Web](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 应用与 Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 多模型 AI 驱动的笔记应用示例](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [使用 Prompt flow 微调并集成自定义 Phi-3 模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [在 Azure AI Foundry 中使用 Prompt flow 微调并集成自定义 Phi-3 模型](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [在 Azure AI Foundry 中评估微调后的 Phi-3 / Phi-3.5 模型，重点关注微软的负责任 AI 原则](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct 语言预测示例（中文/英文）](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG 聊天机器人](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [使用 Windows GPU 创建基于 Phi-3.5-Instruct ONNX 的 Prompt flow 解决方案](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [使用 Microsoft Phi-3.5 tflite 创建 Android 应用](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [使用 Microsoft.ML.OnnxRuntime 的本地 ONNX Phi-3 模型进行问答 .NET 示例](../../md/04.HOL/dotnet/src/LabsPhi301)
- [使用语义内核和 Phi-3 的控制台聊天 .NET 应用](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI 推理 SDK 基于代码的示例
  - Phi-4 示例 🆕
    - [📓] [使用 Phi-4-multimodal 生成项目代码](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 示例
    - [使用 Microsoft Phi-3 系列构建自己的 Visual Studio Code GitHub Copilot 聊天](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [使用 GitHub 模型通过 Phi-3.5 创建自己的 Visual Studio Code 聊天助手代理](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- 高级推理示例
  - Phi-4 示例 🆕
    - [📓] [Phi-4-mini-reasoning 或 Phi-4-reasoning 示例](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [使用 Microsoft Olive 微调 Phi-4-mini-reasoning](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [使用 Apple MLX 微调 Phi-4-mini-reasoning](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [使用 GitHub 模型的 Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [使用 Azure AI Foundry 模型的 Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- 演示
    - [Phi-4-mini 演示托管在 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal 演示托管在 Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- 视觉示例
  - Phi-4 示例 🆕
    - [📓] [使用 Phi-4-multimodal 读取图像并生成代码](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 示例
    - [📓][Phi-3-vision-图像文本到文本](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP 嵌入](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [演示：Phi-3 回收](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - 视觉语言助手 - 使用 Phi3-Vision 和 OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision 多帧或多图像示例](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [使用 Microsoft.ML.OnnxRuntime .NET 的本地 ONNX 模型的 Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [基于菜单的使用 Microsoft.ML.OnnxRuntime .NET 的本地 ONNX 模型的 Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi304)

- 数学示例
  - Phi-4-Mini-Flash-Reasoning-Instruct 示例 🆕 [使用 Phi-4-Mini-Flash-Reasoning-Instruct 的数学演示](../../md/02.Application/09.Math/MathDemo.ipynb)

- 音频示例
  - Phi-4 示例 🆕
    - [📓] [使用 Phi-4-multimodal 提取音频转录](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal 音频示例](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal 语音翻译示例](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET 控制台应用使用 Phi-4-multimodal 音频分析音频文件并生成转录](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE 示例
  - Phi-3 / 3.5 示例
    - [📓] [Phi-3.5 专家模型（MoEs）社交媒体示例](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [使用 NVIDIA NIM Phi-3 MOE、Azure AI 搜索和 LlamaIndex 构建检索增强生成（RAG）管道](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- 函数调用示例
  - Phi-4 示例 🆕
    - [📓] [使用 Phi-4-mini 进行函数调用](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [使用函数调用创建多代理与 Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [使用 Ollama 进行函数调用](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [使用 ONNX 进行函数调用](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- 多模态混合示例
  - Phi-4 示例 🆕
    - [📓] [使用 Phi-4-multimodal 作为技术记者](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET 控制台应用使用 Phi-4-multimodal 分析图像](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi 微调示例
  - [微调场景](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [微调与 RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [微调让 Phi-3 成为行业专家](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [使用 AI 工具包为 VS Code 微调 Phi-3](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [使用 Azure 机器学习服务微调 Phi-3](./md/03.FineTuning/Introduce_AzureML.md)
  - [使用 Lora 微调 Phi-3](./md/03.FineTuning/FineTuning_Lora.md)
  - [使用 QLora 微调 Phi-3](./md/03.FineTuning/FineTuning_Qlora.md)
  - [使用 Azure AI Foundry 微调 Phi-3](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [使用 Azure ML CLI/SDK 微调 Phi-3](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [使用 Microsoft Olive 微调](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [使用 Microsoft Olive 实践实验室](./md/03.FineTuning/olive-lab/readme.md)
  - [使用 Weights and Bias 微调 Phi-3-vision](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [使用 Apple MLX 框架微调 Phi-3](./md/03.FineTuning/FineTuning_MLX.md)
  - [微调 Phi-3-vision（官方支持）](./md/03.FineTuning/FineTuning_Vision.md)
  - [使用 Kaito AKS 和 Azure 容器微调 Phi-3（官方支持）](./md/03.FineTuning/FineTuning_Kaito.md)
  - [微调 Phi-3 和 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- 实践实验室
  - [探索前沿模型：LLMs、SLMs、本地开发等](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [释放 NLP 潜力：使用 Microsoft Olive 微调](https://github.com/azure/Ignite_FineTuning_workshop)

- 学术研究论文和出版物
  - [教科书是你所需的一切 II：phi-1.5 技术报告](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技术报告：一个功能强大的语言模型，可在手机上本地运行](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技术报告](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技术报告：通过 LoRA 混合实现紧凑但强大的多模态语言模型](https://arxiv.org/abs/2503.01743)
  - [优化车载功能调用的小型语言模型](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) 微调PHI-3以应对多项选择题：方法、结果和挑战](https://arxiv.org/abs/2501.01588)
  - [Phi-4推理技术报告](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini推理技术报告](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## 使用Phi模型

### Azure AI Foundry上的Phi

您可以学习如何使用Microsoft Phi，并在不同的硬件设备上构建端到端解决方案。要亲自体验Phi，请从试用模型并根据您的场景定制Phi开始，使用 [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 了解更多信息，请参阅[Azure AI Foundry快速入门](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)。

**Playground**
每个模型都有专属的测试平台 [Azure AI Playground](https://aka.ms/try-phi3)。

### GitHub上的Phi模型

您可以学习如何使用Microsoft Phi，并在不同的硬件设备上构建端到端解决方案。要亲自体验Phi，请从试用模型并根据您的场景定制Phi开始，使用 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 了解更多信息，请参阅[GitHub Model Catalog快速入门](/md/02.QuickStart/GitHubModel_QuickStart.md)。

**Playground**
每个模型都有专属的[测试平台](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Hugging Face上的Phi

您也可以在 [Hugging Face](https://huggingface.co/microsoft) 上找到模型。

**Playground**
 [Hugging Chat测试平台](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 负责任的AI

Microsoft致力于帮助客户负责任地使用我们的AI产品，分享我们的经验，并通过透明性说明和影响评估等工具建立基于信任的合作关系。许多资源可以在[https://aka.ms/RAI](https://aka.ms/RAI)找到。
Microsoft的负责任AI方法基于我们的AI原则：公平性、可靠性和安全性、隐私和安全性、包容性、透明性和问责制。

大规模自然语言、图像和语音模型——如本示例中使用的模型——可能会以不公平、不可靠或冒犯的方式表现，从而造成伤害。请参阅[Azure OpenAI服务透明性说明](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)以了解风险和限制。

减轻这些风险的推荐方法是在您的架构中包含一个安全系统，该系统可以检测和防止有害行为。[Azure AI内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview)提供了一个独立的保护层，能够检测应用程序和服务中的用户生成和AI生成的有害内容。Azure AI内容安全包括文本和图像API，允许您检测有害材料。在Azure AI Foundry中，内容安全服务允许您查看、探索和试用检测不同模态有害内容的示例代码。以下[快速入门文档](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)指导您如何向服务发出请求。

另一个需要考虑的方面是整体应用性能。在多模态和多模型应用中，我们认为性能意味着系统按您和用户的期望运行，包括不生成有害输出。评估整体应用性能时，可以使用[性能和质量以及风险和安全评估器](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)。您还可以创建和评估[自定义评估器](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)。

您可以在开发环境中使用[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html)评估您的AI应用程序。通过测试数据集或目标，您的生成式AI应用程序生成的内容可以通过内置评估器或您选择的自定义评估器进行定量测量。要开始使用Azure AI Evaluation SDK评估您的系统，可以参考[快速入门指南](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)。执行评估运行后，您可以[在Azure AI Foundry中可视化结果](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商标

此项目可能包含项目、产品或服务的商标或标志。使用Microsoft商标或标志需获得授权，并必须遵守[Microsoft商标和品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。
在修改版本的项目中使用Microsoft商标或标志不得引起混淆或暗示Microsoft赞助。任何使用第三方商标或标志的行为均需遵守第三方的政策。

## 获取帮助

如果您遇到困难或对构建AI应用有任何疑问，请加入：

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

如果您有产品反馈或在构建过程中遇到错误，请访问：

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。