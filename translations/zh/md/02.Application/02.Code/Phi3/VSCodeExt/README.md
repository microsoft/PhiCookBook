<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7302d85639441c7cedbae09795e6b9a6",
  "translation_date": "2025-04-03T07:42:35+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi3\\VSCodeExt\\README.md",
  "language_code": "zh"
}
-->
# **构建您自己的 Visual Studio Code GitHub Copilot Chat 与 Microsoft Phi-3 系列**

您是否使用过 GitHub Copilot Chat 的工作区代理？您是否希望构建您团队自己的代码代理？这个动手实验旨在结合开源模型，构建企业级代码业务代理。

## **基础**

### **为什么选择 Microsoft Phi-3**

Phi-3 是一个系列家族，包括 phi-3-mini、phi-3-small 和 phi-3-medium，基于不同的训练参数用于文本生成、对话完成和代码生成。此外还有基于视觉的 phi-3-vision。它适合企业或不同团队创建离线生成式 AI 解决方案。

推荐阅读此链接 [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 扩展提供了一个聊天界面，让您可以直接在 VS Code 中与 GitHub Copilot 互动，并获得与编码相关问题的答案，而无需浏览文档或搜索在线论坛。

Copilot Chat 可能会使用语法高亮、缩进和其他格式化功能来使生成的响应更加清晰。根据用户问题的类型，结果可能包含 Copilot 用于生成响应的上下文链接，例如源代码文件或文档，或者访问 VS Code 功能的按钮。

- Copilot Chat 集成到您的开发流程中，在您需要的地方提供帮助：

- 直接从编辑器或终端启动内联聊天会话，在编码时获得帮助

- 使用聊天视图随时获得 AI 助手的支持

- 启动快速聊天以提出问题并迅速回到工作中

您可以在以下场景中使用 GitHub Copilot Chat，例如：

- 回答有关如何最好解决问题的编码问题

- 解释其他人的代码并提出改进建议

- 提议代码修复

- 生成单元测试用例

- 生成代码文档

推荐阅读此链接 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


### **Microsoft GitHub Copilot Chat @workspace**

在 Copilot Chat 中引用 **@workspace** 让您可以对整个代码库提出问题。根据问题的内容，Copilot 智能地检索相关文件和符号，并在其答案中以链接和代码示例的形式引用。

为了回答您的问题，**@workspace** 会搜索开发者在 VS Code 中浏览代码库时使用的相同资源：

- 工作区中的所有文件，除非被 .gitignore 文件忽略

- 带有嵌套文件夹和文件名的目录结构

- 如果工作区是一个 GitHub 仓库并被代码搜索索引，则使用 GitHub 的代码搜索索引

- 工作区中的符号和定义

- 当前选定的文本或活动编辑器中的可见文本

注意：如果您打开了文件或在被忽略的文件中选中了文本，.gitignore 会被绕过。

推荐阅读此链接 [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **了解更多关于本实验的信息**

GitHub Copilot 极大地提高了企业的编程效率，每个企业都希望定制 GitHub Copilot 的相关功能。许多企业已经根据自己的业务场景和开源模型定制了类似 GitHub Copilot 的扩展。对于企业来说，定制的扩展更易于控制，但这也影响了用户体验。毕竟，GitHub Copilot 在处理通用场景和专业性方面功能更强。如果能够保持一致的体验，同时定制企业自己的扩展会更好。GitHub Copilot Chat 提供了相关的 API，让企业可以在聊天体验中进行扩展。保持一致的体验并拥有定制功能会带来更好的用户体验。

本实验主要使用 Phi-3 模型结合本地 NPU 和 Azure 混合，构建一个定制的 GitHub Copilot Chat ***@PHI3*** 代理，帮助企业开发者完成代码生成 ***(@PHI3 /gen)*** 和基于图像生成代码 ***(@PHI3 /img)***。

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.zh.png)

### ***注意：*** 

本实验目前在 Intel CPU 和 Apple Silicon 的 AIPC 上实现。我们将继续更新 Qualcomm 版本的 NPU。


## **实验**


| 名称 | 描述 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - 安装(✅) | 配置和安装相关环境及工具 | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - 使用 Phi-3-mini 运行 Prompt flow (✅) | 结合 AIPC / Apple Silicon，使用本地 NPU 通过 Phi-3-mini 创建代码生成 | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - 在 Azure 机器学习服务上部署 Phi-3-vision (✅) | 通过部署 Azure 机器学习服务的模型目录 - Phi-3-vision 图像生成代码 | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - 在 GitHub Copilot Chat 中创建一个 @phi-3 代理 (✅)  | 在 GitHub Copilot Chat 中创建一个定制的 Phi-3 代理，用于完成代码生成、图形生成代码、RAG 等 | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| 示例代码 (✅)  | 下载示例代码 | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **资源**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. 了解更多关于 GitHub Copilot 的信息 [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. 了解更多关于 GitHub Copilot Chat 的信息 [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. 了解更多关于 GitHub Copilot Chat API 的信息 [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. 了解更多关于 Azure AI Foundry 的信息 [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. 了解更多关于 Azure AI Foundry 的模型目录的信息 [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文的母语版本作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。