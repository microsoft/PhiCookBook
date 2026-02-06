# **介绍 Responsible AI**

[Microsoft Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=aiml-138114-kinfeylo) 是一项旨在帮助开发者和组织构建透明、可信且负责任的 AI 系统的倡议。该倡议提供了开发符合隐私、公平和透明等伦理原则的负责任 AI 解决方案的指导和资源。我们还将探讨构建负责任 AI 系统所面临的一些挑战和最佳实践。

## Microsoft Responsible AI 概述

![RAIPrinciples](../../../../../translated_images/zh-CN/RAIPrinciples.bf9c9bc6ca160d33.webp)

**伦理原则**

Microsoft Responsible AI 以一系列伦理原则为指导，包括隐私、公平、透明、问责和安全。这些原则旨在确保 AI 系统以伦理和负责任的方式开发。

**透明的 AI**

Microsoft Responsible AI 强调 AI 系统透明性的重要性。这包括清晰说明 AI 模型的工作原理，以及确保数据来源和算法公开可用。

**负责任的 AI**

[Microsoft Responsible AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=aiml-138114-kinfeylo) 推动开发负责任的 AI 系统，这些系统能够提供 AI 模型决策过程的洞见，帮助用户理解并信任 AI 系统的输出。

**包容性**

AI 系统应设计为惠及所有人。Microsoft 致力于打造包容性的 AI，考虑多元视角，避免偏见或歧视。

**可靠性和安全性**

确保 AI 系统的可靠性和安全性至关重要。Microsoft 专注于构建表现稳定且避免产生有害结果的稳健模型。

**AI 公平性**

Microsoft Responsible AI 认识到，如果 AI 系统基于有偏见的数据或算法训练，可能会延续偏见。该倡议提供指导，帮助开发不因种族、性别或年龄等因素歧视的公平 AI 系统。

**隐私和安全**

Microsoft Responsible AI 强调保护用户隐私和数据安全的重要性。这包括实施强有力的数据加密和访问控制，并定期审计 AI 系统以发现潜在漏洞。

**问责和责任**

Microsoft Responsible AI 推动 AI 开发和部署中的问责和责任，确保开发者和组织了解 AI 系统潜在风险，并采取措施加以缓解。

## 构建负责任 AI 系统的最佳实践

**使用多样化数据集开发 AI 模型**

为避免 AI 系统中的偏见，使用代表多种视角和经验的多样化数据集非常重要。

**采用可解释的 AI 技术**

可解释的 AI 技术有助于用户理解 AI 模型的决策过程，从而增强对系统的信任。

**定期审计 AI 系统以发现漏洞**

定期对 AI 系统进行审计，有助于识别需要解决的潜在风险和漏洞。

**实施强有力的数据加密和访问控制**

数据加密和访问控制有助于保护 AI 系统中的用户隐私和安全。

**遵循 AI 开发中的伦理原则**

遵循公平、透明和问责等伦理原则，有助于建立对 AI 系统的信任，确保其以负责任的方式开发。

## 使用 AI Foundry 实现 Responsible AI

[Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 是一个强大的平台，帮助开发者和组织快速创建智能、先进、面向市场且负责任的应用。以下是 Azure AI Foundry 的一些关键功能和能力：

**开箱即用的 API 和模型**

Azure AI Foundry 提供预构建且可定制的 API 和模型，涵盖生成式 AI、对话式自然语言处理、搜索、监控、翻译、语音、视觉和决策等多种 AI 任务。

**Prompt Flow**

Azure AI Foundry 中的 Prompt Flow 使您能够创建对话式 AI 体验，设计和管理对话流程，便于构建聊天机器人、虚拟助手及其他交互式应用。

**检索增强生成（RAG）**

RAG 技术结合了基于检索和基于生成的方法，通过利用现有知识（检索）和创造性生成（生成）提升生成回答的质量。

**生成式 AI 的评估和监控指标**

Azure AI Foundry 提供评估和监控生成式 AI 模型的工具，帮助评估其性能、公平性等关键指标，确保负责任的部署。此外，如果您创建了仪表板，可以使用 Azure Machine Learning Studio 中的无代码 UI，基于 [Repsonsible AI Toolbox](https://responsibleaitoolbox.ai/?WT.mc_id=aiml-138114-kinfeylo) Python 库自定义并生成 Responsible AI 仪表板及相关评分卡。该评分卡有助于向技术和非技术利益相关者分享公平性、特征重要性及其他负责任部署的关键信息。

使用 AI Foundry 实现负责任 AI 时，您可以遵循以下最佳实践：

**明确 AI 系统的问题和目标**

在开发前，明确 AI 系统要解决的问题或目标，有助于确定所需的数据、算法和资源，构建有效模型。

**收集并预处理相关数据**

训练 AI 系统所用数据的质量和数量对性能影响重大，因此需收集相关数据，进行清洗和预处理，确保数据能代表目标人群或问题。

**选择合适的评估方法**

根据数据和问题选择最合适的评估算法。

**评估并解释模型**

构建模型后，使用合适的指标评估其性能，并以透明的方式解释结果，帮助识别模型中的偏见或局限，并进行改进。

**确保透明性和可解释性**

AI 系统应具备透明性和可解释性，让用户理解其工作原理和决策过程，尤其适用于对人类生活有重大影响的领域，如医疗、金融和法律系统。

**监控并更新模型**

AI 系统应持续监控和更新，确保其长期保持准确和有效，这需要持续的维护、测试和再训练。

总之，Microsoft Responsible AI 是一项旨在帮助开发者和组织构建透明、可信且负责任 AI 系统的倡议。负责任的 AI 实施至关重要，而 Azure AI Foundry 致力于让组织能够切实实现这一目标。通过遵循伦理原则和最佳实践，我们可以确保 AI 系统以负责任的方式开发和部署，造福整个社会。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。