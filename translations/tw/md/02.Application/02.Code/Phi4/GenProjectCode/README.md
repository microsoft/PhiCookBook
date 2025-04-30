<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aacf82e3da702afd8469bba99b662509",
  "translation_date": "2025-04-04T06:46:39+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi4\\GenProjectCode\\README.md",
  "language_code": "tw"
}
-->
## **使用 Phi-4-mini-mm 生成程式碼**

Phi-4-mini 延續了 Phi 家族強大的編碼能力。你可以使用 Prompt 提出與編碼相關的問題。當然，在加入了強大的推理能力後，它的編碼能力更為強大，例如可以根據需求生成專案。例如，根據需求生成專案，如下：

### **需求**

建立一個購物車應用程式

- 建立一個具有以下方法的 API Rest：
    - 使用頁面偏移量和限制數量獲取啤酒列表。
    - 根據 ID 獲取啤酒詳細資訊。
    - 根據名稱、描述、標語、搭配食物和價格搜尋啤酒。
- 在主頁面建立產品列表。
    - 建立一個搜尋欄來篩選產品。
    - 當使用者點擊產品時，導航至詳細資訊頁面。
- （可選）建立價格篩選器來篩選產品。
- 建立一個購物車。
    - 將產品加入購物車。
    - 從購物車中移除產品。
    - 計算購物車中產品的總價格。

### **範例程式碼 - Python**

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

**免責聲明**:  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文檔應被視為具有權威性的來源。對於重要信息，建議使用專業的人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。