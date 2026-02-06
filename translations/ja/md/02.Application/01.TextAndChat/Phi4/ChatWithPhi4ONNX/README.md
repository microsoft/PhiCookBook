# **Phi-4-mini ONNXとのチャット**

***ONNX*** は機械学習モデルを表現するために作られたオープンフォーマットです。ONNXは、機械学習や深層学習モデルの基本要素である共通の演算子セットと、さまざまなフレームワーク、ツール、ランタイム、コンパイラでモデルを利用できるようにする共通のファイル形式を定義しています。

ジェネレーティブAIモデルをエッジデバイスに展開し、限られた計算リソースやオフライン環境で利用することを目指しています。現在、この目標はモデルを量子化して変換することで達成可能です。量子化されたモデルはGGUFまたはONNX形式に変換できます。

Microsoft OliveはSLMを量子化されたONNX形式に変換するのを支援します。モデル変換を実現する方法は非常にシンプルです。

**Microsoft Olive SDKのインストール**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNXサポートへの変換**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** この例はCPUを使用しています


### **ONNX Runtime GenAIでPhi-4-mini ONNXモデルを推論する**

- **ONNX Runtime GenAIのインストール**

```bash

pip install --pre onnxruntime-genai

```

- **Pythonコード**

*これはONNX Runtime GenAI 0.5.2バージョンです*

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


*これはONNX Runtime GenAI 0.6.0バージョンです*

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

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。