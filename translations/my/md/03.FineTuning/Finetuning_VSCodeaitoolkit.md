<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:24:51+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "my"
}
-->
## VS Code အတွက် AI Toolkit မှ ကြိုဆိုပါသည်

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) သည် Azure AI Studio Catalog နှင့် Hugging Face ကဲ့သို့သော အခြား catalog များမှ မော်ဒယ်များကို စုပေါင်းပေးထားပြီး၊ generative AI tools နှင့် မော်ဒယ်များဖြင့် AI app များ ဖန်တီးရာတွင် အသုံးပြုသော ပုံမှန် ဖွံ့ဖြိုးတိုးတက်မှု လုပ်ငန်းများကို လွယ်ကူစေသည်။  
Toolkit ၏ အဓိက လုပ်ဆောင်ချက်များမှာ -  
- မော်ဒယ် ရှာဖွေခြင်းနှင့် playground ဖြင့် စတင်ခြင်း  
- ဒေသခံ ကွန်ပျူတာ အရင်းအမြစ်များဖြင့် မော်ဒယ် fine-tuning နှင့် inference  
- Azure အရင်းအမြစ်များဖြင့် အဝေးမှ fine-tuning နှင့် inference  

[VSCode အတွက် AI Toolkit ကို 설치ပါ](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/my/Aitoolkit.7157953df04812dc.png)

**[Private Preview]** Azure Container Apps တွင် မော်ဒယ် fine-tuning နှင့် inference ကို cloud မှာ တစ်ချက်နှိပ်ပြီး စတင်အသုံးပြုနိုင်သည်။

ယခု သင့် AI app ဖွံ့ဖြိုးတိုးတက်မှုကို စတင်ကြည့်ကြရအောင် -

- [VS Code အတွက် AI Toolkit မှ ကြိုဆိုပါသည်](../../../../md/03.FineTuning)
- [ဒေသခံ ဖွံ့ဖြိုးတိုးတက်မှု](../../../../md/03.FineTuning)
  - [ပြင်ဆင်မှုများ](../../../../md/03.FineTuning)
  - [Conda ကို ဖွင့်ပါ](../../../../md/03.FineTuning)
  - [Base မော်ဒယ် fine-tuning သာ](../../../../md/03.FineTuning)
  - [မော်ဒယ် fine-tuning နှင့် inference](../../../../md/03.FineTuning)
  - [မော်ဒယ် Fine-tuning](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Fine Tuning နမူနာများနှင့် အရင်းအမြစ်များ](../../../../md/03.FineTuning)
- [**\[Private Preview\]** အဝေးမှ ဖွံ့ဖြိုးတိုးတက်မှု](../../../../md/03.FineTuning)
  - [လိုအပ်ချက်များ](../../../../md/03.FineTuning)
  - [အဝေးမှ ဖွံ့ဖြိုးတိုးတက်မှု ပရောဂျက် တည်ဆောက်ခြင်း](../../../../md/03.FineTuning)
  - [Azure အရင်းအမြစ်များ ပေးအပ်ခြင်း](../../../../md/03.FineTuning)
  - [\[Optional\] Huggingface Token ကို Azure Container App Secret ထဲ ထည့်ခြင်း](../../../../md/03.FineTuning)
  - [Fine-tuning ကို စတင်ပြုလုပ်ခြင်း](../../../../md/03.FineTuning)
  - [Inference Endpoint ကို ပေးအပ်ခြင်း](../../../../md/03.FineTuning)
  - [Inference Endpoint ကို တပ်ဆင်ခြင်း](../../../../md/03.FineTuning)
  - [အဆင့်မြင့် အသုံးပြုမှု](../../../../md/03.FineTuning)

## ဒေသခံ ဖွံ့ဖြိုးတိုးတက်မှု
### ပြင်ဆင်မှုများ

1. Host စက်တွင် NVIDIA driver တပ်ဆင်ထားမှုရှိကြောင်း သေချာစေပါ။  
2. Hugging Face dataset အသုံးပြုမည်ဆိုပါက `huggingface-cli login` ကို ပြုလုပ်ပါ။  
3. `Olive` key settings များသည် memory အသုံးပြုမှုကို ပြောင်းလဲသည့် အရာများအတွက် ရှင်းလင်းချက်များ ဖြစ်သည်။  

### Conda ကို ဖွင့်ပါ  
WSL ပတ်ဝန်းကျင်ကို အသုံးပြုနေပြီး မျှဝေထားသောကြောင့် Conda ပတ်ဝန်းကျင်ကို ကိုယ်တိုင် manually ဖွင့်ရပါမည်။ ဒီအဆင့်ပြီးနောက် fine-tuning သို့မဟုတ် inference ကို ပြုလုပ်နိုင်ပါပြီ။

```bash
conda activate [conda-env-name] 
```

### Base မော်ဒယ် fine-tuning သာ  
Fine-tuning မပြုလုပ်ဘဲ base မော်ဒယ်ကို စမ်းသပ်လိုပါက Conda ဖွင့်ပြီးနောက် အောက်ပါ command ကို အသုံးပြုနိုင်ပါသည်။

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### မော်ဒယ် fine-tuning နှင့် inference  
Dev container ထဲတွင် workspace ဖွင့်ပြီးနောက် terminal (default path သည် project root) ကို ဖွင့်ပြီး အောက်ပါ command ဖြင့် ရွေးချယ်ထားသော dataset ပေါ်တွင် LLM ကို fine-tune ပြုလုပ်နိုင်ပါသည်။

```bash
python finetuning/invoke_olive.py 
```

Checkpoints နှင့် နောက်ဆုံးမော်ဒယ်ကို `models` ဖိုလ်ဒါတွင် သိမ်းဆည်းမည်ဖြစ်သည်။

နောက်တစ်ဆင့်တွင် fine-tuned မော်ဒယ်ဖြင့် `console`, `web browser` သို့မဟုတ် `prompt flow` မှတဆင့် chats ဖြင့် inference ပြုလုပ်နိုင်ပါသည်။

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

VS Code တွင် `prompt flow` ကို အသုံးပြုရန်အတွက် ဒီ [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html) ကို ကြည့်ပါ။

### မော်ဒယ် Fine-tuning

နောက်တစ်ဆင့်တွင် သင့်စက်တွင် GPU ရှိမရှိအပေါ် မူတည်၍ အောက်ပါ မော်ဒယ်ကို ဒေါင်းလုပ်လုပ်ပါ။

QLoRA ဖြင့် ဒေသခံ fine-tuning session ကို စတင်ရန် မော်ဒယ် catalog မှ fine-tune လုပ်လိုသော မော်ဒယ်ကို ရွေးချယ်ပါ။  
| Platform(s) | GPU ရှိ/မရှိ | မော်ဒယ်အမည် | အရွယ်အစား (GB) |
|---------|---------|--------|--------|
| Windows | ရှိသည် | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | ရှိသည် | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | မရှိ | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_မှတ်ချက်_** မော်ဒယ်များ ဒေါင်းလုပ်လုပ်ရန်အတွက် Azure အကောင့် မလိုအပ်ပါ။

Phi3-mini (int4) မော်ဒယ်သည် ၂GB မှ ၃GB အထိ အရွယ်အစားရှိပြီး၊ သင့်ကွန်ယက်အမြန်နှုန်းပေါ်မူတည်၍ ဒေါင်းလုပ်ချိန်ကာလကွာခြားနိုင်သည်။

ပရောဂျက်အမည်နှင့် တည်နေရာကို ရွေးချယ်ခြင်းဖြင့် စတင်ပါ။  
နောက်တစ်ဆင့်တွင် မော်ဒယ် catalog မှ မော်ဒယ်ကို ရွေးချယ်ပါ။ ပရောဂျက် template ကို ဒေါင်းလုပ်လုပ်ရန် တောင်းဆိုမည်ဖြစ်ပြီး "Configure Project" ကို နှိပ်၍ အမျိုးမျိုးသော ဆက်တင်များကို ပြင်ဆင်နိုင်ပါသည်။

### Microsoft Olive

[Olive](https://microsoft.github.io/Olive/why-olive.html) ကို PyTorch မော်ဒယ်များအပေါ် QLoRA fine-tuning ပြုလုပ်ရန် အသုံးပြုသည်။ မူရင်းတန်ဖိုးများဖြင့် အလိုအလျောက် ပြင်ဆင်ထားပြီး memory အသုံးပြုမှုကို ထိရောက်စွာ စီမံနိုင်ရန် optimize လုပ်ထားသည်။ သို့သော် သင့်အခြေအနေအတွက် ပြင်ဆင်နိုင်ပါသည်။

### Fine Tuning နမူနာများနှင့် အရင်းအမြစ်များ

- [Fine tuning စတင်လေ့လာရန် လမ်းညွှန်](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)  
- [HuggingFace Dataset ဖြင့် Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)  
- [Simple DataSet ဖြင့် Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)  

## **[Private Preview]** အဝေးမှ ဖွံ့ဖြိုးတိုးတက်မှု

### လိုအပ်ချက်များ

1. အဝေးမှ Azure Container App ပတ်ဝန်းကျင်တွင် မော်ဒယ် fine-tuning ပြုလုပ်ရန် သင့် subscription တွင် လိုအပ်သော GPU စွမ်းဆောင်ရည် ရှိကြောင်း သေချာစေပါ။ သင့် application အတွက် လိုအပ်သော စွမ်းဆောင်ရည်ကို တောင်းဆိုရန် [support ticket](https://azure.microsoft.com/support/create-ticket/) တင်ပါ။ [GPU စွမ်းဆောင်ရည်အကြောင်း ပိုမိုသိရှိရန်](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)  
2. HuggingFace တွင် private dataset အသုံးပြုပါက [HuggingFace အကောင့်](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) ရှိပြီး [access token ထုတ်ယူထား](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo) ရှိကြောင်း သေချာစေပါ။  
3. AI Toolkit for VS Code တွင် Remote Fine-tuning နှင့် Inference feature flag ကို ဖွင့်ပါ  
   1. VS Code Settings ကို *File -> Preferences -> Settings* မှ ဖွင့်ပါ။  
   2. *Extensions* သို့ သွားပြီး *AI Toolkit* ကို ရွေးချယ်ပါ။  
   3. *"Enable Remote Fine-tuning And Inference"* ကို ဖွင့်ပါ။  
   4. ပြောင်းလဲမှုများ အကျိုးသက်ရောက်ရန် VS Code ကို ပြန်လည်စတင်ပါ။  

- [Remote Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### အဝေးမှ ဖွံ့ဖြိုးတိုးတက်မှု ပရောဂျက် တည်ဆောက်ခြင်း  
1. Command palette မှ `AI Toolkit: Focus on Resource View` ကို အကောင်အထည်ဖော်ပါ။  
2. *Model Fine-tuning* သို့ သွားပြီး မော်ဒယ် catalog ကို ဝင်ရောက်ပါ။ သင့်ပရောဂျက်အမည်နှင့် တည်နေရာကို သတ်မှတ်ပြီး *"Configure Project"* ခလုတ်ကို နှိပ်ပါ။  
3. ပရောဂျက် ဆက်တင်များ  
    1. *"Fine-tune locally"* ကို ဖွင့်ခြင်း မပြုပါနှင့်။  
    2. Olive configuration ဆက်တင်များသည် မူရင်းတန်ဖိုးများဖြင့် ပြသမည်ဖြစ်ပြီး လိုအပ်သလို ပြင်ဆင်နိုင်ပါသည်။  
    3. *Generate Project* ကို ဆက်လုပ်ပါ။ ဒီအဆင့်တွင် WSL ကို အသုံးပြုကာ Conda ပတ်ဝန်းကျင်အသစ် တည်ဆောက်ခြင်းနှင့် Dev Containers အတွက် ပြင်ဆင်မှုများ ပါဝင်သည်။  
4. *"Relaunch Window In Workspace"* ကို နှိပ်၍ အဝေးမှ ဖွံ့ဖြိုးတိုးတက်မှု ပရောဂျက်ကို ဖွင့်ပါ။

> **မှတ်ချက်** ပရောဂျက်သည် AI Toolkit for VS Code တွင် ဒေသခံ သို့မဟုတ် အဝေးမှ တစ်ခုတည်းသာ လည်ပတ်နိုင်သည်။ ပရောဂျက်ဖန်တီးစဉ် *"Fine-tune locally"* ကို ရွေးချယ်ပါက WSL အတွင်းတွင်သာ လည်ပတ်မည်ဖြစ်ပြီး အဝေးမှ ဖွံ့ဖြိုးတိုးတက်မှု မရရှိပါ။ *"Fine-tune locally"* ကို မဖွင့်ပါက အဝေးမှ Azure Container App ပတ်ဝန်းကျင်တွင်သာ လည်ပတ်မည်ဖြစ်သည်။

### Azure အရင်းအမြစ်များ ပေးအပ်ခြင်း  
အဝေးမှ fine-tuning စတင်ရန် Azure Resource ကို ပေးအပ်ရမည်။ Command palette မှ `AI Toolkit: Provision Azure Container Apps job for fine-tuning` ကို အသုံးပြုပါ။

Output channel တွင် ပြသသော link မှတဆင့် ပေးအပ်မှု တိုးတက်မှုကို ကြည့်ရှုနိုင်ပါသည်။

### [Optional] Huggingface Token ကို Azure Container App Secret ထဲ ထည့်ခြင်း  
Private HuggingFace dataset အသုံးပြုပါက HuggingFace token ကို environment variable အဖြစ် သတ်မှတ်၍ Hugging Face Hub တွင် လက်ဖြင့် login ပြုလုပ်ရန် မလိုအပ်စေရန် ပြုလုပ်နိုင်သည်။  
`AI Toolkit: Add Azure Container Apps Job secret for fine-tuning` command ဖြင့် secret name ကို [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) အဖြစ် သတ်မှတ်ပြီး Hugging Face token ကို secret value အဖြစ် သတ်မှတ်နိုင်ပါသည်။

### Fine-tuning ကို စတင်ပြုလုပ်ခြင်း  
အဝေးမှ fine-tuning job ကို စတင်ရန် `AI Toolkit: Run fine-tuning` command ကို အသုံးပြုပါ။

စနစ်နှင့် console logs များကို ကြည့်ရန် output panel တွင် ဖော်ပြထားသော link ဖြင့် Azure portal သို့ ဝင်ရောက်ကြည့်ရှုနိုင်သည် ([View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure))။ သို့မဟုတ် VSCode output panel တွင် `AI Toolkit: Show the running fine-tuning job streaming logs` command ဖြင့် console logs ကို တိုက်ရိုက် ကြည့်ရှုနိုင်ပါသည်။  
> **မှတ်ချက်** အရင်းအမြစ် မလုံလောက်မှုကြောင့် job များ စောင့်ဆိုင်းရနိုင်သည်။ log မပြသပါက `AI Toolkit: Show the running fine-tuning job streaming logs` command ကို ပြန်လည် အသုံးပြု၍ streaming log နှင့် ပြန်ဆက်သွယ်ပါ။

ဒီလုပ်ငန်းစဉ်တွင် QLoRA ကို fine-tuning အတွက် အသုံးပြုမည်ဖြစ်ပြီး inference အတွက် မော်ဒယ် LoRA adapters များ ဖန်တီးမည်ဖြစ်သည်။  
Fine-tuning ရလဒ်များကို Azure Files တွင် သိမ်းဆည်းမည်ဖြစ်သည်။

### Inference Endpoint ကို ပေးအပ်ခြင်း  
အဝေးမှ ပတ်ဝန်းကျင်တွင် adapters များ သင်ကြားပြီးနောက် မော်ဒယ်နှင့် ဆက်သွယ်ရန် ရိုးရှင်းသော Gradio application ကို အသုံးပြုပါ။  
Fine-tuning လုပ်ငန်းစဉ်ကဲ့သို့ Azure Resources ကို inference အတွက်လည်း `AI Toolkit: Provision Azure Container Apps for inference` command ဖြင့် ပေးအပ်ရမည်။

ပုံမှန်အားဖြင့် subscription နှင့် resource group များသည် fine-tuning အတွက် အသုံးပြုထားသည့် အတိုင်း ဖြစ်ရမည်။ Inference သည် Azure Container App Environment တူညီသည့် ပတ်ဝန်းကျင်ကို အသုံးပြုကာ fine-tuning အဆင့်တွင် Azure Files တွင် သိမ်းဆည်းထားသော မော်ဒယ်နှင့် မော်ဒယ် adapter များကို အသုံးပြုမည်ဖြစ်သည်။

### Inference Endpoint ကို တပ်ဆင်ခြင်း  
Inference code ကို ပြင်ဆင်လိုပါက သို့မဟုတ် inference မော်ဒယ်ကို ပြန်လည်တင်လိုပါက `AI Toolkit: Deploy for inference` command ကို အသုံးပြုပါ။ ၎င်းသည် သင့်နောက်ဆုံး code ကို Azure Container App နှင့် đồng bộ ပြုလုပ်ပြီး replica ကို ပြန်စတင်မည်ဖြစ်သည်။

တပ်ဆင်မှု အောင်မြင်ပြီးပါက VSCode notification တွင် ပြသသော "*Go to Inference Endpoint*" ခလုတ်ကို နှိပ်၍ inference API ကို ဝင်ရောက်အသုံးပြုနိုင်သည်။ သို့မဟုတ် inference API endpoint ကို `./infra/inference.config.json` ဖိုင်အတွင်း `ACA_APP_ENDPOINT` တွင်နှင့် output panel တွင် တွေ့နိုင်သည်။ ယခု သင်သည် မော်ဒယ်ကို အဆိုပါ endpoint ဖြင့် စမ်းသပ်ရန် အသင့်ဖြစ်ပါပြီ။

### အဆင့်မြင့် အသုံးပြုမှု  
AI Toolkit ဖြင့် အဝေးမှ ဖွံ့ဖြိုးတိုးတက်မှုအကြောင်း ပိုမိုသိရှိလိုပါက [Fine-Tuning models remotely](https://aka.ms/ai-toolkit/remote-provision) နှင့် [Inferencing with the fine-tuned model](https://aka.ms/ai-toolkit/remote-inference) စာတမ်းများကို ကြည့်ရှုပါ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။