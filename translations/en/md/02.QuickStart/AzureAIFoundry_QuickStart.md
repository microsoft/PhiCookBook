<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:17:41+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "en"
}
-->
# **Using Phi-3 in Azure AI Foundry**

With the rise of Generative AI, we aim to use a unified platform to manage different LLMs and SLMs, integrate enterprise data, handle fine-tuning/RAG operations, and evaluate various enterprise applications after integrating LLMs and SLMs, enabling smarter generative AI applications. [Azure AI Foundry](https://ai.azure.com) is an enterprise-grade generative AI application platform.

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93d6fb1d0a69b635bc36834da1f0615d7d2b8be216021d9eeb.en.png)

Azure AI Foundry allows you to evaluate large language model (LLM) responses and orchestrate prompt application components using prompt flow for improved performance. The platform supports scalability, making it easy to transition from proof of concepts to full production. Continuous monitoring and refinement ensure long-term success.

You can quickly deploy the Phi-3 model on Azure AI Foundry with simple steps, then use Azure AI Foundry to handle Phi-3 related Playground/Chat, fine-tuning, evaluation, and other tasks.

## **1. Preparation**

If you already have the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) installed on your machine, using this template is as easy as running this command in a new directory.

## Manual Creation

Creating a Microsoft Azure AI Foundry project and hub is a great way to organize and manage your AI work. Here’s a step-by-step guide to get started:

### Creating a Project in Azure AI Foundry

1. **Go to Azure AI Foundry**: Sign in to the Azure AI Foundry portal.
2. **Create a Project**:
   - If you’re inside a project, select "Azure AI Foundry" at the top left to go to the Home page.
   - Click "+ Create project".
   - Enter a name for your project.
   - If you have a hub, it will be selected by default. If you have access to multiple hubs, you can choose a different one from the dropdown. To create a new hub, select "Create new hub" and provide a name.
   - Click "Create".

### Creating a Hub in Azure AI Foundry

1. **Go to Azure AI Foundry**: Sign in with your Azure account.
2. **Create a Hub**:
   - Select the Management center from the left menu.
   - Click "All resources", then the down arrow next to "+ New project" and select "+ New hub".
   - In the "Create a new hub" dialog, enter a name for your hub (e.g., contoso-hub) and adjust other fields as needed.
   - Click "Next", review the details, then click "Create".

For more detailed instructions, refer to the official [Microsoft documentation](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Once created, you can access your studio through [ai.azure.com](https://ai.azure.com/).

You can have multiple projects within one AI Foundry. Create a project in AI Foundry to get started.

Check out Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code).

## **2. Deploy a Phi model in Azure AI Foundry**

Click the Explore option in your project to open the Model Catalog and select Phi-3.

Choose Phi-3-mini-4k-instruct.

Click 'Deploy' to deploy the Phi-3-mini-4k-instruct model.

> [!NOTE]
>
> You can select the computing power during deployment.

## **3. Playground Chat Phi in Azure AI Foundry**

Go to the deployment page, select Playground, and start chatting with Phi-3 in Azure AI Foundry.

## **4. Deploying the Model from Azure AI Foundry**

To deploy a model from the Azure Model Catalog, follow these steps:

- Sign in to Azure AI Foundry.
- Select the model you want to deploy from the Azure AI Foundry model catalog.
- On the model’s Details page, click Deploy, then choose Serverless API with Azure AI Content Safety.
- Select the project where you want to deploy your model. To use the Serverless API, your workspace must be in the East US 2 or Sweden Central region. You can customize the Deployment name.
- In the deployment wizard, review Pricing and terms to understand the costs and usage policies.
- Click Deploy. Wait until deployment completes and you’re redirected to the Deployments page.
- Click Open in playground to start interacting with the model.
- You can return to the Deployments page, select your deployment, and find the endpoint’s Target URL and Secret Key, which you’ll use to call the deployment and generate completions.
- You can always find endpoint details, URLs, and access keys by going to the Build tab and selecting Deployments under Components.

> [!NOTE]
> Make sure your account has the Azure AI Developer role permissions on the Resource Group to perform these steps.

## **5. Using Phi API in Azure AI Foundry**

You can access https://{Your project name}.region.inference.ml.azure.com/swagger.json via Postman GET and combine it with your Key to explore the available interfaces.

This makes it easy to get request parameters as well as response parameters.

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.