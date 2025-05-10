<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-05-09T13:14:25+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "th"
}
-->
# **การใช้งาน Inference Phi-3-Vision ในเครื่อง**

Phi-3-vision-128k-instruct ช่วยให้ Phi-3 ไม่เพียงแต่เข้าใจภาษา แต่ยังสามารถมองเห็นโลกในรูปแบบภาพได้ ผ่าน Phi-3-vision-128k-instruct เราสามารถแก้ไขปัญหาภาพต่างๆ เช่น OCR, การวิเคราะห์ตาราง, การรู้จำวัตถุ, การบรรยายภาพ เป็นต้น เราสามารถทำงานเหล่านี้ได้อย่างง่ายดายโดยไม่ต้องใช้ข้อมูลฝึกสอนจำนวนมาก ดังนี้เป็นเทคนิคและกรณีการใช้งานที่เกี่ยวข้องซึ่งอ้างอิงโดย Phi-3-vision-128k-instruct

## **0. การเตรียมความพร้อม**

โปรดตรวจสอบให้แน่ใจว่าได้ติดตั้งไลบรารี Python ต่อไปนี้ก่อนใช้งาน (แนะนำ Python 3.10 ขึ้นไป)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

แนะนำให้ใช้ ***CUDA 11.6+*** และติดตั้ง flatten

```bash
pip install flash-attn --no-build-isolation
```

สร้าง Notebook ใหม่ เพื่อทำตามตัวอย่าง แนะนำให้สร้างเนื้อหาต่อไปนี้ก่อน

```python
from PIL import Image
import requests
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoProcessor

model_id = "microsoft/Phi-3-vision-128k-instruct"

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, torch_dtype="auto").cuda()

user_prompt = '<|user|>\n'
assistant_prompt = '<|assistant|>\n'
prompt_suffix = "<|end|>\n"
```

## **1. วิเคราะห์ภาพด้วย Phi-3-Vision**

เราต้องการให้ AI สามารถวิเคราะห์เนื้อหาของภาพและให้คำอธิบายที่เกี่ยวข้อง

```python
prompt = f"{user_prompt}<|image_1|>\nCould you please introduce this stock to me?{prompt_suffix}{assistant_prompt}"


url = "https://g.foolcdn.com/editorial/images/767633/nvidiadatacenterrevenuefy2017tofy2024.png"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=True, 
                                  clean_up_tokenization_spaces=False)[0]
```

เราสามารถรับคำตอบที่เกี่ยวข้องได้โดยการรันสคริปต์ต่อไปนี้ใน Notebook

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR ด้วย Phi-3-Vision**

นอกจากการวิเคราะห์ภาพแล้ว เรายังสามารถดึงข้อมูลจากภาพได้อีกด้วย นี่คือกระบวนการ OCR ซึ่งก่อนหน้านี้เราต้องเขียนโค้ดยุ่งยากเพื่อทำให้เสร็จ

```python
prompt = f"{user_prompt}<|image_1|>\nHelp me get the title and author information of this book?{prompt_suffix}{assistant_prompt}"

url = "https://marketplace.canva.com/EAFPHUaBrFc/1/0/1003w/canva-black-and-white-modern-alone-story-book-cover-QHBKwQnsgzs.jpg"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=False, 
                                  clean_up_tokenization_spaces=False)[0]

```

ผลลัพธ์คือ

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. การเปรียบเทียบภาพหลายภาพ**

Phi-3 Vision รองรับการเปรียบเทียบภาพหลายภาพ เราสามารถใช้โมเดลนี้เพื่อค้นหาความแตกต่างระหว่างภาพได้

```python
prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\n What is difference in this two images?{prompt_suffix}{assistant_prompt}"

print(f">>> Prompt\n{prompt}")

url = "https://hinhnen.ibongda.net/upload/wallpaper/doi-bong/2012/11/22/arsenal-wallpaper-free.jpg"

image_1 = Image.open(requests.get(url, stream=True).raw)

url = "https://assets-webp.khelnow.com/d7293de2fa93b29528da214253f1d8d0/news/uploads/2021/07/Arsenal-1024x576.jpg.webp"

image_2 = Image.open(requests.get(url, stream=True).raw)

images = [image_1, image_2]

inputs = processor(prompt, images, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

ผลลัพธ์คือ

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้