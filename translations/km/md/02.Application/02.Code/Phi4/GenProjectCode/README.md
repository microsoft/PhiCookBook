## **ការប្រើប្រាស់ Phi-4-mini-mm ដើម្បីបង្កើតកូដ**

Phi-4-mini បន្តសមត្ថភាពកូដខ្លាំងរបស់ Phi Family។ អ្នកអាចប្រើ Prompt ដើម្បីសួរពីកូដ។ នៅពេលប្រាកដបន្ថែមសមត្ថភាពហ្កោលហលខ្លាំង វាមានសមត្ថភាពកូដខ្លាំងជាងមុន ដូចជា បង្កើតគម្រោងតាមតម្រូវការ។ ឧទាហរណ៍ បង្កើតគម្រោងតាមតម្រូវការ ដូចជា៖

### **តម្រូវការ**

បង្កើតកម្មវិធីទិញទំនិញ (Shopping Cart App)

- បង្កើត API Rest ជាមួយវិធីសាស្រ្តដូចខាងក្រោម:
    - ទទួលបានបញ្ជីបៀរតាម page offset និង limit។
    - ទទួលបានព័ត៌មានលម្អិតបៀរតាម id។
    - ស្វែងរកបៀរតាមឈ្មោះ ពត៌មានលម្អិត ស្លាកមុខម្ហូប តម្លៃ។
- បង្កើតបញ្ជីផលិតផលនៅផ្ទាំងចម្បង។
    - បង្កើតរបារស្វែងរកដើម្បីតម្រៀបផលិតផល។
    - បញ្ជូនទៅផ្ទាំងព័ត៌មានពេលអ្នកប្រើចុចលើផលិតផលមួយ។
- (ជាជម្រើស) Slicer ដើម្បីតម្រៀបផលិតផលតាមតម្លៃ។
- បង្កើតកន្ត្រកទិញទំនិញ។
    - បន្ថែមផលិតផលទៅកន្ត្រក។
    - យកផលិតផលចេញពីកន្ត្រក។
    - គណនាតម្លៃសរុបនៃផលិតផលនៅក្នុងកន្ត្រក។

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

               ## ផ្នែកបន្ទ.backend
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## ផ្នែកមុខend
                 
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
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខំប្រឹងឱ្យបានការត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយអូតូម៉ាទစ်អាចមានកំហុស ឬការមិនត្រឹមត្រូវរួមបញ្ចូល។ ឯកសារដើមនៅក្នុងភាសា​ដើមគួរត្រូវបានគិតថា​ជាប្រភព​ដ៏មានសារៈៈសំខាន់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្តល់អនុសាសន៍ឱ្យមានការបកប្រែដោយអ្នកជំនាញមនុស្សវិជ្ជមាន។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->