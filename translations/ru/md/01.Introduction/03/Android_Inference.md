<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-03-27T07:07:12+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "ru"
}
-->
# **Inference Phi-3 на Android**

Давайте рассмотрим, как можно выполнять вывод с использованием Phi-3-mini на устройствах Android. Phi-3-mini — это новая серия моделей от Microsoft, которая позволяет внедрять крупные языковые модели (LLMs) на устройствах периферии и IoT.

## Semantic Kernel и вывод

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) — это фреймворк для создания приложений, совместимых с Azure OpenAI Service, моделями OpenAI и даже локальными моделями. Если вы новичок в Semantic Kernel, рекомендуем ознакомиться с [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Доступ к Phi-3-mini через Semantic Kernel

Вы можете использовать его вместе с коннектором Hugging Face в Semantic Kernel. Ознакомьтесь с этим [примером кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

По умолчанию он соответствует идентификатору модели на Hugging Face. Однако вы также можете подключиться к локальному серверу модели Phi-3-mini.

### Вызов квантованных моделей с помощью Ollama или LlamaEdge

Многие пользователи предпочитают использовать квантованные модели для локального запуска. [Ollama](https://ollama.com/) и [LlamaEdge](https://llamaedge.com) позволяют индивидуальным пользователям вызывать различные квантованные модели:

#### Ollama

Вы можете напрямую запустить `ollama run Phi-3` или настроить его офлайн, создав `Modelfile` с путем к вашему файлу `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Если вы хотите использовать файлы `.gguf` одновременно в облаке и на устройствах периферии, LlamaEdge — отличный выбор. Вы можете ознакомиться с этим [примером кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo), чтобы начать.

### Установка и запуск на Android-устройствах

1. **Скачайте приложение MLC Chat** (бесплатно) для Android-устройств.
2. Скачайте APK-файл (148MB) и установите его на устройство.
3. Запустите приложение MLC Chat. Вы увидите список AI-моделей, включая Phi-3-mini.

В итоге, Phi-3-mini открывает захватывающие возможности для генеративного ИИ на устройствах периферии, и вы можете начать исследовать его возможности на Android.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверные интерпретации, возникшие в результате использования данного перевода.