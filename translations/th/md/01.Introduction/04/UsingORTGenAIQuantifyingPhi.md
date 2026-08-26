# **การควอนไทซ์ Phi Family โดยใช้ส่วนขยาย Generative AI สำหรับ onnxruntime**

## **ส่วนขยาย Generative AI สำหรับ onnxruntime คืออะไร**

ส่วนขยายนี่ช่วยให้คุณรัน Generative AI กับ ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) มันให้วงจร Generative AI สำหรับโมเดล ONNX รวมถึงการอนุมานด้วย ONNX Runtime, การประมวลผล logits, การค้นหาและการสุ่มตัวอย่าง, และการจัดการแคช KV นักพัฒนาสามารถเรียกใช้วิธี generate() ระดับสูง หรือรันแต่ละรอบของโมเดลในรูปแบบลูป สร้างโทเค็นทีละตัว และสามารถปรับพารามิเตอร์การสร้างภายในลูปได้ตามต้องการ รองรับการค้นหา greedy/beam และการสุ่มแบบ TopP, TopK เพื่อสร้างลำดับโทเค็น รวมถึงการประมวลผล logits ในตัวเช่นการลงโทษความซ้ำซ้อน คุณยังสามารถเพิ่มการให้คะแนนแบบกำหนดเองได้อย่างง่ายดาย

ในระดับแอปพลิเคชัน คุณสามารถใช้ส่วนขยาย Generative AI สำหรับ onnxruntime เพื่อสร้างแอปพลิเคชันโดยใช้ C++/ C# / Python ในระดับโมเดล คุณสามารถใช้มันเพื่อผสานโมเดลที่ปรับแต่งแล้วและทำงานที่เกี่ยวข้องกับการปรับใช้เชิงปริมาณ


## **การควอนไทซ์ Phi-3.5 ด้วยส่วนขยาย Generative AI สำหรับ onnxruntime**

### **โมเดลที่รองรับ**

ส่วนขยาย Generative AI สำหรับ onnxruntime รองรับการแปลงควอนไทซ์ของ Microsoft Phi, Google Gemma, Mistral, Meta LLaMA


### **ตัวสร้างโมเดลในส่วนขยาย Generative AI สำหรับ onnxruntime**

ตัวสร้างโมเดลช่วยเร่งการสร้างโมเดล ONNX ที่ปรับแต่งและควอนไทซ์ให้ทำงานกับ API generate() ของ ONNX Runtime ได้อย่างเร็วขึ้นมาก

ผ่าน Model Builder คุณสามารถควอนไทซ์โมเดลเป็น INT4, INT8, FP16, FP32 และรวมวิธีเร่งฮาร์ดแวร์ที่แตกต่างกัน เช่น CPU, CUDA, DirectML, Mobile เป็นต้น

เพื่อใช้ Model Builder คุณต้องติดตั้ง

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

หลังติดตั้ง คุณสามารถรันสคริปต์ Model Builder จากเทอร์มินัลเพื่อแปลงรูปแบบโมเดลและควอนไทซ์ได้


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

ทำความเข้าใจกับพารามิเตอร์ที่เกี่ยวข้อง

1. **model_name** หมายถึงโมเดลบน Hugging face เช่น microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct เป็นต้น หรืออาจเป็นเส้นทางที่คุณเก็บโมเดลไว้

2. **path_to_output_folder** เส้นทางบันทึกผลการแปลงควอนไทซ์

3. **execution_provider** การรองรับการเร่งฮาร์ดแวร์แตกต่างกัน เช่น cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** เราดาวน์โหลดโมเดลจาก Hugging face และแคชไว้ในเครื่องท้องถิ่น




***หมายเหตุ：*** <ul>แม้ว่า Generative AI extensions สำหรับ onnxruntime จะอยู่ในสถานะพรีวิว แต่มันได้ถูกรวมเข้ากับ Microsoft Olive แล้ว และคุณยังสามารถเรียกใช้ฟังก์ชัน Model Builder ของ Generative AI extensions สำหรับ onnxruntime ผ่าน Microsoft Olive ได้ด้วย</ul>

## **วิธีใช้ Model Builder เพื่อควอนไทซ์ Phi-3.5**

Model Builder รองรับการควอนไทซ์โมเดล ONNX สำหรับ Phi-3.5 Instruct และ Phi-3.5-Vision

### **Phi-3.5-Instruct**


**การแปลงแบบเร่งด้วย CPU สำหรับ INT4 ที่ควอนไทซ์แล้ว**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**การแปลงแบบเร่งด้วย CUDA สำหรับ INT4 ที่ควอนไทซ์แล้ว**

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

2. ดาวน์โหลด microsoft/Phi-3.5-vision-instruct ไปที่โฟลเดอร์ models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. โปรดดาวน์โหลดไฟล์เหล่านี้ไปที่โฟลเดอร์ Phi-3.5-vision-instruct ของคุณ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ดาวน์โหลดไฟล์นี้ไปที่โฟลเดอร์ models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ไปที่เทอร์มินัล

    แปลง ONNX โดยรองรับ FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **หมายเหตุ：**

1. Model Builder ตอนนี้รองรับการแปลง Phi-3.5-Instruct และ Phi-3.5-Vision แต่ไม่รองรับ Phi-3.5-MoE

2. เพื่อใช้โมเดลควอนไทซ์ของ ONNX คุณสามารถใช้ผ่าน Generative AI extensions สำหรับ onnxruntime SDK

3. เราต้องคำนึงถึง AI ที่มีความรับผิดชอบมากขึ้น ดังนั้นหลังการแปลงควอนไทซ์โมเดล แนะนำให้ทดสอบผลลัพธ์อย่างมีประสิทธิภาพเพิ่มเติม

4. โดยการควอนไทซ์โมเดล CPU INT4 เราสามารถปรับใช้กับอุปกรณ์ Edge Device ซึ่งมีสถานการณ์ใช้งานที่ดีขึ้น ดังนั้นเราจึงได้ทำ Phi-3.5-Instruct รอบ INT4 เสร็จแล้ว


## **แหล่งข้อมูล**

1. เรียนรู้เพิ่มเติมเกี่ยวกับ Generative AI extensions สำหรับ onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. แหล่งที่เก็บ Generative AI extensions สำหรับ onnxruntime บน GitHub [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->