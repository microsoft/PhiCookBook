# **ការប៉ាន់ប្រមាណ Phi-3-Vision នៅលើម៉ាស៊ីនក្នុងស្រុក**

Phi-3-vision-128k-instruct អនុញ្ញាតឱ្យ Phi-3 មិនត្រឹមតែយល់ភាសាទេ ប៉ុន្តែអាចមើលឃើញពិភពដោយរូបភាពផងដែរ។ តាមរយៈ Phi-3-vision-128k-instruct យើងអាចដោះស្រាយបញ្ហាផ្នែករូបភាពផ្សេងៗ ដូចជា OCR, ការវិភាគតារាង, ការទទួលស្គាល់វត្ថុ, ការពណ៌នារូបភាព ល។ យើងអាចបំពេញកិច្ចការ ដែលមុននេះត្រូវការបណ្តុះបណ្តាលទិន្នន័យច្រើន បានយ៉ាងងាយស្រួល។ ខាងក្រោមគឺជាបច្ចេកទេស និងសេណារីយ៉ូកម្មវិធីដែល Phi-3-vision-128k-instruct បានយោង។

## **0. ការរៀបចំ**

សូមប្រាកដថា បានដំឡើងបណ្ណាល័យ Python ខាងក្រោមមុនពេលប្រើ (សូមណែនាំ Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

ណែនាំឱ្យប្រើ ***CUDA 11.6+*** និងដំឡើង flatten

```bash
pip install flash-attn --no-build-isolation
```

បង្កើត Notebook ថ្មី។ ដើម្បីបញ្ចប់ឧទាហរណ៍ទាំងនេះ ណែនាំឱ្យអ្នកបង្កើតខ្លឹមសារខាងក្រោមនេះជាមុន។

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

យើងចង់ឱ្យ AI អាចវិភាគមាតិកានៃរូបភាពរបស់យើង ហើយផ្តល់ការពណ៌នាដែលពាក់ព័ន្ធ

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

យើងអាចទទួលបានចម្លើយដែលពាក់ព័ន្ធដោយរត់ស្គ្រីបខាងក្រោមក្នុង Notebook

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR ជាមួយ Phi-3-Vision**

លើសពីការវិភាគរូបភាព យើងក៏អាចដកស្រង់ព័ត៌មានពីរូបភាពបានផងដែរ។ នេះគឺជា ប្រតិបត្តិការកាត់សរសេរ OCR ដែលមុននេះយើងត្រូវសរសេរកូដស្មុគស្មាញដើម្បីបញ្ចប់។

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

## **3. Comparison of multiple images**

Phi-3 Vision គាំទ្រការប្រៀបធៀបរូបភាពច្រើន។ យើងអាចប្រើម៉ូដែលនេះដើម្បីស្វែងយល់ពីភាពខុសគ្នារវាងរូបភាពទាំងនោះ។

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
**ការមិនទទួលខុសត្រូវ**:
ឯកសារ​នេះ​ត្រូវ​បាន​បកប្រែ​ដោយ​ប្រើ​សេវា​បកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈ​ដែល​យើង​ខំប្រឹង​សម្រាប់​ភាព​ត្រឹមត្រូវ សូម​ចំណាំ​ថា ការ​បកប្រែ​ដោយ​ស្វ័យ​ប្រវត្តិ​អាច​មាន​កំហុស ឬ​មិន​ទាន់​ត្រឹមត្រូវ។ ឯកសារ​ដើម​ក្នុង​ភាសាដើម​គួរ​ត្រូវ​បាន​ទទួល​ស្គាល់​ថា​ជា​ប្រភព​អធិបតេយ្យ។ សម្រាប់​ព័ត៌មាន​សំខាន់ៗ យើងផ្ដល់​អនុសាសន៍​ឲ្យ​ប្រើ​ការ​បកប្រែ​ដោយ​អ្នកជំនាញ​មនុស្ស។ យើង​មិន​ទទួល​ខុស​ត្រូវ​ចំពោះ​ការ​យល់​ខុស ឬ​ការ​បក​អត្ថន័យ​ខុស​ណា​មួយ​ដែល​កើតឡើង​ពី​ការ​ប្រើប្រាស់​ការ​បកប្រែ​នេះ​ទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->