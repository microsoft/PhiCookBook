# Microsoft Foundry နှင့် Phi-3 ကို ကြည့်၍ နည်းလမ်းမှန်ဆန်းကြည့်ခြင်း

 Microsoft ရဲ့ Phi-3 Mini ဘာသာစကားမော်ဒယ်ကို Microsoft Foundry အသုံးပြု၍ ဘယ်လိုနည်းလမ်းမှန်ဆန်းလုပ်မလဲဆိုတာ ကို ရှင်းပြကြမယ်။ နည်းလမ်းမှန်ဆန်းခြင်းက Phi-3 Mini ကို တိကျတဲ့တာဝန်တွေမှာအသုံးပြုဖို့ အထောက်အကူဖြစ်စေပြီး ပိုမိုတိုးတက်ပြီး စဉ်ဆက်မပြတ်အသုံးပြုနိုင်အောင်လုပ်ပေးပါတယ်။

## စဉ်းစားရန်အချက်များ

- **စွမ်းရည်များ:** ဘယ်မော်ဒယ်တွေကို နည်းလမ်းမှန်ဆန်းလို့ရမလဲ? မူလမော်ဒယ်ကို ဘာတွေပြောင်းလဲလို့ရမလဲ?
- **ကုန်ကျစရိတ်:** နည်းလမ်းမှန်ဆန်းမှုအတွက် စျေးနှုန်း မော်ဒယ် ဘယ်လိုရှိပါသလဲ?
- **ပြင်ဆင်နိုင်မှု:** မူလမော်ဒယ်ကို ဘယ်လောက်ပြောင်းလဲလို့ရသလဲ – ဘယ်လိုလမ်းများဖြင့်?
- **အသုံးပြုရအဆင်ပြေမှု:** နည်းလမ်းမှန်ဆန်းခြင်းဟာ ဘယ်လိုလုပ်ဆောင်ရသလဲ – ကိုယ်ပိုင်ကုဒ်ရေးရမလား? ကိုယ်ပိုင်ကွန်ပျူတာတွဲကြောင်းတင်ရမလား?
- **ဘေးကင်းလုံခြုံမှု:** နည်းလမ်းမှန်ဆန်းထားတဲ့မော်ဒယ်တွေမှာ ဘေးကင်းလုံခြုံမှုဆိုင်ရာကာကွယ်ချက်တွေရှိလား?

![AIFoundry Models](../../../../translated_images/my/AIFoundryModels.0e1b16f7d0b09b73.webp)

## နည်းလမ်းမှန်ဆန်းခြင်းအတွက် အဆင်သင့်ပြင်ဆင်ခြင်း

### လိုအပ်ချက်များ

> [!NOTE]
> Phi-3 မိသားစု မော်ဒယ်များအတွက် pay-as-you-go မော်ဒယ်နည်းလမ်းမှန်ဆန်းမှုကို **East US 2** ဒေသတွင် ဖန်တီးထားသော hubs တွင်သာ အသုံးပြုနိုင်ပါသည်။

- Azure subscription တစ်ခု။ Azure subscription မရှိပါက၊ စတင်ရန် [ပေးသွင်းသော Azure အကောင့်](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) တစ်ခု ဖန်တီးပါ။

- [AI Foundry စီမံကိန်း](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) တစ်ခု။
- Microsoft Foundry တွင် လုပ်ဆောင်ချက် ဝင်ခွင့်များအတွက် Azure role-based access control (Azure RBAC) ကို အသုံးပြုသည်။ ဤဆောင်းပါးတွင် ဖော်ပြထားသော အဆင့်များကို လုပ်ဆောင်ရန် သင့်အသုံးပြုသူအကောင့်သည် resource group တွင် __Azure AI Developer အခန်းကဏ္ဍ__ ပြဿနာတစ်ခု ရှိရပါမည်။

### Subscription provider မှတ်ပုံတင်ခြင်း

`Microsoft.Network` resource provider သို့ subscription မှတ်ပုံတင်ထားမှုကို သေချာစစ်ဆေးပါ။

1. [Azure portal](https://portal.azure.com) သို့ ဝင်ရောက်ပါ။
1. ဘယ်ဘက် menu မှ **Subscriptions** ကို ရွေးချယ်ပါ။
1. သုံးရန် ရွေးချယ်လိုသော subscription ကို ရွေးပါ။
1. ဘယ်ဘက် menu မှ **AI project settings** > **Resource providers** ကို ရွေးချယ်ပါ။
1. **Microsoft.Network** သည် resource providers စာရင်းတွင် ပါဝင်နေကြောင်း အတည်ပြုပါ။ မပါလျှင် ထည့်သွင်းပါ။

### ဒေတာပြင်ဆင်ခြင်း

သင့်မော်ဒယ်ကို နည်းလမ်းမှန်ဆန်းရန် သင်ယူမှုနှင့် အတည်ပြုမှု ဒေတာများကို ပြင်ဆင်ပါ။ သင်ယူမှု ဒေတာနှင့် အတည်ပြုမှု ဒေတာစုံတွင်းမှာ မော်ဒယ် တုန့်ပြန်မှုစွမ်းရည် အပ္ النارညအတိအကျ များကိုပြသထားခြင်းဖြစ်သည်။

သင်ယူမှု ဥပမာများအားလုံးသည် စောင့်ကြည့်ချက်မှတ်စုများထည့်သွင်းထားသော ပုံစံနှင့် ကိုက်ညီရန် သေချာစေပါ။ မော်ဒယ်များကို ထိရောက်စွာ နည်းလမ်းမှန်ဆန်းရန်, ဒေတာထဲတွင် တန်းတူညီမျှမှုနှင့် မျိုးစုံမှုရှိခြင်း သေချာစေရမည်။

ဤသည်မှာ ဒေတာထဲတွင် ထိပ်တန်းအချက်အလက်မတူညီမှု ထိန်းသိမ်းခြင်း၊ ကွဲပြားသော သဘောထားများထည့်သွင်းခြင်းနှင့် လက်တွေ့အသုံးပြုမှုနှင့် ကိုက်ညီရန် ဒေတာကို စာချုပ်ဆောင်ရွက်ခြင်းတို့ ပါဝင်သည်။ ထို့ကြောင့် မော်ဒယ် တုန့်ပြန်မှုများမှာ တိကျမှန်ကန်ပြီး တန်းတူညီမျှမှုရှိစေပါသည်။

မတူညီသော မော်ဒယ်အမျိုးအစားများကို သင်ယူမှု ဒေတာပုံစံ မတူညီသည်။

### စကားဝိုင်း ပြည့်စုံမှု

သင်သုံးမယ့် သင်ယူမှု နှင့် အတည်ပြုမှု ဒေတာများကို JSON Lines (JSONL) စာရွက်အဖြစ် အတိုင်းအတာဖြစ်သင့်သည်။ `Phi-3-mini-128k-instruct` အတွက် နည်းလမ်းမှန်ဆန်း ဒေတာများသည် Chat completions API မှ အသုံးပြုနေသော စကားဝိုင်း ပုံစံ အတိုင်း ဖြစ်ရမည်။

### ဥပမာဖိုင် ပုံစံ

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```
  
အထောက်အထား ဖိုင် အမျိုးအစားမှာ JSON Lines ဖြစ်သည်။ ဖိုင်များကို ပုံမှန် datastore တွင် တင်ပြီး သင့် စီမံကိန်းတွင် အသုံးပြုနိုင်သည်။

## Microsoft Foundry နှင့် Phi-3 ကို နည်းလမ်းမှန်ဆန်းခြင်း

Microsoft Foundry သည် မကြီးမားသော ဘာသာစကားမော်ဒယ်များကို ကိုယ်ပိုင် ဒေတာအစုအဝေးများ သို့ ကိုက်ညီအောင် နည်းလမ်းမှန်ဆန်းစေလို့ရသည်။ နည်းလမ်းမှန်ဆန်းခြင်းသည် ထူးခြားသော တာဝန်များနဲ့ လျှောက်လွှာများအတွက် တိကျမှုနှင့် တိုးတက်မှု၊ စျေးနှုန်းပိုတတ်နိုင်ခြင်း၊ တုံ့ပြန်ချိန်လျော့နည်းမှုနဲ့ ကိုက်ညီစေရန် ထူးခြားသော တန်ဖိုးများ ပေးသည်။

![Finetune AI Foundry](../../../../translated_images/my/AIFoundryfinetune.193aaddce48d553c.webp)

### စီမံကိန်းအသစ် ဖန်တီးခြင်း

1. [Microsoft Foundry](https://ai.azure.com) သို့ ၀င်ရောက်ပါ။

1. **+New project** ကို နှိပ်ကာ Microsoft Foundry မှ စီမံကိန်းအသစ် ဖန်တီးပါ။

    ![FineTuneSelect](../../../../translated_images/my/select-new-project.cd31c0404088d7a3.webp)

1. အောက်ဖော်ပြပါ အလုပ်များကို ဆောင်ရွက်ပါ-

    - စီမံကိန်း **Hub name** ကို ထည့်သွင်းပါ။ ထူးခြားသောတန်ဖိုးဖြစ်ရမည်။
    - အသုံးပြုမည့် **Hub** ကို ရွေးချယ်ပါ (လိုအပ်လျှင် အသစ်တည်ဆောက်ပါ)။

    ![FineTuneSelect](../../../../translated_images/my/create-project.ca3b71298b90e420.webp)

1. Hub အသစ် ဖန်တီးရန် အောက်ပါ အချက်အလက်များ ထည့်သွင်းပါ-

    - **Hub name** ထည့်သွင်းပါ။ ထူးခြားသောတန်ဖိုး ဖြစ်ရမည်။
    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - 사용하려는 **Resource group** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်ဖန်တီးပါ)။
    - အသုံးပြုမည့် **Location** ကို ရွေးချယ်ပါ။
    - အသုံးပြုမည့် **Connect Azure AI Services** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ်ဖန်တီးပါ)။
    - **Connect Azure AI Search** ကို **Skip connecting** အဖြစ် ရွေးချယ်ပါ။

    ![FineTuneSelect](../../../../translated_images/my/create-hub.49e53d235e80779e.webp)

1. **Next** ကို နှိပ်ပါ။
1. **Create a project** ကို နှိပ်ပါ။

### ဒေတာပြင်ဆင်ခြင်း

နည်းလမ်းမှန်ဆန်းခြင်းမလုပ်ခင်၊ သင့်တာဝန်နှင့် သက်ဆိုင်သော ဒေတာအစုအဝေး (ဥပမာ စကားဝိုင်း လမ်းညွှန်ချက်များ၊ မေးခွန်း-ဖြေကြား စာရင်းများ သို့မဟုတ် အခြားသက်ဆိုင်သော စာသားဒေတာ) များ စုဆောင်း သို့မဟုတ် ဖန်တီးပါ။ ဤဒေတာများကို မဆိုးရွားမှု, လျော့နည်းမှုများ ဆောင်ရွက်ပြီး စာသား Tokenization လုပ်ပါ။

### Microsoft Foundry တွင် Phi-3 မော်ဒယ်များ နည်းလမ်းမှန်ဆန်းခြင်း

> [!NOTE]
> Phi-3 မော်ဒယ်များအတွက် နည်းလမ်းမှန်ဆန်းခြင်းသည် ယခုအခါ East US 2 တွင် တည်ရှိေသာ စီမံကိန်းများအတွက်သာ ထောက်ပံ့ထားသည်။

1. ဘယ်ဘက်အပေါ်မှ အတန်းအဆင့်таб မှ **Model catalog** ကို ရွေးချယ်ပါ။

1. **ရှာဖွေရေးခုံ** တွင် *phi-3* ဟု ရိုက်ထည့်ပြီး သင် အသုံးပြုလိုသော phi-3 မော်ဒယ်ကို ရွေးချယ်ပါ။

    ![FineTuneSelect](../../../../translated_images/my/select-model.60ef2d4a6a3cec57.webp)

1. **Fine-tune** ကို ရွေးပါ။

    ![FineTuneSelect](../../../../translated_images/my/select-finetune.a976213b543dd9d8.webp)

1. **Fine-tuned model name** ကို ထည့်ပါ။

    ![FineTuneSelect](../../../../translated_images/my/finetune1.c2b39463f0d34148.webp)

1. **Next** ကို နှိပ်ပါ။

1. အောက်ပါ အလုပ်များကို ဆောင်ရွက်ပါ-

    - **task type** ကို **Chat completion** အဖြစ် ရွေးချယ်ပါ။
    - သင်သုံးလိုသော **Training data** ကို ရွေးချယ်ပါ။ Microsoft Foundry ၏ ဒေတာသိုလှောင်မှုမှ သို့မဟုတ် ကိုယ်တည်မြှောက်ထားသော လုပ်ငန်းဆောင်ရွက်ပတ်ဝန်းကျင်မှ တင်နိုင်ပါသည်။

    ![FineTuneSelect](../../../../translated_images/my/finetune2.43cb099b1a94442d.webp)

1. **Next** ကို နှိပ်ပါ။

1. သင်သုံးမည့် **Validation data** ကို တင်ပါ။ သို့မဟုတ် **Automatic split of training data** ကို ရွေးချယ်နိုင်ပါသည်။

    ![FineTuneSelect](../../../../translated_images/my/finetune3.fd96121b67dcdd92.webp)

1. **Next** ကို နှိပ်ပါ။

1. အောက်ဖော်ပြပါ အလုပ်များကို ဆောင်ရွက်ပါ-

    - သင်သုံးချင်သော **Batch size multiplier** ကို ရွေးပါ။
    - သင်သုံးချင်သော **Learning rate** ကို ရွေးပါ။
    - သင်သုံးချင်သော **Epochs** ကို ရွေးပါ။

    ![FineTuneSelect](../../../../translated_images/my/finetune4.e18b80ffccb5834a.webp)

1. နည်းလမ်းမှန်ဆန်းခြင်းလုပ်ငန်းစဉ်စတင်ရန် **Submit** ကို နှိပ်ပါ။

    ![FineTuneSelect](../../../../translated_images/my/select-submit.0a3802d581bac271.webp)

1. မော်ဒယ်ဆန်းသစ်မှု ပြီးဆုံးပါက အခြေအနေနှင့် **Completed** ဟု မြင်နိုင်ပါမည်။ ယခုမော်ဒယ်ကို တပ်ဆင်ပြီး ကိုယ်ပိုင် အကောင့်၊ playground သို့မဟုတ် prompt flow တွင် အသုံးပြုနိုင်ပါပြီ။ ဆက်လက်သိရှိရန် [Microsoft Foundry ဖြင့် Phi-3 မော်ဒယ် ပြန်လည်တပ်ဆင်ခြင်း](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ကို ကြည့်ပါ။

    ![FineTuneSelect](../../../../translated_images/my/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Phi-3 မော်ဒယ်များ နည်းလမ်းမှန်ဆန်းခြင်းအပေါ် အသေးစိတ် အချက်အလက်များအတွက် [Microsoft Foundry တွင် Phi-3 မော်ဒယ်များ နည်းလမ်းမှန်ဆန်းခြင်း](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini) ကို ကြည့်ပါ။

## နည်းလမ်းမှန်ဆန်းထားမော်ဒယ် များကို ရှင်းလင်းခြင်း

[Microsoft Foundry](https://ai.azure.com) ၏ နည်းလမ်းမှန်ဆန်းထားမော်ဒယ်စာရင်းမှ သို့မဟုတ် မော်ဒယ်အသေးစိတ်စာမျက်နှာမှ နည်းလမ်းမှန်ဆန်းထားမော်ဒယ်ကို ဖျက်ရန် ရွေးချယ်ပြီး Delete ခလုတ်ကို နှိပ်ပါ။

> [!NOTE]
> လက်ရှိ တပ်ဆင်ထားသော မော်ဒယ်ကို ဖျက်၍ မရပါ။ မော်ဒယ်ဖျက်ရန် မူရင်းမော်ဒယ်ဒေတာ တပ်ဆင်မှုကို ပထမဦးဆုံး ဖျက်သိမ်းရန် လိုအပ်ပါသည်။

## စရိတ်နှင့် မှန်ကန်မှုများ

### Phi-3 မော်ဒယ်များကို ဝန်ဆောင်မှု အဖြစ် နည်းလမ်းမှန်ဆန်းခြင်း စရိတ်နှင့် အကန့်အသတ်များ

Phi မော်ဒယ်များကို Microsoft က တိုးချဲ့ပေးထားပြီး Microsoft Foundry နှင့် ပေါင်းစပ်အသုံးပြုနိုင်သည်။ မော်ဒယ်များကို တပ်ဆင်ခြင်း သို့မဟုတ် နည်းလမ်းမှန်ဆန်းခြင်း စဉ်တွင် စျေးနှုန်းကို Deployment Wizard ၏ Pricing နှင့် Terms tab တွင် ကြည့်ရှုနိုင်ပါသည်။

## အကြောင်းအရာ စစ်ထုတ်ခြင်း

pay-as-you-go ဝန်ဆောင်မှုအဖြစ် တပ်ဆင်ထားသော မော်ဒယ်များသည် Azure AI Content Safety ခြံရံပေးသည်။ အချိန်နှင့်တပြေးညီ Endpoint တွင် တပ်ဆင်သောအခါ ဤစနစ်ကို ရွေးချယ်ချလိုက်နိုင်သည်။ Azure AI Content Safety သည် Prompt နှင့် Completion နှစ်ဖက်လုံးကို မသင့်တော်သော အကြောင်းအရာ ထွက်ပေါ်ခြင်းကိုမှတ်သား စစ်ဆေးကာ တားဆီးရန် ရည်ရွယ်သော မော်ဒယ်များစုစည်းထားသော စနစ်ဖြစ်သည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering) အကြောင်း ပိုမိုသိရှိရန် ကြည့်ရန်။

**နည်းလမ်းမှန်ဆန်းမှု ပြင်ဆင်ပုံ**

Hyperparameters: learning rate, batch size, အားလုံးသော training epochs တို့ကို သတ်မှတ်ပါ။

**ဆုံးရှုံးမှု ဖွင့်ဆိုမှု**

သင်လုပ်ဆောင်လိုသည့်တာဝန်အတွက် (ဥပမာ cross-entropy) သင့်တော်သော loss function ကို ရွေးချယ်ပါ။

**Optimizer**

သင်ယူခြင်းအလားအလာ အတွက် optimizer (ဥပမာ Adam) ကို ရွေးချယ်ပါ။

**နည်းလမ်းမှန်ဆန်းမှု လုပ်ငန်းစဉ်**

- Pre-Trained Model အား Load ရယူပါ: Phi-3 Mini checkpoint ကို Load ရယူပါ။
- Custom Layers ကို ထည့်သွင်းပါ: တာဝန်အလိုက် အဆင့်ပိုမို (ဥပမာ စကားဝိုင်း လမ်းညွှန်ချက်များအတွက် classification ကိုယ်တိုင်) ထည့်သွင်းပါ။

**မော်ဒယ် သင်ယူခြင်း**  
သင့်ပြင်ဆင်ထားသော ဒေတာအသုံးပြု၍ နည်းလမ်းမှန်ဆန်းပါ။ သင်ယူမှုတိုးတက်မှုကို စောင့်ကြည့်ပြီး Hyperparameters များကို လိုအပ်သလို ပြင်ဆင်ပါ။

**အတည်ပြုခြင်း နှင့် စစ်ဆေးခြင်း**

Validation Set: သင်ယူမှု ဒေတာကို နှစ်ပိုင်းခွဲထားပါ။

**စွမ်းဆောင်ရည် တိုင်းတာခြင်း**

တိကျမှု, F1-score သို့မဟုတ် perplexity စသည်ဖြင့် မော်ဒယ်၏ စွမ်းဆောင်ရည် ကို တိုင်းတာပါ။

## နည်းလမ်းမှန်ဆန်းထား မော်ဒယ် သိမ်းဆည်းခြင်း

**Checkpoint**  
နောက်အတွက် အသုံးပြုရန် နည်းလမ်းမှန်ဆန်းထားသော မော်ဒယ် checkpoint ကို သိမ်းဆည်းပါ။

## တပ်ဆင်ခြင်း

- Web Service အဖြစ် တပ်ဆင်ခြင်း: Microsoft Foundry တွင် သင့်နည်းလမ်းမှန်ဆန်းထား မော်ဒယ်ကို web service အဖြစ် တပ်ဆင်ပါ။
- Endpoint စမ်းသပ်ခြင်း: တပ်ဆင်ပြီး endpoint ကို စမ်းသပ်မေးမြန်းပေးခြင်းဖြင့် လုပ်ဆောင်နိုင်မှုကို အတည်ပြုပါ။

## ပြန်လည်တိုးတက်ရေးဆွဲခြင်းနှင့် တိုးတက်မှု

ထူးခွားမှု မရရှိခဲ့ရင် Hyperparameters ပြင်ဆင်ခြင်း၊ ဒေတာ ပိုမို ထည့်သွင်းခြင်း သို့မဟုတ် epochs ပိုမို များပြားအောင် နည်းလမ်းမှန်ဆန်းခြင်း ဆက်လုပ်ပါ။

## စောင့်ကြည့်ခြင်းနှင့် ပြင်ဆင်ခြင်း

မော်ဒယ်၏ လုပ်ရပ်များကို ဆက်လက် မျက်မှောက်၍ လိုအပ်ပါက ပြန်လည်ပြောင်းလဲပါ။

## ကိုယ်ပိုင်ပြင်ဆင်ခြင်းနှင့် တိုးချဲ့ခြင်း

Custom Tasks: Phi-3 Mini သည် စကားဝိုင်း လမ်းညွှန်ချက်များမှ ပို၍ ကြားနာမှု မတူညီသောတာဝန်များအတွက် နည်းလမ်းမှန်ဆန်းလို့ ရသည်။ အခြားအသုံးပြုမှုများကိုလည်း စမ်းသပ်ပါ။
နည်းလမ်းများ: စွန့်စားမှုနှင့် လေ့လာမှုများ ပြုလုပ်ကာ ဆောက်လုပ်မှု အမျိုးမျိုး၊ အဆင့်ပေါင်းများနှင့် နည်းဗျူဟာများ အသုံးပြုပြီး စွမ်းဆောင်မှု တိုးတက်အောင် ကြိုးပမ်းပါ။

> [!NOTE]
> နည်းလမ်းမှန်ဆန်းခြင်းသည် အချိန်အကြာကြီး ဆက်လက်ဆောင်ရွက်ရမည့် လုပ်ငန်းစဉ်ဖြစ်သည်။ စမ်းသပ်၊ သင်ယူကာ မော်ဒယ်အား သင့်တာဝန်အတွက် အကောင်းဆုံး ရလဒ်ရရှိရန် ထိန်းသိမ်းပြင်ဆင်လိုက်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ငါးမႉးစာ**:
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျနော်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းလျက်ရှိသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုရန် လိုအပ်ပါသည်။ နိုင်ငံရပ်ခြားဘာသာစကားဖြင့် ရေးသားထားသော မူရင်းစာတမ်းကို အာဏာပိုင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လူ့ဘာသာပြန် အတတ်ပညာရှင်များ၏ ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသည့် နားမလည်မှုများ သို့မဟုတ် အဓိပ္ပါယ်လွဲမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->