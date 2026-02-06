# **Inference Phi-3 på Android**

Låt oss utforska hur du kan göra inferens med Phi-3-mini på Android-enheter. Phi-3-mini är en ny modellserie från Microsoft som möjliggör distribution av stora språkmodeller (LLMs) på edge-enheter och IoT-enheter.

## Semantic Kernel och inferens

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) är ett applikationsramverk som låter dig skapa applikationer kompatibla med Azure OpenAI Service, OpenAI-modeller och även lokala modeller. Om du är ny på Semantic Kernel rekommenderar vi att du tittar på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### För att komma åt Phi-3-mini med Semantic Kernel

Du kan kombinera det med Hugging Face Connector i Semantic Kernel. Se detta [exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard motsvarar det modell-ID:t på Hugging Face. Men du kan också ansluta till en lokalt uppbyggd Phi-3-mini-modellserver.

### Anropa kvantiserade modeller med Ollama eller LlamaEdge

Många användare föredrar att använda kvantiserade modeller för att köra modeller lokalt. [Ollama](https://ollama.com/) och [LlamaEdge](https://llamaedge.com) låter individuella användare anropa olika kvantiserade modeller:

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

Om du vill använda `.gguf`-filer både i molnet och på edge-enheter samtidigt är LlamaEdge ett utmärkt val. Du kan titta på denna [exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) för att komma igång.

### Installera och kör på Android-telefoner

1. **Ladda ner MLC Chat-appen** (gratis) för Android-telefoner.  
2. Ladda ner APK-filen (148MB) och installera den på din enhet.  
3. Starta MLC Chat-appen. Du kommer att se en lista med AI-modeller, inklusive Phi-3-mini.

Sammanfattningsvis öppnar Phi-3-mini upp spännande möjligheter för generativ AI på edge-enheter, och du kan börja utforska dess kapabiliteter på Android.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.