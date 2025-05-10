<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:50:30+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "hu"
}
-->
# **Phi-3 inferencia Androidon**

Nézzük meg, hogyan végezhetünk inferenciát a Phi-3-mini segítségével Android eszközökön. A Phi-3-mini a Microsoft új modellcsaládja, amely lehetővé teszi a nagyméretű nyelvi modellek (LLM-ek) telepítését élőhelyi és IoT eszközökön.

## Semantic Kernel és inferencia

A [Semantic Kernel](https://github.com/microsoft/semantic-kernel) egy alkalmazáskeret, amely lehetővé teszi, hogy olyan alkalmazásokat hozz létre, amelyek kompatibilisek az Azure OpenAI Service-szel, az OpenAI modellekkel, sőt akár helyi modellekkel is. Ha még nem ismered a Semantic Kernel-t, javasoljuk, hogy nézd meg a [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) anyagát.

### Phi-3-mini elérése a Semantic Kernel segítségével

Összekapcsolhatod a Semantic Kernel-t a Hugging Face Connectorral. Ehhez lásd ezt a [példakódot](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Alapértelmezés szerint a Hugging Face-en található modellazonosítóhoz kapcsolódik. Ugyanakkor csatlakozhatsz helyileg futtatott Phi-3-mini modell szerverhez is.

### Kvantált modellek használata Ollama vagy LlamaEdge segítségével

Sokan előnyben részesítik a kvantált modellek helyi futtatását. Az [Ollama](https://ollama.com/) és a [LlamaEdge](https://llamaedge.com) lehetőséget adnak az egyéni felhasználóknak, hogy különböző kvantált modelleket hívjanak meg:

#### Ollama

Közvetlenül futtathatod a `ollama run Phi-3`-t, vagy offline konfigurálhatod egy `Modelfile` létrehozásával, amely tartalmazza a `.gguf` fájl elérési útját.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Példakód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ha egyszerre szeretnéd használni a `.gguf` fájlokat a felhőben és élőhelyi eszközökön, a LlamaEdge remek választás. Ehhez ezt a [példakódot](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ajánljuk.

### Telepítés és futtatás Android telefonokon

1. **Töltsd le az MLC Chat alkalmazást** (ingyenes) Android telefonokra.
2. Töltsd le az APK fájlt (148MB), majd telepítsd az eszközödre.
3. Indítsd el az MLC Chat alkalmazást. Láthatod az AI modellek listáját, köztük a Phi-3-mini-t.

Összefoglalva, a Phi-3-mini izgalmas lehetőségeket nyit a generatív AI számára élőhelyi eszközökön, és Androidon már elkezdheted felfedezni a képességeit.

**Nyilatkozat:**  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.