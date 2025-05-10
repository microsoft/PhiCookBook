<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:56:34+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "th"
}
-->
# **การทำ Quantizing Phi-3.5 ด้วย Intel OpenVINO**

Intel เป็นผู้ผลิต CPU แบบดั้งเดิมที่มีผู้ใช้จำนวนมาก เมื่อการเรียนรู้ของเครื่องและการเรียนรู้เชิงลึกเติบโตขึ้น Intel ก็เข้าร่วมการแข่งขันเพื่อเร่งความเร็ว AI ด้วย สำหรับการทำ inference ของโมเดล Intel ไม่ได้ใช้แค่ GPU และ CPU เท่านั้น แต่ยังใช้ NPU ด้วย

เราหวังที่จะนำ Phi-3.x Family ไปใช้งานบนฝั่งปลายทาง โดยตั้งใจให้เป็นส่วนสำคัญที่สุดของ AI PC และ Copilot PC การโหลดโมเดลบนฝั่งปลายทางขึ้นอยู่กับความร่วมมือของผู้ผลิตฮาร์ดแวร์ต่างๆ บทนี้จะเน้นไปที่การใช้งาน Intel OpenVINO ในฐานะโมเดลเชิงปริมาณ

## **OpenVINO คืออะไร**

OpenVINO เป็นชุดเครื่องมือแบบโอเพ่นซอร์สสำหรับการปรับแต่งและนำโมเดลการเรียนรู้เชิงลึกไปใช้งานจากคลาวด์สู่เอดจ์ มันช่วยเร่งความเร็วการทำ inference ของ deep learning ในหลายกรณีใช้งาน เช่น generative AI, วิดีโอ, เสียง และภาษา โดยรองรับโมเดลจากเฟรมเวิร์กยอดนิยมอย่าง PyTorch, TensorFlow, ONNX และอื่นๆ แปลงและปรับแต่งโมเดล แล้วนำไปใช้งานบนฮาร์ดแวร์และสภาพแวดล้อมของ Intel® ที่หลากหลาย ทั้งในองค์กร อุปกรณ์ บราวเซอร์ หรือบนคลาวด์

ตอนนี้ด้วย OpenVINO คุณสามารถทำ quantize โมเดล GenAI บนฮาร์ดแวร์ Intel ได้อย่างรวดเร็วและเร่งความเร็วการอ้างอิงโมเดล

ตอนนี้ OpenVINO รองรับการแปลง quantization ของ Phi-3.5-Vision และ Phi-3.5 Instruct

### **การตั้งค่าสภาพแวดล้อม**

โปรดตรวจสอบให้แน่ใจว่าติดตั้ง dependencies ของสภาพแวดล้อมดังต่อไปนี้แล้ว นี่คือ requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **การทำ Quantizing Phi-3.5-Instruct ด้วย OpenVINO**

ใน Terminal โปรดรันสคริปต์นี้

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **การทำ Quantizing Phi-3.5-Vision ด้วย OpenVINO**

โปรดรันสคริปต์นี้ใน Python หรือ Jupyter lab

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

### **🤖 ตัวอย่างสำหรับ Phi-3.5 กับ Intel OpenVINO**

| Labs    | แนะนำ | ไปที่ |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | เรียนรู้วิธีใช้ Phi-3.5 Instruct ใน AI PC ของคุณ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | เรียนรู้วิธีใช้ Phi-3.5 Vision เพื่อวิเคราะห์ภาพใน AI PC ของคุณ      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | เรียนรู้วิธีใช้ Phi-3.5 Vision เพื่อวิเคราะห์วิดีโอใน AI PC ของคุณ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **แหล่งข้อมูล**

1. เรียนรู้เพิ่มเติมเกี่ยวกับ Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ควรใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้