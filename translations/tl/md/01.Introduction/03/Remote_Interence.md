<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-05-09T12:44:28+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "tl"
}
-->
# Remote Inferencing gamit ang fine-tuned na modelo

Pagkatapos ma-train ang mga adapter sa remote na kapaligiran, gamitin ang simpleng Gradio application para makipag-ugnayan sa modelo.

![Fine-tune complete](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.tl.png)

### Pag-provision ng Azure Resources  
Kailangan mong i-setup ang Azure Resources para sa remote inference sa pamamagitan ng pagpapatakbo ng `AI Toolkit: Provision Azure Container Apps for inference` mula sa command palette. Sa setup na ito, hihilingin kang pumili ng iyong Azure Subscription at resource group.  
![Provision Inference Resource](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.tl.png)
   
Karaniwan, ang subscription at resource group para sa inference ay dapat tumugma sa mga ginamit sa fine-tuning. Gagamitin ng inference ang parehong Azure Container App Environment at a-access ang modelo at model adapter na naka-imbak sa Azure Files, na nilikha noong fine-tuning step. 

## Paggamit ng AI Toolkit

### Deployment para sa Inference  
Kung nais mong baguhin ang inference code o i-reload ang inference model, patakbuhin ang `AI Toolkit: Deploy for inference` command. Ito ay magsi-synchronize ng iyong pinakabagong code sa ACA at ire-restart ang replica.  

![Deploy for inference](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.tl.png)

Pagkatapos ng matagumpay na deployment, handa na ang modelo para sa pagsusuri gamit ang endpoint na ito.

### Pag-access sa Inference API

Maaari mong ma-access ang inference API sa pamamagitan ng pag-click sa "*Go to Inference Endpoint*" na button na makikita sa VSCode notification. Bilang alternatibo, ang web API endpoint ay matatagpuan sa ilalim ng `ACA_APP_ENDPOINT` sa `./infra/inference.config.json` at sa output panel.

![App Endpoint](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.tl.png)

> **Note:** Maaaring kailanganin ng ilang minuto bago tuluyang maging operational ang inference endpoint.

## Mga Inference Components na Kasama sa Template
 
| Folder | Nilalaman |
| ------ |--------- |
| `infra` | Naglalaman ng lahat ng kinakailangang configuration para sa remote operations. |
| `infra/provision/inference.parameters.json` | Nagtataglay ng mga parameter para sa bicep templates, na ginagamit para sa pag-provision ng Azure resources para sa inference. |
| `infra/provision/inference.bicep` | Naglalaman ng mga template para sa pag-provision ng Azure resources para sa inference. |
| `infra/inference.config.json` | Ang configuration file, na nilikha ng `AI Toolkit: Provision Azure Container Apps for inference` command. Ginagamit ito bilang input para sa iba pang remote command palettes. |

### Paggamit ng AI Toolkit para sa pag-configure ng Azure Resource Provision  
I-configure ang [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Mag-provision ng Azure Container Apps para sa inference` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` file. Pagkatapos, patakbuhin ang `AI Toolkit: Provision Azure Container Apps for inference` command mula sa command palette. Ina-update nito ang anumang tinukoy na resources at lumilikha ng mga nawawala.

Halimbawa, kung mayroon kang umiiral na Azure container environment, ang iyong `./infra/finetuning.parameters.json` ay dapat ganito:

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

### Manual na Provision  
Kung nais mong mano-manong i-configure ang Azure resources, maaari mong gamitin ang mga ibinigay na bicep files sa `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json` file.

Halimbawa:

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

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagsisikapang maging tumpak ang pagsasalin, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.