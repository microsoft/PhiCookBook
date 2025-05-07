<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-05-07T14:43:04+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "zh"
}
-->
# **使用 Azure AI Foundry 进行评估**

![aistudo](../../../../../translated_images/AIFoundry.9e0b513e999a1c5aa227e4c7028b5ff9a6cb712e6613c696705445ee4ca8f35d.zh.png)

如何使用 [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 评估你的生成式 AI 应用。无论是评估单轮对话还是多轮对话，Azure AI Foundry 都提供了评估模型性能和安全性的工具。

![aistudo](../../../../../translated_images/AIPortfolio.69da59a8e1eaa70f2bab1836c11a69fc97e59f1b1b4154ce5e58bc589d278047.zh.png)

## 如何使用 Azure AI Foundry 评估生成式 AI 应用
更多详细说明请参见 [Azure AI Foundry 文档](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

以下是入门步骤：

## 在 Azure AI Foundry 中评估生成式 AI 模型

**前提条件**

- 一个以 CSV 或 JSON 格式的测试数据集。
- 一个已部署的生成式 AI 模型（例如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一个带有计算实例的运行时环境，用于执行评估。

## 内置评估指标

Azure AI Foundry 支持评估单轮和复杂的多轮对话。
对于基于特定数据的检索增强生成（RAG）场景，可以使用内置的评估指标来衡量性能。
此外，还可以评估通用的单轮问答场景（非 RAG）。

## 创建评估运行

在 Azure AI Foundry 界面中，进入 Evaluate 页面或 Prompt Flow 页面。
按照评估创建向导设置评估运行。可以为评估提供一个可选名称。
选择与你的应用目标相符的场景。
选择一个或多个评估指标来衡量模型输出。

## 自定义评估流程（可选）

如果需要更高的灵活性，可以创建自定义评估流程，根据具体需求定制评估过程。

## 查看结果

评估完成后，在 Azure AI Foundry 中记录、查看并分析详细的评估指标。深入了解你的应用能力和局限。

**Note** Azure AI Foundry 当前处于公开预览阶段，建议用于试验和开发。生产环境请考虑其他方案。更多详情和操作步骤请参见官方 [AI Foundry 文档](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或曲解承担责任。