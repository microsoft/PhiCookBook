<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:53:03+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "th"
}
-->
# การใช้ Windows GPU เพื่อสร้างโซลูชัน Prompt flow ด้วย Phi-3.5-Instruct ONNX

เอกสารนี้เป็นตัวอย่างวิธีการใช้ PromptFlow ร่วมกับ ONNX (Open Neural Network Exchange) สำหรับพัฒนาแอปพลิเคชัน AI ที่อิงตามโมเดล Phi-3

PromptFlow คือชุดเครื่องมือสำหรับการพัฒนา ที่ออกแบบมาเพื่อช่วยให้กระบวนการพัฒนาแอปพลิเคชัน AI ที่ใช้ LLM (Large Language Model) ตั้งแต่การคิดไอเดีย การทำต้นแบบ ไปจนถึงการทดสอบและประเมินผล เป็นไปอย่างราบรื่น

ด้วยการรวม PromptFlow กับ ONNX นักพัฒนาสามารถ:

- ปรับประสิทธิภาพของโมเดล: ใช้ ONNX เพื่อเพิ่มประสิทธิภาพในการรันและการใช้งานโมเดล
- ทำให้การพัฒนาง่ายขึ้น: ใช้ PromptFlow ในการจัดการเวิร์กโฟลว์และอัตโนมัติงานที่ทำซ้ำๆ
- เพิ่มความร่วมมือ: ช่วยให้ทีมทำงานร่วมกันได้ดีขึ้นด้วยสภาพแวดล้อมการพัฒนาที่เป็นหนึ่งเดียว

**Prompt flow** คือชุดเครื่องมือสำหรับการพัฒนา ที่ออกแบบมาเพื่อช่วยให้กระบวนการพัฒนาแอปพลิเคชัน AI ที่ใช้ LLM ตั้งแต่การคิดไอเดีย การทำต้นแบบ การทดสอบ การประเมินผล ไปจนถึงการนำไปใช้งานจริงและการติดตามผล เป็นไปอย่างมีประสิทธิภาพ ช่วยให้งานวิศวกรรม prompt ง่ายขึ้นและช่วยให้คุณสร้างแอป LLM ที่มีคุณภาพระดับโปรดักชันได้

Prompt flow สามารถเชื่อมต่อกับ OpenAI, Azure OpenAI Service และโมเดลที่ปรับแต่งได้ (Huggingface, LLM/SLM ในเครื่อง) เราหวังว่าจะนำโมเดล ONNX แบบ quantized ของ Phi-3.5 ไปใช้ในแอปพลิเคชันภายในเครื่อง Prompt flow จะช่วยให้เราวางแผนธุรกิจได้ดีขึ้นและสร้างโซลูชันในเครื่องที่อิงกับ Phi-3.5 ได้ ในตัวอย่างนี้ เราจะรวม ONNX Runtime GenAI Library เพื่อสร้างโซลูชัน Prompt flow บน Windows GPU

## **การติดตั้ง**

### **ONNX Runtime GenAI สำหรับ Windows GPU**

อ่านคำแนะนำนี้เพื่อตั้งค่า ONNX Runtime GenAI สำหรับ Windows GPU [คลิกที่นี่](./ORTWindowGPUGuideline.md)

### **การตั้งค่า Prompt flow ใน VSCode**

1. ติดตั้ง Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.th.png)

2. หลังจากติดตั้ง Prompt flow VS Code Extension แล้ว ให้คลิกที่ส่วนขยายนี้ และเลือก **Installation dependencies** ตามคำแนะนำนี้เพื่อติดตั้ง Prompt flow SDK ในสภาพแวดล้อมของคุณ

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.th.png)

3. ดาวน์โหลด [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) และใช้ VS Code เปิดตัวอย่างนี้

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.th.png)

4. เปิดไฟล์ **flow.dag.yaml** เพื่อเลือกสภาพแวดล้อม Python ของคุณ

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.th.png)

   เปิดไฟล์ **chat_phi3_ort.py** เพื่อเปลี่ยนตำแหน่งโมเดล Phi-3.5-instruct ONNX ของคุณ

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.th.png)

5. รัน prompt flow เพื่อทดสอบ

เปิดไฟล์ **flow.dag.yaml** แล้วคลิกที่ visual editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.th.png)

หลังจากคลิกนี้ ให้รันเพื่อทดสอบ

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.th.png)

1. คุณสามารถรันแบบ batch ใน terminal เพื่อตรวจสอบผลลัพธ์เพิ่มเติม


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

คุณสามารถดูผลลัพธ์ได้ในเว็บเบราว์เซอร์เริ่มต้นของคุณ


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.th.png)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับถือเป็นแหล่งข้อมูลที่ถูกต้องและเชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้