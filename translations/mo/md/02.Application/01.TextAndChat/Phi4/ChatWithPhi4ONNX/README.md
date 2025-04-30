<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "17451c69069b49f37a5395131a61ee52",
  "translation_date": "2025-04-04T12:47:05+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi4\\ChatWithPhi4ONNX\\README.md",
  "language_code": "mo"
}
-->
# **Phi-4-mini ONNX-თან ჩატი**

***ONNX*** არის ღია ფორმატი, რომელიც შექმნილია მანქანური სწავლების მოდელების წარმოდგენისთვის. ONNX განსაზღვრავს ოპერატორების საერთო ნაკრებს - მანქანური და ღრმა სწავლების მოდელების საფუძვლებს - და საერთო ფაილის ფორმატს, რაც საშუალებას აძლევს AI დეველოპერებს გამოიყენონ მოდელები სხვადასხვა ჩარჩოებთან, ინსტრუმენტებთან, გაშვების გარემოებთან და კომპილატორებთან.

ჩვენი მიზანია, განვათავსოთ გენერაციული AI მოდელები საზღვრულ მოწყობილობებზე და გამოვიყენოთ ისინი შეზღუდული გამოთვლითი რესურსებით ან ოფლაინ გარემოში. ახლა შეგვიძლია ამ მიზნის მიღწევა მოდელის კვანტიზებული მეთოდით გარდაქმნით. კვანტიზებული მოდელის გადაყვანა შესაძლებელია GGUF ან ONNX ფორმატში.

Microsoft Olive დაგეხმარებათ SLM-ის კვანტიზებულ ONNX ფორმატში გარდაქმნაში. მოდელის გარდაქმნის მეთოდი ძალიან მარტივია.

**Microsoft Olive SDK-ის ინსტალაცია**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX მხარდაჭერის გარდაქმნა**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***შენიშვნა*** ეს მაგალითი იყენებს CPU-ს.

### **Phi-4-mini ONNX მოდელის ინფერენცია ONNX Runtime GenAI-ით**

- **ONNX Runtime GenAI-ის ინსტალაცია**

```bash

pip install --pre onnxruntime-genai

```

- **Python კოდი**

*ეს არის ONNX Runtime GenAI 0.5.2 ვერსია*

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

*ეს არის ONNX Runtime GenAI 0.6.0 ვერსია*

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

It seems like you want the text translated to "mo," but could you clarify what "mo" refers to? Are you asking for translation into Māori, Mongolian, or another language?