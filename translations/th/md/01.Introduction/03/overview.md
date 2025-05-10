<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:25:43+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "th"
}
-->
ในบริบทของ Phi-3-mini การ inference หมายถึงกระบวนการใช้โมเดลในการทำนายหรือสร้างผลลัพธ์จากข้อมูลนำเข้า ให้ผมอธิบายรายละเอียดเพิ่มเติมเกี่ยวกับ Phi-3-mini และความสามารถในการ inference ของมัน

Phi-3-mini เป็นส่วนหนึ่งของซีรีส์โมเดล Phi-3 ที่พัฒนาโดย Microsoft โมเดลเหล่านี้ถูกออกแบบมาเพื่อเปลี่ยนแปลงขอบเขตของความเป็นไปได้กับ Small Language Models (SLMs)

นี่คือจุดสำคัญบางประการเกี่ยวกับ Phi-3-mini และความสามารถในการ inference ของมัน:

## **ภาพรวมของ Phi-3-mini:**
- Phi-3-mini มีขนาดพารามิเตอร์ 3.8 พันล้าน
- สามารถทำงานได้ไม่เพียงแค่บนอุปกรณ์คอมพิวเตอร์ทั่วไป แต่ยังรวมถึงอุปกรณ์ edge เช่น อุปกรณ์มือถือและอุปกรณ์ IoT
- การเปิดตัว Phi-3-mini ช่วยให้บุคคลและองค์กรสามารถติดตั้ง SLMs บนอุปกรณ์ฮาร์ดแวร์ต่างๆ โดยเฉพาะในสภาพแวดล้อมที่มีข้อจำกัดด้านทรัพยากร
- รองรับรูปแบบโมเดลหลากหลาย รวมถึงรูปแบบ PyTorch แบบดั้งเดิม รูปแบบ gguf ที่ถูก quantize และรุ่น quantized บนพื้นฐาน ONNX

## **การเข้าถึง Phi-3-mini:**
เพื่อเข้าถึง Phi-3-mini คุณสามารถใช้ [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ในแอปพลิเคชัน Copilot Semantic Kernel โดยทั่วไปเข้ากันได้กับ Azure OpenAI Service, โมเดลโอเพ่นซอร์สบน Hugging Face และโมเดลในเครื่อง
คุณยังสามารถใช้ [Ollama](https://ollama.com) หรือ [LlamaEdge](https://llamaedge.com) เพื่อเรียกใช้โมเดล quantized Ollama อนุญาตให้ผู้ใช้แต่ละคนเรียกใช้โมเดล quantized ต่างๆ ในขณะที่ LlamaEdge ให้บริการข้ามแพลตฟอร์มสำหรับโมเดล GGUF

## **โมเดล Quantized:**
ผู้ใช้จำนวนมากชอบใช้โมเดล quantized สำหรับการ inference ในเครื่อง ตัวอย่างเช่น คุณสามารถรัน Ollama run Phi-3 โดยตรง หรือกำหนดค่าแบบออฟไลน์โดยใช้ Modelfile ซึ่ง Modelfile จะระบุเส้นทางไฟล์ GGUF และรูปแบบ prompt

## **ความเป็นไปได้ของ Generative AI:**
การผสมผสาน SLMs อย่าง Phi-3-mini เปิดโอกาสใหม่ๆ สำหรับ generative AI การ inference เป็นเพียงขั้นตอนแรก; โมเดลเหล่านี้สามารถนำไปใช้ในงานหลากหลายในสถานการณ์ที่มีข้อจำกัดด้านทรัพยากร, latency ต่ำ และต้นทุนจำกัด

## **ปลดล็อก Generative AI กับ Phi-3-mini: คู่มือการ Inference และ Deployment**  
เรียนรู้วิธีใช้ Semantic Kernel, Ollama/LlamaEdge และ ONNX Runtime เพื่อเข้าถึงและทำ inference กับโมเดล Phi-3-mini พร้อมสำรวจความเป็นไปได้ของ generative AI ในสถานการณ์การใช้งานต่างๆ

**คุณสมบัติ**
Inference โมเดล phi3-mini ใน:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

โดยสรุป Phi-3-mini ช่วยให้นักพัฒนาสามารถสำรวจรูปแบบโมเดลต่างๆ และใช้ประโยชน์จาก generative AI ในสถานการณ์การใช้งานที่หลากหลายได้

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่น่าเชื่อถือที่สุด สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้