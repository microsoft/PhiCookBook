<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T21:59:02+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "fa"
}
-->
# **کوانتایز کردن Phi-3.5 با استفاده از Intel OpenVINO**

اینتل یکی از قدیمی‌ترین تولیدکنندگان CPU با تعداد زیادی کاربر است. با رشد یادگیری ماشین و یادگیری عمیق، اینتل نیز وارد رقابت برای تسریع هوش مصنوعی شده است. برای استنتاج مدل، اینتل نه تنها از GPU و CPU استفاده می‌کند، بلکه از NPUها نیز بهره می‌برد.

امیدواریم خانواده Phi-3.x را در سمت انتهایی پیاده‌سازی کنیم و به بخش مهمی از کامپیوترهای هوش مصنوعی و کامپیوترهای همراه تبدیل شویم. بارگذاری مدل در سمت انتهایی به همکاری تولیدکنندگان سخت‌افزار مختلف بستگی دارد. این فصل عمدتاً بر سناریوی کاربردی Intel OpenVINO به عنوان یک مدل کوانتیزه شده تمرکز دارد.

## **OpenVINO چیست**

OpenVINO یک مجموعه ابزار متن‌باز برای بهینه‌سازی و استقرار مدل‌های یادگیری عمیق از فضای ابری تا لبه است. این ابزار استنتاج یادگیری عمیق را در کاربردهای مختلف مانند هوش مصنوعی مولد، ویدئو، صدا و زبان با مدل‌هایی از فریم‌ورک‌های محبوبی مانند PyTorch، TensorFlow، ONNX و غیره تسریع می‌کند. مدل‌ها را تبدیل و بهینه‌سازی کرده و در ترکیبی از سخت‌افزار و محیط‌های اینتل، چه در محل و چه روی دستگاه، در مرورگر یا در فضای ابری مستقر می‌کند.

اکنون با OpenVINO می‌توانید مدل GenAI را به سرعت روی سخت‌افزار اینتل کوانتیزه کرده و استنتاج مدل را تسریع کنید.

در حال حاضر OpenVINO از تبدیل کوانتیزه Phi-3.5-Vision و Phi-3.5 Instruct پشتیبانی می‌کند.

### **راه‌اندازی محیط**

لطفاً اطمینان حاصل کنید که وابستگی‌های محیط زیر نصب شده‌اند، این فایل requirement.txt است

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **کوانتایز کردن Phi-3.5-Instruct با استفاده از OpenVINO**

در ترمینال، لطفاً این اسکریپت را اجرا کنید

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **کوانتایز کردن Phi-3.5-Vision با استفاده از OpenVINO**

لطفاً این اسکریپت را در پایتون یا Jupyter lab اجرا کنید

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

### **🤖 نمونه‌هایی برای Phi-3.5 با Intel OpenVINO**

| آزمایشگاه‌ها    | معرفی | رفتن |
| -------- | ------- |  ------- |
| 🚀 معرفی آزمایشگاه Phi-3.5 Instruct  | یاد بگیرید چگونه از Phi-3.5 Instruct در کامپیوتر هوش مصنوعی خود استفاده کنید    |  [رفتن](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (تصویر) | یاد بگیرید چگونه از Phi-3.5 Vision برای تحلیل تصویر در کامپیوتر هوش مصنوعی خود استفاده کنید      |  [رفتن](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (ویدئو)   | یاد بگیرید چگونه از Phi-3.5 Vision برای تحلیل ویدئو در کامپیوتر هوش مصنوعی خود استفاده کنید    |  [رفتن](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **منابع**

1. اطلاعات بیشتر درباره Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. مخزن GitHub Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.