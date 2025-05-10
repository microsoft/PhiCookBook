<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:49:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "nl"
}
-->
# **Microsoft Phi-3.5 tflite gebruiken om Android-app te maken**

Dit is een Androidvoorbeeld dat Microsoft Phi-3.5 tflite-modellen gebruikt.

## **📚 Kennis**

Android LLM Inference API stelt je in staat om grote taalmodellen (LLM's) volledig op het apparaat uit te voeren voor Android-applicaties. Hiermee kun je allerlei taken uitvoeren, zoals tekst genereren, informatie ophalen in natuurlijke taal en documenten samenvatten. De taak biedt ingebouwde ondersteuning voor meerdere tekst-naar-tekst grote taalmodellen, zodat je de nieuwste generatieve AI-modellen op het apparaat kunt toepassen in je Android-apps.

Google AI Edge Torch is een Python-bibliotheek die het converteren van PyTorch-modellen naar een .tflite-formaat ondersteunt, dat vervolgens kan worden uitgevoerd met TensorFlow Lite en MediaPipe. Dit maakt applicaties voor Android, iOS en IoT mogelijk die modellen volledig op het apparaat kunnen draaien. AI Edge Torch biedt brede CPU-ondersteuning, met aanvankelijke ondersteuning voor GPU en NPU. AI Edge Torch streeft naar nauwe integratie met PyTorch, bouwend op torch.export() en biedt goede dekking van Core ATen-operators.

## **🪬 Richtlijn**

### **🔥 Microsoft Phi-3.5 converteren naar tflite-ondersteuning**

0. Dit voorbeeld is voor Android 14+

1. Installeer Python 3.10.12

***Suggestie:*** gebruik conda om je Python-omgeving te installeren

2. Ubuntu 20.04 / 22.04 (focus op [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestie:*** gebruik Azure Linux VM of een cloud-VM van een derde partij om je omgeving op te zetten

3. Ga naar je Linux bash om de Python-bibliotheek te installeren

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Download Microsoft-3.5-Instruct van Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Converteer Microsoft Phi-3.5 naar tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Converteren naar Microsoft Phi-3.5 Android Mediapipe Bundle**

Installeer eerst mediapipe

```bash

pip install mediapipe

```

Voer deze code uit in [jouw notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Gebruik adb push om het taakmodel naar het pad op je Android-apparaat te kopiëren**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Je Android-code uitvoeren**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.nl.png)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.