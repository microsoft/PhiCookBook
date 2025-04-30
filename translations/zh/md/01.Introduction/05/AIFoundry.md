<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5dfb4983a2e74e4b5e8317eb16fc2154",
  "translation_date": "2025-04-03T07:07:07+00:00",
  "source_file": "md\\01.Introduction\\05\\AIFoundry.md",
  "language_code": "zh"
}
-->
# **使用 Azure AI Foundry 进行评估**

![aistudo](../../../../../translated_images/AIFoundry.61da8c74bccc0241ce9a4cb53a170912245871de9235043afcb796ccbc076fdc.zh.png)

如何使用 [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 评估您的生成式 AI 应用程序。无论是评估单轮对话还是多轮对话，Azure AI Foundry 都提供了评估模型性能和安全性的工具。

![aistudo](../../../../../translated_images/AIPortfolio.5aaa2b25e9157624a4542fe041d66a96a1c1ec6007e4e5aadd926c6ec8ce18b3.zh.png)

## 如何使用 Azure AI Foundry 评估生成式 AI 应用程序
有关详细说明，请参阅 [Azure AI Foundry 文档](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)。

以下是开始的步骤：

## 在 Azure AI Foundry 中评估生成式 AI 模型

**先决条件**

- 一个以 CSV 或 JSON 格式保存的测试数据集。
- 一个已部署的生成式 AI 模型（例如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一个运行时环境，配备计算实例以运行评估。

## 内置评估指标

Azure AI Foundry 允许您评估单轮对话以及复杂的多轮对话。
对于基于特定数据的检索增强生成（RAG）场景，可以使用内置评估指标来评估性能。
此外，还可以评估一般的单轮问答场景（非 RAG）。

## 创建评估运行

在 Azure AI Foundry 用户界面中，导航到 Evaluate 页面或 Prompt Flow 页面。
按照评估创建向导设置评估运行。为您的评估提供一个可选名称。
选择与您的应用目标一致的场景。
选择一个或多个评估指标来评估模型的输出。

## 自定义评估流程（可选）

如果需要更大的灵活性，可以建立一个自定义评估流程。根据您的具体需求定制评估过程。

## 查看结果

运行评估后，在 Azure AI Foundry 中记录、查看和分析详细的评估指标。深入了解您的应用程序的能力和局限性。

**注意** Azure AI Foundry 目前处于公开预览阶段，因此建议用于实验和开发目的。对于生产工作负载，请考虑其他选项。有关更多详细信息和分步说明，请探索官方 [AI Foundry 文档](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)。

**免责声明**：  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原文档的母语版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误读不承担责任。