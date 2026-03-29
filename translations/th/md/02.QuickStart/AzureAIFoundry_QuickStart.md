# **การใช้ Phi-3 ใน Microsoft Foundry**

ด้วยการพัฒนา Generative AI เราหวังว่าจะใช้แพลตฟอร์มแบบรวมเพื่อจัดการ LLM และ SLM ต่าง ๆ การรวมข้อมูลองค์กร การปรับแต่ง/การทำ RAG และการประเมินธุรกิจองค์กรหลังจากการรวม LLM และ SLM เป็นต้น เพื่อให้แอปพลิเคชัน generative AI ถูกนำไปใช้ได้ดีขึ้น [Microsoft Foundry](https://ai.azure.com) เป็นแพลตฟอร์มแอปพลิเคชัน generative AI ระดับองค์กร

![aistudo](../../../../translated_images/th/aifoundry_home.f28a8127c96c7d93.webp)

ด้วย Microsoft Foundry คุณสามารถประเมินผลการตอบสนองของโมเดลภาษาใหญ่ (LLM) และจัดการส่วนประกอบของแอปพลิเคชัน prompt ด้วย prompt flow เพื่อประสิทธิภาพที่ดียิ่งขึ้น แพลตฟอร์มนี้ช่วยให้สามารถขยายสเกลจากการทดสอบแนวคิดสู่การผลิตเต็มรูปแบบได้อย่างง่ายดาย พร้อมการตรวจสอบและปรับปรุงอย่างต่อเนื่องเพื่อความสำเร็จในระยะยาว

เราสามารถ deploy โมเดล Phi-3 บน Microsoft Foundry ได้อย่างรวดเร็วผ่านขั้นตอนง่าย ๆ จากนั้นใช้ Microsoft Foundry ทำงานที่เกี่ยวข้องกับ Phi-3 เช่น Playground/Chat, Fine-tuning, การประเมินผล และงานอื่น ๆ

## **1. การเตรียมตัว**

หากคุณติดตั้ง [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) ไว้แล้วบนเครื่องของคุณ การใช้เทมเพลตนี้ก็แค่รันคำสั่งนี้ในไดเรกทอรีใหม่เท่านั้น

## การสร้างด้วยตนเอง

การสร้างโปรเจกต์และ hub ใน Microsoft Foundry เป็นวิธีที่ดีในการจัดระเบียบและจัดการงาน AI ของคุณ นี่คือคำแนะนำทีละขั้นตอนเพื่อเริ่มต้น:

### การสร้างโปรเจกต์ใน Microsoft Foundry

1. **ไปที่ Microsoft Foundry**: ลงชื่อเข้าใช้พอร์ทัล Microsoft Foundry
2. **สร้างโปรเจกต์**:
   - หากคุณอยู่ในโปรเจกต์ ให้เลือก "Microsoft Foundry" ที่ด้านบนซ้ายของหน้าเพื่อไปที่หน้าโฮม
   - เลือก "+ Create project"
   - กรอกชื่อโปรเจกต์
   - หากคุณมี hub อยู่แล้ว จะถูกเลือกโดยอัตโนมัติ หากคุณเข้าถึง hub มากกว่าหนึ่งที่ คุณสามารถเลือก hub อื่นจากเมนูดรอปดาวน์ หากต้องการสร้าง hub ใหม่ ให้เลือก "Create new hub" และกรอกชื่อ
   - เลือก "Create"

### การสร้าง Hub ใน Microsoft Foundry

1. **ไปที่ Microsoft Foundry**: ลงชื่อเข้าใช้ด้วยบัญชี Azure ของคุณ
2. **สร้าง Hub**:
   - เลือกศูนย์จัดการ (Management center) จากเมนูด้านซ้าย
   - เลือก "All resources" จากนั้นคลิกลูกศรลงข้าง "+ New project" และเลือก "+ New hub"
   - ในกล่องโต้ตอบ "Create a new hub" ให้กรอกชื่อ hub ของคุณ (เช่น contoso-hub) และแก้ไขข้อมูลอื่น ๆ ตามต้องการ
   - เลือก "Next" ตรวจสอบข้อมูล แล้วเลือก "Create"

สำหรับคำแนะนำที่ละเอียดขึ้น คุณสามารถดูได้ที่ [เอกสาร Microsoft อย่างเป็นทางการ](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects)

หลังจากสร้างเสร็จสมบูรณ์แล้ว คุณสามารถเข้าถึงสตูดิโอที่คุณสร้างผ่าน [ai.azure.com](https://ai.azure.com/)

สามารถมีโปรเจกต์หลายโปรเจกต์บน AI Foundry สร้างโปรเจกต์ใน AI Foundry เพื่อเตรียมตัว

สร้าง Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. การนำโมเดล Phi ไปใช้งานบน Microsoft Foundry**

คลิกตัวเลือก Explore ของโปรเจกต์เพื่อเข้าสู่ Model Catalog และเลือก Phi-3

เลือก Phi-3-mini-4k-instruct

คลิก 'Deploy' เพื่อ deploy โมเดล Phi-3-mini-4k-instruct

> [!NOTE]
>
> คุณสามารถเลือกกำลังคำนวณเมื่อนำไปใช้งาน

## **3. Playground Chat Phi ใน Microsoft Foundry**

ไปที่หน้าการนำไปใช้งาน เลือก Playground และแชทกับ Phi-3 ของ Microsoft Foundry

## **4. การ deploy โมเดลจาก Microsoft Foundry**

เมื่อต้องการ deploy โมเดลจาก Azure Model Catalog ให้ทำตามขั้นตอนดังนี้:

- ลงชื่อเข้าใช้ Microsoft Foundry
- เลือกโมเดลที่ต้องการ deploy จาก Microsoft Foundry model catalog
- ในหน้ารายละเอียดโมเดล ให้เลือก Deploy จากนั้นเลือก Serverless API พร้อม Azure AI Content Safety
- เลือกโปรเจกต์ที่จะ deploy โมเดล ในการใช้ Serverless API นี้ workspace ของคุณต้องอยู่ในภูมิภาค East US 2 หรือ Sweden Central คุณสามารถตั้งชื่อ Deployment ได้เอง
- ในตัวช่วย deploy ให้เลือก Pricing and terms เพื่อเรียนรู้เกี่ยวกับราคาและเงื่อนไขการใช้งาน
- เลือก Deploy รอจน deployment พร้อมและถูกเปลี่ยนเส้นทางไปที่หน้าการ Deployments
- เลือก Open in playground เพื่อเริ่มต้นโต้ตอบกับโมเดล
- คุณสามารถกลับไปที่หน้าการ Deployments เลือก deployment และจดบันทึก Target URL และ Secret Key ซึ่งสามารถใช้เรียก deployment เพื่อสร้างผลลัพธ์
- คุณสามารถค้นหารายละเอียดของ endpoint, URL และคีย์การเข้าถึงได้เสมอโดยไปที่แท็บ Build และเลือก Deployments จากส่วน Components

> [!NOTE]
> โปรดทราบว่าบัญชีของคุณต้องมีสิทธิ์ Azure AI Developer role บน Resource Group เพื่อดำเนินการตามขั้นตอนเหล่านี้

## **5. การใช้ Phi API ใน Microsoft Foundry**

คุณสามารถเข้าถึง https://{Your project name}.region.inference.ml.azure.com/swagger.json ผ่าน Postman GET และผสานกับ Key เพื่อเรียนรู้เกี่ยวกับอินเทอร์เฟซที่มีให้

คุณสามารถรับพารามิเตอร์คำขอได้อย่างสะดวก รวมถึงพารามิเตอร์การตอบสนองด้วย

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงที่สุด โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งอ้างอิงหลัก สำหรับข้อมูลที่มีความสำคัญ ควรใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เรายังไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->