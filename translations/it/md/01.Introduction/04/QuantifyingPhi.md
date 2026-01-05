<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T03:18:54+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "it"
}
-->
# **Quantificazione della famiglia Phi**

La quantizzazione del modello si riferisce al processo di mappatura dei parametri (come pesi e valori di attivazione) in un modello di rete neurale da un intervallo di valori ampio (di solito un intervallo di valori continuo) a un intervallo finito più piccolo. Questa tecnologia può ridurre le dimensioni e la complessità computazionale del modello e migliorare l’efficienza operativa del modello in ambienti con risorse limitate come dispositivi mobili o sistemi embedded. La quantizzazione del modello ottiene la compressione riducendo la precisione dei parametri, ma introduce anche una certa perdita di precisione. Pertanto, nel processo di quantizzazione è necessario bilanciare dimensione del modello, complessità computazionale e precisione. I metodi di quantizzazione comuni includono quantizzazione a punto fisso, quantizzazione in virgola mobile, ecc. È possibile scegliere la strategia di quantizzazione appropriata in base allo scenario e alle necessità specifiche.

Speriamo di distribuire modelli GenAI su dispositivi edge e consentire a più dispositivi di entrare negli scenari GenAI, come dispositivi mobili, AI PC/Copilot+PC e dispositivi IoT tradizionali. Attraverso la quantizzazione dei modelli, possiamo distribuirli su diversi dispositivi edge a seconda dell’hardware. In combinazione con il framework di accelerazione del modello e i modelli quantizzati forniti dai produttori hardware, possiamo costruire migliori scenari applicativi SLM.

Nello scenario di quantizzazione, abbiamo diverse precisioni (INT4, INT8, FP16, FP32). Di seguito è riportata una spiegazione delle precisioni di quantizzazione comunemente usate

### **INT4**

La quantizzazione INT4 è un metodo di quantizzazione radicale che quantizza i pesi e i valori di attivazione del modello in interi a 4 bit. La quantizzazione INT4 di solito comporta una perdita di precisione maggiore a causa del range di rappresentazione più ristretto e della precisione inferiore. Tuttavia, rispetto alla quantizzazione INT8, la quantizzazione INT4 può ridurre ulteriormente i requisiti di archiviazione e la complessità computazionale del modello. Va notato che la quantizzazione INT4 è relativamente rara nelle applicazioni pratiche, perché una precisione troppo bassa può causare un degrado significativo delle prestazioni del modello. Inoltre, non tutto l’hardware supporta le operazioni INT4, quindi è necessario considerare la compatibilità hardware quando si sceglie un metodo di quantizzazione.

### **INT8**

La quantizzazione INT8 è il processo di conversione dei pesi e delle attivazioni di un modello da numeri in virgola mobile a interi a 8 bit. Sebbene l’intervallo numerico rappresentato dagli interi INT8 sia più piccolo e meno preciso, può ridurre significativamente i requisiti di memoria e computazione. Nella quantizzazione INT8, i pesi e i valori di attivazione del modello attraversano un processo di quantizzazione, che include scaling e offset, per preservare il più possibile le informazioni originali in virgola mobile. Durante l’inferenza, questi valori quantizzati vengono dequantizzati nuovamente in numeri in virgola mobile per il calcolo, e poi quantizzati di nuovo in INT8 per il passo successivo. Questo metodo può fornire una precisione sufficiente nella maggior parte delle applicazioni mantenendo un’elevata efficienza computazionale.

### **FP16**

Il formato FP16, cioè numeri in virgola mobile a 16 bit (float16), riduce l’ingombro di memoria della metà rispetto ai numeri in virgola mobile a 32 bit (float32), il che presenta vantaggi significativi nelle applicazioni di deep learning su larga scala. Il formato FP16 consente di caricare modelli più grandi o elaborare più dati entro le stesse limitazioni di memoria GPU. Poiché l’hardware GPU moderno continua a supportare le operazioni FP16, l’uso del formato FP16 può anche comportare miglioramenti nella velocità di calcolo. Tuttavia, il formato FP16 ha anche svantaggi intrinseci, ossia una precisione inferiore, che può portare a instabilità numerica o perdita di precisione in alcuni casi.

### **FP32**

Il formato FP32 offre una precisione maggiore e può rappresentare con accuratezza un’ampia gamma di valori. Negli scenari in cui vengono eseguite operazioni matematiche complesse o sono necessari risultati ad alta precisione, il formato FP32 è preferito. Tuttavia, l’elevata precisione comporta anche un maggiore utilizzo di memoria e tempi di calcolo più lunghi. Per i modelli di deep learning su larga scala, in particolare quando ci sono molti parametri del modello e una grande quantità di dati, il formato FP32 può causare insufficienza di memoria GPU o una diminuzione della velocità di inferenza.

Su dispositivi mobili o dispositivi IoT, possiamo convertire i modelli Phi-3.x in INT4, mentre AI PC / Copilot PC possono utilizzare precisioni più elevate come INT8, FP16, FP32.

Attualmente, diversi produttori hardware dispongono di framework per supportare modelli generativi, come OpenVINO di Intel, QNN di Qualcomm, MLX di Apple e CUDA di Nvidia, ecc., da combinare con la quantizzazione dei modelli per completare la distribuzione locale.

Dal punto di vista tecnologico, dopo la quantizzazione supportiamo diversi formati, come il formato PyTorch / TensorFlow, GGUF e ONNX. Ho fatto un confronto di formati e scenari di applicazione tra GGUF e ONNX. Qui raccomando il formato di quantizzazione ONNX, che ha un buon supporto dal framework del modello all’hardware. In questo capitolo, ci concentreremo su ONNX Runtime per GenAI, OpenVINO e Apple MLX per eseguire la quantizzazione del modello (se avete un metodo migliore, potete anche proporcelo inviando una PR)

**Questo capitolo include**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Esclusione di responsabilità**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua di partenza deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo responsabilità per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->