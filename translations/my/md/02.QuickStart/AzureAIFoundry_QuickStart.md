# **Microsoft Foundry တွင် Phi-3 အသုံးပြုခြင်း**

Generative AI အဆင့်တိုးတက်လာမှုနှင့်အတူ၊ ကွဲပြားတဲ့ LLM နှင့် SLM များ၊ စီးပွားရေးဒေတာပေါင်းစည်းမှု၊ fine-tuning/RAG လုပ်ငန်းဆောင်တာများနှင့် LLM နှင့် SLM ပေါင်းစပ်ပြီးနောက် စီးပွားရေးလုပ်ငန်းများအကဲဖြတ်ခြင်းများကို စုစည်းစီမံရန် ယုံကြည်စိတ်ချရသောပလက်ဖောင်းတစ်ခုအသုံးပြုနိုင်ရန်၊ generative AI ကို Smart applications တွင် ပိုမိုကောင်းမွန်စွာ ဆောင်ရွက်နိုင်ရန်ကို မျှော်လင့်ပါတယ်။ [Microsoft Foundry](https://ai.azure.com) သည် စီးပွားရေးအဆင့် generative AI အက်ပ်ပလီကေးရှင်းပလက်ဖောင်းတစ်ခုဖြစ်သည်။

![aistudo](../../../../translated_images/my/aifoundry_home.f28a8127c96c7d93.webp)

Microsoft Foundry ဖြင့် LLM အဖြေများအား အကဲဖြတ်ခြင်းနှင့် prompt flow အသုံးပြု၍ prompt application အစိတ်အပိုင်းများကို စီမံခန့်ခွဲကာ ပိုမိုကောင်းမွန်သောစွမ်းဆောင်ရည်ရရှိစေရန် အစီအစဉ်ရေးဆွဲနိုင်သည်။ ဤပလက်ဖောင်းသည် proof of concepts မှ အထူးပြည့်စုံသော ထုတ်လုပ်မှုဖြစ်လာရန် အလွယ်တကူ အဆင့်တိုးနိုင်စေပြီး၊ ဆက်လက်ကြည့်ရှုခြင်းနှင့် တိုးတက်မှုဆောင်ရွက်မှုများကို ရှေ့ဆက်အောင်လုပ်ဆောင် နိုင်သည်။

Microsoft Foundry တွင် Phi-3 မော်ဒယ်ကို လွယ်ကူသောခြေလှမ်းများဖြင့် အမြန်လှုပ်ရှားတပ်ဆင်နိုင်ပြီး၊ ပြီးနောက် Microsoft Foundry ကို အသုံးပြု၍ Phi-3 နှင့်ပတ်သတ်သော Playground/Chat, Fine-tuning, အကဲဖြတ်ခြင်းနှင့် အခြားဆက်စပ်အလုပ်များ ပြီးမြောက်နိုင်သည်။

## **1. ပြင်ဆင်မှု**

သင့်ကွန်ပျူတာတွင် [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) များကို ရှိပြီးသားဖြစ်ပါက၊ ဤ template ကို အသစ် directory တစ်ခုတွင် ဒီ command ကို run ပြုလုပ်ရန်သာ လိုအပ်ပါသည်။

## လက်ဖြင့်ဖန်တီးခြင်း

Microsoft Foundry project နှင့် hub ဖန်တီးခြင်းသည် သင့် AI အလုပ်များကို စီစဉ်စနစ်ရှိစွာ စီမံရန်အတွက်ကောင်းမွန်သောနည်းလမ်းဖြစ်သည်။ စတင်ရန်အတွက် လမ်းညွှန်ချက်အဆင့်ဆင့်မှာ အောက်ပါအတိုင်းဖြစ်သည်-

### Microsoft Foundry တွင် Project တစ်ခု ဖန်တီးခြင်း

1. **Microsoft Foundry သို့ သွားပါ**: Microsoft Foundry portal တွင် လက်ရှိ၀င်ပါ။
2. **Project ဖန်တီးပါ**:
   - Project အတွင်းရှိပါက၊ စာမျက်နှာ၏ ဘယ်ဘက်ထိပ်တွင်ရှိသော "Microsoft Foundry" ကိုရွေးချယ်၍ Home စာမျက်နှာသို့ သွားပါ။
   - "+ Create project" ကိုရွေးပါ။
   - Project အတွက် နာမည်ထည့်ပါ။
   - Hub ရှိပါက အလိုအလျောက် ရွေးချယ်ထားမည်။ Hub များစွာ ရရှိနိုင်ပါက dropdown မှ အခြား hub ကို ရွေးချယ်နိုင်သည်။ Hub အသစ်တစ်ခု ဖန်တီးလိုပါက "Create new hub" ကိုရွေးချယ်ပြီး နာမည်ထည့်ပါ။
   - "Create" ကိုနှိပ်ပါ။

### Microsoft Foundry တွင် Hub တစ်ခု ဖန်တီးခြင်း

1. **Microsoft Foundry သို့ သွားပါ**: Azure အကောင့်ဖြင့် လက်ရှိ၀င်ပါ။
2. **Hub တစ်ခု ဖန်တီးပါ**:
   - ဘယ်ဘက် menu မှ Management center ကို ရွေးပါ။
   - "All resources" ကိုရွေးပြီး၊ "+ New project" ရှိအောက်ကျသော down arrow ကိုနှိပ်၍ "+ New hub" ကိုရွေးပါ။
   - "Create a new hub" ပြတင်းပေါ်တွင် hub အတွက် နာမည်ကိုထည့်ပါ (ဥပမာ contoso-hub) နှင့် အခြား field များကိုလိုအပ်သလို ပြောင်းလဲပါ။
   - "Next" ကိုနှိပ်ပြီး သတင်းအချက်အလက်များ ရှုထောင့်ကြည့်ပါ၊ ပြီးနောက် "Create" ကို နှိပ်ပါ။

အသေးစိတ်အချက်အလက်များအတွက် တရားဝင် [Microsoft စာတမ်းများ](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects) ကို ရည်ညွှန်းနိုင်ပါသည်။

ဖန်တီးမှု အောင်မြင်ပြီးနောက် သင်ဖန်တီးသော studio ကို [ai.azure.com](https://ai.azure.com/) မှတဆင့် ဝင်ရောက် ကြည့်ရှုနိုင်မည်ဖြစ်သည်။

AI Foundry တစ်ခုအတွင်း project များစွာ ရှိနိုင်သည်။ AI Foundry တွင် project တစ်ခုဖန်တီး၍ ပြင်ဆင်ပါ။

Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code) များကို ဖန်တီးပါ။

## **2. Microsoft Foundry တွင် Phi မော်ဒယ် တပ်ဆင်ခြင်း**

Project ၏ Explore ရွေးချယ်မှုကိုနှိပ်၍ Model Catalog ထဲသို့ ဝင်ပါ၊ Phi-3 ကို ရွေးချယ်ပါ။

Phi-3-mini-4k-instruct ကို ရွေးပါ။

'Deploy' ကိုနှိပ်၍ Phi-3-mini-4k-instruct မော်ဒယ်ကို တပ်ဆင်ပါ။

> [!NOTE]
>
> တပ်ဆင်စဉ်တွင် computing power ကို ရွေးချယ်နိုင်သည်။

## **3. Microsoft Foundry တွင် Playground Chat Phi**

Deployment စာမျက်နှာသို့ သွား၍ Playground ကို ရွေးချယ်ပါ၊ Microsoft Foundry ၏ Phi-3 နှင့် စကားပြောနိုင်သည်။

## **4. Microsoft Foundry မှ Model တပ်ဆင်ခြင်း**

Azure Model Catalog မှ မော်ဒယ်တစ်ခုကို တက်ဆင်ရန်အတွက် အောက်ပါအဆင့်များကိုလိုက်နာပါ-

- Microsoft Foundry တွင် လက်မှတ်ထိုး၀င်ပါ။
- Microsoft Foundry model catalog မှ တပ်ဆင်လိုသည့် မော်ဒယ်ကို ရွေးချယ်ပါ။
- မော်ဒယ်၏ Details စာမျက်နှာတွင် Deploy ကိုရွေး၍ Azure AI Content Safety ပါသော Serverless API ကိုရွေးပါ။
- မော်ဒယ်များ တပ်ဆင်မည့် project ကို ရွေးချယ်ပါ။ Serverless API ကို အသုံးပြုရန် workspace သင့်သည် East US 2 သို့မဟုတ် Sweden Central ဒေသတွင် တည်ရှိရမည်ဖြစ်သည်။ Deployment နာမည်ကို သင့်ကြိုက်နှစ်သက်ရာဖြင့် ပုံသွင်းနိုင်ပါသည်။
- Deployment wizard တွင် Pricing နှင့် terms များကို လေ့လာပါ။
- Deploy ကိုနှိပ်ပါ။ Deployment ပြီးဆုံးပြီး Deployments စာမျက်နှာသို့ ရောက်သည်အထိ ခံစားစားပါ။
- PlayGround တွင် ဖွင့်ပြီး မော်ဒယ်နှင့် ဆက်သွယ်မှုအစပြုနိုင်သည်။
- Deployments စာမျက်နှာသို့ ပြန်ရောက်၊ သတ်မှတ်ထားသော deployment ကို ရွေးချယ်၍ Target URL နှင့် Secret Key ကို မှတ်သားပါ၊ မတိုင်မီ deployment ကိုခေါ်ယူ၍ completions များ ဖန်တီးရန်အသုံးပြုနိုင်သည်။
- Endpoint ၏ အသေးစိတ်များ၊ URL နှင့် access keys များကို Build tab ထဲရှိ Components အပိုင်းမှ Deployments ကိုရွေးချယ်ကာ ပြန်လည်ကြည့်ရှုနိုင်သည်။

> [!NOTE]
> ဤအဆင့်များ ဆောင်ရွက်လိုပါက သင်၏အကောင့်တွင် Resource Group အပေါ် Azure AI Developer role permissions ရှိရမည်ဖြစ်သည်။

## **5. Microsoft Foundry တွင် Phi API အသုံးပြုခြင်း**

https://{Your project name}.region.inference.ml.azure.com/swagger.json သို့ Postman GET ဖြင့် ဝင်ရောက်နိုင်ပြီး Key နှင့် ပေါင်းစပ်၍ ပံ့ပိုးသော အင်တာဖေ့စ်များအကြောင်း သိရှိနိုင်ပါသည်။

တောင်းဆိုချက် parameters များနှင့် တုံ့ပြန်ချက် parameters များ အလွန်အဆင်ပြေစွာ ရနိုင်သည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**နိဒါန်း**:  
ဤစာတမ်းကို AI ဘာသာပြန်မှုဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် မှားယွင်းချက်များ သို့မဟုတ် မှန်ကန်မှုလျော့နည်းမှုများ ရှိနိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံပါသည်။ မူလစာတမ်းမှာ သူ့ဘာသာဖြင့်သာ ထိပ်တန်း ယုံကြည်စိတ်ချရသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုရာမှ ဖြစ်ပေါ်နိုင်သော မသိမှတ်ချက်များ သို့မဟုတ် မမှန်ကန်စွာအသိနားလည်မှုများအတွက် ကျွန်ုပ်တို့ တာဝန် မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->