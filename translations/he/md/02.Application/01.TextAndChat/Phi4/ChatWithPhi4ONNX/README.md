<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c98217bb3eff6c24e97b104b21632fd0",
  "translation_date": "2025-05-09T19:02:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md",
  "language_code": "he"
}
-->
# **שיחה עם Phi-4-mini ONNX**

***ONNX*** הוא פורמט פתוח שנבנה כדי לייצג מודלים של למידת מכונה. ONNX מגדיר סט משותף של אופרטורים - אבני הבניין של מודלי למידת מכונה ולמידה עמוקה - ופורמט קובץ משותף שמאפשר למפתחי AI להשתמש במודלים עם מגוון מסגרות עבודה, כלים, סביבות ריצה ומקמפלרים.

אנחנו מקווים לפרוס מודלים של AI גנרטיבי במכשירים שוליים ולהשתמש בהם בסביבות עם כוח מחשוב מוגבל או במצב לא מקוון. עכשיו אפשר להשיג מטרה זו על ידי המרת המודל בצורה מקודדת. ניתן להמיר את המודל המקודד לפורמט GGUF או ONNX.

Microsoft Olive יכול לעזור לך להמיר SLM לפורמט ONNX מקודד. השיטה להשגת המרת מודל היא פשוטה מאוד

**התקן את Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**המרת תמיכה ב-CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***הערה*** דוגמה זו משתמשת ב-CPU


### **הרצת מודל Phi-4-mini ONNX עם ONNX Runtime GenAI**

- **התקן את ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **קוד פייתון**

*זו גרסת ONNX Runtime GenAI 0.5.2*

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


*זו גרסת ONNX Runtime GenAI 0.6.0*

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

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור המוסמך. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות על כל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.