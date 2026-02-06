# **Phi-3 ಅನ್ನು Azure AI Foundry ನಲ್ಲಿ ಬಳಸುವುದು**

ಜನರೇಟಿವ್ AI の ಅಭಿವೃದ್ಧಿಯೊಂದಿಗೆ, ನಮಗೆ ವಿವಿಧ LLM ಮತ್ತು SLM, ಎಂಟರ್‌ಪ್ರೈಸ್ ಡೇಟಾ ಏಕೀಕರಣ, ಫೈನ್-ಟ್ಯೂನಿಂಗ್/RAG ಕಾರ್ಯಗಳು ಮತ್ತು LLM ಮತ್ತು SLM ಏಕೀಕರಿಸುವ ನಂತರ ವಿಭಿನ್ನエಂಟರ್‌ಪ್ರೈಸ್ ವ್ಯವಹಾರಗಳ ಮೌಲ್ಯಮಾಪನಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಏಕೀಕೃತ ವೇದಿಕೆಯ<|vq_image_11612|><|vq_image_5976|><|vq_image_9307|><|vq_image_1291|><|vq_image_13117|><|vq_image_4993|><|vq_image_8217|><|vq_image_12356|><|vq_image_643|><|vq_image_10097|><|vq_image_7380|><|vq_image_6573|><|vq_image_5696|><|vq_image_8086|><|vq_image_15150|><|vq_image_166|><|image_border_9|><|vq_image_15146|><|vq_image_12183|><|vq_image_5763|><|vq_image_1858|><|vq_image_3187|><|vq_image_15087|><|vq_image_8214|><|vq_image_14084|><|vq_image_3664|><|vq_image_174|><|vq_image_9523|><|vq_image_12812|><|vq_image_5047|><|vq_image_3141|><|vq_image_9398|><|vq_image_11837|><|image_border_10|><|vq_image_6210|><|vq_image_7800|><|vq_image_13816|><|vq_image_4410|><|vq_image_4637|><|vq_image_7030|><|vq_image_9258|><|vq_image_2117|><|vq_image_3733|><|vq_image_4637|><|vq_image_6267|><|vq_image_4433|><|vq_image_14187|><|vq_image_15526|><|vq_image_8615|><|vq_image_12202|><|image_border_11|><|vq_image_4563|><|vq_image_2099|><|vq_image_6017|><|vq_image_4326|><|vq_image_3830|><|vq_image_4326|><|vq_image_10636|><|vq_image_7821|><|vq_image_5988|><|vq_image_11292|><|vq_image_6593|><|vq_image_1230|><|vq_image_5814|><|vq_image_1798|><|vq_image_12227|><|vq_image_11230|><|image_border_12|><|vq_image_11354|><|vq_image_9131|><|vq_image_12474|><|vq_image_6363|><|vq_image_7228|><|vq_image_9880|><|vq_image_3175|><|vq_image_13512|><|vq_image_12521|><|vq_image_2329|><|vq_image_15798|><|vq_image_5527|><|vq_image_3251|><|vq_image_6654|><|vq_image_6076|><|vq_image_6316|><|image_border_13|><|vq_image_237|><|vq_image_10299|><|vq_image_1340|><|vq_image_167|><|vq_image_2905|><|vq_image_7757|><|vq_image_11712|><|vq_image_11717|><|vq_image_422|><|vq_image_11431|><|vq_image_11645|><|vq_image_3719|><|vq_image_2424|><|vq_image_4003|><|vq_image_12232|><|vq_image_5484|><|image_border_14|><|vq_image_12520|><|vq_image_18|><|vq_image_5323|><|vq_image_14063|><|vq_image_15537|><|vq_image_1408|><|vq_image_8960|><|vq_image_14626|><|vq_image_14585|><|vq_image_14575|><|vq_image_741|><|vq_image_2103|><|vq_image_12381|><|vq_image_4978|><|vq_image_5012|><|vq_image_10112|><|image_border_15|><|vq_image_3134|><|vq_image_14225|><|vq_image_6095|><|vq_image_15751|><|vq_image_2687|><|vq_image_5622|><|vq_image_10733|><|vq_image_13854|><|vq_image_9433|><|vq_image_13936|><|vq_image_2482|><|vq_image_8240|><|vq_image_14867|><|vq_image_14761|><|vq_image_5048|><|vq_image_5486|> 

[Azure AI Foundry](https://ai.azure.com) ಈ ವೇದಿಕೆಯ ಮೂಲಕ ನೀವು LLM ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಬಹುದು ಮತ್ತು ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಗಾಗಿ prompt flow ಮೂಲಕ prompt ಅನ್ವಯಿಕೆ ಘಟಕಗಳನ್ನು ಸಂಯೋಜಿಸಬಹುದು. ಈ ವೇದಿಕೆ ಸಾಬೀತು-ಕಾನ್ಸೆಪ್ಟ್ಗಳನ್ನು ಸುಲಭವಾಗಿ ಉತ್ಪಾದನೆಗೆ ಪರಿವರ್ತಿಸಲು ಸ್ಕೇಲಾಬಿಲಿಟಿಯನ್ನು ಹೊಂದಿಸುತ್ತದೆ. ನಿರಂತರ ಮೇಲ್ವಿಚಾರಣೆ ಮತ್ತು ಸುಧಾರಣೆ ದೀರ್ಘಕಾಲೀನ ಯಶಸ್ಸಿಗೆ ನೆರವಾಗುತ್ತದೆ.

We can quickly deploy the Phi-3 model on Azure AI Foundry through simple steps, and then use Azure AI Foundry to complete Phi-3 related Playground/Chat, Fine-tuning, evaluation and other related work.

## **1. ತಯಾರಿ**

If you already have the [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) installed on your machine, using this template is as simple as running this command in a new directory.

## Manual Creation

Creating a Microsoft Azure AI Foundry project and hub is a great way to organize and manage your AI work. Here's a step-by-step guide to get you started:

### Azure AI Foundry ನಲ್ಲಿ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸುವುದು

1. **Go to Azure AI Foundry**: Azure AI Foundry ಪೋರ್ಟಲ್‌ಗೆ ಸೈನ್ ಇನ್ ಮಾಡಿ.
2. **Create a Project**:
   - If you're in a project, select "Azure AI Foundry" at the top left of the page to go to the Home page.
   - Select "+ Create project".
   - Enter a name for the project.
   - If you have a hub, it will be selected by default. If you have access to more than one hub, you can select a different one from the dropdown. If you want to create a new hub, select "Create new hub" and supply a name.
   - Select "Create".

### Azure AI Foundry ನಲ್ಲಿ ಹಬ್ ರಚಿಸುವುದು

1. **Go to Azure AI Foundry**: ನಿಮ್ಮ Azure ಖಾತೆಯಿಂದ ಸೈನ್ ಇನ್ ಮಾಡಿ.
2. **Create a Hub**:
   - ಎಡ ಮೆನುಯಿಂದ Management center ಆಯ್ಕೆಮಾಡಿ.
   - "All resources" ಆಯ್ಕೆಮಾಡಿ, ನಂತರ "+ New project" ಬಳಸಿದಲ್ಲಿ ಕೆಳಗಿನ ತಳದಿಂದ ಇರುವ down arrow ಆಯ್ಕೆಮಾಡಿ ಮತ್ತು "+ New hub" ಆಯ್ಕೆಮಾಡಿ.
   - "Create a new hub" ಡೈಲಾಗ್ನಲ್ಲಿ ನಿಮ್ಮ ಹಬ್‌ಗೆ ಹೆಸರು ನಮೂದಿಸಿ (ಉದಾ., contoso-hub) ಮತ್ತು ಬೇರೆ ಫೀಲ್ಡ್‌ಗಳನ್ನು ಅಗತ್ಯಕ್ಕೆ ಅನುಗುಣವಾಗಿ ತಿದ್ದುಪಡಿ ಮಾಡಿ.
   - "Next" ಆಯ್ಕೆಮಾಡಿ, ಮಾಹಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ, ಮತ್ತು ನಂತರ "Create" ಆಯ್ಕೆಮಾಡಿ.

For more detailed instructions, you can refer to the official [Microsoft documentation](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

After successful creation, you can access the studio you created through [ai.azure.com](https://ai.azure.com/)

There can be multiple projects on one AI Foundry. Create a project in AI Foundry to prepare.

Create Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Azure AI Foundry ನಲ್ಲಿ Phi ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸುವುದು**

Click the Explore option of the project to enter the Model Catalog and select Phi-3

Select Phi-3-mini-4k-instruct

Click 'Deploy' to deploy the Phi-3-mini-4k-instruct model

> [!NOTE]
>
> ನೀವು ನಿಯೋಜಿಸುವಾಗ ಕಂಪ್ಯೂಟಿಂಗ್ ಶಕ್ತಿ ಆಯ್ಕೆಮಾಡಬಹುದು

## **3. Azure AI Foundry ನಲ್ಲಿ Playgroundನಲ್ಲಿ Phi ಜೊತೆ ಚಾಟ್**

Go to the deployment page, select Playground, and chat with Phi-3 of Azure AI Foundry

## **4. Azure AI Foundry ನಿಂದ ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸುವುದು**

To deploy a model from the Azure Model Catalog, you can follow these steps:

- Sign in to Azure AI Foundry.
- Choose the model you want to deploy from the Azure AI Foundry model catalog.
- On the model's Details page, select Deploy and then select Serverless API with Azure AI Content Safety.
- Select the project in which you want to deploy your models. To use the Serverless API offering, your workspace must belong to the East US 2 or Sweden Central region. You can customize the Deployment name.
- On the deployment wizard, select the Pricing and terms to learn about the pricing and terms of use.
- Select Deploy. Wait until the deployment is ready and you're redirected to the Deployments page.
- Select Open in playground to start interacting with the model.
- You can return to the Deployments page, select the deployment, and note the endpoint's Target URL and the Secret Key, which you can use to call the deployment and generate completions.
- You can always find the endpoint's details, URL, and access keys by navigating to the Build tab and selecting Deployments from the Components section.

> [!NOTE]
> ದಯವಿಟ್ಟು ಗಮನಿಸಿ ಈ ಕ್ರಮಗಳನ್ನು ನಿರ್ವಹಿಸಲು ನಿಮ್ಮ ಖಾತೆಗೆ Resource Group ಮೇಲೆ Azure AI Developer ಭೂಮಿಕೆಯ اجازتಗಳಿರಬೇಕು.

## **5. Azure AI Foundry ನಲ್ಲಿ Phi API ಬಳಕೆ**

You can access https://{Your project name}.region.inference.ml.azure.com/swagger.json through Postman GET and combine it with Key to learn about the provided interfaces

You can get the request parameters very conveniently, as well as the response parameters.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ Co-op Translator (https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅನಿಖರತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿರಲಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮುಖ್ಯ ಹಾಗೂ ನಿರ್ಣಾಯಕ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ցանկացած ತಪ್ಪು ಅರ್ಥಗೊಳ್ಳುವಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗಾಗಿ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->