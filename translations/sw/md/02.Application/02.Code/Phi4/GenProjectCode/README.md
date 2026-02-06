## **Kutumia Phi-4-mini-mm kuunda msimbo**

Phi-4-mini inaendelea na uwezo mkubwa wa kuandika msimbo wa Familia ya Phi. Unaweza kutumia Prompt kuuliza maswali yanayohusiana na uandishi wa msimbo. Bila shaka, baada ya kuongeza uwezo mkubwa wa kufikiri, ina uwezo mkubwa zaidi wa kuandika msimbo, kama vile kuunda miradi kulingana na mahitaji. Kwa mfano, kuunda miradi kulingana na mahitaji, kama:

### **Mahitaji**

Tengeneza Programu ya Gari la Ununuzi

- Tengeneza API Rest yenye njia zifuatazo:
    - Pata orodha ya bia kwa kutumia page offset na limit.
    - Pata maelezo ya bia kwa id.
    - Tafuta bia kwa jina, maelezo, tagline, mchanganyiko wa chakula, na bei.
- Tengeneza orodha ya bidhaa kwenye ukurasa mkuu.
    - Tengeneza upau wa utafutaji kuchuja bidhaa.
    - Elekeza kwenye ukurasa wa maelezo wakati mtumiaji anabonyeza bidhaa.
- (Hiari) Slicer kuchuja bidhaa kwa bei.
- Tengeneza gari la ununuzi.
    - Ongeza bidhaa kwenye gari.
    - Ondoa bidhaa kutoka kwenye gari.
    - Hesabu jumla ya bei ya bidhaa zilizoko kwenye gari.

### **Mfano wa Msimbo - Python**


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

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.