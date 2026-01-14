<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:54:58+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "sk"
}
-->
# **Použitie Microsoft Phi-3.5 tflite na vytvorenie Android aplikácie**

Toto je ukážka pre Android využívajúca modely Microsoft Phi-3.5 tflite.

## **📚 Vedomosti**

Android LLM Inference API umožňuje spúšťať veľké jazykové modely (LLM) úplne priamo na zariadení pre Android aplikácie, ktoré môžete využiť na širokú škálu úloh, ako je generovanie textu, získavanie informácií v prirodzenom jazyku a zhrnutie dokumentov. Táto úloha poskytuje vstavanú podporu pre viaceré text-to-text veľké jazykové modely, takže môžete do svojich Android aplikácií aplikovať najnovšie generatívne AI modely priamo na zariadení.

Googld AI Edge Torch je python knižnica, ktorá podporuje konverziu PyTorch modelov do formátu .tflite, ktorý je možné následne spustiť pomocou TensorFlow Lite a MediaPipe. To umožňuje aplikácie pre Android, iOS a IoT, ktoré môžu modely spúšťať úplne lokálne na zariadení. AI Edge Torch ponúka širokú podporu CPU, s počiatočnou podporou GPU a NPU. AI Edge Torch sa snaží úzko integrovať s PyTorch, stavajúc na torch.export() a poskytujúc dobrú podporu pre Core ATen operátory.

## **🪬 Návod**

### **🔥 Konverzia Microsoft Phi-3.5 na tflite podporu**

0. Táto ukážka je pre Android 14+

1. Nainštalujte Python 3.10.12

***Odporúčanie:*** použite conda na vytvorenie Python prostredia

2. Ubuntu 20.04 / 22.04 (zamerajte sa na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Odporúčanie:*** Použite Azure Linux VM alebo cloudové VM od tretej strany na vytvorenie prostredia

3. Otvorte Linux bash a nainštalujte Python knižnicu

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Stiahnite Microsoft-3.5-Instruct z Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertujte Microsoft Phi-3.5 na tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konverzia Microsoft Phi-3.5 na Android Mediapipe Bundle**

najskôr nainštalujte mediapipe

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

### **🔥 Použitie adb push na presun modelu úlohy do cesty na vašom Android zariadení**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Spustenie vášho Android kódu**

![demo](../../../../../../translated_images/sk/demo.06d5a4246f057d1b.png)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.