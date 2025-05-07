<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-05-07T11:12:54+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "ar"
}
-->
# **الدردشة مع Phi-4-mini ONNX**

***ONNX*** هو تنسيق مفتوح تم إنشاؤه لتمثيل نماذج تعلم الآلة. يحدد ONNX مجموعة مشتركة من المشغلين - وهي اللبنات الأساسية لنماذج تعلم الآلة والتعلم العميق - وتنسيق ملف مشترك لتمكين مطوري الذكاء الاصطناعي من استخدام النماذج مع مجموعة متنوعة من الأُطُر، الأدوات، بيئات التشغيل، والمترجمات.

نأمل في نشر نماذج الذكاء الاصطناعي التوليدية على الأجهزة الطرفية واستخدامها في بيئات ذات قدرة حوسبة محدودة أو بدون اتصال بالإنترنت. يمكننا الآن تحقيق هذا الهدف عن طريق تحويل النموذج بطريقة كمية. يمكننا تحويل النموذج الكمي إلى تنسيق GGUF أو ONNX.

يمكن لـ Microsoft Olive مساعدتك في تحويل SLM إلى تنسيق ONNX كمي. الطريقة لتحقيق تحويل النموذج بسيطة جدًا.

**تثبيت Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**دعم تحويل ONNX لوحدة المعالجة المركزية**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***ملاحظة*** يستخدم هذا المثال وحدة المعالجة المركزية


### **تشغيل نموذج Phi-4-mini ONNX باستخدام ONNX Runtime GenAI**

- **تثبيت ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **كود بايثون**

*هذا هو إصدار ONNX Runtime GenAI 0.5.2*

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


*هذا هو إصدار ONNX Runtime GenAI 0.6.0*

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

**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.