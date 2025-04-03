<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "17451c69069b49f37a5395131a61ee52",
  "translation_date": "2025-04-03T07:39:29+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi4\\ChatWithPhi4ONNX\\README.md",
  "language_code": "ur"
}
-->
# **Phi-4-mini ONNX کے ساتھ بات چیت کریں**

***ONNX*** ایک اوپن فارمیٹ ہے جو مشین لرننگ ماڈلز کی نمائندگی کے لیے بنایا گیا ہے۔ ONNX مشین لرننگ اور ڈیپ لرننگ ماڈلز کے بنیادی اجزاء کے لیے ایک عام سیٹ فراہم کرتا ہے اور ایک عام فائل فارمیٹ کی وضاحت کرتا ہے تاکہ AI ڈویلپرز مختلف فریم ورک، ٹولز، رن ٹائمز، اور کمپائلرز کے ساتھ ماڈلز استعمال کر سکیں۔

ہم امید کرتے ہیں کہ جنریٹیو AI ماڈلز کو ایج ڈیوائسز پر تعینات کریں اور انہیں محدود کمپیوٹنگ پاور یا آف لائن ماحول میں استعمال کریں۔ اب ہم اس مقصد کو ماڈل کو کوانٹائزڈ طریقے سے تبدیل کر کے حاصل کر سکتے ہیں۔ ہم کوانٹائزڈ ماڈل کو GGUF یا ONNX فارمیٹ میں تبدیل کر سکتے ہیں۔

Microsoft Olive آپ کو SLM کو کوانٹائزڈ ONNX فارمیٹ میں تبدیل کرنے میں مدد دے سکتا ہے۔ ماڈل کنورژن حاصل کرنے کا طریقہ بہت آسان ہے۔

**Microsoft Olive SDK انسٹال کریں**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX سپورٹ میں تبدیلی کریں**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***نوٹ*** یہ مثال CPU استعمال کرتی ہے۔

### **ONNX Runtime GenAI کے ساتھ Phi-4-mini ONNX ماڈل کا انفیرنس کریں**

- **ONNX Runtime GenAI انسٹال کریں**

```bash

pip install --pre onnxruntime-genai

```

- **پائتھن کوڈ**

*یہ ONNX Runtime GenAI 0.5.2 ورژن ہے*

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

*یہ ONNX Runtime GenAI 0.6.0 ورژن ہے*

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

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی پوری کوشش کرتے ہیں، براہ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔