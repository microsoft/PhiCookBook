<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:55:07+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ro"
}
-->
# **Folosirea Microsoft Phi-3.5 tflite pentru a crea o aplicație Android**

Acesta este un exemplu Android care utilizează modelele Microsoft Phi-3.5 tflite.

## **📚 Cunoștințe**

Android LLM Inference API îți permite să rulezi modele mari de limbaj (LLM-uri) complet pe dispozitiv pentru aplicațiile Android, pe care le poți folosi pentru o gamă largă de sarcini, cum ar fi generarea de text, extragerea informațiilor în formă naturală și rezumarea documentelor. Această funcție oferă suport integrat pentru mai multe modele mari de limbaj text-la-text, astfel încât să poți aplica cele mai noi modele generative AI pe dispozitiv în aplicațiile tale Android.

Googld AI Edge Torch este o bibliotecă Python care suportă conversia modelelor PyTorch în format .tflite, care pot fi apoi rulate cu TensorFlow Lite și MediaPipe. Aceasta permite aplicații pentru Android, iOS și IoT care pot rula modelele complet pe dispozitiv. AI Edge Torch oferă o acoperire largă pentru CPU, cu suport inițial pentru GPU și NPU. AI Edge Torch urmărește o integrare strânsă cu PyTorch, construind pe baza torch.export() și oferind o bună acoperire a operatorilor Core ATen.

## **🪬 Ghid**

### **🔥 Conversia Microsoft Phi-3.5 la suport tflite**

0. Acest exemplu este pentru Android 14+

1. Instalează Python 3.10.12

***Sugestie:*** folosește conda pentru a-ți instala mediul Python

2. Ubuntu 20.04 / 22.04 (te rugăm să te concentrezi pe [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugestie:*** Folosește o mașină virtuală Azure Linux sau o mașină virtuală cloud de la terți pentru a-ți crea mediul

3. Deschide terminalul Linux și instalează biblioteca Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Descarcă Microsoft-3.5-Instruct de pe Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convertește Microsoft Phi-3.5 în tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Conversia Microsoft Phi-3.5 în pachet Android Mediapipe**

te rugăm să instalezi mai întâi mediapipe

```bash

pip install mediapipe

```

rulează acest cod în [notebook-ul tău](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Folosirea adb push pentru a transfera modelul task pe calea dispozitivului tău Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Rularea codului tău Android**

![demo](../../../../../../translated_images/ro/demo.06d5a4246f057d1b.png)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.