<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-05-09T12:40:38+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "sv"
}
-->
# Fjärrinferens med den finjusterade modellen

Efter att adaptrarna har tränats i den fjärranslutna miljön, använd en enkel Gradio-applikation för att interagera med modellen.

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.sv.png)

### Provisionera Azure-resurser  
Du behöver ställa in Azure-resurserna för fjärrinferens genom att köra `AI Toolkit: Provision Azure Container Apps for inference` från kommandopaletten. Under denna setup kommer du att bli ombedd att välja din Azure-prenumeration och resursgrupp.  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.sv.png)
   
Som standard bör prenumerationen och resursgruppen för inferens matcha de som användes för finjusteringen. Inferensen kommer att använda samma Azure Container App-miljö och få åtkomst till modellen och modeladapter som lagras i Azure Files, vilka skapades under finjusteringssteget.

## Använda AI Toolkit

### Distribution för inferens  
Om du vill ändra inferenskoden eller ladda om inferensmodellen, kör då kommandot `AI Toolkit: Deploy for inference`. Detta synkroniserar din senaste kod med ACA och startar om replikan.

![Deploy for inference](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.sv.png)

Efter att distributionen har slutförts framgångsrikt är modellen nu redo för utvärdering via denna endpoint.

### Åtkomst till inferens-API

Du kan nå inferens-API:t genom att klicka på knappen "*Go to Inference Endpoint*" som visas i VSCode-notifikationen. Alternativt hittar du webb-API-endpointen under `ACA_APP_ENDPOINT` i `./infra/inference.config.json` och i utdatapanelen.

![App Endpoint](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.sv.png)

> **Note:** Inferens-endpointen kan ta några minuter innan den är helt operativ.

## Inferenskomponenter inkluderade i mallen

| Mapp | Innehåll |
| ------ |--------- |
| `infra` | Innehåller alla nödvändiga konfigurationer för fjärrdrift. |
| `infra/provision/inference.parameters.json` | Innehåller parametrar för bicep-mallar, används för att provisionera Azure-resurser för inferens. |
| `infra/provision/inference.bicep` | Innehåller mallar för provisionering av Azure-resurser för inferens. |
| `infra/inference.config.json` | Konfigurationsfilen, genererad av kommandot `AI Toolkit: Provision Azure Container Apps for inference`. Den används som input för andra fjärrkommandon. |

### Använda AI Toolkit för att konfigurera Azure Resource Provision  
Konfigurera [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Provisionera Azure Container Apps för inferens` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json`-filen. Kör sedan kommandot `AI Toolkit: Provision Azure Container Apps for inference` från kommandopaletten. Detta uppdaterar angivna resurser och skapar de som saknas.

Till exempel, om du har en befintlig Azure container-miljö, bör din `./infra/finetuning.parameters.json` se ut så här:

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### Manuell provisionering  
Om du föredrar att konfigurera Azure-resurserna manuellt kan du använda de medföljande bicep-filerna i `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json`-filen.

Till exempel:

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.