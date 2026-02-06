## Kaip naudoti pokalbių užbaigimo komponentus iš Azure ML sistemos registro modelio pritaikymui

Šiame pavyzdyje atliksime Phi-3-mini-4k-instruct modelio pritaikymą, kad užbaigtume pokalbį tarp dviejų žmonių, naudodami ultrachat_200k duomenų rinkinį.

![MLFineTune](../../../../imgs/03/ft/MLFineTune.png)

Pavyzdys parodys, kaip atlikti modelio pritaikymą naudojant Azure ML SDK ir Python, o vėliau pritaikytą modelį įdiegti į internetinį galinį tašką realaus laiko prognozėms.

### Mokymo duomenys

Naudosime ultrachat_200k duomenų rinkinį. Tai stipriai filtruota UltraChat duomenų rinkinio versija, kuri buvo naudojama Zephyr-7B-β, pažangiausio 7b pokalbių modelio, mokymui.

### Modelis

Naudosime Phi-3-mini-4k-instruct modelį, kad parodytume, kaip vartotojas gali pritaikyti modelį pokalbių užbaigimo užduočiai. Jei atidarėte šį užrašų knygelę iš konkretaus modelio kortelės, nepamirškite pakeisti konkretaus modelio pavadinimo.

### Užduotys

- Pasirinkti modelį pritaikymui.
- Pasirinkti ir išanalizuoti mokymo duomenis.
- Konfigūruoti pritaikymo užduotį.
- Paleisti pritaikymo užduotį.
- Peržiūrėti mokymo ir vertinimo metrikas.
- Užregistruoti pritaikytą modelį.
- Įdiegti pritaikytą modelį realaus laiko prognozėms.
- Išvalyti resursus.

## 1. Paruošiamieji veiksmai

- Įdiegti priklausomybes.
- Prisijungti prie AzureML darbo srities. Daugiau informacijos rasite SDK autentifikacijos nustatymuose. Pakeiskite <WORKSPACE_NAME>, <RESOURCE_GROUP> ir <SUBSCRIPTION_ID>.
- Prisijungti prie AzureML sistemos registro.
- Nustatyti pasirenkamą eksperimentų pavadinimą.
- Patikrinti arba sukurti skaičiavimo resursus.

> [!NOTE]
> Reikalavimai: vienas GPU mazgas gali turėti kelias GPU kortas. Pavyzdžiui, viename Standard_NC24rs_v3 mazge yra 4 NVIDIA V100 GPU, o Standard_NC12s_v3 mazge yra 2 NVIDIA V100 GPU. Daugiau informacijos rasite dokumentacijoje. GPU kortų skaičius mazge nustatomas parametre gpus_per_node. Teisingai nustatytas šis parametras užtikrins visų GPU mazge panaudojimą. Rekomenduojamus GPU skaičiavimo SKU galite rasti čia ir čia.

### Python bibliotekos

Įdiekite priklausomybes paleisdami žemiau esantį kodą. Tai nėra pasirenkamas žingsnis, jei dirbate naujoje aplinkoje.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Sąveika su Azure ML

1. Šis Python scenarijus naudojamas sąveikai su Azure Machine Learning (Azure ML) paslauga. Štai ką jis daro:

    - Importuoja reikalingus modulius iš azure.ai.ml, azure.identity ir azure.ai.ml.entities paketų. Taip pat importuoja time modulį.

    - Bando autentifikuotis naudojant DefaultAzureCredential(), kuris suteikia supaprastintą autentifikacijos patirtį greitai pradėti kurti programas Azure debesyje. Jei tai nepavyksta, pereina prie InteractiveBrowserCredential(), kuris pateikia interaktyvų prisijungimo langą.

    - Bando sukurti MLClient egzempliorių naudodamas from_config metodą, kuris skaito konfigūraciją iš numatytojo konfigūracijos failo (config.json). Jei tai nepavyksta, sukuria MLClient egzempliorių rankiniu būdu pateikdamas subscription_id, resource_group_name ir workspace_name.

    - Sukuria kitą MLClient egzempliorių, šį kartą Azure ML registrui, pavadintam "azureml". Šis registras yra vieta, kur saugomi modeliai, pritaikymo procesai ir aplinkos.

    - Nustato experiment_name kaip "chat_completion_Phi-3-mini-4k-instruct".

    - Generuoja unikalų laiko žymeklį, konvertuodamas dabartinį laiką (sekundėmis nuo epochos, kaip slankiojo taško skaičių) į sveikąjį skaičių, o tada į eilutę. Šis laiko žymeklis gali būti naudojamas unikaliems pavadinimams ir versijoms kurti.

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

## 2. Pasirinkti bazinį modelį pritaikymui

1. Phi-3-mini-4k-instruct yra 3.8B parametrų, lengvas, pažangiausias atviras modelis, sukurtas remiantis duomenų rinkiniais, naudotais Phi-2. Modelis priklauso Phi-3 modelių šeimai, o Mini versija turi dvi variantus: 4K ir 128K, kurie yra konteksto ilgiai (žetonais), kuriuos jis gali palaikyti. Mums reikia pritaikyti modelį mūsų specifiniam tikslui, kad galėtume jį naudoti. Šiuos modelius galite naršyti Modelių kataloge AzureML studijoje, filtruodami pagal pokalbių užbaigimo užduotį. Šiame pavyzdyje naudojame Phi-3-mini-4k-instruct modelį. Jei atidarėte šį užrašų knygelę kitam modeliui, atitinkamai pakeiskite modelio pavadinimą ir versiją.

    > [!NOTE]
    > Modelio id savybė. Ji bus perduota kaip įvestis pritaikymo užduočiai. Ji taip pat yra prieinama kaip Asset ID laukas modelio detalių puslapyje AzureML Studio Model Catalog.

2. Šis Python scenarijus sąveikauja su Azure Machine Learning (Azure ML) paslauga. Štai ką jis daro:

    - Nustato model_name kaip "Phi-3-mini-4k-instruct".

    - Naudoja get metodą iš models savybės registry_ml_client objekto, kad gautų naujausią modelio versiją su nurodytu pavadinimu iš Azure ML registro. get metodas kviečiamas su dviem argumentais: modelio pavadinimu ir etikete, nurodančia, kad reikia gauti naujausią modelio versiją.

    - Spausdina pranešimą konsolėje, nurodantį modelio pavadinimą, versiją ir id, kuris bus naudojamas pritaikymui. format metodas eilutėje naudojamas įterpti modelio pavadinimą, versiją ir id į pranešimą. Modelio pavadinimas, versija ir id pasiekiami kaip foundation_model objekto savybės.

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

## 3. Sukurti skaičiavimo resursus, kurie bus naudojami užduočiai

Pritaikymo užduotis VEIKIA TIK su GPU skaičiavimo resursais. Skaičiavimo resursų dydis priklauso nuo modelio dydžio, ir daugeliu atvejų tampa sudėtinga nustatyti tinkamus resursus užduočiai. Šiame langelyje vartotojui pateikiame gaires, kaip pasirinkti tinkamus resursus užduočiai.

> [!NOTE]
> Žemiau išvardyti skaičiavimo resursai veikia su optimizuota konfigūracija. Bet kokie konfigūracijos pakeitimai gali sukelti Cuda Out Of Memory klaidą. Tokiais atvejais pabandykite atnaujinti skaičiavimo resursus į didesnį dydį.

> [!NOTE]
> Pasirinkdami compute_cluster_size žemiau, įsitikinkite, kad skaičiavimo resursai yra prieinami jūsų resursų grupėje. Jei tam tikri skaičiavimo resursai nėra prieinami, galite pateikti prašymą gauti prieigą prie skaičiavimo resursų.

### Modelio patikrinimas pritaikymo palaikymui

1. Šis Python scenarijus sąveikauja su Azure Machine Learning (Azure ML) modeliu. Štai ką jis daro:

    - Importuoja ast modulį, kuris teikia funkcijas Python abstrakčios sintaksės gramatikos medžiams apdoroti.

    - Tikrina, ar foundation_model objektas (kuris atstovauja modelį Azure ML) turi žymą finetune_compute_allow_list. Žymos Azure ML yra raktų-reikšmių poros, kurias galite sukurti ir naudoti modeliams filtruoti bei rūšiuoti.

    - Jei finetune_compute_allow_list žyma yra, naudoja ast.literal_eval funkciją, kad saugiai išanalizuotų žymos reikšmę (eilutę) į Python sąrašą. Šis sąrašas priskiriamas computes_allow_list kintamajam. Tada spausdina pranešimą, nurodantį, kad skaičiavimo resursai turėtų būti sukurti iš sąrašo.

    - Jei finetune_compute_allow_list žyma nėra, nustato computes_allow_list kaip None ir spausdina pranešimą, nurodantį, kad finetune_compute_allow_list žyma nėra modelio žymų dalis.

    - Apibendrinant, šis scenarijus tikrina konkrečią žymą modelio metaduomenyse, konvertuoja žymos reikšmę į sąrašą, jei ji egzistuoja, ir pateikia atitinkamą grįžtamąjį ryšį vartotojui.

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

### Skaičiavimo resurso patikrinimas

1. Šis Python scenarijus sąveikauja su Azure Machine Learning (Azure ML) paslauga ir atlieka kelis patikrinimus skaičiavimo resursui. Štai ką jis daro:

    - Bando gauti skaičiavimo resursą, kurio pavadinimas saugomas compute_cluster, iš Azure ML darbo srities. Jei skaičiavimo resurso būklė yra "failed", išmeta ValueError.

    - Tikrina, ar computes_allow_list nėra None. Jei nėra, konvertuoja visus sąraše esančius skaičiavimo dydžius į mažąsias raides ir tikrina, ar dabartinio skaičiavimo resurso dydis yra sąraše. Jei nėra, išmeta ValueError.

    - Jei computes_allow_list yra None, tikrina, ar dabartinio skaičiavimo resurso dydis yra sąraše, kuriame yra nepalaikomi GPU VM dydžiai. Jei yra, išmeta ValueError.

    - Gauti visų prieinamų skaičiavimo dydžių sąrašą darbo srityje. Tada iteruoja per šį sąrašą, ir kiekvienam skaičiavimo dydžiui tikrina, ar jo pavadinimas atitinka dabartinio skaičiavimo resurso dydį. Jei taip, gauna GPU skaičių tam skaičiavimo dydžiui ir nustato gpu_count_found kaip True.

    - Jei gpu_count_found yra True, spausdina GPU skaičių skaičiavimo resurse. Jei gpu_count_found yra False, išmeta ValueError.

    - Apibendrinant, šis scenarijus atlieka kelis patikrinimus skaičiavimo resursui Azure ML darbo srityje, įskaitant jo būklės, dydžio ir GPU skaičiaus patikrinimą.

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

## 4. Pasirinkti duomenų rinkinį modelio pritaikymui

1. Naudojame ultrachat_200k duomenų rinkinį. Duomenų rinkinys turi keturis skirstymus, tinkamus Supervised fine-tuning (sft) ir Generation ranking (gen). Skirstymų pavyzdžių skaičius pateikiamas taip:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Toliau pateikti langeliai rodo pagrindinį duomenų paruošimą pritaikymui:

### Vizualizuoti keletą duomenų eilučių

Norime, kad šis pavyzdys veiktų greitai, todėl išsaugome train_sft, test_sft failus, kuriuose yra 5% jau apkarpytų eilučių. Tai reiškia, kad pritaikytas modelis turės mažesnį tikslumą, todėl jis neturėtų būti naudojamas realiame pasaulyje.
download-dataset.py naudojamas ultrachat_200k duomenų rinkiniui atsisiųsti ir transformuoti duomenų rinkinį į pritaikymo proceso komponentų vartojamą formatą. Kadangi duomenų rinkinys yra didelis, čia pateikiame tik dalį duomenų rinkinio.

1. Paleidus žemiau esantį scenarijų atsisiunčiama tik 5% duomenų. Tai galima padidinti pakeičiant dataset_split_pc parametrą į norimą procentą.

    > [!NOTE]
    > Kai kurie kalbos modeliai turi skirtingus kalbos kodus, todėl stulpelių pavadinimai duomenų rinkinyje turėtų atspindėti tai.

1. Štai pavyzdys, kaip turėtų atrodyti duomenys:
Pokalbių užbaigimo duomenų rinkinys saugomas parquet formatu, kiekvienas įrašas naudoja šią schemą:

    - Tai yra JSON (JavaScript Object Notation) dokumentas, kuris yra populiarus duomenų mainų formatas. Tai nėra vykdomasis kodas, o būdas saugoti ir perduoti duomenis. Štai jo struktūros aprašymas:

    - "prompt": Šis raktas turi eilutės reikšmę, kuri atspindi užduotį arba klausimą, pateiktą AI asistentui.

    - "messages": Šis raktas turi objektų masyvą. Kiekvienas objektas atspindi pranešimą pokalbyje tarp vartotojo ir AI asistento. Kiekvienas pranešimo objektas turi du raktus:

    - "content": Šis raktas turi eilutės reikšmę, kuri atspindi pranešimo turinį.
    - "role": Šis raktas turi eilutės reikšmę, kuri atspindi pranešimą siuntusio subjekto vaidmenį. Tai gali būti "user" arba "assistant".
    - "prompt_id": Šis raktas turi eilutės reikšmę, kuri atspindi unikalų identifikatorių užduočiai.

1. Šiame konkrečiame JSON dokumente pateikiamas pokalbis, kuriame vartotojas prašo AI asistento sukurti pagrindinį veikėją distopinei istorijai. Asistentas atsako, o vartotojas prašo daugiau detalių. Asistentas sutinka pateikti daugiau detalių. Visas pokalbis susijęs su konkrečiu prompt id.

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

### Duomenų atsisiuntimas

1. Šis Python scenarijus naudojamas duomenų rinkiniui atsisiųsti naudojant pagalbinį scenarijų download-dataset.py. Štai ką jis daro:

    - Importuoja os modulį, kuris suteikia nešiojamą būdą naudoti operacinės sistemos priklausomą funkcionalumą.

    - Naudoja os.system funkciją, kad paleistų download-dataset.py scenarijų apvalkale su konkrečiais komandų eilutės argumentais. Argumentai nurodo, kokį duomenų rinkinį atsisiųsti (HuggingFaceH4/ultrachat_200k), katalogą, į kurį jį atsisiųsti (ultrachat_200k_dataset), ir duomenų rinkinio procentą (5). os.system funkcija grąžina vykdomos komandos išėjimo būseną; ši būsena saugoma exit_status kintamajame.

    - Tikrina, ar exit_status nėra 0. Unix tipo operacinėse sistemose išėjimo būsena 0 paprastai nurodo, kad komanda buvo sėkminga, o bet kuris kitas skaičius nurodo klaidą. Jei exit_status nėra 0, išmeta Exception su pranešimu, nurodančiu, kad buvo klaida atsisiunčiant duomenų rinkinį.

    - Apibendrinant, šis scenarijus paleidžia komandą duomenų rinkiniui atsisiųsti naudojant pagalbinį scenarijų ir išmeta išimtį, jei komanda nepavyksta.

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

### Duomenų įkėlimas į DataFrame

1. Šis Python scenarijus įkelia JSON Lines failą į pandas DataFrame ir rodo pirmas 5 eilutes. Štai ką jis daro:

    - Importuoja pandas biblioteką, kuri yra galinga duomenų manipuliavimo ir analizės biblioteka.

    - Nustato maksimalų stulpelio plotį pandas rodymo parinktyse į 0. Tai reiškia, kad bus rodomas visas kiekvieno stulpelio tekstas be sutrump
- Jis naudoja „head“ metodą, kad parodytų pirmas 5 „DataFrame“ eilutes. Jei „DataFrame“ turi mažiau nei 5 eilutes, bus parodytos visos.

- Apibendrinant, šis scenarijus įkelia JSON Lines failą į „DataFrame“ ir parodo pirmas 5 eilutes su pilnu stulpelių tekstu.

## 5. Pateikite modelio derinimo užduotį naudodami modelį ir duomenis kaip įvestis

Sukurkite užduotį, kuri naudoja „chat-completion“ komponentą. Sužinokite daugiau apie visus parametrus, palaikomus modelio derinimui.

### Apibrėžkite derinimo parametrus

1. Derinimo parametrai gali būti suskirstyti į 2 kategorijas: mokymo parametrai ir optimizavimo parametrai.

1. Mokymo parametrai apibrėžia mokymo aspektus, tokius kaip:

    - Naudojamas optimizatorius, planuotojas
    - Metrika, pagal kurią optimizuojamas modelio derinimas
    - Mokymo žingsnių skaičius, partijų dydis ir pan.
    - Optimizavimo parametrai padeda optimizuoti GPU atmintį ir efektyviai naudoti skaičiavimo išteklius.

1. Žemiau pateikiami keli šios kategorijos parametrai. Optimizavimo parametrai skiriasi priklausomai nuo modelio ir yra įtraukti į modelį, kad būtų galima valdyti šiuos skirtumus.

    - Įjungti „deepspeed“ ir „LoRA“
    - Įjungti mišrų tikslumo mokymą
    - Įjungti mokymą keliuose mazguose

> [!NOTE]
> Prižiūrimas modelio derinimas gali sukelti suderinimo praradimą arba katastrofišką užmarštį. Rekomenduojame patikrinti šią problemą ir atlikti suderinimo etapą po modelio derinimo.

### Modelio derinimo parametrai

1. Šis „Python“ scenarijus nustato parametrus mašininio mokymosi modelio derinimui. Štai ką jis daro:

    - Nustato numatytuosius mokymo parametrus, tokius kaip mokymo epochų skaičius, mokymo ir vertinimo partijų dydžiai, mokymosi greitis ir mokymosi greičio planuotojo tipas.

    - Nustato numatytuosius optimizavimo parametrus, tokius kaip „LoRA“ ir „DeepSpeed“ taikymas bei „DeepSpeed“ etapas.

    - Sujungia mokymo ir optimizavimo parametrus į vieną žodyną, pavadintą „finetune_parameters“.

    - Patikrina, ar „foundation_model“ turi modelio specifinius numatytuosius parametrus. Jei taip, jis išspausdina įspėjimo pranešimą ir atnaujina „finetune_parameters“ žodyną su šiais modelio specifiniais numatytaisiais parametrais. Funkcija „ast.literal_eval“ naudojama modelio specifinius numatytuosius parametrus konvertuoti iš eilutės į „Python“ žodyną.

    - Išspausdina galutinį modelio derinimo parametrų rinkinį, kuris bus naudojamas vykdymui.

    - Apibendrinant, šis scenarijus nustato ir parodo parametrus mašininio mokymosi modelio derinimui, su galimybe pakeisti numatytuosius parametrus modelio specifiniais.

### Mokymo procesas

1. Šis „Python“ scenarijus apibrėžia funkciją, skirtą sugeneruoti mokymo proceso pavadinimą, ir tada ją iškviečia, kad sugeneruotų ir išspausdintų pavadinimą. Štai ką jis daro:

1. Apibrėžiama funkcija „get_pipeline_display_name“. Ši funkcija sugeneruoja pavadinimą, remdamasi įvairiais mokymo proceso parametrais.

1. Funkcijos viduje apskaičiuojamas bendras partijų dydis, padauginus įrenginio partijų dydį, gradientų kaupimo žingsnių skaičių, GPU skaičių viename mazge ir mazgų skaičių, naudojamą modelio derinimui.

1. Gaunami įvairūs kiti parametrai, tokie kaip mokymosi greičio planuotojo tipas, ar taikomas „DeepSpeed“, „DeepSpeed“ etapas, ar taikomas „LoRA“, modelio kontrolinių taškų skaičiaus limitas ir maksimali sekos ilgis.

1. Sukuriama eilutė, kurioje visi šie parametrai yra atskirti brūkšniais. Jei taikomas „DeepSpeed“ arba „LoRA“, eilutėje įtraukiama „ds“ su „DeepSpeed“ etapu arba „lora“. Jei ne, įtraukiama „nods“ arba „nolora“.

1. Funkcija grąžina šią eilutę, kuri tarnauja kaip mokymo proceso pavadinimas.

1. Po funkcijos apibrėžimo ji iškviečiama, kad sugeneruotų pavadinimą, kuris tada išspausdinamas.

1. Apibendrinant, šis scenarijus sugeneruoja mokymo proceso pavadinimą, remdamasis įvairiais parametrais, ir tada išspausdina šį pavadinimą.

### Konfigūruoti procesą

Šis „Python“ scenarijus apibrėžia ir konfigūruoja mašininio mokymosi procesą, naudodamas „Azure Machine Learning SDK“. Štai ką jis daro:

1. Importuoja reikalingus modulius iš „Azure AI ML SDK“.

1. Iš registro gauna proceso komponentą, pavadintą „chat_completion_pipeline“.

1. Apibrėžia proceso užduotį, naudodamas „@pipeline“ dekoratorių ir funkciją „create_pipeline“. Proceso pavadinimas nustatomas kaip „pipeline_display_name“.

1. Funkcijos „create_pipeline“ viduje inicijuojamas gautas proceso komponentas su įvairiais parametrais, įskaitant modelio kelią, skaičiavimo klasterius skirtingiems etapams, duomenų rinkinių padalijimus mokymui ir testavimui, GPU skaičių, naudojamą modelio derinimui, ir kitus modelio derinimo parametrus.

1. Proceso užduoties išvestis susiejama su proceso užduoties išvestimi. Tai daroma tam, kad modelis būtų lengvai registruojamas, kas būtina modelio diegimui į internetinį arba paketų galinį tašką.

1. Sukuriamas proceso egzempliorius, iškviečiant funkciją „create_pipeline“.

1. Nustatoma proceso „force_rerun“ parinktis kaip „True“, reiškianti, kad nebus naudojami anksčiau atliktų užduočių talpyklos rezultatai.

1. Nustatoma proceso „continue_on_step_failure“ parinktis kaip „False“, reiškianti, kad procesas sustos, jei bet kuris žingsnis nepavyks.

1. Apibendrinant, šis scenarijus apibrėžia ir konfigūruoja mašininio mokymosi procesą, skirtą pokalbių užduočiai, naudodamas „Azure Machine Learning SDK“.

### Pateikti užduotį

1. Šis „Python“ scenarijus pateikia mašininio mokymosi proceso užduotį „Azure Machine Learning“ darbo erdvėje ir tada laukia, kol užduotis bus baigta. Štai ką jis daro:

    - Jis iškviečia „create_or_update“ metodą iš „jobs“ objekto „workspace_ml_client“, kad pateiktų proceso užduotį. Procesas, kuris bus vykdomas, nurodomas „pipeline_object“, o eksperimentas, kuriame vykdoma užduotis, nurodomas „experiment_name“.

    - Tada jis iškviečia „stream“ metodą iš „jobs“ objekto „workspace_ml_client“, kad lauktų, kol proceso užduotis bus baigta. Užduotis, kurią reikia laukti, nurodoma „pipeline_job“ objekto „name“ atributu.

1. Apibendrinant, šis scenarijus pateikia mašininio mokymosi proceso užduotį „Azure Machine Learning“ darbo erdvėje ir tada laukia, kol užduotis bus baigta.

## 6. Registruoti modelį darbo erdvėje

Mes registruosime modelį iš modelio derinimo užduoties išvesties. Tai leis sekti ryšį tarp modelio ir modelio derinimo užduoties. Modelio derinimo užduotis, savo ruožtu, seka ryšį su pagrindiniu modeliu, duomenimis ir mokymo kodu.

### ML modelio registravimas

1. Šis „Python“ scenarijus registruoja mašininio mokymosi modelį, kuris buvo apmokytas „Azure Machine Learning“ procese. Štai ką jis daro:

    - Importuoja reikalingus modulius iš „Azure AI ML SDK“.

    - Patikrina, ar „trained_model“ išvestis yra prieinama iš proceso užduoties, iškviečiant „get“ metodą iš „jobs“ objekto „workspace_ml_client“ ir pasiekiant jo „outputs“ atributą.

    - Sukuria kelią į apmokytą modelį, formatuodamas eilutę su proceso užduoties pavadinimu ir išvesties pavadinimu („trained_model“).

    - Apibrėžia pavadinimą apmokytam modeliui, pridedant „-ultrachat-200k“ prie originalaus modelio pavadinimo ir pakeičiant bet kokius pasviruosius brūkšnius į brūkšnius.

    - Paruošia modelio registravimą, sukuriant „Model“ objektą su įvairiais parametrais, įskaitant kelią į modelį, modelio tipą („MLflow model“), modelio pavadinimą ir versiją bei modelio aprašymą.

    - Registruoja modelį, iškviečiant „create_or_update“ metodą iš „models“ objekto „workspace_ml_client“ su „Model“ objektu kaip argumentu.

    - Išspausdina registruotą modelį.

1. Apibendrinant, šis scenarijus registruoja mašininio mokymosi modelį, kuris buvo apmokytas „Azure Machine Learning“ procese.

## 7. Diegti modelį į internetinį galinį tašką

Internetiniai galiniai taškai suteikia patvarų REST API, kurį galima integruoti su programomis, kurios turi naudoti modelį.

### Valdyti galinį tašką

1. Šis „Python“ scenarijus sukuria valdomą internetinį galinį tašką „Azure Machine Learning“ registruotam modeliui. Štai ką jis daro:

    - Importuoja reikalingus modulius iš „Azure AI ML SDK“.

    - Apibrėžia unikalų pavadinimą internetiniam galiniam taškui, pridedant laiko žymą prie eilutės „ultrachat-completion-“.

    - Paruošia internetinio galinio taško sukūrimą, sukuriant „ManagedOnlineEndpoint“ objektą su įvairiais parametrais, įskaitant galinio taško pavadinimą, aprašymą ir autentifikavimo režimą („key“).

    - Sukuria internetinį galinį tašką, iškviečiant „begin_create_or_update“ metodą iš „workspace_ml_client“ su „ManagedOnlineEndpoint“ objektu kaip argumentu. Tada laukia, kol sukūrimo operacija bus baigta, iškviečiant „wait“ metodą.

1. Apibendrinant, šis scenarijus sukuria valdomą internetinį galinį tašką „Azure Machine Learning“ registruotam modeliui.

> [!NOTE]
> Čia galite rasti SKU sąrašą, palaikomą diegimui - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Modelio diegimas

1. Šis „Python“ scenarijus diegia registruotą mašininio mokymosi modelį į valdomą internetinį galinį tašką „Azure Machine Learning“. Štai ką jis daro:

    - Importuoja „ast“ modulį, kuris teikia funkcijas „Python“ abstrakčios sintaksės medžių apdorojimui.

    - Nustato diegimo instancijos tipą kaip „Standard_NC6s_v3“.

    - Patikrina, ar „foundation model“ turi „inference_compute_allow_list“ žymą. Jei taip, jis konvertuoja žymos vertę iš eilutės į „Python“ sąrašą ir priskiria ją „inference_computes_allow_list“. Jei ne, jis nustato „inference_computes_allow_list“ kaip „None“.

    - Patikrina, ar nurodytas instancijos tipas yra leidžiamame sąraše. Jei ne, jis išspausdina pranešimą, prašydamas vartotojo pasirinkti instancijos tipą iš leidžiamo sąrašo.

    - Paruošia diegimą, sukuriant „ManagedOnlineDeployment“ objektą su įvairiais parametrais, įskaitant diegimo pavadinimą, galinio taško pavadinimą, modelio ID, instancijos tipą ir skaičių, gyvybingumo patikros nustatymus ir užklausos nustatymus.

    - Sukuria diegimą, iškviečiant „begin_create_or_update“ metodą iš „workspace_ml_client“ su „ManagedOnlineDeployment“ objektu kaip argumentu. Tada laukia, kol sukūrimo operacija bus baigta, iškviečiant „wait“ metodą.

    - Nustato galinio taško srautą, kad nukreiptų 100% srauto į „demo“ diegimą.

    - Atnaujina galinį tašką, iškviečiant „begin_create_or_update“ metodą iš „workspace_ml_client“ su galinio taško objektu kaip argumentu. Tada laukia, kol atnaujinimo operacija bus baigta, iškviečiant „result“ metodą.

1. Apibendrinant, šis scenarijus diegia registruotą mašininio mokymosi modelį į valdomą internetinį galinį tašką „Azure Machine Learning“.

## 8. Testuoti galinį tašką su pavyzdiniais duomenimis

Mes paimsime pavyzdinius duomenis iš testavimo duomenų rinkinio ir pateiksime juos internetiniam galiniam taškui, kad gautume prognozes. Tada parodysime prognozuotas etiketes kartu su tikrosiomis etiketėmis.

### Rezultatų skaitymas

1. Šis „Python“ scenarijus skaito JSON Lines failą į „pandas DataFrame“, paima atsitiktinį pavyzdį ir atnaujina indeksą. Štai ką jis daro:

    - Jis skaito failą ./ultrachat_200k_dataset/test_gen.jsonl į „pandas DataFrame“. Funkcija „read_json“ naudojama su „lines=True“ argumentu, nes failas yra JSON Lines formato, kur kiekviena eilutė yra atskiras JSON objektas.

    - Jis paima atsitiktinį 1 eilutės pavyzdį iš „DataFrame“. Funkcija „sample“ naudojama su „n=1“ argumentu, kad nurodytų atsitiktinių eilučių skaičių.

    - Jis atnaujina „DataFrame“ indeksą. Funkcija „reset_index“ naudojama su „drop=True“ argumentu, kad pašalintų originalų indeksą ir pakeistų jį nauju numatytųjų sveikųjų skaičių indeksu.

    - Jis parodo pirmas 2 „DataFrame“ eilutes, naudodamas „head“ funkciją su argumentu 2. Tačiau, kadangi „DataFrame“ po pavyzdžio paėmimo turi tik vieną eilutę, bus parodyta tik ta viena eilutė.

1. Apibendrinant, šis scenarijus skaito JSON Lines failą į „pandas DataFrame“, paima atsitiktinį 1 eilutės pavyzdį, atnaujina indeksą ir parodo pirmą eilutę.

### JSON objekto kūrimas

1. Šis „Python“ scenarijus sukuria JSON objektą su specifiniais parametrais ir išsaugo jį faile. Štai ką jis daro:

    - Importuoja „json“ modulį, kuris teikia funkcijas darbui su JSON duomenimis.

    - Sukuria žodyną „parameters“ su raktais ir reikšmėmis, kurie atspindi mašininio mokymosi modelio parametrus. Raktai yra „temperature“, „top_p“, „do_sample“ ir „max_new_tokens“, o jų atitinkamos reikšmės yra 0.6, 0.9, True ir 200.

    - Sukuria kitą žodyną „test_json“ su dviem raktais: „input_data“ ir „params“. „input_data“ reikšmė yra kitas žodynas su raktais „input_string“ ir „parameters“. „input_string“ reikšmė yra sąrašas, kuriame yra pirmoji žinutė iš „test_df
- Atidaro failą, pavadintą sample_score.json

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

### Endpointo iškvietimas

1. Šis Python skriptas iškviečia internetinį endpointą Azure Machine Learning platformoje, kad įvertintų JSON failą. Štai ką jis daro:

    - Naudoja workspace_ml_client objekto online_endpoints savybės invoke metodą. Šis metodas siunčia užklausą į internetinį endpointą ir gauna atsakymą.

    - Nurodo endpointo ir diegimo pavadinimus, naudodamas endpoint_name ir deployment_name argumentus. Šiuo atveju endpointo pavadinimas saugomas kintamajame online_endpoint_name, o diegimo pavadinimas yra "demo".

    - Nurodo kelią į JSON failą, kurį reikia įvertinti, naudodamas request_file argumentą. Šiuo atveju failo kelias yra ./ultrachat_200k_dataset/sample_score.json.

    - Atsakymą iš endpointo saugo kintamajame response.

    - Spausdina neapdorotą atsakymą.

1. Apibendrinant, šis skriptas iškviečia internetinį endpointą Azure Machine Learning platformoje, kad įvertintų JSON failą, ir spausdina atsakymą.

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

## 9. Internetinio endpointo ištrynimas

1. Nepamirškite ištrinti internetinio endpointo, kitaip paliksite aktyvų skaičiavimo resursų naudojimą, už kurį bus skaičiuojami mokesčiai. Ši Python kodo eilutė ištrina internetinį endpointą Azure Machine Learning platformoje. Štai ką ji daro:

    - Naudoja workspace_ml_client objekto online_endpoints savybės begin_delete metodą. Šis metodas pradeda internetinio endpointo ištrynimo procesą.

    - Nurodo endpointo pavadinimą, kurį reikia ištrinti, naudodamas name argumentą. Šiuo atveju endpointo pavadinimas saugomas kintamajame online_endpoint_name.

    - Naudoja wait metodą, kad palauktų, kol ištrynimo operacija bus baigta. Tai yra blokuojanti operacija, reiškianti, kad skriptas nebus tęsiamas, kol ištrynimas nebus užbaigtas.

    - Apibendrinant, ši kodo eilutė pradeda internetinio endpointo ištrynimą Azure Machine Learning platformoje ir laukia, kol operacija bus baigta.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.