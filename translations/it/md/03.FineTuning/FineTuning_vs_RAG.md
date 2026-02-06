## Finetuning vs RAG

## Retrieval Augmented Generation

RAG è recupero dati + generazione di testo. I dati strutturati e non strutturati dell’azienda sono memorizzati nel database vettoriale. Quando si cerca contenuto rilevante, si trovano il riassunto e il contenuto pertinenti per formare un contesto, e si combina la capacità di completamento testuale di LLM/SLM per generare contenuti.

## Processo RAG
![FinetuningvsRAG](../../../../translated_images/it/rag.2014adc59e6f6007.webp)

## Fine-tuning
Il fine-tuning si basa sul miglioramento di un modello specifico. Non è necessario partire dall’algoritmo del modello, ma i dati devono essere accumulati continuamente. Se desideri una terminologia e un’espressione linguistica più precise nelle applicazioni industriali, il fine-tuning è la scelta migliore. Tuttavia, se i tuoi dati cambiano frequentemente, il fine-tuning può diventare complicato.

## Come scegliere
Se la nostra risposta richiede l’introduzione di dati esterni, RAG è la scelta migliore.

Se hai bisogno di fornire conoscenze industriali stabili e precise, il fine-tuning sarà una buona opzione. RAG dà priorità al recupero di contenuti rilevanti, ma potrebbe non cogliere sempre le sfumature specialistiche.

Il fine-tuning richiede un set di dati di alta qualità e, se si tratta solo di un piccolo insieme di dati, non farà molta differenza. RAG è più flessibile.  
Il fine-tuning è una scatola nera, una metafisica, ed è difficile comprendere il meccanismo interno. Ma RAG può facilitare l’individuazione della fonte dei dati, permettendo così di correggere efficacemente allucinazioni o errori di contenuto e offrendo una migliore trasparenza.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.