<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-07T14:07:53+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "mo"
}
-->
# **استعمال Microsoft Phi-3.5 tflite کے ذریعے Android ایپ بنانا**

یہ ایک Android سیمپل ہے جو Microsoft Phi-3.5 tflite ماڈلز استعمال کرتا ہے۔

## **📚 معلومات**

Android LLM Inference API آپ کو بڑے زبان کے ماڈلز (LLMs) کو مکمل طور پر ڈیوائس پر چلانے کی سہولت دیتا ہے، جس سے آپ مختلف قسم کے کام انجام دے سکتے ہیں، جیسے کہ متن تیار کرنا، قدرتی زبان میں معلومات حاصل کرنا، اور دستاویزات کا خلاصہ بنانا۔ یہ ٹاسک متعدد text-to-text بڑے زبان کے ماڈلز کی بلٹ ان سپورٹ فراہم کرتا ہے، تاکہ آپ جدید on-device generative AI ماڈلز کو اپنی Android ایپس میں استعمال کر سکیں۔

Google AI Edge Torch ایک پائتھن لائبریری ہے جو PyTorch ماڈلز کو .tflite فارمیٹ میں تبدیل کرنے کی حمایت کرتی ہے، جسے پھر TensorFlow Lite اور MediaPipe کے ساتھ چلایا جا سکتا ہے۔ یہ Android، iOS اور IoT ایپلیکیشنز کے لیے ہے جو ماڈلز کو مکمل طور پر ڈیوائس پر چلانے کی صلاحیت رکھتی ہیں۔ AI Edge Torch وسیع CPU سپورٹ فراہم کرتا ہے، اور ابتدائی GPU اور NPU سپورٹ بھی شامل ہے۔ AI Edge Torch PyTorch کے ساتھ قریبی انضمام کا مقصد رکھتا ہے، torch.export() کے اوپر بنایا گیا ہے اور Core ATen آپریٹرز کی اچھی کوریج فراہم کرتا ہے۔

## **🪬 رہنما اصول**

### **🔥 Microsoft Phi-3.5 کو tflite میں تبدیل کرنا**

0. یہ سیمپل Android 14+ کے لیے ہے۔

1. Python 3.10.12 انسٹال کریں۔

***تجویز:*** conda استعمال کر کے Python ماحول انسٹال کریں۔

2. Ubuntu 20.04 / 22.04 (براہ کرم [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) پر توجہ دیں)

***تجویز:*** Azure Linux VM یا کسی 3rd پارٹی کلاؤڈ VM کا استعمال کریں تاکہ اپنا ماحول بنائیں۔

3. اپنے Linux bash میں جائیں اور Python لائبریری انسٹال کریں

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face سے Microsoft-3.5-Instruct ڈاؤن لوڈ کریں

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 کو tflite میں تبدیل کریں

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 کو Android Mediapipe Bundle میں تبدیل کرنا**

براہ کرم پہلے mediapipe انسٹال کریں

```bash

pip install mediapipe

```

اس کوڈ کو [اپنے نوٹ بک](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) میں چلائیں

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

### **🔥 adb push کے ذریعے ماڈل کو اپنے Android ڈیوائس کے راستے پر بھیجنا**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 اپنے Android کوڈ کو چلانا**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.mo.png)

**Disclaimer**:  
Dis dokument haz bin translaited yusing AI translait serviz [Co-op Translator](https://github.com/Azure/co-op-translator). Wile wi stryv for akyurasy, pleez bi awair dat otomaytid translaitions mey contain erors or inakurysez. Da orijinal dokument in its naytiv langwaj shud bi konsidrd da autoritativ sors. For kritikul informashun, profeshunal hyuman translaiton iz rekomended. Wi ar not laybl for eni misanderstandings or misinterpretashuns arising from da yus of dis translaiton.