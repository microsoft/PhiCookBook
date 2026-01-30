<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:19:49+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "zh"
}
-->
# **在 Azure AI Foundry 中使用 Phi-3**

随着生成式 AI 的发展，我们希望通过一个统一的平台来管理不同的 LLM 和 SLM、企业数据集成、微调/RAG 操作，以及整合 LLM 和 SLM 后对不同企业业务的评估等，从而更好地实现生成式 AI 的智能应用。[Azure AI Foundry](https://ai.azure.com) 是一个面向企业级的生成式 AI 应用平台。

![aistudo](../../../../translated_images/zh-CN/aifoundry_home.f28a8127c96c7d93.webp)

借助 Azure AI Foundry，您可以评估大型语言模型（LLM）的响应，并通过 prompt flow 协调提示应用组件以提升性能。该平台支持从概念验证到完整生产的无缝扩展，持续监控和优化助力长期成功。

我们可以通过简单步骤快速在 Azure AI Foundry 上部署 Phi-3 模型，然后利用 Azure AI Foundry 完成 Phi-3 相关的 Playground/Chat、微调、评估等工作。

## **1. 准备工作**

如果您已经在机器上安装了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)，使用此模板只需在新目录中运行该命令即可。

## 手动创建

创建 Microsoft Azure AI Foundry 项目和 hub 是组织和管理 AI 工作的好方法。以下是入门的分步指南：

### 在 Azure AI Foundry 中创建项目

1. **访问 Azure AI Foundry**：登录 Azure AI Foundry 门户。
2. **创建项目**：
   - 如果您已在某个项目中，点击页面左上角的“Azure AI Foundry”返回主页。
   - 选择“+ Create project”。
   - 输入项目名称。
   - 如果已有 hub，会默认选择该 hub。如果您有多个 hub 的访问权限，可以从下拉菜单中选择其他 hub。若要创建新 hub，选择“Create new hub”并填写名称。
   - 点击“Create”。

### 在 Azure AI Foundry 中创建 Hub

1. **访问 Azure AI Foundry**：使用您的 Azure 账号登录。
2. **创建 Hub**：
   - 从左侧菜单选择管理中心。
   - 选择“所有资源”，点击“+ New project”旁的下拉箭头，选择“+ New hub”。
   - 在“Create a new hub”对话框中，输入 hub 名称（例如 contoso-hub），并根据需要修改其他字段。
   - 点击“Next”，确认信息后选择“Create”。

更多详细说明，请参考官方 [Microsoft 文档](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)。

创建成功后，您可以通过 [ai.azure.com](https://ai.azure.com/) 访问您创建的 studio。

一个 AI Foundry 中可以有多个项目。请先在 AI Foundry 中创建项目以做准备。

创建 Azure AI Foundry [快速入门](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. 在 Azure AI Foundry 中部署 Phi 模型**

点击项目的 Explore 选项，进入模型目录，选择 Phi-3。

选择 Phi-3-mini-4k-instruct。

点击“Deploy”部署 Phi-3-mini-4k-instruct 模型。

> [!NOTE]
>
> 部署时可以选择计算资源。

## **3. 在 Azure AI Foundry 中使用 Playground Chat Phi**

进入部署页面，选择 Playground，与 Azure AI Foundry 的 Phi-3 进行对话。

## **4. 从 Azure AI Foundry 部署模型**

要从 Azure 模型目录部署模型，可以按照以下步骤操作：

- 登录 Azure AI Foundry。
- 从 Azure AI Foundry 模型目录中选择您想部署的模型。
- 在模型详情页，选择“Deploy”，然后选择带有 Azure AI 内容安全的 Serverless API。
- 选择您想部署模型的项目。要使用 Serverless API，您的工作区必须位于 East US 2 或 Sweden Central 区域。您可以自定义部署名称。
- 在部署向导中，选择“Pricing and terms”了解价格和使用条款。
- 点击“Deploy”。等待部署完成并跳转到部署页面。
- 选择“Open in playground”开始与模型交互。
- 您可以返回部署页面，选择该部署，查看终端的目标 URL 和密钥，用于调用部署并生成结果。
- 您也可以通过导航到“Build”标签页，在“Components”部分选择“Deployments”随时查看终端详情、URL 和访问密钥。

> [!NOTE]
> 请注意，您的账户必须在资源组中拥有 Azure AI Developer 角色权限，才能执行这些操作。

## **5. 在 Azure AI Foundry 中使用 Phi API**

您可以通过 Postman 使用 GET 请求访问 https://{Your project name}.region.inference.ml.azure.com/swagger.json，并结合密钥了解提供的接口。

您可以非常方便地获取请求参数和响应参数。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。