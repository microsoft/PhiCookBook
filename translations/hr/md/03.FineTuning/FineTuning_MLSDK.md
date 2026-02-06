## Kako koristiti chat-completion komponente iz Azure ML sustava registra za fino podešavanje modela

U ovom primjeru ćemo provesti fino podešavanje modela Phi-3-mini-4k-instruct za dovršavanje razgovora između 2 osobe koristeći ultrachat_200k skup podataka.

![MLFineTune](../../../../translated_images/hr/MLFineTune.928d4c6b3767dd35.webp)

Primjer će vam pokazati kako provesti fino podešavanje koristeći Azure ML SDK i Python, te zatim implementirati fino podešen model na online endpoint za real-time inference.

### Podaci za treniranje

Koristit ćemo ultrachat_200k skup podataka. Ovo je snažno filtrirana verzija UltraChat skupa podataka koji je korišten za trening Zephyr-7B-β, vrhunskog 7b chat modela.

### Model

Koristit ćemo Phi-3-mini-4k-instruct model kako bismo pokazali kako korisnik može fino podesiti model za zadatak chat dovršavanja. Ako ste otvorili ovu bilježnicu za određenu karticu modela, zapamtite da zamijenite specifično ime modela.

### Zadaci

- Odaberite model za fino podešavanje.
- Odaberite i istražite podatke za treniranje.
- Konfigurirajte posao finog podešavanja.
- Pokrenite posao finog podešavanja.
- Pregledajte metrike treniranja i evaluacije.
- Registrirajte fino podešeni model.
- Implementirajte fino podešeni model za real-time inference.
- Očistite resurse.

## 1. Postavljanje preduvjeta

- Instalirajte ovisnosti
- Povežite se na AzureML Workspace. Više saznajte u postavljanju SDK autentifikacije. Zamijenite <WORKSPACE_NAME>, <RESOURCE_GROUP> i <SUBSCRIPTION_ID> dolje.
- Povežite se na azureml sustavni registar
- Postavite neobavezni naziv eksperimenta
- Provjerite ili kreirajte računalo.

> [!NOTE]
> Zahtijeva jedan GPU čvor koji može imati više GPU kartica. Na primjer, u jednom čvoru Standard_NC24rs_v3 postoje 4 NVIDIA V100 GPU-a dok u Standard_NC12s_v3 postoje 2 NVIDIA V100 GPU-a. Pogledajte dokumentaciju za ove informacije. Broj GPU kartica po čvoru postavlja se u parametru gpus_per_node dolje. Ispravno postavljanje ove vrijednosti osigurava korištenje svih GPU-a u čvoru. Preporučene GPU compute SKU-ove možete pronaći ovdje i ovdje.

### Python knjižnice

Instalirajte ovisnosti pokretanjem sljedeće ćelije. Ovo nije neobavan korak ako pokrećete u novom okruženju.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interakcija s Azure ML

1. Ovaj Python skripta koristi se za interakciju sa Azure Machine Learning (Azure ML) servisom. Evo što radi:

    - Uvozi potrebne module iz paketa azure.ai.ml, azure.identity i azure.ai.ml.entities. Također uvozi modul time.

    - Pokušava autentificirati se koristeći DefaultAzureCredential(), što pruža pojednostavljeno iskustvo autentifikacije za brzo započinjanje razvoja aplikacija u Azure oblaku. Ako to ne uspije, koristi InteractiveBrowserCredential(), koji pruža interaktivni login prompt.

    - Zatim pokušava napraviti instancu MLClient koristeći metodu from_config, koja čita konfiguraciju iz zadane konfiguracijske datoteke (config.json). Ako to ne uspije, stvara MLClient ručno prosljeđujući subscription_id, resource_group_name i workspace_name.

    - Kreira još jedan MLClient, ovaj put za Azure ML registar pod nazivom "azureml". Taj registar služi za pohranu modela, fine-tuning pipelineova i okruženja.

    - Postavlja naziv eksperimenta na "chat_completion_Phi-3-mini-4k-instruct".

    - Generira jedinstveni vremenski žig pretvarajući trenutno vrijeme (u sekundama od epoh, kao decimalni broj) u cijeli broj pa potom u string. Taj žig može se koristiti za kreiranje jedinstvenih imena i verzija.

    ```python
    # Uvezi potrebne module iz Azure ML i Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Uvezi modul time
    
    # Pokušaj se autentificirati koristeći DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Ako DefaultAzureCredential ne uspije, koristi InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Pokušaj kreirati MLClient instancu koristeći zadani config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Ako to ne uspije, kreiraj MLClient instancu ručnim unosom podataka
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Kreiraj još jednu MLClient instancu za Azure ML registar nazvan "azureml"
    # Ovaj registar je mjesto gdje se pohranjuju modeli, fine-tuning pipeline-i i okruženja
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Postavi naziv eksperimenta
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generiraj jedinstveni timestamp koji se može koristiti za nazive i verzije koje trebaju biti jedinstvene
    timestamp = str(int(time.time()))
    ```

## 2. Odaberite osnovni model za fino podešavanje

1. Phi-3-mini-4k-instruct je lagani, vrhunski open model s 3,8 milijardi parametara, građen na skupovima podataka korištenim za Phi-2. Model pripada Phi-3 obitelji modela, i Mini verzija dolazi u dvjema varijantama: 4K i 128K, što je duljina konteksta (u tokenima) koju može podržati. Potrebno je fino podesiti model za naš specifični zadatak prije korištenja. Možete pregledati ove modele u Model Catalog u AzureML Studiu, filtrirajući prema zadatku chat dovršavanja. U ovom primjeru koristimo Phi-3-mini-4k-instruct model. Ako ste otvorili bilježnicu za drugi model, zamijenite ime i verziju modela sukladno tome.

> [!NOTE]
> id svojstvo modela. Ovo će se proslijediti kao ulaz u posao finog podešavanja. Također je dostupno kao polje Asset ID u detaljima modela u AzureML Studio Model Catalogu.

2. Ovaj Python skripta komunicira sa Azure Machine Learning (Azure ML) servisom. Evo što radi:

    - Postavlja model_name na "Phi-3-mini-4k-instruct".

    - Koristi metodu get iz svojstva models objekta registry_ml_client da preuzme najnoviju verziju modela sa zadanim imenom iz Azure ML registra. Metoda get se poziva s dva argumenta: ime modela i oznaka koja specificira da se treba dohvatiti najnovija verzija.

    - Ispisuje poruku u konzolu koja pokazuje ime, verziju i id modela koji će se koristiti za fino podešavanje. Metoda format niza koristi se za umetanje imena, verzije i id modela u poruku. Ime, verzija i id modela pristupaju se kao svojstva objekta foundation_model.

    ```python
    # Postavi ime modela
    model_name = "Phi-3-mini-4k-instruct"
    
    # Dohvati najnoviju verziju modela iz Azure ML registra
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Ispiši ime modela, verziju i ID
    # Ove informacije su korisne za praćenje i otklanjanje pogrešaka
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Kreirajte računalo koje će se koristiti za posao

Jobs fino podešavanja rade SAMO s GPU računalima. Veličina računala ovisi o veličini modela, a u većini slučajeva teško je odabrati ispravno računalo za posao. U ovoj ćeliji vodimo korisnika da odabere ispravno računalo za posao.

> [!NOTE]
> Computeri navedeni dolje rade s najoptimiziranijom konfiguracijom. Bilo kakve promjene konfiguracije mogu rezultirati Cuda Out Of Memory greškom. U takvim slučajevima pokušajte nadograditi računalo na veću veličinu.

> [!NOTE]
> Prilikom odabira compute_cluster_size dolje, provjerite da je računalo dostupno u vašoj resource grupi. Ako određeno računalo nije dostupno, možete zatražiti pristup računalnim resursima.

### Provjera podrške modela za fino podešavanje

1. Ovaj Python skripta komunicira s Azure Machine Learning (Azure ML) modelom. Evo što radi:

    - Uvozi modul ast, koji pruža funkcije za obradu stabala apstraktnog sintaksnog drveta Pythona.

    - Provjerava ima li objekt foundation_model (koji predstavlja model u Azure ML) oznaku pod imenom finetune_compute_allow_list. Oznake u Azure ML su ključ-vrijednost parovi koje možete kreirati i koristiti za filtriranje i sortiranje modela.

    - Ako je oznaka finetune_compute_allow_list prisutna, koristi ast.literal_eval funkciju za sigurno parsiranje vrijednosti oznake (string) u Python listu. Ta lista se zatim dodjeljuje varijabli computes_allow_list. Ispisuje poruku da se računalo treba kreirati iz navedene liste.

    - Ako oznaka finetune_compute_allow_list nije prisutna, postavlja computes_allow_list na None i ispisuje poruku da oznaka nije dio oznaka modela.

    - Ukratko, ovaj skripta provjerava određenu oznaku u metapodacima modela, pretvara vrijednost oznake u listu ako postoji, te pruža korisničke povratne informacije.

    ```python
    # Uvezi modul ast, koji pruža funkcije za obradu stabala apstraktne sintakse Python jezika
    import ast
    
    # Provjeri postoji li oznaka 'finetune_compute_allow_list' u oznakama modela
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Ako oznaka postoji, koristi ast.literal_eval za sigurno parsiranje vrijednosti oznake (string) u Python listu
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # pretvori string u Python listu
        # Ispiši poruku koja pokazuje da bi se trebao kreirati compute iz liste
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ako oznaka ne postoji, postavi computes_allow_list na None
        computes_allow_list = None
        # Ispiši poruku koja pokazuje da oznaka 'finetune_compute_allow_list' nije dio oznaka modela
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Provjera računalnog instanca

1. Ovaj Python skripta komunicira sa Azure Machine Learning (Azure ML) servisom i obavlja niz provjera na računarskoj instanci. Evo što radi:

    - Pokušava dohvatiti računalnu instancu s imenom pohranjenim u compute_cluster iz Azure ML workspace-a. Ako je stanje provisioning-a "failed", baci ValueError.

    - Provjerava ako je computes_allow_list različito od None. Ako jest, pretvara sve veličine računala na listi u mala slova te provjerava je li veličina trenutne računalne instance u toj listi. Ako nije, baci ValueError.

    - Ako je computes_allow_list None, provjerava je li veličina računala na listi nepodržanih GPU VM veličina. Ako jest, baci ValueError.

    - Dohvaća listu svih dostupnih veličina računala u workspace-u. Zatim prolazi kroz tu listu i za svaku veličinu, provjerava odgovara li nazivu veličina trenutne instance. Ako odgovara, dohvaća broj GPU-a za tu veličinu i postavlja gpu_count_found na True.

    - Ako je gpu_count_found True, ispisuje broj GPU-a u računalu. Ako nije, baca ValueError.

    - Ukratko, skripta provodi više provjera na računalnoj instanci u Azure ML workspace-u, uključujući provjeru statusa provisioning-a, veličine naspram dozvoljene liste ili liste zabrana, i broja GPU-a.

    ```python
    # Ispiši poruku iznimke
    print(e)
    # Podigni ValueError ako veličina računala nije dostupna u radnom prostoru
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Dohvati primjerak računala iz Azure ML radnog prostora
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Provjeri je li stanje provisioniranja primjerka računala "failed"
    if compute.provisioning_state.lower() == "failed":
        # Podigni ValueError ako je stanje provisioniranja "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Provjeri je li computes_allow_list različit od None
    if computes_allow_list is not None:
        # Pretvori sve veličine računala u computes_allow_list u mala slova
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Provjeri je li veličina primjerka računala u computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Podigni ValueError ako veličina primjerka računala nije u computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Definiraj listu nepodržanih GPU VM veličina
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Provjeri je li veličina primjerka računala u unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Podigni ValueError ako je veličina primjerka računala u unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Inicijaliziraj zastavicu za provjeru je li broj GPU-ova u primjerku računala pronađen
    gpu_count_found = False
    # Dohvati listu svih dostupnih veličina računala u radnom prostoru
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iteriraj kroz listu dostupnih veličina računala
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Provjeri odgovara li naziv veličine računala veličini primjerka računala
        if compute_sku.name.lower() == compute.size.lower():
            # Ako odgovara, dohvati broj GPU-ova za tu veličinu računala i postavi gpu_count_found na True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Ako je gpu_count_found True, ispiši broj GPU-ova u primjerku računala
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Ako je gpu_count_found False, podigni ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Odaberite skup podataka za fino podešavanje modela

1. Koristimo ultrachat_200k skup podataka. Skup ima četiri podijela, prikladna za Supervised fine-tuning (sft).
Generacijsko rangiranje (gen). Broj primjera po podijelu prikazan je kako slijedi:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Sljedeće ćelije pokazuju osnovnu pripremu podataka za fino podešavanje:

### Prikaz nekoliko redaka podataka

Želimo da primjer brzo radi, stoga spremamo train_sft, test_sft datoteke koje sadrže 5% već isječenih redaka. To znači da će fino podešeni model imati manju točnost, stoga ne treba biti korišten u stvarnim uvjetima.
download-dataset.py se koristi za preuzimanje ultrachat_200k skupa podataka i pretvaranje skupa podataka u format prihvatljiv za fine-tune pipeline komponente. Također, budući da je skup podataka velik, ovdje imamo samo dio skupa podataka.

1. Pokretanje sljedećeg skriptnog bloka preuzima samo 5% podataka. To se može povećati promjenom parametra dataset_split_pc na željeni postotak.

> [!NOTE]
> Neki jezični modeli imaju različite jezične kodove pa bi nazivi stupaca u skupu podataka trebali to odražavati.

1. Evo primjera kako podaci trebaju izgledati
Chat-completion skup podataka pohranjen je u parquet formatu s unosima prema sljedećoj shemi:

    - Ovo je JSON (JavaScript Object Notation) dokument, popularni format za razmjenu podataka. Nije izvršni kod, već način za pohranu i prenošenje podataka. Evo raspodjele njegove strukture:

    - "prompt": Ovaj ključ drži string vrijednost koja predstavlja zadatak ili pitanje postavljeno AI asistentu.

    - "messages": Ovaj ključ drži niz objekata. Svaki objekt predstavlja poruku u razgovoru između korisnika i AI asistenta. Svaka poruka ima dva ključa:

    - "content": Drži string vrijednost sadržaja poruke.
    - "role": Drži string vrijednost koja označava ulogu entiteta koji je poslao poruku. Može biti "user" ili "assistant".
    - "prompt_id": Drži string vrijednost koja predstavlja jedinstveni identifikator prompta.

1. U ovom JSON dokumentu predstavlja se razgovor gdje korisnik traži od AI asistenta da stvori protagoniste za distopijsku priču. Asistent odgovara, a korisnik traži više detalja. Asistent pristaje dati dodatne informacije. Cijeli razgovor povezan je s određenim ID-jem prompta.

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

### Preuzimanje podataka

1. Ovaj Python skripta koristi se za preuzimanje skupa podataka pomoću pomoćnog skripta download-dataset.py. Evo što radi:

    - Uvozi modul os koji pruža prenosivu funkcionalnost ovisnu o operacijskom sustavu.

    - Koristi os.system funkciju za pokretanje download-dataset.py skripte u ljusci s određenim argumentima. Argumenti specificiraju koji skup podataka preuzeti (HuggingFaceH4/ultrachat_200k), direktorij za spremanje (ultrachat_200k_dataset) i postotak podijele skupa podataka (5). os.system vraća status izlaza naredbe koji se sprema u exit_status varijablu.

    - Provjerava je li exit_status različit od 0. U Unix-sličnim OS-ovima, status 0 obično znači da je naredba uspješno izvršena, dok svaki drugi broj označava grešku. Ako je exit_status različit od 0, podiže Exception s porukom o grešci prilikom preuzimanja skupa podataka.

    - Ukratko, skripta pokreće naredbu za preuzimanje skupa podataka korištenjem pomoćnog skripta, te podiže iznimku ako naredba ne uspije.

    ```python
    # Uvoz modula os, koji pruža način korištenja funkcionalnosti ovisnih o operativnom sustavu
    import os
    
    # Koristite funkciju os.system za pokretanje skripte download-dataset.py u ljusci s određenim argumentima iz naredbenog retka
    # Argumenti specificiraju skup podataka za preuzimanje (HuggingFaceH4/ultrachat_200k), direktorij za preuzimanje (ultrachat_200k_dataset) i postotak skupa podataka za podjelu (5)
    # Funkcija os.system vraća izlazni status izvršene naredbe; taj status se sprema u varijablu exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Provjerite je li exit_status različit od 0
    # U Unix-sličnim operativnim sustavima, izlazni status 0 obično znači da je naredba uspjela, dok bilo koji drugi broj označava pogrešku
    # Ako exit_status nije 0, baci Exception s porukom koja ukazuje na pogrešku pri preuzimanju skupa podataka
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Učitavanje podataka u DataFrame

1. Ovaj Python skripta učitava JSON Lines datoteku u pandas DataFrame i prikazuje prvih 5 redaka. Evo što radi:

    - Uvozi pandas biblioteku, moćan alat za manipulaciju i analizu podataka.

    - Postavlja maksimalnu širinu stupca za pandasove opcije prikaza na 0. To znači da će se prikazati cijeli tekst svakog stupca bez skraćivanja kada se DataFrame ispiše.
    - Koristi funkciju pd.read_json za učitavanje datoteke train_sft.jsonl iz direktorija ultrachat_200k_dataset u DataFrame. Argument lines=True označava da je datoteka u JSON Lines formatu, gdje je svaki redak poseban JSON objekt.

    - Koristi metodu head za prikaz prvih 5 redaka DataFrame-a. Ako DataFrame ima manje od 5 redaka, prikazat će ih sve.

    - Ukratko, ovaj skript učitava JSON Lines datoteku u DataFrame i prikazuje prvih 5 redaka s punim tekstom stupaca.
    
    ```python
    # Uvezi pandas biblioteku, koja je moćna biblioteka za manipulaciju i analizu podataka
    import pandas as pd
    
    # Postavi maksimalnu širinu stupca za pandas prikaz opcije na 0
    # To znači da će se cijeli tekst svakog stupca prikazati bez skraćivanja kada se DataFrame ispiše
    pd.set_option("display.max_colwidth", 0)
    
    # Koristi pd.read_json funkciju za učitavanje datoteke train_sft.jsonl iz direktorija ultrachat_200k_dataset u DataFrame
    # Argument lines=True označava da je datoteka u JSON Lines formatu, gdje je svaki redak zaseban JSON objekt
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Koristi metodu head za prikaz prvih 5 redaka DataFramea
    # Ako DataFrame ima manje od 5 redaka, prikazat će ih sve
    df.head()
    ```

## 5. Pošaljite posao fino podešavanja koristeći model i podatke kao ulaze

Kreirajte posao koji koristi komponentu pipeline-a za chat-dovršavanje. Saznajte više o svim parametrima koje podržava fino podešavanje.

### Definirajte parametre finog podešavanja

1. Parametri finog podešavanja mogu se podijeliti u 2 kategorije - parametri treninga, parametri optimizacije

1. Parametri treninga definiraju aspekte treninga poput -

    - Optimizator, scheduler koji se koristi
    - Metriku koju treba optimizirati pri finom podešavanju
    - Broj trening koraka i veličinu batcha i slično
    - Parametri optimizacije pomažu u optimiziranju GPU memorije i učinkovitoj upotrebi računalnih resursa.

1. Ispod su neki od parametara koji pripadaju ovoj kategoriji. Parametri optimizacije razlikuju se za svaki model i pakirani su s modelom za upravljanje tim razlikama.

    - Omogućite deepspeed i LoRA
    - Omogućite trening miješane preciznosti
    - Omogućite trening na više čvorova

> [!NOTE]
> Supervizirano fino podešavanje može rezultirati gubitkom usklađenosti ili katastrofalnim zaboravljanjem. Preporučujemo provjeru ovog problema i pokretanje faze usklađivanja nakon finog podešavanja.

### Parametri finog podešavanja

1. Ovaj Python skript postavlja parametre za fino podešavanje strojnog modela. Evo pregleda što radi:

    - Postavlja zadane parametre treninga poput broja epoha treninga, veličina batcha za trening i evaluaciju, stopu učenja i tip schedulera stope učenja.

    - Postavlja zadane parametre optimizacije poput primjene Layer-wise Relevance Propagation (LoRa) i DeepSpeed, te stupanj DeepSpeed-a.

    - Kombinira parametre treninga i optimizacije u jedinstveni rječnik nazvan finetune_parameters.

    - Provjerava ima li foundation_model bilo kakve model-specifične zadane parametre. Ako ih ima, ispisuje upozorenje i ažurira rječnik finetune_parameters s tim model-specifičnim zadanim vrijednostima. Funkcija ast.literal_eval koristi se za pretvaranje model-specifičnih zadanih vrijednosti iz stringa u Python rječnik.

    - Ispisuje konačni skup parametara za fino podešavanje koji će se koristiti za izvođenje.

    - Ukratko, ovaj skript postavlja i prikazuje parametre za fino podešavanje strojnog modela s mogućnošću zamjene zadanih parametara model-specifičnim.

    ```python
    # Postavi zadane parametre treniranja kao što su broj epoha treniranja, veličine batch-eva za treniranje i evaluaciju, brzina učenja i tip raspoređivača brzine učenja
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Postavi zadane parametre optimizacije kao što su primjena Layer-wise Relevance Propagation (LoRa) i DeepSpeed, te DeepSpeed faza
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Spoji parametre treniranja i optimizacije u jedan rječnik pod nazivom finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Provjeri ima li foundation_model neke specifične zadanosti modela
    # Ako ima, ispiši poruku upozorenja i ažuriraj finetune_parameters rječnik s tim specifičnim zadanim vrijednostima modela
    # Funkcija ast.literal_eval se koristi za pretvaranje specifičnih zadanosti modela iz stringa u Python rječnik
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # pretvori string u Python rječnik
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Ispiši konačni skup parametara za fino podešavanje koji će se koristiti za pokretanje
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline za trening

1. Ovaj Python skript definira funkciju za generiranje naziva prikaza za pipeline trening strojnog učenja, a zatim poziva tu funkciju da generira i ispiše naziv prikaza. Evo pregleda što radi:

1. Definirana je funkcija get_pipeline_display_name. Ova funkcija generira naziv prikaza na temelju različitih parametara povezanih s pipeline-om za trening.

1. Unutar funkcije izračunava se ukupna veličina batcha množenjem veličine batcha po uređaju, broja koraka akumulacije gradijenta, broja GPU-a po čvoru i broja čvorova korištenih za fino podešavanje.

1. Dohvaćaju se razni drugi parametri poput tipa schedulera stope učenja, primjene DeepSpeed-a, stupnja DeepSpeed-a, primjene Layer-wise Relevance Propagation (LoRa), ograničenja broja spremljenih checkpointova modela te maksimalne duljine sekvence.

1. Konstruira se niz koji uključuje sve te parametre, odvojene crticama. Ako se primjenjuje DeepSpeed ili LoRa, niz uključuje "ds" praćeno stupnjem DeepSpeed-a ili "lora". Ako se ne primjenjuju, uključuje "nods" ili "nolora".

1. Funkcija vraća taj niz koji služi kao naziv prikaza za pipeline treninga.

1. Nakon definiranja funkcije, ona se poziva da generira naziv prikaza, koji se zatim ispisuje.

1. Ukratko, ovaj skript generira naziv prikaza za pipeline trening strojnog učenja na temelju različitih parametara i zatim ispisuje taj naziv prikaza.

    ```python
    # Definirajte funkciju za generiranje prikaznog imena za trening pipeline
    def get_pipeline_display_name():
        # Izračunajte ukupnu veličinu batcha množenjem veličine batcha po uređaju, broja koraka akumulacije gradijenta, broja GPU-ova po čvoru i broja čvorova korištenih za fino podešavanje
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Dohvatite tip raspoređivača stope učenja
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Dohvatite je li primijenjen DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Dohvatite DeepSpeed razinu
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Ako je DeepSpeed primijenjen, uključite "ds" praćeno DeepSpeed razinom u prikazno ime; ako nije, uključite "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Dohvatite je li primijenjeno slojevito relevantno propagiranje (LoRa)
        lora = finetune_parameters.get("apply_lora", "false")
        # Ako je LoRa primijenjena, uključite "lora" u prikazno ime; ako nije, uključite "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Dohvatite ograničenje na broj model checkpoints koje treba zadržati
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Dohvatite maksimalnu duljinu sekvence
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Konstruirajte prikazno ime spajanjem svih ovih parametara, odvojenih crticama
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
    
    # Pozovite funkciju za generiranje prikaznog imena
    pipeline_display_name = get_pipeline_display_name()
    # Ispišite prikazno ime
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Konfiguriranje pipeline-a

Ovaj Python skript definira i konfigurira pipeline strojnog učenja koristeći Azure Machine Learning SDK. Evo pregleda što radi:

1. Uvozi potrebne module iz Azure AI ML SDK-a.

1. Dohvaća komponentu pipeline-a nazvanu "chat_completion_pipeline" iz registra.

1. Definira posao pipeline-a koristeći dekorator `@pipeline` i funkciju `create_pipeline`. Naziv pipeline-a postavljen je na `pipeline_display_name`.

1. Unutar funkcije `create_pipeline` inicijalizira dohvaćenu komponentu pipeline-a s raznim parametrima, uključujući putanju do modela, računalne klastere za različite faze, podjele dataset-a za trening i testiranje, broj GPU-a za fino podešavanje i ostale parametre finog podešavanja.

1. Mapira izlaz iz posla finog podešavanja na izlaz pipeline posla. To je učinjeno kako bi se fino podešavani model mogao lako registrirati, što je potrebno za raspoređivanje modela na online ili batch endpoint.

1. Kreira instancu pipeline-a pozivom funkcije `create_pipeline`.

1. Postavlja postavku `force_rerun` pipeline-a na `True`, što znači da se neće koristiti rezultati iz predmemorije prethodnih poslova.

1. Postavlja postavku `continue_on_step_failure` pipeline-a na `False`, što znači da će pipeline stati ako bilo koji korak ne uspije.

1. Ukratko, ovaj skript definira i konfigurira pipeline strojnog učenja za zadatak chat-dovršavanja koristeći Azure Machine Learning SDK.

    ```python
    # Uvezite potrebne module iz Azure AI ML SDK-a
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Dohvatite komponentu cjevovoda nazvanu "chat_completion_pipeline" iz registra
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Definirajte posao cjevovoda koristeći @pipeline dekorator i funkciju create_pipeline
    # Naziv cjevovoda se postavlja na pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Inicijalizirajte dohvaćenu komponentu cjevovoda s različitim parametrima
        # To uključuje putanju modela, računalne klastere za različite faze, podjele dataset-a za trening i testiranje, broj GPU-a za fino podešavanje i druge parametre fino podešavanja
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Preslikajte podjele dataset-a na parametre
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Postavke treninga
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Postavljeno na broj dostupnih GPU-a u izračunu
            **finetune_parameters
        )
        return {
            # Preslikajte izlaz posla finog podešavanja na izlaz posla cjevovoda
            # Ovo se radi kako bismo lako mogli registrirati fino podešani model
            # Registracija modela je potrebna za implementaciju modela na online ili batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Kreirajte instancu cjevovoda pozivom funkcije create_pipeline
    pipeline_object = create_pipeline()
    
    # Nemojte koristiti predmemorirane rezultate iz prethodnih poslova
    pipeline_object.settings.force_rerun = True
    
    # Postavite da se ne nastavlja u slučaju neuspjeha koraka na False
    # To znači da će se cjevovod zaustaviti ako bilo koji korak ne uspije
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Pošaljite posao

1. Ovaj Python skript šalje posao pipeline-a strojnog učenja u Azure Machine Learning workspace i zatim čeka da posao završi. Evo pregleda što radi:

    - Poziva metodu create_or_update objekta jobs u workspace_ml_client da pošalje pipeline posao. Pipeline koji će se izvršiti specificiran je s pipeline_object, a eksperiment pod kojim se posao izvršava specificiran je s experiment_name.

    - Zatim poziva metodu stream objekta jobs u workspace_ml_client da čeka da pipeline posao završi. Posao za čekanje specificiran je imenom atributa pipeline_job objekta.

    - Ukratko, ovaj skript šalje posao pipeline-a strojnog učenja u Azure Machine Learning workspace i zatim čeka da se posao završi.

    ```python
    # Pošaljite zadatak cjevovoda u Azure Machine Learning radni prostor
    # Cjevovod koji će se pokrenuti specificira se putem pipeline_object
    # Eksperiment pod kojim se zadatak izvršava specificira se putem experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Pričekajte da se zadatak cjevovoda dovrši
    # Zadatak za čekanje specificira se putem atributa name objekta pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Registrirajte fino podešani model u workspace

Registrirat ćemo model iz izlaza posla finog podešavanja. To će pratiti povezanost između fino podešanog modela i posla finog podešavanja. Posao finog podešavanja dodatno prati povezanost s temeljnim modelom, podacima i kodom za treniranje.

### Registracija ML modela

1. Ovaj Python skript registrira strojni model koji je treniran u Azure Machine Learning pipeline-u. Evo pregleda što radi:

    - Uvozi potrebne module iz Azure AI ML SDK-a.

    - Provjerava je li izlaz trained_model dostupan iz pipeline posla pozivom metode get objekta jobs u workspace_ml_client i pristupajući njegovom atributu outputs.

    - Konstrukcija putanje do treniranog modela formatiranjem stringa s imenom pipeline posla i imenom izlaza ("trained_model").

    - Definira ime za fino podešani model dodavanjem "-ultrachat-200k" na izvornim naziv modela i zamjenom svih kosih crta crticama.

    - Priprema se za registraciju modela kreiranjem Model objekta s raznim parametrima, uključujući putanju modela, tip modela (MLflow model), ime i verziju modela te opis modela.

    - Registrira model pozivom metode create_or_update objekta models u workspace_ml_client s Model objektom kao argumentom.

    - Ispisuje registrirani model.

1. Ukratko, ovaj skript registrira strojni model treniran u Azure Machine Learning pipeline-u.
    
    ```python
    # Uvezite potrebne module iz Azure AI ML SDK-a
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Provjerite je li izlaz `trained_model` dostupan iz pipeline posla
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Konstruirajte put do treniranog modela formatiranjem stringa s imenom pipeline posla i imenom izlaza ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Definirajte ime za fino podešeni model dodavanjem "-ultrachat-200k" izvornom imenu modela i zamjenom svih kosa crta s crticama
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Pripremite se za registraciju modela stvaranjem Model objekta s raznim parametrima
    # To uključuje put do modela, tip modela (MLflow model), ime i verziju modela te opis modela
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Koristite vremensku oznaku kao verziju kako biste izbjegli sukob verzija
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Registrirajte model pozivanjem metode create_or_update objekta models u workspace_ml_client s Model objektom kao argumentom
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Ispišite registrirani model
    print("registered model: \n", registered_model)
    ```

## 7. Rasporedite fino podešani model na online endpoint

Online endpointi pružaju trajni REST API koji se može koristiti za integraciju s aplikacijama koje trebaju koristiti model.

### Upravljanje endpointom

1. Ovaj Python skript stvara upravljani online endpoint u Azure Machine Learning za registrirani model. Evo pregleda što radi:

    - Uvozi potrebne module iz Azure AI ML SDK-a.

    - Definira jedinstveno ime online endpointa dodavanjem vremenske oznake na niz "ultrachat-completion-".

    - Priprema se za stvaranje online endpointa kreiranjem ManagedOnlineEndpoint objekta s raznim parametrima, uključujući ime endpointa, opis endpointa i način autentifikacije ("key").

    - Stvara online endpoint pozivom metode begin_create_or_update workspace_ml_client-a s ManagedOnlineEndpoint objektom kao argumentom. Zatim čeka da operacija stvaranja završi pozivom metode wait.

1. Ukratko, ovaj skript stvara upravljani online endpoint u Azure Machine Learning za registrirani model.

    ```python
    # Uvezi potrebne module iz Azure AI ML SDK-a
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Definiraj jedinstveno ime za online endpoint dodavanjem vremenske oznake nakon niza "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Pripremi se za stvaranje online endpointa kreiranjem ManagedOnlineEndpoint objekta s različitim parametrima
    # U njih spadaju ime endpointa, opis endpointa i način autentifikacije ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Kreiraj online endpoint pozivanjem metode begin_create_or_update workspace_ml_client objektom ManagedOnlineEndpoint kao argumentom
    # Zatim čekaj da operacija stvaranja završi pozivom metode wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Ovdje možete pronaći popis SKU-ova podržanih za raspoređivanje - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Raspoređivanje ML modela

1. Ovaj Python skript raspoređuje registrirani strojni model na upravljani online endpoint u Azure Machine Learning. Evo pregleda što radi:

    - Uvozi modul ast, koji pruža funkcije za obradu stabala Pythona apstraktne sintakse.

    - Postavlja tip instance za raspoređivanje na "Standard_NC6s_v3".

    - Provjerava postoji li oznaka inference_compute_allow_list u foundation modelu. Ako postoji, konvertira vrijednost oznake iz stringa u Python listu i dodjeljuje je varijabli inference_computes_allow_list. Ako ne postoji, postavlja inference_computes_allow_list na None.

    - Provjerava je li specificirani tip instance u dopuštenom popisu. Ako nije, ispisuje poruku korisniku da odabere tip instance s dopuštenog popisa.

    - Priprema se za stvaranje rasporeda kreiranjem ManagedOnlineDeployment objekta s raznim parametrima, uključujući ime rasporeda, ime endpointa, ID modela, tip i broj instanci, postavke liveness probe i postavke zahtjeva.

    - Stvara raspored pozivom metode begin_create_or_update workspace_ml_client-a s ManagedOnlineDeployment objektom kao argumentom. Zatim čeka da operacija stvaranja završi pozivom metode wait.

    - Postavlja promet endpointa da usmjeri 100% prometa na raspored "demo".

    - Ažurira endpoint pozivom metode begin_create_or_update workspace_ml_client-a s objektom endpoint kao argumentom. Zatim čeka da operacija ažuriranja završi pozivom metode result.

1. Ukratko, ovaj skript raspoređuje registrirani strojni model na upravljani online endpoint u Azure Machine Learning.

    ```python
    # Uvezi modul ast, koji pruža funkcije za obradu stabala apstraktne sintakse Pythona
    import ast
    
    # Postavi tip instance za raspored
    instance_type = "Standard_NC6s_v3"
    
    # Provjeri postoji li oznaka `inference_compute_allow_list` u osnovnom modelu
    if "inference_compute_allow_list" in foundation_model.tags:
        # Ako postoji, pretvori vrijednost oznake iz stringa u Python listu i dodijeli je `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ako ne postoji, postavi `inference_computes_allow_list` na `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Provjeri je li navedeni tip instance na dozvoljenoj listi
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Pripremi stvaranje rasporeda kreiranjem objekta `ManagedOnlineDeployment` s različitim parametrima
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Kreiraj raspored pozivom metode `begin_create_or_update` klijenta `workspace_ml_client` s objektom `ManagedOnlineDeployment` kao argumentom
    # Zatim čekaj da operacija kreiranja završi pozivanjem metode `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Postavi promet krajnje točke da usmjeri 100% prometa na raspored "demo"
    endpoint.traffic = {"demo": 100}
    
    # Ažuriraj krajnju točku pozivom metode `begin_create_or_update` klijenta `workspace_ml_client` s objektom `endpoint` kao argumentom
    # Zatim čekaj da operacija ažuriranja završi pozivanjem metode `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Testirajte endpoint s uzorcima podataka

Uzet ćemo nekoliko uzoraka podataka iz testnog skupa i poslati na online endpoint za izvođenje zaključaka. Zatim ćemo prikazati dodijeljene oznake usporedno s stvarnim oznakama.

### Čitanje rezultata

1. Ovaj Python skript učitava JSON Lines datoteku u pandas DataFrame, uzima slučajni uzorak i resetira indeks. Evo pregleda što radi:

    - Učitava datoteku ./ultrachat_200k_dataset/test_gen.jsonl u pandas DataFrame. Funkcija read_json koristi se s argumentom lines=True jer je datoteka u JSON Lines formatu, gdje je svaki redak zaseban JSON objekt.

    - Uzima slučajni uzorak od 1 retka iz DataFrame-a. Funkcija sample koristi se s argumentom n=1 za označavanje broja slučajnih redaka za odabir.

    - Resetira indeks DataFrame-a. Funkcija reset_index koristi se s argumentom drop=True da ukloni originalni indeks i zamijeni ga novim indeksom s zadanim cjelobrojnim vrijednostima.

    - Prikazuje prva 2 retka DataFrame-a koristeći funkciju head s argumentom 2. Međutim, budući da DataFrame sadrži samo jedan redak nakon uzorkovanja, prikazat će samo taj jedan redak.

1. Ukratko, ovaj skript učitava JSON Lines datoteku u pandas DataFrame, uzima slučajni uzorak jednog retka, resetira indeks i prikazuje prvi redak.
    
    ```python
    # Uvezi biblioteku pandas
    import pandas as pd
    
    # Učitaj JSON Lines datoteku './ultrachat_200k_dataset/test_gen.jsonl' u pandas DataFrame
    # Argument 'lines=True' označava da je datoteka u JSON Lines formatu, gdje je svaki redak zaseban JSON objekt
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Uzmi nasumični uzorak od 1 retka iz DataFrame-a
    # Argument 'n=1' određuje broj nasumičnih redaka za odabir
    test_df = test_df.sample(n=1)
    
    # Resetiraj indeks DataFrame-a
    # Argument 'drop=True' označava da se originalni indeks smije odbaciti i zamijeniti novim indeksom sa zadanim cijelim brojevima
    # Argument 'inplace=True' označava da se DataFrame treba izmijeniti na licu mjesta (bez stvaranja novog objekta)
    test_df.reset_index(drop=True, inplace=True)
    
    # Prikaži prvih 2 retka DataFrame-a
    # Međutim, budući da DataFrame sadrži samo jedan redak nakon uzorkovanja, prikazat će se samo taj jedan redak
    test_df.head(2)
    ```

### Kreirajte JSON objekt

1. Ovaj Python skript kreira JSON objekt sa specifičnim parametrima i sprema ga u datoteku. Evo pregleda što radi:

    - Uvozi modul json, koji pruža funkcije za rad s JSON podacima.
    - Stvara rječnik parameters s ključevima i vrijednostima koji predstavljaju parametre za model strojnog učenja. Ključevi su "temperature", "top_p", "do_sample" i "max_new_tokens", a njihove odgovarajuće vrijednosti su 0.6, 0.9, True i 200.

    - Stvara drugi rječnik test_json s dva ključa: "input_data" i "params". Vrijednost "input_data" je drugi rječnik s ključevima "input_string" i "parameters". Vrijednost "input_string" je lista koja sadrži prvu poruku iz DataFramea test_df. Vrijednost "parameters" je prethodno kreirani rječnik parameters. Vrijednost "params" je prazan rječnik.

    - Otvara datoteku pod nazivom sample_score.json
    
    ```python
    # Uvoz modula json, koji pruža funkcije za rad s JSON podacima
    import json
    
    # Kreirajte rječnik `parameters` s ključevima i vrijednostima koje predstavljaju parametre za model strojnog učenja
    # Ključevi su "temperature", "top_p", "do_sample" i "max_new_tokens", a njihove odgovarajuće vrijednosti su 0.6, 0.9, True i 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Kreirajte drugi rječnik `test_json` s dva ključa: "input_data" i "params"
    # Vrijednost "input_data" je drugi rječnik s ključevima "input_string" i "parameters"
    # Vrijednost "input_string" je lista koja sadrži prvu poruku iz DataFrame-a `test_df`
    # Vrijednost "parameters" je rječnik `parameters` kreiran ranije
    # Vrijednost "params" je prazan rječnik
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Otvorite datoteku pod nazivom `sample_score.json` u direktoriju `./ultrachat_200k_dataset` u načinu pisanja
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Zapišite rječnik `test_json` u datoteku u JSON formatu koristeći funkciju `json.dump`
        json.dump(test_json, f)
    ```

### Pozivanje krajnje točke

1. Ovaj Python skript poziva online krajnju točku u Azure Machine Learningu za ocjenjivanje JSON datoteke. Evo pregleda što radi:

    - Poziva metodu invoke svojstva online_endpoints objekta workspace_ml_client. Ova metoda se koristi za slanje zahtjeva prema online krajnjoj točki i dobivanje odgovora.

    - Navodi ime krajnje točke i implementacije s argumentima endpoint_name i deployment_name. U ovom slučaju, ime krajnje točke pohranjeno je u varijabli online_endpoint_name, a ime implementacije je "demo".

    - Navodi putanju do JSON datoteke koja se ocjenjuje s argumentom request_file. U ovom slučaju, datoteka je ./ultrachat_200k_dataset/sample_score.json.

    - Sprema odgovor s krajnje točke u varijablu response.

    - Ispisuje sirovi odgovor.

1. Ukratko, ovaj skript poziva online krajnju točku u Azure Machine Learningu za ocjenjivanje JSON datoteke i ispisuje odgovor.

    ```python
    # Pozovite online krajnju točku u Azure Machine Learning za ocjenjivanje datoteke `sample_score.json`
    # Metoda `invoke` svojstva `online_endpoints` objekta `workspace_ml_client` koristi se za slanje zahtjeva online krajnjoj točki i dobivanje odgovora
    # Argument `endpoint_name` specificira ime krajnje točke, koje je pohranjeno u varijabli `online_endpoint_name`
    # Argument `deployment_name` specificira ime implementacije, koje je "demo"
    # Argument `request_file` specificira putanju do JSON datoteke koja se ocjenjuje, koja je `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Ispiši neobrađeni odgovor s krajnje točke
    print("raw response: \n", response, "\n")
    ```

## 9. Brisanje online krajnje točke

1. Ne zaboravite izbrisati online krajnju točku, inače će vam se računati trošak za korištenje resursa koje krajnja točka koristi. Ovaj redak Python koda briše online krajnju točku u Azure Machine Learningu. Evo pregleda što radi:

    - Poziva metodu begin_delete svojstva online_endpoints objekta workspace_ml_client. Ova metoda započinje brisanje online krajnje točke.

    - Navodi ime krajnje točke koja se briše argumentom name. U ovom slučaju, ime krajnje točke pohranjeno je u varijabli online_endpoint_name.

    - Poziva metodu wait da čeka dovršetak operacije brisanja. Ovo je blokirajuća operacija, što znači da će spriječiti nastavak izvođenja skripte dok se brisanje ne završi.

    - Ukratko, ovaj redak koda započinje brisanje online krajnje točke u Azure Machine Learningu i čeka dovršetak operacije.

    ```python
    # Izbriši online endpoint u Azure Machine Learning
    # Metoda `begin_delete` svojstva `online_endpoints` objekta `workspace_ml_client` koristi se za pokretanje brisanja online endpointa
    # Argument `name` specificira ime endpointa koji će se izbrisati, a koji je pohranjen u varijabli `online_endpoint_name`
    # Metoda `wait` se poziva kako bi se čekalo da operacija brisanja završi. Ovo je blokirajuća operacija, što znači da će spriječiti nastavak skripte dok brisanje ne bude završeno
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučujemo profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->