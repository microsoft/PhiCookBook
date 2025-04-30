<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aacf82e3da702afd8469bba99b662509",
  "translation_date": "2025-04-03T07:51:02+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi4\\GenProjectCode\\README.md",
  "language_code": "ur"
}
-->
## **Phi-4-mini-mm کا استعمال کرتے ہوئے کوڈ تیار کرنا**

Phi-4-mini Phi فیملی کی مضبوط کوڈنگ صلاحیتوں کو جاری رکھتا ہے۔ آپ کوڈنگ سے متعلق سوالات پوچھنے کے لیے Prompt کا استعمال کر سکتے ہیں۔ یقیناً، مضبوط منطقی قابلیت شامل کرنے کے بعد، اس میں کوڈنگ کی مزید بہتر صلاحیتیں ہیں، جیسے کہ ضروریات کے مطابق پروجیکٹس تیار کرنا۔ مثال کے طور پر، ضروریات کے مطابق پروجیکٹس تیار کریں، جیسے:

### **ضرورت**

ایک شاپنگ کارٹ ایپ بنائیں

- درج ذیل طریقوں کے ساتھ ایک API Rest بنائیں:
    - صفحہ آفسیٹ اور حد کے ساتھ بیئرز کی فہرست حاصل کریں۔
    - id کے ذریعے بیئر کی تفصیلات حاصل کریں۔
    - نام، وضاحت، ٹیگ لائن، کھانے کے ساتھ میل جول، اور قیمت کے ذریعے بیئر تلاش کریں۔
- مین صفحے پر پروڈکٹس کی ایک فہرست بنائیں۔
    - پروڈکٹس کو فلٹر کرنے کے لیے ایک سرچ بار بنائیں۔
    - جب صارف کسی پروڈکٹ پر کلک کرے تو تفصیلات کے صفحے پر جائیں۔
- (اختیاری) قیمت کے ذریعے پروڈکٹس کو فلٹر کرنے کے لیے ایک سلائسر۔
- ایک شاپنگ کارٹ بنائیں۔
    - پروڈکٹس کو کارٹ میں شامل کریں۔
    - پروڈکٹس کو کارٹ سے ہٹائیں۔
    - کارٹ میں موجود پروڈکٹس کی کل قیمت کا حساب لگائیں۔

### **نمونہ کوڈ - پائتھن**


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
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ ہم درستگی کی بھرپور کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ذمہ دار نہیں ہیں۔