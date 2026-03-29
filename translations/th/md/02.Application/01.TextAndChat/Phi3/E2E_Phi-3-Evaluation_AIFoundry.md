# ประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Microsoft Foundry โดยเน้นที่หลักการ AI ที่รับผิดชอบของ Microsoft

ตัวอย่างแบบครบวงจรนี้อ้างอิงจากคำแนะนำ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" จาก Microsoft Tech Community

## ภาพรวม

### คุณจะประเมินความปลอดภัยและประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Microsoft Foundry ได้อย่างไร?

การปรับแต่งโมเดลอาจนำไปสู่การตอบสนองที่ไม่คาดคิดหรือไม่พึงประสงค์ได้ เพื่อให้มั่นใจว่าโมเดลยังคงปลอดภัยและมีประสิทธิภาพจึงเป็นสิ่งสำคัญที่จะต้องประเมินความสามารถของโมเดลในการสร้างเนื้อหาที่เป็นอันตรายและความสามารถในการให้คำตอบที่ถูกต้อง มีความเกี่ยวข้อง และสอดคล้องกัน ในบทช่วยสอนนี้ คุณจะได้เรียนรู้วิธีการประเมินความปลอดภัยและประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งซึ่งรวมเข้ากับ Prompt flow ใน Microsoft Foundry

นี่คือกระบวนการประเมินของ Microsoft Foundry

![Architecture of tutorial.](../../../../../../translated_images/th/architecture.10bec55250f5d6a4.webp)

*แหล่งที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> สำหรับข้อมูลที่ละเอียดยิ่งขึ้นและเพื่อสำรวจแหล่งข้อมูลเพิ่มเติมเกี่ยวกับ Phi-3 / Phi-3.5 โปรดเยี่ยมชม [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)

### ความต้องการเบื้องต้น

- [Python](https://www.python.org/downloads)
- [การสมัครใช้งาน Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- โมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งแล้ว

### สารบัญ

1. [**สถานการณ์ที่ 1: แนะนำการประเมิน Prompt flow ของ Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [แนะนำการประเมินความปลอดภัย](#แนะนำการประเมินความปลอดภัย)
    - [แนะนำการประเมินประสิทธิภาพ](#แนะนำการประเมินประสิทธิภาพ)

1. [**สถานการณ์ที่ 2: การประเมินโมเดล Phi-3 / Phi-3.5 ใน Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [ก่อนเริ่มต้น](#ก่อนเริ่มต้น)
    - [ปรับใช้ Azure OpenAI เพื่อประเมินโมเดล Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [ประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งโดยใช้การประเมิน Prompt flow ของ Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [ขอแสดงความยินดี!](#ขอแสดงความยินดี)

## **สถานการณ์ที่ 1: แนะนำการประเมิน Prompt flow ของ Microsoft Foundry**

### แนะนำการประเมินความปลอดภัย

เพื่อให้แน่ใจว่าโมเดล AI ของคุณมีจริยธรรมและปลอดภัย สิ่งสำคัญคือการประเมินโมเดลเพื่อให้สอดคล้องกับหลักการ AI ที่รับผิดชอบของ Microsoft ใน Microsoft Foundry การประเมินความปลอดภัยจะช่วยให้คุณประเมินความอ่อนแอต่อการถูกโจมตีแบบ jailbreak และศักยภาพในการสร้างเนื้อหาที่เป็นอันตรายของโมเดล ซึ่งสอดคล้องโดยตรงกับหลักการเหล่านี้

![Safaty evaluation.](../../../../../../translated_images/th/safety-evaluation.083586ec88dfa950.webp)

*แหล่งที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### หลักการ AI ที่รับผิดชอบของ Microsoft

ก่อนเริ่มดำเนินการทางเทคนิค สิ่งสำคัญคือการเข้าใจหลักการ AI ที่รับผิดชอบของ Microsoft ซึ่งเป็นกรอบจริยธรรมที่ออกแบบมาเพื่อชี้แนะแนวทางการพัฒนา การใช้งาน และการดำเนินงานของระบบ AI อย่างรับผิดชอบ หลักการเหล่านี้ชี้แนะแนวทางการออกแบบ การพัฒนา และการใช้งานระบบ AI อย่างรับผิดชอบ เพื่อให้แน่ใจว่าเทคโนโลยี AI ถูกสร้างขึ้นอย่างเป็นธรรม โปร่งใส และครอบคลุม หลักการเหล่านี้เป็นรากฐานสำหรับการประเมินความปลอดภัยของโมเดล AI

หลักการ AI ที่รับผิดชอบของ Microsoft ประกอบด้วย:

- **ความเป็นธรรมและครอบคลุม**: ระบบ AI ควรปฏิบัติต่อทุกคนอย่างเป็นธรรมและหลีกเลี่ยงการมีผลกระทบต่อกลุ่มคนที่มีสถานการณ์คล้ายคลึงกันในลักษณะที่แตกต่างกัน ตัวอย่างเช่น เมื่อระบบ AI ให้คำแนะนำเกี่ยวกับการรักษาพยาบาล การขอสินเชื่อ หรือการจ้างงาน ระบบควรให้คำแนะนำเดียวกันแก่ทุกคนที่มีอาการ สถานการณ์ทางการเงิน หรือคุณสมบัติทางวิชาชีพที่คล้ายคลึงกัน

- **ความน่าเชื่อถือและความปลอดภัย**: เพื่อสร้างความไว้วางใจ ระบบ AI ต้องทำงานได้อย่างน่าเชื่อถือ ปลอดภัย และสม่ำเสมอ ระบบเหล่านี้ควรสามารถทำงานได้ตามที่ออกแบบไว้ ตอบสนองอย่างปลอดภัยต่อสถานการณ์ที่ไม่คาดคิด และทนทานต่อการถูกปรับเปลี่ยนที่เป็นอันตราย พฤติกรรมและสถานการณ์ที่ระบบจัดการได้สะท้อนถึงสถานการณ์และความคาดหวังที่นักพัฒนาคาดการณ์ไว้ในช่วงการออกแบบและทดสอบ

- **ความโปร่งใส**: เมื่อระบบ AI ช่วยตัดสินใจที่มีผลกระทบอย่างใหญ่หลวงต่อชีวิตของผู้คน เป็นสิ่งสำคัญที่ผู้คนจะเข้าใจว่าการตัดสินใจเหล่านั้นทำอย่างไร ตัวอย่างเช่น ธนาคารอาจใช้ระบบ AI เพื่อตัดสินว่าบุคคลหนึ่งน่าเชื่อถือทางการเงินหรือไม่ บริษัทอาจใช้ระบบ AI เพื่อตัดสินใจเลือกผู้สมัครที่มีคุณสมบัติเหมาะสมที่สุด

- **ความเป็นส่วนตัวและความปลอดภัย**: เมื่อ AI เริ่มมีบทบาทมากขึ้น การปกป้องความเป็นส่วนตัวและรักษาความปลอดภัยของข้อมูลส่วนบุคคลและข้อมูลเชิงธุรกิจจึงมีความสำคัญและซับซ้อนยิ่งขึ้น ด้วย AI ความเป็นส่วนตัวและความปลอดภัยของข้อมูลต้องได้รับความสนใจอย่างใกล้ชิด เพราะการเข้าถึงข้อมูลเป็นสิ่งสำคัญสำหรับระบบ AI ในการทำการทำนายและตัดสินใจที่ถูกต้องและมีข้อมูลประกอบ

- **ความรับผิดชอบ**: ผู้ที่ออกแบบและใช้งานระบบ AI ต้องรับผิดชอบต่อวิธีการทำงานของระบบ องค์กรควรใช้มาตรฐานอุตสาหกรรมเพื่อพัฒนากฎเกณฑ์ความรับผิดชอบ กฎเกณฑ์เหล่านี้ช่วยให้มั่นใจว่าระบบ AI จะไม่เป็นอำนาจสูงสุดในการตัดสินใจใดๆ ที่กระทบชีวิตผู้คน และช่วยให้มนุษย์ยังคงควบคุมระบบ AI อัตโนมัติในระดับสำคัญได้

![Fill hub.](../../../../../../translated_images/th/responsibleai2.c07ef430113fad8c.webp)

*แหล่งที่มาของภาพ: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับหลักการ AI ที่รับผิดชอบของ Microsoft โปรดเยี่ยมชม [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)

#### ตัวชี้วัดความปลอดภัย

ในบทช่วยสอนนี้ คุณจะประเมินความปลอดภัยของโมเดล Phi-3 ที่ผ่านการปรับแต่งโดยใช้ตัวชี้วัดความปลอดภัยของ Microsoft Foundry ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินศักยภาพของโมเดลในการสร้างเนื้อหาที่เป็นอันตรายและความอ่อนแอต่อการโจมตีแบบ jailbreak ตัวชี้วัดความปลอดภัยประกอบด้วย:

- **เนื้อหาที่เกี่ยวข้องกับการทำร้ายตนเอง**: ประเมินว่าโมเดลมีแนวโน้มที่จะผลิตเนื้อหาที่เกี่ยวข้องกับการทำร้ายตนเองหรือไม่
- **เนื้อหาที่เต็มไปด้วยความเกลียดชังและไม่เป็นธรรม**: ประเมินว่าโมเดลมีแนวโน้มที่จะแสดงเนื้อหาที่เต็มไปด้วยความเกลียดชังหรือไม่เป็นธรรมหรือไม่
- **เนื้อหารุนแรง**: ประเมินว่าโมเดลมีแนวโน้มที่จะผลิตเนื้อหารุนแรงหรือไม่
- **เนื้อหาทางเพศ**: ประเมินว่าโมเดลมีแนวโน้มที่จะผลิตเนื้อหาทางเพศที่ไม่เหมาะสมหรือไม่

การประเมินด้านเหล่านี้ช่วยให้มั่นใจว่าโมเดล AI จะไม่ผลิตเนื้อหาที่เป็นอันตรายหรือไม่เหมาะสม ซึ่งสอดคล้องกับค่านิยมทางสังคมและมาตรฐานด้านกฎระเบียบ

![Evaluate based on safety.](../../../../../../translated_images/th/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### แนะนำการประเมินประสิทธิภาพ

เพื่อให้แน่ใจว่าโมเดล AI ของคุณทำงานตามที่คาดหวัง สิ่งสำคัญคือการประเมินประสิทธิภาพของมันเทียบกับตัวชี้วัดประสิทธิภาพ ใน Microsoft Foundry การประเมินประสิทธิภาพช่วยให้คุณประเมินความสามารถของโมเดลในการสร้างคำตอบที่ถูกต้อง มีความเกี่ยวข้อง และสอดคล้องกัน

![Safaty evaluation.](../../../../../../translated_images/th/performance-evaluation.48b3e7e01a098740.webp)

*แหล่งที่มาของภาพ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### ตัวชี้วัดประสิทธิภาพ

ในบทช่วยสอนนี้ คุณจะประเมินประสิทธิภาพของโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งโดยใช้ตัวชี้วัดประสิทธิภาพของ Microsoft Foundry ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินประสิทธิผลของโมเดลในการสร้างคำตอบที่ถูกต้อง มีความเกี่ยวข้อง และสอดคล้องกัน ตัวชี้วัดประสิทธิภาพประกอบด้วย:

- **ความสอดคล้องกับข้อมูลต้นทาง (Groundedness)**: ประเมินว่าคำตอบที่สร้างขึ้นสอดคล้องกับข้อมูลจากแหล่งข้อมูลต้นทางมากน้อยเพียงใด
- **ความเกี่ยวข้อง (Relevance)**: ประเมินความเกี่ยวข้องของคำตอบที่สร้างขึ้นกับคำถามที่ได้รับ
- **ความสอดคล้องกัน (Coherence)**: ประเมินความไหลลื่นของข้อความที่สร้างขึ้น อ่านได้อย่างเป็นธรรมชาติ และคล้ายกับภาษาของมนุษย์
- **ความคล่องแคล่ว (Fluency)**: ประเมินความสามารถทางภาษาของข้อความที่สร้างขึ้น
- **ความคล้ายคลึงกับ GPT (GPT Similarity)**: เปรียบเทียบคำตอบที่สร้างขึ้นกับความจริงพื้นฐานเพื่อวัดความคล้ายคลึง
- **คะแนน F1 (F1 Score)**: คำนวณอัตราส่วนของคำที่ร่วมกันระหว่างคำตอบที่สร้างขึ้นและข้อมูลต้นทาง

ตัวชี้วัดเหล่านี้ช่วยให้คุณประเมินประสิทธิผลของโมเดลในการสร้างคำตอบที่ถูกต้อง มีความเกี่ยวข้อง และสอดคล้องกัน

![Evaluate based on performance.](../../../../../../translated_images/th/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **สถานการณ์ที่ 2: การประเมินโมเดล Phi-3 / Phi-3.5 ใน Microsoft Foundry**

### ก่อนเริ่มต้น

บทช่วยสอนนี้เป็นชุดต่อเนื่องจากบล็อกโพสต์ก่อนหน้า "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" และ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ซึ่งในโพสต์เหล่านี้เราได้สอนกระบวนการปรับแต่งโมเดล Phi-3 / Phi-3.5 ใน Microsoft Foundry และการรวมเข้ากับ Prompt flow

ในบทช่วยสอนนี้ คุณจะปรับใช้โมเดล Azure OpenAI เป็นผู้ประเมินใน Microsoft Foundry และใช้มันในการประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งของคุณ

ก่อนเริ่มบทช่วยสอนนี้ โปรดตรวจสอบให้แน่ใจว่าคุณมีความพร้อมดังต่อไปนี้ ตามที่ได้อธิบายไว้ในบทช่วยสอนก่อนหน้า:

1. ชุดข้อมูลที่เตรียมไว้สำหรับประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง
1. โมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งและปรับใช้ใน Azure Machine Learning แล้ว
1. Prompt flow ที่ผนวกเข้ากับโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งใน Microsoft Foundry

> [!NOTE]
> คุณจะใช้ไฟล์ *test_data.jsonl* ซึ่งอยู่ในโฟลเดอร์ data จากชุดข้อมูล **ULTRACHAT_200k** ที่ดาวน์โหลดจากบล็อกโพสต์ก่อนหน้า เป็นชุดข้อมูลสำหรับประเมินโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่ง

#### รวมโมเดล Phi-3 / Phi-3.5 ที่กำหนดเองเข้ากับ Prompt flow ใน Microsoft Foundry (วิธีการเขียนโค้ดก่อน)

> [!NOTE]
> หากคุณทำตามวิธี low-code ที่อธิบายใน "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" คุณสามารถข้ามแบบฝึกหัดนี้และดำเนินการต่อไปยังแบบฝึกหัดถัดไปได้
> อย่างไรก็ตาม หากคุณใช้วิธีเขียนโค้ดก่อนซึ่งอธิบายใน "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" เพื่อปรับแต่งและปรับใช้โมเดล Phi-3 / Phi-3.5 ของคุณ กระบวนการเชื่อมต่อโมเดลของคุณกับ Prompt flow จะมีความแตกต่างเล็กน้อย คุณจะได้เรียนรู้กระบวนการนี้ในแบบฝึกหัดนี้

ในการดำเนินการต่อ คุณต้องรวมโมเดล Phi-3 / Phi-3.5 ที่ผ่านการปรับแต่งของคุณเข้ากับ Prompt flow ใน Microsoft Foundry

#### สร้าง Microsoft Foundry Hub

คุณต้องสร้าง Hub ก่อนสร้างโปรเจ็กต์ Hub ทำหน้าที่เหมือน Resource Group ช่วยให้คุณจัดระเบียบและจัดการโปรเจ็กต์หลายชิ้นใน Microsoft Foundry ได้
1. ลงชื่อเข้าใช้ [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. เลือก **All hubs** จากแถบด้านซ้าย

1. เลือก **+ New hub** จากเมนูนำทาง

    ![Create hub.](../../../../../../translated_images/th/create-hub.5be78fb1e21ffbf1.webp)

1. ทำตามขั้นตอนดังต่อไปนี้:

    - กรอก **Hub name** ต้องเป็นค่าที่ไม่ซ้ำกัน
    - เลือก **Subscription** ของ Azure ของคุณ
    - เลือก **Resource group** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Location** ที่คุณต้องการใช้
    - เลือก **Connect Azure AI Services** ที่จะใช้ (สร้างใหม่ถ้าจำเป็น)
    - เลือก **Connect Azure AI Search** เป็น **Skip connecting**

    ![Fill hub.](../../../../../../translated_images/th/fill-hub.baaa108495c71e34.webp)

1. เลือก **Next**

#### สร้างโปรเจกต์ Microsoft Foundry

1. ใน Hub ที่คุณสร้างขึ้น เลือก **All projects** จากแถบด้านซ้าย

1. เลือก **+ New project** จากเมนูนำทาง

    ![Select new project.](../../../../../../translated_images/th/select-new-project.cd31c0404088d7a3.webp)

1. กรอก **Project name** ต้องเป็นค่าที่ไม่ซ้ำกัน

    ![Create project.](../../../../../../translated_images/th/create-project.ca3b71298b90e420.webp)

1. เลือก **Create a project**

#### เพิ่มการเชื่อมต่อแบบกำหนดเองสำหรับโมเดล Phi-3 / Phi-3.5 ที่ได้ปรับแต่งแล้ว

เพื่อรวมโมเดล Phi-3 / Phi-3.5 ที่คุณปรับแต่งเองกับ Prompt flow คุณต้องบันทึกจุดเชื่อมต่อและคีย์ของโมเดลไว้ในการเชื่อมต่อแบบกำหนดเอง วิธีนี้จะทำให้สามารถเข้าถึงโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองใน Prompt flow ได้

#### กำหนดค่า api key และ endpoint uri ของโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้ว

1. ไปที่ [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)

1. ไปที่ Azure Machine learning workspace ที่คุณสร้างไว้

1. เลือก **Endpoints** จากแถบด้านซ้าย

    ![Select endpoints.](../../../../../../translated_images/th/select-endpoints.ee7387ecd68bd18d.webp)

1. เลือก endpoint ที่คุณสร้างไว้

    ![Select endpoints.](../../../../../../translated_images/th/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. เลือก **Consume** จากเมนูนำทาง

1. คัดลอก **REST endpoint** และ **Primary key** ของคุณ

    ![Copy api key and endpoint uri.](../../../../../../translated_images/th/copy-endpoint-key.0650c3786bd646ab.webp)

#### เพิ่มการเชื่อมต่อแบบกำหนดเอง

1. ไปที่ [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปที่โปรเจกต์ Microsoft Foundry ที่คุณสร้างไว้

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Settings** จากแถบด้านซ้าย

1. เลือก **+ New connection**

    ![Select new connection.](../../../../../../translated_images/th/select-new-connection.fa0f35743758a74b.webp)

1. เลือก **Custom keys** จากเมนูนำทาง

    ![Select custom keys.](../../../../../../translated_images/th/select-custom-keys.5a3c6b25580a9b67.webp)

1. ทำตามขั้นตอนดังนี้:

    - เลือก **+ Add key value pairs**
    - สำหรับชื่อคีย์ ให้ใส่ **endpoint** และวาง endpoint ที่คุณคัดลอกจาก Azure ML Studio ในช่องค่า
    - เลือก **+ Add key value pairs** อีกครั้ง
    - สำหรับชื่อคีย์ ให้ใส่ **key** และวางคีย์ที่คุณคัดลอกจาก Azure ML Studio ในช่องค่า
    - หลังจากเพิ่มคีย์แล้ว ให้เลือก **is secret** เพื่อป้องกันไม่ให้คีย์ถูกเปิดเผย

    ![Add connection.](../../../../../../translated_images/th/add-connection.ac7f5faf8b10b0df.webp)

1. เลือก **Add connection**

#### สร้าง Prompt flow

คุณได้เพิ่มการเชื่อมต่อแบบกำหนดเองใน Microsoft Foundry แล้ว ตอนนี้เราจะสร้าง Prompt flow โดยใช้ขั้นตอนต่อไปนี้ จากนั้นคุณจะเชื่อมต่อ Prompt flow นี้กับการเชื่อมต่อแบบกำหนดเองเพื่อใช้โมเดลที่ปรับแต่งแล้วใน Prompt flow

1. ไปที่โปรเจกต์ Microsoft Foundry ที่คุณสร้างไว้

1. เลือก **Prompt flow** จากแถบด้านซ้าย

1. เลือก **+ Create** จากเมนูนำทาง

    ![Select Promptflow.](../../../../../../translated_images/th/select-promptflow.18ff2e61ab9173eb.webp)

1. เลือก **Chat flow** จากเมนูนำทาง

    ![Select chat flow.](../../../../../../translated_images/th/select-flow-type.28375125ec9996d3.webp)

1. กรอก **Folder name** ที่ต้องการใช้

    ![Select chat flow.](../../../../../../translated_images/th/enter-name.02ddf8fb840ad430.webp)

1. เลือก **Create**

#### ตั้งค่า Prompt flow เพื่อแชทกับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองของคุณ

คุณต้องผสานโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้วเข้ากับ Prompt flow อย่างไรก็ตาม Prompt flow ที่มีอยู่ไม่ได้ออกแบบมาสำหรับวัตถุประสงค์นี้ ดังนั้นคุณต้องออกแบบ Prompt flow ใหม่เพื่อให้รองรับการผสานโมเดลแบบกำหนดเองได้

1. ใน Prompt flow ให้ทำตามขั้นตอนดังนี้เพื่อสร้าง flow ใหม่:

    - เลือก **Raw file mode**
    - ลบโค้ดทั้งหมดที่มีอยู่ในไฟล์ *flow.dag.yml*
    - เพิ่มโค้ดดังต่อไปนี้ใน *flow.dag.yml*

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

    ![Select raw file mode.](../../../../../../translated_images/th/select-raw-file-mode.06c1eca581ce4f53.webp)

1. เพิ่มโค้ดดังต่อไปนี้ใน *integrate_with_promptflow.py* เพื่อใช้โมเดล Phi-3 / Phi-3.5 แบบกำหนดเองใน Prompt flow

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # การตั้งค่าการบันทึก
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

        # "connection" คือชื่อของการเชื่อมต่อแบบกำหนดเอง, "endpoint", "key" คือคีย์ในการเชื่อมต่อแบบกำหนดเอง
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
            
            # บันทึกการตอบกลับ JSON แบบเต็ม
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

    ![Paste prompt flow code.](../../../../../../translated_images/th/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> สำหรับข้อมูลที่ละเอียดขึ้นเกี่ยวกับการใช้ Prompt flow ใน Microsoft Foundry สามารถดูได้ที่ [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)

1. เลือก **Chat input**, **Chat output** เพื่อเปิดใช้งานการแชทกับโมเดลของคุณ

    ![Select Input Output.](../../../../../../translated_images/th/select-input-output.c187fc58f25fbfc3.webp)

1. ตอนนี้คุณพร้อมที่จะสนทนากับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้วของคุณแล้ว ในแบบฝึกหัดถัดไป คุณจะได้เรียนรู้วิธีเริ่ม Prompt flow และใช้งานเพื่อสนทนากับโมเดลที่ปรับแต่งแล้วนี้

> [!NOTE]
>
> โฟลว์ที่สร้างใหม่ควรมีลักษณะเหมือนภาพด้านล่างนี้:
>
> ![Flow example](../../../../../../translated_images/th/graph-example.82fd1bcdd3fc545b.webp)
>

#### เริ่ม Prompt flow

1. เลือก **Start compute sessions** เพื่อเริ่ม Prompt flow

    ![Start compute session.](../../../../../../translated_images/th/start-compute-session.9acd8cbbd2c43df1.webp)

1. เลือก **Validate and parse input** เพื่อรีเฟรชพารามิเตอร์

    ![Validate input.](../../../../../../translated_images/th/validate-input.c1adb9543c6495be.webp)

1. เลือก **Value** ของ **connection** ให้เป็นการเชื่อมต่อแบบกำหนดเองที่คุณสร้าง เช่น *connection*

    ![Connection.](../../../../../../translated_images/th/select-connection.1f2b59222bcaafef.webp)

#### สนทนากับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองของคุณ

1. เลือก **Chat**

    ![Select chat.](../../../../../../translated_images/th/select-chat.0406bd9687d0c49d.webp)

1. นี่คือตัวอย่างผลลัพธ์: ตอนนี้คุณสามารถสนทนากับโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองได้ แนะนำให้ถามคำถามที่เกี่ยวข้องกับข้อมูลที่ใช้สำหรับการปรับแต่ง

    ![Chat with prompt flow.](../../../../../../translated_images/th/chat-with-promptflow.1cf8cea112359ada.webp)

### เปิดใช้งาน Azure OpenAI เพื่อตรวจสอบโมเดล Phi-3 / Phi-3.5

เพื่อตรวจสอบโมเดล Phi-3 / Phi-3.5 ใน Microsoft Foundry คุณต้องเปิดใช้งานโมเดล Azure OpenAI โมเดลนี้จะถูกใช้เพื่อประเมินประสิทธิภาพของโมเดล Phi-3 / Phi-3.5

#### เปิดใช้งาน Azure OpenAI

1. ลงชื่อเข้าใช้ [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปที่โปรเจกต์ Microsoft Foundry ที่คุณสร้างไว้

    ![Select Project.](../../../../../../translated_images/th/select-project-created.5221e0e403e2c9d6.webp)

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Deployments** จากแถบด้านซ้าย

1. เลือก **+ Deploy model** จากเมนูนำทาง

1. เลือก **Deploy base model**

    ![Select Deployments.](../../../../../../translated_images/th/deploy-openai-model.95d812346b25834b.webp)

1. เลือกโมเดล Azure OpenAI ที่คุณต้องการใช้ เช่น **gpt-4o**

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/th/select-openai-model.959496d7e311546d.webp)

1. เลือก **Confirm**

### ประเมินโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้วโดยใช้ Prompt flow evaluation ของ Microsoft Foundry

### เริ่มการประเมินใหม่

1. ไปที่ [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)

1. ไปที่โปรเจกต์ Microsoft Foundry ที่คุณสร้างไว้

    ![Select Project.](../../../../../../translated_images/th/select-project-created.5221e0e403e2c9d6.webp)

1. ในโปรเจกต์ที่คุณสร้าง เลือก **Evaluation** จากแถบด้านซ้าย

1. เลือก **+ New evaluation** จากเมนูนำทาง

    ![Select evaluation.](../../../../../../translated_images/th/select-evaluation.2846ad7aaaca7f4f.webp)

1. เลือกประเมินผล **Prompt flow**

    ![Select Prompt flow evaluation.](../../../../../../translated_images/th/promptflow-evaluation.cb9758cc19b4760f.webp)

1. ทำตามขั้นตอนดังนี้:

    - กรอกชื่อการประเมินผล ต้องไม่ซ้ำกัน
    - เลือกประเภทงานเป็น **Question and answer without context** เนื่องจากชุดข้อมูล **UlTRACHAT_200k** ที่ใช้ในบทเรียนนี้ไม่มีบริบท
    - เลือก prompt flow ที่คุณต้องการประเมิน

    ![Prompt flow evaluation.](../../../../../../translated_images/th/evaluation-setting1.4aa08259ff7a536e.webp)

1. เลือก **Next**

1. ทำตามขั้นตอนดังนี้:

    - เลือก **Add your dataset** เพื่ออัปโหลดชุดข้อมูล เช่น ไฟล์ชุดข้อมูลทดสอบ *test_data.json1* ที่แนบมากับชุดข้อมูล **ULTRACHAT_200k**
    - เลือกคอลัมน์ชุดข้อมูลที่เหมาะสมกับชุดข้อมูล เช่น ถ้าใช้ชุดข้อมูล **ULTRACHAT_200k** ให้เลือก **${data.prompt}** เป็นคอลัมน์ชุดข้อมูล

    ![Prompt flow evaluation.](../../../../../../translated_images/th/evaluation-setting2.07036831ba58d64e.webp)

1. เลือก **Next**

1. ทำตามขั้นตอนเพื่อกำหนดค่าตัวชี้วัดประสิทธิภาพและคุณภาพ:

    - เลือกตัวชี้วัดประสิทธิภาพและคุณภาพที่ต้องการใช้
    - เลือกโมเดล Azure OpenAI ที่คุณสร้างเพื่อใช้ประเมิน เช่น เลือก **gpt-4o**

    ![Prompt flow evaluation.](../../../../../../translated_images/th/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. กำหนดค่าวัดความเสี่ยงและความปลอดภัยดังนี้:

    - เลือกตัวชี้วัดความเสี่ยงและความปลอดภัยที่ต้องการใช้
    - เลือกเกณฑ์ขั้นต่ำเพื่อคำนวณอัตราข้อบกพร่อง เช่น เลือก **Medium**
    - สำหรับ **question** เลือก **Data source** เป็น **{$data.prompt}**
    - สำหรับ **answer** เลือก **Data source** เป็น **{$run.outputs.answer}**
    - สำหรับ **ground_truth** เลือก **Data source** เป็น **{$data.message}**

    ![Prompt flow evaluation.](../../../../../../translated_images/th/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. เลือก **Next**

1. เลือก **Submit** เพื่อเริ่มการประเมินผล

1. การประเมินผลจะใช้เวลาสักครู่ในการดำเนินการ คุณสามารถติดตามความคืบหน้าได้ในแท็บ **Evaluation**

### ตรวจสอบผลการประเมิน

> [!NOTE]
> ผลลัพธ์ที่แสดงด้านล่างนี้มีไว้เพื่อแสดงกระบวนการประเมิน ในบทเรียนนี้เราใช้โมเดลที่ปรับแต่งบนชุดข้อมูลขนาดเล็กซึ่งอาจทำให้ผลลัพธ์ไม่เต็มประสิทธิภาพ ผลลัพธ์จริงอาจแตกต่างอย่างมากขึ้นอยู่กับขนาด คุณภาพ และความหลากหลายของชุดข้อมูล รวมถึงการตั้งค่าเฉพาะของโมเดลด้วย

เมื่อการประเมินเสร็จสิ้น คุณสามารถตรวจสอบผลลัพธ์ได้ทั้งตัวชี้วัดประสิทธิภาพและความปลอดภัย
1. ตัวชี้วัดประสิทธิภาพและคุณภาพ:

    - ประเมินประสิทธิผลของโมเดลในการสร้างคำตอบที่สอดคล้อง ลื่นไหล และเกี่ยวข้อง

    ![Evaluation result.](../../../../../../translated_images/th/evaluation-result-gpu.85f48b42dfb74254.webp)

1. ตัวชี้วัดความเสี่ยงและความปลอดภัย:

    - ตรวจสอบให้แน่ใจว่าผลลัพธ์ของโมเดลปลอดภัยและสอดคล้องกับหลักการ AI ที่มีความรับผิดชอบ ป้องกันเนื้อหาที่เป็นอันตรายหรือหยาบคาย

    ![Evaluation result.](../../../../../../translated_images/th/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. คุณสามารถเลื่อนลงเพื่อดู **ผลลัพธ์ตัวชี้วัดโดยละเอียด**

    ![Evaluation result.](../../../../../../translated_images/th/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. โดยการประเมินโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งเองของคุณทั้งในแง่ของตัวชี้วัดประสิทธิภาพและความปลอดภัย คุณสามารถยืนยันได้ว่าโมเดลไม่เพียงแต่มีประสิทธิผล แต่ยังปฏิบัติตามหลักการ AI ที่มีความรับผิดชอบ ทำให้พร้อมสำหรับการใช้งานจริง

## ขอแสดงความยินดี!

### คุณได้ทำแบบฝึกหัดนี้เสร็จสมบูรณ์แล้ว

คุณได้ประเมินโมเดล Phi-3 ที่ปรับแต่งแล้วซึ่งผสานรวมกับ Prompt flow ใน Microsoft Foundry เรียบร้อยแล้ว นี่เป็นขั้นตอนสำคัญในการรับรองว่าแบบจำลอง AI ของคุณไม่เพียงแต่ทำงานได้ดีเท่านั้น แต่ยังปฏิบัติตามหลักการ AI ที่มีความรับผิดชอบของ Microsoft ซึ่งจะช่วยให้คุณสร้างแอปพลิเคชัน AI ที่น่าเชื่อถือและไว้วางใจได้

![Architecture.](../../../../../../translated_images/th/architecture.10bec55250f5d6a4.webp)

## การทำความสะอาดทรัพยากร Azure

ล้างทรัพยากร Azure ของคุณเพื่อหลีกเลี่ยงค่าใช้จ่ายเพิ่มเติมในบัญชีของคุณ ไปที่พอร์ทัล Azure และลบทรัพยากรดังต่อไปนี้:

- ทรัพยากร Azure Machine learning
- จุดสิ้นสุดโมเดล Azure Machine learning
- ทรัพยากรโปรเจกต์ Microsoft Foundry
- ทรัพยากร Prompt flow ของ Microsoft Foundry

### ขั้นตอนต่อไป

#### เอกสาร

- [ประเมินระบบ AI โดยใช้แดชบอร์ด Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [ตัวชี้วัดการประเมินและการตรวจสอบสำหรับ AI สร้างสรรค์](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [เอกสาร Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [เอกสาร Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### เนื้อหาการฝึกอบรม

- [แนะนำแนวทาง Responsible AI ของ Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [แนะนำ Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### อ้างอิง

- [AI ที่มีความรับผิดชอบคืออะไร?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [ประกาศเครื่องมือใหม่ใน Azure AI เพื่อช่วยคุณสร้างแอปพลิเคชัน AI สร้างสรรค์ที่ปลอดภัยและน่าเชื่อถือมากขึ้น](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [การประเมินแอปพลิเคชัน AI สร้างสรรค์](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ควรใช้การแปลโดยผู้เชี่ยวชาญด้านมนุษย์ เรายังไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->