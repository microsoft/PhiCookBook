<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-03-27T11:02:59+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "fr"
}
-->
# **Utiliser Microsoft Phi-3.5 tflite pour créer une application Android**

Ceci est un exemple d'application Android utilisant les modèles tflite de Microsoft Phi-3.5.

## **📚 Connaissances**

L'API Android LLM Inference vous permet d'exécuter des modèles de langage de grande taille (LLMs) entièrement sur l'appareil pour les applications Android. Vous pouvez l'utiliser pour effectuer une large gamme de tâches, telles que la génération de texte, la récupération d'informations sous forme de langage naturel et le résumé de documents. Cette API prend en charge plusieurs modèles de langage textuel, vous permettant d'appliquer les derniers modèles d'IA générative sur appareil à vos applications Android.

Googld AI Edge Torch est une bibliothèque Python qui permet de convertir des modèles PyTorch en format .tflite, pouvant ensuite être exécutés avec TensorFlow Lite et MediaPipe. Cela permet de créer des applications pour Android, iOS et IoT capables d'exécuter des modèles entièrement sur l'appareil. AI Edge Torch offre une large couverture des processeurs (CPU), avec un support initial pour les GPU et NPU. AI Edge Torch cherche à s'intégrer étroitement avec PyTorch, en s'appuyant sur torch.export() et en offrant une bonne couverture des opérateurs Core ATen.

## **🪬 Instructions**

### **🔥 Convertir Microsoft Phi-3.5 pour prise en charge tflite**

0. Cet exemple est conçu pour Android 14+

1. Installer Python 3.10.12

***Suggestion :*** utiliser conda pour installer votre environnement Python

2. Ubuntu 20.04 / 22.04 (veuillez vous concentrer sur [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion :*** Utiliser une VM Linux Azure ou une VM cloud tierce pour créer votre environnement

3. Accédez à votre terminal Linux pour installer la bibliothèque Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Télécharger Microsoft-3.5-Instruct depuis Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convertir Microsoft Phi-3.5 en tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Convertir Microsoft Phi-3.5 en bundle Android Mediapipe**

Veuillez installer Mediapipe au préalable

```bash

pip install mediapipe

```

Exécutez ce code dans [votre notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Utiliser adb pour transférer le modèle de tâche vers le chemin de vos appareils Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Exécuter votre code Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.fr.png)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.