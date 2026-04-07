# **ការអនុញ្ញាត Phi-3-Vision ក្នុងតំបន់មូលដ្ឋាន**

Phi-3-vision-128k-instruct អនុញ្ញាតឱ្យ Phi-3 មិនត្រឹមតែយល់ភាសាប៉ុណ្ណោះទេ ប៉ុន្តែក៏អាចមើលឃើញពិភពលោកផងដែរ។ តាមរយៈ Phi-3-vision-128k-instruct អ្នកអាចដោះស្រាយបញ្ហាទស្សន៍ផ្សេងៗ ដូចជាការយល់អក្សរដោយ OCR, វិភាគតារាង, ស្គាល់វត្ថុ, ពិពណ៌នារូបភាព និងផ្សេងទៀត។ យើងអាចបញ្ចប់កិច្ចការដែលពីមុនត្រូវការបណ្តុះបណ្តាលទិន្នន័យច្រើនបានយ៉ាងងាយស្រួល។ ខាងក្រោមជាបច្ចេកទេសពាក់ព័ន្ធ និងស្ថានการณ์កម្មវិធីដែលបានយោងដោយ Phi-3-vision-128k-instruct

## **0. ការរៀបចំ**

សូមប្រាកដថាបណ្ណាល័យ Python ខាងក្រោមត្រូវបានដំឡើងរួចហើយមុនប្រើប្រាស់ (ណែនាំ Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

ណែនាំឲ្យប្រើ ***CUDA 11.6+*** ហើយដំឡើង flatten

```bash
pip install flash-attn --no-build-isolation
```

បង្កើតសៀវភៅកំណត់ត្រាថ្មីមួយ។ ដើម្បីបញ្ចប់ឧទាហរណ៍ យើងណែនាំឲ្យបង្កើតមាតិកាទីនេះជាលំដាប់

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

## **1. វិភាគរូបភាពជាមួយ Phi-3-Vision**

យើងចង់ឲ្យ AI អាចវិភាគមាតិការូបភាពរបស់យើង ហើយផ្តល់ការពិពណ៌នាដែលពាក់ព័ន្ធ

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

យើងអាចទទួលបានចម្លើយដែលពាក់ព័ន្ធដោយអនុវត្តស្គ្រីបខាងក្រោមក្នុងសៀវភៅកំណត់ត្រា

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR ជាមួយ Phi-3-Vision**

ក្រៅតែវិភាគរូបភាព យើងក៏អាចយកព័ត៌មានពីរូបភាពបានផងដែរ។ នេះជាដំណើរការរបស់ OCR ដែលពីមុនយើងត្រូវការសរសេរកូដស្មុគស្មាញដើម្បីបញ្ចប់

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

លទ្ធផលគឺ

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. ការប្រៀបធៀបរូបភាពច្រើន**

Phi-3 Vision គាំទ្រការប្រៀបធៀបរូបភាពច្រើន។ យើងអាចប្រើម៉ូដែលនេះដើម្បីស្វែងរកភាពខុសគ្នារវាងរូបភាព

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

លទ្ធផលគឺ

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបញ្ចូនបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំព្យាយាមរក្សាគុណភាពនៃការបកប្រែឲ្យមានភាពត្រឹមត្រូវ ក៏សូមស្វែងយល់ថាការបកប្រែដោយស្វ័យប្រវ័ត្រ​អាចមានកំហុសឬការខ្វះត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាមាតុភូមិគួរត្រូវបានគេចាត់ទុកថាជា ប្រភពផ្លូវការតែមួយ។ សម្រាប់ព័ត៌មានសំខាន់ៗ, ការបកប្រែដោយមនុស្សជំនាញគឺត្រូវបានផ្ដល់អាទិភាព។ យើងខ្ញុំមិនមានកិច្ចបន្ទុកចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសដល់ខុសដោយការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->