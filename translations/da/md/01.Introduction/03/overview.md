<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:26:34+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "da"
}
-->
I forbindelse med Phi-3-mini refererer inference til processen med at bruge modellen til at lave forudsigelser eller generere output baseret på inputdata. Lad mig give dig flere detaljer om Phi-3-mini og dens inference-muligheder.

Phi-3-mini er en del af Phi-3-serien af modeller udgivet af Microsoft. Disse modeller er designet til at gendefinere, hvad der er muligt med Small Language Models (SLMs).

Her er nogle nøglepunkter om Phi-3-mini og dens inference-muligheder:

## **Phi-3-mini Oversigt:**
- Phi-3-mini har en parameterstørrelse på 3,8 milliarder.
- Den kan køre ikke kun på traditionelle computerenheder, men også på edge-enheder såsom mobiltelefoner og IoT-enheder.
- Udgivelsen af Phi-3-mini gør det muligt for både enkeltpersoner og virksomheder at implementere SLMs på forskellige hardwareenheder, især i miljøer med begrænsede ressourcer.
- Den understøtter forskellige modelformater, herunder det traditionelle PyTorch-format, den kvantiserede version af gguf-formatet og den ONNX-baserede kvantiserede version.

## **Adgang til Phi-3-mini:**
For at få adgang til Phi-3-mini kan du bruge [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) i en Copilot-applikation. Semantic Kernel er generelt kompatibel med Azure OpenAI Service, open source-modeller på Hugging Face og lokale modeller.  
Du kan også bruge [Ollama](https://ollama.com) eller [LlamaEdge](https://llamaedge.com) til at kalde kvantiserede modeller. Ollama tillader individuelle brugere at kalde forskellige kvantiserede modeller, mens LlamaEdge tilbyder tværplatform-tilgængelighed for GGUF-modeller.

## **Kvantiserede modeller:**
Mange brugere foretrækker at bruge kvantiserede modeller til lokal inference. For eksempel kan du direkte køre Ollama run Phi-3 eller konfigurere det offline ved hjælp af en Modelfile. Modelfilen specificerer GGUF-filens sti og promptformatet.

## **Generative AI-muligheder:**
Kombinationen af SLMs som Phi-3-mini åbner op for nye muligheder inden for generativ AI. Inference er kun det første skridt; disse modeller kan bruges til forskellige opgaver i ressourcebegrænsede, latenstidssensitive og omkostningsbegrænsede scenarier.

## **Unlocking Generative AI with Phi-3-mini: A Guide to Inference and Deployment**  
Lær, hvordan du bruger Semantic Kernel, Ollama/LlamaEdge og ONNX Runtime til at få adgang til og køre inference på Phi-3-mini-modeller, og udforsk mulighederne for generativ AI i forskellige anvendelsesscenarier.

**Funktioner**  
Inference af phi3-mini model i:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Sammenfattende giver Phi-3-mini udviklere mulighed for at udforske forskellige modelformater og udnytte generativ AI i forskellige anvendelsesscenarier.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.