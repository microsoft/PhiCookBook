<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-07-17T04:45:36+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "th"
}
-->
## **การใช้ Phi-4-mini-mm ในการสร้างโค้ด**

Phi-4-mini สานต่อความสามารถในการเขียนโค้ดที่แข็งแกร่งของ Phi Family คุณสามารถใช้ Prompt เพื่อถามคำถามที่เกี่ยวข้องกับการเขียนโค้ด แน่นอนว่าหลังจากเพิ่มความสามารถในการวิเคราะห์ที่แข็งแกร่งแล้ว มันก็มีความสามารถในการเขียนโค้ดที่ดียิ่งขึ้น เช่น การสร้างโปรเจกต์ตามความต้องการ ตัวอย่างเช่น การสร้างโปรเจกต์ตามความต้องการ ดังนี้

### **ความต้องการ**

สร้างแอปตะกร้าสินค้า

- สร้าง API Rest ด้วยเมธอดดังต่อไปนี้:
    - ดึงรายการเบียร์โดยใช้ page offset และ limit
    - ดึงรายละเอียดเบียร์ตาม id
    - ค้นหาเบียร์โดยใช้ชื่อ คำอธิบาย คำโปรย คู่กับอาหาร และราคา
- สร้างรายการสินค้าบนหน้าหลัก
    - สร้างแถบค้นหาเพื่อกรองสินค้า
    - นำทางไปยังหน้าคำอธิบายเมื่อผู้ใช้คลิกที่สินค้า
- (ไม่บังคับ) ตัวกรองเพื่อกรองสินค้าตามราคา
- สร้างตะกร้าสินค้า
    - เพิ่มสินค้าในตะกร้า
    - ลบสินค้าออกจากตะกร้า
    - คำนวณราคารวมของสินค้าที่อยู่ในตะกร้า

### **ตัวอย่างโค้ด - Python**


```python

import requests
import torch
from PIL import Image
import soundfile
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = 'Your Phi-4-mini-mm-instruct'

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype='auto',
    _attn_implementation='flash_attention_2',
).cuda()

generation_config = GenerationConfig.from_pretrained(model_path, 'generation_config.json')

user_prompt = '<|user|>'
assistant_prompt = '<|assistant|>'
prompt_suffix = '<|end|>'

requirement = """

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - Get a list of beers using page offset and limit.
    - Get beer details by id.
    - Search for beer by name, description, tagline, food pairings, and price.
- Create a list of products on the main page.
    - Create a search bar to filter products.
    - Navigate to the description page when the user clicks on a product.
- (Optional) Slicer to filter products by price.
- Create a shopping cart.
    - Add products to the cart.
    - Remove products from the cart.
    - Calculate the total price of the products in the cart."""

note = """ 

            Note:

            1. Use Python Flask to create a Repository pattern based on the following structure to generate the files

            ｜- models
            ｜- controllers
            ｜- repositories
            ｜- views

            2. For the view page, please use SPA + VueJS + TypeScript to build

            3. Firstly use markdown to output the generated project structure (including directories and files), and then generate the  file names and corresponding codes step by step, output like this 

               ## Project Structure

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## Backend
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## Frontend
                 
                   #### `templates/index.html`
                   ```html

                   ```
                   ......."""

prompt = f'{user_prompt}Please create a project with Python and Flask according to the following requirements：\n{requirement}{note}{prompt_suffix}{assistant_prompt}'

inputs = processor(prompt, images=None, return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=2048,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)

```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้