<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:50:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "cs"
}
-->
# **Using Microsoft Phi-3.5 tflite to create Android app**

This is an Android example using Microsoft Phi-3.5 tflite models.

## **📚 Knowledge**

Android LLM Inference API allows you to run large language models (LLMs) fully on-device for Android apps, enabling a variety of tasks such as generating text, retrieving information in natural language, and summarizing documents. The API supports multiple text-to-text large language models out of the box, so you can integrate the latest on-device generative AI models into your Android applications.

Googld AI Edge Torch is a Python library that supports converting PyTorch models into a .tflite format, which can then be executed with TensorFlow Lite and MediaPipe. This makes it possible to build Android, iOS, and IoT apps that run models entirely on-device. AI Edge Torch offers extensive CPU support, with initial GPU and NPU capabilities. It aims for tight integration with PyTorch by building on torch.export() and providing comprehensive coverage of Core ATen operators.

## **🪬 Guideline**

### **🔥 Convert Microsoft Phi-3.5 to tflite support**

0. This sample targets Android 14+

1. Install Python 3.10.12

***Suggestion:*** use conda to set up your Python environment

2. Ubuntu 20.04 / 22.04 (focus on [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion:*** Use Azure Linux VM or a third-party cloud VM to create your environment

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

### **🔥 Use adb push to transfer the task model to your Android device path**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Running your Android code**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.cs.png)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.