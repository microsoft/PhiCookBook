<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:01:52+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "th"
}
-->
# **การควอนไทซ์ Phi-3.5 ด้วย Intel OpenVINO**

Intel เป็นผู้ผลิต CPU ที่มีประวัติยาวนานและมีผู้ใช้งานจำนวนมาก เมื่อการเรียนรู้ของเครื่องและการเรียนรู้เชิงลึกเติบโตขึ้น Intel ก็เข้าร่วมการแข่งขันในด้านการเร่งความเร็ว AI ด้วย สำหรับการทำ inference ของโมเดล Intel ไม่ได้ใช้แค่ GPU และ CPU เท่านั้น แต่ยังใช้ NPU ด้วย

เราหวังที่จะนำ Phi-3.x Family ไปใช้งานที่ฝั่งปลายทาง โดยตั้งเป้าให้เป็นส่วนสำคัญที่สุดของ AI PC และ Copilot PC การโหลดโมเดลที่ฝั่งปลายทางขึ้นอยู่กับความร่วมมือของผู้ผลิตฮาร์ดแวร์ต่างๆ บทนี้จะเน้นไปที่การใช้งาน Intel OpenVINO ในฐานะโมเดลเชิงปริมาณ

## **OpenVINO คืออะไร**

OpenVINO เป็นชุดเครื่องมือโอเพนซอร์สสำหรับการปรับแต่งและนำโมเดลการเรียนรู้เชิงลึกไปใช้งานตั้งแต่บนคลาวด์จนถึง edge ช่วยเร่งการทำ inference ของ deep learning ในหลายกรณีใช้งาน เช่น generative AI, วิดีโอ, เสียง และภาษา โดยรองรับโมเดลจากเฟรมเวิร์กยอดนิยมอย่าง PyTorch, TensorFlow, ONNX และอื่นๆ อีกมากมาย สามารถแปลงและปรับแต่งโมเดล พร้อมนำไปใช้งานบนฮาร์ดแวร์และสภาพแวดล้อมของ Intel® ทั้งในองค์กร อุปกรณ์ปลายทาง บนเบราว์เซอร์ หรือบนคลาวด์

ตอนนี้ด้วย OpenVINO คุณสามารถควอนไทซ์โมเดล GenAI บนฮาร์ดแวร์ Intel ได้อย่างรวดเร็วและเร่งความเร็วการอ้างอิงโมเดล

ปัจจุบัน OpenVINO รองรับการแปลงควอนไทซ์ของ Phi-3.5-Vision และ Phi-3.5 Instruct

### **การตั้งค่าสภาพแวดล้อม**

โปรดตรวจสอบให้แน่ใจว่าติดตั้ง dependencies ตามนี้แล้ว ซึ่งเป็น requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **การควอนไทซ์ Phi-3.5-Instruct ด้วย OpenVINO**

ใน Terminal ให้รันสคริปต์นี้

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **การควอนไทซ์ Phi-3.5-Vision ด้วย OpenVINO**

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
| 🚀 Lab-แนะนำ Phi-3.5 Instruct  | เรียนรู้วิธีใช้ Phi-3.5 Instruct ใน AI PC ของคุณ    |  [ไปที่](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-แนะนำ Phi-3.5 Vision (ภาพ) | เรียนรู้วิธีใช้ Phi-3.5 Vision วิเคราะห์ภาพใน AI PC ของคุณ      |  [ไปที่](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-แนะนำ Phi-3.5 Vision (วิดีโอ)   | เรียนรู้วิธีใช้ Phi-3.5 Vision วิเคราะห์วิดีโอใน AI PC ของคุณ    |  [ไปที่](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **แหล่งข้อมูล**

1. เรียนรู้เพิ่มเติมเกี่ยวกับ Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้