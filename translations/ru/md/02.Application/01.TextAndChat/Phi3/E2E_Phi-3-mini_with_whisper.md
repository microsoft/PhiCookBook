<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:13:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "ru"
}
-->
# Интерактивный Phi 3 Mini 4K Instruct чат-бот с Whisper

## Обзор

Интерактивный Phi 3 Mini 4K Instruct чат-бот — это инструмент, который позволяет пользователям взаимодействовать с демонстрацией Microsoft Phi 3 Mini 4K instruct с помощью текстового или голосового ввода. Чат-бот можно использовать для различных задач, таких как перевод, получение прогноза погоды и сбор общей информации.

### Начало работы

Чтобы использовать этот чат-бот, просто выполните следующие шаги:

1. Откройте новый [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. В главном окне ноутбука вы увидите интерфейс чат-бокса с полем для ввода текста и кнопкой «Send».
3. Чтобы использовать текстовый чат-бот, просто введите сообщение в поле ввода и нажмите кнопку «Send». Чат-бот ответит аудиофайлом, который можно воспроизвести прямо в ноутбуке.

**Note**: Для работы этого инструмента требуется GPU и доступ к моделям Microsoft Phi-3 и OpenAI Whisper, которые используются для распознавания речи и перевода.

### Требования к GPU

Для запуска этой демонстрации вам потребуется 12 ГБ видеопамяти.

Требования к памяти для запуска демонстрации **Microsoft-Phi-3-Mini-4K instruct** на GPU зависят от нескольких факторов, таких как размер входных данных (аудио или текст), язык перевода, скорость модели и доступная память на GPU.

В целом, модель Whisper разработана для работы на GPU. Рекомендуемый минимальный объем видеопамяти для запуска модели Whisper — 8 ГБ, но она может использовать и больше памяти при необходимости.

Важно отметить, что при обработке большого объема данных или большого количества запросов модель может потребовать больше видеопамяти и/или возникнуть проблемы с производительностью. Рекомендуется тестировать ваш сценарий с разными настройками и контролировать использование памяти, чтобы определить оптимальные параметры для ваших задач.

## Пример E2E для интерактивного Phi 3 Mini 4K Instruct чат-бота с Whisper

Jupyter ноутбук под названием [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) демонстрирует, как использовать демонстрацию Microsoft Phi 3 Mini 4K instruct для генерации текста из аудио или письменного ввода. В ноутбуке определены несколько функций:

1. `tts_file_name(text)`: Эта функция генерирует имя файла на основе входного текста для сохранения сгенерированного аудиофайла.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Эта функция использует API Edge TTS для генерации аудиофайла из списка фрагментов текста. Входные параметры — список фрагментов, скорость речи, имя голоса и путь для сохранения сгенерированного аудиофайла.
1. `talk(input_text)`: Эта функция генерирует аудиофайл с помощью API Edge TTS и сохраняет его под случайным именем в директории /content/audio. Входной параметр — текст для преобразования в речь.
1. `run_text_prompt(message, chat_history)`: Эта функция использует демонстрацию Microsoft Phi 3 Mini 4K instruct для генерации аудиофайла из текстового сообщения и добавляет его в историю чата.
1. `run_audio_prompt(audio, chat_history)`: Эта функция преобразует аудиофайл в текст с помощью API модели Whisper и передает результат в функцию `run_text_prompt()`.
1. Код запускает приложение Gradio, которое позволяет пользователям взаимодействовать с демонстрацией Phi 3 Mini 4K instruct, вводя сообщения или загружая аудиофайлы. Результат отображается в виде текстового сообщения внутри приложения.

## Устранение неполадок

Установка драйверов Cuda для GPU

1. Убедитесь, что ваше Linux-приложение обновлено

    ```bash
    sudo apt update
    ```

1. Установите драйверы Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Зарегистрируйте расположение драйвера cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Проверка объема видеопамяти Nvidia GPU (требуется 12 ГБ видеопамяти)

    ```bash
    nvidia-smi
    ```

1. Очистка кэша: Если вы используете PyTorch, вызовите torch.cuda.empty_cache(), чтобы освободить всю неиспользуемую кэшированную память, чтобы её могли использовать другие приложения на GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Проверка Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Выполните следующие действия для создания токена Hugging Face.

    - Перейдите на [страницу настроек токенов Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Выберите **New token**.
    - Введите название проекта в поле **Name**.
    - Выберите тип **Write**.

> **Note**
>
> Если вы столкнулись с ошибкой:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Чтобы решить проблему, введите следующую команду в терминале.
>
> ```bash
> sudo ldconfig
> ```

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.