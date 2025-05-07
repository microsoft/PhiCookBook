<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-07T14:07:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ru"
}
-->
# **Использование Microsoft Phi-3.5 tflite для создания Android-приложения**

Это пример для Android с использованием моделей Microsoft Phi-3.5 tflite.

## **📚 Знания**

Android LLM Inference API позволяет запускать большие языковые модели (LLM) полностью на устройстве для Android-приложений. С его помощью можно выполнять широкий спектр задач, таких как генерация текста, поиск информации в естественной форме и создание кратких обзоров документов. Этот инструмент поддерживает несколько текстовых больших языковых моделей, что позволяет использовать современные генеративные AI-модели прямо в Android-приложениях.

Google AI Edge Torch — это библиотека на Python, которая поддерживает конвертацию моделей PyTorch в формат .tflite, который затем можно запускать с помощью TensorFlow Lite и MediaPipe. Это позволяет создавать приложения для Android, iOS и IoT, которые работают полностью на устройстве. AI Edge Torch обеспечивает широкую поддержку CPU, а также начальную поддержку GPU и NPU. AI Edge Torch стремится к тесной интеграции с PyTorch, опираясь на torch.export() и обеспечивая хорошую поддержку основных операторов Core ATen.

## **🪬 Руководство**

### **🔥 Конвертация Microsoft Phi-3.5 в поддержку tflite**

0. Этот пример предназначен для Android 14+

1. Установите Python 3.10.12

***Рекомендация:*** используйте conda для создания Python окружения

2. Ubuntu 20.04 / 22.04 (обратите внимание на [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Рекомендация:*** используйте Azure Linux VM или виртуальную машину в облаке стороннего провайдера для создания окружения

3. Откройте терминал Linux и установите необходимые Python-библиотеки

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Скачайте Microsoft-3.5-Instruct с Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Конвертируйте Microsoft Phi-3.5 в tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Конвертация Microsoft Phi-3.5 в Android Mediapipe Bundle**

Сначала установите mediapipe

```bash

pip install mediapipe

```

Запустите этот код в [вашем ноутбуке](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Отправка модели на Android-устройство с помощью adb push**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Запуск вашего Android-кода**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.ru.png)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.