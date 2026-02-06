## **Korištenje Phi-4-mini-mm za generiranje koda**

Phi-4-mini nastavlja snažne mogućnosti kodiranja iz Phi Family. Možete koristiti Prompt za postavljanje pitanja vezanih uz kodiranje. Naravno, uz dodatak snažne sposobnosti rezoniranja, ima i jače mogućnosti kodiranja, poput generiranja projekata prema zahtjevima. Na primjer, generiranje projekata prema zahtjevima, kao što su:

### **Zahtjev**

Izradite aplikaciju za košaricu za kupovinu

- Izradite REST API s sljedećim metodama:
    - Dohvati popis piva koristeći page offset i limit.
    - Dohvati detalje piva prema id-u.
    - Pretraži pivo po imenu, opisu, taglineu, uparivanju s hranom i cijeni.
- Izradite popis proizvoda na glavnoj stranici.
    - Izradite tražilicu za filtriranje proizvoda.
    - Preusmjerite na stranicu s opisom kada korisnik klikne na proizvod.
- (Opcionalno) Slicer za filtriranje proizvoda po cijeni.
- Izradite košaricu za kupovinu.
    - Dodajte proizvode u košaricu.
    - Uklonite proizvode iz košarice.
    - Izračunajte ukupnu cijenu proizvoda u košarici.

### **Primjer koda - Python**


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

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.