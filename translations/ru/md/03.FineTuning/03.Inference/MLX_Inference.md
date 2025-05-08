<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-07T13:41:26+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "ru"
}
-->
# **Инференс Phi-3 с использованием Apple MLX Framework**

## **Что такое MLX Framework**

MLX — это фреймворк для работы с массивами, предназначенный для исследований в области машинного обучения на Apple Silicon, разработанный командой Apple Machine Learning Research.

MLX создан исследователями машинного обучения для исследователей машинного обучения. Фреймворк ориентирован на удобство использования, но при этом обеспечивает эффективное обучение и развертывание моделей. Концепция самого фреймворка также достаточно проста. Мы хотим, чтобы исследователям было легко расширять и улучшать MLX с целью быстрого эксперимента с новыми идеями.

LLM можно ускорить на устройствах Apple Silicon с помощью MLX, а модели удобно запускать локально.

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

Результат (мое окружение — Apple M1 Max, 64GB):

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.ru.png)

### **3. Квантизация Phi-3-mini с MLX в терминале**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Модель можно квантизировать с помощью mlx_lm.convert, при этом по умолчанию используется INT4. В этом примере Phi-3-mini квантизируется в INT4.

Модель квантизируется через mlx_lm.convert, и по умолчанию используется INT4. После квантизации она сохраняется в директорию по умолчанию ./mlx_model

Мы можем протестировать квантизированную модель с помощью MLX из терминала


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Результат:

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.ru.png)


### **4. Запуск Phi-3-mini с MLX в Jupyter Notebook**


![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.ru.png)

***Note:*** Пожалуйста, ознакомьтесь с этим примером [по ссылке](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Ресурсы**

1. Узнайте больше о Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Репозиторий Apple MLX на GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.