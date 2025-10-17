<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-10-11T12:23:32+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "ta"
}
-->
# தொலைதூர முடிவுகளை fine-tuned மாடலுடன் மேற்கொள்வது

Adapterகள் தொலைதூர சூழலில் பயிற்சி செய்யப்பட்ட பிறகு, Gradio பயன்பாட்டை பயன்படுத்தி மாடலுடன் தொடர்பு கொள்ளலாம்.

![Fine-tune முடிந்தது](../../../../../imgs/03/RemoteServer/log-finetuning-res.png)

### Azure வளங்களை அமைத்தல்
தொலைதூர முடிவுகளுக்கான Azure வளங்களை அமைக்க, `AI Toolkit: Provision Azure Container Apps for inference` என்ற கட்டளையை command palette-ல் செயல்படுத்த வேண்டும். இந்த அமைப்பின் போது, உங்கள் Azure Subscription மற்றும் resource group-ஐ தேர்ந்தெடுக்க வேண்டும்.  
![Provision Inference Resource](../../../../../imgs/03/RemoteServer/command-provision-inference.png)
   
இயல்பாக, subscription மற்றும் resource group fine-tuning-க்கு பயன்படுத்தியவையே inference-க்கும் பொருந்த வேண்டும். inference, Azure Container App சூழலைப் பயன்படுத்தி, fine-tuning படியில் உருவாக்கப்பட்ட Azure Files-ல் சேமிக்கப்பட்ட மாடல் மற்றும் மாடல் adapter-ஐ அணுகும்.

## AI Toolkit பயன்படுத்துதல்

### முடிவுகளுக்கான Deployment  
Inference code-ஐ திருத்த அல்லது inference மாடலை மீண்டும் ஏற்ற விரும்பினால், `AI Toolkit: Deploy for inference` கட்டளையை செயல்படுத்தவும். இது உங்கள் சமீபத்திய code-ஐ ACA-வுடன் ஒத்திசைக்கவும் மற்றும் replica-ஐ மீண்டும் தொடங்கவும் உதவும்.  

![Deploy for inference](../../../../../imgs/01/03/RemoteServer/command-deploy.png)

Deployment வெற்றிகரமாக முடிந்த பிறகு, இந்த endpoint-ஐ பயன்படுத்தி மாடலை மதிப்பீடு செய்ய தயாராக இருக்கும்.

### Inference API-ஐ அணுகுதல்

VSCode notification-ல் காணப்படும் "*Go to Inference Endpoint*" பொத்தானை கிளிக் செய்து inference API-ஐ அணுகலாம். மாற்றாக, web API endpoint `ACA_APP_ENDPOINT` என்ற பெயரில் `./infra/inference.config.json` மற்றும் output panel-ல் காணலாம்.

![App Endpoint](../../../../../imgs/01/03/RemoteServer/notification-deploy.png)

> **குறிப்பு:** Inference endpoint முழுமையாக செயல்பட சில நிமிடங்கள் தேவைப்படலாம்.

## Template-ல் உள்ள inference கூறுகள்
 
| கோப்புறை | உள்ளடக்கம் |
| ------ |--------- |
| `infra` | தொலைதூர செயல்பாடுகளுக்கான தேவையான அனைத்து கட்டமைப்புகளையும் கொண்டுள்ளது. |
| `infra/provision/inference.parameters.json` | Azure வளங்களை inference-க்கு provision செய்ய பயன்படுத்தப்படும் bicep templates-க்கான அளவுருக்களை கொண்டுள்ளது. |
| `infra/provision/inference.bicep` | Azure வளங்களை inference-க்கு provision செய்ய templates-ஐ கொண்டுள்ளது. |
| `infra/inference.config.json` | `AI Toolkit: Provision Azure Container Apps for inference` கட்டளையால் உருவாக்கப்படும் கட்டமைப்பு கோப்பு. இது மற்ற தொலைதூர command palette-களுக்கான input ஆக பயன்படுத்தப்படுகிறது. |

### Azure Resource Provision-ஐ AI Toolkit மூலம் அமைத்தல்
[AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) அமைக்கவும்.

Provision Azure Container Apps for inference` கட்டளை.

`./infra/provision/inference.parameters.json` கோப்பில் கட்டமைப்பு அளவுருக்களை காணலாம். விவரங்கள் இங்கே:
| அளவுரு | விளக்கம் |
| --------- |------------ |
| `defaultCommands` | இது web API-ஐ தொடங்குவதற்கான கட்டளைகள். |
| `maximumInstanceCount` | GPU instance-களின் அதிகபட்ச திறனை அமைக்க இந்த அளவுரு பயன்படுத்தப்படுகிறது. |
| `location` | Azure வளங்கள் provision செய்யப்படும் இடம். இயல்பாக, resource group-ஐ தேர்ந்தெடுத்த இடத்துடன் பொருந்தும். |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | Azure வளங்களுக்கு பெயர் அமைக்க இந்த அளவுருக்கள் பயன்படுத்தப்படுகின்றன. இயல்பாக, fine-tuning resource பெயர்களுடன் பொருந்தும். நீங்கள் புதிய, பயன்படுத்தப்படாத resource பெயரை உள்ளீடு செய்து உங்கள் சொந்த resource-களை உருவாக்கலாம் அல்லது ஏற்கனவே உள்ள Azure resource பெயரை உள்ளீடு செய்து அதை பயன்படுத்தலாம். மேலும் விவரங்களுக்கு [Using existing Azure Resources](../../../../../md/01.Introduction/03) பகுதியை பார்க்கவும். |

### ஏற்கனவே உள்ள Azure வளங்களை பயன்படுத்துதல்

இயல்பாக, inference provision fine-tuning-க்கு பயன்படுத்திய Azure Container App சூழல், Storage Account, Azure File Share மற்றும் Azure Log Analytics-ஐ பயன்படுத்துகிறது. inference API-க்கு தனியாக ஒரு Azure Container App உருவாக்கப்படுகிறது. 

Fine-tuning படியில் Azure வளங்களை தனிப்பயனாக்கியிருந்தால் அல்லது inference-க்கு உங்கள் சொந்த Azure வளங்களை பயன்படுத்த விரும்பினால், அவற்றின் பெயர்களை `./infra/inference.parameters.json` கோப்பில் குறிப்பிடவும். பின்னர், command palette-ல் இருந்து `AI Toolkit: Provision Azure Container Apps for inference` கட்டளையை இயக்கவும். இது குறிப்பிடப்பட்ட வளங்களை புதுப்பித்து, இல்லாதவற்றை உருவாக்கும்.

உதாரணமாக, ஏற்கனவே உள்ள Azure container சூழல் இருந்தால், உங்கள் `./infra/finetuning.parameters.json` இவ்வாறு இருக்கும்:

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

### கையேடு மூலம் Provision  
Azure வளங்களை கையேடு மூலம் அமைக்க விரும்பினால், `./infra/provision` கோப்புறைகளில் உள்ள bicep கோப்புகளை பயன்படுத்தலாம். AI Toolkit command palette-ஐ பயன்படுத்தாமல் Azure வளங்களை அமைத்து, configure செய்திருந்தால், resource பெயர்களை `inference.config.json` கோப்பில் உள்ளீடு செய்யலாம்.

உதாரணமாக:

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

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்செயல்முறைகளுக்கு முழு முயற்சி எடுத்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் இயல்பான மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.