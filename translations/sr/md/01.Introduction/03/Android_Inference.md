<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:16:13+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "sr"
}
-->
# **Инференција Phi-3 на Андроиду**

Хајде да истражимо како можете извршити инференцију са Phi-3-mini на Андроид уређајима. Phi-3-mini је нова серија модела из Microsoft-а која омогућава покретање великих језичких модела (LLM) на уређајима на ивици мреже и IoT уређајима.

## Semantic Kernel и инференција

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) је апликациони оквир који вам омогућава да креирате апликације компатибилне са Azure OpenAI Service, OpenAI моделима, па чак и локалним моделима. Ако сте нови у Semantic Kernel-у, препоручујемо да погледате [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Како приступити Phi-3-mini користећи Semantic Kernel

Можете га комбиновати са Hugging Face Connector-ом у Semantic Kernel-у. Погледајте овај [пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Подразумевано, одговара моделу са Hugging Face-а. Међутим, можете се повезати и на локално изграђени Phi-3-mini сервер модела.

### Позивање квантованих модела помоћу Ollama или LlamaEdge

Многи корисници више воле да користе квантоване моделе за локално покретање модела. [Ollama](https://ollama.com/) и [LlamaEdge](https://llamaedge.com) омогућавају појединцима да позивају различите квантоване моделе:

#### Ollama

Можете директно покренути `ollama run Phi-3` или га конфигурисати офлајн креирањем `Modelfile` са путањом до вашег `.gguf` фајла.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ако желите да користите `.gguf` фајлове у облаку и на уређајима на ивици мреже истовремено, LlamaEdge је одличан избор. Можете погледати овај [пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) за почетак.

### Инсталација и покретање на Андроид телефонима

1. **Преузмите MLC Chat апликацију** (бесплатно) за Андроид телефоне.  
2. Преузмите APK фајл (148MB) и инсталирајте га на свој уређај.  
3. Покрените MLC Chat апликацију. Видећете листу AI модела, укључујући Phi-3-mini.

Укратко, Phi-3-mini отвара узбудљиве могућности за генеративну вештачку интелигенцију на уређајима на ивици мреже, и можете почети да истражујете његове могућности на Андроиду.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.