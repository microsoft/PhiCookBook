<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-07T14:51:43+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **Quantizing Phi Family using llama.cpp**

## **What's llama.cpp**

llama.cpp သည် C++ ဖြင့်ရေးသားထားသော open-source software library တစ်ခုဖြစ်ပြီး Llama ကဲ့သို့သော အကြီးစား ဘာသာစကားမော်ဒယ်များ (LLMs) တွင် inference ပြုလုပ်ရန် အသုံးပြုသည်။ ၎င်း၏ အဓိကရည်ရွယ်ချက်မှာ hardware မျိုးစုံတွင် setup နည်းနည်းဖြင့် LLM inference အတွက် နောက်ဆုံးပေါ် စွမ်းဆောင်ရည်ကို ပေးနိုင်ရန်ဖြစ်သည်။ ထို့အပြင် Python bindings များလည်း ရရှိနိုင်ပြီး၊ text completion အတွက် high-level API နှင့် OpenAI နှင့် ကိုက်ညီသော web server ကို ပံ့ပိုးပေးသည်။

llama.cpp ၏ အဓိကရည်ရွယ်ချက်မှာ hardware မျိုးစုံတွင် မိမိ device တွင် သို့မဟုတ် cloud ပေါ်တွင် setup နည်းနည်းဖြင့် နောက်ဆုံးပေါ် စွမ်းဆောင်ရည်ဖြင့် LLM inference ပြုလုပ်နိုင်ရန်ဖြစ်သည်။

- အခြေခံ C/C++ ဖြင့် dependencies မလိုအပ်ဘဲ အကောင်အထည်ဖော်ထားခြင်း
- Apple silicon ကို ပထမတန်းစား အနေဖြင့် ARM NEON, Accelerate နှင့် Metal frameworks များဖြင့် အထူးပြု optimize ပြုလုပ်ထားခြင်း
- x86 architecture များအတွက် AVX, AVX2 နှင့် AVX512 ပံ့ပိုးမှု
- inference လျင်မြန်စေရန်နှင့် memory သုံးစွဲမှု လျော့နည်းစေရန် 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, နှင့် 8-bit integer quantization များ
- NVIDIA GPU များတွင် LLM များကို လည်ပတ်စေသော custom CUDA kernels (AMD GPU များအတွက် HIP ဖြင့် ပံ့ပိုးမှု)
- Vulkan နှင့် SYCL backend ပံ့ပိုးမှု
- VRAM စွမ်းရည်ကျော်မည့် မော်ဒယ်များအတွက် CPU+GPU hybrid inference ဖြင့် အချို့အပိုင်းများကို အမြန်ပြုလုပ်နိုင်ခြင်း

## **Quantizing Phi-3.5 with llama.cpp**

Phi-3.5-Instruct မော်ဒယ်ကို llama.cpp ဖြင့် quantize ပြုလုပ်နိုင်သော်လည်း Phi-3.5-Vision နှင့် Phi-3.5-MoE များကို မထောက်ပံ့သေးပါ။ llama.cpp မှ ပြောင်းလဲသည့် format သည် gguf ဖြစ်ပြီး၊ quantization အတွက် အများဆုံး အသုံးပြုသော format ဖြစ်သည်။

Hugging face တွင် quantized GGUF format မော်ဒယ်များ အများအပြား ရှိသည်။ AI Foundry, Ollama နှင့် LlamaEdge များသည် llama.cpp ကို အခြေခံထားပြီး GGUF မော်ဒယ်များကိုလည်း မကြာခဏ အသုံးပြုကြသည်။

### **What's GGUF**

GGUF သည် မော်ဒယ်များကို လျင်မြန်စွာ load နှင့် save ပြုလုပ်ရန် အထူး optimize ပြုလုပ်ထားသော binary format ဖြစ်ပြီး inference အတွက် ထူးခြားစွာ ထိရောက်သည်။ GGUF သည် GGML နှင့် အခြား executor များတွင် အသုံးပြုရန် ရည်ရွယ်ထားသည်။ GGUF ကို llama.cpp ၏ ဖန်တီးသူ @ggerganov က ဖန်တီးခဲ့ပြီး llama.cpp သည် C/C++ LLM inference framework အဖြစ် နာမည်ကြီးသည်။ PyTorch ကဲ့သို့သော framework များတွင် ဖန်တီးထားသော မော်ဒယ်များကို GGUF format သို့ ပြောင်းလဲ၍ အသုံးပြုနိုင်သည်။

### **ONNX vs GGUF**

ONNX သည် ရိုးရာ machine learning/deep learning format တစ်ခုဖြစ်ပြီး AI Framework များစွာတွင် ကောင်းစွာ ထောက်ပံ့ထားပြီး edge device များတွင် အသုံးပြုမှု ကောင်းမွန်သည်။ GGUF သည် llama.cpp အခြေခံပြီး GenAI ခေတ်တွင် ဖန်တီးထားသော format ဖြစ်သည်။ နှစ်ခုစလုံး အသုံးပြုမှုများ ဆင်တူသည်။ embedded hardware နှင့် application layer များတွင် ပိုမိုကောင်းမွန်သော စွမ်းဆောင်ရည်လိုလျှင် ONNX ကို ရွေးချယ်နိုင်သည်။ llama.cpp ၏ derivative framework နှင့် နည်းပညာများကို အသုံးပြုလျှင် GGUF သည် ပိုမိုသင့်တော်သည်။

### **Quantization Phi-3.5-Instruct using llama.cpp**

**1. Environment Configuration**


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

Phi-3.5 ကို INT4 သို့ quantize ပြုလုပ်ခြင်း


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testing**

llama-cpp-python ကို 설치


```bash

pip install llama-cpp-python -U

```

***Note*** 

Apple Silicon ကို အသုံးပြုပါက llama-cpp-python ကို ဒီလို 설치ပါ


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

စမ်းသပ်ခြင်း 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resources**

1. llama.cpp အကြောင်းပိုမိုလေ့လာရန် [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntime အကြောင်းပိုမိုလေ့လာရန် [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUF အကြောင်းပိုမိုလေ့လာရန် [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.