<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-05-09T12:45:56+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "sk"
}
-->
# Vzdialené inferovanie s doladeným modelom

Po natrénovaní adaptérov vo vzdialenom prostredí použite jednoduchú Gradio aplikáciu na interakciu s modelom.

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.sk.png)

### Príprava Azure zdrojov
Pre vzdialené inferovanie je potrebné nastaviť Azure zdroje spustením príkazu `AI Toolkit: Provision Azure Container Apps for inference` z príkazovej palety. Počas tohto nastavenia budete vyzvaní na výber Azure predplatného a skupiny zdrojov.  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.sk.png)
   
Predvolene by predplatné a skupina zdrojov pre inferovanie mali zodpovedať tým, ktoré sa použili pri doladení modelu. Inferovanie bude využívať rovnaké Azure Container App Environment a pristupovať k modelu a adaptérovi uloženým v Azure Files, ktoré boli vytvorené počas kroku doladenia.

## Použitie AI Toolkit

### Nasadenie pre inferovanie  
Ak chcete upraviť kód pre inferovanie alebo znovu načítať inferovací model, spustite príkaz `AI Toolkit: Deploy for inference`. Tým sa synchronizuje váš najnovší kód s ACA a reštartuje sa replika.

![Deploy for inference](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.sk.png)

Po úspešnom dokončení nasadenia je model pripravený na vyhodnotenie pomocou tohto endpointu.

### Prístup k API inferovania

K API inferovania sa dostanete kliknutím na tlačidlo "*Go to Inference Endpoint*" v notifikácii VSCode. Alternatívne je webový API endpoint dostupný pod `ACA_APP_ENDPOINT` v `./infra/inference.config.json` a v paneli výstupu.

![App Endpoint](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.sk.png)

> **Note:** Endpoint pre inferovanie môže potrebovať niekoľko minút, kým bude plne funkčný.

## Komponenty inferovania zahrnuté v šablóne
 
| Priečinok | Obsah |
| --------- |-------|
| `infra` | Obsahuje všetky potrebné konfigurácie pre vzdialené operácie. |
| `infra/provision/inference.parameters.json` | Uchováva parametre pre bicep šablóny, ktoré sa používajú na prípravu Azure zdrojov pre inferovanie. |
| `infra/provision/inference.bicep` | Obsahuje šablóny pre prípravu Azure zdrojov pre inferovanie. |
| `infra/inference.config.json` | Konfiguračný súbor, vygenerovaný príkazom `AI Toolkit: Provision Azure Container Apps for inference`. Používa sa ako vstup pre ostatné vzdialené príkazové palety. |

### Použitie AI Toolkit na konfiguráciu Azure Resource Provision
Nakonfigurujte [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Pripravte Azure Container Apps pre inferovanie pomocou ` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` súboru. Potom spustite príkaz `AI Toolkit: Provision Azure Container Apps for inference` z príkazovej palety. Týmto sa aktualizujú zadané zdroje a vytvoria sa chýbajúce.

Napríklad, ak už máte existujúce Azure container prostredie, váš `./infra/finetuning.parameters.json` by mal vyzerať takto:

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

### Manuálna príprava  
Ak preferujete manuálne nastavenie Azure zdrojov, môžete použiť poskytnuté bicep súbory v priečinku `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json`.

Napríklad:

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

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.