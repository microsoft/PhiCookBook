<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-05-09T15:55:03+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "th"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

โค้ดนี้จะส่งออกโมเดลเป็นรูปแบบ OpenVINO, โหลดโมเดล และใช้โมเดลในการสร้างคำตอบสำหรับ prompt ที่กำหนด

1. **การส่งออกโมเดล**:  
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```  
   - คำสั่งนี้ใช้ `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`

2. **การนำเข้าห้องสมุดที่จำเป็น**:  
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```  
   - บรรทัดเหล่านี้นำเข้าคลาสจากโมดูล `transformers` library and the `optimum.intel.openvino` ซึ่งจำเป็นสำหรับการโหลดและใช้งานโมเดล

3. **การตั้งค่าไดเรกทอรีโมเดลและการกำหนดค่า**:  
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```  
   - `model_dir` specifies where the model files are stored.
   - `ov_config` เป็นดิกชันนารีที่ตั้งค่าโมเดล OpenVINO ให้เน้นความหน่วงต่ำ, ใช้สตรีม inference เพียงหนึ่ง และไม่ใช้ไดเรกทอรีแคช

4. **การโหลดโมเดล**:  
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```  
   - บรรทัดนี้โหลดโมเดลจากไดเรกทอรีที่กำหนด โดยใช้การตั้งค่าที่กำหนดไว้ก่อนหน้า และอนุญาตให้รันโค้ดจากระยะไกลถ้าจำเป็น

5. **การโหลด Tokenizer**:  
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```  
   - บรรทัดนี้โหลด tokenizer ซึ่งมีหน้าที่แปลงข้อความเป็นโทเค็นที่โมเดลเข้าใจได้

6. **การตั้งค่าอาร์กิวเมนต์ของ Tokenizer**:  
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```  
   - ดิกชันนารีนี้ระบุว่าจะไม่เพิ่มโทเค็นพิเศษลงในผลลัพธ์ที่ถูก tokenize

7. **การกำหนด Prompt**:  
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```  
   - สตริงนี้ตั้งค่า prompt สำหรับการสนทนา โดยที่ผู้ใช้ขอให้ AI assistant แนะนำตัวเอง

8. **การแปลง Prompt เป็นโทเค็น**:  
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```  
   - บรรทัดนี้แปลง prompt เป็นโทเค็นที่โมเดลสามารถประมวลผลได้ โดยส่งคืนผลลัพธ์ในรูปแบบ PyTorch tensors

9. **การสร้างคำตอบ**:  
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```  
   - บรรทัดนี้ใช้โมเดลสร้างคำตอบจากโทเค็นอินพุต โดยกำหนดจำนวนโทเค็นใหม่สูงสุดที่ 1024

10. **การถอดรหัสคำตอบ**:  
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```  
    - บรรทัดนี้แปลงโทเค็นที่สร้างกลับเป็นข้อความที่อ่านได้ โดยข้ามโทเค็นพิเศษ และดึงผลลัพธ์ตัวแรกออกมา

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่น่าเชื่อถือ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดใด ๆ ที่เกิดจากการใช้การแปลนี้