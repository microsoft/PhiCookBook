<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aacf82e3da702afd8469bba99b662509",
  "translation_date": "2025-04-04T12:58:53+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi4\\GenProjectCode\\README.md",
  "language_code": "mo"
}
-->
## **Phi-4-mini-mm ke saath code generate karna**

Phi-4-mini Phi Family ki mazboot coding kshamataon ko jari rakhta hai. Aap Prompt ka upyog karke coding se jude prashn pooch sakte hain. Swabhavik roop se, mazboot tarkshakti jodne ke baad, ismein aur bhi adhik shaktishali coding kshamataein hain, jaise ki aavashyaktaon ke anusar projects generate karna. Udaharan ke liye, aavashyaktaon ke anusar projects generate karna, jaise:

### **Aavashyakta**

Ek Shopping Cart App banaiye

- Ek API Rest banaiye jismein nimnlikhit methods ho:
    - Page offset aur limit ka upyog karke beers ki list prapt karein.
    - Id ke madhyam se beer ke details prapt karein.
    - Naam, varnana, tagline, food pairings, aur price ke aadhar par beer khojein.
- Main page par products ki ek list banaiye.
    - Products ko filter karne ke liye ek search bar banaiye.
    - Jab user kisi product par click kare, to description page par navigate karein.
- (Vikalp) Price ke aadhar par products ko filter karne ke liye ek slicer banaiye.
- Ek shopping cart banaiye.
    - Products ko cart mein add karein.
    - Cart se products ko remove karein.
    - Cart mein products ki total price calculate karein.

### **Udaharan Code - Python**

```python

import requests
import torch
from PIL import Image
import soundfile
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = 'Your Phi-4-mini-mm-instruct'

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype='auto',
    _attn_implementation='flash_attention_2',
).cuda()

generation_config = GenerationConfig.from_pretrained(model_path, 'generation_config.json')

user_prompt = '<|user|>'
assistant_prompt = '<|assistant|>'
prompt_suffix = '<|end|>'

requirement = """

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - Get a list of beers using page offset and limit.
    - Get beer details by id.
    - Search for beer by name, description, tagline, food pairings, and price.
- Create a list of products on the main page.
    - Create a search bar to filter products.
    - Navigate to the description page when the user clicks on a product.
- (Optional) Slicer to filter products by price.
- Create a shopping cart.
    - Add products to the cart.
    - Remove products from the cart.
    - Calculate the total price of the products in the cart."""

note = """ 

            Note:

            1. Use Python Flask to create a Repository pattern based on the following structure to generate the files

            ｜- models
            ｜- controllers
            ｜- repositories
            ｜- views

            2. For the view page, please use SPA + VueJS + TypeScript to build

            3. Firstly use markdown to output the generated project structure (including directories and files), and then generate the  file names and corresponding codes step by step, output like this 

               ## Project Structure

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## Backend
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## Frontend
                 
                   #### `templates/index.html`
                   ```html

                   ```
                   ......."""

prompt = f'{user_prompt}Please create a project with Python and Flask according to the following requirements：\n{requirement}{note}{prompt_suffix}{assistant_prompt}'

inputs = processor(prompt, images=None, return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=2048,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)

```

It seems you are requesting a translation into "mo." Could you clarify what "mo" refers to? Are you referring to a specific language or dialect?