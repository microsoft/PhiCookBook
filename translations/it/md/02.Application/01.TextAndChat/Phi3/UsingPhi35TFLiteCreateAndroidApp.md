<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:48:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "it"
}
-->
# **Utilizzo di Microsoft Phi-3.5 tflite per creare un'app Android**

Questo è un esempio Android che utilizza i modelli Microsoft Phi-3.5 tflite.

## **📚 Conoscenze**

Android LLM Inference API ti permette di eseguire modelli di linguaggio di grandi dimensioni (LLM) completamente sul dispositivo per applicazioni Android, consentendoti di svolgere una vasta gamma di attività, come generare testo, recuperare informazioni in forma naturale e riassumere documenti. Il task offre supporto integrato per diversi modelli di grandi dimensioni testo-testo, così puoi applicare i più recenti modelli di AI generativa on-device alle tue app Android.

Googld AI Edge Torch è una libreria Python che supporta la conversione di modelli PyTorch in formato .tflite, che può poi essere eseguito con TensorFlow Lite e MediaPipe. Questo abilita applicazioni per Android, iOS e IoT che possono eseguire modelli completamente sul dispositivo. AI Edge Torch offre una copertura ampia della CPU, con supporto iniziale per GPU e NPU. AI Edge Torch mira a integrarsi strettamente con PyTorch, basandosi su torch.export() e offrendo una buona copertura degli operatori Core ATen.


## **🪬 Linee guida**

### **🔥 Convertire Microsoft Phi-3.5 in supporto tflite**

0. Questo esempio è per Android 14+

1. Installa Python 3.10.12

***Suggerimento:*** usa conda per installare il tuo ambiente Python

2. Ubuntu 20.04 / 22.04 (focalizzati su [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggerimento:*** usa una VM Azure Linux o una VM cloud di terze parti per creare il tuo ambiente

3. Vai nel terminale Linux e installa la libreria Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Scarica Microsoft-3.5-Instruct da Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Converti Microsoft Phi-3.5 in tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Convertire Microsoft Phi-3.5 in Android Mediapipe Bundle**

per favore installa prima mediapipe

```bash

pip install mediapipe

```

esegui questo codice nel [tuo notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)


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


### **🔥 Usare adb push per trasferire il modello task nel percorso del dispositivo Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Esecuzione del codice Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.it.png)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.