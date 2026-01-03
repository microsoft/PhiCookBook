<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:39:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "th"
}
-->
# ประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Azure AI Foundry โดยเน้นหลักการ Responsible AI ของ Microsoft

ตัวอย่างแบบครบวงจร (E2E) นี้อ้างอิงจากคู่มือ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" จาก Microsoft Tech Community

## ภาพรวม

### คุณจะประเมินความปลอดภัยและประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Azure AI Foundry ได้อย่างไร?

การปรับแต่งโมเดลอาจทำให้เกิดการตอบสนองที่ไม่คาดคิดหรือไม่พึงประสงค์ได้ เพื่อให้มั่นใจว่าโมเดลยังคงปลอดภัยและมีประสิทธิภาพ จึงจำเป็นต้องประเมินความเป็นไปได้ที่โมเดลจะสร้างเนื้อหาที่เป็นอันตราย รวมถึงความสามารถในการให้คำตอบที่ถูกต้อง สอดคล้อง และเหมาะสม ในบทเรียนนี้ คุณจะได้เรียนรู้วิธีประเมินความปลอดภัยและประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งและผสานรวมกับ Prompt flow ใน Azure AI Foundry

นี่คือกระบวนการประเมินของ Azure AI Foundry

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4.th.png)

*ที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> สำหรับข้อมูลเชิงลึกเพิ่มเติมและแหล่งข้อมูลเกี่ยวกับ Phi-3 / Phi-3.5 โปรดเยี่ยมชม [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)

### สิ่งที่ต้องเตรียม

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- โมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งแล้ว

### สารบัญ

1. [**สถานการณ์ที่ 1: แนะนำการประเมิน Prompt flow ใน Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [แนะนำการประเมินความปลอดภัย](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [แนะนำการประเมินประสิทธิภาพ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**สถานการณ์ที่ 2: การประเมินโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [ก่อนเริ่มต้น](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ปรับใช้ Azure OpenAI เพื่อประเมินโมเดล Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งโดยใช้การประเมิน Prompt flow ของ Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [ขอแสดงความยินดี!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **สถานการณ์ที่ 1: แนะนำการประเมิน Prompt flow ใน Azure AI Foundry**

### แนะนำการประเมินความปลอดภัย

เพื่อให้มั่นใจว่าโมเดล AI ของคุณมีจริยธรรมและปลอดภัย จำเป็นต้องประเมินโมเดลตามหลักการ Responsible AI ของ Microsoft ใน Azure AI Foundry การประเมินความปลอดภัยช่วยให้คุณตรวจสอบความเสี่ยงที่โมเดลอาจถูกโจมตีแบบ jailbreak และความเป็นไปได้ที่โมเดลจะสร้างเนื้อหาที่เป็นอันตราย ซึ่งสอดคล้องกับหลักการเหล่านี้โดยตรง

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa950.th.png)

*ที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### หลักการ Responsible AI ของ Microsoft

ก่อนเริ่มขั้นตอนทางเทคนิค จำเป็นต้องเข้าใจหลักการ Responsible AI ของ Microsoft ซึ่งเป็นกรอบจริยธรรมที่ออกแบบมาเพื่อชี้นำการพัฒนา การปรับใช้ และการดำเนินงานของระบบ AI อย่างรับผิดชอบ หลักการเหล่านี้ช่วยให้การออกแบบ พัฒนา และปรับใช้ระบบ AI เป็นไปอย่างยุติธรรม โปร่งใส และครอบคลุม หลักการเหล่านี้เป็นรากฐานสำหรับการประเมินความปลอดภัยของโมเดล AI

หลักการ Responsible AI ของ Microsoft ประกอบด้วย:

- **ความยุติธรรมและความครอบคลุม**: ระบบ AI ควรปฏิบัติต่อทุกคนอย่างเท่าเทียมและหลีกเลี่ยงการมีผลกระทบที่แตกต่างกันในกลุ่มคนที่มีสถานการณ์คล้ายกัน เช่น เมื่อระบบ AI ให้คำแนะนำเกี่ยวกับการรักษาทางการแพทย์ การขอสินเชื่อ หรือการจ้างงาน ควรให้คำแนะนำเดียวกันกับทุกคนที่มีอาการ สถานะทางการเงิน หรือคุณสมบัติทางวิชาชีพที่คล้ายกัน

- **ความน่าเชื่อถือและความปลอดภัย**: เพื่อสร้างความไว้วางใจ ระบบ AI ต้องทำงานได้อย่างน่าเชื่อถือ ปลอดภัย และสม่ำเสมอ ระบบเหล่านี้ควรทำงานตามที่ออกแบบไว้ ตอบสนองอย่างปลอดภัยต่อสถานการณ์ที่ไม่คาดคิด และต้านทานการถูกแทรกแซงที่เป็นอันตราย พฤติกรรมและความสามารถในการรับมือกับสถานการณ์ต่างๆ สะท้อนถึงสถานการณ์และเงื่อนไขที่นักพัฒนาได้คาดการณ์ไว้ในระหว่างการออกแบบและทดสอบ

- **ความโปร่งใส**: เมื่อระบบ AI ช่วยในการตัดสินใจที่มีผลกระทบอย่างมากต่อชีวิตผู้คน จำเป็นที่ผู้คนจะต้องเข้าใจว่าการตัดสินใจเหล่านั้นเกิดขึ้นได้อย่างไร เช่น ธนาคารอาจใช้ระบบ AI ในการตัดสินว่าบุคคลนั้นมีความน่าเชื่อถือทางเครดิตหรือไม่ หรือบริษัทอาจใช้ระบบ AI เพื่อคัดเลือกผู้สมัครที่มีคุณสมบัติเหมาะสมที่สุด

- **ความเป็นส่วนตัวและความปลอดภัย**: เมื่อ AI มีบทบาทมากขึ้น การปกป้องความเป็นส่วนตัวและข้อมูลส่วนบุคคลรวมถึงข้อมูลธุรกิจก็ยิ่งมีความสำคัญและซับซ้อนมากขึ้น ด้วย AI การรักษาความเป็นส่วนตัวและความปลอดภัยของข้อมูลต้องได้รับความใส่ใจอย่างใกล้ชิด เพราะการเข้าถึงข้อมูลเป็นสิ่งจำเป็นสำหรับระบบ AI ในการทำนายและตัดสินใจอย่างถูกต้องและมีข้อมูลครบถ้วนเกี่ยวกับผู้คน

- **ความรับผิดชอบ**: ผู้ที่ออกแบบและปรับใช้ระบบ AI ต้องรับผิดชอบต่อการทำงานของระบบของตน องค์กรควรใช้มาตรฐานในอุตสาหกรรมเพื่อพัฒนากฎเกณฑ์ความรับผิดชอบ กฎเกณฑ์เหล่านี้ช่วยให้มั่นใจว่าระบบ AI จะไม่เป็นผู้ตัดสินขั้นสุดท้ายในเรื่องที่ส่งผลต่อชีวิตผู้คน และยังช่วยให้มนุษย์ยังคงควบคุมระบบ AI ที่มีความเป็นอิสระสูงได้อย่างมีความหมาย

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c.th.png)

*ที่มาของภาพ: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับหลักการ Responsible AI ของ Microsoft โปรดเยี่ยมชม [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)

#### ตัวชี้วัดความปลอดภัย

ในบทเรียนนี้ คุณจะประเมินความปลอดภัยของโมเดล Phi-3 ที่ผ่านการปรับแต่งโดยใช้ตัวชี้วัดความปลอดภัยของ Azure AI Foundry ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินความเป็นไปได้ที่โมเดลจะสร้างเนื้อหาที่เป็นอันตรายและความเสี่ยงต่อการถูกโจมตีแบบ jailbreak ตัวชี้วัดความปลอดภัยประกอบด้วย:

- **เนื้อหาที่เกี่ยวข้องกับการทำร้ายตัวเอง**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาที่เกี่ยวข้องกับการทำร้ายตัวเองหรือไม่
- **เนื้อหาที่เกลียดชังและไม่เป็นธรรม**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาที่เกลียดชังหรือไม่เป็นธรรมหรือไม่
- **เนื้อหาความรุนแรง**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาความรุนแรงหรือไม่
- **เนื้อหาทางเพศ**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาทางเพศที่ไม่เหมาะสมหรือไม่

การประเมินด้านเหล่านี้ช่วยให้มั่นใจว่าโมเดล AI จะไม่สร้างเนื้อหาที่เป็นอันตรายหรือไม่เหมาะสม สอดคล้องกับค่านิยมทางสังคมและมาตรฐานทางกฎหมาย

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07.th.png)

### แนะนำการประเมินประสิทธิภาพ

เพื่อให้มั่นใจว่าโมเดล AI ของคุณทำงานได้ตามที่คาดหวัง จำเป็นต้องประเมินประสิทธิภาพของโมเดลตามตัวชี้วัดประสิทธิภาพ ใน Azure AI Foundry การประเมินประสิทธิภาพช่วยให้คุณประเมินความสามารถของโมเดลในการสร้างคำตอบที่ถูกต้อง สอดคล้อง และเหมาะสม

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740.th.png)

*ที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### ตัวชี้วัดประสิทธิภาพ

ในบทเรียนนี้ คุณจะประเมินประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งโดยใช้ตัวชี้วัดประสิทธิภาพของ Azure AI Foundry ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินความสามารถของโมเดลในการสร้างคำตอบที่ถูกต้อง สอดคล้อง และเหมาะสม ตัวชี้วัดประสิทธิภาพประกอบด้วย:

- **ความสอดคล้องกับข้อมูลต้นทาง (Groundedness)**: ประเมินว่าคำตอบที่สร้างขึ้นสอดคล้องกับข้อมูลจากแหล่งข้อมูลต้นทางมากน้อยเพียงใด
- **ความเกี่ยวข้อง (Relevance)**: ประเมินความเหมาะสมของคำตอบที่สร้างขึ้นกับคำถามที่ได้รับ
- **ความลื่นไหลและต่อเนื่อง (Coherence)**: ประเมินความลื่นไหลของข้อความที่สร้างขึ้น อ่านแล้วเป็นธรรมชาติ และคล้ายภาษามนุษย์
- **ความคล่องแคล่วทางภาษา (Fluency)**: ประเมินความชำนาญทางภาษาของข้อความที่สร้างขึ้น
- **ความคล้ายคลึงกับ GPT (GPT Similarity)**: เปรียบเทียบคำตอบที่สร้างขึ้นกับคำตอบจริงเพื่อวัดความคล้ายคลึง
- **คะแนน F1 (F1 Score)**: คำนวณอัตราส่วนของคำที่เหมือนกันระหว่างคำตอบที่สร้างขึ้นกับข้อมูลต้นทาง

ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินความสามารถของโมเดลในการสร้างคำตอบที่ถูกต้อง สอดคล้อง และเหมาะสม

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e8.th.png)

## **สถานการณ์ที่ 2: การประเมินโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry**

### ก่อนเริ่มต้น

บทเรียนนี้เป็นการต่อยอดจากบล็อกก่อนหน้า "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" และ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ในบทความเหล่านี้ เราได้แนะนำขั้นตอนการปรับแต่งโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry และการผสานรวมกับ Prompt flow

ในบทเรียนนี้ คุณจะปรับใช้โมเดล Azure OpenAI เป็นตัวประเมินใน Azure AI Foundry และใช้มันในการประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งของคุณ

ก่อนเริ่มบทเรียนนี้ โปรดตรวจสอบว่าคุณมีสิ่งที่ต้องเตรียมดังต่อไปนี้ตามที่อธิบายในบทเรียนก่อนหน้า:

1. ชุดข้อมูลที่เตรียมไว้สำหรับประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง
1. โมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งและปรับใช้ใน Azure Machine Learning แล้ว
1. Prompt flow ที่ผสานรวมกับโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Azure AI Foundry

> [!NOTE]
> คุณจะใช้ไฟล์ *test_data.jsonl* ซึ่งอยู่ในโฟลเดอร์ data จากชุดข้อมูล **ULTRACHAT_200k** ที่ดาวน์โหลดในบล็อกก่อนหน้า เป็นชุดข้อมูลสำหรับประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง

#### การผสานรวมโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองกับ Prompt flow ใน Azure AI Foundry (แนวทางเขียนโค้ดก่อน)
> [!NOTE]
> หากคุณใช้วิธี low-code ตามที่อธิบายใน "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" คุณสามารถข้ามแบบฝึกหัดนี้และไปยังแบบฝึกหัดถัดไปได้
> อย่างไรก็ตาม หากคุณใช้วิธี code-first ตามที่อธิบายใน "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" เพื่อปรับแต่งและปรับใช้โมเดล Phi-3 / Phi-3.5 ของคุณ กระบวนการเชื่อมต่อโมเดลกับ Prompt flow จะแตกต่างกันเล็กน้อย คุณจะได้เรียนรู้กระบวนการนี้ในแบบฝึกหัดนี้
ในการดำเนินการต่อ คุณจำเป็นต้องผสานรวมโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งแล้วของคุณเข้ากับ Prompt flow ใน Azure AI Foundry

#### สร้าง Azure AI Foundry Hub

คุณต้องสร้าง Hub ก่อนที่จะสร้าง Project Hub ทำหน้าที่เหมือน Resource Group ช่วยให้คุณจัดระเบียบและจัดการหลายโครงการภายใน Azure AI Foundry ได้

1. ลงชื่อเข้าใช้ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. เลือก **All hubs** จากแท็บด้านซ้าย

1. เลือก **+ New hub** จากเมนูนำทาง

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1.th.png)

1. ดำเนินการตามขั้นตอนดังนี้:

    - กรอก **Hub name** ต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือก Azure **Subscription** ของคุณ
    - เลือก **Resource group** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Location** ที่คุณต้องการใช้
    - เลือก **Connect Azure AI Services** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Connect Azure AI Search** เป็น **Skip connecting**

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e34.th.png)

1. เลือก **Next**

#### สร้าง Azure AI Foundry Project

1. ใน Hub ที่คุณสร้างขึ้น เลือก **All projects** จากแท็บด้านซ้าย

1. เลือก **+ New project** จากเมนูนำทาง

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a3.th.png)

1. กรอก **Project name** ต้องเป็นค่าที่ไม่ซ้ำกัน

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e420.th.png)

1. เลือก **Create a project**

#### เพิ่มการเชื่อมต่อแบบกำหนดเองสำหรับโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง

เพื่อผสานรวมโมเดล Phi-3 / Phi-3.5 แบบกำหนดเองของคุณกับ Prompt flow คุณต้องบันทึก endpoint และ key ของโมเดลในการเชื่อมต่อแบบกำหนดเอง การตั้งค่านี้จะช่วยให้สามารถเข้าถึงโมเดล Phi-3 / Phi-3.5 แบบกำหนดเองใน Prompt flow ได้

#### ตั้งค่า api key และ endpoint uri ของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง

1. เข้าไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. ไปยัง Azure Machine learning workspace ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแท็บด้านซ้าย

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d.th.png)

1. เลือก endpoint ที่คุณสร้างไว้

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2e.th.png)

1. เลือก **Consume** จากเมนูนำทาง

1. คัดลอก **REST endpoint** และ **Primary key** ของคุณ

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab.th.png)

#### เพิ่มการเชื่อมต่อแบบกำหนดเอง

1. เข้าไปที่ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Settings** จากแท็บด้านซ้าย

1. เลือก **+ New connection**

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b.th.png)

1. เลือก **Custom keys** จากเมนูนำทาง

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67.th.png)

1. ดำเนินการตามขั้นตอนดังนี้:

    - เลือก **+ Add key value pairs**
    - สำหรับชื่อ key ให้กรอก **endpoint** และวาง endpoint ที่คุณคัดลอกจาก Azure ML Studio ลงในช่องค่า
    - เลือก **+ Add key value pairs** อีกครั้ง
    - สำหรับชื่อ key ให้กรอก **key** และวาง key ที่คุณคัดลอกจาก Azure ML Studio ลงในช่องค่า
    - หลังจากเพิ่ม key แล้ว ให้เลือก **is secret** เพื่อป้องกันไม่ให้ key ถูกเปิดเผย

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0df.th.png)

1. เลือก **Add connection**

#### สร้าง Prompt flow

คุณได้เพิ่มการเชื่อมต่อแบบกำหนดเองใน Azure AI Foundry แล้ว ตอนนี้มาสร้าง Prompt flow โดยทำตามขั้นตอนต่อไปนี้ จากนั้นคุณจะเชื่อมต่อ Prompt flow นี้กับการเชื่อมต่อแบบกำหนดเองเพื่อใช้โมเดลที่ผ่านการปรับแต่งภายใน Prompt flow

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. เลือก **Prompt flow** จากแท็บด้านซ้าย

1. เลือก **+ Create** จากเมนูนำทาง

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb.th.png)

1. เลือก **Chat flow** จากเมนูนำทาง

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d3.th.png)

1. กรอก **Folder name** ที่ต้องการใช้

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad430.th.png)

1. เลือก **Create**

#### ตั้งค่า Prompt flow เพื่อสนทนากับโมเดล Phi-3 / Phi-3.5 แบบกำหนดเองของคุณ

คุณจำเป็นต้องผสานรวมโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งเข้ากับ Prompt flow อย่างไรก็ตาม Prompt flow ที่มีอยู่ไม่ได้ออกแบบมาเพื่อวัตถุประสงค์นี้ ดังนั้นคุณต้องออกแบบ Prompt flow ใหม่เพื่อให้สามารถผสานรวมโมเดลแบบกำหนดเองได้

1. ใน Prompt flow ให้ทำตามขั้นตอนต่อไปนี้เพื่อสร้าง flow ใหม่:

    - เลือก **Raw file mode**
    - ลบโค้ดทั้งหมดที่มีอยู่ในไฟล์ *flow.dag.yml*
    - เพิ่มโค้ดต่อไปนี้ลงใน *flow.dag.yml*

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - เลือก **Save**

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f53.th.png)

1. เพิ่มโค้ดต่อไปนี้ใน *integrate_with_promptflow.py* เพื่อใช้โมเดล Phi-3 / Phi-3.5 แบบกำหนดเองใน Prompt flow

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec28.th.png)

> [!NOTE]
> สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้ Prompt flow ใน Azure AI Foundry คุณสามารถดูได้ที่ [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)

1. เลือก **Chat input**, **Chat output** เพื่อเปิดใช้งานการสนทนากับโมเดลของคุณ

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc3.th.png)

1. ตอนนี้คุณพร้อมที่จะสนทนากับโมเดล Phi-3 / Phi-3.5 แบบกำหนดเองของคุณแล้ว ในแบบฝึกหัดถัดไป คุณจะได้เรียนรู้วิธีเริ่มต้น Prompt flow และใช้งานเพื่อสนทนากับโมเดลที่ผ่านการปรับแต่ง

> [!NOTE]
>
> โฟลว์ที่สร้างใหม่ควรมีลักษณะเหมือนภาพด้านล่างนี้:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545b.th.png)
>

#### เริ่มต้น Prompt flow

1. เลือก **Start compute sessions** เพื่อเริ่ม Prompt flow

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df1.th.png)

1. เลือก **Validate and parse input** เพื่อรีเฟรชพารามิเตอร์

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be.th.png)

1. เลือก **Value** ของ **connection** เป็นการเชื่อมต่อแบบกำหนดเองที่คุณสร้างไว้ เช่น *connection*

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafef.th.png)

#### สนทนากับโมเดล Phi-3 / Phi-3.5 แบบกำหนดเองของคุณ

1. เลือก **Chat**

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d.th.png)

1. นี่คือตัวอย่างผลลัพธ์: ตอนนี้คุณสามารถสนทนากับโมเดล Phi-3 / Phi-3.5 แบบกำหนดเองของคุณได้ แนะนำให้ถามคำถามที่เกี่ยวข้องกับข้อมูลที่ใช้ในการปรับแต่งโมเดล

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada.th.png)

### นำ Azure OpenAI มาใช้งานเพื่อประเมินโมเดล Phi-3 / Phi-3.5

เพื่อประเมินโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry คุณจำเป็นต้องนำโมเดล Azure OpenAI มาใช้งาน โมเดลนี้จะใช้ในการประเมินประสิทธิภาพของโมเดล Phi-3 / Phi-3.5

#### นำ Azure OpenAI มาใช้งาน

1. ลงชื่อเข้าใช้ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6.th.png)

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Deployments** จากแท็บด้านซ้าย

1. เลือก **+ Deploy model** จากเมนูนำทาง

1. เลือก **Deploy base model**

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b.th.png)

1. เลือกโมเดล Azure OpenAI ที่คุณต้องการใช้ เช่น **gpt-4o**

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d.th.png)

1. เลือก **Confirm**

### ประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งโดยใช้การประเมิน Prompt flow ของ Azure AI Foundry

### เริ่มการประเมินใหม่

1. เข้าไปที่ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6.th.png)

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Evaluation** จากแท็บด้านซ้าย

1. เลือก **+ New evaluation** จากเมนูนำทาง

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f.th.png)

1. เลือกการประเมินแบบ **Prompt flow**

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f.th.png)

1. ดำเนินการตามขั้นตอนดังนี้:

    - กรอกชื่อการประเมิน ต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือก **Question and answer without context** เป็นประเภทงาน เนื่องจากชุดข้อมูล **UlTRACHAT_200k** ที่ใช้ในบทเรียนนี้ไม่มีบริบท
    - เลือก prompt flow ที่คุณต้องการประเมิน

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e.th.png)

1. เลือก **Next**

1. ดำเนินการตามขั้นตอนดังนี้:

    - เลือก **Add your dataset** เพื่ออัปโหลดชุดข้อมูล เช่น ไฟล์ชุดข้อมูลทดสอบ *test_data.json1* ซึ่งรวมอยู่ในชุดข้อมูล **ULTRACHAT_200k**
    - เลือก **Dataset column** ที่เหมาะสมกับชุดข้อมูลของคุณ เช่น หากใช้ชุดข้อมูล **ULTRACHAT_200k** ให้เลือก **${data.prompt}** เป็นคอลัมน์ชุดข้อมูล

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64e.th.png)

1. เลือก **Next**

1. ดำเนินการตามขั้นตอนเพื่อกำหนดค่าตัวชี้วัดประสิทธิภาพและคุณภาพ:

    - เลือกตัวชี้วัดประสิทธิภาพและคุณภาพที่คุณต้องการใช้
    - เลือกโมเดล Azure OpenAI ที่คุณสร้างขึ้นเพื่อการประเมิน เช่น **gpt-4o**

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e.th.png)

1. ดำเนินการตามขั้นตอนเพื่อกำหนดค่าตัวชี้วัดความเสี่ยงและความปลอดภัย:

    - เลือกตัวชี้วัดความเสี่ยงและความปลอดภัยที่คุณต้องการใช้
    - เลือกระดับเกณฑ์เพื่อคำนวณอัตราข้อผิดพลาด เช่น เลือก **Medium**
    - สำหรับ **question** เลือก **Data source** เป็น **{$data.prompt}**
    - สำหรับ **answer** เลือก **Data source** เป็น **{$run.outputs.answer}**
    - สำหรับ **ground_truth** เลือก **Data source** เป็น **{$data.message}**

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2.th.png)

1. เลือก **Next**

1. เลือก **Submit** เพื่อเริ่มการประเมิน

1. การประเมินจะใช้เวลาสักครู่ คุณสามารถติดตามความคืบหน้าได้ในแท็บ **Evaluation**

### ตรวจสอบผลการประเมิน
> [!NOTE]
> ผลลัพธ์ที่แสดงด้านล่างนี้มีจุดประสงค์เพื่อแสดงขั้นตอนการประเมิน ในบทเรียนนี้ เราใช้โมเดลที่ผ่านการปรับแต่งด้วยชุดข้อมูลขนาดค่อนข้างเล็ก ซึ่งอาจทำให้ผลลัพธ์ไม่สมบูรณ์แบบ ผลลัพธ์จริงอาจแตกต่างกันอย่างมากขึ้นอยู่กับขนาด คุณภาพ และความหลากหลายของชุดข้อมูลที่ใช้ รวมถึงการตั้งค่าที่เฉพาะเจาะจงของโมเดลด้วย
เมื่อการประเมินเสร็จสิ้น คุณสามารถตรวจสอบผลลัพธ์ทั้งในด้านประสิทธิภาพและมาตรฐานความปลอดภัยได้

1. ตัวชี้วัดประสิทธิภาพและคุณภาพ:

    - ประเมินประสิทธิผลของโมเดลในการสร้างคำตอบที่สอดคล้อง ลื่นไหล และเกี่ยวข้อง

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb74254.th.png)

1. ตัวชี้วัดความเสี่ยงและความปลอดภัย:

    - ตรวจสอบให้แน่ใจว่าผลลัพธ์ของโมเดลปลอดภัยและสอดคล้องกับ Responsible AI Principles หลีกเลี่ยงเนื้อหาที่เป็นอันตรายหรือไม่เหมาะสม

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0.th.png)

1. คุณสามารถเลื่อนลงเพื่อดู **ผลลัพธ์ตัวชี้วัดโดยละเอียด**

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f17.th.png)

1. โดยการประเมินโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองของคุณทั้งในด้านประสิทธิภาพและความปลอดภัย คุณจะมั่นใจได้ว่าโมเดลไม่เพียงแต่มีประสิทธิภาพเท่านั้น แต่ยังปฏิบัติตามแนวทาง Responsible AI ทำให้พร้อมสำหรับการใช้งานจริง

## ขอแสดงความยินดี!

### คุณได้ทำแบบฝึกหัดนี้เสร็จสมบูรณ์แล้ว

คุณได้ประเมินโมเดล Phi-3 ที่ปรับแต่งและผสานรวมกับ Prompt flow ใน Azure AI Foundry สำเร็จแล้ว นี่เป็นขั้นตอนสำคัญในการรับรองว่าโมเดล AI ของคุณไม่เพียงแต่ทำงานได้ดี แต่ยังสอดคล้องกับหลักการ Responsible AI ของ Microsoft เพื่อช่วยให้คุณสร้างแอปพลิเคชัน AI ที่น่าเชื่อถือและมั่นใจได้

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4.th.png)

## ล้างทรัพยากร Azure

ล้างทรัพยากร Azure ของคุณเพื่อหลีกเลี่ยงค่าบริการเพิ่มเติมในบัญชีของคุณ ไปที่พอร์ทัล Azure และลบทรัพยากรต่อไปนี้:

- Azure Machine learning resource
- Azure Machine learning model endpoint
- Azure AI Foundry Project resource
- Azure AI Foundry Prompt flow resource

### ขั้นตอนถัดไป

#### เอกสารประกอบ

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### เนื้อหาการฝึกอบรม

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### เอกสารอ้างอิง

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้