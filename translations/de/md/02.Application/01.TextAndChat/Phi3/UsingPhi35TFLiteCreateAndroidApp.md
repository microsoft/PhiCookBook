<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-03-27T11:05:03+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "de"
}
-->
# **Verwendung von Microsoft Phi-3.5 tflite zur Erstellung einer Android-App**

Dies ist ein Android-Beispiel, das Microsoft Phi-3.5 tflite-Modelle verwendet.

## **📚 Wissen**

Die Android LLM Inference API ermöglicht es, große Sprachmodelle (LLMs) vollständig auf Android-Geräten auszuführen. Sie können damit eine Vielzahl von Aufgaben durchführen, wie beispielsweise das Generieren von Text, das Abrufen von Informationen in natürlicher Sprache und das Zusammenfassen von Dokumenten. Die API bietet integrierte Unterstützung für mehrere Text-zu-Text-Sprachmodelle, sodass Sie die neuesten generativen KI-Modelle direkt auf Ihren Android-Apps anwenden können.

Googld AI Edge Torch ist eine Python-Bibliothek, die die Umwandlung von PyTorch-Modellen in das .tflite-Format unterstützt. Diese Modelle können dann mit TensorFlow Lite und MediaPipe ausgeführt werden. Dies ermöglicht Anwendungen für Android, iOS und IoT, die Modelle vollständig auf dem Gerät ausführen können. AI Edge Torch bietet eine breite CPU-Abdeckung, mit anfänglicher Unterstützung für GPU und NPU. AI Edge Torch strebt eine enge Integration mit PyTorch an, baut auf torch.export() auf und bietet eine gute Abdeckung der Core ATen-Operatoren.

## **🪬 Anleitung**

### **🔥 Microsoft Phi-3.5 in tflite konvertieren**

0. Dieses Beispiel ist für Android 14+

1. Python 3.10.12 installieren

***Empfehlung:*** Verwenden Sie conda, um Ihre Python-Umgebung zu installieren.

2. Ubuntu 20.04 / 22.04 (bitte konzentrieren Sie sich auf [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Empfehlung:*** Verwenden Sie eine Azure Linux VM oder eine VM eines Drittanbieters, um Ihre Umgebung zu erstellen.

3. Wechseln Sie zu Ihrer Linux-Bash, um die Python-Bibliothek zu installieren.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Laden Sie Microsoft-3.5-Instruct von Hugging Face herunter.

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertieren Sie Microsoft Phi-3.5 in tflite.

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 in Android Mediapipe Bundle konvertieren**

Installieren Sie zuerst Mediapipe.

```bash

pip install mediapipe

```

Führen Sie diesen Code in [Ihrem Notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) aus.

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

### **🔥 Modell mit adb push auf den Pfad Ihres Android-Geräts übertragen**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Ihren Android-Code ausführen**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.de.png)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.