<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-03-27T08:15:43+00:00",
  "source_file": "md\\01.Introduction\\03\\Vision_Inference.md",
  "language_code": "fa"
}
-->
# **استفاده از Phi-3-Vision به صورت محلی**

Phi-3-vision-128k-instruct به Phi-3 این امکان را می‌دهد که نه تنها زبان را بفهمد، بلکه بتواند جهان را به صورت بصری نیز مشاهده کند. با استفاده از Phi-3-vision-128k-instruct، می‌توانیم مسائل بصری مختلفی مانند تشخیص متن (OCR)، تحلیل جداول، شناسایی اشیا، توصیف تصاویر و غیره را حل کنیم. این ابزار به ما کمک می‌کند وظایفی را که پیش‌تر نیاز به آموزش داده‌های زیادی داشتند، به سادگی انجام دهیم. در ادامه، تکنیک‌ها و سناریوهای کاربردی مرتبط با Phi-3-vision-128k-instruct آورده شده است.

## **0. آماده‌سازی**

لطفاً اطمینان حاصل کنید که کتابخانه‌های زیر در Python نصب شده‌اند (پیشنهاد می‌شود از Python 3.10+ استفاده کنید)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

توصیه می‌شود از ***CUDA 11.6+*** استفاده کنید و flatten را نصب کنید

```bash
pip install flash-attn --no-build-isolation
```

یک Notebook جدید ایجاد کنید. برای تکمیل مثال‌ها، پیشنهاد می‌شود ابتدا محتوای زیر را ایجاد کنید.

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

## **1. تحلیل تصویر با Phi-3-Vision**

ما می‌خواهیم که هوش مصنوعی بتواند محتوای تصاویر ما را تحلیل کرده و توضیحات مرتبط ارائه دهد.

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

می‌توانیم با اجرای اسکریپت زیر در Notebook پاسخ‌های مرتبط را دریافت کنیم.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. انجام OCR با Phi-3-Vision**

علاوه بر تحلیل تصاویر، می‌توانیم اطلاعات را نیز از تصاویر استخراج کنیم. این فرآیند OCR است که پیش‌تر نیاز به نوشتن کدهای پیچیده داشت.

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

نتیجه به صورت زیر است:

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. مقایسه چند تصویر**

Phi-3 Vision از مقایسه چند تصویر پشتیبانی می‌کند. می‌توانیم از این مدل برای یافتن تفاوت‌های بین تصاویر استفاده کنیم.

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

نتیجه به صورت زیر است:

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که تلاش می‌کنیم دقت را رعایت کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما هیچ مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.