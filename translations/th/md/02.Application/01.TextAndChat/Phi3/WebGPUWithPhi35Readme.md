<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:57:51+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "th"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## ตัวอย่างสาธิตการใช้งาน WebGPU และรูปแบบ RAG

รูปแบบ RAG กับโมเดล Phi-3.5 Onnx Hosted ใช้วิธี Retrieval-Augmented Generation ที่ผสานพลังของโมเดล Phi-3.5 กับการโฮสต์ ONNX เพื่อการใช้งาน AI ที่มีประสิทธิภาพ รูปแบบนี้มีบทบาทสำคัญในการปรับแต่งโมเดลสำหรับงานเฉพาะด้าน โดยให้ความสมดุลระหว่างคุณภาพ ต้นทุน และความเข้าใจเนื้อหายาว ๆ เป็นส่วนหนึ่งของชุด Azure AI ที่มีโมเดลหลากหลายซึ่งหา ทดลอง และใช้งานได้ง่าย ตอบโจทย์การปรับแต่งในอุตสาหกรรมต่าง ๆ

## WebGPU คืออะไร
WebGPU คือ API กราฟิกเว็บสมัยใหม่ที่ออกแบบมาเพื่อให้เข้าถึงหน่วยประมวลผลกราฟิก (GPU) ของอุปกรณ์ได้อย่างมีประสิทธิภาพโดยตรงจากเว็บเบราว์เซอร์ โดยมีเป้าหมายเป็นตัวแทนของ WebGL พร้อมการปรับปรุงสำคัญหลายประการ:

1. **รองรับ GPU สมัยใหม่**: WebGPU ถูกสร้างมาให้ทำงานได้อย่างราบรื่นกับสถาปัตยกรรม GPU ยุคใหม่ โดยใช้ API ของระบบอย่าง Vulkan, Metal และ Direct3D 12
2. **ประสิทธิภาพที่ดีขึ้น**: รองรับการประมวลผลทั่วไปบน GPU และการทำงานที่รวดเร็วขึ้น เหมาะทั้งสำหรับการเรนเดอร์กราฟิกและงานด้าน machine learning
3. **ฟีเจอร์ขั้นสูง**: WebGPU ให้การเข้าถึงความสามารถของ GPU ที่ซับซ้อนและไดนามิกมากขึ้น รองรับงานกราฟิกและการคำนวณที่ซับซ้อนกว่าเดิม
4. **ลดภาระงานของ JavaScript**: โดยการย้ายงานไปที่ GPU มากขึ้น WebGPU ช่วยลดภาระของ JavaScript ทำให้ประสิทธิภาพดีขึ้นและประสบการณ์ใช้งานลื่นไหลกว่าเดิม

ปัจจุบัน WebGPU รองรับในเบราว์เซอร์อย่าง Google Chrome และกำลังขยายการรองรับไปยังแพลตฟอร์มอื่น ๆ

### 03.WebGPU
สภาพแวดล้อมที่ต้องการ:

**เบราว์เซอร์ที่รองรับ:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly

### เปิดใช้งาน WebGPU:

- ใน Chrome/Microsoft Edge  

เปิดใช้งาน `chrome://flags/#enable-unsafe-webgpu` flag

#### เปิดเบราว์เซอร์ของคุณ:
เปิด Google Chrome หรือ Microsoft Edge

#### เข้าสู่หน้าธง:
พิมพ์ `chrome://flags` ในแถบที่อยู่แล้วกด Enter

#### ค้นหาธง:
ในช่องค้นหาด้านบนของหน้า พิมพ์ 'enable-unsafe-webgpu'

#### เปิดใช้งานธง:
ค้นหา #enable-unsafe-webgpu ในรายการผลลัพธ์

คลิกเมนูแบบเลื่อนลงข้าง ๆ แล้วเลือก Enabled

#### รีสตาร์ทเบราว์เซอร์ของคุณ:

หลังจากเปิดใช้งานธงแล้ว คุณต้องรีสตาร์ทเบราว์เซอร์เพื่อให้การเปลี่ยนแปลงมีผล คลิกปุ่ม Relaunch ที่ปรากฏด้านล่างของหน้า

- สำหรับ Linux ให้เปิดเบราว์เซอร์ด้วย `--enable-features=Vulkan`  
- Safari 18 (macOS 15) เปิดใช้งาน WebGPU มาโดยค่าเริ่มต้น  
- ใน Firefox Nightly ให้พิมพ์ about:config ในแถบที่อยู่แล้ว `set dom.webgpu.enabled to true`

### การตั้งค่า GPU สำหรับ Microsoft Edge

ขั้นตอนการตั้งค่า GPU ประสิทธิภาพสูงสำหรับ Microsoft Edge บน Windows:

- **เปิดการตั้งค่า:** คลิกเมนู Start แล้วเลือก Settings  
- **การตั้งค่าระบบ:** ไปที่ System แล้วเลือก Display  
- **การตั้งค่ากราฟิก:** เลื่อนลงแล้วคลิก Graphics settings  
- **เลือกแอป:** ใน “Choose an app to set preference” เลือก Desktop app แล้วคลิก Browse  
- **เลือก Edge:** ไปยังโฟลเดอร์ติดตั้ง Edge (โดยปกติ `C:\Program Files (x86)\Microsoft\Edge\Application`) แล้วเลือก `msedge.exe`  
- **ตั้งค่าความต้องการ:** คลิก Options เลือก High performance แล้วคลิก Save  
ขั้นตอนนี้จะทำให้ Microsoft Edge ใช้ GPU ประสิทธิภาพสูงของคุณเพื่อประสิทธิภาพที่ดีกว่า  
- **รีสตาร์ท** เครื่องเพื่อให้การตั้งค่ามีผล

### ตัวอย่าง: โปรด [คลิกลิงก์นี้](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้