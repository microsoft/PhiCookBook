# **Inferens Phi-3 på Android**

Låt oss utforska hur du kan utföra inferens med Phi-3-mini på Android-enheter. Phi-3-mini är en ny modellserie från Microsoft som möjliggör distribution av stora språkmodeller (LLMs) på edge-enheter och IoT-enheter.

## Semantic Kernel och Inferens

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) är ett applikationsramverk som låter dig skapa applikationer kompatibla med Azure OpenAI Service, OpenAI-modeller och även lokala modeller. Om du är ny till Semantic Kernel rekommenderar vi att du tittar på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### För att få tillgång till Phi-3-mini med Semantic Kernel

Du kan kombinera det med Hugging Face Connector i Semantic Kernel. Se detta [exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard motsvarar det modell-ID på Hugging Face. Men du kan också ansluta till en lokalt byggd Phi-3-mini modellserver.

### Anropa kvantiserade modeller med Ollama eller LlamaEdge

Många användare föredrar att använda kvantiserade modeller för att köra modeller lokalt. [Ollama](https://ollama.com/) och [LlamaEdge](https://llamaedge.com) tillåter individuella användare att anropa olika kvantiserade modeller:

#### Ollama

Du kan köra `ollama run Phi-3` direkt eller konfigurera det offline genom att skapa en `Modelfile` med sökvägen till din `.gguf`-fil.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Om du vill använda `.gguf`-filer i molnet och på edge-enheter samtidigt är LlamaEdge ett utmärkt val. Du kan se denna [exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) för att komma igång.

### Installera och kör på Android-telefoner

1. **Ladda ner MLC Chat-appen** (Gratis) för Android-telefoner.
2. Ladda ner APK-filen (148MB) och installera den på din enhet.
3. Starta MLC Chat-appen. Du kommer att se en lista över AI-modeller, inklusive Phi-3-mini.

### Kör Phi-4-mini-reasoning med LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) finns tillgänglig som ett community-konverterat int4 `.litertlm` paket för Googles [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) körning på enheten. På Android körs den på CPU eller GPU via [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) appen (importera paketet från Hugging Face inuti appen) eller via LiteRT-LM Kotlin API; samma paket fungerar också på iOS, macOS, Linux och Windows. Modellkortet listar de uppmätta hastigheterna och körkommandona.

Sammanfattningsvis öppnar Phi-3-mini upp spännande möjligheter för generativ AI på edge-enheter, och du kan börja utforska dess kapaciteter på Android.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->