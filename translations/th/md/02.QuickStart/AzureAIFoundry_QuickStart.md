<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-05-09T20:11:55+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "th"
}
-->
# **การใช้ Phi-3 ใน Azure AI Foundry**

ด้วยการพัฒนา Generative AI เราหวังว่าจะใช้แพลตฟอร์มเดียวกันในการจัดการ LLM และ SLM ต่างๆ การรวมข้อมูลขององค์กร การปรับแต่ง/การทำ RAG และการประเมินผลธุรกิจองค์กรหลังจากการรวม LLM และ SLM เพื่อให้แอปพลิเคชัน AI อัจฉริยะสามารถใช้งานได้ดีขึ้น [Azure AI Foundry](https://ai.azure.com) เป็นแพลตฟอร์มแอปพลิเคชัน generative AI สำหรับองค์กร

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.th.png)

ด้วย Azure AI Foundry คุณสามารถประเมินคำตอบของ large language model (LLM) และจัดการส่วนประกอบแอปพลิเคชัน prompt ด้วย prompt flow เพื่อประสิทธิภาพที่ดียิ่งขึ้น แพลตฟอร์มนี้ช่วยให้ขยายขนาดได้ง่ายสำหรับการเปลี่ยนจาก proof of concept ไปสู่การผลิตเต็มรูปแบบ การติดตามและปรับปรุงอย่างต่อเนื่องช่วยสนับสนุนความสำเร็จในระยะยาว

เราสามารถติดตั้งโมเดล Phi-3 บน Azure AI Foundry ได้อย่างรวดเร็วผ่านขั้นตอนง่ายๆ จากนั้นใช้ Azure AI Foundry เพื่อทำงาน Playground/Chat, Fine-tuning, การประเมิน และงานที่เกี่ยวข้องกับ Phi-3 ได้

## **1. การเตรียมตัว**

หากคุณมี [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) ติดตั้งในเครื่องอยู่แล้ว การใช้เทมเพลตนี้ก็ง่ายเพียงแค่รันคำสั่งนี้ในไดเรกทอรีใหม่

## การสร้างด้วยตนเอง

การสร้างโปรเจกต์และฮับใน Microsoft Azure AI Foundry เป็นวิธีที่ดีในการจัดระเบียบและจัดการงาน AI ของคุณ นี่คือคำแนะนำทีละขั้นตอนเพื่อเริ่มต้น:

### การสร้างโปรเจกต์ใน Azure AI Foundry

1. **ไปที่ Azure AI Foundry**: ลงชื่อเข้าใช้พอร์ทัล Azure AI Foundry
2. **สร้างโปรเจกต์**:
   - หากคุณอยู่ในโปรเจกต์ ให้เลือก "Azure AI Foundry" ที่มุมบนซ้ายของหน้าเพื่อกลับไปยังหน้าโฮม
   - เลือก "+ Create project"
   - กรอกชื่อโปรเจกต์
   - หากคุณมีฮับ ระบบจะเลือกให้โดยอัตโนมัติ หากคุณมีสิทธิ์เข้าถึงฮับมากกว่าหนึ่ง สามารถเลือกฮับอื่นจากเมนูดรอปดาวน์ได้ หากต้องการสร้างฮับใหม่ เลือก "Create new hub" และกรอกชื่อ
   - เลือก "Create"

### การสร้างฮับใน Azure AI Foundry

1. **ไปที่ Azure AI Foundry**: ลงชื่อเข้าใช้ด้วยบัญชี Azure ของคุณ
2. **สร้างฮับ**:
   - เลือก Management center จากเมนูด้านซ้าย
   - เลือก "All resources" แล้วคลิกลูกศรลงข้าง "+ New project" และเลือก "+ New hub"
   - ในหน้าต่าง "Create a new hub" กรอกชื่อฮับของคุณ (เช่น contoso-hub) และปรับแต่งฟิลด์อื่นตามต้องการ
   - เลือก "Next" ตรวจสอบข้อมูล แล้วเลือก "Create"

สำหรับคำแนะนำอย่างละเอียดเพิ่มเติม คุณสามารถดูได้จาก [เอกสาร Microsoft อย่างเป็นทางการ](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)

หลังจากสร้างเสร็จ คุณสามารถเข้าถึงสตูดิโอที่สร้างผ่าน [ai.azure.com](https://ai.azure.com/)

ใน AI Foundry สามารถมีโปรเจกต์ได้หลายโปรเจกต์ สร้างโปรเจกต์ใน AI Foundry เพื่อเตรียมพร้อม

สร้าง Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. การติดตั้งโมเดล Phi ใน Azure AI Foundry**

คลิกตัวเลือก Explore ของโปรเจกต์เพื่อเข้าสู่ Model Catalog และเลือก Phi-3

เลือก Phi-3-mini-4k-instruct

คลิก 'Deploy' เพื่อติดตั้งโมเดล Phi-3-mini-4k-instruct

> [!NOTE]
>
> คุณสามารถเลือกพลังการประมวลผลเมื่อทำการติดตั้งได้

## **3. Playground Chat Phi ใน Azure AI Foundry**

ไปที่หน้าการติดตั้ง เลือก Playground และแชทกับ Phi-3 ของ Azure AI Foundry

## **4. การติดตั้งโมเดลจาก Azure AI Foundry**

ในการติดตั้งโมเดลจาก Azure Model Catalog คุณสามารถทำตามขั้นตอนนี้:

- ลงชื่อเข้าใช้ Azure AI Foundry
- เลือกโมเดลที่ต้องการติดตั้งจาก Azure AI Foundry model catalog
- ในหน้า Details ของโมเดล เลือก Deploy จากนั้นเลือก Serverless API พร้อม Azure AI Content Safety
- เลือกโปรเจกต์ที่ต้องการติดตั้งโมเดล เพื่อใช้ Serverless API พื้นที่ทำงานของคุณต้องอยู่ในภูมิภาค East US 2 หรือ Sweden Central คุณสามารถกำหนดชื่อ Deployment ได้เอง
- ในตัวช่วยติดตั้ง เลือก Pricing and terms เพื่อศึกษาข้อมูลราคาและเงื่อนไขการใช้งาน
- เลือก Deploy รอจนการติดตั้งเสร็จและถูกนำไปยังหน้า Deployments
- เลือก Open in playground เพื่อเริ่มโต้ตอบกับโมเดล
- คุณสามารถกลับไปที่หน้า Deployments เลือกการติดตั้ง และจดบันทึก Target URL ของ endpoint และ Secret Key ที่ใช้เรียกใช้งานการติดตั้งและสร้างผลลัพธ์
- คุณสามารถดูรายละเอียด endpoint, URL และคีย์การเข้าถึงได้เสมอโดยไปที่แท็บ Build แล้วเลือก Deployments ในส่วน Components

> [!NOTE]
> โปรดทราบว่าบัญชีของคุณต้องมีสิทธิ์ Azure AI Developer role บน Resource Group เพื่อทำขั้นตอนเหล่านี้

## **5. การใช้ Phi API ใน Azure AI Foundry**

คุณสามารถเข้าถึง https://{Your project name}.region.inference.ml.azure.com/swagger.json ผ่าน Postman ด้วยคำสั่ง GET และใช้ร่วมกับ Key เพื่อศึกษาข้อมูลอินเทอร์เฟซที่ให้มา

คุณจะได้รับพารามิเตอร์คำขออย่างสะดวก รวมถึงพารามิเตอร์ตอบกลับด้วย

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับถือเป็นแหล่งข้อมูลที่ถูกต้องและน่าเชื่อถือ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้