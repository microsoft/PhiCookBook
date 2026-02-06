# **Phi-4-mini ONNX తో చాట్**

***ONNX*** ఒక ఓపెన్ ఫార్మాట్, ఇది మెషిన్ లెర్నింగ్ మోడల్స్‌ను ప్రతిబింబించేందుకు రూపొందించబడింది. ONNX సాధారణ ఆపరేటర్ల సమూహాన్ని నిర్వచిస్తుంది - ఇవి మెషిన్ లెర్నింగ్ మరియు డీప్ లెర్నింగ్ మోడల్స్‌కి నిర్మాణ ఖండాలు - అలాగే వివిధ ఫ్రేమ్‌వర్క్స్, టూల్స్, రన్‌టైమ్స్ మరియు కంపైలర్లతో మోడల్స్‌ను ఉపయోగించుకునేలా సాధారణ ఫైల్ ఫార్మాట్‌ను అందిస్తుంది. 

మేము ఉత్పత్తిజన్య AI మోడల్స్‌ను ఎడ్జ్ డివైసుల్లో డిప్లాయ్ చేసి పరిమిత కంప్యూటింగ్ శక్తి లేదా ఆఫ్‌లైన్ వాతావరణాల్లో ఉపయోగించగలగాలని ఆశిస్తున్నాము. ఇప్పుడు మోడల్‌ను క్వాంటైజ్ చేసిన రీతిలో మార్చి ఈ లక్ష్యాన్ని సాధించవచ్చు. క్వాంటైజ్ చేసిన మోడల్‌ను GGUF లేదా ONNX ఫార్మాట్‌కు మార్చవచ్చు.

Microsoft Olive మీకు SLM ను క్వాంటైజ్ చేసిన ONNX ఫార్మాట్‌కు మార్చడంలో సహాయపడగలదు. మోడల్ మార్పిడిని సాధించే విధానం చాలా సులభం

**Microsoft Olive SDK ను ఇన్‌స్టాల్ చేయండి**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX మద్దతును మార్చండి**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***గమనిక*** ఈ ఉదాహరణ CPU ను ఉపయోగిస్తుంది


### **ONNX Runtime GenAI తో Phi-4-mini ONNX మోడల్ ఇన్ఫరెన్స్**

- **ONNX Runtime GenAI ను ఇన్‌స్టాల్ చేయండి**

```bash

pip install --pre onnxruntime-genai

```

- **Python కోడ్**

*ఈది ONNX Runtime GenAI 0.5.2 వెర్షన్*

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


*ఈది ONNX Runtime GenAI 0.6.0 వెర్షన్*

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
      # ముద్రించు(టోకనైజర్_స్ట్రీమ్.డీకోడ్(కొత్త_టోకెన్), end='', flush=True)
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
అస్పష్టం (Disclaimer):
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పుడు వివరాలు ఉండవచ్చు అని దయచేసి గమనించండి. అసలైన పత్రాన్ని దాని స్థానిక భాషలో ఉన్నదే అధికారిక మరియు ఆధారమైన మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదం చేయించుకోవడం సూచించబడుతుంది. ఈ అనువాదాన్ని ఉపయోగించినందున ఏర్పడిన ఏవైనా అవగాహనా లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడాలకో సంబంధించి మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->