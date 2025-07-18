<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-07-17T03:16:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "mr"
}
-->
# **Phi-4-mini ONNX सोबत संवाद करा**

***ONNX*** हा मशीन लर्निंग मॉडेल्स सादर करण्यासाठी तयार केलेला एक खुला फॉरमॅट आहे. ONNX सामान्य ऑपरेटर सेट परिभाषित करतो - जे मशीन लर्निंग आणि डीप लर्निंग मॉडेल्सचे मूलभूत घटक आहेत - आणि एक सामान्य फाइल फॉरमॅट देखील देतो ज्यामुळे AI विकसक विविध फ्रेमवर्क्स, टूल्स, रनटाइम्स आणि कंपाइलर्ससह मॉडेल्स वापरू शकतात.

आम्हाला जनरेटिव्ह AI मॉडेल्स एज डिव्हाइसेसवर तैनात करायचे आहेत आणि मर्यादित संगणकीय शक्ती किंवा ऑफलाइन वातावरणात वापरायचे आहेत. आता आपण हे उद्दिष्ट क्वांटाइज्ड पद्धतीने मॉडेल रूपांतरित करून साध्य करू शकतो. आपण क्वांटाइज्ड मॉडेल GGUF किंवा ONNX फॉरमॅटमध्ये रूपांतरित करू शकतो.

Microsoft Olive तुम्हाला SLM ला क्वांटाइज्ड ONNX फॉरमॅटमध्ये रूपांतरित करण्यात मदत करू शकतो. मॉडेल रूपांतर करण्याची पद्धत खूप सोपी आहे

**Microsoft Olive SDK इंस्टॉल करा**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX सपोर्ट रूपांतरित करा**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***टीप*** या उदाहरणात CPU वापरले आहे


### **ONNX Runtime GenAI सह Phi-4-mini ONNX मॉडेलचे इन्फरन्स करा**

- **ONNX Runtime GenAI इंस्टॉल करा**

```bash

pip install --pre onnxruntime-genai

```

- **Python कोड**

*हे ONNX Runtime GenAI 0.5.2 आवृत्ती आहे*

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


*हे ONNX Runtime GenAI 0.6.0 आवृत्ती आहे*

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

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.