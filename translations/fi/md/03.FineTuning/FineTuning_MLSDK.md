<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:31:05+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "fi"
}
-->
## Kuinka käyttää chat-completion-komponentteja Azure ML -järjestelmärekisteristä mallin hienosäätöön

Tässä esimerkissä teemme hienosäädön Phi-3-mini-4k-instruct-mallille, jotta se osaa täydentää keskustelun kahden henkilön välillä käyttäen ultrachat_200k-datasarjaa.

![MLFineTune](../../../../translated_images/fi/MLFineTune.928d4c6b3767dd35.png)

Esimerkki näyttää, miten hienosäätö tehdään Azure ML SDK:lla ja Pythonilla, ja miten hienosäädetty malli otetaan käyttöön online-päätepisteessä reaaliaikaista päättelyä varten.

### Koulutusdata

Käytämme ultrachat_200k-datasarjaa. Tämä on voimakkaasti suodatettu versio UltraChat-datasarjasta, jota käytettiin Zephyr-7B-β:n kouluttamiseen, joka on huippuluokan 7 miljardin parametrin chat-malli.

### Malli

Käytämme Phi-3-mini-4k-instruct-mallia näyttämään, miten käyttäjä voi hienosäätää mallin chat-completion-tehtävään. Jos avasit tämän muistikirjan tietystä mallikortista, muista korvata mallin nimi vastaavasti.

### Tehtävät

- Valitse hienosäädettävä malli.
- Valitse ja tutki koulutusdata.
- Määritä hienosäätötyö.
- Suorita hienosäätötyö.
- Tarkastele koulutus- ja arviointimittareita.
- Rekisteröi hienosäädetty malli.
- Ota hienosäädetty malli käyttöön reaaliaikaista päättelyä varten.
- Siivoa resurssit.

## 1. Valmistele esivaatimukset

- Asenna riippuvuudet
- Yhdistä AzureML-työtilaan. Lisätietoja löytyy kohdasta SDK-todennuksen asetukset. Korvaa alla <WORKSPACE_NAME>, <RESOURCE_GROUP> ja <SUBSCRIPTION_ID>.
- Yhdistä azureml-järjestelmärekisteriin
- Aseta valinnainen kokeen nimi
- Tarkista tai luo laskentaresurssi.

> [!NOTE]
> Vaatimuksena on yksittäinen GPU-solmu, jossa voi olla useita GPU-kortteja. Esimerkiksi Standard_NC24rs_v3-solmussa on 4 NVIDIA V100 GPU:ta, kun taas Standard_NC12s_v3-solmussa on 2 NVIDIA V100 GPU:ta. Katso lisätietoja dokumentaatiosta. GPU-korttien määrä per solmu määritetään alla parametrilla gpus_per_node. Oikea arvo varmistaa kaikkien GPU:iden käytön solmussa. Suositellut GPU-laskentatyypit löytyvät täältä ja täältä.

### Python-kirjastot

Asenna riippuvuudet suorittamalla alla oleva solu. Tämä ei ole valinnainen vaihe uudessa ympäristössä.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Vuorovaikutus Azure ML:n kanssa

1. Tämä Python-skripti on tarkoitettu vuorovaikutukseen Azure Machine Learning (Azure ML) -palvelun kanssa. Tässä mitä se tekee:

    - Se tuo tarvittavat moduulit azure.ai.ml, azure.identity ja azure.ai.ml.entities -paketeista. Lisäksi se tuo time-moduulin.

    - Se yrittää todennusta DefaultAzureCredential()-luokalla, joka tarjoaa yksinkertaistetun todennuksen Azure-pilvessä ajettaville sovelluksille. Jos tämä epäonnistuu, se käyttää InteractiveBrowserCredential()-luokkaa, joka avaa interaktiivisen kirjautumisikkunan.

    - Se yrittää luoda MLClient-instanssin from_config-metodilla, joka lukee asetukset oletuskonfiguraatiotiedostosta (config.json). Jos tämä epäonnistuu, se luo MLClient-instanssin manuaalisesti antamalla subscription_id, resource_group_name ja workspace_name.

    - Se luo toisen MLClient-instanssin Azure ML -rekisterille nimeltä "azureml". Tämä rekisteri sisältää mallit, hienosäätöputket ja ympäristöt.

    - Se asettaa experiment_name-arvoksi "chat_completion_Phi-3-mini-4k-instruct".

    - Se luo uniikin aikaleiman muuntamalla nykyisen ajan (sekunteina epochista liukulukuna) kokonaisluvuksi ja sitten merkkijonoksi. Tätä aikaleimaa voi käyttää uniikkien nimien ja versioiden luomiseen.

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

## 2. Valitse perusmalli hienosäätöön

1. Phi-3-mini-4k-instruct on 3,8 miljardin parametrin kevyt, huippuluokan avoin malli, joka perustuu Phi-2:n käyttämään datasarjaan. Malli kuuluu Phi-3-malliperheeseen, ja Mini-versiota on kahta tyyppiä: 4K ja 128K, jotka kuvaavat kontekstin pituutta (tokeneina), jota malli tukee. Malli täytyy hienosäätää omaan käyttötarkoitukseen. Voit selata näitä malleja AzureML Studion Model Catalogissa suodattamalla chat-completion-tehtävän mukaan. Tässä esimerkissä käytämme Phi-3-mini-4k-instruct-mallia. Jos avasit tämän muistikirjan eri mallille, vaihda mallin nimi ja versio vastaavasti.

    > [!NOTE]
    > Mallin id-ominaisuus. Tätä käytetään syötteenä hienosäätötyöhön. Se löytyy myös Asset ID -kentästä mallin tiedoissa AzureML Studion Model Catalogissa.

2. Tämä Python-skripti on vuorovaikutuksessa Azure Machine Learning (Azure ML) -palvelun kanssa. Tässä mitä se tekee:

    - Se asettaa model_name-arvoksi "Phi-3-mini-4k-instruct".

    - Se käyttää registry_ml_client-objektin models-ominaisuuden get-metodia hakeakseen mallin viimeisimmän version Azure ML -rekisteristä. get-metodi saa kaksi argumenttia: mallin nimen ja labelin, joka määrittää, että haetaan viimeisin versio.

    - Se tulostaa konsoliin viestin, jossa kerrotaan mallin nimi, versio ja id, joita käytetään hienosäätöön. Viestiin lisätään tiedot foundation_model-objektin ominaisuuksista.

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

## 3. Luo laskentaresurssi työtä varten

Hienosäätötyö toimii VAIN GPU-laskennalla. Laskennan koko riippuu mallin koosta, ja oikean laskennan valinta voi olla haastavaa. Tässä solussa ohjataan käyttäjää valitsemaan sopiva laskentaresurssi.

> [!NOTE]
> Alla listatut laskennat toimivat optimaalisella kokoonpanolla. Muutokset voivat aiheuttaa Cuda Out Of Memory -virheen. Tällöin kokeile päivittää laskenta suurempaan kokoon.

> [!NOTE]
> Valitessasi compute_cluster_size varmista, että laskenta on saatavilla resurssiryhmässäsi. Jos tietty laskenta ei ole saatavilla, voit pyytää pääsyä laskentaresursseihin.

### Mallin hienosäätötuen tarkistus

1. Tämä Python-skripti on vuorovaikutuksessa Azure Machine Learning (Azure ML) -mallin kanssa. Tässä mitä se tekee:

    - Se tuo ast-moduulin, joka tarjoaa funktioita Pythonin abstraktin syntaksipuun käsittelyyn.

    - Se tarkistaa, onko foundation_model-objektilla tagi nimeltä finetune_compute_allow_list. Tagit Azure ML:ssä ovat avain-arvo-pareja, joita voi käyttää mallien suodattamiseen ja lajitteluun.

    - Jos finetune_compute_allow_list-tagi löytyy, se käyttää ast.literal_eval-funktiota turvallisesti muuntaakseen tagin arvon (merkkijonon) Python-listaksi. Tämä lista tallennetaan computes_allow_list-muuttujaan. Se tulostaa viestin, että laskenta tulisi luoda listan perusteella.

    - Jos tagia ei löydy, computes_allow_list asetetaan None-arvoksi ja tulostetaan viesti, että tagi ei kuulu mallin tageihin.

    - Yhteenvetona skripti tarkistaa mallin metatiedoista tietyn tagin, muuntaa sen arvon listaksi jos se on olemassa, ja antaa käyttäjälle palautetta.

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

### Laskenta-instanssin tarkistus

1. Tämä Python-skripti on vuorovaikutuksessa Azure Machine Learning (Azure ML) -palvelun kanssa ja suorittaa useita tarkistuksia laskenta-instanssille. Tässä mitä se tekee:

    - Se yrittää hakea compute_cluster-nimisen laskenta-instanssin Azure ML -työtilasta. Jos instanssin provisioning-tila on "failed", se nostaa ValueErrorin.

    - Se tarkistaa, onko computes_allow_list ei-None. Jos on, se muuttaa kaikki listan laskentakoot pieniksi kirjaimiksi ja tarkistaa, onko nykyisen instanssin koko listassa. Jos ei ole, se nostaa ValueErrorin.

    - Jos computes_allow_list on None, se tarkistaa, onko instanssin koko kiellettyjen GPU-VM-kokojen listalla. Jos on, se nostaa ValueErrorin.

    - Se hakee kaikki työtilan saatavilla olevat laskentakoot. Käy ne läpi ja jos jokin vastaa instanssin kokoa, se hakee kyseisen laskentakoon GPU-määrän ja asettaa gpu_count_found-arvoksi True.

    - Jos gpu_count_found on True, se tulostaa GPU-määrän instanssissa. Muuten se nostaa ValueErrorin.

    - Yhteenvetona skripti tarkistaa laskenta-instanssin provisioning-tilan, koon sallitun listan tai kielletyn listan mukaan, ja GPU-määrän.

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

## 4. Valitse datasarja mallin hienosäätöön

1. Käytämme ultrachat_200k-datasarjaa. Datasarjassa on neljä osaa, jotka sopivat valvottuun hienosäätöön (sft). Generointijärjestys (gen). Esimerkkien määrä per osa on seuraava:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Seuraavat solut näyttävät perusdatan valmistelun hienosäätöä varten:

### Visualisoi muutama datarivi

Haluamme, että tämä esimerkki suoritetaan nopeasti, joten tallennamme train_sft ja test_sft -tiedostot, jotka sisältävät 5 % jo rajatuista riveistä. Tämä tarkoittaa, että hienosäädetyn mallin tarkkuus on alhaisempi, joten sitä ei tulisi käyttää tuotantokäytössä.
download-dataset.py -skripti lataa ultrachat_200k-datasarjan ja muuntaa sen hienosäätöputken komponenttien käyttämään muotoon. Koska datasarja on suuri, meillä on tässä vain osa siitä.

1. Alla oleva skripti lataa vain 5 % datasta. Tätä voi kasvattaa muuttamalla dataset_split_pc-parametria haluttuun prosenttiosuuteen.

    > [!NOTE]
    > Joillakin kielimalleilla on eri kielikoodit, joten datasarjan sarakenimien tulisi vastata tätä.

1. Tässä esimerkki siitä, miltä data näyttää
Chat-completion-datasarja on tallennettu parquet-muodossa, ja jokainen merkintä noudattaa seuraavaa rakennetta:

    - Tämä on JSON (JavaScript Object Notation) -dokumentti, joka on suosittu tiedonvaihtoformaatti. Se ei ole suoritettavaa koodia, vaan tapa tallentaa ja siirtää tietoa. Tässä rakenne:

    - "prompt": Avain, jonka arvo on merkkijono, joka kuvaa tehtävää tai kysymystä AI-avustajalle.

    - "messages": Avain, jonka arvo on taulukko objekteja. Jokainen objekti edustaa viestiä käyttäjän ja AI-avustajan välisessä keskustelussa. Jokaisella viestiobjektilla on kaksi avainta:

    - "content": Merkkijono, joka sisältää viestin sisällön.
    - "role": Merkkijono, joka kertoo viestin lähettäjän roolin. Se voi olla "user" tai "assistant".
    - "prompt_id": Merkkijono, joka on yksilöllinen tunniste promptille.

1. Tässä JSON-dokumentissa käydään keskustelu, jossa käyttäjä pyytää AI-avustajaa luomaan päähenkilön dystooppiseen tarinaan. Avustaja vastaa, ja käyttäjä pyytää lisätietoja. Avustaja suostuu antamaan lisätietoja. Koko keskustelu liittyy tiettyyn prompt_id:hen.

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

### Lataa data

1. Tämä Python-skripti lataa datasarjan apuskriptillä download-dataset.py. Tässä mitä se tekee:

    - Se tuo os-moduulin, joka tarjoaa käyttöjärjestelmäriippuvaisia toimintoja.

    - Se käyttää os.system-funktiota ajaakseen download-dataset.py-skriptin komentoriviparametreilla. Parametrit määrittävät ladattavan datasarjan (HuggingFaceH4/ultrachat_200k), hakemiston (ultrachat_200k_dataset) ja datan osan prosentteina (5). os.system palauttaa komennon poistumistilan, joka tallennetaan exit_status-muuttujaan.

    - Se tarkistaa, onko exit_status eri kuin 0. Unix-tyyppisissä järjestelmissä 0 tarkoittaa onnistumista, muut arvot virhettä. Jos exit_status ei ole 0, se nostaa poikkeuksen, jossa kerrotaan virhe latauksessa.

    - Yhteenvetona skripti ajaa komennon datasarjan lataamiseksi apuskriptillä ja nostaa virheen, jos lataus epäonnistuu.

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

### Lataa data DataFrameen

1. Tämä Python-skripti lataa JSON Lines -tiedoston pandas DataFrameen ja näyttää ensimmäiset 5 riviä. Tässä mitä se tekee:

    - Se tuo pandas-kirjaston, joka on tehokas tietojen käsittely- ja analysointikirjasto.

    - Se asettaa pandas:n näyttöasetuksissa sarakkeiden maksimileveydeksi 0, mikä tarkoittaa, että sarakkeiden koko sisältö näytetään ilman katkaisua.

    - Se käyttää pd.read_json-funktiota ladatakseen train_sft.jsonl-tiedoston ultrachat_200k_dataset-hakemistosta DataFrameen. lines=True tarkoittaa, että tiedosto on JSON Lines -muodossa, jossa jokainen rivi on oma JSON-objekti.
- Se käyttää head-metodia näyttääkseen DataFramen ensimmäiset 5 riviä. Jos DataFramessa on alle 5 riviä, se näyttää kaikki rivit.

- Yhteenvetona tämä skripti lataa JSON Lines -tiedoston DataFrameen ja näyttää ensimmäiset 5 riviä täydellisine saraketeksteineen.

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

## 5. Lähetä hienosäätötyö käyttäen mallia ja dataa syötteinä

Luo työ, joka käyttää chat-completion pipeline -komponenttia. Lue lisää kaikista hienosäätöä tukevista parametreista.

### Määritä hienosäätöparametrit

1. Hienosäätöparametrit voidaan jakaa kahteen ryhmään – koulutusparametrit ja optimointiparametrit

1. Koulutusparametrit määrittelevät koulutuksen osa-alueet, kuten -

    - Käytettävän optimointimenetelmän ja ajastimen
    - Mittarin, jota hienosäädössä optimoidaan
    - Koulutusaskelten määrän, eräkoot ja niin edelleen
    - Optimointiparametrit auttavat optimoimaan GPU-muistia ja käyttämään laskentaresursseja tehokkaasti.

1. Alla on muutamia tähän kategoriaan kuuluvia parametreja. Optimointiparametrit vaihtelevat mallikohtaisesti ja ne sisältyvät mallipakettiin näiden erojen hallitsemiseksi.

    - Ota käyttöön deepspeed ja LoRA
    - Ota käyttöön mixed precision -koulutus
    - Ota käyttöön monisolmuinen koulutus


> [!NOTE]
> Ohjattu hienosäätö voi johtaa kohdistuksen menetykseen tai katastrofaaliseen unohtamiseen. Suosittelemme tarkistamaan tämän ongelman ja suorittamaan kohdistusvaiheen hienosäädön jälkeen.

### Hienosäätöparametrit

1. Tämä Python-skripti määrittää parametrit koneoppimismallin hienosäätöä varten. Tässä yhteenveto siitä, mitä se tekee:

    - Se asettaa oletuskoulutusparametrit, kuten koulutusepokien määrän, eräkoot koulutukselle ja arvioinnille, oppimisnopeuden ja oppimisnopeuden ajastimen tyypin.

    - Se asettaa oletusoptimointiparametrit, kuten Layer-wise Relevance Propagationin (LoRa) ja DeepSpeedin käytön sekä DeepSpeed-vaiheen.

    - Se yhdistää koulutus- ja optimointiparametrit yhdeksi sanakirjaksi nimeltä finetune_parameters.

    - Se tarkistaa, onko foundation_modelilla mallikohtaisia oletusparametreja. Jos on, se tulostaa varoituksen ja päivittää finetune_parameters-sanakirjan näillä mallikohtaisilla oletuksilla. ast.literal_eval -funktiota käytetään muuntamaan mallikohtaiset oletukset merkkijonosta Python-sanakirjaksi.

    - Se tulostaa lopullisen hienosäätöparametrien joukon, jota käytetään suorituksessa.

    - Yhteenvetona tämä skripti määrittää ja näyttää koneoppimismallin hienosäätöparametrit, mahdollistaen oletusparametrien korvaamisen mallikohtaisilla arvoilla.

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

### Koulutusputki

1. Tämä Python-skripti määrittelee funktion, joka luo näyttönimen koneoppimisen koulutusputkelle, ja kutsuu tätä funktiota näyttönimen luomiseksi ja tulostamiseksi. Tässä yhteenveto siitä, mitä se tekee:

1. Määritellään get_pipeline_display_name-funktio, joka luo näyttönimen koulutusputken eri parametreihin perustuen.

1. Funktion sisällä lasketaan kokonaiseräkoko kertomalla laitekohtainen eräkoko, gradienttien kertymisaskelten määrä, solmukohtainen GPU-määrä ja hienosäätöön käytettyjen solmujen määrä.

1. Haetaan muita parametreja, kuten oppimisnopeuden ajastimen tyyppi, onko DeepSpeed käytössä, DeepSpeed-vaihe, onko Layer-wise Relevance Propagation (LoRa) käytössä, säilytettävien mallitarkistuspisteiden enimmäismäärä ja maksimisekvenssin pituus.

1. Rakennetaan merkkijono, joka sisältää kaikki nämä parametrit yhdistettynä väliviivoin. Jos DeepSpeed tai LoRa on käytössä, merkkijono sisältää "ds" ja DeepSpeed-vaiheen tai "lora". Muussa tapauksessa se sisältää "nods" tai "nolora".

1. Funktio palauttaa tämän merkkijonon, joka toimii koulutusputken näyttönimenä.

1. Funktion määrittelyn jälkeen sitä kutsutaan näyttönimen luomiseksi, joka tulostetaan.

1. Yhteenvetona tämä skripti luo koneoppimisen koulutusputken näyttönimen eri parametrien perusteella ja tulostaa sen.

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

### Putken konfigurointi

Tämä Python-skripti määrittelee ja konfiguroi koneoppimisen putken Azure Machine Learning SDK:lla. Tässä yhteenveto siitä, mitä se tekee:

1. Se tuo tarvittavat moduulit Azure AI ML SDK:sta.

1. Se hakee rekisteristä pipeline-komponentin nimeltä "chat_completion_pipeline".

1. Se määrittelee pipeline-työn käyttäen `@pipeline`-koristetta ja funktiota `create_pipeline`. Putken nimeksi asetetaan `pipeline_display_name`.

1. `create_pipeline`-funktion sisällä alustetaan haettu pipeline-komponentti eri parametreilla, mukaan lukien mallin polku, laskentaklustereita eri vaiheisiin, datasetin jaot koulutukseen ja testaukseen, hienosäätöön käytettävien GPU:iden määrä ja muut hienosäätöparametrit.

1. Se yhdistää hienosäätötyön tulosteen pipeline-työn tulosteeksi, jotta hienosäädetty malli voidaan helposti rekisteröidä, mikä on tarpeen mallin käyttöönotossa online- tai batch-päätepisteeseen.

1. Se luo pipeline-instanssin kutsumalla `create_pipeline`-funktiota.

1. Se asettaa pipeline:n `force_rerun`-asetuksen arvoksi `True`, mikä tarkoittaa, että aiempien töiden välimuistissa olevia tuloksia ei käytetä.

1. Se asettaa pipeline:n `continue_on_step_failure`-asetuksen arvoksi `False`, eli pipeline pysähtyy, jos jokin vaihe epäonnistuu.

1. Yhteenvetona tämä skripti määrittelee ja konfiguroi koneoppimisen putken chat completion -tehtävään Azure Machine Learning SDK:lla.

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

### Lähetä työ

1. Tämä Python-skripti lähettää koneoppimisen pipeline-työn Azure Machine Learning -työtilaan ja odottaa työn valmistumista. Tässä yhteenveto siitä, mitä se tekee:

    - Se kutsuu workspace_ml_clientin jobs-olion create_or_update-metodia pipeline-työn lähettämiseksi. Suoritettava pipeline määritellään pipeline_objectilla ja kokeilu, jonka alla työ suoritetaan, määritellään experiment_name-arvolla.

    - Sen jälkeen se kutsuu workspace_ml_clientin jobs-olion stream-metodia odottaakseen pipeline-työn valmistumista. Odotettava työ määritellään pipeline_job-olion name-attribuutilla.

    - Yhteenvetona tämä skripti lähettää koneoppimisen pipeline-työn Azure Machine Learning -työtilaan ja odottaa työn valmistumista.

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

## 6. Rekisteröi hienosäädetty malli työtilaan

Rekisteröimme mallin hienosäätötyön tuloksena. Tämä seuraa jäljitettävyyttä hienosäädetyn mallin ja hienosäätötyön välillä. Hienosäätötyö puolestaan seuraa jäljitettävyyttä perustamalliin, dataan ja koulutuskoodiin.

### ML-mallin rekisteröinti

1. Tämä Python-skripti rekisteröi koneoppimismallin, joka on koulutettu Azure Machine Learning -putkessa. Tässä yhteenveto siitä, mitä se tekee:

    - Se tuo tarvittavat moduulit Azure AI ML SDK:sta.

    - Se tarkistaa, onko pipeline-työn trained_model-tulos saatavilla kutsumalla workspace_ml_clientin jobs-olion get-metodia ja pääsemällä sen outputs-attribuuttiin.

    - Se rakentaa polun koulutettuun malliin muotoilemalla merkkijonon pipeline-työn nimen ja tuloksen ("trained_model") nimen avulla.

    - Se määrittelee hienosäädetylle mallille nimen lisäämällä alkuperäisen mallin nimeen "-ultrachat-200k" ja korvaamalla mahdolliset kauttaviivat väliviivoilla.

    - Se valmistautuu rekisteröimään mallin luomalla Model-olion, johon sisältyy mallin polku, mallin tyyppi (MLflow-malli), mallin nimi ja versio sekä mallin kuvaus.

    - Se rekisteröi mallin kutsumalla workspace_ml_clientin models-olion create_or_update-metodia Model-oliolla argumenttina.

    - Se tulostaa rekisteröidyn mallin.

1. Yhteenvetona tämä skripti rekisteröi koneoppimismallin, joka on koulutettu Azure Machine Learning -putkessa.

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

## 7. Ota hienosäädetty malli käyttöön online-päätepisteessä

Online-päätepisteet tarjoavat kestävän REST-rajapinnan, jota voidaan käyttää sovelluksissa, jotka tarvitsevat mallin käyttöä.

### Päätepisteen hallinta

1. Tämä Python-skripti luo hallitun online-päätepisteen Azure Machine Learningissä rekisteröidylle mallille. Tässä yhteenveto siitä, mitä se tekee:

    - Se tuo tarvittavat moduulit Azure AI ML SDK:sta.

    - Se määrittelee uniikin nimen online-päätepisteelle lisäämällä aikaleiman merkkijonoon "ultrachat-completion-".

    - Se valmistautuu luomaan online-päätepisteen luomalla ManagedOnlineEndpoint-olion, johon sisältyy päätepisteen nimi, kuvaus ja todennustila ("key").

    - Se luo online-päätepisteen kutsumalla workspace_ml_clientin begin_create_or_update-metodia ManagedOnlineEndpoint-oliolla argumenttina ja odottaa luontiprosessin valmistumista kutsumalla wait-metodia.

1. Yhteenvetona tämä skripti luo hallitun online-päätepisteen Azure Machine Learningissä rekisteröidylle mallille.

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
> Täältä löydät listan käyttöönottoa tukevista SKU:ista - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML-mallin käyttöönotto

1. Tämä Python-skripti ottaa rekisteröidyn koneoppimismallin käyttöön hallitussa online-päätepisteessä Azure Machine Learningissä. Tässä yhteenveto siitä, mitä se tekee:

    - Se tuo ast-moduulin, joka tarjoaa funktioita Pythonin abstraktin syntaksipuun käsittelyyn.

    - Se asettaa käyttöönoton instanssityypiksi "Standard_NC6s_v3".

    - Se tarkistaa, onko foundation_modelissa inference_compute_allow_list -tagi. Jos on, se muuntaa tagin arvon merkkijonosta Python-listaksi ja asettaa sen inference_computes_allow_list -muuttujaan. Jos ei ole, asettaa arvoksi None.

    - Se tarkistaa, onko määritelty instanssityyppi sallittujen listalla. Jos ei ole, se tulostaa viestin, jossa pyytää käyttäjää valitsemaan instanssityypin sallitulta listalta.

    - Se valmistautuu luomaan käyttöönoton luomalla ManagedOnlineDeployment-olion, johon sisältyy käyttöönoton nimi, päätepisteen nimi, mallin ID, instanssityyppi ja -määrä, liveness probe -asetukset ja pyyntöasetukset.

    - Se luo käyttöönoton kutsumalla workspace_ml_clientin begin_create_or_update-metodia ManagedOnlineDeployment-oliolla argumenttina ja odottaa luontiprosessin valmistumista kutsumalla wait-metodia.

    - Se asettaa päätepisteen liikenteen ohjaamaan 100 % liikenteestä "demo"-käyttöönotolle.

    - Se päivittää päätepisteen kutsumalla workspace_ml_clientin begin_create_or_update-metodia päätepiste-oliolla argumenttina ja odottaa päivityksen valmistumista kutsumalla result-metodia.

1. Yhteenvetona tämä skripti ottaa rekisteröidyn koneoppimismallin käyttöön hallitussa online-päätepisteessä Azure Machine Learningissä.

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

## 8. Testaa päätepistettä esimerkkidatalla

Haemme esimerkkidataa testidatasetistä ja lähetämme sen online-päätepisteeseen inferenssiä varten. Näytämme sitten arvioidut luokat rinnakkain todellisten luokkien kanssa.

### Tulosten lukeminen

1. Tämä Python-skripti lukee JSON Lines -tiedoston pandas DataFrameen, ottaa satunnaisotoksen ja nollaa indeksin. Tässä yhteenveto siitä, mitä se tekee:

    - Se lukee tiedoston ./ultrachat_200k_dataset/test_gen.jsonl pandas DataFrameen. read_json-funktiota käytetään lines=True -parametrilla, koska tiedosto on JSON Lines -muodossa, jossa kukin rivi on erillinen JSON-objekti.

    - Se ottaa satunnaisotoksen yhdestä rivistä DataFramesta. sample-funktiota käytetään n=1 -parametrilla määrittämään valittavien rivien määrä.

    - Se nollaa DataFramen indeksin. reset_index-funktiota käytetään drop=True -parametrilla, jolloin alkuperäinen indeksi poistetaan ja korvataan oletuskokonaislukuarvoilla.

    - Se näyttää DataFramen ensimmäiset 2 riviä head-funktiolla argumentilla 2. Koska DataFrame sisältää otoksen jälkeen vain yhden rivin, tämä näyttää vain kyseisen rivin.

1. Yhteenvetona tämä skripti lukee JSON Lines -tiedoston pandas DataFrameen, ottaa satunnaisotoksen yhdestä rivistä, nollaa indeksin ja näyttää ensimmäisen rivin.

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

### Luo JSON-objekti

1. Tämä Python-skripti luo JSON-objektin tietyillä parametreilla ja tallentaa sen tiedostoon. Tässä yhteenveto siitä, mitä se tekee:

    - Se tuo json-moduulin, joka tarjoaa funktioita JSON-datan käsittelyyn.

    - Se luo sanakirjan parameters, jonka avaimet ja arvot kuvaavat koneoppimismallin parametreja. Avaimet ovat "temperature", "top_p", "do_sample" ja "max_new_tokens", ja niiden arvot ovat vastaavasti 0.6, 0.9, True ja 200.

    - Se luo toisen sanakirjan test_json, jossa on kaksi avainta: "input_data" ja "params". "input_data":n arvo on toinen sanakirja, jonka avaimet ovat "input_string" ja "parameters". "input_string":n arvo on lista, joka sisältää ensimmäisen viestin test_df DataFramesta. "parameters":n arvo on aiemmin luotu parameters-sanakirja. "params":n arvo on tyhjä sanakirja.
- Se avaa tiedoston nimeltä sample_score.json

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

### Päätepisteen kutsuminen

1. Tämä Python-skripti kutsuu Azure Machine Learningin online-päätepistettä pisteyttääkseen JSON-tiedoston. Tässä on erittely siitä, mitä se tekee:

    - Se kutsuu workspace_ml_client-olion online_endpoints-ominaisuuden invoke-metodia. Tätä metodia käytetään lähettämään pyyntö online-päätepisteelle ja saamaan vastaus.

    - Se määrittää päätepisteen ja käyttöönoton nimet endpoint_name- ja deployment_name-argumenteilla. Tässä tapauksessa päätepisteen nimi on tallennettu online_endpoint_name-muuttujaan ja käyttöönoton nimi on "demo".

    - Se määrittää pisteytettävän JSON-tiedoston polun request_file-argumentilla. Tässä tapauksessa tiedosto on ./ultrachat_200k_dataset/sample_score.json.

    - Se tallentaa päätepisteen vastauksen response-muuttujaan.

    - Se tulostaa raakavastauksen.

1. Yhteenvetona, tämä skripti kutsuu Azure Machine Learningin online-päätepistettä pisteyttääkseen JSON-tiedoston ja tulostaa vastauksen.

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

## 9. Poista online-päätepiste

1. Muista poistaa online-päätepiste, muuten laskutus jatkuu käytetyn laskentatehon osalta. Tämä Python-koodirivi poistaa online-päätepisteen Azure Machine Learningissä. Tässä on erittely siitä, mitä se tekee:

    - Se kutsuu workspace_ml_client-olion online_endpoints-ominaisuuden begin_delete-metodia. Tätä metodia käytetään aloittamaan online-päätepisteen poisto.

    - Se määrittää poistettavan päätepisteen nimen name-argumentilla. Tässä tapauksessa päätepisteen nimi on tallennettu online_endpoint_name-muuttujaan.

    - Se kutsuu wait-metodia odottaakseen poisto-operaation valmistumista. Tämä on estävä operaatio, eli se estää skriptiä jatkamasta ennen kuin poisto on valmis.

    - Yhteenvetona, tämä koodirivi aloittaa online-päätepisteen poiston Azure Machine Learningissä ja odottaa operaation valmistumista.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.