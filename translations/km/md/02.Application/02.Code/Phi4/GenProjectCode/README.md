## **ប្រើ Phi-4-mini-mm ដើម្បីបង្កើតកូដ**

Phi-4-mini continues the strong coding capabilities of Phi Family. You can use Prompt to ask questions related to coding. Of course, after adding the strong reasoning ability, it has stronger coding capabilities, such as generating projects according to requirements.For example, generate projects according to requirements, such as:

### **តម្រូវការ**

Create a Shopping Cart App

- បង្កើត API Rest ជាមួយវិធីសាស្ត្រដូចខាងក្រោម:
    - ទទួលបញ្ជីស្រា ដោយប្រើ page offset និង limit។
    - ទទួលព័ត៌មានលម្អិតអំពីស្រាតាម id۔
    - ស្វែងរកស្រាតាមឈ្មោះ, ពិពណ៌នា, tagline, food pairings, និងតម្លៃ។

- បង្កើតបញ្ជីផលិតផលនៅលើទំព័រដើម:
    - បង្កើតប្រអប់ស្វែងរកសម្រាប់ចម្រាញ់ផលិតផល។
    - បញ្ជូនទៅទំព័រពិពណ៌នាពេលអ្នកប្រើចុចលើផលិតផល។

- (Optional) Slicer ដើម្បីចម្រាញ់ផលិតផលតាមតម្លៃ។

- បង្កើតរទេះទិញទំនិញ:
    - បន្ថែមផលិតផលទៅក្នុងរទេះ។
    - លុបផលិតផលចេញពីរទេះ។
    - គណនាតម្លៃសរុបនៃផលិតផលដែលនៅក្នុងរទេះ។

### **កូដគំរូ - Python**


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

               ## រចនាសម្ព័ន្ធគម្រោង

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## ផ្នែកខាងក្រោយ
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## ផ្នែកខាងមុខ
                 
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
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយ៉ាងណា ខណៈពេលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាម្ចាស់គួរត្រូវបានចាត់ទុកថាជាប្រភពដើមដែលអាចទុកចិត្តបាន។ សម្រាប់ព័ត៌មានសំខាន់ យើងសូមណែនាំឱ្យប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនោះ ឬការបកស្រាយខុសដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->