<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-07-17T03:15:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "ur"
}
-->
# **Phi-4-mini ONNX کے ساتھ چیٹ کریں**

***ONNX*** ایک کھلا فارمیٹ ہے جو مشین لرننگ ماڈلز کی نمائندگی کے لیے بنایا گیا ہے۔ ONNX ایک مشترکہ آپریٹرز کا سیٹ متعین کرتا ہے - جو مشین لرننگ اور ڈیپ لرننگ ماڈلز کے بنیادی اجزاء ہیں - اور ایک مشترکہ فائل فارمیٹ فراہم کرتا ہے تاکہ AI ڈویلپرز مختلف فریم ورکس، ٹولز، رن ٹائمز، اور کمپائلرز کے ساتھ ماڈلز استعمال کر سکیں۔

ہم امید کرتے ہیں کہ جنریٹو AI ماڈلز کو ایج ڈیوائسز پر تعینات کریں اور انہیں محدود کمپیوٹنگ پاور یا آف لائن ماحول میں استعمال کریں۔ اب ہم یہ مقصد ماڈل کو کوانٹائزڈ طریقے سے تبدیل کر کے حاصل کر سکتے ہیں۔ ہم کوانٹائزڈ ماڈل کو GGUF یا ONNX فارمیٹ میں تبدیل کر سکتے ہیں۔

Microsoft Olive آپ کی مدد کر سکتا ہے کہ آپ SLM کو کوانٹائزڈ ONNX فارمیٹ میں تبدیل کریں۔ ماڈل کنورژن کا طریقہ بہت آسان ہے۔

**Microsoft Olive SDK انسٹال کریں**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX سپورٹ کو تبدیل کریں**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***نوٹ*** یہ مثال CPU استعمال کرتی ہے


### **ONNX Runtime GenAI کے ساتھ Phi-4-mini ONNX ماڈل کی انفرنس**

- **ONNX Runtime GenAI انسٹال کریں**

```bash

pip install --pre onnxruntime-genai

```

- **پائتھن کوڈ**

*یہ ONNX Runtime GenAI ورژن 0.5.2 ہے*

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


*یہ ONNX Runtime GenAI ورژن 0.6.0 ہے*

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

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔