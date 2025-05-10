<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:50:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "hu"
}
-->
# **Microsoft Phi-3.5 tflite használata Android alkalmazás készítéséhez**

Ez egy Android példa, amely a Microsoft Phi-3.5 tflite modelleket használja.

## **📚 Tudnivalók**

Az Android LLM Inference API lehetővé teszi, hogy nagy nyelvi modelleket (LLM-eket) teljesen eszközön futtass Android alkalmazásokhoz, amelyeket különféle feladatokra használhatsz, például szöveg generálására, természetes nyelvű információ lekérésére vagy dokumentumok összefoglalására. A feladat beépített támogatást nyújt több szövegből szövegbe nagy nyelvi modellhez, így a legújabb eszközön futtatható generatív AI modelleket alkalmazhatod Android alkalmazásaidban.

A Google AI Edge Torch egy Python könyvtár, amely támogatja PyTorch modellek .tflite formátumba való konvertálását, amelyeket aztán TensorFlow Lite és MediaPipe segítségével lehet futtatni. Ez lehetővé teszi Android, iOS és IoT alkalmazások számára, hogy a modelleket teljes mértékben eszközön futtassák. Az AI Edge Torch széles CPU lefedettséget kínál, kezdeti GPU és NPU támogatással. Az AI Edge Torch szoros integrációra törekszik a PyTorch-tal, a torch.export() funkcióra építve, és jó lefedettséget biztosít a Core ATen operátorokból.

## **🪬 Útmutató**

### **🔥 Microsoft Phi-3.5 konvertálása tflite formátumba**

0. Ez a minta Android 14+ rendszerekhez készült

1. Telepítsd a Python 3.10.12 verziót

***Javaslat:*** conda használata a Python környezet telepítéséhez

2. Ubuntu 20.04 / 22.04 (figyelj a [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) projekt részleteire)

***Javaslat:*** Azure Linux VM vagy harmadik fél felhőalapú VM használata a környezet létrehozásához

3. Nyisd meg a Linux bash-t, és telepítsd a Python könyvtárakat

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Töltsd le a Microsoft-3.5-Instruct modellt a Hugging face-ről

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertáld a Microsoft Phi-3.5 modellt tflite formátumba

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 konvertálása Android Mediapipe csomaggá**

Először telepítsd a mediapipe csomagot

```bash

pip install mediapipe

```

Futtasd ezt a kódot a [jegyzetfüzetedben](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Task modell átvitele adb push segítségével Android eszközöd megfelelő útvonalára**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android kód futtatása**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.hu.png)

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.