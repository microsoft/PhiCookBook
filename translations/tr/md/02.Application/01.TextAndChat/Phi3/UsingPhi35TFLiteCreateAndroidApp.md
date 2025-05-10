<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:48:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "tr"
}
-->
# **Microsoft Phi-3.5 tflite kullanarak Android uygulaması oluşturma**

Bu, Microsoft Phi-3.5 tflite modellerini kullanan bir Android örneğidir.

## **📚 Bilgi**

Android LLM Inference API, Android uygulamaları için büyük dil modellerini (LLM) tamamen cihaz üzerinde çalıştırmanıza olanak tanır. Bu sayede metin oluşturma, doğal dil biçiminde bilgi alma ve belgeleri özetleme gibi çeşitli görevleri gerçekleştirebilirsiniz. Bu görev, birden fazla metin-temelli büyük dil modelini destekler, böylece en yeni cihaz üzeri üretken yapay zeka modellerini Android uygulamalarınıza uygulayabilirsiniz.

Googld AI Edge Torch, PyTorch modellerini .tflite formatına dönüştürmeyi destekleyen bir Python kütüphanesidir ve bu modeller TensorFlow Lite ve MediaPipe ile çalıştırılabilir. Bu sayede Android, iOS ve IoT uygulamaları için modeller tamamen cihaz üzerinde çalıştırılabilir. AI Edge Torch geniş CPU desteği sunar ve başlangıçta GPU ile NPU desteği sağlar. AI Edge Torch, torch.export() üzerine inşa edilerek PyTorch ile sıkı entegrasyon hedefler ve Core ATen operatörlerinin iyi bir kapsamını sağlar.

## **🪬 Kılavuz**

### **🔥 Microsoft Phi-3.5’i tflite formatına dönüştürme**

0. Bu örnek Android 14+ içindir.

1. Python 3.10.12 yükleyin

***Öneri:*** Python ortamınızı kurmak için conda kullanın

2. Ubuntu 20.04 / 22.04 (lütfen [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) projesine odaklanın)

***Öneri:*** Ortamınızı oluşturmak için Azure Linux VM veya 3. taraf bulut VM kullanın

3. Linux bash’inize gidin ve Python kütüphanesini yükleyin

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face’den Microsoft-3.5-Instruct modelini indirin

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5’i tflite formatına dönüştürün

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5’i Android Mediapipe Paketine dönüştürme**

Lütfen öncelikle mediapipe’i kurun

```bash

pip install mediapipe

```

Bu kodu [notebook’unuzda](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) çalıştırın

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

### **🔥 adb push ile model dosyasını Android cihazınızın yoluna gönderme**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android kodunuzu çalıştırma**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.tr.png)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.