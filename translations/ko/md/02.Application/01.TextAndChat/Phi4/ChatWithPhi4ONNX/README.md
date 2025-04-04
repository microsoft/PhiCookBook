<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "17451c69069b49f37a5395131a61ee52",
  "translation_date": "2025-04-04T06:35:17+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi4\\ChatWithPhi4ONNX\\README.md",
  "language_code": "ko"
}
-->
# **Phi-4-mini ONNX와 대화하기**

***ONNX***는 머신러닝 모델을 표현하기 위해 만들어진 개방형 포맷입니다. ONNX는 머신러닝 및 딥러닝 모델의 구성 요소인 공통 연산자 세트와 파일 형식을 정의하여 AI 개발자가 다양한 프레임워크, 도구, 런타임, 컴파일러를 사용해 모델을 활용할 수 있도록 합니다.

우리는 생성형 AI 모델을 엣지 디바이스에 배포하고 제한된 컴퓨팅 자원이나 오프라인 환경에서 사용할 수 있기를 희망합니다. 이제 모델을 양자화 방식으로 변환함으로써 이러한 목표를 달성할 수 있습니다. 양자화된 모델을 GGUF 또는 ONNX 형식으로 변환할 수 있습니다.

Microsoft Olive를 사용하면 SLM을 양자화된 ONNX 형식으로 변환할 수 있습니다. 모델 변환을 수행하는 방법은 매우 간단합니다.

**Microsoft Olive SDK 설치**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX 지원 변환**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** 이 예시는 CPU를 사용합니다.

### **ONNX Runtime GenAI를 사용한 Phi-4-mini ONNX 모델 추론**

- **ONNX Runtime GenAI 설치**

```bash

pip install --pre onnxruntime-genai

```

- **Python 코드**

*이 코드는 ONNX Runtime GenAI 0.5.2 버전을 사용합니다*

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

*이 코드는 ONNX Runtime GenAI 0.6.0 버전을 사용합니다*

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

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 내용이 포함될 수 있습니다. 원문(원래 언어로 작성된 문서)이 신뢰할 수 있는 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로써 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.