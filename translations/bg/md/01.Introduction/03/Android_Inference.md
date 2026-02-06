# **Inference Phi-3 в Android**

Нека разгледаме как можете да извършите inference с Phi-3-mini на Android устройства. Phi-3-mini е нова серия модели от Microsoft, която позволява внедряване на големи езикови модели (LLMs) на edge устройства и IoT устройства.

## Semantic Kernel и Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) е рамка за приложения, която ви позволява да създавате приложения, съвместими с Azure OpenAI Service, OpenAI модели и дори локални модели. Ако сте нови в Semantic Kernel, препоръчваме да разгледате [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Как да достъпите Phi-3-mini чрез Semantic Kernel

Можете да го комбинирате с Hugging Face Connector в Semantic Kernel. Вижте този [примерен код](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

По подразбиране той съответства на model ID в Hugging Face. Въпреки това, можете също да се свържете с локално изградена Phi-3-mini модел сървър.

### Извикване на квантизирани модели с Ollama или LlamaEdge

Много потребители предпочитат да използват квантизирани модели за локално изпълнение. [Ollama](https://ollama.com/) и [LlamaEdge](https://llamaedge.com) позволяват на отделни потребители да извикват различни квантизирани модели:

#### Ollama

Можете директно да стартирате `ollama run Phi-3` или да го конфигурирате офлайн, като създадете `Modelfile` с пътя към вашия `.gguf` файл.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Примерен код](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ако искате да използвате `.gguf` файлове едновременно в облака и на edge устройства, LlamaEdge е отличен избор. Можете да се запознаете с този [примерен код](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo), за да започнете.

### Инсталиране и стартиране на Android телефони

1. **Изтеглете приложението MLC Chat** (безплатно) за Android телефони.  
2. Изтеглете APK файла (148MB) и го инсталирайте на устройството си.  
3. Стартирайте приложението MLC Chat. Ще видите списък с AI модели, включително Phi-3-mini.

В обобщение, Phi-3-mini отваря вълнуващи възможности за генеративен AI на edge устройства и можете да започнете да изследвате неговите възможности на Android.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.