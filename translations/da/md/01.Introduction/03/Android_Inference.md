<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:14:08+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "da"
}
-->
# **Inference Phi-3 på Android**

Lad os se på, hvordan du kan udføre inference med Phi-3-mini på Android-enheder. Phi-3-mini er en ny modelserie fra Microsoft, der muliggør implementering af Large Language Models (LLMs) på edge-enheder og IoT-enheder.

## Semantic Kernel og Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) er et applikationsframework, der giver dig mulighed for at skabe applikationer, der er kompatible med Azure OpenAI Service, OpenAI-modeller og endda lokale modeller. Hvis du er ny til Semantic Kernel, anbefaler vi, at du kigger på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### For at få adgang til Phi-3-mini via Semantic Kernel

Du kan kombinere det med Hugging Face Connector i Semantic Kernel. Se dette [eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard svarer det til model-ID’et på Hugging Face. Men du kan også forbinde til en lokalt opbygget Phi-3-mini modelserver.

### Kald kvantiserede modeller med Ollama eller LlamaEdge

Mange brugere foretrækker at bruge kvantiserede modeller for at køre modeller lokalt. [Ollama](https://ollama.com/) og [LlamaEdge](https://llamaedge.com) giver individuelle brugere mulighed for at kalde forskellige kvantiserede modeller:

#### Ollama

Du kan køre `ollama run Phi-3` direkte eller konfigurere det offline ved at oprette en `Modelfile` med stien til din `.gguf`-fil.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Hvis du vil bruge `.gguf`-filer både i skyen og på edge-enheder samtidig, er LlamaEdge et godt valg. Du kan se denne [eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) for at komme i gang.

### Installer og kør på Android-telefoner

1. **Download MLC Chat-appen** (gratis) til Android-telefoner.  
2. Download APK-filen (148MB) og installer den på din enhed.  
3. Start MLC Chat-appen. Du vil se en liste over AI-modeller, inklusive Phi-3-mini.

Sammenfattende åbner Phi-3-mini spændende muligheder for generativ AI på edge-enheder, og du kan begynde at udforske dens funktioner på Android.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.