# **Utilizzo di Phi-3 in Microsoft Foundry**

Con lo sviluppo dell'IA generativa, speriamo di utilizzare una piattaforma unificata per gestire diversi LLM e SLM, integrazione dei dati aziendali, operazioni di fine-tuning/RAG e la valutazione di diverse attività aziendali dopo l'integrazione di LLM e SLM, ecc., in modo che l'IA generativa possa implementare meglio applicazioni intelligenti. [Microsoft Foundry](https://ai.azure.com) è una piattaforma di applicazioni IA generativa a livello aziendale.

![aistudo](../../../../translated_images/it/aifoundry_home.f28a8127c96c7d93.webp)

Con Microsoft Foundry, puoi valutare le risposte dei modelli di linguaggio di grandi dimensioni (LLM) e orchestrare componenti di applicazione prompt con prompt flow per migliori prestazioni. La piattaforma facilita la scalabilità nella trasformazione di proof of concept in produzione completa con facilità. Il monitoraggio continuo e il perfezionamento supportano il successo a lungo termine.

Possiamo rapidamente distribuire il modello Phi-3 su Microsoft Foundry tramite semplici passaggi, e poi utilizzare Microsoft Foundry per completare Playground/Chat, Fine-tuning, valutazione e altri lavori correlati a Phi-3.

## **1. Preparazione**

Se hai già installato [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) sulla tua macchina, usare questo template è semplice come eseguire questo comando in una nuova directory.

## Creazione Manuale

Creare un progetto e un hub in Microsoft Foundry è un ottimo modo per organizzare e gestire il tuo lavoro di IA. Ecco una guida passo-passo per iniziare:

### Creare un Progetto in Microsoft Foundry

1. **Vai a Microsoft Foundry**: Accedi al portale Microsoft Foundry.
2. **Crea un Progetto**:
   - Se sei dentro un progetto, seleziona "Microsoft Foundry" in alto a sinistra della pagina per andare alla Home page.
   - Seleziona "+ Crea progetto".
   - Inserisci un nome per il progetto.
   - Se hai un hub, sarà selezionato di default. Se hai accesso a più di un hub, puoi selezionarne uno diverso dal menu a tendina. Se vuoi creare un nuovo hub, seleziona "Crea nuovo hub" e fornisci un nome.
   - Seleziona "Crea".

### Creare un Hub in Microsoft Foundry

1. **Vai a Microsoft Foundry**: Accedi con il tuo account Azure.
2. **Crea un Hub**:
   - Seleziona il Centro di gestione dal menu a sinistra.
   - Seleziona "Tutte le risorse", poi la freccia verso il basso accanto a "+ Nuovo progetto" e seleziona "+ Nuovo hub".
   - Nella finestra "Crea un nuovo hub", inserisci un nome per il tuo hub (ad esempio, contoso-hub) e modifica gli altri campi come desiderato.
   - Seleziona "Avanti", rivedi le informazioni, quindi seleziona "Crea".

Per istruzioni più dettagliate, puoi fare riferimento alla documentazione ufficiale di [Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Dopo la creazione avvenuta con successo, puoi accedere allo studio creato tramite [ai.azure.com](https://ai.azure.com/)

È possibile avere più progetti su un singolo AI Foundry. Crea un progetto in AI Foundry per prepararti.

Crea i [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code) di Microsoft Foundry


## **2. Distribuire un modello Phi in Microsoft Foundry**

Clicca sull'opzione Esplora del progetto per entrare nel Catalogo Modelli e seleziona Phi-3

Seleziona Phi-3-mini-4k-instruct

Clicca su 'Distribuisci' per distribuire il modello Phi-3-mini-4k-instruct

> [!NOTE]
>
> Puoi selezionare la potenza di calcolo durante la distribuzione

## **3. Playground Chat Phi in Microsoft Foundry**

Vai alla pagina di distribuzione, seleziona Playground e chatta con Phi-3 di Microsoft Foundry

## **4. Distribuire il Modello da Microsoft Foundry**

Per distribuire un modello dal Catalogo Modelli di Azure, puoi seguire questi passaggi:

- Accedi a Microsoft Foundry.
- Scegli il modello che desideri distribuire dal catalogo modelli di Microsoft Foundry.
- Nella pagina Dettagli del modello, seleziona Distribuisci e poi seleziona Serverless API con Azure AI Content Safety.
- Seleziona il progetto in cui vuoi distribuire i tuoi modelli. Per usare l'offerta Serverless API, il tuo workspace deve appartenere alla regione East US 2 o Sweden Central. Puoi personalizzare il nome della distribuzione.
- Sul wizard di distribuzione, seleziona i Prezzi e termini per conoscere i prezzi e i termini di utilizzo.
- Seleziona Distribuisci. Attendi che la distribuzione sia pronta e verrai reindirizzato alla pagina Distribuzioni.
- Seleziona Apri in playground per iniziare a interagire con il modello.
- Puoi tornare alla pagina Distribuzioni, selezionare la distribuzione e annotare l'URL di destinazione dell'endpoint e la Chiave segreta, che puoi usare per chiamare la distribuzione e generare completamenti.
- Puoi sempre trovare i dettagli dell'endpoint, URL e chiavi di accesso navigando alla scheda Build e selezionando Distribuzioni dalla sezione Componenti.

> [!NOTE]
> Tieni presente che il tuo account deve avere i permessi del ruolo Azure AI Developer sul Gruppo di Risorse per eseguire questi passaggi.

## **5. Utilizzo dell'API Phi in Microsoft Foundry**

Puoi accedere a https://{Your project name}.region.inference.ml.azure.com/swagger.json tramite Postman con GET e combinarla con la Chiave per conoscere le interfacce fornite

Puoi ottenere in modo molto comodo i parametri di richiesta, così come i parametri di risposta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l'accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->