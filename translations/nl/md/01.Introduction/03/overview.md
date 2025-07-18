<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:11:18+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "nl"
}
-->
In de context van Phi-3-mini verwijst inferentie naar het proces waarbij het model wordt gebruikt om voorspellingen te doen of output te genereren op basis van invoergegevens. Ik geef je graag meer details over Phi-3-mini en de inferentiemogelijkheden ervan.

Phi-3-mini maakt deel uit van de Phi-3-serie modellen die door Microsoft zijn uitgebracht. Deze modellen zijn ontworpen om de mogelijkheden van Small Language Models (SLM's) opnieuw te definiëren.

Hier zijn enkele belangrijke punten over Phi-3-mini en de inferentiemogelijkheden:

## **Overzicht Phi-3-mini:**
- Phi-3-mini heeft een parameteromvang van 3,8 miljard.
- Het kan niet alleen draaien op traditionele computers, maar ook op edge-apparaten zoals mobiele apparaten en IoT-apparaten.
- De release van Phi-3-mini maakt het voor individuen en bedrijven mogelijk om SLM's te implementeren op verschillende hardware, vooral in omgevingen met beperkte middelen.
- Het ondersteunt diverse modelformaten, waaronder het traditionele PyTorch-formaat, de gekwantiseerde versie van het gguf-formaat en de op ONNX gebaseerde gekwantiseerde versie.

## **Toegang tot Phi-3-mini:**
Om toegang te krijgen tot Phi-3-mini kun je [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) gebruiken in een Copilot-applicatie. Semantic Kernel is over het algemeen compatibel met Azure OpenAI Service, open-source modellen op Hugging Face en lokale modellen.  
Je kunt ook [Ollama](https://ollama.com) of [LlamaEdge](https://llamaedge.com) gebruiken om gekwantiseerde modellen aan te roepen. Ollama stelt individuele gebruikers in staat verschillende gekwantiseerde modellen te gebruiken, terwijl LlamaEdge cross-platform beschikbaarheid biedt voor GGUF-modellen.

## **Gekwantiseerde modellen:**
Veel gebruikers geven de voorkeur aan gekwantiseerde modellen voor lokale inferentie. Zo kun je bijvoorbeeld Ollama direct gebruiken om Phi-3 uit te voeren of het offline configureren met een Modelfile. De Modelfile specificeert het GGUF-bestandspad en het promptformaat.

## **Mogelijkheden van Generatieve AI:**
Het combineren van SLM's zoals Phi-3-mini opent nieuwe mogelijkheden voor generatieve AI. Inferentie is slechts de eerste stap; deze modellen kunnen worden ingezet voor diverse taken in omgevingen met beperkte middelen, lage latency en kostenbeperkingen.

## **Generatieve AI ontgrendelen met Phi-3-mini: Een gids voor inferentie en implementatie**  
Leer hoe je Semantic Kernel, Ollama/LlamaEdge en ONNX Runtime gebruikt om Phi-3-mini modellen te benaderen en infereren, en ontdek de mogelijkheden van generatieve AI in verschillende toepassingsscenario’s.

**Kenmerken**  
Inferentie van phi3-mini model in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Samenvattend stelt Phi-3-mini ontwikkelaars in staat om verschillende modelformaten te verkennen en generatieve AI te benutten in uiteenlopende toepassingsscenario’s.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.