<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T14:00:03+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ms"
}
-->
# **استخدام Intel OpenVINO لتكميم Phi-3.5**

تُعتبر Intel من أقدم مصنعي وحدات المعالجة المركزية ولديها العديد من المستخدمين. مع تزايد استخدام التعلم الآلي والتعلم العميق، انضمت Intel أيضًا إلى سباق تسريع الذكاء الاصطناعي. في استدلال النماذج، لا تستخدم Intel فقط وحدات المعالجة الرسومية ووحدات المعالجة المركزية، بل تستخدم أيضًا وحدات المعالجة العصبية (NPU).

نأمل في نشر عائلة Phi-3.x على الطرف النهائي، مع الطموح لتصبح الجزء الأهم في أجهزة AI PC و Copilot PC. تحميل النموذج على الطرف النهائي يعتمد على تعاون مختلف مصنعي الأجهزة. يركز هذا الفصل بشكل رئيسي على سيناريو تطبيق Intel OpenVINO كنموذج كمي.

## **ما هو OpenVINO**

OpenVINO هو مجموعة أدوات مفتوحة المصدر لتحسين ونشر نماذج التعلم العميق من السحابة إلى الطرف النهائي. يسرع استدلال التعلم العميق في مختلف حالات الاستخدام، مثل الذكاء الاصطناعي التوليدي، الفيديو، الصوت، واللغة باستخدام نماذج من أُطر عمل شهيرة مثل PyTorch، TensorFlow، ONNX، وغيرها. يمكنك تحويل وتحسين النماذج، ونشرها عبر مجموعة متنوعة من أجهزة وبرمجيات Intel®، سواء في بيئة محلية أو على الجهاز، في المتصفح أو في السحابة.

الآن مع OpenVINO، يمكنك بسرعة تكميم نموذج GenAI على أجهزة Intel وتسريع استدلال النموذج.

يدعم OpenVINO الآن تحويل التكميم لنماذج Phi-3.5-Vision و Phi-3.5 Instruct

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

### **تكميم Phi-3.5-Instruct باستخدام OpenVINO**

في الطرفية، يرجى تشغيل هذا السكربت

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **تكميم Phi-3.5-Vision باستخدام OpenVINO**

يرجى تشغيل هذا السكربت في Python أو Jupyter lab

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

| المختبرات  | التعريف | ابدأ |
| -------- | ------- | ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | تعلّم كيفية استخدام Phi-3.5 Instruct في جهاز AI PC الخاص بك    |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (صورة) | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الصور في جهاز AI PC الخاص بك      |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (فيديو)   | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الفيديو في جهاز AI PC الخاص بك    |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **المصادر**

1. تعرّف أكثر على Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. مستودع Intel OpenVINO على GitHub [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.