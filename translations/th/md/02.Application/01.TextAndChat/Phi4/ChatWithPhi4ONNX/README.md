# **แชทกับ Phi-4-mini ONNX**

***ONNX*** คือรูปแบบเปิดที่สร้างขึ้นเพื่อแทนโมเดลการเรียนรู้ของเครื่อง ONNX กำหนดชุดของตัวดำเนินการทั่วไป - ซึ่งเป็นส่วนประกอบหลักของโมเดลการเรียนรู้ของเครื่องและการเรียนรู้เชิงลึก - และรูปแบบไฟล์ทั่วไปเพื่อช่วยให้นักพัฒนา AI สามารถใช้โมเดลกับเฟรมเวิร์ก เครื่องมือ รันไทม์ และคอมไพเลอร์ต่างๆ ได้

เราหวังที่จะนำโมเดล AI สร้างสรรค์ไปใช้งานบนอุปกรณ์ edge และใช้งานในสภาพแวดล้อมที่มีพลังการประมวลผลจำกัดหรือออฟไลน์ ตอนนี้เราสามารถบรรลุเป้าหมายนี้ได้โดยการแปลงโมเดลในรูปแบบที่มีการควอนไทซ์ เราสามารถแปลงโมเดลที่ควอนไทซ์แล้วเป็นรูปแบบ GGUF หรือ ONNX

Microsoft Olive สามารถช่วยคุณแปลง SLM เป็นรูปแบบ ONNX ที่ควอนไทซ์ วิธีการแปลงโมเดลง่ายมาก

**ติดตั้ง Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**แปลง ONNX สำหรับ CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***หมายเหตุ*** ตัวอย่างนี้ใช้ CPU


### **การทำ Inference โมเดล Phi-4-mini ONNX ด้วย ONNX Runtime GenAI**

- **ติดตั้ง ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **โค้ด Python**

*นี่คือเวอร์ชัน ONNX Runtime GenAI 0.5.2*

```python

import onnxruntime_genai as og
import numpy as np
import os


model_folder = "Your Phi-4-mini-onnx-cpu-int4 location"


model = og.Model(model_folder)


tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()


search_options = {}
search_options['max_length'] = 2048
search_options['past_present_share_buffer'] = False


chat_template = "<|user|>\n{input}</s>\n<|assistant|>"


text = """Can you introduce yourself"""


prompt = f'{chat_template.format(input=text)}'


input_tokens = tokenizer.encode(prompt)


params = og.GeneratorParams(model)


params.set_search_options(**search_options)
params.input_ids = input_tokens


generator = og.Generator(model, params)


while not generator.is_done():
      generator.compute_logits()
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      print(tokenizer_stream.decode(new_token), end='', flush=True)

```


*นี่คือเวอร์ชัน ONNX Runtime GenAI 0.6.0*

```python

import onnxruntime_genai as og
import numpy as np
import os
import time
import psutil

model_folder = "Your Phi-4-mini-onnx model path"

model = og.Model(model_folder)

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

search_options = {}
search_options['max_length'] = 1024
search_options['past_present_share_buffer'] = False

chat_template = "<|user|>{input}<|assistant|>"

text = """can you introduce yourself"""

prompt = f'{chat_template.format(input=text)}'

input_tokens = tokenizer.encode(prompt)

params = og.GeneratorParams(model)

params.set_search_options(**search_options)

generator = og.Generator(model, params)

generator.append_tokens(input_tokens)

while not generator.is_done():
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      token_text = tokenizer.decode(new_token)
      # print(tokenizer_stream.decode(new_token), end='', flush=True)
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้