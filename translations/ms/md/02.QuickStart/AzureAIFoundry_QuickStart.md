<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-05-09T20:13:41+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "ms"
}
-->
# **在 Azure AI Foundry 中使用 Phi-3**

随着生成式 AI 的发展，我们希望通过一个统一的平台来管理不同的 LLM 和 SLM、企业数据集成、微调/RAG 操作，以及整合 LLM 和 SLM 后对不同企业业务的评估等，从而更好地实现生成式 AI 智能应用。[Azure AI Foundry](https://ai.azure.com) 是一个企业级的生成式 AI 应用平台。

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.ms.png)

借助 Azure AI Foundry，您可以评估大型语言模型（LLM）的响应，并通过 prompt flow 协调提示应用组件以提升性能。该平台支持将概念验证快速扩展为成熟的生产环境，且具备持续监控和优化功能，助力长期成功。

我们可以通过简单步骤快速在 Azure AI Foundry 上部署 Phi-3 模型，随后使用 Azure AI Foundry 完成 Phi-3 相关的 Playground/Chat、微调、评估等工作。

## **1. 准备工作**

如果您已经在本机安装了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)，使用此模板只需在新目录下运行此命令即可。

## 手动创建

创建 Microsoft Azure AI Foundry 项目和 hub 是组织和管理 AI 工作的好方法。以下是入门的详细步骤：

### 在 Azure AI Foundry 中创建项目

1. **进入 Azure AI Foundry**：登录 Azure AI Foundry 门户。
2. **创建项目**：
   - 如果您已在某个项目中，点击页面左上角的“Azure AI Foundry”返回首页。
   - 选择“+ Create project”。
   - 输入项目名称。
   - 如果已有 hub，会默认选择。如果有多个 hub 权限，可以从下拉菜单选择其他 hub。若需新建 hub，选择“Create new hub”并填写名称。
   - 点击“Create”。

### 在 Azure AI Foundry 中创建 Hub

1. **进入 Azure AI Foundry**：使用 Azure 账户登录。
2. **创建 Hub**：
   - 从左侧菜单选择管理中心。
   - 选择“所有资源”，点击“+ New project”旁边的下拉箭头，选择“+ New hub”。
   - 在“Create a new hub”对话框中，输入 hub 名称（例如 contoso-hub），并根据需要修改其他字段。
   - 点击“Next”，确认信息后点击“Create”。

更多详细说明请参考官方 [Microsoft 文档](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)。

创建成功后，可通过 [ai.azure.com](https://ai.azure.com/) 访问您创建的 studio。

一个 AI Foundry 中可以有多个项目，先创建项目以做准备。

创建 Azure AI Foundry [快速入门](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. 在 Azure AI Foundry 中部署 Phi 模型**

点击项目的 Explore 选项，进入模型目录，选择 Phi-3。

选择 Phi-3-mini-4k-instruct。

点击“Deploy”部署 Phi-3-mini-4k-instruct 模型。

> [!NOTE]
>
> 部署时可以选择计算资源。

## **3. 在 Azure AI Foundry 中使用 Playground Chat Phi**

进入部署页面，选择 Playground，开始与 Azure AI Foundry 中的 Phi-3 聊天。

## **4. 从 Azure AI Foundry 部署模型**

从 Azure 模型目录部署模型，步骤如下：

- 登录 Azure AI Foundry。
- 从 Azure AI Foundry 模型目录中选择要部署的模型。
- 在模型详情页，选择“Deploy”，然后选择“Serverless API with Azure AI Content Safety”。
- 选择要部署模型的项目。要使用 Serverless API，工作区必须位于 East US 2 或 Sweden Central 区域。可自定义部署名称。
- 在部署向导中，查看“Pricing and terms”了解价格和使用条款。
- 选择“Deploy”。等待部署完成，系统会跳转到部署页面。
- 选择“Open in playground”开始与模型交互。
- 您可以返回部署页面，选择该部署，查看端点的 Target URL 和 Secret Key，用于调用部署并生成结果。
- 端点详情、URL 和访问密钥可随时在“Build”标签下的“Components”部分的“Deployments”中查看。

> [!NOTE]
> 请注意，您的账户必须在资源组上拥有 Azure AI Developer 角色权限，才能执行这些操作。

## **5. 在 Azure AI Foundry 中使用 Phi API**

您可以通过 Postman 以 GET 方式访问 https://{Your project name}.region.inference.ml.azure.com/swagger.json，结合 Key 查看提供的接口。

请求参数和响应参数均可方便获取。

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.