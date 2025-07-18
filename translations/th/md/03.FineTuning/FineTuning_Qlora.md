<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:19:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "th"
}
-->
**การปรับแต่ง Phi-3 ด้วย QLoRA**

การปรับแต่งโมเดลภาษา Phi-3 Mini ของ Microsoft โดยใช้ [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)

QLoRA จะช่วยเพิ่มความเข้าใจในการสนทนาและการสร้างคำตอบ

ในการโหลดโมเดลแบบ 4 บิตด้วย transformers และ bitsandbytes คุณต้องติดตั้ง accelerate และ transformers จากซอร์สโค้ด และตรวจสอบให้แน่ใจว่าคุณมีเวอร์ชันล่าสุดของไลบรารี bitsandbytes

**ตัวอย่าง**
- [เรียนรู้เพิ่มเติมด้วยสมุดบันทึกตัวอย่างนี้](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [ตัวอย่างสคริปต์ Python สำหรับการปรับแต่ง](../../../../code/03.Finetuning/FineTrainingScript.py)
- [ตัวอย่างการปรับแต่งบน Hugging Face Hub ด้วย LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [ตัวอย่างการปรับแต่งบน Hugging Face Hub ด้วย QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้