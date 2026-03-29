# **Utilizzo di Microsoft Foundry per la valutazione**

![aistudo](../../../../../translated_images/it/AIFoundry.9e0b513e999a1c5a.webp)

Come valutare la tua applicazione di intelligenza artificiale generativa utilizzando [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Che tu stia valutando conversazioni a turno singolo o multi-turno, Microsoft Foundry fornisce strumenti per valutare le prestazioni del modello e la sicurezza.

![aistudo](../../../../../translated_images/it/AIPortfolio.69da59a8e1eaa70f.webp)

## Come valutare le app di intelligenza artificiale generativa con Microsoft Foundry
Per istruzioni più dettagliate consulta la [Documentazione di Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Ecco i passaggi per iniziare:

## Valutazione dei modelli di intelligenza artificiale generativa in Microsoft Foundry

**Prerequisiti**

- Un dataset di test in formato CSV o JSON.
- Un modello di intelligenza artificiale generativa distribuito (come Phi-3, GPT 3.5, GPT 4 o modelli Davinci).
- Un runtime con un'istanza di calcolo per eseguire la valutazione.

## Metriche di valutazione incorporate

Microsoft Foundry consente di valutare sia conversazioni a turno singolo sia conversazioni complesse multi-turno.  
Per scenari di Retrieval Augmented Generation (RAG), dove il modello si basa su dati specifici, è possibile valutare le prestazioni utilizzando le metriche di valutazione incorporate.  
Inoltre, è possibile valutare scenari generali di risposta a domande a turno singolo (non RAG).

## Creazione di una sessione di valutazione

Dall'interfaccia di Microsoft Foundry, vai alla pagina Evaluate oppure alla pagina Prompt Flow.  
Segui la procedura guidata per la creazione della valutazione per configurare una sessione di valutazione. Fornisci un nome facoltativo per la tua valutazione.  
Seleziona lo scenario che corrisponde agli obiettivi della tua applicazione.  
Scegli una o più metriche di valutazione per valutare l'output del modello.

## Flusso di valutazione personalizzato (opzionale)

Per una maggiore flessibilità, puoi creare un flusso di valutazione personalizzato. Personalizza il processo di valutazione in base ai tuoi requisiti specifici.

## Visualizzazione dei risultati

Dopo aver eseguito la valutazione, registra, visualizza e analizza le metriche di valutazione dettagliate in Microsoft Foundry. Ottieni informazioni sulle capacità e le limitazioni della tua applicazione.

**Note** Microsoft Foundry è attualmente in anteprima pubblica, quindi usalo per scopi di sperimentazione e sviluppo. Per carichi di lavoro di produzione, considera altre opzioni. Esplora la documentazione ufficiale di [AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) per maggiori dettagli e istruzioni passo passo.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur sforzandoci di garantire l’accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->