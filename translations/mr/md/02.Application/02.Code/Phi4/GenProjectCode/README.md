<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-07-17T04:44:34+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "mr"
}
-->
## **Phi-4-mini-mm वापरून कोड तयार करणे**

Phi-4-mini Phi कुटुंबाच्या मजबूत कोडिंग क्षमतेला पुढे नेते. तुम्ही कोडिंगशी संबंधित प्रश्न विचारण्यासाठी Prompt वापरू शकता. अर्थातच, त्यात मजबूत तर्कशक्ती जोडल्यामुळे, त्याची कोडिंग क्षमता अधिक प्रगल्भ झाली आहे, जसे की गरजेनुसार प्रोजेक्ट तयार करणे. उदाहरणार्थ, गरजेनुसार प्रोजेक्ट तयार करणे, जसे की:

### **गरज**

शॉपिंग कार्ट अॅप तयार करा

- खालील पद्धतींसह API Rest तयार करा:
    - पेज ऑफसेट आणि लिमिट वापरून बिअर्सची यादी मिळवा.
    - आयडीने बिअर तपशील मिळवा.
    - नाव, वर्णन, टॅगलाइन, फूड पेअरिंग्ज आणि किंमतीनुसार बिअर शोधा.
- मुख्य पृष्ठावर उत्पादनांची यादी तयार करा.
    - उत्पादन फिल्टर करण्यासाठी सर्च बार तयार करा.
    - वापरकर्ता एखाद्या उत्पादनावर क्लिक केल्यावर वर्णन पृष्ठावर नेव्हिगेट करा.
- (ऐच्छिक) किंमतीनुसार उत्पादन फिल्टर करण्यासाठी स्लायसर.
- शॉपिंग कार्ट तयार करा.
    - कार्टमध्ये उत्पादने जोडा.
    - कार्टमधून उत्पादने काढा.
    - कार्टमधील उत्पादनांची एकूण किंमत मोजा.

### **नमुना कोड - Python**


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
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.