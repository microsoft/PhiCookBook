<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-12-21T21:45:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "pcm"
}
-->
# **Chop tori wit Phi-4-mini ONNX**

***ONNX*** na open format wey dem build to represent machine learning models. ONNX dey define a common set of operators - di building blocks of machine learning and deep learning models - and a common file format wey enable AI developers make dem fit use models wit different frameworks, tools, runtimes, and compilers. 

We dey hope to deploy generative AI models for edge devices an use dem for limited computing power or offline environments. Now we fit achieve dis goal by converting di model in a quantized way. We fit convert di quantized model to GGUF or ONNX format.

Microsoft Olive fit help you convert SLM to quantized ONNX format. Di method to achieve model conversion dey very simple

**Install Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**Convert CPU ONNX Support**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** dis example dey use CPU


### **How to run inference for Phi-4-mini ONNX model wit ONNX Runtime GenAI**

- **Install ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python Code**

*Dis na ONNX Runtime GenAI 0.5.2 version*

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


*Dis na ONNX Runtime GenAI 0.6.0 version*

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
      # Print di decoded new_token from tokenizer_stream, no new line at di end, an make am flush immediately.
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate by AI translation service Co‑op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make everything correct, make you sabi say machine/automatic translations fit get mistakes or wrong tins. The original document for im own language suppose be di official/authoritative source. For critical information, e better make you use professional human translator. We no dey liable for any misunderstanding or wrong interpretation wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->