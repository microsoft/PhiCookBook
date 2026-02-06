ในบริบทของ Phi-3-mini การทำ inference หมายถึงกระบวนการใช้โมเดลเพื่อทำนายหรือสร้างผลลัพธ์จากข้อมูลนำเข้า ให้ผมอธิบายรายละเอียดเพิ่มเติมเกี่ยวกับ Phi-3-mini และความสามารถในการทำ inference ของมัน

Phi-3-mini เป็นส่วนหนึ่งของชุดโมเดล Phi-3 ที่พัฒนาโดย Microsoft โมเดลเหล่านี้ถูกออกแบบมาเพื่อเปลี่ยนแปลงขอบเขตความเป็นไปได้ของ Small Language Models (SLMs)

นี่คือประเด็นสำคัญเกี่ยวกับ Phi-3-mini และความสามารถในการทำ inference ของมัน:

## **ภาพรวมของ Phi-3-mini:**
- Phi-3-mini มีขนาดพารามิเตอร์ 3.8 พันล้าน
- สามารถทำงานได้ไม่เพียงแค่บนอุปกรณ์คอมพิวเตอร์ทั่วไป แต่ยังรวมถึงอุปกรณ์ edge เช่น อุปกรณ์มือถือและอุปกรณ์ IoT
- การเปิดตัว Phi-3-mini ช่วยให้บุคคลและองค์กรสามารถนำ SLMs ไปใช้งานบนฮาร์ดแวร์ที่หลากหลาย โดยเฉพาะในสภาพแวดล้อมที่มีข้อจำกัดด้านทรัพยากร
- รองรับรูปแบบโมเดลหลากหลาย รวมถึงรูปแบบ PyTorch แบบดั้งเดิม, รูปแบบ gguf ที่ถูก quantized และรูปแบบ ONNX ที่ถูก quantized

## **การเข้าถึง Phi-3-mini:**
เพื่อเข้าถึง Phi-3-mini คุณสามารถใช้ [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ในแอปพลิเคชัน Copilot Semantic Kernel โดยทั่วไปรองรับ Azure OpenAI Service, โมเดลโอเพนซอร์สบน Hugging Face และโมเดลที่รันในเครื่อง
คุณยังสามารถใช้ [Ollama](https://ollama.com) หรือ [LlamaEdge](https://llamaedge.com) เพื่อเรียกใช้โมเดลที่ถูก quantized Ollama อนุญาตให้ผู้ใช้แต่ละคนเรียกใช้โมเดล quantized ต่างๆ ได้ ขณะที่ LlamaEdge ให้บริการข้ามแพลตฟอร์มสำหรับโมเดล GGUF

## **โมเดลที่ถูก Quantized:**
ผู้ใช้จำนวนมากนิยมใช้โมเดลที่ถูก quantized สำหรับการทำ inference ในเครื่อง เช่น คุณสามารถรัน Ollama เพื่อเรียกใช้ Phi-3 โดยตรง หรือกำหนดค่าแบบออฟไลน์ผ่าน Modelfile ซึ่งระบุเส้นทางไฟล์ GGUF และรูปแบบ prompt

## **ความเป็นไปได้ของ Generative AI:**
การรวม SLMs อย่าง Phi-3-mini เปิดโอกาสใหม่ๆ สำหรับ generative AI การทำ inference เป็นเพียงก้าวแรก โมเดลเหล่านี้สามารถนำไปใช้ในงานต่างๆ ที่มีข้อจำกัดด้านทรัพยากร ความหน่วงเวลา และต้นทุน

## **ปลดล็อก Generative AI ด้วย Phi-3-mini: คู่มือการทำ Inference และ Deployment**  
เรียนรู้วิธีใช้ Semantic Kernel, Ollama/LlamaEdge และ ONNX Runtime เพื่อเข้าถึงและทำ inference กับโมเดล Phi-3-mini พร้อมสำรวจความเป็นไปได้ของ generative AI ในสถานการณ์การใช้งานต่างๆ

**คุณสมบัติ**  
ทำ inference กับโมเดล phi3-mini ใน:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

สรุปแล้ว Phi-3-mini ช่วยให้นักพัฒนาสามารถสำรวจรูปแบบโมเดลที่หลากหลายและใช้ประโยชน์จาก generative AI ในสถานการณ์การใช้งานที่แตกต่างกันได้อย่างมีประสิทธิภาพ

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้