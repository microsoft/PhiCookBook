<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:50:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "tl"
}
-->
# **Paggamit ng Microsoft Phi-3.5 tflite para gumawa ng Android app**

Ito ay isang Android sample gamit ang Microsoft Phi-3.5 tflite models.

## **📚 Kaalaman**

Ang Android LLM Inference API ay nagpapahintulot sa'yo na patakbuhin ang malalaking language models (LLMs) nang buo sa device para sa mga Android application, na magagamit mo para sa iba't ibang gawain, tulad ng paggawa ng teksto, pagkuha ng impormasyon sa natural na wika, at pagbubuod ng mga dokumento. Ang task na ito ay may built-in na suporta para sa maraming text-to-text large language models, kaya maaari mong gamitin ang pinakabagong on-device generative AI models sa iyong mga Android apps.

Ang Googld AI Edge Torch ay isang python library na sumusuporta sa pag-convert ng PyTorch models papuntang .tflite format, na maaaring patakbuhin gamit ang TensorFlow Lite at MediaPipe. Pinapagana nito ang mga aplikasyon para sa Android, iOS, at IoT na kayang patakbuhin ang mga modelo nang buo sa device. Ang AI Edge Torch ay may malawak na suporta sa CPU, kasama ang panimulang suporta para sa GPU at NPU. Layunin ng AI Edge Torch na maging malapit ang integrasyon sa PyTorch, gamit ang torch.export() at nagbibigay ng mahusay na coverage sa Core ATen operators.

## **🪬 Patnubay**

### **🔥 I-convert ang Microsoft Phi-3.5 sa tflite support**

0. Ang sample na ito ay para sa Android 14+

1. I-install ang Python 3.10.12

***Suhestiyon:*** gamitin ang conda para i-install ang iyong Python environment

2. Ubuntu 20.04 / 22.04 (paki-tutok sa [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suhestiyon:*** Gumamit ng Azure Linux VM o third party cloud vm para gumawa ng iyong environment

3. Pumunta sa iyong Linux bash, para i-install ang Python library

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. I-download ang Microsoft-3.5-Instruct mula sa Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. I-convert ang Microsoft Phi-3.5 sa tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 I-convert ang Microsoft Phi-3.5 sa Android Mediapipe Bundle**

paki-install muna ang mediapipe

```bash

pip install mediapipe

```

patakbuhin ang code na ito sa [iyong notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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


### **🔥 Gamitin ang adb push para ilagay ang task model sa path ng iyong Android device**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Patakbuhin ang iyong Android code**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.tl.png)

**Pagtatanggol**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagsisikapang maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.