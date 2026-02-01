# **Phi-4-mini ONNX နှင့် စကားပြောခြင်း**

***ONNX*** သည် စက်လေ့လာမှု မော်ဒယ်များကို ကိုယ်စားပြုရန် ဖွင့်လှစ်ထားသော ဖော်မတ်တစ်ခုဖြစ်သည်။ ONNX သည် စက်လေ့လာမှုနှင့် နက်ရှိုင်းသောလေ့လာမှု မော်ဒယ်များ၏ အခြေခံအဆောက်အအုံဖြစ်သော အော်ပရေတာများကို သတ်မှတ်ပေးပြီး၊ AI ဖန်တီးသူများအနေဖြင့် မော်ဒယ်များကို အမျိုးမျိုးသော ဖရိမ်ဝပ်များ၊ ကိရိယာများ၊ အချိန်ပြေးပတ်စက်များနှင့် ကုဒ်ပြောင်းသူများနှင့် အသုံးပြုနိုင်ရန် ပုံစံတစ်ခုအဖြစ် ဖိုင်ဖော်မတ်တစ်ခုကို သတ်မှတ်ပေးထားသည်။

ကျွန်ုပ်တို့သည် edge စက်ပစ္စည်းများပေါ်တွင် generative AI မော်ဒယ်များကို တပ်ဆင်ပြီး ကန့်သတ်ထားသော ကွန်ပျူတာစွမ်းအား သို့မဟုတ် အော့ဖ်လိုင်းပတ်ဝန်းကျင်များတွင် အသုံးပြုလိုပါသည်။ ယခုအခါ မော်ဒယ်ကို quantized နည်းဖြင့် ပြောင်းလဲခြင်းဖြင့် ဤရည်မှန်းချက်ကို အောင်မြင်စွာ ရောက်ရှိနိုင်ပါပြီ။ quantized မော်ဒယ်ကို GGUF သို့မဟုတ် ONNX ဖော်မတ်သို့ ပြောင်းလဲနိုင်ပါသည်။

Microsoft Olive သည် SLM ကို quantized ONNX ဖော်မတ်သို့ ပြောင်းလဲရာတွင် ကူညီပေးနိုင်ပါသည်။ မော်ဒယ်ပြောင်းလဲခြင်းနည်းလမ်းမှာ အလွန်ရိုးရှင်းပါသည်။

**Microsoft Olive SDK ကို တပ်ဆင်ပါ**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX ကို ပံ့ပိုးမှု ပြောင်းလဲခြင်း**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** ဤဥပမာတွင် CPU ကို အသုံးပြုထားသည်


### **ONNX Runtime GenAI ဖြင့် Phi-4-mini ONNX မော်ဒယ်ကို ခန့်မှန်းခြင်း**

- **ONNX Runtime GenAI ကို တပ်ဆင်ပါ**

```bash

pip install --pre onnxruntime-genai

```

- **Python ကုဒ်**

*ဤသည်မှာ ONNX Runtime GenAI 0.5.2 ဗားရှင်းဖြစ်သည်*

```python

import onnxruntime_genai as og
import numpy as np
import os


model_folder = "Your Phi-4-mini-onnx-cpu-int4 location"


model = og.Model(model_folder)


tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()


search_options = {}
search_options['max_length'] = 2048
search_options['past_present_share_buffer'] = False


chat_template = "<|user|>\n{input}</s>\n<|assistant|>"


text = """Can you introduce yourself"""


prompt = f'{chat_template.format(input=text)}'


input_tokens = tokenizer.encode(prompt)


params = og.GeneratorParams(model)


params.set_search_options(**search_options)
params.input_ids = input_tokens


generator = og.Generator(model, params)


while not generator.is_done():
      generator.compute_logits()
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      print(tokenizer_stream.decode(new_token), end='', flush=True)

```


*ဤသည်မှာ ONNX Runtime GenAI 0.6.0 ဗားရှင်းဖြစ်သည်*

```python

import onnxruntime_genai as og
import numpy as np
import os
import time
import psutil

model_folder = "Your Phi-4-mini-onnx model path"

model = og.Model(model_folder)

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

search_options = {}
search_options['max_length'] = 1024
search_options['past_present_share_buffer'] = False

chat_template = "<|user|>{input}<|assistant|>"

text = """can you introduce yourself"""

prompt = f'{chat_template.format(input=text)}'

input_tokens = tokenizer.encode(prompt)

params = og.GeneratorParams(model)

params.set_search_options(**search_options)

generator = og.Generator(model, params)

generator.append_tokens(input_tokens)

while not generator.is_done():
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      token_text = tokenizer.decode(new_token)
      # print(tokenizer_stream.decode(new_token), end='', flush=True)
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။