<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:40:36+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "hu"
}
-->
## Hogyan használjuk az Azure ML rendszerregiszter chat-kiegészítő komponenseit modell finomhangolásához

Ebben a példában a Phi-3-mini-4k-instruct modellt finomhangoljuk, hogy egy két személy közötti beszélgetést fejezzen be az ultrachat_200k adathalmaz segítségével.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35.hu.png)

A példa bemutatja, hogyan végezhetünk finomhangolást az Azure ML SDK és Python használatával, majd hogyan telepíthetjük a finomhangolt modellt egy online végpontra valós idejű lekérdezéshez.

### Tanító adatok

Az ultrachat_200k adathalmazt fogjuk használni. Ez az UltraChat adathalmaz erősen szűrt változata, amelyet a Zephyr-7B-β, egy csúcstechnológiás 7 milliárd paraméteres chat modell betanításához használtak.

### Modell

A Phi-3-mini-4k-instruct modellt használjuk, hogy megmutassuk, hogyan lehet egy modellt finomhangolni chat-kiegészítő feladatra. Ha ezt a jegyzetfüzetet egy adott modellkártyáról nyitottad meg, ne felejtsd el kicserélni a modellspecifikus nevet.

### Feladatok

- Válassz egy modellt a finomhangoláshoz.
- Válaszd ki és vizsgáld meg a tanító adatokat.
- Állítsd be a finomhangolási feladatot.
- Futtasd a finomhangolási feladatot.
- Tekintsd át a tanítási és értékelési mutatókat.
- Regisztráld a finomhangolt modellt.
- Telepítsd a finomhangolt modellt valós idejű lekérdezéshez.
- Takarítsd el az erőforrásokat.

## 1. Előfeltételek beállítása

- Telepítsd a függőségeket
- Csatlakozz az AzureML munkaterülethez. További információkért lásd az SDK hitelesítés beállítását. Cseréld ki az alábbi <WORKSPACE_NAME>, <RESOURCE_GROUP> és <SUBSCRIPTION_ID> értékeket.
- Csatlakozz az azureml rendszerregiszterhez
- Állíts be opcionálisan egy kísérlet nevet
- Ellenőrizd vagy hozd létre a számítási erőforrást.

> [!NOTE]
> Egyetlen GPU csomópont több GPU kártyát is tartalmazhat. Például a Standard_NC24rs_v3 csomópontban 4 NVIDIA V100 GPU van, míg a Standard_NC12s_v3-ban 2 NVIDIA V100 GPU található. Erről további információ a dokumentációban. A csomópontonkénti GPU kártyák számát az alábbi gpus_per_node paraméter határozza meg. Ennek helyes beállítása biztosítja az összes GPU kihasználását a csomóponton. Az ajánlott GPU számítási SKU-k itt és itt találhatók.

### Python könyvtárak

Telepítsd a függőségeket az alábbi cella futtatásával. Ez nem opcionális lépés új környezetben.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Kapcsolódás az Azure ML-hez

1. Ez a Python szkript az Azure Machine Learning (Azure ML) szolgáltatással való interakcióra szolgál. Íme, mit csinál:

    - Importálja a szükséges modulokat az azure.ai.ml, azure.identity és azure.ai.ml.entities csomagokból. Emellett importálja a time modult is.

    - Megpróbál hitelesíteni a DefaultAzureCredential() segítségével, amely egyszerűsített hitelesítést biztosít az Azure felhőben futó alkalmazások gyors fejlesztéséhez. Ha ez nem sikerül, az InteractiveBrowserCredential()-re vált, amely interaktív bejelentkezési ablakot nyit.

    - Ezután megpróbál létrehozni egy MLClient példányt a from_config metódussal, amely az alapértelmezett config fájlból (config.json) olvassa be a beállításokat. Ha ez nem sikerül, manuálisan hoz létre MLClient példányt a subscription_id, resource_group_name és workspace_name megadásával.

    - Létrehoz egy másik MLClient példányt az "azureml" nevű Azure ML rendszerregiszterhez. Ebben a regiszterben tárolják a modelleket, finomhangolási pipeline-okat és környezeteket.

    - Beállítja az experiment_name értékét "chat_completion_Phi-3-mini-4k-instruct"-ra.

    - Egyedi időbélyeget generál az aktuális idő (másodpercben az epoch óta, lebegőpontos számként) egész számra konvertálásával, majd sztringgé alakításával. Ezt az időbélyeget egyedi nevek és verziók létrehozásához használhatjuk.

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

## 2. Válassz egy alapmodellt a finomhangoláshoz

1. A Phi-3-mini-4k-instruct egy 3,8 milliárd paraméteres, könnyű, csúcstechnológiás nyílt modell, amely a Phi-2 modellhez használt adathalmazokon alapul. A modell a Phi-3 modellcsaládhoz tartozik, és a Mini verzió két változatban érhető el: 4K és 128K, ami a támogatott kontextushossz (tokenekben). A modellt a saját célunkra kell finomhangolni. Ezeket a modelleket megtekintheted az AzureML Studio Modell Katalógusában, a chat-kiegészítő feladatra szűrve. Ebben a példában a Phi-3-mini-4k-instruct modellt használjuk. Ha más modellhez nyitottad meg ezt a jegyzetfüzetet, cseréld ki a modell nevét és verzióját ennek megfelelően.

    > [!NOTE]
    > A modell id tulajdonsága. Ezt adjuk majd meg bemenetként a finomhangolási feladatnak. Ez az Asset ID mezőként is elérhető a modell részletei között az AzureML Studio Modell Katalógusban.

2. Ez a Python szkript az Azure Machine Learning (Azure ML) szolgáltatással kommunikál. Íme, mit csinál:

    - Beállítja a model_name értékét "Phi-3-mini-4k-instruct"-ra.

    - A registry_ml_client objektum models tulajdonságának get metódusával lekéri a megadott nevű modell legfrissebb verzióját az Azure ML rendszerregiszterből. A get metódus két argumentummal hívódik: a modell neve és egy címke, amely azt jelzi, hogy a legfrissebb verziót kérjük.

    - Kiír egy üzenetet a konzolra, amely tartalmazza a finomhangoláshoz használt modell nevét, verzióját és azonosítóját. A string format metódusa segítségével illeszti be ezeket az értékeket az üzenetbe. A modell neve, verziója és azonosítója a foundation_model objektum tulajdonságai.

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

## 3. Hozz létre számítási erőforrást a feladathoz

A finomhangolási feladat CSAK GPU számításon működik. A számítási erőforrás mérete a modell méretétől függ, és sok esetben nehéz megtalálni a megfelelő erőforrást. Ebben a cellában segítünk a megfelelő számítási erőforrás kiválasztásában.

> [!NOTE]
> Az alábbi számítási erőforrások a legoptimálisabb konfigurációval működnek. Bármilyen konfigurációváltoztatás Cuda Out Of Memory hibához vezethet. Ilyen esetekben próbáld meg nagyobb méretű számítást választani.

> [!NOTE]
> A compute_cluster_size kiválasztásakor győződj meg róla, hogy az adott számítási erőforrás elérhető a saját erőforráscsoportodban. Ha egy adott számítási erőforrás nem elérhető, kérhetsz hozzáférést.

### A modell finomhangolási támogatásának ellenőrzése

1. Ez a Python szkript egy Azure Machine Learning (Azure ML) modellel kommunikál. Íme, mit csinál:

    - Importálja az ast modult, amely a Python absztrakt szintaxisfájának feldolgozásához nyújt funkciókat.

    - Ellenőrzi, hogy a foundation_model objektumnak (ami egy Azure ML modellt reprezentál) van-e finetune_compute_allow_list nevű címkéje. Az Azure ML címkék kulcs-érték párok, amelyeket modellek szűrésére és rendezésére használhatunk.

    - Ha a finetune_compute_allow_list címke jelen van, az ast.literal_eval függvénnyel biztonságosan átalakítja a címke értékét (ami egy sztring) Python listává. Ezt a listát a computes_allow_list változóhoz rendeli. Ezután kiír egy üzenetet, hogy a számítási erőforrást ebből a listából kell létrehozni.

    - Ha a finetune_compute_allow_list címke nem található, a computes_allow_list értékét None-ra állítja, és kiírja, hogy a címke nem része a modell címkéinek.

    - Összefoglalva, ez a szkript ellenőrzi a modell metaadataiban egy adott címke meglétét, ha van, listává alakítja az értékét, és visszajelzést ad a felhasználónak.

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

### Számítási példány ellenőrzése

1. Ez a Python szkript az Azure Machine Learning (Azure ML) szolgáltatással kommunikál, és több ellenőrzést végez egy számítási példányon. Íme, mit csinál:

    - Megpróbálja lekérni a compute_cluster nevű számítási példányt az Azure ML munkaterületről. Ha a példány provisioning állapota "failed", hibát dob.

    - Ellenőrzi, hogy a computes_allow_list nem None-e. Ha nem az, az összes engedélyezett számítási méretet kisbetűssé alakítja, majd ellenőrzi, hogy a jelenlegi számítási példány mérete szerepel-e a listában. Ha nem, hibát dob.

    - Ha a computes_allow_list None, akkor ellenőrzi, hogy a számítási példány mérete nem szerepel-e az alátámasztatlan GPU VM méretek listájában. Ha igen, hibát dob.

    - Lekéri az összes elérhető számítási méret listáját a munkaterületen. Végigiterál ezen a listán, és ha talál olyan méretet, amely megegyezik a jelenlegi számítási példány méretével, lekéri az adott mérethez tartozó GPU-k számát, és beállítja a gpu_count_found változót True-ra.

    - Ha gpu_count_found True, kiírja a számítási példányban található GPU-k számát. Ha False, hibát dob.

    - Összefoglalva, ez a szkript több ellenőrzést végez egy Azure ML munkaterületen lévő számítási példányon, beleértve a provisioning állapotát, méretét az engedélyezett vagy tiltott listák alapján, valamint a GPU-k számát.

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

## 4. Válaszd ki az adathalmazt a modell finomhangolásához

1. Az ultrachat_200k adathalmazt használjuk. Az adathalmaz négy részre van osztva, amelyek alkalmasak felügyelt finomhangolásra (sft). Generációs rangsorolás (gen). Az egyes részek példáinak száma a következő:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. A következő néhány cella az alapvető adat-előkészítést mutatja be a finomhangoláshoz:

### Néhány adat sor megjelenítése

A mintát gyors futtatás érdekében úgy mentjük el, hogy a train_sft és test_sft fájlok az eredeti adatok 5%-át tartalmazzák. Ez azt jelenti, hogy a finomhangolt modell pontossága alacsonyabb lesz, ezért nem ajánlott valós környezetben használni.
A download-dataset.py segédprogram letölti az ultrachat_200k adathalmazt, és átalakítja azt a finomhangolási pipeline komponens által fogyasztható formátumba. Mivel az adathalmaz nagy, itt csak egy részét használjuk.

1. Az alábbi szkript csak az adatok 5%-át tölti le. Ezt a dataset_split_pc paraméter módosításával növelheted a kívánt százalékra.

    > [!NOTE]
    > Egyes nyelvi modellek eltérő nyelvkódokat használnak, ezért az adathalmaz oszlopneveinek is ennek megfelelően kell tükrözniük ezt.

1. Íme egy példa arra, hogyan néz ki az adat
A chat-kiegészítő adathalmaz parquet formátumban van tárolva, minden bejegyzés a következő sémát követi:

    - Ez egy JSON (JavaScript Object Notation) dokumentum, amely egy népszerű adatcsere formátum. Nem futtatható kód, hanem adat tárolására és továbbítására szolgál. Íme a szerkezete:

    - "prompt": Ez a kulcs egy sztring értéket tartalmaz, amely egy feladatot vagy kérdést jelöl az AI asszisztens felé.

    - "messages": Ez a kulcs egy objektumokból álló tömböt tartalmaz. Minden objektum egy üzenetet jelöl egy felhasználó és egy AI asszisztens közötti beszélgetésben. Minden üzenet objektumnak két kulcsa van:

    - "content": Ez a kulcs egy sztring értéket tartalmaz, amely az üzenet tartalmát jelöli.
    - "role": Ez a kulcs egy sztring értéket tartalmaz, amely az üzenetet küldő entitás szerepét jelöli. Lehet "user" vagy "assistant".
    - "prompt_id": Ez a kulcs egy sztring értéket tartalmaz, amely az adott prompt egyedi azonosítója.

1. Ebben a konkrét JSON dokumentumban egy beszélgetés látható, ahol a felhasználó egy disztópikus történet főszereplőjének megalkotását kéri az AI asszisztenstől. Az asszisztens válaszol, majd a felhasználó további részleteket kér. Az asszisztens beleegyezik, hogy több részletet ad. Az egész beszélgetés egy adott prompt azonosítóhoz kapcsolódik.

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

### Adatok letöltése

1. Ez a Python szkript egy segédprogramot, a download-dataset.py-t használja egy adathalmaz letöltésére. Íme, mit csinál:

    - Importálja az os modult, amely hordozható módon biztosít operációs rendszer függő funkciókat.

    - Az os.system függvénnyel futtatja a download-dataset.py szkriptet a shellben, megadva a letöltendő adathalmazt (HuggingFaceH4/ultrachat_200k), a letöltési könyvtárat (ultrachat_200k_dataset) és az adathalmaz felosztásának százalékát (5). Az os.system a parancs kilépési státuszát adja vissza, amelyet az exit_status változóban tárol.

    - Ellenőrzi, hogy az exit_status nem 0-e. Unix-szerű rendszereken a 0 azt jelenti, hogy a parancs sikeresen lefutott, minden más érték hibát jelez. Ha nem 0, kivételt dob egy hibaüzenettel, amely jelzi, hogy hiba történt az adathalmaz letöltése során.

    - Összefoglalva, ez a szkript egy segédprogram segítségével letölt egy adathalmazt, és hibát jelez, ha a letöltés nem sikerül.

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

### Adatok betöltése DataFrame-be

1. Ez a Python szkript egy JSON Lines fájlt tölt be egy pandas DataFrame-be, és megjeleníti az első 5 sort. Íme, mit csinál:

    - Importálja a pandas könyvtárat, amely egy erőteljes adatmanipulációs és elemző könyvtár.

    - Beállítja a pandas megjelenítési opciói között az oszlopok maximális szélességét 0-ra, ami azt jelenti, hogy az oszlopok teljes szövege megjelenik, nem lesz levágva, amikor a DataFrame-et kiírjuk.

    - A pd.read_json függvénnyel betölti a train_sft.jsonl fájlt az ultrachat_200k_dataset könyvtárból egy DataFrame-be.
- A head metódust használja a DataFrame első 5 sorának megjelenítésére. Ha a DataFrame kevesebb, mint 5 sort tartalmaz, akkor az összes sort megjeleníti.

- Összefoglalva, ez a szkript egy JSON Lines fájlt tölt be egy DataFrame-be, és megjeleníti az első 5 sort a teljes oszlopszöveggel.

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

## 5. Küldje be a finomhangolási feladatot a modell és az adatok megadásával

Hozza létre azt a feladatot, amely a chat-completion pipeline komponenst használja. Tudjon meg többet a finomhangoláshoz támogatott összes paraméterről.

### Finomhangolási paraméterek meghatározása

1. A finomhangolási paraméterek két kategóriába sorolhatók – tanítási paraméterek és optimalizációs paraméterek

1. A tanítási paraméterek a tanítási folyamat szempontjait határozzák meg, például -

    - Az alkalmazott optimalizáló és ütemező
    - A finomhangolás optimalizálására szolgáló metrika
    - A tanítási lépések száma, a batch méret és így tovább
    - Az optimalizációs paraméterek segítenek a GPU memória optimalizálásában és a számítási erőforrások hatékony kihasználásában.

1. Az alábbiakban néhány paraméter található, amelyek ebbe a kategóriába tartoznak. Az optimalizációs paraméterek modellfüggőek, és a modellhez csomagolva kezelik ezeket a különbségeket.

    - DeepSpeed és LoRA engedélyezése
    - Vegyes precizitású tanítás engedélyezése
    - Többcsomópontos tanítás engedélyezése


> [!NOTE]
> A felügyelt finomhangolás eredményezhet eltérést az illeszkedésben vagy katasztrofális felejtést. Javasoljuk, hogy ellenőrizze ezt a problémát, és futtasson egy illeszkedési szakaszt a finomhangolás után.

### Finomhangolási paraméterek

1. Ez a Python szkript beállítja a gépi tanulási modell finomhangolásához szükséges paramétereket. Íme, mit csinál:

    - Beállítja az alapértelmezett tanítási paramétereket, mint például a tanítási epochok száma, a tanítási és értékelési batch méretek, a tanulási ráta és a tanulási ráta ütemező típusa.

    - Beállítja az alapértelmezett optimalizációs paramétereket, például hogy alkalmazza-e a Layer-wise Relevance Propagation-t (LoRa) és a DeepSpeed-et, valamint a DeepSpeed szintjét.

    - Egyesíti a tanítási és optimalizációs paramétereket egyetlen szótárba, amelynek neve finetune_parameters.

    - Ellenőrzi, hogy a foundation_model rendelkezik-e modell-specifikus alapértelmezett paraméterekkel. Ha igen, figyelmeztető üzenetet ír ki, és frissíti a finetune_parameters szótárat ezekkel a modell-specifikus alapértelmezettekkel. Az ast.literal_eval függvényt használja a modell-specifikus alapértelmezettek sztringből Python szótárrá alakításához.

    - Kiírja a finomhangoláshoz használt végleges paramétereket.

    - Összefoglalva, ez a szkript beállítja és megjeleníti a gépi tanulási modell finomhangolásához szükséges paramétereket, lehetőséget adva az alapértelmezett paraméterek modell-specifikus felülírására.

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

### Tanítási pipeline

1. Ez a Python szkript egy függvényt definiál, amely egy megjelenítendő nevet generál egy gépi tanulási tanítási pipeline számára, majd meghívja ezt a függvényt a név generálására és kiírására. Íme, mit csinál:

1. Definiálja a get_pipeline_display_name függvényt, amely a tanítási pipeline különböző paraméterei alapján generál megjelenítendő nevet.

1. A függvényen belül kiszámolja az összesített batch méretet úgy, hogy megszorozza az eszközönkénti batch méretet, a gradiens akumulációs lépések számát, a node-onkénti GPU-k számát és a finomhangoláshoz használt node-ok számát.

1. Lekéri a tanulási ráta ütemező típusát, hogy alkalmazzák-e a DeepSpeed-et, a DeepSpeed szintjét, hogy alkalmazzák-e a Layer-wise Relevance Propagation-t (LoRa), a megtartandó modell checkpointok számának korlátját, valamint a maximális szekvencia hosszát.

1. Összeállít egy sztringet, amely tartalmazza ezeket a paramétereket kötőjellel elválasztva. Ha DeepSpeed vagy LoRa alkalmazva van, a sztring tartalmazza a "ds" és a DeepSpeed szintjét, vagy "lora" szavakat. Ha nem, akkor "nods" vagy "nolora" szerepel benne.

1. A függvény visszaadja ezt a sztringet, amely a tanítási pipeline megjelenítendő neve lesz.

1. A függvény definiálása után meghívja azt a megjelenítendő név generálására, majd kiírja azt.

1. Összefoglalva, ez a szkript egy gépi tanulási tanítási pipeline megjelenítendő nevét generálja különböző paraméterek alapján, majd kiírja azt.

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

### Pipeline konfigurálása

Ez a Python szkript egy gépi tanulási pipeline-t definiál és konfigurál az Azure Machine Learning SDK segítségével. Íme, mit csinál:

1. Importálja a szükséges modulokat az Azure AI ML SDK-ból.

1. Lekéri a "chat_completion_pipeline" nevű pipeline komponenst a regiszterből.

1. Definiál egy pipeline feladatot a `@pipeline` dekorátorral és a `create_pipeline` függvénnyel. A pipeline neve a `pipeline_display_name` lesz.

1. A `create_pipeline` függvényen belül inicializálja a lekért pipeline komponenst különböző paraméterekkel, beleértve a modell elérési útját, a különböző szakaszokhoz tartozó számítási klasztereket, a tanítási és tesztelési adathalmaz részeket, a finomhangoláshoz használt GPU-k számát és egyéb finomhangolási paramétereket.

1. Leképezi a finomhangolási feladat kimenetét a pipeline feladat kimenetére. Ez azért történik, hogy a finomhangolt modellt könnyen regisztrálni lehessen, ami szükséges a modell online vagy batch végpontra történő telepítéséhez.

1. Létrehozza a pipeline példányát a `create_pipeline` függvény meghívásával.

1. Beállítja a pipeline `force_rerun` beállítását `True` értékre, ami azt jelenti, hogy a korábbi feladatok gyorsítótárazott eredményeit nem használja fel.

1. Beállítja a pipeline `continue_on_step_failure` beállítását `False` értékre, vagyis a pipeline leáll, ha bármelyik lépés hibát jelez.

1. Összefoglalva, ez a szkript egy gépi tanulási pipeline-t definiál és konfigurál egy chat completion feladathoz az Azure Machine Learning SDK segítségével.

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

### Feladat beküldése

1. Ez a Python szkript egy gépi tanulási pipeline feladatot küld be egy Azure Machine Learning munkaterületre, majd várja a feladat befejezését. Íme, mit csinál:

    - Meghívja a workspace_ml_client jobs objektumának create_or_update metódusát a pipeline feladat beküldéséhez. A futtatandó pipeline a pipeline_object, az alá tartozó kísérlet pedig az experiment_name.

    - Ezután meghívja a workspace_ml_client jobs objektumának stream metódusát, hogy megvárja a pipeline feladat befejezését. A várakozás a pipeline_job objektum name attribútuma alapján történik.

    - Összefoglalva, ez a szkript egy gépi tanulási pipeline feladatot küld be egy Azure Machine Learning munkaterületre, majd várja a feladat befejezését.

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

## 6. Regisztrálja a finomhangolt modellt a munkaterületen

A finomhangolási feladat kimenetéből regisztráljuk a modellt. Ez nyomon követi a kapcsolatot a finomhangolt modell és a finomhangolási feladat között. A finomhangolási feladat tovább követi a kapcsolatot az alapmodelltől, az adatoktól és a tanítási kódtól.

### ML modell regisztrálása

1. Ez a Python szkript egy gépi tanulási modellt regisztrál, amelyet egy Azure Machine Learning pipeline-ban tanítottak. Íme, mit csinál:

    - Importálja a szükséges modulokat az Azure AI ML SDK-ból.

    - Ellenőrzi, hogy a pipeline feladatból elérhető-e a trained_model kimenet a workspace_ml_client jobs objektumának get metódusával és annak outputs attribútumával.

    - Összeállít egy elérési utat a tanított modellhez a pipeline feladat nevének és a kimenet ("trained_model") nevének formázásával.

    - Meghatároz egy nevet a finomhangolt modellnek úgy, hogy a modell eredeti nevéhez hozzáfűzi a "-ultrachat-200k" sztringet, és a perjeleket kötőjelekkel helyettesíti.

    - Előkészíti a modell regisztrálását egy Model objektum létrehozásával, amely tartalmazza a modell elérési útját, típusát (MLflow modell), nevét, verzióját és leírását.

    - Regisztrálja a modellt a workspace_ml_client models objektumának create_or_update metódusával, a Model objektumot átadva.

    - Kiírja a regisztrált modellt.

1. Összefoglalva, ez a szkript egy gépi tanulási modellt regisztrál, amelyet egy Azure Machine Learning pipeline-ban tanítottak.

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

## 7. Telepítse a finomhangolt modellt online végpontra

Az online végpontok tartós REST API-t biztosítanak, amelyet alkalmazások integrálására lehet használni, amelyeknek szükségük van a modell használatára.

### Végpont kezelése

1. Ez a Python szkript egy kezelt online végpontot hoz létre az Azure Machine Learning-ben egy regisztrált modellhez. Íme, mit csinál:

    - Importálja a szükséges modulokat az Azure AI ML SDK-ból.

    - Egyedi nevet definiál az online végpontnak úgy, hogy a "ultrachat-completion-" sztringhez hozzáfűz egy időbélyeget.

    - Előkészíti az online végpont létrehozását egy ManagedOnlineEndpoint objektum létrehozásával, amely tartalmazza a végpont nevét, leírását és az autentikációs módot ("key").

    - Létrehozza az online végpontot a workspace_ml_client begin_create_or_update metódusával, majd megvárja a létrehozási művelet befejezését a wait metódussal.

1. Összefoglalva, ez a szkript egy kezelt online végpontot hoz létre az Azure Machine Learning-ben egy regisztrált modellhez.

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
> Itt található a telepítéshez támogatott SKU-k listája - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML modell telepítése

1. Ez a Python szkript egy regisztrált gépi tanulási modellt telepít egy kezelt online végpontra az Azure Machine Learning-ben. Íme, mit csinál:

    - Importálja az ast modult, amely a Python absztrakt szintaxisfájának feldolgozásához nyújt funkciókat.

    - Beállítja a telepítéshez használt példány típusát "Standard_NC6s_v3"-ra.

    - Ellenőrzi, hogy a foundation model tartalmazza-e az inference_compute_allow_list címkét. Ha igen, a címke értékét sztringből Python listává alakítja, és hozzárendeli az inference_computes_allow_list változóhoz. Ha nem, akkor None értéket ad neki.

    - Ellenőrzi, hogy a megadott példány típus szerepel-e az engedélyezett listán. Ha nem, üzenetet ír ki, amelyben arra kéri a felhasználót, hogy válasszon az engedélyezett lista elemei közül.

    - Előkészíti a telepítést egy ManagedOnlineDeployment objektum létrehozásával, amely tartalmazza a telepítés nevét, a végpont nevét, a modell azonosítóját, a példány típusát és számát, az élő állapot ellenőrző beállításokat és a kérés beállításokat.

    - Létrehozza a telepítést a workspace_ml_client begin_create_or_update metódusával, majd megvárja a létrehozási művelet befejezését a wait metódussal.

    - Beállítja a végpont forgalmát úgy, hogy a forgalom 100%-át a "demo" telepítésre irányítsa.

    - Frissíti a végpontot a workspace_ml_client begin_create_or_update metódusával, majd megvárja a frissítés befejezését a result metódussal.

1. Összefoglalva, ez a szkript egy regisztrált gépi tanulási modellt telepít egy kezelt online végpontra az Azure Machine Learning-ben.

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

## 8. Tesztelje a végpontot mintaadatokkal

Lekérünk néhány mintaadatot a teszt adathalmazból, és elküldjük az online végpontra inferenciára. Ezután megjelenítjük az előre jelzett címkéket a valós címkékkel együtt.

### Eredmények olvasása

1. Ez a Python szkript egy JSON Lines fájlt olvas be egy pandas DataFrame-be, véletlenszerű mintát vesz, és visszaállítja az indexet. Íme, mit csinál:

    - Beolvassa a ./ultrachat_200k_dataset/test_gen.jsonl fájlt egy pandas DataFrame-be. A read_json függvényt a lines=True argumentummal használja, mert a fájl JSON Lines formátumú, ahol minden sor egy külön JSON objektum.

    - Véletlenszerűen kiválaszt 1 sort a DataFrame-ből. A sample függvényt az n=1 argumentummal használja, hogy meghatározza a kiválasztandó sorok számát.

    - Visszaállítja a DataFrame indexét. A reset_index függvényt a drop=True argumentummal használja, hogy eldobja az eredeti indexet, és új, alapértelmezett egész szám indexet hozzon létre.

    - Megjeleníti a DataFrame első 2 sorát a head függvénnyel, 2-es argumentummal. Mivel azonban a DataFrame csak egy sort tartalmaz a mintavétel után, csak azt az egy sort jeleníti meg.

1. Összefoglalva, ez a szkript egy JSON Lines fájlt olvas be egy pandas DataFrame-be, véletlenszerűen kiválaszt egy sort, visszaállítja az indexet, és megjeleníti az első sort.

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

### JSON objektum létrehozása

1. Ez a Python szkript egy JSON objektumot hoz létre meghatározott paraméterekkel, és elmenti egy fájlba. Íme, mit csinál:

    - Importálja a json modult, amely JSON adatok kezelésére szolgáló funkciókat biztosít.

    - Létrehoz egy parameters nevű szótárat, amely kulcsokat és értékeket tartalmaz, amelyek egy gépi tanulási modell paramétereit képviselik. A kulcsok: "temperature", "top_p", "do_sample" és "max_new_tokens", értékeik rendre 0.6, 0.9, True és 200.

    - Létrehoz egy másik test_json nevű szótárat két kulccsal: "input_data" és "params". Az "input_data" értéke egy másik szótár, amely tartalmazza az "input_string" és "parameters" kulcsokat. Az "input_string" értéke egy
- Megnyit egy sample_score.json nevű fájlt

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

### Végpont meghívása

1. Ez a Python szkript egy online végpontot hív meg az Azure Machine Learning-ben, hogy értékeljen egy JSON fájlt. Íme, mit csinál pontosan:

    - Meghívja a workspace_ml_client objektum online_endpoints tulajdonságának invoke metódusát. Ezt a metódust arra használják, hogy kérés küldjenek egy online végponthoz, és választ kapjanak.

    - Megadja a végpont és a telepítés nevét az endpoint_name és deployment_name argumentumokkal. Ebben az esetben a végpont neve az online_endpoint_name változóban van tárolva, a telepítés neve pedig "demo".

    - Megadja a pontozandó JSON fájl elérési útját a request_file argumentummal. Ebben az esetben a fájl a ./ultrachat_200k_dataset/sample_score.json.

    - Elmenti a végpont válaszát a response változóba.

    - Kiírja a nyers választ.

1. Összefoglalva, ez a szkript egy online végpontot hív meg az Azure Machine Learning-ben, hogy értékeljen egy JSON fájlt, majd kiírja a választ.

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

## 9. Az online végpont törlése

1. Ne felejtsd el törölni az online végpontot, különben a végpont által használt számítási erőforrások számlálója tovább fut. Ez a Python kódsor egy online végpont törlését indítja el az Azure Machine Learning-ben. Íme, mit csinál pontosan:

    - Meghívja a workspace_ml_client objektum online_endpoints tulajdonságának begin_delete metódusát. Ezt a metódust arra használják, hogy elindítsák egy online végpont törlését.

    - Megadja a törlendő végpont nevét a name argumentummal. Ebben az esetben a végpont neve az online_endpoint_name változóban van tárolva.

    - Meghívja a wait metódust, hogy megvárja a törlési művelet befejeződését. Ez egy blokkoló művelet, vagyis megakadályozza, hogy a szkript folytatódjon, amíg a törlés be nem fejeződik.

    - Összefoglalva, ez a kódsor elindítja egy online végpont törlését az Azure Machine Learning-ben, és megvárja a művelet befejezését.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.