<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "17451c69069b49f37a5395131a61ee52",
  "translation_date": "2025-04-04T12:47:28+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi4\\ChatWithPhi4ONNX\\README.md",
  "language_code": "ja"
}
-->
# **Phi-4-mini ONNXとチャット**

***ONNX*** は、機械学習モデルを表現するためのオープンフォーマットです。ONNXは、機械学習およびディープラーニングモデルの構成要素である共通の演算子セットと、さまざまなフレームワーク、ツール、ランタイム、コンパイラでモデルを利用できるようにする共通のファイル形式を定義しています。

私たちは生成型AIモデルをエッジデバイスで展開し、限られた計算能力やオフライン環境で使用することを目指しています。この目標は、モデルを量子化することで達成できます。量子化されたモデルをGGUFまたはONNX形式に変換することが可能です。

Microsoft Oliveを使用すると、SLMを量子化されたONNX形式に変換できます。モデル変換を実現する方法は非常に簡単です。

**Microsoft Olive SDKのインストール**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNXサポートの変換**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** この例ではCPUを使用しています。

### **ONNX Runtime GenAIを使ったPhi-4-mini ONNXモデルの推論**

- **ONNX Runtime GenAIのインストール**

```bash

pip install --pre onnxruntime-genai

```

- **Pythonコード**

*こちらはONNX Runtime GenAIバージョン0.5.2です*

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

*こちらはONNX Runtime GenAIバージョン0.6.0です*

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

**免責事項**:  
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。原文（元の言語で記載された文書）が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤訳について、当方は一切の責任を負いかねます。