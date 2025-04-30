<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "17451c69069b49f37a5395131a61ee52",
  "translation_date": "2025-04-04T06:34:49+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi4\\ChatWithPhi4ONNX\\README.md",
  "language_code": "tw"
}
-->
# **與 Phi-4-mini ONNX 聊天**

***ONNX*** 是一種開放格式，用於表示機器學習模型。ONNX 定義了一組通用的運算符——機器學習和深度學習模型的基本構建模塊，以及一種通用的文件格式，幫助 AI 開發者使用多種框架、工具、運行時和編譯器來運行模型。

我們希望能將生成式 AI 模型部署到邊緣設備上，並在有限的計算能力或離線環境中使用。現在，透過量化方式轉換模型，我們可以實現這個目標。我們能將量化後的模型轉換為 GGUF 或 ONNX 格式。

Microsoft Olive 可以幫助你將 SLM 轉換為量化的 ONNX 格式。實現模型轉換的方法非常簡單。

**安裝 Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**轉換為支援 CPU 的 ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***注意*** 此範例使用 CPU

### **使用 ONNX Runtime GenAI 推理 Phi-4-mini ONNX 模型**

- **安裝 ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python 程式碼**

*這是 ONNX Runtime GenAI 0.5.2 版本*

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

*這是 ONNX Runtime GenAI 0.6.0 版本*

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

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。