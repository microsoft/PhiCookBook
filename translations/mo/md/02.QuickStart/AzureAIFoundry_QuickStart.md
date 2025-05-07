<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-05-07T13:07:18+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "mo"
}
-->
# **Using Phi-3 in Azure AI Foundry**

随着生成式 AI 的发展，我们希望通过一个统一的平台来管理不同的 LLM 和 SLM，企业数据集成，微调/RAG 操作，以及整合 LLM 和 SLM 后对不同企业业务的评估等，从而更好地实现生成式 AI 的智能应用。[Azure AI Foundry](https://ai.azure.com) 是一个企业级的生成式 AI 应用平台。

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93d6fb1d0a69b635bc36834da1f0615d7d2b8be216021d9eeb.mo.png)

借助 Azure AI Foundry，您可以评估大语言模型（LLM）的响应，并通过 prompt flow 编排提示应用组件，以提升性能。该平台支持将概念验证轻松转化为成熟的生产环境，实现良好的扩展性。持续监控和优化助力长期成功。

我们可以通过简单步骤快速在 Azure AI Foundry 上部署 Phi-3 模型，随后利用 Azure AI Foundry 完成 Phi-3 相关的 Playground/Chat、微调、评估等工作。

## **1. 准备工作**

如果您已经在机器上安装了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)，使用此模板只需在新目录下运行该命令即可。

## 手动创建

创建 Microsoft Azure AI Foundry 项目和 hub 是组织和管理 AI 工作的好方法。以下是详细的操作指南：

### 在 Azure AI Foundry 创建项目

1. **进入 Azure AI Foundry**：登录 Azure AI Foundry 门户。
2. **创建项目**：
   - 如果当前处于某个项目中，点击页面左上角的 “Azure AI Foundry” 返回首页。
   - 选择 “+ Create project”。
   - 输入项目名称。
   - 如果已有 hub，会默认选中。如果有多个 hub 可用，可从下拉列表中选择其他 hub。若需新建 hub，选择 “Create new hub” 并输入名称。
   - 点击 “Create”。

### 在 Azure AI Foundry 创建 Hub

1. **进入 Azure AI Foundry**：使用您的 Azure 账号登录。
2. **创建 Hub**：
   - 从左侧菜单选择管理中心（Management center）。
   - 选择 “All resources”，然后点击 “+ New project” 旁的下拉箭头，选择 “+ New hub”。
   - 在 “Create a new hub” 对话框中，输入 hub 名称（例如 contoso-hub），并根据需要修改其他字段。
   - 点击 “Next”，确认信息后点击 “Create”。

更多详细说明，请参考官方 [Microsoft 文档](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)。

创建成功后，可通过 [ai.azure.com](https://ai.azure.com/) 访问您创建的工作室。

一个 AI Foundry 中可以有多个项目，先在 AI Foundry 创建项目以做好准备。

创建 Azure AI Foundry [快速入门](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. 在 Azure AI Foundry 部署 Phi 模型**

点击项目的 Explore 选项，进入模型目录，选择 Phi-3。

选择 Phi-3-mini-4k-instruct。

点击“Deploy”部署 Phi-3-mini-4k-instruct 模型。

> [!NOTE]
>
> 部署时可选择计算资源。

## **3. 在 Azure AI Foundry Playground Chat 使用 Phi**

进入部署页面，选择 Playground，即可与 Azure AI Foundry 中的 Phi-3 进行对话。

## **4. 从 Azure AI Foundry 部署模型**

要从 Azure 模型目录部署模型，请按照以下步骤操作：

- 登录 Azure AI Foundry。
- 从 Azure AI Foundry 模型目录中选择想要部署的模型。
- 在模型详情页，点击 Deploy，然后选择带 Azure AI 内容安全的 Serverless API。
- 选择您要部署模型的项目。要使用 Serverless API，工作区必须属于 East US 2 或 Sweden Central 区域。您可以自定义部署名称。
- 在部署向导中，选择“Pricing and terms”了解定价和使用条款。
- 点击 Deploy。等待部署完成并跳转到部署页面。
- 选择“Open in playground”开始与模型交互。
- 您可以返回部署页面，选择该部署，查看终端的 Target URL 和 Secret Key，使用它们调用部署并生成结果。
- 终端详情、URL 和访问密钥始终可以通过 Build 标签下的 Components 部分中的 Deployments 找到。

> [!NOTE]
> 请确保您的账号在资源组中拥有 Azure AI Developer 角色权限，才能执行这些操作。

## **5. 在 Azure AI Foundry 使用 Phi API**

您可以通过 Postman 使用 GET 访问 https://{Your project name}.region.inference.ml.azure.com/swagger.json，并结合 Key 了解提供的接口。

请求参数和响应参数都能非常方便地获取。

**Disclaimer**:  
Thi documont has ben translatid yusing AI translatyon servys [Co-op Translator](https://github.com/Azure/co-op-translator). Whil we stryv for accurasy, plese be awar that automatyd translatyons may contayn errors or inaccyrasys. The orygynal documont in its natyve langwage shold be consydryd the authorytatyve sorce. For critycal ynformasyon, profeshonal human translatyon is recomended. We ar not lyable for any mysunderstandyngs or mysinterpretytayons arysyng from the use of this translatyon.