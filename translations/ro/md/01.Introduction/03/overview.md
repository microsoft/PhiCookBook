În contextul Phi-3-mini, inferența se referă la procesul de utilizare a modelului pentru a face predicții sau a genera rezultate pe baza datelor de intrare. Permiteți-mi să vă ofer mai multe detalii despre Phi-3-mini și capacitățile sale de inferență.

Phi-3-mini face parte din seria de modele Phi-3 lansate de Microsoft. Aceste modele sunt concepute pentru a redefini ceea ce este posibil cu Modelele de Limbaj Mici (SLM).

Iată câteva puncte cheie despre Phi-3-mini și capacitățile sale de inferență:

## **Prezentare generală Phi-3-mini:**
- Phi-3-mini are o dimensiune de 3,8 miliarde de parametri.
- Poate rula nu doar pe dispozitivele tradiționale de calcul, ci și pe dispozitive edge, cum ar fi dispozitive mobile și dispozitive IoT.
- Lansarea Phi-3-mini permite persoanelor și companiilor să implementeze SLM-uri pe diferite dispozitive hardware, în special în medii cu resurse limitate.
- Suportă diverse formate de modele, inclusiv formatul tradițional PyTorch, versiunea cuantificată a formatului gguf și versiunea cuantificată bazată pe ONNX.

## **Accesarea Phi-3-mini:**
Pentru a accesa Phi-3-mini, puteți folosi [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) într-o aplicație Copilot. Semantic Kernel este în general compatibil cu Azure OpenAI Service, modelele open-source de pe Hugging Face și modelele locale.  
De asemenea, puteți folosi [Ollama](https://ollama.com) sau [LlamaEdge](https://llamaedge.com) pentru a apela modele cuantificate. Ollama permite utilizatorilor individuali să apeleze diferite modele cuantificate, în timp ce LlamaEdge oferă disponibilitate cross-platform pentru modelele GGUF.

## **Modele cuantificate:**
Mulți utilizatori preferă să folosească modele cuantificate pentru inferență locală. De exemplu, puteți rula direct Ollama run Phi-3 sau îl puteți configura offline folosind un Modelfile. Modelfile specifică calea fișierului GGUF și formatul promptului.

## **Posibilități AI generativă:**
Combinarea SLM-urilor precum Phi-3-mini deschide noi posibilități pentru AI generativă. Inferența este doar primul pas; aceste modele pot fi folosite pentru diverse sarcini în scenarii cu resurse limitate, cu latență redusă și costuri restrânse.

## **Dezvăluirea AI generative cu Phi-3-mini: Un ghid pentru inferență și implementare**  
Aflați cum să folosiți Semantic Kernel, Ollama/LlamaEdge și ONNX Runtime pentru a accesa și a face inferență cu modelele Phi-3-mini și explorați posibilitățile AI generative în diverse scenarii de aplicație.

**Caracteristici**  
Inferență model phi3-mini în:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

În concluzie, Phi-3-mini le permite dezvoltatorilor să exploreze diferite formate de modele și să valorifice AI generativă în diverse scenarii de aplicație.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.