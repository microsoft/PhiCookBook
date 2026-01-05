<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-05T14:20:50+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "it"
}
-->
# **Quantificazione della Famiglia Phi**

La quantificazione del modello si riferisce al processo di mappatura dei parametri (come pesi e valori di attivazione) in un modello di rete neurale da un ampio intervallo di valori (di solito un intervallo di valori continui) a un intervallo di valori finito più piccolo. Questa tecnologia può ridurre la dimensione e la complessità computazionale del modello e migliorare l'efficienza operativa del modello in ambienti con risorse limitate come dispositivi mobili o sistemi embedded. La quantificazione del modello ottiene la compressione riducendo la precisione dei parametri, ma introduce anche una certa perdita di precisione. Pertanto, nel processo di quantificazione è necessario bilanciare la dimensione del modello, la complessità computazionale e la precisione. I metodi di quantificazione comuni includono la quantificazione a punto fisso, la quantificazione a virgola mobile, ecc. È possibile scegliere la strategia di quantificazione appropriata in base allo scenario specifico e alle esigenze.

Speriamo di distribuire modelli GenAI su dispositivi edge e consentire a più dispositivi di entrare negli scenari GenAI, come dispositivi mobili, PC AI/Copilot+PC e dispositivi IoT tradizionali. Attraverso il modello quantificato, possiamo distribuirlo su diversi dispositivi edge in base ai dispositivi. Combinato con il framework di accelerazione del modello e il modello quantificato forniti dai produttori di hardware, possiamo costruire migliori scenari di applicazione SLM.

Nello scenario di quantificazione, abbiamo diverse precisioni (INT4, INT8, FP16, FP32). Di seguito è riportata una spiegazione delle precisioni di quantificazione comunemente usate.

### **INT4**

La quantificazione INT4 è un metodo radicale di quantificazione che quantifica i pesi e i valori di attivazione del modello in interi a 4 bit. La quantificazione INT4 solitamente comporta una perdita di precisione maggiore a causa dell'intervallo di rappresentazione più piccolo e della precisione inferiore. Tuttavia, rispetto alla quantificazione INT8, la quantificazione INT4 può ulteriormente ridurre i requisiti di memoria e la complessità computazionale del modello. Va notato che la quantificazione INT4 è relativamente rara nelle applicazioni pratiche, perché una precisione troppo bassa potrebbe causare un significativo degrado delle prestazioni del modello. Inoltre, non tutto l'hardware supporta operazioni INT4, quindi la compatibilità hardware deve essere considerata nella scelta del metodo di quantificazione.

### **INT8**

La quantificazione INT8 è il processo di conversione dei pesi e delle attivazioni di un modello da numeri in virgola mobile a interi a 8 bit. Sebbene l'intervallo numerico rappresentato dagli interi INT8 sia più piccolo e meno preciso, può ridurre significativamente i requisiti di memoria e di calcolo. Nella quantificazione INT8, i pesi e i valori di attivazione del modello attraversano un processo di quantificazione che include scalatura e offset, per preservare il più possibile l'informazione originale in virgola mobile. Durante l'inferenza, questi valori quantificati vengono dequantificati nuovamente in numeri in virgola mobile per il calcolo, e quindi quantificati nuovamente in INT8 per la fase successiva. Questo metodo può fornire una precisione sufficiente nella maggior parte delle applicazioni mantenendo un'elevata efficienza computazionale.

### **FP16**

Il formato FP16, cioè numeri a virgola mobile a 16 bit (float16), riduce l'occupazione di memoria della metà rispetto ai numeri a virgola mobile a 32 bit (float32), il che ha vantaggi significativi nelle applicazioni di deep learning su larga scala. Il formato FP16 consente di caricare modelli più grandi o elaborare una maggiore quantità di dati nei limiti di memoria della GPU. Poiché l'hardware GPU moderno continua a supportare le operazioni FP16, l'uso del formato FP16 può anche comportare miglioramenti nella velocità di calcolo. Tuttavia, il formato FP16 ha anche i suoi svantaggi intrinseci, cioè una precisione inferiore, che può portare a instabilità numerica o perdita di precisione in alcuni casi.

### **FP32**

Il formato FP32 fornisce una precisione più elevata e può rappresentare accuratamente un ampio intervallo di valori. Negli scenari in cui si eseguono operazioni matematiche complesse o sono richiesti risultati ad alta precisione, si preferisce il formato FP32. Tuttavia, l'alta precisione comporta anche un maggior utilizzo della memoria e tempi di calcolo più lunghi. Per modelli di deep learning su larga scala, soprattutto quando ci sono molti parametri del modello e una grande quantità di dati, il formato FP32 può causare insufficienza di memoria GPU o una diminuzione della velocità di inferenza.

Su dispositivi mobili o dispositivi IoT, possiamo convertire i modelli Phi-3.x in INT4, mentre PC AI / Copilot PC possono utilizzare una precisione più elevata come INT8, FP16, FP32.

Attualmente, i diversi produttori di hardware dispongono di diversi framework per supportare modelli generativi, come OpenVINO di Intel, QNN di Qualcomm, MLX di Apple e CUDA di Nvidia, ecc., combinati con la quantificazione del modello per completare la distribuzione locale.

Dal punto di vista tecnico, disponiamo di diversi supporti di formato dopo la quantificazione, come i formati PyTorch / TensorFlow, GGUF e ONNX. Ho fatto un confronto tra i formati e gli scenari applicativi tra GGUF e ONNX. Qui raccomando il formato di quantificazione ONNX, che ha un buon supporto dal framework del modello all'hardware. In questo capitolo, ci concentreremo su ONNX Runtime per GenAI, OpenVINO e Apple MLX per eseguire la quantificazione del modello (se avete modi migliori, potete anche fornirceli inviando una PR).

**Questo capitolo include**

1. [Quantificazione di Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantificazione di Phi-3.5 / 4 usando estensioni Generative AI per onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantificazione di Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantificazione di Phi-3.5 / 4 usando Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur facendo del nostro meglio per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda la traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->