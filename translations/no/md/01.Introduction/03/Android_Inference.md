# **Inference Phi-3 på Android**

La oss utforske hvordan du kan utføre inferens med Phi-3-mini på Android-enheter. Phi-3-mini er en ny serie modeller fra Microsoft som muliggjør distribusjon av store språkmodeller (LLMs) på edge-enheter og IoT-enheter.

## Semantic Kernel og inferens

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) er et rammeverk for applikasjoner som lar deg lage applikasjoner kompatible med Azure OpenAI Service, OpenAI-modeller og til og med lokale modeller. Hvis du er ny på Semantic Kernel, foreslår vi at du ser på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### For å få tilgang til Phi-3-mini ved bruk av Semantic Kernel

Du kan kombinere det med Hugging Face Connector i Semantic Kernel. Se dette [eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard tilsvarer det modell-ID-en på Hugging Face. Du kan imidlertid også koble til en lokalt bygget Phi-3-mini modellserver.

### Kjøre kvantiserte modeller med Ollama eller LlamaEdge

Mange brukere foretrekker å bruke kvantiserte modeller for å kjøre modeller lokalt. [Ollama](https://ollama.com/) og [LlamaEdge](https://llamaedge.com) lar individuelle brukere kjøre ulike kvantiserte modeller:

#### Ollama

Du kan kjøre `ollama run Phi-3` direkte eller konfigurere det offline ved å lage en `Modelfile` med stien til `.gguf`-filen din.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Hvis du vil bruke `.gguf`-filer i skyen og på edge-enheter samtidig, er LlamaEdge et godt valg. Du kan se denne [eksempelkoden](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) for å komme i gang.

### Installer og kjør på Android-telefoner

1. **Last ned MLC Chat-appen** (gratis) for Android-telefoner.
2. Last ned APK-filen (148MB) og installer den på enheten din.
3. Start MLC Chat-appen. Du vil se en liste over AI-modeller, inkludert Phi-3-mini.

### Kjør Phi-4-mini-resonnering med LiteRT-LM

[Phi-4-mini-resonnering](https://huggingface.co/litert-community/Phi-4-mini-reasoning) er tilgjengelig som en fellesskaps-konvertert int4 `.litertlm` pakke for Googles [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) enhetsbaserte runtime. På Android kjører den på CPU eller GPU gjennom [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery)-appen (importer pakken fra Hugging Face inne i appen) eller gjennom LiteRT-LM Kotlin API; samme pakke kjører også på iOS, macOS, Linux og Windows. Modellkortet lister opp målte hastigheter og kjørekommandoer.

Oppsummert åpner Phi-3-mini spennende muligheter for generativ AI på edge-enheter, og du kan begynne å utforske dens kapasiteter på Android.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->