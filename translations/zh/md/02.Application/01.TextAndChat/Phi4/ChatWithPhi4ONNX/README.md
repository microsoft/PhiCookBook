<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "17451c69069b49f37a5395131a61ee52",
  "translation_date": "2025-04-03T07:40:02+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi4\\ChatWithPhi4ONNX\\README.md",
  "language_code": "zh"
}
-->
# **与 Phi-4-mini ONNX 互动**

***ONNX*** 是一种开放格式，用于表示机器学习模型。ONNX定义了一组通用的操作符——机器学习和深度学习模型的构建模块——以及一种通用的文件格式，使AI开发者能够在多种框架、工具、运行时和编译器中使用模型。

我们希望将生成式AI模型部署到边缘设备，并在有限的计算能力或离线环境中使用它们。现在，我们可以通过量化的方式转换模型来实现这一目标。量化后的模型可以转换为GGUF或ONNX格式。

Microsoft Olive可以帮助您将SLM转换为量化的ONNX格式。实现模型转换的方法非常简单。

**安装Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**转换支持CPU的ONNX模型**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***注意*** 此示例使用CPU


### **使用ONNX Runtime GenAI推理Phi-4-mini ONNX模型**

- **安装ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python代码**

*这是ONNX Runtime GenAI 0.5.2版本*

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

*这是ONNX Runtime GenAI 0.6.0版本*

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

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文件应被视为权威来源。对于关键信息，建议寻求专业人工翻译服务。我们对因使用此翻译而产生的任何误解或误读不承担责任。