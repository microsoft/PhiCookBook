<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-09-12T14:31:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "lt"
}
-->
# **Naudojant Microsoft Phi-3.5 tflite Android programėlei kurti**

Tai yra Android pavyzdys, naudojantis Microsoft Phi-3.5 tflite modelius.

## **📚 Žinios**

Android LLM Inference API leidžia vykdyti didelius kalbos modelius (LLMs) tiesiogiai įrenginyje Android programėlėms. Šiuos modelius galima naudoti įvairioms užduotims atlikti, tokioms kaip teksto generavimas, informacijos paieška natūralia kalba ir dokumentų santraukų kūrimas. Ši funkcija turi integruotą palaikymą keliems tekstas-į-tekstą dideliems kalbos modeliams, todėl galite pritaikyti naujausius generatyviosios AI modelius savo Android programėlėse.

Google AI Edge Torch yra Python biblioteka, kuri palaiko PyTorch modelių konvertavimą į .tflite formatą, kurį galima vykdyti naudojant TensorFlow Lite ir MediaPipe. Tai leidžia kurti Android, iOS ir IoT programėles, kurios gali vykdyti modelius tiesiogiai įrenginyje. AI Edge Torch siūlo platų CPU palaikymą, taip pat pradinį GPU ir NPU palaikymą. AI Edge Torch siekia glaudžiai integruotis su PyTorch, remdamasis torch.export() ir užtikrindamas gerą Core ATen operatorių aprėptį.

## **🪬 Gairės**

### **🔥 Konvertuoti Microsoft Phi-3.5 į tflite palaikymą**

0. Šis pavyzdys skirtas Android 14+

1. Įdiekite Python 3.10.12

***Pasiūlymas:*** naudokite conda Python aplinkai įdiegti

2. Ubuntu 20.04 / 22.04 (atkreipkite dėmesį į [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Pasiūlymas:*** naudokite Azure Linux VM arba trečiųjų šalių debesų VM aplinkai sukurti

3. Eikite į Linux bash ir įdiekite Python biblioteką

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Atsisiųskite Microsoft-3.5-Instruct iš Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertuokite Microsoft Phi-3.5 į tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konvertuoti Microsoft Phi-3.5 į Android Mediapipe paketą**

Pirmiausia įdiekite mediapipe

```bash

pip install mediapipe

```

Paleiskite šį kodą [savo užrašinėje](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Naudojant adb push užduoties modelį Android įrenginio kelyje**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Paleiskite savo Android kodą**

![demo](../../../../../../imgs/02/android-tf/demo.png)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.