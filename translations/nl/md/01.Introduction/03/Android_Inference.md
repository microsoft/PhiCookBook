# **Inference Phi-3 op Android**

Laten we bekijken hoe je inference kunt uitvoeren met Phi-3-mini op Android-apparaten. Phi-3-mini is een nieuwe serie modellen van Microsoft die de uitrol van Large Language Models (LLM's) op edge-apparaten en IoT-apparaten mogelijk maakt.

## Semantic Kernel en Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) is een applicatiekader waarmee je applicaties kunt maken die compatibel zijn met Azure OpenAI Service, OpenAI-modellen en zelfs lokale modellen. Als je nieuw bent met Semantic Kernel, raden we aan om te kijken naar de [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Toegang krijgen tot Phi-3-mini met Semantic Kernel

Je kunt het combineren met de Hugging Face Connector in Semantic Kernel. Zie deze [voorbeeldcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Standaard komt dit overeen met het model-ID op Hugging Face. Je kunt echter ook verbinding maken met een lokaal gebouwd Phi-3-mini modelserver.

### Aangeroepen van gequantiseerde modellen met Ollama of LlamaEdge

Veel gebruikers geven de voorkeur aan het gebruiken van gequantiseerde modellen om modellen lokaal uit te voeren. [Ollama](https://ollama.com/) en [LlamaEdge](https://llamaedge.com) stellen individuele gebruikers in staat om verschillende gequantiseerde modellen aan te roepen:

#### Ollama

Je kunt direct `ollama run Phi-3` uitvoeren of het offline configureren door een `Modelfile` te maken met het pad naar je `.gguf` bestand.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Voorbeeldcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Als je `.gguf` bestanden tegelijk in de cloud en op edge-apparaten wilt gebruiken, is LlamaEdge een uitstekende keuze. Je kunt deze [voorbeeldcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) raadplegen om aan de slag te gaan.

### Installeren en uitvoeren op Android-telefoons

1. **Download de MLC Chat-app** (gratis) voor Android-telefoons.
2. Download het APK-bestand (148MB) en installeer het op je apparaat.
3. Start de MLC Chat-app. Je ziet een lijst met AI-modellen, inclusief Phi-3-mini.

### Phi-4-mini-reasoning uitvoeren met LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) is beschikbaar als een community-geconverteerde int4 `.litertlm` bundel voor Google's [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) on-device runtime. Op Android draait het op CPU of GPU via de [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) app (importeert de bundel van Hugging Face binnen de app) of via de LiteRT-LM Kotlin API; dezelfde bundel draait ook op iOS, macOS, Linux en Windows. De modelkaart vermeldt de gemeten snelheden en de uitvoercommando's.

Samenvattend opent Phi-3-mini spannende mogelijkheden voor generatieve AI op edge-apparaten, en je kunt beginnen met het verkennen van de mogelijkheden op Android.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->