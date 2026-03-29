# **สร้าง Visual Studio Code GitHub Copilot Chat ของคุณเองด้วย Microsoft Phi-3 Family**

คุณเคยใช้ workspace agent ใน GitHub Copilot Chat หรือไม่? คุณต้องการสร้างตัวแทนโค้ดของทีมคุณเองหรือไม่? ห้องทดลองนี้หวังว่าจะรวมโมเดลโอเพนซอร์สเพื่อสร้างตัวแทนธุรกิจโค้ดระดับองค์กร

## **พื้นฐาน**

### **ทำไมต้องเลือก Microsoft Phi-3**

Phi-3 เป็นชุดตระกูล ซึ่งรวมถึง phi-3-mini, phi-3-small, และ phi-3-medium โดยอิงจากพารามิเตอร์การฝึกอบรมที่แตกต่างกันสำหรับการสร้างข้อความ การตอบสนองบทสนทนา และการสร้างโค้ด นอกจากนี้ยังมี phi-3-vision ที่อิงจาก Vision เหมาะสำหรับองค์กรหรือทีมต่างๆ ในการสร้างโซลูชัน AI สร้างสรรค์แบบออฟไลน์

แนะนำให้อ่านลิงก์นี้ [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

ส่วนขยาย GitHub Copilot Chat มอบอินเทอร์เฟซแชทที่ช่วยให้คุณโต้ตอบกับ GitHub Copilot และรับคำตอบสำหรับคำถามเกี่ยวกับการเขียนโค้ดโดยตรงภายใน VS Code โดยไม่ต้องสลับไปดูเอกสารหรือค้นหาในฟอรั่มออนไลน์

Copilot Chat อาจใช้การเน้นไวยากรณ์ การเยื้อง และคุณสมบัติการจัดรูปแบบอื่นๆ เพื่อเพิ่มความชัดเจนให้กับการตอบสนองที่สร้างขึ้น ขึ้นอยู่กับประเภทของคำถามจากผู้ใช้ ผลลัพธ์อาจประกอบด้วยลิงก์ไปยังบริบทที่ Copilot ใช้สำหรับการสร้างคำตอบ เช่น ไฟล์ซอร์สโค้ดหรือเอกสาร หรือปุ่มสำหรับเข้าถึงฟังก์ชันการทำงานของ VS Code

- Copilot Chat ผสานรวมในกระบวนการพัฒนาของคุณและให้ความช่วยเหลือตรงที่คุณต้องการ:

- เริ่มการสนทนาแชทแบบอินไลน์จากตัวแก้ไขหรือเทอร์มินัลเพื่อขอความช่วยเหลือขณะเขียนโค้ด

- ใช้มุมมองแชทเพื่อมีผู้ช่วย AI ข้างๆ เพื่อช่วยคุณตลอดเวลา

- เปิด Quick Chat เพื่อถามคำถามด่วนและกลับไปทำงานของคุณต่อ

คุณสามารถใช้ GitHub Copilot Chat ในสถานการณ์ต่างๆ เช่น:

- ตอบคำถามเกี่ยวกับการเขียนโค้ดว่าจะแก้ปัญหาได้ดีที่สุดอย่างไร

- อธิบายโค้ดของผู้อื่นและแนะนำการปรับปรุง

- เสนอการแก้ไขโค้ด

- สร้างกรณีทดสอบหน่วย

- สร้างเอกสารโค้ด

แนะนำให้อ่านลิงก์นี้ [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

การอ้างอิง **@workspace** ใน Copilot Chat ช่วยให้คุณถามคำถามเกี่ยวกับโค้ดฐานข้อมูลทั้งหมดของคุณได้ ตามคำถาม Copilot จะดึงไฟล์และสัญลักษณ์ที่เกี่ยวข้องอย่างชาญฉลาด ซึ่งจากนั้นจะแสดงในคำตอบของมันเป็นลิงก์และตัวอย่างโค้ด

ในการตอบคำถามของคุณ **@workspace** จะค้นหาผ่านแหล่งข้อมูลเดียวกับที่นักพัฒนาจะใช้เมื่อเรียกดูโค้ดฐานข้อมูลใน VS Code:

- ไฟล์ทั้งหมดใน workspace ยกเว้นไฟล์ที่ถูกละเว้นโดยไฟล์ .gitignore

- โครงสร้างไดเรกทอรีพร้อมโฟลเดอร์และชื่อไฟล์ที่ซ้อนกัน

- ดัชนีการค้นหาโค้ดของ GitHub หาก workspace เป็น repository บน GitHub และถูกจัดทำดัชนีโดยโค้ดเซิร์ช

- สัญลักษณ์และคำจำกัดความใน workspace

- ข้อความที่เลือกในปัจจุบันหรือข้อความที่มองเห็นในตัวแก้ไขที่เปิดใช้งาน

หมายเหตุ: .gitignore จะถูกข้ามไปหากคุณเปิดไฟล์หรือเลือกข้อความภายในไฟล์ที่ถูกละเว้น

แนะนำให้อ่านลิงก์นี้ [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **รู้จักห้องทดลองนี้เพิ่มเติม**

GitHub Copilot ได้ปรับปรุงประสิทธิภาพการเขียนโปรแกรมขององค์กรอย่างมาก และทุกองค์กรหวังที่จะปรับแต่งฟังก์ชันที่เกี่ยวข้องของ GitHub Copilot องค์กรหลายแห่งได้ปรับแต่ง Extensions ที่คล้ายกับ GitHub Copilot โดยอิงจากสถานการณ์ธุรกิจและโมเดลโอเพนซอร์สของตนเอง สำหรับองค์กร Extensions ที่ปรับแต่งเองจะควบคุมได้ง่ายกว่า แต่สิ่งนี้ก็มีผลต่อประสบการณ์ผู้ใช้เช่นกัน เพราะท้ายที่สุด GitHub Copilot มีฟังก์ชันที่แข็งแกร่งกว่าในการจัดการกับสถานการณ์ทั่วไปและความเป็นมืออาชีพ หากประสบการณ์ยังคงสอดคล้องกัน จะดีกว่าที่จะปรับแต่ง Extension ขององค์กรเอง GitHub Copilot Chat ให้ APIs ที่เกี่ยวข้องสำหรับองค์กรขยายประสบการณ์การแชท การรักษาประสบการณ์ที่สอดคล้องกันและมีฟังก์ชันที่ปรับแต่งเองคือประสบการณ์ผู้ใช้ที่ดีกว่า

ห้องทดลองนี้ส่วนใหญ่ใช้โมเดล Phi-3 ร่วมกับ NPU ในเครื่องและ Azure แบบไฮบริดในการสร้าง Agent ปรับแต่งใน GitHub Copilot Chat ***@PHI3*** เพื่อช่วยนักพัฒนาองค์กรในการสร้างโค้ด***(@PHI3 /gen)*** และสร้างโค้ดโดยอิงจากภาพ ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/th/cover.1017ebc9a7c46d09.webp)

### ***หมายเหตุ:*** 

ห้องทดลองนี้ดำเนินการในขณะนี้บน AIPC ของ Intel CPU และ Apple Silicon เราจะอัปเดตเวอร์ชัน Qualcomm ของ NPU ต่อไป


## **ห้องทดลอง**


| ชื่อ | คำอธิบาย | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - การติดตั้ง(✅) | กำหนดค่าและติดตั้งสภาพแวดล้อมและเครื่องมือติดตั้งที่เกี่ยวข้อง | [ไปที่](./HOL/AIPC/01.Installations.md) |[ไปที่](./HOL/Apple/01.Installations.md) |
| Lab1 - รัน Prompt flow กับ Phi-3-mini (✅) | ร่วมกับ AIPC / Apple Silicon ใช้ NPU ในเครื่องสร้างโค้ดผ่าน Phi-3-mini | [ไปที่](./HOL/AIPC/02.PromptflowWithNPU.md) |  [ไปที่](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - ติดตั้ง Phi-3-vision บน Azure Machine Learning Service(✅) | สร้างโค้ดโดยการติดตั้ง Model Catalog ของ Azure Machine Learning Service - Phi-3-vision image | [ไปที่](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[ไปที่](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - สร้าง @phi-3 agent ใน GitHub Copilot Chat(✅)  | สร้างตัวแทน Phi-3 ปรับแต่งใน GitHub Copilot Chat เพื่อสร้างโค้ด กราฟโค้ด RAG ฯลฯ | [ไปที่](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [ไปที่](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| ตัวอย่างโค้ด (✅)  | ดาวน์โหลดตัวอย่างโค้ด | [ไปที่](../../../../../../../code/07.Lab/01/AIPC) | [ไปที่](../../../../../../../code/07.Lab/01/Apple) |


## **ทรัพยากร**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. เรียนรู้เพิ่มเติมเกี่ยวกับ GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. เรียนรู้เพิ่มเติมเกี่ยวกับ GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. เรียนรู้เพิ่มเติมเกี่ยวกับ GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. เรียนรู้เพิ่มเติมเกี่ยวกับ Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. เรียนรู้เพิ่มเติมเกี่ยวกับ Model Catalog ของ Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้เกิดความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องได้ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญทางภาษา เรายินยอมไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->