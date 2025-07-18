<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-07-16T21:40:51+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "uk"
}
-->
# **Інференс Phi-3-Vision локально**

Phi-3-vision-128k-instruct дозволяє Phi-3 не лише розуміти мову, а й бачити світ візуально. Завдяки Phi-3-vision-128k-instruct ми можемо розв’язувати різні візуальні задачі, такі як OCR, аналіз таблиць, розпізнавання об’єктів, опис зображень тощо. Ми легко виконуємо завдання, для яких раніше потрібні були великі обсяги даних для навчання. Нижче наведені пов’язані техніки та сценарії застосування, які використовує Phi-3-vision-128k-instruct.

## **0. Підготовка**

Переконайтеся, що перед використанням встановлені наступні бібліотеки Python (рекомендується Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Рекомендується використовувати ***CUDA 11.6+*** та встановити flatten

```bash
pip install flash-attn --no-build-isolation
```

Створіть новий Notebook. Щоб виконати приклади, рекомендується спочатку створити наступний вміст.

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

## **1. Аналіз зображення за допомогою Phi-3-Vision**

Ми хочемо, щоб ШІ міг аналізувати вміст наших зображень і давати відповідні описи

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

Отримати потрібні відповіді можна, виконавши наступний скрипт у Notebook

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR за допомогою Phi-3-Vision**

Окрім аналізу зображення, ми також можемо витягувати інформацію з нього. Це процес OCR, для якого раніше потрібно було писати складний код.

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

Результат

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Порівняння кількох зображень**

Phi-3 Vision підтримує порівняння кількох зображень. Ми можемо використовувати цю модель, щоб знаходити відмінності між зображеннями.

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

Результат

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.