<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T21:59:12+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ur"
}
-->
# **Intel OpenVINO کے ذریعے Phi-3.5 کی مقداری تبدیلی**

Intel سب سے روایتی CPU بنانے والا ہے جس کے بہت سے صارفین ہیں۔ مشین لرننگ اور ڈیپ لرننگ کے عروج کے ساتھ، Intel نے بھی AI کی تیز رفتاری کے مقابلے میں حصہ لیا ہے۔ ماڈل کی انفرنس کے لیے، Intel نہ صرف GPUs اور CPUs استعمال کرتا ہے بلکہ NPUs کا بھی استعمال کرتا ہے۔

ہم امید کرتے ہیں کہ Phi-3.x فیملی کو اینڈ ڈیوائس پر تعینات کیا جائے گا، تاکہ یہ AI PC اور Copilot PC کا سب سے اہم حصہ بن جائے۔ اینڈ ڈیوائس پر ماڈل کی لوڈنگ مختلف ہارڈویئر بنانے والوں کے تعاون پر منحصر ہے۔ یہ باب خاص طور پر Intel OpenVINO کے مقداری ماڈل کے استعمال کے منظرنامے پر توجہ دیتا ہے۔

## **OpenVINO کیا ہے**

OpenVINO ایک اوپن سورس ٹول کٹ ہے جو کلاؤڈ سے ایج تک ڈیپ لرننگ ماڈلز کو بہتر بنانے اور تعینات کرنے کے لیے ہے۔ یہ مختلف استعمال کے کیسز میں، جیسے جنریٹو AI، ویڈیو، آڈیو، اور زبان، میں ڈیپ لرننگ انفرنس کو تیز کرتا ہے، اور مشہور فریم ورکس جیسے PyTorch، TensorFlow، ONNX وغیرہ کے ماڈلز کے ساتھ کام کرتا ہے۔ ماڈلز کو تبدیل کریں اور بہتر بنائیں، اور Intel® ہارڈویئر اور ماحولیات کے امتزاج پر، آن-پرمیسس اور ڈیوائس پر، براؤزر یا کلاؤڈ میں تعینات کریں۔

اب OpenVINO کے ساتھ، آپ Intel ہارڈویئر میں GenAI ماڈل کو جلدی مقداری بنا سکتے ہیں اور ماڈل کی ریفرنس کو تیز کر سکتے ہیں۔

اب OpenVINO Phi-3.5-Vision اور Phi-3.5 Instruct کی مقداری تبدیلی کی حمایت کرتا ہے۔

### **ماحول کی ترتیب**

براہ کرم یقینی بنائیں کہ درج ذیل ماحول کی ضروریات انسٹال ہیں، یہ requirement.txt ہے

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO کے ذریعے Phi-3.5-Instruct کی مقداری تبدیلی**

ٹرمینل میں، براہ کرم یہ اسکرپٹ چلائیں

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO کے ذریعے Phi-3.5-Vision کی مقداری تبدیلی**

براہ کرم Python یا Jupyter lab میں یہ اسکرپٹ چلائیں

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
| 🚀 Lab-Introduce Phi-3.5 Instruct  | سیکھیں کہ اپنے AI PC میں Phi-3.5 Instruct کو کیسے استعمال کریں    |  [جائیں](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (تصویر) | سیکھیں کہ اپنے AI PC میں تصویر کا تجزیہ کرنے کے لیے Phi-3.5 Vision کو کیسے استعمال کریں      |  [جائیں](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (ویڈیو)   | سیکھیں کہ اپنے AI PC میں ویڈیو کا تجزیہ کرنے کے لیے Phi-3.5 Vision کو کیسے استعمال کریں    |  [جائیں](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **وسائل**

1. Intel OpenVINO کے بارے میں مزید جانیں [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub ریپو [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔