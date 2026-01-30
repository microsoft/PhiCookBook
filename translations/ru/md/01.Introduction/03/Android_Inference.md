# **Инференс Phi-3 на Android**

Давайте рассмотрим, как можно выполнять инференс с Phi-3-mini на устройствах Android. Phi-3-mini — это новая серия моделей от Microsoft, которая позволяет запускать большие языковые модели (LLM) на периферийных устройствах и в IoT.

## Semantic Kernel и инференс

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) — это фреймворк для создания приложений, совместимых с Azure OpenAI Service, моделями OpenAI и даже локальными моделями. Если вы новичок в Semantic Kernel, рекомендуем ознакомиться с [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Доступ к Phi-3-mini через Semantic Kernel

Вы можете использовать его вместе с Hugging Face Connector в Semantic Kernel. Смотрите этот [пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

По умолчанию используется модель с идентификатором на Hugging Face. Однако вы также можете подключиться к локальному серверу модели Phi-3-mini.

### Вызов квантизированных моделей с помощью Ollama или LlamaEdge

Многие пользователи предпочитают использовать квантизированные модели для локального запуска. [Ollama](https://ollama.com/) и [LlamaEdge](https://llamaedge.com) позволяют индивидуальным пользователям вызывать различные квантизированные модели:

#### Ollama

Вы можете напрямую запустить `ollama run Phi-3` или настроить офлайн, создав `Modelfile` с указанием пути к вашему `.gguf` файлу.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Если вы хотите использовать `.gguf` файлы одновременно в облаке и на периферийных устройствах, LlamaEdge — отличный выбор. Для начала работы смотрите этот [пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Установка и запуск на Android

1. **Скачайте приложение MLC Chat** (бесплатно) для Android.
2. Скачайте APK-файл (148 МБ) и установите его на устройство.
3. Запустите приложение MLC Chat. Вы увидите список AI-моделей, включая Phi-3-mini.

В итоге, Phi-3-mini открывает новые возможности для генеративного ИИ на периферийных устройствах, и вы можете начать изучать его возможности на Android.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.