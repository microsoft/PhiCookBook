<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-03-27T12:39:21+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi4\\GenProjectCode\\README.md",
  "language_code": "ar"
}
-->
## **استخدام Phi-4-mini-mm لإنشاء الكود**

يواصل Phi-4-mini تقديم قدرات برمجية قوية كجزء من عائلة Phi. يمكنك استخدام Prompt لطرح أسئلة تتعلق بالبرمجة. وبالطبع، بعد إضافة القدرة القوية على التفكير، أصبح لديه قدرات برمجية أقوى، مثل إنشاء المشاريع وفقًا للمتطلبات. على سبيل المثال، إنشاء مشاريع بناءً على المتطلبات، مثل:

### **المتطلبات**

إنشاء تطبيق عربة تسوق

- إنشاء API Rest يحتوي على الطرق التالية:
    - الحصول على قائمة من أنواع البيرة باستخدام تعويض الصفحة والحد.
    - الحصول على تفاصيل البيرة باستخدام معرفها.
    - البحث عن البيرة باستخدام الاسم، الوصف، الشعار، توافق الطعام، والسعر.
- إنشاء قائمة بالمنتجات على الصفحة الرئيسية.
    - إنشاء شريط بحث لتصفية المنتجات.
    - الانتقال إلى صفحة الوصف عندما ينقر المستخدم على منتج.
- (اختياري) إضافة فلتر لتصفية المنتجات حسب السعر.
- إنشاء عربة تسوق.
    - إضافة المنتجات إلى العربة.
    - إزالة المنتجات من العربة.
    - حساب السعر الإجمالي للمنتجات الموجودة في العربة.

### **عينة الكود - Python**


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

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى باستخدام ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.