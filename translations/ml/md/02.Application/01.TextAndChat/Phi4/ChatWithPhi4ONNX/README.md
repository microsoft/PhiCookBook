# **Phi-4-mini ONNX-ഉടൻ ചാറ്റ്**

***ONNX*** മെഷീൻ ലേണിംഗ് മോഡലുകൾ പ്രതിനിധീകരിക്കാൻ രൂപകല്പന ചെയ്ത ഒരു തുറന്ന ഫോർമാറ്റാണ്. ONNX മെഷീൻ ലേണിങ്ങിന്റെയും ഡീപ്പ് ലേണിങ്ങിന്റെയും നിര്‍മ്മാണഘടകങ്ങളായ ഓപ്പറേറ്റർമാരുടെ പൊതുവായ ഒരു സെറ്റ് നിർവചിക്കുകയും വിവിധ ഫ്രെയിംവർക്കുകൾ, ടൂളുകൾ, റൺടൈമുകൾ, കമ്പൈലറുകൾ എന്നിവയുമായി മോഡലുകൾ ഉപയോഗിക്കാൻ സാധ്യമാക്കുന്ന ഒരു പൊതുഫയൽ ഫോർമാറ്റും നിർവചിക്കുകയും ചെയ്യുന്നു. 

ഞങ്ങൾ ജെനറേറ്റീവ് AI മോഡലുകൾ എഡ്ജ് ഉപകരണങ്ങളിൽ വിന്യසിച്ച് അപര്യാപ്തമായ കമ്പ്യൂട്ടിംഗ് ശേഷിയുള്ള അല്ലെങ്കിൽ ഓഫ്‌ലൈൻ പരിസ്ഥിതികളിൽ അവ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്നു. ഇതിലെടുപ്പം നാം മോഡൽ ക്വാൻടൈസ് ചെയ്യുന്ന രീതിയിൽ ലഭ്യമാക്കാം. ക്വാൻടൈസ്ഡ് മോഡലിനെ GGUF അല്ലെങ്കിൽ ONNX ഫോർമാറ്റിലേയ്ക്ക് പരിവർത്തനം ചെയ്യാൻ കഴിയും.

Microsoft Olive നിങ്ങൾക്ക് SLM-നെ ക്വാൻടൈസ്ഡ് ONNX ഫോർമാറ്റിലേയ്ക്ക് പരിവർത്തനം ചെയ്യാൻ സഹായിക്കും. മോഡൽ പരിവർത്തനത്തിന് ഉപയോഗിക്കുന്ന രീതി വളരെ ലളിതമാണ്

**Microsoft Olive SDK ഇൻസ്റ്റാൾ ചെയ്യുക**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX പിന്തുണ പരിവർത്തനം ചെയ്യുക**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***കുറിപ്പ്*** ഈ ഉദാഹരണം CPU ഉപയോഗിക്കുന്നു


### **ONNX Runtime GenAI ഉപയോഗിച്ച് Phi-4-mini ONNX മോഡൽ ഇൻഫറൻസ്**

- **ONNX Runtime GenAI ഇൻസ്റ്റാൾ ചെയ്യുക**

```bash

pip install --pre onnxruntime-genai

```

- **Python കോഡ്**

*ഇത് ONNX Runtime GenAI 0.5.2 പതിപ്പാണ്*

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


*ഇത് ONNX Runtime GenAI 0.6.0 പതിപ്പാണ്*

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
      # tokenizer_stream.decode(new_token) ന്റെ ഫലം end='' ആക്കി, flush=True ഉപയോഗിച്ച് പ്രിന്റ് ചെയ്യുക
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അറിയിപ്പ്:

ഈ രേഖ AI പരിഭാഷാ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷ ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് പരിശ്രമിച്ചിരുന്നാലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാവുന്നതാണ് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂല ഭാഷയിലുള്ള രേഖയെ പ്രാമാണിക ഉറവിടമായി കരുതണം. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യപരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിക്കുന്നത് മൂലം ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->