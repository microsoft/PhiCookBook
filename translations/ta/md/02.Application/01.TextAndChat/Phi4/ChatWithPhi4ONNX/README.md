<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-10-11T12:11:06+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "ta"
}
-->
# **Phi-4-mini ONNX உடன் உரையாடல்**

***ONNX*** என்பது இயந்திரக் கற்றல் மாதிரிகளை பிரதிநிதித்துவப்படுத்த உருவாக்கப்பட்ட ஒரு திறந்த வடிவமாகும். ONNX இயந்திரக் கற்றல் மற்றும் ஆழமான கற்றல் மாதிரிகளின் கட்டமைப்புகளான பொதுவான செயல்பாடுகளின் தொகுப்பை வரையறுக்கிறது - மற்றும் AI டெவலப்பர்கள் பல்வேறு கட்டமைப்புகள், கருவிகள், ரன்டைம்கள் மற்றும் கம்பைலர்களுடன் மாதிரிகளைப் பயன்படுத்த ஒரு பொதுவான கோப்பு வடிவத்தை வழங்குகிறது.

நாங்கள் ஜெனரேட்டிவ் AI மாதிரிகளை எட்ஜ் சாதனங்களில் பிரயோகிக்கவும், குறைந்த கணினி சக்தி அல்லது ஆஃப்லைன் சூழல்களில் பயன்படுத்தவும் நம்புகிறோம். இப்போது மாதிரியை ஒரு குவாண்டைஸ் செய்யப்பட்ட முறையில் மாற்றுவதன் மூலம் இந்த இலக்கை அடையலாம். குவாண்டைஸ் செய்யப்பட்ட மாதிரியை GGUF அல்லது ONNX வடிவத்திற்கு மாற்றலாம்.

Microsoft Olive உங்களை SLM ஐ குவாண்டைஸ் செய்யப்பட்ட ONNX வடிவத்திற்கு மாற்ற உதவுகிறது. மாதிரி மாற்றத்தை அடையும் முறை மிகவும் எளிமையானது.

**Microsoft Olive SDK ஐ நிறுவவும்**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX ஆதரவை மாற்றவும்**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***குறிப்பு*** இந்த எடுத்துக்காட்டு CPU ஐ பயன்படுத்துகிறது

### **ONNX Runtime GenAI உடன் Phi-4-mini ONNX மாதிரியை முன்னறிவிப்பு செய்யவும்**

- **ONNX Runtime GenAI ஐ நிறுவவும்**

```bash

pip install --pre onnxruntime-genai

```

- **Python குறியீடு**

*இது ONNX Runtime GenAI 0.5.2 பதிப்பு*

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


*இது ONNX Runtime GenAI 0.6.0 பதிப்பு*

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

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.