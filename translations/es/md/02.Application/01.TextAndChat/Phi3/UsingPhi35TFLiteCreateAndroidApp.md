<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-03-27T11:04:01+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "es"
}
-->
# **Usar Microsoft Phi-3.5 tflite para crear una app de Android**

Este es un ejemplo de Android que utiliza modelos Microsoft Phi-3.5 tflite.

## **📚 Conocimientos**

La API de Inferencia LLM de Android te permite ejecutar modelos de lenguaje grande (LLMs) completamente en el dispositivo para aplicaciones Android, que puedes usar para realizar una amplia gama de tareas, como generar texto, recuperar información en lenguaje natural y resumir documentos. La tarea incluye soporte integrado para múltiples modelos de lenguaje grande de texto a texto, por lo que puedes aplicar los últimos modelos generativos de IA en el dispositivo a tus aplicaciones Android.

Googld AI Edge Torch es una biblioteca de Python que permite convertir modelos PyTorch al formato .tflite, que luego pueden ejecutarse con TensorFlow Lite y MediaPipe. Esto habilita aplicaciones para Android, iOS e IoT que pueden ejecutar modelos completamente en el dispositivo. AI Edge Torch ofrece una amplia cobertura de CPU, con soporte inicial para GPU y NPU. AI Edge Torch busca integrarse estrechamente con PyTorch, basándose en torch.export() y proporcionando una buena cobertura de los operadores Core ATen.

## **🪬 Guía**

### **🔥 Convertir Microsoft Phi-3.5 a formato tflite**

0. Este ejemplo es para Android 14+

1. Instalar Python 3.10.12

***Sugerencia:*** usar conda para instalar tu entorno de Python.

2. Ubuntu 20.04 / 22.04 (por favor enfócate en [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugerencia:*** usar Azure Linux VM o una máquina virtual de terceros para crear tu entorno.

3. Ve a tu terminal de Linux para instalar la biblioteca de Python.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Descarga Microsoft-3.5-Instruct desde Hugging Face.

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convierte Microsoft Phi-3.5 a tflite.

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Convertir Microsoft Phi-3.5 a Android Mediapipe Bundle**

Primero, instala mediapipe.

```bash

pip install mediapipe

```

Ejecuta este código en [tu notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb).

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

### **🔥 Usar adb push para transferir el modelo a la ruta de tu dispositivo Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Ejecutar tu código de Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.es.png)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.