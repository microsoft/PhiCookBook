<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:54:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "hu"
}
-->
# **Microsoft Phi-3.5 tflite használata Android alkalmazás készítéséhez**

Ez egy Android példa, amely a Microsoft Phi-3.5 tflite modelleket használja.

## **📚 Tudás**

Az Android LLM Inference API lehetővé teszi, hogy nagy nyelvi modelleket (LLM-eket) teljes mértékben eszközön futtass Android alkalmazásokhoz, amelyeket különféle feladatokra használhatsz, például szöveg generálására, természetes nyelvű információ lekérésére és dokumentumok összefoglalására. A feladat beépített támogatást nyújt több szöveg-szöveg nagy nyelvi modellhez, így a legújabb eszközön futtatható generatív AI modelleket alkalmazhatod Android alkalmazásaidban.

A Googld AI Edge Torch egy Python könyvtár, amely támogatja a PyTorch modellek .tflite formátumba történő átalakítását, amelyeket aztán TensorFlow Lite és MediaPipe segítségével lehet futtatni. Ez lehetővé teszi Android, iOS és IoT alkalmazások számára, hogy a modelleket teljes mértékben eszközön futtassák. Az AI Edge Torch széles CPU támogatást kínál, kezdeti GPU és NPU támogatással. Az AI Edge Torch célja, hogy szorosan integrálódjon a PyTorch-hoz, a torch.export() funkcióra építve, és jó lefedettséget biztosít a Core ATen operátorokhoz.

## **🪬 Útmutató**

### **🔥 Microsoft Phi-3.5 átalakítása tflite támogatásra**

0. Ez a példa Android 14+ verzióhoz készült

1. Telepítsd a Python 3.10.12 verziót

***Javaslat:*** conda használata a Python környezet telepítéséhez

2. Ubuntu 20.04 / 22.04 (kérlek, fókuszálj a [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) projektjére)

***Javaslat:*** Azure Linux VM vagy harmadik fél felhő alapú VM használata a környezet létrehozásához

3. Nyisd meg a Linux bash-t, és telepítsd a Python könyvtárat

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

5. Alakítsd át a Microsoft Phi-3.5 modellt tflite formátumba

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 átalakítása Android Mediapipe csomaggá**

Először telepítsd a mediapipe-t

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

### **🔥 A modell átvitele adb push segítségével az Android eszközödre**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Az Android kód futtatása**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1b.hu.png)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.