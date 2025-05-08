<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-07T14:42:13+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "mo"
}
-->
Phi-3-mini ၏အကြောင်းအရာတွင်၊ inference ဆိုသည်မှာ မော်ဒယ်ကို အသုံးပြု၍ input ဒေတာအပေါ် အခြေခံကာ ခန့်မှန်းချက်များ သို့မဟုတ် output များ ဖန်တီးခြင်းဖြစ်သည်။ Phi-3-mini နှင့် ၎င်း၏ inference စွမ်းရည်များအကြောင်း ပိုမိုအသေးစိတ် ဖော်ပြပေးလိုပါသည်။

Phi-3-mini သည် Microsoft မှ ထုတ်ပြန်သော Phi-3 စီးရီးမော်ဒယ်များအတွင်း ပါဝင်သည်။ ဤမော်ဒယ်များသည် Small Language Models (SLMs) အတွက် အလားအလာအသစ်များ ဖန်တီးရန် ရည်ရွယ်ထားသည်။

Phi-3-mini နှင့် ၎င်း၏ inference စွမ်းရည်များအကြောင်း အချက်အလက်အချို့မှာ -

## **Phi-3-mini အကျဉ်းချုပ်**
- Phi-3-mini ၏ parameter အရွယ်အစားမှာ 3.8 ဘီလီယံဖြစ်သည်။
- ယင်းသည် ရိုးရာ ကွန်ပျူတာပစ္စည်းများတွင်သာမက မိုဘိုင်းပစ္စည်းများနှင့် IoT ပစ္စည်းများကဲ့သို့သော edge ပစ္စည်းများတွင်ပါ ပြေးနိုင်သည်။
- Phi-3-mini ထုတ်ပြန်ခြင်းဖြင့် လူတစ်ဦးချင်းစီနှင့် စီးပွားရေးလုပ်ငန်းများသည် SLM များကို မတူညီသော hardware ပစ္စည်းများပေါ်တွင် တပ်ဆင်အသုံးပြုနိုင်ခြင်း၊ အထူးသဖြင့် အရင်းအမြစ်ကန့်သတ်ထားသော ပတ်ဝန်းကျင်များတွင် အသုံးပြုနိုင်ခြင်း ဖြစ်သည်။
- ယင်းသည် ရိုးရာ PyTorch format၊ gguf format ၏ quantized ဗားရှင်းနှင့် ONNX-based quantized ဗားရှင်းတို့အပါအဝင် မော်ဒယ်ဖော်မတ်မျိုးစုံကို ထောက်ပံ့သည်။

## **Phi-3-mini ကို အသုံးပြုခြင်း**
Phi-3-mini ကို အသုံးပြုရန် Semantic Kernel ကို Copilot application တစ်ခုတွင် အသုံးပြုနိုင်သည်။ Semantic Kernel သည် Azure OpenAI Service၊ Hugging Face တွင်ရှိသော open-source မော်ဒယ်များနှင့် local မော်ဒယ်များနှင့် ယေဘုယျအားဖြင့် ကိုက်ညီသည်။
quantized မော်ဒယ်များကို ခေါ်ယူရန် Ollama သို့မဟုတ် LlamaEdge ကိုလည်း အသုံးပြုနိုင်သည်။ Ollama သည် တစ်ဦးချင်း အသုံးပြုသူများအား quantized မော်ဒယ်မျိုးစုံကို ခေါ်ယူခွင့်ပြုသည်၊ LlamaEdge သည် GGUF မော်ဒယ်များအတွက် cross-platform အသုံးပြုနိုင်မှုကို ပံ့ပိုးပေးသည်။

## **Quantized မော်ဒယ်များ**
အများပြည်သူသည် local inference အတွက် quantized မော်ဒယ်များကို ပိုမိုနှစ်သက်ကြသည်။ ဥပမာအားဖြင့် Ollama ဖြင့် Phi-3 ကို တိုက်ရိုက် run ပြုလုပ်နိုင်သလို၊ Modelfile ကို အသုံးပြု၍ offline တွင်လည်း ပြင်ဆင်နိုင်သည်။ Modelfile တွင် GGUF ဖိုင်လမ်းကြောင်းနှင့် prompt ဖော်မတ်ကို ဖော်ပြထားသည်။

## **Generative AI ၏ အခွင့်အလမ်းများ**
Phi-3-mini ကဲ့သို့ SLM များပေါင်းစပ်ခြင်းဖြင့် generative AI အတွက် အသစ်အဆန်းများ ဖန်တီးနိုင်သည်။ inference သည် ပထမဆုံးအဆင့်သာဖြစ်ပြီး၊ ၎င်းမော်ဒယ်များကို အရင်းအမြစ်ကန့်သတ်ထားသော၊ latency ကန့်သတ်ထားသော၊ သက်သာမှုကန့်သတ်ထားသော ပတ်ဝန်းကျင်များတွင် မတူညီသော လုပ်ငန်းများအတွက် အသုံးပြုနိုင်သည်။

## **Phi-3-mini ဖြင့် Generative AI ကို ဖွင့်လှစ်ခြင်း: Inference နှင့် Deployment လမ်းညွှန်**
Semantic Kernel, Ollama/LlamaEdge, နှင့် ONNX Runtime ကို အသုံးပြု၍ Phi-3-mini မော်ဒယ်များကို ရယူခြင်းနှင့် inference ပြုလုပ်ခြင်း၊ မတူညီသော လျှောက်လွှာအခြေအနေများတွင် generative AI ၏ အခွင့်အလမ်းများကို ရှာဖွေပါ။

**Features**
phi3-mini မော်ဒယ်ကို အောက်ပါတွင် inference ပြုလုပ်နိုင်သည်-

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

အကျဉ်းချုပ်အားဖြင့် Phi-3-mini သည် ဖန်တီးမှု AI ကို မတူညီသော မော်ဒယ်ဖော်မတ်များနှင့် လျှောက်လွှာအခြေအနေများတွင် လေ့လာအသုံးချရန် ဖန်တီးသူများအား အခွင့်အလမ်းများ ပေးစွမ်းသည်။

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.