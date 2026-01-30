<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:51:54+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "pt"
}
-->
# **Usar Microsoft Phi-3.5 tflite para criar app Android**

Este é um exemplo para Android usando os modelos Microsoft Phi-3.5 tflite.

## **📚 Conhecimento**

A API Android LLM Inference permite executar grandes modelos de linguagem (LLMs) totalmente no dispositivo para aplicações Android, que pode usar para realizar uma ampla variedade de tarefas, como gerar texto, recuperar informação em linguagem natural e resumir documentos. A tarefa oferece suporte incorporado para múltiplos modelos de linguagem grandes texto-para-texto, para que possa aplicar os mais recentes modelos de IA generativa no dispositivo nas suas apps Android.

Googld AI Edge Torch é uma biblioteca Python que suporta a conversão de modelos PyTorch para o formato .tflite, que depois pode ser executado com TensorFlow Lite e MediaPipe. Isto permite aplicações para Android, iOS e IoT que podem correr modelos totalmente no dispositivo. AI Edge Torch oferece ampla cobertura para CPU, com suporte inicial para GPU e NPU. AI Edge Torch procura integrar-se de forma próxima com PyTorch, construindo sobre torch.export() e fornecendo boa cobertura dos operadores Core ATen.

## **🪬 Guia**

### **🔥 Converter Microsoft Phi-3.5 para suporte tflite**

0. Este exemplo é para Android 14+

1. Instale Python 3.10.12

***Sugestão:*** usar conda para instalar o seu ambiente Python

2. Ubuntu 20.04 / 22.04 (por favor foque-se em [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugestão:*** Usar uma VM Linux Azure ou VM de cloud de terceiros para criar o seu ambiente

3. Vá para o seu bash Linux, para instalar a biblioteca Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Descarregue Microsoft-3.5-Instruct do Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Converta Microsoft Phi-3.5 para tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Converter Microsoft Phi-3.5 para Android Mediapipe Bundle**

por favor instale mediapipe primeiro

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

### **🔥 Usar adb push para enviar o modelo para o caminho do seu dispositivo Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Executar o seu código Android**

![demo](../../../../../../translated_images/pt-PT/demo.06d5a4246f057d1b.webp)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.