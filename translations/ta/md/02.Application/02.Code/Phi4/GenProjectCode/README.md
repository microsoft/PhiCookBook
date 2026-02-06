## **Phi-4-mini-mm பயன்படுத்தி குறியீடு உருவாக்குதல்**

Phi-4-mini, Phi குடும்பத்தின் வலுவான குறியீட்டு திறன்களை தொடர்கிறது. நீங்கள் Prompt-ஐ பயன்படுத்தி குறியீடு தொடர்பான கேள்விகளை கேட்கலாம். மேலும், வலுவான காரணமறிதல் திறனைச் சேர்த்த பிறகு, இது மேலும் வலுவான குறியீட்டு திறன்களை கொண்டுள்ளது, உதாரணமாக தேவைகளுக்கு ஏற்ப திட்டங்களை உருவாக்குதல். உதாரணமாக, தேவைகளுக்கு ஏற்ப திட்டங்களை உருவாக்குதல், இதுபோல:

### **தேவை**

ஒரு Shopping Cart App உருவாக்கவும்

- பின்வரும் முறைகளுடன் ஒரு API Rest உருவாக்கவும்:
    - பக்கம் offset மற்றும் limit பயன்படுத்தி பியரின் பட்டியலைப் பெறவும்.
    - id மூலம் பியர் விவரங்களைப் பெறவும்.
    - பெயர், விளக்கம், tagline, உணவு இணைப்புகள் மற்றும் விலை மூலம் பியரைத் தேடவும்.
- முதன்மை பக்கத்தில் பொருட்களின் பட்டியலை உருவாக்கவும்.
    - பொருட்களை வடிகட்ட ஒரு தேடல் பட்டியை உருவாக்கவும்.
    - பயனர் ஒரு பொருளை கிளிக் செய்தால், விளக்கம் பக்கத்திற்கு செல்லவும்.
- (விருப்பம்) பொருட்களை விலை மூலம் வடிகட்ட slicer உருவாக்கவும்.
- ஒரு Shopping Cart உருவாக்கவும்.
    - பொருட்களை கார்டில் சேர்க்கவும்.
    - பொருட்களை கார்டிலிருந்து நீக்கவும்.
    - கார்டில் உள்ள பொருட்களின் மொத்த விலையை கணக்கிடவும்.

### **மாதிரி குறியீடு - Python**

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

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்சிறப்பிற்காக முயற்சி செய்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.