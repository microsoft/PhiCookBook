<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:32:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "th"
}
-->
# ประเมินโมเดล Fine-tuned Phi-3 / Phi-3.5 ใน Azure AI Foundry โดยเน้นหลักการ Responsible AI ของ Microsoft

ตัวอย่างแบบครบวงจร (E2E) นี้อ้างอิงจากคำแนะนำ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" จาก Microsoft Tech Community

## ภาพรวม

### คุณจะประเมินความปลอดภัยและประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Azure AI Foundry ได้อย่างไร?

การปรับแต่งโมเดลบางครั้งอาจทำให้เกิดคำตอบที่ไม่ตั้งใจหรือไม่ต้องการ เพื่อให้แน่ใจว่าโมเดลยังคงปลอดภัยและมีประสิทธิภาพ จึงจำเป็นต้องประเมินความเสี่ยงที่โมเดลอาจสร้างเนื้อหาที่เป็นอันตราย และความสามารถในการให้คำตอบที่ถูกต้อง เหมาะสม และสอดคล้องกัน ในบทเรียนนี้ คุณจะได้เรียนรู้วิธีประเมินความปลอดภัยและประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งและผสานรวมกับ Prompt flow ใน Azure AI Foundry

นี่คือกระบวนการประเมินของ Azure AI Foundry

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.th.png)

*ที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> สำหรับข้อมูลเชิงลึกเพิ่มเติมและแหล่งข้อมูลเกี่ยวกับ Phi-3 / Phi-3.5 โปรดเยี่ยมชม [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)

### ข้อกำหนดเบื้องต้น

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- โมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง

### สารบัญ

1. [**สถานการณ์ที่ 1: แนะนำการประเมิน Prompt flow ของ Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [แนะนำการประเมินความปลอดภัย](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [แนะนำการประเมินประสิทธิภาพ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**สถานการณ์ที่ 2: การประเมินโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [ก่อนเริ่มต้น](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ปรับใช้ Azure OpenAI เพื่อประเมินโมเดล Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งโดยใช้การประเมิน Prompt flow ของ Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [ยินดีด้วย!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **สถานการณ์ที่ 1: แนะนำการประเมิน Prompt flow ของ Azure AI Foundry**

### แนะนำการประเมินความปลอดภัย

เพื่อให้แน่ใจว่าโมเดล AI ของคุณมีจริยธรรมและปลอดภัย จำเป็นต้องประเมินโมเดลตามหลักการ Responsible AI ของ Microsoft ใน Azure AI Foundry การประเมินความปลอดภัยช่วยให้คุณประเมินความเสี่ยงที่โมเดลจะถูกโจมตีแบบ jailbreak และความสามารถในการสร้างเนื้อหาที่เป็นอันตราย ซึ่งสอดคล้องโดยตรงกับหลักการเหล่านี้

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.th.png)

*ที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### หลักการ Responsible AI ของ Microsoft

ก่อนเริ่มขั้นตอนทางเทคนิค จำเป็นต้องเข้าใจหลักการ Responsible AI ของ Microsoft ซึ่งเป็นกรอบจริยธรรมที่ออกแบบมาเพื่อชี้นำการพัฒนา การปรับใช้ และการดำเนินงานของระบบ AI อย่างรับผิดชอบ หลักการเหล่านี้ชี้นำการออกแบบ พัฒนา และปรับใช้ระบบ AI อย่างรับผิดชอบ เพื่อให้เทคโนโลยี AI ถูกสร้างขึ้นอย่างยุติธรรม โปร่งใส และครอบคลุม หลักการเหล่านี้เป็นพื้นฐานในการประเมินความปลอดภัยของโมเดล AI

หลักการ Responsible AI ของ Microsoft ประกอบด้วย:

- **ความยุติธรรมและครอบคลุม**: ระบบ AI ควรปฏิบัติต่อทุกคนอย่างยุติธรรม และหลีกเลี่ยงการมีผลกระทบแตกต่างกันในกลุ่มคนที่มีสถานการณ์คล้ายกัน เช่น เมื่อระบบ AI ให้คำแนะนำด้านการรักษาพยาบาล การขอสินเชื่อ หรือการจ้างงาน ควรให้คำแนะนำเหมือนกันกับทุกคนที่มีอาการ สถานะการเงิน หรือคุณสมบัติทางวิชาชีพที่คล้ายกัน

- **ความน่าเชื่อถือและความปลอดภัย**: เพื่อสร้างความไว้วางใจ ระบบ AI ต้องทำงานได้อย่างน่าเชื่อถือ ปลอดภัย และสม่ำเสมอ ระบบเหล่านี้ควรทำงานตามที่ออกแบบไว้ ตอบสนองอย่างปลอดภัยต่อสถานการณ์ที่ไม่คาดคิด และทนต่อการถูกโจมตีอย่างเป็นอันตราย พฤติกรรมและความสามารถในการรับมือกับสถานการณ์ต่างๆ สะท้อนถึงช่วงสถานการณ์ที่นักพัฒนาได้คาดการณ์ไว้ในขั้นตอนการออกแบบและทดสอบ

- **ความโปร่งใส**: เมื่อระบบ AI ช่วยในการตัดสินใจที่มีผลกระทบต่อชีวิตผู้คนอย่างมาก จำเป็นที่ผู้คนจะต้องเข้าใจว่าการตัดสินใจเหล่านั้นเกิดขึ้นอย่างไร เช่น ธนาคารอาจใช้ระบบ AI ในการตัดสินว่าบุคคลใดมีเครดิตดี หรือบริษัทอาจใช้ระบบ AI เพื่อคัดเลือกผู้สมัครที่เหมาะสมที่สุด

- **ความเป็นส่วนตัวและความปลอดภัย**: เมื่อ AI กลายเป็นสิ่งที่แพร่หลายมากขึ้น การปกป้องความเป็นส่วนตัวและข้อมูลส่วนบุคคล รวมถึงข้อมูลทางธุรกิจ จึงมีความสำคัญและซับซ้อนมากขึ้น ด้วย AI ความเป็นส่วนตัวและความปลอดภัยของข้อมูลต้องได้รับความใส่ใจอย่างใกล้ชิด เพราะการเข้าถึงข้อมูลเป็นสิ่งจำเป็นสำหรับระบบ AI ในการทำการทำนายและตัดสินใจที่ถูกต้องและมีข้อมูลรองรับ

- **ความรับผิดชอบ**: ผู้ที่ออกแบบและปรับใช้ระบบ AI ต้องรับผิดชอบต่อการทำงานของระบบ องค์กรควรใช้มาตรฐานในอุตสาหกรรมเพื่อพัฒนามาตรฐานความรับผิดชอบ มาตรฐานเหล่านี้จะช่วยให้ระบบ AI ไม่ใช่อำนาจสุดท้ายในการตัดสินใจที่ส่งผลต่อชีวิตผู้คน และยังช่วยให้มนุษย์ยังคงควบคุมระบบ AI ที่มีความเป็นอิสระสูงได้อย่างมีความหมาย

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.th.png)

*ที่มาของภาพ: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับหลักการ Responsible AI ของ Microsoft โปรดเยี่ยมชม [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)

#### ตัวชี้วัดความปลอดภัย

ในบทเรียนนี้ คุณจะประเมินความปลอดภัยของโมเดล Phi-3 ที่ผ่านการปรับแต่งโดยใช้ตัวชี้วัดความปลอดภัยของ Azure AI Foundry ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินความเสี่ยงที่โมเดลจะสร้างเนื้อหาที่เป็นอันตรายและความเปราะบางต่อการโจมตีแบบ jailbreak ตัวชี้วัดความปลอดภัยประกอบด้วย:

- **เนื้อหาที่เกี่ยวกับการทำร้ายตัวเอง**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาที่เกี่ยวข้องกับการทำร้ายตัวเองหรือไม่
- **เนื้อหาที่เกลียดชังและไม่เป็นธรรม**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาที่เกลียดชังหรือไม่เป็นธรรมหรือไม่
- **เนื้อหาความรุนแรง**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาที่มีความรุนแรงหรือไม่
- **เนื้อหาทางเพศ**: ประเมินว่าโมเดลมีแนวโน้มที่จะสร้างเนื้อหาทางเพศที่ไม่เหมาะสมหรือไม่

การประเมินด้านเหล่านี้ช่วยให้แน่ใจว่าโมเดล AI จะไม่สร้างเนื้อหาที่เป็นอันตรายหรือก่อให้เกิดความรำคาญ ซึ่งสอดคล้องกับค่านิยมของสังคมและมาตรฐานข้อกำหนด

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.th.png)

### แนะนำการประเมินประสิทธิภาพ

เพื่อให้แน่ใจว่าโมเดล AI ของคุณทำงานได้ตามที่คาดหวัง จำเป็นต้องประเมินประสิทธิภาพโดยใช้ตัวชี้วัดประสิทธิภาพ ใน Azure AI Foundry การประเมินประสิทธิภาพช่วยให้คุณประเมินความสามารถของโมเดลในการสร้างคำตอบที่ถูกต้อง เหมาะสม และสอดคล้องกัน

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.th.png)

*ที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### ตัวชี้วัดประสิทธิภาพ

ในบทเรียนนี้ คุณจะประเมินประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งโดยใช้ตัวชี้วัดประสิทธิภาพของ Azure AI Foundry ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินความสามารถของโมเดลในการสร้างคำตอบที่ถูกต้อง เหมาะสม และสอดคล้องกัน ตัวชี้วัดประสิทธิภาพประกอบด้วย:

- **ความสอดคล้องกับข้อมูลต้นทาง (Groundedness)**: ประเมินว่าคำตอบที่สร้างขึ้นสอดคล้องกับข้อมูลจากแหล่งข้อมูลต้นทางมากน้อยเพียงใด
- **ความเกี่ยวข้อง (Relevance)**: ประเมินความเหมาะสมของคำตอบที่สร้างขึ้นกับคำถามที่ได้รับ
- **ความสอดคล้องในเนื้อหา (Coherence)**: ประเมินความลื่นไหลของข้อความที่สร้างขึ้น อ่านแล้วเป็นธรรมชาติ และคล้ายภาษาที่มนุษย์ใช้
- **ความคล่องแคล่วทางภาษา (Fluency)**: ประเมินความเชี่ยวชาญทางภาษาในข้อความที่สร้างขึ้น
- **ความคล้ายกับ GPT (GPT Similarity)**: เปรียบเทียบคำตอบที่สร้างขึ้นกับคำตอบจริงเพื่อดูความคล้ายคลึง
- **คะแนน F1 (F1 Score)**: คำนวณอัตราส่วนของคำที่เหมือนกันระหว่างคำตอบที่สร้างขึ้นและข้อมูลต้นทาง

ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินความสามารถของโมเดลในการสร้างคำตอบที่ถูกต้อง เหมาะสม และสอดคล้องกัน

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.th.png)

## **สถานการณ์ที่ 2: การประเมินโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry**

### ก่อนเริ่มต้น

บทเรียนนี้เป็นภาคต่อจากโพสต์บล็อกก่อนหน้านี้ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" และ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ในโพสต์เหล่านี้ เราได้แนะนำขั้นตอนการปรับแต่งโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry และการผสานรวมกับ Prompt flow

ในบทเรียนนี้ คุณจะปรับใช้โมเดล Azure OpenAI เป็นตัวประเมินใน Azure AI Foundry และใช้มันในการประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งของคุณ

ก่อนเริ่มบทเรียนนี้ ให้แน่ใจว่าคุณมีข้อกำหนดเบื้องต้นดังต่อไปนี้ตามที่อธิบายในบทเรียนก่อนหน้า:

1. ชุดข้อมูลที่เตรียมไว้สำหรับประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง
1. โมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งและปรับใช้ใน Azure Machine Learning แล้ว
1. Prompt flow ที่ผสานรวมกับโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Azure AI Foundry

> [!NOTE]
> คุณจะใช้ไฟล์ *test_data.jsonl* ซึ่งอยู่ในโฟลเดอร์ข้อมูลจากชุดข้อมูล **ULTRACHAT_200k** ที่ดาวน์โหลดในโพสต์บล็อกก่อนหน้า เป็นชุดข้อมูลสำหรับประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง

#### การผสานรวมโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองกับ Prompt flow ใน Azure AI Foundry (วิธีแบบเขียนโค้ดก่อน)

> [!NOTE]
> หากคุณใช้วิธีแบบ low-code ที่อธิบายใน "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" คุณสามารถข้ามแบบฝึกหัดนี้และไปยังขั้นตอนถัดไปได้
> แต่ถ้าคุณใช้วิธีแบบเขียนโค้ดก่อนตามที่อธิบายใน "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" เพื่อปรับแต่งและปรับใช้โมเดล Phi-3 / Phi-3.5 ของคุณ ขั้นตอนการเชื่อมต่อโมเดลกับ Prompt flow จะต่างออกไปเล็กน้อย คุณจะได้เรียนรู้ขั้นตอนนี้ในแบบฝึกหัดนี้

ในการดำเนินการต่อ คุณต้องผสานรวมโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งของคุณเข้ากับ Prompt flow ใน Azure AI Foundry

#### สร้าง Azure AI Foundry Hub

คุณต้องสร้าง Hub ก่อนที่จะสร้าง Project Hub ทำหน้าที่เหมือน Resource Group ที่ช่วยให้คุณจัดระเบียบและจัดการหลาย Project ภายใน Azure AI Foundry ได้

1. ลงชื่อเข้าใช้ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. เลือก **All hubs** จากแท็บด้านซ้าย

1. เลือก **+ New hub** จากเมนูนำทาง

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.th.png)

1. ดำเนินการตามขั้นตอนต่อไปนี้:

    - กรอก **Hub name** โดยต้องเป็นชื่อที่ไม่ซ้ำกัน
    - เลือก Azure **Subscription** ของคุณ
    - เลือก **Resource group** ที่ต้องการใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Location** ที่ต้องการใช้
    - เลือก **Connect Azure AI Services** ที่ต้องการใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Connect Azure AI Search** เป็น **Skip connecting**
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.th.png)

1. เลือก **Next**

#### สร้างโปรเจกต์ Azure AI Foundry

1. ใน Hub ที่คุณสร้างขึ้น ให้เลือก **All projects** จากแท็บด้านซ้าย

1. เลือก **+ New project** จากเมนูนำทาง

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.th.png)

1. กรอก **Project name** ต้องเป็นค่าที่ไม่ซ้ำกัน

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.th.png)

1. เลือก **Create a project**

#### เพิ่มการเชื่อมต่อแบบกำหนดเองสำหรับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้ว

เพื่อรวมโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองกับ Prompt flow คุณต้องบันทึก endpoint และ key ของโมเดลในการเชื่อมต่อแบบกำหนดเอง การตั้งค่านี้จะช่วยให้สามารถเข้าถึงโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองใน Prompt flow ได้

#### ตั้งค่า api key และ endpoint uri ของโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้ว

1. เข้าไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. ไปยัง workspace ของ Azure Machine learning ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแท็บด้านซ้าย

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.th.png)

1. เลือก endpoint ที่คุณสร้างไว้

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.th.png)

1. เลือก **Consume** จากเมนูนำทาง

1. คัดลอก **REST endpoint** และ **Primary key**

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.th.png)

#### เพิ่มการเชื่อมต่อแบบกำหนดเอง

1. เข้าไปที่ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Settings** จากแท็บด้านซ้าย

1. เลือก **+ New connection**

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.th.png)

1. เลือก **Custom keys** จากเมนูนำทาง

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.th.png)

1. ดำเนินการตามขั้นตอนต่อไปนี้:

    - เลือก **+ Add key value pairs**
    - สำหรับชื่อ key ให้ใส่ **endpoint** และวาง endpoint ที่คัดลอกจาก Azure ML Studio ลงในช่องค่า
    - เลือก **+ Add key value pairs** อีกครั้ง
    - สำหรับชื่อ key ให้ใส่ **key** และวาง key ที่คัดลอกจาก Azure ML Studio ลงในช่องค่า
    - หลังจากเพิ่ม key แล้ว ให้เลือก **is secret** เพื่อป้องกันการเปิดเผย key

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.th.png)

1. เลือก **Add connection**

#### สร้าง Prompt flow

คุณได้เพิ่มการเชื่อมต่อแบบกำหนดเองใน Azure AI Foundry แล้ว ตอนนี้มาสร้าง Prompt flow ด้วยขั้นตอนต่อไปนี้ จากนั้นคุณจะเชื่อมต่อ Prompt flow นี้กับการเชื่อมต่อแบบกำหนดเองเพื่อใช้โมเดลที่ปรับแต่งแล้วใน Prompt flow

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. เลือก **Prompt flow** จากแท็บด้านซ้าย

1. เลือก **+ Create** จากเมนูนำทาง

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.th.png)

1. เลือก **Chat flow** จากเมนูนำทาง

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.th.png)

1. กรอก **Folder name** ที่จะใช้

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.th.png)

1. เลือก **Create**

#### ตั้งค่า Prompt flow เพื่อแชทกับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเอง

คุณต้องรวมโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้วเข้ากับ Prompt flow อย่างไรก็ตาม Prompt flow ที่มีอยู่ไม่ได้ออกแบบมาเพื่อจุดประสงค์นี้ ดังนั้นคุณจึงต้องออกแบบ Prompt flow ใหม่เพื่อให้สามารถรวมโมเดลแบบกำหนดเองได้

1. ใน Prompt flow ให้ทำตามขั้นตอนต่อไปนี้เพื่อสร้าง flow ใหม่:

    - เลือก **Raw file mode**
    - ลบโค้ดทั้งหมดในไฟล์ *flow.dag.yml* ที่มีอยู่
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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.th.png)

1. เพิ่มโค้ดต่อไปนี้ลงใน *integrate_with_promptflow.py* เพื่อใช้โมเดล Phi-3 / Phi-3.5 แบบกำหนดเองใน Prompt flow

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.th.png)

> [!NOTE]
> สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้ Prompt flow ใน Azure AI Foundry คุณสามารถดูได้ที่ [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)

1. เลือก **Chat input**, **Chat output** เพื่อเปิดใช้งานการแชทกับโมเดลของคุณ

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.th.png)

1. ตอนนี้คุณพร้อมแชทกับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองแล้ว ในแบบฝึกหัดถัดไป คุณจะได้เรียนรู้วิธีเริ่ม Prompt flow และใช้งานเพื่อแชทกับโมเดลที่ปรับแต่งแล้ว

> [!NOTE]
>
> Flow ที่สร้างใหม่ควรมีลักษณะดังภาพด้านล่าง:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.th.png)
>

#### เริ่ม Prompt flow

1. เลือก **Start compute sessions** เพื่อเริ่ม Prompt flow

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.th.png)

1. เลือก **Validate and parse input** เพื่อรีเฟรชพารามิเตอร์

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.th.png)

1. เลือก **Value** ของ **connection** ไปยังการเชื่อมต่อแบบกำหนดเองที่คุณสร้างไว้ เช่น *connection*

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.th.png)

#### แชทกับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเอง

1. เลือก **Chat**

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.th.png)

1. นี่คือตัวอย่างผลลัพธ์: ตอนนี้คุณสามารถแชทกับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองได้ แนะนำให้ถามคำถามที่เกี่ยวข้องกับข้อมูลที่ใช้ในการปรับแต่งโมเดล

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.th.png)

### นำ Azure OpenAI มาใช้ประเมินโมเดล Phi-3 / Phi-3.5

เพื่อประเมินโมเดล Phi-3 / Phi-3.5 ใน Azure AI Foundry คุณต้องนำโมเดล Azure OpenAI มาใช้ โมเดลนี้จะใช้ในการประเมินประสิทธิภาพของโมเดล Phi-3 / Phi-3.5

#### นำ Azure OpenAI มาใช้

1. ลงชื่อเข้าใช้ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.th.png)

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Deployments** จากแท็บด้านซ้าย

1. เลือก **+ Deploy model** จากเมนูนำทาง

1. เลือก **Deploy base model**

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.th.png)

1. เลือกโมเดล Azure OpenAI ที่ต้องการใช้ เช่น **gpt-4o**

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.th.png)

1. เลือก **Confirm**

### ประเมินโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้วโดยใช้การประเมิน Prompt flow ของ Azure AI Foundry

### เริ่มการประเมินใหม่

1. เข้าไปที่ [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปยังโปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.th.png)

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Evaluation** จากแท็บด้านซ้าย

1. เลือก **+ New evaluation** จากเมนูนำทาง
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.th.png)

1. เลือกการประเมิน **Prompt flow**

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.th.png)

1. ทำงานตามขั้นตอนต่อไปนี้:

    - กรอกชื่อการประเมิน ต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือกประเภทงานเป็น **Question and answer without context** เพราะชุดข้อมูล **UlTRACHAT_200k** ที่ใช้ในบทเรียนนี้ไม่มีบริบท
    - เลือก prompt flow ที่ต้องการประเมิน

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.th.png)

1. เลือก **Next**

1. ทำงานตามขั้นตอนต่อไปนี้:

    - เลือก **Add your dataset** เพื่ออัปโหลดชุดข้อมูล เช่น ไฟล์ชุดข้อมูลทดสอบ *test_data.json1* ที่รวมมาเมื่อดาวน์โหลดชุดข้อมูล **ULTRACHAT_200k**
    - เลือก **Dataset column** ที่เหมาะสมกับชุดข้อมูลของคุณ เช่น หากใช้ชุดข้อมูล **ULTRACHAT_200k** ให้เลือก **${data.prompt}** เป็นคอลัมน์ชุดข้อมูล

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.th.png)

1. เลือก **Next**

1. ทำงานตามขั้นตอนต่อไปนี้เพื่อกำหนดค่าตัวชี้วัดประสิทธิภาพและคุณภาพ:

    - เลือกตัวชี้วัดประสิทธิภาพและคุณภาพที่ต้องการใช้
    - เลือกรุ่น Azure OpenAI ที่สร้างไว้สำหรับการประเมิน เช่น เลือก **gpt-4o**

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.th.png)

1. ทำงานตามขั้นตอนต่อไปนี้เพื่อกำหนดค่าตัวชี้วัดความเสี่ยงและความปลอดภัย:

    - เลือกตัวชี้วัดความเสี่ยงและความปลอดภัยที่ต้องการใช้
    - เลือกระดับเกณฑ์เพื่อคำนวณอัตราความผิดพลาด เช่น เลือก **Medium**
    - สำหรับ **question** เลือก **Data source** เป็น **{$data.prompt}**
    - สำหรับ **answer** เลือก **Data source** เป็น **{$run.outputs.answer}**
    - สำหรับ **ground_truth** เลือก **Data source** เป็น **{$data.message}**

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.th.png)

1. เลือก **Next**

1. เลือก **Submit** เพื่อเริ่มการประเมิน

1. การประเมินจะใช้เวลาสักครู่ คุณสามารถติดตามความคืบหน้าได้ที่แท็บ **Evaluation**

### ทบทวนผลลัพธ์การประเมิน

> [!NOTE]
> ผลลัพธ์ที่แสดงด้านล่างนี้มีไว้เพื่อแสดงตัวอย่างกระบวนการประเมิน ในบทเรียนนี้เราใช้โมเดลที่ปรับแต่งบนชุดข้อมูลขนาดค่อนข้างเล็ก ซึ่งอาจทำให้ผลลัพธ์ไม่สมบูรณ์แบบ ผลลัพธ์จริงอาจแตกต่างอย่างมากขึ้นอยู่กับขนาด คุณภาพ และความหลากหลายของชุดข้อมูลที่ใช้ รวมถึงการตั้งค่าของโมเดลแต่ละตัว

เมื่อการประเมินเสร็จสิ้น คุณสามารถตรวจสอบผลลัพธ์ทั้งตัวชี้วัดประสิทธิภาพและความปลอดภัยได้

1. ตัวชี้วัดประสิทธิภาพและคุณภาพ:

    - ประเมินประสิทธิผลของโมเดลในการสร้างคำตอบที่สอดคล้อง ลื่นไหล และเกี่ยวข้อง

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.th.png)

1. ตัวชี้วัดความเสี่ยงและความปลอดภัย:

    - ตรวจสอบให้แน่ใจว่าผลลัพธ์ของโมเดลปลอดภัยและสอดคล้องกับหลักการ Responsible AI หลีกเลี่ยงเนื้อหาที่เป็นอันตรายหรือไม่เหมาะสม

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.th.png)

1. คุณสามารถเลื่อนลงเพื่อดู **Detailed metrics result**

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.th.png)

1. โดยการประเมินโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองกับตัวชี้วัดทั้งประสิทธิภาพและความปลอดภัย คุณจะมั่นใจได้ว่าโมเดลไม่เพียงแต่มีประสิทธิภาพเท่านั้น แต่ยังสอดคล้องกับแนวปฏิบัติ Responsible AI พร้อมสำหรับการนำไปใช้งานจริง

## ขอแสดงความยินดี!

### คุณทำบทเรียนนี้สำเร็จแล้ว

คุณได้ประเมินโมเดล Phi-3 ที่ปรับแต่งแล้วซึ่งผสานกับ Prompt flow ใน Azure AI Foundry สำเร็จ นี่เป็นขั้นตอนสำคัญในการรับรองว่าโมเดล AI ของคุณไม่เพียงแต่ทำงานได้ดี แต่ยังสอดคล้องกับหลักการ Responsible AI ของ Microsoft เพื่อช่วยให้คุณสร้างแอปพลิเคชัน AI ที่น่าเชื่อถือและปลอดภัย

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.th.png)

## ทำความสะอาดทรัพยากร Azure

ลบทรัพยากร Azure ของคุณเพื่อหลีกเลี่ยงค่าใช้จ่ายเพิ่มเติม ไปที่พอร์ทัล Azure และลบทรัพยากรต่อไปนี้:

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
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่ถูกต้องและเชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยมืออาชีพที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้