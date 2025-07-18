<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:45:58+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "it"
}
-->
# **Quantificazione della famiglia Phi**

La quantizzazione del modello si riferisce al processo di mappatura dei parametri (come pesi e valori di attivazione) in un modello di rete neurale da un ampio intervallo di valori (di solito un intervallo continuo) a un intervallo finito più piccolo. Questa tecnologia può ridurre la dimensione e la complessità computazionale del modello e migliorare l’efficienza operativa del modello in ambienti con risorse limitate, come dispositivi mobili o sistemi embedded. La quantizzazione del modello ottiene la compressione riducendo la precisione dei parametri, ma introduce anche una certa perdita di precisione. Pertanto, nel processo di quantizzazione è necessario bilanciare la dimensione del modello, la complessità computazionale e la precisione. I metodi di quantizzazione comuni includono la quantizzazione a punto fisso, la quantizzazione a virgola mobile, ecc. È possibile scegliere la strategia di quantizzazione più adatta in base allo scenario specifico e alle esigenze.

L’obiettivo è distribuire i modelli GenAI su dispositivi edge e permettere a un numero maggiore di dispositivi di entrare negli scenari GenAI, come dispositivi mobili, AI PC/Copilot+PC e dispositivi IoT tradizionali. Attraverso il modello quantizzato, possiamo distribuirlo su diversi dispositivi edge in base alle caratteristiche di ciascun dispositivo. In combinazione con il framework di accelerazione del modello e il modello quantizzato forniti dai produttori hardware, possiamo costruire scenari applicativi SLM migliori.

Nello scenario di quantizzazione, abbiamo diverse precisioni (INT4, INT8, FP16, FP32). Di seguito una spiegazione delle precisioni di quantizzazione più comuni.

### **INT4**

La quantizzazione INT4 è un metodo di quantizzazione radicale che converte i pesi e i valori di attivazione del modello in interi a 4 bit. La quantizzazione INT4 solitamente comporta una perdita di precisione maggiore a causa del range di rappresentazione più piccolo e della precisione inferiore. Tuttavia, rispetto alla quantizzazione INT8, la quantizzazione INT4 può ridurre ulteriormente i requisiti di memoria e la complessità computazionale del modello. Va notato che la quantizzazione INT4 è relativamente rara nelle applicazioni pratiche, perché una precisione troppo bassa può causare un degrado significativo delle prestazioni del modello. Inoltre, non tutti gli hardware supportano operazioni INT4, quindi è necessario considerare la compatibilità hardware nella scelta del metodo di quantizzazione.

### **INT8**

La quantizzazione INT8 è il processo di conversione dei pesi e delle attivazioni di un modello da numeri in virgola mobile a interi a 8 bit. Sebbene l’intervallo numerico rappresentato dagli interi INT8 sia più piccolo e meno preciso, può ridurre significativamente i requisiti di memoria e calcolo. Nella quantizzazione INT8, i pesi e i valori di attivazione del modello passano attraverso un processo di quantizzazione che include scaling e offset, per preservare il più possibile le informazioni originali in virgola mobile. Durante l’inferenza, questi valori quantizzati vengono dequantizzati nuovamente in numeri in virgola mobile per il calcolo, e poi quantizzati di nuovo in INT8 per la fase successiva. Questo metodo può fornire una precisione sufficiente nella maggior parte delle applicazioni mantenendo un’elevata efficienza computazionale.

### **FP16**

Il formato FP16, cioè numeri in virgola mobile a 16 bit (float16), riduce di metà l’occupazione di memoria rispetto ai numeri in virgola mobile a 32 bit (float32), offrendo vantaggi significativi nelle applicazioni di deep learning su larga scala. Il formato FP16 consente di caricare modelli più grandi o di elaborare più dati entro i limiti di memoria della GPU. Poiché l’hardware GPU moderno continua a supportare operazioni FP16, l’uso del formato FP16 può anche portare a miglioramenti nella velocità di calcolo. Tuttavia, il formato FP16 presenta anche svantaggi intrinseci, ovvero una precisione inferiore, che in alcuni casi può causare instabilità numerica o perdita di precisione.

### **FP32**

Il formato FP32 offre una precisione più elevata e può rappresentare accuratamente un’ampia gamma di valori. In scenari in cui si eseguono operazioni matematiche complesse o si richiedono risultati ad alta precisione, il formato FP32 è preferito. Tuttavia, l’alta precisione comporta anche un maggiore utilizzo di memoria e tempi di calcolo più lunghi. Per modelli di deep learning su larga scala, specialmente quando ci sono molti parametri e una grande quantità di dati, il formato FP32 può causare insufficienza di memoria GPU o una diminuzione della velocità di inferenza.

Su dispositivi mobili o dispositivi IoT, possiamo convertire i modelli Phi-3.x in INT4, mentre AI PC / Copilot PC possono utilizzare precisioni più elevate come INT8, FP16, FP32.

Attualmente, diversi produttori hardware offrono framework differenti per supportare modelli generativi, come OpenVINO di Intel, QNN di Qualcomm, MLX di Apple e CUDA di Nvidia, combinati con la quantizzazione del modello per completare la distribuzione locale.

Dal punto di vista tecnologico, abbiamo diversi formati supportati dopo la quantizzazione, come i formati PyTorch / Tensorflow, GGUF e ONNX. Ho effettuato un confronto tra formati e scenari applicativi tra GGUF e ONNX. Qui raccomando il formato di quantizzazione ONNX, che gode di un buon supporto dal framework del modello all’hardware. In questo capitolo ci concentreremo su ONNX Runtime per GenAI, OpenVINO e Apple MLX per eseguire la quantizzazione del modello (se avete un metodo migliore, potete anche inviarcelo tramite PR).

**Questo capitolo include**

1. [Quantizzazione di Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizzazione di Phi-3.5 / 4 usando le estensioni Generative AI per onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizzazione di Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizzazione di Phi-3.5 / 4 usando Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.