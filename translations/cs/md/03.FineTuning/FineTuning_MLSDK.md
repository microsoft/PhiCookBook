## Jak používat komponenty chat-completion ze systémového registru Azure ML pro doladění modelu

V tomto příkladu provedeme doladění modelu Phi-3-mini-4k-instruct pro dokončení konverzace mezi 2 lidmi pomocí datasetu ultrachat_200k.

![MLFineTune](../../../../translated_images/cs/MLFineTune.928d4c6b3767dd35.webp)

Příklad vám ukáže, jak provést doladění pomocí Azure ML SDK a Pythonu a poté nasadit doladěný model na online endpoint pro inference v reálném čase.

### Trénovací data

Použijeme dataset ultrachat_200k. Jedná se o silně filtrovanou verzi datasetu UltraChat, který byl použit pro trénink Zephyr-7B-β, špičkového 7b chat modelu.

### Model

Použijeme model Phi-3-mini-4k-instruct, abychom ukázali, jak může uživatel doladit model pro úkol chat-completion. Pokud jste otevřeli tento notebook z konkrétního modelového záznamu, nezapomeňte vyměnit specifický název modelu.

### Úkoly

- Vybrat model k doladění.
- Vybrat a prozkoumat trénovací data.
- Nakonfigurovat úlohu doladění.
- Spustit úlohu doladění.
- Zkontrolovat trénovací a hodnoticí metriky.
- Registrovat doladěný model.
- Nasadit doladěný model pro inference v reálném čase.
- Uvolnit prostředky.

## 1. Nastavení předpokladů

- Instalace závislostí
- Připojení k AzureML Workspace. Více se dozvíte v nastavení autentifikace SDK. Nahraďte <WORKSPACE_NAME>, <RESOURCE_GROUP> a <SUBSCRIPTION_ID> níže.
- Připojení k systémovému registru azureml
- Nastavení volitelného jména experimentu
- Kontrola nebo vytvoření compute.

> [!NOTE]
> Požadavky: jeden GPU uzel může mít více GPU kart. Například v jednom uzlu Standard_NC24rs_v3 jsou 4 NVIDIA V100 GPU, zatímco v Standard_NC12s_v3 jsou 2 NVIDIA V100 GPU. Odkazy na dokumentaci k tomuto naleznete zde. Počet GPU karet na uzel je nastaven v parametru gpus_per_node níže. Správné nastavení této hodnoty zajistí využití všech GPU v uzlu. Doporučené SKU GPU výpočetních instancí najdete zde a zde.

### Python knihovny

Nainstalujte závislosti spuštěním níže uvedené buňky. Tento krok není volitelný při běhu v novém prostředí.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interakce s Azure ML

1. Tento Python skript slouží k interakci se službou Azure Machine Learning (Azure ML). Zde je rozbor, co dělá:

    - Importuje potřebné moduly z balíčků azure.ai.ml, azure.identity a azure.ai.ml.entities. Dále importuje modul time.

    - Pokouší se autentifikovat pomocí DefaultAzureCredential(), který poskytuje zjednodušený způsob autentifikace pro rychlý vývoj aplikací běžících v Azure cloudu. Pokud toto selže, přepne na InteractiveBrowserCredential(), který poskytuje interaktivní přihlašovací výzvu.

    - Poté se pokouší vytvořit instanci MLClient pomocí metody from_config, která načítá konfiguraci z výchozího konfiguračního souboru (config.json). Pokud to selže, vytvoří instanci MLClient manuálním poskytnutím subscription_id, resource_group_name a workspace_name.

    - Vytváří další instanci MLClient, tentokrát pro Azure ML registr pojmenovaný „azureml“. Tento registr slouží k uchovávání modelů, pipeline pro doladění a prostředí.

    - Nastaví experiment_name na „chat_completion_Phi-3-mini-4k-instruct“.

    - Vygeneruje jedinečný časový údaj převedením aktuálního času (v sekundách od epochy jako desetinné číslo) na celé číslo a potom na řetězec. Tento časový údaj lze použít pro vytváření jedinečných jmen a verzí.

    ```python
    # Importujte potřebné moduly z Azure ML a Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Importujte modul time
    
    # Pokuste se autentizovat pomocí DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Pokud DefaultAzureCredential selže, použijte InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Pokuste se vytvořit instanci MLClient pomocí výchozího konfiguračního souboru
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Pokud to selže, vytvořte instanci MLClient ručním zadáním detailů
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Vytvořte další instanci MLClient pro registr Azure ML nazvaný "azureml"
    # Tento registr je místo, kde jsou uloženy modely, pipelines pro doladění a prostředí
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Nastavte název experimentu
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Vygenerujte jedinečný časový razítko, které lze použít pro názvy a verze, jež musí být unikátní
    timestamp = str(int(time.time()))
    ```

## 2. Vyberte základní model k doladění

1. Phi-3-mini-4k-instruct je model s 3,8 miliardami parametrů, lehký, špičkový otevřený model postavený na datech použitých pro Phi-2. Model patří do rodiny Phi-3 a verze Mini existuje ve dvou variantách 4K a 128K, což je délka kontextu (v tokenech), kterou může podporovat. Model je třeba doladit pro náš specifický účel, aby jej bylo možné použít. Můžete si prohlédnout tyto modely v katalogu modelů v AzureML Studiu filtrováním podle úkolu chat-completion. V tomto příkladu používáme model Phi-3-mini-4k-instruct. Pokud jste otevřeli tento notebook pro jiný model, vyměňte název modelu a verzi odpovídajícím způsobem.

> [!NOTE]
> property model id modelu. Toto je předáno jako vstup do úlohy doladění. Je to také dostupné jako pole Asset ID na stránce detailů modelu v AzureML Studiu v Katalogu modelů.

2. Tento Python skript interaguje se službou Azure Machine Learning (Azure ML). Zde je rozbor, co dělá:

    - Nastaví model_name na „Phi-3-mini-4k-instruct“.

    - Používá metodu get vlastnosti models objektu registry_ml_client, aby získal nejnovější verzi modelu se specifikovaným názvem z Azure ML registru. Metoda get se volá se dvěma argumenty: názvem modelu a štítkem označujícím, že má být načtena nejnovější verze modelu.

    - Vypíše zprávu do konzole, která uvádí název, verzi a id modelu, který bude použit pro doladění. Metoda format řetězce se použije k vložení názvu, verze a id modelu do zprávy. Název, verze a id modelu jsou přístupné jako vlastnosti objektu foundation_model.

    ```python
    # Nastavte název modelu
    model_name = "Phi-3-mini-4k-instruct"
    
    # Získejte nejnovější verzi modelu z registru Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Vytiskněte název modelu, verzi a ID
    # Tyto informace jsou užitečné pro sledování a ladění
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Vytvořte compute, který bude použit s úlohou

Úloha doladění funguje POUZE s GPU compute. Velikost computu záleží na velikosti modelu a ve většině případů je obtížné správně určit správný compute pro úlohu. V této buňce vedeme uživatele k výběru správného computu pro danou úlohu.

> [!NOTE]
> Níže uvedené compute fungují s nejoptimalizovanější konfigurací. Jakékoli změny v konfiguraci mohou vést k chybě Cuda Out Of Memory. V takových případech zkuste přejít na větší velikost compute.

> [!NOTE]
> Při výběru compute_cluster_size níže se ujistěte, že je compute dostupný ve vaší skupině prostředků. Pokud není konkrétní compute dostupný, můžete požádat o přístup k výpočetním prostředkům.

### Kontrola modelu pro podporu doladění

1. Tento Python skript interaguje s modelem Azure Machine Learning (Azure ML). Zde je rozbor, co dělá:

    - Importuje modul ast, který poskytuje funkce ke zpracování stromů abstraktní syntaxe Pythonu.

    - Kontroluje, zda má objekt foundation_model (který představuje model v Azure ML) tag s názvem finetune_compute_allow_list. Tagy v Azure ML jsou páry klíč-hodnota, které můžete vytvářet a používat k filtrování a řazení modelů.

    - Pokud je tag finetune_compute_allow_list přítomen, použije funkci ast.literal_eval k bezpečnému parsování hodnoty tagu (řetězec) do Python seznamu. Tento seznam je následně přiřazen do proměnné computes_allow_list. Poté vypíše zprávu, že by měl být vytvořen compute ze seznamu.

    - Pokud tag finetune_compute_allow_list není přítomen, nastaví computes_allow_list na None a vypíše zprávu, že tag finetune_compute_allow_list není součástí tagů modelu.

    - Shrnutí: tento skript kontroluje přítomnost konkrétního tagu v metadatech modelu, převádí hodnotu tagu na seznam, pokud existuje, a poskytuje zpětnou vazbu uživateli.

    ```python
    # Importujte modul ast, který poskytuje funkce pro zpracování stromů abstraktní syntaxe Pythonu
    import ast
    
    # Zkontrolujte, zda je v tagách modelu přítomen tag 'finetune_compute_allow_list'
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Pokud je tag přítomen, použijte ast.literal_eval pro bezpečné parsování hodnoty tagu (řetězce) do Python seznamu
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # převeďte řetězec na python seznam
        # Vytiskněte zprávu, která naznačuje, že by měl být vytvořen compute ze seznamu
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Pokud tag není přítomen, nastavte computes_allow_list na None
        computes_allow_list = None
        # Vytiskněte zprávu, která oznamuje, že tag 'finetune_compute_allow_list' není součástí tagů modelu
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Kontrola compute instance

1. Tento Python skript interaguje se službou Azure Machine Learning (Azure ML) a provádí několik kontrol compute instance. Zde je rozbor, co dělá:

    - Pokouší se získat compute instanci s názvem uloženým v proměnné compute_cluster z Azure ML workspace. Pokud je stav provisioningu compute instance „failed“, vyvolá ValueError.

    - Kontroluje, zda není computes_allow_list None. Pokud není, převede všechny velikosti compute ve seznamu na malá písmena a ověří, zda velikost aktuální compute instance je v tomto seznamu. Pokud není, vyvolá ValueError.

    - Pokud je computes_allow_list None, zkontroluje, zda velikost compute instance není v seznamu nepodporovaných GPU VM velikostí. Pokud ano, vyvolá ValueError.

    - Získá seznam všech dostupných velikostí compute ve workspace. Poté iteruje přes tento seznam a pro každou velikost compute ověřuje, zda se její název shoduje s velikostí aktuální compute instance. Pokud ano, zjistí počet GPU pro tuto velikost compute a nastaví gpu_count_found na True.

    - Pokud je gpu_count_found True, vypíše počet GPU v compute instanci. Pokud je False, vyvolá ValueError.

    - Shrnutí: tento skript provádí několik kontrol compute instance v Azure ML workspace, včetně kontroly stavu provisioningu, velikosti dle povoleného nebo zakázaného seznamu a počtu GPU.

    ```python
    # Vytiskněte zprávu výjimky
    print(e)
    # Vyvolat ValueError, pokud velikost výpočetního prostředku není ve workspace dostupná
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Získat výpočetní instanci z Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Zkontrolovat, zda je stav nasazení výpočetní instance "failed"
    if compute.provisioning_state.lower() == "failed":
        # Vyvolat ValueError, pokud je stav nasazení "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Zkontrolovat, zda computes_allow_list není None
    if computes_allow_list is not None:
        # Převést všechny velikosti výpočetních prostředků v computes_allow_list na malá písmena
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Zkontrolovat, zda je velikost výpočetní instance v computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Vyvolat ValueError, pokud velikost výpočetní instance není v computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Definovat seznam nepodporovaných GPU VM velikostí
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Zkontrolovat, zda je velikost výpočetní instance v unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Vyvolat ValueError, pokud je velikost výpočetní instance v unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Inicializovat příznak pro kontrolu, zda byl nalezen počet GPU ve výpočetní instanci
    gpu_count_found = False
    # Získat seznam všech dostupných velikostí výpočetních prostředků ve workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Procházet seznam dostupných velikostí výpočetních prostředků
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Zkontrolovat, zda název velikosti výpočetního prostředku odpovídá velikosti výpočetní instance
        if compute_sku.name.lower() == compute.size.lower():
            # Pokud ano, získat počet GPU pro tuto velikost výpočetního prostředku a nastavit gpu_count_found na True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Pokud je gpu_count_found True, vytisknout počet GPU ve výpočetní instanci
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Pokud je gpu_count_found False, vyvolat ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Vyberte dataset pro doladění modelu

1. Používáme dataset ultrachat_200k. Dataset má čtyři rozdělení, vhodná pro Supervised fine-tuning (sft).
Generation ranking (gen). Počet příkladů na každé rozdělení je uveden následovně:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Následující buňky ukazují základní přípravu dat pro doladění:

### Vizualizace několika řádků dat

Chceme, aby tento příklad běžel rychle, takže uložíme train_sft, test_sft soubory obsahující 5 % již oříznutých řádků. To znamená, že doladěný model bude mít nižší přesnost, a proto by neměl být použit v reálném nasazení.
download-dataset.py se používá ke stažení dat ultrachat_200k a transformaci datasetu do formátu vhodného pro komponentu pipeline doladění. Protože je dataset velký, zde máme pouze jeho část.

1. Spuštění níže uvedeného skriptu stáhne pouze 5 % dat. Toto lze zvýšit změnou parametru dataset_split_pc na požadované procento.

> [!NOTE]
> Některé jazykové modely mají různé jazykové kódy a proto by názvy sloupců v datasetu měly odpovídat stejným kódům.

1. Zde je příklad, jak by data měla vypadat
Dataset chat-completion je uložen ve formátu parquet, přičemž každý záznam používá následující schéma:

    - Jedná se o JSON dokument (JavaScript Object Notation), což je populární formát pro výměnu dat. Není to spustitelný kód, ale způsob ukládání a přenosu dat. Zde je rozbor jeho struktury:

    - „prompt“: Tento klíč obsahuje řetězec, který představuje úkol nebo otázku směrovanou na AI asistenta.

    - „messages“: Tento klíč obsahuje pole objektů. Každý objekt představuje zprávu v konverzaci mezi uživatelem a AI asistentem. Každý objekt zprávy má dva klíče:

    - „content“: Tento klíč obsahuje řetězec, který představuje obsah zprávy.
    - „role“: Tento klíč obsahuje řetězec, který reprezentuje roli entity, která zprávu poslala. Může být buď „user“ nebo „assistant“.
    - „prompt_id“: Tento klíč obsahuje řetězec představující jedinečný identifikátor promptu.

1. V tomto konkrétním JSON dokumentu je znázorněna konverzace, kde uživatel žádá AI asistenta o vytvoření protagonisty pro dystopický příběh. Asistent odpovídá a uživatel pak žádá o více podrobností. Asistent souhlasí s poskytnutím více detailů. Celá konverzace je spojena s konkrétním prompt_id.

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

### Stažení dat

1. Tento Python skript slouží ke stažení datasetu pomocí pomocného skriptu download-dataset.py. Zde je rozbor toho, co dělá:

    - Importuje modul os, který poskytuje přístup k funkcím závislým na operačním systému.

    - Používá funkci os.system k spuštění skriptu download-dataset.py v shellu s konkrétními příkazovými argumenty. Argumenty určí dataset ke stažení (HuggingFaceH4/ultrachat_200k), adresář pro stažení (ultrachat_200k_dataset) a procentní podíl datasetu k použití (5). Funkce os.system vrací stav ukončení příkazu; tento stav je uložen v proměnné exit_status.

    - Kontroluje, zda exit_status není 0. V operačních systémech podobných Unixu obvykle znamená stav 0 úspěch příkazu, všechny ostatní čísla označují chybu. Pokud exit_status není 0, vyvolá výjimku Exception se zprávou o chybě při stahování datasetu.

    - Shrnutí: tento skript spouští příkaz ke stažení datasetu pomocí pomocného skriptu a v případě selhání příkazu vyvolá výjimku.

    ```python
    # Importujte modul os, který poskytuje způsob, jak používat funkce závislé na operačním systému
    import os
    
    # Použijte funkci os.system ke spuštění skriptu download-dataset.py v shellu s konkrétními argumenty příkazové řádky
    # Argumenty určují dataset ke stažení (HuggingFaceH4/ultrachat_200k), adresář pro stažení (ultrachat_200k_dataset) a procento datasetu pro rozdělení (5)
    # Funkce os.system vrací výstupní stav vykonaného příkazu; tento stav je uložen v proměnné exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Zkontrolujte, zda exit_status není 0
    # V unixových operačních systémech výstupní stav 0 obvykle znamená úspěch příkazu, zatímco jakékoli jiné číslo značí chybu
    # Pokud exit_status není 0, vyvolejte výjimku Exception s hlášením, že při stahování datasetu došlo k chybě
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Načtení dat do DataFrame

1. Tento Python skript načítá soubor JSON Lines do pandas DataFrame a zobrazí prvních 5 řádků. Zde je rozbor toho, co dělá:

    - Importuje knihovnu pandas, která je silným nástrojem pro manipulaci a analýzu dat.

    - Nastaví maximální šířku sloupce pro zobrazování pandas na 0. To znamená, že celý text každého sloupce bude zobrazen bez oříznutí při vytištění DataFrame.
    - Používá funkci pd.read_json k načtení souboru train_sft.jsonl z adresáře ultrachat_200k_dataset do DataFrame. Argument lines=True označuje, že soubor je ve formátu JSON Lines, kde každý řádek je samostatný JSON objekt.

    - Používá metodu head k zobrazení prvních 5 řádků DataFrame. Pokud má DataFrame méně než 5 řádků, zobrazí všechny.

    - Stručně řečeno, tento skript načítá soubor JSON Lines do DataFrame a zobrazuje prvních 5 řádků s plným textem sloupců.
    
    ```python
    # Importujte knihovnu pandas, která je výkonnou knihovnou pro manipulaci a analýzu dat
    import pandas as pd
    
    # Nastavte maximální šířku sloupce pro zobrazovací možnosti pandas na 0
    # To znamená, že při tisku DataFrame bude zobrazen celý text každého sloupce bez ořezu
    pd.set_option("display.max_colwidth", 0)
    
    # Použijte funkci pd.read_json k načtení souboru train_sft.jsonl z adresáře ultrachat_200k_dataset do DataFrame
    # Argument lines=True znamená, že soubor je ve formátu JSON Lines, kde každý řádek je samostatný JSON objekt
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Použijte metodu head k zobrazení prvních 5 řádků DataFrame
    # Pokud má DataFrame méně než 5 řádků, zobrazí všechny z nich
    df.head()
    ```

## 5. Odeslání úlohy doladění pomocí modelu a dat jako vstupů

Vytvořte úlohu, která používá komponentu pipeline chat-completion. Více o všech podporovaných parametrech pro doladění se dozvíte zde.

### Definování parametrů doladění

1. Parametry doladění lze rozdělit do 2 kategorií – tréninkové parametry, optimalizační parametry

1. Tréninkové parametry definují aspekty tréninku, jako jsou -

    - Optimalizátor, plánovač, který se má použít
    - Metrika pro optimalizaci doladění
    - Počet tréninkových kroků, velikost dávky a další
    - Optimalizační parametry pomáhají optimalizovat paměť GPU a efektivně využívat výpočetní zdroje.

1. Níže jsou některé z parametrů, které patří do této kategorie. Optimalizační parametry se liší pro každý model a jsou zabaleny s modelem, aby tyto rozdíly zvládaly.

    - Povolení deepspeed a LoRA
    - Povolení tréninku s smíšenou přesností
    - Povolení tréninku na více uzlech

> [!NOTE]
> Supervised finetuning může vést ke ztrátě zarovnání nebo katastrofickému zapomenutí. Doporučujeme tuto záležitost zkontrolovat a po doladění provést fázi zarovnání.

### Parametry doladění

1. Tento Python skript nastavuje parametry pro doladění strojového učení. Podrobný popis:

    - Nastavuje výchozí tréninkové parametry, jako je počet tréninkových epoch, velikost dávek pro trénink a vyhodnocení, učící rychlost a typ plánovače učící rychlosti.

    - Nastavuje výchozí optimalizační parametry, jako je použití Layer-wise Relevance Propagation (LoRa) a DeepSpeed a stupeň DeepSpeed.

    - Kombinuje tréninkové a optimalizační parametry do jednoho slovníku nazvaného finetune_parameters.

    - Kontroluje, zda foundation_model má nějaké model-specifické výchozí parametry. Pokud ano, vytiskne varování a aktualizuje slovník finetune_parameters těmito model-specifickými výchozími hodnotami. Funkce ast.literal_eval se používá k převodu model-specifických výchozích hodnot ze stringu na slovník Pythonu.

    - Vytiskne konečnou sadu parametrů pro doladění, které budou použity pro běh.

    - Stručně řečeno, tento skript nastavuje a zobrazuje parametry pro doladění strojového učení s možností přepsat výchozí parametry model-specifickými.

    ```python
    # Nastavte výchozí parametry tréninku, jako je počet epoch tréninku, velikosti batchů pro trénink a vyhodnocení, učící rychlost a typ plánovače učící rychlosti
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Nastavte výchozí parametry optimalizace, například zda použít Layer-wise Relevance Propagation (LoRa) a DeepSpeed, a stupeň DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Kombinujte parametry tréninku a optimalizace do jednoho slovníku nazvaného finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Zkontrolujte, zda má foundation_model nějaké modelově specifické výchozí parametry
    # Pokud ano, vytiskněte varovnou zprávu a aktualizujte slovník finetune_parameters těmito modelově specifickými výchozími hodnotami
    # Funkce ast.literal_eval se používá k převodu modelově specifických výchozích hodnot ze stringu na Python slovník
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # převést řetězec na Python slovník
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Vytiskněte konečnou sadu parametrů doladění, které budou použity pro běh
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Tréninková pipeline

1. Tento Python skript definuje funkci pro generování zobrazovaného jména tréninkové pipeline strojového učení a následně tuto funkci zavolá pro vytvoření a vytištění jména. Podrobnosti:

1. Definována je funkce get_pipeline_display_name. Tato funkce generuje zobrazované jméno založené na různých parametrech týkajících se tréninkové pipeline.

1. Uvnitř funkce se vypočítá celková velikost dávky vynásobením velikosti dávky na zařízení, počtu kroků akumulace gradientu, počtu GPU na uzel a počtu uzlů použitých při doladění.

1. Získává další parametry, jako je typ plánovače učící rychlosti, zda je použit DeepSpeed, stupeň DeepSpeed, zda je aplikováno Layer-wise Relevance Propagation (LoRa), limit počtu kontrolních bodů modelu, které se mají uchovat, a maximální délka sekvence.

1. Sestavuje řetězec, který zahrnuje všechny tyto parametry oddělené pomlčkami. Pokud je použit DeepSpeed nebo LoRa, řetězec obsahuje „ds“ následované stupněm DeepSpeed, nebo „lora“. Pokud ne, obsahuje „nods“ nebo „nolora“.

1. Funkce vrátí tento řetězec jako zobrazované jméno tréninkové pipeline.

1. Po definici je funkce zavolána k vygenerování zobrazovaného jména, které je následně vytištěno.

1. Stručně řečeno, tento skript vygeneruje zobrazované jméno tréninkové pipeline strojového učení na základě různých parametrů a poté toto jméno vytiskne.

    ```python
    # Definujte funkci pro generování zobrazovaného jména pro tréninkový proces
    def get_pipeline_display_name():
        # Vypočítejte celkovou velikost dávky vynásobením velikosti dávky na zařízení, počtu kroků akumulace gradientu, počtu GPU na uzel a počtu uzlů použitých pro doladění
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Získejte typ plánovače rychlosti učení
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Získejte informaci, zda je použit DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Získejte fázi DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Pokud je použit DeepSpeed, zahrňte „ds“ následované fází DeepSpeed do zobrazovaného jména; pokud ne, zahrňte „nods“
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Získejte informaci, zda je použita vrstvová relevance propagace (LoRa)
        lora = finetune_parameters.get("apply_lora", "false")
        # Pokud je použita LoRa, zahrňte „lora“ do zobrazovaného jména; pokud ne, zahrňte „nolora“
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Získejte omezení počtu uchovávaných modelových kontrolních bodů
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Získejte maximální délku sekvence
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Sestavte zobrazované jméno spojováním všech těchto parametrů oddělených pomlčkami
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
    
    # Zavolejte funkci pro generování zobrazovaného jména
    pipeline_display_name = get_pipeline_display_name()
    # Vytiskněte zobrazované jméno
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Konfigurace pipeline

Tento Python skript definuje a konfiguruje pipeline strojového učení pomocí Azure Machine Learning SDK. Podrobnosti:

1. Importuje potřebné moduly z Azure AI ML SDK.

1. Získá komponentu pipeline s názvem „chat_completion_pipeline“ z registru.

1. Definuje pipeline úlohu pomocí dekorátoru `@pipeline` a funkce `create_pipeline`. Název pipeline je nastaven na `pipeline_display_name`.

1. Ve funkci `create_pipeline` inicializuje staženou pipeline komponentu s různými parametry, včetně cesty k modelu, výpočetních clusterů pro různé fáze, rozdělení datasetu pro trénink a testování, počtu GPU použitých pro doladění a dalších parametrů doladění.

1. Mapuje výstup doladění modelu na výstup pipeline úlohy. To umožňuje snadnou registraci doladěného modelu, což je požadavek pro nasazení modelu na online nebo dávkový endpoint.

1. Vytvoří instanci pipeline zavoláním funkce `create_pipeline`.

1. Nastavuje volbu `force_rerun` pipeline na `True`, což znamená, že nebudou použity uložené výsledky z předchozích úloh.

1. Nastavuje volbu `continue_on_step_failure` pipeline na `False`, takže pipeline zastaví běh, pokud některý krok selže.

1. Stručně řečeno, tento skript definuje a konfiguruje pipeline strojového učení pro úlohu chat completion pomocí Azure Machine Learning SDK.

    ```python
    # Importujte potřebné moduly z Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Získejte komponentu pipeline s názvem "chat_completion_pipeline" z registru
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Definujte pipeline job pomocí dekorátoru @pipeline a funkce create_pipeline
    # Název pipeline je nastaven na pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Inicializujte získanou komponentu pipeline s různými parametry
        # Patří sem cesta k modelu, výpočetní clustery pro různé fáze, rozdělení datasetu pro trénink a testování, počet GPU použitých pro doladění a další parametry doladění
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Namapujte rozdělení datasetu na parametry
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Nastavení pro trénink
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Nastaveno na počet GPU dostupných ve výpočetním prostředí
            **finetune_parameters
        )
        return {
            # Namapujte výstup úlohy doladění na výstup pipeline jobu
            # Toto je provedeno, abychom mohli snadno zaregistrovat doladěný model
            # Registrace modelu je vyžadována pro nasazení modelu na online nebo batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Vytvořte instanci pipeline zavoláním funkce create_pipeline
    pipeline_object = create_pipeline()
    
    # Nepoužívejte cachované výsledky z předchozích úloh
    pipeline_object.settings.force_rerun = True
    
    # Nastavte pokračování při selhání kroku na False
    # To znamená, že pipeline se zastaví, pokud některý krok selže
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Odeslat úlohu

1. Tento Python skript odesílá pipeline úlohu strojového učení do Azure Machine Learning workspace a čeká na dokončení úlohy. Podrobnosti:

    - Volá metodu create_or_update objektu jobs ve workspace_ml_client pro odeslání pipeline úlohy. Pipeline, která se má spustit, je specifikována proměnnou pipeline_object a experiment, pod kterým úloha běží, je specifikován parametrem experiment_name.

    - Následně volá metodu stream objektu jobs ve workspace_ml_client, aby čekal na dokončení pipeline úlohy. Úloha, na kterou se čeká, je určená atributem name objektu pipeline_job.

    - Stručně řečeno, tento skript odesílá pipeline úlohu strojového učení do Azure Machine Learning workspace a čeká na dokončení úlohy.

    ```python
    # Odešlete úlohu pipeline do pracovního prostoru Azure Machine Learning
    # Pipeline, která má být spuštěna, je určena objektem pipeline_object
    # Experiment, pod kterým je úloha spuštěna, je určen názvem experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Čekejte na dokončení úlohy pipeline
    # Úloha, na kterou se čeká, je určena atributem name objektu pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Registrace doladěného modelu do workspace

Zaregistrujeme model z výstupu doladění. To umožní sledování původu mezi doladěným modelem a doladěcí úlohou. Doladěcí úloha dále sleduje původ základu modelu, dat a tréninkového kódu.

### Registrace ML modelu

1. Tento Python skript registruje model strojového učení, který byl trénován v Azure Machine Learning pipeline. Podrobnosti:

    - Importuje potřebné moduly z Azure AI ML SDK.

    - Kontroluje, zda je výstup trained_model dostupný z pipeline úlohy pomocí metody get objektu jobs ve workspace_ml_client a přístupu k atributu outputs.

    - Vytváří cestu k trénovanému modelu formátováním řetězce s názvem pipeline úlohy a názvem výstupu („trained_model“).

    - Definuje název pro doladěný model přidáním „-ultrachat-200k“ k původnímu názvu modelu a nahrazením lomítek pomlčkami.

    - Připravuje registraci modelu vytvořením objektu Model s různými parametry, včetně cesty k modelu, typu modelu (MLflow model), názvu a verze modelu a popisu modelu.

    - Registruje model zavoláním metody create_or_update objektu models ve workspace_ml_client s objektem Model jako argumentem.

    - Vytiskne registrovaný model.

1. Stručně řečeno, tento skript registruje model strojového učení vytrénovaný v Azure Machine Learning pipeline.
    
    ```python
    # Importujte potřebné moduly z Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Zkontrolujte, zda je výstup `trained_model` k dispozici z pipeline jobu
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Vytvořte cestu k vyškolenému modelu formátováním řetězce s názvem pipeline jobu a názvem výstupu ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Definujte název pro doladěný model přidáním "-ultrachat-200k" k původnímu názvu modelu a nahrazením lomítek pomlčkami
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Připravte registraci modelu vytvořením objektu Model s různými parametry
    # Ty zahrnují cestu k modelu, typ modelu (MLflow model), název a verzi modelu a popis modelu
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Použijte časové razítko jako verzi, aby nedošlo ke konfliktu verzí
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Zaregistrujte model zavoláním metody create_or_update objektu models ve workspace_ml_client s objektem Model jako argumentem
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Vytiskněte registrovaný model
    print("registered model: \n", registered_model)
    ```

## 7. Nasazení doladěného modelu na online endpoint

Online endpointy poskytují trvalé REST API, které lze použít k integraci s aplikacemi vyžadujícími použití modelu.

### Správa endpointu

1. Tento Python skript vytváří spravovaný online endpoint v Azure Machine Learning pro registrovaný model. Podrobnosti:

    - Importuje potřebné moduly z Azure AI ML SDK.

    - Definuje unikátní název online endpointu přidáním časové známky k řetězci „ultrachat-completion-“.

    - Připravuje vytvoření online endpointu vytvořením ManagedOnlineEndpoint objektu s různými parametry, včetně názvu endpointu, popisu endpointu a autentizačním režimu („key“).

    - Vytváří online endpoint voláním metody begin_create_or_update workspace_ml_client s objektem ManagedOnlineEndpoint. Následně čeká na dokončení vytvoření pomocí metody wait.

1. Stručně řečeno, tento skript vytváří spravovaný online endpoint v Azure Machine Learning pro registrovaný model.

    ```python
    # Importujte potřebné moduly z Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Definujte jedinečný název pro online endpoint přidáním časového razítka k řetězci "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Připravte se na vytvoření online endpointu vytvořením objektu ManagedOnlineEndpoint s různými parametry
    # Patří sem název endpointu, popis endpointu a režim ověřování ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Vytvořte online endpoint zavoláním metody begin_create_or_update klienta workspace_ml_client s objektem ManagedOnlineEndpoint jako argumentem
    # Poté počkejte na dokončení operace vytvoření zavoláním metody wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Seznam podporovaných SKU pro nasazení najdete zde - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Nasazení ML modelu

1. Tento Python skript nasazuje registrovaný model strojového učení na spravovaný online endpoint v Azure Machine Learning. Podrobnosti:

    - Importuje modul ast, který poskytuje funkce pro zpracování stromů abstraktní syntaxe Pythonu.

    - Nastavuje typ instance pro nasazení na „Standard_NC6s_v3“.

    - Kontroluje, zda je v foundation model přítagován tag inference_compute_allow_list. Pokud ano, převede hodnotu tagu ze stringu na Python seznam a přiřadí ji proměnné inference_computes_allow_list. Pokud ne, nastaví tuto proměnnou na None.

    - Kontroluje, zda je specifikovaný typ instance v allow listu. Pokud není, vypíše zprávu s výzvou k výběru instance z uvedeného seznamu.

    - Připravuje vytvoření nasazení vytvořením ManagedOnlineDeployment objektu s různými parametry, včetně názvu nasazení, názvu endpointu, ID modelu, typu a počtu instancí, nastavení zdravotních kontrol (liveness probe) a nastavení požadavků.

    - Vytváří nasazení zavoláním metody begin_create_or_update workspace_ml_client s objektem ManagedOnlineDeployment a čeká na dokončení pomocí metody wait.

    - Nastavuje traffic endpointu na 100 % směrování na deployment „demo“.

    - Aktualizuje endpoint zavoláním metody begin_create_or_update workspace_ml_client s objektem endpoint a čeká na dokončení pomocí metody result.

1. Stručně řečeno, tento skript nasazuje registrovaný model strojového učení na spravovaný online endpoint v Azure Machine Learning.

    ```python
    # Importujte modul ast, který poskytuje funkce pro zpracování stromů abstraktní syntaxe Pythonu
    import ast
    
    # Nastavte typ instance pro nasazení
    instance_type = "Standard_NC6s_v3"
    
    # Zkontrolujte, zda je v základním modelu přítomen tag `inference_compute_allow_list`
    if "inference_compute_allow_list" in foundation_model.tags:
        # Pokud ano, převedte hodnotu tagu ze stringu na Python seznam a přiřaďte ji do `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Pokud ne, nastavte `inference_computes_allow_list` na `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Zkontrolujte, zda je specifikovaný typ instance v seznamu povolených
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Připravte se na vytvoření nasazení vytvořením objektu `ManagedOnlineDeployment` s různými parametry
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Vytvořte nasazení zavoláním metody `begin_create_or_update` klienta `workspace_ml_client` s objektem `ManagedOnlineDeployment` jako argumentem
    # Poté počkejte na dokončení operace vytvoření zavoláním metody `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Nastavte traffic endpointu tak, aby směřoval 100 % provozu na nasazení "demo"
    endpoint.traffic = {"demo": 100}
    
    # Aktualizujte endpoint zavoláním metody `begin_create_or_update` klienta `workspace_ml_client` s objektem `endpoint` jako argumentem
    # Poté počkejte na dokončení operace aktualizace zavoláním metody `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Test endpointu se vzorovými daty

Získáme vzorová data z testovacího datasetu a odešleme je na online endpoint pro inferenci. Následně zobrazíme vyhodnocené štítky vedle skutečných štítků.

### Čtení výsledků

1. Tento Python skript čte soubor JSON Lines do pandas DataFrame, vezme náhodný vzorek a resetuje index. Podrobnosti:

    - Načte soubor ./ultrachat_200k_dataset/test_gen.jsonl do pandas DataFrame. Funkce read_json je použita s argumentem lines=True, protože soubor je ve formátu JSON Lines, kde je každý řádek samostatný JSON objekt.

    - Vezme náhodný vzorek 1 řádku z DataFrame. Funkce sample je použita s argumentem n=1 k určení počtu vybraných náhodných řádků.

    - Resetuje index DataFrame. Funkce reset_index je použita s argumentem drop=True, aby původní index byl odstraněn a nahrazen novým indexem s výchozími celočíselnými hodnotami.

    - Zobrazí prvních 2 řádků DataFrame pomocí funkce head s argumentem 2. Protože DataFrame po výběru vzorku obsahuje pouze jeden řádek, bude zobrazen pouze tento jeden řádek.

1. Stručně řečeno, tento skript načte soubor JSON Lines do pandas DataFrame, vezme náhodný vzorek 1 řádku, resetuje index a zobrazí první řádek.
    
    ```python
    # Importovat knihovnu pandas
    import pandas as pd
    
    # Načíst soubor JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' do pandas DataFrame
    # Argument 'lines=True' označuje, že soubor je ve formátu JSON Lines, kde každý řádek je samostatný JSON objekt
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Vzít náhodný vzorek 1 řádku z DataFrame
    # Argument 'n=1' určuje počet náhodných řádků k výběru
    test_df = test_df.sample(n=1)
    
    # Resetovat index DataFrame
    # Argument 'drop=True' označuje, že původní index by měl být odstraněn a nahrazen novým indexem s výchozími celočíselnými hodnotami
    # Argument 'inplace=True' označuje, že DataFrame by měl být upraven přímo (bez vytváření nového objektu)
    test_df.reset_index(drop=True, inplace=True)
    
    # Zobrazit první 2 řádky DataFrame
    # Nicméně, protože DataFrame obsahuje po vzorkování pouze jeden řádek, zobrazí se pouze ten jeden řádek
    test_df.head(2)
    ```

### Vytvoření JSON objektu

1. Tento Python skript vytváří JSON objekt s konkrétními parametry a ukládá jej do souboru. Podrobnosti:

    - Importuje modul json, který poskytuje funkce pro práci s JSON daty.
    - Vytváří slovník parameters s klíči a hodnotami, které představují parametry pro model strojového učení. Klíče jsou "temperature", "top_p", "do_sample" a "max_new_tokens" a jejich odpovídající hodnoty jsou 0.6, 0.9, True a 200.

    - Vytváří další slovník test_json se dvěma klíči: "input_data" a "params". Hodnota "input_data" je další slovník s klíči "input_string" a "parameters". Hodnota "input_string" je seznam obsahující první zprávu z DataFrame test_df. Hodnota "parameters" je dříve vytvořený slovník parameters. Hodnota "params" je prázdný slovník.

    - Otevírá soubor jménem sample_score.json
    
    ```python
    # Importujte modul json, který poskytuje funkce pro práci s JSON daty
    import json
    
    # Vytvořte slovník `parameters` s klíči a hodnotami, které představují parametry pro model strojového učení
    # Klíče jsou "temperature", "top_p", "do_sample" a "max_new_tokens" a jejich odpovídající hodnoty jsou 0.6, 0.9, True a 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Vytvořte další slovník `test_json` se dvěma klíči: "input_data" a "params"
    # Hodnota "input_data" je další slovník s klíči "input_string" a "parameters"
    # Hodnota "input_string" je seznam obsahující první zprávu z DataFrame `test_df`
    # Hodnota "parameters" je slovník `parameters` vytvořený dříve
    # Hodnota "params" je prázdný slovník
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Otevřete soubor s názvem `sample_score.json` v adresáři `./ultrachat_200k_dataset` v režimu zápisu
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Zapište slovník `test_json` do souboru ve formátu JSON pomocí funkce `json.dump`
        json.dump(test_json, f)
    ```

### Volání endpointu

1. Tento Python skript volá online endpoint v Azure Machine Learning, aby ohodnotil JSON soubor. Zde je rozbor toho, co dělá:

    - Volá metodu invoke vlastnosti online_endpoints objektu workspace_ml_client. Tato metoda slouží k zaslání žádosti online endpointu a získání odpovědi.

    - Specifikuje jméno endpointu a nasazení pomocí argumentů endpoint_name a deployment_name. V tomto případě je jméno endpointu uloženo v proměnné online_endpoint_name a jméno nasazení je "demo".

    - Specifikuje cestu k JSON souboru, který se má ohodnotit, pomocí argumentu request_file. V tomto případě je soubor ./ultrachat_200k_dataset/sample_score.json.

    - Ukládá odpověď z endpointu do proměnné response.

    - Vypisuje surovou odpověď.

1. Celkově tento skript volá online endpoint v Azure Machine Learning za účelem ohodnocení JSON souboru a tiskne odpověď.

    ```python
    # Zavolejte online koncový bod v Azure Machine Learning pro ohodnocení souboru `sample_score.json`
    # Metoda `invoke` vlastnosti `online_endpoints` objektu `workspace_ml_client` se používá k odeslání požadavku na online koncový bod a získání odpovědi
    # Argument `endpoint_name` určuje název koncového bodu, který je uložen v proměnné `online_endpoint_name`
    # Argument `deployment_name` určuje název nasazení, které je "demo"
    # Argument `request_file` určuje cestu k JSON souboru, který má být ohodnocen, což je `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Vytiskněte surovou odpověď z koncového bodu
    print("raw response: \n", response, "\n")
    ```

## 9. Odstranění online endpointu

1. Nezapomeňte odstranit online endpoint, jinak by vám běžel měřič účtování za výpočetní prostředky použité endpointem. Tento řádek Python kódu odstraňuje online endpoint v Azure Machine Learning. Zde je rozbor toho, co dělá:

    - Volá metodu begin_delete vlastnosti online_endpoints objektu workspace_ml_client. Tato metoda slouží k zahájení odstranění online endpointu.

    - Specifikuje jméno endpointu, který se má odstranit, pomocí argumentu name. V tomto případě je jméno endpointu uloženo v proměnné online_endpoint_name.

    - Volá metodu wait, která čeká na dokončení operace odstranění. Jedná se o blokující operaci, což znamená, že zabrání skriptu pokračovat, dokud není odstranění dokončeno.

    - Celkově tento řádek kódu zahajuje odstranění online endpointu v Azure Machine Learning a čeká na dokončení operace.

    ```python
    # Smazat online endpoint v Azure Machine Learning
    # Metoda `begin_delete` vlastnosti `online_endpoints` objektu `workspace_ml_client` se používá pro zahájení smazání online endpointu
    # Argument `name` specifikuje jméno endpointu, který má být smazán, a je uložen v proměnné `online_endpoint_name`
    # Metoda `wait` je volána, aby počkala na dokončení operace mazání. Jedná se o blokující operaci, což znamená, že zabrání pokračování skriptu, dokud není mazání dokončeno
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí služeb automatického překladu [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Není nám vymezeno jakékoli právní odpovědnosti za nedorozumění nebo nesprávné výklady vyplývající z užití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->