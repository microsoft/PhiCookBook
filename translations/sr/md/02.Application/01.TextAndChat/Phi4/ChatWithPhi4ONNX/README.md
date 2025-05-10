<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-05-09T19:03:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "sr"
}
-->
# **Ćaskaj sa Phi-4-mini ONNX**

***ONNX*** je otvoreni format napravljen za predstavljanje modela mašinskog učenja. ONNX definiše zajednički skup operatora - osnovnih elemenata modela mašinskog i dubokog učenja - i zajednički format fajla koji omogućava AI programerima da koriste modele sa različitim framework-ovima, alatima, runtime-ovima i kompajlerima.

Nadamo se da ćemo moći da pokrenemo generativne AI modele na edge uređajima i koristimo ih u okruženjima sa ograničenom računalnom snagom ili offline. Sada možemo postići ovaj cilj konvertovanjem modela na kvantizovan način. Kvantizovani model možemo konvertovati u GGUF ili ONNX format.

Microsoft Olive može pomoći da konvertujete SLM u kvantizovani ONNX format. Metod za konverziju modela je veoma jednostavan

**Instalirajte Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**Konvertujte CPU ONNX podršku**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Napomena*** ovaj primer koristi CPU


### **Izvedite inferencu Phi-4-mini ONNX modela sa ONNX Runtime GenAI**

- **Instalirajte ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python kod**

*Ovo je ONNX Runtime GenAI verzija 0.5.2*

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


*Ovo je ONNX Runtime GenAI verzija 0.6.0*

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

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било какве неспоразуме или погрешна тумачења настала употребом овог превода.