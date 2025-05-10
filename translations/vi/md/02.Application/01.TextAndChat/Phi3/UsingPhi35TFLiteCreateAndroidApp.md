<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:49:49+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "vi"
}
-->
# **Sử dụng Microsoft Phi-3.5 tflite để tạo ứng dụng Android**

Đây là một mẫu Android sử dụng các mô hình Microsoft Phi-3.5 tflite.

## **📚 Kiến thức**

Android LLM Inference API cho phép bạn chạy các mô hình ngôn ngữ lớn (LLMs) hoàn toàn trên thiết bị cho các ứng dụng Android, giúp bạn thực hiện nhiều tác vụ khác nhau như tạo văn bản, truy xuất thông tin dưới dạng ngôn ngữ tự nhiên, và tóm tắt tài liệu. Tác vụ này hỗ trợ sẵn nhiều mô hình ngôn ngữ lớn dạng text-to-text, giúp bạn áp dụng các mô hình AI sinh tạo mới nhất ngay trên thiết bị cho ứng dụng Android của mình.

Googld AI Edge Torch là thư viện python hỗ trợ chuyển đổi các mô hình PyTorch sang định dạng .tflite, sau đó có thể chạy với TensorFlow Lite và MediaPipe. Điều này giúp phát triển ứng dụng trên Android, iOS và IoT có thể chạy mô hình hoàn toàn trên thiết bị. AI Edge Torch hỗ trợ đa dạng CPU, với hỗ trợ GPU và NPU ban đầu. AI Edge Torch hướng tới tích hợp sâu với PyTorch, xây dựng dựa trên torch.export() và cung cấp hỗ trợ tốt cho các toán tử Core ATen.

## **🪬 Hướng dẫn**

### **🔥 Chuyển đổi Microsoft Phi-3.5 sang tflite**

0. Mẫu này dành cho Android 14+

1. Cài đặt Python 3.10.12

***Gợi ý:*** sử dụng conda để cài đặt môi trường Python của bạn

2. Ubuntu 20.04 / 22.04 (hãy chú ý đến [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Gợi ý:*** Sử dụng Azure Linux VM hoặc các dịch vụ đám mây bên thứ ba để tạo môi trường

3. Mở bash trên Linux, cài đặt thư viện Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Tải Microsoft-3.5-Instruct từ Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Chuyển đổi Microsoft Phi-3.5 sang tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Chuyển đổi Microsoft Phi-3.5 sang Android Mediapipe Bundle**

vui lòng cài đặt mediapipe trước

```bash

pip install mediapipe

```

chạy đoạn mã này trong [notebook của bạn](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 Dùng adb push để chuyển model tác vụ vào đường dẫn trên thiết bị Android của bạn**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Chạy mã Android của bạn**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.vi.png)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tham khảo chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.