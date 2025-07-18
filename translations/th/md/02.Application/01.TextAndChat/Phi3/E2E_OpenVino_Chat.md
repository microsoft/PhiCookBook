<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a54312eea82ac654fb0f6d39b1f772",
  "translation_date": "2025-07-16T23:04:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md",
  "language_code": "th"
}
-->
[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

โค้ดนี้จะส่งออกโมเดลเป็นรูปแบบ OpenVINO, โหลดโมเดล และใช้โมเดลในการสร้างคำตอบสำหรับข้อความที่กำหนด

1. **การส่งออกโมเดล**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - คำสั่งนี้ใช้เครื่องมือ `optimum-cli` เพื่อส่งออกโมเดลเป็นรูปแบบ OpenVINO ซึ่งถูกปรับแต่งให้เหมาะกับการประมวลผลที่มีประสิทธิภาพ
   - โมเดลที่ถูกส่งออกคือ `"microsoft/Phi-3-mini-4k-instruct"` ซึ่งถูกตั้งค่าให้ทำงานในงานสร้างข้อความตามบริบทที่ผ่านมา
   - น้ำหนักของโมเดลถูกทำให้เป็นแบบ 4 บิต (`int4`) เพื่อช่วยลดขนาดโมเดลและเร่งความเร็วในการประมวลผล
   - พารามิเตอร์อื่นๆ เช่น `group-size`, `ratio` และ `sym` ถูกใช้เพื่อปรับแต่งกระบวนการควอนไทซ์
   - โมเดลที่ส่งออกจะถูกบันทึกไว้ในไดเรกทอรี `./model/phi3-instruct/int4`

2. **การนำเข้าห้องสมุดที่จำเป็น**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - บรรทัดเหล่านี้นำเข้าคลาสจากไลบรารี `transformers` และโมดูล `optimum.intel.openvino` ซึ่งจำเป็นสำหรับการโหลดและใช้งานโมเดล

3. **การตั้งค่าไดเรกทอรีและการกำหนดค่าโมเดล**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` ระบุที่เก็บไฟล์โมเดล
   - `ov_config` เป็นพจนานุกรมที่ตั้งค่าโมเดล OpenVINO ให้เน้นความหน่วงต่ำ ใช้สตรีมการอนุมานเพียงหนึ่ง และไม่ใช้ไดเรกทอรีแคช

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
   - บรรทัดนี้โหลดโมเดลจากไดเรกทอรีที่ระบุ โดยใช้การตั้งค่าที่กำหนดไว้ก่อนหน้า และอนุญาตให้รันโค้ดระยะไกลได้หากจำเป็น

5. **การโหลด Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - บรรทัดนี้โหลด tokenizer ซึ่งมีหน้าที่แปลงข้อความเป็นโทเค็นที่โมเดลสามารถเข้าใจได้

6. **การตั้งค่าอาร์กิวเมนต์ของ Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - พจนานุกรมนี้ระบุว่าไม่ควรเพิ่มโทเค็นพิเศษลงในผลลัพธ์ที่ถูกโทเค็น

7. **การกำหนด Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - สตริงนี้ตั้งค่าข้อความสนทนาโดยที่ผู้ใช้ขอให้ผู้ช่วย AI แนะนำตัวเอง

8. **การโทเค็นข้อความ Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - บรรทัดนี้แปลงข้อความ prompt เป็นโทเค็นที่โมเดลสามารถประมวลผลได้ โดยส่งคืนผลลัพธ์ในรูปแบบ PyTorch tensors

9. **การสร้างคำตอบ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - บรรทัดนี้ใช้โมเดลในการสร้างคำตอบจากโทเค็นอินพุต โดยจำกัดจำนวนโทเค็นใหม่สูงสุดที่ 1024

10. **การถอดรหัสคำตอบ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - บรรทัดนี้แปลงโทเค็นที่สร้างขึ้นกลับเป็นข้อความที่อ่านได้สำหรับมนุษย์ โดยข้ามโทเค็นพิเศษ และดึงผลลัพธ์แรกออกมาใช้

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้