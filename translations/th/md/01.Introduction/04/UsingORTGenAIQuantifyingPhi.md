<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:21:06+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "th"
}
-->
## **วิธีใช้ Model Builder ในการทำ Quantizing Phi-3.5**

ตอนนี้ Model Builder รองรับการทำ Quantization ของโมเดล ONNX สำหรับ Phi-3.5 Instruct และ Phi-3.5-Vision

### **Phi-3.5-Instruct**

**การแปลงแบบเร่งด้วย CPU สำหรับ Quantized INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**การแปลงแบบเร่งด้วย CUDA สำหรับ Quantized INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ตั้งค่าสภาพแวดล้อมในเทอร์มินัล

```bash

mkdir models

cd models 

```

2. ดาวน์โหลด microsoft/Phi-3.5-vision-instruct ไปยังโฟลเดอร์ models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. กรุณาดาวน์โหลดไฟล์เหล่านี้ไปยังโฟลเดอร์ Phi-3.5-vision-instruct ของคุณ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ดาวน์โหลดไฟล์นี้ไปยังโฟลเดอร์ models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ไปที่เทอร์มินัล

    แปลงโมเดล ONNX ให้รองรับ FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **หมายเหตุ：**

1. Model Builder รองรับการแปลง Phi-3.5-Instruct และ Phi-3.5-Vision ในขณะนี้ แต่ยังไม่รองรับ Phi-3.5-MoE

2. หากต้องการใช้โมเดล ONNX ที่ทำ Quantized แล้ว สามารถใช้งานผ่าน Generative AI extensions for onnxruntime SDK ได้

3. เราควรคำนึงถึงความรับผิดชอบด้าน AI มากขึ้น ดังนั้นหลังจากการแปลงโมเดลควรทดสอบผลลัพธ์อย่างมีประสิทธิภาพ

4. การทำ Quantizing โมเดล CPU INT4 ช่วยให้เราสามารถนำไปใช้งานบน Edge Device ได้ดีขึ้น ซึ่งเหมาะกับสถานการณ์การใช้งานจริง ดังนั้นเราจึงได้ทำ Phi-3.5-Instruct ในรูปแบบ INT4 เสร็จสมบูรณ์แล้ว

## **แหล่งข้อมูล**

1. เรียนรู้เพิ่มเติมเกี่ยวกับ Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub Repo ของ Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้