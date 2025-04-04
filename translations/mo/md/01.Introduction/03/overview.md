<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d570fac7029d6697ad8ab1c963b43811",
  "translation_date": "2025-04-04T12:07:34+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "mo"
}
-->
Phi-3-mini မှာ inference ဆိုတာ input data အပေါ်အခြေခံပြီး မော်ဒယ်ကိုအသုံးပြုကာ ခန့်မှန်းချက်လုပ်ခြင်း သို့မဟုတ် output ထုတ်လုပ်ခြင်း ဖြစ်ပါတယ်။ အောက်မှာ Phi-3-mini နဲ့ သူ့ရဲ့ inference လုပ်ဆောင်ချက်တွေကို ပိုမိုသိရှိစေရန် အသေးစိတ်ဖော်ပြပေးလိုက်ပါတယ်။

Phi-3-mini ဟာ Microsoft က ထုတ်လုပ်ထားတဲ့ Phi-3 မော်ဒယ်တွေရဲ့ တစ်စိတ်တစ်ပိုင်းဖြစ်ပြီး Small Language Models (SLMs) နဲ့အတူ သက်တောင့်သက်သာ အသုံးပြုနိုင်မယ့် နည်းလမ်းအသစ်တွေကို ဖော်ဆောင်ပေးပါတယ်။

## **Phi-3-mini အကျဉ်းချုပ်:**
- Phi-3-mini ရဲ့ parameter အရွယ်အစားက 3.8 ဘီလျံဖြစ်ပါတယ်။
- ဒါဟာ ရိုးရိုးကွန်ပျူတာစနစ်တွေပေါ်မှာပဲမဟုတ်ဘဲ မိုဘိုင်းပစ္စည်းတွေ၊ IoT စနစ်တွေလို edge devices တွေပေါ်မှာတောင်လည်း အဆင်ပြေစွာ chạy လိုက်နိုင်ပါတယ်။
- Phi-3-mini ထုတ်ဝေမှုကြောင့် လူပုဂ္ဂိုလ်တွေ နဲ့ လုပ်ငန်းတွေဟာ SLMs ကို အရင်းအမြစ် အကန့်အသတ်ရှိတဲ့ ပစ္စည်းတွေမှာတောင် လွယ်လွယ်ကူကူ အသုံးပြုနိုင်လာပါတယ်။
- PyTorch format အပါအဝင် gguf format ရဲ့ quantized version နဲ့ ONNX-based quantized version အစရှိတဲ့ မော်ဒယ် format မျိုးစုံကို ပံ့ပိုးပေးပါတယ်။

## **Phi-3-mini ကိုရယူရန်:**
Phi-3-mini ကိုရယူဖို့ [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ကို Copilot အက်ပလီကေးရှင်းမှာအသုံးပြုနိုင်ပါတယ်။ Semantic Kernel ဟာ Azure OpenAI Service, Hugging Face ပေါ်မှာရှိတဲ့ open-source မော်ဒယ်တွေ၊ နဲ့ local မော်ဒယ်တွေကို အထွေထွေထောက်ပံ့ပေးပါတယ်။
အခြားနည်းလမ်းအနေနဲ့ [Ollama](https://ollama.com) သို့မဟုတ် [LlamaEdge](https://llamaedge.com) ကိုအသုံးပြုပြီး quantized မော်ဒယ်တွေကိုခေါ်နိုင်ပါတယ်။ Ollama ဟာ တစ်ဦးချင်းသုံးစွဲသူတွေကို quantized မော်ဒယ်မျိုးစုံခေါ်ရန် အခွင့်အလမ်းပေးပြီး၊ LlamaEdge က GGUF မော်ဒယ်တွေအတွက် cross-platform ပံ့ပိုးမှုပေးပါတယ်။

## **Quantized မော်ဒယ်များ:**
သုံးစွဲသူအများစုဟာ local inference အတွက် quantized မော်ဒယ်တွေကို သဘောကျစွာအသုံးပြုကြပါတယ်။ ဥပမာအားဖြင့် Ollama run Phi-3 ကိုတိုက်ရိုက် chạy သို့မဟုတ် Modelfile သုံးပြီး offline မှာ configure လုပ်နိုင်ပါတယ်။ Modelfile မှာ GGUF ဖိုင်လမ်းကြောင်းနဲ့ prompt format ကို သတ်မှတ်ပေးထားပါတယ်။

## **Generative AI ရဲ့ အခွင့်အလမ်းများ:**
Phi-3-mini လို SLMs တွေကို ပေါင်းစပ်အသုံးပြုခြင်းက Generative AI ရဲ့ အခွင့်အလမ်းအသစ်တွေကို ဖွင့်လှစ်ပေးပါတယ်။ Inference က စတင်ခြင်းသာဖြစ်ပြီး၊ ဒီမော်ဒယ်တွေကို အရင်းအမြစ်အကန့်အသတ်၊ latency-bound နဲ့ cost-constrained အခြေအနေတွေမှာ အမျိုးမျိုးအသုံးချနိုင်ပါတယ်။

## **Phi-3-mini နဲ့ Generative AI ကိုဖွင့်လှစ်ခြင်း: Inference နဲ့ Deployment လမ်းညွှန်**
Semantic Kernel, Ollama/LlamaEdge နဲ့ ONNX Runtime ကိုအသုံးပြုပြီး Phi-3-mini မော်ဒယ်တွေကို ရယူပြီး inference လုပ်နည်း၊ Generative AI ရဲ့ အခွင့်အလမ်းတွေကို အမျိုးမျိုးသော အက်ပလီကေးရှင်းအခြေအနေများတွင် ရှာဖွေပါ။

**Features**
Phi-3-mini မော်ဒယ်ကို အောက်ပါနေရာများတွင် inference လုပ်နိုင်ပါသည် -

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

အကျဉ်းချုပ်အနေနဲ့ Phi-3-mini ဟာ developer တွေကို မော်ဒယ် format မျိုးစုံကို စမ်းသပ်ခွင့်ပေးပြီး၊ Generative AI ကို အမျိုးမျိုးသော အက်ပလီကေးရှင်းအခြေအနေများတွင် အသုံးချနိုင်စေပါတယ်။

It seems like you want the text translated into "mo." Could you please clarify what "mo" refers to? Are you referring to a specific language or dialect?