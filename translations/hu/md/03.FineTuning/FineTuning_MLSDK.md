## Hogyan használjuk az Azure ML rendszerregiszter chat-komplettációs komponenseit egy modell finomhangolásához

Ebben a példában elvégezzük a Phi-3-mini-4k-instruct modell finomhangolását egy két ember közötti beszélgetés befejezésére az ultrachat_200k adatállomány felhasználásával.

![MLFineTune](../../../../translated_images/hu/MLFineTune.928d4c6b3767dd35.webp)

A példában megmutatjuk, hogyan lehet finomhangolást végezni az Azure ML SDK és Python segítségével, majd hogyan lehet a finomhangolt modellt online végpontra telepíteni valós idejű következtetéshez.

### Tanulóadatok

Az ultrachat_200k adathalmazt fogjuk használni. Ez az UltraChat adathalmaz erősen szűrt változata, és a Zephyr-7B-β, egy csúcstechnológiás 7 milliárd paraméteres csevegőmodell kiképzéséhez használták.

### Modell

A Phi-3-mini-4k-instruct modellt fogjuk használni, hogy megmutassuk, hogyan tudja a felhasználó finomhangolni a modellt chat-komplettációs feladatra. Ha ezt a jegyzetfüzetet egy adott modellkártyáról nyitotta meg, ne feledje cserélni a modellspecifikus nevet.

### Feladatok

- Válasszunk modellt finomhangolásra.
- Válasszunk és vizsgáljunk meg tanulóadatokat.
- Konfiguráljuk a finomhangolási munkát.
- Futtassuk a finomhangolási munkát.
- Tekintsük át a tanulási és értékelési mutatókat.
- Regisztráljuk a finomhangolt modellt.
- Telepítsük a finomhangolt modellt valós idejű következtetésre.
- Takarítsuk el az erőforrásokat.

## 1. Előkészületek beállítása

- Telepítsük a függőségeket
- Csatlakozzunk az AzureML munkaterülethez. További információ a SDK hitelesítés beállításáról. Cserélje ki az alábbi <WORKSPACE_NAME>, <RESOURCE_GROUP> és <SUBSCRIPTION_ID> értékeket.
- Csatlakozzunk az azureml rendszerregiszterhez
- Állítsunk be opcionális kísérletnevet
- Ellenőrizzük vagy hozzunk létre számítási erőforrást.

> [!NOTE]
> Követelmény, hogy egyetlen GPU csomópont több GPU kártyát is tartalmazhat. Például a Standard_NC24rs_v3 csomópontban 4 NVIDIA V100 GPU van, míg a Standard_NC12s_v3-ban 2 NVIDIA V100 GPU található. Ezt az információt a dokumentációban találja. A csomópontra jutó GPU kártyák számát az alábbi gpus_per_node paraméterben kell megadni. Ennek helyes beállítása biztosítja az összes GPU kihasználását a csomópontban. Az ajánlott GPU számítási SKU-k itt és itt találhatók.

### Python könyvtárak

Telepítse a függőségeket az alábbi cella futtatásával. Ez nem opcionális lépés, ha új környezetben futtat.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interakció az Azure ML-lel

1. Ez a Python szkript az Azure Machine Learning (Azure ML) szolgáltatással való interakcióra szolgál. A lényeg:

    - Betölti az azure.ai.ml, azure.identity és azure.ai.ml.entities csomagok szükséges moduljait. Importálja továbbá a time modult.

    - Megpróbál hitelesíteni a DefaultAzureCredential() használatával, mely egyszerűsített hitelesítést biztosít az Azure felhőben futó alkalmazások gyors fejlesztéséhez. Ha ez nem sikerül, az InteractiveBrowserCredential() fut le, amely interaktív bejelentkezést kínál.

    - Ezután megpróbál egy MLClient példányt létrehozni a from_config metódussal, amely az alapértelmezett konfigurációs fájlból (config.json) olvassa be a beállításokat. Sikertelenség esetén manuálisan hozza létre az MLClient-et az előfizetés azonosító, erőforráscsoport és munkaterület megadásával.

    - Létrehoz egy másik MLClient példányt az Azure ML "azureml" nevű rendszerregiszteréhez. Ebben a regiszterben tárolódnak a modellek, finomhangolási folyamatok és környezetek.

    - Beállítja az experiment_name változót "chat_completion_Phi-3-mini-4k-instruct" értékre.

    - Egyedi időbélyeget generál az aktuális idő lebegőpontos számként való lekérésével, majd egész számmá és karakterlánccá alakításával. Ezt a timestamp-et egyedi nevek és verziók létrehozásához használhatja.

    ```python
    # Importálja a szükséges modulokat az Azure ML-ből és az Azure Identity-ból
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Importálja az idő modult
    
    # Próbáljon meg hitelesítést végezni a DefaultAzureCredential használatával
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Ha a DefaultAzureCredential meghiúsul, használja az InteractiveBrowserCredential-et
        credential = InteractiveBrowserCredential()
    
    # Próbáljon meg létrehozni egy MLClient példányt az alapértelmezett konfigurációs fájl segítségével
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Ha ez nem sikerül, hozzon létre egy MLClient példányt a részletek kézi megadásával
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Hozzon létre egy másik MLClient példányt az "azureml" nevű Azure ML regisztrációhoz
    # Ez a regisztráció tárolja a modelleket, finomhangolási folyamatokat és környezeteket
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Állítsa be a kísérlet nevét
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generáljon egy egyedi időbélyeget, amelyet neveknél és verzióknál lehet használni, ha egyedinek kell lennie
    timestamp = str(int(time.time()))
    ```

## 2. Válasszon alapmodellt finomhangoláshoz

1. A Phi-3-mini-4k-instruct egy 3,8 milliárd paraméteres, könnyű, csúcstechnológiás, nyílt modell, amely az Phi-2-höz használt adathalmazokra épül. A modell a Phi-3 modellcsaládba tartozik, a Mini változat két változatban érhető el: 4K és 128K, ami a támogatott kontextushossz (tokenekben). A modellt finomhangolni kell a saját céljainkra. Ezeket a modelleket megtekintheti az AzureML Studio modellkatalógusában a chat-komplettációs feladatra szűrve. Ebben a példában a Phi-3-mini-4k-instruct modellt használjuk. Ha ezt a jegyzetfüzetet más modellhez nyitotta meg, kérjük, cserélje le a modellt és verziót ennek megfelelően.

> [!NOTE]
> a modell azonosító tulajdonsága. Ez kerül bemeneti paraméterként a finomhangolási munkához. Ez elérhető az Asset ID mezőként is az AzureML Studio Modellkatalógus modell részletei oldalán.

2. Ez a Python szkript az Azure Machine Learning (Azure ML) szolgáltatással kommunikál. A lényeg:

    - Beállítja a model_name értékét "Phi-3-mini-4k-instruct"-ra.

    - A registry_ml_client objektum models tulajdonságának get metódusával lekéri a megadott nevű modell legújabb verzióját az Azure ML rendszerregiszterből. A get metódust két argumentummal hívja meg: a modell nevével és egy címkével, amely az adott modell legújabb verziójának lekérését jelzi.

    - Kiír a konzolra egy üzenetet, amely tartalmazza a finomhangoláshoz használt modell nevét, verzióját és azonosítóját. Az üzenetet a format metódussal illeszti be a modell adatait, melyek a foundation_model objektum tulajdonságai.

    ```python
    # Állítsa be a modell nevét
    model_name = "Phi-3-mini-4k-instruct"
    
    # Szerezze be a modell legújabb verzióját az Azure ML nyilvántartásából
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Nyomtassa ki a modell nevét, verzióját és azonosítóját
    # Ezek az információk hasznosak a nyomon követéshez és hibakereséshez
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Létrehozunk egy számítási erőforrást a munkához

A finomhangolási munka CSAK GPU számításon fut. A számítási erőforrás mérete a modell méretétől függ, és a legtöbb esetben nehéz megtalálni a megfelelő számítást a feladathoz. Ebben a cellában segítünk a felhasználónak a megfelelő számítás kiválasztásában.

> [!NOTE]
> Az alábbi listán szereplő számítások a legoptimálisabb konfigurációval működnek. Bármilyen konfigurációs változtatás Cuda Out Of Memory hibához vezethet. Ilyen esetekben próbálja meg a számítást nagyobb méretűre frissíteni.

> [!NOTE]
> A számítási_cluster méretének kiválasztásánál győződjön meg arról, hogy az elérhető az Ön erőforráscsoportjában. Ha egy adott számítás nem érhető el, kérhető hozzáférés a számítási erőforrásokhoz.

### Finomhangolási támogatás ellenőrzése a modellen

1. Ez a Python szkript az Azure Machine Learning (Azure ML) modelljével kommunikál. A lényeg:

    - Importálja az ast modult, amely funkciókat biztosít a Python absztrakt szintaxisfa feldolgozásához.

    - Ellenőrzi, hogy a foundation_model objektumnak van-e olyan címkéje, hogy finetune_compute_allow_list. Az címkék az Azure ML-ben kulcs-érték párok, melyek szűrésre és rendezésre használhatók.

    - Ha létezik a finetune_compute_allow_list címke, az ast.literal_eval segítségével biztonságosan Python listává alakítja a címke értékét (ami sztring), és ezt a computes_allow_list változóhoz rendeli. Ezután kiír egy üzenetet, hogy a számítási erőforrást a listából válasszuk ki.

    - Ha nem létezik a finetune_compute_allow_list címke, akkor a computes_allow_list értékét None-ra állítja és kiír egy üzenetet, hogy ez a címke nincs a modell címkéi között.

    - Összességében a szkript egy meghatározott címkét keres a modell metaadataiban, értékét listává alakítja ha létezik, és ennek megfelelő visszajelzést ad.

    ```python
    # Importálja az ast modult, amely függvényeket biztosít a Python absztrakt szintaxis fa feldolgozásához
    import ast
    
    # Ellenőrizze, hogy a 'finetune_compute_allow_list' címke jelen van-e a modell címkéi között
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Ha a címke jelen van, használja az ast.literal_eval-t a címke értékének (egy string) biztonságos Python listává való feldolgozásához
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # String átalakítása Python listává
        # Üzenet nyomtatása, amely jelzi, hogy egy számítást kell létrehozni a listából
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ha a címke nincs jelen, állítsa be a computes_allow_list-et None értékre
        computes_allow_list = None
        # Üzenet nyomtatása, amely jelzi, hogy a 'finetune_compute_allow_list' címke nem része a modell címkéinek
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Számítási példány ellenőrzése

1. Ez a Python szkript az Azure Machine Learning (Azure ML) szolgáltatással kommunikál, és több ellenőrzést végez egy számítási példányon. A lényeg:

    - Megpróbálja lekérni azt a számítási példányt, amelynek a neve compute_cluster változóban van tárolva az Azure ML munkaterületéről. Ha a példány provisioning állapota "failed", hibát dob.

    - Ellenőrzi, hogy a computes_allow_list nem None-e. Ha nem, akkor a lista összes számítási méretét kisbetűssé alakítja, majd ellenőrzi, hogy a jelenlegi számítás mérete benne van-e a listában. Ha nincs, hibát dob.

    - Ha a computes_allow_list None, akkor ellenőrzi, hogy a számítási példány mérete szerepel-e a nem támogatott GPU VM méretek között. Ha igen, hibát dob.

    - Lekér egy listát az elérhető számítási méretekről a munkaterületen. Végigiterál ezen a listán, és ahol a név megegyezik a számítási példány méretével, lekéri a GPU-k számát és a gpu_count_found igazra áll.

    - Ha gpu_count_found igaz, kiírja a GPU-k számát a számítási példányban. Ha nem, hibát dob.

    - Összefoglalva, a szkript több ellenőrzést végez egy Azure ML munkaterületi számítási példányon, mint az állapot, a méret engedélyezett vagy tiltott listán való szereplése, és a GPU-k száma.
    
    ```python
    # Nyomtasd ki a kivétel üzenetét
    print(e)
    # Dobjon ValueError kivételt, ha a számítási méret nem érhető el a munkaterületen
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Szerezd meg a számítási példányt az Azure ML munkaterületről
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Ellenőrizd, hogy a számítási példány előállítási állapota "hibás"-e
    if compute.provisioning_state.lower() == "failed":
        # Dobjon ValueError kivételt, ha az előállítási állapot "hibás"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Ellenőrizd, hogy a computes_allow_list nem None-e
    if computes_allow_list is not None:
        # Alakítsd át a computes_allow_list-ben szereplő összes számítási méretet kisbetűssé
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Ellenőrizd, hogy a számítási példány mérete szerepel-e a computes_allow_list_lower_case listában
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Dobjon ValueError kivételt, ha a számítási példány mérete nem szerepel a computes_allow_list_lower_case listában
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Definiálj egy listát a nem támogatott GPU VM méretekről
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Ellenőrizd, hogy a számítási példány mérete szerepel-e a unsupported_gpu_vm_list-ben
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Dobjon ValueError kivételt, ha a számítási példány mérete szerepel a unsupported_gpu_vm_list-ben
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Inicializálj egy jelzőt, hogy megtudd, megtaláltad-e a számítási példány GPU számát
    gpu_count_found = False
    # Szerezz egy listát az összes elérhető számítási méretről a munkaterületen
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterálj végig az elérhető számítási méretek listáján
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Ellenőrizd, hogy a számítási méret neve egyezik-e a számítási példány méretével
        if compute_sku.name.lower() == compute.size.lower():
            # Ha igen, szerezd meg az adott számítási mérethez tartozó GPU számot, és állítsd a gpu_count_found értékét True-ra
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Ha a gpu_count_found True, írd ki a számítási példány GPU számát
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Ha a gpu_count_found False, dobj ValueError kivételt
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Válasszuk ki az adathalmazt a modell finomhangolásához

1. Az ultrachat_200k adathalmazt használjuk. Az adathalmaz négy részre van bontva, amelyek alkalmasak a felügyelt finomhangolásra (Supervised fine-tuning, sft). Ez a rangsorolás generálása (gen). Az egyes részekhez tartozó példák száma a következő:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. A következő néhány cella bemutatja az alapvető adatelőkészítést a finomhangoláshoz:

### Néhány adat sor megjelenítése

A mintát gyors lefutásra optimalizáltuk, ezért a train_sft és test_sft fájlok 5%-át tartalmazzák a már szűrt soroknak. Ez azt jelenti, hogy a finomhangolt modell pontossága alacsonyabb lesz, ezért nem javasolt valós alkalmazásban használni.
A download-dataset.py scriptet az ultrachat_200k adatállomány letöltésére és a finomhangolási pipeline komponens számára fogyasztható formátumra alakítására használjuk. Az adatbázis mérete miatt csak egy részét használjuk az adatbázisnak.

1. Az alábbi szkript csak az adatok 5%-át tölti le. Ez a dataset_split_pc paraméter növelésével módosítható.

> [!NOTE]
> Egyes nyelvi modellek különböző nyelvkódokat használnak, ezért az adatbázis oszlopai ennek megfelelően legyenek elnevezve.

1. Az adatok például így néznek ki
A chat-komplettációs adathalmaz parquet formátumban tárolódik, minden bejegyzés a következő séma szerint:

    - Ez egy JSON (JavaScript Object Notation) dokumentum, ami egy népszerű adatcsere formátum. Nem végrehajtható kód, hanem adatok tárolásának és átvitelének módja. Itt az összetétele:

    - "prompt": Ez a kulcs egy sztringet tartalmaz, amely egy feladatot vagy kérdést jelöl, amelyet egy MI asszisztenshez intéznek.

    - "messages": Ez a kulcs egy objektumokból álló tömböt tartalmaz. Minden objektum egy üzenetet jelöl a felhasználó és az MI-asszisztens közötti beszélgetésben. Minden üzenet objektumnak két kulcsa van:

    - "content": Ez a kulcs egy sztringet tartalmaz, az üzenet tartalmát.
    - "role": Ez a kulcs egy sztringet tartalmaz, amely az üzenet küldőjének szerepét jelöli. Lehet "user" vagy "assistant".
    - "prompt_id": Ez a kulcs egy sztring, amely az adott prompt egyedi azonosítója.

1. Ebben a specifikus JSON dokumentumban egy beszélgetés van ábrázolva, ahol egy felhasználó egy dystópikus történet főszereplőjének létrehozását kéri az MI-asszisztenstől. Az asszisztens válaszol, majd a felhasználó további részleteket kér. Az asszisztens ígéretet tesz a részletek megadására. Az egész beszélgetés egy adott prompt azonosítóhoz tartozik.

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

1. Ez a Python szkript egy dataset letöltésére használ egy segédscriptet, a download-dataset.py-t. A lényeg:

    - Importálja az os modult, amely hordozható módon biztosít operációs rendszerfüggő funkciókat.

    - Az os.system függvénnyel futtatja a download-dataset.py scriptet shell környezetben a következő parancssori argumentumokkal: az adatállomány neve (HuggingFaceH4/ultrachat_200k), a letöltés helye (ultrachat_200k_dataset) és az adatállományból kinyert százalék (5). Az os.system visszatérési értéke az exit státusz, amelyet az exit_status változóban tárol.

    - Ellenőrzi, hogy az exit_status nem 0-e. Az Unix-szerű rendszerekben 0 jelenti a sikeres lefutást, míg bármely más érték hibát jelez. Ha az exit_status nem 0, akkor kivételt dob hibaüzenettel, hogy a dataset letöltés hibás volt.

    - Összességében a script egy parancsot futtat egy dataset letöltésére segédscript segítségével, és hibát jelez, ha a folyamat sikertelen.
    
    ```python
    # Importálja az os modult, amely lehetőséget biztosít az operációs rendszer függő funkciók használatára
    import os
    
    # Használja az os.system függvényt a download-dataset.py script futtatására a shell-ben, meghatározott parancssori argumentumokkal
    # Az argumentumok megadják a letöltendő adatállományt (HuggingFaceH4/ultrachat_200k), a letöltési könyvtárat (ultrachat_200k_dataset) és az adatállomány felosztásának százalékát (5)
    # Az os.system függvény visszaadja a végrehajtott parancs kilépési állapotát; ezt az értéket az exit_status változóban tárolja
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Ellenőrzi, hogy az exit_status nem 0-e
    # Unix-szerű operációs rendszerekben a 0 kilépési állapot általában a parancs sikerességét jelzi, míg bármely más érték hibára utal
    # Ha az exit_status nem 0, akkor kivételt dob egy üzenettel, amely jelzi, hogy hiba történt az adatállomány letöltése során
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Adatok betöltése DataFrame-be

1. Ez a Python szkript egy JSON Lines fájlt tölt be egy pandas DataFrame-be és megjeleníti az első 5 sort. A lényeg:

    - Importálja a pandas könyvtárat, amely egy erőteljes adatkezelési és elemzési könyvtár.

    - Beállítja a pandas megjelenítési opcióiban a maximális oszlopszélességet 0-ra. Ez azt jelenti, hogy a DataFrame nyomtatásakor az oszlop teljes szövege levágás nélkül jelenik meg.
- A pd.read_json függvényt használja az ultrachat_200k_dataset könyvtárból a train_sft.jsonl fájl betöltésére egy DataFrame-be. A lines=True argumentum azt jelzi, hogy a fájl JSON Lines formátumban van, ahol minden sor egy külön JSON objektum.

- A head metódust használja a DataFrame első 5 sorának megjelenítésére. Ha a DataFrame kevesebb, mint 5 sort tartalmaz, akkor mindet megjeleníti.

- Összefoglalva, ez a szkript egy JSON Lines fájlt tölt be egy DataFrame-be, és az első 5 sort jeleníti meg a teljes oszlopszöveggel.
    
    ```python
    # Importálja a pandas könyvtárat, amely egy hatékony adatmanipulációs és elemző könyvtár
    import pandas as pd
    
    # Beállítja a pandas megjelenítési opciók maximális oszlopszélességét 0-ra
    # Ez azt jelenti, hogy az egyes oszlopok teljes szövege megjelenik vágás nélkül, amikor a DataFrame ki van nyomtatva
    pd.set_option("display.max_colwidth", 0)
    
    # Használja a pd.read_json függvényt, hogy betöltse a train_sft.jsonl fájlt az ultrachat_200k_dataset könyvtárból egy DataFrame-be
    # A lines=True argumentum azt jelzi, hogy a fájl JSON Lines formátumú, ahol minden sor egy külön JSON objektum
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Használja a head metódust a DataFrame első 5 sorának megjelenítéséhez
    # Ha a DataFrame kevesebb, mint 5 sort tartalmaz, az összes sor megjelenítésre kerül
    df.head()
    ```

## 5. Finomhangolási feladat beküldése a modellt és az adatokat bemenetként használva

Hozzon létre egy feladatot, amely a chat-completion pipeline komponenst használja. Tudjon meg többet a finomhangoláshoz támogatott összes paraméterről.

### Finomhangolási paraméterek meghatározása

1. A finomhangolási paraméterek két kategóriába csoportosíthatók - tanítási paraméterek, optimalizációs paraméterek

1. A tanítási paraméterek a tanítási aspektusokat határozzák meg, mint például -

    - Az alkalmazandó optimalizáló és ütemező
    - A finomhangolásban optimalizálandó mérőszám
    - Tanítási lépések száma, batch méret és így tovább
    - Az optimalizációs paraméterek segítenek a GPU memória optimalizálásában és a számítási erőforrások hatékony használatában.

1. Az alábbiakban néhány olyan paraméter látható, amelyek ehhez a kategóriához tartoznak. Az optimalizációs paraméterek modelltől függően változnak, és a modellhez csomagolva vannak ezen eltérések kezelésére.

    - DeepSpeed és LoRA engedélyezése
    - Vegyes precizitású tanítás engedélyezése
    - Több csomópontos tanítás engedélyezése

> [!NOTE]
> Felügyelt finomhangolás esetén előfordulhat az illeszkedés elvesztése vagy katasztrofális elfelejtés. Javasoljuk, hogy ellenőrizze ezt a problémát, és futtasson illeszkedési szakaszt a finomhangolás után.

### Finomhangolási paraméterek

1. Ez a Python szkript beállítja a gépi tanulási modell finomhangolásához szükséges paramétereket. Íme, mit csinál:

    - Alapértelmezett tanítási paramétereket állít be, mint például az epochok száma, az edzéshez és értékeléshez használt batch méret, tanulási ráta és tanulási ráta ütemező típusa.

    - Alapértelmezett optimalizációs paramétereket állít be, mint például a Layer-wise Relevance Propagation (LoRa) és DeepSpeed alkalmazása, illetve a DeepSpeed szakasz.

    - Összevonja a tanítási és optimalizációs paramétereket egyetlen szótárba, amelyet finetune_parameters néven tárol.

    - Ellenőrzi, hogy a foundation_model rendelkezik-e modell-specifikus alapértelmezett paraméterekkel. Ha igen, figyelmeztető üzenetet ír ki, és frissíti a finetune_parameters szótárat ezekkel a modell-specifikus alapértelmezett értékekkel. Az ast.literal_eval függvényt használja a modell-specifikus alapértelmezettek sztringből Python szótárrá alakítására.

    - Kiírja a finomhangoláshoz használt végső paraméterkészletet.

    - Összefoglalva, ez a szkript beállítja és megjeleníti a gépi tanulási modell finomhangolásához szükséges paramétereket, lehetőséget adva az alapértelmezett paraméterek modell-specifikus felülírására.

    ```python
    # Állítsa be az alapértelmezett tréning paramétereket, például a tréning epochok számát, a tréning és értékelés batch méreteit, a tanulási rátát és a tanulási ráta ütemező típusát
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Állítsa be az alapértelmezett optimalizációs paramétereket, például hogy alkalmazza-e a Layer-wise Relevance Propagation (LoRa) és a DeepSpeed funkciókat, valamint a DeepSpeed szintjét
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Egyesítse a tréning és optimalizációs paramétereket egy finetune_parameters nevű szótárba
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Ellenőrizze, hogy a foundation_model rendelkezik-e modell-specifikus alapértelmezett paraméterekkel
    # Ha igen, írjon ki egy figyelmeztető üzenetet, és frissítse a finetune_parameters szótárat ezekkel a modell-specifikus alapértelmezettekkel
    # Az ast.literal_eval függvény a modell-specifikus alapértelmezetteket konvertálja stringből Python szótárrá
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # konvertálja a stringet Python szótárrá
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Nyomtassa ki a futtatáshoz használt végső finomhangolási paramétereket
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Tanítási Pipeline

1. Ez a Python szkript egy függvényt definiál, amely gépi tanulási tanítási pipeline megjelenítendő nevét generálja, majd meghívja ezt a függvényt a név generálására és kiírására. Íme, mit csinál:

1. Definiálja a get_pipeline_display_name függvényt, amely egy megjelenítendő nevet generál különböző, a tanítási pipeline-hoz kapcsolódó paraméterek alapján.

1. A függvény belsejében kiszámítja a teljes batch méretet az egy eszközön lévő batch méret, a gradiens akumulációs lépések száma, az egy csomóponton lévő GPU-k száma és a finomhangoláshoz használt csomópontok száma szorzataként.

1. Lekéri az egyéb paramétereket, például a tanulási ráta ütemező típusát, hogy alkalmazzák-e a DeepSpeed-et, a DeepSpeed szakaszt, alkalmazzák-e a Layer-wise Relevance Propagation (LoRa) kérelmet, a megtartandó modell ellenőrzőpontok darabszámának korlátját, és a maximális szekvencia hosszát.

1. Összeállít egy sztringet, amely tartalmazza ezeket az összes paramétert kötőjellel elválasztva. Ha DeepSpeed vagy LoRa alkalmazva van, a sztring tartalmazza a "ds" követve a DeepSpeed szakaszt, vagy "lora" részt, egyébként "nods" vagy "nolora" részt.

1. A függvény visszaadja ezt a sztringet, amely a tanítási pipeline megjelenítendő neveként szolgál.

1. A függvény definiálása után meghívja azt, hogy generálja a megjelenítendő nevet, amelyet aztán kiír.

1. Összefoglalva, ez a szkript megjelenítendő nevet generál egy gépi tanulási tanítási pipeline-hoz különböző paraméterek alapján, majd kiírja ezt a nevet.

    ```python
    # Definiáljon egy függvényt a betanító folyamat megjelenítési nevének generálásához
    def get_pipeline_display_name():
        # Számítsa ki az összesített batch méretet a készülékenkénti batch méret, a gradiens akumulációs lépések száma, a GPU-k száma csomópontonként és a finomhangoláshoz használt csomópontok száma szorzataként
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Szerezze be a tanulási ráta ütemező típusát
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Szerezze be, hogy alkalmaznak-e DeepSpeed-et
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Szerezze be a DeepSpeed szakaszt
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Ha DeepSpeed-et alkalmaznak, vegye fel a megjelenítési névbe a "ds"-t, utána a DeepSpeed szakaszt; ha nem, akkor a "nods"-t
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Szerezze be, hogy alkalmaznak-e Layer-wise Relevance Propagation-öt (LoRa)
        lora = finetune_parameters.get("apply_lora", "false")
        # Ha LoRa-t alkalmaznak, vegye fel a megjelenítési névbe az "lora"-t; ha nem, akkor a "nolora"-t
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Szerezze be a megőrzendő model checkpointok számára vonatkozó korlátot
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Szerezze be a maximális szekvencia hosszát
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Állítsa össze a megjelenítési nevet ezeknek a paramétereknek a kötőjellel elválasztott összefűzésével
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
    
    # Hívja meg a függvényt a megjelenítési név generálásához
    pipeline_display_name = get_pipeline_display_name()
    # Írja ki a megjelenítési nevet
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Pipeline konfigurálása

Ez a Python szkript gépi tanulási pipeline-t definiál és konfigurál az Azure Machine Learning SDK használatával. Íme, mit csinál:

1. Szükséges modulokat importál az Azure AI ML SDK-ból.

1. Lekéri a "chat_completion_pipeline" nevű pipeline komponenst a regiszterből.

1. Definiál egy pipeline feladatot az `@pipeline` dekorátorral és a `create_pipeline` függvénnyel. A pipeline neve a `pipeline_display_name` változó értékére van beállítva.

1. A `create_pipeline` függvényben a lekért pipeline komponenst különböző paraméterekkel inicializálja, beleértve a modell elérési útját, különböző cluster számítási erőforrásokat a különböző szakaszokhoz, az adatbontásokat a tanításhoz és teszteléshez, a finomhangoláshoz használt GPU-k számát és egyéb finomhangolási paramétereket.

1. Leképezi a finomhangolási feladat kimenetét a pipeline feladat kimenetére. Ez azért történik, hogy a finomhangolt modellt könnyen lehessen regisztrálni, ami szükséges a modell online vagy batch végpontra történő telepítéséhez.

1. Létrehozza a pipeline példányát a `create_pipeline` függvény meghívásával.

1. Beállítja a pipeline `force_rerun` beállítását `True` értékre, ami azt jelenti, hogy az előző feladatok gyorsítótárazott eredményeit nem használja fel.

1. Beállítja a pipeline `continue_on_step_failure` beállítását `False` értékre, ami azt jelenti, hogy a pipeline leáll, ha bármelyik lépés sikertelen.

1. Összefoglalva, ez a szkript egy gépi tanulási pipeline-t definiál és konfigurál egy chat befejezési feladathoz az Azure Machine Learning SDK használatával.

    ```python
    # Szükséges modulok importálása az Azure AI ML SDK-ból
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # A "chat_completion_pipeline" nevű pipeline komponenst lekéri a regiszterből
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # A pipeline feladat definiálása az @pipeline dekorátorral és a create_pipeline függvénnyel
    # A pipeline neve a pipeline_display_name értékre van állítva
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # A lekért pipeline komponenst inicializálja különböző paraméterekkel
        # Ezek tartalmazzák a modell elérési útját, a különböző szakaszokhoz tartozó számítási klasztereket, az adatbontásokat edzéshez és teszthez, a finomhangoláshoz használt GPU-k számát, valamint egyéb finomhangolási paramétereket
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Az adatbontásokat a paraméterekhez rendeli
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Tanítási beállítások
            number_of_gpu_to_use_finetuning=gpus_per_node,  # A számítási klaszter rendelkezésre álló GPUinak számára állítva
            **finetune_parameters
        )
        return {
            # A finomhangolási munka kimenetét összekapcsolja a pipeline munka kimenetével
            # Ez azért történik, hogy könnyen regisztrálhassuk a finomhangolt modellt
            # A modell regisztrálása szükséges a modell online vagy batch végpontra történő telepítéséhez
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Példányt hoz létre a pipeline-ból a create_pipeline függvény meghívásával
    pipeline_object = create_pipeline()
    
    # Ne használjon gyorsítótárazott eredményeket korábbi futtatásokból
    pipeline_object.settings.force_rerun = True
    
    # Állítsa a hiba esetén folytatás engedélyezését False-ra
    # Ez azt jelenti, hogy a pipeline leáll, ha bármelyik lépés hibát jelez
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Feladat benyújtása

1. Ez a Python szkript egy gépi tanulási pipeline feladatot nyújt be egy Azure Machine Learning munkaterületre, majd megvárja a feladat befejezését. Íme, mit csinál:

    - Meghívja a create_or_update metódust a workspace_ml_client jobs objektumán a pipeline feladat benyújtásához. A futtatandó pipeline az pipeline_object, míg az alá tartozó kísérlet a experiment_name.

    - Ezután meghívja a stream metódust a workspace_ml_client jobs objektumán, hogy megvárja a pipeline feladat befejezését. Az esemény, amire vár, a pipeline_job objektum name attribútuma.

    - Összefoglalva, ez a szkript egy gépi tanulási pipeline feladatot nyújt be egy Azure Machine Learning munkaterületre, majd megvárja a feladat befejezését.

    ```python
    # Küldje el a pipeline munkát az Azure Machine Learning munkaterületre
    # A futtatandó folyamatot a pipeline_object határozza meg
    # A kísérlet, amely alatt a munka fut, az experiment_name által van megadva
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Várjon a pipeline munka befejezésére
    # A várakozásra kijelölt munka a pipeline_job objektum name attribútuma által van meghatározva
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. A finomhangolt modell regisztrálása a munkaterületen

Regisztrálni fogjuk a modellt a finomhangolási feladat kimenetéből. Ez követi a leszármazási láncot a finomhangolt modell és a finomhangolási feladat között. A finomhangolási feladat pedig követi a leszármazási láncot az alapmodellhez, az adathoz és a tanítási kódhoz.

### A gépi tanulási modell regisztrálása

1. Ez a Python szkript egy gépi tanulási modellt regisztrál, amelyet egy Azure Machine Learning pipeline-ban tanítottak. Íme, mit csinál:

    - Szükséges modulokat importál az Azure AI ML SDK-ból.

    - Ellenőrzi, hogy elérhető-e a trained_model kimenet a pipeline feladatból, a workspace_ml_client jobs objektumán keresztül a get metódusával, és annak outputs attribútumával.

    - Összeállít egy elérési utat a tanított modellhez, a pipeline feladat nevének és az output ("trained_model") nevének formázásával.

    - Meghatároz egy nevet a finomhangolt modellhez, amely az eredeti modellnévhez hozzáfűzi a "-ultrachat-200k" kifejezést, és az esetleges perjeleket kötőjelekkel helyettesíti.

    - Előkészíti a modell regisztrálását egy Model objektum létrehozásával különböző paraméterekkel, beleértve a modell elérési útját, típusát (MLflow modell), nevét és verzióját, valamint leírását.

    - Regisztrálja a modellt a workspace_ml_client models objektumának create_or_update metódusával, melynek argumentuma a Model objektum.

    - Kiírja a regisztrált modellt.

1. Összefoglalva, ez a szkript egy gépi tanulási modellt regisztrál, amelyet Azure Machine Learning pipeline-ban tanítottak.
    
    ```python
    # Szükséges modulok importálása az Azure AI ML SDK-ból
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Ellenőrizze, hogy elérhető-e a `trained_model` kimenet a pipeline feladatból
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Útvonal létrehozása a betanított modellhez a pipeline feladat nevének és a kimenet ("trained_model") nevének formázásával
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # A finomhangolt modell nevének meghatározása az eredeti modellnévhez "-ultrachat-200k" hozzáfűzésével és a perjelek kötőjelre cserélésével
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # A modell regisztrálására való előkészítés Model objektum létrehozásával különféle paraméterekkel
    # Ezek közé tartozik a modell útvonala, a modell típusa (MLflow modell), a modell neve és verziója, valamint a modell leírása
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Verzióütközés elkerülése érdekében időbélyeg használata verzióként
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # A modell regisztrálása a workspace_ml_client models objektumának create_or_update metódusának hívásával a Model objektum argumentumként történő átadásával
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # A regisztrált modell kiíratása
    print("registered model: \n", registered_model)
    ```

## 7. A finomhangolt modell telepítése online végpontra

Az online végpontok tartós REST API-t biztosítanak, amely alkalmazásokkal integrálható a modell használatához.

### Végpont kezelése

1. Ez a Python szkript menedzselt online végpontot hoz létre egy regisztrált modellhez az Azure Machine Learningben. Íme, mit csinál:

    - Szükséges modulokat importál az Azure AI ML SDK-ból.

    - Egyedi nevet határoz meg az online végpontnak, amelyhez egy időbélyeget fűz hozzá az "ultrachat-completion-" sztringhez.

    - Előkészíti az online végpont létrehozását egy ManagedOnlineEndpoint objektum létrehozásával különböző paraméterekkel, beleértve a végpont nevét, leírását és hitelesítési módját ("key").

    - Létrehozza az online végpontot a workspace_ml_client begin_create_or_update metódusával a ManagedOnlineEndpoint objektummal, majd megvárja a művelet befejezését a wait metódussal.

1. Összefoglalva, ez a szkript menedzselt online végpontot hoz létre egy regisztrált modell számára az Azure Machine Learningben.

    ```python
    # A szükséges modulok importálása az Azure AI ML SDK-ból
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Egyedi név definiálása az online végponthoz, a "ultrachat-completion-" sztringhez egy időbélyeg hozzáfűzésével
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Az online végpont létrehozására való felkészülés egy ManagedOnlineEndpoint objektum létrehozásával különböző paraméterekkel
    # Ezek között szerepel a végpont neve, egy leírás a végpontról, és az azonosítási mód ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Az online végpont létrehozása a workspace_ml_client begin_create_or_update metódusának meghívásával, a ManagedOnlineEndpoint objektum átadásával
    # Ezután várakozás a létrehozási művelet befejezésére a wait metódus meghívásával
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Itt találja a telepítéshez támogatott SKU-k listáját - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Gépi tanulási modell telepítése

1. Ez a Python szkript egy regisztrált gépi tanulási modellt telepít menedzselt online végpontra az Azure Machine Learningben. Íme, mit csinál:

    - Importálja az ast modult, amely funkciókat biztosít a Python absztrakt szintaxisgráf feldolgozásához.

    - Beállítja a telepítéshez használt példány típusát "Standard_NC6s_v3"-ra.

    - Ellenőrzi, hogy a foundation_model tartalmazza-e az inference_compute_allow_list címkét. Ha igen, a címke értékét sztringből Python listává alakítja, majd hozzárendeli az inference_computes_allow_list változóhoz. Ha nincs, akkor az inference_computes_allow_list értéke None.

    - Ellenőrzi, hogy a megadott példány típus benne van-e az engedélyezett listában. Ha nincs, akkor üzenetet ír ki, amely kéri a felhasználót, hogy válasszon az engedélyezett listából.

    - Előkészíti a telepítést egy ManagedOnlineDeployment objektum létrehozásával, amely több paramétert tartalmaz, beleértve a telepítés nevét, a végpont nevét, a modell azonosítóját, az példány típusát és számát, az élőellenőrzési beállításokat és a kérelmi beállításokat.

    - Létrehozza a telepítést a workspace_ml_client begin_create_or_update metódusával a ManagedOnlineDeployment objektummal, majd megvárja a művelet befejezését a wait metódussal.

    - Beállítja a végpont forgalmát úgy, hogy a forgalom 100%-át a "demo" telepítéshez irányítja.

    - Frissíti a végpontot a workspace_ml_client begin_create_or_update metódusával az endpoint objektummal, majd megvárja a frissítés befejezését a result metódussal.

1. Összefoglalva, ez a szkript regisztrált gépi tanulási modellt telepít menedzselt online végpontra Azure Machine Learning környezetben.

    ```python
    # Importálja az ast modult, amely függvényeket biztosít a Python absztrakt szintaxis fáinak feldolgozásához
    import ast
    
    # Állítsa be a példány típusát a telepítéshez
    instance_type = "Standard_NC6s_v3"
    
    # Ellenőrizze, hogy a `inference_compute_allow_list` címke jelen van-e az alapmodellen
    if "inference_compute_allow_list" in foundation_model.tags:
        # Ha igen, alakítsa át a címke értékét stringből Python listává, és rendelje az `inference_computes_allow_list` változóhoz
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ha nem, állítsa az `inference_computes_allow_list` értékét `None`-ra
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Ellenőrizze, hogy a megadott példány típus szerepel-e az engedélyezési listában
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Készítse elő a telepítést egy `ManagedOnlineDeployment` objektum létrehozásával különböző paraméterekkel
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Hozza létre a telepítést azzal, hogy meghívja a `workspace_ml_client` `begin_create_or_update` metódusát a `ManagedOnlineDeployment` objektummal argumentumként
    # Ezután várja meg a létrehozási művelet befejeződését a `wait` metódus hívásával
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Állítsa be a végpont forgalmát úgy, hogy a forgalom 100%-át a "demo" telepítéshez irányítsa
    endpoint.traffic = {"demo": 100}
    
    # Frissítse a végpontot azzal, hogy meghívja a `workspace_ml_client` `begin_create_or_update` metódusát az `endpoint` objektummal argumentumként
    # Ezután várja meg a frissítési művelet befejeződését a `result` metódus hívásával
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. A végpont tesztelése mintaadatokkal

Lekérünk néhány minta adatot a teszt adatbázisból, és elküldjük az online végpontnak következtetésre. Ezután a pontozott címkéket megjelenítjük az igaz címkék mellett.

### Eredmények olvasása

1. Ez a Python szkript egy JSON Lines fájlt olvas be pandas DataFrame-be, véletlenszerű mintát vesz, majd visszaállítja a indexet. Íme, mit csinál:

    - Beolvassa a ./ultrachat_200k_dataset/test_gen.jsonl fájlt pandas DataFrame-be. A read_json függvényt használja a lines=True argumentummal, mert a fájl JSON Lines formátumban van, ahol minden sor egy külön JSON objektum.

    - Véletlenszerű mintát vesz egy sorral a DataFrame-ből. A sample függvényt az n=1 argumentummal használja a kiválasztandó véletlen sorok számának megadásához.

    - Visszaállítja a DataFrame indexét. A reset_index függvényt használja drop=True argumentummal az eredeti index elhagyásához és egy új, alapértelmezett egész számokból álló index létrehozásához.

    - Megjeleníti a DataFrame első 2 sorát a head függvénnyel 2 argumentummal. Mivel azonban a DataFrame mintavételezés után csak egy sort tartalmaz, csak azt az egy sort fogja megjeleníteni.

1. Összefoglalva, ez a szkript egy JSON Lines fájlt olvas be egy pandas DataFrame-be, egy sort véletlenszerűen kiválaszt, visszaállítja az indexet, majd megjeleníti az első sort.
    
    ```python
    # Pandas könyvtár importálása
    import pandas as pd
    
    # A JSON Lines fájl './ultrachat_200k_dataset/test_gen.jsonl' beolvasása pandas DataFrame-be
    # A 'lines=True' argumentum jelzi, hogy a fájl JSON Lines formátumú, ahol minden sor egy külön JSON objektum
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Véletlenszerűen kiválaszt egy sort a DataFrame-ből
    # Az 'n=1' argumentum megadja, hogy hány véletlenszerű sort válasszon ki
    test_df = test_df.sample(n=1)
    
    # A DataFrame indexének visszaállítása
    # A 'drop=True' argumentum jelzi, hogy az eredeti indexet el kell dobni, és helyette alapértelmezett egész szám értékű új indexet kell létrehozni
    # Az 'inplace=True' argumentum jelzi, hogy a DataFrame-et helyben módosítsuk (új objektum létrehozása nélkül)
    test_df.reset_index(drop=True, inplace=True)
    
    # Az első 2 sor megjelenítése a DataFrame-ből
    # Mivel azonban a DataFrame csak egy sort tartalmaz a mintavételezés után, ez csak azt az egy sort fogja megjeleníteni
    test_df.head(2)
    ```

### JSON objektum létrehozása

1. Ez a Python szkript egy adott paraméterekkel rendelkező JSON objektumot hoz létre és ment el fájlba. Íme, mit csinál:

    - Importálja a json modult, amely JSON adatok kezeléséhez szükséges funkciókat biztosít.
    - Létrehoz egy parameters nevű szótárat, amely a gépi tanulási modell paramétereit tartalmazza kulcs-érték párok formájában. A kulcsok a "temperature", "top_p", "do_sample" és "max_new_tokens", és a hozzájuk tartozó értékek rendre 0.6, 0.9, True és 200.

    - Létrehoz egy másik test_json nevű szótárat két kulccsal: "input_data" és "params". Az "input_data" értéke egy másik szótár, amely a "input_string" és "parameters" kulcsokat tartalmazza. Az "input_string" értéke egy lista, amely a test_df DataFrame első üzenetét tartalmazza. A "parameters" értéke az előzőleg létrehozott parameters szótár. A "params" értéke egy üres szótár.

    - Megnyit egy sample_score.json nevű fájlt
    
    ```python
    # Importáld a json modult, amely funkciókat biztosít JSON adatok kezeléséhez
    import json
    
    # Hozz létre egy `parameters` szótárat kulcsokkal és értékekkel, amelyek egy gépi tanulási modell paramétereit reprezentálják
    # A kulcsok "temperature", "top_p", "do_sample" és "max_new_tokens", és a megfelelő értékek rendre 0.6, 0.9, True és 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Hozz létre egy másik `test_json` szótárat két kulccsal: "input_data" és "params"
    # Az "input_data" értéke egy másik szótár, amelynek kulcsai "input_string" és "parameters"
    # Az "input_string" értéke egy lista, amely a `test_df` DataFrame első üzenetét tartalmazza
    # A "parameters" értéke a korábban létrehozott `parameters` szótár
    # A "params" értéke egy üres szótár
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Nyiss meg egy `sample_score.json` nevű fájlt írási módban a `./ultrachat_200k_dataset` könyvtárban
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Írd a `test_json` szótárat a fájlba JSON formátumban a `json.dump` függvény segítségével
        json.dump(test_json, f)
    ```

### Endpoint meghívása

1. Ez a Python szkript egy Azure Machine Learning online végpontját hívja meg egy JSON fájl pontozásához. Íme, mit csinál:

    - Meghívja a workspace_ml_client objektum online_endpoints tulajdonságának invoke metódusát. Ezt a metódust egy kérés elküldésére használják egy online végponthoz és a válasz fogadására.

    - Megadja a végpont nevét és a deployment nevét az endpoint_name és deployment_name argumentumokkal. Ebben az esetben a végpont neve az online_endpoint_name változóban van tárolva, a deployment neve pedig "demo".

    - Megadja a pontozandó JSON fájl elérési útját a request_file argumentummal. Ebben az esetben a fájl: ./ultrachat_200k_dataset/sample_score.json.

    - A végpont válaszát a response változóban tárolja.

    - Kiírja a nyers választ.

1. Összefoglalva: ez a szkript egy Azure Machine Learning online végpontját hívja meg egy JSON fájl pontozásához és kiírja a választ.

    ```python
    # Hívja meg az Azure Machine Learning online végpontját a `sample_score.json` fájl kiértékeléséhez
    # A `workspace_ml_client` objektum `online_endpoints` tulajdonságának `invoke` metódusát használjuk kérés küldésére az online végponthoz és válasz fogadására
    # Az `endpoint_name` argumentum az végpont nevét adja meg, amely az `online_endpoint_name` változóban van tárolva
    # A `deployment_name` argumentum a telepítés nevét adja meg, amely "demo"
    # A `request_file` argumentum a kiértékelendő JSON fájl elérési útját adja meg, amely `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Nyomtassa ki a végpont nyers válaszát
    print("raw response: \n", response, "\n")
    ```

## 9. Online végpont törlése

1. Ne felejtsd el törölni az online végpontot, különben a végpont által használt számítási erőforrás miatt a számlálás tovább fut. Ez a Python kód egy Azure Machine Learning online végpontját törli. Íme, mit csinál:

    - Meghívja a workspace_ml_client objektum online_endpoints tulajdonságának begin_delete metódusát. Ez a metódus az online végpont törlésének elindítására szolgál.

    - Megadja a törlendő végpont nevét a name argumentummal. Ebben az esetben a végpont neve az online_endpoint_name változóban van tárolva.

    - Meghívja a wait metódust, hogy megvárja a törlési művelet befejezését. Ez egy blokkoló művelet, ami azt jelenti, hogy a szkript addig nem folytatódik, amíg a törlés be nem fejeződik.

    - Összefoglalva: ez a sor elindítja egy Azure Machine Learning online végpont törlését, és megvárja a művelet befejeződését.

    ```python
    # Törölje az online végpontot az Azure Machine Learning-ben
    # A `workspace_ml_client` objektum `online_endpoints` tulajdonságának `begin_delete` módszerét használjuk az online végpont törlésének elindításához
    # A `name` argumentum az törlendő végpont nevét adja meg, amely az `online_endpoint_name` változóban van tárolva
    # Meghívjuk a `wait` metódust, hogy megvárjuk a törlési művelet befejezését. Ez egy blokkoló művelet, ami megakadályozza, hogy a szkript folytatódjon a törlés befejezéséig
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár igyekszünk pontos fordítást készíteni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum annak eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetében szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->