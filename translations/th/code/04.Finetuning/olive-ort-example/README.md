<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:26:30+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "th"
}
-->
# ปรับแต่ง Phi3 ด้วย Olive

ในตัวอย่างนี้ คุณจะใช้ Olive เพื่อ:

1. ปรับแต่ง LoRA adapter เพื่อจำแนกวลีเป็น Sad, Joy, Fear, Surprise
1. รวมค่าน้ำหนักของ adapter เข้ากับโมเดลฐาน
1. ปรับแต่งและทำ Quantize โมเดลเป็น `int4`

เราจะแสดงวิธีการทำ inference กับโมเดลที่ปรับแต่งแล้วโดยใช้ ONNX Runtime (ORT) Generate API

> **⚠️ สำหรับการปรับแต่ง คุณจะต้องมี GPU ที่เหมาะสม เช่น A10, V100, A100**

## 💾 ติดตั้ง

สร้าง Python virtual environment ใหม่ (เช่น ใช้ `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

จากนั้นติดตั้ง Olive และ dependencies สำหรับ workflow การปรับแต่ง:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 ปรับแต่ง Phi3 ด้วย Olive
[ไฟล์การตั้งค่า Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) มี *workflow* ที่ประกอบด้วย *passes* ดังนี้:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

โดยภาพรวม workflow นี้จะ:

1. ปรับแต่ง Phi3 (เป็นเวลา 150 ขั้นตอน ซึ่งคุณสามารถแก้ไขได้) โดยใช้ข้อมูลจาก [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)
1. รวมค่าน้ำหนักของ LoRA adapter เข้ากับโมเดลฐาน ซึ่งจะได้โมเดลเดียวในรูปแบบ ONNX
1. Model Builder จะปรับแต่งโมเดลสำหรับ ONNX runtime *และ* ทำ Quantize โมเดลเป็น `int4`

เพื่อรัน workflow ให้ใช้คำสั่ง:

```bash
olive run --config phrase-classification.json
```

เมื่อ Olive ทำงานเสร็จ โมเดล Phi3 ที่ปรับแต่งและ optimized เป็น `int4` จะอยู่ที่: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`

## 🧑‍💻 นำ Phi3 ที่ปรับแต่งแล้วไปใช้ในแอปของคุณ

เพื่อรันแอป:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

ผลลัพธ์ควรเป็นการจำแนกประเภทคำตอบแบบคำเดียวของวลี (Sad/Joy/Fear/Surprise)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้