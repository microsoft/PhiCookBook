# **Using Phi-3 na Microsoft Foundry**

With di development of Generative AI, we dey hope to use one unified platform to manage different LLM and SLM, enterprise data integration, fine-tuning/RAG operations, plus to evaluate different enterprise businesses after dem don integrate LLM and SLM, etc., so dat generative AI fit dey implement Smart applications better. [Microsoft Foundry](https://ai.azure.com) na enterprise-level generative AI application platform.

![aistudo](../../../../translated_images/pcm/aifoundry_home.f28a8127c96c7d93.webp)

With Microsoft Foundry, you fit evaluate large language model (LLM) response and arrange prompt application components with prompt flow for better performance. Di platform dey help scalability to transform proof of concepts go full production sharp sharp. E dey support continuous monitoring and refinement for long-term success.

We fit quickly deploy di Phi-3 model for Microsoft Foundry with simple steps, then use Microsoft Foundry complete Phi-3 related Playground/Chat, Fine-tuning, evaluation plus other related work.

## **1. Preparation**

If you don already get di [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) installed for your machine, to use dis template na just run dis command for new directory.

## Manual Creation

To create Microsoft Foundry project and hub na beta way to arrange and manage your AI work. Dis na step-by-step guide to help you start:

### Creating a Project for Microsoft Foundry

1. **Go Microsoft Foundry**: Sign in for Microsoft Foundry portal.
2. **Create Project**:
   - If you dey inside project, select "Microsoft Foundry" for top left of page make e carry you go Home page.
   - Select "+ Create project".
   - Put name for di project.
   - If you get hub, e go auto select. If you get access to more than one hub, you fit select different one from dropdown. If you want create new hub, select "Create new hub" and put name.
   - Select "Create".

### Creating a Hub for Microsoft Foundry

1. **Go Microsoft Foundry**: Sign in with your Azure account.
2. **Create Hub**:
   - Select Management center from left menu.
   - Select "All resources", then di down arrow next to "+ New project" and select "+ New hub".
   - For "Create a new hub" dialog, put name for your hub (example: contoso-hub) and change other fields as you want.
   - Select "Next", check di info, then select "Create".

For more detailed instructions, you fit refer to the official [Microsoft documentation](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

After you create am well, you fit enter di studio wey you create through [ai.azure.com](https://ai.azure.com/)

You fit get multiple projects for one AI Foundry. Create project inside AI Foundry to prepare.

Create Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Deploy Phi model for Microsoft Foundry**

Click Explore option for the project go enter Model Catalog and select Phi-3

Select Phi-3-mini-4k-instruct

Click 'Deploy' to deploy di Phi-3-mini-4k-instruct model

> [!NOTE]
>
> You fit select computing power when you dey deploy

## **3. Playground Chat Phi for Microsoft Foundry**

Go deployment page, select Playground, then yarn with Phi-3 of Microsoft Foundry

## **4. Deploying Model from Microsoft Foundry**

To deploy model from Azure Model Catalog, follow dis steps:

- Sign in to Microsoft Foundry.
- Choose di model wey you want deploy from Microsoft Foundry model catalog.
- For model's Details page, select Deploy then select Serverless API with Azure AI Content Safety.
- Select di project wey you want deploy your models inside. To use Serverless API offering, your workspace must dey inside East US 2 or Sweden Central region. You fit customize di Deployment name.
- For deployment wizard, select Pricing and terms to sabi di pricing and terms of use.
- Select Deploy. Wait until deployment ready and e carry you go Deployments page.
- Select Open in playground to start interact with di model.
- You fit go back to Deployments page, select the deployment, and see di endpoint's Target URL and Secret Key, wey you fit use call the deployment and generate completions.
- You fit always find endpoint details, URL, and access keys by waka go Build tab and select Deployments from Components section.

> [!NOTE]
> Abeg note say your account must get Azure AI Developer role permission for the Resource Group to fit do dis steps.

## **5. Using Phi API for Microsoft Foundry**

You fit access https://{Your project name}.region.inference.ml.azure.com/swagger.json through Postman GET and join am with Key to learn about di interfaces wey dem provide

You go fit get di request parameters well well, plus di response parameters.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg sabi say automated translations fit get yawa or mistakes. The original document wey dey for im own language na the correct one wey you suppose trust. For important matter, make person wey sabi human translation do am. We no go take blame if anybody misunderstand or make wrong meaning from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->