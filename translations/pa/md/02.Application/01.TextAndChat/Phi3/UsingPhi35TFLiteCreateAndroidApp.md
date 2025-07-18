<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:51:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "pa"
}
-->
# **Microsoft Phi-3.5 tflite ਦੀ ਵਰਤੋਂ ਕਰਕੇ Android ਐਪ ਬਣਾਉਣਾ**

ਇਹ Microsoft Phi-3.5 tflite ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ ਬਣਾਇਆ ਗਿਆ ਇੱਕ Android ਸੈਂਪਲ ਹੈ।

## **📚 ਜਾਣਕਾਰੀ**

Android LLM Inference API ਤੁਹਾਨੂੰ Android ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLMs) ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਕੰਮ ਕਰ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ ਟੈਕਸਟ ਬਣਾਉਣਾ, ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨਾ ਅਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਦਾ ਸਾਰ ਬਣਾਉਣਾ। ਇਹ ਟਾਸਕ ਕਈ ਟੈਕਸਟ-ਟੂ-ਟੈਕਸਟ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਲਈ ਬਿਲਟ-ਇਨ ਸਹਾਇਤਾ ਦਿੰਦਾ ਹੈ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੇ Android ਐਪਸ ਵਿੱਚ ਨਵੀਂ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਲਾਗੂ ਕਰ ਸਕੋ।

Google AI Edge Torch ਇੱਕ ਪਾਇਥਨ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ PyTorch ਮਾਡਲਾਂ ਨੂੰ .tflite ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਦੀ ਸਹਾਇਤਾ ਕਰਦੀ ਹੈ, ਜਿਸਨੂੰ ਫਿਰ TensorFlow Lite ਅਤੇ MediaPipe ਨਾਲ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹ Android, iOS ਅਤੇ IoT ਲਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਡਿਵਾਈਸ 'ਤੇ ਮਾਡਲ ਚਲਾਉਣ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ। AI Edge Torch ਵਿਆਪਕ CPU ਕਵਰੇਜ ਦਿੰਦਾ ਹੈ, ਅਤੇ ਸ਼ੁਰੂਆਤੀ GPU ਅਤੇ NPU ਸਹਾਇਤਾ ਵੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। AI Edge Torch PyTorch ਨਾਲ ਨੇੜੇ ਤੌਰ 'ਤੇ ਇੰਟੀਗ੍ਰੇਟ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦਾ ਹੈ, torch.export() 'ਤੇ ਅਧਾਰਿਤ ਹੈ ਅਤੇ Core ATen ਓਪਰੇਟਰਾਂ ਦੀ ਚੰਗੀ ਕਵਰੇਜ ਦਿੰਦਾ ਹੈ।

## **🪬 ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼**

### **🔥 Microsoft Phi-3.5 ਨੂੰ tflite ਵਿੱਚ ਬਦਲਣਾ**

0. ਇਹ ਸੈਂਪਲ Android 14+ ਲਈ ਹੈ।

1. Python 3.10.12 ਇੰਸਟਾਲ ਕਰੋ।

***ਸੁਝਾਅ:*** ਆਪਣਾ Python ਵਾਤਾਵਰਣ ਬਣਾਉਣ ਲਈ conda ਦੀ ਵਰਤੋਂ ਕਰੋ।

2. Ubuntu 20.04 / 22.04 (ਕਿਰਪਾ ਕਰਕੇ [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) 'ਤੇ ਧਿਆਨ ਦਿਓ)

***ਸੁਝਾਅ:*** ਆਪਣਾ ਵਾਤਾਵਰਣ ਬਣਾਉਣ ਲਈ Azure Linux VM ਜਾਂ ਕਿਸੇ ਤੀਜੇ ਪੱਖ ਦੇ ਕਲਾਉਡ VM ਦੀ ਵਰਤੋਂ ਕਰੋ।

3. ਆਪਣੇ Linux ਬੈਸ਼ 'ਤੇ ਜਾ ਕੇ Python ਲਾਇਬ੍ਰੇਰੀ ਇੰਸਟਾਲ ਕਰੋ

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face ਤੋਂ Microsoft-3.5-Instruct ਡਾਊਨਲੋਡ ਕਰੋ

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 ਨੂੰ tflite ਵਿੱਚ ਬਦਲੋ

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 ਨੂੰ Android Mediapipe ਬੰਡਲ ਵਿੱਚ ਬਦਲਣਾ**

ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ mediapipe ਇੰਸਟਾਲ ਕਰੋ

```bash

pip install mediapipe

```

ਇਹ ਕੋਡ [ਤੁਹਾਡੇ ਨੋਟਬੁੱਕ](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) ਵਿੱਚ ਚਲਾਓ

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

### **🔥 adb push ਨਾਲ ਮਾਡਲ ਨੂੰ ਆਪਣੇ Android ਡਿਵਾਈਸ ਦੇ ਰਸਤੇ 'ਤੇ ਭੇਜੋ**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 ਆਪਣੇ Android ਕੋਡ ਨੂੰ ਚਲਾਉਣਾ**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.pa.png)

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।