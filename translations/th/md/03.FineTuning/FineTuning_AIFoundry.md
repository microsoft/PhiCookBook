# การปรับแต่ง Phi-3 ด้วย Microsoft Foundry

 มาสำรวจวิธีการปรับแต่งโมเดลภาษา Phi-3 Mini ของ Microsoft โดยใช้ Microsoft Foundry การปรับแต่งช่วยให้คุณสามารถปรับ Phi-3 Mini ให้เหมาะสมกับงานเฉพาะ ทำให้มีความสามารถและความเข้าใจบริบทที่มากขึ้น

## ข้อควรพิจารณา

- **ความสามารถ:** โมเดลใดบ้างที่สามารถปรับแต่งได้? โมเดลฐานสามารถปรับเพื่อทำอะไรได้บ้าง?
- **ค่าใช้จ่าย:** รูปแบบการคิดราคาสำหรับการปรับแต่งเป็นอย่างไร
- **ความสามารถในการปรับแต่ง:** ฉันสามารถแก้ไขโมเดลฐานได้มากน้อยแค่ไหน – และในรูปแบบใดบ้าง?
- **ความสะดวก:** การปรับแต่งเกิดขึ้นอย่างไร – ฉันต้องเขียนโค้ดเองไหม? ต้องเตรียมทรัพยากรคอมพิวเตอร์เองไหม?
- **ความปลอดภัย:** โมเดลที่ได้รับการปรับแต่งมักมีความเสี่ยงด้านความปลอดภัย – มีมาตรการป้องกันเพื่อป้องกันความเสียหายที่ไม่คาดคิดหรือไม่?

![AIFoundry Models](../../../../translated_images/th/AIFoundryModels.0e1b16f7d0b09b73.webp)

## การเตรียมความพร้อมสำหรับการปรับแต่ง

### ข้อกำหนดเบื้องต้น

> [!NOTE]
> สำหรับโมเดลในตระกูล Phi-3 บริการปรับแต่งแบบจ่ายตามการใช้งานจะพร้อมใช้งานเฉพาะกับฮับที่สร้างในภูมิภาค **East US 2** เท่านั้น

- มีการสมัครใช้งาน Azure หากคุณยังไม่มีการสมัครใช้งาน Azure ให้สร้าง [บัญชี Azure ที่ชำระเงิน](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) เพื่อเริ่มต้น

- มี [โปรเจค AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)
- ใช้การควบคุมการเข้าถึงตามบทบาทของ Azure (Azure RBAC) เพื่อให้สิทธิ์ในการดำเนินการใน Microsoft Foundry เพื่อทำตามขั้นตอนในบทความนี้ บัญชีผู้ใช้ของคุณต้องได้รับมอบหมาย __บทบาท Azure AI Developer__ บนกลุ่มทรัพยากร

### การลงทะเบียนผู้ให้บริการสำหรับการสมัครใช้งาน

ตรวจสอบว่าการสมัครใช้งานถูกลงทะเบียนกับผู้ให้บริการทรัพยากร `Microsoft.Network` แล้ว

1. ลงชื่อเข้าใช้ [Azure portal](https://portal.azure.com)
1. เลือก **Subscriptions** จากเมนูด้านซ้าย
1. เลือกการสมัครใช้งานที่ต้องการใช้
1. เลือก **AI project settings** > **Resource providers** จากเมนูด้านซ้าย
1. ยืนยันว่า **Microsoft.Network** อยู่ในรายชื่อผู้ให้บริการทรัพยากร หากไม่อยู่ให้เพิ่มเข้าไป

### การเตรียมข้อมูล

เตรียมข้อมูลฝึกสอนและข้อมูลตรวจสอบสำหรับการปรับแต่งโมเดล ข้อมูลฝึกสอนและข้อมูลตรวจสอบประกอบด้วยตัวอย่างอินพุตและเอาต์พุตสำหรับวิธีที่คุณต้องการให้โมเดลทำงาน

ตรวจสอบให้แน่ใจว่าตัวอย่างการฝึกทั้งหมดของคุณอยู่ในรูปแบบที่คาดหวังสำหรับการอนุมาน เพื่อปรับแต่งโมเดลอย่างมีประสิทธิภาพ ให้แน่ใจว่าชุดข้อมูลมีความสมดุลและหลากหลาย

ซึ่งรวมถึงการรักษาสมดุลของข้อมูล การรวมสถานการณ์ต่างๆ และการปรับปรุงข้อมูลฝึกสอนเป็นระยะเพื่อให้สอดคล้องกับความคาดหวังในโลกจริง ซึ่งสุดท้ายจะนำไปสู่คำตอบของโมเดลที่แม่นยำและสมดุลมากขึ้น

โมเดลแต่ละประเภทต้องการรูปแบบข้อมูลการฝึกสอนที่แตกต่างกัน

### การสนทนาแบบเติมเต็ม (Chat Completion)

ข้อมูลฝึกสอนและตรวจสอบที่คุณใช้ **จะต้อง** อยู่ในรูปแบบเอกสาร JSON Lines (JSONL) สำหรับ `Phi-3-mini-128k-instruct` ชุดข้อมูลสำหรับการปรับแต่งต้องอยู่ในรูปแบบสนทนาเดียวกับ API สำหรับการสนทนาแบบเติมเต็ม (Chat completions)

### ตัวอย่างรูปแบบไฟล์

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

ประเภทไฟล์ที่รองรับคือ JSON Lines ไฟล์จะถูกอัปโหลดไปยังที่เก็บข้อมูลเริ่มต้นและพร้อมใช้งานในโปรเจคของคุณ

## การปรับแต่ง Phi-3 ด้วย Microsoft Foundry

Microsoft Foundry ช่วยให้คุณปรับแต่งโมเดลภาษาขนาดใหญ่กับชุดข้อมูลส่วนตัวของคุณโดยใช้กระบวนการที่เรียกว่าการปรับแต่ง การปรับแต่งให้คุณค่าอย่างมากโดยช่วยให้ปรับแต่งและเพิ่มประสิทธิภาพสำหรับงานและแอปพลิเคชันเฉพาะ นำไปสู่ประสิทธิภาพที่ดีขึ้น ประหยัดค่าใช้จ่าย ลดระยะเวลาหน่วง และผลลัพธ์ที่ตรงกับความต้องการ

![Finetune AI Foundry](../../../../translated_images/th/AIFoundryfinetune.193aaddce48d553c.webp)

### สร้างโปรเจคใหม่

1. ลงชื่อเข้าใช้ [Microsoft Foundry](https://ai.azure.com)

1. เลือก **+New project** เพื่อสร้างโปรเจคใหม่ใน Microsoft Foundry

    ![FineTuneSelect](../../../../translated_images/th/select-new-project.cd31c0404088d7a3.webp)

1. ดำเนินการตามขั้นตอนดังนี้:

    - ตั้งชื่อ **Hub name** สำหรับโปรเจค ต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือก **Hub** ที่ต้องการใช้ (สร้างใหม่ถ้าจำเป็น)

    ![FineTuneSelect](../../../../translated_images/th/create-project.ca3b71298b90e420.webp)

1. ดำเนินการตามขั้นตอนดังนี้เพื่อสร้างฮับใหม่:

    - กรอก **Hub name** ต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือกการสมัครใช้งาน Azure ของคุณ (**Subscription**)
    - เลือกกลุ่มทรัพยากร (**Resource group**) ที่ต้องการใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือกตำแหน่งที่ตั้ง (**Location**) ที่ต้องการใช้
    - เลือก **Connect Azure AI Services** ที่ต้องการใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Connect Azure AI Search** เป็น **Skip connecting**

    ![FineTuneSelect](../../../../translated_images/th/create-hub.49e53d235e80779e.webp)

1. เลือก **Next**
1. เลือก **Create a project**

### การเตรียมข้อมูล

ก่อนลงมือปรับแต่ง รวบรวมหรือสร้างชุดข้อมูลที่เกี่ยวข้องกับงานของคุณ เช่น คำสั่งสนทนา คู่คำถาม-คำตอบ หรือข้อมูลข้อความอื่น ๆ ที่เกี่ยวข้อง ทำความสะอาดและเตรียมข้อมูลนี้โดยการกำจัดเสียงรบกวน จัดการค่าที่หายไป และทำการตัดคำ

### การปรับแต่งโมเดล Phi-3 ใน Microsoft Foundry

> [!NOTE]
> การปรับแต่งโมเดล Phi-3 รองรับเฉพาะโปรเจคที่ตั้งอยู่ใน East US 2 เท่านั้น

1. เลือก **Model catalog** จากแท็บด้านซ้าย

1. พิมพ์ *phi-3* ใน **ช่องค้นหา** และเลือกโมเดล phi-3 ที่คุณต้องการใช้

    ![FineTuneSelect](../../../../translated_images/th/select-model.60ef2d4a6a3cec57.webp)

1. เลือก **Fine-tune**

    ![FineTuneSelect](../../../../translated_images/th/select-finetune.a976213b543dd9d8.webp)

1. กรอกชื่อ **Fine-tuned model name**

    ![FineTuneSelect](../../../../translated_images/th/finetune1.c2b39463f0d34148.webp)

1. เลือก **Next**

1. ดำเนินการตามขั้นตอนดังนี้:

    - เลือก **task type** เป็น **Chat completion**
    - เลือก **Training data** ที่ต้องการใช้ คุณสามารถอัปโหลดผ่านข้อมูลของ Microsoft Foundry หรือจากเครื่องของคุณ

    ![FineTuneSelect](../../../../translated_images/th/finetune2.43cb099b1a94442d.webp)

1. เลือก **Next**

1. อัปโหลด **Validation data** ที่ต้องการใช้ หรือเลือก **Automatic split of training data**

    ![FineTuneSelect](../../../../translated_images/th/finetune3.fd96121b67dcdd92.webp)

1. เลือก **Next**

1. ดำเนินการตามขั้นตอนดังนี้:

    - เลือก **Batch size multiplier** ที่ต้องการใช้
    - เลือก **Learning rate** ที่ต้องการใช้
    - เลือก **Epochs** ที่ต้องการใช้

    ![FineTuneSelect](../../../../translated_images/th/finetune4.e18b80ffccb5834a.webp)

1. เลือก **Submit** เพื่อเริ่มกระบวนการปรับแต่ง

    ![FineTuneSelect](../../../../translated_images/th/select-submit.0a3802d581bac271.webp)

1. เมื่อตัวแบบของคุณถูกปรับแต่งเรียบร้อยแล้ว สถานะจะแสดงเป็น **Completed** ดังภาพด้านล่าง ตอนนี้คุณสามารถนำโมเดลไปใช้งานในแอปพลิเคชันของคุณเอง ใน playground หรือใน prompt flow สำหรับข้อมูลเพิ่มเติม ดูที่ [วิธีการนำ Phi-3 family ของโมเดลภาษาขนาดเล็กไปใช้กับ Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)

    ![FineTuneSelect](../../../../translated_images/th/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการปรับแต่ง Phi-3 โปรดเยี่ยมชม [การปรับแต่งโมเดล Phi-3 ใน Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)

## การลบโมเดลที่ปรับแต่งแล้ว

คุณสามารถลบโมเดลที่ปรับแต่งแล้วจากรายการโมเดลปรับแต่งใน [Microsoft Foundry](https://ai.azure.com) หรือจากหน้ารายละเอียดโมเดล เลือกโมเดลที่ต้องการลบจากหน้าการปรับแต่ง แล้วเลือกปุ่มลบเพื่อทำการลบโมเดล

> [!NOTE]
> คุณไม่สามารถลบโมเดลที่สร้างขึ้นเองได้หากมีการใช้งานในdeployment อยู่ก่อน คุณต้องลบการใช้งานโมเดลนั้นก่อนถึงจะลบโมเดลได้

## ค่าใช้จ่ายและโควต้า

### ข้อควรพิจารณาค่าใช้จ่ายและโควต้าสำหรับโมเดล Phi-3 ที่ปรับแต่งเป็นบริการ

โมเดล Phi ที่ปรับแต่งเป็นบริการได้รับการเสนอโดย Microsoft และผสานรวมกับ Microsoft Foundry เพื่อใช้งาน คุณสามารถดูราคาตอน [การนำไปใช้งาน](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) หรือปรับแต่งโมเดลได้ที่แท็บ Pricing and terms ในตัวช่วยการนำไปใช้งาน

## การกรองเนื้อหา

โมเดลที่นำไปใช้งานเป็นบริการแบบจ่ายตามการใช้งานจะได้รับการปกป้องโดย Azure AI Content Safety เมื่อเปิดใช้งานที่ endpoints แบบเรียลไทม์ คุณสามารถเลือกไม่เปิดใช้งานความสามารถนี้ได้ เมื่อเปิดใช้งาน Azure AI content safety ทั้ง prompt และ completion จะผ่านระบบจำแนกประเภทที่ออกแบบมาเพื่อตรวจจับและป้องกันการแสดงเนื้อหาที่เป็นอันตราย ระบบกรองเนื้อหาจะตรวจจับและดำเนินการกับหมวดหมู่เฉพาะของเนื้อหาที่อาจเป็นอันตรายในทั้ง prompt และ output ดูรายละเอียดเพิ่มเติมที่ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)

**การตั้งค่าการปรับแต่ง**

กำหนดไฮเปอร์พารามิเตอร์ เช่น อัตราการเรียนรู้ ขนาดแบตช์ และจำนวนรอบการฝึก

**ฟังก์ชันการสูญเสีย (Loss Function)**

เลือกฟังก์ชันการสูญเสียที่เหมาะสมกับงานของคุณ (เช่น cross-entropy)

**ตัวเพิ่มประสิทธิภาพ (Optimizer)**

เลือกตัวเพิ่มประสิทธิภาพ (เช่น Adam) สำหรับการปรับปรุงความชันในระหว่างการฝึก

**กระบวนการปรับแต่ง**

- โหลดโมเดลฝึกสอนล่วงหน้า: โหลดเช็คพอยต์ของ Phi-3 Mini
- เพิ่มเลเยอร์ที่กำหนดเอง: เพิ่มเลเยอร์เฉพาะงาน (เช่น หัวจำแนกสำหรับคำสั่งสนทนา)

**ฝึกโมเดล**
ปรับแต่งโมเดลโดยใช้ชุดข้อมูลที่เตรียมไว้ ตรวจสอบความคืบหน้าการฝึก และปรับไฮเปอร์พารามิเตอร์ตามต้องการ

**การประเมินและตรวจสอบ**

ชุดตรวจสอบ: แบ่งข้อมูลเป็นชุดฝึกและชุดตรวจสอบ

**ประเมินประสิทธิภาพ**

ใช้เมตริก เช่น ความแม่นยำ F1-score หรือ perplexity เพื่อประเมินประสิทธิภาพของโมเดล

## การบันทึกโมเดลที่ปรับแต่งแล้ว

**เช็คพอยต์**
บันทึกเช็คพอยต์ของโมเดลที่ปรับแต่งแล้วเพื่อใช้งานในอนาคต

## การนำไปใช้งาน

- นำไปใช้งานเป็นเว็บเซอร์วิส: นำโมเดลที่ปรับแต่งแล้วไปใช้งานเป็นเว็บเซอร์วิสใน Microsoft Foundry
- ทดสอบ Endpoint: ส่งคำถามทดสอบไปยัง endpoint ที่นำไปใช้เพื่อยืนยันการทำงาน

## การปรับปรุงและพัฒนา

ทำซ้ำ: หากผลลัพธ์ยังไม่เป็นที่น่าพอใจ ให้ปรับไฮเปอร์พารามิเตอร์ เพิ่มข้อมูล หรือฝึกเพิ่มรอบได้

## การตรวจสอบและปรับแต่ง

ติดตามพฤติกรรมของโมเดลอย่างต่อเนื่องและปรับแต่งตามต้องการ

## การกำหนดค่าเฉพาะและขยายความสามารถ

งานเฉพาะ: Phi-3 Mini สามารถปรับแต่งสำหรับงานต่าง ๆ นอกจากคำสั่งสนทนา ลองสำรวจกรณีใช้งานอื่น ๆ
ทดลอง: ลองโครงสร้าง เลเยอร์ต่าง ๆ และเทคนิคเพื่อเพิ่มประสิทธิภาพ

> [!NOTE]
> การปรับแต่งเป็นกระบวนการทำซ้ำ ทดลอง เรียนรู้ และปรับโมเดลของคุณเพื่อให้ได้ผลลัพธ์ที่ดีที่สุดสำหรับงานเฉพาะของคุณ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->