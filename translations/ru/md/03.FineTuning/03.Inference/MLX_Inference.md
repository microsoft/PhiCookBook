<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-03-27T16:07:06+00:00",
  "source_file": "md\\03.FineTuning\\03.Inference\\MLX_Inference.md",
  "language_code": "ru"
}
-->
# **Inference Phi-3 с использованием Apple MLX Framework**

## **Что такое MLX Framework**

MLX — это фреймворк для исследований в области машинного обучения на устройствах с чипами Apple Silicon, разработанный Apple machine learning research.

MLX создан исследователями машинного обучения для исследователей машинного обучения. Фреймворк разработан так, чтобы быть удобным для пользователя, но при этом оставаться эффективным для обучения и внедрения моделей. Концепция самого фреймворка также довольно проста. Мы стремимся сделать его доступным для расширения и улучшения, чтобы ускорить процесс исследования новых идей.

LLM-модели могут быть ускорены на устройствах с Apple Silicon через MLX, а запуск моделей локально становится очень удобным.

## **Использование MLX для инференса Phi-3-mini**

### **1. Настройка окружения MLX**

1. Python 3.11.x  
2. Установите библиотеку MLX  

```bash

pip install mlx-lm

```

### **2. Запуск Phi-3-mini в терминале с MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Результат (мое окружение: Apple M1 Max, 64GB):

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.ru.png)

### **3. Квантование Phi-3-mini с помощью MLX в терминале**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Примечание:*** Модель может быть квантована через mlx_lm.convert, и квантование по умолчанию выполняется в формате INT4. В этом примере Phi-3-mini квантуется в INT4.

Модель можно квантовать с помощью mlx_lm.convert, где формат INT4 используется по умолчанию. В данном примере модель Phi-3-mini квантуется в INT4. После квантования она будет сохранена в стандартной директории ./mlx_model.

Мы можем протестировать квантованную модель с помощью MLX через терминал.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Результат:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.ru.png)

### **4. Запуск Phi-3-mini с MLX в Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.ru.png)

***Примечание:*** Ознакомьтесь с этим примером [по ссылке](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Ресурсы**

1. Узнайте больше о Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Репозиторий Apple MLX на GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.