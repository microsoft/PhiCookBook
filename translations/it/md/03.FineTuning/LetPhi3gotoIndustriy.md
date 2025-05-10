<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-05-09T22:26:14+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "it"
}
-->
# **Lascia che Phi-3 diventi un esperto del settore**

Per applicare il modello Phi-3 in un settore industriale, è necessario integrare i dati aziendali specifici di quel settore nel modello Phi-3. Abbiamo due opzioni diverse: la prima è RAG (Retrieval Augmented Generation) e la seconda è il Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG combina il recupero dati con la generazione di testo. I dati strutturati e non strutturati dell’azienda vengono memorizzati in un database vettoriale. Durante la ricerca di contenuti rilevanti, si individuano sommari e contenuti pertinenti per creare un contesto, che viene poi combinato con la capacità di completamento testuale di LLM/SLM per generare il contenuto.

### **Fine-tuning**

Il fine-tuning consiste nel miglioramento di un modello specifico. Non è necessario partire dall’algoritmo del modello, ma è indispensabile un accumulo continuo di dati. Se si desidera una terminologia più precisa e un’espressione linguistica più accurata nelle applicazioni di settore, il fine-tuning è la scelta migliore. Tuttavia, se i dati cambiano frequentemente, il fine-tuning può diventare complicato.

### **Come scegliere**

1. Se la nostra risposta richiede l’introduzione di dati esterni, RAG è la scelta migliore

2. Se serve un output stabile e preciso di conoscenze di settore, il fine-tuning è la scelta giusta. RAG dà priorità al recupero di contenuti rilevanti ma potrebbe non cogliere sempre le sfumature specialistiche.

3. Il fine-tuning richiede un set di dati di alta qualità; se si dispone solo di un piccolo insieme di dati, il suo impatto sarà limitato. RAG è più flessibile.

4. Il fine-tuning è una “scatola nera”, una sorta di metafisica, ed è difficile comprendere il meccanismo interno. RAG, invece, facilita l’individuazione della fonte dei dati, permettendo di correggere efficacemente allucinazioni o errori di contenuto e offrendo maggiore trasparenza.

### **Scenari**

1. I settori verticali che richiedono un vocabolario e un’espressione professionale specifica trovano nel ***Fine-tuning*** la scelta migliore

2. Per sistemi di QA che coinvolgono la sintesi di diversi punti di conoscenza, ***RAG*** è la soluzione ottimale

3. La combinazione di flussi di lavoro aziendali automatizzati è meglio supportata da ***RAG + Fine-tuning***

## **Come utilizzare RAG**

![rag](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.it.png)

Un database vettoriale è una raccolta di dati memorizzati in forma matematica. I database vettoriali facilitano ai modelli di machine learning il ricordo di input precedenti, consentendo l’utilizzo del machine learning per casi d’uso come ricerca, raccomandazioni e generazione di testo. I dati possono essere identificati in base a metriche di similarità piuttosto che corrispondenze esatte, permettendo ai modelli di comprendere il contesto dei dati.

Il database vettoriale è la chiave per realizzare RAG. Possiamo convertire i dati in formato vettoriale tramite modelli vettoriali come text-embedding-3, jina-ai-embedding, ecc.

Per approfondire la creazione di applicazioni RAG visita [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Come utilizzare il Fine-tuning**

Gli algoritmi comunemente usati nel Fine-tuning sono Lora e QLora. Come scegliere?
- [Approfondisci con questo notebook di esempio](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Esempio di FineTuning in Python](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora e QLora**

![lora](../../../../translated_images/qlora.6aeba71122bc0c8d56ccf0bc36b861304939fee087f43c1fc6cc5c9cb8764725.it.png)

LoRA (Low-Rank Adaptation) e QLoRA (Quantized Low-Rank Adaptation) sono tecniche utilizzate per il fine-tuning di grandi modelli di linguaggio (LLM) tramite Parameter Efficient Fine Tuning (PEFT). Le tecniche PEFT sono progettate per addestrare i modelli in modo più efficiente rispetto ai metodi tradizionali.  
LoRA è una tecnica di fine-tuning autonoma che riduce l’uso di memoria applicando un’approssimazione a rango basso alla matrice di aggiornamento dei pesi. Offre tempi di addestramento rapidi mantenendo prestazioni vicine a quelle del fine-tuning tradizionale.

QLoRA è una versione estesa di LoRA che incorpora tecniche di quantizzazione per ridurre ulteriormente l’uso di memoria. QLoRA quantizza la precisione dei parametri di peso del modello pre-addestrato a 4 bit, risultando più efficiente in termini di memoria rispetto a LoRA. Tuttavia, l’addestramento con QLoRA è circa il 30% più lento rispetto a LoRA a causa dei passaggi aggiuntivi di quantizzazione e dequantizzazione.

QLoRA utilizza LoRA come supporto per correggere gli errori introdotti dalla quantizzazione. QLoRA permette il fine-tuning di modelli enormi con miliardi di parametri su GPU relativamente piccole e facilmente reperibili. Ad esempio, QLoRA può eseguire il fine-tuning di un modello da 70 miliardi di parametri che normalmente richiederebbe 36 GPU, utilizzandone solo 2.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non ci assumiamo responsabilità per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.