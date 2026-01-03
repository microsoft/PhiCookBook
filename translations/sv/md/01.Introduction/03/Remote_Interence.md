<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-07-16T21:19:26+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "sv"
}
-->
# Fjärrinferens med den finjusterade modellen

Efter att adaptrarna har tränats i den fjärranslutna miljön, använd en enkel Gradio-applikation för att interagera med modellen.

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.7b92254e7e822c7f.sv.png)

### Provisionera Azure-resurser  
Du behöver ställa in Azure-resurserna för fjärrinferens genom att köra kommandot `AI Toolkit: Provision Azure Container Apps for inference` från kommandopaletten. Under denna setup kommer du att bli ombedd att välja din Azure-prenumeration och resursgrupp.  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.467afc8d351642fc.sv.png)

Som standard bör prenumerationen och resursgruppen för inferens matcha de som användes för finjusteringen. Inferensen kommer att använda samma Azure Container App-miljö och få tillgång till modellen och modeladapter som lagras i Azure Files, vilka genererades under finjusteringssteget.

## Använda AI Toolkit

### Distribution för inferens  
Om du vill ändra inferenskoden eller ladda om inferensmodellen, kör kommandot `AI Toolkit: Deploy for inference`. Detta synkroniserar din senaste kod med ACA och startar om replikan.

![Deploy for inference](../../../../../translated_images/command-deploy.9adb4e310dd0b0ae.sv.png)

Efter att distributionen har slutförts framgångsrikt är modellen nu redo för utvärdering via denna endpoint.

### Åtkomst till inferens-API

Du kan nå inferens-API:t genom att klicka på knappen "*Go to Inference Endpoint*" som visas i VSCode-notifikationen. Alternativt kan web API-endpointen hittas under `ACA_APP_ENDPOINT` i `./infra/inference.config.json` och i utmatningspanelen.

![App Endpoint](../../../../../translated_images/notification-deploy.446e480a44b1be58.sv.png)

> **Note:** Inferens-endpointen kan ta några minuter innan den är fullt operativ.

## Inferenskomponenter som ingår i mallen

| Mapp | Innehåll |
| ------ |--------- |
| `infra` | Innehåller alla nödvändiga konfigurationer för fjärroperationer. |
| `infra/provision/inference.parameters.json` | Innehåller parametrar för bicep-mallar, används för att provisionera Azure-resurser för inferens. |
| `infra/provision/inference.bicep` | Innehåller mallar för att provisionera Azure-resurser för inferens. |
| `infra/inference.config.json` | Konfigurationsfilen, genererad av kommandot `AI Toolkit: Provision Azure Container Apps for inference`. Den används som input för andra fjärrkommandon i paletten. |

### Använda AI Toolkit för att konfigurera Azure Resource Provision  
Konfigurera [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Kör kommandot `Provision Azure Container Apps for inference`.

Du hittar konfigurationsparametrar i filen `./infra/provision/inference.parameters.json`. Här är detaljerna:  
| Parameter | Beskrivning |
| --------- |------------ |
| `defaultCommands` | Kommandon för att starta ett web API. |
| `maximumInstanceCount` | Denna parameter anger maxkapaciteten för GPU-instanser. |
| `location` | Platsen där Azure-resurserna provisioneras. Standardvärdet är samma som den valda resursgruppens plats. |
| `storageAccountName`, `fileShareName`, `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`, `acaLogAnalyticsName` | Dessa parametrar används för att namnge Azure-resurserna vid provisionering. Som standard kommer de att vara samma som namnet på finjusteringsresursen. Du kan ange ett nytt, oanvänt resursnamn för att skapa egna resurser med anpassade namn, eller ange namnet på en redan existerande Azure-resurs om du vill använda den. För detaljer, se avsnittet [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Använda befintliga Azure-resurser

Som standard använder provisioneringen för inferens samma Azure Container App-miljö, Storage Account, Azure File Share och Azure Log Analytics som användes för finjusteringen. En separat Azure Container App skapas enbart för inferens-API:t.

Om du har anpassat Azure-resurserna under finjusteringssteget eller vill använda dina egna befintliga Azure-resurser för inferens, specificera deras namn i filen `./infra/inference.parameters.json`. Kör sedan kommandot `AI Toolkit: Provision Azure Container Apps for inference` från kommandopaletten. Detta uppdaterar eventuella angivna resurser och skapar de som saknas.

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
Om du föredrar att manuellt konfigurera Azure-resurserna kan du använda de medföljande bicep-filerna i mapparna `./infra/provision`. Om du redan har satt upp och konfigurerat alla Azure-resurser utan att använda AI Toolkit-kommandopaletten, kan du helt enkelt ange resursnamnen i filen `inference.config.json`.

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
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.