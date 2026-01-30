# **الدردشة مع Phi-4-mini ONNX**

***ONNX*** هو تنسيق مفتوح مصمم لتمثيل نماذج التعلم الآلي. يحدد ONNX مجموعة مشتركة من العمليات - وهي اللبنات الأساسية لنماذج التعلم الآلي والتعلم العميق - بالإضافة إلى تنسيق ملف موحد لتمكين مطوري الذكاء الاصطناعي من استخدام النماذج مع مجموعة متنوعة من الأُطُر، الأدوات، بيئات التشغيل، والمُجمّعات.

نأمل في نشر نماذج الذكاء الاصطناعي التوليدية على الأجهزة الطرفية واستخدامها في بيئات ذات قدرة حوسبة محدودة أو بدون اتصال بالإنترنت. الآن يمكننا تحقيق هذا الهدف عن طريق تحويل النموذج بطريقة كمية. يمكننا تحويل النموذج الكمي إلى تنسيق GGUF أو ONNX.

يمكن لـ Microsoft Olive مساعدتك في تحويل SLM إلى تنسيق ONNX الكمي. طريقة تحقيق تحويل النموذج بسيطة جدًا.

**تثبيت Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**تحويل دعم ONNX لوحدة المعالجة المركزية**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***ملاحظة*** هذا المثال يستخدم وحدة المعالجة المركزية


### **استدلال نموذج Phi-4-mini ONNX باستخدام ONNX Runtime GenAI**

- **تثبيت ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **كود بايثون**

*هذه نسخة ONNX Runtime GenAI 0.5.2*

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


*هذه نسخة ONNX Runtime GenAI 0.6.0* 

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

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.