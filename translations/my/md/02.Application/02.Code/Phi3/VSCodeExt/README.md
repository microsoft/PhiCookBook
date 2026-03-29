# **Microsoft Phi-3 မိသားစုဖြင့် သင့်ကိုယ်ပိုင် Visual Studio Code GitHub Copilot Chat တည်ဆောက်ခြင်း**

GitHub Copilot Chat တွင် workspace agent ကို အသုံးပြုဖူးပါသလား? သင့်အဖွဲ့ရဲ့ ကိုယ်ပိုင် code agent တည်ဆောက်ချင်ပါသလား? ဒီလက်တွေ့လုပ်ငန်းခန်းသည် open source မော်ဒယ်ကို ပေါင်းစပ်ကာ တစ်ခုတည်းကုမ္ပဏီအဆင့် code စီးပွားရေး agent တည်ဆောက်ဖို့ ရည်ရွယ်ထားသည်။

## **အခြေခံ**

### **Microsoft Phi-3 ကို ဘာကြောင့်ရွေးချယ်သင့်သလဲ**

Phi-3 သည် မိသားစုစီးရီးဖြစ်ပြီး၊ စာသားထုတ်ပေးခြင်း၊ စကားပြောပြီးစီးခြင်းနှင့် ကုဒ်ထုတ်ပေးခြင်းအတွက် အမျိုးမျိုးသော လေ့ကျင့်မှု ပါရာမီတာအပေါ် အခြေခံ၍ phi-3-mini၊ phi-3-small နှင့် phi-3-medium တို့ပါဝင်သည်။ Vision အခြေပြု phi-3-vision ကိုလည်း တွဲဖက်ထားသည်။ ကုမ္ပဏီများ သို့မဟုတ် မတူညီသောအဖွဲ့များအတွက် အော့ဖ်လိုင်း ထုတ်လုပ်နိုင်သော AI ဖြေရှင်းချက်များ ဖန်တီးရန် သင့်လျော်သည်။

အောက်ပါလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုသည် [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat extension သည် သင့်အား GitHub Copilot နှင့်ဆက်သွယ်နိုင်သော စကားပြောမျက်နှာပြင်တစ်ခု ပေးသည်၊ VS Code အတွင်း မည်သည့်အချိန်မဆို ကုဒ်ရေးဆွဲခြင်းဆိုင်ရာမေးခွန်းများအား အဖြေများကို တိုက်ရိုက်ရယူနိုင်ပြီး၊ စာတမ်းရှာဖွေရန် သို့မဟုတ် အွန်လိုင်းဖိုရမ်များကို ရှာဖွေရန် မလိုအပ်ပါ။

Copilot Chat သည် syntax highlighting၊ indentation နှင့် အခြား format များကို အသုံးပြု၍ ထုတ်ပေးသော အဖြေများကို ပိုမိုရှင်းလင်းစေသည်။ အသုံးပြုသူ၏ မေးခွန်းအမျိုးအစားအပေါ် မူတည်ပြီး၊ Copilot သည် ဖြေကြားမှုအတွက် အသုံးပြုသော အကြောင်းအရာများသို့ လင့်ခ်များ (ဥပမာ - ကိုးဒ်ဖိုင်များ သို့မဟုတ် စာတမ်းများ) သို့မဟုတ် VS Code လုပ်ဆောင်ချက်များသို့ သွားရန် ခလုတ်များ ပါဝင်နိုင်သည်။

- Copilot Chat သည် သင့် developer လည်ပတ်မှုတွင်း ပေါင်းစည်းပြီး အကူအညီလိုအပ်သည့်နေရာတွင် ရရှိစေပါသည်။

- မိမိ ကုဒ်ရေးစဉ် တိုက်ရိုက် editor သို့ terminal မှ inline chat စတင်စကားဆိုနိုင်သည်

- Chat ရှုထောင့်ကို အသုံးပြု၍ မည်သည့်အချိန်မဆို AI အကူအညီရရှိစေသည်

- Quick Chat ကို စတင်၍ အမြန်မေးခွန်းမေးကာ သင့်လုပ်ဆောင်နေသည့်အလုပ်ထဲ ပြန်သွားနိုင်သည်

GitHub Copilot Chat ကို အမျိုးမျိုးသောအခြေအနေများတွင် အသုံးပြုနိုင်သည်၊ ဥပမာ-

- ပြဿနာကို ဖြေရှင်းရန် ကုဒ်ရေးဆွဲခြင်းဆိုင်ရာ မေးခွန်းများ ဖြေကြားခြင်း

- တခြားသူ၏ ကုဒ်ကို ရှင်းပြ၍ မြှင့်တင်မှုများ ဖော်ပြခြင်း

- ကုဒ်ပြုပြင်မှု အကြံပေးခြင်း

- Unit test case များ ထုတ်ပေးခြင်း

- ကုဒ်စာတမ်းများ ထုတ်ဖတ်ခြင်း

အောက်ပါလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုသည် [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat တွင် **@workspace** ကို ကိုးကားခြင်းက သင့်ကုဒ်အစုလိုက် အရေးကြီးသော မေးခွန်းများကို မေးနိုင်စေသည်။ မေးခွန်းအပေါ် အခြေခံပြီး Copilot သည် သင့်အတွက် သင့်လျော်သောဖိုင်များနှင့် သင်္ကေတများကို အလိမ်လည်ကောက်ယူကာ သူ၏အဖြေတွင် လင့်ခ်များ၊ ကုဒ်နမူနာအဖြစ် ကိုးကားပေးသည်။

မေးခွန်းကို ဖြေရှင်းရန် **@workspace** သည် VS Code တွင် developer တစ်ဦး ကုဒ်အစုလိုက်ကို ရွှေ့လျားစဉ် အသုံးပြုသည့်အတိုင်း မူရင်းရင်းမြစ်များကို ရှာဖွေသည် -

- .gitignore ဖိုင်ဖြင့်မပါသော workspace တြင် ရှိသည့် ဖိုင်အားလုံး

- ဖိုင်များနှင့်ဖိုလ်ဒါများ ပါဝင်သည့် ဖိုင်လမ်းကြောင်းဖွဲ့စည်းပုံ

- GitHub မှ code search index ကိုယုံကြည်၍ workspace သည် GitHub repository ဖြစ်ပြီး code search ဖြင့် အညွှန်းပြုထားသည်

- workspace တြင် ရှိသည့် သင်္ကေတများနှင့် သတ်မှတ်ချက်များ

- လက်ရှိရွေးချယ်ထားသည့် စာသား သို့မဟုတ် လက်ရှိ editor တွင် မြင်သာသော စာသား

မှတ်ချက် - သင်္ကေတလုံးဝမပါသော ဖိုင်ကို ဖွင့်ထားပါက သို့မဟုတ် ဖြတ်ကြားသူဖြစ်သော ဖိုင်တွင် စာသားရွေးရှိပါက .gitignore ကို ကျော်လွှားမည်ဖြစ်သည်။

အောက်ပါလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုသည် [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **ဒီ Lab အကြောင်း ပိုမိုသိရှိရန်**

GitHub Copilot သည် ကုမ္ပဏီများ၏ ပရိုဂရမ်ရေးဆွဲမှု ထိရောက်မှုကိုအလွန်တိုးတက်စေပြီး၊ ကုမ္ပဏီတိုင်းသည် GitHub Copilot ၏ သင့်တော်သောလုပ်ဆောင်ချက်များကို ကိုယ်ပိုင်သတ်မှတ်ချင်ကြသည်။ ကုမ္ပဏီများအများအပြားသည် ကိုယ်ပိုင် စီးပွားရေးအခြေအနေများ နှင့် open source မော်ဒယ်အပေါ် အခြေခံ၍ GitHub Copilot မျိုးဆက်သော Extensions များကို ကိုယ်တိုင်ပြင်ဆင်ထားကြသည်။ ကုမ္ပဏီများအတွက် customized Extension များမှာ ထိန်းချုပ်ရလွယ်ကူပြီး မူလ GitHub Copilot ထက် အသုံးပြုသူအတွေ့အကြုံပြောင်းလဲမှုကို ဖယ်ရှားနိုင်ပါသည်။ အချို့သော စီးပွားရေးဆိုင်ရာ အသုံးချမှုနှင့် နိုင်ငံတကာအဆင့်ရှိသော GitHub Copilot ၏ လုပ်ဆောင်ချက်များ ပိုမိုခိုင်မာသောကြောင့်၊ အတွေ့အကြုံတူညီမှုကို ထိန်းသိမ်းထားနိုင်ပါက ကိုယ်ပိုင် customized Extension ပြုလုပ်ခြင်းက အကောင်းဆုံးဖြစ်ပါသည်။ GitHub Copilot Chat မှ စကားဝိုင်းအတွေ့အကြုံ တိုးချဲ့ရန် သက်ဆိုင်ရာ API များကို ကုမ္ပဏီများ အသုံးပြုနိုင်အောင် ပံ့ပိုးပေးသည်။ အတွေ့အကြုံတူညီမှုရှိခြင်းနှင့် customized လုပ်ဆောင်ချက်များ ရရှိခြင်းသည် ပိုမိုကောင်းမွန်သော အသုံးပြုသူအတွေ့အကြုံ ဖြစ်သည်။

ဒီ lab သည် အဓိကအားဖြင့် Phi-3 မော်ဒယ်ကို ဒေသခံ NPU နှင့် Azure အနှံ့ ပေါင်းစပ် အသုံးပြုကာ GitHub Copilot Chat တွင် ကိုယ်ပိုင် Agent ***@PHI3*** တည်ဆောက်ကာ ကုမ္ပဏီ developer များအား ကုဒ်ထုတ်ပေးခြင်း ***(@PHI3 /gen)*** နှင့်ပုံများအပေါ် အခြေခံကာ ကုဒ်ထုတ်ပေးခြင်း ***(@PHI3 /img)*** အကူအညီ ပေးရန် ဖြစ်သည်။

![PHI3](../../../../../../../translated_images/my/cover.1017ebc9a7c46d09.webp)

### ***မှတ်ချက်:*** 

လက်ရှိတွင် ဒီ lab ကို Intel CPU နှင့် Apple Silicon အတွက် AIPC တွင် အသုံးပြုထားပြီး Qualcomm NPU ဗားရှင်းကို ဆက်လက် update လုပ်သွားမည်ဖြစ်သည်။


## **Lab**

| Name | Description | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | ဆက်စပ်ပတ်ဝန်းကျင်များနှင့် 설치 도구များ ကို ပြင်ဆင်တပ်ဆင်ခြင်း | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | AIPC / Apple Silicon နှင့်ပေါင်းစပ်ကာ ဒေသခံ NPU သုံး၍ Phi-3-mini ဖြင့် ကုဒ်ထုတ်ခြင်း | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Azure Machine Learning Service ၏ Model Catalog တွင် Phi-3-vision image တင်ပြီး ကုဒ်ထုတ်ခြင်း | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | GitHub Copilot Chat တွင် ကိုယ်ပိုင် Phi-3 agent တည်ဆောက်ကာ ကုဒ်ထုတ်ခြင်း၊ ဂရပ်ဖစ်ကုဒ်ထုတ်ခြင်း၊ RAG စသဖြင့် ပြုလုပ်ခြင်း | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | နမူနာကုဒ် ဒေါင်းလုပ်လုပ်ရန် | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **အရင်းအမြစ်များ**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API အကြောင်း ပိုမိုသိရှိရန် [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry ၏ Model Catalog အကြောင်း ပိုမိုသိရှိရန် [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အပြောကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်မှုဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြုပြီး ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းပါသောကြောင့်၊ အလိုအလျောက်ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် တိကျမှုနည်းပါးမှုများ ဖြစ်ပေါ်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပညာရှင်လူသားများဘက်မှ ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အနားလွတ်မှုများ သို့မဟုတ် နားလွတ်ချက်များအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->