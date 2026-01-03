<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:32:25+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "nl"
}
-->
## Hoe chat-completion componenten uit de Azure ML system registry te gebruiken om een model fijn af te stemmen

In dit voorbeeld voeren we een fine tuning uit van het Phi-3-mini-4k-instruct model om een gesprek tussen 2 personen te voltooien met behulp van de ultrachat_200k dataset.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35.nl.png)

Het voorbeeld laat zien hoe je fine tuning uitvoert met de Azure ML SDK en Python, en vervolgens het fijn afgestemde model inzet op een online endpoint voor realtime inferentie.

### Trainingsdata

We gebruiken de ultrachat_200k dataset. Dit is een sterk gefilterde versie van de UltraChat dataset en werd gebruikt om Zephyr-7B-β te trainen, een geavanceerd 7b chatmodel.

### Model

We gebruiken het Phi-3-mini-4k-instruct model om te laten zien hoe een gebruiker een model kan fijn afstemmen voor een chat-completion taak. Als je deze notebook hebt geopend vanuit een specifieke modelkaart, vergeet dan niet de modelnaam aan te passen.

### Taken

- Kies een model om fijn af te stemmen.
- Kies en verken de trainingsdata.
- Configureer de fine tuning taak.
- Voer de fine tuning taak uit.
- Bekijk trainings- en evaluatiestatistieken.
- Registreer het fijn afgestemde model.
- Zet het fijn afgestemde model in voor realtime inferentie.
- Ruim de gebruikte resources op.

## 1. Voorbereidingen treffen

- Installeer de benodigde dependencies
- Verbind met de AzureML Workspace. Meer informatie vind je bij het instellen van SDK authenticatie. Vervang hieronder <WORKSPACE_NAME>, <RESOURCE_GROUP> en <SUBSCRIPTION_ID>.
- Verbind met de azureml system registry
- Stel een optionele experimentnaam in
- Controleer of maak een compute aan.

> [!NOTE]
> Vereisten: een enkele GPU node kan meerdere GPU-kaarten bevatten. Bijvoorbeeld, in een node van Standard_NC24rs_v3 zitten 4 NVIDIA V100 GPU’s, terwijl in Standard_NC12s_v3 er 2 NVIDIA V100 GPU’s zijn. Raadpleeg de documentatie voor deze informatie. Het aantal GPU-kaarten per node wordt ingesteld in de parameter gpus_per_node hieronder. Door deze waarde correct in te stellen, wordt het gebruik van alle GPU’s in de node gegarandeerd. De aanbevolen GPU compute SKUs vind je hier en hier.

### Python Libraries

Installeer de dependencies door onderstaande cel uit te voeren. Dit is geen optionele stap als je in een nieuwe omgeving werkt.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interactie met Azure ML

1. Dit Python script wordt gebruikt om te communiceren met de Azure Machine Learning (Azure ML) service. Hier volgt een overzicht van wat het doet:

    - Het importeert benodigde modules uit de azure.ai.ml, azure.identity en azure.ai.ml.entities pakketten. Ook wordt de time module geïmporteerd.

    - Het probeert te authenticeren met DefaultAzureCredential(), wat een vereenvoudigde authenticatie biedt om snel applicaties te ontwikkelen die in de Azure cloud draaien. Als dit mislukt, valt het terug op InteractiveBrowserCredential(), wat een interactieve login prompt geeft.

    - Vervolgens probeert het een MLClient instantie te maken met de from_config methode, die de configuratie leest uit het standaard config bestand (config.json). Als dit mislukt, maakt het handmatig een MLClient aan met subscription_id, resource_group_name en workspace_name.

    - Het maakt een andere MLClient instantie aan, ditmaal voor de Azure ML registry met de naam "azureml". Deze registry is de plek waar modellen, fine-tuning pipelines en omgevingen worden opgeslagen.

    - Het stelt de experiment_name in op "chat_completion_Phi-3-mini-4k-instruct".

    - Het genereert een unieke timestamp door de huidige tijd (in seconden sinds de epoch, als float) om te zetten naar een integer en vervolgens naar een string. Deze timestamp kan gebruikt worden voor unieke namen en versies.

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

## 2. Kies een foundation model om fijn af te stemmen

1. Phi-3-mini-4k-instruct is een lichtgewicht, state-of-the-art open model met 3,8 miljard parameters, gebaseerd op datasets die ook voor Phi-2 werden gebruikt. Het model behoort tot de Phi-3 model familie, en de Mini versie komt in twee varianten: 4K en 128K, wat de contextlengte (in tokens) is die het kan ondersteunen. We moeten het model fijn afstemmen voor ons specifieke doel om het te kunnen gebruiken. Je kunt deze modellen bekijken in de Model Catalog in AzureML Studio, filterend op de chat-completion taak. In dit voorbeeld gebruiken we het Phi-3-mini-4k-instruct model. Als je deze notebook voor een ander model hebt geopend, vervang dan de modelnaam en versie.

    > [!NOTE]
    > de model id eigenschap van het model. Deze wordt als input doorgegeven aan de fine tuning taak. Dit is ook beschikbaar als het Asset ID veld op de model detailpagina in AzureML Studio Model Catalog.

2. Dit Python script communiceert met de Azure Machine Learning (Azure ML) service. Hier volgt een overzicht van wat het doet:

    - Het stelt model_name in op "Phi-3-mini-4k-instruct".

    - Het gebruikt de get methode van de models property van het registry_ml_client object om de nieuwste versie van het model met de opgegeven naam op te halen uit de Azure ML registry. De get methode wordt aangeroepen met twee argumenten: de naam van het model en een label die aangeeft dat de nieuwste versie moet worden opgehaald.

    - Het print een bericht naar de console met de naam, versie en id van het model dat gebruikt zal worden voor fine tuning. De format methode van de string wordt gebruikt om naam, versie en id in het bericht te plaatsen. Deze eigenschappen worden uit het foundation_model object gehaald.

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

## 3. Maak een compute aan die gebruikt wordt voor de taak

De fine tune taak werkt ALLEEN met GPU compute. De grootte van de compute hangt af van hoe groot het model is en in de meeste gevallen is het lastig om de juiste compute te kiezen. In deze cel begeleiden we de gebruiker bij het selecteren van de juiste compute.

> [!NOTE]
> De hieronder genoemde computes werken met de meest geoptimaliseerde configuratie. Wijzigingen in de configuratie kunnen leiden tot Cuda Out Of Memory fouten. In dat geval kun je proberen de compute te upgraden naar een grotere compute grootte.

> [!NOTE]
> Bij het kiezen van compute_cluster_size hieronder, zorg ervoor dat de compute beschikbaar is in je resource group. Als een bepaalde compute niet beschikbaar is, kun je een verzoek indienen om toegang te krijgen tot de compute resources.

### Controleren of het model fine tuning ondersteunt

1. Dit Python script communiceert met een Azure Machine Learning (Azure ML) model. Hier volgt een overzicht van wat het doet:

    - Het importeert de ast module, die functies biedt om Python abstracte syntaxisbomen te verwerken.

    - Het controleert of het foundation_model object (dat een model in Azure ML vertegenwoordigt) een tag heeft met de naam finetune_compute_allow_list. Tags in Azure ML zijn key-value paren die je kunt gebruiken om modellen te filteren en sorteren.

    - Als de finetune_compute_allow_list tag aanwezig is, gebruikt het ast.literal_eval om de waarde van de tag (een string) veilig te parsen naar een Python lijst. Deze lijst wordt toegewezen aan de variabele computes_allow_list. Daarna print het een bericht dat een compute uit deze lijst moet worden gekozen.

    - Als de finetune_compute_allow_list tag niet aanwezig is, wordt computes_allow_list op None gezet en wordt een bericht geprint dat de tag niet aanwezig is in de model tags.

    - Samengevat controleert dit script op een specifieke tag in de metadata van het model, zet de waarde om naar een lijst als die bestaat, en geeft feedback aan de gebruiker.

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

### Controleren van de Compute Instance

1. Dit Python script communiceert met de Azure Machine Learning (Azure ML) service en voert verschillende controles uit op een compute instance. Hier volgt een overzicht van wat het doet:

    - Het probeert de compute instance op te halen met de naam die is opgeslagen in compute_cluster uit de Azure ML workspace. Als de provisioning status van de compute instance "failed" is, wordt een ValueError opgegooid.

    - Het controleert of computes_allow_list niet None is. Als dat zo is, zet het alle compute groottes in de lijst om naar kleine letters en controleert of de grootte van de huidige compute instance in die lijst staat. Zo niet, dan wordt een ValueError opgegooid.

    - Als computes_allow_list None is, controleert het of de grootte van de compute instance in een lijst van niet-ondersteunde GPU VM groottes staat. Als dat zo is, wordt een ValueError opgegooid.

    - Het haalt een lijst op van alle beschikbare compute groottes in de workspace. Daarna loopt het deze lijst door en controleert voor elke compute grootte of de naam overeenkomt met de grootte van de huidige compute instance. Als dat zo is, haalt het het aantal GPU’s voor die compute grootte op en zet gpu_count_found op True.

    - Als gpu_count_found True is, print het het aantal GPU’s in de compute instance. Als gpu_count_found False is, wordt een ValueError opgegooid.

    - Samengevat voert dit script verschillende controles uit op een compute instance in een Azure ML workspace, waaronder de provisioning status, de grootte ten opzichte van een toegestane lijst of een verboden lijst, en het aantal GPU’s.

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

## 4. Kies de dataset voor het fijn afstemmen van het model

1. We gebruiken de ultrachat_200k dataset. De dataset heeft vier splits, geschikt voor Supervised fine-tuning (sft).
Generation ranking (gen). Het aantal voorbeelden per split is als volgt:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. De volgende cellen laten basis data voorbereiding zien voor fine tuning:

### Visualiseer enkele datarijen

We willen dat dit voorbeeld snel draait, dus slaan we train_sft en test_sft bestanden op met 5% van de reeds ingekorte rijen. Dit betekent dat het fijn afgestemde model minder nauwkeurig zal zijn, en daarom niet in de praktijk gebruikt moet worden.
Het script download-dataset.py wordt gebruikt om de ultrachat_200k dataset te downloaden en om te zetten naar een formaat dat door de fine tune pipeline component kan worden gebruikt. Omdat de dataset groot is, hebben we hier slechts een deel van de dataset.

1. Het onderstaande script downloadt slechts 5% van de data. Dit kan verhoogd worden door de parameter dataset_split_pc aan te passen naar het gewenste percentage.

    > [!NOTE]
    > Sommige taalmodellen hebben verschillende taalcodes, dus de kolomnamen in de dataset moeten hierop afgestemd zijn.

1. Hier is een voorbeeld van hoe de data eruit zou moeten zien
De chat-completion dataset is opgeslagen in parquet formaat waarbij elke invoer het volgende schema gebruikt:

    - Dit is een JSON (JavaScript Object Notation) document, een populair data-uitwisselingsformaat. Het is geen uitvoerbare code, maar een manier om data op te slaan en te transporteren. Hier volgt een overzicht van de structuur:

    - "prompt": Deze sleutel bevat een string die een taak of vraag aan een AI-assistent voorstelt.

    - "messages": Deze sleutel bevat een array van objecten. Elk object vertegenwoordigt een bericht in een gesprek tussen een gebruiker en een AI-assistent. Elk berichtobject heeft twee sleutels:

    - "content": Deze sleutel bevat een string met de inhoud van het bericht.
    - "role": Deze sleutel bevat een string die de rol van de entiteit die het bericht stuurde aangeeft. Dit kan "user" of "assistant" zijn.
    - "prompt_id": Deze sleutel bevat een string die een unieke identificatie voor de prompt voorstelt.

1. In dit specifieke JSON document wordt een gesprek weergegeven waarin een gebruiker een AI-assistent vraagt een protagonist te creëren voor een dystopisch verhaal. De assistent reageert, en de gebruiker vraagt vervolgens om meer details. De assistent stemt toe om meer details te geven. Het hele gesprek is gekoppeld aan een specifieke prompt id.

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

### Data downloaden

1. Dit Python script wordt gebruikt om een dataset te downloaden met behulp van een hulpscript genaamd download-dataset.py. Hier volgt een overzicht van wat het doet:

    - Het importeert de os module, die een platformonafhankelijke manier biedt om functies van het besturingssysteem te gebruiken.

    - Het gebruikt de os.system functie om het download-dataset.py script uit te voeren in de shell met specifieke commandoregelargumenten. De argumenten geven aan welke dataset gedownload moet worden (HuggingFaceH4/ultrachat_200k), naar welke map het gedownload moet worden (ultrachat_200k_dataset), en welk percentage van de dataset gesplitst moet worden (5). De os.system functie retourneert de exit status van het uitgevoerde commando; deze status wordt opgeslagen in de variabele exit_status.

    - Het controleert of exit_status niet 0 is. In Unix-achtige besturingssystemen betekent een exit status van 0 meestal dat een commando succesvol was, en elke andere waarde duidt op een fout. Als exit_status niet 0 is, wordt een Exception opgegooid met een bericht dat er een fout was bij het downloaden van de dataset.

    - Samengevat voert dit script een commando uit om een dataset te downloaden met een hulpscript, en gooit een uitzondering als het commando faalt.

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

### Data laden in een DataFrame

1. Dit Python script laadt een JSON Lines bestand in een pandas DataFrame en toont de eerste 5 rijen. Hier volgt een overzicht van wat het doet:

    - Het importeert de pandas bibliotheek, een krachtige bibliotheek voor data manipulatie en analyse.

    - Het stelt de maximale kolombreedte in voor de pandas display opties op 0. Dit betekent dat de volledige tekst van elke kolom wordt weergegeven zonder afkapping wanneer de DataFrame wordt geprint.

    - Het gebruikt de pd.read_json functie om het train_sft.jsonl bestand uit de ultrachat_200k_dataset map te laden in een DataFrame. De parameter lines=True geeft aan dat het bestand in JSON Lines formaat is, waarbij elke regel een apart JSON object is.
- Het gebruikt de head-methode om de eerste 5 rijen van de DataFrame weer te geven. Als de DataFrame minder dan 5 rijen bevat, worden ze allemaal getoond.

- Samengevat laadt dit script een JSON Lines-bestand in een DataFrame en toont het de eerste 5 rijen met volledige kolomtekst.

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

## 5. Dien de fine tuning-taak in met het model en de data als invoer

Maak de taak aan die de chat-completion pipeline component gebruikt. Lees meer over alle parameters die worden ondersteund voor fine tuning.

### Definieer finetune parameters

1. Finetune parameters kunnen worden onderverdeeld in 2 categorieën - trainingsparameters en optimalisatieparameters

1. Trainingsparameters definiëren de trainingsaspecten zoals -

    - De optimizer en scheduler die gebruikt worden
    - De metric die geoptimaliseerd wordt tijdens de fine tuning
    - Aantal trainingsstappen, batchgrootte, enzovoort
    - Optimalisatieparameters helpen bij het optimaliseren van het GPU-geheugen en het effectief gebruiken van de rekenmiddelen.

1. Hieronder staan enkele parameters die tot deze categorie behoren. De optimalisatieparameters verschillen per model en worden meegeleverd met het model om deze variaties af te handelen.

    - Deepspeed en LoRA inschakelen
    - Mixed precision training inschakelen
    - Multi-node training inschakelen


> [!NOTE]
> Supervised finetuning kan leiden tot verlies van alignment of catastrofaal vergeten. We raden aan om dit te controleren en een alignment-fase uit te voeren nadat je hebt gefinetuned.

### Fine Tuning Parameters

1. Dit Python-script stelt parameters in voor het fine-tunen van een machine learning-model. Hier is een overzicht van wat het doet:

    - Het stelt standaard trainingsparameters in zoals het aantal trainings-epochs, batchgroottes voor training en evaluatie, leersnelheid en het type learning rate scheduler.

    - Het stelt standaard optimalisatieparameters in zoals of Layer-wise Relevance Propagation (LoRa) en DeepSpeed worden toegepast, en de DeepSpeed stage.

    - Het combineert de trainings- en optimalisatieparameters in één dictionary genaamd finetune_parameters.

    - Het controleert of foundation_model model-specifieke standaardparameters heeft. Zo ja, dan wordt een waarschuwingsbericht weergegeven en worden deze model-specifieke standaardwaarden toegevoegd aan finetune_parameters. De functie ast.literal_eval wordt gebruikt om de model-specifieke standaardwaarden van een string naar een Python dictionary om te zetten.

    - Het print de uiteindelijke set fine-tuning parameters die gebruikt zullen worden voor de run.

    - Samengevat stelt dit script de parameters in voor het fine-tunen van een machine learning-model en toont deze, met de mogelijkheid om de standaardparameters te overschrijven met model-specifieke waarden.

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

### Trainingspipeline

1. Dit Python-script definieert een functie om een weergavenaam te genereren voor een machine learning trainingspipeline, en roept deze functie vervolgens aan om de naam te genereren en af te drukken. Hier is een overzicht van wat het doet:

1. De functie get_pipeline_display_name wordt gedefinieerd. Deze functie genereert een weergavenaam op basis van verschillende parameters die betrekking hebben op de trainingspipeline.

1. Binnen de functie wordt de totale batchgrootte berekend door de batchgrootte per apparaat te vermenigvuldigen met het aantal gradient accumulation stappen, het aantal GPU's per node en het aantal nodes dat wordt gebruikt voor fine-tuning.

1. Het haalt verschillende andere parameters op zoals het type learning rate scheduler, of DeepSpeed wordt toegepast, de DeepSpeed stage, of Layer-wise Relevance Propagation (LoRa) wordt toegepast, het limiet op het aantal model checkpoints om te bewaren, en de maximale sequentielengte.

1. Het bouwt een string op die al deze parameters bevat, gescheiden door streepjes. Als DeepSpeed of LoRa wordt toegepast, bevat de string respectievelijk "ds" gevolgd door de DeepSpeed stage, of "lora". Zo niet, dan bevat het "nods" of "nolora".

1. De functie retourneert deze string, die dient als de weergavenaam voor de trainingspipeline.

1. Nadat de functie is gedefinieerd, wordt deze aangeroepen om de weergavenaam te genereren, die vervolgens wordt afgedrukt.

1. Samengevat genereert dit script een weergavenaam voor een machine learning trainingspipeline op basis van verschillende parameters, en drukt deze naam af.

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

### Pipeline configureren

Dit Python-script definieert en configureert een machine learning pipeline met behulp van de Azure Machine Learning SDK. Hier is een overzicht van wat het doet:

1. Het importeert de benodigde modules uit de Azure AI ML SDK.

1. Het haalt een pipeline component op met de naam "chat_completion_pipeline" uit het register.

1. Het definieert een pipeline job met de `@pipeline` decorator en de functie `create_pipeline`. De naam van de pipeline wordt ingesteld op `pipeline_display_name`.

1. Binnen de functie `create_pipeline` initialiseert het de opgehaalde pipeline component met verschillende parameters, waaronder het modelpad, compute clusters voor verschillende fasen, dataset splits voor training en testen, het aantal GPU's dat gebruikt wordt voor fine-tuning, en andere fine-tuning parameters.

1. Het koppelt de output van de fine-tuning taak aan de output van de pipeline job. Dit wordt gedaan zodat het gefinetunede model eenvoudig geregistreerd kan worden, wat nodig is om het model te kunnen deployen naar een online of batch endpoint.

1. Het maakt een instantie van de pipeline aan door de functie `create_pipeline` aan te roepen.

1. Het zet de `force_rerun` instelling van de pipeline op `True`, wat betekent dat gecachte resultaten van eerdere taken niet worden gebruikt.

1. Het zet de `continue_on_step_failure` instelling van de pipeline op `False`, wat betekent dat de pipeline stopt als een stap faalt.

1. Samengevat definieert en configureert dit script een machine learning pipeline voor een chat completion taak met behulp van de Azure Machine Learning SDK.

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

### Dien de taak in

1. Dit Python-script dient een machine learning pipeline job in bij een Azure Machine Learning workspace en wacht vervolgens tot de taak is voltooid. Hier is een overzicht van wat het doet:

    - Het roept de create_or_update methode aan van het jobs-object in de workspace_ml_client om de pipeline job in te dienen. De pipeline die uitgevoerd moet worden wordt gespecificeerd door pipeline_object, en het experiment waaronder de taak wordt uitgevoerd wordt gespecificeerd door experiment_name.

    - Daarna roept het de stream methode aan van het jobs-object in de workspace_ml_client om te wachten tot de pipeline job is voltooid. De taak waar op gewacht wordt wordt gespecificeerd door het name attribuut van het pipeline_job object.

    - Samengevat dient dit script een machine learning pipeline job in bij een Azure Machine Learning workspace en wacht tot de taak is afgerond.

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

## 6. Registreer het gefinetunede model bij de workspace

We zullen het model registreren vanuit de output van de fine tuning taak. Dit zal de afstamming bijhouden tussen het gefinetunede model en de fine tuning taak. De fine tuning taak houdt op zijn beurt de afstamming bij naar het foundation model, de data en de trainingscode.

### ML Model registreren

1. Dit Python-script registreert een machine learning model dat getraind is in een Azure Machine Learning pipeline. Hier is een overzicht van wat het doet:

    - Het importeert de benodigde modules uit de Azure AI ML SDK.

    - Het controleert of de output trained_model beschikbaar is van de pipeline job door de get-methode aan te roepen van het jobs-object in de workspace_ml_client en toegang te krijgen tot de outputs-attribuut.

    - Het bouwt een pad naar het getrainde model door een string te formatteren met de naam van de pipeline job en de naam van de output ("trained_model").

    - Het definieert een naam voor het gefinetunede model door "-ultrachat-200k" toe te voegen aan de originele modelnaam en eventuele schuine strepen te vervangen door streepjes.

    - Het bereidt de registratie van het model voor door een Model-object te maken met verschillende parameters, waaronder het pad naar het model, het type model (MLflow model), de naam en versie van het model, en een beschrijving van het model.

    - Het registreert het model door de create_or_update methode aan te roepen van het models-object in de workspace_ml_client met het Model-object als argument.

    - Het print het geregistreerde model.

1. Samengevat registreert dit script een machine learning model dat getraind is in een Azure Machine Learning pipeline.

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

## 7. Deploy het gefinetunede model naar een online endpoint

Online endpoints bieden een duurzame REST API die gebruikt kan worden om te integreren met applicaties die het model willen gebruiken.

### Endpoint beheren

1. Dit Python-script maakt een managed online endpoint aan in Azure Machine Learning voor een geregistreerd model. Hier is een overzicht van wat het doet:

    - Het importeert de benodigde modules uit de Azure AI ML SDK.

    - Het definieert een unieke naam voor het online endpoint door een timestamp toe te voegen aan de string "ultrachat-completion-".

    - Het bereidt het aanmaken van het online endpoint voor door een ManagedOnlineEndpoint-object te maken met verschillende parameters, waaronder de naam van het endpoint, een beschrijving van het endpoint, en de authenticatiemodus ("key").

    - Het maakt het online endpoint aan door de begin_create_or_update methode aan te roepen van de workspace_ml_client met het ManagedOnlineEndpoint-object als argument. Daarna wacht het op het voltooien van de aanmaakoperatie door de wait-methode aan te roepen.

1. Samengevat maakt dit script een managed online endpoint aan in Azure Machine Learning voor een geregistreerd model.

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
> Hier vind je de lijst met SKU's die ondersteund worden voor deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML Model deployen

1. Dit Python-script deployt een geregistreerd machine learning model naar een managed online endpoint in Azure Machine Learning. Hier is een overzicht van wat het doet:

    - Het importeert de ast-module, die functies biedt om bomen van de Python abstracte syntaxisgrammatica te verwerken.

    - Het stelt het instance type voor de deployment in op "Standard_NC6s_v3".

    - Het controleert of de tag inference_compute_allow_list aanwezig is in het foundation model. Als dat zo is, zet het de tagwaarde om van een string naar een Python-lijst en wijst deze toe aan inference_computes_allow_list. Zo niet, dan wordt inference_computes_allow_list op None gezet.

    - Het controleert of het opgegeven instance type in de allow list staat. Zo niet, dan print het een bericht waarin de gebruiker wordt gevraagd een instance type uit de allow list te kiezen.

    - Het bereidt de deployment voor door een ManagedOnlineDeployment-object te maken met verschillende parameters, waaronder de naam van de deployment, de naam van het endpoint, de ID van het model, het instance type en aantal, de instellingen voor de liveness probe, en de request instellingen.

    - Het maakt de deployment aan door de begin_create_or_update methode aan te roepen van de workspace_ml_client met het ManagedOnlineDeployment-object als argument. Daarna wacht het op het voltooien van de aanmaakoperatie door de wait-methode aan te roepen.

    - Het stelt het verkeer van het endpoint in om 100% van het verkeer naar de "demo" deployment te sturen.

    - Het werkt het endpoint bij door de begin_create_or_update methode aan te roepen van de workspace_ml_client met het endpoint-object als argument. Daarna wacht het op het voltooien van de update-operatie door de result-methode aan te roepen.

1. Samengevat deployt dit script een geregistreerd machine learning model naar een managed online endpoint in Azure Machine Learning.

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

## 8. Test het endpoint met voorbeelddata

We halen wat voorbeelddata op uit de testdataset en sturen deze naar het online endpoint voor inferentie. Daarna tonen we de gescoorde labels naast de grondwaarheidslabels.

### Resultaten lezen

1. Dit Python-script leest een JSON Lines-bestand in een pandas DataFrame, neemt een willekeurige steekproef, en reset de index. Hier is een overzicht van wat het doet:

    - Het leest het bestand ./ultrachat_200k_dataset/test_gen.jsonl in een pandas DataFrame. De read_json functie wordt gebruikt met het argument lines=True omdat het bestand in JSON Lines-formaat is, waarbij elke regel een apart JSON-object is.

    - Het neemt een willekeurige steekproef van 1 rij uit de DataFrame. De sample functie wordt gebruikt met het argument n=1 om het aantal willekeurige rijen te specificeren.

    - Het reset de index van de DataFrame. De reset_index functie wordt gebruikt met het argument drop=True om de originele index te verwijderen en te vervangen door een nieuwe index met standaard gehele getallen.

    - Het toont de eerste 2 rijen van de DataFrame met de head functie en het argument 2. Omdat de DataFrame na de steekproef slechts één rij bevat, wordt alleen die ene rij getoond.

1. Samengevat leest dit script een JSON Lines-bestand in een pandas DataFrame, neemt een willekeurige steekproef van 1 rij, reset de index, en toont de eerste rij.

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

### JSON-object maken

1. Dit Python-script maakt een JSON-object met specifieke parameters en slaat dit op in een bestand. Hier is een overzicht van wat het doet:

    - Het importeert de json-module, die functies biedt om met JSON-data te werken.

    - Het maakt een dictionary parameters met sleutels en waarden die parameters voor een machine learning-model vertegenwoordigen. De sleutels zijn "temperature", "top_p", "do_sample" en "max_new_tokens", met respectievelijk de waarden 0.6, 0.9, True en 200.

    - Het maakt een andere dictionary test_json met twee sleutels: "input_data" en "params". De waarde van "input_data" is een andere dictionary met de sleutels "input_string" en "parameters". De waarde van "input_string" is een lijst die het eerste bericht uit de test_df DataFrame bevat. De waarde van "parameters" is de eerder gemaakte parameters dictionary. De waarde van "params" is een lege dictionary.
- Het opent een bestand met de naam sample_score.json

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

### Endpoint aanroepen

1. Dit Python-script roept een online endpoint aan in Azure Machine Learning om een JSON-bestand te scoren. Hier is een overzicht van wat het doet:

    - Het roept de invoke-methode aan van de online_endpoints-eigenschap van het workspace_ml_client-object. Deze methode wordt gebruikt om een verzoek naar een online endpoint te sturen en een antwoord te ontvangen.

    - Het geeft de naam van het endpoint en de deployment op met de argumenten endpoint_name en deployment_name. In dit geval is de naam van het endpoint opgeslagen in de variabele online_endpoint_name en de deployment-naam is "demo".

    - Het geeft het pad naar het JSON-bestand dat gescoord moet worden op met het argument request_file. In dit geval is het bestand ./ultrachat_200k_dataset/sample_score.json.

    - Het slaat de reactie van het endpoint op in de variabele response.

    - Het print de ruwe reactie.

1. Samengevat roept dit script een online endpoint aan in Azure Machine Learning om een JSON-bestand te scoren en print het de reactie.

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

## 9. Verwijder het online endpoint

1. Vergeet niet het online endpoint te verwijderen, anders blijft de kostenmeter doorlopen voor de compute die door het endpoint wordt gebruikt. Deze regel Python-code verwijdert een online endpoint in Azure Machine Learning. Hier is een overzicht van wat het doet:

    - Het roept de begin_delete-methode aan van de online_endpoints-eigenschap van het workspace_ml_client-object. Deze methode start het verwijderingsproces van een online endpoint.

    - Het geeft de naam van het te verwijderen endpoint op met het argument name. In dit geval is de naam van het endpoint opgeslagen in de variabele online_endpoint_name.

    - Het roept de wait-methode aan om te wachten tot de verwijderingsoperatie is voltooid. Dit is een blokkerende operatie, wat betekent dat het script niet verder gaat totdat de verwijdering is afgerond.

    - Samengevat start deze regel code het verwijderen van een online endpoint in Azure Machine Learning en wacht op het voltooien van de operatie.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.