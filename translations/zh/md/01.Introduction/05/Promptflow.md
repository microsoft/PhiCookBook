<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "01a5ee7478befb159e2b7ded29832206",
  "translation_date": "2025-04-03T07:08:37+00:00",
  "source_file": "md\\01.Introduction\\05\\Promptflow.md",
  "language_code": "zh"
}
-->
# **介绍 Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) 是一个可视化工作流自动化工具，允许用户通过预构建的模板和自定义连接器创建自动化工作流。它旨在帮助开发人员和业务分析师快速构建用于数据管理、协作和流程优化等任务的自动化流程。通过 Prompt Flow，用户可以轻松连接不同的服务、应用程序和系统，并自动化复杂的业务流程。

Microsoft Prompt Flow 旨在简化基于大型语言模型（LLMs）的 AI 应用程序的端到端开发周期。无论是在构思、原型设计、测试、评估还是部署基于 LLM 的应用程序时，Prompt Flow 都能简化流程，并帮助您构建具有生产质量的 LLM 应用。

## 以下是使用 Microsoft Prompt Flow 的主要功能和优势：

**互动式创作体验**

Prompt Flow 提供了工作流结构的可视化表示，使您能够轻松理解和导航项目。
它提供类似笔记本的编码体验，以提高工作流开发和调试效率。

**提示变体和优化**

创建并比较多个提示变体，以促进迭代优化过程。评估不同提示的性能，选择最有效的提示。

**内置评估流程**

使用内置评估工具评估您的提示和工作流的质量与效果。
了解基于 LLM 的应用程序的性能表现。

**全面的资源库**

Prompt Flow 包含一个内置工具、示例和模板的资源库。这些资源可以作为开发的起点，激发创意并加速开发过程。

**协作与企业级支持**

支持团队协作，允许多个用户共同参与提示工程项目。
有效维护版本控制并共享知识。简化整个提示工程流程，从开发和评估到部署和监控。

## 在 Prompt Flow 中的评估

在 Microsoft Prompt Flow 中，评估在衡量 AI 模型性能方面起着至关重要的作用。让我们来探讨如何在 Prompt Flow 中自定义评估流程和指标：

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.zh.png)

**理解 Prompt Flow 中的评估**

在 Prompt Flow 中，工作流代表了一系列处理输入并生成输出的节点。评估流程是专门设计用来根据特定标准和目标评估运行表现的特殊工作流。

**评估流程的关键特点**

评估流程通常在被测试的工作流之后运行，使用其输出结果。它们计算分数或指标以衡量被测试工作流的性能。指标可以包括准确性、相关性分数或其他相关度量。

### 自定义评估流程

**定义输入**

评估流程需要接收被测试运行的输出。定义输入的方式与标准工作流类似。
例如，如果您在评估一个问答工作流，可以将输入命名为 "answer"；如果评估一个分类工作流，可以将输入命名为 "category"。可能还需要实际标签等真实值输入。

**输出和指标**

评估流程生成的结果用于衡量被测试工作流的性能。可以使用 Python 或 LLM（大型语言模型）计算指标。使用 log_metric() 函数记录相关指标。

**使用自定义评估流程**

根据您的具体任务和目标开发自己的评估流程。根据评估目标自定义指标。
将此自定义评估流程应用于批量运行，以进行大规模测试。

## 内置评估方法

Prompt Flow 还提供了内置评估方法。
您可以提交批量运行，并使用这些方法评估工作流在大数据集上的表现。
查看评估结果，比较指标，并根据需要进行迭代。
请记住，评估对于确保您的 AI 模型满足期望的标准和目标至关重要。请参阅官方文档以获取有关在 Microsoft Prompt Flow 中开发和使用评估流程的详细说明。

总之，Microsoft Prompt Flow 通过简化提示工程和提供强大的开发环境，帮助开发人员创建高质量的 LLM 应用。如果您正在使用 LLM，Prompt Flow 是一个值得探索的工具。请查阅 [Prompt Flow 评估文档](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo)，了解有关在 Microsoft Prompt Flow 中开发和使用评估流程的详细说明。

**免责声明**:  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而引发的任何误解或误读，我们不承担任何责任。