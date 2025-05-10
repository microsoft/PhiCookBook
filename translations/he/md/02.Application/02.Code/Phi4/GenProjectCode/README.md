<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-05-09T19:51:03+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "he"
}
-->
## **שימוש ב-Phi-4-mini-mm ליצירת קוד**

Phi-4-mini ממשיך את יכולות הקידוד החזקות של משפחת Phi. ניתן להשתמש ב-Prompt כדי לשאול שאלות הקשורות לקידוד. כמובן, לאחר הוספת יכולת ההיגיון החזקה, יש לו יכולות קידוד חזקות יותר, כמו יצירת פרויקטים לפי דרישות. לדוגמה, יצירת פרויקטים לפי דרישות, כמו:

### **דרישה**

יצירת אפליקציית עגלת קניות

- יצירת API Rest עם השיטות הבאות:
    - קבלת רשימת בירות תוך שימוש ב-offset ו-limit של הדף.
    - קבלת פרטי בירה לפי מזהה.
    - חיפוש בירה לפי שם, תיאור, סלוגן, שילובי אוכל, ומחיר.
- יצירת רשימת מוצרים בדף הראשי.
    - יצירת סרגל חיפוש לסינון מוצרים.
    - ניווט לדף התיאור כאשר המשתמש לוחץ על מוצר.
- (אופציונלי) פילטר לסינון מוצרים לפי מחיר.
- יצירת עגלת קניות.
    - הוספת מוצרים לעגלה.
    - הסרת מוצרים מהעגלה.
    - חישוב המחיר הכולל של המוצרים בעגלה.

### **קוד לדוגמה - Python**


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

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו המקורית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.