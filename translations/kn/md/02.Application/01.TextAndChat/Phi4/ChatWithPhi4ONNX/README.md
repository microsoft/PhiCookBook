<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-12-21T21:49:56+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "kn"
}
-->
# **Phi-4-mini ONNX ಜೊತೆಗೆ ಚಾಟ್**

***ONNX*** ಎಂಬುದು ಯಂತ್ರಶಿಕ್ಷಣ ಮಾದರಿಗಳನ್ನು ಪ್ರತಿನಿಧಿಸಲು ನಿರ್ಮಿಸಲಾದ ಓಪನ್ ಫಾರ್ಮ್ಯಾಟ್ ಆಗಿದೆ. ONNX ಸಾಮಾನ್ಯ ಆಪರೇಟರ್‌ಗಳ ಸಮೂಹವನ್ನು — ಯಂತ್ರಶಿಕ್ಷಣ ಮತ್ತು ಡೀಪ್ ಲರ್ನಿಂಗ್ ಮಾದರಿಗಳ ನಿರ್ಮಾಣ ಘಟಕಗಳು — ಮತ್ತು ವಿಭಿನ್ನ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು, ಟೂಲ್ಗಳು, ರನ್‌ಟೈಮ್‌ಗಳು ಮತ್ತು ಕಂಪೈಲರ್‌ಗಳೊಂದಿಗೆ AI ಡೆವಲಪರ್‌ಗಳು ಮಾದರಿಗಳನ್ನು ಬಳಸಲು ಸಾಧ್ಯವಾಗಿಸುವ ಸಾಮಾನ್ಯ ಫೈಲ್ ಫಾರ್ಮ್ಯಾಟ್ ಅನ್ನು ಒದಗಿಸುತ್ತದೆ. 

ನಾವು ಜನರೇಟಿವ್ AI ಮಾದರಿಗಳನ್ನು ಎಡ್ಜ್ ಸಾಧನಗಳಲ್ಲಿ ನಿಯೋಜಿಸಿ ಕಡಿಮೆ ಗಣನಶಕ್ತಿ ಅಥವಾ ಆಫ್‌ಲೈನ್ ಪರಿಸರಗಳಲ್ಲಿ ಬಳಸಲು ಆಶಿಸುತ್ತೇವೆ. ಈಗ ನಾವು ಈ ಗುರಿಯನ್ನು ಮಾದರಿಯನ್ನು ಕ್ವಾಂಟೈಜ್ಡ್ (quantized) ರೀತಿಯಲ್ಲಿ ಪರಿವರ್ತಿಸುವ ಮೂಲಕ ಸಾಧಿಸಬಹುದು. ನಾವು ಕ್ವಾಂಟೈಜ್ಡ್ ಮಾದರಿಯನ್ನು GGUF ಅಥವಾ ONNX ಫಾರ್ಮ್ಯಟ್‌ಗೆ ಪರಿವರ್ತಿಸಬಹುದು.

Microsoft Olive ನಿಮಗೆ SLM ಅನ್ನು ಕ್ವಾಂಟೈಜ್ಡ್ ONNX ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸಲು ಸಹಾಯ ಮಾಡಬಹುದು. ಮಾದರಿ ಪರಿವರ್ತನೆ ಸಾಧಿಸುವ ವಿಧಾನ ಬಹಳ ಸರಳವಾಗಿದೆ

**Microsoft Olive SDK ಅನ್ನು ಸ್ಥಾಪಿಸಿ**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX ಬೆಂಬಲಕ್ಕೆ ಪರಿವರ್ತಿಸಿ**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***ಗಮನಿಸಿ*** ಈ ಉದಾಹರಣೆ CPU ಅನ್ನು ಬಳಸುತ್ತದೆ


### **ONNX Runtime GenAI ಮೂಲಕ Phi-4-mini ONNX ಮಾದರಿಯನ್ನು ಇನ್ಫಾರೆನ್ಸ್ ಮಾಡುವುದು**

- **ONNX Runtime GenAI ಅನ್ನು ಸ್ಥಾಪಿಸಿ**

```bash

pip install --pre onnxruntime-genai

```

- **Python ಕೋಡ್**

*ಇದು ONNX Runtime GenAI 0.5.2 ಆವೃತ್ತಿಯಾಗಿದೆ*

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


*ಇದು ONNX Runtime GenAI 0.6.0 ಆವೃತ್ತಿಯಾಗಿದೆ*

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
      # tokenizer_stream.decode(new_token) ಅನ್ನು ಮುದ್ರಿಸಿ, end='' ಮತ್ತು flush=True
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಾಖಲೆಯನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿಕೊಂಡು ಅನುವದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಗೆ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ ಸಹ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತಿ ವಿವರಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನದಲ್ಲಿಡಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆ ಅನ್ನು ಅಧಿಕಾರಪ್ರದ ಮೂಲ ಎಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಣೆಗಳು ಅಥವಾ ತಪ್ಪುವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->