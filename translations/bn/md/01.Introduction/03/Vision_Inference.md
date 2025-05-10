<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-05-09T13:11:37+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "bn"
}
-->
# **স্থানীয়ভাবে Phi-3-Vision এর ইনফারেন্স**

Phi-3-vision-128k-instruct Phi-3 কে কেবল ভাষা বুঝতে সাহায্য করে না, বরং ভিজ্যুয়ালি বিশ্বকে দেখতে সক্ষম করে। Phi-3-vision-128k-instruct এর মাধ্যমে আমরা বিভিন্ন ভিজ্যুয়াল সমস্যা যেমন OCR, টেবিল বিশ্লেষণ, অবজেক্ট শনাক্তকরণ, ছবি বর্ণনা ইত্যাদি সমাধান করতে পারি। পূর্বে যেসব কাজের জন্য প্রচুর ডেটা ট্রেনিং দরকার ছিল, সেগুলো এখন সহজেই সম্পন্ন করা যায়। নিচে Phi-3-vision-128k-instruct দ্বারা উল্লেখিত সম্পর্কিত প্রযুক্তি এবং অ্যাপ্লিকেশন সিচুয়েশনগুলি দেওয়া হলো।

## **0. প্রস্তুতি**

ব্যবহারের আগে দয়া করে নিশ্চিত করুন যে নিম্নলিখিত Python লাইব্রেরিগুলো ইনস্টল করা হয়েছে (Python 3.10+ ব্যবহার করার পরামর্শ দেওয়া হয়)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ব্যবহার করার এবং flatten ইনস্টল করার পরামর্শ দেওয়া হয়

```bash
pip install flash-attn --no-build-isolation
```

একটি নতুন Notebook তৈরি করুন। উদাহরণগুলো সম্পূর্ণ করতে, প্রথমে নিচের বিষয়বস্তু তৈরি করা ভালো।

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

## **1. Phi-3-Vision দিয়ে ছবি বিশ্লেষণ**

আমরা চাই AI আমাদের ছবির বিষয়বস্তু বিশ্লেষণ করতে পারে এবং প্রাসঙ্গিক বর্ণনা দিতে পারে

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

Notebook এ নিচের স্ক্রিপ্টটি চালিয়ে আমরা প্রাসঙ্গিক উত্তর পেতে পারি

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision দিয়ে OCR**

ছবি বিশ্লেষণের পাশাপাশি, আমরা ছবির থেকে তথ্যও বের করতে পারি। এটি হল OCR প্রক্রিয়া, যা আগে জটিল কোড লিখে সম্পন্ন করতে হতো।

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

ফলাফল হল

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. একাধিক ছবির তুলনা**

Phi-3 Vision একাধিক ছবির তুলনাকে সমর্থন করে। আমরা এই মডেলটি ব্যবহার করে ছবিগুলোর মধ্যে পার্থক্য খুঁজে পেতে পারি।

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

ফলাফল হল

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।