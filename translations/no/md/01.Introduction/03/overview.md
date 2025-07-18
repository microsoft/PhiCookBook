<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:10:59+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "no"
}
-->
I sammenheng med Phi-3-mini refererer inferens til prosessen med å bruke modellen til å gjøre prediksjoner eller generere resultater basert på inndata. La meg gi deg mer informasjon om Phi-3-mini og dens inferensevner.

Phi-3-mini er en del av Phi-3-serien av modeller utgitt av Microsoft. Disse modellene er designet for å redefinere hva som er mulig med små språkmodeller (SLM).

Her er noen viktige punkter om Phi-3-mini og dens inferensevner:

## **Oversikt over Phi-3-mini:**
- Phi-3-mini har en parameterstørrelse på 3,8 milliarder.
- Den kan kjøre ikke bare på tradisjonelle datamaskiner, men også på edge-enheter som mobiltelefoner og IoT-enheter.
- Lanseringen av Phi-3-mini gjør det mulig for både enkeltpersoner og bedrifter å distribuere SLM-er på ulike maskinvareenheter, spesielt i miljøer med begrensede ressurser.
- Den støtter flere modellformater, inkludert det tradisjonelle PyTorch-formatet, den kvantiserte versjonen av gguf-formatet, og den ONNX-baserte kvantiserte versjonen.

## **Tilgang til Phi-3-mini:**
For å få tilgang til Phi-3-mini kan du bruke [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) i en Copilot-applikasjon. Semantic Kernel er generelt kompatibel med Azure OpenAI Service, open source-modeller på Hugging Face, og lokale modeller.  
Du kan også bruke [Ollama](https://ollama.com) eller [LlamaEdge](https://llamaedge.com) for å kalle kvantiserte modeller. Ollama lar individuelle brukere kalle ulike kvantiserte modeller, mens LlamaEdge tilbyr plattformuavhengig tilgjengelighet for GGUF-modeller.

## **Kvantiserte modeller:**
Mange brukere foretrekker å bruke kvantiserte modeller for lokal inferens. For eksempel kan du kjøre Ollama direkte med Phi-3 eller konfigurere det offline ved hjelp av en Modelfile. Modelfilen spesifiserer GGUF-filens bane og promptformatet.

## **Muligheter med generativ AI:**
Kombinasjonen av SLM-er som Phi-3-mini åpner for nye muligheter innen generativ AI. Inferens er bare det første steget; disse modellene kan brukes til ulike oppgaver i miljøer med begrensede ressurser, lav ventetid og kostnadsbegrensninger.

## **Åpne opp for generativ AI med Phi-3-mini: En guide til inferens og distribusjon**  
Lær hvordan du bruker Semantic Kernel, Ollama/LlamaEdge og ONNX Runtime for å få tilgang til og kjøre inferens på Phi-3-mini-modeller, og utforsk mulighetene for generativ AI i ulike applikasjonsscenarier.

**Funksjoner**  
Inferens av phi3-mini-modellen i:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Oppsummert gir Phi-3-mini utviklere muligheten til å utforske ulike modellformater og utnytte generativ AI i forskjellige applikasjonsscenarier.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.