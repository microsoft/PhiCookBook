# **تحويل Phi-3.5 إلى كمي باستخدام Intel OpenVINO**

تُعتبر إنتل من أقدم الشركات المصنعة لوحدات المعالجة المركزية (CPU) ولديها عدد كبير من المستخدمين. مع ازدياد انتشار التعلم الآلي والتعلم العميق، انضمت إنتل أيضًا إلى سباق تسريع الذكاء الاصطناعي. في استنتاج النماذج، لا تستخدم إنتل فقط وحدات معالجة الرسوميات (GPU) ووحدات المعالجة المركزية (CPU)، بل تستخدم أيضًا وحدات معالجة الشبكات العصبية (NPU).

نأمل في نشر عائلة Phi-3.x على الأجهزة الطرفية، على أمل أن تصبح الجزء الأهم في حواسيب الذكاء الاصطناعي وحواسيب المساعد الذكي. تحميل النموذج على الأجهزة الطرفية يعتمد على تعاون مختلف مصنعي الأجهزة. يركز هذا الفصل بشكل رئيسي على سيناريو تطبيق Intel OpenVINO كنموذج كمي.

## **ما هو OpenVINO**

OpenVINO هو مجموعة أدوات مفتوحة المصدر لتحسين ونشر نماذج التعلم العميق من السحابة إلى الحافة. يسرّع استنتاج التعلم العميق عبر استخدامات متعددة، مثل الذكاء الاصطناعي التوليدي، الفيديو، الصوت، واللغة باستخدام نماذج من أُطُر عمل شهيرة مثل PyTorch وTensorFlow وONNX وغيرها. يمكنك تحويل وتحسين النماذج، ونشرها عبر مجموعة متنوعة من أجهزة وبرمجيات إنتل، سواء في الموقع أو على الجهاز، في المتصفح أو في السحابة.

الآن مع OpenVINO، يمكنك بسرعة تحويل نموذج GenAI إلى كمي على أجهزة إنتل وتسريع استدعاء النموذج.

يدعم OpenVINO الآن تحويل النماذج الكمية لـ Phi-3.5-Vision و Phi-3.5 Instruct.

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

### **تحويل Phi-3.5-Instruct إلى كمي باستخدام OpenVINO**

في الطرفية، يرجى تشغيل هذا السكربت

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **تحويل Phi-3.5-Vision إلى كمي باستخدام OpenVINO**

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

| المختبرات    | التعريف | الذهاب |
| -------- | ------- |  ------- |
| 🚀 مختبر - تعريف Phi-3.5 Instruct  | تعلّم كيفية استخدام Phi-3.5 Instruct في حاسوب الذكاء الاصطناعي الخاص بك    |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 مختبر - تعريف Phi-3.5 Vision (صورة) | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الصور في حاسوب الذكاء الاصطناعي الخاص بك      |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 مختبر - تعريف Phi-3.5 Vision (فيديو)   | تعلّم كيفية استخدام Phi-3.5 Vision لتحليل الفيديو في حاسوب الذكاء الاصطناعي الخاص بك    |  [اذهب](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **الموارد**

1. تعرّف أكثر على Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. مستودع Intel OpenVINO على GitHub [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.