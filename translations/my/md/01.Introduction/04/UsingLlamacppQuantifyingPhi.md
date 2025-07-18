<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-07-16T22:13:00+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "my"
}
-->
# **llama.cpp ကို အသုံးပြုပြီး Phi မိသားစုကို Quantize လုပ်ခြင်း**

## **llama.cpp ဆိုတာဘာလဲ**

llama.cpp သည် C++ ဖြင့်ရေးသားထားသော open-source ဆော့ဖ်ဝဲစာကြည့်တိုက်တစ်ခုဖြစ်ပြီး Llama ကဲ့သို့သော အကြီးစားဘာသာစကားမော်ဒယ်များ (LLMs) တွင် inference လုပ်ဆောင်ပေးသည်။ ၎င်း၏ အဓိကရည်ရွယ်ချက်မှာ hardware မျိုးစုံပေါ်တွင် အနည်းဆုံးပြင်ဆင်မှုဖြင့် LLM inference အတွက် အဆင့်မြင့်စွမ်းဆောင်ရည်ကို ပေးစွမ်းခြင်းဖြစ်သည်။ ထို့အပြင် Python bindings များလည်း ရရှိနိုင်ပြီး၊ ၎င်းတို့က စာသားဖြည့်စွက်ခြင်းအတွက် အဆင့်မြင့် API နှင့် OpenAI ကိုက်ညီသော web server ကို ပံ့ပိုးပေးသည်။

llama.cpp ၏ အဓိကရည်ရွယ်ချက်မှာ hardware မျိုးစုံပေါ်တွင် အနည်းဆုံးပြင်ဆင်မှုဖြင့် LLM inference ကို ဒေသတွင်းနှင့် cloud ပေါ်တွင် state-of-the-art စွမ်းဆောင်ရည်ဖြင့် လုပ်ဆောင်နိုင်စေရန်ဖြစ်သည်။

- မည်သည့် dependency မပါသော ရိုးရှင်းသော C/C++ အကောင်အထည်ဖော်မှု
- Apple silicon ကို အထူးဂရုစိုက်ထားပြီး ARM NEON, Accelerate နှင့် Metal frameworks များဖြင့် အကောင်းဆုံး optimize လုပ်ထားသည်
- x86 architecture များအတွက် AVX, AVX2 နှင့် AVX512 ပံ့ပိုးမှု
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit နှင့် 8-bit integer quantization များဖြင့် inference မြန်ဆန်စေပြီး memory အသုံးပြုမှုလျော့နည်းစေခြင်း
- NVIDIA GPU များတွင် LLM များကို လည်ပတ်စေသော custom CUDA kernels (AMD GPU များအတွက် HIP ဖြင့် ပံ့ပိုးမှု)
- Vulkan နှင့် SYCL backend ပံ့ပိုးမှု
- CPU+GPU ပေါင်းစပ် inference ဖြင့် VRAM စွမ်းဆောင်ရည်ထက် ကြီးမားသော မော်ဒယ်များကို အပိုင်းအစမြန်ဆန်စေခြင်း

## **llama.cpp ဖြင့် Phi-3.5 ကို Quantize လုပ်ခြင်း**

Phi-3.5-Instruct မော်ဒယ်ကို llama.cpp ဖြင့် quantize လုပ်နိုင်သော်လည်း Phi-3.5-Vision နှင့် Phi-3.5-MoE များကို မထောက်ပံ့သေးပါ။ llama.cpp က ပြောင်းလဲပေးသော ဖိုင်ဖော်မတ်မှာ gguf ဖြစ်ပြီး၊ ၎င်းသည် အများဆုံးအသုံးပြုသော quantization ဖော်မတ်လည်း ဖြစ်သည်။

Hugging face တွင် quantized GGUF ဖော်မတ် မော်ဒယ်များစွာ ရှိသည်။ AI Foundry, Ollama နှင့် LlamaEdge များသည် llama.cpp ကို အခြေခံထားသောကြောင့် GGUF မော်ဒယ်များကိုလည်း မကြာခဏ အသုံးပြုကြသည်။

### **GGUF ဆိုတာဘာလဲ**

GGUF သည် မော်ဒယ်များကို မြန်ဆန်စွာ load နှင့် save လုပ်နိုင်ရန် optimized လုပ်ထားသော binary ဖော်မတ်ဖြစ်ပြီး inference အတွက် ထိရောက်မှုမြင့်သည်။ GGUF ကို GGML နှင့် အခြား executor များတွင် အသုံးပြုရန် ဒီဇိုင်းဆွဲထားသည်။ GGUF ကို llama.cpp ၏ ဖန်တီးသူ @ggerganov က ဖန်တီးခဲ့ပြီး၊ llama.cpp သည် လူကြိုက်များသော C/C++ LLM inference framework တစ်ခုဖြစ်သည်။ PyTorch ကဲ့သို့သော framework များတွင် ဖန်တီးထားသော မော်ဒယ်များကို GGUF ဖော်မတ်သို့ ပြောင်းလဲ၍ အသုံးပြုနိုင်သည်။

### **ONNX နှင့် GGUF**

ONNX သည် ရိုးရာ machine learning/deep learning ဖော်မတ်ဖြစ်ပြီး AI Framework များစွာတွင် ကောင်းမွန်စွာ ပံ့ပိုးထားပြီး edge device များတွင် အသုံးပြုမှုကောင်းသည်။ GGUF သည် llama.cpp အခြေခံပြီး GenAI ခေတ်တွင် ဖန်တီးထားသော ဖော်မတ်ဖြစ်သည်။ နှစ်ခုစလုံး အသုံးပြုမှုများမှာ ဆင်တူသည်။ embedded hardware နှင့် application layer များတွင် ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည်လိုလျှင် ONNX ကို ရွေးချယ်နိုင်သည်။ llama.cpp ၏ derivative framework နှင့် နည်းပညာများကို အသုံးပြုမည်ဆိုလျှင် GGUF သည် ပိုမိုသင့်တော်သည်။

### **llama.cpp ဖြင့် Phi-3.5-Instruct ကို Quantize လုပ်ခြင်း**

**1. ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

llama.cpp ကို အသုံးပြုပြီး Phi-3.5-Instruct ကို FP16 GGUF သို့ ပြောင်းလဲခြင်း


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 ကို INT4 သို့ Quantize လုပ်ခြင်း


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. စမ်းသပ်ခြင်း**

llama-cpp-python ကို 설치 လုပ်ပါ


```bash

pip install llama-cpp-python -U

```

***မှတ်ချက်***

Apple Silicon ကို အသုံးပြုပါက llama-cpp-python ကို အောက်ပါအတိုင်း 설치 လုပ်ပါ


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

စမ်းသပ်ခြင်း


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **အရင်းအမြစ်များ**

1. llama.cpp အကြောင်း ပိုမိုလေ့လာရန် [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime အကြောင်း ပိုမိုလေ့လာရန် [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF အကြောင်း ပိုမိုလေ့လာရန် [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။