<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:24:46+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "it"
}
-->
# **Quantificazione della famiglia Phi**

La quantizzazione del modello si riferisce al processo di mappatura dei parametri (come pesi e valori di attivazione) in un modello di rete neurale da un ampio intervallo di valori (di solito un intervallo continuo) a un intervallo finito più piccolo. Questa tecnologia può ridurre la dimensione e la complessità computazionale del modello, migliorando l'efficienza operativa in ambienti con risorse limitate come dispositivi mobili o sistemi embedded. La quantizzazione del modello ottiene la compressione riducendo la precisione dei parametri, ma introduce anche una certa perdita di precisione. Pertanto, durante il processo di quantizzazione è necessario bilanciare dimensione del modello, complessità computazionale e precisione. I metodi di quantizzazione comuni includono la quantizzazione a punto fisso, la quantizzazione in virgola mobile, ecc. È possibile scegliere la strategia di quantizzazione più adatta in base allo scenario specifico e alle esigenze.

L'obiettivo è distribuire i modelli GenAI su dispositivi edge e permettere a più dispositivi di entrare negli scenari GenAI, come dispositivi mobili, AI PC/Copilot+PC e dispositivi IoT tradizionali. Attraverso il modello quantizzato, possiamo implementarlo su diversi dispositivi edge in base alle caratteristiche di ciascuno. Integrando il framework di accelerazione del modello e il modello di quantizzazione forniti dai produttori hardware, possiamo costruire scenari applicativi SLM migliori.

Nello scenario di quantizzazione, disponiamo di diverse precisioni (INT4, INT8, FP16, FP32). Di seguito una spiegazione delle precisioni di quantizzazione più comuni.

### **INT4**

La quantizzazione INT4 è un metodo radicale che converte pesi e valori di attivazione del modello in interi a 4 bit. La quantizzazione INT4 solitamente comporta una perdita di precisione maggiore a causa del range di rappresentazione più piccolo e della precisione inferiore. Tuttavia, rispetto alla quantizzazione INT8, l’INT4 può ridurre ulteriormente i requisiti di archiviazione e la complessità computazionale del modello. Va notato che l’INT4 è relativamente raro nelle applicazioni pratiche, perché una precisione troppo bassa può causare un degrado significativo delle prestazioni del modello. Inoltre, non tutti gli hardware supportano operazioni INT4, quindi è necessario considerare la compatibilità hardware nella scelta del metodo di quantizzazione.

### **INT8**

La quantizzazione INT8 è il processo di conversione di pesi e attivazioni del modello da numeri in virgola mobile a interi a 8 bit. Sebbene l’intervallo numerico rappresentato dagli interi INT8 sia più piccolo e meno preciso, può ridurre significativamente i requisiti di archiviazione e calcolo. Nella quantizzazione INT8, pesi e valori di attivazione passano attraverso un processo di quantizzazione che include scaling e offset per preservare il più possibile le informazioni originali in virgola mobile. Durante l'inferenza, questi valori quantizzati vengono dequantizzati in numeri in virgola mobile per il calcolo e poi nuovamente quantizzati in INT8 per il passo successivo. Questo metodo offre un’accuratezza sufficiente nella maggior parte delle applicazioni mantenendo un’elevata efficienza computazionale.

### **FP16**

Il formato FP16, cioè numeri in virgola mobile a 16 bit (float16), riduce dell’50% l’occupazione di memoria rispetto ai numeri in virgola mobile a 32 bit (float32), vantaggio significativo nelle applicazioni di deep learning su larga scala. Il formato FP16 consente di caricare modelli più grandi o elaborare più dati entro i limiti di memoria GPU disponibili. Con il supporto crescente da parte delle moderne GPU per le operazioni FP16, l’uso di questo formato può anche migliorare la velocità di calcolo. Tuttavia, il formato FP16 presenta anche svantaggi intrinseci, come la precisione inferiore, che in alcuni casi può portare a instabilità numerica o perdita di precisione.

### **FP32**

Il formato FP32 offre una precisione più elevata e può rappresentare con accuratezza un ampio intervallo di valori. In scenari in cui si eseguono operazioni matematiche complesse o si richiedono risultati ad alta precisione, il formato FP32 è preferibile. Tuttavia, l’alta precisione comporta un maggiore utilizzo di memoria e tempi di calcolo più lunghi. Per modelli di deep learning su larga scala, specialmente con molti parametri e grandi quantità di dati, il formato FP32 può causare insufficienza di memoria GPU o rallentamenti nell’inferenza.

Su dispositivi mobili o IoT possiamo convertire i modelli Phi-3.x in INT4, mentre AI PC / Copilot PC possono utilizzare precisioni più elevate come INT8, FP16, FP32.

Attualmente, diversi produttori hardware offrono framework differenti per supportare modelli generativi, come OpenVINO di Intel, QNN di Qualcomm, MLX di Apple e CUDA di Nvidia, combinati con la quantizzazione del modello per completare la distribuzione locale.

Dal punto di vista tecnologico, dopo la quantizzazione supportiamo diversi formati, come PyTorch / Tensorflow, GGUF e ONNX. Ho fatto un confronto tra formati e scenari applicativi tra GGUF e ONNX. Qui raccomando il formato di quantizzazione ONNX, che gode di un buon supporto dal framework modello all’hardware. In questo capitolo ci concentreremo su ONNX Runtime per GenAI, OpenVINO e Apple MLX per eseguire la quantizzazione del modello (se avete metodi migliori, potete inviarli tramite PR).

**Questo capitolo include**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.