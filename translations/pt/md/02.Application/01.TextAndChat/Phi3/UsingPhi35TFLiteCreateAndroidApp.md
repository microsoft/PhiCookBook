<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:48:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "pt"
}
-->
# **Usando Microsoft Phi-3.5 tflite para criar app Android**

Este é um exemplo para Android usando os modelos Microsoft Phi-3.5 tflite.

## **📚 Conhecimento**

A API de Inferência LLM para Android permite executar grandes modelos de linguagem (LLMs) totalmente no dispositivo para aplicações Android, que você pode usar para realizar diversas tarefas, como gerar texto, recuperar informações em linguagem natural e resumir documentos. A tarefa oferece suporte integrado para múltiplos modelos de linguagem grandes texto-para-texto, para que você possa aplicar os modelos mais recentes de IA generativa no dispositivo em seus apps Android.

Googld AI Edge Torch é uma biblioteca Python que suporta a conversão de modelos PyTorch para o formato .tflite, que pode ser executado com TensorFlow Lite e MediaPipe. Isso possibilita aplicações para Android, iOS e IoT que rodam modelos totalmente no dispositivo. AI Edge Torch oferece ampla cobertura para CPU, com suporte inicial para GPU e NPU. O AI Edge Torch busca uma integração próxima com PyTorch, construindo sobre torch.export() e oferecendo boa cobertura dos operadores Core ATen.

## **🪬 Guia**

### **🔥 Converter Microsoft Phi-3.5 para suporte tflite**

0. Este exemplo é para Android 14+

1. Instale Python 3.10.12

***Sugestão:*** use conda para instalar seu ambiente Python

2. Ubuntu 20.04 / 22.04 (fique atento ao [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugestão:*** use uma VM Linux Azure ou VM em nuvem de terceiros para criar seu ambiente

3. Acesse seu bash Linux para instalar a biblioteca Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Baixe Microsoft-3.5-Instruct do Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Converta Microsoft Phi-3.5 para tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Converter Microsoft Phi-3.5 para Android Mediapipe Bundle**

por favor, instale mediapipe primeiro

```bash

pip install mediapipe

```

execute este código no [seu notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Usando adb para enviar o modelo da tarefa para o caminho do seu dispositivo Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Executando seu código Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.pt.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.