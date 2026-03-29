# Valutare il modello Phi-3 / Phi-3.5 personalizzato in Microsoft Foundry concentrandosi sui Principi di AI Responsabile di Microsoft

Questo esempio end-to-end (E2E) si basa sulla guida "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" della Microsoft Tech Community.

## Panoramica

### Come puoi valutare la sicurezza e le prestazioni di un modello Phi-3 / Phi-3.5 personalizzato in Microsoft Foundry?

La personalizzazione di un modello può a volte portare a risposte non intenzionali o indesiderate. Per garantire che il modello rimanga sicuro ed efficace, è importante valutare il potenziale del modello di generare contenuti dannosi e la sua capacità di produrre risposte accurate, pertinenti e coerenti. In questo tutorial, imparerai come valutare la sicurezza e le prestazioni di un modello Phi-3 / Phi-3.5 personalizzato integrato con Prompt flow in Microsoft Foundry.

Ecco il processo di valutazione di Microsoft Foundry.

![Architettura del tutorial.](../../../../../../translated_images/it/architecture.10bec55250f5d6a4.webp)

*Fonte immagine: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Per informazioni più dettagliate ed esplorare ulteriori risorse su Phi-3 / Phi-3.5, visita il [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prerequisiti

- [Python](https://www.python.org/downloads)
- [Abbonamento Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modello Phi-3 / Phi-3.5 personalizzato

### Indice

1. [**Scenario 1: Introduzione alla valutazione con Prompt flow di Microsoft Foundry**](#scenario-1-introduzione-alla-valutazione-con-prompt-flow-di-azure-ai-studios)

    - [Introduzione alla valutazione della sicurezza](#introduzione-alla-valutazione-della-sicurezza)
    - [Introduzione alla valutazione delle prestazioni](#introduzione-alla-valutazione-delle-prestazioni)

1. [**Scenario 2: Valutazione del modello Phi-3 / Phi-3.5 in Microsoft Foundry**](#scenario-2-valutazione-del-modello-phi-3--phi-35-in-azure-ai-studio)

    - [Prima di iniziare](#prima-di-iniziare)
    - [Distribuire Azure OpenAI per valutare il modello Phi-3 / Phi-3.5](#distribuire-azure-openai-per-valutare-il-modello-phi-3--phi-35)
    - [Valutare il modello Phi-3 / Phi-3.5 personalizzato usando la valutazione Prompt flow di Microsoft Foundry](#valutare-il-modello-phi-3--phi-35-personalizzato-usando-la-valutazione-prompt-flow-di-azure-ai-studio)

1. [Congratulazioni!](#congratulazioni)

## **Scenario 1: Introduzione alla valutazione con Prompt flow di Microsoft Foundry**

### Introduzione alla valutazione della sicurezza

Per garantire che il tuo modello di AI sia etico e sicuro, è fondamentale valutarlo rispetto ai Principi di AI Responsabile di Microsoft. In Microsoft Foundry, le valutazioni di sicurezza ti permettono di valutare la vulnerabilità del tuo modello ad attacchi di jailbreak e il suo potenziale di generare contenuti dannosi, in linea diretta con questi principi.

![Valutazione della sicurezza.](../../../../../../translated_images/it/safety-evaluation.083586ec88dfa950.webp)

*Fonte immagine: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### I Principi di AI Responsabile di Microsoft

Prima di iniziare i passaggi tecnici, è essenziale comprendere i Principi di AI Responsabile di Microsoft, un quadro etico progettato per guidare lo sviluppo, la distribuzione e l’operatività responsabile dei sistemi di AI. Questi principi guidano la progettazione, sviluppo e distribuzione responsabile di sistemi di AI, assicurando che le tecnologie AI siano costruite in modo equo, trasparente e inclusivo. Questi principi costituiscono la base per valutare la sicurezza dei modelli AI.

I Principi di AI Responsabile di Microsoft includono:

- **Equità e Inclusività**: I sistemi AI dovrebbero trattare tutti in modo equo ed evitare di influenzare gruppi di persone in situazioni simili in modi differenti. Ad esempio, quando i sistemi AI forniscono indicazioni su trattamenti medici, richieste di prestito o occupazione, dovrebbero fare le stesse raccomandazioni a chiunque abbia sintomi simili, condizioni finanziarie o qualifiche professionali simili.

- **Affidabilità e Sicurezza**: Per costruire fiducia, è fondamentale che i sistemi AI operino in modo affidabile, sicuro e coerente. Questi sistemi dovrebbero essere in grado di funzionare come progettati originariamente, rispondere in sicurezza a condizioni impreviste e resistere a manipolazioni dannose. Il loro comportamento e la varietà di condizioni che possono gestire riflettono l’ampiezza delle situazioni e circostanze anticipate dagli sviluppatori durante progettazione e test.

- **Trasparenza**: Quando i sistemi AI aiutano a informare decisioni che hanno forti impatti sulle vite delle persone, è fondamentale che le persone capiscano come quelle decisioni sono state prese. Per esempio, una banca potrebbe usare un sistema AI per decidere se una persona è meritevole di credito. Un’azienda potrebbe usare un sistema AI per determinare i candidati più qualificati da assumere.

- **Privacy e Sicurezza**: Con la crescente diffusione dell’AI, proteggere la privacy e mettere in sicurezza le informazioni personali e aziendali diventano sempre più importanti e complessi. Con l’AI, la privacy e la sicurezza dei dati richiedono particolare attenzione perché l’accesso ai dati è essenziale affinché i sistemi AI effettuino previsioni e decisioni accurate e informate riguardo alle persone.

- **Responsabilità**: Le persone che progettano e distribuiscono i sistemi AI devono essere responsabili di come i loro sistemi operano. Le organizzazioni dovrebbero basarsi su standard industriali per sviluppare norme di responsabilità. Queste norme possono garantire che i sistemi AI non siano l’autorità finale su nessuna decisione che influisca sulle vite delle persone. Possono anche assicurare che gli umani mantengano un controllo significativo su sistemi AI altrimenti altamente autonomi.

![Fill hub.](../../../../../../translated_images/it/responsibleai2.c07ef430113fad8c.webp)

*Fonte immagine: [Cos’è l’AI Responsabile?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Per saperne di più sui Principi di AI Responsabile di Microsoft, visita la pagina [Cos’è l’AI Responsabile?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metriche di sicurezza

In questo tutorial, valuterai la sicurezza del modello Phi-3 personalizzato utilizzando le metriche di sicurezza di Microsoft Foundry. Queste metriche ti aiutano a valutare il potenziale del modello di generare contenuti dannosi e la sua vulnerabilità ad attacchi di jailbreak. Le metriche di sicurezza includono:

- **Contenuti relazionati all’autolesionismo**: Valuta se il modello tende a produrre contenuti relativi all’autolesionismo.
- **Contenuti d’odio e ingiusti**: Valuta se il modello tende a produrre contenuti d’odio o ingiusti.
- **Contenuti violenti**: Valuta se il modello tende a produrre contenuti violenti.
- **Contenuti sessuali**: Valuta se il modello tende a produrre contenuti sessuali inappropriati.

Valutare questi aspetti garantisce che il modello AI non produca contenuti dannosi o offensivi, allineandolo con i valori sociali e gli standard normativi.

![Valutazione basata sulla sicurezza.](../../../../../../translated_images/it/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introduzione alla valutazione delle prestazioni

Per assicurarti che il tuo modello AI stia funzionando come previsto, è importante valutarne le prestazioni rispetto a metriche di performance. In Microsoft Foundry, le valutazioni di prestazioni ti consentono di valutare l’efficacia del modello nel generare risposte accurate, pertinenti e coerenti.

![Valutazione della sicurezza.](../../../../../../translated_images/it/performance-evaluation.48b3e7e01a098740.webp)

*Fonte immagine: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metriche di prestazione

In questo tutorial, valuterai le prestazioni del modello Phi-3 / Phi-3.5 personalizzato utilizzando le metriche di prestazione di Microsoft Foundry. Queste metriche ti aiutano a valutare l’efficacia del modello nel generare risposte accurate, rilevanti e coerenti. Le metriche di prestazione includono:

- **Accuratezza rispetto alla fonte (Groundedness)**: Valuta quanto le risposte generate si allineano alle informazioni dalla fonte di input.
- **Rilevanza**: Valuta la pertinenza delle risposte generate alle domande fornite.
- **Coerenza**: Valuta quanto fluido è il testo generato, se si legge in modo naturale e somiglia al linguaggio umano.
- **Fluidità**: Valuta la competenza linguistica del testo generato.
- **Similarità GPT**: Confronta la risposta generata con la verità di base per similarità.
- **Punteggio F1**: Calcola la proporzione di parole in comune tra la risposta generata e i dati di origine.

Queste metriche ti aiutano a valutare l’efficacia del modello nel generare risposte accurate, pertinenti e coerenti.

![Valutazione basata sulle prestazioni.](../../../../../../translated_images/it/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenario 2: Valutazione del modello Phi-3 / Phi-3.5 in Microsoft Foundry**

### Prima di iniziare

Questo tutorial è un seguito dei precedenti post del blog, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In questi post, abbiamo percorso il processo di personalizzazione di un modello Phi-3 / Phi-3.5 in Microsoft Foundry e la sua integrazione con Prompt flow.

In questo tutorial, distribuirai un modello Azure OpenAI come valutatore in Microsoft Foundry e lo userai per valutare il tuo modello Phi-3 / Phi-3.5 personalizzato.

Prima di iniziare questo tutorial, assicurati di avere i seguenti prerequisiti, come descritto nei tutorial precedenti:

1. Un dataset preparato per valutare il modello Phi-3 / Phi-3.5 personalizzato.
1. Un modello Phi-3 / Phi-3.5 personalizzato che sia stato fine-tuned e distribuito su Azure Machine Learning.
1. Un Prompt flow integrato con il tuo modello Phi-3 / Phi-3.5 personalizzato in Microsoft Foundry.

> [!NOTE]
> Userai il file *test_data.jsonl*, situato nella cartella data del dataset **ULTRACHAT_200k** scaricato nei post precedenti, come dataset per valutare il modello Phi-3 / Phi-3.5 personalizzato.

#### Integrare il modello personalizzato Phi-3 / Phi-3.5 con Prompt flow in Microsoft Foundry (approccio code first)

> [!NOTE]
> Se hai seguito l’approccio low-code descritto in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", puoi saltare questo esercizio e procedere al successivo.  
> Tuttavia, se hai seguito l’approccio code-first descritto in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" per personalizzare e distribuire il tuo modello Phi-3 / Phi-3.5, il processo di connessione del modello a Prompt flow è leggermente diverso. Imparerai questo processo in questo esercizio.

Per procedere, devi integrare il tuo modello Phi-3 / Phi-3.5 personalizzato in Prompt flow in Microsoft Foundry.

#### Creare Microsoft Foundry Hub

È necessario creare un Hub prima di creare il Progetto. Un Hub funge da Resource Group, permettendoti di organizzare e gestire più Progetti all’interno di Microsoft Foundry.
1. Accedi a [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Seleziona **Tutti gli hub** dalla scheda laterale sinistra.

1. Seleziona **+ Nuovo hub** dal menu di navigazione.

    ![Create hub.](../../../../../../translated_images/it/create-hub.5be78fb1e21ffbf1.webp)

1. Esegui le seguenti operazioni:

    - Inserisci **Nome hub**. Deve essere un valore univoco.
    - Seleziona la tua **Sottoscrizione** Azure.
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo se necessario).
    - Seleziona la **Posizione** che desideri utilizzare.
    - Seleziona **Connetti servizi AI di Azure** da utilizzare (creane uno nuovo se necessario).
    - Seleziona **Connetti Azure AI Search** su **Salta connessione**.

    ![Fill hub.](../../../../../../translated_images/it/fill-hub.baaa108495c71e34.webp)

1. Seleziona **Avanti**.

#### Crea Progetto Microsoft Foundry

1. Nell’Hub che hai creato, seleziona **Tutti i progetti** dalla scheda laterale sinistra.

1. Seleziona **+ Nuovo progetto** dal menu di navigazione.

    ![Select new project.](../../../../../../translated_images/it/select-new-project.cd31c0404088d7a3.webp)

1. Inserisci **Nome progetto**. Deve essere un valore univoco.

    ![Create project.](../../../../../../translated_images/it/create-project.ca3b71298b90e420.webp)

1. Seleziona **Crea progetto**.

#### Aggiungi una connessione personalizzata per il modello Phi-3 / Phi-3.5 fine-tuned

Per integrare il tuo modello Phi-3 / Phi-3.5 personalizzato con Prompt flow, devi salvare l'endpoint e la chiave del modello in una connessione personalizzata. Questa configurazione garantisce l'accesso al tuo modello Phi-3 / Phi-3.5 personalizzato in Prompt flow.

#### Imposta la chiave api e l'URI dell'endpoint del modello Phi-3 / Phi-3.5 fine-tuned

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviga allo spazio di lavoro Azure Machine learning che hai creato.

1. Seleziona **Endpoints** dalla scheda laterale sinistra.

    ![Select endpoints.](../../../../../../translated_images/it/select-endpoints.ee7387ecd68bd18d.webp)

1. Seleziona l’endpoint che hai creato.

    ![Select endpoints.](../../../../../../translated_images/it/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Seleziona **Consume** dal menu di navigazione.

1. Copia il tuo **endpoint REST** e la **Chiave primaria**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/it/copy-endpoint-key.0650c3786bd646ab.webp)

#### Aggiungi la Connessione Personalizzata

1. Visita [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviga al progetto Microsoft Foundry che hai creato.

1. Nel Progetto che hai creato, seleziona **Impostazioni** dalla scheda laterale sinistra.

1. Seleziona **+ Nuova connessione**.

    ![Select new connection.](../../../../../../translated_images/it/select-new-connection.fa0f35743758a74b.webp)

1. Seleziona **Chiavi personalizzate** dal menu di navigazione.

    ![Select custom keys.](../../../../../../translated_images/it/select-custom-keys.5a3c6b25580a9b67.webp)

1. Esegui le seguenti operazioni:

    - Seleziona **+ Aggiungi coppie chiave-valore**.
    - Per il nome della chiave, inserisci **endpoint** e incolla l’endpoint copiato da Azure ML Studio nel campo valore.
    - Seleziona nuovamente **+ Aggiungi coppie chiave-valore**.
    - Per il nome della chiave, inserisci **key** e incolla la chiave copiata da Azure ML Studio nel campo valore.
    - Dopo aver aggiunto le chiavi, seleziona **è segreta** per evitare che la chiave venga esposta.

    ![Add connection.](../../../../../../translated_images/it/add-connection.ac7f5faf8b10b0df.webp)

1. Seleziona **Aggiungi connessione**.

#### Crea Prompt flow

Hai aggiunto una connessione personalizzata in Microsoft Foundry. Ora, creiamo un Prompt flow seguendo questi passaggi. Successivamente collegherai questo Prompt flow alla connessione personalizzata per usare il modello fine-tuned all’interno del Prompt flow.

1. Naviga al progetto Microsoft Foundry che hai creato.

1. Seleziona **Prompt flow** dalla scheda laterale sinistra.

1. Seleziona **+ Crea** dal menu di navigazione.

    ![Select Promptflow.](../../../../../../translated_images/it/select-promptflow.18ff2e61ab9173eb.webp)

1. Seleziona **Chat flow** dal menu di navigazione.

    ![Select chat flow.](../../../../../../translated_images/it/select-flow-type.28375125ec9996d3.webp)

1. Inserisci **Nome cartella** da usare.

    ![Select chat flow.](../../../../../../translated_images/it/enter-name.02ddf8fb840ad430.webp)

1. Seleziona **Crea**.

#### Configura Prompt flow per chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato

Devi integrare il modello Phi-3 / Phi-3.5 fine-tuned in un Prompt flow. Tuttavia, il Prompt flow esistente fornito non è stato progettato per questo scopo. Pertanto, devi riprogettare il Prompt flow per abilitare l’integrazione del modello personalizzato.

1. Nel Prompt flow, esegui le seguenti operazioni per ricostruire il flusso esistente:

    - Seleziona **Modalità file grezzo**.
    - Cancella tutto il codice esistente nel file *flow.dag.yml*.
    - Aggiungi il seguente codice in *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Seleziona **Salva**.

    ![Select raw file mode.](../../../../../../translated_images/it/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Aggiungi il seguente codice in *integrate_with_promptflow.py* per usare il modello Phi-3 / Phi-3.5 personalizzato nel Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Configurazione del logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" è il nome della Connessione Personalizzata, "endpoint", "key" sono le chiavi nella Connessione Personalizzata
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Registra la risposta JSON completa
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/it/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Per informazioni più dettagliate sull’uso di Prompt flow in Microsoft Foundry, puoi fare riferimento a [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Seleziona **Chat input**, **Chat output** per abilitare la chat con il modello.

    ![Select Input Output.](../../../../../../translated_images/it/select-input-output.c187fc58f25fbfc3.webp)

1. Ora sei pronto per chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato. Nel prossimo esercizio, imparerai come avviare Prompt flow e usarlo per chattare con il modello Phi-3 / Phi-3.5 fine-tuned.

> [!NOTE]
>
> Il flusso ricostruito dovrebbe apparire come nell’immagine seguente:
>
> ![Flow example](../../../../../../translated_images/it/graph-example.82fd1bcdd3fc545b.webp)
>

#### Avvia Prompt flow

1. Seleziona **Avvia sessioni di calcolo** per avviare Prompt flow.

    ![Start compute session.](../../../../../../translated_images/it/start-compute-session.9acd8cbbd2c43df1.webp)

1. Seleziona **Convalida e analizza input** per aggiornare i parametri.

    ![Validate input.](../../../../../../translated_images/it/validate-input.c1adb9543c6495be.webp)

1. Seleziona il **Valore** della **connessione** verso la connessione personalizzata che hai creato. Ad esempio, *connection*.

    ![Connection.](../../../../../../translated_images/it/select-connection.1f2b59222bcaafef.webp)

#### Chatta con il tuo modello Phi-3 / Phi-3.5 personalizzato

1. Seleziona **Chat**.

    ![Select chat.](../../../../../../translated_images/it/select-chat.0406bd9687d0c49d.webp)

1. Ecco un esempio dei risultati: ora puoi chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato. Si consiglia di porre domande basate sui dati utilizzati per il fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/it/chat-with-promptflow.1cf8cea112359ada.webp)

### Distribuire Azure OpenAI per valutare il modello Phi-3 / Phi-3.5

Per valutare il modello Phi-3 / Phi-3.5 in Microsoft Foundry, è necessario distribuire un modello Azure OpenAI. Questo modello sarà utilizzato per valutare le prestazioni del modello Phi-3 / Phi-3.5.

#### Distribuisci Azure OpenAI

1. Accedi a [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviga al progetto Microsoft Foundry che hai creato.

    ![Select Project.](../../../../../../translated_images/it/select-project-created.5221e0e403e2c9d6.webp)

1. Nel Progetto che hai creato, seleziona **Distribuzioni** dalla scheda laterale sinistra.

1. Seleziona **+ Distribuisci modello** dal menu di navigazione.

1. Seleziona **Distribuisci modello base**.

    ![Select Deployments.](../../../../../../translated_images/it/deploy-openai-model.95d812346b25834b.webp)

1. Seleziona il modello Azure OpenAI che desideri usare. Ad esempio, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/it/select-openai-model.959496d7e311546d.webp)

1. Seleziona **Conferma**.

### Valuta il modello Phi-3 / Phi-3.5 fine-tuned usando la valutazione Prompt flow di Microsoft Foundry

### Avvia una nuova valutazione

1. Visita [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviga al progetto Microsoft Foundry che hai creato.

    ![Select Project.](../../../../../../translated_images/it/select-project-created.5221e0e403e2c9d6.webp)

1. Nel Progetto che hai creato, seleziona **Valutazione** dalla scheda laterale sinistra.

1. Seleziona **+ Nuova valutazione** dal menu di navigazione.

    ![Select evaluation.](../../../../../../translated_images/it/select-evaluation.2846ad7aaaca7f4f.webp)

1. Seleziona la valutazione **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/it/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Esegui le seguenti operazioni:

    - Inserisci il nome della valutazione. Deve essere un valore univoco.
    - Seleziona **Domanda e risposta senza contesto** come tipo di attività. Perché il dataset **UlTRACHAT_200k** usato in questo tutorial non contiene contesto.
    - Seleziona il prompt flow che desideri valutare.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting1.4aa08259ff7a536e.webp)

1. Seleziona **Avanti**.

1. Esegui le seguenti operazioni:

    - Seleziona **Aggiungi il tuo dataset** per caricare il dataset. Ad esempio, puoi caricare il file del dataset di test, come *test_data.json1*, incluso quando scarichi il dataset **ULTRACHAT_200k**.
    - Seleziona la **Colonna dataset** appropriata che corrisponde al tuo dataset. Ad esempio, se usi il dataset **ULTRACHAT_200k**, seleziona **${data.prompt}** come colonna dataset.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting2.07036831ba58d64e.webp)

1. Seleziona **Avanti**.

1. Esegui le seguenti operazioni per configurare le metriche di prestazioni e qualità:

    - Seleziona le metriche di prestazioni e qualità che desideri usare.
    - Seleziona il modello Azure OpenAI che hai creato per la valutazione. Ad esempio, seleziona **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Esegui le seguenti operazioni per configurare le metriche di rischio e sicurezza:

    - Seleziona le metriche di rischio e sicurezza che desideri usare.
    - Seleziona la soglia per calcolare il tasso di difetti che desideri utilizzare. Ad esempio, seleziona **Medio**.
    - Per **domanda**, seleziona **Origine dati** su **{$data.prompt}**.
    - Per **risposta**, seleziona **Origine dati** su **{$run.outputs.answer}**.
    - Per **verità di terra**, seleziona **Origine dati** su **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Seleziona **Avanti**.

1. Seleziona **Invia** per avviare la valutazione.

1. La valutazione richiederà del tempo per essere completata. Puoi monitorare i progressi nella scheda **Valutazione**.

### Esamina i risultati della valutazione

> [!NOTE]
> I risultati presentati di seguito sono intesi a illustrare il processo di valutazione. In questo tutorial, abbiamo utilizzato un modello fine-tuned su un dataset relativamente piccolo, che potrebbe portare a risultati subottimali. I risultati effettivi possono variare significativamente in base alla dimensione, qualità e diversità del dataset utilizzato, nonché alla configurazione specifica del modello.

Una volta completata la valutazione, puoi rivedere i risultati sia delle metriche di prestazioni che di sicurezza.
1. Metriche di prestazione e qualità:

    - valuta l'efficacia del modello nel generare risposte coerenti, fluenti e pertinenti.

    ![Evaluation result.](../../../../../../translated_images/it/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Metriche di rischio e sicurezza:

    - Assicurati che gli output del modello siano sicuri e allineati ai Principi di AI Responsabile, evitando contenuti dannosi o offensivi.

    ![Evaluation result.](../../../../../../translated_images/it/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Puoi scorrere verso il basso per visualizzare il **risultato dettagliato delle metriche**.

    ![Evaluation result.](../../../../../../translated_images/it/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Valutando il tuo modello personalizzato Phi-3 / Phi-3.5 sia con metriche di prestazione che di sicurezza, puoi confermare che il modello non è solo efficace, ma aderisce anche alle pratiche di AI responsabile, rendendolo pronto per il deployment nel mondo reale.

## Congratulazioni!

### Hai completato questo tutorial

Hai valutato con successo il modello Phi-3 fine-tuned integrato con Prompt flow in Microsoft Foundry. Questo è un passo importante per garantire che i tuoi modelli AI non solo abbiano buone prestazioni, ma rispettino anche i principi di AI Responsabile di Microsoft, aiutandoti a costruire applicazioni AI affidabili e di fiducia.

![Architecture.](../../../../../../translated_images/it/architecture.10bec55250f5d6a4.webp)

## Pulizia delle risorse Azure

Pulisci le tue risorse Azure per evitare costi aggiuntivi sul tuo account. Vai al portale Azure ed elimina le seguenti risorse:

- La risorsa Azure Machine learning.
- L'endpoint modello Azure Machine learning.
- La risorsa progetto Microsoft Foundry.
- La risorsa Prompt flow di Microsoft Foundry.

### Passaggi successivi

#### Documentazione

- [Valuta i sistemi AI usando la dashboard di AI Responsabile](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metriche di valutazione e monitoraggio per AI generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentazione Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentazione Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenuti di formazione

- [Introduzione all'approccio di Microsoft all'AI Responsabile](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduzione a Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Riferimenti

- [Cos'è l'AI Responsabile?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Annuncio di nuovi strumenti in Azure AI per aiutarti a costruire applicazioni generative AI più sicure e affidabili](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Valutazione delle applicazioni di AI generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->