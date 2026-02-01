# **Android တွင် Phi-3 ဖြင့် အနုတ်ယူခြင်း**

Android စက်များပေါ်တွင် Phi-3-mini ဖြင့် အနုတ်ယူခြင်းကို မည်သို့ပြုလုပ်နိုင်သည်ကို လေ့လာကြမယ်။ Phi-3-mini သည် Microsoft မှ ထုတ်လုပ်သော မော်ဒယ်အသစ်တစ်ခုဖြစ်ပြီး Edge စက်များနှင့် IoT စက်များပေါ်တွင် Large Language Models (LLMs) ကို တပ်ဆင်အသုံးပြုနိုင်စေသည်။

## Semantic Kernel နှင့် အနုတ်ယူခြင်း

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) သည် Azure OpenAI Service၊ OpenAI မော်ဒယ်များနှင့် ဒေသခံမော်ဒယ်များနှင့် ကိုက်ညီသော အက်ပလီကေးရှင်းများ ဖန်တီးနိုင်သော အက်ပလီကေးရှင်း ဖရိမ်ဝတ်တစ်ခုဖြစ်သည်။ Semantic Kernel အသစ်ဖြစ်သူများအတွက် [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ကို ကြည့်ရှုရန် အကြံပြုပါသည်။

### Semantic Kernel ဖြင့် Phi-3-mini ကို အသုံးပြုရန်

Semantic Kernel တွင် Hugging Face Connector နှင့် ပေါင်းစပ်အသုံးပြုနိုင်သည်။ ဤ [နမူနာကုဒ်](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) ကို ရည်ညွှန်းပါ။

ပုံမှန်အားဖြင့် Hugging Face ပေါ်ရှိ မော်ဒယ် ID နှင့် ကိုက်ညီသည်။ သို့သော် ဒေသခံတွင် တည်ဆောက်ထားသော Phi-3-mini မော်ဒယ်ဆာဗာကိုလည်း ချိတ်ဆက်အသုံးပြုနိုင်သည်။

### Ollama သို့မဟုတ် LlamaEdge ဖြင့် Quantized မော်ဒယ်များကို ခေါ်ယူခြင်း

အသုံးပြုသူများအများစုသည် မော်ဒယ်များကို ဒေသခံတွင် ပြေးဆွဲရန် quantized မော်ဒယ်များကို သုံးရန် နှစ်သက်ကြသည်။ [Ollama](https://ollama.com/) နှင့် [LlamaEdge](https://llamaedge.com) သည် အသုံးပြုသူတစ်ဦးချင်းစီအတွက် မတူညီသော quantized မော်ဒယ်များကို ခေါ်ယူနိုင်စေသည်။

#### Ollama

`ollama run Phi-3` ကို တိုက်ရိုက် ပြေးဆွဲနိုင်ပြီး သို့မဟုတ် `.gguf` ဖိုင်လမ်းကြောင်းပါရှိသော `Modelfile` တစ်ခု ဖန်တီး၍ အော့ဖ်လိုင်းတွင် ပြင်ဆင်နိုင်သည်။

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[နမူနာကုဒ်](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

`.gguf` ဖိုင်များကို Cloud နှင့် Edge စက်များတွင် တပြိုင်နက် အသုံးပြုလိုပါက LlamaEdge သည် အကောင်းဆုံးရွေးချယ်မှုဖြစ်သည်။ စတင်ရန် ဤ [နမူနာကုဒ်](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ကို ရည်ညွှန်းနိုင်သည်။

### Android ဖုန်းများတွင် တပ်ဆင်ပြီး ပြေးဆွဲခြင်း

1. **MLC Chat app ကို ဒေါင်းလုပ်လုပ်ပါ** (အခမဲ့) Android ဖုန်းများအတွက်။
2. APK ဖိုင် (148MB) ကို ဒေါင်းလုပ်လုပ်ပြီး စက်တွင် တပ်ဆင်ပါ။
3. MLC Chat app ကို ဖွင့်ပါ။ Phi-3-mini အပါအဝင် AI မော်ဒယ်များ စာရင်းကို တွေ့မြင်ရမည်။

အကျဉ်းချုပ်အားဖြင့် Phi-3-mini သည် Edge စက်များပေါ်တွင် generative AI အတွက် စိတ်လှုပ်ရှားဖွယ် အခွင့်အလမ်းများ ဖန်တီးပေးပြီး Android ပေါ်တွင် ၎င်း၏ စွမ်းဆောင်ရည်များကို စတင်လေ့လာနိုင်ပါသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။