<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-09-12T14:28:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "lt"
}
-->
# **Pokalbis su Phi-4-mini ONNX**

***ONNX*** yra atviras formatas, sukurtas mašininio mokymosi modeliams atvaizduoti. ONNX apibrėžia bendrą operatorių rinkinį – mašininio mokymosi ir giluminio mokymosi modelių pagrindinius elementus – ir bendrą failo formatą, leidžiantį AI kūrėjams naudoti modelius su įvairiomis sistemomis, įrankiais, vykdymo aplinkomis ir kompiliatoriais.

Tikimės diegti generatyvinius AI modelius kraštiniuose įrenginiuose ir naudoti juos ribotos skaičiavimo galios arba neprisijungus veikiančiose aplinkose. Dabar šį tikslą galime pasiekti konvertuodami modelį į kvantizuotą formatą. Kvantizuotą modelį galime konvertuoti į GGUF arba ONNX formatą.

Microsoft Olive gali padėti jums konvertuoti SLM į kvantizuotą ONNX formatą. Modelio konvertavimo metodas yra labai paprastas.

**Įdiekite Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Konvertuokite CPU ONNX palaikymą**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Pastaba*** šiame pavyzdyje naudojamas CPU.

### **Phi-4-mini ONNX modelio įžvalga su ONNX Runtime GenAI**

- **Įdiekite ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python kodas**

*Tai yra ONNX Runtime GenAI 0.5.2 versija*

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

*Tai yra ONNX Runtime GenAI 0.6.0 versija*

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

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.