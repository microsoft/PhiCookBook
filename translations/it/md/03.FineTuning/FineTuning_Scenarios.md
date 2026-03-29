## Scenari di Fine Tuning

![FineTuning with MS Services](../../../../translated_images/it/FinetuningwithMS.3d0cec8ae693e094.webp)

Questa sezione fornisce una panoramica degli scenari di fine-tuning negli ambienti Microsoft Foundry e Azure, inclusi modelli di distribuzione, livelli infrastrutturali e tecniche di ottimizzazione comunemente utilizzate.

**Piattaforma**  
Questo include servizi gestiti come Microsoft Foundry (precedentemente Microsoft Foundry) e Azure Machine Learning, che offrono gestione del modello, orchestrazione, tracciamento degli esperimenti e workflow di deployment.

**Infrastruttura**  
Il fine-tuning richiede risorse di calcolo scalabili. Negli ambienti Azure, questo tipicamente include macchine virtuali basate su GPU e risorse CPU per carichi di lavoro leggeri, insieme a storage scalabile per dataset e checkpoint.

**Strumenti e Framework**  
I workflow di fine-tuning si basano comunemente su framework e librerie di ottimizzazione come Hugging Face Transformers, DeepSpeed e PEFT (Parameter-Efficient Fine-Tuning).

Il processo di fine-tuning con le tecnologie Microsoft copre servizi di piattaforma, infrastruttura di calcolo e framework di training. Comprendendo come questi componenti lavorano insieme, gli sviluppatori possono adattare efficacemente i modelli di base a compiti specifici e scenari di produzione.

## Modello come Servizio

Fine-tunizza il modello utilizzando il fine-tuning ospitato, senza la necessità di creare e gestire il calcolo.

![MaaS Fine Tuning](../../../../translated_images/it/MaaSfinetune.3eee4630607aff0d.webp)

Il fine-tuning serverless è ora disponibile per le famiglie di modelli Phi-3, Phi-3.5 e Phi-4, permettendo agli sviluppatori di personalizzare rapidamente e facilmente i modelli per scenari cloud e edge senza dover organizzare il calcolo.

## Modello come Piattaforma 

Gli utenti gestiscono il proprio calcolo per poter fine-tunizzare i loro modelli.

![Maap Fine Tuning](../../../../translated_images/it/MaaPFinetune.fd3829c1122f5d1c.webp)

[Campione di Fine Tuning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Confronto Tecniche di Fine-Tuning

|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Adattare LLM pre-addestrati a compiti o domini specifici|Sì|Sì|Sì|Sì|Sì|Sì|
|Fine-tuning per compiti NLP come classificazione testuale, riconoscimento entità nominate e traduzione automatica|Sì|Sì|Sì|Sì|Sì|Sì|
|Fine-tuning per compiti di QA|Sì|Sì|Sì|Sì|Sì|Sì|
|Fine-tuning per generare risposte simili a quelle umane nei chatbot|Sì|Sì|Sì|Sì|Sì|Sì|
|Fine-tuning per generare musica, arte o altre forme di creatività|Sì|Sì|Sì|Sì|Sì|Sì|
|Riduzione dei costi computazionali e finanziari|Sì|Sì|Sì|Sì|Sì|Sì|
|Riduzione dell’uso della memoria|Sì|Sì|Sì|Sì|Sì|Sì|
|Utilizzo di meno parametri per un fine-tuning efficiente|Sì|Sì|Sì|No|No|Sì|
|Forma di data parallelism efficiente in memoria che consente l’accesso alla memoria aggregata GPU di tutti i dispositivi GPU disponibili|No|No|No|Sì|Sì|No|

> [!NOTE]
> LoRA, QLoRA, PEFT e DoRA sono metodi di fine-tuning efficienti in termini di parametri, mentre DeepSpeed e ZeRO si concentrano sull’addestramento distribuito e l’ottimizzazione della memoria.

## Esempi di Prestazioni nel Fine Tuning

![Finetuning Performance](../../../../translated_images/it/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->