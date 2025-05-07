<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-07T14:07:19+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "fr"
}
-->
# **Utiliser Microsoft Phi-3.5 tflite pour créer une application Android**

Ceci est un exemple Android utilisant les modèles Microsoft Phi-3.5 tflite.

## **📚 Connaissances**

L'API Android LLM Inference vous permet d'exécuter des modèles de langage volumineux (LLM) entièrement sur l'appareil pour les applications Android, ce qui vous permet d'effectuer une large gamme de tâches, telles que générer du texte, récupérer des informations en langage naturel, et résumer des documents. La tâche offre un support intégré pour plusieurs modèles de langage volumineux texte-à-texte, vous permettant d'appliquer les derniers modèles d'IA générative embarqués à vos applications Android.

Google AI Edge Torch est une bibliothèque python qui prend en charge la conversion des modèles PyTorch au format .tflite, pouvant ensuite être exécutés avec TensorFlow Lite et MediaPipe. Cela permet de créer des applications pour Android, iOS et IoT capables d'exécuter des modèles entièrement sur l'appareil. AI Edge Torch offre une large couverture CPU, avec un support initial pour GPU et NPU. AI Edge Torch cherche à s'intégrer étroitement avec PyTorch, en s'appuyant sur torch.export() et en couvrant bien les opérateurs Core ATen.


## **🪬 Guide**

### **🔥 Convertir Microsoft Phi-3.5 au format tflite**

0. Cet exemple est destiné à Android 14+

1. Installez Python 3.10.12

***Suggestion :*** utiliser conda pour installer votre environnement Python

2. Ubuntu 20.04 / 22.04 (concentrez-vous sur [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion :*** Utilisez une VM Linux Azure ou une VM cloud tierce pour créer votre environnement

3. Ouvrez votre terminal Linux, pour installer la bibliothèque Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Téléchargez Microsoft-3.5-Instruct depuis Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convertissez Microsoft Phi-3.5 au format tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Convertir Microsoft Phi-3.5 en bundle Android Mediapipe**

Veuillez d'abord installer mediapipe

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


### **🔥 Utiliser adb push pour transférer le modèle task vers le chemin de votre appareil Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Exécuter votre code Android**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.fr.png)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.