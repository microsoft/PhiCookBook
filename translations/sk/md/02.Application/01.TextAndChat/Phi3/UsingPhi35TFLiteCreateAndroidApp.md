<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:50:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "sk"
}
-->
# **Použitie Microsoft Phi-3.5 tflite na vytvorenie Android aplikácie**

Toto je ukážka pre Android využívajúca modely Microsoft Phi-3.5 tflite.

## **📚 Znalosti**

Android LLM Inference API umožňuje spúšťať veľké jazykové modely (LLM) priamo na zariadení pre Android aplikácie, ktoré môžete použiť na rôzne úlohy, ako generovanie textu, získavanie informácií v prirodzenom jazyku alebo zhrnutie dokumentov. Táto úloha má zabudovanú podporu pre viacero text-to-text veľkých jazykových modelov, takže môžete využiť najnovšie generatívne AI modely priamo vo vašich Android aplikáciách.

Google AI Edge Torch je python knižnica, ktorá podporuje konverziu PyTorch modelov do formátu .tflite, ktorý sa potom dá spustiť pomocou TensorFlow Lite a MediaPipe. To umožňuje aplikáciám pre Android, iOS a IoT bežať modely kompletne priamo na zariadení. AI Edge Torch ponúka širokú podporu CPU, s počiatočnou podporou GPU a NPU. AI Edge Torch sa snaží úzko integrovať s PyTorch, stavajúc na torch.export() a poskytujúc dobrú podporu pre Core ATen operátory.

## **🪬 Návod**

### **🔥 Konverzia Microsoft Phi-3.5 na podporu tflite**

0. Tento príklad je určený pre Android 14+

1. Nainštalujte Python 3.10.12

***Odporúčanie:*** použite conda na inštaláciu vášho Python prostredia

2. Ubuntu 20.04 / 22.04 (zamerajte sa na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Odporúčanie:*** Použite Azure Linux VM alebo cloudové VM od tretích strán na vytvorenie prostredia

3. Otvorte Linux bash a nainštalujte Python knižnice

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Stiahnite Microsoft-3.5-Instruct z Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertujte Microsoft Phi-3.5 na tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konverzia Microsoft Phi-3.5 na Android Mediapipe Bundle**

najprv nainštalujte mediapipe

```bash

pip install mediapipe

```

spustite tento kód vo [vašom notebooku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Použitie adb push na presunutie modelu do cesty na vašom Android zariadení**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Spustenie vášho Android kódu**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.sk.png)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.