<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-07-17T03:16:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "bn"
}
-->
# **Phi-4-mini ONNX এর সাথে চ্যাট করুন**

***ONNX*** হলো একটি ওপেন ফরম্যাট যা মেশিন লার্নিং মডেলগুলো উপস্থাপনের জন্য তৈরি। ONNX একটি সাধারণ অপারেটর সেট নির্ধারণ করে — যা মেশিন লার্নিং এবং ডিপ লার্নিং মডেলের মূল উপাদান — এবং একটি সাধারণ ফাইল ফরম্যাট প্রদান করে যাতে AI ডেভেলপাররা বিভিন্ন ফ্রেমওয়ার্ক, টুল, রানটাইম এবং কম্পাইলারের সাথে মডেল ব্যবহার করতে পারেন।

আমরা আশা করি জেনারেটিভ AI মডেলগুলোকে এজ ডিভাইসে ডিপ্লয় করতে এবং সীমিত কম্পিউটিং ক্ষমতা বা অফলাইন পরিবেশে ব্যবহার করতে পারব। এখন আমরা এই লক্ষ্য অর্জন করতে পারি মডেলকে কোয়ান্টাইজড পদ্ধতিতে রূপান্তর করে। আমরা কোয়ান্টাইজড মডেলকে GGUF বা ONNX ফরম্যাটে রূপান্তর করতে পারি।

Microsoft Olive আপনাকে SLM থেকে কোয়ান্টাইজড ONNX ফরম্যাটে রূপান্তর করতে সাহায্য করতে পারে। মডেল রূপান্তরের পদ্ধতি খুবই সহজ।

**Microsoft Olive SDK ইনস্টল করুন**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX সাপোর্ট রূপান্তর করুন**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** এই উদাহরণে CPU ব্যবহার করা হয়েছে


### **ONNX Runtime GenAI দিয়ে Phi-4-mini ONNX মডেল ইনফারেন্স করুন**

- **ONNX Runtime GenAI ইনস্টল করুন**

```bash

pip install --pre onnxruntime-genai

```

- **Python কোড**

*এটি ONNX Runtime GenAI 0.5.2 ভার্সন*

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


*এটি ONNX Runtime GenAI 0.6.0 ভার্সন*

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

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।