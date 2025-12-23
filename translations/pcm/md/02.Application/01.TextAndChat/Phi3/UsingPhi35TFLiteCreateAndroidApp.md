<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-12-21T21:36:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "pcm"
}
-->
# **How to use Microsoft Phi-3.5 tflite make Android app**

Na Android sample wey dey use Microsoft Phi-3.5 tflite models.

## **📚 Wetin you need sabi**

Android LLM Inference API dey allow you run large language models (LLMs) complete on-device for Android applications, wey you fit use to do plenty different tasks, like generate text, retrieve information for natural language, and summarize documents. The task get built-in support for multiple text-to-text large language models, so you fit apply the latest on-device generative AI models to your Android apps.

Googld AI Edge Torch na python library wey dey support converting PyTorch models into a .tflite format, wey you fit run with TensorFlow Lite and MediaPipe. This one enable applications for Android, iOS and IoT wey fit run models complete on-device. AI Edge Torch dey offer broad CPU coverage, with initial GPU and NPU support. AI Edge Torch dey try join well with PyTorch, build on top of torch.export() and provide good coverage of Core ATen operators.


## **🪬 Guideline**

### **🔥 Convert Microsoft Phi-3.5 go tflite support**

0. Dis sample na for Android 14+

1. Install Python 3.10.12

***Suggestion:*** use conda take install your Python env

2. Ubuntu 20.04 / 22.04 (abeg focus on [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion:*** Use Azure Linux VM or 3rd party cloud vm take create your env

3. Go enter your Linux bash , make you install Python library 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Make you download Microsoft-3.5-Instruct from Hugging face


```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convert Microsoft Phi-3.5 go tflite


```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Convert to Microsoft Phi-3.5 to Android Mediapipe Bundle**

abeg install mediapipe first

```bash

pip install mediapipe

```

run dis code for [your notebook](../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)



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


### **🔥 Using adb push put model to your  Android devices path**


```bash

adb shell rm -r /data/local/tmp/llm/ # Comot any models wey dem don load before

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Running your Android code**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.pcm.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate by AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get errors or mistakes. The original document for im own language na di correct/authoritative source. If na important information, make you use professional human translation. We no dey liable for any misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->