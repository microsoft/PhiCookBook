<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f766ec7e68d97f6009b58794b471d66",
  "translation_date": "2025-04-03T07:03:19+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ur"
}
-->
# **Phi-3.5 کو Intel OpenVINO کے ذریعے کوانٹائز کرنا**

Intel دنیا کی سب سے روایتی CPU بنانے والی کمپنی ہے جس کے بے شمار صارفین ہیں۔ مشین لرننگ اور ڈیپ لرننگ کے بڑھتے ہوئے رجحان کے ساتھ، Intel نے بھی AI ایکسیلیریشن کی دوڑ میں شامل ہونے کا فیصلہ کیا۔ ماڈل انفیرنس کے لیے، Intel نہ صرف GPUs اور CPUs بلکہ NPUs کا بھی استعمال کرتا ہے۔

ہم امید کرتے ہیں کہ Phi-3.x فیملی کو اینڈ سائیڈ پر ڈپلائے کریں تاکہ یہ AI PC اور Copilot PC کا سب سے اہم حصہ بن سکے۔ اینڈ سائیڈ پر ماڈل لوڈ کرنے کا انحصار مختلف ہارڈویئر مینوفیکچررز کے تعاون پر ہے۔ یہ باب خاص طور پر Intel OpenVINO کو ایک کوانٹیٹیٹو ماڈل کے طور پر استعمال کرنے کے ایپلیکیشن سیناریو پر مرکوز ہے۔

## **OpenVINO کیا ہے؟**

OpenVINO ایک اوپن سورس ٹول کٹ ہے جو ڈیپ لرننگ ماڈلز کو کلاؤڈ سے ایج تک بہتر بنانے اور ڈپلائے کرنے کے لیے بنایا گیا ہے۔ یہ مختلف استعمال کے کیسز میں ڈیپ لرننگ انفیرنس کو تیز کرتا ہے، جیسے جنریٹیو AI، ویڈیو، آڈیو، اور زبان، مشہور فریم ورک جیسے PyTorch، TensorFlow، ONNX، اور دیگر کے ماڈلز کے ساتھ۔ ماڈلز کو کنورٹ اور بہتر کریں، اور Intel® ہارڈویئر اور ماحولیات کے امتزاج پر ڈپلائے کریں، چاہے آن پرمائس ہو یا ڈیوائس پر، براؤزر میں یا کلاؤڈ میں۔

اب OpenVINO کے ذریعے، آپ Intel ہارڈویئر پر GenAI ماڈل کو جلدی کوانٹائز کر سکتے ہیں اور ماڈل ریفرنس کو تیز کر سکتے ہیں۔

اب OpenVINO Phi-3.5-Vision اور Phi-3.5-Instruct کے کوانٹائزیشن کنورژن کو سپورٹ کرتا ہے۔

### **ماحول کی ترتیب**

براہ کرم یقینی بنائیں کہ درج ذیل ماحول کی ضروریات انسٹال ہیں، یہ requirement.txt ہے:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instruct کو OpenVINO کے ذریعے کوانٹائز کرنا**

ٹرمینل میں، براہ کرم یہ اسکرپٹ چلائیں:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Vision کو OpenVINO کے ذریعے کوانٹائز کرنا**

براہ کرم یہ اسکرپٹ Python یا Jupyter lab میں چلائیں:

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Intel OpenVINO کے ساتھ Phi-3.5 کے نمونے**

| لیبز    | تعارف | جائیں |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | اپنے AI PC میں Phi-3.5 Instruct استعمال کرنے کا طریقہ سیکھیں    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | اپنے AI PC میں تصویر کا تجزیہ کرنے کے لیے Phi-3.5 Vision استعمال کرنے کا طریقہ سیکھیں      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | اپنے AI PC میں ویڈیو کا تجزیہ کرنے کے لیے Phi-3.5 Vision استعمال کرنے کا طریقہ سیکھیں    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **وسائل**

1. Intel OpenVINO کے بارے میں مزید جانیں [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی پوری کوشش کرتے ہیں، لیکن براہ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔