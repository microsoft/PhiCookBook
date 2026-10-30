# **Инференција Phi-3 на Андроиду**

Хајде да истражимо како можете извршити инференцију са Phi-3-mini на Андроид уређајима. Phi-3-mini је нова серија модела од Microsoft-а која омогућава распоређивање великих језичких модела (LLMs) на периферним уређајима и IoT уређајима.

## Семантичко језгро и инференција

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) је оквир апликација који вам омогућава да креирате апликације компатибилне са Azure OpenAI Service, OpenAI моделима, па чак и локалним моделима. Ако сте нови у Semantic Kernel, препоручујемо да прегледате [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Како приступити Phi-3-mini користећи Semantic Kernel

Можете га комбиновати са Hugging Face конектором у Semantic Kernel-у. Погледајте овај [Пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

По дифолту, одговара ID-ју модела на Hugging Face. Међутим, такође можете повезати локално изграђени Phi-3-mini сервер модела.

### Позивање квантизованих модела са Ollama или LlamaEdge

Многи корисници преферирају коришћење квантизованих модела за локално покретање модела. [Ollama](https://ollama.com/) и [LlamaEdge](https://llamaedge.com) омогућавају појединачним корисницима да позивају различите квантизоване моделе:

#### Ollama

Можете директно покренути `ollama run Phi-3` или подесити ван мреже креирањем `Modelfile` са путем до вашег `.gguf` фајла.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ако желите да користите `.gguf` фајлове у облаку и на периферним уређајима истовремено, LlamaEdge је одличан избор. Можете погледати овај [пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) за почетак.

### Инсталирајте и покрените на Андроид телефонима

1. **Преузмите МЛЦ Чат апликацију** (бесплатно) за Андроид телефоне.
2. Преузмите APK фајл (148MB) и инсталирајте га на свој уређај.
3. Покрените МЛЦ Чат апликацију. Видећете листу AI модела, укључујући Phi-3-mini.

### Покрените Phi-4-mini-reasoning са LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) је доступан као заједнички конвертовани int4 `.litertlm` пакет за Google-ов [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) рачунски оквир на уређају. На Андроиду ради на CPU или GPU преко [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) апликације (увезите пакет са Hugging Face из апликације) или преко LiteRT-LM Kotlin API-ја; исти пакет се покреће и на iOS, macOS, Linux и Windows. Модел карта садржи измерене брзине и команде за покретање.

Укратко, Phi-3-mini отвара узбудљиве могућности за генеративни AI на периферним уређајима, и можете почети да истражујете његове способности на Андроиду.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->