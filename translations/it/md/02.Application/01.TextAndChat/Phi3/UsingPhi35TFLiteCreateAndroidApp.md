# **Utilizzo di Microsoft Phi-3.5 tflite per creare un'app Android**

Questo è un esempio Android che utilizza i modelli Microsoft Phi-3.5 tflite.

## **📚 Conoscenze**

L'API Android LLM Inference ti permette di eseguire modelli di linguaggio di grandi dimensioni (LLM) completamente sul dispositivo per applicazioni Android, consentendoti di svolgere una vasta gamma di compiti, come generare testo, recuperare informazioni in forma naturale e riassumere documenti. Il task offre supporto integrato per diversi modelli di linguaggio di grandi dimensioni testo-su-testo, così puoi applicare i più recenti modelli di AI generativa on-device alle tue app Android.

Google AI Edge Torch è una libreria Python che supporta la conversione di modelli PyTorch in formato .tflite, che possono poi essere eseguiti con TensorFlow Lite e MediaPipe. Questo abilita applicazioni per Android, iOS e IoT che possono eseguire modelli completamente sul dispositivo. AI Edge Torch offre un'ampia copertura CPU, con supporto iniziale per GPU e NPU. AI Edge Torch mira a integrarsi strettamente con PyTorch, basandosi su torch.export() e fornendo una buona copertura degli operatori Core ATen.

## **🪬 Linee guida**

### **🔥 Convertire Microsoft Phi-3.5 in supporto tflite**

0. Questo esempio è per Android 14+

1. Installa Python 3.10.12

***Suggerimento:*** usa conda per installare il tuo ambiente Python

2. Ubuntu 20.04 / 22.04 (focalizzati su [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggerimento:*** usa una VM Linux Azure o una VM cloud di terze parti per creare il tuo ambiente

3. Vai al tuo terminale Linux e installa la libreria Python

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

![demo](../../../../../../translated_images/it/demo.06d5a4246f057d1b.webp)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.