# **Trò chuyện với Phi-4-mini ONNX**

***ONNX*** là một định dạng mở được xây dựng để biểu diễn các mô hình học máy. ONNX định nghĩa một tập hợp các toán tử chung - những thành phần cơ bản của các mô hình học máy và học sâu - cùng với một định dạng tệp chung giúp các nhà phát triển AI có thể sử dụng mô hình với nhiều framework, công cụ, runtime và trình biên dịch khác nhau.

Chúng tôi hy vọng sẽ triển khai các mô hình AI sinh tạo trên các thiết bị biên và sử dụng chúng trong môi trường có hạn chế về sức mạnh tính toán hoặc khi không có kết nối mạng. Giờ đây, chúng ta có thể đạt được mục tiêu này bằng cách chuyển đổi mô hình theo cách lượng tử hóa. Chúng ta có thể chuyển đổi mô hình đã lượng tử hóa sang định dạng GGUF hoặc ONNX.

Microsoft Olive có thể giúp bạn chuyển đổi SLM sang định dạng ONNX đã lượng tử hóa. Phương pháp để thực hiện chuyển đổi mô hình rất đơn giản

**Cài đặt Microsoft Olive SDK**


```bash

pip install olive-ai

pip install transformers

```

**Chuyển đổi hỗ trợ ONNX trên CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Lưu ý*** ví dụ này sử dụng CPU


### **Suy luận mô hình Phi-4-mini ONNX với ONNX Runtime GenAI**

- **Cài đặt ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Mã Python**

*Đây là phiên bản ONNX Runtime GenAI 0.5.2*

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


*Đây là phiên bản ONNX Runtime GenAI 0.6.0*

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

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.