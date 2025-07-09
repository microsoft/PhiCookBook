<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-07-09T20:04:41+00:00",
  "source_file": "md/01.Introduction/03/Remote_Interence.md",
  "language_code": "my"
}
-->
# Remote Inferencing with the fine-tuned model

အဒပ်တာတွေကို remote ပတ်ဝန်းကျင်မှာ သင်ကြားပြီးနောက်၊ မော်ဒယ်နဲ့ အပြန်အလှန် ဆက်သွယ်ဖို့အတွက် ရိုးရှင်းတဲ့ Gradio အက်ပ်လီကေးရှင်းကို အသုံးပြုပါ။

![Fine-tune complete](../../../../../imgs/03/RemoteServer/log-finetuning-res.png)

### Azure အရင်းအမြစ်များ စီစဉ်ခြင်း  
Remote inference အတွက် Azure အရင်းအမြစ်များကို စီစဉ်ဖို့ `AI Toolkit: Provision Azure Container Apps for inference` ကို command palette မှာ အကောင်အထည်ဖော်ပါ။ ဒီစီစဉ်မှုအတွင်း သင့် Azure Subscription နဲ့ resource group ကို ရွေးချယ်ဖို့ တောင်းခံပါလိမ့်မယ်။  
![Provision Inference Resource](../../../../../imgs/03/RemoteServer/command-provision-inference.png)

ပုံမှန်အားဖြင့် subscription နဲ့ resource group တွေဟာ fine-tuning အတွက် အသုံးပြုထားတဲ့ အတိုင်း ဖြစ်သင့်ပါတယ်။ Inference မှာလည်း fine-tuning အဆင့်မှာ ဖန်တီးထားတဲ့ Azure Container App Environment ကို အသုံးပြုပြီး Azure Files ထဲမှာ သိမ်းဆည်းထားတဲ့ မော်ဒယ်နဲ့ မော်ဒယ်အဒပ်တာကို ဝင်ရောက်အသုံးပြုပါလိမ့်မယ်။

## AI Toolkit ကို အသုံးပြုခြင်း

### Inference အတွက် Deployment  
Inference ကုဒ်ကို ပြန်လည်ပြင်ဆင်ချင်ပါက သို့မဟုတ် inference မော်ဒယ်ကို ပြန်လည်တင်ချင်ပါက `AI Toolkit: Deploy for inference` command ကို အကောင်အထည်ဖော်ပါ။ ဒါက သင့်နောက်ဆုံးကုဒ်ကို ACA နဲ့ đồng bộ လုပ်ပြီး replica ကို ပြန်စတင်ပေးပါလိမ့်မယ်။

![Deploy for inference](../../../../../imgs/01/03/RemoteServer/command-deploy.png)

Deployment အောင်မြင်ပြီးနောက် မော်ဒယ်ကို ဒီ endpoint မှတဆင့် သုံးသပ်နိုင်ပါပြီ။

### Inference API ကို ဝင်ရောက်အသုံးပြုခြင်း

VSCode notification မှာ ပြသထားတဲ့ "*Go to Inference Endpoint*" ခလုတ်ကို နှိပ်ခြင်းဖြင့် inference API ကို ဝင်ရောက်အသုံးပြုနိုင်ပါတယ်။ ဒါမှမဟုတ် `./infra/inference.config.json` ဖိုင်ထဲရှိ `ACA_APP_ENDPOINT` မှာလည်း web API endpoint ကို တွေ့နိုင်ပြီး output panel မှာလည်း ရှိပါတယ်။

![App Endpoint](../../../../../imgs/01/03/RemoteServer/notification-deploy.png)

> **Note:** Inference endpoint ဟာ လုံးဝအလုပ်လုပ်ဖို့ အချိန်အနည်းငယ် လိုအပ်နိုင်ပါတယ်။

## Template ထဲ ပါဝင်သော Inference အစိတ်အပိုင်းများ

| Folder | အကြောင်းအရာ |
| ------ |-------------- |
| `infra` | Remote လုပ်ဆောင်မှုများအတွက် လိုအပ်သော configuration များ ပါဝင်သည်။ |
| `infra/provision/inference.parameters.json` | Azure resource များကို inference အတွက် provision လုပ်ရာတွင် အသုံးပြုသော bicep template များအတွက် parameter များ ပါဝင်သည်။ |
| `infra/provision/inference.bicep` | Azure resource များကို inference အတွက် provision လုပ်ရာတွင် အသုံးပြုသော template များ ပါဝင်သည်။ |
| `infra/inference.config.json` | `AI Toolkit: Provision Azure Container Apps for inference` command ဖြင့် ဖန်တီးသော configuration ဖိုင်ဖြစ်ပြီး အခြား remote command palette များအတွက် input အဖြစ် အသုံးပြုသည်။ |

### AI Toolkit ဖြင့် Azure Resource Provision ကို စီမံခြင်း  
[AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) ကို စီမံရန်

`Provision Azure Container Apps for inference` command ကို အသုံးပြုပါ။

`./infra/provision/inference.parameters.json` ဖိုင်ထဲမှာ configuration parameter များကို တွေ့နိုင်ပါသည်။ အသေးစိတ်如下:

| Parameter | ဖော်ပြချက် |
| --------- |------------ |
| `defaultCommands` | Web API ကို စတင်ဖို့ အသုံးပြုသော command များဖြစ်သည်။ |
| `maximumInstanceCount` | GPU instance များအတွက် အများဆုံး စွမ်းဆောင်ရည်ကို သတ်မှတ်သည်။ |
| `location` | Azure resource များ provision လုပ်မည့် တည်နေရာဖြစ်ပြီး ပုံမှန်အားဖြင့် ရွေးချယ်ထားသော resource group ၏ တည်နေရာနှင့် တူညီသည်။ |
| `storageAccountName`, `fileShareName`, `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`, `acaLogAnalyticsName` | Azure resource များအတွက် အမည်များ သတ်မှတ်ရာတွင် အသုံးပြုသည်။ ပုံမှန်အားဖြင့် fine-tuning resource အမည်နှင့် တူညီပါသည်။ သင့်ကိုယ်ပိုင် အမည်အသစ် မသုံးထားသေးသော resource များ ဖန်တီးလိုပါက အသစ်ထည့်နိုင်ပြီး၊ ရှိပြီးသား Azure resource များကို အသုံးပြုလိုပါက အမည်များကို ထည့်သွင်းနိုင်ပါသည်။ အသေးစိတ်အတွက် [Using existing Azure Resources](../../../../../md/01.Introduction/03) ကို ကြည့်ပါ။ |

### ရှိပြီးသား Azure Resources များကို အသုံးပြုခြင်း

ပုံမှန်အားဖြင့် inference provision မှာ fine-tuning အတွက် အသုံးပြုထားသော Azure Container App Environment, Storage Account, Azure File Share, Azure Log Analytics များကို တူညီစွာ အသုံးပြုသည်။ Inference API အတွက် သီးခြား Azure Container App တစ်ခု ဖန်တီးထားသည်။

Fine-tuning အဆင့်တွင် Azure resource များကို ကိုယ်တိုင်ပြင်ဆင်ထားပါက သို့မဟုတ် ကိုယ်ပိုင် ရှိပြီးသား Azure resource များကို inference အတွက် အသုံးပြုလိုပါက `./infra/inference.parameters.json` ဖိုင်ထဲတွင် အမည်များကို သတ်မှတ်ပါ။ ထို့နောက် command palette မှ `AI Toolkit: Provision Azure Container Apps for inference` command ကို အကောင်အထည်ဖော်ပါ။ ဒါက သတ်မှတ်ထားသော resource များကို update လုပ်ပြီး မရှိသေးသော resource များကို ဖန်တီးပေးပါလိမ့်မယ်။

ဥပမာအားဖြင့် ရှိပြီးသား Azure container environment ရှိပါက သင့် `./infra/finetuning.parameters.json` ဖိုင်မှာ အောက်ပါအတိုင်း ဖြစ်သင့်သည်-

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

### လက်ဖြင့် Provision လုပ်ခြင်း  
Azure resource များကို လက်ဖြင့် စီမံချင်ပါက `./infra/provision` ဖိုလ်ဒါအတွင်းရှိ bicep ဖိုင်များကို အသုံးပြုနိုင်ပါသည်။ AI Toolkit command palette ကို မသုံးဘဲ Azure resource များအားလုံးကို ရှိပြီးသား စီမံပြီးသားဖြစ်ပါက `inference.config.json` ဖိုင်ထဲတွင် resource အမည်များကိုသာ ထည့်သွင်းနိုင်ပါသည်။

ဥပမာ-

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

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။