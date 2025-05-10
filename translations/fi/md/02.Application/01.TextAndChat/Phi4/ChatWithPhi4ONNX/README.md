<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-05-09T19:02:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "fi"
}
-->
# **Keskustele Phi-4-mini ONNX:n kanssa**

***ONNX*** on avoin formaatti, joka on suunniteltu koneoppimismallien esittämiseen. ONNX määrittelee yhteisen joukon operaattoreita – koneoppimis- ja syväoppimismallien rakennuspalikoita – sekä yhteisen tiedostomuodon, jonka avulla tekoälykehittäjät voivat käyttää malleja monenlaisissa kehyksissä, työkaluissa, suoritinympäristöissä ja kääntäjissä.

Tavoitteenamme on ottaa generatiiviset tekoälymallit käyttöön reunalaitteissa ja käyttää niitä rajallisella laskentateholla tai offline-ympäristöissä. Nyt voimme saavuttaa tämän muuntamalla mallin kvantisoidussa muodossa. Voimme muuntaa kvantisoidun mallin GGUF- tai ONNX-muotoon.

Microsoft Olive voi auttaa sinua muuntamaan SLM:n kvantisoituun ONNX-muotoon. Mallin muuntamisen menetelmä on hyvin yksinkertainen.

**Asenna Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**Muunnos CPU ONNX -tuella**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Huom*** tämä esimerkki käyttää CPU:ta


### **Phi-4-mini ONNX -mallin päätteennäyttö ONNX Runtime GenAI:lla**

- **Asenna ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python-koodi**

*Tämä on ONNX Runtime GenAI -version 0.5.2 koodi*

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


*Tämä on ONNX Runtime GenAI -version 0.6.0 koodi*

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

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on pidettävä virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.