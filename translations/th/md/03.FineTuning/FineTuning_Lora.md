<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:32:30+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "th"
}
-->
# **การปรับแต่ง Phi-3 ด้วย Lora**

การปรับแต่งโมเดลภาษา Phi-3 Mini ของ Microsoft โดยใช้ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) บนชุดข้อมูลคำสั่งแชทที่กำหนดเอง

LORA จะช่วยเพิ่มความเข้าใจในการสนทนาและการสร้างคำตอบให้ดีขึ้น

## คู่มือทีละขั้นตอนสำหรับการปรับแต่ง Phi-3 Mini:

**การนำเข้าและการตั้งค่า**

การติดตั้ง loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

เริ่มต้นด้วยการนำเข้าห้องสมุดที่จำเป็น เช่น datasets, transformers, peft, trl และ torch  
ตั้งค่าการบันทึกข้อมูลเพื่อเฝ้าติดตามกระบวนการฝึกสอน

คุณสามารถเลือกปรับแต่งบางเลเยอร์โดยการแทนที่ด้วยเวอร์ชันที่ใช้งานใน loralib ขณะนี้รองรับเฉพาะ nn.Linear, nn.Embedding และ nn.Conv2d เท่านั้น  
นอกจากนี้ยังรองรับ MergedLinear สำหรับกรณีที่ nn.Linear ตัวเดียวแทนเลเยอร์มากกว่าหนึ่งเลเยอร์ เช่น ในบางการใช้งานของ attention qkv projection (ดูหมายเหตุเพิ่มเติมสำหรับรายละเอียด)

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

ก่อนเริ่มลูปการฝึก ให้กำหนดให้พารามิเตอร์ของ LoRA เท่านั้นที่สามารถฝึกได้

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

เมื่อบันทึก checkpoint ให้สร้าง state_dict ที่มีเฉพาะพารามิเตอร์ของ LoRA เท่านั้น

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

เมื่อโหลด checkpoint ด้วย load_state_dict ให้ตั้งค่า strict=False

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ตอนนี้สามารถเริ่มการฝึกได้ตามปกติ

**ไฮเปอร์พารามิเตอร์**

กำหนดพจนานุกรมสองชุด: training_config และ peft_config  
training_config ประกอบด้วยไฮเปอร์พารามิเตอร์สำหรับการฝึก เช่น อัตราการเรียนรู้ ขนาดแบตช์ และการตั้งค่าการบันทึกข้อมูล

peft_config ระบุพารามิเตอร์ที่เกี่ยวข้องกับ LoRA เช่น rank, dropout และประเภทงาน

**การโหลดโมเดลและ Tokenizer**

ระบุเส้นทางไปยังโมเดล Phi-3 ที่ผ่านการฝึกมาแล้ว (เช่น "microsoft/Phi-3-mini-4k-instruct")  
ตั้งค่าการใช้งานโมเดล รวมถึงการใช้แคช ชนิดข้อมูล (bfloat16 สำหรับ mixed precision) และการใช้งาน attention

**การฝึกสอน**

ปรับแต่งโมเดล Phi-3 โดยใช้ชุดข้อมูลคำสั่งแชทที่กำหนดเอง  
ใช้การตั้งค่า LoRA จาก peft_config เพื่อการปรับแต่งที่มีประสิทธิภาพ  
ติดตามความคืบหน้าการฝึกด้วยกลยุทธ์การบันทึกข้อมูลที่กำหนดไว้  
การประเมินผลและการบันทึก: ประเมินโมเดลที่ผ่านการปรับแต่ง  
บันทึก checkpoint ระหว่างการฝึกเพื่อใช้งานในภายหลัง

**ตัวอย่าง**  
- [เรียนรู้เพิ่มเติมด้วยสมุดโน้ตตัวอย่างนี้](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [ตัวอย่างสคริปต์ Python สำหรับ FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [ตัวอย่างการ Fine Tuning บน Hugging Face Hub ด้วย LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [ตัวอย่าง Model Card บน Hugging Face - ตัวอย่าง Fine Tuning ด้วย LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [ตัวอย่างการ Fine Tuning บน Hugging Face Hub ด้วย QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้