<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:48:58+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "th"
}
-->
# **การใช้ Microsoft Phi-3.5 tflite เพื่อสร้างแอป Android**

นี่คือตัวอย่าง Android ที่ใช้โมเดล Microsoft Phi-3.5 tflite

## **📚 ความรู้**

Android LLM Inference API ช่วยให้คุณรันโมเดลภาษาใหญ่ (LLMs) ได้ทั้งหมดบนอุปกรณ์ Android สำหรับแอปพลิเคชัน ซึ่งคุณสามารถใช้ทำงานหลากหลาย เช่น การสร้างข้อความ ดึงข้อมูลในรูปแบบภาษาธรรมชาติ และสรุปเอกสาร งานนี้รองรับโมเดลข้อความต่อข้อความหลายตัวในตัว ทำให้คุณสามารถใช้โมเดล AI สร้างสรรค์บนอุปกรณ์ล่าสุดกับแอป Android ของคุณได้

Google AI Edge Torch คือไลบรารี Python ที่รองรับการแปลงโมเดล PyTorch เป็นรูปแบบ .tflite ซึ่งสามารถรันด้วย TensorFlow Lite และ MediaPipe ได้ ทำให้แอปสำหรับ Android, iOS และ IoT สามารถรันโมเดลได้ทั้งหมดบนอุปกรณ์ AI Edge Torch ครอบคลุมการใช้งาน CPU อย่างกว้างขวาง พร้อมการรองรับ GPU และ NPU ในขั้นต้น AI Edge Torch มุ่งเน้นการผสานกับ PyTorch อย่างใกล้ชิด โดยสร้างบน torch.export() และรองรับ Core ATen operators อย่างดี

## **🪬 แนวทาง**

### **🔥 แปลง Microsoft Phi-3.5 เป็น tflite**

0. ตัวอย่างนี้สำหรับ Android 14+

1. ติดตั้ง Python 3.10.12

***คำแนะนำ:*** ใช้ conda ในการติดตั้งสภาพแวดล้อม Python ของคุณ

2. Ubuntu 20.04 / 22.04 (โปรดดูที่ [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***คำแนะนำ:*** ใช้ Azure Linux VM หรือคลาวด์ของบุคคลที่สามเพื่อสร้างสภาพแวดล้อมของคุณ

3. เข้าไปที่ bash บน Linux ของคุณ เพื่อติดตั้งไลบรารี Python

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

กรุณาติดตั้ง mediapipe ก่อน

```bash

pip install mediapipe

```

รันโค้ดนี้ใน [สมุดบันทึกของคุณ](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 ใช้ adb push เพื่อส่งโมเดลงานไปยังเส้นทางบนอุปกรณ์ Android ของคุณ**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 การรันโค้ด Android ของคุณ**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.th.png)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้บริการแปลโดยผู้เชี่ยวชาญที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้