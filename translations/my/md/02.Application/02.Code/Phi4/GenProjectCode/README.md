<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e7bb23ac4d9ef7b419305d8a5745b7aa",
  "translation_date": "2025-07-09T19:36:06+00:00",
  "source_file": "md/02.Application/02.Code/Phi4/GenProjectCode/README.md",
  "language_code": "my"
}
-->
## **Phi-4-mini-mm ကို ကုဒ်ဖန်တီးရန် အသုံးပြုခြင်း**

Phi-4-mini သည် Phi Family ၏ အားကောင်းသော ကုဒ်ရေးနိုင်မှုများကို ဆက်လက်ထောက်ပံ့ပေးသည်။ သင်သည် Prompt ကို အသုံးပြု၍ ကုဒ်ရေးခြင်းနှင့် ဆိုင်သော မေးခွန်းများကို မေးနိုင်သည်။ သဘာဝတရားအရ အကြောင်းပြချက်ပြနိုင်မှုအားကောင်းလာပြီးနောက်တွင် ကုဒ်ရေးနိုင်မှု ပိုမိုတိုးတက်လာပြီး၊ လိုအပ်ချက်အရ ပရောဂျက်များ ဖန်တီးနိုင်သည်။ ဥပမာအားဖြင့် လိုအပ်ချက်အရ ပရောဂျက်များ ဖန်တီးခြင်းကဲ့သို့ဖြစ်သည်-

### **လိုအပ်ချက်**

Shopping Cart App တစ်ခု ဖန်တီးပါ

- အောက်ပါနည်းလမ်းများဖြင့် API Rest တစ်ခု ဖန်တီးပါ-
    - စာမျက်နှာ offset နှင့် အကန့်အသတ်ကို အသုံးပြု၍ ဘီယာစာရင်း ရယူပါ။
    - id ဖြင့် ဘီယာအသေးစိတ် ရယူပါ။
    - နာမည်၊ ဖော်ပြချက်၊ tagline၊ အစားအစာတွဲဖက်မှုများနှင့် စျေးနှုန်းဖြင့် ဘီယာ ရှာဖွေပါ။
- မူလစာမျက်နှာတွင် ထုတ်ကုန်စာရင်း တစ်ခု ဖန်တီးပါ။
    - ထုတ်ကုန်များကို စစ်ထုတ်ရန် ရှာဖွေရေးဘား တစ်ခု ဖန်တီးပါ။
    - အသုံးပြုသူသည် ထုတ်ကုန်တစ်ခုကို နှိပ်သောအခါ ဖော်ပြချက်စာမျက်နှာသို့ သွားပါ။
- (Optional) စျေးနှုန်းအလိုက် ထုတ်ကုန်များကို စစ်ထုတ်ရန် Slicer တစ်ခု။
- Shopping cart တစ်ခု ဖန်တီးပါ။
    - ထုတ်ကုန်များကို ကတ်ထဲ ထည့်ပါ။
    - ထုတ်ကုန်များကို ကတ်ထဲမှ ဖယ်ရှားပါ။
    - ကတ်ထဲရှိ ထုတ်ကုန်များ၏ စုစုပေါင်းစျေးနှုန်းကိုတွက်ချက်ပါ။

### **နမူနာကုဒ် - Python**


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

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။