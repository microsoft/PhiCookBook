<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-05-09T19:49:27+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "bn"
}
-->
## **Phi-4-mini-mm ব্যবহার করে কোড তৈরি করা**

Phi-4-mini Phi পরিবারে শক্তিশালী কোডিং ক্ষমতা বজায় রাখে। আপনি Prompt ব্যবহার করে কোডিং সম্পর্কিত প্রশ্ন করতে পারেন। অবশ্যই, শক্তিশালী যুক্তি যোগ করার পর এর কোডিং ক্ষমতা আরও বাড়িয়েছে, যেমন প্রয়োজন অনুসারে প্রকল্প তৈরি করা। উদাহরণস্বরূপ, প্রয়োজন অনুসারে প্রকল্প তৈরি করা, যেমন:

### **প্রয়োজনীয়তা**

একটি শপিং কার্ট অ্যাপ তৈরি করুন

- নিম্নলিখিত মেথড সহ একটি API Rest তৈরি করুন:
    - পেজ অফসেট এবং লিমিট ব্যবহার করে বিয়ারের তালিকা পান।
    - আইডি দ্বারা বিয়ারের বিস্তারিত পান।
    - নাম, বিবরণ, ট্যাগলাইন, খাবারের জোড়া এবং মূল্যের মাধ্যমে বিয়ার অনুসন্ধান করুন।
- মেইন পেজে পণ্যের একটি তালিকা তৈরি করুন।
    - পণ্য ফিল্টার করার জন্য একটি সার্চ বার তৈরি করুন।
    - ব্যবহারকারী পণ্যের উপর ক্লিক করলে বিবরণ পৃষ্ঠায় নেভিগেট করুন।
- (ঐচ্ছিক) মূল্য অনুযায়ী পণ্য ফিল্টার করার জন্য স্লাইসার।
- একটি শপিং কার্ট তৈরি করুন।
    - কার্টে পণ্য যোগ করুন।
    - কার্ট থেকে পণ্য সরান।
    - কার্টে থাকা পণ্যের মোট মূল্য হিসাব করুন।

### **নমুনা কোড - পাইথন**


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

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে জানুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নয়।