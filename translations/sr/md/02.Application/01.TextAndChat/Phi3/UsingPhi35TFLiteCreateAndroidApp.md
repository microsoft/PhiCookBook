<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:51:04+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "sr"
}
-->
# **Korišćenje Microsoft Phi-3.5 tflite za kreiranje Android aplikacije**

Ovo je Android primer koji koristi Microsoft Phi-3.5 tflite modele.

## **📚 Znanje**

Android LLM Inference API omogućava pokretanje velikih jezičkih modela (LLM) potpuno na uređaju za Android aplikacije, što možete koristiti za obavljanje raznih zadataka, kao što su generisanje teksta, pretraživanje informacija u prirodnom jeziku i sažimanje dokumenata. Ovaj zadatak ima ugrađenu podršku za više tekstualnih velikih jezičkih modela, tako da možete primeniti najnovije generativne AI modele direktno na Android aplikacijama.

Google AI Edge Torch je Python biblioteka koja podržava konvertovanje PyTorch modela u .tflite format, koji se potom može pokretati preko TensorFlow Lite i MediaPipe. Ovo omogućava aplikacijama za Android, iOS i IoT da modele pokreću potpuno na uređaju. AI Edge Torch nudi široku podršku za CPU, sa početnom podrškom za GPU i NPU. AI Edge Torch teži bliskoj integraciji sa PyTorch-om, gradeći se na torch.export() i pružajući dobru pokrivenost Core ATen operatora.

## **🪬 Uputstvo**

### **🔥 Konvertovanje Microsoft Phi-3.5 u tflite format**

0. Ovaj primer je za Android 14+

1. Instalirajte Python 3.10.12

***Preporuka:*** koristite conda za instalaciju Python okruženja

2. Ubuntu 20.04 / 22.04 (obratite pažnju na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Preporuka:*** koristite Azure Linux VM ili VM na nekoj cloud platformi za kreiranje okruženja

3. Otvorite Linux bash i instalirajte Python biblioteku

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Preuzmite Microsoft-3.5-Instruct sa Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertujte Microsoft Phi-3.5 u tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konvertovanje Microsoft Phi-3.5 u Android Mediapipe Bundle**

prvo instalirajte mediapipe

```bash

pip install mediapipe

```

pokrenite ovaj kod u [vašem notebook-u](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Korišćenje adb push za prebacivanje modela na putanju Android uređaja**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Pokretanje vašeg Android koda**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.sr.png)

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.