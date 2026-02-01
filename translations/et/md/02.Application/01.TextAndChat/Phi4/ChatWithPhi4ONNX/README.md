# **Vestlus Phi-4-mini ONNX-iga**

***ONNX*** on avatud formaat, mis on loodud masinõppe mudelite esitamiseks. ONNX määratleb ühise komplekti operaatoreid - masinõppe ja süvaõppe mudelite ehituskive - ning ühise failivormingu, et võimaldada AI arendajatel kasutada mudeleid erinevate raamistikude, tööriistade, käituskeskkondade ja kompilaatoritega.

Meie eesmärk on juurutada generatiivseid AI-mudeleid servaseadmetel ja kasutada neid piiratud arvutusvõimsuse või võrguühenduseta keskkondades. Nüüd saame selle eesmärgi saavutada, muutes mudeli kvantiseeritud kujul. Kvantiseeritud mudeli saab teisendada GGUF või ONNX formaati.

Microsoft Olive aitab teil SLM-i kvantiseeritud ONNX formaati teisendada. Mudeli teisendamise meetod on väga lihtne.

**Paigaldage Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Teisendage CPU ONNX tugi**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Märkus*** see näide kasutab CPU-d

### **Inference Phi-4-mini ONNX mudel ONNX Runtime GenAI-ga**

- **Paigaldage ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python kood**

*See on ONNX Runtime GenAI versioon 0.5.2*

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


*See on ONNX Runtime GenAI versioon 0.6.0*

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

**Vastutusest loobumine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tulemusena.