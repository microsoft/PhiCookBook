<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:49:04+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "en"
}
-->
# **Using Microsoft Phi-3.5 tflite to create Android app**

This is an Android sample using Microsoft Phi-3.5 tflite models.

## **📚 Knowledge**

Android LLM Inference API allows you to run large language models (LLMs) entirely on-device for Android apps. You can use it to perform a variety of tasks such as generating text, retrieving information in natural language, and summarizing documents. The API supports multiple text-to-text large language models out of the box, enabling you to integrate the latest on-device generative AI models into your Android applications.

Google AI Edge Torch is a Python library that supports converting PyTorch models into the .tflite format, which can then be executed with TensorFlow Lite and MediaPipe. This makes it possible to build Android, iOS, and IoT applications that run models fully on-device. AI Edge Torch offers extensive CPU support, with initial GPU and NPU compatibility. It aims to integrate closely with PyTorch by building on torch.export() and providing comprehensive coverage of Core ATen operators.

## **🪬 Guideline**

### **🔥 Convert Microsoft Phi-3.5 to tflite support**

0. This sample is for Android 14+

1. Install Python 3.10.12

***Suggestion:*** use conda to set up your Python environment

2. Ubuntu 20.04 / 22.04 (please refer to [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion:*** Use an Azure Linux VM or a third-party cloud VM to create your environment

3. Open your Linux bash and install the Python libraries

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Download Microsoft-3.5-Instruct from Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convert Microsoft Phi-3.5 to tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Convert Microsoft Phi-3.5 to Android Mediapipe Bundle**

Please install mediapipe first

```bash

pip install mediapipe

```

Run this code in [your notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Use adb to push the task model to your Android device path**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Running your Android code**

![demo](../../../../../../translated_images/en/demo.06d5a4246f057d1b.webp)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.