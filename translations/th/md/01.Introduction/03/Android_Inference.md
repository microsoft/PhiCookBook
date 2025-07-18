<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:13:52+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "th"
}
-->
# **การทำ Inference Phi-3 บน Android**

มาดูกันว่าคุณจะทำ inference กับ Phi-3-mini บนอุปกรณ์ Android ได้อย่างไร Phi-3-mini เป็นซีรีส์โมเดลใหม่จาก Microsoft ที่ช่วยให้สามารถนำ Large Language Models (LLMs) ไปใช้งานบนอุปกรณ์ edge และอุปกรณ์ IoT ได้

## Semantic Kernel และการทำ Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) คือเฟรมเวิร์กสำหรับสร้างแอปพลิเคชันที่รองรับ Azure OpenAI Service, โมเดล OpenAI และแม้แต่โมเดลที่รันในเครื่อง หากคุณยังไม่คุ้นเคยกับ Semantic Kernel เราแนะนำให้ดูที่ [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)

### การเข้าถึง Phi-3-mini ด้วย Semantic Kernel

คุณสามารถผสานกับ Hugging Face Connector ใน Semantic Kernel ได้ ดูตัวอย่างโค้ดนี้ [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)

โดยค่าเริ่มต้นจะเชื่อมต่อกับ model ID บน Hugging Face แต่คุณก็สามารถเชื่อมต่อกับเซิร์ฟเวอร์โมเดล Phi-3-mini ที่สร้างขึ้นในเครื่องได้เช่นกัน

### การเรียกใช้โมเดล Quantized ด้วย Ollama หรือ LlamaEdge

ผู้ใช้หลายคนชอบใช้โมเดล quantized เพื่อรันโมเดลในเครื่อง [Ollama](https://ollama.com/) และ [LlamaEdge](https://llamaedge.com) ช่วยให้ผู้ใช้แต่ละคนเรียกใช้โมเดล quantized ต่างๆ ได้

#### Ollama

คุณสามารถรันคำสั่ง `ollama run Phi-3` ได้โดยตรง หรือจะตั้งค่าแบบออฟไลน์โดยสร้างไฟล์ `Modelfile` ที่ระบุเส้นทางไปยังไฟล์ `.gguf` ของคุณ

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

ถ้าคุณต้องการใช้ไฟล์ `.gguf` ทั้งบนคลาวด์และอุปกรณ์ edge พร้อมกัน LlamaEdge เป็นตัวเลือกที่ดี คุณสามารถดูตัวอย่างโค้ดนี้ [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) เพื่อเริ่มต้น

### การติดตั้งและใช้งานบนโทรศัพท์ Android

1. **ดาวน์โหลดแอป MLC Chat** (ฟรี) สำหรับโทรศัพท์ Android  
2. ดาวน์โหลดไฟล์ APK (ขนาด 148MB) และติดตั้งบนอุปกรณ์ของคุณ  
3. เปิดแอป MLC Chat คุณจะเห็นรายชื่อโมเดล AI รวมถึง Phi-3-mini

สรุปแล้ว Phi-3-mini เปิดโอกาสใหม่ๆ สำหรับ generative AI บนอุปกรณ์ edge และคุณสามารถเริ่มสำรวจความสามารถนี้บน Android ได้ทันที

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้