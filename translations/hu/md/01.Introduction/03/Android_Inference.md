# **Phi-3 következtetés Androidon**

Nézzük meg, hogyan végezhetsz következtetést Phi-3-mini modellel Android eszközökön. A Phi-3-mini a Microsoft új modellcsaládja, amely lehetővé teszi a nagy nyelvi modellek (LLM-ek) telepítését élő eszközökön és IoT eszközökön.

## Semantic Kernel és következtetés

A [Semantic Kernel](https://github.com/microsoft/semantic-kernel) egy alkalmazáskeret, amely lehetővé teszi olyan alkalmazások létrehozását, amelyek kompatibilisek az Azure OpenAI Service-szel, OpenAI modellekkel, sőt helyi modellekkel is. Ha még nem ismered a Semantic Kernel-t, javasoljuk, hogy nézd meg a [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) anyagát.

### Phi-3-mini elérése Semantic Kernel segítségével

Összekapcsolhatod a Semantic Kernel Hugging Face Connectorával. Ehhez lásd ezt a [példakódot](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Alapértelmezés szerint a Hugging Face-en található modellazonosítónak felel meg, de csatlakozhatsz helyileg futó Phi-3-mini modell szerverhez is.

### Kvantált modellek hívása Ollama vagy LlamaEdge segítségével

Sokan előnyben részesítik a kvantált modellek használatát a helyi futtatáshoz. Az [Ollama](https://ollama.com/) és a [LlamaEdge](https://llamaedge.com) lehetőséget adnak egyéni felhasználóknak különböző kvantált modellek hívására:

#### Ollama

Egyszerűen futtathatod az `ollama run Phi-3` parancsot, vagy offline konfigurálhatod egy `Modelfile` létrehozásával, amely a `.gguf` fájl elérési útját tartalmazza.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Példakód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ha egyszerre szeretnéd használni a `.gguf` fájlokat felhőben és élő eszközökön, a LlamaEdge kiváló választás. Ehhez ezt a [példakódot](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ajánljuk.

### Telepítés és futtatás Android telefonokon

1. **Töltsd le az MLC Chat alkalmazást** (ingyenes) Android telefonokra.
2. Töltsd le az APK fájlt (148MB), és telepítsd az eszközödre.
3. Indítsd el az MLC Chat alkalmazást. Megjelenik az AI modellek listája, köztük a Phi-3-mini is.

Összefoglalva, a Phi-3-mini izgalmas lehetőségeket nyit a generatív AI számára élő eszközökön, és Androidon is elkezdheted felfedezni a képességeit.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.