<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:46:12+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "my"
}
-->
# **Nvidia Jetson တွင် Phi-3 အာရုံစူးစိုက်မှု**

Nvidia Jetson သည် Nvidia မှ ထုတ်လုပ်သော embedded computing board များ စီးရီးဖြစ်သည်။ Jetson TK1, TX1 နှင့် TX2 မော်ဒယ်များတွင် Nvidia ၏ Tegra processor (သို့) SoC တစ်ခုပါဝင်ပြီး ARM architecture အခြေခံ CPU ကို ထည့်သွင်းထားသည်။ Jetson သည် စွမ်းအင်သက်သာပြီး machine learning application များကို မြန်ဆန်စွာ ဆောင်ရွက်ရန် ရည်ရွယ်ထားသော စနစ်ဖြစ်သည်။ Nvidia Jetson ကို စက်မှုလုပ်ငန်းအမျိုးမျိုးတွင် ထူးခြားသော AI ထုတ်ကုန်များ ဖန်တီးရန် ပရော်ဖက်ရှင်နယ် developer များ အသုံးပြုကြပြီး ကျောင်းသားများနှင့် စိတ်ဝင်စားသူများကလည်း လက်တွေ့ AI သင်ယူမှုနှင့် စိတ်ဝင်စားဖွယ် project များ ဖန်တီးရာတွင် အသုံးပြုကြသည်။ SLM ကို Jetson ကဲ့သို့သော edge device များတွင် တပ်ဆင်ထားပြီး စက်မှုလုပ်ငန်း generative AI application များကို ပိုမိုကောင်းမွန်စွာ အကောင်အထည်ဖော်နိုင်စေသည်။

## NVIDIA Jetson တွင် တပ်ဆင်ခြင်း
အလိုအလျောက် ရုပ်ရှင်စက်များနှင့် embedded device များပေါ်တွင် အလုပ်လုပ်နေသော developer များသည် Phi-3 Mini ကို အသုံးပြုနိုင်သည်။ Phi-3 ၏ အရွယ်အစား သေးငယ်မှုကြောင့် edge deployment အတွက် အထူးသင့်တော်သည်။ သင်ကြားမှုအတွင်း parameter များကို ဂရုစိုက်စွာ ချိန်ညှိထားပြီး တုံ့ပြန်မှုများတွင် တိကျမှန်ကန်မှု မြင့်မားစေသည်။

### TensorRT-LLM အဆင့်မြှင့်တင်ခြင်း
NVIDIA ၏ [TensorRT-LLM library](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) သည် ဘာသာစကား မော်ဒယ်ကြီးများ၏ inference ကို အထူးပြု optimize လုပ်ပေးသည်။ Phi-3 Mini ၏ context window ကြီးရှည်မှုကို ထောက်ပံ့ကာ throughput နှင့် latency နှစ်ခုလုံးကို တိုးတက်စေသည်။ အဆင့်မြှင့်တင်မှုများတွင် LongRoPE, FP8 နှင့် inflight batching ကဲ့သို့သော နည်းပညာများ ပါဝင်သည်။

### ရရှိနိုင်မှုနှင့် တပ်ဆင်ခြင်း
Developer များသည် 128K context window ပါသော Phi-3 Mini ကို [NVIDIA ၏ AI စာမျက်နှာ](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) တွင် စမ်းသပ်လေ့လာနိုင်သည်။ ၎င်းကို NVIDIA NIM အဖြစ် ထုပ်ပိုးထားပြီး မည်သည့်နေရာတွင်မဆို တပ်ဆင်နိုင်သော standard API ပါသော microservice တစ်ခုဖြစ်သည်။ ထို့အပြင် [TensorRT-LLM ၏ GitHub တွင် ရှိသော implementation များ](https://github.com/NVIDIA/TensorRT-LLM) ကိုလည်း ကြည့်ရှုနိုင်သည်။

## **1. ပြင်ဆင်မှု**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Jetson တွင် Phi-3 ကို လည်ပတ်ခြင်း**

[Ollama](https://ollama.com) သို့မဟုတ် [LlamaEdge](https://llamaedge.com) ကို ရွေးချယ်အသုံးပြုနိုင်သည်။

cloud နှင့် edge device များတွင် gguf ကို တပြိုင်နက် အသုံးပြုလိုပါက LlamaEdge ကို WasmEdge အဖြစ် နားလည်နိုင်သည် (WasmEdge သည် cloud native, edge နှင့် decentralized application များအတွက် သင့်တော်သော အလေးချိန်နည်း၊ မြန်ဆန်ပြီး တိုးချဲ့နိုင်သော WebAssembly runtime ဖြစ်သည်။ serverless application များ၊ embedded function များ၊ microservice များ၊ smart contract များနှင့် IoT device များကို ထောက်ပံ့သည်။ gguf ၏ quantitative model ကို LlamaEdge မှတဆင့် edge device များနှင့် cloud တွင် တပ်ဆင်နိုင်သည်)။

![llamaedge](../../../../../translated_images/my/llamaedge.e9d6ff96dff11cf7.jpg)

အသုံးပြုရန် အဆင့်များမှာ

1. ဆက်စပ် library များနှင့် ဖိုင်များကို ထည့်သွင်းဒေါင်းလုပ်လုပ်ပါ

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**မှတ်ချက်**: llama-api-server.wasm နှင့် chatbot-ui ကို တူညီသော ဖိုင်လ်ဒါတွင်ထားရန် လိုအပ်သည်

2. terminal တွင် script များကို လည်ပတ်ပါ

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

အောက်တွင် လည်ပတ်မှုရလဒ်ကို မြင်ရမည်

![llamaedgerun](../../../../../translated_images/my/llamaedgerun.bed921516c9a821c.png)

***နမူနာကုဒ်*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

အကျဉ်းချုပ်အားဖြင့် Phi-3 Mini သည် ဘာသာစကား မော်ဒယ်တစ်ခုအနေဖြင့် ထိရောက်မှု၊ context ကို နားလည်မှုနှင့် NVIDIA ၏ optimization အားကို ပေါင်းစပ်ထားသော တိုးတက်မှုကြီးတစ်ခုဖြစ်သည်။ ရုပ်ရှင်စက်များ သို့မဟုတ် edge application များ တည်ဆောက်ရာတွင် Phi-3 Mini သည် သိထားသင့်သော အင်အားကြီးကိရိယာတစ်ခုဖြစ်သည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။