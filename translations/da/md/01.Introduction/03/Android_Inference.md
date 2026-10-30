# **Inference Phi-3 på Android**

Lad os udforske, hvordan du kan udføre inference med Phi-3-mini på Android-enheder. Phi-3-mini er en ny serie af modeller fra Microsoft, der muliggør implementering af Large Language Models (LLM'er) på edge-enheder og IoT-enheder.

## Semantic Kernel og Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) er et applikationsframework, der giver dig mulighed for at skabe applikationer kompatible med Azure OpenAI Service, OpenAI-modeller og endda lokale modeller. Hvis du er ny til Semantic Kernel, foreslår vi, at du kigger på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### For at få adgang til Phi-3-mini ved brug af Semantic Kernel

Du kan kombinere det med Hugging Face Connector i Semantic Kernel. Se denne [eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard svarer det til model-ID'et på Hugging Face. Men du kan også forbinde til en lokalt opbygget Phi-3-mini modelserver.

### Kald af kvantiserede modeller med Ollama eller LlamaEdge

Mange brugere foretrækker at bruge kvantiserede modeller for at køre modeller lokalt. [Ollama](https://ollama.com/) og [LlamaEdge](https://llamaedge.com) giver individuelle brugere mulighed for at kalde forskellige kvantiserede modeller:

#### Ollama

Du kan køre `ollama run Phi-3` direkte eller konfigurere det offline ved at oprette en `Modelfile` med stien til din `.gguf` fil.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Hvis du vil bruge `.gguf` filer i skyen og på edge-enheder samtidig, er LlamaEdge et godt valg. Du kan henholde dig til denne [eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) for at komme i gang.

### Installer og kør på Android-telefoner

1. **Download MLC Chat-appen** (gratis) til Android-telefoner.
2. Download APK-filen (148MB) og installer den på din enhed.
3. Start MLC Chat-appen. Du vil se en liste over AI-modeller, inklusive Phi-3-mini.

### Kør Phi-4-mini-reasoning med LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) er tilgængelig som en community-konverteret int4 `.litertlm` pakke til Googles [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) on-device runtime. På Android kører det på CPU eller GPU gennem [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) appen (importer pakken fra Hugging Face inde i appen) eller gennem LiteRT-LM Kotlin API; den samme pakke kører også på iOS, macOS, Linux og Windows. Modelkortet opregner de målte hastigheder og kørselskommandoer.

Samlet set åbner Phi-3-mini spændende muligheder for generativ AI på edge-enheder, og du kan begynde at udforske dens kapaciteter på Android.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->