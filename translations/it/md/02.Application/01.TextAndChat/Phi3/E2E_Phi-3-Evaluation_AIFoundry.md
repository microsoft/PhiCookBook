<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:35:12+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "it"
}
-->
# Valutare il modello Phi-3 / Phi-3.5 fine-tuned in Azure AI Foundry con focus sui Principi di Responsible AI di Microsoft

Questo esempio end-to-end (E2E) si basa sulla guida "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" della Microsoft Tech Community.

## Panoramica

### Come valutare la sicurezza e le prestazioni di un modello Phi-3 / Phi-3.5 fine-tuned in Azure AI Foundry?

Il fine-tuning di un modello può a volte portare a risposte indesiderate o non intenzionali. Per garantire che il modello rimanga sicuro ed efficace, è importante valutarne la potenzialità di generare contenuti dannosi e la capacità di produrre risposte accurate, pertinenti e coerenti. In questo tutorial imparerai come valutare la sicurezza e le prestazioni di un modello Phi-3 / Phi-3.5 fine-tuned integrato con Prompt flow in Azure AI Foundry.

Ecco il processo di valutazione di Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/it/architecture.10bec55250f5d6a4.webp)

*Fonte immagine: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Per informazioni più dettagliate e per esplorare ulteriori risorse su Phi-3 / Phi-3.5, visita il [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prerequisiti

- [Python](https://www.python.org/downloads)
- [Sottoscrizione Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modello Phi-3 / Phi-3.5 fine-tuned

### Indice

1. [**Scenario 1: Introduzione alla valutazione con Prompt flow di Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduzione alla valutazione della sicurezza](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduzione alla valutazione delle prestazioni](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Valutazione del modello Phi-3 / Phi-3.5 in Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Prima di iniziare](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuire Azure OpenAI per valutare il modello Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Valutare il modello Phi-3 / Phi-3.5 fine-tuned usando la valutazione con Prompt flow di Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Congratulazioni!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduzione alla valutazione con Prompt flow di Azure AI Foundry**

### Introduzione alla valutazione della sicurezza

Per garantire che il tuo modello AI sia etico e sicuro, è fondamentale valutarlo in base ai Principi di Responsible AI di Microsoft. In Azure AI Foundry, le valutazioni di sicurezza ti permettono di analizzare la vulnerabilità del modello ad attacchi di jailbreak e la sua potenzialità di generare contenuti dannosi, in linea diretta con questi principi.

![Safaty evaluation.](../../../../../../translated_images/it/safety-evaluation.083586ec88dfa950.webp)

*Fonte immagine: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principi di Responsible AI di Microsoft

Prima di iniziare con i passaggi tecnici, è essenziale comprendere i Principi di Responsible AI di Microsoft, un quadro etico pensato per guidare lo sviluppo, il deployment e l’operatività responsabile dei sistemi AI. Questi principi orientano la progettazione, lo sviluppo e l’implementazione responsabile dei sistemi AI, assicurando che le tecnologie AI siano costruite in modo equo, trasparente e inclusivo. Sono la base per valutare la sicurezza dei modelli AI.

I Principi di Responsible AI di Microsoft includono:

- **Equità e Inclusività**: I sistemi AI devono trattare tutti in modo equo ed evitare di influenzare in modo diverso gruppi di persone con situazioni simili. Ad esempio, quando i sistemi AI forniscono indicazioni su trattamenti medici, richieste di prestito o assunzioni, dovrebbero fare le stesse raccomandazioni a chi ha sintomi, condizioni finanziarie o qualifiche professionali simili.

- **Affidabilità e Sicurezza**: Per costruire fiducia, è fondamentale che i sistemi AI operino in modo affidabile, sicuro e coerente. Questi sistemi devono funzionare come progettati, rispondere in modo sicuro a condizioni impreviste e resistere a manipolazioni dannose. Il loro comportamento e la varietà di condizioni che possono gestire riflettono le situazioni previste dagli sviluppatori durante progettazione e test.

- **Trasparenza**: Quando i sistemi AI aiutano a prendere decisioni che hanno un impatto significativo sulla vita delle persone, è fondamentale che queste comprendano come sono state prese tali decisioni. Ad esempio, una banca potrebbe usare un sistema AI per decidere se una persona è affidabile per un prestito. Un’azienda potrebbe usare un sistema AI per selezionare i candidati più qualificati.

- **Privacy e Sicurezza**: Con la crescente diffusione dell’AI, proteggere la privacy e la sicurezza delle informazioni personali e aziendali diventa sempre più importante e complesso. Con l’AI, privacy e sicurezza dei dati richiedono particolare attenzione perché l’accesso ai dati è essenziale affinché i sistemi AI possano fare previsioni e decisioni accurate e informate sulle persone.

- **Responsabilità**: Chi progetta e distribuisce sistemi AI deve essere responsabile del loro funzionamento. Le organizzazioni dovrebbero adottare standard di settore per sviluppare norme di responsabilità. Queste norme possono garantire che i sistemi AI non siano l’autorità finale su decisioni che influenzano la vita delle persone e che gli esseri umani mantengano un controllo significativo su sistemi AI altrimenti altamente autonomi.

![Fill hub.](../../../../../../translated_images/it/responsibleai2.c07ef430113fad8c.webp)

*Fonte immagine: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Per approfondire i Principi di Responsible AI di Microsoft, visita la pagina [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metriche di sicurezza

In questo tutorial valuterai la sicurezza del modello Phi-3 fine-tuned usando le metriche di sicurezza di Azure AI Foundry. Queste metriche ti aiutano a valutare la potenzialità del modello di generare contenuti dannosi e la sua vulnerabilità ad attacchi di jailbreak. Le metriche di sicurezza includono:

- **Contenuti legati all’autolesionismo**: Valuta se il modello tende a produrre contenuti relativi all’autolesionismo.
- **Contenuti d’odio e ingiusti**: Valuta se il modello tende a produrre contenuti d’odio o ingiusti.
- **Contenuti violenti**: Valuta se il modello tende a produrre contenuti violenti.
- **Contenuti sessuali**: Valuta se il modello tende a produrre contenuti sessuali inappropriati.

Valutare questi aspetti assicura che il modello AI non generi contenuti dannosi o offensivi, allineandolo ai valori sociali e agli standard normativi.

![Evaluate based on safety.](../../../../../../translated_images/it/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introduzione alla valutazione delle prestazioni

Per assicurarti che il tuo modello AI funzioni come previsto, è importante valutarne le prestazioni rispetto a metriche specifiche. In Azure AI Foundry, le valutazioni delle prestazioni ti permettono di analizzare l’efficacia del modello nel generare risposte accurate, pertinenti e coerenti.

![Safaty evaluation.](../../../../../../translated_images/it/performance-evaluation.48b3e7e01a098740.webp)

*Fonte immagine: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metriche di prestazione

In questo tutorial valuterai le prestazioni del modello Phi-3 / Phi-3.5 fine-tuned usando le metriche di prestazione di Azure AI Foundry. Queste metriche ti aiutano a valutare l’efficacia del modello nel generare risposte accurate, pertinenti e coerenti. Le metriche di prestazione includono:

- **Groundedness**: Valuta quanto le risposte generate siano allineate con le informazioni della fonte di input.
- **Rilevanza**: Valuta la pertinenza delle risposte generate rispetto alle domande fornite.
- **Coerenza**: Valuta quanto il testo generato scorra in modo fluido, sia naturale e somigli a un linguaggio umano.
- **Fluidità**: Valuta la competenza linguistica del testo generato.
- **Somiglianza GPT**: Confronta la risposta generata con la verità di riferimento per similarità.
- **F1 Score**: Calcola il rapporto di parole condivise tra la risposta generata e i dati di origine.

Queste metriche ti aiutano a valutare l’efficacia del modello nel generare risposte accurate, pertinenti e coerenti.

![Evaluate based on performance.](../../../../../../translated_images/it/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenario 2: Valutazione del modello Phi-3 / Phi-3.5 in Azure AI Foundry**

### Prima di iniziare

Questo tutorial è un seguito dei precedenti post sul blog, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In questi post abbiamo illustrato il processo di fine-tuning di un modello Phi-3 / Phi-3.5 in Azure AI Foundry e la sua integrazione con Prompt flow.

In questo tutorial distribuirai un modello Azure OpenAI come valutatore in Azure AI Foundry e lo userai per valutare il tuo modello Phi-3 / Phi-3.5 fine-tuned.

Prima di iniziare questo tutorial, assicurati di avere i seguenti prerequisiti, come descritto nei tutorial precedenti:

1. Un dataset preparato per valutare il modello Phi-3 / Phi-3.5 fine-tuned.
1. Un modello Phi-3 / Phi-3.5 fine-tuned e distribuito su Azure Machine Learning.
1. Un Prompt flow integrato con il tuo modello Phi-3 / Phi-3.5 fine-tuned in Azure AI Foundry.

> [!NOTE]
> Userai il file *test_data.jsonl*, situato nella cartella data del dataset **ULTRACHAT_200k** scaricato nei post precedenti, come dataset per valutare il modello Phi-3 / Phi-3.5 fine-tuned.

#### Integrare il modello personalizzato Phi-3 / Phi-3.5 con Prompt flow in Azure AI Foundry (approccio Code first)
> [!NOTE]
> Se hai seguito l'approccio low-code descritto in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", puoi saltare questo esercizio e passare al successivo.
> Tuttavia, se hai seguito l'approccio code-first descritto in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" per affinare e distribuire il tuo modello Phi-3 / Phi-3.5, il processo di collegamento del modello a Prompt flow è leggermente diverso. Imparerai questo processo in questo esercizio.
Per procedere, devi integrare il tuo modello Phi-3 / Phi-3.5 fine-tuned in Prompt flow in Azure AI Foundry.

#### Crea Azure AI Foundry Hub

Devi creare un Hub prima di creare il Progetto. Un Hub funziona come un Resource Group, permettendoti di organizzare e gestire più Progetti all'interno di Azure AI Foundry.

1. Accedi a [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Seleziona **All hubs** dalla scheda laterale sinistra.

1. Seleziona **+ New hub** dal menu di navigazione.

    ![Create hub.](../../../../../../translated_images/it/create-hub.5be78fb1e21ffbf1.webp)

1. Esegui le seguenti operazioni:

    - Inserisci il **Nome Hub**. Deve essere un valore univoco.
    - Seleziona la tua **Subscription** di Azure.
    - Seleziona il **Resource group** da utilizzare (creane uno nuovo se necessario).
    - Seleziona la **Location** che desideri utilizzare.
    - Seleziona **Connect Azure AI Services** da utilizzare (creane uno nuovo se necessario).
    - Seleziona **Connect Azure AI Search** su **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/it/fill-hub.baaa108495c71e34.webp)

1. Seleziona **Next**.

#### Crea progetto Azure AI Foundry

1. Nell’Hub che hai creato, seleziona **All projects** dalla scheda laterale sinistra.

1. Seleziona **+ New project** dal menu di navigazione.

    ![Select new project.](../../../../../../translated_images/it/select-new-project.cd31c0404088d7a3.webp)

1. Inserisci il **Nome Progetto**. Deve essere un valore univoco.

    ![Create project.](../../../../../../translated_images/it/create-project.ca3b71298b90e420.webp)

1. Seleziona **Create a project**.

#### Aggiungi una connessione personalizzata per il modello Phi-3 / Phi-3.5 fine-tuned

Per integrare il tuo modello Phi-3 / Phi-3.5 personalizzato con Prompt flow, devi salvare l’endpoint e la chiave del modello in una connessione personalizzata. Questa configurazione garantisce l’accesso al tuo modello Phi-3 / Phi-3.5 personalizzato in Prompt flow.

#### Imposta api key e endpoint uri del modello Phi-3 / Phi-3.5 fine-tuned

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviga allo workspace di Azure Machine Learning che hai creato.

1. Seleziona **Endpoints** dalla scheda laterale sinistra.

    ![Select endpoints.](../../../../../../translated_images/it/select-endpoints.ee7387ecd68bd18d.webp)

1. Seleziona l’endpoint che hai creato.

    ![Select endpoints.](../../../../../../translated_images/it/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Seleziona **Consume** dal menu di navigazione.

1. Copia il tuo **REST endpoint** e la **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/it/copy-endpoint-key.0650c3786bd646ab.webp)

#### Aggiungi la Connessione Personalizzata

1. Visita [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviga al progetto Azure AI Foundry che hai creato.

1. Nel Progetto che hai creato, seleziona **Settings** dalla scheda laterale sinistra.

1. Seleziona **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/it/select-new-connection.fa0f35743758a74b.webp)

1. Seleziona **Custom keys** dal menu di navigazione.

    ![Select custom keys.](../../../../../../translated_images/it/select-custom-keys.5a3c6b25580a9b67.webp)

1. Esegui le seguenti operazioni:

    - Seleziona **+ Add key value pairs**.
    - Per il nome della chiave, inserisci **endpoint** e incolla l’endpoint copiato da Azure ML Studio nel campo valore.
    - Seleziona nuovamente **+ Add key value pairs**.
    - Per il nome della chiave, inserisci **key** e incolla la chiave copiata da Azure ML Studio nel campo valore.
    - Dopo aver aggiunto le chiavi, seleziona **is secret** per evitare che la chiave venga esposta.

    ![Add connection.](../../../../../../translated_images/it/add-connection.ac7f5faf8b10b0df.webp)

1. Seleziona **Add connection**.

#### Crea Prompt flow

Hai aggiunto una connessione personalizzata in Azure AI Foundry. Ora, creiamo un Prompt flow seguendo i passaggi seguenti. Successivamente, collegherai questo Prompt flow alla connessione personalizzata per usare il modello fine-tuned all’interno del Prompt flow.

1. Naviga al progetto Azure AI Foundry che hai creato.

1. Seleziona **Prompt flow** dalla scheda laterale sinistra.

1. Seleziona **+ Create** dal menu di navigazione.

    ![Select Promptflow.](../../../../../../translated_images/it/select-promptflow.18ff2e61ab9173eb.webp)

1. Seleziona **Chat flow** dal menu di navigazione.

    ![Select chat flow.](../../../../../../translated_images/it/select-flow-type.28375125ec9996d3.webp)

1. Inserisci il **Nome cartella** da utilizzare.

    ![Select chat flow.](../../../../../../translated_images/it/enter-name.02ddf8fb840ad430.webp)

1. Seleziona **Create**.

#### Configura Prompt flow per chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato

Devi integrare il modello Phi-3 / Phi-3.5 fine-tuned in un Prompt flow. Tuttavia, il Prompt flow esistente fornito non è progettato per questo scopo. Pertanto, devi riprogettare il Prompt flow per abilitare l’integrazione del modello personalizzato.

1. Nel Prompt flow, esegui le seguenti operazioni per ricostruire il flusso esistente:

    - Seleziona **Raw file mode**.
    - Elimina tutto il codice esistente nel file *flow.dag.yml*.
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

    - Seleziona **Save**.

    ![Select raw file mode.](../../../../../../translated_images/it/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Aggiungi il seguente codice in *integrate_with_promptflow.py* per usare il modello Phi-3 / Phi-3.5 personalizzato in Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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
> Per informazioni più dettagliate sull’uso di Prompt flow in Azure AI Foundry, puoi consultare [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Seleziona **Chat input**, **Chat output** per abilitare la chat con il tuo modello.

    ![Select Input Output.](../../../../../../translated_images/it/select-input-output.c187fc58f25fbfc3.webp)

1. Ora sei pronto per chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato. Nel prossimo esercizio imparerai come avviare Prompt flow e usarlo per chattare con il tuo modello Phi-3 / Phi-3.5 fine-tuned.

> [!NOTE]
>
> Il flusso ricostruito dovrebbe apparire come nell’immagine sottostante:
>
> ![Flow example](../../../../../../translated_images/it/graph-example.82fd1bcdd3fc545b.webp)
>

#### Avvia Prompt flow

1. Seleziona **Start compute sessions** per avviare Prompt flow.

    ![Start compute session.](../../../../../../translated_images/it/start-compute-session.9acd8cbbd2c43df1.webp)

1. Seleziona **Validate and parse input** per aggiornare i parametri.

    ![Validate input.](../../../../../../translated_images/it/validate-input.c1adb9543c6495be.webp)

1. Seleziona il **Valore** della **connection** alla connessione personalizzata che hai creato. Per esempio, *connection*.

    ![Connection.](../../../../../../translated_images/it/select-connection.1f2b59222bcaafef.webp)

#### Chatta con il tuo modello Phi-3 / Phi-3.5 personalizzato

1. Seleziona **Chat**.

    ![Select chat.](../../../../../../translated_images/it/select-chat.0406bd9687d0c49d.webp)

1. Ecco un esempio dei risultati: ora puoi chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato. Si consiglia di porre domande basate sui dati usati per il fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/it/chat-with-promptflow.1cf8cea112359ada.webp)

### Distribuisci Azure OpenAI per valutare il modello Phi-3 / Phi-3.5

Per valutare il modello Phi-3 / Phi-3.5 in Azure AI Foundry, devi distribuire un modello Azure OpenAI. Questo modello sarà usato per valutare le prestazioni del modello Phi-3 / Phi-3.5.

#### Distribuisci Azure OpenAI

1. Accedi a [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviga al progetto Azure AI Foundry che hai creato.

    ![Select Project.](../../../../../../translated_images/it/select-project-created.5221e0e403e2c9d6.webp)

1. Nel Progetto che hai creato, seleziona **Deployments** dalla scheda laterale sinistra.

1. Seleziona **+ Deploy model** dal menu di navigazione.

1. Seleziona **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/it/deploy-openai-model.95d812346b25834b.webp)

1. Seleziona il modello Azure OpenAI che desideri utilizzare. Per esempio, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/it/select-openai-model.959496d7e311546d.webp)

1. Seleziona **Confirm**.

### Valuta il modello Phi-3 / Phi-3.5 fine-tuned usando la valutazione Prompt flow di Azure AI Foundry

### Avvia una nuova valutazione

1. Visita [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviga al progetto Azure AI Foundry che hai creato.

    ![Select Project.](../../../../../../translated_images/it/select-project-created.5221e0e403e2c9d6.webp)

1. Nel Progetto che hai creato, seleziona **Evaluation** dalla scheda laterale sinistra.

1. Seleziona **+ New evaluation** dal menu di navigazione.

    ![Select evaluation.](../../../../../../translated_images/it/select-evaluation.2846ad7aaaca7f4f.webp)

1. Seleziona la valutazione **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/it/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Esegui le seguenti operazioni:

    - Inserisci il nome della valutazione. Deve essere un valore univoco.
    - Seleziona **Question and answer without context** come tipo di attività. Perché il dataset **ULTRACHAT_200k** usato in questo tutorial non contiene contesto.
    - Seleziona il prompt flow che desideri valutare.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting1.4aa08259ff7a536e.webp)

1. Seleziona **Next**.

1. Esegui le seguenti operazioni:

    - Seleziona **Add your dataset** per caricare il dataset. Per esempio, puoi caricare il file del dataset di test, come *test_data.json1*, incluso nel download del dataset **ULTRACHAT_200k**.
    - Seleziona la **Dataset column** appropriata che corrisponde al tuo dataset. Per esempio, se usi il dataset **ULTRACHAT_200k**, seleziona **${data.prompt}** come colonna del dataset.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting2.07036831ba58d64e.webp)

1. Seleziona **Next**.

1. Esegui le seguenti operazioni per configurare le metriche di performance e qualità:

    - Seleziona le metriche di performance e qualità che desideri utilizzare.
    - Seleziona il modello Azure OpenAI che hai creato per la valutazione. Per esempio, seleziona **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Esegui le seguenti operazioni per configurare le metriche di rischio e sicurezza:

    - Seleziona le metriche di rischio e sicurezza che desideri utilizzare.
    - Seleziona la soglia per calcolare il tasso di difetti che desideri utilizzare. Per esempio, seleziona **Medium**.
    - Per **question**, seleziona **Data source** su **{$data.prompt}**.
    - Per **answer**, seleziona **Data source** su **{$run.outputs.answer}**.
    - Per **ground_truth**, seleziona **Data source** su **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/it/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Seleziona **Next**.

1. Seleziona **Submit** per avviare la valutazione.

1. La valutazione richiederà un po’ di tempo per completarsi. Puoi monitorare i progressi nella scheda **Evaluation**.

### Esamina i risultati della valutazione
> [!NOTE]
> I risultati presentati di seguito sono intesi a illustrare il processo di valutazione. In questo tutorial, abbiamo utilizzato un modello ottimizzato su un dataset relativamente piccolo, il che potrebbe portare a risultati non ottimali. I risultati effettivi possono variare significativamente a seconda delle dimensioni, della qualità e della diversità del dataset utilizzato, oltre che della configurazione specifica del modello.
Una volta completata la valutazione, puoi esaminare i risultati sia per le metriche di performance che di sicurezza.

1. Metriche di performance e qualità:

    - valuta l’efficacia del modello nel generare risposte coerenti, fluide e pertinenti.

    ![Evaluation result.](../../../../../../translated_images/it/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Metriche di rischio e sicurezza:

    - Assicurati che le uscite del modello siano sicure e in linea con i Principi di Responsible AI, evitando contenuti dannosi o offensivi.

    ![Evaluation result.](../../../../../../translated_images/it/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Puoi scorrere verso il basso per visualizzare il **Risultato dettagliato delle metriche**.

    ![Evaluation result.](../../../../../../translated_images/it/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Valutando il tuo modello personalizzato Phi-3 / Phi-3.5 sia sulle metriche di performance che di sicurezza, puoi confermare che il modello non è solo efficace, ma rispetta anche le pratiche di AI responsabile, rendendolo pronto per l’implementazione nel mondo reale.

## Congratulazioni!

### Hai completato questo tutorial

Hai valutato con successo il modello Phi-3 fine-tuned integrato con Prompt flow in Azure AI Foundry. Questo è un passaggio importante per garantire che i tuoi modelli AI non solo abbiano buone prestazioni, ma aderiscano anche ai principi di Responsible AI di Microsoft, aiutandoti a costruire applicazioni AI affidabili e di fiducia.

![Architecture.](../../../../../../translated_images/it/architecture.10bec55250f5d6a4.webp)

## Pulizia delle risorse Azure

Pulisci le tue risorse Azure per evitare addebiti aggiuntivi sul tuo account. Vai al portale Azure ed elimina le seguenti risorse:

- La risorsa Azure Machine learning.
- L’endpoint del modello Azure Machine learning.
- La risorsa Azure AI Foundry Project.
- La risorsa Azure AI Foundry Prompt flow.

### Passi successivi

#### Documentazione

- [Valuta i sistemi AI utilizzando il Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metriche di valutazione e monitoraggio per l’AI generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentazione Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentazione Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenuti di formazione

- [Introduzione all’approccio Responsible AI di Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduzione ad Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Riferimenti

- [Cos’è Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Annuncio di nuovi strumenti in Azure AI per aiutarti a costruire applicazioni AI generative più sicure e affidabili](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Valutazione delle applicazioni AI generative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.