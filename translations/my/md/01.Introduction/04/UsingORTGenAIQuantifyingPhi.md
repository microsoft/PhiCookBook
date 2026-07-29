# **onnxruntime အတွက် Generative AI ပြွန်များကို အသုံးပြု၍ Phi မိသားစုကို Quantizing ပြုလုပ်ခြင်း**

## **onnxruntime အတွက် Generative AI ပြွန်များ ဆိုတာဘာလဲ**

ဤပြွန်များသည် ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) နှင့် generative AI ကို အကောင်အထည်ဖော်ရန် အကူအညီပေးသည်။ ONNX မော်ဒယ်များအတွက် generative AI လုပ်ငန်းစဉ်ကို ပံ့ပိုးပေးပြီး ONNX Runtime ဖြင့် အနုတ်ယူခြင်း၊ logits အချက်အလက်များကို သုံးသပ်ခြင်း၊ ရှာဖွေမှုနှင့် စမ်းသပ်မှု၊ KV cache စီမံခန့်ခွဲမှုပေါင်းစပ်သည်။ ဖန်တီးသူများသည် generate() အဆင့်မြင့်နည်းလမ်းကို ခေါ်ယူနိုင်ပြီး မော်ဒယ်၏ အမျိုးမျိုး iteration များကို loop ဖြင့် တစ်ကြိမ်လျှင် တစ်ခုချင်း token များ ကို generate လုပ်နိုင်သည်။ loop အတွင်း generation parameters များကို လိုအပ်သလို ပြင်ဆင်နိုင်သည်။ greedy/beam search နှင့် TopP, TopK sampling ကို token စဉ်များ ဖန်တီးရာတွင် ပံ့ပိုးပေးပြီး repetitions အတွက် logits ကို ကျူးလွန်ဆန့်ကျင်ရေးများ ပါဝင်သည်။ သင်သည် custom scoring ကိုလည်း လွယ်ကူစွာ ထည့်သွင်းနိုင်သည်။

အပလီကေးရှင်းအဆင့်တွင် C++/ C# / Python အသုံးပြုပြီး onnxruntime အတွက် Generative AI ပြွန်များဖြင့် အပလီကေးရှင်းများ ဖန်တီးနိုင်သည်။ မော်ဒယ်အဆင့်တွင် fine-tuned မော်ဒယ်များကို ပေါင်းစပ်ပြီး သက်ဆိုင်ရာ quantitative deployment လုပ်ငန်းများ ဆောင်ရွက်နိုင်သည်။


## **onnxruntime အတွက် Generative AI ပြွန်များဖြင့် Phi-3.5 Quantizing ပြုလုပ်ခြင်း**

### **ပံ့ပိုးမော်ဒယ်များ**

onnxruntime အတွက် Generative AI ပြွန်များတွင် Microsoft Phi၊ Google Gemma, Mistral, Meta LLaMA မော်ဒယ်များ၏ quantization conversion ကို ပံ့ပိုးပေးသည်။


### **onnxruntime အတွက် Generative AI ပြွန်များအတွင်း Model Builder**

Model Builder သည် ONNX Runtime generate() API နှင့် လုပ်ဆောင်နိုင်သည့် optimized နှင့် quantized ONNX မော်ဒယ်များ ဖန်တီးခြင်းကို အလွန်မြန်ဆန်စေသည်။

Model Builder မှတဆင့် မော်ဒယ်ကို INT4, INT8, FP16, FP32 အဖြစ် quantize ပြုလုပ်နိုင်ပြီး CPU, CUDA, DirectML, Mobile စသည့် hardware acceleration နည်းလမ်းများပေါင်းစပ် အသုံးပြုနိုင်သည်။

Model Builder အသုံးပြုရန်အတွက် သင်သည် အောက်ပါအတိုင်း ထည့်သွင်းရပါမည်

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ထည့်သွင်းပြီးနောက် terminal မှ Model Builder script ကို chạy၍ မော်ဒယ်ဖော်မတ်နှင့် quantization conversion ပြုလုပ်နိုင်သည်။


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

သက်ဆိုင်သော parameters များကိုနားလည်ပါ

၁။ **model_name** - Hugging face တွင်ရှိသည့် မော်ဒယ်အမည်ဖြစ်ပြီး microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct စသည်ဖြစ်နိုင်သည်။ သို့မဟုတ် မော်ဒယ်ကို သိမ်းထားသော လမ်းကြောင်းဖြစ်နိုင်သည်။

၂။ **path_to_output_folder** - Quantized ပြောင်းလဲပြီး သိမ်းဆည်းမည့် လမ်းကြောင်း

၃။ **execution_provider** - CPU, CUDA, DirectML ကဲ့သို့သော hardware acceleration support များ

၄။ **cache_dir_to_save_hf_files** - Hugging face မှ မော်ဒယ်ကို ဒေါင်းလုပ်လုပ်ပြီး ဒေသတွင်းသိုလှောင်သည့်နေရာ




***Note：*** <ul>onnxruntime အတွက် Generative AI ပြွန်များသည် အခုအချိန်တွင် တစိတ်တဒေ Preview အနေဖြင့် ရှိသော်လည်း Microsoft Olive တွင် အပေါင်းအခြားထည့်သွင်းပြီးဖြစ်ကာ၊ Microsoft Olive မှတဆင့် onnxruntime အတွက် Generative AI ပြွန်များ Model Builder လုပ်ဆောင်ချက်များကိုလည်း ခေါ်ယူအသုံးပြုနိုင်သည်။</ul>

## **Phi-3.5 ကို Quantizing ပြုလုပ်ရန် Model Builder ကို ဘယ်လိုအသုံးပြုမလဲ**

Model Builder သည် ယခု Phi-3.5 Instruct နှင့် Phi-3.5-Vision မော်ဒယ်များအတွက် ONNX မော်ဒယ် quantization ကို ပံ့ပိုးပေးသည်။

### **Phi-3.5-Instruct**


**CPU အားဖြင့် စတင်ကာ quantized INT4 conversion ပြုလုပ်ခြင်း**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA အားဖြင့် စတင်ကာ quantized INT4 conversion ပြုလုပ်ခြင်း**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

၁။ Terminal တွင် ပတ်ဝန်းကျင် ပြင်ဆင်ရန်  

```bash

mkdir models

cd models 

```

၂။ models ဖိုလ်ဒါတွင် microsoft/Phi-3.5-vision-instruct ကို ဒေါင်းလုပ်လုပ်ပါ  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

၃။ ဤဖိုင်များကို သင့် Phi-3.5-vision-instruct ဖိုလ်ဒါသို့ ဒေါင်းလုပ်လုပ်ပါ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


၄။ models ဖိုလ်ဒါသို့ ဤဖိုင်ကို ဒေါင်းလုပ်လုပ်ပါ  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

၅။ Terminal သို့ သွားပါ

    FP32 ဖြင့် ONNX ပံ့ပိုးမှုကို ပြောင်းလဲပါ


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **မှတ်ချက်：**

၁။ Model Builder သည် ယခုအခါ Phi-3.5-Instruct နှင့် Phi-3.5-Vision မော်ဒယ်များကိုသာ ပြောင်းလဲမှုများပံ့ပိုးပေးပြီး Phi-3.5-MoE မဟုတ်ပါ။

၂။ ONNX ၏ quantized မော်ဒယ်ကို onnxruntime အတွက် Generative AI ပြွန်များ SDK မှတဆင့် အသုံးပြုနိုင်သည်။

၃။ ပိုမို တာဝန်ရှိသော AI ကို စဉ်းစားရန်လိုအပ်သောကြောင့် မော်ဒယ် quantization ပြောင်းလဲခြင်းပြီးနောက် အကျိုးသက်ရောက်မှု အနည်းငယ်သော စစ်ဆေးချက်များ ဆောင်ရွက်သင့်သည်။

၄။ CPU INT4 မော်ဒယ်ကို quantizing ပြုလုပ်ခြင်းဖြင့် Edge Device သို့ deployment ပြုလုပ်နိုင်ပြီး အသုံးချရလဒ်ကောင်းမွန်သော အပလီကေးရှင်းများ ဖန်တီးနိုင်သည်။ ထို့ကြောင့် Phi-3.5-Instruct ကို INT4 ရှိသည့် ပုံစံပတ်ဝန်းကျင်တွင် ပြီးမြောက်ထားသည်။


## **အရင်းအမြစ်များ**

၁။ onnxruntime အတွက် Generative AI ပြွန်များ အကြောင်း ပိုမိုသိရှိရန် [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

၂။ onnxruntime အတွက် Generative AI ပြွန်များ GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->