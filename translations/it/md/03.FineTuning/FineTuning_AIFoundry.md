# Fine-tuning di Phi-3 con Microsoft Foundry

Esploriamo come fare il fine-tuning del modello linguistico Phi-3 Mini di Microsoft utilizzando Microsoft Foundry. Il fine-tuning ti permette di adattare Phi-3 Mini a compiti specifici, rendendolo ancora più potente e consapevole del contesto.

## Considerazioni

- **Capacità:** Quali modelli possono essere sottoposti a fine-tuning? Cosa può fare il modello base una volta fine-tuned?
- **Costo:** Qual è il modello di pricing per il fine-tuning
- **Personalizzazione:** Quanto posso modificare il modello base – e in quali modi?
- **Convenienza:** Come avviene il fine-tuning – devo scrivere codice personalizzato? Devo portare la mia potenza di calcolo?
- **Sicurezza:** I modelli fine-tuned sono noti per avere rischi di sicurezza – ci sono delle salvaguardie per proteggere da danni non intenzionali?

![AIFoundry Models](../../../../translated_images/it/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Preparazione per il fine-tuning

### Prerequisiti

> [!NOTE]
> Per i modelli della famiglia Phi-3, l'offerta di fine-tuning pay-as-you-go è disponibile solo con hub creati nella regione **East US 2**.

- Un abbonamento Azure. Se non possiedi un abbonamento Azure, crea un [account Azure a pagamento](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) per iniziare.

- Un [progetto AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- I controlli di accesso basati sui ruoli di Azure (Azure RBAC) vengono utilizzati per concedere accesso alle operazioni in Microsoft Foundry. Per eseguire i passaggi in questo articolo, il tuo account utente deve essere assegnato al __ruolo Azure AI Developer__ sul gruppo di risorse.

### Registrazione del provider di sottoscrizione

Verifica che la sottoscrizione sia registrata al provider di risorse `Microsoft.Network`.

1. Accedi al [portale di Azure](https://portal.azure.com).
1. Seleziona **Sottoscrizioni** dal menu a sinistra.
1. Seleziona la sottoscrizione che vuoi usare.
1. Seleziona **Impostazioni progetto AI** > **Provider di risorse** dal menu a sinistra.
1. Conferma che **Microsoft.Network** sia nella lista dei provider di risorse. Altrimenti aggiungilo.

### Preparazione dei dati

Prepara i dati di training e validazione per il fine-tuning del tuo modello. I dataset di training e validazione consistono in esempi di input e output che mostrano come desideri che il modello si comporti.

Assicurati che tutti gli esempi di training seguano il formato previsto per l’inferenza. Per eseguire un fine-tuning efficace, assicurati di avere un dataset bilanciato e variegato.

Ciò comporta mantenere bilanciamento nei dati, includere vari scenari e affinare periodicamente i dati di training per allinearli alle aspettative reali, portando a risposte del modello più accurate e bilanciate.

Tipi diversi di modello richiedono formati differenti dei dati di training.

### Chat Completion

I dati di training e validazione che usi **devono** essere formattati come documento JSON Lines (JSONL). Per `Phi-3-mini-128k-instruct`, il dataset per il fine-tuning deve essere formato nel formato conversazionale usato dall'API di Chat completions.

### Formato file esempio

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Il tipo di file supportato è JSON Lines. I file vengono caricati nel datastore predefinito e resi disponibili nel tuo progetto.

## Fine-Tuning di Phi-3 con Microsoft Foundry

Microsoft Foundry ti consente di personalizzare grandi modelli linguistici sui tuoi dataset personali tramite un processo noto come fine-tuning. Il fine-tuning fornisce un grande valore abilitando la personalizzazione e l’ottimizzazione per compiti e applicazioni specifici. Porta a prestazioni migliorate, efficienza dei costi, riduzione della latenza e output personalizzati.

![Finetune AI Foundry](../../../../translated_images/it/AIFoundryfinetune.193aaddce48d553c.webp)

### Creare un nuovo progetto

1. Accedi a [Microsoft Foundry](https://ai.azure.com).

1. Seleziona **+New project** per creare un nuovo progetto in Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/it/select-new-project.cd31c0404088d7a3.webp)

1. Esegui i seguenti passaggi:

    - Inserisci il **Nome Hub** del progetto. Deve essere un valore univoco.
    - Seleziona l'**Hub** da utilizzare (creane uno nuovo se necessario).

    ![FineTuneSelect](../../../../translated_images/it/create-project.ca3b71298b90e420.webp)

1. Esegui i passaggi seguenti per creare un nuovo hub:

    - Inserisci il **Nome Hub**. Deve essere un valore univoco.
    - Seleziona la tua **Sottoscrizione Azure**.
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo se necessario).
    - Seleziona la **Posizione** che vuoi usare.
    - Seleziona il **Connect Azure AI Services** da usare (creane uno nuovo se necessario).
    - Seleziona **Connect Azure AI Search** su **Salta connessione**.

    ![FineTuneSelect](../../../../translated_images/it/create-hub.49e53d235e80779e.webp)

1. Seleziona **Avanti**.
1. Seleziona **Crea un progetto**.

### Preparazione dei dati

Prima del fine-tuning, raccogli o crea un dataset rilevante per il tuo compito, ad esempio istruzioni chat, coppie domanda-risposta o qualsiasi altro testo pertinente. Pulisci e pre-processa i dati rimuovendo rumore, gestendo valori mancanti e tokenizzando il testo.

### Fine-tuning dei modelli Phi-3 in Microsoft Foundry

> [!NOTE]
> Il fine-tuning dei modelli Phi-3 è attualmente supportato solo in progetti localizzati in East US 2.

1. Seleziona **Catalogo modelli** dal pannello a sinistra.

1. Digita *phi-3* nella **barra di ricerca** e seleziona il modello phi-3 che vuoi utilizzare.

    ![FineTuneSelect](../../../../translated_images/it/select-model.60ef2d4a6a3cec57.webp)

1. Seleziona **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/it/select-finetune.a976213b543dd9d8.webp)

1. Inserisci il **Nome del modello fine-tuned**.

    ![FineTuneSelect](../../../../translated_images/it/finetune1.c2b39463f0d34148.webp)

1. Seleziona **Avanti**.

1. Esegui i seguenti passaggi:

    - Seleziona il **tipo di task** come **Completamento chat**.
    - Seleziona i **dati di training** che vuoi utilizzare. Puoi caricarli tramite i dati di Microsoft Foundry o dal tuo ambiente locale.

    ![FineTuneSelect](../../../../translated_images/it/finetune2.43cb099b1a94442d.webp)

1. Seleziona **Avanti**.

1. Carica i **dati di validazione** che vuoi utilizzare, oppure seleziona **Suddivisione automatica dei dati di training**.

    ![FineTuneSelect](../../../../translated_images/it/finetune3.fd96121b67dcdd92.webp)

1. Seleziona **Avanti**.

1. Esegui i seguenti passaggi:

    - Seleziona il **moltiplicatore della dimensione batch** che desideri usare.
    - Seleziona il **learning rate** desiderato.
    - Seleziona il numero di **epoche** da usare.

    ![FineTuneSelect](../../../../translated_images/it/finetune4.e18b80ffccb5834a.webp)

1. Seleziona **Invia** per avviare il processo di fine-tuning.

    ![FineTuneSelect](../../../../translated_images/it/select-submit.0a3802d581bac271.webp)


1. Una volta che il modello è stato fine-tuned, lo stato sarà visualizzato come **Completato**, come mostrato nell’immagine sottostante. Ora puoi distribuire il modello e usarlo nella tua applicazione, nel playground o in prompt flow. Per maggiori informazioni, consulta [Come distribuire la famiglia di modelli linguistici piccoli Phi-3 con Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/it/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Per informazioni più dettagliate sul fine-tuning di Phi-3, visita [Fine-tune dei modelli Phi-3 in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Pulizia dei tuoi modelli fine-tuned

Puoi eliminare un modello fine-tuned dalla lista dei modelli di fine-tuning in [Microsoft Foundry](https://ai.azure.com) o dalla pagina dei dettagli del modello. Seleziona il modello fine-tuned da eliminare nella pagina Fine-tuning, quindi seleziona il pulsante Elimina per rimuoverlo.

> [!NOTE]
> Non puoi eliminare un modello personalizzato se ha una distribuzione esistente. Devi prima eliminare la distribuzione del modello prima di poter eliminare il modello personalizzato.

## Costi e quote

### Considerazioni su costi e quote per modelli Phi-3 fine-tuned come servizio

I modelli Phi fine-tuned come servizio sono offerti da Microsoft e integrati con Microsoft Foundry per l’uso. Puoi trovare i prezzi per la [distribuzione](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) o il fine-tuning dei modelli nella scheda Prezzi e termini della procedura guidata di distribuzione.

## Filtro dei contenuti

I modelli distribuiti come servizio con pay-as-you-go sono protetti da Azure AI Content Safety. Quando distribuiti in endpoint realtime, puoi scegliere di disabilitare questa funzionalità. Con Azure AI Content Safety abilitato, sia il prompt che la risposta passano attraverso un insieme di modelli di classificazione mirati a rilevare e prevenire l’output di contenuti dannosi. Il sistema di filtro dei contenuti rileva e prende azioni su specifiche categorie di contenuti potenzialmente dannosi sia nei prompt di input sia nelle risposte di output. Scopri di più su [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configurazione Fine-Tuning**

Iperparametri: Definisci iperparametri come learning rate, dimensione batch, numero di epoche di training.

**Funzione di perdita**

Scegli una funzione di perdita appropriata per il tuo task (es. cross-entropy).

**Ottimizzatore**

Seleziona un ottimizzatore (es. Adam) per gli aggiornamenti del gradiente durante l’addestramento.

**Processo di fine-tuning**

- Carica il modello preaddestrato: carica il checkpoint Phi-3 Mini.
- Aggiungi layer personalizzati: aggiungi layer specifici per il task (es. testa di classificazione per istruzioni da chat).

**Addestra il modello**

Fine-tuning del modello usando il dataset preparato. Monitora il progresso dell’addestramento e adatta gli iperparametri se necessario.

**Valutazione e validazione**

Set di validazione: suddividi i dati in set di training e validazione.

**Valuta le prestazioni**

Usa metriche come accuratezza, F1-score o perplexity per valutare le prestazioni del modello.

## Salva il modello fine-tuned

**Checkpoint**

Salva il checkpoint del modello fine-tuned per usi futuri.

## Distribuzione

- Distribuisci come servizio web: Distribuisci il modello fine-tuned come un servizio web in Microsoft Foundry.
- Testa l’endpoint: Invia query di test all’endpoint distribuito per verificarne il funzionamento.

## Itera e migliora

Itèra: se le prestazioni non sono soddisfacenti, itera regolando iperparametri, aggiungendo dati o eseguendo fine-tuning per epoche aggiuntive.

## Monitora e affina

Monitora continuamente il comportamento del modello e affinalo se necessario.

## Personalizza ed estendi

Task personalizzati: Phi-3 Mini può essere fine-tuned per vari compiti oltre alle istruzioni da chat. Esplora altri casi d’uso!
Sperimenta: Prova architetture diverse, combinazioni di layer e tecniche per migliorare le prestazioni.

> [!NOTE]
> Il fine-tuning è un processo iterativo. Sperimenta, impara e adatta il tuo modello per ottenere i migliori risultati per il tuo specifico compito!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur facendo il possibile per garantire la precisione, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->