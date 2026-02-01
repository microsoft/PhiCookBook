## **Phi-4-mini-mm ഉപയോഗിച്ച് കോഡ് സൃഷ്ടിക്കാൻ**

Phi-4-mini Phi Family-യുടെ ശക്തമായ കോഡിംഗ് ശേഷികളെ തുടരുമാണ്. കോഡിങ്ങുമായി ബന്ധപ്പെട്ട ചോദ്യങ്ങൾ ചോദിക്കാൻ നിങ്ങൾക്ക് Prompt ഉപയോഗിക്കാം. തീർച്ചയായും, ശക്തമായ തർക്കചിന്തന ശേഷി ചേർക്കപ്പെട്ടതോടെ, അതിന്റെ കോഡിംഗ് കഴിവുകൾ കൂടുതൽ ശക്തമാകുകയും ആവശ്യകതകളനുസരിച്ച് പ്രോജക്ടുകൾ ജനറേറ്റ് ചെയ്യാനും കഴിയും. ഉദാഹരണത്തിന്, ആവശ്യകതകൾ അനുസരിച്ച് പ്രോജക്ടുകൾ താഴെപറയുന്നപോലെ സൃഷ്ടിക്കാവുന്നതാണ്:

### **Requirement**

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - Page offset and limit ഉപയോഗിച്ച് ബിയറുകളുടെ പട്ടിക നേടുക.
    - ഐഡിയുടെ അടിസ്ഥാനത്തിൽ ബിയറിന്റെ വിശദാംശങ്ങൾ നേടുക.
    - നാമം, വിവരണം, ടാഗ്ലൈൻ, ഭക്ഷണ ജോഡികൾ, വില എന്നിവയാൽ ബിയർ തിരയുക.
- Create a list of products on the main page.
    - ഉൽപ്പന്നങ്ങൾ ഫിൽട്ടർ ചെയ്യാൻ ഒരു സെർച് ബാർ സൃഷ്ടിക്കുക.
    - ഉപയോക്താവ് ഒരു ഉൽപ്പന്നത്തിൽ ക്ലിക്ക് ചെയ്യുമ്പോൾ വിവരണ പേജിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.
- (Optional) വില പ്രകാരം ഉൽപ്പന്നങ്ങൾ ഫിൽട്ടർ ചെയ്യാൻ ഒരു സ്ലൈസർ.
- Create a shopping cart.
    - ഉൽപ്പന്നങ്ങൾ കാർട്ടിൽ ചേർക്കുക.
    - കാർട്ടിൽ നിന്ന് ഉൽപ്പന്നങ്ങൾ നീക്കം ചെയ്യുക.
    - കാർട്ടിലുള്ള ഉൽപ്പന്നങ്ങളുടെ മൊത്ത വില കണക്കാക്കുക.

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

               ## പ്രോജക്ട് ഘടന

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## ബാക്ക് എൻഡ്
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## ഫ്രണ്ട് എൻഡ്
                 
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
ഡിസ്‌ക്ലെയിമർ:
ഈ ഡോക്യുമെന്റ് AI-ആധാരിത വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിച്ചെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ അശുദ്ധികൾ ഉണ്ടാവാൻ സാധ്യതയുണ്ട് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിനാൽ, യഥാർത്ഥ ഭാഷയിൽ ഉള്ള മൂല രേഖ പ്രാമാണിക ഉറവിടമായി പരിഗണിക്കണം. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്താൽ ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്ക് ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->