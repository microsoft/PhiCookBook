<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-07-17T04:44:41+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "ne"
}
-->
## **Phi-4-mini-mm प्रयोग गरेर कोड सिर्जना गर्ने**

Phi-4-mini ले Phi परिवारको बलियो कोडिङ क्षमताहरूलाई निरन्तरता दिएको छ। तपाईंले कोडिङ सम्बन्धी प्रश्नहरू सोध्न Prompt प्रयोग गर्न सक्नुहुन्छ। पक्कै पनि, बलियो तर्क क्षमतासँगै यसले अझ बलियो कोडिङ क्षमता प्रदान गर्दछ, जस्तै आवश्यकताअनुसार प्रोजेक्टहरू सिर्जना गर्ने। उदाहरणका लागि, आवश्यकताअनुसार प्रोजेक्टहरू सिर्जना गर्नुहोस्, जस्तै:

### **आवश्यकता**

शपिंग कार्ट एप बनाउनुहोस्

- तलका विधिहरू सहित API Rest बनाउनुहोस्:
    - पेज अफसेट र लिमिट प्रयोग गरेर बियरहरूको सूची प्राप्त गर्नुहोस्।
    - आईडी द्वारा बियर विवरण प्राप्त गर्नुहोस्।
    - नाम, विवरण, ट्यागलाइन, खाना जोडी, र मूल्य अनुसार बियर खोज्नुहोस्।
- मुख्य पृष्ठमा उत्पादनहरूको सूची बनाउनुहोस्।
    - उत्पादनहरू फिल्टर गर्न खोज पट्टी बनाउनुहोस्।
    - प्रयोगकर्ताले उत्पादनमा क्लिक गर्दा विवरण पृष्ठमा जानुहोस्।
- (वैकल्पिक) मूल्य अनुसार उत्पादनहरू फिल्टर गर्न स्लाइसर।
- शपिंग कार्ट बनाउनुहोस्।
    - कार्टमा उत्पादनहरू थप्नुहोस्।
    - कार्टबाट उत्पादनहरू हटाउनुहोस्।
    - कार्टमा रहेका उत्पादनहरूको कुल मूल्य गणना गर्नुहोस्।

### **नमूना कोड - Python**


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

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।