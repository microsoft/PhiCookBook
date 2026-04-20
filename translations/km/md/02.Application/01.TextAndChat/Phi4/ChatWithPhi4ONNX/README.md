# **សន្ទនាជាមួយ Phi-4-mini ONNX**

***ONNX*** គឺជាទ្រង์ទ្រាយ​បើក​មួយ​ដែលបង្កើតឡើងដើម្បីតំណាងឱ្យ​មូឌែល​រៀន​ម៉ាស៊ីន។ ONNX កំណត់សំណុំព័ន្ធនៃប្រតិបត្តិការ - ជាផ្នែកសង់សម្រាប់មូឌែល​រៀន​ម៉ាស៊ីន និងមូឌែល​រៀន​ជ្រៅ - និងទ្រង់ទ្រាយឯកសារសាមញ្ញមួយ ដើម្បីអនុញ្ញាតឱ្យអ្នកអភិវឌ្ឍ AI អាចប្រើមូឌែលជាមួយស៊ុម (frameworks), ឧបករណ៍, runtimes, និង compilers ផ្សេងៗ។

យើងសង្ឃឹមថានឹងអាចផ្ទុកមូឌែល AI បង្កើតលើឧបករណ៍ភីរុញ (edge devices) និងប្រើវានៅក្នុងបរិយាកាសដែលមានថាមពលគណនា​កំណត់ ឬក្រៅបណ្ដាញ។ ឥឡូវនេះយើងអាចសម្រេចគោលដៅនេះដោយបំលែងមូឌែលនៅក្នុងរបៀបបរិមាណ (quantized)។ យើងអាចបំលែងមូឌែលដែលបានបរិមាណទៅជា​ទ្រង់ទ្រាយ GGUF ឬ ONNX។

Microsoft Olive អាចជួយអ្នកបំលែង SLM ទៅជាទ្រង់ទ្រាយ ONNX ដែលបានបរិមាណ។ វិធីសាស្រ្តដើម្បីសម្រេចការបំលែងមូឌែលនេះគឺសាមញ្ញណាស់

**ដំឡើង Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**បំលែងការគាំទ្រ ONNX សម្រាប់ CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***សម្គាល់***ឧទាហរណ៍នេះប្រើ CPU


### **ការធ្វើអ៊ីនភឺរ៉ែនស៍ (Inference) នៃមូឌែល Phi-4-mini ONNX ជាមួយ ONNX Runtime GenAI**

- **ដំឡើង ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **កូដ Python**

*នេះគឺជាកំណែ ONNX Runtime GenAI 0.5.2*

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


*នេះគឺជាកំណែ ONNX Runtime GenAI 0.6.0*

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
      # បោះពុម្ពលទ្ធផលពី tokenizer_stream.decode(new_token) ដោយកំណត់ end='' និង flush=True
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈពេលយើងខិតខំដើម្បីឲ្យបានភាពត្រឹមត្រូវ សូមចំណាំថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬមានភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាដើមគួរត្រូវបានគេចាត់ទុកជាឯកសារយោងដែលមានសុពលភាព។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមណែនាំឲ្យប្រើការបកប្រែដោយអ្នកបកប្រែវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->