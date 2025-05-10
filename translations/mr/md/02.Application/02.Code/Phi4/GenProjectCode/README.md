<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-05-09T19:49:33+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "mr"
}
-->
## **Phi-4-mini-mm वापरून कोड तयार करणे**

Phi-4-mini Phi कुटुंबाच्या मजबूत कोडिंग क्षमतांना पुढे नेत आहे. तुम्ही Prompt वापरून कोडिंगशी संबंधित प्रश्न विचारू शकता. अर्थातच, मजबूत तर्कशक्ती जोडल्यामुळे याची कोडिंग क्षमता अधिक वाढली आहे, जसे की गरजेनुसार प्रोजेक्ट तयार करणे. उदाहरणार्थ, गरजेनुसार प्रोजेक्ट तयार करणे, जसे की:

### **गरज**

Shopping Cart App तयार करा

- खालील पद्धतींसह API Rest तयार करा:
    - पृष्ठ ऑफसेट आणि लिमिट वापरून बिअरची यादी मिळवा.
    - id नुसार बिअरचे तपशील मिळवा.
    - नाव, वर्णन, टॅगलाइन, अन्न जोडी आणि किंमत यानुसार बिअर शोधा.
- मुख्य पानावर उत्पादनांची यादी तयार करा.
    - उत्पादनं फिल्टर करण्यासाठी सर्च बार तयार करा.
    - वापरकर्ता उत्पादनावर क्लिक केल्यावर वर्णन पानावर जा.
- (ऐच्छिक) किंमतीनुसार उत्पादनं फिल्टर करण्यासाठी स्लायसर.
- शॉपिंग कार्ट तयार करा.
    - उत्पादनं कार्टमध्ये जोडा.
    - उत्पादनं कार्टमधून काढा.
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
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितींसाठी व्यावसायिक मानवी भाषांतर शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.