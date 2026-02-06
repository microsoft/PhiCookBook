## Hvordan bruger man chat-completion komponenter fra Azure ML systemregisteret til finjustering af en model

I dette eksempel vil vi udføre finjustering af Phi-3-mini-4k-instruct modellen for at fuldføre en samtale mellem 2 personer ved brug af ultrachat_200k datasættet.

![MLFineTune](../../../../translated_images/da/MLFineTune.928d4c6b3767dd35.webp)

Eksemplet vil vise, hvordan man udfører finjustering ved brug af Azure ML SDK og Python og derefter udruller den finjusterede model til en online endepunkt til realtidsinferens.

### Træningsdata

Vi vil bruge ultrachat_200k datasættet. Dette er en kraftigt filtreret version af UltraChat datasættet og blev brugt til at træne Zephyr-7B-β, en topmoderne 7b chat-model.

### Model

Vi vil bruge Phi-3-mini-4k-instruct modellen til at vise, hvordan brugeren kan finjustere en model til chat-completion opgaven. Hvis du har åbnet denne notesbog fra et specifikt modelkort, skal du huske at erstatte det specifikke modelnavn.

### Opgaver

- Vælg en model til finjustering.
- Vælg og udforsk træningsdata.
- Konfigurer finjusteringsjobbet.
- Kør finjusteringsjobbet.
- Gennemgå trænings- og evalueringsmålinger.
- Registrer den finjusterede model.
- Udrul den finjusterede model til realtidsinferens.
- Ryd op i ressourcer.

## 1. Opsæt forudsætninger

- Installer afhængigheder
- Forbind til AzureML Workspace. Læs mere ved opsætning af SDK autentificering. Erstat <WORKSPACE_NAME>, <RESOURCE_GROUP> og <SUBSCRIPTION_ID> nedenfor.
- Forbind til azureml systemregister
- Sæt et valgfrit eksperimentnavn
- Tjek eller opret compute.

> [!NOTE]
> Krav: en enkelt GPU-node kan have flere GPU-kort. For eksempel har en node af Standard_NC24rs_v3 4 NVIDIA V100 GPU'er, mens Standard_NC12s_v3 har 2 NVIDIA V100 GPU'er. Se dokumentationen for denne information. Antallet af GPU-kort pr. node sættes i parameteren gpus_per_node nedenfor. At sætte denne værdi korrekt sikrer udnyttelse af alle GPU'er i noden. De anbefalede GPU compute SKUs kan findes her og her.

### Python biblioteker

Installer afhængigheder ved at køre nedenstående celle. Dette er ikke et valgfrit trin, hvis man kører i et nyt miljø.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interaktion med Azure ML

1. Dette Python script bruges til at interagere med Azure Machine Learning (Azure ML) tjenesten. Her er en opsummering af, hvad det gør:

    - Det importerer nødvendige moduler fra pakkerne azure.ai.ml, azure.identity og azure.ai.ml.entities. Det importerer også time modulet.

    - Det forsøger at autentificere ved hjælp af DefaultAzureCredential(), som giver en forenklet autentificeringsoplevelse til hurtigt at begynde udvikling af applikationer kørt i Azure skyen. Hvis dette fejler, falder det tilbage til InteractiveBrowserCredential(), som giver en interaktiv login prompt.

    - Dernæst forsøger det at oprette en MLClient instans ved hjælp af from_config metoden, som læser konfigurationen fra standard konfigurationsfilen (config.json). Hvis dette fejler, opretter det en MLClient instans ved manuelt at angive subscription_id, resource_group_name og workspace_name.

    - Det opretter en anden MLClient instans, denne gang til Azure ML registret navngivet "azureml". Dette register er hvor modeller, finjusterings-pipelines og miljøer bliver gemt.

    - Det sætter experiment_name til "chat_completion_Phi-3-mini-4k-instruct".

    - Det genererer et unikt timestamp ved at konvertere det aktuelle tidspunkt (i sekunder siden epoken som et flydende tal) til et heltal og derefter til en streng. Dette timestamp kan bruges til at skabe unikke navne og versioner.

    ```python
    # Importer nødvendige moduler fra Azure ML og Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Importer tidsmodul
    
    # Prøv at godkende ved hjælp af DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Hvis DefaultAzureCredential fejler, brug InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Prøv at oprette en MLClient-instans ved hjælp af standard konfigurationsfil
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Hvis det fejler, opret en MLClient-instans ved manuelt at angive detaljer
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Opret en anden MLClient-instans for Azure ML-registreringsdatabasen med navnet "azureml"
    # Denne registreringsdatabase er hvor modeller, finjusterings pipelines og miljøer gemmes
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Indstil eksperimentets navn
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generer et unikt tidsstempel, der kan bruges til navne og versioner, der skal være unikke
    timestamp = str(int(time.time()))
    ```

## 2. Vælg en fundamentmodel til finjustering

1. Phi-3-mini-4k-instruct er en 3,8 mia. parameter, letvægts, topmoderne open model bygget på datasæt brugt til Phi-2. Modellen tilhører Phi-3 model familien, og Mini versionen findes i to varianter 4K og 128K, som angiver kontekstlængden (i tokens), den kan håndtere. Vi skal finjustere modellen til vores specifikke formål for at kunne bruge den. Du kan browse disse modeller i Modelkataloget i AzureML Studio, filtreret på chat-completion opgaven. I dette eksempel bruger vi Phi-3-mini-4k-instruct modellen. Hvis du har åbnet denne notesbog for en anden model, skal du erstatte modelnavnet og versionen tilsvarende.

> [!NOTE]
> model id egenskaben for modellen. Denne vil blive brugt som input til finjusteringsjobbet. Denne findes også som Asset ID feltet på modelsidet i AzureML Studio Modelkatalog.

2. Dette Python script interagerer med Azure Machine Learning (Azure ML) tjenesten. Her er en opsummering af, hvad det gør:

    - Det sætter model_name til "Phi-3-mini-4k-instruct".

    - Det bruger get metoden af models ejendommen på registry_ml_client objektet til at hente den nyeste version af modellen med det angivne navn fra Azure ML registret. Get metoden kaldes med to argumenter: navnet på modellen og en label der angiver, at den nyeste version skal hentes.

    - Det printer en besked til konsollen, der angiver navn, version og id på modellen, som skal bruges til finjustering. Format metoden på strengen bruges til at indsætte navn, version og id på modellen i beskeden. Navn, version og id hentes som egenskaber på foundation_model objektet.

    ```python
    # Angiv modelnavnet
    model_name = "Phi-3-mini-4k-instruct"
    
    # Hent den nyeste version af modellen fra Azure ML-registreringsdatabasen
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Udskriv modelnavnet, versionen og id'et
    # Disse oplysninger er nyttige til sporing og fejlfinding
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Opret en compute til brug for jobbet

Finjusteringsjobbet virker KUN med GPU compute. Compute størrelsen afhænger af hvor stor modellen er og i de fleste tilfælde kan det være vanskeligt at identificere den rette compute til jobbet. I denne celle guider vi brugeren til at vælge den rette compute til jobbet.

> [!NOTE]
> De nedenstående listede computes virker med den mest optimerede konfiguration. Eventuelle ændringer i konfigurationen kan føre til Cuda Out Of Memory fejl. I sådanne tilfælde bør man prøve at opgradere computen til en større compute størrelse.

> [!NOTE]
> Når man vælger compute_cluster_size nedenfor, skal man sikre sig, at computen er tilgængelig i din resourcegruppe. Hvis en bestemt compute ikke er tilgængelig, kan man anmode om adgang til computerrressourcerne.

### Tjek af model for finjusteringsstøtte

1. Dette Python script interagerer med en Azure Machine Learning (Azure ML) model. Her er en opsummering af, hvad det gør:

    - Det importerer ast modulet, som tilbyder funktioner til at behandle træer af Python abstrakt syntaks grammatik.

    - Det tjekker om foundation_model objektet (som repræsenterer en model i Azure ML) har et tag med navnet finetune_compute_allow_list. Tags i Azure ML er nøgle-værdi par, som man kan oprette og bruge til at filtrere og sortere modeller.

    - Hvis finetune_compute_allow_list tagget er til stede, bruger det ast.literal_eval funktionen til sikkert at parse taggets værdi (en streng) til en Python liste. Denne liste tildeles variablen computes_allow_list. Derefter printes en besked om at der skal oprettes compute fra listen.

    - Hvis finetune_compute_allow_list tagget ikke findes, sættes computes_allow_list til None og en besked printes om, at tagget ikke er en del af modellens tags.

    - Samlet set tjekker scriptet efter et specifikt tag i modellens metadata, konverterer taggets værdi til en liste hvis det findes, og giver feedback til brugeren.

    ```python
    # Importer ast-modulet, som leverer funktioner til at bearbejde træer af Pythons abstrakte syntaksgrammatik
    import ast
    
    # Tjek om 'finetune_compute_allow_list' tagget er til stede i modellens tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Hvis tagget er til stede, brug ast.literal_eval til sikkert at parse taggets værdi (en streng) til en Python-liste
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # konverter streng til python-liste
        # Udskriv en besked der angiver, at der skal oprettes en compute fra listen
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Hvis tagget ikke er til stede, sæt computes_allow_list til None
        computes_allow_list = None
        # Udskriv en besked der angiver, at 'finetune_compute_allow_list' tagget ikke er en del af modellens tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Tjek af Compute Instance

1. Dette Python script interagerer med Azure Machine Learning (Azure ML) tjenesten og udfører flere tjek på en compute instance. Her er en opsummering af, hvad det gør:

    - Det forsøger at hente compute instancen med det navn, der er gemt i compute_cluster, fra Azure ML workspace. Hvis compute instancens provisioning status er "failed", kastes en ValueError.

    - Det tjekker om computes_allow_list ikke er None. Hvis det ikke er det, konverterer den alle compute størrelser i listen til små bogstaver og tjekker om størrelsen på den aktuelle compute instance findes i listen. Hvis ikke kastes en ValueError.

    - Hvis computes_allow_list er None, tjekker den om størrelsen på compute instancen findes i en liste over ikke-understøttede GPU VM størrelser. Hvis den gør, kastes en ValueError.

    - Den henter en liste over alle tilgængelige compute størrelser i workspace. Itererer over denne liste, og for hver compute størrelse tjekker den om navnet matcher størrelsen på den aktuelle compute instance. Hvis ja, henter den antallet af GPU'er for denne compute størrelse og sætter gpu_count_found til True.

    - Hvis gpu_count_found er True, printes antallet af GPU'er i compute instancen. Hvis False kastes en ValueError.

    - Samlet set udfører scriptet en række tjek på en compute instance i et Azure ML workspace, inklusiv tjek af provisioning status, størrelsesgodkendelse mod en tilladelses- eller afvisningsliste, og antallet af GPU'er.

    ```python
    # Udskriv undtagelsesmeddelelsen
    print(e)
    # Rejs en ValueError hvis beregningsstørrelsen ikke er tilgængelig i arbejdsområdet
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Hent beregningsinstansen fra Azure ML arbejdsområdet
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Kontroller om forsyningstilstanden for beregningsinstansen er "fejlet"
    if compute.provisioning_state.lower() == "failed":
        # Rejs en ValueError hvis forsyningstilstanden er "fejlet"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Kontroller om computes_allow_list ikke er None
    if computes_allow_list is not None:
        # Konverter alle beregningsstørrelser i computes_allow_list til små bogstaver
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Kontroller om størrelsen på beregningsinstansen er i computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Rejs en ValueError hvis størrelsen på beregningsinstansen ikke er i computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Definer en liste over understøttede GPU VM-størrelser
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Kontroller om størrelsen på beregningsinstansen er i unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Rejs en ValueError hvis størrelsen på beregningsinstansen er i unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialiser et flag for at tjekke om antallet af GPU'er i beregningsinstansen er fundet
    gpu_count_found = False
    # Hent en liste over alle tilgængelige beregningsstørrelser i arbejdsområdet
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterer over listen af tilgængelige beregningsstørrelser
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Kontroller om navnet på beregningsstørrelsen matcher størrelsen på beregningsinstansen
        if compute_sku.name.lower() == compute.size.lower():
            # Hvis det gør, hent antallet af GPU'er for denne beregningsstørrelse og sæt gpu_count_found til True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Hvis gpu_count_found er True, udskriv antallet af GPU'er i beregningsinstansen
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Hvis gpu_count_found er False, rejs en ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Vælg datasættet til finjustering af modellen

1. Vi bruger ultrachat_200k datasættet. Datasættet har fire opdelinger, egnet til Supervised finjustering (sft).
Generationsrangering (gen). Antallet af eksempler pr. opdeling vises som følger:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. De næste par celler viser grundlæggende databehandling til finjustering:

### Visualiser nogle data rækker

Vi ønsker at dette eksempel kører hurtigt, så gem train_sft, test_sft filer, som indeholder 5% af de allerede trimmede rækker. Det betyder at den finjusterede model vil have lavere nøjagtighed, og derfor bør den ikke bruges i reelle scenarier.
download-dataset.py bruges til at hente ultrachat_200k datasættet og transformere datasættet til format, der kan bruges af finjusterings pipeline komponenten. Da datasættet er stort, har vi her kun en del af datasættet.

1. Kørsel af nedenstående script downloader kun 5% af data. Dette kan øges ved at ændre dataset_split_pc parameter til ønsket procentdel.

> [!NOTE]
> Nogle sprogmodeller har forskellige sproglignende koder, og derfor bør kolonnenavne i datasættet afspejle dette.

1. Her er et eksempel på, hvordan dataene skal se ud
chat-completion datasættet er gemt i parquet format, hvor hver post bruger følgende skema:

    - Dette er et JSON (JavaScript Object Notation) dokument, som er et populært dataudvekslingsformat. Det er ikke kørbar kode, men en måde at gemme og transportere data på. Her er en opdeling af strukturen:

    - "prompt": Denne nøgle indeholder en strengværdi, der repræsenterer en opgave eller et spørgsmål stillet til en AI-assistent.

    - "messages": Denne nøgle indeholder en liste af objekter. Hvert objekt repræsenterer en besked i en samtale mellem en bruger og en AI-assistent. Hvert besked-objekt har to nøgler:

    - "content": Denne nøgle indeholder en strengværdi, der repræsenterer indholdet af beskeden.
    - "role": Denne nøgle indeholder en strengværdi, som repræsenterer rollen af den enhed, der sendte beskeden. Det kan være enten "user" eller "assistant".
    - "prompt_id": Denne nøgle indeholder en strengværdi, der repræsenterer en unik identifikator for prompten.

1. I dette specifikke JSON dokument er en samtale repræsenteret, hvor en bruger beder en AI-assistent om at skabe en protagonist til en dystopisk historie. Assistenten svarer, og brugeren beder så om flere detaljer. Assistenten accepterer at give flere detaljer. Hele samtalen er tilknyttet en specifik prompt id.

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

### Download Data

1. Dette Python script bruges til at downloade et datasæt ved at bruge et hjælpe-script kaldet download-dataset.py. Her er en opsummering af, hvad det gør:

    - Det importerer os modulet, som giver en platformuafhængig måde at bruge operativsystemfunktionalitet.

    - Det bruger os.system funktionen til at køre download-dataset.py scriptet i shell med specifikke kommandolinjeargumenter. Argumenterne angiver datasættet der skal downloades (HuggingFaceH4/ultrachat_200k), den mappe det skal downloades til (ultrachat_200k_dataset), og procentdelen af datasættet som skal splittes (5). os.system funktionen returnerer afslutningsstatus for den udførte kommando; denne status gemmes i exit_status variablen.

    - Den tjekker om exit_status ikke er 0. I Unix-lignende systemer indikerer en exit status på 0 som regel, at kommandoen lykkedes, mens ethvert andet tal indikerer en fejl. Hvis exit_status ikke er 0, kaster den en Exception med en besked, der angiver at der var en fejl ved download af datasættet.

    - Sammensat kører scriptet en kommando for at downloade et datasæt ved hjælp af et hjælpe-script, og det kaster en undtagelse hvis kommandoen fejler.
    
    ```python
    # Importer os-modulet, som giver en måde at bruge operativsystemsafhængig funktionalitet på
    import os
    
    # Brug os.system-funktionen til at køre scriptet download-dataset.py i shell'en med specifikke kommandolinjeargumenter
    # Argumenterne angiver datasættet, der skal downloades (HuggingFaceH4/ultrachat_200k), mappen det skal downloades til (ultrachat_200k_dataset), og procentdelen af datasættet, der skal deles (5)
    # Os.system-funktionen returnerer afslutningsstatus for den kommando, den eksekverede; denne status gemmes i variablen exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Tjek om exit_status ikke er 0
    # I Unix-lignende operativsystemer indikerer en afslutningsstatus på 0 normalt, at en kommando har været succesfuld, mens et andet tal angiver en fejl
    # Hvis exit_status ikke er 0, kast en undtagelse med en meddelelse om, at der var en fejl ved download af datasættet
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Indlæsning af data i en DataFrame

1. Dette Python script indlæser en JSON Lines fil i en pandas DataFrame og viser de første 5 rækker. Her er en opsummering af, hvad det gør:

    - Det importerer pandas biblioteket, som er et kraftfuldt værktøj til datamanipulation og analyse.

    - Det sætter den maksimale kolonnebredde for pandas’ display muligheder til 0. Det betyder, at hele teksten for hver kolonne vil blive vist uden forkortelse, når DataFrame printes.
    - Den bruger pd.read_json-funktionen til at indlæse filen train_sft.jsonl fra mappen ultrachat_200k_dataset i en DataFrame. Argumentet lines=True angiver, at filen er i JSON Lines-format, hvor hver linje er et separat JSON-objekt.

    - Den bruger head-metoden til at vise de første 5 rækker af DataFrame'en. Hvis DataFrame'en har færre end 5 rækker, vil den vise alle.

    - Samlet set indlæser dette script en JSON Lines-fil i en DataFrame og viser de første 5 rækker med fuld kolonnetekst.
    
    ```python
    # Importer pandas-biblioteket, som er et kraftfuldt bibliotek til datamanipulation og analyse
    import pandas as pd
    
    # Indstil den maksimale kolonnebredde for pandas' visningsmuligheder til 0
    # Dette betyder, at den fulde tekst i hver kolonne vil blive vist uden forkortelse, når DataFrame printes
    pd.set_option("display.max_colwidth", 0)
    
    # Brug pd.read_json-funktionen til at indlæse filen train_sft.jsonl fra mappen ultrachat_200k_dataset i en DataFrame
    # Argumentet lines=True angiver, at filen er i JSON Lines-format, hvor hver linje er et separat JSON-objekt
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Brug head-metoden til at vise de første 5 rækker af DataFrame
    # Hvis DataFrame har færre end 5 rækker, vil den vise dem alle
    df.head()
    ```

## 5. Indsend finjusteringsjobbet ved brug af modellen og data som input

Opret jobbet, der bruger chat-completion pipeline-komponenten. Lær mere om alle de parametre, der understøttes til finjustering.

### Definer finjusteringsparametre

1. Finjusteringsparametre kan grupperes i 2 kategorier - træningsparametre, optimeringsparametre

1. Træningsparametre definerer træningsaspekter som -

    - Optimeringsmetoden, scheduler der skal bruges
    - Metrikken til at optimere finjusteringen
    - Antallet af træningstrin og batch-størrelse osv.
    - Optimeringsparametre hjælper med at optimere GPU-hukommelsen og effektivt bruge beregningsressourcerne.

1. Nedenfor er nogle af parametrene, der hører til denne kategori. Optimeringsparametrene varierer for hver model og er pakket sammen med modellen for at håndtere disse variationer.

    - Aktiver deepspeed og LoRA
    - Aktiver mixed precision training
    - Aktiver multi-node training

> [!NOTE]
> Overvåget finjustering kan medføre tab af alignment eller katastrofalt glemsel. Vi anbefaler at kontrollere for dette problem og køre en alignment-fase efter finjusteringen.

### Finjusteringsparametre

1. Dette Python-script opsætter parametre til finjustering af en maskinlæringsmodel. Her er en oversigt over, hvad det gør:

    - Det opsætter standard træningsparametre såsom antal træningsepochs, batch-størrelser til træning og evaluering, læringsrate og type af læringsrate-scheduler.

    - Det opsætter standard optimeringsparametre såsom om Layer-wise Relevance Propagation (LoRa) og DeepSpeed skal anvendes, og DeepSpeed stadiet.

    - Det kombinerer trænings- og optimeringsparametre i én ordbog kaldet finetune_parameters.

    - Det tjekker, om foundation_model har model-specifikke standardparametre. Hvis det har, udskriver den en advarselsbesked og opdaterer finetune_parameters-ordbogen med disse model-specifikke standarder. Funktionen ast.literal_eval bruges til at konvertere de model-specifikke standarder fra en streng til en Python-ordbog.

    - Den udskriver det endelige sæt af finjusteringsparametre, som vil blive brugt for kørslen.

    - Samlet set opsætter og viser dette script parametrene til finjustering af en maskinlæringsmodel med mulighed for at tilsidesætte standardparametrene med model-specifikke.

    ```python
    # Opsæt standard træningsparametre såsom antallet af trænings-epoker, batchstørrelser til træning og evaluering, læringsrate og type af læringsrate-planlægger
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Opsæt standard optimeringsparametre såsom om Layer-wise Relevance Propagation (LoRa) og DeepSpeed skal anvendes, samt DeepSpeed scenen
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Kombiner trænings- og optimeringsparametrene i en enkelt ordbog kaldet finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Tjek om foundation_model har model-specifikke standardparametre
    # Hvis den har, udskriv en advarselsbesked og opdater finetune_parameters ordbogen med disse model-specifikke standarder
    # Funktionen ast.literal_eval bruges til at konvertere de model-specifikke standarder fra en streng til en Python ordbog
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # konverter streng til python ordbog
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Udskriv det endelige sæt af fine-tuning parametre, der vil blive brugt til kørslen
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Træningspipeline

1. Dette Python-script definerer en funktion til at generere et visningsnavn for en maskinlærings træningspipeline og kalder derefter denne funktion for at generere og udskrive visningsnavnet. Her er en oversigt over, hvad det gør:

1. Funktionen get_pipeline_display_name defineres. Denne funktion genererer et visningsnavn baseret på forskellige parametre relateret til træningspipelinens opsætning.

1. Inde i funktionen beregner den den samlede batch-størrelse ved at multiplicere batch-størrelsen pr. enhed, antal gradient-akkumulerings-trin, antal GPU'er pr. node, og antal noder, der bruges til finjustering.

1. Den henter andre parametre såsom typen af læringsrate-scheduler, om DeepSpeed anvendes, DeepSpeed stadiet, om Layer-wise Relevance Propagation (LoRa) anvendes, grænsen på antal model-checkpoints der skal gemmes, og maksimal sekvenslængde.

1. Den konstruerer en streng, der inkluderer alle disse parametre adskilt af bindestreger. Hvis DeepSpeed eller LoRa anvendes, indeholder strengen henholdsvis "ds" efterfulgt af DeepSpeed stadiet eller "lora". Hvis ikke, indeholder den "nods" eller "nolora".

1. Funktionen returnerer denne streng, som tjener som visningsnavn for træningspipelinens kørsel.

1. Efter definitionen kaldes funktionen for at generere visningsnavnet, som herefter bliver udskrevet.

1. Samlet set genererer dette script et visningsnavn for en maskinlærings træningspipeline baseret på forskellige parametre og udskriver herefter dette visningsnavn.

    ```python
    # Definer en funktion til at generere et visningsnavn til træningspipelinjen
    def get_pipeline_display_name():
        # Beregn den samlede batchstørrelse ved at multiplicere batchstørrelsen pr. enhed, antallet af gradientakkumuleringssteps, antallet af GPU'er pr. node, og antallet af noder brugt til finjustering
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Hent typen af læringsrategenerator
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Hent om DeepSpeed anvendes
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Hent DeepSpeed stadiet
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Hvis DeepSpeed anvendes, inkluder "ds" efterfulgt af DeepSpeed stadiet i visningsnavnet; hvis ikke, inkluder "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Hent om Layer-wise Relevance Propagation (LoRa) anvendes
        lora = finetune_parameters.get("apply_lora", "false")
        # Hvis LoRa anvendes, inkluder "lora" i visningsnavnet; hvis ikke, inkluder "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Hent grænsen for antallet af model checkpoints, der skal gemmes
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Hent den maksimale sekvenslængde
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Konstruer visningsnavnet ved at sammenkæde alle disse parametre, adskilt af bindestreger
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
    
    # Kald funktionen for at generere visningsnavnet
    pipeline_display_name = get_pipeline_display_name()
    # Udskriv visningsnavnet
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Konfigurering af Pipeline

Dette Python-script definerer og konfigurerer en maskinlæringspipeline ved brug af Azure Machine Learning SDK. Her er en opsummering af, hvad det gør:

1. Det importerer nødvendige moduler fra Azure AI ML SDK.

1. Det henter en pipelinekomponent med navnet "chat_completion_pipeline" fra registret.

1. Det definerer et pipelinejob ved brug af `@pipeline` dekoratoren og funktionen `create_pipeline`. Navnet på pipelinen sættes til `pipeline_display_name`.

1. Inde i `create_pipeline` funktionen initialiserer den den hentede pipelinekomponent med forskellige parametre, bl.a. modelsti, compute-klynger til forskellige stadier, datasæt-split til træning og test, antal GPU'er til finjustering samt andre finjusteringsparametre.

1. Den mapper outputtet fra finjusteringsjobbet til outputtet fra pipelinejobbet. Dette gøres, så den finjusterede model nemt kan registreres, hvilket kræves for at deployere modellen til et online- eller batch-endpoint.

1. Den opretter en instans af pipelinen ved at kalde `create_pipeline` funktionen.

1. Den sætter pipelinens `force_rerun` indstilling til `True`, hvilket betyder, at cachede resultater fra tidligere job ikke vil blive brugt.

1. Den sætter pipelinens `continue_on_step_failure` indstilling til `False`, hvilket betyder, at pipelinen stopper, hvis et trin fejler.

1. Samlet set definerer og konfigurerer dette script en maskinlæringspipeline til en chat completion-opgave ved brug af Azure Machine Learning SDK.

    ```python
    # Importer nødvendige moduler fra Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Hent pipeline komponenten med navnet "chat_completion_pipeline" fra registret
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Definer pipeline jobben ved at bruge @pipeline dekoratøren og funktionen create_pipeline
    # Navnet på pipelinen sættes til pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialiser den hentede pipeline komponent med forskellige parametre
        # Disse inkluderer modelstien, compute klynger til forskellige stadier, datasæt opdelinger til træning og test, antallet af GPU'er til fine-tuning og andre fine-tuning parametre
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Kortlæg datasæt opdelinger til parametre
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Træningsindstillinger
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Sæt til antallet af GPU'er tilgængelige i computeren
            **finetune_parameters
        )
        return {
            # Kortlæg outputtet af fine tuning jobbet til outputtet af pipeline jobbet
            # Dette gøres så vi nemt kan registrere den finjusterede model
            # Registrering af modellen er krævet for at kunne implementere modellen til en online eller batch endepunkt
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Opret en instans af pipelinen ved at kalde create_pipeline funktionen
    pipeline_object = create_pipeline()
    
    # Brug ikke cachede resultater fra tidligere jobs
    pipeline_object.settings.force_rerun = True
    
    # Sæt fortsæt ved trinfejl til False
    # Dette betyder, at pipelinen stopper, hvis et trin fejler
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Indsend jobbet

1. Dette Python-script indsender et maskinlæringspipelinejob til et Azure Machine Learning arbejdsområde og venter derefter på, at jobbet bliver færdigt. Her er en oversigt over, hvad det gør:

    - Det kalder create_or_update-metoden på jobs-objektet i workspace_ml_client for at indsende pipelinejobbet. Pipelinjen, der skal køres, specificeres af pipeline_object, og eksperimentet, som jobbet køres under, specificeres af experiment_name.

    - Det kalder derefter stream-metoden på jobs-objektet i workspace_ml_client for at vente på, at pipelinejobbet bliver færdigt. Jobbet, der skal ventes på, specificeres ved navn-atributten på pipeline_job-objektet.

    - Samlet set indsender dette script et maskinlæringspipelinejob til et Azure Machine Learning arbejdsområde og venter derefter på, at jobbet bliver færdigt.

    ```python
    # Indsend pipeline-jobbet til Azure Machine Learning-arbejdsområdet
    # Pipelinjen, der skal køres, angives via pipeline_object
    # Eksperimentet, under hvilket jobbet køres, angives via experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Vent på, at pipeline-jobbet fuldføres
    # Jobbet, der skal ventes på, angives via navn-attributten i pipeline_job-objektet
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Registrer den finjusterede model i arbejdsområdet

Vi vil registrere modellen fra outputtet af finjusteringsjobbet. Dette vil spore slægtskab mellem den finjusterede model og finjusteringsjobbet. Finjusteringsjobbet sporer yderligere slægtskab til foundation-modellen, data og træningskode.

### Registrering af ML-model

1. Dette Python-script registrerer en maskinlæringsmodel, som blev trænet i en Azure Machine Learning-pipeline. Her er en oversigt over, hvad det gør:

    - Det importerer nødvendige moduler fra Azure AI ML SDK.

    - Det tjekker, om outputtet trained_model er tilgængeligt fra pipelinejobbet ved at kalde get-metoden på jobs-objektet i workspace_ml_client og adgangen til dets outputs-attribut.

    - Det konstruerer en sti til den trænede model ved at formatere en streng med navnet på pipelinejobbet og navnet på outputtet ("trained_model").

    - Det definerer et navn for den finjusterede model ved at tilføje "-ultrachat-200k" til det oprindelige modelnavn og erstatte eventuelle skråstreger med bindestreger.

    - Det forbereder registrering af modellen ved at oprette et Model-objekt med forskellige parametre, herunder sti til modellen, typen af model (MLflow-model), modelens navn og version samt en beskrivelse af modellen.

    - Det registrerer modellen ved at kalde create_or_update-metoden på models-objektet i workspace_ml_client med Model-objektet som argument.

    - Det udskriver den registrerede model.

1. Samlet set registrerer dette script en maskinlæringsmodel, som blev trænet i en Azure Machine Learning-pipeline.
    
    ```python
    # Importer nødvendige moduler fra Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Tjek om `trained_model` outputtet er tilgængeligt fra pipeline jobbet
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Konstruer en sti til den trænede model ved at formatere en streng med navnet på pipeline jobbet og navnet på outputtet ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Definer et navn til den finjusterede model ved at tilføje "-ultrachat-200k" til det originale modelnavn og erstatte alle skråstreger med bindestreger
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Forbered registrering af modellen ved at oprette et Model-objekt med forskellige parametre
    # Disse inkluderer stien til modellen, typen af modellen (MLflow model), navnet og versionen af modellen, samt en beskrivelse af modellen
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Brug tidsstempel som version for at undgå versionskonflikt
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Registrer modellen ved at kalde create_or_update metoden på models objektet i workspace_ml_client med Model objektet som argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Udskriv den registrerede model
    print("registered model: \n", registered_model)
    ```

## 7. Deployér den finjusterede model til et online-endpoint

Online endpoints giver en holdbar REST API, som kan bruges til at integrere med applikationer, der skal bruge modellen.

### Administrer Endpoint

1. Dette Python-script opretter et administreret online-endpoint i Azure Machine Learning for en registreret model. Her er en oversigt over, hvad det gør:

    - Det importerer nødvendige moduler fra Azure AI ML SDK.

    - Det definerer et unikt navn for online-endpointet ved at tilføje et tidsstempel til strengen "ultrachat-completion-".

    - Det forbereder oprettelse af online-endpointet ved at oprette et ManagedOnlineEndpoint-objekt med forskellige parametre, herunder navnet på endpointet, en beskrivelse af endpointet og autentificeringsmetoden ("key").

    - Det opretter online-endpointet ved at kalde begin_create_or_update-metoden på workspace_ml_client med ManagedOnlineEndpoint-objektet som argument. Derefter afventer det oprettelsesprocessen ved at kalde wait-metoden.

1. Samlet set opretter dette script et administreret online-endpoint i Azure Machine Learning for en registreret model.

    ```python
    # Importer nødvendige moduler fra Azure AI ML SDK'en
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Definer et unikt navn til den online endpoint ved at tilføje et tidsstempel til strengen "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Forbered oprettelse af den online endpoint ved at oprette et ManagedOnlineEndpoint-objekt med forskellige parametre
    # Disse inkluderer navnet på endpointen, en beskrivelse af endpointen og autentificeringsmetoden ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Opret den online endpoint ved at kalde begin_create_or_update-metoden på workspace_ml_client med ManagedOnlineEndpoint-objektet som argument
    # Vent derefter på, at oprettelsesoperationen er fuldført, ved at kalde wait-metoden
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Du kan finde listen over SKU'er, der understøttes til deployment her - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Deployering af ML-model

1. Dette Python-script deployerer en registreret maskinlæringsmodel til et administreret online-endpoint i Azure Machine Learning. Her er en oversigt over, hvad det gør:

    - Det importerer ast-modulet, som giver funktioner til at behandle træer i Pythons abstrakte syntaks.

    - Det sætter instanstypen til deployment til "Standard_NC6s_v3".

    - Det tjekker, om tagget inference_compute_allow_list er til stede i foundation model. Hvis det er, konverterer det tagværdien fra en streng til en Python-liste og tildeler den til inference_computes_allow_list. Hvis ikke, sætter det inference_computes_allow_list til None.

    - Det tjekker, om den specificerede instanstype er på tilladelseslisten. Hvis den ikke er, udskriver det en besked, som beder brugeren vælge en instanstype fra listen.

    - Det forbereder oprettelsen af deployment ved at oprette et ManagedOnlineDeployment-objekt med forskellige parametre, herunder navnet på deploymenten, navnet på endpointet, ID'et for modellen, instanstype og antal instanser, liveness probe-indstillinger og request-indstillinger.

    - Det opretter deployment ved at kalde begin_create_or_update-metoden på workspace_ml_client med ManagedOnlineDeployment-objektet som argument. Den venter derefter på, at oprettelsesoperationen bliver færdig ved at kalde wait-metoden.

    - Det sætter trafikken på endpointet til at dirigere 100 % af trafikken til "demo"-deploymenten.

    - Det opdaterer endpointet ved at kalde begin_create_or_update-metoden på workspace_ml_client med endpoint-objektet som argument. Den venter derefter på, at opdateringsoperationen bliver færdig ved at kalde result-metoden.

1. Samlet set deployerer dette script en registreret maskinlæringsmodel til et administreret online-endpoint i Azure Machine Learning.

    ```python
    # Importer ast-modulet, som leverer funktioner til at behandle træer af Pythons abstrakte syntaksgrammatik
    import ast
    
    # Indstil instanstypen for udrulningen
    instance_type = "Standard_NC6s_v3"
    
    # Tjek om tagget `inference_compute_allow_list` er til stede i grundmodellen
    if "inference_compute_allow_list" in foundation_model.tags:
        # Hvis det er, konverter tagværdien fra en streng til en Python-liste og tildel den til `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Hvis ikke, sæt `inference_computes_allow_list` til `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Tjek om den angivne instanstype er i tilladelseslisten
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Forbered oprettelse af udrulningen ved at oprette et `ManagedOnlineDeployment`-objekt med forskellige parametre
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Opret udrulningen ved at kalde `begin_create_or_update`-metoden af `workspace_ml_client` med `ManagedOnlineDeployment`-objektet som argument
    # Vent derefter på, at oprettelsesoperationen fuldføres ved at kalde `wait`-metoden
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Indstil trafik på endepunktet til at dirigere 100 % af trafikken til "demo"-udrulningen
    endpoint.traffic = {"demo": 100}
    
    # Opdater endepunktet ved at kalde `begin_create_or_update`-metoden af `workspace_ml_client` med `endpoint`-objektet som argument
    # Vent derefter på, at opdateringsoperationen fuldføres ved at kalde `result`-metoden
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Test endpointet med prøve-data

Vi vil hente noget prøve-data fra testdatasættet og sende det til online-endpointet til inferens. Derefter vil vi vise de scorede labels side om side med de sande labels.

### Læs resultaterne

1. Dette Python-script læser en JSON Lines-fil ind i en pandas DataFrame, tager et tilfældigt prøveudtag, og nulstiller indekset. Her er en oversigt over, hvad det gør:

    - Det læser filen ./ultrachat_200k_dataset/test_gen.jsonl ind i en pandas DataFrame. Funktionen read_json bruges med argumentet lines=True, fordi filen er i JSON Lines-format, hvor hver linje er et separat JSON-objekt.

    - Det tager et tilfældigt prøveudtag med 1 række fra DataFrame'en. Funktionen sample bruges med n=1 til at angive, at der skal vælges 1 tilfældig række.

    - Det nulstiller DataFrame'ens indeks. Funktionen reset_index bruges med drop=True for at droppe det oprindelige indeks og erstatte det med et nyt indeks bestående af standard heltal.

    - Det viser de første 2 rækker af DataFrame'en ved at bruge head-funktionen med argumentet 2. Men da DataFrame'en kun indeholder én række efter prøveudtaget, vil den kun vise denne ene række.

1. Samlet set læser dette script en JSON Lines-fil ind i en pandas DataFrame, tager et tilfældigt prøveudtag på 1 række, nulstiller indekset og viser den første række.
    
    ```python
    # Importer pandas biblioteket
    import pandas as pd
    
    # Læs JSON Lines-filen './ultrachat_200k_dataset/test_gen.jsonl' ind i en pandas DataFrame
    # Argumentet 'lines=True' angiver, at filen er i JSON Lines-format, hvor hver linje er et separat JSON-objekt
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Tag et tilfældigt udvalg af 1 række fra DataFrame
    # Argumentet 'n=1' specificerer antallet af tilfældige rækker, der skal vælges
    test_df = test_df.sample(n=1)
    
    # Nulstil indeks i DataFrame
    # Argumentet 'drop=True' angiver, at det oprindelige indeks skal fjernes og erstattes med et nyt indeks af standard heltalsværdier
    # Argumentet 'inplace=True' angiver, at DataFrame skal ændres på stedet (uden at oprette et nyt objekt)
    test_df.reset_index(drop=True, inplace=True)
    
    # Vis de første 2 rækker af DataFrame
    # Da DataFrame dog kun indeholder én række efter udvælgelsen, vil dette kun vise den ene række
    test_df.head(2)
    ```

### Opret JSON-objekt

1. Dette Python-script opretter et JSON-objekt med specifikke parametre og gemmer det i en fil. Her er en oversigt over, hvad det gør:

    - Det importerer json-modulet, som giver funktioner til at arbejde med JSON-data.
- Den opretter en ordbog parameters med nøgler og værdier, der repræsenterer parametre for en maskinlæringsmodel. Nøglerne er "temperature", "top_p", "do_sample" og "max_new_tokens", og deres tilsvarende værdier er henholdsvis 0,6, 0,9, True og 200.

- Den opretter en anden ordbog test_json med to nøgler: "input_data" og "params". Værdien af "input_data" er en anden ordbog med nøglerne "input_string" og "parameters". Værdien af "input_string" er en liste, der indeholder den første besked fra DataFrame test_df. Værdien af "parameters" er den tidligere oprettede parameters-ordbog. Værdien af "params" er en tom ordbog.

- Den åbner en fil med navnet sample_score.json

    ```python
    # Importer json-modulet, som giver funktioner til at arbejde med JSON-data
    import json
    
    # Opret en ordbog `parameters` med nøgler og værdier, der repræsenterer parametre for en maskinlæringsmodel
    # Nøglerne er "temperature", "top_p", "do_sample" og "max_new_tokens", og deres tilsvarende værdier er henholdsvis 0,6, 0,9, True og 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Opret en anden ordbog `test_json` med to nøgler: "input_data" og "params"
    # Værdien af "input_data" er en anden ordbog med nøglerne "input_string" og "parameters"
    # Værdien af "input_string" er en liste, der indeholder den første besked fra `test_df` DataFrame
    # Værdien af "parameters" er den tidligere oprettede `parameters` ordbog
    # Værdien af "params" er en tom ordbog
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Åbn en fil med navnet `sample_score.json` i `./ultrachat_200k_dataset` mappen i skrive-tilstand
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Skriv `test_json` ordbogen til filen i JSON-format ved hjælp af `json.dump` funktionen
        json.dump(test_json, f)
    ```

### Kald af Endepunkt

1. Dette Python-script kalder et online endepunkt i Azure Machine Learning for at score en JSON-fil. Her er en oversigt over, hvad det gør:

    - Det kalder metoden invoke af online_endpoints-ejendommen i workspace_ml_client-objektet. Denne metode bruges til at sende en anmodning til et online endepunkt og få et svar.

    - Det angiver navnet på endepunktet og deployment med argumenterne endpoint_name og deployment_name. I dette tilfælde er endepunktsnavnet gemt i variablen online_endpoint_name, og deployment-navnet er "demo".

    - Det angiver stien til JSON-filen, der skal scores, med argumentet request_file. I dette tilfælde er filen ./ultrachat_200k_dataset/sample_score.json.

    - Det gemmer svaret fra endepunktet i variablen response.

    - Det udskriver det rå svar.

1. Kort sagt kalder dette script et online endepunkt i Azure Machine Learning for at score en JSON-fil og udskriver svaret.

    ```python
    # Påkald online-endpointet i Azure Machine Learning for at score filen `sample_score.json`
    # Metoden `invoke` af `online_endpoints`-egenskaben i `workspace_ml_client`-objektet bruges til at sende en forespørgsel til et online-endpoint og få et svar
    # Argumentet `endpoint_name` angiver navnet på endpointet, som er gemt i variablen `online_endpoint_name`
    # Argumentet `deployment_name` angiver navnet på deployeringen, som er "demo"
    # Argumentet `request_file` angiver stien til JSON-filen, der skal scores, som er `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Udskriv det rå svar fra endpointet
    print("raw response: \n", response, "\n")
    ```

## 9. Slet det online endepunkt

1. Glem ikke at slette det online endepunkt, ellers vil du efterlade regnemåleren kørende for den beregning, der bruges af endepunktet. Denne Python-kodelinje sletter et online endepunkt i Azure Machine Learning. Her er en oversigt over, hvad den gør:

    - Den kalder metoden begin_delete af online_endpoints-ejendommen i workspace_ml_client-objektet. Denne metode bruges til at starte sletningen af et online endepunkt.

    - Den angiver navnet på det endepunkt, der skal slettes, med argumentet name. I dette tilfælde er navnet på endepunktet gemt i variablen online_endpoint_name.

    - Den kalder metoden wait for at vente på, at sletteoperationen er færdig. Dette er en blokerende operation, hvilket betyder, at den forhindrer scriptet i at fortsætte, indtil sletningen er afsluttet.

    - Sammenfattende starter denne kodelinje sletningen af et online endepunkt i Azure Machine Learning og venter på, at operationen er gennemført.

    ```python
    # Slet den online endepunkt i Azure Machine Learning
    # `begin_delete`-metoden for `online_endpoints`-egenskaben på `workspace_ml_client`-objektet bruges til at starte sletningen af en online endepunkt
    # Argumentet `name` angiver navnet på den endepunkt, der skal slettes, som er gemt i variablen `online_endpoint_name`
    # `wait`-metoden kaldes for at vente på, at sletteoperationen er fuldført. Dette er en blokkerende operation, hvilket betyder, at scriptet ikke fortsætter, før sletningen er færdig
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->