<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-07T10:46:08+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ar"
}
-->
# **تحجيم Phi-3.5 باستخدام Intel OpenVINO**

تُعتبر Intel من أقدم شركات تصنيع وحدات المعالجة المركزية ولديها عدد كبير من المستخدمين. مع صعود التعلم الآلي والتعلم العميق، انضمت Intel أيضًا إلى المنافسة في تسريع الذكاء الاصطناعي. بالنسبة لاستدلال النماذج، لا تستخدم Intel وحدات معالجة الرسومات ووحدات المعالجة المركزية فقط، بل تستخدم أيضًا وحدات معالجة الشبكات العصبية (NPUs).

نأمل في نشر عائلة Phi-3.x على الجانب النهائي، مع تطلعها لأن تصبح الجزء الأهم في حواسيب الذكاء الاصطناعي وحواسيب المساعد الذكي. يعتمد تحميل النموذج على الجانب النهائي على تعاون مصنعي الأجهزة المختلفين. يركز هذا الفصل بشكل أساسي على سيناريو تطبيق Intel OpenVINO كنموذج كمي.

## **ما هو OpenVINO**

OpenVINO هو مجموعة أدوات مفتوحة المصدر لتحسين ونشر نماذج التعلم العميق من السحابة إلى الحافة. يسرع استدلال التعلم العميق عبر استخدامات متعددة، مثل الذكاء الاصطناعي التوليدي، الفيديو، الصوت، واللغة مع نماذج من أُطُر شائعة مثل PyTorch و TensorFlow و ONNX والمزيد. يحول ويحسن النماذج، وينشرها عبر مجموعة من أجهزة وبرمجيات Intel®، سواء في البيئات المحلية أو على الجهاز، في المتصفح أو في السحابة.

الآن مع OpenVINO، يمكنك بسرعة تحجيم نموذج GenAI على أجهزة Intel وتسريع استدعاء النموذج.

يدعم OpenVINO الآن تحويل التحجيم لـ Phi-3.5-Vision و Phi-3.5 Instruct

### **إعداد البيئة**

يرجى التأكد من تثبيت تبعيات البيئة التالية، هذا هو ملف requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **تحجيم Phi-3.5-Instruct باستخدام OpenVINO**

في الطرفية، يرجى تشغيل هذا السكربت

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **تحجيم Phi-3.5-Vision باستخدام OpenVINO**

يرجى تشغيل هذا السكربت في بايثون أو Jupyter lab

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

### **🤖 عينات لـ Phi-3.5 مع Intel OpenVINO**

| المختبرات    | التعريف | الانتقال |
| -------- | ------- |  ------- |
| 🚀 تعريف مختبر Phi-3.5 Instruct  | تعلّم كيفية استخدام Phi-3.5 Instruct في حاسوب الذكاء الاصطناعي الخاص بك    |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 تعريف مختبر Phi-3.5 Vision (صورة) | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الصور في حاسوب الذكاء الاصطناعي الخاص بك      |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 تعريف مختبر Phi-3.5 Vision (فيديو)   | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الفيديو في حاسوب الذكاء الاصطناعي الخاص بك    |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |


## **الموارد**

1. تعلّم المزيد عن Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. مستودع Intel OpenVINO على GitHub [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. بالنسبة للمعلومات الهامة، يُنصح بالترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.