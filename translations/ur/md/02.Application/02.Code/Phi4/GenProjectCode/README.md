<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-05-07T13:45:17+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "ur"
}
-->
## **استعمال Phi-4-mini-mm برائے کوڈ جنریشن**

Phi-4-mini، Phi فیملی کی مضبوط کوڈنگ صلاحیتوں کو جاری رکھتا ہے۔ آپ Prompt کا استعمال کر کے کوڈنگ سے متعلق سوالات پوچھ سکتے ہیں۔ ظاہر ہے، مضبوط استدلال کی صلاحیت شامل کرنے کے بعد، اس کی کوڈنگ صلاحیتیں مزید بہتر ہو گئی ہیں، جیسے کہ ضروریات کے مطابق پروجیکٹس بنانا۔ مثال کے طور پر، ضروریات کے مطابق پروجیکٹس بنائیں، جیسے:

### **ضرورت**

Shopping Cart App بنائیں

- درج ذیل طریقوں کے ساتھ API Rest بنائیں:
    - صفحہ آفسیٹ اور حد کا استعمال کرتے ہوئے بیئرز کی فہرست حاصل کریں۔
    - id کے ذریعے بیئر کی تفصیلات حاصل کریں۔
    - نام، وضاحت، ٹیگ لائن، فوڈ پیئرنگز، اور قیمت کے ذریعے بیئر تلاش کریں۔
- مرکزی صفحے پر مصنوعات کی فہرست بنائیں۔
    - مصنوعات کو فلٹر کرنے کے لیے سرچ بار بنائیں۔
    - جب صارف کسی مصنوعات پر کلک کرے تو وضاحت کے صفحے پر جائیں۔
- (اختیاری) قیمت کے حساب سے مصنوعات کو فلٹر کرنے کے لیے Slicer۔
- Shopping cart بنائیں۔
    - مصنوعات کو کارٹ میں شامل کریں۔
    - مصنوعات کو کارٹ سے ہٹائیں۔
    - کارٹ میں مصنوعات کی کل قیمت کا حساب لگائیں۔

### **نمونہ کوڈ - Python**

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

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا عدم صحت ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔