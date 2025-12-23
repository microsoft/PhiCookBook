<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-12-21T19:25:10+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "pcm"
}
-->
## **How to use Phi-4-mini-mm take make code**

Phi-4-mini dey continue the strong coding capabilities wey Phi Family get. You fit use Prompt to ask questions wey concern coding. Of course, as e don add strong reasoning ability, e get even stronger coding skills — e fit generate projects according to requirements. For example, e fit generate projects based on requirements, like:

### **Wetin Dem Want**

Create a Shopping Cart App

- Make an API Rest wey get the following methods:
    - Get list of beers using page offset and limit.
    - Get beer details by id.
    - Search beer by name, description, tagline, food pairings, and price.
- Make list of products for the main page.
    - Make search bar wey go filter products.
    - Make e navigate go the description page when user click one product.
- (Optional) Slicer wey go filter products by price.
- Make shopping cart.
    - Add products to the cart.
    - Remove products from the cart.
    - Calculate the total price of the products wey dey inside the cart.

### **Sample Code - Python**


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

               ## How di project dey arranged

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## Back-end (wey dey handle di server)
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## Front-end (wey di user dey see)
                 
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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document na AI translation wey [Co-op Translator](https://github.com/Azure/co-op-translator) do. Even though we dey try make am correct, abeg sabi say automatic translations fit get errors or mistakes. The original document for im original language suppose be di main authority. If na critical information, e better make professional human translator do di translation. We no be responsible for any misunderstanding or wrong interpretation wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->