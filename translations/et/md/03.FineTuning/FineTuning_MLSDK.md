<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-10-11T11:48:56+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "et"
}
-->
## Kuidas kasutada Azure ML süsteemiregistri vestluse lõpetamise komponente mudeli peenhäälestamiseks

Selles näites teeme Phi-3-mini-4k-instruct mudeli peenhäälestuse, et lõpetada vestlus kahe inimese vahel, kasutades ultrachat_200k andmestikku.

![MLFineTune](../../../../imgs/03/ft/MLFineTune.png)

Näide näitab, kuidas teha peenhäälestust Azure ML SDK ja Pythoniga ning seejärel juurutada peenhäälestatud mudel reaalajas järelduste tegemiseks veebipõhises lõpp-punktis.

### Treeningandmed

Kasutame ultrachat_200k andmestikku. See on tugevalt filtreeritud versioon UltraChat andmestikust, mida kasutati Zephyr-7B-β, tipptasemel 7B vestlusmudeli, treenimiseks.

### Mudel

Kasutame Phi-3-mini-4k-instruct mudelit, et näidata, kuidas kasutaja saab mudelit peenhäälestada vestluse lõpetamise ülesande jaoks. Kui avasite selle märkmiku konkreetse mudeli kaardilt, asendage konkreetse mudeli nimi.

### Ülesanded

- Valige mudel peenhäälestamiseks.
- Valige ja uurige treeningandmeid.
- Konfigureerige peenhäälestuse töö.
- Käivitage peenhäälestuse töö.
- Vaadake üle treeningu ja hindamise mõõdikud.
- Registreerige peenhäälestatud mudel.
- Juurutage peenhäälestatud mudel reaalajas järelduste tegemiseks.
- Puhastage ressursid.

## 1. Eeltingimuste seadistamine

- Installige sõltuvused
- Ühendage AzureML tööruumiga. Lisateavet leiate SDK autentimise seadistamise juhendist. Asendage <WORKSPACE_NAME>, <RESOURCE_GROUP> ja <SUBSCRIPTION_ID> allpool.
- Ühendage AzureML süsteemiregistriga
- Määrake valikuline eksperimendi nimi
- Kontrollige või looge arvutusressurss.

> [!NOTE]
> Nõuded: üks GPU sõlm võib sisaldada mitut GPU kaarti. Näiteks Standard_NC24rs_v3 sõlmes on 4 NVIDIA V100 GPU-d, samas kui Standard_NC12s_v3 sõlmes on 2 NVIDIA V100 GPU-d. Vaadake dokumentatsiooni selle teabe kohta. GPU kaartide arv sõlme kohta määratakse allpool parameetriga gpus_per_node. Selle väärtuse korrektne seadistamine tagab kõigi sõlme GPU-de kasutamise. Soovitatavad GPU arvutusressursid leiate siit ja siit.

### Python'i teegid

Installige sõltuvused, käivitades alloleva lahtri. See ei ole valikuline samm, kui töötate uues keskkonnas.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML-iga suhtlemine

1. See Python'i skript on mõeldud suhtlemiseks Azure Machine Learning (Azure ML) teenusega. Siin on ülevaade, mida see teeb:

    - Impordib vajalikud moodulid paketist azure.ai.ml, azure.identity ja azure.ai.ml.entities. Samuti impordib mooduli time.

    - Püüab autentida, kasutades DefaultAzureCredential(), mis pakub lihtsustatud autentimiskogemust, et kiiresti alustada rakenduste arendamist Azure'i pilves. Kui see ebaõnnestub, langeb tagasi InteractiveBrowserCredential() meetodile, mis pakub interaktiivset sisselogimise akent.

    - Püüab luua MLClient eksemplari, kasutades meetodit from_config, mis loeb konfiguratsiooni vaikimisi konfiguratsioonifailist (config.json). Kui see ebaõnnestub, loob MLClient eksemplari, pakkudes käsitsi subscription_id, resource_group_name ja workspace_name.

    - Loob teise MLClient eksemplari, seekord Azure ML registri jaoks nimega "azureml". See register on koht, kus hoitakse mudeleid, peenhäälestuse torujuhtmeid ja keskkondi.

    - Määrab eksperimendi nimeks "chat_completion_Phi-3-mini-4k-instruct".

    - Genereerib unikaalse ajatempli, teisendades praeguse aja (sekundites alates epohhist, ujukomaarvuna) täisarvuks ja seejärel stringiks. Seda ajatemplit saab kasutada unikaalsete nimede ja versioonide loomiseks.

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

## 2. Valige peenhäälestamiseks alusmudel

1. Phi-3-mini-4k-instruct on 3.8B parameetritega, kergekaaluline, tipptasemel avatud mudel, mis põhineb Phi-2 jaoks kasutatud andmestikel. Mudel kuulub Phi-3 mudeliperekonda ning Mini versioonil on kaks varianti: 4K ja 128K, mis tähistavad konteksti pikkust (tokenites), mida see toetab. Me peame mudeli peenhäälestama meie konkreetse eesmärgi jaoks, et seda kasutada. Saate neid mudeleid sirvida AzureML Studio mudelikataloogis, filtreerides vestluse lõpetamise ülesande järgi. Selles näites kasutame Phi-3-mini-4k-instruct mudelit. Kui olete avanud selle märkmiku teise mudeli jaoks, asendage mudeli nimi ja versioon vastavalt.

    > [!NOTE]
    > Mudeli id omadus. See edastatakse peenhäälestuse töö sisendina. See on saadaval ka Asset ID väljana mudeli detailide lehel AzureML Studio mudelikataloogis.

2. See Python'i skript suhtleb Azure Machine Learning (Azure ML) teenusega. Siin on ülevaade, mida see teeb:

    - Määrab mudeli nimeks "Phi-3-mini-4k-instruct".

    - Kasutab registry_ml_client objekti models omaduse meetodit get, et hankida Azure ML registrist määratud nimega mudeli uusim versioon. Meetod get kutsutakse kahe argumendiga: mudeli nimi ja silt, mis määrab, et tuleb hankida mudeli uusim versioon.

    - Prindib konsoolile sõnumi, mis näitab peenhäälestamiseks kasutatava mudeli nime, versiooni ja id-d. Stringi meetod format kasutatakse mudeli nime, versiooni ja id sisestamiseks sõnumisse. Mudeli nimi, versioon ja id on juurdepääsetavad foundation_model objekti omadustena.

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

## 3. Looge arvutusressurss töö jaoks

Peenhäälestuse töö töötab AINULT GPU arvutusressursiga. Arvutusressursi suurus sõltub mudeli suurusest ja enamikul juhtudel on õige ressursi tuvastamine keeruline. Selles lahtris juhendame kasutajat õige ressursi valimisel.

> [!NOTE]
> Allpool loetletud arvutusressursid töötavad kõige optimeerituma konfiguratsiooniga. Konfiguratsiooni muutmine võib põhjustada Cuda Out Of Memory vea. Sellisel juhul proovige uuendada arvutusressurssi suuremaks.

> [!NOTE]
> Valides allpool compute_cluster_size, veenduge, et arvutusressurss on teie ressursigrupis saadaval. Kui konkreetne arvutusressurss pole saadaval, saate esitada taotluse ressursi saamiseks.

### Mudeli peenhäälestuse toe kontrollimine

1. See Python'i skript suhtleb Azure Machine Learning (Azure ML) mudeliga. Siin on ülevaade, mida see teeb:

    - Impordib ast mooduli, mis pakub funktsioone Python'i abstraktse süntaksipuu töötlemiseks.

    - Kontrollib, kas foundation_model objektil (mis esindab Azure ML mudelit) on silt nimega finetune_compute_allow_list. Azure ML sildid on võtme-väärtuse paarid, mida saate luua ja kasutada mudelite filtreerimiseks ja sortimiseks.

    - Kui finetune_compute_allow_list silt on olemas, kasutab ast.literal_eval funktsiooni, et ohutult teisendada sildi väärtus (string) Python'i loendiks. See loend määratakse muutujale computes_allow_list. Seejärel prindib sõnumi, mis näitab, et arvutusressurss tuleks luua loendist.

    - Kui finetune_compute_allow_list silt pole olemas, määrab computes_allow_list väärtuseks None ja prindib sõnumi, mis näitab, et finetune_compute_allow_list silt ei kuulu mudeli siltide hulka.

    - Kokkuvõttes kontrollib see skript mudeli metaandmetes konkreetset silti, teisendab sildi väärtuse loendiks, kui see eksisteerib, ja annab kasutajale vastavalt tagasisidet.

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

### Arvutusressursi kontrollimine

1. See Python'i skript suhtleb Azure Machine Learning (Azure ML) teenusega ja teeb mitmeid kontrolle arvutusressursi kohta. Siin on ülevaade, mida see teeb:

    - Püüab hankida arvutusressurssi nimega compute_cluster Azure ML tööruumist. Kui arvutusressursi ettevalmistamise olek on "failed", viskab ValueError'i.

    - Kontrollib, kas computes_allow_list pole None. Kui ei ole, teisendab kõik loendis olevad arvutusressursi suurused väikesteks tähtedeks ja kontrollib, kas praeguse arvutusressursi suurus on loendis. Kui ei ole, viskab ValueError'i.

    - Kui computes_allow_list on None, kontrollib, kas arvutusressursi suurus on loendis unsupported GPU VM sizes. Kui on, viskab ValueError'i.

    - Hangib loendi kõigist tööruumis saadaval olevatest arvutusressursside suurustest. Seejärel iteratsioonib selle loendi üle ja iga arvutusressursi suuruse puhul kontrollib, kas selle nimi vastab praeguse arvutusressursi suurusele. Kui vastab, hangib GPU-de arvu selle arvutusressursi suuruse jaoks ja määrab gpu_count_found väärtuseks True.

    - Kui gpu_count_found on True, prindib arvutusressursi GPU-de arvu. Kui gpu_count_found on False, viskab ValueError'i.

    - Kokkuvõttes teeb see skript mitmeid kontrolle Azure ML tööruumi arvutusressursi kohta, sealhulgas kontrollib selle ettevalmistamise olekut, suurust lubatud või keelatud loendi vastu ja GPU-de arvu.

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

## 4. Valige mudeli peenhäälestamiseks andmestik

1. Kasutame ultrachat_200k andmestikku. Andmestikul on neli jaotust, mis sobivad juhendatud peenhäälestamiseks (sft).
Generatsiooni järjestamine (gen). Näidete arv jaotuse kohta on näidatud järgmiselt:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Järgnevad lahtrid näitavad peenhäälestuseks põhilist andmete ettevalmistamist:

### Visualiseerige mõned andmeread

Soovime, et see näidis töötaks kiiresti, seega salvestage train_sft, test_sft failid, mis sisaldavad 5% juba kärbitud ridadest. See tähendab, et peenhäälestatud mudelil on madalam täpsus, mistõttu ei tohiks seda kasutada reaalses maailmas.
Skript download-dataset.py kasutatakse ultrachat_200k andmestiku allalaadimiseks ja andmestiku teisendamiseks peenhäälestuse torujuhtme komponendi tarbitavasse vormingusse. Kuna andmestik on suur, siis siin on ainult osa andmestikust.

1. Alloleva skripti käivitamine laadib alla ainult 5% andmetest. Seda saab suurendada, muutes dataset_split_pc parameetri soovitud protsendiks.

    > [!NOTE]
    > Mõnel keelemudelil on erinevad keelekoodid ja seetõttu peaksid andmestiku veerunimed kajastama sama.

1. Siin on näide, kuidas andmed peaksid välja nägema:
Vestluse lõpetamise andmestik salvestatakse parquet-vormingus, kus iga kirje kasutab järgmist skeemi:

    - See on JSON (JavaScript Object Notation) dokument, mis on populaarne andmevahetusvorming. See ei ole täidetav kood, vaid viis andmete salvestamiseks ja edastamiseks. Siin on selle struktuuri ülevaade:

    - "prompt": See võti sisaldab stringi väärtust, mis esindab ülesannet või küsimust, mis esitatakse AI assistendile.

    - "messages": See võti sisaldab objektide massiivi. Iga objekt esindab sõnumit vestluses kasutaja ja AI assistendi vahel. Igal sõnumi objektil on kaks võtit:

    - "content": See võti sisaldab stringi väärtust, mis esindab sõnumi sisu.
    - "role": See võti sisaldab stringi väärtust, mis esindab sõnumi saatja rolli. See võib olla kas "user" või "assistant".
    - "prompt_id": See võti sisaldab stringi väärtust, mis esindab unikaalset identifikaatorit ülesande jaoks.

1. Selles konkreetses JSON dokumendis on esindatud vestlus, kus kasutaja palub AI assistendil luua peategelase düstoopilisele loole. Assistend vastab ja kasutaja palub rohkem detaile. Assistent nõustub detaile pakkuma. Kogu vestlus on seotud konkreetse prompt_id-ga.

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

### Andmete allalaadimine

1. See Python'i skript on mõeldud andmestiku allalaadimiseks, kasutades abiskripti nimega download-dataset.py. Siin on ülevaade, mida see teeb:

    - Impordib os mooduli, mis pakub operatsioonisüsteemiga seotud funktsionaalsust.

    - Kasutab os.system funktsiooni, et käivitada download-dataset.py skript shellis konkreetsete käsurea argumentidega. Argumendid määravad allalaaditava andmestiku (HuggingFaceH4/ultrachat_200k), kataloogi, kuhu see alla laaditakse (ultrachat_200k_dataset), ja protsendi andmestiku jaotamiseks (5). Funktsioon os.system tagastab käivitatud käsu väljumisoleku; see olek salvestatakse muutujasse exit_status.

    - Kontrollib, kas exit_status ei ole 0. Unix-laadsetes operatsioonisüsteemides näitab väljumisolek 0 tavaliselt, et käsk õnnestus, samas kui mis tahes muu number näitab viga. Kui exit_status ei ole 0, viskab Exception'i koos sõnumiga, mis näitab, et andmestiku allalaadimisel tekkis viga.

    - Kokkuvõttes käivitab see skript käsu, et laadida andmestik abiskripti abil, ja viskab erandi, kui käsk ebaõnnestub.

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

### Andmete laadimine DataFrame'i

1. See Python'i skript laadib JSON Lines faili pandas DataFrame'i ja kuvab esimesed 5 rida. Siin on ülevaade, mida see teeb:

    - Impordib pandas teegi, mis on võimas andmete manipuleerimise ja analüüsi teek.

    - Seadistab pandas'i kuvamisvalikute maksimaalse veeru laiuse väärtuseks 0. See tähendab, et iga veeru täielik tekst kuvatakse ilma kärpimiseta, kui DataFrame prinditakse.
- See kasutab funktsiooni pd.read_json, et laadida fail train_sft.jsonl kataloogist ultrachat_200k_dataset DataFrame'i. Argument lines=True näitab, et fail on JSON Lines formaadis, kus iga rida on eraldi JSON-objekt.

- See kasutab meetodit head, et kuvada DataFrame'i esimesed 5 rida. Kui DataFrame'is on vähem kui 5 rida, kuvatakse kõik read.

- Kokkuvõttes laadib see skript JSON Lines faili DataFrame'i ja kuvab esimesed 5 rida koos täisteksti veergudega.

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

## 5. Esita peenhäälestuse töö, kasutades mudelit ja andmeid sisenditena

Loo töö, mis kasutab chat-completion torujuhtme komponenti. Lisateavet kõigi peenhäälestuse jaoks toetatud parameetrite kohta leiate siit.

### Peenhäälestuse parameetrite määratlemine

1. Peenhäälestuse parameetrid saab jagada kahte kategooriasse - treeningparameetrid ja optimeerimisparameetrid.

1. Treeningparameetrid määravad treeningu aspektid, näiteks:

    - Millist optimeerijat ja ajastajat kasutada
    - Millist mõõdikut peenhäälestuse optimeerimiseks kasutada
    - Treeningusammude arv, partii suurus jne
    - Optimeerimisparameetrid aitavad GPU mälu optimeerida ja arvutusressursse tõhusalt kasutada.

1. Allpool on mõned selle kategooria parameetrid. Optimeerimisparameetrid erinevad iga mudeli puhul ja need on mudeliga pakendatud, et neid erinevusi hallata.

    - Luba deepspeed ja LoRA
    - Luba segatäpsusega treening
    - Luba mitme sõlmega treening

> [!NOTE]
> Juhendatud peenhäälestus võib põhjustada joondamise kaotust või katastroofilist unustamist. Soovitame seda probleemi kontrollida ja pärast peenhäälestust joondamise etappi läbi viia.

### Peenhäälestuse parameetrid

1. See Python-skript seab üles parameetrid masinõppemudeli peenhäälestamiseks. Siin on ülevaade, mida see teeb:

    - Seab vaikimisi treeningparameetrid, nagu treeningepohhide arv, treeningu ja hindamise partii suurused, õppemäär ja õppemäära ajastaja tüüp.

    - Seab vaikimisi optimeerimisparameetrid, näiteks kas rakendada Layer-wise Relevance Propagation (LoRa) ja DeepSpeed ning DeepSpeed'i etapp.

    - Kombineerib treening- ja optimeerimisparameetrid ühte sõnastikku nimega finetune_parameters.

    - Kontrollib, kas foundation_model sisaldab mudelispetsiifilisi vaikimisi. Kui see nii on, prindib hoiatussõnumi ja uuendab finetune_parameters sõnastikku nende mudelispetsiifiliste vaikimistega. Funktsiooni ast.literal_eval kasutatakse mudelispetsiifiliste vaikimiste teisendamiseks stringist Python-sõnastikuks.

    - Prindib lõpliku peenhäälestuse parameetrite komplekti, mida jooksutamiseks kasutatakse.

    - Kokkuvõttes seab see skript üles ja kuvab masinõppemudeli peenhäälestuse parameetrid, võimaldades vaikimisi parameetreid mudelispetsiifilistega üle kirjutada.

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

### Treeningtorujuhe

1. See Python-skript määratleb funktsiooni masinõppe treeningtorujuhtme kuvamise nime genereerimiseks ja kutsub seejärel selle funktsiooni välja, et genereerida ja printida kuvamise nimi. Siin on ülevaade, mida see teeb:

1. Funktsioon get_pipeline_display_name on määratletud. See funktsioon genereerib kuvamise nime, mis põhineb erinevatel treeningtorujuhtmega seotud parameetritel.

1. Funktsiooni sees arvutatakse kogu partii suurus, korrutades seadme kohta oleva partii suuruse, gradientide akumuleerimise sammude arvu, GPU-de arvu sõlme kohta ja sõlmede arvu, mida peenhäälestamiseks kasutatakse.

1. See hangib erinevaid muid parameetreid, nagu õppemäära ajastaja tüüp, kas DeepSpeed on rakendatud, DeepSpeed'i etapp, kas Layer-wise Relevance Propagation (LoRa) on rakendatud, mudeli kontrollpunktide arvu piirang ja maksimaalne järjestuse pikkus.

1. See koostab stringi, mis sisaldab kõiki neid parameetreid, eraldatuna sidekriipsudega. Kui DeepSpeed või LoRa on rakendatud, sisaldab string "ds", millele järgneb DeepSpeed'i etapp, või "lora". Kui mitte, sisaldab see "nods" või "nolora".

1. Funktsioon tagastab selle stringi, mis toimib treeningtorujuhtme kuvamise nimena.

1. Pärast funktsiooni määratlemist kutsutakse see välja, et genereerida kuvamise nimi, mis seejärel prinditakse.

1. Kokkuvõttes genereerib see skript masinõppe treeningtorujuhtme kuvamise nime, mis põhineb erinevatel parameetritel, ja prindib selle kuvamise nime.

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

### Torujuhtme konfigureerimine

See Python-skript määratleb ja konfigureerib masinõppe torujuhtme, kasutades Azure Machine Learning SDK-d. Siin on ülevaade, mida see teeb:

1. See impordib vajalikud moodulid Azure AI ML SDK-st.

1. See hangib torujuhtme komponendi nimega "chat_completion_pipeline" registrist.

1. See määratleb torujuhtme töö, kasutades `@pipeline` dekoraatorit ja funktsiooni `create_pipeline`. Torujuhtme nimi on seatud väärtusele `pipeline_display_name`.

1. Funktsiooni `create_pipeline` sees algatab see hangitud torujuhtme komponendi erinevate parameetritega, sealhulgas mudeli tee, arvutusklastrid erinevate etappide jaoks, andmekogumi jaotused treeninguks ja testimiseks, GPU-de arvu, mida peenhäälestamiseks kasutada, ja muud peenhäälestuse parameetrid.

1. See kaardistab peenhäälestuse töö väljundi torujuhtme töö väljundiga. See tehakse nii, et peenhäälestatud mudel saaks hõlpsasti registreeritud, mis on vajalik mudeli juurutamiseks veebis või partii lõpp-punktis.

1. See loob torujuhtme eksemplari, kutsudes välja funktsiooni `create_pipeline`.

1. See seab torujuhtme `force_rerun` seade väärtusele `True`, mis tähendab, et eelmiste tööde vahemällu salvestatud tulemusi ei kasutata.

1. See seab torujuhtme `continue_on_step_failure` seade väärtusele `False`, mis tähendab, et torujuhe peatub, kui mõni samm ebaõnnestub.

1. Kokkuvõttes määratleb ja konfigureerib see skript masinõppe torujuhtme vestluse lõpetamise ülesande jaoks, kasutades Azure Machine Learning SDK-d.

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

### Töö esitamine

1. See Python-skript esitab masinõppe torujuhtme töö Azure Machine Learning tööruumi ja ootab seejärel töö valmimist. Siin on ülevaade, mida see teeb:

    - See kutsub välja meetodi create_or_update objektis jobs tööruumi_ml_client'is, et esitada torujuhtme töö. Torujuhe, mida käitada, on määratud pipeline_object'iga ja eksperiment, mille all töö käivitatakse, on määratud experiment_name'iga.

    - Seejärel kutsub see välja meetodi stream objektis jobs tööruumi_ml_client'is, et oodata torujuhtme töö valmimist. Töö, mida oodata, on määratud pipeline_job objekti name atribuudiga.

    - Kokkuvõttes esitab see skript masinõppe torujuhtme töö Azure Machine Learning tööruumi ja ootab seejärel töö valmimist.

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

## 6. Registreeri peenhäälestatud mudel tööruumis

Registreerime mudeli peenhäälestuse töö väljundist. See jälgib seost peenhäälestatud mudeli ja peenhäälestuse töö vahel. Peenhäälestuse töö jälgib omakorda seost algmudeli, andmete ja treeningkoodiga.

### ML-mudeli registreerimine

1. See Python-skript registreerib masinõppemudeli, mis treeniti Azure Machine Learning torujuhtmes. Siin on ülevaade, mida see teeb:

    - See impordib vajalikud moodulid Azure AI ML SDK-st.

    - See kontrollib, kas treenitud_mudel väljund on saadaval torujuhtme tööst, kutsudes välja meetodi get objektis jobs tööruumi_ml_client'is ja pääsedes ligi selle outputs atribuudile.

    - See koostab tee treenitud mudelile, vormindades stringi torujuhtme töö nime ja väljundi nimega ("trained_model").

    - See määratleb peenhäälestatud mudeli nime, lisades algsele mudeli nimele "-ultrachat-200k" ja asendades kõik kaldkriipsud sidekriipsudega.

    - See valmistub mudeli registreerimiseks, luues Model objekti erinevate parameetritega, sealhulgas mudeli tee, mudeli tüübi (MLflow mudel), mudeli nime ja versiooni ning mudeli kirjeldusega.

    - See registreerib mudeli, kutsudes välja meetodi create_or_update objektis models tööruumi_ml_client'is, kasutades Model objekti argumendina.

    - See prindib registreeritud mudeli.

1. Kokkuvõttes registreerib see skript masinõppemudeli, mis treeniti Azure Machine Learning torujuhtmes.

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

## 7. Juuruta peenhäälestatud mudel veebipõhisesse lõpp-punkti

Veebipõhised lõpp-punktid pakuvad püsivat REST API-d, mida saab kasutada rakendustega integreerimiseks, mis vajavad mudeli kasutamist.

### Lõpp-punkti haldamine

1. See Python-skript loob hallatava veebipõhise lõpp-punkti Azure Machine Learning'is registreeritud mudeli jaoks. Siin on ülevaade, mida see teeb:

    - See impordib vajalikud moodulid Azure AI ML SDK-st.

    - See määratleb veebipõhise lõpp-punkti jaoks unikaalse nime, lisades stringile "ultrachat-completion-" ajatempli.

    - See valmistub veebipõhise lõpp-punkti loomiseks, luues ManagedOnlineEndpoint objekti erinevate parameetritega, sealhulgas lõpp-punkti nimi, lõpp-punkti kirjeldus ja autentimisrežiim ("key").

    - See loob veebipõhise lõpp-punkti, kutsudes välja meetodi begin_create_or_update objektis workspace_ml_client, kasutades ManagedOnlineEndpoint objekti argumendina. Seejärel ootab see loomistoimingu lõpuleviimist, kutsudes välja meetodi wait.

1. Kokkuvõttes loob see skript hallatava veebipõhise lõpp-punkti Azure Machine Learning'is registreeritud mudeli jaoks.

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
> Siit leiate juurutamiseks toetatud SKU-de loendi - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML-mudeli juurutamine

1. See Python-skript juurutab registreeritud masinõppemudeli hallatavasse veebipõhisesse lõpp-punkti Azure Machine Learning'is. Siin on ülevaade, mida see teeb:

    - See impordib ast mooduli, mis pakub funktsioone Python'i abstraktse süntaksi grammatika puude töötlemiseks.

    - See määrab juurutamise jaoks eksemplari tüübiks "Standard_NC6s_v3".

    - See kontrollib, kas inference_compute_allow_list silt on algmudelis olemas. Kui see on olemas, teisendab see sildi väärtuse stringist Python'i loendiks ja määrab selle väärtuseks inference_computes_allow_list. Kui see pole olemas, määrab selle väärtuseks None.

    - See kontrollib, kas määratud eksemplari tüüp on lubatud loendis. Kui see pole, prindib sõnumi, paludes kasutajal valida eksemplari tüüp lubatud loendist.

    - See valmistub juurutamise loomiseks, luues ManagedOnlineDeployment objekti erinevate parameetritega, sealhulgas juurutamise nimi, lõpp-punkti nimi, mudeli ID, eksemplari tüüp ja arv, elususe kontrolli seaded ja päringu seaded.

    - See loob juurutamise, kutsudes välja meetodi begin_create_or_update objektis workspace_ml_client, kasutades ManagedOnlineDeployment objekti argumendina. Seejärel ootab see loomistoimingu lõpuleviimist, kutsudes välja meetodi wait.

    - See määrab lõpp-punkti liikluse suunama 100% liiklusest "demo" juurutamisele.

    - See uuendab lõpp-punkti, kutsudes välja meetodi begin_create_or_update objektis workspace_ml_client, kasutades lõpp-punkti objekti argumendina. Seejärel ootab see uuendustoimingu lõpuleviimist, kutsudes välja meetodi result.

1. Kokkuvõttes juurutab see skript registreeritud masinõppemudeli hallatavasse veebipõhisesse lõpp-punkti Azure Machine Learning'is.

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

## 8. Testi lõpp-punkti näidisandmetega

Toome testandmekogumist mõned näidisandmed ja esitame need veebipõhisele lõpp-punktile järelduste tegemiseks. Seejärel kuvame hinnatud sildid koos tegelike siltidega.

### Tulemuste lugemine

1. See Python-skript loeb JSON Lines faili pandas DataFrame'i, valib juhusliku näidise ja lähtestab indeksi. Siin on ülevaade, mida see teeb:

    - See loeb faili ./ultrachat_200k_dataset/test_gen.jsonl pandas DataFrame'i. Funktsiooni read_json kasutatakse koos argumendiga lines=True, kuna fail on JSON Lines formaadis, kus iga rida on eraldi JSON-objekt.

    - See valib juhusliku näidise 1 reast DataFrame'is. Funktsiooni sample kasutatakse koos argumendiga n=1, et määrata juhuslikult valitavate ridade arv.

    - See lähtestab DataFrame'i indeksi. Funktsiooni reset_index kasutatakse koos argumendiga drop=True, et eemaldada algne indeks ja asendada see uue vaikimisi täisarvulise indeksiga.

    - See kuvab DataFrame'i esimesed 2 rida, kasutades funktsiooni head koos argumendiga 2. Kuid kuna pärast valimist sisaldab DataFrame ainult ühte rida, kuvatakse ainult see üks rida.

1. Kokkuvõttes loeb see skript JSON Lines faili pandas DataFrame'i, valib juhusliku näidise 1 reast, lähtestab indeksi ja kuvab esimese rea.

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

### JSON-objekti loomine

1. See Python-skript loob JSON-objekti kindlate parameetritega ja salvestab selle faili. Siin on ülevaade, mida see teeb:

    - See impordib json mooduli, mis pakub funktsioone JSON-andmetega töötamiseks.
- See loob sõnastiku nimega parameters, mille võtmed ja väärtused esindavad masinõppe mudeli parameetreid. Võtmed on "temperature", "top_p", "do_sample" ja "max_new_tokens", ning nende vastavad väärtused on 0.6, 0.9, True ja 200.

- See loob teise sõnastiku nimega test_json, millel on kaks võtit: "input_data" ja "params". "input_data" väärtuseks on teine sõnastik, mille võtmed on "input_string" ja "parameters". "input_string" väärtuseks on loend, mis sisaldab test_df DataFrame'i esimest sõnumit. "parameters" väärtuseks on varem loodud parameters sõnastik. "params" väärtuseks on tühi sõnastik.

- See avab faili nimega sample_score.json.

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

### Endpointi kasutamine

1. See Python skript kasutab Azure Machine Learningi veebipõhist endpointi, et skoorida JSON-faili. Siin on ülevaade, mida see teeb:

   - See kutsub workspace_ml_client objekti online_endpoints omaduse invoke meetodit. Seda meetodit kasutatakse veebipõhisele endpointile päringu saatmiseks ja vastuse saamiseks.

   - See määrab endpointi ja deploymendi nime argumentidega endpoint_name ja deployment_name. Antud juhul endpointi nimi on salvestatud muutujasse online_endpoint_name ja deploymendi nimi on "demo".

   - See määrab skooritava JSON-faili tee argumendiga request_file. Antud juhul failiks on ./ultrachat_200k_dataset/sample_score.json.

   - See salvestab endpointilt saadud vastuse muutujasse response.

   - See prindib toorvastuse.

1. Kokkuvõttes kutsub see skript Azure Machine Learningi veebipõhist endpointi, et skoorida JSON-faili, ja prindib vastuse.

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

## 9. Veebipõhise endpointi kustutamine

1. Ära unusta veebipõhist endpointi kustutada, muidu jääb arvutusressursside arvestus aktiivseks ja sellega kaasnevad kulud. See Python koodirida kustutab Azure Machine Learningi veebipõhise endpointi. Siin on ülevaade, mida see teeb:

   - See kutsub workspace_ml_client objekti online_endpoints omaduse begin_delete meetodit. Seda meetodit kasutatakse veebipõhise endpointi kustutamise alustamiseks.

   - See määrab kustutatava endpointi nime argumendiga name. Antud juhul endpointi nimi on salvestatud muutujasse online_endpoint_name.

   - See kutsub wait meetodit, et oodata kustutamise operatsiooni lõppu. See on blokeeriv operatsioon, mis tähendab, et skript ei jätka enne, kui kustutamine on lõpetatud.

   - Kokkuvõttes alustab see koodirida Azure Machine Learningi veebipõhise endpointi kustutamist ja ootab operatsiooni lõppu.

    ```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.