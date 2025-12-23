<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-12-21T19:30:14+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "kn"
}
-->
## **Phi-4-mini-mm ಅನ್ನು ಕೋಡ್ ರಚಿಸಲು ಬಳಸುವುದು**

Phi-4-mini Phi Family ರ ಶಕ್ತಿಶಾಲಿ ಕೋಡಿಂಗ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಮುಂದುವರಿಸುತ್ತದೆ. ನೀವು Prompt ಅನ್ನು ಕೋಡಿಂಗ್‌ಗೆ ಸಂಬಂಧಿಸಿದ ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳಲು ಬಳಸಬಹುದು. ಹೊರತುಪಡಿಸಿ, ಶಕ್ತಿಶಾಲಿ ತರ್ಕ ಸಾಮರ್ಥ್ಯವನ್ನು ಸೇರಿಸಿದ ನಂತರ, ಅದರ ಕೋಡಿಂಗ್ ಸಾಮರ್ಥ್ಯಗಳು ಇನ್ನೂ ಬಲಿಷ್ಠವಾಗುತ್ತವೆ, ಉದಾಹರಣೆಗೆ ಅಗತ್ಯಗಳ ಪ್ರಕಾರ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳನ್ನು ರಚಿಸುವಂತಹ ಕಾರ್ಯಗಳನ್ನು ನಡೆಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ಅಗತ್ಯಗಳ ಪ್ರಕಾರ ಕೆಳಗಿನಂತಹ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳನ್ನು ರಚಿಸಬಹುದು:

### **Requirement**

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - ಪುಟ ಆಫ್‌ಸೆಟ್ ಮತ್ತು ಮಿತಿಯನ್ನು ಬಳಸಿ ಬೀಯರ್‌ಗಳ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯಿರಿ.
    - id ಮೂಲಕ ಬೀಯರ್ ವಿವರಗಳನ್ನು ಪಡೆಯಿರಿ.
    - ಹೆಸರು, ವಿವರಣೆ, ಟ್ಯಾಗ್ಲೈನ್, ಆಹಾರದ ಜೋಡಣೆಗಳು ಮತ್ತು ಬೆಲೆ ಮೂಲಕ ಬೀಯರ್ ಅನ್ನು ಹುಡುಕಿ.
- Create a list of products on the main page.
    - ಉತ್ಪನ್ನಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡಲು ಒಂದು ಶೋಧನಾ ಬಾರ್ ರಚಿಸಿ.
    - ಬಳಕೆದಾರರು ಉತ್ಪನ್ನದ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿದಾಗ ಅವರು ವಿವರಣೆ ಪುಟಕ್ಕೆ ಹೋಗಲಿ.
- (Optional) ಬೆಲೆಯ ಮೂಲಕ ಉತ್ಪನ್ನಗಳನ್ನು ಫಿಲ್ಟರ್ ಮಾಡಲು ಸ್ಲೈಸರ್.
- Create a shopping cart.
    - ಕಾರ್ಟಿಗೆ ಉತ್ಪನ್ನಗಳನ್ನು ಸೇರಿಸಿ.
    - ಕಾರ್ಟ್‌ನಿಂದ ಉತ್ಪನ್ನಗಳನ್ನು ತೆಗೆದುಹಾಕಿ.
    - ಕಾರ್ಟ್‌ನಲ್ಲಿ ಇರುವ ಉತ್ಪನ್ನಗಳ ಒಟ್ಟು ಬೆಲೆಯನ್ನು ಲೆಕ್ಕಿಸಿ.

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

               ## ಪ್ರಾಜೆಕ್ಟ್ ಸಂರಚನೆ

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## ಬ್ಯಾಕೆಂಡ್
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## ಫ್ರಂಟೆಂಡ್
                 
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
ಅಸ್ವೀಕರಣ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ Co‑op Translator (https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯತ್ತ ಪ್ರಯತ್ನಿಸಿದರೂ ಸಹ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದದಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ನಿಖರತೆಯ ಕೊರತೆಗಳಿರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲ ದಸ್ತಾವೇಜನ್ನುಾಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಅಥವಾ ಅತ್ಯವಶ್ಯಕ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅರ್ಥಭ್ರಂಶಗಳು ಅಥವಾ ತಪ್ಪು ಅರ್ಥಗಳಕ್ಕಾಗಿ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->