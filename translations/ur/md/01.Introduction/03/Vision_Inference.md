<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "110bee6270dad2ebf506d90a30b46dde",
  "translation_date": "2025-05-07T14:38:11+00:00",
  "source_file": "md/01.Introduction/03/Vision_Inference.md",
  "language_code": "ur"
}
-->
# **مقامی سطح پر Inference Phi-3-Vision**

Phi-3-vision-128k-instruct نہ صرف زبان کو سمجھنے کی صلاحیت دیتا ہے بلکہ دنیا کو بصری طور پر دیکھنے کی بھی اجازت دیتا ہے۔ Phi-3-vision-128k-instruct کے ذریعے ہم مختلف بصری مسائل حل کر سکتے ہیں، جیسے OCR، جدول کا تجزیہ، اشیاء کی شناخت، تصویر کی وضاحت وغیرہ۔ ہم آسانی سے ایسے کام مکمل کر سکتے ہیں جن کے لیے پہلے بہت زیادہ ڈیٹا کی تربیت کی ضرورت ہوتی تھی۔ ذیل میں Phi-3-vision-128k-instruct کے حوالے سے متعلقہ تکنیکیں اور اطلاقی منظرنامے دیے گئے ہیں۔

## **0. تیاری**

براہ کرم استعمال سے پہلے درج ذیل Python لائبریریاں انسٹال ہونے کی تصدیق کریں (Python 3.10+ کی سفارش کی جاتی ہے)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

تجویز کی جاتی ہے کہ ***CUDA 11.6+*** استعمال کریں اور flatten انسٹال کریں

```bash
pip install flash-attn --no-build-isolation
```

نیا Notebook بنائیں۔ مثالیں مکمل کرنے کے لیے، سفارش کی جاتی ہے کہ آپ پہلے درج ذیل مواد تیار کریں۔

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

## **1. Phi-3-Vision کے ساتھ تصویر کا تجزیہ**

ہم چاہتے ہیں کہ AI ہماری تصاویر کے مواد کا تجزیہ کر سکے اور متعلقہ وضاحتیں فراہم کرے

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

ہم Notebook میں درج ذیل اسکرپٹ چلانے سے متعلقہ جوابات حاصل کر سکتے ہیں

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision کے ساتھ OCR**

تصویر کا تجزیہ کرنے کے علاوہ، ہم تصویر سے معلومات بھی نکال سکتے ہیں۔ یہ وہ OCR عمل ہے جس کے لیے ہمیں پہلے پیچیدہ کوڈ لکھنا پڑتا تھا۔

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

نتیجہ یہ ہے

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. متعدد تصاویر کا موازنہ**

Phi-3 Vision متعدد تصاویر کے موازنہ کی حمایت کرتا ہے۔ ہم اس ماڈل کا استعمال تصاویر کے درمیان فرق تلاش کرنے کے لیے کر سکتے ہیں۔

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

نتیجہ یہ ہے

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**دستخطی**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔