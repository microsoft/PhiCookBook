<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-09T14:10:42+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "th"
}
-->
# **การควอนไทซ์ Phi Family โดยใช้ llama.cpp**

## **llama.cpp คืออะไร**

llama.cpp เป็นไลบรารีซอฟต์แวร์โอเพนซอร์สที่เขียนด้วยภาษา C++ เป็นหลัก ใช้สำหรับการทำ inference กับ Large Language Models (LLMs) ต่างๆ เช่น Llama จุดประสงค์หลักคือเพื่อให้การทำ inference ของ LLM มีประสิทธิภาพสูงสุดบนฮาร์ดแวร์หลากหลายประเภทโดยตั้งค่าขั้นต่ำ นอกจากนี้ยังมี Python bindings สำหรับไลบรารีนี้ที่ให้ API ระดับสูงสำหรับการเติมข้อความและเว็บเซิร์ฟเวอร์ที่รองรับ OpenAI

เป้าหมายหลักของ llama.cpp คือการทำให้การทำ inference กับ LLM เป็นไปได้ง่ายและมีประสิทธิภาพสูงบนฮาร์ดแวร์หลากหลายประเภท ทั้งในเครื่องและบนคลาวด์

- การใช้งานแบบ C/C++ ล้วนโดยไม่ต้องพึ่งพาไลบรารีอื่น
- รองรับ Apple silicon อย่างเต็มที่ โดยปรับแต่งผ่าน ARM NEON, Accelerate และ Metal frameworks
- รองรับ AVX, AVX2 และ AVX512 สำหรับสถาปัตยกรรม x86
- ควอนไทซ์แบบจำนวนเต็ม 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit และ 8-bit เพื่อเพิ่มความเร็วในการ inference และลดการใช้หน่วยความจำ
- มี CUDA kernels ที่ปรับแต่งสำหรับการรัน LLM บน NVIDIA GPUs (รองรับ AMD GPUs ผ่าน HIP)
- รองรับ backend แบบ Vulkan และ SYCL
- การ inference แบบผสม CPU+GPU เพื่อเร่งความเร็วโมเดลที่มีขนาดใหญ่เกินกว่าความจุ VRAM ทั้งหมด

## **การควอนไทซ์ Phi-3.5 ด้วย llama.cpp**

โมเดล Phi-3.5-Instruct สามารถควอนไทซ์ได้โดยใช้ llama.cpp แต่ Phi-3.5-Vision และ Phi-3.5-MoE ยังไม่รองรับ รูปแบบที่แปลงโดย llama.cpp คือ gguf ซึ่งเป็นรูปแบบควอนไทซ์ที่ได้รับความนิยมมากที่สุด

มีโมเดลในรูปแบบ GGUF ที่ควอนไทซ์แล้วจำนวนมากบน Hugging Face AI Foundry, Ollama และ LlamaEdge ใช้ llama.cpp ดังนั้นโมเดล GGUF จึงถูกใช้งานบ่อยเช่นกัน

### **GGUF คืออะไร**

GGUF เป็นรูปแบบไบนารีที่ถูกออกแบบมาให้โหลดและบันทึกโมเดลได้อย่างรวดเร็ว เหมาะสำหรับการทำ inference GGUF ถูกออกแบบมาใช้กับ GGML และ executors อื่นๆ GGUF ถูกพัฒนาโดย @ggerganov ผู้พัฒนา llama.cpp ซึ่งเป็นเฟรมเวิร์ก C/C++ สำหรับการทำ inference LLM โมเดลที่พัฒนาด้วยเฟรมเวิร์กอย่าง PyTorch สามารถแปลงเป็นรูปแบบ GGUF เพื่อใช้งานกับเอนจินเหล่านี้ได้

### **ONNX กับ GGUF**

ONNX เป็นรูปแบบสำหรับ machine learning/deep learning แบบดั้งเดิมที่ได้รับการสนับสนุนอย่างดีในเฟรมเวิร์ก AI ต่างๆ และเหมาะกับการใช้งานบนอุปกรณ์ edge ส่วน GGUF นั้นพัฒนาขึ้นจาก llama.cpp และถือเป็นรูปแบบที่เกิดขึ้นในยุค GenAI ทั้งสองมีการใช้งานที่คล้ายกัน หากต้องการประสิทธิภาพที่ดีกว่าในฮาร์ดแวร์ฝังตัวและชั้นแอปพลิเคชัน ONNX อาจเป็นตัวเลือกที่เหมาะสม แต่ถ้าใช้เฟรมเวิร์กและเทคโนโลยีที่พัฒนาต่อยอดจาก llama.cpp GGUF อาจเหมาะสมกว่า

### **การควอนไทซ์ Phi-3.5-Instruct โดยใช้ llama.cpp**

**1. การตั้งค่าสภาพแวดล้อม**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. การควอนไทซ์**

ใช้ llama.cpp แปลง Phi-3.5-Instruct เป็น FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

ควอนไทซ์ Phi-3.5 เป็น INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. การทดสอบ**

ติดตั้ง llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***หมายเหตุ***

ถ้าใช้ Apple Silicon กรุณาติดตั้ง llama-cpp-python ด้วยวิธีนี้


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

การทดสอบ


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **แหล่งข้อมูล**

1. เรียนรู้เพิ่มเติมเกี่ยวกับ llama.cpp [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. เรียนรู้เพิ่มเติมเกี่ยวกับ onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. เรียนรู้เพิ่มเติมเกี่ยวกับ GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญด้านภาษามนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดขึ้นจากการใช้การแปลฉบับนี้