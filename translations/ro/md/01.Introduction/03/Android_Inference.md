# **Inferență Phi-3 pe Android**

Să explorăm cum poți realiza inferență cu Phi-3-mini pe dispozitive Android. Phi-3-mini este o nouă serie de modele de la Microsoft care permite implementarea modelelor mari de limbaj (LLM) pe dispozitive edge și IoT.

## Semantic Kernel și Inferența

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) este un cadru de aplicații care îți permite să creezi aplicații compatibile cu Azure OpenAI Service, modelele OpenAI și chiar modele locale. Dacă ești nou în Semantic Kernel, îți recomandăm să consulți [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Accesarea Phi-3-mini folosind Semantic Kernel

Poți să îl combini cu Hugging Face Connector în Semantic Kernel. Consultă acest [exemplu de cod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Implicit, corespunde ID-ului modelului de pe Hugging Face. Totuși, poți conecta și un server local construit pentru modelul Phi-3-mini.

### Apelarea modelelor cuantificate cu Ollama sau LlamaEdge

Mulți utilizatori preferă să folosească modele cuantificate pentru a rula modelele local. [Ollama](https://ollama.com/) și [LlamaEdge](https://llamaedge.com) permit utilizatorilor individuali să apeleze diferite modele cuantificate:

#### Ollama

Poți rula direct `ollama run Phi-3` sau îl poți configura offline creând un `Modelfile` cu calea către fișierul tău `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Exemplu de cod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Dacă vrei să folosești fișiere `.gguf` în cloud și pe dispozitive edge simultan, LlamaEdge este o alegere excelentă. Poți consulta acest [exemplu de cod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) pentru a începe.

### Instalare și rulare pe telefoane Android

1. **Descarcă aplicația MLC Chat** (gratuită) pentru telefoane Android.  
2. Descarcă fișierul APK (148MB) și instalează-l pe dispozitivul tău.  
3. Deschide aplicația MLC Chat. Vei vedea o listă cu modele AI, inclusiv Phi-3-mini.

Pe scurt, Phi-3-mini deschide posibilități interesante pentru AI generativ pe dispozitive edge, iar tu poți începe să explorezi capabilitățile sale pe Android.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.