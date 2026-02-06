Phi-3-mini အတွက် inference ဆိုသည်မှာ input data အပေါ် အခြေခံပြီး မော်ဒယ်ကို အသုံးပြု၍ ခန့်မှန်းချက်များ ထုတ်ပေးခြင်း သို့မဟုတ် output များ ဖန်တီးခြင်း ဖြစ်သည်။ Phi-3-mini နှင့် ၎င်း၏ inference စွမ်းဆောင်ရည်များအကြောင်း ပိုမိုအသေးစိတ် ဖော်ပြပေးလိုပါသည်။

Phi-3-mini သည် Microsoft မှ ထုတ်ပြန်သော Phi-3 စီးရီး မော်ဒယ်များထဲမှ တစ်ခုဖြစ်သည်။ ဤမော်ဒယ်များသည် Small Language Models (SLMs) အတွက် ဖြစ်နိုင်ခြေများကို ပြန်လည်သတ်မှတ်ရန် ရည်ရွယ်ထားသည်။

Phi-3-mini နှင့် ၎င်း၏ inference စွမ်းဆောင်ရည်များအကြောင်း အချက်အလက်အချို့မှာ အောက်ပါအတိုင်း ဖြစ်ပါသည်-

## **Phi-3-mini အကျဉ်းချုပ်**
- Phi-3-mini ၏ parameter အရွယ်အစားမှာ ၃.၈ ဘီလီယံ ဖြစ်သည်။
- ယင်းသည် ရိုးရာ ကွန်ပျူတာပစ္စည်းများတွင်သာမက မိုဘိုင်းပစ္စည်းများနှင့် IoT ပစ္စည်းများကဲ့သို့သော edge devices များတွင်လည်း လည်ပတ်နိုင်သည်။
- Phi-3-mini ထုတ်ပြန်ခြင်းဖြင့် လူပုဂ္ဂိုလ်များနှင့် စီးပွားရေးလုပ်ငန်းများသည် အမျိုးမျိုးသော hardware ပစ္စည်းများပေါ်တွင် SLM များကို တပ်ဆင်အသုံးပြုနိုင်ပြီး အရင်းအမြစ်ကန့်သတ်ထားသော ပတ်ဝန်းကျင်များတွင် အထူးသဖြင့် အသုံးဝင်စေသည်။
- ၎င်းသည် ရိုးရာ PyTorch ဖော်မတ်၊ gguf ဖော်မတ်၏ quantized ဗားရှင်းနှင့် ONNX အခြေခံ quantized ဗားရှင်းတို့ အပါအဝင် မော်ဒယ်ဖော်မတ်အမျိုးမျိုးကို ထောက်ပံ့ပေးသည်။

## **Phi-3-mini ကို အသုံးပြုခြင်း**
Phi-3-mini ကို အသုံးပြုရန်အတွက် Copilot application တွင် [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ကို အသုံးပြုနိုင်သည်။ Semantic Kernel သည် Azure OpenAI Service၊ Hugging Face တွင်ရှိသော open-source မော်ဒယ်များနှင့် ဒေသခံ မော်ဒယ်များနှင့် အထွေထွေကိုက်ညီမှုရှိသည်။
ထို့အပြင် quantized မော်ဒယ်များကို ခေါ်ယူရန် [Ollama](https://ollama.com) သို့မဟုတ် [LlamaEdge](https://llamaedge.com) ကိုလည်း အသုံးပြုနိုင်သည်။ Ollama သည် တစ်ဦးချင်း အသုံးပြုသူများအတွက် quantized မော်ဒယ်များကို ခေါ်ယူခွင့်ပြုသည့်အပြင် LlamaEdge သည် GGUF မော်ဒယ်များအတွက် cross-platform အသုံးပြုနိုင်မှုကို ပံ့ပိုးပေးသည်။

## **Quantized မော်ဒယ်များ**
အများစုသော အသုံးပြုသူများသည် ဒေသခံ inference အတွက် quantized မော်ဒယ်များကို ပိုမိုနှစ်သက်ကြသည်။ ဥပမာအားဖြင့် Ollama ကို တိုက်ရိုက် အသုံးပြု၍ Phi-3 ကို run လိုက်နိုင်သလို Modelfile ဖြင့် offline အနေဖြင့် ဖွဲ့စည်းနိုင်သည်။ Modelfile တွင် GGUF ဖိုင်လမ်းကြောင်းနှင့် prompt ဖော်မတ်ကို ဖော်ပြထားသည်။

## **Generative AI ၏ အခွင့်အလမ်းများ**
Phi-3-mini ကဲ့သို့သော SLM များ ပေါင်းစပ်အသုံးပြုခြင်းဖြင့် generative AI အတွက် အသစ်သော အခွင့်အလမ်းများ ဖွင့်လှစ်ပေးသည်။ Inference သည် ပထမဆုံးအဆင့်သာဖြစ်ပြီး၊ ဤမော်ဒယ်များကို အရင်းအမြစ်ကန့်သတ်ထားသော၊ latency ကန့်သတ်ထားသောနှင့် ကုန်ကျစရိတ်ကန့်သတ်ထားသော အခြေအနေများတွင် အမျိုးမျိုးသော လုပ်ငန်းများအတွက် အသုံးပြုနိုင်သည်။

## **Phi-3-mini ဖြင့် Generative AI ကို ဖွင့်လှစ်ခြင်း - Inference နှင့် Deployment လမ်းညွှန်**
Semantic Kernel၊ Ollama/LlamaEdge နှင့် ONNX Runtime ကို အသုံးပြု၍ Phi-3-mini မော်ဒယ်များကို ခေါ်ယူပြီး inference ပြုလုပ်နည်းကို လေ့လာနိုင်ပြီး၊ အမျိုးမျိုးသော application ပတ်ဝန်းကျင်များတွင် generative AI ၏ အခွင့်အလမ်းများကို ရှာဖွေတွေ့ရှိနိုင်သည်။

**အင်္ဂါရပ်များ**  
Phi-3-mini မော်ဒယ်ကို အောက်ပါနေရာများတွင် inference ပြုလုပ်နိုင်သည်-

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

အကျဉ်းချုပ်အားဖြင့် Phi-3-mini သည် ဖန်တီးသူများအား မော်ဒယ်ဖော်မတ်အမျိုးမျိုးကို စမ်းသပ်လေ့လာနိုင်စေပြီး၊ အမျိုးမျိုးသော application ပတ်ဝန်းကျင်များတွင် generative AI ကို အသုံးချနိုင်စေသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။