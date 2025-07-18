<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-07-16T21:39:38+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "sw"
}
-->
# **Inference Phi-3-Vision kwa Ndani**

Phi-3-vision-128k-instruct inaruhusu Phi-3 si tu kuelewa lugha, bali pia kuona dunia kwa njia ya kuona. Kupitia Phi-3-vision-128k-instruct, tunaweza kutatua matatizo mbalimbali ya kuona, kama vile OCR, uchambuzi wa meza, utambuzi wa vitu, kueleza picha n.k. Tunaweza kumaliza kazi ambazo awali zilihitaji mafunzo mengi ya data kwa urahisi. Hapa chini ni mbinu na matukio ya matumizi yanayohusiana yanayotajwa na Phi-3-vision-128k-instruct

## **0. Maandalizi**

Tafadhali hakikisha maktaba zifuatazo za Python zimewekwa kabla ya matumizi (Python 3.10+ inapendekezwa)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Inapendekezwa kutumia ***CUDA 11.6+*** na kusakinisha flatten

```bash
pip install flash-attn --no-build-isolation
```

Tengeneza Notebook mpya. Ili kukamilisha mifano, inapendekezwa kwanza kuunda maudhui yafuatayo.

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

## **1. Kuchambua picha kwa Phi-3-Vision**

Tunataka AI iweze kuchambua yaliyomo kwenye picha zetu na kutoa maelezo yanayofaa

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

Tunaweza kupata majibu yanayohusiana kwa kutekeleza script ifuatayo katika Notebook

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR kwa Phi-3-Vision**

Mbali na kuchambua picha, pia tunaweza kutoa taarifa kutoka kwenye picha. Huu ni mchakato wa OCR ambao hapo awali tulihitaji kuandika msimbo mgumu kukamilisha.

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

Matokeo ni

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Ulinganishaji wa picha nyingi**

Phi-3 Vision inaunga mkono ulinganishaji wa picha nyingi. Tunaweza kutumia modeli hii kutambua tofauti kati ya picha hizo.

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

Matokeo ni

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.