<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:56:05+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "uk"
}
-->
# **Використання Microsoft Phi-3.5 tflite для створення Android-додатку**

Це приклад для Android, який використовує моделі Microsoft Phi-3.5 у форматі tflite.

## **📚 Знання**

Android LLM Inference API дозволяє запускати великі мовні моделі (LLM) повністю на пристрої для Android-додатків, що дає змогу виконувати широкий спектр завдань, таких як генерація тексту, отримання інформації у вигляді природної мови та підсумовування документів. Цей інтерфейс має вбудовану підтримку кількох великих мовних моделей текст-в-текст, тож ви можете застосовувати найновіші генеративні AI-моделі безпосередньо на Android.

Googld AI Edge Torch — це бібліотека на Python, яка підтримує конвертацію моделей PyTorch у формат .tflite, що потім можна запускати за допомогою TensorFlow Lite та MediaPipe. Це відкриває можливості для додатків на Android, iOS та IoT, які можуть працювати повністю на пристрої. AI Edge Torch забезпечує широку підтримку CPU, а також початкову підтримку GPU та NPU. AI Edge Torch прагне тісно інтегруватися з PyTorch, базуючись на torch.export() та забезпечуючи хорошу підтримку операторів Core ATen.

## **🪬 Інструкція**

### **🔥 Конвертація Microsoft Phi-3.5 у tflite**

0. Цей приклад призначений для Android 14+

1. Встановіть Python 3.10.12

***Рекомендація:*** використовуйте conda для створення вашого Python-середовища

2. Ubuntu 20.04 / 22.04 (зверніть увагу на [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Рекомендація:*** Використовуйте Azure Linux VM або віртуальну машину в хмарі від сторонніх провайдерів для створення середовища

3. Відкрийте термінал Linux і встановіть бібліотеки Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Завантажте Microsoft-3.5-Instruct з Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Конвертуйте Microsoft Phi-3.5 у tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Конвертація Microsoft Phi-3.5 у Android Mediapipe Bundle**

спочатку встановіть mediapipe

```bash

pip install mediapipe

```

запустіть цей код у [вашому ноутбуці](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Використання adb для копіювання моделі завдання на шлях пристрою Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Запуск вашого Android-коду**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1b.uk.png)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.