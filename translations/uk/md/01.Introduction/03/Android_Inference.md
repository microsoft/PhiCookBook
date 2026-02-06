# **Inference Phi-3 на Android**

Давайте розглянемо, як можна виконувати інференс з Phi-3-mini на пристроях Android. Phi-3-mini — це нова серія моделей від Microsoft, яка дозволяє розгортати великі мовні моделі (LLM) на пристроях на периферії та в IoT.

## Semantic Kernel та інференс

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) — це фреймворк для створення додатків, сумісних із Azure OpenAI Service, моделями OpenAI та навіть локальними моделями. Якщо ви новачок у Semantic Kernel, радимо ознайомитися з [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Як отримати доступ до Phi-3-mini за допомогою Semantic Kernel

Ви можете поєднати його з Hugging Face Connector у Semantic Kernel. Ознайомтеся з цим [прикладом коду](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

За замовчуванням він відповідає ідентифікатору моделі на Hugging Face. Проте ви також можете підключитися до локального сервера моделі Phi-3-mini.

### Виклик квантизованих моделей за допомогою Ollama або LlamaEdge

Багато користувачів віддають перевагу квантизованим моделям для запуску моделей локально. [Ollama](https://ollama.com/) та [LlamaEdge](https://llamaedge.com) дозволяють окремим користувачам викликати різні квантизовані моделі:

#### Ollama

Ви можете безпосередньо запустити `ollama run Phi-3` або налаштувати офлайн, створивши `Modelfile` з шляхом до вашого `.gguf` файлу.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Приклад коду](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Якщо ви хочете використовувати `.gguf` файли одночасно в хмарі та на пристроях на периферії, LlamaEdge — чудовий вибір. Ви можете скористатися цим [прикладом коду](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo), щоб почати.

### Встановлення та запуск на Android

1. **Завантажте додаток MLC Chat** (безкоштовно) для Android.
2. Завантажте APK-файл (148 МБ) та встановіть його на свій пристрій.
3. Запустіть додаток MLC Chat. Ви побачите список AI-моделей, включно з Phi-3-mini.

Підсумовуючи, Phi-3-mini відкриває захопливі можливості для генеративного ШІ на пристроях на периферії, і ви можете почати досліджувати його можливості на Android.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.