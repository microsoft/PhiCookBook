<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-07T14:31:26+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ru"
}
-->
# **Инференс Phi-3 на Android**

Давайте рассмотрим, как можно выполнять инференс с Phi-3-mini на устройствах Android. Phi-3-mini — это новая серия моделей от Microsoft, которая позволяет запускать большие языковые модели (LLM) на edge-устройствах и устройствах Интернета вещей.

## Semantic Kernel и инференс

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) — это фреймворк для создания приложений, совместимых с Azure OpenAI Service, моделями OpenAI и даже локальными моделями. Если вы новичок в Semantic Kernel, рекомендуем ознакомиться с [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Доступ к Phi-3-mini через Semantic Kernel

Вы можете использовать его вместе с Hugging Face Connector в Semantic Kernel. Смотрите этот [пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

По умолчанию используется модель с Hugging Face, но также можно подключиться к локальному серверу модели Phi-3-mini.

### Вызов квантизированных моделей с помощью Ollama или LlamaEdge

Многие пользователи предпочитают запускать квантизированные модели локально. [Ollama](https://ollama.com/) и [LlamaEdge](https://llamaedge.com) позволяют индивидуальным пользователям работать с разными квантизированными моделями:

#### Ollama

Вы можете запустить `ollama run Phi-3` напрямую или настроить офлайн, создав `Modelfile` с указанием пути к вашему файлу `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Если хотите использовать `.gguf` файлы одновременно в облаке и на edge-устройствах, LlamaEdge — отличный выбор. Начать можно с этого [примера кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Установка и запуск на Android

1. **Скачайте приложение MLC Chat** (бесплатно) для Android.
2. Загрузите APK-файл (148 МБ) и установите его на устройство.
3. Запустите MLC Chat. Вы увидите список AI-моделей, включая Phi-3-mini.

В итоге, Phi-3-mini открывает новые возможности для генеративного ИИ на edge-устройствах, и вы можете начать исследовать его возможности на Android.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.