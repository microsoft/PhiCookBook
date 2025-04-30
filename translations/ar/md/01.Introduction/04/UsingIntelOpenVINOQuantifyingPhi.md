<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-03-27T08:33:07+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ar"
}
-->
# **استخدام Intel OpenVINO لتكميم Phi-3.5**

إنتل هي واحدة من أقدم الشركات المصنعة لوحدات المعالجة المركزية (CPU) ولديها العديد من المستخدمين. مع صعود التعلم الآلي والتعلم العميق، انضمت إنتل أيضًا إلى المنافسة في تسريع الذكاء الاصطناعي. لا تقتصر إنتل على استخدام وحدات المعالجة المركزية (CPU) ووحدات معالجة الرسومات (GPU) فقط، بل تستخدم أيضًا وحدات المعالجة العصبية (NPU).

نأمل في نشر عائلة Phi-3.x على الأجهزة الطرفية، بهدف أن تصبح جزءًا أساسيًا من أجهزة الحاسوب الذكية وأجهزة الحاسوب المساعدة. يعتمد تحميل النموذج على الأجهزة الطرفية على تعاون مختلف مصنعي الأجهزة. يركز هذا الفصل بشكل أساسي على سيناريو تطبيق Intel OpenVINO كنموذج تكميم.

## **ما هو OpenVINO**

OpenVINO هو مجموعة أدوات مفتوحة المصدر تهدف إلى تحسين ونشر نماذج التعلم العميق من السحابة إلى الأجهزة الطرفية. تُسرّع OpenVINO استدلال التعلم العميق عبر العديد من حالات الاستخدام، مثل الذكاء الاصطناعي التوليدي، الفيديو، الصوت، واللغة باستخدام نماذج من أطر عمل شائعة مثل PyTorch، TensorFlow، ONNX، وغيرها. يمكن تحويل النماذج وتحسينها، ثم نشرها عبر مزيج من أجهزة إنتل® وبيئات مختلفة، سواء في الموقع أو على الأجهزة أو عبر المتصفح أو في السحابة.

الآن، مع OpenVINO، يمكنك بسرعة تكميم نموذج GenAI على أجهزة إنتل وتسريع استدلال النموذج.

حاليًا، يدعم OpenVINO تحويل التكميم لـ Phi-3.5-Vision و Phi-3.5 Instruct.

### **إعداد البيئة**

يرجى التأكد من تثبيت التبعيات البيئية التالية، هذا هو ملف requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **تكميم Phi-3.5-Instruct باستخدام OpenVINO**

في الطرفية (Terminal)، يرجى تشغيل هذا السكربت

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **تكميم Phi-3.5-Vision باستخدام OpenVINO**

يرجى تشغيل هذا السكربت في Python أو Jupyter Lab

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

### **🤖 أمثلة على Phi-3.5 مع Intel OpenVINO**

| المعامل    | الوصف | الانتقال |
| -------- | ------- |  ------- |
| 🚀 معمل - تقديم Phi-3.5 Instruct  | تعلم كيفية استخدام Phi-3.5 Instruct في جهاز الحاسوب الذكي الخاص بك    |  [الانتقال](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 معمل - تقديم Phi-3.5 Vision (الصورة) | تعلم كيفية استخدام Phi-3.5 Vision لتحليل الصور في جهاز الحاسوب الذكي الخاص بك      |  [الانتقال](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 معمل - تقديم Phi-3.5 Vision (الفيديو)   | تعلم كيفية استخدام Phi-3.5 Vision لتحليل الفيديو في جهاز الحاسوب الذكي الخاص بك    |  [الانتقال](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **المصادر**

1. تعرف أكثر على Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. مستودع GitHub الخاص بـ Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.