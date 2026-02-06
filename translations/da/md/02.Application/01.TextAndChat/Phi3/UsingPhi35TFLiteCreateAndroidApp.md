# **Brug af Microsoft Phi-3.5 tflite til at skabe Android-app**

Dette er et Android-eksempel, der bruger Microsoft Phi-3.5 tflite-modeller.

## **📚 Viden**

Android LLM Inference API giver dig mulighed for at køre store sprogmodeller (LLMs) helt på enheden til Android-applikationer, som du kan bruge til at udføre en bred vifte af opgaver, såsom at generere tekst, hente information i naturligt sprog og opsummere dokumenter. Opgaven har indbygget support til flere tekst-til-tekst store sprogmodeller, så du kan anvende de nyeste generative AI-modeller på enheden i dine Android-apps.

Googld AI Edge Torch er et Python-bibliotek, der understøtter konvertering af PyTorch-modeller til et .tflite-format, som derefter kan køres med TensorFlow Lite og MediaPipe. Dette muliggør applikationer til Android, iOS og IoT, der kan køre modeller helt på enheden. AI Edge Torch tilbyder bred CPU-dækning med indledende GPU- og NPU-understøttelse. AI Edge Torch søger at integrere tæt med PyTorch ved at bygge videre på torch.export() og give god dækning af Core ATen-operatorer.

## **🪬 Retningslinje**

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

4. Download Microsoft-3.5-Instruct fra Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konverter Microsoft Phi-3.5 til tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konverter Microsoft Phi-3.5 til Android Mediapipe Bundle**

Installer venligst mediapipe først

```bash

pip install mediapipe

```

Kør denne kode i [din notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

![demo](../../../../../../translated_images/da/demo.06d5a4246f057d1b.webp)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.