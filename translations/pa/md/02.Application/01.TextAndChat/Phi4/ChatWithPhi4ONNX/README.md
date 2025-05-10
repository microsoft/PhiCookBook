<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-05-09T19:01:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "pa"
}
-->
# **Phi-4-mini ONNX ਨਾਲ ਗੱਲਬਾਤ**

***ONNX*** ਇੱਕ ਖੁੱਲ੍ਹਾ ਫਾਰਮੈਟ ਹੈ ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ONNX ਇੱਕ ਆਮ ਸੈੱਟ ਆਪਰੇਟਰਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ - ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਅਤੇ ਡੀਪ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਦੇ ਬਿਲਡਿੰਗ ਬਲਾਕ ਹਨ - ਅਤੇ ਇੱਕ ਆਮ ਫਾਈਲ ਫਾਰਮੈਟ ਵੀ ਜੋ AI ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਫਰੇਮਵਰਕ, ਟੂਲ, ਰਨਟਾਈਮ ਅਤੇ ਕੰਪਾਇਲਰਾਂ ਨਾਲ ਮਾਡਲਾਂ ਨੂੰ ਵਰਤਣ ਦੇ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ।

ਅਸੀਂ ਉਮੀਦ ਕਰਦੇ ਹਾਂ ਕਿ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਨੂੰ ਏਜ ਡਿਵਾਈਸز 'ਤੇ ਤਾਇਨਾਤ ਕਰਾਂਗੇ ਅਤੇ ਘੱਟ ਕੰਪਿਊਟਿੰਗ ਸ਼ਕਤੀ ਜਾਂ ਆਫਲਾਈਨ ਮਾਹੌਲ ਵਿੱਚ ਵਰਤਾਂਗੇ। ਹੁਣ ਅਸੀਂ ਇਹ ਮਕਸਦ ਮਾਡਲ ਨੂੰ ਕੁਆੰਟਾਈਜ਼ਡ ਤਰੀਕੇ ਨਾਲ ਬਦਲ ਕੇ ਹਾਸਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਅਸੀਂ ਕੁਆੰਟਾਈਜ਼ਡ ਮਾਡਲ ਨੂੰ GGUF ਜਾਂ ONNX ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲ ਸਕਦੇ ਹਾਂ।

Microsoft Olive ਤੁਹਾਡੇ ਲਈ SLM ਨੂੰ ਕੁਆੰਟਾਈਜ਼ਡ ONNX ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ। ਮਾਡਲ ਬਦਲਣ ਦਾ ਤਰੀਕਾ ਬਹੁਤ ਸਧਾਰਨ ਹੈ।

**Microsoft Olive SDK ਇੰਸਟਾਲ ਕਰੋ**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX ਸਹਾਇਤਾ ਬਦਲੋ**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***ਨੋਟ*** ਇਹ ਉਦਾਹਰਨ CPU ਵਰਤਦੀ ਹੈ


### **ONNX Runtime GenAI ਨਾਲ Phi-4-mini ONNX ਮਾਡਲ ਦੀ ਇਨਫਰੈਂਸ ਕਰੋ**

- **ONNX Runtime GenAI ਇੰਸਟਾਲ ਕਰੋ**

```bash

pip install --pre onnxruntime-genai

```

- **Python ਕੋਡ**

*ਇਹ ONNX Runtime GenAI ਦਾ 0.5.2 ਵਰਜ਼ਨ ਹੈ*

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


*ਇਹ ONNX Runtime GenAI ਦਾ 0.6.0 ਵਰਜ਼ਨ ਹੈ*

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

**ਅਸਵੀਕਾਰੋਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਸਮਝਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।