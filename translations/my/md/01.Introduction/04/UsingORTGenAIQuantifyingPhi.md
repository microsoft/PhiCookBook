<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-09T19:44:38+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "my"
}
-->
## **Model Builder ကို အသုံးပြုပြီး Phi-3.5 ကို Quantize လုပ်နည်း**

Model Builder သည် ယခုအခါ Phi-3.5 Instruct နှင့် Phi-3.5-Vision အတွက် ONNX မော်ဒယ် Quantization ကို ထောက်ပံ့ပေးပါသည်။

### **Phi-3.5-Instruct**

**CPU ဖြင့် အမြန်ပြောင်းလဲနိုင်သော INT4 Quantized Conversion**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ဖြင့် အမြန်ပြောင်းလဲနိုင်သော INT4 Quantized Conversion**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Terminal တွင် ပတ်ဝန်းကျင်ကို သတ်မှတ်ပါ

```bash

mkdir models

cd models 

```

2. models ဖိုလ်ဒါအတွင်း microsoft/Phi-3.5-vision-instruct ကို ဒေါင်းလုပ်လုပ်ပါ  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. အောက်ပါဖိုင်များကို သင့် Phi-3.5-vision-instruct ဖိုလ်ဒါထဲသို့ ဒေါင်းလုပ်လုပ်ပါ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ဒီဖိုင်ကို models ဖိုလ်ဒါထဲ ဒေါင်းလုပ်လုပ်ပါ  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Terminal သို့ သွားပါ

    FP32 ဖြင့် ONNX ထောက်ပံ့မှု ပြောင်းလဲပါ

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **မှတ်ချက်**

1. Model Builder သည် လက်ရှိတွင် Phi-3.5-Instruct နှင့် Phi-3.5-Vision မော်ဒယ်များကိုသာ ပြောင်းလဲပေးနိုင်ပြီး Phi-3.5-MoE ကို မထောက်ပံ့သေးပါ။

2. ONNX ၏ quantized မော်ဒယ်ကို အသုံးပြုလိုပါက Generative AI extensions for onnxruntime SDK မှတဆင့် အသုံးပြုနိုင်ပါသည်။

3. ပိုမိုတာဝန်ရှိသော AI ဖြစ်စေရန် မော်ဒယ် Quantization ပြောင်းလဲပြီးနောက် ထိရောက်သော ရလဒ်စမ်းသပ်မှုများ ပြုလုပ်ရန် အကြံပြုပါသည်။

4. CPU INT4 မော်ဒယ်ကို Quantize လုပ်ခြင်းဖြင့် Edge Device များတွင် တပ်ဆင်နိုင်ပြီး အသုံးပြုမှုအခြေအနေများ ပိုမိုကောင်းမွန်သည့်အတွက် Phi-3.5-Instruct ကို INT4 အခြေခံပြီး ပြီးစီးထားပါသည်။

## **အရင်းအမြစ်များ**

1. Generative AI extensions for onnxruntime အကြောင်း ပိုမိုလေ့လာရန် [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။