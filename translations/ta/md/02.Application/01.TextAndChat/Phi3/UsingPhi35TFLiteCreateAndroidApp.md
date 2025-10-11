<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-10-11T12:06:07+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ta"
}
-->
# **Microsoft Phi-3.5 tflite பயன்படுத்தி Android பயன்பாட்டை உருவாக்குதல்**

இது Microsoft Phi-3.5 tflite மாதிரிகளைப் பயன்படுத்தும் Android மாதிரி.

## **📚 அறிவு**

Android LLM Inference API மூலம் Android பயன்பாடுகளுக்காக பெரிய மொழி மாதிரிகளை (LLMs) முழுவதும் சாதனத்தில் இயக்க முடியும். இதை நீங்கள் பல்வேறு பணிகளைச் செய்ய பயன்படுத்தலாம், உதாரணமாக உரை உருவாக்குதல், இயற்கை மொழி வடிவத்தில் தகவல்களை பெறுதல், மற்றும் ஆவணங்களை சுருக்குதல். இந்த பணிக்கான ஆதரவு பல உரை-உரைக்கு பெரிய மொழி மாதிரிகளுக்கு உள்ளடக்கமாக வழங்கப்படுகிறது, எனவே நீங்கள் சமீபத்திய சாதனத்தில் இயங்கும் Generative AI மாதிரிகளை உங்கள் Android பயன்பாடுகளில் பயன்படுத்தலாம்.

Google AI Edge Torch என்பது PyTorch மாதிரிகளை .tflite வடிவமாக மாற்றுவதற்கு ஆதரவு வழங்கும் Python நூலகமாகும், இதை TensorFlow Lite மற்றும் MediaPipe உடன் இயக்க முடியும். இது Android, iOS மற்றும் IoT பயன்பாடுகளுக்கு முழுவதும் சாதனத்தில் இயங்கும் மாதிரிகளை இயக்க அனுமதிக்கிறது. AI Edge Torch பரந்த CPU ஆதரவை வழங்குகிறது, ஆரம்ப GPU மற்றும் NPU ஆதரவு உடன். AI Edge Torch PyTorch உடன் நெருக்கமாக ஒருங்கிணைக்க முயற்சிக்கிறது, torch.export() மேல் கட்டமைக்கிறது மற்றும் Core ATen இயக்கிகளுக்கு நல்ல ஆதரவை வழங்குகிறது.

## **🪬 வழிகாட்டுதல்**

### **🔥 Microsoft Phi-3.5 ஐ tflite ஆதரவாக மாற்றுதல்**

0. இந்த மாதிரி Android 14+ க்காக.

1. Python 3.10.12 ஐ நிறுவவும்

***பரிந்துரை:*** உங்கள் Python சூழலை நிறுவ conda பயன்படுத்தவும்

2. Ubuntu 20.04 / 22.04 (தயவுசெய்து [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) மீது கவனம் செலுத்தவும்)

***பரிந்துரை:*** Azure Linux VM அல்லது 3rd party cloud vm ஐ உங்கள் சூழலை உருவாக்க பயன்படுத்தவும்

3. உங்கள் Linux bash க்கு சென்று Python நூலகத்தை நிறுவவும் 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face இல் இருந்து Microsoft-3.5-Instruct ஐ பதிவிறக்கவும்

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 ஐ tflite ஆக மாற்றவும்

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Microsoft Phi-3.5 ஐ Android Mediapipe Bundle ஆக மாற்றுதல்**

முதலில் mediapipe ஐ நிறுவவும்

```bash

pip install mediapipe

```

இந்த குறியீட்டை [உங்கள் நோட்புக்](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) இல் இயக்கவும்

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


### **🔥 adb push task மாதிரியை உங்கள் Android சாதனத்தின் பாதையில் அனுப்புதல்**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 உங்கள் Android குறியீட்டை இயக்குதல்**

![demo](../../../../../../imgs/02/android-tf/demo.png)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்சிறப்பிற்காக முயற்சி செய்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.