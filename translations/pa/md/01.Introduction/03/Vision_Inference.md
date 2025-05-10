<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-05-09T13:12:33+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "pa"
}
-->
# **ਲੋਕਲ ਵਿੱਚ Inference Phi-3-Vision**

Phi-3-vision-128k-instruct Phi-3 ਨੂੰ ਸਿਰਫ਼ ਭਾਸ਼ਾ ਸਮਝਣ ਹੀ ਨਹੀਂ ਦਿੰਦਾ, ਸਗੋਂ ਦੁਨੀਆ ਨੂੰ ਵਿਜ਼ੂਅਲੀ ਤੌਰ 'ਤੇ ਵੀ ਦੇਖਣ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। Phi-3-vision-128k-instruct ਰਾਹੀਂ, ਅਸੀਂ ਵੱਖ-ਵੱਖ ਵਿਜ਼ੂਅਲ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਹੱਲ ਕਰ ਸਕਦੇ ਹਾਂ, ਜਿਵੇਂ ਕਿ OCR, ਟੇਬਲ ਵਿਸ਼ਲੇਸ਼ਣ, ਵਸਤੂ ਪਹਿਚਾਣ, ਤਸਵੀਰ ਦਾ ਵਰਣਨ ਆਦਿ। ਅਸੀਂ ਆਸਾਨੀ ਨਾਲ ਉਹ ਕੰਮ ਕਰ ਸਕਦੇ ਹਾਂ ਜੋ ਪਹਿਲਾਂ ਬਹੁਤ ਸਾਰੇ ਡਾਟਾ ਟ੍ਰੇਨਿੰਗ ਦੀ ਲੋੜ ਹੁੰਦੇ ਸਨ। ਹੇਠਾਂ Phi-3-vision-128k-instruct ਵੱਲੋਂ ਦਰਸਾਏ ਗਏ ਸੰਬੰਧਿਤ ਤਕਨੀਕਾਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਸਥਿਤੀਆਂ ਦਿੱਤੀਆਂ ਗਈਆਂ ਹਨ।

## **0. ਤਿਆਰੀ**

ਕਿਰਪਾ ਕਰਕੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੀਆਂ Python ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਸਟਾਲ ਹੋ ਚੁਕੀਆਂ ਹਨ (Python 3.10+ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ਵਰਤਣ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ flatten ਇੰਸਟਾਲ ਕਰੋ

```bash
pip install flash-attn --no-build-isolation
```

ਇੱਕ ਨਵਾਂ Notebook ਬਣਾਓ। ਉਦਾਹਰਣਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ, ਪਹਿਲਾਂ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਬਣਾਉਣਾ ਸਿਫਾਰਸ਼ੀ ਹੈ।

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

## **1. Phi-3-Vision ਨਾਲ ਤਸਵੀਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ**

ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ AI ਸਾਡੇ ਚਿੱਤਰਾਂ ਦੀ ਸਮੱਗਰੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਸੰਬੰਧਿਤ ਵਰਣਨ ਦੇ ਸਕੇ

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

ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤਾ ਸਕ੍ਰਿਪਟ Notebook ਵਿੱਚ ਚਲਾਕੇ ਸੰਬੰਧਿਤ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision ਨਾਲ OCR**

ਤਸਵੀਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਦੇ ਨਾਲ-ਨਾਲ, ਅਸੀਂ ਤਸਵੀਰ ਵਿੱਚੋਂ ਜਾਣਕਾਰੀ ਵੀ ਕੱਢ ਸਕਦੇ ਹਾਂ। ਇਹ ਉਹ OCR ਪ੍ਰਕਿਰਿਆ ਹੈ ਜੋ ਪਹਿਲਾਂ ਸਾਡੇ ਲਈ ਮੁਸ਼ਕਲ ਕੋਡ ਲਿਖਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਸੀ।

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

ਨਤੀਜਾ ਹੈ

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. ਕਈ ਤਸਵੀਰਾਂ ਦੀ ਤੁਲਨਾ**

Phi-3 Vision ਕਈ ਤਸਵੀਰਾਂ ਦੀ ਤੁਲਨਾ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਅਸੀਂ ਇਸ ਮਾਡਲ ਨੂੰ ਵਰਤ ਕੇ ਤਸਵੀਰਾਂ ਵਿੱਚ ਫਰਕ ਲੱਭ ਸਕਦੇ ਹਾਂ।

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

ਨਤੀਜਾ ਹੈ

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਤੀਰਤਾ ਹੋ ਸਕਦੀ ਹੈ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।