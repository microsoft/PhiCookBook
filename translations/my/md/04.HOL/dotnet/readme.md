<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-09T19:36:33+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "my"
}
-->
﻿## C# ဖြင့် Phi labs သို့ ကြိုဆိုပါသည်

.NET ပတ်ဝန်းကျင်တွင် Phi မော်ဒယ်များ၏ အမျိုးမျိုးသောဗားရှင်းများကို ထိရောက်စွာ ပေါင်းစပ်အသုံးပြုနည်းကို ပြသသည့် လက်တွေ့လုပ်ငန်းခွင်များ ရွေးချယ်ထားပါသည်။

## လိုအပ်ချက်များ

နမူနာကို စတင်အသုံးပြုမည့်အခါ အောက်ပါအရာများကို သေချာထည့်သွင်းထားပါ။

**.NET 9:** သင့်ကွန်ပျူတာတွင် [နောက်ဆုံးထွက် .NET ဗားရှင်း](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ကို ထည့်သွင်းထားကြောင်း သေချာပါစေ။

**(ရွေးချယ်စရာ) Visual Studio သို့မဟုတ် Visual Studio Code:** .NET ပရောဂျက်များကို အလုပ်လုပ်နိုင်သော IDE သို့မဟုတ် ကုဒ်တည်းဖြတ်ကိရိယာတစ်ခု လိုအပ်ပါသည်။ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) သို့မဟုတ် [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ကို အကြံပြုပါသည်။

**git ကို အသုံးပြု၍** Hugging Face မှ Phi-3, Phi3.5 သို့မဟုတ် Phi-4 ဗားရှင်းများထဲမှ တစ်ခုကို ဒေသိယကွန်ပျူတာသို့ clone လုပ်ပါ။ [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)

**Phi-4 ONNX မော်ဒယ်များကို** သင့်ဒေသိယကွန်ပျူတာသို့ ဒေါင်းလုပ်လုပ်ပါ။

### မော်ဒယ်များ သိမ်းဆည်းမည့် ဖိုလ်ဒါသို့ သွားပါ

```bash
cd c:\phi\models
```

### lfs အတွက် ထောက်ပံ့မှု ထည့်သွင်းပါ

```bash
git lfs install 
```

### Phi-4 mini instruct မော်ဒယ်နှင့် Phi-4 multi modal မော်ဒယ်ကို clone လုပ်ပြီး ဒေါင်းလုပ်လုပ်ပါ

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX မော်ဒယ်များကို** သင့်ဒေသိယကွန်ပျူတာသို့ ဒေါင်းလုပ်လုပ်ပါ။

### Phi-3 mini 4K instruct မော်ဒယ်နှင့် Phi-3 vision 128K မော်ဒယ်ကို clone လုပ်ပြီး ဒေါင်းလုပ်လုပ်ပါ

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**အရေးကြီးချက်:** လက်ရှိ ပြသမှုများသည် မော်ဒယ်၏ ONNX ဗားရှင်းများကို အသုံးပြုရန် ဒီဇိုင်းဆွဲထားပါသည်။ အထက်ပါအဆင့်များသည် အောက်ပါ မော်ဒယ်များကို clone လုပ်ပါသည်။

## Labs များအကြောင်း

အဓိက ဖြေရှင်းချက်တွင် C# ဖြင့် Phi မော်ဒယ်များ၏ စွမ်းဆောင်ရည်များကို ပြသသည့် နမူနာ Labs များစွာ ပါဝင်သည်။

| ပရောဂျက် | မော်ဒယ် | ဖော်ပြချက် |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 သို့မဟုတ် Phi-3.5 | အသုံးပြုသူ မေးခွန်းမေးနိုင်သည့် နမူနာ console chat ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ ONNX Phi-3 မော်ဒယ်ကို `Microsoft.ML.OnnxRuntime` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 သို့မဟုတ် Phi-3.5 | အသုံးပြုသူ မေးခွန်းမေးနိုင်သည့် နမူနာ console chat ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ ONNX Phi-3 မော်ဒယ်ကို `Microsoft.Semantic.Kernel` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 သို့မဟုတ် Phi-3.5 | ဒေသိယ phi3 vision မော်ဒယ်ကို အသုံးပြု၍ ပုံများကို စိစစ်သုံးသပ်သည့် နမူနာပရောဂျက်ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ ONNX Phi-3 Vision မော်ဒယ်ကို `Microsoft.ML.OnnxRuntime` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 သို့မဟုတ် Phi-3.5 | ဒေသိယ phi3 vision မော်ဒယ်ကို အသုံးပြု၍ ပုံများကို စိစစ်သုံးသပ်သည့် နမူနာပရောဂျက်ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ ONNX Phi-3 Vision မော်ဒယ်ကို `Microsoft.ML.OnnxRuntime` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ ထို့အပြင် အသုံးပြုသူနှင့် ဆက်သွယ်ရန် မီနူးရွေးချယ်စရာများကိုလည်း ဖော်ပြသည်။ | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | အသုံးပြုသူ မေးခွန်းမေးနိုင်သည့် နမူနာ console chat ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ ONNX Phi-4 မော်ဒယ်ကို `Microsoft.ML.OnnxRuntime` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | အသုံးပြုသူ မေးခွန်းမေးနိုင်သည့် နမူနာ console chat ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ ONNX Phi-4 မော်ဒယ်ကို `Semantic Kernel` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | အသုံးပြုသူ မေးခွန်းမေးနိုင်သည့် နမူနာ console chat ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ ONNX Phi-4 မော်ဒယ်ကို `Microsoft.ML.OnnxRuntimeGenAI` စာကြည့်တိုက်များဖြင့် ဖွင့်ပြီး `Microsoft.Extensions.AI` မှ `IChatClient` ကို အကောင်အထည်ဖော်ထားသည်။ |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | အသုံးပြုသူ မေးခွန်းမေးနိုင်သည့် နမူနာ console chat ဖြစ်သည်။ chat တွင် မှတ်ဉာဏ်စနစ် ပါဝင်သည်။ |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | ဒေသိယ Phi-4 မော်ဒယ်ကို အသုံးပြု၍ ပုံများကို စိစစ်သုံးသပ်ပြီး ရလဒ်ကို console တွင် ပြသသည့် နမူနာပရောဂျက်ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ Phi-4-`multimodal-instruct-onnx` မော်ဒယ်ကို `Microsoft.ML.OnnxRuntime` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | ဒေသိယ Phi-4 မော်ဒယ်ကို အသုံးပြု၍ အသံဖိုင်ကို စိစစ်သုံးသပ်ပြီး ဖိုင်၏ စာသားပြန်လည်ထုတ်ပေးကာ ရလဒ်ကို console တွင် ပြသသည့် နမူနာပရောဂျက်ဖြစ်သည်။ ပရောဂျက်သည် ဒေသိယ Phi-4-`multimodal-instruct-onnx` မော်ဒယ်ကို `Microsoft.ML.OnnxRuntime` စာကြည့်တိုက်များဖြင့် ဖွင့်သည်။ |

## ပရောဂျက်များကို မည်သို့ ပြေးမည်နည်း

ပရောဂျက်များကို ပြေးရန် အောက်ပါအဆင့်များကို လိုက်နာပါ။

1. Repository ကို သင့်ဒေသိယကွန်ပျူတာသို့ clone လုပ်ပါ။

1. Terminal ကို ဖွင့်ပြီး လိုချင်သော ပရောဂျက်သို့ သွားပါ။ ဥပမာအားဖြင့် `LabsPhi4-Chat-01OnnxRuntime` ကို ပြေးကြည့်မည်။

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. အောက်ပါ command ဖြင့် ပရောဂျက်ကို ပြေးပါ။

    ```bash
    dotnet run
    ```

1. နမူနာပရောဂျက်သည် အသုံးပြုသူထံမှ input တောင်းပြီး ဒေသိယ မော်ဒယ်ကို အသုံးပြု၍ ပြန်လည်ဖြေကြားပါသည်။

   ပြေးနေသော demo သည် အောက်ပါအတိုင်း ဖြစ်ပါသည်။

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။