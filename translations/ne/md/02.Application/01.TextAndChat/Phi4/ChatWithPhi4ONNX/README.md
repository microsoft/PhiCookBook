<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-05-09T19:01:17+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "ne"
}
-->
# **Phi-4-mini ONNX सँग कुराकानी**

***ONNX*** एउटा खुला ढाँचा हो जुन मेसिन लर्निङ मोडेलहरू प्रतिनिधित्व गर्न बनाइएको हो। ONNX ले सामान्य अपरेटरहरूको सेट परिभाषित गर्दछ - जुन मेसिन लर्निङ र डीप लर्निङ मोडेलहरूको आधारभूत ईकाइहरू हुन् - र एउटा साझा फाइल ढाँचा प्रदान गर्छ जसले AI विकासकर्ताहरूलाई विभिन्न फ्रेमवर्क, उपकरण, रनटाइम, र कम्पाइलरहरूसँग मोडेलहरू प्रयोग गर्न सक्षम बनाउँछ।

हामी जेनेरेटिभ AI मोडेलहरूलाई एज उपकरणहरूमा तैनाथ गर्न र सीमित कम्प्युटिङ शक्ति वा अफलाइन वातावरणमा प्रयोग गर्न चाहन्छौं। अब हामी यो लक्ष्य क्वान्टाइज गरिएको तरिकाले मोडेल रूपान्तरण गरेर प्राप्त गर्न सक्छौं। हामी क्वान्टाइज गरिएको मोडेललाई GGUF वा ONNX ढाँचामा रूपान्तरण गर्न सक्छौं।

Microsoft Olive ले तपाईंलाई SLM लाई क्वान्टाइज गरिएको ONNX ढाँचामा रूपान्तरण गर्न मद्दत गर्न सक्छ। मोडेल रूपान्तरण प्राप्त गर्ने तरिका धेरै सरल छ

**Microsoft Olive SDK स्थापना गर्नुहोस्**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX समर्थन रूपान्तरण गर्नुहोस्**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** यो उदाहरण CPU प्रयोग गर्दछ


### **ONNX Runtime GenAI सँग Phi-4-mini ONNX मोडेल इन्फरेन्स गर्नुहोस्**

- **ONNX Runtime GenAI स्थापना गर्नुहोस्**

```bash

pip install --pre onnxruntime-genai

```

- **Python कोड**

*यो ONNX Runtime GenAI 0.5.2 संस्करण हो*

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


*यो ONNX Runtime GenAI 0.6.0 संस्करण हो*

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
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज़लाई यसको मूल भाषामा नै आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।