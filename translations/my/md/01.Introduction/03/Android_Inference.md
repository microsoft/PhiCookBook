# **Android တွင် Phi-3 အား ခန့်မှန်းခြေခြင်း**

Android စက်များပေါ်တွင် Phi-3-mini ဖြင့် ခန့်မှန်းခြေမှုကို မည်သို့ ဆောင်ရွက်နိုင်သည်ကို စူးစမ်းကြည့်လိုက်ရအောင်။ Phi-3-mini သည် Microsoft ကနေ ထုတ်လုပ်သည့် မော်ဒယ်စီးရီးသစ်ဖြစ်ပြီး Edge စက်များနှင့် IoT စက်များပေါ်တွင် Large Language Models (LLMs) များကို တပ်ဆင်အသုံးပြုနိုင်စေပါသည်။

## Semantic Kernel နှင့် ခန့်မှန်းခြေမှု

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) သည် Azure OpenAI Service၊ OpenAI မော်ဒယ်များနှင့် ဒေသဆိုင်ရာ မော်ဒယ်များနှင့် သင့်တော်သော အက်ပ်ပလီကေးရှင်းများကို ဖန်တီးခွင့်ပြုသည့် အက်ပ်ဖလက်ဝမ်ဖြစ်ပါသည်။ Semantic Kernel အသစ်သောသူများအတွက် [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ကို ကြည့်ရှုရန် အကြံပြုပါသည်။

### Semantic Kernel ဖြင့် Phi-3-mini ကို ဝင်ရောက်အသုံးပြုရန်

Semantic Kernel ထဲတွင် Hugging Face Connector နှင့် ပေါင်းစပ်နိုင်သည်။ ဤ [နမူနာကုတ်](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) ကို ကြည့်ပါ။

မူလအားဖြင့် Hugging Face ပေါ်ရှိ မော်ဒယ် ID နှင့် ကိုက်ညီသည်။ သို့သော် ဆောက်လုပ်ပြီးသား ဒေသဆိုင်ရာ Phi-3-mini မော်ဒယ်ဆာဗာကိုလည်း ချိတ်ဆက်အသုံးပြုနိုင်ပါသည်။

### Ollama သို့မဟုတ် LlamaEdge ဖြင့် Quantized မော်ဒယ်များ ခေါ်ယူခြင်း

မော်ဒယ်များကို ဒေသတွင်းပြေးဆွဲရန် သုံးသည့် အသုံးပြုသူများအများစုသည် quantized မော်ဒယ်များကို ပိုမိုတိုက်တွန်းကြသည်။ [Ollama](https://ollama.com/) နှင့် [LlamaEdge](https://llamaedge.com) တို့က တစ်ဦးချင်းအသုံးပြုသူတွေကို အမျိုးမျိုးသော quantized မော်ဒယ်များကို ခေါ်ယူခွင့်ပြုသည်။

#### Ollama

သင့် `ollama run Phi-3` ကို တိုက်ရိုက်ပြေးနိုင်သလို သင့် `.gguf` ဖိုင်လမ်းကြောင်းဖြင့် `Modelfile` ပြုလုပ်ပြီး အော့ဖ်လိုင်းမှာသတ်မှတ်နိုင်ပါသည်။

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[နမူနာကုတ်](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

သင်သည် `.gguf` ဖိုင်များကို မိုဃ်းတိမ်နှင့် အနားရှိ စက်ပစ္စည်းများ၌ တစ်ပြိုင်နက်တည်း အသုံးပြုလိုပါက LlamaEdge သည် အလွန်ကောင်းမွန်သောရွေးချယ်မှုဖြစ်သည်။ စတင်ရန်အတွက် ဤ [နမူနာကုဒ်](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ကို ကိုးကားနိုင်ပါသည်။

### အန်ဒရွိုက်ဖုန်းများတွင် တပ်ဆင်ပြီး ပြေးဆွဲခြင်း

1. အန်ဒရွိုက်ဖုန်းများအတွက် **MLC Chat app** (အခမဲ့) ကို ဒေါင်းလုဒ်ဆွဲပါ။
2. APK ဖိုင် (148MB) ကို ဒေါင်းလုဒ်ဆွဲ၍ သင့်စက်ပေါ်တွင် တပ်ဆင်ပါ။
3. MLC Chat app ကို စတင်ဖွင့်ပါ။ Phi-3-mini အပါအဝင် AI မော်ဒယ်များစာရင်း တစ်ခုကို တွေ့မြင်မည်ဖြစ်သည်။

### LiteRT-LM ဖြင့် Phi-4-mini-reasoning ကို ပြေးဆွဲခြင်း

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) သည် ကြိုးပမ်းအားထုတ်မှုဖြင့် ကွန်မြူနာလ်ကူးပြောင်းထားသည့် int4 `.litertlm` ဘန်ဒယ်တစ်ခုအဖြစ် Google ၏ [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) စက်ပေါ် runtime တွင် အသုံးပြုနိုင်သည်။ အန်ဒရွိုက်တွင် [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) app (app ထဲမှ Hugging Face မှ ဘန်ဒယ်ကို တင်သွင်းပါ) ကြောင့် CPU သို့မဟုတ် GPU ပေါ်တွင် ပြေးဆွဲနိုင်ပြီး၊ LiteRT-LM Kotlin API ဖြင့်လည်းအသုံးပြုနိုင်သည်။ အဆိုပါ ဘန်ဒယ်သည် iOS, macOS, Linux နဲ့ Windows ပေါ်တွင်လည်း ပြေးဆွဲနိုင်သည်။ မော်ဒယ်အကြောင်းအရာဇယားတွင် တိုင်းတာထားသည့် အရှိန်နှုန်းများနှင့် ပြေးဆွဲရန်အမိန့်များ ပါရှိသည်။

အကျဉ်းချုပ်အားဖြင့် Phi-3-mini သည် အနားရှိ စက်ပစ္စည်းများပေါ်တွင် ထုတ်လုပ်မှု AI အတွက် စိတ်လှုပ်ရှားဖွယ် အလားအလာများကို ဖွင့်ပေးပြီး၊ သင်သည် အန်ဒရွိုက်ပေါ်တွင် ၎င်း၏ စွမ်းရည်များကို စတင်လေ့လာနိုင်ပါသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->