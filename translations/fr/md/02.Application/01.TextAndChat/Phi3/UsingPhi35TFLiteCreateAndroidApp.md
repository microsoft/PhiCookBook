<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:49:12+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "fr"
}
-->
# **Utilisation de Microsoft Phi-3.5 tflite pour créer une application Android**

Ceci est un exemple Android utilisant les modèles Microsoft Phi-3.5 tflite.

## **📚 Connaissances**

L’API d’inférence LLM Android vous permet d’exécuter des modèles de langage de grande taille (LLM) entièrement sur l’appareil pour les applications Android, ce que vous pouvez utiliser pour réaliser une large gamme de tâches, telles que générer du texte, récupérer des informations en langage naturel, et résumer des documents. La tâche offre un support intégré pour plusieurs modèles de langage de grande taille texte-à-texte, vous permettant ainsi d’appliquer les derniers modèles d’IA générative sur appareil à vos applications Android.

Googld AI Edge Torch est une bibliothèque Python qui permet de convertir des modèles PyTorch au format .tflite, pouvant ensuite être exécutés avec TensorFlow Lite et MediaPipe. Cela permet de créer des applications pour Android, iOS et IoT capables d’exécuter les modèles entièrement sur l’appareil. AI Edge Torch offre une large couverture CPU, avec un support initial pour GPU et NPU. AI Edge Torch vise une intégration étroite avec PyTorch, en s’appuyant sur torch.export() et en couvrant bien les opérateurs Core ATen.

## **🪬 Guide**

### **🔥 Conversion de Microsoft Phi-3.5 au format tflite**

0. Cet exemple est destiné à Android 14+

1. Installez Python 3.10.12

***Suggestion :*** utilisez conda pour installer votre environnement Python

2. Ubuntu 20.04 / 22.04 (concentrez-vous sur [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion :*** utilisez une VM Linux Azure ou une VM cloud tierce pour créer votre environnement

3. Ouvrez votre terminal Linux pour installer la bibliothèque Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Téléchargez Microsoft-3.5-Instruct depuis Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convertissez Microsoft Phi-3.5 en tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Conversion de Microsoft Phi-3.5 en bundle Android Mediapipe**

Veuillez installer mediapipe en premier lieu

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

### **🔥 Utilisation de adb push pour transférer le modèle task vers le chemin de votre appareil Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Exécution de votre code Android**

![demo](../../../../../../translated_images/fr/demo.06d5a4246f057d1b.png)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.