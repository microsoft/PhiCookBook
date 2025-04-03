<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2faa9c6d61c5aa2708aec02a39ec464b",
  "translation_date": "2025-04-03T07:36:22+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ur"
}
-->
# **مائیکروسافٹ Phi-3.5 tflite استعمال کرتے ہوئے اینڈرائیڈ ایپ بنانا**

یہ ایک اینڈرائیڈ نمونہ ہے جو مائیکروسافٹ Phi-3.5 tflite ماڈلز استعمال کرتا ہے۔

## **📚 معلومات**

اینڈرائیڈ LLM انفرنس API آپ کو بڑے زبان ماڈلز (LLMs) مکمل طور پر ڈیوائس پر چلانے کی اجازت دیتا ہے، جو اینڈرائیڈ ایپلیکیشنز میں مختلف کاموں کے لیے استعمال ہو سکتے ہیں، جیسے کہ متن تیار کرنا، قدرتی زبان میں معلومات حاصل کرنا، اور دستاویزات کا خلاصہ بنانا۔ یہ کام متعدد ٹیکسٹ-ٹو-ٹیکسٹ بڑے زبان ماڈلز کے لیے بلٹ-ان سپورٹ فراہم کرتا ہے، تاکہ آپ اپنے اینڈرائیڈ ایپس میں جدید ترین جنریٹو AI ماڈلز کا اطلاق کر سکیں۔

گوگل AI ایج ٹارچ ایک پائتھون لائبریری ہے جو PyTorch ماڈلز کو .tflite فارمیٹ میں تبدیل کرنے کی سہولت فراہم کرتی ہے، جسے پھر TensorFlow Lite اور MediaPipe کے ساتھ چلایا جا سکتا ہے۔ یہ اینڈرائیڈ، iOS اور IoT کے لیے ایسے ایپلیکیشنز کو ممکن بناتا ہے جو مکمل طور پر ڈیوائس پر ماڈلز چلا سکتے ہیں۔ AI ایج ٹارچ وسیع CPU کوریج فراہم کرتا ہے، ابتدائی GPU اور NPU سپورٹ کے ساتھ۔ AI ایج ٹارچ PyTorch کے ساتھ قریبی انضمام کے لیے کوشش کرتا ہے، torch.export() پر مبنی اور Core ATen آپریٹرز کی اچھی کوریج فراہم کرتا ہے۔

## **🪬 رہنمائی**

### **🔥 مائیکروسافٹ Phi-3.5 کو tflite سپورٹ میں تبدیل کرنا**

0. یہ نمونہ اینڈرائیڈ 14+ کے لیے ہے۔

1. Python 3.10.12 انسٹال کریں۔

***تجویز:*** اپنی Python انوائرمنٹ انسٹال کرنے کے لیے conda استعمال کریں۔

2. Ubuntu 20.04 / 22.04 (براہ کرم [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) پر توجہ دیں)

***تجویز:*** Azure Linux VM یا کسی تیسرے فریق کے کلاؤڈ VM کا استعمال کرکے اپنا انوائرمنٹ بنائیں۔

3. اپنے لینکس bash میں جائیں، Python لائبریری انسٹال کرنے کے لیے:

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face سے Microsoft-3.5-Instruct ڈاؤنلوڈ کریں:

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 کو tflite میں تبدیل کریں:

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 مائیکروسافٹ Phi-3.5 کو اینڈرائیڈ Mediapipe بنڈل میں تبدیل کرنا**

پہلے mediapipe انسٹال کریں:

```bash

pip install mediapipe

```

یہ کوڈ [اپنے نوٹ بک](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) میں چلائیں:

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

### **🔥 adb کے ذریعے ماڈل کو اپنے اینڈرائیڈ ڈیوائسز کے راستے میں منتقل کریں**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 اپنے اینڈرائیڈ کوڈ کو چلائیں**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ur.png)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔