<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:09:38+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "it"
}
-->
Nel contesto di Phi-3-mini, l'inferenza si riferisce al processo di utilizzo del modello per fare previsioni o generare output basati sui dati di input. Ti fornirò maggiori dettagli su Phi-3-mini e le sue capacità di inferenza.

Phi-3-mini fa parte della serie Phi-3 di modelli rilasciati da Microsoft. Questi modelli sono progettati per ridefinire ciò che è possibile con i Small Language Models (SLM).

Ecco alcuni punti chiave su Phi-3-mini e le sue capacità di inferenza:

## **Panoramica di Phi-3-mini:**
- Phi-3-mini ha una dimensione di 3,8 miliardi di parametri.
- Può essere eseguito non solo su dispositivi di calcolo tradizionali, ma anche su dispositivi edge come dispositivi mobili e dispositivi IoT.
- Il rilascio di Phi-3-mini consente a individui e aziende di distribuire SLM su diversi dispositivi hardware, specialmente in ambienti con risorse limitate.
- Supporta vari formati di modello, incluso il formato tradizionale PyTorch, la versione quantizzata del formato gguf e la versione quantizzata basata su ONNX.

## **Accesso a Phi-3-mini:**
Per accedere a Phi-3-mini, puoi utilizzare [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) in un'applicazione Copilot. Semantic Kernel è generalmente compatibile con Azure OpenAI Service, modelli open-source su Hugging Face e modelli locali.  
Puoi anche usare [Ollama](https://ollama.com) o [LlamaEdge](https://llamaedge.com) per chiamare modelli quantizzati. Ollama permette agli utenti individuali di chiamare diversi modelli quantizzati, mentre LlamaEdge offre disponibilità cross-platform per i modelli GGUF.

## **Modelli Quantizzati:**
Molti utenti preferiscono utilizzare modelli quantizzati per l'inferenza locale. Ad esempio, puoi eseguire direttamente Ollama run Phi-3 o configurarlo offline usando un Modelfile. Il Modelfile specifica il percorso del file GGUF e il formato del prompt.

## **Possibilità di AI Generativa:**
Combinare SLM come Phi-3-mini apre nuove possibilità per l’AI generativa. L’inferenza è solo il primo passo; questi modelli possono essere utilizzati per vari compiti in scenari con risorse limitate, vincoli di latenza e costi contenuti.

## **Sbloccare l’AI Generativa con Phi-3-mini: Guida all’Inferenza e al Deployment**  
Scopri come utilizzare Semantic Kernel, Ollama/LlamaEdge e ONNX Runtime per accedere e inferire modelli Phi-3-mini, ed esplora le possibilità dell’AI generativa in diversi scenari applicativi.

**Caratteristiche**  
Inferenza del modello phi3-mini in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

In sintesi, Phi-3-mini permette agli sviluppatori di esplorare diversi formati di modello e sfruttare l’AI generativa in molteplici scenari applicativi.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.