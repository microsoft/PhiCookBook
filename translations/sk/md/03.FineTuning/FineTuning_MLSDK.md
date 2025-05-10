<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-09T21:33:16+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "sk"
}
-->
## Ako používať chat-completion komponenty zo systému Azure ML registry na doladenie modelu

V tomto príklade budeme doladiť model Phi-3-mini-4k-instruct, aby dokončil konverzáciu medzi 2 osobami pomocou datasetu ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.sk.png)

Príklad vám ukáže, ako vykonať doladenie pomocou Azure ML SDK a Pythonu, a následne nasadiť doladený model na online endpoint pre inferenciu v reálnom čase.

### Tréningové dáta

Použijeme dataset ultrachat_200k. Ide o výrazne filtrovanú verziu UltraChat datasetu, ktorý sa použil na trénovanie modelu Zephyr-7B-β, špičkového 7b chat modelu.

### Model

Použijeme model Phi-3-mini-4k-instruct, aby sme ukázali, ako si používateľ môže doladiť model pre úlohu chat-completion. Ak ste otvorili tento notebook zo špecifickej modelovej karty, nezabudnite nahradiť názov modelu.

### Úlohy

- Vybrať model na doladenie.
- Vybrať a preskúmať tréningové dáta.
- Nakonfigurovať doladenie.
- Spustiť doladenie.
- Skontrolovať tréningové a evaluačné metriky.
- Zaregistrovať doladený model.
- Nasadiť doladený model pre inferenciu v reálnom čase.
- Vyčistiť zdroje.

## 1. Nastavenie predpokladov

- Nainštalovať závislosti
- Pripojiť sa k AzureML Workspace. Viac informácií nájdete v nastavení autentifikácie SDK. Nahradiť <WORKSPACE_NAME>, <RESOURCE_GROUP> a <SUBSCRIPTION_ID> nižšie.
- Pripojiť sa k azureml systémovému registru
- Nastaviť voliteľný názov experimentu
- Skontrolovať alebo vytvoriť výpočtové prostredie.

> [!NOTE]
> Požiadavky: jeden GPU uzol môže mať viac GPU kariet. Napríklad, uzol Standard_NC24rs_v3 má 4 NVIDIA V100 GPU, zatiaľ čo Standard_NC12s_v3 má 2 NVIDIA V100 GPU. Podrobnosti nájdete v dokumentácii. Počet GPU kariet na uzol sa nastavuje v parametri gpus_per_node nižšie. Správne nastavenie zabezpečí využitie všetkých GPU v uzle. Odporúčané GPU compute SKU nájdete tu a tu.

### Python knižnice

Nainštalujte závislosti spustením nasledujúcej bunky. Tento krok nie je voliteľný, ak bežíte v novom prostredí.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interakcia s Azure ML

1. Tento Python skript slúži na interakciu so službou Azure Machine Learning (Azure ML). Tu je rozpis, čo robí:

    - Importuje potrebné moduly z balíkov azure.ai.ml, azure.identity a azure.ai.ml.entities. Tiež importuje modul time.

    - Pokúša sa autentifikovať pomocou DefaultAzureCredential(), ktorý zjednodušuje autentifikáciu pre rýchly vývoj aplikácií bežiacich v Azure cloude. Ak to zlyhá, použije InteractiveBrowserCredential(), ktorý zobrazí interaktívne prihlasovacie okno.

    - Pokúša sa vytvoriť inštanciu MLClient pomocou from_config metódy, ktorá číta konfiguráciu z predvoleného konfiguračného súboru (config.json). Ak to zlyhá, vytvorí MLClient manuálnym poskytnutím subscription_id, resource_group_name a workspace_name.

    - Vytvorí ďalšiu inštanciu MLClient, tentokrát pre Azure ML register s názvom "azureml". Tento register uchováva modely, doladenia a prostredia.

    - Nastaví experiment_name na "chat_completion_Phi-3-mini-4k-instruct".

    - Vygeneruje jedinečný timestamp konverziou aktuálneho času (v sekundách od epochy, ako float) na celé číslo a potom na reťazec. Tento timestamp sa môže použiť na vytváranie jedinečných mien a verzií.

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

## 2. Výber základného modelu na doladenie

1. Phi-3-mini-4k-instruct je model s 3,8 miliardami parametrov, ľahký, špičkový open model postavený na dátach použitých pre Phi-2. Model patrí do rodiny Phi-3 a Mini verzia prichádza v dvoch variantoch 4K a 128K, čo je dĺžka kontextu (v tokenoch), ktorú môže podporovať. Model je potrebné doladiť pre náš konkrétny účel. Tieto modely si môžete prezrieť v Model Catalog v AzureML Studiu, filtrovaním podľa úlohy chat-completion. V tomto príklade používame model Phi-3-mini-4k-instruct. Ak ste otvorili tento notebook pre iný model, nahraďte názov modelu a verziu.

    > [!NOTE]
    > id modelu je vlastnosť modelu. Táto hodnota sa odovzdáva ako vstup do doladenia. Je tiež dostupná ako Asset ID na stránke detailov modelu v AzureML Studio Model Catalog.

2. Tento Python skript komunikuje so službou Azure Machine Learning (Azure ML). Tu je, čo robí:

    - Nastaví model_name na "Phi-3-mini-4k-instruct".

    - Použije metódu get z vlastnosti models objektu registry_ml_client na získanie najnovšej verzie modelu s daným názvom z Azure ML registra. Metóda get sa volá s dvoma argumentmi: názvom modelu a štítkom, ktorý určuje, že má byť získaná najnovšia verzia modelu.

    - Vypíše správu do konzoly s názvom, verziou a id modelu, ktorý sa použije na doladenie. Na formátovanie správy sa používa metóda format reťazca. Názov, verzia a id modelu sa získavajú ako vlastnosti objektu foundation_model.

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

## 3. Vytvorenie výpočtového prostredia pre job

Doladenie funguje IBA s GPU výpočtom. Veľkosť výpočtu závisí od veľkosti modelu a často je ťažké vybrať správny výpočet pre job. V tejto bunke pomáhame používateľovi vybrať správny výpočet.

> [!NOTE]
> Nižšie uvedené výpočty fungujú s najoptimalizovanejšou konfiguráciou. Akékoľvek zmeny môžu spôsobiť chybu Cuda Out Of Memory. V takom prípade skúste upgradovať výpočet na väčší.

> [!NOTE]
> Pri výbere compute_cluster_size nižšie sa uistite, že výpočet je dostupný vo vašej resource group. Ak nie je, môžete požiadať o prístup k výpočtovým zdrojom.

### Kontrola podpory doladenia modelu

1. Tento Python skript komunikuje s modelom Azure Machine Learning (Azure ML). Tu je, čo robí:

    - Importuje modul ast, ktorý poskytuje funkcie na spracovanie stromov Python abstraktnej syntaxe.

    - Kontroluje, či objekt foundation_model (reprezentujúci model v Azure ML) obsahuje tag s názvom finetune_compute_allow_list. Tagy v Azure ML sú kľúč-hodnota páry, ktoré môžete vytvárať a používať na filtrovanie a triedenie modelov.

    - Ak tag finetune_compute_allow_list existuje, použije ast.literal_eval na bezpečné parsovanie hodnoty tagu (reťazec) do Python zoznamu. Tento zoznam priradí premennej computes_allow_list a vypíše správu, že by sa mal vytvoriť výpočet z tohto zoznamu.

    - Ak tag neexistuje, nastaví computes_allow_list na None a vypíše správu, že tag nie je súčasťou tagov modelu.

    - Skript teda kontroluje špecifický tag v metadátach modelu, konvertuje jeho hodnotu na zoznam, ak existuje, a poskytuje používateľovi spätnú väzbu.

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

### Kontrola výpočtovej inštancie

1. Tento Python skript komunikuje so službou Azure Machine Learning (Azure ML) a vykonáva viaceré kontroly na výpočtovej inštancii. Tu je, čo robí:

    - Pokúša sa získať výpočtovú inštanciu s názvom uloženým v premennej compute_cluster z Azure ML workspace. Ak je stav provisioning "failed", vyvolá ValueError.

    - Kontroluje, či computes_allow_list nie je None. Ak nie je, prevedie všetky veľkosti výpočtu v zozname na malé písmená a skontroluje, či veľkosť aktuálnej výpočtovej inštancie je v zozname. Ak nie je, vyvolá ValueError.

    - Ak computes_allow_list je None, skontroluje, či veľkosť výpočtovej inštancie je v zozname nepodporovaných GPU VM veľkostí. Ak áno, vyvolá ValueError.

    - Získa zoznam všetkých dostupných veľkostí výpočtov v workspace. Pre každú veľkosť skontroluje, či sa jej názov zhoduje s veľkosťou aktuálnej inštancie. Ak áno, získa počet GPU pre túto veľkosť a nastaví gpu_count_found na True.

    - Ak je gpu_count_found True, vypíše počet GPU vo výpočtovej inštancii. Ak nie, vyvolá ValueError.

    - Skript teda vykonáva viaceré kontroly na výpočtovej inštancii v Azure ML workspace, vrátane stavu provisioning, veľkosti podľa povoleného alebo zakázaného zoznamu a počtu GPU.

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

## 4. Výber datasetu pre doladenie modelu

1. Používame dataset ultrachat_200k. Dataset má štyri časti, vhodné pre Supervised fine-tuning (sft). Generation ranking (gen). Počet príkladov v jednotlivých častiach je nasledovný:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Nasledujúce bunky ukazujú základnú prípravu dát pre doladenie:

### Vizualizácia niektorých riadkov dát

Chceme, aby tento príklad bežal rýchlo, preto uložíme train_sft, test_sft súbory obsahujúce 5 % už orezaných riadkov. To znamená, že doladený model bude menej presný, preto by sa nemal používať v reálnom svete.  
download-dataset.py sa používa na stiahnutie datasetu ultrachat_200k a transformáciu datasetu do formátu použiteľného v doladení. Keďže dataset je veľký, tu máme len časť datasetu.

1. Spustením nasledujúceho skriptu sa stiahne len 5 % dát. Toto môžete zvýšiť zmenou parametra dataset_split_pc na požadované percento.

    > [!NOTE]
    > Niektoré jazykové modely majú rôzne jazykové kódy, preto by názvy stĺpcov v datasete mali zodpovedať týmto kódom.

1. Tu je príklad, ako by mali dáta vyzerať:  
Dataset chat-completion je uložený vo formáte parquet, pričom každý záznam má nasledujúcu schému:

    - Ide o JSON (JavaScript Object Notation) dokument, populárny formát na výmenu dát. Nie je to vykonateľný kód, ale spôsob ukladania a prenosu dát. Tu je rozpis jeho štruktúry:

    - "prompt": tento kľúč obsahuje reťazec, ktorý predstavuje úlohu alebo otázku pre AI asistenta.

    - "messages": tento kľúč obsahuje pole objektov. Každý objekt predstavuje správu v konverzácii medzi používateľom a AI asistentom. Každá správa má dva kľúče:

    - "content": reťazec predstavujúci obsah správy.
    - "role": reťazec predstavujúci rolu entity, ktorá správu poslala. Môže byť "user" alebo "assistant".
    - "prompt_id": reťazec predstavujúci jedinečný identifikátor promptu.

1. V tomto konkrétnom JSON dokumente je znázornená konverzácia, kde používateľ žiada AI asistenta, aby vytvoril protagonistu pre dystopický príbeh. Asistent odpovedá, používateľ žiada o viac detailov a asistent súhlasí ich poskytnúť. Celá konverzácia je priradená ku konkrétnemu prompt_id.

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

### Sťahovanie dát

1. Tento Python skript slúži na stiahnutie datasetu pomocou pomocného skriptu download-dataset.py. Tu je, čo robí:

    - Importuje modul os, ktorý poskytuje prenositeľné funkcie závislé od operačného systému.

    - Používa os.system na spustenie skriptu download-dataset.py v shelli s konkrétnymi argumentmi príkazového riadku. Argumenty určujú dataset na stiahnutie (HuggingFaceH4/ultrachat_200k), adresár na uloženie (ultrachat_200k_dataset) a percento rozdelenia datasetu (5). Funkcia os.system vráti stav ukončenia príkazu, ktorý sa uloží do premennej exit_status.

    - Kontroluje, či exit_status nie je 0. V Unix-like systémoch stav 0 znamená úspech, iné číslo chybu. Ak exit_status nie je 0, vyvolá výnimku s chybovou správou o chybe pri sťahovaní datasetu.

    - Skript teda spúšťa príkaz na stiahnutie datasetu pomocou pomocného skriptu a vyvolá výnimku, ak príkaz zlyhá.

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

### Načítanie dát do DataFrame

1. Tento Python skript načítava JSON Lines súbor do pandas DataFrame a zobrazuje prvých 5 riadkov. Tu je, čo robí:

    - Importuje knižnicu pandas, ktorá je výkonným nástrojom na manipuláciu a analýzu dát.

    - Nastaví maximálnu šírku stĺpca v pandas na 0, čo znamená, že sa zobrazí celý text stĺpca bez skrátenia.

    - Použije pd.read_json na načítanie train_sft.jsonl zo zložky ultrachat_200k_dataset do DataFrame. Argument lines=True znamená, že súbor je vo formáte JSON Lines, kde každý riadok je samostatný JSON objekt.

    - Použije metódu head na zobrazenie prvých 5 riadkov DataFrame. Ak je menej než 5 riadkov, zobrazia sa všetky.

    - Skript teda načíta JSON Lines súbor do DataFrame a zobrazí prvých 5 riadkov s plným textom stĺpcov.

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

## 5. Odoslanie jobu na doladenie s použitím modelu a dát ako vstupov

Vytvorte job, ktorý používa chat-completion pipeline komponent. Viac o parametroch podporovaných pri doladení.

### Definovanie parametrov doladenia

1. Parametre doladenia možno rozdeliť do 2 kategórií - tréningové parametre, optimalizačné parametre.

1. Tréningové parametre definujú aspekty tréningu ako:

    - Optimizer, scheduler, ktoré sa použijú
    - Metriku, ktorú chceme optimalizovať pri doladení
    - Počet tréningových krokov, veľkosť batchu a podobne
    - Optimalizačné parametre pomáhajú optimalizovať GPU pamäť a efektívne využívať výpočtové zdroje.

1. Nižšie sú uvedené niektoré z parametrov tejto kategórie. Optimalizačné parametre sa líšia pre každý model a sú zabalené s modelom, aby sa tieto variácie zvládli.

    - Povoliť deepspeed a LoRA
    - Povoliť trénovanie s miešanou presnosťou
    - Povoliť multi-node trénovanie

> [!NOTE]
> Supervised doladenie môže viesť k strate zarovnania alebo katastrofickému zabudnutiu. Odporúčame toto skontrolovať a po doladení spustiť fázu zarovnania.

### Parametre doladenia

1. Tento Python skript nastavuje parametre pre doladenie modelu strojového učenia. Tu je, čo robí:  
- Nastavuje predvolené tréningové parametre ako počet epoch, veľkosti batchov pre tréning a evaluáciu, learning rate a typ scheduleru.  
- Nastavuje predvolené optimalizačné parametre ako použitie LoRa a DeepSpeed, a stupeň DeepSpeed.  
- Kombinuje tréningové a optimalizačné parametre do jedného slovníka finetune_parameters.  
- Kontroluje, či foundation_model má nejaké modelovo špecifické predvolené param
training pipeline založený na rôznych parametroch, a potom vypisovanie tohto zobrazovaného mena. ```python
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

### Konfigurácia pipeline

Tento Python skript definuje a konfiguruje pipeline strojového učenia pomocou Azure Machine Learning SDK. Tu je rozpis toho, čo robí:

1. Importuje potrebné moduly z Azure AI ML SDK.
2. Získava komponent pipeline s názvom "chat_completion_pipeline" z registra.
3. Definuje pipeline job pomocou `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, čo znamená, že pipeline sa zastaví, ak niektorý krok zlyhá.
4. Zhrnutie: tento skript definuje a konfiguruje pipeline strojového učenia pre úlohu dokončenia chatu pomocou Azure Machine Learning SDK.

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

### Odoslanie jobu

1. Tento Python skript odosiela pipeline job strojového učenia do Azure Machine Learning workspace a potom čaká na dokončenie jobu. Tu je rozpis toho, čo robí:

- Volá metódu create_or_update objektu jobs v workspace_ml_client na odoslanie pipeline jobu. Pipeline, ktorá sa má spustiť, je určená pomocou pipeline_object a experiment, pod ktorým sa job spúšťa, je určený pomocou experiment_name.
- Potom volá metódu stream objektu jobs v workspace_ml_client, aby počkal na dokončenie pipeline jobu. Job, na ktorý sa čaká, je určený atribútom name objektu pipeline_job.
- Zhrnutie: tento skript odosiela pipeline job strojového učenia do Azure Machine Learning workspace a čaká na jeho dokončenie.

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

## 6. Registrácia doladeného modelu do workspace

Zaregistrujeme model z výstupu doladenia. Toto bude sledovať väzbu medzi doladeným modelom a doladiacim jobom. Doladiaci job ďalej sleduje väzbu na základný model, dáta a tréningový kód.

### Registrácia ML modelu

1. Tento Python skript registruje model strojového učenia, ktorý bol natrénovaný v Azure Machine Learning pipeline. Tu je rozpis toho, čo robí:

- Importuje potrebné moduly z Azure AI ML SDK.
- Kontroluje, či je výstup trained_model dostupný z pipeline jobu pomocou metódy get objektu jobs v workspace_ml_client a prístupu k jeho outputs atribútu.
- Vytvára cestu k trénovanému modelu formátovaním reťazca s názvom pipeline jobu a názvom výstupu ("trained_model").
- Definuje názov pre doladený model pridaním "-ultrachat-200k" k pôvodnému názvu modelu a nahradí všetky lomky pomlčkami.
- Pripravuje registráciu modelu vytvorením objektu Model s rôznymi parametrami vrátane cesty k modelu, typu modelu (MLflow model), názvu a verzie modelu a popisu modelu.
- Registruje model volaním metódy create_or_update objektu models v workspace_ml_client s objektom Model ako argumentom.
- Vypisuje registrovaný model.

1. Zhrnutie: tento skript registruje model strojového učenia, ktorý bol natrénovaný v Azure Machine Learning pipeline.

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

## 7. Nasadenie doladeného modelu na online endpoint

Online endpointy poskytujú trvalé REST API, ktoré sa dá použiť na integráciu s aplikáciami, ktoré potrebujú model používať.

### Správa endpointu

1. Tento Python skript vytvára spravovaný online endpoint v Azure Machine Learning pre registrovaný model. Tu je rozpis toho, čo robí:

- Importuje potrebné moduly z Azure AI ML SDK.
- Definuje jedinečný názov pre online endpoint pridaním časovej značky k reťazcu "ultrachat-completion-".
- Pripravuje vytvorenie online endpointu vytvorením objektu ManagedOnlineEndpoint s rôznymi parametrami, vrátane názvu endpointu, popisu a režimu autentifikácie ("key").
- Vytvára online endpoint volaním metódy begin_create_or_update workspace_ml_client s objektom ManagedOnlineEndpoint ako argumentom. Potom čaká na dokončenie operácie volaním metódy wait.

1. Zhrnutie: tento skript vytvára spravovaný online endpoint v Azure Machine Learning pre registrovaný model.

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
> Tu nájdete zoznam SKU podporovaných pre nasadenie - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Nasadenie ML modelu

1. Tento Python skript nasadzuje registrovaný model strojového učenia na spravovaný online endpoint v Azure Machine Learning. Tu je rozpis toho, čo robí:

- Importuje modul ast, ktorý poskytuje funkcie na spracovanie stromov Python abstraktnej syntaxe.
- Nastavuje typ inštancie pre nasadenie na "Standard_NC6s_v3".
- Kontroluje, či tag inference_compute_allow_list existuje v základnom modeli. Ak áno, konvertuje hodnotu tagu zo stringu na Python zoznam a priradí ho do inference_computes_allow_list. Ak nie, nastaví inference_computes_allow_list na None.
- Kontroluje, či je zadaný typ inštancie v zozname povolených. Ak nie je, vypíše správu, aby používateľ vybral typ inštancie zo zoznamu povolených.
- Pripravuje vytvorenie nasadenia vytvorením objektu ManagedOnlineDeployment s rôznymi parametrami, vrátane názvu nasadenia, názvu endpointu, ID modelu, typu a počtu inštancií, nastavení liveness probe a request settings.
- Vytvára nasadenie volaním metódy begin_create_or_update workspace_ml_client s objektom ManagedOnlineDeployment ako argumentom. Potom čaká na dokončenie operácie volaním metódy wait.
- Nastavuje traffic endpointu tak, aby 100 % trafficu smeroval na nasadenie "demo".
- Aktualizuje endpoint volaním metódy begin_create_or_update workspace_ml_client s endpoint objektom ako argumentom. Potom čaká na dokončenie aktualizácie volaním metódy result.

1. Zhrnutie: tento skript nasadzuje registrovaný model strojového učenia na spravovaný online endpoint v Azure Machine Learning.

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

## 8. Testovanie endpointu s ukážkovými dátami

Získame niekoľko ukážkových dát z testovacej množiny a odošleme ich na online endpoint na inferenciu. Následne zobrazíme skórované štítky spolu s referenčnými štítkami.

### Čítanie výsledkov

1. Tento Python skript načítava JSON Lines súbor do pandas DataFrame, vyberie náhodný vzorok a resetuje index. Tu je rozpis toho, čo robí:

- Načíta súbor ./ultrachat_200k_dataset/test_gen.jsonl do pandas DataFrame. Funkcia read_json sa používa s argumentom lines=True, pretože súbor je vo formáte JSON Lines, kde každý riadok je samostatný JSON objekt.
- Vyberie náhodný vzorok 1 riadku z DataFrame. Funkcia sample sa používa s argumentom n=1 na určenie počtu náhodných riadkov.
- Resetuje index DataFrame. Funkcia reset_index sa používa s argumentom drop=True, aby sa pôvodný index zahodil a nahradil novým štandardným celočíselným indexom.
- Zobrazí prvé 2 riadky DataFrame pomocou funkcie head s argumentom 2. Keďže DataFrame obsahuje len jeden riadok po vzorkovaní, zobrazí sa len tento jeden riadok.

1. Zhrnutie: tento skript načítava JSON Lines súbor do pandas DataFrame, vyberie náhodný vzorok jedného riadku, resetuje index a zobrazí prvý riadok.

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

### Vytvorenie JSON objektu

1. Tento Python skript vytvára JSON objekt so špecifickými parametrami a ukladá ho do súboru. Tu je rozpis toho, čo robí:

- Importuje modul json, ktorý poskytuje funkcie na prácu s JSON dátami.
- Vytvára slovník parameters s kľúčmi a hodnotami reprezentujúcimi parametre pre model strojového učenia. Kľúče sú "temperature", "top_p", "do_sample" a "max_new_tokens" a ich hodnoty sú 0.6, 0.9, True a 200.
- Vytvára ďalší slovník test_json so dvoma kľúčmi: "input_data" a "params". Hodnota "input_data" je ďalší slovník s kľúčmi "input_string" a "parameters". Hodnota "input_string" je zoznam obsahujúci prvú správu z DataFrame test_df. Hodnota "parameters" je slovník parameters vytvorený predtým. Hodnota "params" je prázdny slovník.
- Otvára súbor sample_score.json

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

### Volanie endpointu

1. Tento Python skript volá online endpoint v Azure Machine Learning na skórovanie JSON súboru. Tu je rozpis toho, čo robí:

- Volá metódu invoke z vlastnosti online_endpoints objektu workspace_ml_client. Táto metóda slúži na odoslanie požiadavky na online endpoint a získanie odpovede.
- Špecifikuje názov endpointu a nasadenia pomocou argumentov endpoint_name a deployment_name. V tomto prípade je názov endpointu uložený v premennej online_endpoint_name a názov nasadenia je "demo".
- Špecifikuje cestu k JSON súboru, ktorý sa má skórovať, pomocou argumentu request_file. V tomto prípade je to súbor ./ultrachat_200k_dataset/sample_score.json.
- Ukladá odpoveď z endpointu do premennej response.
- Vypisuje surovú odpoveď.

1. Zhrnutie: tento skript volá online endpoint v Azure Machine Learning na skórovanie JSON súboru a vypisuje odpoveď.

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

## 9. Vymazanie online endpointu

1. Nezabudnite vymazať online endpoint, inak vám bude bežať fakturácia za výpočtové zdroje použité endpointom. Tento riadok Python kódu vymazáva online endpoint v Azure Machine Learning. Tu je rozpis toho, čo robí:

- Volá metódu begin_delete z vlastnosti online_endpoints objektu workspace_ml_client. Táto metóda slúži na začatie vymazania online endpointu.
- Špecifikuje názov endpointu, ktorý sa má vymazať, pomocou argumentu name. V tomto prípade je názov endpointu uložený v premennej online_endpoint_name.
- Volá metódu wait, aby počkal na dokončenie vymazávacej operácie. Ide o blokujúcu operáciu, ktorá zabráni pokračovaniu skriptu, kým sa vymazanie neukončí.
- Zhrnutie: tento riadok kódu začína vymazanie online endpointu v Azure Machine Learning a čaká na dokončenie operácie.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.