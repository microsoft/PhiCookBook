<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-09T19:31:43+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "my"
}
-->
# **Microsoft Phi-3 မိသားစုဖြင့် သင့်ကိုယ်ပိုင် Visual Studio Code GitHub Copilot Chat တည်ဆောက်ခြင်း**

GitHub Copilot Chat မှာ workspace agent ကို အသုံးပြုဖူးပါသလား? သင့်အဖွဲ့ရဲ့ ကိုဒ်အေးဂျင့်ကို ကိုယ်တိုင် တည်ဆောက်ချင်ပါသလား? ဒီလက်တွေ့လေ့ကျင့်ခန်းက open source မော်ဒယ်ကို ပေါင်းစပ်ပြီး စီးပွားရေးအဆင့်ရှိ ကိုဒ်လုပ်ငန်းအေးဂျင့်တစ်ခု တည်ဆောက်ဖို့ ရည်ရွယ်ထားပါတယ်။

## **အခြေခံအချက်များ**

### **Microsoft Phi-3 ကို ဘာကြောင့် ရွေးချယ်သင့်သလဲ**

Phi-3 သည် မိသားစုစီးရီးတစ်ခုဖြစ်ပြီး phi-3-mini, phi-3-small, phi-3-medium တို့ကို စာသားဖန်တီးခြင်း၊ စကားပြောပြီးစီးခြင်းနှင့် ကိုဒ်ဖန်တီးခြင်းအတွက် သင်ကြားမှု ပါရာမီတာ မတူညီမှုအပေါ် အခြေခံ၍ ဖွဲ့စည်းထားသည်။ Vision အခြေခံ phi-3-vision လည်း ပါဝင်သည်။ စီးပွားရေးလုပ်ငန်းများ သို့မဟုတ် အဖွဲ့အစည်းအမျိုးမျိုးအတွက် offline generative AI ဖြေရှင်းချက်များ ဖန်တီးရန် သင့်တော်သည်။

အောက်ပါလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုသည် [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat extension သည် VS Code အတွင်း GitHub Copilot နှင့် ဆက်သွယ်နိုင်သော စကားပြောအင်တာဖေ့စ်ကို ပေးပြီး ကိုဒ်ရေးရာဆိုင်ရာ မေးခွန်းများကို တိုက်ရိုက်ဖြေကြားပေးသည်။ ဒါကြောင့် စာရွက်စာတမ်းများကို ရှာဖွေရန် သို့မဟုတ် အွန်လိုင်းဖိုရမ်များကို ရှာဖွေရန် မလိုအပ် again။

Copilot Chat သည် syntax highlighting, indentation နှင့် အခြားဖော်မတ်လုပ်ဆောင်ချက်များကို အသုံးပြု၍ ဖန်တီးထားသော ဖြေကြားချက်ကို ပိုမိုရှင်းလင်းစေသည်။ အသုံးပြုသူ မေးခွန်းအမျိုးအစားပေါ်မူတည်၍ Copilot သည် ဖြေကြားချက်ထဲတွင် အသုံးပြုထားသော အကြောင်းအရာများ (ဥပမာ - ကိုဒ်ဖိုင်များ သို့မဟုတ် စာရွက်စာတမ်းများ) သို့မဟုတ် VS Code လုပ်ဆောင်ချက်များကို ချိတ်ဆက်ပေးသည့် ခလုတ်များ ပါဝင်နိုင်သည်။

- Copilot Chat သည် သင့် developer လုပ်ငန်းစဉ်နှင့် ပေါင်းစပ်ပြီး လိုအပ်သည့်နေရာတွင် အကူအညီပေးသည်။

- ကိုဒ်ရေးနေစဉ်တွင် တိုက်ရိုက် editor သို့ terminal မှ inline chat စတင်နိုင်သည်။

- Chat view ကို အသုံးပြု၍ အချိန်မရွေး AI အကူအညီကို ရရှိနိုင်သည်။

- Quick Chat ကို စတင်၍ မေးခွန်းတိုတောင်းပြီး လုပ်ဆောင်နေသည့်အရာသို့ ပြန်သွားနိုင်သည်။

GitHub Copilot Chat ကို အမျိုးမျိုးသော အခြေအနေများတွင် အသုံးပြုနိုင်သည်၊ ဥပမာ -

- ပြဿနာကို အကောင်းဆုံး ဖြေရှင်းနည်းများကို ဖြေကြားခြင်း

- တခြားသူ၏ ကိုဒ်ကို ရှင်းပြပြီး တိုးတက်မှုအကြံပြုခြင်း

- ကိုဒ်ပြင်ဆင်မှုများ အကြံပြုခြင်း

- Unit test case များ ဖန်တီးခြင်း

- ကိုဒ်စာရွက်စာတမ်းများ ဖန်တီးခြင်း

အောက်ပါလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုသည် [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat တွင် **@workspace** ကို ကိုးကားခြင်းဖြင့် သင့်ကုဒ်ဘေ့စ်အားလုံးအကြောင်း မေးမြန်းနိုင်သည်။ မေးခွန်းအပေါ်မူတည်၍ Copilot သည် သင့်မေးခွန်းနှင့် သက်ဆိုင်သော ဖိုင်များနှင့် သင်္ကေတများကို အတိအကျ ရှာဖွေပြီး ဖြေကြားချက်တွင် ချိတ်ဆက်ထားသော လင့်ခ်များနှင့် ကိုဒ်နမူနာများအဖြစ် ဖော်ပြပေးသည်။

သင့်မေးခွန်းကို ဖြေကြားရန် **@workspace** သည် VS Code တွင် developer တစ်ဦးက ကုဒ်ဘေ့စ်ကို ရှာဖွေသည့် အရင်းအမြစ်များကို ရှာဖွေသည် -

- .gitignore ဖိုင်ဖြင့် မပါဝင်သော ဖိုင်များကို ထည့်သွင်း၍ workspace အတွင်းရှိ ဖိုင်အားလုံး

- ဖိုလ်ဒါနှင့် ဖိုင်အမည်များပါသော ဖိုင်စနစ်ဖွဲ့စည်းမှု

- workspace သည် GitHub repository ဖြစ်ပြီး code search မှ index လုပ်ထားပါက GitHub code search index

- workspace အတွင်းရှိ သင်္ကေတများနှင့် သတ်မှတ်ချက်များ

- လက်ရှိရွေးချယ်ထားသော စာသား သို့မဟုတ် active editor တွင် မြင်သာသော စာသား

မှတ်ချက် - .gitignore ဖိုင်ဖြင့် မပါဝင်သော ဖိုင်တစ်ခုကို ဖွင့်ထား သို့မဟုတ် စာသားရွေးထားပါက .gitignore ကို ကျော်လွှားသွားမည်။

အောက်ပါလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုသည် [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **ဒီ Lab အကြောင်း ပိုမိုသိရှိရန်**

GitHub Copilot သည် စီးပွားရေးလုပ်ငန်းများ၏ ပရိုဂရမ်ရေးဆွဲမှု ထိရောက်မှုကို အလွန်တိုးတက်စေပြီး၊ စီးပွားရေးလုပ်ငန်းတိုင်းသည် GitHub Copilot ၏ သက်ဆိုင်ရာ လုပ်ဆောင်ချက်များကို ကိုယ်ပိုင်ပြင်ဆင်လိုသည်။ စီးပွားရေးလုပ်ငန်းများစွာသည် ကိုယ်ပိုင် စီးပွားရေးအခြေအနေများနှင့် open source မော်ဒယ်များအပေါ် အခြေခံ၍ GitHub Copilot နှင့် ဆင်တူသော Extensions များကို ကိုယ်တိုင်ပြင်ဆင်ထားကြသည်။ စီးပွားရေးလုပ်ငန်းများအတွက် ကိုယ်ပိုင်ပြင်ဆင်ထားသော Extensions များသည် ထိန်းချုပ်ရလွယ်ကူသော်လည်း အသုံးပြုသူအတွေ့အကြုံကို ထိခိုက်စေနိုင်သည်။ အကြောင်းမှာ GitHub Copilot သည် အထွေထွေ အခြေအနေများနှင့် ပရော်ဖက်ရှင်နယ်အဆင့်များကို ကိုင်တွယ်ရာတွင် ပိုမိုခိုင်မာသော လုပ်ဆောင်ချက်များ ရှိသည်။ အသုံးပြုသူအတွေ့အကြုံကို တူညီစေပြီး ကိုယ်ပိုင် Extension ကို ပြင်ဆင်နိုင်ပါက ပိုမိုကောင်းမွန်မည်ဖြစ်သည်။ GitHub Copilot Chat သည် စီးပွားရေးလုပ်ငန်းများအတွက် Chat အတွေ့အကြုံကို တိုးချဲ့နိုင်ရန် သက်ဆိုင်ရာ API များကို ပံ့ပိုးပေးသည်။ တူညီသော အတွေ့အကြုံကို ထိန်းသိမ်းထားခြင်းနှင့် ကိုယ်ပိုင်ပြင်ဆင်ထားသော လုပ်ဆောင်ချက်များ ရှိခြင်းသည် ပိုမိုကောင်းမွန်သော အသုံးပြုသူအတွေ့အကြုံ ဖြစ်သည်။

ဒီ lab သည် Phi-3 မော်ဒယ်ကို ဒေသခံ NPU နှင့် Azure ပေါင်းစပ်ပြီး GitHub Copilot Chat တွင် ကိုယ်ပိုင် Agent ***@PHI3*** တည်ဆောက်ကာ စီးပွားရေးလုပ်ငန်း developer များကို ကိုဒ်ဖန်တီးခြင်း***(@PHI3 /gen)*** နှင့် ပုံများအပေါ် အခြေခံ၍ ကိုဒ်ဖန်တီးခြင်း***(@PHI3 /img)*** တွင် အကူအညီပေးရန် ရည်ရွယ်သည်။

![PHI3](../../../../../../../imgs/02/vscodeext/cover.png)

### ***မှတ်ချက်:***

ဒီ lab ကို လက်ရှိ Intel CPU နှင့် Apple Silicon အတွက် AIPC တွင် အကောင်အထည်ဖော်ထားပြီး Qualcomm NPU ဗားရှင်းကို ဆက်လက် update လုပ်သွားမည်ဖြစ်သည်။

## **Lab**

| Name | ဖော်ပြချက် | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | သက်ဆိုင်ရာ ပတ်ဝန်းကျင်များနှင့် installation tools များကို ပြင်ဆင်တပ်ဆင်ခြင်း | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | AIPC / Apple Silicon နှင့် ပေါင်းစပ်၍ ဒေသခံ NPU ကို အသုံးပြုကာ Phi-3-mini ဖြင့် ကိုဒ်ဖန်တီးခြင်း | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Azure Machine Learning Service ၏ Model Catalog - Phi-3-vision image ကို တပ်ဆင်ကာ ကိုဒ်ဖန်တီးခြင်း | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | GitHub Copilot Chat တွင် ကိုယ်ပိုင် Phi-3 agent တစ်ခု ဖန်တီးကာ ကိုဒ်ဖန်တီးခြင်း၊ ဂရပ်ဖ်ဖန်တီးခြင်း၊ RAG စသည်ဖြင့် ပြီးမြောက်စေခြင်း | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | နမူနာကိုဒ် ဒေါင်းလုပ်လုပ်ရန် | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **အရင်းအမြစ်များ**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API အကြောင်း ပိုမိုသိရှိရန် [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry ၏ Model Catalog အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။