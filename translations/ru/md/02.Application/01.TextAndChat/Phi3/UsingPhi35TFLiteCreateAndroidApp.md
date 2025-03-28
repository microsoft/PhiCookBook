<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-03-27T11:06:03+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ru"
}
-->
# **Использование Microsoft Phi-3.5 tflite для создания Android-приложения**

Это пример Android-приложения, использующего модели Microsoft Phi-3.5 tflite.

## **📚 Знания**

API для выполнения LLM на Android позволяет запускать крупные языковые модели (LLM) полностью на устройстве для Android-приложений. Вы можете использовать это для выполнения широкого спектра задач, таких как генерация текста, извлечение информации в форме естественного языка и суммирование документов. API предоставляет встроенную поддержку для нескольких текстовых языковых моделей, чтобы вы могли применять новейшие генеративные модели ИИ на устройствах в своих Android-приложениях.

Google AI Edge Torch — это библиотека на Python, которая поддерживает преобразование моделей PyTorch в формат .tflite, который затем можно запускать с помощью TensorFlow Lite и MediaPipe. Это позволяет создавать приложения для Android, iOS и IoT, которые могут выполнять модели полностью на устройстве. AI Edge Torch обеспечивает широкую поддержку процессоров (CPU), а также начальную поддержку графических процессоров (GPU) и нейропроцессоров (NPU). AI Edge Torch стремится к тесной интеграции с PyTorch, используя torch.export() и предоставляя хорошее покрытие для Core ATen операторов.

## **🪬 Руководство**

### **🔥 Конвертация Microsoft Phi-3.5 в формат tflite**

0. Этот пример предназначен для Android 14+

1. Установите Python 3.10.12

***Рекомендация:*** использовать conda для установки вашего окружения Python

2. Ubuntu 20.04 / 22.04 (обратите внимание на [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Рекомендация:*** использовать Azure Linux VM или виртуальную машину стороннего поставщика для создания окружения

3. Перейдите в ваш Linux bash, чтобы установить библиотеку Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Скачайте Microsoft-3.5-Instruct с Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Конвертируйте Microsoft Phi-3.5 в формат tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Конвертация Microsoft Phi-3.5 в Android Mediapipe Bundle**

Сначала установите mediapipe

```bash

pip install mediapipe

```

Запустите этот код в [вашей записной книжке](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Использование adb для передачи модели на ваше Android-устройство**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Запуск вашего Android-кода**

![демо](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ru.png)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за недоразумения или неверные интерпретации, возникающие в результате использования данного перевода.