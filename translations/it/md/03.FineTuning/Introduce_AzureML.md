<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:40:40+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "it"
}
-->
# **Introduzione a Azure Machine Learning Service**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) è un servizio cloud per accelerare e gestire il ciclo di vita dei progetti di machine learning (ML).

I professionisti del ML, data scientist e ingegneri possono utilizzarlo nelle loro attività quotidiane per:

- Addestrare e distribuire modelli.
- Gestire le operazioni di machine learning (MLOps).
- È possibile creare un modello in Azure Machine Learning oppure utilizzare un modello sviluppato su piattaforme open source come PyTorch, TensorFlow o scikit-learn.
- Gli strumenti MLOps aiutano a monitorare, riaddestrare e ridistribuire i modelli.

## A chi è rivolto Azure Machine Learning?

**Data Scientist e ML Engineer**

Possono utilizzare strumenti per accelerare e automatizzare le attività quotidiane.
Azure ML offre funzionalità per equità, spiegabilità, tracciamento e auditabilità.

**Sviluppatori di applicazioni:**

Possono integrare modelli in applicazioni o servizi in modo fluido.

**Sviluppatori di piattaforme**

Hanno accesso a un set robusto di strumenti supportati da API durature di Azure Resource Manager.
Questi strumenti permettono di costruire tool avanzati per il ML.

**Aziende**

Lavorando nel cloud Microsoft Azure, le aziende beneficiano di sicurezza familiare e controllo degli accessi basato sui ruoli.
Possono configurare progetti per controllare l’accesso a dati protetti e operazioni specifiche.

## Produttività per tutto il team

I progetti ML spesso richiedono un team con competenze diverse per costruire e mantenere i sistemi.

Azure ML offre strumenti che permettono di:
- Collaborare con il team tramite notebook condivisi, risorse di calcolo, calcolo serverless, dati e ambienti.
- Sviluppare modelli con equità, spiegabilità, tracciamento e auditabilità per soddisfare requisiti di tracciabilità e conformità.
- Distribuire modelli ML rapidamente e facilmente su larga scala, gestendoli e governandoli efficacemente con MLOps.
- Eseguire carichi di lavoro di machine learning ovunque con governance, sicurezza e conformità integrate.

## Strumenti della piattaforma compatibili tra loro

Chiunque nel team ML può usare gli strumenti preferiti per portare a termine il lavoro.
Che si tratti di esperimenti rapidi, tuning di iperparametri, costruzione di pipeline o gestione delle inferenze, si possono usare interfacce familiari come:
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

Durante la fase di raffinamento dei modelli e la collaborazione nel ciclo di sviluppo, è possibile condividere e trovare asset, risorse e metriche all’interno dell’interfaccia di Azure Machine Learning studio.

## **LLM/SLM in Azure ML**

Azure ML ha aggiunto molte funzioni legate a LLM/SLM, combinando LLMOps e SLMOps per creare una piattaforma tecnologica di intelligenza artificiale generativa a livello aziendale.

### **Catalogo Modelli**

Gli utenti aziendali possono distribuire modelli diversi in base a scenari di business differenti tramite il Catalogo Modelli, offrendo servizi come Model as Service per sviluppatori o utenti aziendali.

![models](../../../../translated_images/it/models.e6c7ff50a51806fd.png)

Il Catalogo Modelli in Azure Machine Learning studio è il centro per scoprire e utilizzare un’ampia gamma di modelli che permettono di costruire applicazioni di Generative AI. Il catalogo include centinaia di modelli provenienti da provider come Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, inclusi modelli addestrati da Microsoft. I modelli di provider diversi da Microsoft sono considerati Prodotti Non Microsoft, come definito nei Termini di Prodotto Microsoft, e sono soggetti ai termini forniti con il modello.

### **Pipeline di Job**

Il cuore di una pipeline di machine learning è suddividere un compito completo in un flusso di lavoro a più fasi. Ogni fase è un componente gestibile che può essere sviluppato, ottimizzato, configurato e automatizzato singolarmente. Le fasi sono collegate tramite interfacce ben definite. Il servizio pipeline di Azure Machine Learning orchestra automaticamente tutte le dipendenze tra le fasi.

Nel fine-tuning di SLM / LLM, possiamo gestire dati, addestramento e processi di generazione tramite Pipeline.

![finetuning](../../../../translated_images/it/finetuning.6559da198851fa52.png)

### **Prompt flow**

Vantaggi dell’uso di Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow offre una serie di benefici che aiutano gli utenti a passare dall’ideazione alla sperimentazione e, infine, a applicazioni LLM pronte per la produzione:

**Agilità nell’ingegneria dei prompt**

Esperienza di authoring interattiva: Azure Machine Learning prompt flow fornisce una rappresentazione visiva della struttura del flusso, permettendo agli utenti di comprendere e navigare facilmente nei progetti. Offre anche un’esperienza di coding simile a un notebook per uno sviluppo e debug efficienti del flusso.  
Varianti per il tuning dei prompt: gli utenti possono creare e confrontare più varianti di prompt, facilitando un processo iterativo di raffinamento.

Valutazione: i flussi di valutazione integrati permettono di misurare la qualità e l’efficacia di prompt e flussi.

Risorse complete: Azure Machine Learning prompt flow include una libreria di strumenti, esempi e template integrati che fungono da punto di partenza per lo sviluppo, stimolando la creatività e accelerando il processo.

**Prontezza aziendale per applicazioni basate su LLM**

Collaborazione: Azure Machine Learning prompt flow supporta la collaborazione di team, consentendo a più utenti di lavorare insieme su progetti di ingegneria dei prompt, condividere conoscenze e mantenere il controllo delle versioni.

Piattaforma tutto-in-uno: Azure Machine Learning prompt flow semplifica l’intero processo di ingegneria dei prompt, dallo sviluppo e valutazione fino alla distribuzione e monitoraggio. Gli utenti possono distribuire facilmente i loro flussi come endpoint di Azure Machine Learning e monitorarne le prestazioni in tempo reale, garantendo un funzionamento ottimale e miglioramenti continui.

Soluzioni di prontezza aziendale di Azure Machine Learning: Prompt flow sfrutta le robuste soluzioni di prontezza aziendale di Azure Machine Learning, offrendo una base sicura, scalabile e affidabile per lo sviluppo, la sperimentazione e la distribuzione dei flussi.

Con Azure Machine Learning prompt flow, gli utenti possono liberare la loro agilità nell’ingegneria dei prompt, collaborare efficacemente e sfruttare soluzioni di livello enterprise per lo sviluppo e la distribuzione di applicazioni basate su LLM.

Combinando la potenza di calcolo, i dati e i diversi componenti di Azure ML, gli sviluppatori aziendali possono costruire facilmente le proprie applicazioni di intelligenza artificiale.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.