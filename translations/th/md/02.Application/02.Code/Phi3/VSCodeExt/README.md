<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-05-09T19:13:29+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "th"
}
-->
# **สร้าง Visual Studio Code GitHub Copilot Chat ของคุณเองด้วย Microsoft Phi-3 Family**

คุณเคยใช้ workspace agent ใน GitHub Copilot Chat หรือไม่? คุณต้องการสร้างโค้ดเอเจนต์สำหรับทีมของคุณเองหรือเปล่า? แลปนี้ออกแบบมาเพื่อผสานโมเดลโอเพนซอร์สเพื่อสร้างเอเจนต์โค้ดระดับองค์กร

## **พื้นฐาน**

### **ทำไมต้องเลือก Microsoft Phi-3**

Phi-3 เป็นซีรีส์ตระกูลหนึ่ง ประกอบด้วย phi-3-mini, phi-3-small และ phi-3-medium ที่ต่างกันตามพารามิเตอร์การฝึกสำหรับการสร้างข้อความ การตอบโต้บทสนทนา และการสร้างโค้ด นอกจากนี้ยังมี phi-3-vision ที่อิงกับ Vision เหมาะสำหรับองค์กรหรือทีมต่าง ๆ ที่ต้องการสร้างโซลูชัน AI สร้างสรรค์แบบออฟไลน์

แนะนำให้อ่านที่ลิงก์นี้ [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

ส่วนขยาย GitHub Copilot Chat มอบอินเทอร์เฟซแชทที่ให้คุณโต้ตอบกับ GitHub Copilot และรับคำตอบเกี่ยวกับการเขียนโค้ดได้โดยตรงภายใน VS Code โดยไม่ต้องเปิดเอกสารหรือค้นหาฟอรัมออนไลน์

Copilot Chat อาจใช้การเน้นไวยากรณ์ การเยื้องบรรทัด และฟีเจอร์จัดรูปแบบอื่น ๆ เพื่อเพิ่มความชัดเจนให้กับคำตอบที่สร้างขึ้น ขึ้นอยู่กับประเภทคำถามจากผู้ใช้ ผลลัพธ์อาจมีลิงก์ไปยังบริบทที่ Copilot ใช้ในการสร้างคำตอบ เช่น ไฟล์ซอร์สโค้ดหรือเอกสาร หรือปุ่มสำหรับเข้าถึงฟังก์ชันของ VS Code

- Copilot Chat ผสานรวมเข้ากับกระบวนการพัฒนาของคุณและช่วยเหลือคุณในจุดที่ต้องการ:

- เริ่มการสนทนาแชทแบบอินไลน์ได้โดยตรงจากตัวแก้ไขหรือเทอร์มินัลเพื่อขอความช่วยเหลือขณะเขียนโค้ด

- ใช้มุมมอง Chat เพื่อมีผู้ช่วย AI ข้าง ๆ ที่ช่วยคุณได้ตลอดเวลา

- เปิด Quick Chat เพื่อถามคำถามด่วนและกลับไปทำงานของคุณได้ทันที

คุณสามารถใช้ GitHub Copilot Chat ในสถานการณ์ต่าง ๆ เช่น:

- ตอบคำถามเกี่ยวกับการเขียนโค้ดเพื่อหาวิธีแก้ปัญหาที่ดีที่สุด

- อธิบายโค้ดของผู้อื่นและแนะนำการปรับปรุง

- เสนอการแก้ไขโค้ด

- สร้างกรณีทดสอบแบบ unit test

- สร้างเอกสารประกอบโค้ด

แนะนำให้อ่านที่ลิงก์นี้ [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

การอ้างอิง **@workspace** ใน Copilot Chat ช่วยให้คุณถามคำถามเกี่ยวกับโค้ดทั้งหมดในโปรเจกต์ของคุณ โดย Copilot จะดึงไฟล์และสัญลักษณ์ที่เกี่ยวข้องมาใช้อย่างชาญฉลาด แล้วอ้างอิงในคำตอบเป็นลิงก์และตัวอย่างโค้ด

เพื่อให้ตอบคำถามได้ **@workspace** จะค้นหาจากแหล่งเดียวกับที่นักพัฒนาจะใช้เมื่อเรียกดูโค้ดใน VS Code:

- ไฟล์ทั้งหมดใน workspace ยกเว้นไฟล์ที่ถูกละเว้นโดยไฟล์ .gitignore

- โครงสร้างไดเรกทอรีพร้อมชื่อโฟลเดอร์และไฟล์ที่ซ้อนกัน

- ดัชนีการค้นหาโค้ดของ GitHub ถ้า workspace เป็นรีโพส GitHub และถูกจัดทำดัชนีโดย code search

- สัญลักษณ์และคำจำกัดความใน workspace

- ข้อความที่เลือกไว้หรือข้อความที่มองเห็นได้ในตัวแก้ไขที่เปิดใช้งาน

หมายเหตุ: .gitignore จะไม่ถูกนำมาพิจารณาหากคุณเปิดไฟล์หรือเลือกข้อความในไฟล์ที่ถูกละเว้น

แนะนำให้อ่านที่ลิงก์นี้ [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **รู้จักแลปนี้เพิ่มเติม**

GitHub Copilot ช่วยเพิ่มประสิทธิภาพการเขียนโปรแกรมขององค์กรอย่างมาก และทุกองค์กรต่างก็ต้องการปรับแต่งฟังก์ชันที่เกี่ยวข้องของ GitHub Copilot หลายองค์กรได้สร้าง Extensions ที่ปรับแต่งเองคล้ายกับ GitHub Copilot โดยอิงตามสถานการณ์ธุรกิจและโมเดลโอเพนซอร์สของตน สำหรับองค์กร Extensions ที่ปรับแต่งเองจะควบคุมได้ง่ายกว่า แต่ก็ส่งผลต่อประสบการณ์ผู้ใช้ เพราะ GitHub Copilot มีฟังก์ชันที่แข็งแกร่งสำหรับสถานการณ์ทั่วไปและความเป็นมืออาชีพ หากสามารถรักษาประสบการณ์ให้สอดคล้องกันได้ จะเป็นการดีสำหรับการปรับแต่ง Extension ขององค์กรเอง GitHub Copilot Chat จึงมี API ที่เกี่ยวข้องให้กับองค์กรเพื่อขยายประสบการณ์การแชท การรักษาประสบการณ์ที่สอดคล้องและมีฟังก์ชันที่ปรับแต่งเองจึงเป็นประสบการณ์ผู้ใช้ที่ดีกว่า

แลปนี้ใช้โมเดล Phi-3 ร่วมกับ NPU ในเครื่องและ Azure แบบไฮบริด เพื่อสร้างเอเจนต์ที่ปรับแต่งเองใน GitHub Copilot Chat ***@PHI3*** เพื่อช่วยนักพัฒนาองค์กรในการสร้างโค้ด***(@PHI3 /gen)*** และสร้างโค้ดจากภาพ ***(@PHI3 /img)***  

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.th.png)

### ***หมายเหตุ:*** 

แลปนี้ขณะนี้ดำเนินการบน AIPC ของ Intel CPU และ Apple Silicon เราจะอัปเดตเวอร์ชัน Qualcomm ของ NPU ต่อไป


## **แลป**

| ชื่อ | คำอธิบาย | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | ตั้งค่าและติดตั้งสภาพแวดล้อมและเครื่องมือที่เกี่ยวข้อง | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | รวมกับ AIPC / Apple Silicon ใช้ NPU ในเครื่องสร้างการสร้างโค้ดผ่าน Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | สร้างโค้ดโดยการดีพลอย Model Catalog ของ Azure Machine Learning Service - Phi-3-vision image | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | สร้างเอเจนต์ Phi-3 ที่ปรับแต่งเองใน GitHub Copilot Chat เพื่อสร้างโค้ด โค้ดกราฟ RAG ฯลฯ | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | ดาวน์โหลดโค้ดตัวอย่าง | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **แหล่งข้อมูล**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. เรียนรู้เพิ่มเติมเกี่ยวกับ GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. เรียนรู้เพิ่มเติมเกี่ยวกับ GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. เรียนรู้เพิ่มเติมเกี่ยวกับ GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. เรียนรู้เพิ่มเติมเกี่ยวกับ Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. เรียนรู้เพิ่มเติมเกี่ยวกับ Model Catalog ของ Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้