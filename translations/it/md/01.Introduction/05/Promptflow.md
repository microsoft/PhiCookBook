<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-05-09T15:09:55+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "it"
}
-->
# **Introduzione a Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) è uno strumento di automazione dei flussi di lavoro visuale che permette agli utenti di creare flussi automatizzati utilizzando modelli predefiniti e connettori personalizzati. È progettato per consentire a sviluppatori e analisti aziendali di costruire rapidamente processi automatizzati per attività come la gestione dei dati, la collaborazione e l’ottimizzazione dei processi. Con Prompt Flow, gli utenti possono facilmente collegare diversi servizi, applicazioni e sistemi, automatizzando processi aziendali complessi.

Microsoft Prompt Flow è pensato per semplificare l’intero ciclo di sviluppo delle applicazioni AI basate su Large Language Models (LLM). Che tu stia ideando, prototipando, testando, valutando o distribuendo applicazioni basate su LLM, Prompt Flow rende il processo più semplice e ti permette di creare app LLM di qualità produttiva.

## Ecco le principali caratteristiche e vantaggi di Microsoft Prompt Flow:

**Esperienza di Authoring Interattiva**

Prompt Flow offre una rappresentazione visiva della struttura del tuo flusso, rendendo facile comprendere e navigare tra i tuoi progetti.
Fornisce un’esperienza di codifica simile a un notebook per uno sviluppo e debug efficiente dei flussi.

**Varianti di Prompt e Ottimizzazione**

Crea e confronta più varianti di prompt per facilitare un processo iterativo di raffinamento. Valuta le prestazioni dei diversi prompt e scegli quelli più efficaci.

**Flussi di Valutazione Integrati**

Valuta la qualità e l’efficacia dei tuoi prompt e flussi usando strumenti di valutazione integrati.
Comprendi quanto bene stanno performando le tue applicazioni basate su LLM.

**Risorse Complete**

Prompt Flow include una libreria di strumenti, esempi e modelli predefiniti. Queste risorse rappresentano un punto di partenza per lo sviluppo, stimolano la creatività e accelerano il processo.

**Collaborazione e Prontezza Enterprise**

Supporta la collaborazione di team permettendo a più utenti di lavorare insieme su progetti di prompt engineering.
Mantieni il controllo delle versioni e condividi conoscenze in modo efficace. Snellisci l’intero processo di prompt engineering, dallo sviluppo e valutazione fino al deployment e monitoraggio.

## Valutazione in Prompt Flow

In Microsoft Prompt Flow, la valutazione è fondamentale per capire quanto bene performano i tuoi modelli AI. Vediamo come personalizzare i flussi di valutazione e le metriche all’interno di Prompt Flow:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.it.png)

**Comprendere la Valutazione in Prompt Flow**

In Prompt Flow, un flusso rappresenta una sequenza di nodi che elaborano input e generano output. I flussi di valutazione sono tipi speciali di flussi progettati per misurare le prestazioni di una esecuzione basandosi su criteri e obiettivi specifici.

**Caratteristiche principali dei flussi di valutazione**

Di solito vengono eseguiti dopo il flusso testato, utilizzando i suoi output. Calcolano punteggi o metriche per misurare le prestazioni del flusso testato. Le metriche possono includere accuratezza, punteggi di rilevanza o altre misure pertinenti.

### Personalizzare i flussi di valutazione

**Definire gli input**

I flussi di valutazione devono ricevere in input gli output del flusso testato. Definisci gli input come nei flussi standard.
Ad esempio, se stai valutando un flusso QnA, chiama un input "answer". Se valuti un flusso di classificazione, chiama un input "category". Potrebbero essere necessari anche input di ground truth (es. etichette reali).

**Output e metriche**

I flussi di valutazione producono risultati che misurano le prestazioni del flusso testato. Le metriche possono essere calcolate usando Python o LLM. Usa la funzione log_metric() per registrare le metriche rilevanti.

**Utilizzare flussi di valutazione personalizzati**

Sviluppa un flusso di valutazione su misura per i tuoi compiti e obiettivi specifici. Personalizza le metriche in base agli scopi della valutazione.
Applica questo flusso di valutazione personalizzato a esecuzioni batch per test su larga scala.

## Metodi di valutazione integrati

Prompt Flow offre anche metodi di valutazione predefiniti.
Puoi inviare esecuzioni batch e usare questi metodi per valutare come performa il tuo flusso su grandi dataset.
Visualizza i risultati della valutazione, confronta le metriche e itera secondo necessità.
Ricorda, la valutazione è essenziale per garantire che i tuoi modelli AI soddisfino i criteri e gli obiettivi desiderati. Consulta la documentazione ufficiale per istruzioni dettagliate sullo sviluppo e l’uso dei flussi di valutazione in Microsoft Prompt Flow.

In sintesi, Microsoft Prompt Flow consente agli sviluppatori di creare applicazioni LLM di alta qualità semplificando il prompt engineering e offrendo un ambiente di sviluppo robusto. Se lavori con LLM, Prompt Flow è uno strumento prezioso da esplorare. Consulta i [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) per istruzioni dettagliate su come sviluppare e utilizzare i flussi di valutazione in Microsoft Prompt Flow.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.