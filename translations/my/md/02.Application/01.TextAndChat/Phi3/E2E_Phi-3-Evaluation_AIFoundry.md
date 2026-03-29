# Microsoft Foundry တွင် Phi-3 / Phi-3.5 ကို ပြန်လည်သင့်တင်ထားသော မော်ဒယ်ကို Microsoft ၏ တာဝန်ရှိ AI နည်းစနစ်များအပေါ် အခြေခံ၍ အကဲဖြတ်ခြင်း

ဒီ end-to-end (E2E) နမူနာသည် Microsoft Tech Community မှ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" လမ်းညွှန်ချက်အပေါ် အခြေခံထားသည်။

## မျက်နှာချင်းဆိုင်

### Microsoft Foundry တွင် ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်၏ လုံခြုံမှုနှင့် တိုးတက်မှုကို မည်သို့ အကဲဖြတ်နိုင်မလဲ?

မော်ဒယ်တစ်ခုကို fine-tune လုပ်ခြင်းဖြင့် တခါတရံ မမျှော်လင့်ထားသော သို့မဟုတ် မလိုလားအပ်သော ပြန်လည်တုံ့ပြန်မှုများ ဖြစ်ပေါ်နိုင်သည်။ မော်ဒယ်သည် လုံခြုံပြီး အကျိုးရှိရှိနေဖို့၊ ဒါမှမဟုတ် အကျိုးဆက် မကောင်းသော အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုနှင့် တိကျမှု၊ သက်ဆိုင်မှုနှင့် ညီညွတ်သော ပြန်လည်တုံ့ပြန်မှုများ ထုတ်ပေးနိုင်မှုကို အကဲဖြတ်ခြင်းအရေးပါသည်။ ဤ လေ့လာမှုတွင် Microsoft Foundry မှာ Prompt flow ဖြင့် ပေါင်းစည်းထားသော ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်၏ လုံခြုံမှုနှင့် တိုးတက်မှုကို မည်သို့ အကဲဖြတ်ရမည်ကို သင်သိရှိမည်။

ဤမှာ Microsoft Foundry ၏ အကဲဖြတ်ခြင်း လုပ်ငန်းစဉ် ဖြစ်သည်။

![Architecture of tutorial.](../../../../../../translated_images/my/architecture.10bec55250f5d6a4.webp)

*ပုံရင်းမြစ်: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 နှင့် ပတ်သက်၍ ပိုမိုအသေးစိတ်သိရှိရန်နှင့် အရင်းအမြစ်များကို ရှာဖွေရန်၊ [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) ကို သွားရောက်ကြည့်ရှုပါ။

### လိုအပ်ချက်များ

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်

### မူလ အကြောင်းအရာ အကြောင်းအရာစာရင်း

1. [**အမှုလက်ခံ ၁: Microsoft Foundry ၏ Prompt flow အကဲဖြတ်မှု အတွင်းအကြောင်း**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [လုံခြုံမှု အကဲဖြတ်မှု အတွင်းအကြောင်း](#လုံခြုံမှု-အကဲဖြတ်မှု-အတွင်းအကြောင်း)
    - [တိုးတက်မှု အကဲဖြတ်မှု အတွင်းအကြောင်း](#တိုးတက်မှု-အကဲဖြတ်မှု-အတွင်းအကြောင်း)

1. [**အမှုလက်ခံ ၂: Microsoft Foundry တွင် Phi-3 / Phi-3.5 မော်ဒယ် အကဲဖြတ်ခြင်း**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [စတင်ရန် မပြုမီ](#စတင်ရန်-မပြုမီ)
    - [Phi-3 / Phi-3.5 မော်ဒယ် အကဲဖြတ်ရန် Azure OpenAI ကို ပြောင်းလဲတပ်ဆင်ခြင်း](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry ၏ Prompt flow အကဲဖြတ်မှု ဖြင့် ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်ကို အကဲဖြတ်ခြင်း](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [ဂုဏ်ပြုပါတယ်!](#ဂုဏ်ယူပါသည်)

## **အမှုလက်ခံ ၁: Microsoft Foundry ၏ Prompt flow အကဲဖြတ်မှု အတွင်းအကြောင်း**

### လုံခြုံမှု အကဲဖြတ်မှု အတွင်းအကြောင်း

သင့် AI မော်ဒယ်သည် ကျင့်သုံးမှု အညီနှင့် လုံခြုံမှုရှိစေရန်၊ Microsoft ၏ တာဝန်ရှိ AI နည်းစနစ်များ နှင့် ကိုက်ညီမှုရှိစေရန် အရေးကြီးသည်။ Microsoft Foundry တွင် လုံခြုံမှုအကဲဖြတ်မှုက မော်ဒယ်၏ jailbreak တိုက်ခိုက်မှုများမှ ကာကွယ်နိုင်မှုနှင့် အနုတ်လက္ခဏာ အကြောင်းအရာထုတ်ပေးနိုင်မှုကို စမ်းသပ်ရန် ခွင့်ပြုသည်။ ဒီကိစ္စမှာ တိုက်ဆိုင်မှုရှိနေသည်။

![Safaty evaluation.](../../../../../../translated_images/my/safety-evaluation.083586ec88dfa950.webp)

*ပုံရင်းမြစ်: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft ၏ တာဝန်ရှိ AI နည်းစနစ်များ

နည်းပညာဆိုင်ရာခြေလှမ်းစတင်လုပ်ဆောင်မည့် အမူအရာများမတိုင်မီ Microsoft ၏ တာဝန်ရှိ AI နည်းစနစ်များကို နားလည်ထားခြင်း အရေးကြီးသည်။ ဤသဘောတရားများသည် AI စနစ်များကို တာဝန်ရှိစွာ ဒီဇိုင်းရေးဆွဲ၊ ဖန်တီးနှင့် တပ်ဆင်ရာတွင် လမ်းပြသည်။ AI နည်းပညာများကို တရားမျှတ၊ ပွင့်လင်း နှင့် အပါဝင်မှုရှိစေရန် ဒီသဘောတရားများကို အခြေခံသည်။ AI မော်ဒယ်များ လုံခြုံမှုအတွက် အခြေခံ အတွေးအခေါ်ဖြစ်သည်။

Microsoft ၏ တာဝန်ရှိ AI နည်းစနစ်များမှာ -

- **တရားမျှတမှုနှင့် အပါဝင်မှု**: AI စနစ်များသည် လူတိုင်းကို တရားမျှတစွာ ဆက်ဆံရန်၊ လူအုပ်စုတူညီသောအခြေအနေများရှိသူများကို ကွဲပြားစွာ ထိခိုက်မှု မဖြစ်စေရန် ဖြစ်ရမည်။ ဥပမာ၊ AI systems မှ ဆေးကုသမှု လမ်းညွှန်မှု၊ ချေးငွေ လျှောက်ထားမှု သို့မဟုတ် အလုပ်ရွေးချယ်ခြင်းများတွင် တူညီသော ရောဂါလက္ခဏာ၊ ဘဏ္ဍာရေးအခြေအနေ သို့မဟုတ် လုပ်ငန်းအရည်အချင်းရှိသူအားလုံး၌ တူညီသော အကြံပြုချက်ပေးရမည်။

- **ယုံကြည်စိတ်ချရမှုနှင့် လုံခြုံမှု**: ယုံကြည်စိတ်ချနိုင်စေရန် AI systems များသည် ယုံကြည်စိတ်ချရ၊ လုံခြုံပြီး တည်ငြိမ်စွာ လည်ပတ်နိုင်ရန် အရေးကြီးသည်။ ဤစနစ်များသည် စတင်ဒီဇိုင်းရေးဆွဲထားသည့်အတိုင်း လည်ပတ်နိုင်ပြီး မမျှော်လင့်ထားသော အခြေအနေများတွင်လည်း လုံခြုံစွာ မျှော်မှန်းထားသည်။ ထုတ်လုပ်သူတို့ဒီဇိုင်းနှင့် စမ်းသပ်မှုတွင် မျှော်လင့်ထားသည့် အတွေ့အကြုံများအတိုင်း လုပ်ဆောင်နိုင်သည်။

- **ပွင့်လင်းမြင်သာမှု**: လူများ၏ ဘဝများအပေါ် ထိခိုက်မှု အရှိန်အဟုန်မြင့်သော ဆုံးဖြတ်ချက်များတွင် AI systems ကူညီမှုပေးသောအခါ၊ လူများသည် ဆုံးဖြတ်ချက်များ ပြုလုပ်ပုံကို နားလည်ရမည်။ ဥပမာ ဘဏ်တစ်ခုသည် လူတစ်ဦး၏ ခရက်ဒစ်ရည်မှတ်ချက်ကို ဆုံးဖြတ်ရန် AI system ကို အသုံးပြုသည်။ ကုမ္ပဏီတစ်ခုသည် အလုပ်ခန့်ရန် အရည်အချင်းအကောင်းဆုံးလူများကို ရွေးချယ်ရန် AI system ကို အသုံးပြုသည်။

- **ကိုယ်ရေးအချက်အလက်နှင့် လုံခြုံရေး**: AI နည်းပညာများ ပိုမိုမြင့်မားလာသလို ကိုယ်ရေးအချက်အလက်ကို ထိန်းသိမ်းရေးနှင့် စီးပွားရေးဆိုင်ရာ အချက်အလက်များ လုံခြုံစေရန် ပိုမိုအရေးကြီးပြီး ရှုပ်ထွေးလာသည်။ AI တွင်အချက်အလက် ကိုရောက်ရှိနိုင်မှုသည် မှန်ကန်သည့် ခန့်မှန်းချက်များကို ပြုလုပ်ရန် အရေးကြီးသောကြောင့် ကိုယ်ရေးဒေတာနှင့် လုံခြုံရေးကို အထူးဂရုစိုက်ရမည်။

- **တာဝန်ယူမှု**: AI မော်ဒယ်များကို ဒီဇိုင်းဆွဲပြီး တပ်ဆင်သူများမှာ မိမိတို့ စနစ်များ လည်ပတ်မှုအပေါ် တာဝန်ယူရမည်။ အဖွဲ့အစည်းများသည် စက်မှုလုပ်ငန်းစံချိန်များကို အခြေခံ၍ တာဝန်ယူမှု ရိုးရာများ ဖန်တီးသင့်သည်။ ဤရိုးရာများက AI စနစ်များသည် လူသက်ဆိုင်မှုရှိသော ဆုံးဖြတ်ချက်များ အတွက် နောက်ဆုံးအာဏာမဟုတ်ကြောင်း သေချာစေမည်။ အဲဒီလို မဟုတ်ဘဲ လူများသည် အခြားမော်ဒယ်များထက် ပိုပြီး ကိုင်တွယ် ထိန်းချုပ်နိုင်စေရန်လည်း အာမခံပေးမည်။

![Fill hub.](../../../../../../translated_images/my/responsibleai2.c07ef430113fad8c.webp)

*ပုံရင်းမြစ်: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft ၏ တာဝန်ရှိ AI နည်းစနစ်များနှင့် ပိုမိုသိရှိလိုပါက [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) ကို ဖတ်ရှုပါ။

#### လုံခြုံမှု မီတား

ဤလေ့လာမှုတွင် Microsoft Foundry ၏ လုံခြုံမှု မီတားများဖြင့် ပြန်လည်သင့်တင်ထားသော Phi-3 မော်ဒယ်၏ လုံခြုံမှုကို အကဲဖြတ်မည်။ ဤ မီတားများက မော်ဒယ်၏ အနုတ်လက္ခဏာများထုတ်ပေးနိုင်မှုနှင့် jailbreak တိုက်ခိုက်မှုအပေါ် ခံနိုင်ရည်ကို ချိန်မျှတရန် အထောက်အကူဖြစ်သည်။ လုံခြုံမှု မီတားများမှာ -

- **ကိုယ့်ကိုယ်ကို ထိခိုက်မှု အကြောင်းအရာ**: မော်ဒယ်သည် ကိုယ့်ကိုယ်ကို ထိခိုက်သည့် အကြောင်းအရာ ထုတ်ပေးရန် ယေဘုယျစိတ်ထား ရှိမရှိ အကဲဖြတ်သည်။
- **ဒုက္ခတရားနှင့် မတရားသောအကြောင်းအရာ**: မော်ဒယ်သည် ရာဇဝတ်မှုရှိသော သို့မဟုတ် မတရားသော အကြောင်းအရာများ ထုတ်ပေးရန် စိတ်ထား ရှိမရှိ အကဲဖြတ်သည်။
- **အကြမ်းဖက်မှု အကြောင်းအရာ**: မော်ဒယ်သည် အကြမ်းဖက်မှုမှ အကြောင်းအရာများ ထုတ်ပေးရန် စိတ်ထား ရှိမရှိ အကဲဖြတ်သည်။
- **လိင်ဆက်နွယ်သော အကြောင်းအရာ**: မော်ဒယ်သည် မသင့်တင့်သော လိင်ဆက်နွယ်ရေး အကြောင်းအရာ ထုတ်ပေးရန် စိတ်ထား ရှိမရှိ အကဲဖြတ်သည်။

ဤအချက်များကို အကဲဖြတ်ခြင်းဖြင့် AI မော်ဒယ်သည် မတရား၊ ထိခိုက်မှုရှိသော အကြောင်းအရာ မထုတ်ပေးပါက အနည်းငယ်မှန်ကန်မှုနှင့် စည်းမျဉ်းစည်းကြပ်ဖြင့် ကိုက်ညီကြောင်း သေချာသည်။

![Evaluate based on safety.](../../../../../../translated_images/my/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### တိုးတက်မှု အကဲဖြတ်မှု အတွင်းအကြောင်း

သင့် AI မော်ဒယ်သည် မျှော်လင့်သလို လည်ပတ်နေမနေ စစ်ဆေးရန်၊ တိုးတက်မှု မီတားများအားဖြင့် အကဲဖြတ်ရမည်။ Microsoft Foundry တွင် တိုးတက်မှုအကဲဖြတ်မှုက မော်ဒယ်၏ တိကျပြီး သက်ဆိုင်မှုရှိသော၊ ညီညွတ်သော ပြန်လည်တုံ့ပြန်မှုများ ထုတ်ပေးနိုင်မှုကို စမ်းသပ်နိုင်စေသည်။

![Safaty evaluation.](../../../../../../translated_images/my/performance-evaluation.48b3e7e01a098740.webp)

*ပုံရင်းမြစ်: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### တိုးတက်မှု မီတားများ

ဤ လေ့လာမှုတွင် Microsoft Foundry ၏ တိုးတက်မှု မီတားများ အသုံးပြု၍ ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်၏ တိုးတက်မှုကို အကဲဖြတ်မည်။ ဤ မီတားများက မော်ဒယ်၏ တိကျချောမွေ့ပြီး သက်ဆိုင်မှုရှိသော၊ ညီညွတ်သော ပြန်လည်တုံ့ပြန်မှုများ ထုတ်ပေးနိုင်မှုကို စစ်ဆေးရန် အထောက်အကူပြုသည်။ တိုးတက်မှု မီတားများမှာ -

- **အခြေခံမှန်ကန်မှု**: ထုတ်ပေးသော အဖြေများကို အချက်အလက်ရင်းမြစ်နှင့် လိုက်လျောညီထွေ ဖြစ်မှုကို အကဲဖြတ်သည်။
- **သက်ဆိုင်မှု**: ထုတ်ပေးသော ပြန်လည်တုံ့ပြန်မှုများသည် မေးခွန်းများနှင့် မည်သို့ သက်ဆိုင်မှုရှိသနည်း အကဲဖြတ်သည်။
- **ညီညွတ်မှု**: ထုတ်ပေးသော စာသား၏ ပြောင်းလွယ်ပြင်လွယ်မှု၊ သဘာဝကျလေ့နှင့် လူတူဘာသာစကား သဘောတူညီမှုကို အကဲဖြတ်သည်။
- **ဘာသာစကားကျွမ်းကျင်မှု**: ထုတ်ပေးသော စာသား၏ ဘာသာစကားကျွမ်းကျင်မှုကို အကဲဖြတ်သည်။
- **GPT နှင့် ဆင်တူမှု**: ထုတ်ပေးသော ပြန်လည်တုံ့ပြန်မှုနှင့် နာမည်မှန် ပုံစံကို နှိုင်းယှဉ်သည်။
- **F1 ဖြစ်နိုင်မှုသင်္ကေတ**: ထုတ်ပေးသော ပြန်လည်တုံ့ပြန်မှုနှင့် ရင်းမြစ်ဒေတာရှိ စကားလုံးများ၏ အတူတူ ဖြစ်နိုင်မှု အချိုးကို တွက်ချက်သည်။

ဤ မီတားများက မော်ဒယ်၏ တိကျမှန်ကန် သက်ဆိုင်မှုရှိသော နှင့် ညီညွတ်သော ပြန်လည်တုံ့ပြန်မှုများ ထုတ်ပေးနိုင်မှုကို အကဲဖြတ်ရာတွင် အထောက်အကူဖြစ်သည်။

![Evaluate based on performance.](../../../../../../translated_images/my/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **အမှုလက်ခံ ၂: Microsoft Foundry တွင် Phi-3 / Phi-3.5 မော်ဒယ် အကဲဖြတ်ခြင်း**

### စတင်ရန် မပြုမီ

ဤလေ့လာမှုသည် ယခင် ဘလော့ဂ် ဆောင်းပါးများ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" နှင့် "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" တို့၏ ဆက်လက်ဖြစ်သည်။ ဤဆောင်းပါးများတွင် Microsoft Foundry တွင် Phi-3 / Phi-3.5 မော်ဒယ်တစ်ခု ကို fine-tune ပြုလုပ်ခြင်းနှင့် Prompt flow ဖြင့် ပေါင်းစည်းခြင်း လုပ်ငန်းစဉ်များကို လမ်းညွှန်ခဲ့သည်။

ဤ လေ့လာမှုတွင် Azure OpenAI မော်ဒယ်တစ်ခုကို Microsoft Foundry တွင် အကဲဖြတ်သူအဖြစ် တပ်ဆင်ပြီး ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်ကို အကဲဖြတ်ရန် အသုံးပြုမည်ဖြစ်သည်။

ဤ လေ့လာမှုကို စတင်မည့်အောက်တွင် အောက်ပါ လိုအပ်ချက်များရှိကြောင်း ယခင်သင်ခန်းစာများအတိုင်း သေချာစေရန်ပြုလုပ်ပါ။

1. ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်အတွက် အကဲဖြတ်ရန် အသင့်ပြင်ထားသော ဒေတာစုစည်းမှု။
1. Phi-3 / Phi-3.5 မော်ဒယ်တစ်ခု ဖြစ်ပြီး Azure Machine Learning တွင် တပ်ဆင်ပြီး။
1. Microsoft Foundry တွင် ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်နှင့် ပေါင်းစည်းထားသည့် Prompt flow။

> [!NOTE]
> ယခင် ဘလော့ဂ် ဆောင်းပါးများတွင် ဒေါင်းလုပ်လုပ်ထားသော **ULTRACHAT_200k** ဒေတာစု၏ *test_data.jsonl* ဖိုင်ကို ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်အတွက် အကဲဖြတ်မည့် ဒေတာအဖြစ် အသုံးပြုမည်။

#### Microsoft Foundry တွင် Prompt flow နှင့် ကိုယ့်စိတ်ကြိုက် Phi-3 / Phi-3.5 မော်ဒယ် ပေါင်းစည်းခြင်း (Code first နည်းလမ်း)

> [!NOTE]
> "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" တွင် ဖော်ပြထားသည့် low-code နည်းလမ်းကို လိုက်နာပြီးဖြစ်ပါက ဤလေ့ကျင့်ခန်းကို ကျော်လွှားပြီး နောက်တစ်ခုဆက်လုပ်နိုင်သည်။
> သို့သော် "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" တွင် ဖော်ပြထားသည့် code-first နည်းလမ်းဖြင့် Phi-3 / Phi-3.5 မော်ဒယ်ကို fine-tune ပြုလုပ်၍ တပ်ဆင်ထားလျှင် Prompt flow နှင့် ချိတ်ဆက်ခြင်း လုပ်ငန်းစဉ်က တခြားနည်းဖြစ်သည်။ ဤလေ့ကျင့်ခန်းတွင် အဆိုပါ လုပ်ငန်းစဉ် ကိုသင်ယူမည်ဖြစ်သည်။

ဆက်လုပ်ရန်၊ ပြန်လည်သင့်တင်ထားသော Phi-3 / Phi-3.5 မော်ဒယ်ကို Microsoft Foundry တွင် Prompt flow နှင့် ပေါင်းစည်းရန် လိုအပ်သည်။

#### Microsoft Foundry Hub ဖန်တီးခြင်း

Project တည်ဆောက်ရန်မတိုင်မီ Hub တစ်ခု ဖန်တီးရန် လိုအပ်သည်။ Hub သည် Resource Group အနေနှင့် လုပ်ဆောင်ကာ Microsoft Foundry တွင် Projects များစွာကို စီမံခန့်ခွဲနိုင်စေရန် ကူညီပေးသည်။
1. Sign in [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)။

1. ဘယ်ဘက်ဘားမှ **All hubs** ကို ရွေးချယ်ပါ။

1. နေရာသွားပြကွက်မှ **+ New hub** ကို ရွေးချယ်ပါ။

    ![Create hub.](../../../../../../translated_images/my/create-hub.5be78fb1e21ffbf1.webp)

1. အောက်ပါအလုပ်များကို အဆင့်လိုက် လုပ်ဆောင်ပါ -

    - **Hub name** ထည့်ပါ။ ထူးခြားသော တန်ဖိုးဖြစ်ရပါမည်။
    - သင့် Azure **Subscription** ကို ရွေးချယ်ပါ။
    - သုံးမယ့် **Resource group** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ် ဖန်တီးပါ)။
    - သုံးမယ့် **Location** ကို ရွေးချယ်ပါ။
    - သုံးမယ့် **Connect Azure AI Services** ကို ရွေးချယ်ပါ (လိုအပ်ပါက အသစ် ဖန်တီးပါ)။
    - **Connect Azure AI Search** တွင် **Skip connecting** ကို ရွေးချယ်ပါ။

    ![Fill hub.](../../../../../../translated_images/my/fill-hub.baaa108495c71e34.webp)

1. **Next** ကို ရွေးချယ်ပါ။

#### Microsoft Foundry Project ဖန်တီးခြင်း

1. ဖန်တီးထားသော Hub တွင် ဘယ်ဘက်ဘားမှ **All projects** ကို ရွေးချယ်ပါ။

1. နေရာသွားပြကွက်မှ **+ New project** ကို ရွေးချယ်ပါ။

    ![Select new project.](../../../../../../translated_images/my/select-new-project.cd31c0404088d7a3.webp)

1. **Project name** ထည့်ပါ။ ထူးခြားသော တန်ဖိုးဖြစ်ရပါမည်။

    ![Create project.](../../../../../../translated_images/my/create-project.ca3b71298b90e420.webp)

1. **Create a project** ကို ရွေးချယ်ပါ။

#### Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်အတွက် custom connection ထည့်သွင်းခြင်း

သင့်ရဲ့ custom Phi-3 / Phi-3.5 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစည်းရန်အတွက် မော်ဒယ်ရဲ့ endpoint နဲ့ key ကို custom connection တစ်ခုအဖြစ် စာရင်းသွင်းထားရန် လိုအပ်သည်။ ဒီလုပ်ဆောင်မှုက Prompt flow မှာ သင့်ရဲ့ custom Phi-3 / Phi-3.5 မော်ဒယ်ကို အသုံးပြုနိုင်စေပါသည်။

#### Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်အတွက် api key နဲ့ endpoint uri ချိန်ညှိခြင်း

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သွားရောက်ပါ။

1. မိမိဖန်တီးထားသော Azure Machine learning workspace သို့ သွားပါ။

1. ဘယ်ဘက်ဘားမှ **Endpoints** ကို ရွေးချယ်ပါ။

    ![Select endpoints.](../../../../../../translated_images/my/select-endpoints.ee7387ecd68bd18d.webp)

1. ဖန်တီးထားသော endpoint ကို ရွေးချယ်ပါ။

    ![Select endpoints.](../../../../../../translated_images/my/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. နေရာသွားပြကွက်မှ **Consume** ကို ရွေးချယ်ပါ။

1. သင့်ရဲ့ **REST endpoint** နဲ့ **Primary key** ကို ကူးယူပါ။

    ![Copy api key and endpoint uri.](../../../../../../translated_images/my/copy-endpoint-key.0650c3786bd646ab.webp)

#### Custom Connection ထည့်သွင်းခြင်း

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) သွားရောက်ပါ။

1. မိမိဖန်တီးထားသော Microsoft Foundry project သို့ သွားပါ။

1. ဖန်တီးထားသော Project တွင် ဘယ်ဘက်ဘားမှ **Settings** ကို ရွေးချယ်ပါ။

1. **+ New connection** ကို ရွေးချယ်ပါ။

    ![Select new connection.](../../../../../../translated_images/my/select-new-connection.fa0f35743758a74b.webp)

1. နေရာသွားပြကွက်မှ **Custom keys** ကို ရွေးချယ်ပါ။

    ![Select custom keys.](../../../../../../translated_images/my/select-custom-keys.5a3c6b25580a9b67.webp)

1. အောက်ပါအလုပ်များကို လုပ်ဆောင်ပါ -

    - **+ Add key value pairs** ကို ရွေးချယ်ပါ။
    - key name အတွက် **endpoint** ထည့်ပြီး Azure ML Studio မှ ကူးယူထားသော endpoint ကို value အဖြစ် ထည့်ပါ။
    - ထပ်မံ၍ **+ Add key value pairs** ကို ရွေးချယ်ပါ။
    - key name အတွက် **key** ထည့်ပြီး Azure ML Studio မှ ကူးယူထားသော key ကို value အဖြစ် ထည့်ပါ။
    - key တွေအပြီးမှာ **is secret** ကို ရွေးချယ်ပါ။ key မူလတန်ဖိုး ပြပွါးခြင်းကို ကာကွယ်ရန်ဖြစ်သည်။

    ![Add connection.](../../../../../../translated_images/my/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** ကို ရွေးချယ်ပါ။

#### Prompt flow ဖန်တီးခြင်း

Microsoft Foundry မှာ custom connection တစ်ခု ထည့်သွင်းပြီးပါပြီ။ ယခု အောက်ပါအဆင့်များဖြင့် Prompt flow တစ်ခု ဖန်တီးပါ။ ပြီးရင် ဒီ Prompt flow ကို custom connection နဲ့ ချိတ်ဆက်ပြီး fine-tuned မော်ဒယ်ကို Prompt flow မှာ အသုံးပြုပါမည်။

1. မိမိဖန်တီးထားသော Microsoft Foundry project သို့ သွားပါ။

1. ဘယ်ဘက်ဘားမှ **Prompt flow** ကို ရွေးချယ်ပါ။

1. နေရာသွားပြကွက်မှ **+ Create** ကို ရွေးချယ်ပါ။

    ![Select Promptflow.](../../../../../../translated_images/my/select-promptflow.18ff2e61ab9173eb.webp)

1. နေရာသွားပြကွက်မှ **Chat flow** ကို ရွေးချယ်ပါ။

    ![Select chat flow.](../../../../../../translated_images/my/select-flow-type.28375125ec9996d3.webp)

1. အသုံးပြုမယ့် **Folder name** ထည့်ပါ။

    ![Select chat flow.](../../../../../../translated_images/my/enter-name.02ddf8fb840ad430.webp)

1. **Create** ကို ရွေးချယ်ပါ။

#### Prompt flow ကို သင့် custom Phi-3 / Phi-3.5 မော်ဒယ်နဲ့ ဆက်သွယ်ရန် ချိန်ညှိခြင်း

fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို Prompt flow ထဲတွင် ပေါင်းစည်းရန် လိုအပ်ပါသည်။ သို့သော် အဆိုပါရှိပြီးသား Prompt flow သည် ဒီလိုအတွက် မလုပ်ဆောင်နိုင်ပါ။ ထို့ကြောင့် Prompt flow ကို အသစ်ပြန်ဒီဇိုင်းဆွဲရမည်။

1. Prompt flow အတွင်း အောက်ပါအချက်များ လုပ်ဆောင်ပြီး ရှိပြီးသား flow ကို ပြန်တည်ဆောက်ပါ -

    - **Raw file mode** ကို ရွေးချယ်ပါ။
    - *flow.dag.yml* ဖိုင်ရှိ စာသားတိုင်းကို ဖျက်ပစ်ပါ။
    - အောက်ပါကုဒ်အား *flow.dag.yml* ထဲ ထည့်ပါ။

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** ကို ရွေးချယ်ပါ။

    ![Select raw file mode.](../../../../../../translated_images/my/select-raw-file-mode.06c1eca581ce4f53.webp)

1. *integrate_with_promptflow.py* ဖိုင်ထဲသို့ အောက်ပါကုဒ်များ ထည့်သွင်းပြီး Prompt flow တွင် custom Phi-3 / Phi-3.5 မော်ဒယ်ကို အသုံးပြုနိုင်ပါမည်။

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # မှတ်တမ်းတင်ခြင်းဆက်တင်
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" သည် Custom Connection ၏ နာမည်ဖြစ်ပြီး၊ "endpoint", "key" သည် Custom Connection ၏ key များဖြစ်သည်
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # ပြည့်စုံသော JSON ဖြေကြောင်းကို မှတ်တမ်းတင်ပါ
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/my/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry တွင် Prompt flow ကို အသုံးပြုခြင်းနှင့် ပတ်သက်သော အသေးစိတ် အချက်အလက်များအတွက် [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ကို ကြည့်ရှုနိုင်ပါသည်။

1. **Chat input**, **Chat output** ကို ရွေးချယ်၍ မော်ဒယ်နှင့် သွားလာဆက်သွယ်မှု ခွင့်ပြုပါ။

    ![Select Input Output.](../../../../../../translated_images/my/select-input-output.c187fc58f25fbfc3.webp)

1. ယခု သင့် custom Phi-3 / Phi-3.5 မော်ဒယ်နှင့် ဆက်သွယ်ရန် အသင့်ဖြစ်ပြီ။ နောက်ထပ်လေ့ကျင့်ခန်းတွင် Prompt flow ကို စတင်အသုံးပြုနည်းနဲ့ fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်နှင့် ဆက်သွယ်ရန် သင်ယူမှာ ဖြစ်သည်။

> [!NOTE]
>
> ပြန်တည်ဆောက်ထားသော flow သည် အောက်ပါပုံကဲ့သို့ ဖြစ်ရမည် -
>
> ![Flow example](../../../../../../translated_images/my/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow ကို စတင်ခြင်း

1. **Start compute sessions** ကို ရွေးချယ်၍ Prompt flow ကို စတင်ပါ။

    ![Start compute session.](../../../../../../translated_images/my/start-compute-session.9acd8cbbd2c43df1.webp)

1. **Validate and parse input** ကို ရွေးချယ်၍ parameter များကို ပြန်လည်အသစ် ပြုလုပ်ပါ။

    ![Validate input.](../../../../../../translated_images/my/validate-input.c1adb9543c6495be.webp)

1. သင်ဖန်တီးထားသော custom connection ၏ **Value** ကို ရွေးပါ။ ဥပမာ *connection* ဖြစ်သည်။

    ![Connection.](../../../../../../translated_images/my/select-connection.1f2b59222bcaafef.webp)

#### သင့် custom Phi-3 / Phi-3.5 မော်ဒယ်နှင့် စကားပြောခြင်း

1. **Chat** ကို ရွေးချယ်ပါ။

    ![Select chat.](../../../../../../translated_images/my/select-chat.0406bd9687d0c49d.webp)

1. အောက်ပါက ဥပမာအဖြစ် ဖော်ပြထားသည် - ယခု သင့် custom Phi-3 / Phi-3.5 မော်ဒယ်နှင့် စကားပြောနိုင်ပြီ ဖြစ်သည်။ fine-tuning အတွက် အသုံးပြုထားသော ဒေတာအပေါ် အခြေခံ၍ မေးခွန်း မေးရန် အကြံပြုပါသည်။

    ![Chat with prompt flow.](../../../../../../translated_images/my/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 မော်ဒယ် အကဲဖြတ်ရန် Azure OpenAI ကို Deploy ပြုလုပ်ခြင်း

Microsoft Foundry တွင် Phi-3 / Phi-3.5 မော်ဒယ်ကို အကဲဖြတ်ရန်အတွက် Azure OpenAI မော်ဒယ် တစ်ခုကို Deploy လုပ်ရန် လိုအပ်သည်။ ဒီမော်ဒယ်ကို Phi-3 / Phi-3.5 မော်ဒယ်၏ အဆင့်ကို အကဲဖြတ်ရန် အသုံးပြုမည်ဖြစ်သည်။

#### Azure OpenAI ကို Deploy လုပ်ခြင်း

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) တွင် လက်မှတ်ထိုး ဝင်ပါ။

1. မိမိ ဖန်တီးထားသော Microsoft Foundry project သို့ သွားပါ။

    ![Select Project.](../../../../../../translated_images/my/select-project-created.5221e0e403e2c9d6.webp)

1. ဖန်တီးထားသော Project တွင် ဘယ်ဘက်ဘားမှ **Deployments** ကို ရွေးချယ်ပါ။

1. နေရာသွားပြကွက်မှ **+ Deploy model** ကို ရွေးချယ်ပါ။

1. **Deploy base model** ကို ရွေးချယ်ပါ။

    ![Select Deployments.](../../../../../../translated_images/my/deploy-openai-model.95d812346b25834b.webp)

1. သင်သုံးလိုသော Azure OpenAI မော်ဒယ်ကို ရွေးချယ်ပါ။ ဥပမာ **gpt-4o**။

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/my/select-openai-model.959496d7e311546d.webp)

1. **Confirm** ကို ရွေးချယ်ပါ။

### Microsoft Foundry ရဲ့ Prompt flow evaluation ဖြင့် fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို အကဲဖြတ်ခြင်း

### အကဲဖြတ်မှုအသစ် စတင်ခြင်း

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. မိမိ ဖန်တီးထားသော Microsoft Foundry project သို့ သွားပါ။

    ![Select Project.](../../../../../../translated_images/my/select-project-created.5221e0e403e2c9d6.webp)

1. ဖန်တီးထားသော Project တွင် ဘယ်ဘက်ဘားမှ **Evaluation** ကို ရွေးချယ်ပါ။

1. နေရာသွားပြကွက်မှ **+ New evaluation** ကို ရွေးချယ်ပါ။

    ![Select evaluation.](../../../../../../translated_images/my/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** evaluation ကို ရွေးပါ။

    ![Select Prompt flow evaluation.](../../../../../../translated_images/my/promptflow-evaluation.cb9758cc19b4760f.webp)

1. အောက်ပါအလုပ်များကို လုပ်ဆောင်ပါ -

    - အကဲဖြတ်မှုအမည် ထည့်ပါ။ ထူးခြားသော တန်ဖိုးဖြစ်ရမည်။
    - အလုပ်အမျိုးအစားအတွက် **Question and answer without context** ကို ရွေးချယ်ပါ။ ဤသင်ခန်းစာတွင် အသုံးပြုသော **ULTRACHAT_200k** ဒေတာဆောင်းပါးတွင် context မပါဝင်သောကြောင့် ဖြစ်သည်။
    - အကဲဖြတ်လိုသော prompt flow ကို ရွေးချယ်ပါ။

    ![Prompt flow evaluation.](../../../../../../translated_images/my/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next** ကို ရွေးပါ။

1. အောက်ပါအလုပ်များကို လုပ်ဆောင်ပါ -

    - **Add your dataset** ကို ရွေး၍ ဒေတာဆောင်းပါးကို အပလုတ်လုပ်ပါ။ ဥပမာ **ULTRACHAT_200k** dataset ထဲ၌ ပါဝင်သော *test_data.json1* ဖိုင်ကို အပလုတ်လုပ်နိုင်သည်။
    - သင့် dataset နှင့် ကိုက်ညီသော **Dataset column** ကို ရွေးချယ်ပါ။ ဥပမာ **ULTRACHAT_200k** dataset ကို အသုံးပြုသည်ဆိုပါက **${data.prompt}** ကို dataset ကော်လံအဖြစ် ရွေးချယ်ပါ။

    ![Prompt flow evaluation.](../../../../../../translated_images/my/evaluation-setting2.07036831ba58d64e.webp)

1. **Next** ကို ရွေးပါ။

1. အလုပ်စဉ်နှင့် အရည်အသွေး ဆိုင်ရာ အချက်အလက်များ ဝင်ရောက်ပြင်ဆင်ရန် -

    - သင့်အသုံးပြုလိုသော performance နှင့် quality metrics များကို ရွေးချယ်ပါ။
    - အကဲဖြတ်ရန် ဖန်တီးထားသော Azure OpenAI မော်ဒယ်ကို ရွေးပါ။ ဥပမာ **gpt-4o** ကို ရွေးချယ်သည်။

    ![Prompt flow evaluation.](../../../../../../translated_images/my/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. အန္တရာယ်နှင့် လုံခြုံမှုဆိုင်ရာ metrics များ ပြင်ဆင်ရန် -

    - သင့်အသုံးပြုလိုသော risk နှင့် safety metrics များကို ရွေးချယ်ပါ။
    - defect rate ကိုတွက်ချက်ရန် အသုံးပြုလိုသော threshold ကို ရွေးချယ်ပါ။ ဥပမာ **Medium** ကို ရွေးချယ်သည်။
    - **question** အတွက် **Data source** ကို **{$data.prompt}** သို့ သတ်မှတ်ပါ။
    - **answer** အတွက် **Data source** ကို **{$run.outputs.answer}** သို့ သတ်မှတ်ပါ။
    - **ground_truth** အတွက် **Data source** ကို **{$data.message}** သို့ သတ်မှတ်ပါ။

    ![Prompt flow evaluation.](../../../../../../translated_images/my/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next** ကို ရွေးပါ။

1. အကဲဖြတ်မှု စတင်ရန် **Submit** ကို ရွေးပါ။

1. အကဲဖြတ်မှု ပြီးမြောက်ရန် အချိန်ယူပါမည်။ အလုပ်ဖြစ်စဉ်ကို **Evaluation** tab မှာ ကြည့်ရှုနိုင်ပါသည်။

### အကဲဖြတ်မှုရလဒ် ပြန်လည်သုံးသပ်ခြင်း

> [!NOTE]
> အောက်ပါရလဒ်များသည် အကဲဖြတ်မှု လုပ်ငန်းစဉ်ကို ရုပ်သံဖော်ပြရန် ရည်ရွယ်သည်။ ဤသင်ခန်းစာတွင် ဂဏန်းဒေတာအနည်းငယ်ဖြင့် fine-tune ပြုလုပ်ထားသော မော်ဒယ်ကို အသုံးပြုခဲ့ပြီးဖြစ်သည်၊ ၎င်းသည် သင့်တင့်မှုနည်းသော ရလဒ်များ ဖြစ်ပေါ်နိုင်သည်။ အမှန်တကယ်ရရှိမည့်ရလဒ်များမှာ အသုံးပြုသော ဒေတာအရွယ်အစား၊ အရည်အသွေးနှင့် မတူကွဲပြားမှု၊ မော်ဒယ်၏ အတိအကျ ဆက်တင်များ ပေါ်မူတည်၍ များစွာကွဲပြားနိုင်သည်။

အကဲဖြတ်မှု ပြီးဆုံးလျှင်၊ performance metrics နှင့် safety metrics အတွက် ရလဒ်များအား ပြန်လည်ကြည့်ရှုနိုင်ပါသည်။
1. တိုင်းတာမှု အရည်အသွေးနှင့် စွမ်းဆောင်ရည် ချက်များ-

    - မော်ဒယ်၏ ထိရောက်မှုကို စူးစမ်းခြင်း၊ ပေါင်းစပ်မှုရှိပြီး သက်ဆိုင်သော တုံ့ပြန်ချက်များ ဖန်တီးပေးနိုင်မှုကို အကဲသတ်ပါ။

    ![Evaluation result.](../../../../../../translated_images/my/evaluation-result-gpu.85f48b42dfb74254.webp)

1. အန္တရာယ်နှင့် လုံခြုံရေး ချက်များ-

    - မော်ဒယ်ထွက်ပေါက်များက လုံခြုံဖို့နှင့် တာဝန်ရှိသော AI 원칙များနှင့် ကိုက်ညီမှုရှိရန်၊ ထိခိုက်စေသော သို့မဟုတ် မကောင်းသော အကြောင်းအရာများကို ရှောင်ကြဉ်ရန်။

    ![Evaluation result.](../../../../../../translated_images/my/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. **အသေးစိတ် တိုင်းတာမှု ရလဒ်များ** ကြည့်ရှုရန် အောက်ဆင်း၍ ကြည့်ပါ။

    ![Evaluation result.](../../../../../../translated_images/my/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. သင့် ကိုယ်ပိုင် Phi-3 / Phi-3.5 မော်ဒယ်အား စွမ်းဆောင်ရည်နှင့် လုံခြုံရေး ချက်နှစ်ခုစလုံးဖြင့် စိစစ်ခြင်းအားဖြင့် မော်ဒယ်သည် ထိရောက်မှုရှိခြင်းသာမက တာဝန်ရှိသော AI လုပ်ငန်းလိုက်နာမှုများအတိုင်းလည်းလိုက်နာထားခြင်းဖြစ်ကြောင်း အတည်ပြုနိုင်ပြီး စမတ်နယ်ပယ်တွင် အသုံးပြုရန် အသင့်ဖြစ်ပါသည်။

## ဂုဏ်ယူပါသည်!

### သင်ဤ သင်ခန်းစာကို အောင်မြင်စွာ ပြီးမြောက်လိုက်ပြီ ဖြစ်သည်

သင်သည် Microsoft Foundry တွင် Prompt flow နှင့် ပေါင်းစပ်ထားသော Phi-3 fine-tuned မော်ဒယ်ကို အောင်မြင်စွာ အကဲသတ်ပြီးပြီ ဖြစ်သည်။ ၎င်းသည် သင်၏ AI မော်ဒယ်များသည် သာမန္ကောင်းမွန်စွာ လုပ်ဆောင်ခြင်းသာမက Microsoft ၏ တာဝန်ရှိသော AI 원칙များနှင့် ကိုက်ညီမှုရှိ၍ ယုံကြည်စိတ်ချရမှုရှိသော AI လျှောက်လွှာများဖန်တီးနိုင်ရန် အရေးပါသော ကာလတစ်ခု ဖြစ်သည်။

![Architecture.](../../../../../../translated_images/my/architecture.10bec55250f5d6a4.webp)

## Azure အရင်းအမြစ်များကို သန့်ရှင်းပါ

သင့်အကောင့်တွင် အပိုစရိတ် မဖြစ်ပေါ်စေရန် Azure အရင်းအမြစ်များကို သန့်ရှင်းပါ။ Azure ပေါ်ဆော့မှတ်တမ်းတွင် သွား၍ အောက်ပါ အရင်းအမြစ်များကို ဖျက်ပစ်ပါ-

- Azure Machine learning အရင်းအမြစ်။
- Azure Machine learning မော်ဒယ် endpoint။
- Microsoft Foundry Project အရင်းအမြစ်။
- Microsoft Foundry Prompt flow အရင်းအမြစ်။

### နောက်တစ်ဆင့်များ

#### စာရွက်စာတမ်းများ

- [Responsible AI dashboard အသုံးပြု၍ AI စနစ်များကို အကဲဖြတ်ခြင်း](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [generative AI အတွက် အကဲဖြတ်မှုနှင့် ကြည့်ရှုမှု ချက်များ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry စာရွက်စာတမ်းများ](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow စာရွက်စာတမ်းများ](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### သင်ကြားမှု အကြောင်းအရာ

- [Microsoft ၏ တာဝန်ရှိသော AI နည်းလမ်းမိတ်ဆက်](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry မိတ်ဆက်ခြင်း](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### အညွှန်း

- [တာဝန်ရှိသော AI ဆိုသည်မှာ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [လုံခြုံမှုနှင့် ယုံကြည်စိတ်ချရမှု ကောင်းမွန်စေရန် Azure AI တွင် မိတ်ဆက်သော ဂျနရေးတစ် AI အတွက် အသစ်တိုးတက်ထားသော ကိရိယာများ](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [generative AI အထောက်အပံ့ အမျိုးအစားများအတွက် အကဲဖြတ်ခြင်း](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**မှတ်ချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းသည်ဖြစ်သော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါရှိနိုင်ကြောင်း အသိပေးအပ်ပါသည်။ မူရင်းစာရွက်စာတမ်းသည် ကိုယ်ပိုင်ဘာသာစကားဖြင့် ရေးသားထားသည့် အတိုင်ပင်ခံ အရင်းအမြစ်အဖြစ် စဉ်းစားသင့်သည်။ အရေးကြီးသော အချက်အလက်များအတွက် ကျွမ်းကျင်သော လူသားဘာသာပြန်တစ်ဦးအား မည်သူမဆို တပ်ဆင်ရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာတွင် ဖြစ်ပေါ်နိုင်သည့် နားလည်မှု ခြားနားမှုများ သို့မဟုတ် မှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန် မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->