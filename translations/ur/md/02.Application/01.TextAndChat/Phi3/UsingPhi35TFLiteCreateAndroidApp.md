<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:50:04+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ur"
}
-->
# **مائیکروسافٹ Phi-3.5 tflite استعمال کرتے ہوئے اینڈرائیڈ ایپ بنانا**

یہ مائیکروسافٹ Phi-3.5 tflite ماڈلز استعمال کرنے والا اینڈرائیڈ سیمپل ہے۔

## **📚 معلومات**

Android LLM Inference API آپ کو اینڈرائیڈ ایپلیکیشنز کے لیے بڑے زبان کے ماڈلز (LLMs) کو مکمل طور پر ڈیوائس پر چلانے کی سہولت دیتا ہے، جسے آپ مختلف کاموں کے لیے استعمال کر سکتے ہیں، جیسے متن تیار کرنا، قدرتی زبان میں معلومات حاصل کرنا، اور دستاویزات کا خلاصہ بنانا۔ یہ ٹاسک متعدد ٹیکسٹ ٹو ٹیکسٹ بڑے زبان کے ماڈلز کی بلٹ ان سپورٹ فراہم کرتا ہے، تاکہ آپ جدید ترین آن-ڈیوائس جنریٹو AI ماڈلز کو اپنی اینڈرائیڈ ایپس میں لاگو کر سکیں۔

Google AI Edge Torch ایک پائتھن لائبریری ہے جو PyTorch ماڈلز کو .tflite فارمیٹ میں تبدیل کرنے کی حمایت کرتی ہے، جسے پھر TensorFlow Lite اور MediaPipe کے ساتھ چلایا جا سکتا ہے۔ یہ اینڈرائیڈ، iOS اور IoT ایپلیکیشنز کے لیے ماڈلز کو مکمل طور پر ڈیوائس پر چلانے کی سہولت فراہم کرتا ہے۔ AI Edge Torch وسیع CPU کوریج پیش کرتا ہے، اور ابتدائی GPU اور NPU سپورٹ بھی فراہم کرتا ہے۔ AI Edge Torch PyTorch کے ساتھ قریبی انضمام کی کوشش کرتا ہے، torch.export() پر مبنی ہے اور Core ATen آپریٹرز کی اچھی کوریج فراہم کرتا ہے۔

## **🪬 رہنمائی**

### **🔥 Microsoft Phi-3.5 کو tflite میں تبدیل کرنا**

0. یہ سیمپل اینڈرائیڈ 14+ کے لیے ہے۔

1. Python 3.10.12 انسٹال کریں۔

***تجویز:*** Python ماحول بنانے کے لیے conda استعمال کریں۔

2. Ubuntu 20.04 / 22.04 (براہ کرم [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) پر توجہ دیں)

***تجویز:*** اپنا ماحول بنانے کے لیے Azure Linux VM یا کسی تیسرے فریق کے کلاؤڈ VM کا استعمال کریں۔

3. اپنے Linux bash پر جائیں، اور Python لائبریری انسٹال کریں۔

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face سے Microsoft-3.5-Instruct ڈاؤن لوڈ کریں۔

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 کو tflite میں تبدیل کریں۔

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 کو Android Mediapipe Bundle میں تبدیل کرنا**

براہ کرم پہلے mediapipe انسٹال کریں۔

```bash

pip install mediapipe

```

اس کوڈ کو [اپنے نوٹ بک](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) میں چلائیں۔

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

![demo](../../../../../../translated_images/ur/demo.06d5a4246f057d1b.webp)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔