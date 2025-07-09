<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-07-09T19:07:19+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "my"
}
-->
## Fine Tuning Scenarios

![FineTuning with MS Services](../../../../imgs/03/intro/FinetuningwithMS.png)

**Platform** ၎င်းတွင် Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito နှင့် ONNX Runtime ကဲ့သို့သော နည်းပညာမျိုးစုံ ပါဝင်သည်။

**Infrastructure** ၎င်းတွင် fine-tuning လုပ်ငန်းစဉ်အတွက် အရေးကြီးသော CPU နှင့် FPGA ပါဝင်သည်။ နည်းပညာတစ်ခုချင်းစီအတွက် အိုင်ကွန်များကို ပြသပေးပါမည်။

**Tools & Framework** ၎င်းတွင် ONNX Runtime နှစ်ခု ပါဝင်သည်။ နည်းပညာတစ်ခုချင်းစီအတွက် အိုင်ကွန်များကို ပြသပေးပါမည်။
[Insert icons for ONNX Runtime and ONNX Runtime]

Microsoft နည်းပညာများဖြင့် fine-tuning လုပ်ငန်းစဉ်တွင် အစိတ်အပိုင်းများနှင့် ကိရိယာများ မျိုးစုံ ပါဝင်သည်။ ဤနည်းပညာများကို နားလည်ပြီး အသုံးချခြင်းဖြင့် ကျွန်ုပ်တို့၏ အပလီကေးရှင်းများကို ထိရောက်စွာ fine-tune ပြုလုပ်နိုင်ပြီး ပိုမိုကောင်းမွန်သော ဖြေရှင်းချက်များ ဖန်တီးနိုင်ပါသည်။

## Model as Service

Hosted fine-tuning ကို အသုံးပြု၍ compute ကို ဖန်တီးစီမံရန် မလိုအပ်ဘဲ မော်ဒယ်ကို fine-tune ပြုလုပ်ပါ။

![MaaS Fine Tuning](../../../../imgs/03/intro/MaaSfinetune.png)

Serverless fine-tuning သည် Phi-3-mini နှင့် Phi-3-medium မော်ဒယ်များအတွက် ရရှိနိုင်ပြီး၊ developer များအနေဖြင့် cloud နှင့် edge စနစ်များအတွက် မော်ဒယ်များကို လျင်မြန်လွယ်ကူစွာ စိတ်ကြိုက်ပြင်ဆင်နိုင်သည်။ ထို့အပြင် Phi-3-small ကို Models-as-a-Service အဖြစ် ထုတ်ပြန်ထားပြီး developer များအနေဖြင့် အခြေခံအင်ဖရာစတပ်ချာကို စီမံခန့်ခွဲရန် မလိုဘဲ AI ဖွံ့ဖြိုးတိုးတက်မှုကို လျင်မြန်စွာ စတင်နိုင်ပါသည်။

## Model as a Platform

အသုံးပြုသူများသည် မိမိတို့၏ compute ကို ကိုယ်တိုင် စီမံခန့်ခွဲကာ မော်ဒယ်များကို fine-tune ပြုလုပ်ကြသည်။

![Maap Fine Tuning](../../../../imgs/03/intro/MaaPFinetune.png)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Fine Tuning Scenarios

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|အကြိုသင်ကြားပြီးသား LLM များကို အထူးတာဝန်များ သို့မဟုတ် ဒိုမိန်းများအတွက် ကိုက်ညီစေရန်|Yes|Yes|Yes|Yes|Yes|Yes|
|စာသားခွဲခြားခြင်း၊ အမည်သတ်မှတ်ခြင်းနှင့် စက်ဘာသာပြန်ခြင်းကဲ့သို့သော NLP လုပ်ငန်းများအတွက် fine-tuning|Yes|Yes|Yes|Yes|Yes|Yes|
|QA လုပ်ငန်းများအတွက် fine-tuning|Yes|Yes|Yes|Yes|Yes|Yes|
|chatbot များတွင် လူ့စကားသဘောဆန်သော တုံ့ပြန်ချက်များ ဖန်တီးရန် fine-tuning|Yes|Yes|Yes|Yes|Yes|Yes|
|တေးဂီတ၊ အနုပညာ သို့မဟုတ် အခြားဖန်တီးမှုအမျိုးအစားများ ဖန်တီးရန် fine-tuning|Yes|Yes|Yes|Yes|Yes|Yes|
|တွက်ချက်မှုနှင့် ငွေကြေးကုန်ကျစရိတ် လျော့ချခြင်း|Yes|Yes|No|Yes|Yes|No|
|မှတ်ဉာဏ်အသုံးပြုမှု လျော့ချခြင်း|No|Yes|No|Yes|Yes|Yes|
|ထိရောက်သော fine-tuning အတွက် ပရမီတာနည်းပါးစွာ အသုံးပြုခြင်း|No|Yes|Yes|No|No|Yes|
|GPU စက်ပစ္စည်းများအားလုံး၏ စုစုပေါင်း GPU မှတ်ဉာဏ်ကို အသုံးပြုနိုင်သော မှတ်ဉာဏ်ထိရောက်သော ဒေတာပေါ်လွှမ်းမှု|No|No|No|Yes|Yes|Yes|

## Fine Tuning Performance Examples

![Finetuning Performance](../../../../imgs/03/intro/Finetuningexamples.png)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် သတ်မှတ်စဉ်းစားသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။