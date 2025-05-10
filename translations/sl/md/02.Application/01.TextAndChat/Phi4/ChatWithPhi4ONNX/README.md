<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-05-09T19:03:58+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "sl"
}
-->
# **Phi-4-mini ONNX සමඟ කතා කරන්න**

***ONNX*** යනු යන්ත්‍ර ඉගෙනුම් ආදර්ශ නියෝජනය සඳහා නිර්මාණය කළ විවෘත ආකෘතියකි. ONNX යන්ත්‍ර ඉගෙනුම් සහ ගැඹුරු ඉගෙනුම් ආදර්ශ ගොඩනැඟීමේ මූලික කොටස් වන සාමාන්‍ය මෙහෙයුම් කට්ටලයක් සහ AI සංවර්ධකයින්ට විවිධ රාමු, මෙවලම්, ධාවක සහ සංග්‍රහක සමඟ ආදර්ශ භාවිතා කිරීමට හැකි සාමාන්‍ය ගොනු ආකෘතියක් නිර්වචනය කරයි.

අපගේ අරමුණ වන්නේ ජනක AI ආදර්ශ edge උපාංගවලට යොදා ගෙන සීමිත ගණනයන බලය හෝ අන්තර්ජාලයෙන් තොර පරිසරවල භාවිතා කිරීමයි. දැන් අපට මෙය ප්‍රමාණිකරණය කළ ආකාරයෙන් ආදර්ශය පරිවර්තනය කිරීමෙන් සාර්ථක කරගත හැකිය. අපට ප්‍රමාණිකරණය කළ ආදර්ශ GGUF හෝ ONNX ආකෘතියට පරිවර්තනය කළ හැකිය.

Microsoft Olive SLM සිට ප්‍රමාණිකරණය කළ ONNX ආකෘතියට පරිවර්තනය කිරීමට ඔබට උදව් කළ හැකිය. ආදර්ශ පරිවර්තනය සිදුකිරීමේ ක්‍රමය ඉතා සරලයි.

**Microsoft Olive SDK ස්ථාපනය කරන්න**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX සහය පරිවර්තනය කරන්න**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***සටහන*** මෙම උදාහරණය CPU භාවිතා කරයි


### **ONNX Runtime GenAI සමඟ Phi-4-mini ONNX ආදර්ශය පූර්ව අනුමාන කරන්න**

- **ONNX Runtime GenAI ස්ථාපනය කරන්න**

```bash

pip install --pre onnxruntime-genai

```

- **Python කේතය**

*මෙය ONNX Runtime GenAI 0.5.2 සංස්කරණයයි*

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


*මෙය ONNX Runtime GenAI 0.6.0 සංස්කරණයයි*

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

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.