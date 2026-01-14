<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:49:58+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "sl"
}
-->
## Kako uporabljati komponente za dokončanje pogovora iz Azure ML sistemskega registra za fino nastavitev modela

V tem primeru bomo izvedli fino nastavitev modela Phi-3-mini-4k-instruct za dokončanje pogovora med dvema osebama z uporabo podatkovne zbirke ultrachat_200k.

![MLFineTune](../../../../translated_images/sl/MLFineTune.928d4c6b3767dd35.png)

Primer bo prikazal, kako izvesti fino nastavitev z uporabo Azure ML SDK in Pythona ter nato razporediti fino nastavljeni model na spletno točko za realnočasovno sklepanje.

### Podatki za učenje

Uporabili bomo podatkovno zbirko ultrachat_200k. To je močno filtrirana različica podatkovne zbirke UltraChat, ki je bila uporabljena za učenje Zephyr-7B-β, vrhunskega 7-milijardnega modela za klepet.

### Model

Uporabili bomo model Phi-3-mini-4k-instruct, da pokažemo, kako lahko uporabnik fino nastavi model za nalogo dokončanja pogovora. Če ste odprli ta zvezek iz določene kartice modela, ne pozabite zamenjati imena modela.

### Naloge

- Izberite model za fino nastavitev.
- Izberite in preglejte podatke za učenje.
- Konfigurirajte nalogo fine nastavitve.
- Zaženite nalogo fine nastavitve.
- Preglejte metrike učenja in ocenjevanja.
- Registrirajte fino nastavljeni model.
- Razporedite fino nastavljeni model za realnočasovno sklepanje.
- Očistite vire.

## 1. Priprava predpogojev

- Namestite odvisnosti
- Povežite se z AzureML Workspace. Več o tem na set up SDK authentication. Spodaj zamenjajte <WORKSPACE_NAME>, <RESOURCE_GROUP> in <SUBSCRIPTION_ID>.
- Povežite se z azureml sistemskim registrom
- Nastavite neobvezno ime eksperimenta
- Preverite ali ustvarite računske vire.

> [!NOTE]
> Zahteva en sam GPU vozlišče, ki lahko ima več GPU kartic. Na primer, v enem vozlišču Standard_NC24rs_v3 so 4 NVIDIA V100 GPU-ji, medtem ko ima Standard_NC12s_v3 2 NVIDIA V100 GPU-ja. Za več informacij glejte dokumentacijo. Število GPU kartic na vozlišče je nastavljeno v parametru gpus_per_node spodaj. Pravilna nastavitev zagotavlja uporabo vseh GPU-jev v vozlišču. Priporočene GPU računske SKU-je najdete tukaj in tukaj.

### Python knjižnice

Namestite odvisnosti z zagonom spodnje celice. To ni neobvezen korak, če delate v novem okolju.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interakcija z Azure ML

1. Ta Python skripta se uporablja za interakcijo z Azure Machine Learning (Azure ML) storitvijo. Tukaj je povzetek, kaj počne:

    - Uvozi potrebne module iz paketov azure.ai.ml, azure.identity in azure.ai.ml.entities. Prav tako uvozi modul time.

    - Poskuša se avtenticirati z DefaultAzureCredential(), ki omogoča poenostavljeno avtentikacijo za hitro začetek razvoja aplikacij v Azure oblaku. Če to ne uspe, preklopi na InteractiveBrowserCredential(), ki omogoča interaktivno prijavo preko brskalnika.

    - Nato poskuša ustvariti instanco MLClient z metodo from_config, ki prebere konfiguracijo iz privzete datoteke (config.json). Če to ne uspe, ročno ustvari MLClient z vnosom subscription_id, resource_group_name in workspace_name.

    - Ustvari še eno instanco MLClient, tokrat za Azure ML register z imenom "azureml". Ta register hrani modele, pipeline za fino nastavitev in okolja.

    - Nastavi ime eksperimenta na "chat_completion_Phi-3-mini-4k-instruct".

    - Ustvari edinstven časovni žig tako, da trenutni čas (v sekundah od epohe, kot plavajoče število) pretvori v celo število in nato v niz. Ta časovni žig se lahko uporabi za ustvarjanje unikatnih imen in različic.

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

## 2. Izberite osnovni model za fino nastavitev

1. Phi-3-mini-4k-instruct je model z 3,8 milijardami parametrov, lahek, vrhunski odprtokodni model, zgrajen na podatkih, uporabljenih za Phi-2. Model spada v družino Phi-3, Mini različica pa je na voljo v dveh variantah 4K in 128K, kar predstavlja dolžino konteksta (v tokenih), ki jo podpira. Model moramo fino nastaviti za naš specifičen namen, da ga lahko uporabimo. Te modele lahko pregledujete v Model Catalog v AzureML Studiu, filtrirano po nalogi dokončanja pogovora. V tem primeru uporabljamo model Phi-3-mini-4k-instruct. Če ste odprli ta zvezek za drug model, ustrezno zamenjajte ime in različico modela.

    > [!NOTE]
    > lastnost model_id modela. To bo posredovano kot vhod v nalogo fine nastavitve. Na voljo je tudi kot polje Asset ID na strani z informacijami o modelu v AzureML Studio Model Catalog.

2. Ta Python skripta komunicira z Azure Machine Learning (Azure ML) storitvijo. Tukaj je povzetek, kaj počne:

    - Nastavi model_name na "Phi-3-mini-4k-instruct".

    - Uporabi metodo get lastnosti models objekta registry_ml_client, da pridobi najnovejšo različico modela z določenim imenom iz Azure ML registra. Metoda get je poklicana z dvema argumentoma: imenom modela in oznako, ki določa, da se pridobi najnovejša različica modela.

    - Izpiše sporočilo v konzolo, ki prikazuje ime, različico in id modela, ki bo uporabljen za fino nastavitev. Metoda format niza vstavi ime, različico in id modela v sporočilo. Ime, različica in id modela so dostopni kot lastnosti objekta foundation_model.

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

## 3. Ustvarite računski vir za nalogo

Naloga fine nastavitve deluje SAMO z GPU računi. Velikost računa je odvisna od velikosti modela in v večini primerov je težko izbrati pravi račun za nalogo. V tej celici uporabnika usmerjamo pri izbiri pravega računa.

> [!NOTE]
> Spodaj navedeni računi delujejo z najbolj optimizirano konfiguracijo. Vsaka sprememba konfiguracije lahko povzroči napako Cuda Out Of Memory. V takih primerih poskusite nadgraditi račun na večjo velikost.

> [!NOTE]
> Pri izbiri compute_cluster_size spodaj se prepričajte, da je račun na voljo v vaši skupini virov. Če določen račun ni na voljo, lahko zaprosite za dostop do računalniških virov.

### Preverjanje podpore modela za fino nastavitev

1. Ta Python skripta komunicira z modelom Azure Machine Learning (Azure ML). Tukaj je povzetek, kaj počne:

    - Uvozi modul ast, ki omogoča obdelavo dreves abstraktne sintakse Pythona.

    - Preveri, ali ima objekt foundation_model (ki predstavlja model v Azure ML) oznako finetune_compute_allow_list. Oznake v Azure ML so ključ-vrednost pari, ki jih lahko ustvarite in uporabite za filtriranje in razvrščanje modelov.

    - Če oznaka finetune_compute_allow_list obstaja, uporabi funkcijo ast.literal_eval za varno pretvorbo vrednosti oznake (niz) v Python seznam. Ta seznam se nato dodeli spremenljivki computes_allow_list. Izpiše sporočilo, da je treba ustvariti račun iz tega seznama.

    - Če oznake ni, nastavi computes_allow_list na None in izpiše sporočilo, da oznaka finetune_compute_allow_list ni del oznak modela.

    - Skratka, skripta preverja specifično oznako v metapodatkih modela, pretvori vrednost oznake v seznam, če obstaja, in ustrezno obvesti uporabnika.

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

### Preverjanje računalniškega primera

1. Ta Python skripta komunicira z Azure Machine Learning (Azure ML) storitvijo in izvaja več preverjanj na računalniškem primeru. Tukaj je povzetek, kaj počne:

    - Poskuša pridobiti računalniški primer z imenom, shranjenim v compute_cluster, iz Azure ML delovnega prostora. Če je stanje priprave računalniškega primera "failed", sproži ValueError.

    - Preveri, ali je computes_allow_list različen od None. Če je, pretvori vse velikosti računalnikov na seznamu v male črke in preveri, ali je velikost trenutnega računalniškega primera na seznamu. Če ni, sproži ValueError.

    - Če je computes_allow_list None, preveri, ali je velikost računalniškega primera na seznamu nepodprtih velikosti GPU VM-jev. Če je, sproži ValueError.

    - Pridobi seznam vseh razpoložljivih velikosti računalnikov v delovnem prostoru. Nato za vsako velikost preveri, ali se ime ujema z velikostjo trenutnega računalniškega primera. Če se, pridobi število GPU-jev za to velikost in nastavi gpu_count_found na True.

    - Če je gpu_count_found True, izpiše število GPU-jev v računalniškem primeru. Če ni, sproži ValueError.

    - Skratka, skripta izvaja več preverjanj računalniškega primera v Azure ML delovnem prostoru, vključno s preverjanjem stanja priprave, velikosti glede na dovoljen seznam ali seznam prepovedi ter številom GPU-jev.

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

## 4. Izberite podatkovno zbirko za fino nastavitev modela

1. Uporabljamo podatkovno zbirko ultrachat_200k. Podatkovna zbirka ima štiri razdelke, primerne za nadzorovano fino nastavitev (sft).
Generacijsko razvrščanje (gen). Število primerov na razdelek je prikazano spodaj:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Naslednje celice prikazujejo osnovno pripravo podatkov za fino nastavitev:

### Vizualizacija nekaj vrstic podatkov

Želimo, da ta vzorec teče hitro, zato shranimo datoteki train_sft in test_sft, ki vsebujeta 5 % že obrezanih vrstic. To pomeni, da bo fino nastavljeni model imel nižjo natančnost, zato ga ne smemo uporabljati v resničnem svetu.
download-dataset.py se uporablja za prenos podatkovne zbirke ultrachat_200k in pretvorbo podatkov v format, ki ga lahko porabi komponenta pipeline za fino nastavitev. Ker je podatkovna zbirka velika, imamo tukaj le del podatkov.

1. Zagon spodnjega skripta prenese le 5 % podatkov. To lahko povečate z nastavitvijo parametra dataset_split_pc na želen odstotek.

    > [!NOTE]
    > Nekateri jezikovni modeli imajo različne jezikovne kode, zato naj imena stolpcev v podatkovni zbirki temu ustrezajo.

1. Tukaj je primer, kako naj bi podatki izgledali
Podatkovna zbirka za dokončanje pogovora je shranjena v formatu parquet, pri čemer ima vsak zapis naslednjo shemo:

    - To je JSON (JavaScript Object Notation) dokument, priljubljen format za izmenjavo podatkov. Ni izvršljiva koda, ampak način shranjevanja in prenosa podatkov. Tukaj je razčlenitev strukture:

    - "prompt": Ta ključ vsebuje niz, ki predstavlja nalogo ali vprašanje, naslovljeno na AI asistenta.

    - "messages": Ta ključ vsebuje seznam objektov. Vsak objekt predstavlja sporočilo v pogovoru med uporabnikom in AI asistentom. Vsako sporočilo ima dva ključa:

    - "content": Ta ključ vsebuje niz, ki predstavlja vsebino sporočila.
    - "role": Ta ključ vsebuje niz, ki predstavlja vlogo entitete, ki je poslala sporočilo. Lahko je "user" ali "assistant".
    - "prompt_id": Ta ključ vsebuje niz, ki predstavlja edinstveni identifikator za prompt.

1. V tem specifičnem JSON dokumentu je predstavljen pogovor, kjer uporabnik prosi AI asistenta, naj ustvari protagonistko za distopijsko zgodbo. Asistent odgovori, nato uporabnik zahteva več podrobnosti. Asistent se strinja, da jih bo podal. Celoten pogovor je povezan z določenim ID-jem prompta.

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

### Prenos podatkov

1. Ta Python skripta se uporablja za prenos podatkovne zbirke z uporabo pomožne skripte download-dataset.py. Tukaj je povzetek, kaj počne:

    - Uvozi modul os, ki omogoča prenosljiv dostop do funkcionalnosti operacijskega sistema.

    - Uporabi funkcijo os.system za zagon skripte download-dataset.py v lupini z določenimi argumenti ukazne vrstice. Argumenti določajo podatkovno zbirko za prenos (HuggingFaceH4/ultrachat_200k), imenik za prenos (ultrachat_200k_dataset) in odstotek razdelitve podatkov (5). Funkcija os.system vrne izhodni status ukaza, ki se shrani v spremenljivko exit_status.

    - Preveri, ali exit_status ni 0. V operacijskih sistemih, podobnih Unixu, status 0 običajno pomeni uspeh, druga številka pa napako. Če exit_status ni 0, sproži izjemo z sporočilom o napaki pri prenosu podatkov.

    - Skratka, skripta zažene ukaz za prenos podatkov z uporabo pomožne skripte in sproži izjemo, če ukaz ne uspe.

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

### Nalaganje podatkov v DataFrame

1. Ta Python skripta nalaga datoteko JSON Lines v pandas DataFrame in prikaže prvih 5 vrstic. Tukaj je povzetek, kaj počne:

    - Uvozi knjižnico pandas, ki je zmogljiva za manipulacijo in analizo podatkov.

    - Nastavi največjo širino stolpca za prikaz v pandas na 0. To pomeni, da bo ob izpisu DataFrame prikazan celoten tekst vsakega stolpca brez skrajšav.

    - Uporabi funkcijo pd.read_json za nalaganje datoteke train_sft.jsonl iz imenika ultrachat_200k_dataset v DataFrame. Argument lines=True pomeni, da je datoteka v formatu JSON Lines, kjer je vsak vrstica ločen JSON objekt.
- Uporablja metodo head za prikaz prvih 5 vrstic DataFrame-a. Če ima DataFrame manj kot 5 vrstic, bo prikazal vse.

- Na kratko, ta skripta naloži datoteko JSON Lines v DataFrame in prikaže prvih 5 vrstic s celotnim besedilom stolpcev.

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

## 5. Pošljite nalogo za fino nastavitev z modelom in podatki kot vhodoma

Ustvarite nalogo, ki uporablja komponento pipeline za chat-completion. Več o vseh podprtih parametrih za fino nastavitev.

### Določite parametre fino nastavitve

1. Parametre fino nastavitve lahko razdelimo v 2 kategoriji - parametri učenja in parametri optimizacije

1. Parametri učenja določajo vidike učenja, kot so -

    - Optimizator, načrtovalnik, ki ga uporabljamo
    - Metrična vrednost, ki jo optimiziramo pri fino nastavitvi
    - Število učnih korakov, velikost serije in podobno
    - Parametri optimizacije pomagajo pri optimizaciji pomnilnika GPU in učinkoviti uporabi računalniških virov.

1. Spodaj je nekaj parametrov, ki spadajo v to kategorijo. Parametri optimizacije se razlikujejo za vsak model in so vključeni z modelom, da obvladajo te razlike.

    - Omogoči deepspeed in LoRA
    - Omogoči učenje z mešano natančnostjo
    - Omogoči učenje na več vozliščih


> [!NOTE]
> Nadzorovana fino nastavitev lahko povzroči izgubo usklajenosti ali katastrofalno pozabo. Priporočamo, da preverite to težavo in izvedete fazo usklajevanja po fino nastavitvi.

### Parametri fino nastavitve

1. Ta Python skripta nastavlja parametre za fino nastavitev modela strojnega učenja. Tukaj je razčlenitev, kaj počne:

    - Nastavi privzete parametre učenja, kot so število učnih epoh, velikosti serij za učenje in ocenjevanje, hitrost učenja in tip načrtovalnika hitrosti učenja.

    - Nastavi privzete parametre optimizacije, kot so uporaba Layer-wise Relevance Propagation (LoRa) in DeepSpeed ter stopnja DeepSpeed.

    - Združi parametre učenja in optimizacije v en sam slovar z imenom finetune_parameters.

    - Preveri, ali ima foundation_model kakšne model-specifične privzete parametre. Če jih ima, izpiše opozorilo in posodobi slovar finetune_parameters s temi model-specifičnimi privzetimi vrednostmi. Funkcija ast.literal_eval se uporablja za pretvorbo model-specifičnih privzetih vrednosti iz niza v Python slovar.

    - Izpiše končni nabor parametrov za fino nastavitev, ki bodo uporabljeni pri izvajanju.

    - Na kratko, ta skripta nastavlja in prikazuje parametre za fino nastavitev modela strojnega učenja, z možnostjo preglasitve privzetih parametrov z model-specifičnimi.

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

### Učna pipeline

1. Ta Python skripta definira funkcijo za generiranje prikaznega imena učne pipeline in nato pokliče to funkcijo za generiranje in izpis prikaznega imena. Tukaj je razčlenitev, kaj počne:

1. Definirana je funkcija get_pipeline_display_name. Ta funkcija generira prikazno ime na podlagi različnih parametrov, povezanih z učno pipeline.

1. Znotraj funkcije izračuna skupno velikost serije tako, da pomnoži velikost serije na napravo, število korakov akumulacije gradienta, število GPU-jev na vozlišče in število vozlišč, uporabljenih za fino nastavitev.

1. Pridobi različne druge parametre, kot so tip načrtovalnika hitrosti učenja, ali je uporabljen DeepSpeed, stopnja DeepSpeed, ali je uporabljena Layer-wise Relevance Propagation (LoRa), omejitev števila shranjenih kontrolnih točk modela in največja dolžina zaporedja.

1. Sestavi niz, ki vključuje vse te parametre, ločene s pomišljaji. Če je uporabljen DeepSpeed ali LoRa, niz vključuje "ds" s stopnjo DeepSpeed ali "lora". Če ne, vključuje "nods" ali "nolora".

1. Funkcija vrne ta niz, ki služi kot prikazno ime učne pipeline.

1. Po definiciji funkcije jo pokliče za generiranje prikaznega imena, ki se nato izpiše.

1. Na kratko, ta skripta generira prikazno ime učne pipeline za strojno učenje na podlagi različnih parametrov in ga nato izpiše.

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

### Konfiguracija pipeline

Ta Python skripta definira in konfigurira pipeline za strojno učenje z uporabo Azure Machine Learning SDK. Tukaj je razčlenitev, kaj počne:

1. Uvozi potrebne module iz Azure AI ML SDK.

1. Pridobi komponento pipeline z imenom "chat_completion_pipeline" iz registra.

1. Definira pipeline nalogo z dekoratorjem `@pipeline` in funkcijo `create_pipeline`. Ime pipeline je nastavljeno na `pipeline_display_name`.

1. Znotraj funkcije `create_pipeline` inicializira pridobljeno komponento pipeline z različnimi parametri, vključno s potjo do modela, računalniškimi grozdi za različne faze, razdelki podatkov za učenje in testiranje, številom GPU-jev za fino nastavitev in drugimi parametri fino nastavitve.

1. Poveže izhod naloge fino nastavitve z izhodom pipeline naloge. To omogoča enostavno registracijo fino nastavljenega modela, kar je potrebno za nameščanje modela na spletni ali serijski konektor.

1. Ustvari instanco pipeline z klicem funkcije `create_pipeline`.

1. Nastavi nastavitev `force_rerun` pipeline na `True`, kar pomeni, da se ne bodo uporabljali predpomnjeni rezultati prejšnjih nalog.

1. Nastavi nastavitev `continue_on_step_failure` pipeline na `False`, kar pomeni, da se pipeline ustavi, če katerikoli korak ne uspe.

1. Na kratko, ta skripta definira in konfigurira pipeline za strojno učenje za nalogo chat completion z uporabo Azure Machine Learning SDK.

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

### Pošljite nalogo

1. Ta Python skripta pošilja nalogo pipeline za strojno učenje v Azure Machine Learning delovno okolje in nato čaka, da se naloga zaključi. Tukaj je razčlenitev, kaj počne:

    - Pokliče metodo create_or_update objekta jobs v workspace_ml_client za pošiljanje pipeline naloge. Pipeline, ki se izvaja, je določen z pipeline_object, eksperiment, pod katerim se naloga izvaja, pa z experiment_name.

    - Nato pokliče metodo stream objekta jobs v workspace_ml_client, da počaka na zaključek pipeline naloge. Naloga, na katero čaka, je določena z atributom name objekta pipeline_job.

    - Na kratko, ta skripta pošilja pipeline nalogo za strojno učenje v Azure Machine Learning delovno okolje in nato čaka na njen zaključek.

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

## 6. Registrirajte fino nastavljeni model v delovnem okolju

Registrirali bomo model iz izhoda naloge fino nastavitve. To bo sledilo izvoru med fino nastavljenim modelom in nalogo fino nastavitve. Naloga fino nastavitve nato sledi izvoru do osnovnega modela, podatkov in učne kode.

### Registracija ML modela

1. Ta Python skripta registrira model strojnega učenja, ki je bil naučen v Azure Machine Learning pipeline. Tukaj je razčlenitev, kaj počne:

    - Uvozi potrebne module iz Azure AI ML SDK.

    - Preveri, ali je izhod trained_model na voljo iz pipeline naloge z uporabo metode get objekta jobs v workspace_ml_client in dostopom do njegovega atributa outputs.

    - Sestavi pot do naučenega modela z oblikovanjem niza z imenom pipeline naloge in imenom izhoda ("trained_model").

    - Določi ime za fino nastavljeni model tako, da originalnemu imenu modela doda "-ultrachat-200k" in nadomesti vse poševnice s pomišljaji.

    - Pripravi registracijo modela z ustvarjanjem objekta Model z različnimi parametri, vključno s potjo do modela, tipom modela (MLflow model), imenom in različico modela ter opisom modela.

    - Registrira model z uporabo metode create_or_update objekta models v workspace_ml_client z Model objektom kot argumentom.

    - Izpiše registrirani model.

1. Na kratko, ta skripta registrira model strojnega učenja, ki je bil naučen v Azure Machine Learning pipeline.

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

## 7. Namestite fino nastavljeni model na spletni konektor

Spletni konektorji zagotavljajo trajen REST API, ki ga je mogoče uporabiti za integracijo z aplikacijami, ki potrebujejo uporabo modela.

### Upravljanje konektorja

1. Ta Python skripta ustvarja upravljani spletni konektor v Azure Machine Learning za registriran model. Tukaj je razčlenitev, kaj počne:

    - Uvozi potrebne module iz Azure AI ML SDK.

    - Določi edinstveno ime za spletni konektor z dodajanjem časovnega žiga k nizu "ultrachat-completion-".

    - Pripravi ustvarjanje spletnega konektorja z ustvarjanjem objekta ManagedOnlineEndpoint z različnimi parametri, vključno z imenom konektorja, opisom in načinom avtentikacije ("key").

    - Ustvari spletni konektor z uporabo metode begin_create_or_update workspace_ml_client z objektom ManagedOnlineEndpoint kot argumentom. Nato počaka na zaključek operacije z metodo wait.

1. Na kratko, ta skripta ustvarja upravljani spletni konektor v Azure Machine Learning za registriran model.

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
> Tukaj najdete seznam SKU-jev, ki so podprti za nameščanje - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Namestitev ML modela

1. Ta Python skripta namešča registriran model strojnega učenja na upravljani spletni konektor v Azure Machine Learning. Tukaj je razčlenitev, kaj počne:

    - Uvozi modul ast, ki zagotavlja funkcije za obdelavo dreves abstraktne sintakse Pythona.

    - Nastavi tip instance za namestitev na "Standard_NC6s_v3".

    - Preveri, ali je oznaka inference_compute_allow_list prisotna v foundation modelu. Če je, pretvori vrednost oznake iz niza v Python seznam in jo dodeli spremenljivki inference_computes_allow_list. Če ni, nastavi inference_computes_allow_list na None.

    - Preveri, ali je določen tip instance na seznamu dovoljenih. Če ni, izpiše sporočilo, ki uporabnika poziva, naj izbere tip instance s seznama dovoljenih.

    - Pripravi ustvarjanje namestitve z ustvarjanjem objekta ManagedOnlineDeployment z različnimi parametri, vključno z imenom namestitve, imenom konektorja, ID-jem modela, tipom in številom instanc, nastavitvami liveness probe in nastavitvami zahtev.

    - Ustvari namestitev z uporabo metode begin_create_or_update workspace_ml_client z objektom ManagedOnlineDeployment kot argumentom. Nato počaka na zaključek operacije z metodo wait.

    - Nastavi promet konektorja tako, da 100 % prometa usmeri na namestitev "demo".

    - Posodobi konektor z uporabo metode begin_create_or_update workspace_ml_client z objektom endpoint kot argumentom. Nato počaka na zaključek posodobitve z metodo result.

1. Na kratko, ta skripta namešča registriran model strojnega učenja na upravljani spletni konektor v Azure Machine Learning.

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

## 8. Preizkusite konektor z vzorčnimi podatki

Pridobili bomo nekaj vzorčnih podatkov iz testnega nabora in jih poslali na spletni konektor za inferenco. Nato bomo prikazali ocenjene oznake skupaj z dejanskimi oznakami.

### Branje rezultatov

1. Ta Python skripta prebere datoteko JSON Lines v pandas DataFrame, vzame naključni vzorec in ponastavi indeks. Tukaj je razčlenitev, kaj počne:

    - Prebere datoteko ./ultrachat_200k_dataset/test_gen.jsonl v pandas DataFrame. Funkcija read_json se uporablja z argumentom lines=True, ker je datoteka v formatu JSON Lines, kjer je vsaka vrstica ločen JSON objekt.

    - Vzame naključni vzorec 1 vrstico iz DataFrame-a. Funkcija sample se uporablja z argumentom n=1 za določitev števila naključnih vrstic.

    - Ponastavi indeks DataFrame-a. Funkcija reset_index se uporablja z argumentom drop=True, da odstrani originalni indeks in ga nadomesti z novim indeksom s privzetimi celimi števili.

    - Prikaže prvih 2 vrstici DataFrame-a z uporabo funkcije head z argumentom 2. Ker pa DataFrame vsebuje le eno vrstico po vzorčenju, bo prikazal samo to eno vrstico.

1. Na kratko, ta skripta prebere datoteko JSON Lines v pandas DataFrame, vzame naključni vzorec ene vrstice, ponastavi indeks in prikaže prvo vrstico.

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

### Ustvarjanje JSON objekta

1. Ta Python skripta ustvarja JSON objekt z določenimi parametri in ga shrani v datoteko. Tukaj je razčlenitev, kaj počne:

    - Uvozi modul json, ki zagotavlja funkcije za delo z JSON podatki.

    - Ustvari slovar parameters s ključi in vrednostmi, ki predstavljajo parametre za model strojnega učenja. Ključi so "temperature", "top_p", "do_sample" in "max_new_tokens", njihove ustrezne vrednosti pa so 0.6, 0.9, True in 200.

    - Ustvari še en slovar test_json z dvema ključema: "input_data" in "params". Vrednost "input_data" je drug slovar s ključi "input_string" in "parameters". Vrednost "input_string" je seznam, ki vsebuje prvo sporočilo iz DataFrame-a test_df. Vrednost "parameters" je prej ustvarjeni slovar parameters. Vrednost "params" je prazen slovar.
- Odpre datoteko z imenom sample_score.json

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

### Klicanje končne točke

1. Ta Python skripta kliče spletno končno točko v Azure Machine Learning za ocenjevanje JSON datoteke. Tukaj je razlaga, kaj počne:

    - Pokliče metodo invoke lastnosti online_endpoints objekta workspace_ml_client. Ta metoda se uporablja za pošiljanje zahteve spletni končni točki in pridobitev odgovora.

    - Določi ime končne točke in nameščene različice z argumentoma endpoint_name in deployment_name. V tem primeru je ime končne točke shranjeno v spremenljivki online_endpoint_name, ime nameščene različice pa je "demo".

    - Določi pot do JSON datoteke, ki jo je treba oceniti, z argumentom request_file. V tem primeru je datoteka ./ultrachat_200k_dataset/sample_score.json.

    - Shranjuje odgovor končne točke v spremenljivko response.

    - Izpiše surovi odgovor.

1. Povzetek: ta skripta kliče spletno končno točko v Azure Machine Learning za ocenjevanje JSON datoteke in izpiše odgovor.

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

## 9. Brisanje spletne končne točke

1. Ne pozabite izbrisati spletne končne točke, sicer boste pustili merilnik obračunavanja vklopljen za računske vire, ki jih uporablja končna točka. Ta vrstica Python kode briše spletno končno točko v Azure Machine Learning. Tukaj je razlaga, kaj počne:

    - Pokliče metodo begin_delete lastnosti online_endpoints objekta workspace_ml_client. Ta metoda začne postopek brisanja spletne končne točke.

    - Določi ime končne točke, ki jo je treba izbrisati, z argumentom name. V tem primeru je ime končne točke shranjeno v spremenljivki online_endpoint_name.

    - Pokliče metodo wait, da počaka na dokončanje postopka brisanja. To je blokirajoča operacija, kar pomeni, da skripta ne bo nadaljevala, dokler brisanje ni končano.

    - Povzetek: ta vrstica kode začne brisanje spletne končne točke v Azure Machine Learning in počaka, da se operacija zaključi.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.