# **ਲੋਕਲ ਵਿੱਚ Inference Phi-3-Vision**

Phi-3-vision-128k-instruct Phi-3 ਨੂੰ ਸਿਰਫ਼ ਭਾਸ਼ਾ ਸਮਝਣ ਹੀ ਨਹੀਂ ਦਿੰਦਾ, ਸਗੋਂ ਦੁਨੀਆ ਨੂੰ ਵਿਜ਼ੂਅਲ ਤੌਰ 'ਤੇ ਵੇਖਣ ਦੀ ਸਮਰੱਥਾ ਵੀ ਦਿੰਦਾ ਹੈ। Phi-3-vision-128k-instruct ਰਾਹੀਂ ਅਸੀਂ ਵੱਖ-ਵੱਖ ਵਿਜ਼ੂਅਲ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਹੱਲ ਕਰ ਸਕਦੇ ਹਾਂ, ਜਿਵੇਂ ਕਿ OCR, ਟੇਬਲ ਵਿਸ਼ਲੇਸ਼ਣ, ਵਸਤੂ ਪਛਾਣ, ਤਸਵੀਰ ਦਾ ਵਰਣਨ ਆਦਿ। ਅਸੀਂ ਆਸਾਨੀ ਨਾਲ ਉਹ ਕੰਮ ਕਰ ਸਕਦੇ ਹਾਂ ਜਿਨ੍ਹਾਂ ਲਈ ਪਹਿਲਾਂ ਬਹੁਤ ਸਾਰੇ ਡਾਟਾ ਟ੍ਰੇਨਿੰਗ ਦੀ ਲੋੜ ਹੁੰਦੀ ਸੀ। ਹੇਠਾਂ Phi-3-vision-128k-instruct ਵੱਲੋਂ ਦਿੱਤੀਆਂ ਗਈਆਂ ਸੰਬੰਧਿਤ ਤਕਨੀਕਾਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਸਥਿਤੀਆਂ ਹਨ।

## **0. ਤਿਆਰੀ**

ਕਿਰਪਾ ਕਰਕੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੀਆਂ Python ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਹੋ ਚੁੱਕੀਆਂ ਹਨ (Python 3.10+ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ਵਰਤਣ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ flatten ਇੰਸਟਾਲ ਕਰੋ

```bash
pip install flash-attn --no-build-isolation
```

ਨਵਾਂ Notebook ਬਣਾਓ। ਉਦਾਹਰਣਾਂ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ, ਪਹਿਲਾਂ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਬਣਾਉਣਾ ਸਿਫਾਰਸ਼ੀ ਹੈ।

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

ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ AI ਸਾਡੇ ਤਸਵੀਰਾਂ ਦੇ ਸਮੱਗਰੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਸੰਬੰਧਿਤ ਵਰਣਨ ਦੇ ਸਕੇ

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

ਅਸੀਂ Notebook ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਕ੍ਰਿਪਟ ਚਲਾਕੇ ਸੰਬੰਧਿਤ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision ਨਾਲ OCR**

ਤਸਵੀਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਦੇ ਇਲਾਵਾ, ਅਸੀਂ ਤਸਵੀਰ ਵਿੱਚੋਂ ਜਾਣਕਾਰੀ ਵੀ ਕੱਢ ਸਕਦੇ ਹਾਂ। ਇਹ OCR ਪ੍ਰਕਿਰਿਆ ਹੈ ਜਿਸ ਲਈ ਪਹਿਲਾਂ ਸਾਨੂੰ ਜਟਿਲ ਕੋਡ ਲਿਖਣਾ ਪੈਂਦਾ ਸੀ।

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

Phi-3 Vision ਕਈ ਤਸਵੀਰਾਂ ਦੀ ਤੁਲਨਾ ਕਰਨ ਦਾ ਸਮਰੱਥ ਹੈ। ਅਸੀਂ ਇਸ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਵਿੱਚ ਫਰਕ ਲੱਭ ਸਕਦੇ ਹਾਂ।

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

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।