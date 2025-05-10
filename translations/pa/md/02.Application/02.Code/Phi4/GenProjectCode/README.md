<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-05-09T19:49:45+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "pa"
}
-->
## **Phi-4-mini-mm ਨਾਲ ਕੋਡ ਬਣਾਉਣ ਲਈ ਵਰਤੋਂ**

Phi-4-mini Phi ਪਰਿਵਾਰ ਦੀ ਮਜ਼ਬੂਤ ਕੋਡਿੰਗ ਸਮਰੱਥਾ ਨੂੰ ਜਾਰੀ ਰੱਖਦਾ ਹੈ। ਤੁਸੀਂ Prompt ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੋਡਿੰਗ ਨਾਲ ਸਬੰਧਤ ਸਵਾਲ ਪੁੱਛ ਸਕਦੇ ਹੋ। ਬਿਲਕੁਲ, ਮਜ਼ਬੂਤ ਤਰਕਸ਼ੀਲ ਸਮਰੱਥਾ ਸ਼ਾਮਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਇਸਦੀ ਕੋਡਿੰਗ ਸਮਰੱਥਾ ਹੋਰ ਵੀ ਵਧ ਗਈ ਹੈ, ਜਿਵੇਂ ਕਿ ਮੰਗਾਂ ਦੇ ਅਨੁਸਾਰ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣਾ। ਉਦਾਹਰਨ ਵਜੋਂ, ਮੰਗਾਂ ਦੇ ਅਨੁਸਾਰ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣਾ, ਜਿਵੇਂ:

### **ਮੰਗ**

ਇੱਕ Shopping Cart App ਬਣਾਓ

- ਹੇਠਾਂ ਦਿੱਤੇ ਮੈਥਡਾਂ ਨਾਲ ਇੱਕ API Rest ਬਣਾਓ:
    - ਪੇਜ ਆਫਸੈਟ ਅਤੇ ਸੀਮਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬੀਅਰਾਂ ਦੀ ਸੂਚੀ ਲਵੋ।
    - id ਦੇ ਨਾਲ ਬੀਅਰ ਦੇ ਵੇਰਵੇ ਲਵੋ।
    - ਨਾਮ, ਵਰਣਨ, ਟੈਗਲਾਈਨ, ਫੂਡ ਪੇਅਰਿੰਗ ਅਤੇ ਕੀਮਤ ਦੁਆਰਾ ਬੀਅਰ ਖੋਜੋ।
- ਮੁੱਖ ਪੰਨੇ 'ਤੇ ਉਤਪਾਦਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ।
    - ਉਤਪਾਦਾਂ ਨੂੰ ਫਿਲਟਰ ਕਰਨ ਲਈ ਇੱਕ ਖੋਜ ਬਾਰ ਬਣਾਓ।
    - ਜਦੋਂ ਉਪਭੋਗਤਾ ਕਿਸੇ ਉਤਪਾਦ 'ਤੇ ਕਲਿੱਕ ਕਰੇ ਤਾਂ ਵਰਣਨ ਪੰਨੇ ਤੇ ਜਾਓ।
- (ਵਿਕਲਪਿਕ) ਕੀਮਤ ਦੁਆਰਾ ਉਤਪਾਦਾਂ ਨੂੰ ਫਿਲਟਰ ਕਰਨ ਲਈ ਸਲਾਈਸਰ।
- ਇੱਕ shopping cart ਬਣਾਓ।
    - ਕਾਰਟ ਵਿੱਚ ਉਤਪਾਦ ਜੋੜੋ।
    - ਕਾਰਟ ਵਿੱਚੋਂ ਉਤਪਾਦ ਹਟਾਓ।
    - ਕਾਰਟ ਵਿੱਚ ਉਤਪਾਦਾਂ ਦੀ ਕੁੱਲ ਕੀਮਤ ਗਿਣੋ।

### **ਨਮੂਨਾ ਕੋਡ - Python**


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

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਪਜੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।