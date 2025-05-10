<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:47:32+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "nl"
}
-->
# **Inference Phi-3 op Android**

Laten we bekijken hoe je inference kunt uitvoeren met Phi-3-mini op Android-apparaten. Phi-3-mini is een nieuwe modelserie van Microsoft die het mogelijk maakt om Large Language Models (LLM’s) te gebruiken op edge-apparaten en IoT-apparaten.

## Semantic Kernel en Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) is een applicatiekader waarmee je toepassingen kunt maken die compatibel zijn met Azure OpenAI Service, OpenAI-modellen en zelfs lokale modellen. Als je nieuw bent met Semantic Kernel, raden we je aan om de [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) te bekijken.

### Toegang krijgen tot Phi-3-mini via Semantic Kernel

Je kunt het combineren met de Hugging Face Connector in Semantic Kernel. Raadpleeg deze [voorbeeldcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Standaard verwijst dit naar het model-ID op Hugging Face. Maar je kunt ook verbinding maken met een lokaal opgezet Phi-3-mini modelserver.

### Quantized modellen aanroepen met Ollama of LlamaEdge

Veel gebruikers geven de voorkeur aan het gebruik van gequantiseerde modellen om lokaal modellen te draaien. [Ollama](https://ollama.com/) en [LlamaEdge](https://llamaedge.com) maken het voor individuele gebruikers mogelijk om verschillende gequantiseerde modellen aan te roepen:

#### Ollama

Je kunt `ollama run Phi-3` direct uitvoeren of het offline configureren door een `Modelfile` te maken met het pad naar je `.gguf` bestand.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Voorbeeldcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Als je `.gguf` bestanden zowel in de cloud als op edge-apparaten tegelijk wilt gebruiken, is LlamaEdge een uitstekende keuze. Je kunt deze [voorbeeldcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) raadplegen om aan de slag te gaan.

### Installeren en draaien op Android-telefoons

1. **Download de MLC Chat-app** (gratis) voor Android-telefoons.  
2. Download het APK-bestand (148MB) en installeer het op je apparaat.  
3. Start de MLC Chat-app. Je ziet een lijst met AI-modellen, waaronder Phi-3-mini.

Samenvattend opent Phi-3-mini spannende mogelijkheden voor generatieve AI op edge-apparaten, en kun je direct aan de slag met het verkennen van de mogelijkheden op Android.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal geldt als de gezaghebbende bron. Voor belangrijke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.