## Hur man använder chat-kompletteringskomponenter från Azure ML systemregistret för att finjustera en modell

I detta exempel kommer vi att genomföra finjustering av Phi-3-mini-4k-instruct modellen för att slutföra en konversation mellan 2 personer med hjälp av ultrachat_200k dataset.

![MLFineTune](../../../../translated_images/sv/MLFineTune.928d4c6b3767dd35.webp)

Exemplet visar hur man genomför finjustering med Azure ML SDK och Python, och sedan distribuerar den finjusterade modellen till en online-endpoint för realtidsinferens.

### Träningsdata

Vi kommer att använda ultrachat_200k dataset. Detta är en kraftigt filtrerad version av UltraChat-datasetet och användes för att träna Zephyr-7B-β, en toppmodern 7b chattmodell.

### Modell

Vi kommer att använda Phi-3-mini-4k-instruct modellen för att visa hur användare kan finjustera en modell för chat-komplettering. Om du öppnade detta anteckningsblock från ett specifikt modellkort, kom ihåg att byta ut det specifika modellnamnet.

### Uppgifter

- Välj en modell att finjustera.
- Välj och utforska träningsdata.
- Konfigurera finjusteringsjobbet.
- Kör finjusteringsjobbet.
- Granska tränings- och utvärderingsmått.
- Registrera den finjusterade modellen.
- Distribuera den finjusterade modellen för realtidsinferens.
- Rensa upp resurser.

## 1. Sätt upp förutsättningar

- Installera beroenden
- Anslut till AzureML Workspace. Läs mer under sätt upp SDK-auktorisering. Ersätt <WORKSPACE_NAME>, <RESOURCE_GROUP> och <SUBSCRIPTION_ID> nedan.
- Anslut till azureml systemregister
- Sätt ett valfritt experimentnamn
- Kontrollera eller skapa compute.

> [!NOTE]
> Krav: en enskild GPU-nod kan ha flera GPU-kort. Till exempel, i en nod av Standard_NC24rs_v3 finns det 4 NVIDIA V100 GPU:er medan i Standard_NC12s_v3 finns det 2 NVIDIA V100 GPU:er. Se dokumentationen för denna information. Antalet GPU-kort per nod sätts i parametern gpus_per_node nedan. Att sätta detta värde korrekt säkerställer att alla GPU:er i noden används. De rekommenderade GPU compute SKU:erna finns här och här.

### Python-bibliotek

Installera beroenden genom att köra nedanstående cell. Detta är inte ett valfritt steg om du kör i en ny miljö.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interagera med Azure ML

1. Detta Python-skript används för att interagera med Azure Machine Learning (Azure ML) tjänsten. Här är en sammanfattning av vad det gör:

    - Det importerar nödvändiga moduler från paketen azure.ai.ml, azure.identity och azure.ai.ml.entities. Det importerar även modulen time.

    - Det försöker autentisera med DefaultAzureCredential(), vilket ger en förenklad autentiseringsupplevelse för snabb utveckling av applikationer som körs i Azure-molnet. Om detta misslyckas går det över till InteractiveBrowserCredential() som ger en interaktiv inloggningsprompt.

    - Därefter försöker det skapa en MLClient-instans med metoden from_config som läser konfigurationen från standardkonfigurationsfilen (config.json). Om detta misslyckas skapas MLClient-instansen manuellt genom att ange subscription_id, resource_group_name och workspace_name.

    - Det skapar även en annan MLClient-instans, denna gång för Azure ML registret med namnet "azureml". Det registret är där modeller, finjusterings-pipelines och miljöer lagras.

    - Det sätter experiment_name till "chat_completion_Phi-3-mini-4k-instruct".

    - Det genererar en unik tidsstämpel genom att konvertera aktuell tid (i sekunder sedan epoken, som ett flyttal) till ett heltal och sedan till en sträng. Denna tidsstämpel kan användas för att skapa unika namn och versioner.

    ```python
    # Importera nödvändiga moduler från Azure ML och Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Importera time-modulen
    
    # Försök att autentisera med DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Om DefaultAzureCredential misslyckas, använd InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Försök att skapa en MLClient-instans med standard konfigurationsfil
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Om det misslyckas, skapa en MLClient-instans genom att manuellt ange detaljerna
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Skapa ytterligare en MLClient-instans för Azure ML-registret med namnet "azureml"
    # Det här registret är där modeller, finjusteringspipelines och miljöer lagras
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Sätt experimentnamnet
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generera en unik tidsstämpel som kan användas för namn och versioner som måste vara unika
    timestamp = str(int(time.time()))
    ```

## 2. Välj en grundmodell att finjustera

1. Phi-3-mini-4k-instruct är en modell med 3,8 miljarder parametrar, lättviktig och toppmodern öppen modell byggd på dataset som användes för Phi-2. Modellen tillhör Phi-3 modellfamiljen och Mini-versionen finns i två varianter: 4K och 128K, vilket är kontextlängden (i tokens) den kan stödja. Vi behöver finjustera modellen för vårt specifika syfte för att kunna använda den. Du kan bläddra bland dessa modeller i Model Catalog i AzureML Studio, filtrera efter chat-kompletteringsuppgiften. I detta exempel använder vi Phi-3-mini-4k-instruct modellen. Om du har öppnat detta anteckningsblock för en annan modell, byt modellnamn och version därefter.

> [!NOTE]
> modellens id-egenskap. Detta kommer att användas som indata till finjusteringsjobbet. Det finns också som fältet Asset ID på modellens detaljsida i AzureML Studio Model Catalog.

2. Detta Python-skript interagerar med Azure Machine Learning (Azure ML) tjänsten. Här är en sammanfattning av vad det gör:

    - Det sätter model_name till "Phi-3-mini-4k-instruct".

    - Det använder get-metoden av modellen properties i registry_ml_client objektet för att hämta senaste versionen av modellen med det angivna namnet från Azure ML registret. Get-metoden kallas med två argument: modellens namn och en etikett som anger att senaste version av modellen ska hämtas.

    - Det skriver ut ett meddelande till konsolen som anger namn, version och id för den modell som ska användas för finjustering. Format-metoden för strängen används för att infoga namn, version och id från modellen i meddelandet. Namn, version och id hämtas som egenskaper av foundation_model objektet.

    ```python
    # Ange modellnamnet
    model_name = "Phi-3-mini-4k-instruct"
    
    # Hämta den senaste versionen av modellen från Azure ML-registret
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Skriv ut modellnamnet, versionen och id
    # Denna information är användbar för spårning och felsökning
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Skapa en compute som ska användas för jobbet

Finjusteringsjobbet fungerar ENDAST med GPU compute. Compute-storleken beror på hur stor modellen är och i de flesta fall kan det vara svårt att identifiera rätt compute för jobbet. I denna cell vägleder vi användaren att välja rätt compute för jobbet.

> [!NOTE]
> De compute som listas nedan fungerar med den mest optimerade konfigurationen. Eventuella ändringar i konfigurationen kan leda till Cuda Out Of Memory-fel. I sådana fall, försök uppgradera compute till en större storlek.

> [!NOTE]
> När du väljer compute_cluster_size nedan, se till att compute finns tillgänglig i din resursgrupp. Om en viss compute inte är tillgänglig kan du göra en begäran om att få tillgång till compute-resurserna.

### Kontrollera om modellen stödjer finjustering

1. Detta Python-skript interagerar med en Azure Machine Learning (Azure ML) modell. Här är en sammanfattning av vad det gör:

    - Det importerar modulen ast, som erbjuder funktioner för att bearbeta träd av Pythons abstrakta syntax.

    - Det kontrollerar om foundation_model objektet (som representerar en modell i Azure ML) har en tagg som heter finetune_compute_allow_list. Taggar i Azure ML är nyckel-värde-par du kan skapa och använda för att filtrera och sortera modeller.

    - Om finetune_compute_allow_list-taggen finns, använder det ast.literal_eval funktionen för att säkert tolka taggens värde (en sträng) till en Python-lista. Denna lista tilldelas variabeln computes_allow_list. Det skriver sedan ut ett meddelande som anger att en compute bör skapas från listan.

    - Om finetune_compute_allow_list-taggen inte finns, sätts computes_allow_list till None och ett meddelande skrivs ut om att finetune_compute_allow_list-taggen inte finns bland modellens taggar.

    - Sammanfattningsvis kontrollerar skriptet efter en specifik tagg i modellens metadata, konverterar taggens värde till en lista om den finns och ger feedback till användaren därefter.

    ```python
    # Importera ast-modulen, som tillhandahåller funktioner för att bearbeta träd av Pythons abstrakta syntaxgrammatik
    import ast
    
    # Kontrollera om taggen 'finetune_compute_allow_list' finns i modellens taggar
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Om taggen finns, använd ast.literal_eval för att säkert parsa taggens värde (en sträng) till en Python-lista
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # konvertera sträng till python-lista
        # Skriv ut ett meddelande som indikerar att en compute ska skapas från listan
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Om taggen inte finns, sätt computes_allow_list till None
        computes_allow_list = None
        # Skriv ut ett meddelande som indikerar att taggen 'finetune_compute_allow_list' inte ingår i modellens taggar
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Kontrollera Compute-instans

1. Detta Python-skript interagerar med Azure Machine Learning (Azure ML) tjänsten och utför flera kontroller på en compute-instans. Här är en sammanfattning av vad det gör:

    - Det försöker hämta compute-instansen med namnet som är lagrat i compute_cluster från Azure ML workspace. Om compute-instansens provisionsstatus är "failed" kastas ett ValueError.

    - Det kontrollerar om computes_allow_list inte är None. Om så är fallet, konverterar det alla compute-storlekar i listan till små bokstäver och kontrollerar om storleken på den aktuella compute-instansen finns i listan. Om inte, kastas ett ValueError.

    - Om computes_allow_list är None, kontrollerar det om storleken på compute-instansen finns i en lista över icke-stödda GPU VM-storlekar. Om den finns, kastas ett ValueError.

    - Det hämtar en lista över alla tillgängliga compute-storlekar i workspace. Sedan itererar den över denna lista och för varje compute-storlek kontrollerar den om dess namn matchar storleken på den aktuella compute-instansen. Om så är fallet, hämtar den antalet GPU:er för den compute-storleken och sätter gpu_count_found till True.

    - Om gpu_count_found är True, skrivs antalet GPU:er i compute-instansen ut. Om gpu_count_found är False, kastas ett ValueError.

    - Sammanfattningsvis utför detta skript flera kontroller på en compute-instans i en Azure ML workspace, bland annat kontroll av provisionsstatus, storlek mot tillåten lista eller nekat lista, samt antal GPU:er.

    ```python
    # Skriv ut undantagsmeddelandet
    print(e)
    # Kasta ett ValueError om beräkningsstorleken inte finns tillgänglig i arbetsytan
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Hämta beräkningsinstansen från Azure ML-arbetsytan
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Kontrollera om provisioneringstillståndet för beräkningsinstansen är "failed"
    if compute.provisioning_state.lower() == "failed":
        # Kasta ett ValueError om provisioneringstillståndet är "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Kontrollera om computes_allow_list inte är None
    if computes_allow_list is not None:
        # Konvertera alla beräkningsstorlekar i computes_allow_list till gemener
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Kontrollera om storleken på beräkningsinstansen finns i computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Kasta ett ValueError om storleken på beräkningsinstansen inte finns i computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Definiera en lista över icke-stödda GPU VM-storlekar
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Kontrollera om storleken på beräkningsinstansen finns i unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Kasta ett ValueError om storleken på beräkningsinstansen finns i unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initiera en flagga för att kontrollera om antalet GPU:er i beräkningsinstansen har hittats
    gpu_count_found = False
    # Hämta en lista över alla tillgängliga beräkningsstorlekar i arbetsytan
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterera över listan med tillgängliga beräkningsstorlekar
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Kontrollera om namnet på beräkningsstorleken matchar storleken på beräkningsinstansen
        if compute_sku.name.lower() == compute.size.lower():
            # Om så är fallet, hämta antalet GPU:er för den beräkningsstorleken och sätt gpu_count_found till True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Om gpu_count_found är True, skriv ut antalet GPU:er i beräkningsinstansen
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Om gpu_count_found är False, kasta ett ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Välj dataset för att finjustera modellen

1. Vi använder ultrachat_200k dataset. Datasetet har fyra delar, lämpliga för Supervised fine-tuning (sft).
Generationsrankning (gen). Antal exempel per del visas enligt följande:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. De närmaste cellerna visar grundläggande datapreparation för finjustering:

### Visualisera några datarader

Vi vill att detta exempel ska gå snabbt, så spara train_sft och test_sft filer som innehåller 5% av de redan beskurna raderna. Detta innebär att den finjusterade modellen kommer att ha lägre noggrannhet, så den bör inte användas i verkliga tillämpningar.
download-dataset.py används för att ladda ner ultrachat_200k dataset och transformera datasetet till ett format som kan användas av finjusterings-pipelinekomponent. Eftersom datasetet är stort, har vi här bara en del av datasetet.

1. Att köra nedanstående skript laddar endast ner 5% av datat. Detta kan ökas genom att ändra dataset_split_pc-parametern till önskad procentandel.

> [!NOTE]
> Vissa språkmodeller har olika språk-koder och därför bör kolumnnamnen i datasetet reflektera detta.

1. Här är ett exempel på hur datat bör se ut
Chat-kompletteringsdatasetet lagras i parquet-format där varje post använder följande schema:

    - Detta är ett JSON (JavaScript Object Notation) dokument, som är ett populärt format för datautbyte. Det är inte körbar kod utan ett sätt att lagra och transportera data. Här är en översikt av dess struktur:

    - "prompt": Denna nyckel innehåller en sträng som representerar en uppgift eller fråga till en AI-assistent.

    - "messages": Denna nyckel innehåller en array av objekt. Varje objekt representerar ett meddelande i en konversation mellan en användare och en AI-assistent. Varje meddelandeobjekt har två nycklar:

    - "content": Denna nyckel innehåller en sträng som representerar innehållet i meddelandet.
    - "role": Denna nyckel innehåller en sträng som representerar rollen för den som skickade meddelandet. Det kan vara antingen "user" eller "assistant".
    - "prompt_id": Denna nyckel innehåller en sträng som representerar ett unikt ID för prompten.

1. I detta specifika JSON-dokument representeras en konversation där en användare ber en AI-assistent att skapa en protagonist för en dystopisk berättelse. Assistenten svarar, och användaren ber sedan om fler detaljer. Assistenten går med på att ge fler detaljer. Hela konversationen är kopplad till ett specifikt prompt-id.

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

### Ladda ner data

1. Detta Python-skript används för att ladda ner ett dataset med hjälp av ett hjälpskript som heter download-dataset.py. Här är en sammanfattning av vad det gör:

    - Det importerar modulen os, som ger ett portabelt sätt att använda operativsystemets funktionalitet.

    - Det använder os.system funktionen för att köra skriptet download-dataset.py i skalet med specifika kommandoradsargument. Argumenten anger dataset att ladda ner (HuggingFaceH4/ultrachat_200k), katalogen att ladda ner till (ultrachat_200k_dataset), och procentandelen av datasetet som ska delas (5). os.system funktionen returnerar utgångskoden av kommandot; denna lagras i variabeln exit_status.

    - Det kontrollerar om exit_status inte är 0. I Unix-liknande system indikerar en exitstatus på 0 normalt att ett kommando har lyckats, medan andra siffror indikerar ett fel. Om exit_status inte är 0, kastar det ett Exception med ett meddelande om att det uppstod ett fel vid nedladdning av dataset.

    - Sammanfattningsvis kör detta skript ett kommando för att ladda ner ett dataset med ett hjälpskript, och kastar ett undantag om kommandot misslyckas.

    ```python
    # Importera os-modulen, som tillhandahåller ett sätt att använda operativsystemberoende funktionalitet
    import os
    
    # Använd os.system-funktionen för att köra skriptet download-dataset.py i skalet med specifika kommandoradsargument
    # Argumenten specificerar datasetet som ska laddas ner (HuggingFaceH4/ultrachat_200k), katalogen att ladda ner till (ultrachat_200k_dataset) och procentsatsen av datasetet att dela (5)
    # os.system-funktionen returnerar utgångsstatus för kommandot den körde; denna status lagras i variabeln exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Kontrollera om exit_status inte är 0
    # I Unix-liknande operativsystem indikerar en utgångsstatus på 0 vanligtvis att ett kommando har lyckats, medan vilket annat nummer som helst indikerar ett fel
    # Om exit_status inte är 0, kasta ett undantag med ett meddelande som indikerar att det var ett fel vid nedladdning av datasetet
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Ladda data i en DataFrame
1. Detta Python-skript laddar en JSON Lines-fil till en pandas DataFrame och visar de första 5 raderna. Här är en sammanfattning av vad det gör:

    - Det importerar pandas-biblioteket, som är ett kraftfullt bibliotek för datamanipulation och analys.

    - Det sätter maximal kolumnbredd för pandas visningsalternativ till 0. Detta innebär att hela texten i varje kolumn visas utan trunkering när DataFrame skrivs ut.

    - Det använder funktionen pd.read_json för att ladda filen train_sft.jsonl från katalogen ultrachat_200k_dataset till en DataFrame. Argumentet lines=True anger att filen är i JSON Lines-format, där varje rad är ett separat JSON-objekt.

    - Det använder metoden head för att visa de första 5 raderna i DataFrame. Om DataFrame har färre än 5 rader visas alla rader.

    - Sammanfattningsvis laddar detta skript en JSON Lines-fil till en DataFrame och visar de första 5 raderna med full kolumntext.
    
    ```python
    # Importera pandas-biblioteket, som är ett kraftfullt bibliotek för datahantering och analys
    import pandas as pd
    
    # Sätt den maximala kolumnbredden för pandas visningsalternativ till 0
    # Detta betyder att hela texten i varje kolumn kommer att visas utan förkortning när DataFrame skrivs ut
    pd.set_option("display.max_colwidth", 0)
    
    # Använd pd.read_json-funktionen för att ladda filen train_sft.jsonl från katalogen ultrachat_200k_dataset till en DataFrame
    # Argumentet lines=True indikerar att filen är i JSON Lines-format, där varje rad är ett separat JSON-objekt
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Använd metoden head för att visa de första 5 raderna i DataFrame
    # Om DataFrame har färre än 5 rader kommer alla att visas
    df.head()
    ```

## 5. Skicka in finjusteringsjobbet med modellen och data som insats

Skapa jobbet som använder chat-completion pipeline-komponenten. Läs mer om alla parametrar som stöds för finjustering.

### Definiera finjusteringsparametrar

1. Finjusteringsparametrar kan delas in i 2 kategorier – träningsparametrar, optimeringsparametrar

1. Träningsparametrar definierar träningsaspekter såsom -

    - Vilken optimerare, scheduler som ska användas
    - Metriken som ska optimeras under finjusteringen
    - Antal träningssteg och batchstorlek med mera
    - Optimeringsparametrar hjälper till att optimera GPU-minnet och effektivt använda beräkningsresurserna.

1. Nedan är några av parametrarna som hör till denna kategori. Optimeringsparametrarna skiljer sig mellan olika modeller och paketeras med modellen för att hantera dessa variationer.

    - Aktivera deepspeed och LoRA
    - Aktivera mixed precision training
    - Aktivera multi-node training

> [!NOTE]
> Övervakad finjustering kan leda till förlorad anpassning eller katastrofglömska. Vi rekommenderar att kontrollera detta problem och köra en anpassningsfas efter att du finjusterat.

### Finjusteringsparametrar

1. Detta Python-skript ställer in parametrar för finjustering av en maskininlärningsmodell. Här är en sammanfattning av vad det gör:

    - Det ställer in standard träningsparametrar som antal träningsepoker, batchstorlekar för träning och utvärdering, inlärningshastighet och typ av inlärningshastighetsschemaläggare.

    - Det ställer in standard optimeringsparametrar som om Layer-wise Relevance Propagation (LoRa) och DeepSpeed ska tillämpas, samt DeepSpeed-stadiet.

    - Det kombinerar tränings- och optimeringsparametrar i en enda ordbok som kallas finetune_parameters.

    - Det kontrollerar om foundation_model har några modell-specifika standardparametrar. Om så är fallet, skrivs ett varningsmeddelande ut och finetune_parameters-ordboken uppdateras med dessa modell-specifika standardvärden. Funktionen ast.literal_eval används för att konvertera modell-specifika standardvärden från en sträng till en Python-ordbok.

    - Det skriver ut den slutgiltiga uppsättningen finjusteringsparametrar som kommer att användas för körningen.

    - Sammanfattningsvis ställer detta skript in och visar parametrarna för finjustering av en maskininlärningsmodell, med möjlighet att skriva över standardparametrarna med modell-specifika sådana.

    ```python
    # Ställ in standard träningsparametrar såsom antal tränings-epoker, batchstorlekar för träning och utvärdering, inlärningshastighet och typ av inlärningshastighets-schemaläggare
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Ställ in standard optimeringsparametrar såsom om Layer-wise Relevance Propagation (LoRa) och DeepSpeed ska användas, samt DeepSpeed-steget
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Kombinera tränings- och optimeringsparametrar till en enda ordbok som kallas finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Kontrollera om foundation_model har några modell-specifika standardparametrar
    # Om den har det, skriv ut ett varningsmeddelande och uppdatera ordboken finetune_parameters med dessa modell-specifika standardvärden
    # Funktionen ast.literal_eval används för att konvertera de modell-specifika standardvärdena från en sträng till en Python-ordbok
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # konvertera sträng till python-ordbok
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Skriv ut den slutgiltiga uppsättningen av finjusteringsparametrar som kommer att användas för körningen
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Träningspipeline

1. Detta Python-skript definierar en funktion för att generera ett visningsnamn för en maskininlärnings-träningspipeline, och anropar sedan denna funktion för att generera och skriva ut visningsnamnet. Här är en sammanfattning av vad det gör:

1. Funktionen get_pipeline_display_name definieras. Denna funktion genererar ett visningsnamn baserat på olika parametrar relaterade till träningspipen.

1. Inuti funktionen beräknas den totala batchstorleken genom att multiplicera batchstorleken per enhet, antalet gradientuppsamlingssteg, antalet GPU:er per nod samt antalet noder som används för finjustering.

1. Den hämtar flera andra parametrar såsom typ av inlärningshastighetsschemaläggare, om DeepSpeed används, DeepSpeed-stadiet, om Layer-wise Relevance Propagation (LoRa) används, begränsningen för antal modeller att behålla, och maximal sekvenslängd.

1. Den bygger en sträng som inkluderar alla dessa parametrar, separerade med bindestreck. Om DeepSpeed eller LoRa används, inkluderas "ds" följt av DeepSpeed-stadiet, eller "lora", respektive. Om inte, inkluderas "nods" eller "nolora", respektive.

1. Funktionen returnerar denna sträng, som fungerar som visningsnamnet för träningspipen.

1. Efter att funktionen definierats anropas den för att generera visningsnamnet, som sedan skrivs ut.

1. Sammanfattningsvis genererar detta skript ett visningsnamn för en maskininlärnings-träningspipeline baserat på olika parametrar och skriver sedan ut detta visningsnamn.

    ```python
    # Definiera en funktion för att generera ett visningsnamn för träningspipen
    def get_pipeline_display_name():
        # Beräkna total batchstorlek genom att multiplicera batchstorleken per enhet, antalet gradientackumuleringssteg, antalet GPU:er per nod och antal noder som används för finjustering
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Hämta typen av inlärningshastighetsschemaläggare
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Hämta om DeepSpeed används
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Hämta DeepSpeed-stadiet
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Om DeepSpeed används, inkludera "ds" följt av DeepSpeed-stadiet i visningsnamnet; annars inkludera "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Hämta om Layer-wise Relevance Propagation (LoRa) används
        lora = finetune_parameters.get("apply_lora", "false")
        # Om LoRa används, inkludera "lora" i visningsnamnet; annars inkludera "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Hämta begränsningen för antal modellkontrollpunkter att behålla
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Hämta maximal sekvenslängd
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Konstruera visningsnamnet genom att sammanfoga alla dessa parametrar, separerade med bindestreck
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
    
    # Anropa funktionen för att generera visningsnamnet
    pipeline_display_name = get_pipeline_display_name()
    # Skriv ut visningsnamnet
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Konfigurera pipeline

Detta Python-skript definierar och konfigurerar en maskininlärningspipeline med hjälp av Azure Machine Learning SDK. Här är en sammanfattning av vad det gör:

1. Det importerar nödvändiga moduler från Azure AI ML SDK.

1. Det hämtar en pipeline-komponent som heter "chat_completion_pipeline" från registret.

1. Det definierar ett pipelinejobb med hjälp av `@pipeline`-dekoreraren och funktionen `create_pipeline`. Namnet på pipelinen sätts till `pipeline_display_name`.

1. Inuti funktionen `create_pipeline` initialiseras den hämtade pipeline-komponenten med olika parametrar, inklusive sökväg till modellen, beräkningskluster för olika steg, datasetuppdelningar för träning och testning, antal GPU:er att använda för finjustering, och andra finjusteringsparametrar.

1. Det kopplar utdata från finjusteringsjobbet till utdata från pipelinejobbet. Detta görs för att den finjusterade modellen enkelt ska kunna registreras, vilket krävs för att distribuera modellen till en online- eller batch-endpoint.

1. Det skapar en instans av pipelinen genom att anropa funktionen `create_pipeline`.

1. Det sätter inställningen `force_rerun` för pipelinen till `True`, vilket betyder att cachade resultat från tidigare jobb inte kommer att användas.

1. Det sätter inställningen `continue_on_step_failure` på pipelinen till `False`, vilket betyder att pipelinen kommer att stoppas om något steg misslyckas.

1. Sammanfattningsvis definierar och konfigurerar detta skript en maskininlärningspipeline för en chattfärdigställandeuppgift med Azure Machine Learning SDK.

    ```python
    # Importera nödvändiga moduler från Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Hämta pipeline-komponenten med namnet "chat_completion_pipeline" från registret
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Definiera pipeline-jobbet med @pipeline-dekoratorn och funktionen create_pipeline
    # Namnet på pipeline är satt till pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initiera den hämtade pipeline-komponenten med olika parametrar
        # Dessa inkluderar modellvägen, beräkningskluster för olika steg, dataset-delningar för träning och testning, antalet GPU:er att använda för finjustering, och andra finjusteringsparametrar
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Karta dataset-delningarna till parametrar
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Inställningar för träning
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Sätt till antalet tillgängliga GPU:er i beräkningen
            **finetune_parameters
        )
        return {
            # Karta utdata från finjusteringsjobbet till utdatan för pipeline-jobbet
            # Detta görs så att vi enkelt kan registrera den finjusterade modellen
            # Att registrera modellen krävs för att distribuera modellen till en online- eller batch-endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Skapa en instans av pipelinen genom att kalla på create_pipeline-funktionen
    pipeline_object = create_pipeline()
    
    # Använd inte cachade resultat från tidigare jobb
    pipeline_object.settings.force_rerun = True
    
    # Sätt continue on step failure till False
    # Detta betyder att pipelinen stoppar om något steg misslyckas
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Skicka in jobbet

1. Detta Python-skript skickar in ett maskininlärningspipelinejobb till ett Azure Machine Learning-arbetsytan och väntar sedan på att jobbet ska slutföras. Här är en sammanfattning av vad det gör:

    - Det anropar metoden create_or_update på jobs-objektet i workspace_ml_client för att skicka in pipelinejobbet. Den pipeline som ska köras specificeras av pipeline_object, och experimentet under vilket jobbet körs specificeras av experiment_name.

    - Det anropar sedan metoden stream på jobs-objektet i workspace_ml_client för att vänta på att pipelinejobbet ska slutföras. Jobbet det väntar på specificeras av namn-attributet i pipeline_job-objektet.

    - Sammanfattningsvis skickar detta skript in ett maskininlärningspipelinejobb till en Azure Machine Learning-arbetsyta och väntar sedan på att jobbet ska slutföras.

    ```python
    # Skicka pipelinejobbet till Azure Machine Learning-arbetsytan
    # Pipelinjen som ska köras anges av pipeline_object
    # Experimentet under vilket jobbet körs anges av experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Vänta på att pipelinejobbet ska slutföras
    # Jobbet som ska vänta på anges av namn-attributet i pipeline_job-objektet
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Registrera den finjusterade modellen i arbetsytan

Vi kommer att registrera modellen från utdata av finjusteringsjobbet. Detta spårar härstamning mellan den finjusterade modellen och finjusteringsjobbet. Finjusteringsjobbet spårar vidare härstamning till grundmodellen, data och träningskod.

### Registrera ML-modellen

1. Detta Python-skript registrerar en maskininlärningsmodell som tränats i en Azure Machine Learning-pipeline. Här är en sammanfattning av vad det gör:

    - Det importerar nödvändiga moduler från Azure AI ML SDK.

    - Det kontrollerar om utdata "trained_model" finns tillgängligt från pipelinejobbet genom att anropa metoden get på jobs-objektet i workspace_ml_client och få tillgång till dess outputs-attribut.

    - Det konstruerar en sökväg till den tränade modellen genom att formatera en sträng med namnet på pipelinejobbet och namnet på utdata ("trained_model").

    - Det definierar ett namn för den finjusterade modellen genom att lägga till "-ultrachat-200k" till det ursprungliga modellnamnet och ersätta alla snedstreck med bindestreck.

    - Det förbereder för att registrera modellen genom att skapa ett Model-objekt med olika parametrar, inklusive sökvägen till modellen, modellens typ (MLflow-modell), modellens namn och version samt en beskrivning av modellen.

    - Det registrerar modellen genom att anropa metoden create_or_update på models-objektet i workspace_ml_client med Model-objektet som argument.

    - Det skriver ut den registrerade modellen.

1. Sammanfattningsvis registrerar detta skript en maskininlärningsmodell som tränats i en Azure Machine Learning-pipeline.
    
    ```python
    # Importera nödvändiga moduler från Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Kontrollera om utdata `trained_model` är tillgängligt från pipeline-jobbet
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Konstruera en sökväg till den tränade modellen genom att formatera en sträng med namnet på pipeline-jobbet och namnet på utdata ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Definiera ett namn för den finjusterade modellen genom att lägga till "-ultrachat-200k" till det ursprungliga modellnamnet och ersätta eventuella snedstreck med bindestreck
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Förbered för att registrera modellen genom att skapa ett Model-objekt med olika parametrar
    # Dessa inkluderar sökvägen till modellen, typen av modellen (MLflow-modell), namnet och versionen på modellen samt en beskrivning av modellen
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Använd tidsstämpel som version för att undvika versionskonflikt
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Registrera modellen genom att anropa metoden create_or_update på models-objektet i workspace_ml_client med Model-objektet som argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Skriv ut den registrerade modellen
    print("registered model: \n", registered_model)
    ```

## 7. Distribuera den finjusterade modellen till en online-endpoint

Online-endpoints ger ett hållbart REST API som kan användas för att integrera med applikationer som behöver använda modellen.

### Hantera endpoint

1. Detta Python-skript skapar en hanterad online-endpoint i Azure Machine Learning för en registrerad modell. Här är en sammanfattning av vad det gör:

    - Det importerar nödvändiga moduler från Azure AI ML SDK.

    - Det definierar ett unikt namn för online-endpointen genom att lägga till en tidsstämpel till strängen "ultrachat-completion-".

    - Det förbereder sig för att skapa online-endpointen genom att skapa ett ManagedOnlineEndpoint-objekt med olika parametrar, inklusive endpoint-namnet, en beskrivning av endpointen och autentiseringsläget ("key").

    - Det skapar online-endpointen genom att anropa metoden begin_create_or_update på workspace_ml_client med ManagedOnlineEndpoint-objektet som argument. Det väntar sedan tills skapandeoperationen är klar genom att anropa metoden wait.

1. Sammanfattningsvis skapar detta skript en hanterad online-endpoint i Azure Machine Learning för en registrerad modell.

    ```python
    # Importera nödvändiga moduler från Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Definiera ett unikt namn för den online-endpointen genom att lägga till en tidsstämpel till strängen "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Förbered för att skapa den online-endpointen genom att skapa ett ManagedOnlineEndpoint-objekt med olika parametrar
    # Dessa inkluderar endpointens namn, en beskrivning av endpointen och autentiseringsläget ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Skapa den online-endpointen genom att anropa metoden begin_create_or_update från workspace_ml_client med ManagedOnlineEndpoint-objektet som argument
    # Vänta sedan på att skapelseoperationen ska slutföras genom att anropa metoden wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Här hittar du listan över SKU:er som stöds för distribution – [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Distribuera ML-modell

1. Detta Python-skript distribuerar en registrerad maskininlärningsmodell till en hanterad online-endpoint i Azure Machine Learning. Här är en sammanfattning av vad det gör:

    - Det importerar modulen ast, som tillhandahåller funktioner för att bearbeta Python:s abstrakta syntaxträd.

    - Det sätter instanstypen för distributionen till "Standard_NC6s_v3".

    - Det kontrollerar om taggen inference_compute_allow_list finns i grundmodellen. Om så är fallet konverteras taggens värde från en sträng till en Python-lista och tilldelas inference_computes_allow_list. Om inte sätts inference_computes_allow_list till None.

    - Det kontrollerar om den angivna instanstypen finns i tillåtna listan. Om den inte gör det, skriver det ut ett meddelande där användaren ombeds välja en instanstyp från tillåten lista.

    - Det förbereder distributionen genom att skapa ett ManagedOnlineDeployment-objekt med olika parametrar, inklusive namnet på distributionen, endpointens namn, modellens ID, instanstyp och antal instanser, inställningar för liveness probe och förfrågningsinställningar.

    - Det skapar distributionen genom att anropa metoden begin_create_or_update på workspace_ml_client med ManagedOnlineDeployment-objektet som argument. Det väntar sedan tills skapandeoperationen är klar genom att anropa metoden wait.

    - Det sätter trafiken på endpointen till att dirigera 100 % av trafiken till "demo"-distributionen.

    - Det uppdaterar endpointen genom att anropa metoden begin_create_or_update på workspace_ml_client med endpoint-objektet som argument. Det väntar sedan tills uppdateringsoperationen är klar genom att anropa metoden result.

1. Sammanfattningsvis distribuerar detta skript en registrerad maskininlärningsmodell till en hanterad online-endpoint i Azure Machine Learning.

    ```python
    # Importera ast-modulen, som tillhandahåller funktioner för att bearbeta träd av Pythons abstrakta syntaxgrammatik
    import ast
    
    # Ange instanstypen för distributionen
    instance_type = "Standard_NC6s_v3"
    
    # Kontrollera om taggen `inference_compute_allow_list` finns i grundmodellen
    if "inference_compute_allow_list" in foundation_model.tags:
        # Om den finns, konvertera taggens värde från en sträng till en Python-lista och tilldela den till `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Om den inte finns, sätt `inference_computes_allow_list` till `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Kontrollera om den angivna instanstypen finns i tillåtelselistan
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Förbered för att skapa distributionen genom att skapa ett `ManagedOnlineDeployment`-objekt med olika parametrar
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Skapa distributionen genom att anropa metoden `begin_create_or_update` på `workspace_ml_client` med `ManagedOnlineDeployment`-objektet som argument
    # Vänta sedan på att skapandeoperationen ska slutföras genom att anropa metoden `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Ställ in trafiken för slutpunkten så att 100 % av trafiken går till "demo"-distributionen
    endpoint.traffic = {"demo": 100}
    
    # Uppdatera slutpunkten genom att anropa metoden `begin_create_or_update` på `workspace_ml_client` med `endpoint`-objektet som argument
    # Vänta sedan på att uppdateringsoperationen ska slutföras genom att anropa metoden `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Testa endpointen med provdata

Vi hämtar provdata från testdatasetet och skickar det till online-endpointen för inferens. Vi visar sedan de bedömda etiketterna tillsammans med de faktiska etiketterna.

### Läsa resultaten

1. Detta Python-skript läser en JSON Lines-fil till en pandas DataFrame, tar ett slumpmässigt prov och återställer indexet. Här är en sammanfattning av vad det gör:

    - Det läser filen ./ultrachat_200k_dataset/test_gen.jsonl till en pandas DataFrame. Funktionen read_json används med argumentet lines=True eftersom filen är i JSON Lines-format, där varje rad är ett separat JSON-objekt.

    - Det tar ett slumpmässigt prov på 1 rad från DataFrame. Funktionen sample används med argumentet n=1 för att specificera antal slumpmässiga rader som ska väljas.

    - Det återställer DataFrames index. Funktionen reset_index används med argumentet drop=True för att ta bort det ursprungliga indexet och ersätta det med ett nytt standardindex med heltalsvärden.

    - Det visar de första 2 raderna i DataFrame med funktionen head med argumentet 2. Eftersom DataFrame bara innehåller en rad efter provtagningen, visas dock endast den ena raden.

1. Sammanfattningsvis läser detta skript en JSON Lines-fil till en pandas DataFrame, tar ett slumpmässigt prov på 1 rad, återställer index och visar den första raden.
    
    ```python
    # Importera pandas-biblioteket
    import pandas as pd
    
    # Läs JSON Lines-filen './ultrachat_200k_dataset/test_gen.jsonl' till en pandas DataFrame
    # Argumentet 'lines=True' anger att filen är i JSON Lines-format, där varje rad är ett separat JSON-objekt
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Ta ett slumpmässigt urval på 1 rad från DataFrame
    # Argumentet 'n=1' specificerar antalet slumpmässiga rader att välja
    test_df = test_df.sample(n=1)
    
    # Nollställ indexet för DataFrame
    # Argumentet 'drop=True' anger att det ursprungliga indexet ska tas bort och ersättas med ett nytt index med standard heltalsvärden
    # Argumentet 'inplace=True' anger att DataFrame ska modifieras på plats (utan att skapa ett nytt objekt)
    test_df.reset_index(drop=True, inplace=True)
    
    # Visa de första 2 raderna i DataFrame
    # Eftersom DataFrame dock endast innehåller en rad efter urvalet, kommer detta endast att visa den raden
    test_df.head(2)
    ```

### Skapa JSON-objekt
1. Detta Python-skript skapar ett JSON-objekt med specifika parametrar och sparar det till en fil. Här är en genomgång av vad det gör:

    - Det importerar json-modulen, som tillhandahåller funktioner för att arbeta med JSON-data.

    - Det skapar en ordlista parameters med nycklar och värden som representerar parametrar för en maskininlärningsmodell. Nycklarna är "temperature", "top_p", "do_sample" och "max_new_tokens", och deras motsvarande värden är 0.6, 0.9, True och 200 respektive.

    - Det skapar en annan ordlista test_json med två nycklar: "input_data" och "params". Värdet av "input_data" är en annan ordlista med nycklarna "input_string" och "parameters". Värdet av "input_string" är en lista som innehåller det första meddelandet från DataFrame:en test_df. Värdet av "parameters" är parameters-ordlistan som skapades tidigare. Värdet av "params" är en tom ordlista.

    - Det öppnar en fil med namnet sample_score.json
    
    ```python
    # Importera json-modulen, som tillhandahåller funktioner för att arbeta med JSON-data
    import json
    
    # Skapa en ordbok `parameters` med nycklar och värden som representerar parametrar för en maskininlärningsmodell
    # Nycklarna är "temperature", "top_p", "do_sample" och "max_new_tokens", och deras motsvarande värden är 0.6, 0.9, True och 200 respektive
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Skapa en annan ordbok `test_json` med två nycklar: "input_data" och "params"
    # Värdet för "input_data" är en annan ordbok med nycklarna "input_string" och "parameters"
    # Värdet för "input_string" är en lista som innehåller det första meddelandet från `test_df` DataFrame
    # Värdet för "parameters" är den tidigare skapade ordboken `parameters`
    # Värdet för "params" är en tom ordbok
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Öppna en fil med namnet `sample_score.json` i katalogen `./ultrachat_200k_dataset` i skrivläge
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Skriv ordboken `test_json` till filen i JSON-format med hjälp av funktionen `json.dump`
        json.dump(test_json, f)
    ```

### Anropa endpoint

1. Detta Python-skript anropar en online-endpoint i Azure Machine Learning för att skatta en JSON-fil. Här är en genomgång av vad det gör:

    - Det anropar metoden invoke på online_endpoints-egenskapen hos workspace_ml_client-objektet. Denna metod används för att skicka en förfrågan till en online-endpoint och få ett svar.

    - Det specificerar namnet på endpointen och distributionen med argumenten endpoint_name och deployment_name. I detta fall är endpoint-namnet lagrat i variabeln online_endpoint_name och distributionsnamnet är "demo".

    - Det specificerar sökvägen till JSON-filen som ska skattas med argumentet request_file. I detta fall är filen ./ultrachat_200k_dataset/sample_score.json.

    - Det sparar svaret från endpointen i variabeln response.

    - Det skriver ut det råa svaret.

1. Sammanfattningsvis anropar detta skript en online-endpoint i Azure Machine Learning för att skatta en JSON-fil och skriver ut svaret.

    ```python
    # Anropa den online-endpointen i Azure Machine Learning för att skatta filen `sample_score.json`
    # Metoden `invoke` från egenskapen `online_endpoints` hos objektet `workspace_ml_client` används för att skicka en förfrågan till en online-endpoint och få ett svar
    # Argumentet `endpoint_name` specificerar namnet på endpointen, vilket lagras i variabeln `online_endpoint_name`
    # Argumentet `deployment_name` specificerar namnet på distributionen, vilket är "demo"
    # Argumentet `request_file` specificerar sökvägen till JSON-filen som ska skattas, vilket är `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Skriv ut det råa svaret från endpointen
    print("raw response: \n", response, "\n")
    ```

## 9. Radera online-endpointen

1. Glöm inte att ta bort online-endpointen, annars kommer du att lämna betalningsmätaren igång för den beräkning som används av endpointen. Denna Python-rad raderar en online-endpoint i Azure Machine Learning. Här är en genomgång av vad den gör:

    - Det anropar metoden begin_delete på online_endpoints-egenskapen hos workspace_ml_client-objektet. Denna metod används för att påbörja raderingen av en online-endpoint.

    - Det specificerar namnet på endpointen som ska raderas med argumentet name. I detta fall är endpoint-namnet lagrat i variabeln online_endpoint_name.

    - Det anropar metoden wait för att vänta på att raderingsoperationen ska slutföras. Detta är en blockerande operation, vilket innebär att den förhindrar att skriptet fortsätter förrän raderingen är klar.

    - Sammanfattningsvis startar denna kodrad raderingen av en online-endpoint i Azure Machine Learning och väntar på att operationen ska slutföras.

    ```python
    # Ta bort den online-endpointen i Azure Machine Learning
    # Metoden `begin_delete` för egenskapen `online_endpoints` hos objektet `workspace_ml_client` används för att starta borttagningen av en online-endpoint
    # Argumentet `name` specificerar namnet på endpointen som ska tas bort, vilket är lagrat i variabeln `online_endpoint_name`
    # Metoden `wait` anropas för att vänta på att borttagningsoperationen ska slutföras. Detta är en blockerande operation, vilket innebär att skriptet inte fortsätter förrän borttagningen är klar
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungsspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->