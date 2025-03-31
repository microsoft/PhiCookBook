<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-03-27T11:25:36+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi4\\ChatWithPhi4ONNX\\README.md",
  "language_code": "ar"
}
-->
# **الدردشة مع Phi-4-mini ONNX**

***ONNX*** هو تنسيق مفتوح تم تصميمه لتمثيل نماذج التعلم الآلي. يقوم ONNX بتعريف مجموعة مشتركة من المشغلين - وهي اللبنات الأساسية لنماذج التعلم الآلي والتعلم العميق - وتنسيق ملفات موحد لتمكين مطوري الذكاء الاصطناعي من استخدام النماذج مع مجموعة متنوعة من الأطر والأدوات وبيئات التشغيل والمترجمات.

نأمل في نشر نماذج الذكاء الاصطناعي التوليدية على الأجهزة الطرفية واستخدامها في بيئات ذات قدرة حوسبة محدودة أو في وضع عدم الاتصال. يمكننا الآن تحقيق هذا الهدف من خلال تحويل النموذج بطريقة مضغوطة. يمكننا تحويل النموذج المضغوط إلى تنسيق GGUF أو ONNX.

يمكن لـ Microsoft Olive مساعدتك في تحويل SLM إلى تنسيق ONNX مضغوط. طريقة تحقيق تحويل النموذج بسيطة للغاية.

**تثبيت Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**تحويل دعم ONNX الخاص بوحدة المعالجة المركزية**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***ملاحظة*** هذا المثال يستخدم وحدة المعالجة المركزية.

### **استنتاج نموذج Phi-4-mini ONNX باستخدام ONNX Runtime GenAI**

- **تثبيت ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **كود بايثون**

*هذا الإصدار هو ONNX Runtime GenAI 0.5.2*

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

*هذا الإصدار هو ONNX Runtime GenAI 0.6.0*

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
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). على الرغم من أننا نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. بالنسبة للمعلومات الحساسة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ نتيجة استخدام هذه الترجمة.