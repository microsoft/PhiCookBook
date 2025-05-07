<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-07T14:07:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ur"
}
-->
# **مائیکروسافٹ Phi-3.5 tflite استعمال کرتے ہوئے Android ایپ بنائیں**

یہ مائیکروسافٹ Phi-3.5 tflite ماڈلز استعمال کرنے والا ایک Android سیمپل ہے۔

## **📚 معلومات**

Android LLM Inference API آپ کو Android ایپس کے لیے بڑے زبان کے ماڈلز (LLMs) کو مکمل طور پر ڈیوائس پر چلانے کی سہولت دیتا ہے، جس سے آپ مختلف قسم کے کام انجام دے سکتے ہیں، جیسے متن تیار کرنا، قدرتی زبان میں معلومات حاصل کرنا، اور دستاویزات کا خلاصہ بنانا۔ یہ ٹاسک متعدد ٹیکسٹ سے ٹیکسٹ بڑے زبان کے ماڈلز کے لیے بلٹ ان سپورٹ فراہم کرتا ہے، تاکہ آپ جدید آن-ڈیوائس جنریٹو AI ماڈلز کو اپنی Android ایپس میں لاگو کر سکیں۔

Google AI Edge Torch ایک پائتھن لائبریری ہے جو PyTorch ماڈلز کو .tflite فارمیٹ میں تبدیل کرنے کی حمایت کرتی ہے، جسے پھر TensorFlow Lite اور MediaPipe کے ساتھ چلایا جا سکتا ہے۔ اس سے Android، iOS اور IoT کے لیے ایسی ایپلیکیشنز ممکن ہوتی ہیں جو ماڈلز کو مکمل طور پر ڈیوائس پر چلا سکیں۔ AI Edge Torch وسیع CPU کوریج فراہم کرتا ہے، اور ابتدائی GPU اور NPU سپورٹ بھی دیتا ہے۔ AI Edge Torch PyTorch کے ساتھ گہرائی سے انضمام کی کوشش کرتا ہے، torch.export() پر مبنی ہے اور Core ATen آپریٹرز کا اچھا احاطہ فراہم کرتا ہے۔

## **🪬 رہنما اصول**

### **🔥 مائیکروسافٹ Phi-3.5 کو tflite میں تبدیل کرنا**

0. یہ سیمپل Android 14+ کے لیے ہے

1. Python 3.10.12 انسٹال کریں

***تجویز:*** conda استعمال کریں تاکہ Python کا ماحول بنائیں

2. Ubuntu 20.04 / 22.04 (براہ کرم [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) پر توجہ دیں)

***تجویز:*** Azure Linux VM یا کسی تھرڈ پارٹی کلاؤڈ VM کا استعمال کریں تاکہ اپنا ماحول بنائیں

3. اپنے Linux bash پر جائیں، اور Python لائبریری انسٹال کریں

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

### **🔥 Microsoft Phi-3.5 کو Android Mediapipe Bundle میں تبدیل کریں**

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

### **🔥 adb push کے ذریعے ماڈل کو اپنے Android ڈیوائس کے راستے پر بھیجیں**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 اپنی Android کوڈ چلائیں**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.ur.png)

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات کا خیال رکھیں کہ خودکار ترجموں میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔