<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:44:29+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "it"
}
-->
# **Inferenza Phi-3 su Android**

Scopriamo come eseguire inferenze con Phi-3-mini su dispositivi Android. Phi-3-mini è una nuova serie di modelli di Microsoft che consente il deployment di Large Language Models (LLM) su dispositivi edge e IoT.

## Semantic Kernel e Inferenza

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) è un framework applicativo che ti permette di creare applicazioni compatibili con Azure OpenAI Service, modelli OpenAI e persino modelli locali. Se sei nuovo a Semantic Kernel, ti consigliamo di consultare il [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Come Accedere a Phi-3-mini Usando Semantic Kernel

Puoi combinarlo con il Hugging Face Connector in Semantic Kernel. Consulta questo [codice di esempio](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Di default, corrisponde all’ID modello su Hugging Face. Tuttavia, puoi anche collegarti a un server modello Phi-3-mini creato localmente.

### Chiamare Modelli Quantizzati con Ollama o LlamaEdge

Molti utenti preferiscono utilizzare modelli quantizzati per eseguire i modelli localmente. [Ollama](https://ollama.com/) e [LlamaEdge](https://llamaedge.com) permettono agli utenti di chiamare diversi modelli quantizzati:

#### Ollama

Puoi eseguire direttamente `ollama run Phi-3` oppure configurarlo offline creando un `Modelfile` con il percorso al tuo file `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Codice di esempio](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Se vuoi usare file `.gguf` sia nel cloud che su dispositivi edge contemporaneamente, LlamaEdge è una scelta eccellente. Puoi fare riferimento a questo [codice di esempio](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) per iniziare.

### Installazione e Avvio su Telefoni Android

1. **Scarica l’app MLC Chat** (gratuita) per telefoni Android.  
2. Scarica il file APK (148MB) e installalo sul tuo dispositivo.  
3. Avvia l’app MLC Chat. Vedrai una lista di modelli AI, incluso Phi-3-mini.

In sintesi, Phi-3-mini apre nuove interessanti possibilità per l’AI generativa su dispositivi edge, e puoi iniziare a esplorarne le potenzialità su Android.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.