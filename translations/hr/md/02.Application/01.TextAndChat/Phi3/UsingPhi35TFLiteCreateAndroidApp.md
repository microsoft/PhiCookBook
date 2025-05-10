<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:51:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "hr"
}
-->
# **Korištenje Microsoft Phi-3.5 tflite za izradu Android aplikacije**

Ovo je Android primjer koji koristi Microsoft Phi-3.5 tflite modele.

## **📚 Znanje**

Android LLM Inference API omogućuje pokretanje velikih jezičnih modela (LLM) potpuno na uređaju za Android aplikacije, što možete iskoristiti za širok spektar zadataka, poput generiranja teksta, dohvaćanja informacija u prirodnom jeziku i sažimanja dokumenata. Ovaj zadatak ima ugrađenu podršku za više velikih jezičnih modela tekst-u-tekst, pa možete primijeniti najnovije generativne AI modele na uređaju u svojim Android aplikacijama.

Google AI Edge Torch je Python biblioteka koja podržava pretvaranje PyTorch modela u .tflite format, koji se zatim može pokretati pomoću TensorFlow Lite i MediaPipe. To omogućuje aplikacijama za Android, iOS i IoT da modele izvode potpuno na uređaju. AI Edge Torch nudi široku podršku za CPU, s početnom podrškom za GPU i NPU. AI Edge Torch nastoji se usko integrirati s PyTorchom, nadograđujući torch.export() i pružajući dobru podršku za Core ATen operatore.

## **🪬 Upute**

### **🔥 Konvertiranje Microsoft Phi-3.5 u tflite format**

0. Ovaj primjer je za Android 14+

1. Instalirajte Python 3.10.12

***Preporuka:*** koristite conda za instalaciju Python okruženja

2. Ubuntu 20.04 / 22.04 (molimo obratite pažnju na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Preporuka:*** koristite Azure Linux VM ili cloud VM treće strane za kreiranje okruženja

3. Otvorite svoj Linux terminal i instalirajte Python biblioteku

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Preuzmite Microsoft-3.5-Instruct s Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertirajte Microsoft Phi-3.5 u tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konvertiranje Microsoft Phi-3.5 u Android Mediapipe Bundle**

prvo instalirajte mediapipe

```bash

pip install mediapipe

```

pokrenite ovaj kod u [vašem notebooku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Korištenje adb push za prijenos modela zadatka na putanju Android uređaja**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Pokretanje vašeg Android koda**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili kriva tumačenja proizašla iz korištenja ovog prijevoda.