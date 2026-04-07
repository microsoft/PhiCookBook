# **ការសន្ទនាជាមួយ Phi-4-mini ONNX**

***ONNX*** គឺជារូបមន្តបើកដែលបានបង្កើតឡើងដើម្បីតំណាងឱ្យម៉ូដែលរៀនម៉ាស៊ីន។ ONNX កំណត់សំណុំបង្ហាញផ្គាប់អេតមកមួយដែលជាគ្រឿងបង្កើតនៃម៉ូដែលរៀនម៉ាស៊ីន និងរៀនជម្រៅ - និងរូបមន្តឯកសារ សំរាប់ឲ្យអ្នកអwickក្ខរការបញ្ញាសិប្បនិម្មិត អាចប្រើម៉ូដែលជាមួយបរិស្ថាន កម្មវិធីម៉ាស៊ីន សកម្មភាព និងកូដបញ្ចូលជាផ្សេងៗ។

យើងសង្ឃឹមថានឹងដាក់ម៉ូដែល AI បង្កើតនៅលើឧបករណ៍ចំណុចដែក និងប្រើវានៅក្នុងថាមពលកុំព្យូទ័រដែលមានកំណត់ ឬបរិយាកាសតំណក់ត្រង់។ ឥឡូវនេះយើងអាចសម្រេចគោលដៅនេះដោយបម្លែងម៉ូដែលក្នុងវិធីកំណត់ម៉ោង។ យើងអាចបម្លែងម៉ូដែលដែលបានកំណត់ម៉ោងទៅជាទ្រង់ទ្រង់ GGUF ឬ ONNX ។

Microsoft Olive អាចជួយអ្នកបម្លែង SLM ទៅបម្លែង ONNX ដែលបានកំណត់ម៉ោង។ វិធីសាស្ត្រដើម្បីសម្រេចការបម្លែងម៉ូដែលមិនស្មុគស្មាញទេ

**ដំឡើង Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**គាំទ្រ ONNX CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***ចំណាំ*** ឧទាហរណ៍នេះប្រើ CPU


### **វាយតម្លៃម៉ូដែល Phi-4-mini ONNX ជាមួយ ONNX Runtime GenAI**

- **ដំឡើង ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **កូដ Python**

*នេះជាវិធីសាស្ត្រ ONNX Runtime GenAI កំណែ 0.5.2*

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


*នេះជាវិធីសាស្ត្រ ONNX Runtime GenAI កំណែ 0.6.0*

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
      # បោះពុម្ព(tokenizer_stream.decode(new_token), end='', flush=True)
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ក្នុងខណៈពេលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិនោះអាចមានកំហុសឬភាពមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានយកចំពោះជាឯកសារយោងដោយផ្លូវការជាមូលដ្ឋាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសប្រក្រតីដែលកើតចេញពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->