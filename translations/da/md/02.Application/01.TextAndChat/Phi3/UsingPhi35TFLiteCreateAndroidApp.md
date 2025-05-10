<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:49:12+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "da"
}
-->
# **Brug af Microsoft Phi-3.5 tflite til at skabe Android-app**

Dette er et Android-eksempel, der bruger Microsoft Phi-3.5 tflite-modeller.

## **📚 Viden**

Android LLM Inference API giver dig mulighed for at køre store sprogmodeller (LLMs) helt på enheden til Android-applikationer, som du kan bruge til at udføre en bred vifte af opgaver, såsom at generere tekst, hente information i naturligt sprog og opsummere dokumenter. Opgaven har indbygget support til flere tekst-til-tekst store sprogmodeller, så du kan anvende de nyeste generative AI-modeller på enheden i dine Android-apps.

Googld AI Edge Torch er et python-bibliotek, der understøtter konvertering af PyTorch-modeller til et .tflite-format, som derefter kan køres med TensorFlow Lite og MediaPipe. Dette muliggør applikationer til Android, iOS og IoT, der kan køre modeller helt på enheden. AI Edge Torch tilbyder bred CPU-understøttelse med indledende GPU- og NPU-support. AI Edge Torch søger at integrere tæt med PyTorch, bygger oven på torch.export() og giver god dækning af Core ATen-operatører.

## **🪬 Vejledning**

### **🔥 Konverter Microsoft Phi-3.5 til tflite-support**

0. Dette eksempel er til Android 14+

1. Installer Python 3.10.12

***Forslag:*** brug conda til at installere dit Python-miljø

2. Ubuntu 20.04 / 22.04 (fokuser venligst på [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Forslag:*** Brug Azure Linux VM eller en tredjeparts cloud VM til at oprette dit miljø

3. Gå til din Linux bash for at installere Python-biblioteket

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Download Microsoft-3.5-Instruct fra Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konverter Microsoft Phi-3.5 til tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konverter til Microsoft Phi-3.5 til Android Mediapipe Bundle**

Installer venligst mediapipe først

```bash

pip install mediapipe

```

kør denne kode i [din notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Brug adb push til at overføre task-modellen til din Android-enheds sti**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Kør din Android-kode**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.da.png)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.