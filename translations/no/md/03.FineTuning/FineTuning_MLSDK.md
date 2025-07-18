<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:29:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "no"
}
-->
## Hvordan bruke chat-completion-komponenter fra Azure ML systemregisteret for å finjustere en modell

I dette eksempelet skal vi finjustere Phi-3-mini-4k-instruct-modellen for å fullføre en samtale mellom 2 personer ved bruk av ultrachat_200k-datasettet.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.no.png)

Eksempelet viser hvordan du kan finjustere en modell ved hjelp av Azure ML SDK og Python, og deretter distribuere den finjusterte modellen til en online endepunkt for sanntidsinferens.

### Treningsdata

Vi bruker ultrachat_200k-datasettet. Dette er en sterkt filtrert versjon av UltraChat-datasettet og ble brukt til å trene Zephyr-7B-β, en toppmoderne 7b chat-modell.

### Modell

Vi bruker Phi-3-mini-4k-instruct-modellen for å vise hvordan brukeren kan finjustere en modell for chat-completion-oppgaven. Hvis du åpnet denne notatboken fra et spesifikt modellkort, husk å bytte ut modellnavnet.

### Oppgaver

- Velg en modell for finjustering.
- Velg og utforsk treningsdata.
- Konfigurer finjusteringsjobben.
- Kjør finjusteringsjobben.
- Gå gjennom trenings- og evalueringsmetrikker.
- Registrer den finjusterte modellen.
- Distribuer den finjusterte modellen for sanntidsinferens.
- Rydd opp i ressurser.

## 1. Sett opp forutsetninger

- Installer avhengigheter
- Koble til AzureML Workspace. Les mer om hvordan du setter opp SDK-autentisering. Bytt ut <WORKSPACE_NAME>, <RESOURCE_GROUP> og <SUBSCRIPTION_ID> nedenfor.
- Koble til azureml systemregister
- Sett et valgfritt eksperimentnavn
- Sjekk eller opprett compute.

> [!NOTE]
> Krav: En enkelt GPU-node kan ha flere GPU-kort. For eksempel har en node av Standard_NC24rs_v3 4 NVIDIA V100 GPUer, mens Standard_NC12s_v3 har 2 NVIDIA V100 GPUer. Se dokumentasjonen for mer informasjon. Antall GPU-kort per node settes i parameteren gpus_per_node nedenfor. Å sette denne verdien riktig sikrer utnyttelse av alle GPUene i noden. Anbefalte GPU compute SKUer finnes her og her.

### Python-biblioteker

Installer avhengigheter ved å kjøre cellen nedenfor. Dette er ikke et valgfritt steg hvis du kjører i et nytt miljø.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Samhandling med Azure ML

1. Dette Python-skriptet brukes for å samhandle med Azure Machine Learning (Azure ML)-tjenesten. Her er en oversikt over hva det gjør:

    - Importerer nødvendige moduler fra azure.ai.ml, azure.identity og azure.ai.ml.entities-pakkene. Importerer også time-modulen.

    - Forsøker å autentisere med DefaultAzureCredential(), som gir en forenklet autentiseringsopplevelse for raskt å komme i gang med utvikling av applikasjoner som kjører i Azure-skyen. Hvis dette feiler, faller det tilbake til InteractiveBrowserCredential(), som gir en interaktiv påloggingsprompt.

    - Forsøker deretter å opprette en MLClient-instans ved hjelp av from_config-metoden, som leser konfigurasjonen fra standard konfigurasjonsfil (config.json). Hvis dette feiler, opprettes MLClient-instansen manuelt ved å oppgi subscription_id, resource_group_name og workspace_name.

    - Oppretter en annen MLClient-instans, denne gangen for Azure ML-registeret kalt "azureml". Dette registeret er der modeller, finjusteringspipelines og miljøer lagres.

    - Setter experiment_name til "chat_completion_Phi-3-mini-4k-instruct".

    - Genererer et unikt tidsstempel ved å konvertere nåværende tid (i sekunder siden epoken, som flyttall) til et heltall og deretter til en streng. Dette tidsstempelet kan brukes for å lage unike navn og versjoner.

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

## 2. Velg en grunnmodell for finjustering

1. Phi-3-mini-4k-instruct er en 3,8 milliarder parametere stor, lettvekts, toppmoderne åpen modell basert på datasett brukt for Phi-2. Modellen tilhører Phi-3 modellfamilien, og Mini-versjonen kommer i to varianter, 4K og 128K, som angir kontekstlengden (i tokens) den kan støtte. Vi må finjustere modellen for vårt spesifikke formål for å kunne bruke den. Du kan bla gjennom disse modellene i Model Catalog i AzureML Studio, filtrert på chat-completion-oppgaven. I dette eksempelet bruker vi Phi-3-mini-4k-instruct-modellen. Hvis du har åpnet denne notatboken for en annen modell, bytt ut modellnavn og versjon tilsvarende.

    > [!NOTE]
    > modellens id-egenskap. Denne sendes som input til finjusteringsjobben. Den er også tilgjengelig som Asset ID-feltet på modelsiden i AzureML Studio Model Catalog.

2. Dette Python-skriptet samhandler med Azure Machine Learning (Azure ML)-tjenesten. Her er en oversikt over hva det gjør:

    - Setter model_name til "Phi-3-mini-4k-instruct".

    - Bruker get-metoden til models-egenskapen til registry_ml_client-objektet for å hente siste versjon av modellen med det angitte navnet fra Azure ML-registeret. get-metoden kalles med to argumenter: modellnavnet og en etikett som spesifiserer at siste versjon skal hentes.

    - Skriver ut en melding til konsollen som viser navn, versjon og id på modellen som skal brukes til finjustering. format-metoden til strengen brukes for å sette inn navn, versjon og id i meldingen. Disse egenskapene hentes fra foundation_model-objektet.

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

## 3. Opprett en compute som skal brukes med jobben

Finjusteringsjobben fungerer KUN med GPU compute. Størrelsen på compute avhenger av hvor stor modellen er, og i de fleste tilfeller kan det være vanskelig å finne riktig compute for jobben. I denne cellen veileder vi brukeren til å velge riktig compute for jobben.

> [!NOTE]
> Compute-typene listet nedenfor fungerer med den mest optimaliserte konfigurasjonen. Endringer i konfigurasjonen kan føre til Cuda Out Of Memory-feil. I slike tilfeller, prøv å oppgradere compute til en større størrelse.

> [!NOTE]
> Når du velger compute_cluster_size nedenfor, må du sørge for at compute er tilgjengelig i din resource group. Hvis en bestemt compute ikke er tilgjengelig, kan du be om tilgang til compute-ressursene.

### Sjekke modell for støtte til finjustering

1. Dette Python-skriptet samhandler med en Azure Machine Learning (Azure ML)-modell. Her er en oversikt over hva det gjør:

    - Importerer ast-modulen, som gir funksjoner for å behandle trær av Python abstrakt syntaksgrammatikk.

    - Sjekker om foundation_model-objektet (som representerer en modell i Azure ML) har en tag kalt finetune_compute_allow_list. Tags i Azure ML er nøkkel-verdi-par som kan brukes til å filtrere og sortere modeller.

    - Hvis finetune_compute_allow_list-taggen finnes, bruker den ast.literal_eval for å trygt tolke taggens verdi (en streng) til en Python-liste. Denne listen tildeles variabelen computes_allow_list. Skriver deretter ut en melding om at compute bør opprettes fra denne listen.

    - Hvis taggen ikke finnes, settes computes_allow_list til None og det skrives ut en melding om at finetune_compute_allow_list ikke er en del av modellens tags.

    - Oppsummert sjekker skriptet for en spesifikk tag i modellens metadata, konverterer taggens verdi til en liste hvis den finnes, og gir tilbakemelding til brukeren.

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

### Sjekke Compute Instance

1. Dette Python-skriptet samhandler med Azure Machine Learning (Azure ML)-tjenesten og utfører flere sjekker på en compute-instans. Her er en oversikt over hva det gjør:

    - Forsøker å hente compute-instansen med navnet lagret i compute_cluster fra Azure ML workspace. Hvis compute-instansens provisioning-tilstand er "failed", kaster den en ValueError.

    - Sjekker om computes_allow_list ikke er None. Hvis den ikke er det, konverterer den alle compute-størrelser i listen til små bokstaver og sjekker om størrelsen på den nåværende compute-instansen er i listen. Hvis ikke, kaster den en ValueError.

    - Hvis computes_allow_list er None, sjekker den om størrelsen på compute-instansen er i en liste over ikke-støttede GPU VM-størrelser. Hvis den er det, kaster den en ValueError.

    - Henter en liste over alle tilgjengelige compute-størrelser i workspace. Itererer over denne listen, og for hver compute-størrelse sjekker den om navnet matcher størrelsen på den nåværende compute-instansen. Hvis det stemmer, henter den antall GPUer for den compute-størrelsen og setter gpu_count_found til True.

    - Hvis gpu_count_found er True, skriver den ut antall GPUer i compute-instansen. Hvis ikke, kaster den en ValueError.

    - Oppsummert utfører skriptet flere sjekker på en compute-instans i Azure ML workspace, inkludert provisioning-tilstand, størrelse mot en tillatt-liste eller nektet-liste, og antall GPUer.

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

## 4. Velg datasettet for finjustering av modellen

1. Vi bruker ultrachat_200k-datasettet. Datasettet har fire splitt, egnet for Supervised fine-tuning (sft) og Generation ranking (gen). Antall eksempler per splitt vises som følger:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. De neste cellene viser grunnleggende databehandling for finjustering:

### Visualiser noen datarader

Vi ønsker at dette eksempelet skal kjøre raskt, så vi lagrer train_sft og test_sft filer som inneholder 5 % av de allerede trimmede radene. Dette betyr at den finjusterte modellen vil ha lavere nøyaktighet, og bør derfor ikke brukes i produksjon.
download-dataset.py brukes for å laste ned ultrachat_200k-datasettet og transformere datasettet til et format som kan brukes i finjusteringspipelines. Siden datasettet er stort, har vi her kun en del av datasettet.

1. Kjøring av skriptet nedenfor laster kun ned 5 % av dataene. Dette kan økes ved å endre parameteren dataset_split_pc til ønsket prosentandel.

    > [!NOTE]
    > Noen språkmodeller har ulike språk-koder, og kolonnenavnene i datasettet bør derfor reflektere dette.

1. Her er et eksempel på hvordan dataene skal se ut
chat-completion-datasettet lagres i parquet-format med hver oppføring i følgende skjema:

    - Dette er et JSON (JavaScript Object Notation)-dokument, som er et populært datautvekslingsformat. Det er ikke kjørbar kode, men en måte å lagre og transportere data på. Her er en oversikt over strukturen:

    - "prompt": Denne nøkkelen inneholder en streng som representerer en oppgave eller et spørsmål stilt til en AI-assistent.

    - "messages": Denne nøkkelen inneholder en liste med objekter. Hvert objekt representerer en melding i en samtale mellom en bruker og en AI-assistent. Hvert melding-objekt har to nøkler:

    - "content": Denne nøkkelen inneholder en streng som representerer innholdet i meldingen.
    - "role": Denne nøkkelen inneholder en streng som representerer rollen til den som sendte meldingen. Det kan være enten "user" eller "assistant".
    - "prompt_id": Denne nøkkelen inneholder en streng som representerer en unik identifikator for prompten.

1. I dette spesifikke JSON-dokumentet representeres en samtale der en bruker ber en AI-assistent om å lage en protagonist for en dystopisk historie. Assistenten svarer, og brukeren ber deretter om flere detaljer. Assistenten samtykker i å gi flere detaljer. Hele samtalen er knyttet til en spesifikk prompt-id.

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

### Last ned data

1. Dette Python-skriptet brukes for å laste ned et datasett ved hjelp av et hjelpeskript kalt download-dataset.py. Her er en oversikt over hva det gjør:

    - Importerer os-modulen, som gir en plattformuavhengig måte å bruke operativsystemavhengig funksjonalitet på.

    - Bruker os.system-funksjonen for å kjøre download-dataset.py-skriptet i shell med spesifikke kommandolinjeargumenter. Argumentene spesifiserer datasettet som skal lastes ned (HuggingFaceH4/ultrachat_200k), katalogen det skal lastes ned til (ultrachat_200k_dataset), og prosentandelen av datasettet som skal splittes ut (5). os.system returnerer avslutningsstatusen til kommandoen; denne lagres i exit_status-variabelen.

    - Sjekker om exit_status ikke er 0. I Unix-lignende operativsystemer indikerer 0 at kommandoen lykkes, mens andre tall indikerer feil. Hvis exit_status ikke er 0, kaster den en Exception med en melding om at det oppstod en feil ved nedlasting av datasettet.

    - Oppsummert kjører skriptet en kommando for å laste ned et datasett ved hjelp av et hjelpeskript, og kaster unntak hvis kommandoen feiler.

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

### Laste data inn i en DataFrame

1. Dette Python-skriptet laster en JSON Lines-fil inn i en pandas DataFrame og viser de første 5 radene. Her er en oversikt over hva det gjør:

    - Importerer pandas-biblioteket, som er et kraftig verktøy for datamanipulering og analyse.

    - Setter maksimal kolonnebredde for pandas visningsinnstillinger til 0. Dette betyr at hele teksten i hver kolonne vises uten avkorting når DataFrame printes.

    - Bruker pd.read_json-funksjonen for å laste train_sft.jsonl-filen fra ultrachat_200k_dataset-katalogen inn i en DataFrame. Argumentet lines=True indikerer at filen er i JSON Lines-format, hvor hver linje er et eget JSON-objekt.
- Den bruker head-metoden for å vise de første 5 radene i DataFrame. Hvis DataFrame har færre enn 5 rader, vil den vise alle.

- Oppsummert laster dette skriptet en JSON Lines-fil inn i en DataFrame og viser de første 5 radene med full kolonnevisning.

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

## 5. Send inn finjusteringsjobben ved å bruke modellen og data som input

Opprett jobben som bruker chat-completion pipeline-komponenten. Lær mer om alle parametrene som støttes for finjustering.

### Definer finjusteringsparametere

1. Finjusteringsparametere kan deles inn i 2 kategorier – treningsparametere og optimaliseringsparametere

1. Treningsparametere definerer treningsaspekter som –

    - Optimizer og scheduler som skal brukes
    - Metoden for å optimalisere finjusteringen
    - Antall treningssteg, batch-størrelse og så videre
    - Optimaliseringsparametere hjelper med å optimalisere GPU-minnet og utnytte beregningsressursene effektivt.

1. Nedenfor er noen av parametrene som tilhører denne kategorien. Optimaliseringsparametrene varierer for hver modell og følger med modellen for å håndtere disse variasjonene.

    - Aktiver deepspeed og LoRA
    - Aktiver mixed precision training
    - Aktiver multi-node trening


> [!NOTE]
> Supervised finetuning kan føre til tap av justering eller katastrofalt glemsel. Vi anbefaler å sjekke for dette problemet og kjøre en justeringsfase etter finjusteringen.

### Finjusteringsparametere

1. Dette Python-skriptet setter opp parametere for finjustering av en maskinlæringsmodell. Her er en oversikt over hva det gjør:

    - Setter opp standard treningsparametere som antall trenings-epoker, batch-størrelser for trening og evaluering, læringsrate og type læringsrate-scheduler.

    - Setter opp standard optimaliseringsparametere som om Layer-wise Relevance Propagation (LoRa) og DeepSpeed skal brukes, samt DeepSpeed-stadiet.

    - Kombinerer trenings- og optimaliseringsparametere i en enkelt ordbok kalt finetune_parameters.

    - Sjekker om foundation_model har noen modellspesifikke standardparametere. Hvis ja, skriver den ut en advarsel og oppdaterer finetune_parameters med disse modellspesifikke standardene. ast.literal_eval brukes for å konvertere modellspesifikke standarder fra streng til Python-ordbok.

    - Skriver ut det endelige settet med finjusteringsparametere som skal brukes i kjøringen.

    - Oppsummert setter dette skriptet opp og viser parametere for finjustering av en maskinlæringsmodell, med mulighet for å overstyre standardparametere med modellspesifikke.

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

### Treningspipeline

1. Dette Python-skriptet definerer en funksjon for å generere et visningsnavn for en maskinlærings-treningspipeline, og kaller deretter denne funksjonen for å generere og skrive ut visningsnavnet. Her er en oversikt over hva det gjør:

1. Funksjonen get_pipeline_display_name defineres. Denne funksjonen genererer et visningsnavn basert på ulike parametere knyttet til treningspipen.

1. Inne i funksjonen beregnes total batch-størrelse ved å multiplisere batch-størrelse per enhet, antall gradientakkumuleringssteg, antall GPUer per node og antall noder som brukes til finjustering.

1. Den henter også andre parametere som type læringsrate-scheduler, om DeepSpeed er aktivert, DeepSpeed-stadiet, om Layer-wise Relevance Propagation (LoRa) er aktivert, grense for antall modell-sjekkpunkter som skal beholdes, og maksimal sekvenslengde.

1. Den bygger en streng som inkluderer alle disse parameterne, separert med bindestreker. Hvis DeepSpeed eller LoRa er aktivert, inkluderer strengen henholdsvis "ds" etterfulgt av DeepSpeed-stadiet, eller "lora". Hvis ikke, inkluderer den "nods" eller "nolora".

1. Funksjonen returnerer denne strengen, som fungerer som visningsnavnet for treningspipen.

1. Etter at funksjonen er definert, kalles den for å generere visningsnavnet, som deretter skrives ut.

1. Oppsummert genererer dette skriptet et visningsnavn for en maskinlærings-treningspipeline basert på ulike parametere, og skriver deretter ut dette navnet.

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

### Konfigurere pipeline

Dette Python-skriptet definerer og konfigurerer en maskinlæringspipeline ved bruk av Azure Machine Learning SDK. Her er en oversikt over hva det gjør:

1. Importerer nødvendige moduler fra Azure AI ML SDK.

1. Henter en pipeline-komponent kalt "chat_completion_pipeline" fra registeret.

1. Definerer en pipeline-jobb med `@pipeline`-dekoratøren og funksjonen `create_pipeline`. Navnet på pipelinen settes til `pipeline_display_name`.

1. Inne i `create_pipeline`-funksjonen initialiseres den hentede pipeline-komponenten med ulike parametere, inkludert modellbane, compute-klynger for ulike steg, datasett-splittelser for trening og testing, antall GPUer som skal brukes til finjustering, og andre finjusteringsparametere.

1. Mapper output fra finjusteringsjobben til output fra pipeline-jobben. Dette gjøres slik at den finjusterte modellen enkelt kan registreres, noe som kreves for å distribuere modellen til en online- eller batch-endepunkt.

1. Oppretter en instans av pipelinen ved å kalle `create_pipeline`-funksjonen.

1. Setter `force_rerun`-innstillingen for pipelinen til `True`, som betyr at cachede resultater fra tidligere jobber ikke vil bli brukt.

1. Setter `continue_on_step_failure`-innstillingen for pipelinen til `False`, som betyr at pipelinen stopper hvis et steg feiler.

1. Oppsummert definerer og konfigurerer dette skriptet en maskinlæringspipeline for en chat completion-oppgave ved bruk av Azure Machine Learning SDK.

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

### Send inn jobben

1. Dette Python-skriptet sender inn en maskinlæringspipeline-jobb til et Azure Machine Learning-arbeidsområde og venter deretter på at jobben skal fullføres. Her er en oversikt over hva det gjør:

    - Kaller create_or_update-metoden til jobs-objektet i workspace_ml_client for å sende inn pipeline-jobben. Pipen som skal kjøres spesifiseres av pipeline_object, og eksperimentet som jobben kjøres under spesifiseres av experiment_name.

    - Kaller deretter stream-metoden til jobs-objektet i workspace_ml_client for å vente på at pipeline-jobben skal fullføres. Jobben som det ventes på spesifiseres av name-attributtet til pipeline_job-objektet.

    - Oppsummert sender dette skriptet inn en maskinlæringspipeline-jobb til et Azure Machine Learning-arbeidsområde, og venter deretter på at jobben skal fullføres.

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

## 6. Registrer den finjusterte modellen i arbeidsområdet

Vi vil registrere modellen fra outputen til finjusteringsjobben. Dette vil spore opphavet mellom den finjusterte modellen og finjusteringsjobben. Finjusteringsjobben sporer videre opphavet til foundation-modellen, data og treningskode.

### Registrere ML-modellen

1. Dette Python-skriptet registrerer en maskinlæringsmodell som ble trent i en Azure Machine Learning-pipeline. Her er en oversikt over hva det gjør:

    - Importerer nødvendige moduler fra Azure AI ML SDK.

    - Sjekker om outputen trained_model er tilgjengelig fra pipeline-jobben ved å kalle get-metoden til jobs-objektet i workspace_ml_client og aksessere outputs-attributtet.

    - Konstruerer en sti til den trente modellen ved å formatere en streng med navnet på pipeline-jobben og navnet på outputen ("trained_model").

    - Definerer et navn for den finjusterte modellen ved å legge til "-ultrachat-200k" til det opprinnelige modellnavnet og erstatte eventuelle skråstreker med bindestreker.

    - Forbereder registrering av modellen ved å opprette et Model-objekt med ulike parametere, inkludert sti til modellen, modelltype (MLflow-modell), navn og versjon av modellen, og en beskrivelse.

    - Registrerer modellen ved å kalle create_or_update-metoden til models-objektet i workspace_ml_client med Model-objektet som argument.

    - Skriver ut den registrerte modellen.

1. Oppsummert registrerer dette skriptet en maskinlæringsmodell som ble trent i en Azure Machine Learning-pipeline.

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

## 7. Distribuer den finjusterte modellen til et online-endepunkt

Online-endepunkter gir en varig REST API som kan brukes til å integrere med applikasjoner som trenger å bruke modellen.

### Administrer endepunkt

1. Dette Python-skriptet oppretter et administrert online-endepunkt i Azure Machine Learning for en registrert modell. Her er en oversikt over hva det gjør:

    - Importerer nødvendige moduler fra Azure AI ML SDK.

    - Definerer et unikt navn for online-endepunktet ved å legge til et tidsstempel til strengen "ultrachat-completion-".

    - Forbereder opprettelse av online-endepunktet ved å opprette et ManagedOnlineEndpoint-objekt med ulike parametere, inkludert navn på endepunktet, en beskrivelse, og autentiseringsmodus ("key").

    - Oppretter online-endepunktet ved å kalle begin_create_or_update-metoden til workspace_ml_client med ManagedOnlineEndpoint-objektet som argument. Venter deretter på at opprettelsen skal fullføres ved å kalle wait-metoden.

1. Oppsummert oppretter dette skriptet et administrert online-endepunkt i Azure Machine Learning for en registrert modell.

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
> Du finner her listen over SKU-er som støttes for distribusjon – [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Distribuere ML-modell

1. Dette Python-skriptet distribuerer en registrert maskinlæringsmodell til et administrert online-endepunkt i Azure Machine Learning. Her er en oversikt over hva det gjør:

    - Importerer ast-modulen, som gir funksjoner for å behandle trær av Python abstrakt syntaksgrammatikk.

    - Setter instanstypen for distribusjonen til "Standard_NC6s_v3".

    - Sjekker om taggen inference_compute_allow_list finnes i foundation-modellen. Hvis den gjør det, konverterer den taggens verdi fra streng til en Python-liste og tildeler den til inference_computes_allow_list. Hvis ikke, settes inference_computes_allow_list til None.

    - Sjekker om den angitte instanstypen er i tillatelseslisten. Hvis ikke, skriver den ut en melding som ber brukeren velge en instanstype fra tillatelseslisten.

    - Forbereder opprettelse av distribusjonen ved å opprette et ManagedOnlineDeployment-objekt med ulike parametere, inkludert navn på distribusjonen, navn på endepunktet, modell-ID, instanstype og antall, liveness probe-innstillinger og request-innstillinger.

    - Oppretter distribusjonen ved å kalle begin_create_or_update-metoden til workspace_ml_client med ManagedOnlineDeployment-objektet som argument. Venter deretter på at opprettelsen skal fullføres ved å kalle wait-metoden.

    - Setter trafikken til endepunktet slik at 100 % av trafikken går til "demo"-distribusjonen.

    - Oppdaterer endepunktet ved å kalle begin_create_or_update-metoden til workspace_ml_client med endepunktobjektet som argument. Venter deretter på at oppdateringen skal fullføres ved å kalle result-metoden.

1. Oppsummert distribuerer dette skriptet en registrert maskinlæringsmodell til et administrert online-endepunkt i Azure Machine Learning.

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

## 8. Test endepunktet med eksempeldata

Vi vil hente noen eksempeldata fra testdatasettet og sende til online-endepunktet for inferens. Vi vil deretter vise de scorede etikettene sammen med de faktiske etikettene.

### Lese resultatene

1. Dette Python-skriptet leser en JSON Lines-fil inn i en pandas DataFrame, tar et tilfeldig utvalg, og tilbakestiller indeksen. Her er en oversikt over hva det gjør:

    - Leser filen ./ultrachat_200k_dataset/test_gen.jsonl inn i en pandas DataFrame. read_json-funksjonen brukes med argumentet lines=True fordi filen er i JSON Lines-format, der hver linje er et eget JSON-objekt.

    - Tar et tilfeldig utvalg på 1 rad fra DataFrame. sample-funksjonen brukes med n=1 for å spesifisere antall tilfeldige rader som skal velges.

    - Tilbakestiller indeksen til DataFrame. reset_index-funksjonen brukes med drop=True for å fjerne den opprinnelige indeksen og erstatte den med en ny indeks med standard heltallsverdier.

    - Viser de første 2 radene i DataFrame ved hjelp av head-funksjonen med argumentet 2. Siden DataFrame bare inneholder én rad etter utvalget, vil dette bare vise den ene raden.

1. Oppsummert leser dette skriptet en JSON Lines-fil inn i en pandas DataFrame, tar et tilfeldig utvalg på 1 rad, tilbakestiller indeksen og viser den første raden.

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

### Opprett JSON-objekt

1. Dette Python-skriptet oppretter et JSON-objekt med spesifikke parametere og lagrer det til en fil. Her er en oversikt over hva det gjør:

    - Importerer json-modulen, som gir funksjoner for å arbeide med JSON-data.

    - Oppretter en ordbok parameters med nøkler og verdier som representerer parametere for en maskinlæringsmodell. Nøklene er "temperature", "top_p", "do_sample" og "max_new_tokens", med tilhørende verdier 0.6, 0.9, True og 200.

    - Oppretter en annen ordbok test_json med to nøkler: "input_data" og "params". Verdien til "input_data" er en annen ordbok med nøklene "input_string" og "parameters". Verdien til "input_string" er en liste som inneholder den første meldingen fra test_df DataFrame. Verdien til "parameters" er parameters-ordboken som ble opprettet tidligere. Verdien til "params" er en tom ordbok.
- Den åpner en fil som heter sample_score.json

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

### Kalle opp endepunkt

1. Dette Python-skriptet kaller opp et online endepunkt i Azure Machine Learning for å score en JSON-fil. Her er en oversikt over hva det gjør:

    - Det kaller invoke-metoden til online_endpoints-egenskapen til workspace_ml_client-objektet. Denne metoden brukes for å sende en forespørsel til et online endepunkt og få et svar.

    - Det spesifiserer navnet på endepunktet og distribusjonen med argumentene endpoint_name og deployment_name. I dette tilfellet er endepunktsnavnet lagret i variabelen online_endpoint_name, og distribusjonsnavnet er "demo".

    - Det angir banen til JSON-filen som skal scores med request_file-argumentet. I dette tilfellet er filen ./ultrachat_200k_dataset/sample_score.json.

    - Det lagrer svaret fra endepunktet i variabelen response.

    - Det skriver ut det rå svaret.

1. Oppsummert kaller dette skriptet opp et online endepunkt i Azure Machine Learning for å score en JSON-fil og skriver ut svaret.

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

## 9. Slett det online endepunktet

1. Ikke glem å slette det online endepunktet, ellers vil du la faktureringsmåleren gå for den beregningskapasiteten som brukes av endepunktet. Denne linjen med Python-kode sletter et online endepunkt i Azure Machine Learning. Her er en oversikt over hva den gjør:

    - Den kaller begin_delete-metoden til online_endpoints-egenskapen til workspace_ml_client-objektet. Denne metoden brukes for å starte slettingen av et online endepunkt.

    - Den spesifiserer navnet på endepunktet som skal slettes med argumentet name. I dette tilfellet er endepunktsnavnet lagret i variabelen online_endpoint_name.

    - Den kaller wait-metoden for å vente på at sletteoperasjonen skal fullføres. Dette er en blokkering, som betyr at skriptet ikke fortsetter før slettingen er ferdig.

    - Oppsummert starter denne kodelinjen slettingen av et online endepunkt i Azure Machine Learning og venter på at operasjonen skal fullføres.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.