<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:20:49+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "it"
}
-->
## Come usare i componenti chat-completion dal registro di sistema Azure ML per il fine tuning di un modello

In questo esempio eseguiremo il fine tuning del modello Phi-3-mini-4k-instruct per completare una conversazione tra 2 persone utilizzando il dataset ultrachat_200k.

![MLFineTune](../../../../translated_images/it/MLFineTune.928d4c6b3767dd35.png)

L’esempio ti mostrerà come eseguire il fine tuning usando l’Azure ML SDK e Python e poi come distribuire il modello fine tuned su un endpoint online per inferenza in tempo reale.

### Dati di addestramento

Utilizzeremo il dataset ultrachat_200k. Questa è una versione fortemente filtrata del dataset UltraChat ed è stato usato per addestrare Zephyr-7B-β, un modello chat all’avanguardia da 7 miliardi di parametri.

### Modello

Useremo il modello Phi-3-mini-4k-instruct per mostrare come un utente può effettuare il fine tuning di un modello per il task di chat-completion. Se hai aperto questo notebook da una specifica scheda modello, ricorda di sostituire il nome del modello specifico.

### Attività

- Scegliere un modello da fine tunare.
- Selezionare ed esplorare i dati di addestramento.
- Configurare il job di fine tuning.
- Eseguire il job di fine tuning.
- Esaminare le metriche di addestramento e valutazione.
- Registrare il modello fine tuned.
- Distribuire il modello fine tuned per inferenza in tempo reale.
- Pulire le risorse.

## 1. Configurare i prerequisiti

- Installare le dipendenze
- Connettersi all’AzureML Workspace. Per maggiori informazioni consulta set up SDK authentication. Sostituisci <WORKSPACE_NAME>, <RESOURCE_GROUP> e <SUBSCRIPTION_ID> qui sotto.
- Connettersi al registro di sistema azureml
- Impostare un nome opzionale per l’esperimento
- Verificare o creare il compute.

> [!NOTE]
> I requisiti prevedono un singolo nodo GPU che può avere più schede GPU. Ad esempio, in un nodo Standard_NC24rs_v3 ci sono 4 GPU NVIDIA V100 mentre in Standard_NC12s_v3 ce ne sono 2. Consulta la documentazione per queste informazioni. Il numero di schede GPU per nodo è impostato nel parametro gpus_per_node qui sotto. Impostare correttamente questo valore garantirà l’utilizzo di tutte le GPU nel nodo. Le SKU di GPU compute consigliate si trovano qui e qui.

### Librerie Python

Installa le dipendenze eseguendo la cella sottostante. Questo passaggio non è opzionale se si lavora in un ambiente nuovo.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interazione con Azure ML

1. Questo script Python serve per interagire con il servizio Azure Machine Learning (Azure ML). Ecco cosa fa:

    - Importa i moduli necessari dai pacchetti azure.ai.ml, azure.identity e azure.ai.ml.entities. Importa anche il modulo time.

    - Tenta di autenticarsi usando DefaultAzureCredential(), che offre un’esperienza di autenticazione semplificata per iniziare rapidamente a sviluppare applicazioni in esecuzione nel cloud Azure. Se fallisce, passa a InteractiveBrowserCredential(), che fornisce un prompt di login interattivo.

    - Prova quindi a creare un’istanza MLClient usando il metodo from_config, che legge la configurazione dal file di configurazione predefinito (config.json). Se fallisce, crea un’istanza MLClient fornendo manualmente subscription_id, resource_group_name e workspace_name.

    - Crea un’altra istanza MLClient, questa volta per il registro Azure ML chiamato "azureml". Questo registro è dove sono memorizzati modelli, pipeline di fine tuning e ambienti.

    - Imposta experiment_name a "chat_completion_Phi-3-mini-4k-instruct".

    - Genera un timestamp univoco convertendo il tempo corrente (in secondi dall’epoch, come numero float) in un intero e poi in stringa. Questo timestamp può essere usato per creare nomi e versioni unici.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. Scegliere un modello foundation da fine tunare

1. Phi-3-mini-4k-instruct è un modello leggero da 3.8 miliardi di parametri, all’avanguardia, costruito su dataset usati per Phi-2. Il modello appartiene alla famiglia Phi-3, e la versione Mini è disponibile in due varianti 4K e 128K, che indicano la lunghezza del contesto (in token) che può supportare. Dobbiamo effettuare il fine tuning del modello per il nostro scopo specifico prima di usarlo. Puoi esplorare questi modelli nel Catalogo Modelli di AzureML Studio, filtrando per il task chat-completion. In questo esempio usiamo il modello Phi-3-mini-4k-instruct. Se hai aperto questo notebook per un modello diverso, sostituisci nome e versione del modello di conseguenza.

    > [!NOTE]
    > la proprietà model id del modello. Questa verrà passata come input al job di fine tuning. È disponibile anche come campo Asset ID nella pagina dei dettagli del modello nel Catalogo Modelli di AzureML Studio.

2. Questo script Python interagisce con il servizio Azure Machine Learning (Azure ML). Ecco cosa fa:

    - Imposta model_name a "Phi-3-mini-4k-instruct".

    - Usa il metodo get della proprietà models dell’oggetto registry_ml_client per recuperare l’ultima versione del modello con il nome specificato dal registro Azure ML. Il metodo get viene chiamato con due argomenti: il nome del modello e un’etichetta che specifica di recuperare l’ultima versione.

    - Stampa un messaggio sulla console indicando nome, versione e id del modello che sarà usato per il fine tuning. Il metodo format della stringa viene usato per inserire nome, versione e id del modello nel messaggio. Nome, versione e id sono proprietà dell’oggetto foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Creare un compute da usare con il job

Il job di fine tuning funziona SOLO con compute GPU. La dimensione del compute dipende dalla grandezza del modello e nella maggior parte dei casi è complicato identificare il compute giusto per il job. In questa cella guidiamo l’utente nella scelta del compute corretto.

> [!NOTE]
> I compute elencati qui sotto funzionano con la configurazione più ottimizzata. Qualsiasi modifica alla configurazione potrebbe causare errori Cuda Out Of Memory. In questi casi, prova ad aggiornare il compute a una dimensione maggiore.

> [!NOTE]
> Quando selezioni compute_cluster_size qui sotto, assicurati che il compute sia disponibile nel tuo resource group. Se un compute specifico non è disponibile, puoi fare richiesta per ottenere accesso alle risorse compute.

### Verifica del supporto al fine tuning del modello

1. Questo script Python interagisce con un modello Azure Machine Learning (Azure ML). Ecco cosa fa:

    - Importa il modulo ast, che fornisce funzioni per elaborare gli alberi della sintassi astratta di Python.

    - Controlla se l’oggetto foundation_model (che rappresenta un modello in Azure ML) ha un tag chiamato finetune_compute_allow_list. I tag in Azure ML sono coppie chiave-valore che puoi creare e usare per filtrare e ordinare i modelli.

    - Se il tag finetune_compute_allow_list è presente, usa la funzione ast.literal_eval per analizzare in modo sicuro il valore del tag (una stringa) in una lista Python. Questa lista viene assegnata alla variabile computes_allow_list. Stampa quindi un messaggio che indica che un compute dovrebbe essere creato dalla lista.

    - Se il tag finetune_compute_allow_list non è presente, imposta computes_allow_list a None e stampa un messaggio che indica che il tag non fa parte dei tag del modello.

    - In sintesi, questo script verifica la presenza di un tag specifico nei metadati del modello, converte il valore del tag in una lista se esiste, e fornisce un feedback all’utente.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Verifica dell’istanza compute

1. Questo script Python interagisce con il servizio Azure Machine Learning (Azure ML) e svolge diversi controlli su un’istanza compute. Ecco cosa fa:

    - Tenta di recuperare l’istanza compute con il nome memorizzato in compute_cluster dallo workspace Azure ML. Se lo stato di provisioning dell’istanza è "failed", solleva un ValueError.

    - Controlla se computes_allow_list non è None. Se non lo è, converte tutte le dimensioni compute nella lista in minuscolo e verifica se la dimensione dell’istanza compute corrente è nella lista. Se non lo è, solleva un ValueError.

    - Se computes_allow_list è None, verifica se la dimensione dell’istanza compute è in una lista di dimensioni VM GPU non supportate. Se lo è, solleva un ValueError.

    - Recupera una lista di tutte le dimensioni compute disponibili nello workspace. Itera su questa lista e per ogni dimensione verifica se il nome corrisponde alla dimensione dell’istanza compute corrente. Se sì, recupera il numero di GPU per quella dimensione e imposta gpu_count_found a True.

    - Se gpu_count_found è True, stampa il numero di GPU nell’istanza compute. Se è False, solleva un ValueError.

    - In sintesi, questo script esegue diversi controlli su un’istanza compute in uno workspace Azure ML, inclusi stato di provisioning, dimensione rispetto a una lista consentita o negata, e numero di GPU presenti.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Scegliere il dataset per il fine tuning del modello

1. Usiamo il dataset ultrachat_200k. Il dataset ha quattro suddivisioni, adatte per il fine tuning supervisionato (sft).
Ranking di generazione (gen). Il numero di esempi per suddivisione è mostrato come segue:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Le celle successive mostrano la preparazione base dei dati per il fine tuning:

### Visualizzare alcune righe di dati

Vogliamo che questo esempio venga eseguito rapidamente, quindi salviamo i file train_sft e test_sft contenenti il 5% delle righe già filtrate. Questo significa che il modello fine tuned avrà una precisione inferiore, quindi non dovrebbe essere usato in contesti reali.
Il file download-dataset.py viene usato per scaricare il dataset ultrachat_200k e trasformarlo in un formato consumabile dal componente pipeline di fine tuning. Inoltre, dato che il dataset è grande, qui abbiamo solo una parte del dataset.

1. Eseguendo lo script sottostante si scarica solo il 5% dei dati. Questa percentuale può essere aumentata modificando il parametro dataset_split_pc al valore desiderato.

    > [!NOTE]
    > Alcuni modelli linguistici hanno codici lingua diversi e quindi i nomi delle colonne nel dataset dovrebbero riflettere questo.

1. Ecco un esempio di come dovrebbero apparire i dati
Il dataset chat-completion è memorizzato in formato parquet con ogni voce che usa il seguente schema:

    - Questo è un documento JSON (JavaScript Object Notation), un formato popolare per lo scambio di dati. Non è codice eseguibile, ma un modo per memorizzare e trasportare dati. Ecco una spiegazione della sua struttura:

    - "prompt": questa chiave contiene una stringa che rappresenta un compito o una domanda posta a un assistente AI.

    - "messages": questa chiave contiene un array di oggetti. Ogni oggetto rappresenta un messaggio in una conversazione tra un utente e un assistente AI. Ogni messaggio ha due chiavi:

    - "content": questa chiave contiene una stringa che rappresenta il contenuto del messaggio.
    - "role": questa chiave contiene una stringa che rappresenta il ruolo dell’entità che ha inviato il messaggio. Può essere "user" o "assistant".
    - "prompt_id": questa chiave contiene una stringa che rappresenta un identificatore univoco per il prompt.

1. In questo specifico documento JSON, è rappresentata una conversazione in cui un utente chiede a un assistente AI di creare un protagonista per una storia distopica. L’assistente risponde, e l’utente poi chiede maggiori dettagli. L’assistente accetta di fornire più dettagli. L’intera conversazione è associata a un id prompt specifico.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Scaricare i dati

1. Questo script Python serve a scaricare un dataset usando uno script di supporto chiamato download-dataset.py. Ecco cosa fa:

    - Importa il modulo os, che fornisce un modo portabile per usare funzionalità dipendenti dal sistema operativo.

    - Usa la funzione os.system per eseguire lo script download-dataset.py nella shell con argomenti specifici da linea di comando. Gli argomenti specificano il dataset da scaricare (HuggingFaceH4/ultrachat_200k), la directory di destinazione (ultrachat_200k_dataset) e la percentuale di suddivisione del dataset (5). La funzione os.system restituisce lo stato di uscita del comando eseguito; questo stato viene memorizzato nella variabile exit_status.

    - Controlla se exit_status è diverso da 0. Nei sistemi Unix-like, uno stato di uscita 0 indica successo, mentre qualsiasi altro numero indica un errore. Se exit_status non è 0, solleva un’eccezione con un messaggio che indica un errore nel download del dataset.

    - In sintesi, questo script esegue un comando per scaricare un dataset usando uno script di supporto e solleva un’eccezione se il comando fallisce.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Caricare i dati in un DataFrame

1. Questo script Python carica un file JSON Lines in un DataFrame pandas e mostra le prime 5 righe. Ecco cosa fa:

    - Importa la libreria pandas, una potente libreria per manipolazione e analisi dati.

    - Imposta la larghezza massima delle colonne per le opzioni di visualizzazione di pandas a 0. Questo significa che il testo completo di ogni colonna sarà mostrato senza troncamenti quando il DataFrame viene stampato.

    - Usa la funzione pd.read_json per caricare il file train_sft.jsonl dalla directory ultrachat_200k_dataset in un DataFrame. L’argomento lines=True indica che il file è in formato JSON Lines, dove ogni riga è un oggetto JSON separato.
- Usa il metodo head per mostrare le prime 5 righe del DataFrame. Se il DataFrame ha meno di 5 righe, verranno mostrate tutte.

- In sintesi, questo script carica un file JSON Lines in un DataFrame e mostra le prime 5 righe con il testo completo delle colonne.

```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. Invia il job di fine tuning utilizzando il modello e i dati come input

Crea il job che utilizza il componente pipeline chat-completion. Scopri di più su tutti i parametri supportati per il fine tuning.

### Definisci i parametri di finetune

1. I parametri di finetune possono essere suddivisi in 2 categorie - parametri di training, parametri di ottimizzazione

1. I parametri di training definiscono gli aspetti dell’addestramento come -

    - L’ottimizzatore, lo scheduler da utilizzare
    - La metrica da ottimizzare per il fine tuning
    - Numero di step di training, dimensione del batch e così via
    - I parametri di ottimizzazione aiutano a ottimizzare la memoria GPU e a utilizzare efficacemente le risorse di calcolo.

1. Di seguito alcuni parametri che appartengono a questa categoria. I parametri di ottimizzazione variano per ogni modello e sono inclusi nel modello stesso per gestire queste differenze.

    - Abilita deepspeed e LoRA
    - Abilita il training a precisione mista
    - Abilita il training multi-nodo


> [!NOTE]
> Il fine tuning supervisionato può causare perdita di allineamento o dimenticanza catastrofica. Si consiglia di verificare questo problema ed eseguire una fase di allineamento dopo il fine tuning.

### Parametri di Fine Tuning

1. Questo script Python imposta i parametri per il fine tuning di un modello di machine learning. Ecco una panoramica di cosa fa:

    - Imposta i parametri di training di default come il numero di epoche, le dimensioni dei batch per training e valutazione, il learning rate e il tipo di scheduler del learning rate.

    - Imposta i parametri di ottimizzazione di default come l’applicazione di Layer-wise Relevance Propagation (LoRa) e DeepSpeed, e lo stage di DeepSpeed.

    - Combina i parametri di training e ottimizzazione in un unico dizionario chiamato finetune_parameters.

    - Controlla se foundation_model ha parametri di default specifici per il modello. Se sì, stampa un messaggio di avviso e aggiorna il dizionario finetune_parameters con questi parametri specifici. La funzione ast.literal_eval viene usata per convertire i parametri specifici da stringa a dizionario Python.

    - Stampa il set finale di parametri di fine tuning che verranno usati per l’esecuzione.

    - In sintesi, questo script imposta e mostra i parametri per il fine tuning di un modello di machine learning, con la possibilità di sovrascrivere i parametri di default con quelli specifici del modello.

```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline di Training

1. Questo script Python definisce una funzione per generare un nome visualizzato per una pipeline di training di machine learning, e poi chiama questa funzione per generare e stampare il nome. Ecco cosa fa:

1. Viene definita la funzione get_pipeline_display_name. Questa funzione genera un nome visualizzato basato su vari parametri relativi alla pipeline di training.

1. All’interno della funzione, calcola la dimensione totale del batch moltiplicando la dimensione del batch per dispositivo, il numero di step di accumulo del gradiente, il numero di GPU per nodo e il numero di nodi usati per il fine tuning.

1. Recupera vari altri parametri come il tipo di scheduler del learning rate, se DeepSpeed è applicato, lo stage di DeepSpeed, se Layer-wise Relevance Propagation (LoRa) è applicato, il limite sul numero di checkpoint del modello da mantenere, e la lunghezza massima della sequenza.

1. Costruisce una stringa che include tutti questi parametri, separati da trattini. Se DeepSpeed o LoRa sono applicati, la stringa include "ds" seguito dallo stage di DeepSpeed, o "lora", rispettivamente. Altrimenti include "nods" o "nolora", rispettivamente.

1. La funzione restituisce questa stringa, che serve come nome visualizzato per la pipeline di training.

1. Dopo la definizione, la funzione viene chiamata per generare il nome visualizzato, che viene poi stampato.

1. In sintesi, questo script genera un nome visualizzato per una pipeline di training di machine learning basato su vari parametri, e poi stampa questo nome.

```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Configurazione della Pipeline

Questo script Python definisce e configura una pipeline di machine learning usando l’Azure Machine Learning SDK. Ecco cosa fa:

1. Importa i moduli necessari dall’Azure AI ML SDK.

1. Recupera un componente pipeline chiamato "chat_completion_pipeline" dal registro.

1. Definisce un job pipeline usando il decoratore `@pipeline` e la funzione `create_pipeline`. Il nome della pipeline è impostato su `pipeline_display_name`.

1. All’interno della funzione `create_pipeline`, inizializza il componente pipeline recuperato con vari parametri, inclusi il percorso del modello, i cluster di calcolo per le diverse fasi, le suddivisioni del dataset per training e test, il numero di GPU da usare per il fine tuning e altri parametri di fine tuning.

1. Mappa l’output del job di fine tuning all’output del job pipeline. Questo serve a facilitare la registrazione del modello fine tuned, necessaria per il deployment su endpoint online o batch.

1. Crea un’istanza della pipeline chiamando la funzione `create_pipeline`.

1. Imposta l’opzione `force_rerun` della pipeline su `True`, il che significa che non verranno usati risultati in cache di job precedenti.

1. Imposta l’opzione `continue_on_step_failure` della pipeline su `False`, quindi la pipeline si fermerà se un qualsiasi step fallisce.

1. In sintesi, questo script definisce e configura una pipeline di machine learning per un task di completamento chat usando l’Azure Machine Learning SDK.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Invia il Job

1. Questo script Python invia un job pipeline di machine learning a un workspace Azure Machine Learning e poi attende il completamento del job. Ecco cosa fa:

    - Chiama il metodo create_or_update dell’oggetto jobs nel workspace_ml_client per inviare il job pipeline. La pipeline da eseguire è specificata da pipeline_object, e l’esperimento sotto cui il job viene eseguito è specificato da experiment_name.

    - Poi chiama il metodo stream dell’oggetto jobs nel workspace_ml_client per attendere il completamento del job pipeline. Il job da attendere è specificato dall’attributo name dell’oggetto pipeline_job.

    - In sintesi, questo script invia un job pipeline di machine learning a un workspace Azure Machine Learning e poi attende il completamento del job.

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Registra il modello fine tuned nel workspace

Registreremo il modello dall’output del job di fine tuning. Questo traccerà la lineage tra il modello fine tuned e il job di fine tuning. Il job di fine tuning, a sua volta, traccia la lineage verso il foundation model, i dati e il codice di training.

### Registrazione del Modello ML

1. Questo script Python registra un modello di machine learning addestrato in una pipeline Azure Machine Learning. Ecco cosa fa:

    - Importa i moduli necessari dall’Azure AI ML SDK.

    - Controlla se l’output trained_model è disponibile dal job pipeline chiamando il metodo get dell’oggetto jobs nel workspace_ml_client e accedendo all’attributo outputs.

    - Costruisce un percorso al modello addestrato formattando una stringa con il nome del job pipeline e il nome dell’output ("trained_model").

    - Definisce un nome per il modello fine tuned aggiungendo "-ultrachat-200k" al nome originale del modello e sostituendo eventuali slash con trattini.

    - Prepara la registrazione del modello creando un oggetto Model con vari parametri, inclusi il percorso del modello, il tipo di modello (modello MLflow), il nome e la versione del modello, e una descrizione.

    - Registra il modello chiamando il metodo create_or_update dell’oggetto models nel workspace_ml_client con l’oggetto Model come argomento.

    - Stampa il modello registrato.

1. In sintesi, questo script registra un modello di machine learning addestrato in una pipeline Azure Machine Learning.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. Distribuisci il modello fine tuned su un endpoint online

Gli endpoint online forniscono un’API REST duratura che può essere usata per integrare applicazioni che necessitano di utilizzare il modello.

### Gestione Endpoint

1. Questo script Python crea un endpoint online gestito in Azure Machine Learning per un modello registrato. Ecco cosa fa:

    - Importa i moduli necessari dall’Azure AI ML SDK.

    - Definisce un nome univoco per l’endpoint online aggiungendo un timestamp alla stringa "ultrachat-completion-".

    - Prepara la creazione dell’endpoint online creando un oggetto ManagedOnlineEndpoint con vari parametri, inclusi il nome dell’endpoint, una descrizione e la modalità di autenticazione ("key").

    - Crea l’endpoint online chiamando il metodo begin_create_or_update del workspace_ml_client con l’oggetto ManagedOnlineEndpoint come argomento. Poi attende il completamento dell’operazione chiamando il metodo wait.

1. In sintesi, questo script crea un endpoint online gestito in Azure Machine Learning per un modello registrato.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Puoi trovare qui la lista degli SKU supportati per il deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Distribuzione del Modello ML

1. Questo script Python distribuisce un modello di machine learning registrato su un endpoint online gestito in Azure Machine Learning. Ecco cosa fa:

    - Importa il modulo ast, che fornisce funzioni per elaborare gli alberi della grammatica sintattica astratta di Python.

    - Imposta il tipo di istanza per il deployment su "Standard_NC6s_v3".

    - Controlla se il tag inference_compute_allow_list è presente nel foundation model. Se sì, converte il valore del tag da stringa a lista Python e lo assegna a inference_computes_allow_list. Altrimenti lo imposta a None.

    - Controlla se il tipo di istanza specificato è nella lista consentita. Se non lo è, stampa un messaggio chiedendo all’utente di selezionare un tipo di istanza dalla lista consentita.

    - Prepara la creazione del deployment creando un oggetto ManagedOnlineDeployment con vari parametri, inclusi il nome del deployment, il nome dell’endpoint, l’ID del modello, il tipo e il numero di istanze, le impostazioni della liveness probe e le impostazioni delle richieste.

    - Crea il deployment chiamando il metodo begin_create_or_update del workspace_ml_client con l’oggetto ManagedOnlineDeployment come argomento. Poi attende il completamento dell’operazione chiamando il metodo wait.

    - Imposta il traffico dell’endpoint per indirizzare il 100% del traffico al deployment "demo".

    - Aggiorna l’endpoint chiamando il metodo begin_create_or_update del workspace_ml_client con l’oggetto endpoint come argomento. Poi attende il completamento dell’operazione chiamando il metodo result.

1. In sintesi, questo script distribuisce un modello di machine learning registrato su un endpoint online gestito in Azure Machine Learning.

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Testa l’endpoint con dati di esempio

Preleveremo alcuni dati di esempio dal dataset di test e li invieremo all’endpoint online per inferenza. Mostreremo poi le etichette previste insieme a quelle reali.

### Lettura dei risultati

1. Questo script Python legge un file JSON Lines in un DataFrame pandas, prende un campione casuale e resetta l’indice. Ecco cosa fa:

    - Legge il file ./ultrachat_200k_dataset/test_gen.jsonl in un DataFrame pandas. La funzione read_json è usata con l’argomento lines=True perché il file è in formato JSON Lines, dove ogni riga è un oggetto JSON separato.

    - Prende un campione casuale di 1 riga dal DataFrame. La funzione sample è usata con l’argomento n=1 per specificare il numero di righe casuali da selezionare.

    - Resetta l’indice del DataFrame. La funzione reset_index è usata con l’argomento drop=True per eliminare l’indice originale e sostituirlo con un nuovo indice di valori interi di default.

    - Mostra le prime 2 righe del DataFrame usando la funzione head con argomento 2. Tuttavia, dato che il DataFrame contiene solo una riga dopo il campionamento, verrà mostrata solo quella riga.

1. In sintesi, questo script legge un file JSON Lines in un DataFrame pandas, prende un campione casuale di 1 riga, resetta l’indice e mostra la prima riga.

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### Crea oggetto JSON

1. Questo script Python crea un oggetto JSON con parametri specifici e lo salva in un file. Ecco cosa fa:

    - Importa il modulo json, che fornisce funzioni per lavorare con dati JSON.

    - Crea un dizionario parameters con chiavi e valori che rappresentano parametri per un modello di machine learning. Le chiavi sono "temperature", "top_p", "do_sample" e "max_new_tokens", con valori rispettivamente 0.6, 0.9, True e 200.

    - Crea un altro dizionario test_json con due chiavi: "input_data" e "params". Il valore di "input_data" è un altro dizionario con chiavi "input_string" e "parameters". Il valore di "input_string" è una lista contenente il primo messaggio dal DataFrame test_df. Il valore di "parameters" è il dizionario parameters creato in precedenza. Il valore di "params" è un dizionario vuoto.
- Apre un file chiamato sample_score.json

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### Invocazione dell'Endpoint

1. Questo script Python invoca un endpoint online in Azure Machine Learning per valutare un file JSON. Ecco una spiegazione di cosa fa:

    - Chiama il metodo invoke della proprietà online_endpoints dell'oggetto workspace_ml_client. Questo metodo viene usato per inviare una richiesta a un endpoint online e ottenere una risposta.

    - Specifica il nome dell'endpoint e della deployment con gli argomenti endpoint_name e deployment_name. In questo caso, il nome dell'endpoint è memorizzato nella variabile online_endpoint_name e il nome della deployment è "demo".

    - Specifica il percorso del file JSON da valutare con l'argomento request_file. In questo caso, il file è ./ultrachat_200k_dataset/sample_score.json.

    - Memorizza la risposta dall'endpoint nella variabile response.

    - Stampa la risposta grezza.

1. In sintesi, questo script invoca un endpoint online in Azure Machine Learning per valutare un file JSON e stampa la risposta.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Eliminare l'endpoint online

1. Non dimenticare di eliminare l'endpoint online, altrimenti continuerai a pagare per il calcolo utilizzato dall'endpoint. Questa riga di codice Python elimina un endpoint online in Azure Machine Learning. Ecco cosa fa:

    - Chiama il metodo begin_delete della proprietà online_endpoints dell'oggetto workspace_ml_client. Questo metodo avvia l'eliminazione di un endpoint online.

    - Specifica il nome dell'endpoint da eliminare con l'argomento name. In questo caso, il nome dell'endpoint è memorizzato nella variabile online_endpoint_name.

    - Chiama il metodo wait per attendere il completamento dell'operazione di eliminazione. Questa è un'operazione bloccante, il che significa che impedirà allo script di proseguire finché l'eliminazione non sarà terminata.

    - In sintesi, questa riga di codice avvia l'eliminazione di un endpoint online in Azure Machine Learning e attende il completamento dell'operazione.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.