<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:55:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "my"
}
-->
# **Microsoft Phi-3.5 tflite ကို အသုံးပြုပြီး Android app ဖန်တီးခြင်း**

ဤသည်မှာ Microsoft Phi-3.5 tflite မော်ဒယ်များကို အသုံးပြုထားသည့် Android နမူနာဖြစ်သည်။

## **📚 သိရှိရန်**

Android LLM Inference API သည် Android အက်ပလီကေးရှင်းများအတွက် အပြည့်အဝ on-device တွင် အကြီးစားဘာသာစကားမော်ဒယ်များ (LLMs) ကို လည်ပတ်နိုင်စေပြီး၊ စာသားဖန်တီးခြင်း၊ သဘာဝဘာသာစကားဖြင့် သတင်းအချက်အလက် ရယူခြင်း၊ စာရွက်စာတမ်းများကို အကျဉ်းချုပ်ခြင်းကဲ့သို့သော အလုပ်များစွာကို ဆောင်ရွက်နိုင်သည်။ ဤအလုပ်သည် စာသားမှ စာသားသို့ အကြီးစားဘာသာစကားမော်ဒယ်များစွာကို built-in အထောက်အပံ့ပေးထားသဖြင့် နောက်ဆုံးပေါ် on-device generative AI မော်ဒယ်များကို သင့် Android အက်ပလီကေးရှင်းများတွင် အသုံးပြုနိုင်သည်။

Google AI Edge Torch သည် PyTorch မော်ဒယ်များကို .tflite ဖော်မတ်သို့ ပြောင်းလဲပေးနိုင်သော python စာကြည့်တိုက်ဖြစ်ပြီး၊ ထိုဖိုင်များကို TensorFlow Lite နှင့် MediaPipe ဖြင့် လည်ပတ်နိုင်သည်။ ၎င်းသည် Android, iOS နှင့် IoT အက်ပလီကေးရှင်းများအတွက် မော်ဒယ်များကို အပြည့်အဝ on-device တွင် လည်ပတ်စေသည်။ AI Edge Torch သည် CPU များအတွက် ကျယ်ပြန့်သော အထောက်အပံ့ရှိပြီး၊ စတင်အနေဖြင့် GPU နှင့် NPU ကိုလည်း ထောက်ပံ့ပေးသည်။ AI Edge Torch သည် PyTorch နှင့် နီးကပ်စွာ ပေါင်းစည်းရန် ရည်ရွယ်ကာ torch.export() အပေါ်တွင် တည်ဆောက်ပြီး Core ATen operator များကို ကောင်းစွာ ထောက်ပံ့ပေးသည်။

## **🪬 လမ်းညွှန်ချက်**

### **🔥 Microsoft Phi-3.5 ကို tflite သို့ ပြောင်းလဲခြင်း**

0. ဤနမူနာသည် Android 14+ အတွက်ဖြစ်သည်။

1. Python 3.10.12 ကို 설치ပါ။

***အကြံပြုချက်:*** conda ကို အသုံးပြု၍ Python ပတ်ဝန်းကျင်ကို 설치ပါ။

2. Ubuntu 20.04 / 22.04 (ကျေးဇူးပြု၍ [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) ကို အထူးဂရုစိုက်ပါ)

***အကြံပြုချက်:*** Azure Linux VM သို့မဟုတ် တတိယပါတီ cloud vm ကို အသုံးပြု၍ ပတ်ဝန်းကျင်ဖန်တီးပါ။

3. Linux bash သို့ သွား၍ Python စာကြည့်တိုက်ကို 설치ပါ။

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face မှ Microsoft-3.5-Instruct ကို ဒေါင်းလုပ်လုပ်ပါ။

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 ကို tflite သို့ ပြောင်းပါ။

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 ကို Android Mediapipe Bundle သို့ ပြောင်းခြင်း**

ပထမဦးဆုံး mediapipe ကို 설치ပါ။

```bash

pip install mediapipe

```

ဤကုဒ်ကို [သင့် notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) တွင် လည်ပတ်ပါ။

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 adb push ဖြင့် မော်ဒယ်ကို သင့် Android စက်များ၏ လမ်းကြောင်းသို့ ပို့ခြင်း**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 သင့် Android ကုဒ်ကို လည်ပတ်ခြင်း**

![demo](../../../../../../translated_images/my/demo.06d5a4246f057d1b.png)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။