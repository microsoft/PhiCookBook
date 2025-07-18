<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:52:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "th"
}
-->
# **การใช้ Microsoft Phi-3.5 tflite เพื่อสร้างแอป Android**

นี่คือตัวอย่าง Android ที่ใช้โมเดล Microsoft Phi-3.5 tflite

## **📚 ความรู้**

Android LLM Inference API ช่วยให้คุณรันโมเดลภาษาขนาดใหญ่ (LLMs) บนอุปกรณ์ Android ได้ทั้งหมด ซึ่งคุณสามารถใช้ทำงานหลากหลาย เช่น สร้างข้อความ ดึงข้อมูลในรูปแบบภาษาธรรมชาติ และสรุปเอกสาร งานนี้รองรับโมเดลภาษาขนาดใหญ่แบบข้อความต่อข้อความหลายตัวในตัว ทำให้คุณสามารถนำโมเดล AI สร้างสรรค์บนอุปกรณ์ล่าสุดมาใช้กับแอป Android ของคุณได้

Google AI Edge Torch เป็นไลบรารี Python ที่รองรับการแปลงโมเดล PyTorch เป็นไฟล์ .tflite ซึ่งสามารถรันด้วย TensorFlow Lite และ MediaPipe ได้ ทำให้แอปบน Android, iOS และ IoT สามารถรันโมเดลได้ทั้งหมดบนอุปกรณ์ AI Edge Torch ครอบคลุมการใช้งาน CPU อย่างกว้างขวาง พร้อมรองรับ GPU และ NPU ในขั้นต้น AI Edge Torch มุ่งเน้นการผสานกับ PyTorch อย่างใกล้ชิด โดยสร้างบน torch.export() และรองรับ Core ATen operators ได้ดี

## **🪬 แนวทาง**

### **🔥 แปลง Microsoft Phi-3.5 เป็น tflite**

0. ตัวอย่างนี้สำหรับ Android 14 ขึ้นไป

1. ติดตั้ง Python 3.10.12

***แนะนำ:*** ใช้ conda ในการติดตั้งสภาพแวดล้อม Python ของคุณ

2. Ubuntu 20.04 / 22.04 (โปรดดูที่ [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***แนะนำ:*** ใช้ Azure Linux VM หรือ VM บนคลาวด์ของผู้ให้บริการรายอื่นเพื่อสร้างสภาพแวดล้อมของคุณ

3. เปิด bash บน Linux เพื่อติดตั้งไลบรารี Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. ดาวน์โหลด Microsoft-3.5-Instruct จาก Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. แปลง Microsoft Phi-3.5 เป็น tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 แปลง Microsoft Phi-3.5 เป็น Android Mediapipe Bundle**

โปรดติดตั้ง mediapipe ก่อน

```bash

pip install mediapipe

```

รันโค้ดนี้ใน [notebook ของคุณ](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 ใช้ adb push เพื่อส่งโมเดลไปยังเส้นทางในอุปกรณ์ Android ของคุณ**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 รันโค้ด Android ของคุณ**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.th.png)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้