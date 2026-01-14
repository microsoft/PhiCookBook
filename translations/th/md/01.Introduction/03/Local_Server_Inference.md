<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:57:29+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "th"
}
-->
# **การใช้งาน Inference Phi-3 บนเซิร์ฟเวอร์ภายในเครื่อง**

เราสามารถติดตั้ง Phi-3 บนเซิร์ฟเวอร์ภายในเครื่องได้ ผู้ใช้สามารถเลือกใช้โซลูชันจาก [Ollama](https://ollama.com) หรือ [LM Studio](https://llamaedge.com) หรือตัวเลือกเขียนโค้ดเองก็ได้ คุณสามารถเชื่อมต่อบริการ Phi-3 ภายในเครื่องผ่าน [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) หรือ [Langchain](https://www.langchain.com/) เพื่อสร้างแอปพลิเคชัน Copilot

## **ใช้ Semantic Kernel เพื่อเข้าถึง Phi-3-mini**

ในแอปพลิเคชัน Copilot เราสร้างแอปผ่าน Semantic Kernel / LangChain โครงสร้างแอปประเภทนี้โดยทั่วไปรองรับ Azure OpenAI Service / โมเดล OpenAI และยังรองรับโมเดลโอเพนซอร์สบน Hugging Face รวมถึงโมเดลภายในเครื่องอีกด้วย ถ้าเราต้องการใช้ Semantic Kernel เพื่อเข้าถึง Phi-3-mini ควรทำอย่างไร? โดยใช้ .NET เป็นตัวอย่าง เราสามารถผสานกับ Hugging Face Connector ใน Semantic Kernel ได้ โดยค่าเริ่มต้นจะเชื่อมต่อกับ model id บน Hugging Face (ครั้งแรกที่ใช้งาน โมเดลจะถูกดาวน์โหลดจาก Hugging Face ซึ่งใช้เวลานาน) นอกจากนี้ยังสามารถเชื่อมต่อกับบริการที่ติดตั้งภายในเครื่องได้ เมื่อเทียบกันแล้ว เราแนะนำให้ใช้แบบหลังเพราะมีความเป็นอิสระสูงกว่า โดยเฉพาะอย่างยิ่งในแอปพลิเคชันสำหรับองค์กร

![sk](../../../../../translated_images/th/sk.d03785c25edc6d44.png)

จากภาพ การเข้าถึงบริการภายในเครื่องผ่าน Semantic Kernel สามารถเชื่อมต่อกับเซิร์ฟเวอร์โมเดล Phi-3-mini ที่สร้างขึ้นเองได้อย่างง่ายดาย นี่คือตัวอย่างผลลัพธ์ที่รัน

![skrun](../../../../../translated_images/th/skrun.5aafc1e7197dca20.png)

***Sample Code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้