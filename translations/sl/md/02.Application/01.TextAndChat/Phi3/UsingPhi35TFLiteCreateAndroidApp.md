<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:55:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "sl"
}
-->
# **Uporaba Microsoft Phi-3.5 tflite za ustvarjanje Android aplikacije**

To je Android primer, ki uporablja Microsoft Phi-3.5 tflite modele.

## **📚 Znanje**

Android LLM Inference API omogoča izvajanje velikih jezikovnih modelov (LLM) popolnoma na napravi za Android aplikacije, kar lahko uporabite za širok nabor nalog, kot so generiranje besedila, iskanje informacij v naravnem jeziku in povzemanje dokumentov. Ta naloga podpira več velikih jezikovnih modelov za pretvorbo besedila v besedilo, tako da lahko v svoje Android aplikacije vključite najnovejše generativne AI modele, ki delujejo neposredno na napravi.

Google AI Edge Torch je Python knjižnica, ki podpira pretvorbo PyTorch modelov v .tflite format, ki ga nato lahko zaženete s TensorFlow Lite in MediaPipe. To omogoča aplikacije za Android, iOS in IoT, ki lahko modele izvajajo popolnoma na napravi. AI Edge Torch ponuja široko podporo za CPU, z začetno podporo za GPU in NPU. AI Edge Torch si prizadeva za tesno integracijo s PyTorch, temelji na torch.export() in zagotavlja dobro podporo za Core ATen operaterje.

## **🪬 Navodila**

### **🔥 Pretvorba Microsoft Phi-3.5 v tflite podporo**

0. Ta primer je za Android 14+

1. Namestite Python 3.10.12

***Priporočilo:*** uporabite conda za namestitev Python okolja

2. Ubuntu 20.04 / 22.04 (osredotočite se na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Priporočilo:*** Uporabite Azure Linux VM ali VM v oblaku tretje osebe za ustvarjanje okolja

3. Odprite Linux bash in namestite Python knjižnico

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Prenesite Microsoft-3.5-Instruct iz Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Pretvorite Microsoft Phi-3.5 v tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Pretvorba Microsoft Phi-3.5 v Android Mediapipe paket**

Najprej namestite mediapipe

```bash

pip install mediapipe

```

Zaženite ta kodo v [vašem zvezku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Uporaba adb push za prenos modela naloge na pot vaše Android naprave**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Zagon vaše Android kode**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.sl.png)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.