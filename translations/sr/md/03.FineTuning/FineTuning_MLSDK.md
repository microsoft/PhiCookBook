## Како користити компоненте за допуну ћаскања из регистра система Azure ML за фино подешавање модела

У овом примеру ћемо извршити фино подешавање модела Phi-3-mini-4k-instruct да би се завршио разговор између 2 особе користећи скуп података ultrachat_200k.

![MLFineTune](../../../../translated_images/sr/MLFineTune.928d4c6b3767dd35.webp)

Пример ће вам показати како да извршите фино подешавање користећи Azure ML SDK и Python, а затим како да распоредите фино подешени модел на онлајн крајњу тачку за предвиђање у реалном времену.

### Податке за обуку

Користићемо скуп података ultrachat_200k. Ово је јако филтрирана верзија UltraChat скупа података и коришћена је за обуку Zephyr-7B-β, савременог 7 милијарди параметара чата модела.

### Модел

Користићемо модел Phi-3-mini-4k-instruct да бисмо показали како корисник може да изврши фино подешавање модела за задатак допуне ћаскања. Ако сте отворили ову бележницу са странице специфичног модела, запамтите да замените специфично име модела.

### Задаци

- Изаберите модел за фино подешавање.
- Изаберите и истражите податке за обуку.
- Конфигуришите посао фино подешавања.
- Покрените посао фино подешавања.
- Прегледајте метрике обуке и евалуације.
- Региструјте фино подешени модел.
- Распоредите фино подешени модел за предвиђање у реалном времену.
- Очистите ресурсе.

## 1. Подесите предуслове

- Инсталирајте зависности
- Повежите се са AzureML радним простором. Сазнајте више на set up SDK authentication. Замените <WORKSPACE_NAME>, <RESOURCE_GROUP> и <SUBSCRIPTION_ID> доле.
- Повежите се са AzureML регистром система
- Поставите опционално име експеримента
- Проверите или креирајте израчун

> [!NOTE]
> Захтеви један GPU чвор може имати више GPU картица. На пример, у једном чвору Standard_NC24rs_v3 постоје 4 NVIDIA V100 GPU-а, док у Standard_NC12s_v3 има 2 NVIDIA V100 GPU-а. Погледајте документацију за ове информације. Број GPU картица по чвору подешава се у параметру gpus_per_node доле. Правилно подешавање ове вредности обезбедиће коришћење свих GPU-а у чвору. Препоручени GPU конфигурације можете пронаћи овде и овде.

### Python библиотеке

Инсталирајте зависности покретањем ћелије испод. Ово није опционални корак ако покрећете у новом окружењу.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Интеракција са Azure ML

1. Овај Python скрипт се користи за интеракцију са услугом Azure Machine Learning (Azure ML). Ево шта ради:

    - Увозе потребне модуле из пакета azure.ai.ml, azure.identity и azure.ai.ml.entities. Такође увози модул time.

    - Покушава да се аутентификује коришћењем DefaultAzureCredential(), што пружа поједностављено искуство аутентификације за брзо почетно развијање апликација у Azure облаку. Ако то не успе, пада на InteractiveBrowserCredential(), који пружа интерактивни логин упит.

    - Онда покушава да креира MLClient инстанцу користећи методу from_config, која чита конфигурацију из подразумеваног конфигурационог фајла (config.json). Ако то не успе, креира MLClient инстанцу ruчно прослеђујући subscription_id, resource_group_name и workspace_name.

    - Креира још једну MLClient инстанцу, овог пута за Azure ML регистар под називом "azureml". Овај регистар је место где се чувају модели, цевоводи за фино подешавање и окружења.

    - Поставља име експеримента на "chat_completion_Phi-3-mini-4k-instruct".

    - Генерише јединствени временски печат претварајући тренутно време (у секундама од почетка епохе, као број са покретним зарезом) у целобројну вредност, а затим у стринг. Овај временски печат може бити коришћен за креирање јединствених имена и верзија.

    ```python
    # Увоз неопходних модула из Azure ML и Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Увоз модула за време
    
    # Покушај аутентификације коришћењем DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Ако DefaultAzureCredential не успе, користи InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Покушај креирања MLClient инстанце коришћењем подразумеване конфигурационе датотеке
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Ако то не успе, креирај MLClient инстанцу ручним уносом детаља
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Креирај другу MLClient инстанцу за Azure ML регистар са именом "azureml"
    # Овај регистар је место где се чувају модели, пипелини за фино подешавање и окружења
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Постави име експеримента
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Генериши јединствени временски жиг који може да се користи за имена и верзије које морају бити јединствене
    timestamp = str(int(time.time()))
    ```

## 2. Изаберите основни модел за фино подешавање

1. Phi-3-mini-4k-instruct је модел са 3.8 милијарди параметара, лак и савремен отворени модел изграђен на скупу података коришћених за Phi-2. Модел припада Phi-3 породици модела, а Mini верзија долази у две варијанте 4K и 128K што је дужина контекста (у токенима) коју може да подржи, потребно је фино подешавање модела за нашу специфичну сврху како бисмо га користили. Можете прегледати ове моделе у Каталогу модела у AzureML Студију, филтрирајући по задатку допуне ћаскања. У овом примеру користимо модел Phi-3-mini-4k-instruct. Ако сте отворили ову бележницу за други модел, замените име модела и верзију у складу с тим.

> [!NOTE]
> id модела својства модела. Ово ће бити прослеђено као улаз у посао фино подешавања. Ово је такође доступно као поље Asset ID на страници детаља модела у AzureML Студију Каталогу модела.

2. Овај Python скрипт интерагује са услугом Azure Machine Learning (Azure ML). Ево шта ради:

    - Поставља модел_име на "Phi-3-mini-4k-instruct".

    - Користи get методу у својству models објекта registry_ml_client да преузме најновију верзију модела са заданим именом из Azure ML регистра. Метод get се позива са два аргумента: именом модела и ознаком која специфицира да треба преузети најновију верзију модела.

    - Исписује поруку на конзолу која показује име, верзију и ид модела који ће се користити за фино подешавање. Метод format стринга се користи да уметне име, верзију и ид модела у поруку. Име, верзија и ид модела се приступају као својства објекта foundation_model.

    ```python
    # Подеси име модела
    model_name = "Phi-3-mini-4k-instruct"
    
    # Узми најновију верзију модела из Azure ML регистра
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Испиши име модела, верзију и ид
    # Ове информације су корисне за праћење и отклањање грешака
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Креирајте израчун који ће се користити у послу

Посао фино подешавања ради САМО са GPU израчуном. Величина израчуна зависи од тога колико је модел велики и у већини случајева је тешко одредити прави израчун за посао. У овој ћелији водимо корисника да одабере прави израчун за посао.

> [!NOTE]
> Испод наведени израчуни раде са најоптимизованијом конфигурацијом. Било какве измене у конфигурацији могу довести до грешке Cuda Out Of Memory. У таквим случајевима, покушајте да надоградите израчун на већу величину.

> [!NOTE]
> При избору величине compute_cluster_size доле, уверите се да је израчун доступан у вашој resource групи. Ако одређени израчун није доступан, можете затражити приступ ресурсима израчуна.

### Провера подршке модела за фино подешавање

1. Овај Python скрипт интерагује са моделом Azure Machine Learning (Azure ML). Ево шта ради:

    - Увозе аст модул, који пружа функције за обраду стабала Python апстрактне синтаксне граматике.

    - Проверава да ли објекат foundation_model (који представља модел у Azure ML) има ознаку finetune_compute_allow_list. Ознаке у Azure ML су парови кључ-вредност које можете креирати и користити за филтрирање и сортирање модела.

    - Ако постоји ознака finetune_compute_allow_list, користи функцију ast.literal_eval да безбедно парсира вредност ознаке (стринг) у Python листу. Ова листа се затим додељује променљивој computes_allow_list. Затим исписује поруку која указује да треба креирати израчун са листе.

    - Ако ознака finetune_compute_allow_list није присутна, поставља computes_allow_list на None и исписује поруку да ознака finetune_compute_allow_list није део ознака модела.

    - Укратко, овај скрипт проверава постојање одређене ознаке у метаподацима модела, конвертује вредност ознаке у листу ако постоји и даје повратне информације кориснику.

    ```python
    # Увоз модула ast, који пружа функције за обраду стабала апстрактне синтаксе Питон граматике
    import ast
    
    # Проверите да ли је ознака 'finetune_compute_allow_list' присутна у ознакама модела
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Ако је ознака присутна, користите ast.literal_eval за безбедно парсирање вредности ознаке (низа) у Питон листу
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # конвертуј низ у питон листу
        # Испишите поруку која указује да треба креирати рачун из листе
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ако ознака није присутна, подесите computes_allow_list на None
        computes_allow_list = None
        # Испишите поруку која показује да ознака 'finetune_compute_allow_list' није део ознака модела
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Провера инстанце израчуна

1. Овај Python скрипт интерагује са услугом Azure Machine Learning (Azure ML) и извршава неколико провера на инстанци израчуна. Ево шта ради:

    - Пokušава да преузме инстанцу израчуна са именом које је сачувано у compute_cluster из Azure ML радног простора. Ако је стање провизије инстанце израчуна "failed", баца ValueError.

    - Проверава да ли је computes_allow_list различит од None. Ако јесте, конвертује све величине израчуна са листе у мала слова и проверава да ли је величина тренутне инстанце израчуна на листи. Ако није, баца ValueError.

    - Ако је computes_allow_list None, проверава да ли је величина инстанце израчуна на листи неподржаних величина GPU VM-а. Ако јесте, баца ValueError.

    - Преузима листу свих доступних величина израчуна у радном простору. Затим пролази кроз ову листу и за сваки тип израчуна проверава да ли се његово име поклапа са величином тренутне инстанце израчуна. Ако јесте, преузима број GPU-а за ту величину израчуна и подешава gpu_count_found на True.

    - Ако је gpu_count_found True, исписује број GPU-а у инстанци израчуна. Ако није, баца ValueError.

    - Укратко, овај скрипт извршава неколико провера на инстанци израчуна у Azure ML радном простору, укључујући проверу стања провизије, величине у односу на листу дозвољених или забрањених величина и броја GPU-а.

    ```python
    # Испиши поруку изузетка
    print(e)
    # Подигни ValueError ако величина израчунавања није доступна у радном простору
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Преузми инстанцу израчунавања из Azure ML радног простора
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Провери да ли је статус обезбеђивања инстанце израчунавања "failed"
    if compute.provisioning_state.lower() == "failed":
        # Подигни ValueError ако је статус обезбеђивања "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Провери да ли compute_allow_list није None
    if computes_allow_list is not None:
        # Конвертуј све величине израчунавања у compute_allow_list у мала слова
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Провери да ли се величина инстанце израчунавања налази у compute_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Подигни ValueError ако се величина инстанце израчунавања не налази у compute_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Дефиниши листу неподржаних GPU VM величина
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Провери да ли је величина инстанце израчунавања у unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Подигни ValueError ако је величина инстанце израчунавања у unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Иницијализуј флаг за проверу да ли је број GPU-а у инстанци израчунавања пронађен
    gpu_count_found = False
    # Преузми листу свих доступних величина израчунавања у радном простору
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Итерирај кроз листу доступних величина израчунавања
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Провери да ли име величине израчунавања одговара величини инстанце израчунавања
        if compute_sku.name.lower() == compute.size.lower():
            # Ако одговара, преузми број GPU-а за ту величину израчунавања и подеси gpu_count_found на True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Ако је gpu_count_found True, испиши број GPU-а у инстанци израчунавања
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Ако је gpu_count_found False, подигни ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Изаберите скуп података за фино подешавање модела

1. Користимо скуп података ultrachat_200k. Скуп података има четири поделе погодне за Супервизовану фино подешавање (sft).
Рангирање генерисања (gen). Број примера по подели је приказан како следи:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Следеће ћелије показују основну припрему података за фино подешавање:

### Визуелизујте неке редове података

Желимо да овај пример брзо ради, па сачувајте тренинг_fst, тест_fst фајлове који садрже 5% већ обрезаних редова. Ово значи да ће фино подешени модел имати мању тачност, те стога не би требало да се користи у стварном свету.
download-dataset.py се користи за преузимање скупа података ultrachat_200k и трансформацију скупа података у формат који компоненте фино подешавање цевовода могу да конзумирају. Такође, пошто је скуп података велики, овде имамо само део скупа.

1. Покретање скрипте испод преузима само 5% података. Ово се може повећати мењањем параметра dataset_split_pc на жељени проценат.

> [!NOTE]
> Неки језички модели имају различите језичке кодове и стога имена колона у скупу података треба да одражавају то.

1. Ево примера како подаци треба да изгледају
Скуп података за допуну ћаскања складишти се у parquet формату са сваким уносом користећи следећу шему:

    - Ово је JSON (JavaScript Object Notation) документ, који је популаран формат за размену података. Није извршни код, већ начин чувања и преноса података. Ево структуре:

    - "prompt": Ова кључ држи стринг вредност која представља задатак или питање постављено AI асистенту.

    - "messages": Овај кључ држи низ објеката. Сваки објекат представља поруку у разговору између корисника и AI асистента. Сваки објекат поруке има два кључа:

    - "content": Овај кључ држи стринг вредност која представља садржај поруке.
    - "role": Овај кључ држи стринг вредност која представља улогу ентитета који је послао поруку. Може бити "user" или "assistant".
    - "prompt_id": Овај кључ држи стринг вредност која представља јединствени идентификатор за упит.

1. У овом специфичном JSON документу, разговор је представљен где корисник тражи од AI асистента да створи протагониста за дистописку причу. Асистент одговара, а корисник потом тражи више детаља. Асистент се слаже да пружи више детаља. Цео разговор је повезан са специфичним prompt_id.

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

### Преузимање података

1. Овај Python скрипт се користи за преузимање скупа података користећи помоћни скрипт download-dataset.py. Ево шта ради:

    - Увозе модул os, који пружа преносив начин коришћења операцијског система.

    - Користи os.system функцију за покретање download-dataset.py скрипте у шкољци са одређеним аргументима командне линије. Аргументи спецификују скуп података који треба преузети (HuggingFaceH4/ultrachat_200k), директоријум за преузимање (ultrachat_200k_dataset) и проценат поделе скупа података (5). os.system враћа статус изласка команде коју је извршио; овај статус се чува у променљивој exit_status.

    - Проверава да ли exit_status није 0. У Unix-у, статус изласка 0 обично значи да је команда успела, док сваки други број указује на грешку. Ако exit_status није 0, баца изузетак са поруком да је дошло до грешке приликом преузимања скупа података.

    - Укратко, овај скрипт покреће команду за преузимање скупа података користећи помоћни скрипт и баца изузетак ако команда не успе.

    ```python
    # Импортујте os модул, који обезбеђује начин коришћења функционалности зависне од оперативног система
    import os
    
    # Користите функцију os.system да покренете скрипту download-dataset.py у шкољци са одређеним аргументима командне линије
    # Аргументи одређују скуп података који ће се преузети (HuggingFaceH4/ultrachat_200k), директоријум у који ће се преузети (ultrachat_200k_dataset), и проценат скупа података који ће се поделити (5)
    # Функција os.system враћа статус завршетка извршеног командног налога; овај статус се чува у променљивој exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Проверите да ли exit_status није 0
    # У Unix-подобним оперативним системима, статус завршетка 0 обично указује да је команда успешно извршена, док сваки други број означава грешку
    # Ако exit_status није 0, избаците изузетак са поруком која указује да је дошло до грешке приликом преузимања скупа података
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Учитавање података у DataFrame

1. Овај Python скрипт учитава JSON Lines фајл у pandas DataFrame и приказује првих 5 редова. Ево шта ради:

    - Увозе pandas библиотеку, која је моћна библиотека за манипулацију и анализу података.

    - Поставља максималну ширину колоне за pandas display опције на 0. Ово значи да ће се у потпуности приказати текст сваке колоне без скраћивања када се DataFrame испише.
    - Користи функцију pd.read_json да учита датотеку train_sft.jsonl из директоријума ultrachat_200k_dataset у DataFrame. Аргумент lines=True означава да је датотека у JSON Lines формату, где је сваки ред посебан JSON објекат.

    - Користи методу head да прикаже првих 5 редова DataFrame-а. Ако DataFrame има мање од 5 редова, приказаће све њих.

    - Укратко, овај скрипт учитава датотеку у формату JSON Lines у DataFrame и приказује првих 5 редова са потпуним текстом колона.
    
    ```python
    # Увези библиотеку pandas, која је моћна библиотека за манипулацију и анализу података
    import pandas as pd
    
    # Постави максималну ширину колоне за приказ у pandas на 0
    # Ово значи да ће цео текст сваке колоне бити приказан без скраћивања када се DataFrame испише
    pd.set_option("display.max_colwidth", 0)
    
    # Користи функцију pd.read_json да учиташ датотеку train_sft.jsonl из директоријума ultrachat_200k_dataset у DataFrame
    # Аргумент lines=True означава да је датотека у JSON Lines формату, где је свака линија посебан JSON објекат
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Користи метод head да прикажеш првих 5 редова DataFrame-а
    # Ако DataFrame има мање од 5 редова, приказаће све њих
    df.head()
    ```

## 5. Поднесите посао финамских подешавања користећи модел и податке као уносе

Креирајте посао који користи компоненту chat-completion pipeline. Сазнајте више о свим параметрима који се подржавају за финамско подешавање.

### Дефинисање параметара за финамско подешавање

1. Параметри финамског подешавања могу се груписати у 2 категорије - параметри тренинга, параметри оптимизације

1. Параметри тренинга дефинишу аспекте тренинга као што су -

    - Оптимизатор, scheduler који се користи
    - Метрика коју треба оптимизовати током финамског подешавања
    - Број корака тренинга, величина batch-a итд.
    - Параметри оптимизације помажу у оптимизацији GPU меморије и ефикасном коришћењу ресурса за рачунарство.

1. Испод су неки од параметара који припадају овој категорији. Параметри оптимизације се разликују за сваки модел и пакетирају се са моделом за обраду ових варијација.

    - Омогућавање deepspeed и LoRA
    - Омогућавање тренинга са мешовитом прецизношћу
    - Омогућавање мулти-нода тренинга

> [!NOTE]
> Надгледано финамско подешавање може довести до губитка усклађености или катастрофалног заборава. Препоручујемо проверу овог проблема и покретање фазе усклађивања након што завршите финамско подешавање.

### Параметри финамског подешавања

1. Овај Python скрипт поставља параметре за финамско подешавање модела машинског учења. Ево шта ради:

    - Поставља подразумеване параметре тренинга као што су број епоха тренинга, величина batch-а за тренинг и евалуацију, брзина учења (learning rate) и тип scheduler-a брзине учења.

    - Поставља подразумеване параметре оптимизације као што су да ли се примењује Layer-wise Relevance Propagation (LoRa) и DeepSpeed, као и DeepSpeed фаза.

    - Комбинује параметре тренинга и оптимизације у један речник који се зове finetune_parameters.

    - Проверава да ли foundation_model има неке подешавања специфична за модел. Ако има, исписује упозорење и ажурира речник finetune_parameters тим модел-специфичним подразумеваним вредностима. Функција ast.literal_eval се користи да конвертује ове вредности из стринга у Python речник.

    - Исписује коначан скуп параметара за финамско подешавање који ће се користити при покретању.

    - Укратко, овај скрипт подешава и приказује параметре за финамско подешавање модела машинског учења, са могућношћу замене подразумеваних параметара модел-специфичним.

    ```python
    # Подесите подразумеване параметре тренинга као што су број епоха тренинга, величине пакетa за тренинг и евалуацију, стопа учења и тип распореда стопе учења
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Подесите подразумеване параметре оптимизације као што су примена Лајер-вајз релевант пропагатион (LoRa) и DeepSpeed, и DeepSpeed стадијум
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Комбинујте параметре тренинга и оптимизације у један речник који се зове finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Проверите да ли foundation_model има неке подразумеване параметре специфичне за модел
    # Ако има, испишите упозорење и ажурирајте речник finetune_parameters са овим подразумеваним параметрима специфичним за модел
    # Функција ast.literal_eval се користи да се подразумевани параметри специфични за модел претворе из стринга у Python речник
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # претвори стринг у Python речник
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Испишите коначни сет параметара за фино подешавање који ће се користити за извршавање
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Trening Pipelinе

1. Овај Python скрипт дефинише функцију која генерише приказно име за pipeline тренинга машинског учења, а затим позива ту функцију да генерише и испише приказно име. Ево шта ради:

1. Дефинисана је функција get_pipeline_display_name. Ова функција генерише приказно име на основу различитих параметара везаних за pipeline тренинга.

1. Унутар функције, израчунава укупну величину batch-а множењем величине batch-а по уређају, броја корака акумулације градијента, броја GPU-а по чвору и броја чворова који се користе за финамско подешавање.

1. Преузима разне друге параметре као што су тип learning rate scheduler-а, да ли је применљен DeepSpeed, DeepSpeed фаза, да ли је применљен Layer-wise Relevance Propagation (LoRa), ограничење броја задржаних checkpoint-а модела и максимална дужина секвенце.

1. Конструише стринг који укључује све ове параметре, раздвојене цртицама. Ако је примењен DeepSpeed или LoRa, стринг садржи "ds" праћено DeepSpeed фазом, односно "lora". Ако није, укључује "nods" или "nolora".

1. Функција враћа овај стринг, који служи као приказно име pipeline-а за тренинг.

1. Након дефиниције функције, она се позива да генерише приказно име, које се онда исписује.

1. Укратко, овај скрипт генерише приказно име за pipeline тренинга машинског учења на основу разних параметара и потом исписује то име.

    ```python
    # Дефинишите функцију за генерисање имена за приказ за тренинг пипелине
    def get_pipeline_display_name():
        # Израчунати укупну величину пакета множењем величине по уређају, броја корака акумулације градијента, броја GPU-а по чвору и броја чворова који се користе за фајн тунинг
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Добијте тип планера учења
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Добијте да ли се користи DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Добијте DeepSpeed стадијум
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Ако се користи DeepSpeed, укључите "ds" праћен DeepSpeed стадијумом у име за приказ; ако није, укључите "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Добијте да ли се користи Layer-wise Relevance Propagation (LoRa)
        lora = finetune_parameters.get("apply_lora", "false")
        # Ако се користи LoRa, укључите "lora" у име за приказ; ако није, укључите "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Добијте ограничење броја сочива модела које треба сачувати
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Добијте максималну дужину секвенце
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Конструишите име за приказ повезујући све ове параметре, раздвојене цртицама
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
    
    # Позовите функцију за генерисање имена за приказ
    pipeline_display_name = get_pipeline_display_name()
    # Испечатите име за приказ
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Конфигурисање Pipeline-а

Овај Python скрипт дефинише и конфигурише pipeline машинског учења користећи Azure Machine Learning SDK. Ево шта ради:

1. Уноси потребне модуле из Azure AI ML SDK.

1. Преузима pipeline компоненту под именом "chat_completion_pipeline" из регистрија.

1. Дефинише pipeline job користећи `@pipeline` декоратор и функцију `create_pipeline`. Име pipeline-а је подешено на `pipeline_display_name`.

1. Унутар функције `create_pipeline`, иницијализује преузету pipeline компоненту са различитим параметрима, укључујући пут до модела, compute кластер за различите фазе, поделе скупа података за тренинг и тестирање, број GPU-а који се користи за финамско подешавање и друге параметре финамског подешавања.

1. Мапира излаз финамског посла на излаз pipeline job-а. Ово је учињено како би се финамски подешени модел лако регистровао, што је потребно за деплоја модели на онлине или batch endpoint.

1. Креира инстанцу pipeline-а позивом функције `create_pipeline`.

1. Поставља опцију `force_rerun` pipeline-а на `True`, што значи да се неће користити кеширани резултати претходних послова.

1. Поставља опцију `continue_on_step_failure` pipeline-а на `False`, што значи да ће pipeline прекинути извршавање ако неки корак не успе.

1. Укратко, овај скрипт дефинише и конфигурише pipeline машинског учења за задатак chat completion користећи Azure Machine Learning SDK.

    ```python
    # Увези потребне модуле из Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Преузми компоненту цевовода по имену "chat_completion_pipeline" из регистратуре
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Дефиниши посао цевовода користећи @pipeline декоратор и функцију create_pipeline
    # Име цевовода се поставља на pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Иницијализуј преузету компоненту цевовода са различитим параметрима
        # Ово укључује путању модела, кластерe за израчунавање за различите фазе, поделе скупова података за тренинг и тестирање, број GPU-а који се користи за фино подешавање, и друге параметре фино подешавања
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Картографиши поделе скупова података на параметре
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Подешавања тренинга
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Постављено на број доступних GPU-а у систему за израчунавање
            **finetune_parameters
        )
        return {
            # Картографиши излаз из фино подешавања на излаз посла цевовода
            # Ово се ради да бисмо лако регистровали фино подешени модел
            # Регистрација модела је потребна за имплементацију модела на онлајн или батцх крајњу тачку
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Креирај инстанцу цевовода позивањем функције create_pipeline
    pipeline_object = create_pipeline()
    
    # Не користи кеширане резултате из претходних послова
    pipeline_object.settings.force_rerun = True
    
    # Постави наставак при неуспеху корака на False
    # Ово значи да ће цевовод зауставити рад ако неки корак не успе
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Подношење посла

1. Овај Python скрипт подноси pipeline job машинског учења у Azure Machine Learning workspace и затим чека да се посао заврши. Ево шта ради:

    - Позива метод create_or_update објекта jobs у workspace_ml_client да поднесе pipeline job. Pipeline који ће се покренути је назначен са pipeline_object, а експеримент под којим се посао извршава је експеримент_name.

    - Затим позива метод stream објекта jobs у workspace_ml_client да сачека завршетак pipeline job-а. Посао за чекање је назначен преко атрибута name објекта pipeline_job.

    - Укратко, овај скрипт подноси pipeline job машинског учења у Azure Machine Learning workspace и чека да се посао заврши.

    ```python
    # Пошаљите посао линије за обраду у Azure Machine Learning радни простор
    # Линија за обраду која ће се извршити је одређена преко pipeline_object
    # Експеримент у оквиру којег се посао извршава је одређен са experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Сачекајте да посао линије за обраду заврши
    # Посао који треба сачекати је одређен атрибутом name објекта pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Региструјте финамски подешени модел у workspace-у

Регистроваћемо модел из излаза финамског посла. Ово ће пратити однос између финамског модела и посла финамског подешавања. Посао финамског подешавања даље прати однос са foundation моделом, подацима и кодом за тренинг.

### Регистрација ML модела

1. Овај Python скрипт региструје модел машинског учења који је обучен у Azure Machine Learning pipeline-у. Ево шта ради:

    - Уноси потребне модуле из Azure AI ML SDK.

    - Проверава да ли излаз trained_model постоји из pipeline посла позивајући метод get над објектом jobs у workspace_ml_client и приступајући његовом outputs атрибуту.

    - Конструише пут до обученог модела форматирањем стринга са именом pipeline посла и именом излаза ("trained_model").

    - Дефинише име за финамски подешени модел додајући "-ultrachat-200k" оригиналном имену модела и замењујући било које косе црте цртицама.

    - Припрема се за регистрацију модела креирањем Model објекта са разним параметрима, укључујући пут до модела, тип модела (MLflow model), име и верзију модела, и опис модела.

    - Региструје модел позивом create_or_update метода објекта models у workspace_ml_client са Model објектом као аргументом.

    - Исписује регистровани модел.

1. Укратко, овај скрипт региструје модел машинског учења који је обучен у Azure Machine Learning pipeline-у.
    
    ```python
    # Увоз неопходних модула из Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Проверите да ли је излаз `trained_model` доступан из pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Конструишите пут до обученог модела форматирањем стринга са именом pipeline job и именом излаза ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Дефинишите име за фино подешени модел додавањем "-ultrachat-200k" на оригинално име модела и заменом свих косих црта цртицама
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Припремите регистрацију модела креирањем Model објекта са различитим параметрима
    # Ово укључује пут до модела, тип модела (MLflow модел), име и верзију модела, и опис модела
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Користите временску ознаку као верзију да бисте избегли конфликт верзија
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Региструјте модел позивом create_or_update метода објекта models у workspace_ml_client са Model објектом као аргументом
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Штампајте регистровани модел
    print("registered model: \n", registered_model)
    ```

## 7. Деплојујте финамски подешени модел на онлајн endpoint

Онлајн endpoint-ови пружају трајни REST API који се може користити за интеграцију са апликацијама које треба да користе модел.

### Управљање Endpoint-ом

1. Овај Python скрипт креира managed онлајн endpoint у Azure Machine Learning за регистровани модел. Ево шта ради:

    - Уноси потребне модуле из Azure AI ML SDK.

    - Дефинише јединствено име за онлајн endpoint додавањем временског жига на стринг "ultrachat-completion-".

    - Припрема се за креирање онлајн endpoint-а креирањем ManagedOnlineEndpoint објекта са разним параметрима, укључујући име endpoint-а, опис endpoint-а и режим аутентикације ("key").

    - Креира онлајн endpoint позивањем begin_create_or_update метода workspace_ml_client са ManagedOnlineEndpoint објектом као аргументом и потом чека да операција креирања буде завршена позивањем wait метода.

1. Укратко, овај скрипт креира managed онлајн endpoint у Azure Machine Learning за регистровани модел.

    ```python
    # Увези неопходне модуле из Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Дефиниши јединствено име за онлајн ендпоинт додавањем временске ознаке на стринг "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Припреми стварање онлајн ендпоинта креирањем ManagedOnlineEndpoint објекта са разним параметрима
    # Ово укључује име ендпоинта, опис ендпоинта и режим аутентификације ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Креирај онлајн ендпоинт позивом begin_create_or_update методе workspace_ml_client-а са ManagedOnlineEndpoint објектом као аргументом
    # Затим сачекај да операција креирања буде завршена позивом wait методе
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Овде можете пронаћи листу SKU-ова који су подржани за деплојмент - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Деплојовање ML модела

1. Овај Python скрипт деплојује регистровани модел машинског учења на managed онлајн endpoint у Azure Machine Learning. Ево шта ради:

    - Уноси модул ast који пружа функције за обраду стабала опште синтаксе Python-а.

    - Поставља тип инстанце за деплојмент на "Standard_NC6s_v3".

    - Проверава да ли таг inference_compute_allow_list постоји у foundation моделу. Ако постоји, претвара вредност тага из стринга у Python листу и додељује је променљивој inference_computes_allow_list. Ако не постоји, поставља inference_computes_allow_list на None.

    - Проверава да ли је назначени тип инстанце у листи дозвољених. Ако није, исписује поруку која тражи од корисника да изабере тип инстанце из листе дозвољених.

    - Припрема се за креирање деплојмента креирањем ManagedOnlineDeployment објекта са разним параметрима, укључујући име деплојмента, име endpoint-а, ID модела, тип и број инстанци, подешавања probe-а за живост (liveness probe) и подешавања за захтеве.

    - Креира деплојмент позивом begin_create_or_update метода workspace_ml_client са ManagedOnlineDeployment објектом као аргументом и чека да креирање буде завршено позивањем wait метода.

    - Поставља саобраћај на endpoint-у тако да 100% саобраћаја иде ка "demo" деплојменту.

    - Ажурира endpoint позивом begin_create_or_update метода workspace_ml_client са објектом endpoint и чека да ажурирање буде завршено позивом result метода.

1. Укратко, овај скрипт деплојује регистровани модел машинског учења на managed онлајн endpoint у Azure Machine Learning.

    ```python
    # Увоз модула ast, који пружа функције за обраду стабала апстрактне синтаксне граматике Питхона
    import ast
    
    # Постави тип инстанце за распоређивање
    instance_type = "Standard_NC6s_v3"
    
    # Провери да ли је ознака `inference_compute_allow_list` присутна у основном моделу
    if "inference_compute_allow_list" in foundation_model.tags:
        # Ако јесте, претвори вредност ознаке из низа у Питхон листу и додели је у `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ако није, подеси `inference_computes_allow_list` на `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Провери да ли је наведени тип инстанце на листи дозвољених
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Припреми креирање распоређивања креирањем објекта `ManagedOnlineDeployment` са разним параметрима
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Креирај распоређивање позивањем методе `begin_create_or_update` клијента `workspace_ml_client` са објектом `ManagedOnlineDeployment` као аргументом
    # Потом сачекај да операција креирања буде завршена позивањем методе `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Постави саобраћај крајње тачке да усмери 100% саобраћаја на распоређивање "demo"
    endpoint.traffic = {"demo": 100}
    
    # Ажурирај крајњу тачку позивањем методе `begin_create_or_update` клијента `workspace_ml_client` са објектом `endpoint` као аргументом
    # Потом сачекај да операција ажурирања буде завршена позивањем методе `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Тестирајте endpoint са примером података

Преузећемо неке примерке података из test сета и послаћемо их онлајн endpoint-у за инференцу. Потом ћемо приказати оцене за класе уз оригиналне ознаке.

### Читање резултата

1. Овај Python скрипт учитава JSON Lines датотеку у pandas DataFrame, узима насумични узорак и ресетује индекс. Ево шта ради:

    - Учитава датотеку ./ultrachat_200k_dataset/test_gen.jsonl у pandas DataFrame. Функција read_json се користи са аргументом lines=True јер је датотека у JSON Lines формату, где је сваки ред посебан JSON објекат.

    - Узима насумични узорак од 1 реда из DataFrame-а. Функција sample се користи са аргументом n=1 да би се навео број насумичних редова за избор.

    - Ресетује индекс DataFrame-а. Функција reset_index се користи са аргументом drop=True да би се оригинални индекс одбацио и заменио новим индексом заснованим на подразумеваним целобројним вредностима.

    - Приказује прва 2 реда DataFrame-а користећи функцију head са аргументом 2. Међутим, пошто DataFrame садржи само један ред након узорковања, приказаће само тај један ред.

1. Укратко, овај скрипт учитава JSON Lines датотеку у pandas DataFrame, узима насумични узорак од 1 реда, ресетује индекс и приказује први ред.
    
    ```python
    # Увоз библиотеке pandas
    import pandas as pd
    
    # Учитај JSON Lines фајл './ultrachat_200k_dataset/test_gen.jsonl' у pandas DataFrame
    # Аргумент 'lines=True' означава да је фајл у JSON Lines формату, где је свака линија посебан JSON објекат
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Узми насумични узорак од 1 реда из DataFrame-а
    # Аргумент 'n=1' одређује број насумичних редова које треба изабрати
    test_df = test_df.sample(n=1)
    
    # Ресетуј индекс DataFrame-а
    # Аргумент 'drop=True' означава да треба избацити оригинални индекс и заменити га новим индексом са подразумеваним целобројним вредностима
    # Аргумент 'inplace=True' означава да DataFrame треба изменити на месту (без креирања новог објекта)
    test_df.reset_index(drop=True, inplace=True)
    
    # Прикажи прва 2 реда DataFrame-а
    # Међутим, пошто DataFrame садржи само један ред након узорковања, биће приказан само тај један ред
    test_df.head(2)
    ```

### Креирање JSON објекта

1. Овај Python скрипт креира JSON објекат са специфичним параметрима и чува га у датотеку. Ево шта ради:

    - Уноси json модул који пружа функције за рад са JSON подацима.
    - Креира речник parameters са кључевима и вредностима који представљају параметре за модел машинског учења. Кључеви су "temperature", "top_p", "do_sample" и "max_new_tokens", а њихове одговарајуће вредности су 0.6, 0.9, True и 200 респективно.

    - Креира други речник test_json са два кључа: "input_data" и "params". Вредност "input_data" је други речник са кључевима "input_string" и "parameters". Вредност "input_string" је листа која садржи прву поруку из DataFrame-a test_df. Вредност "parameters" је речник parameters који је раније креиран. Вредност "params" је празан речник.

    - Отвара датотеку под именом sample_score.json
    
    ```python
    # Увези json модул, који пружа функције за рад са JSON подацима
    import json
    
    # Направи речник `parameters` са кључевима и вредностима које представљају параметре за модел машинског учења
    # Кључеви су "temperature", "top_p", "do_sample" и "max_new_tokens", а њихове одговарајуће вредности су 0.6, 0.9, True и 200 редом
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Направи други речник `test_json` са два кључа: "input_data" и "params"
    # Вредност за "input_data" је други речник са кључевима "input_string" и "parameters"
    # Вредност за "input_string" је листа која садржи прву поруку из `test_df` DataFrame-а
    # Вредност за "parameters" је речник `parameters` направљен раније
    # Вредност за "params" је празан речник
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Отвори фајл под именом `sample_score.json` у фасцикли `./ultrachat_200k_dataset` у режиму писања
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Запиши речник `test_json` у фајл у JSON формату користећи функцију `json.dump`
        json.dump(test_json, f)
    ```

### Позивање Endpoint-а

1. Овај Python скрипт позива онлајн endpoint у Azure Machine Learning-у да оцени JSON датотеку. Ево шта ради:

    - Позива invoke методу својства online_endpoints објекта workspace_ml_client. Ова метода се користи за слање захтева онлајн endpoint-у и добијање одговора.

    - Наводи име endpoint-а и деплојмента са аргументима endpoint_name и deployment_name. У овом случају, име endpoint-а је смештено у променљиву online_endpoint_name а име деплојмента је "demo".

    - Наводи путању до JSON датотеке коју треба оценити са аргументом request_file. У овом случају, датотека је ./ultrachat_200k_dataset/sample_score.json.

    - Чува одговор од endpoint-а у променљиву response.

    - Штампа неисказани одговор.

1. Укратко, овај скрипт позива онлајн endpoint у Azure Machine Learning-у да оцени JSON датотеку и штампа одговор.

    ```python
    # Позовите онлајн крајњу тачку у Azure Machine Learning да бисте оцењивали `sample_score.json` фајл
    # Метод `invoke` својства `online_endpoints` објекта `workspace_ml_client` се користи за слање захтева онлајн крајњој тачки и добијање одговора
    # Аргумент `endpoint_name` одређује име крајње тачке, које је сачувано у променљивој `online_endpoint_name`
    # Аргумент `deployment_name` одређује име имплементације, које је "demo"
    # Аргумент `request_file` одређује путању до JSON фајла који треба оценити, која је `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Испишите необрађени одговор са крајње тачке
    print("raw response: \n", response, "\n")
    ```

## 9. Бришући онлајн endpoint

1. Не заборавите да обришете онлајн endpoint, иначе ћете оставити мерење наплате отвореним за рачунарске ресурсе које користи endpoint. Овај ред Python кода брише онлајн endpoint у Azure Machine Learning-у. Ево шта ради:

    - Позива begin_delete методу својства online_endpoints објекта workspace_ml_client. Ова метода се користи за покретање брисања онлајн endpoint-а.

    - Наводи име endpoint-а који треба обрисати аргументом name. У овом случају, име endpoint-а је смештено у променљиву online_endpoint_name.

    - Позива методу wait да сачека да брисање буде завршено. Ово је блокирајућа операција, што значи да ће спречити наставак скрипте док се брисање не заврши.

    - Укратко, овај ред кода покреће брисање онлајн endpoint-а у Azure Machine Learning-у и чека да операција буде завршена.

    ```python
    # Обришите онлајн крајњу тачку у Azure Machine Learning
    # Метода `begin_delete` својства `online_endpoints` објекта `workspace_ml_client` се користи за покретање брисања онлајн крајње тачке
    # Аргумент `name` одређује име крајње тачке која ће бити обрисана, а која је сачувана у променљивој `online_endpoint_name`
    # Позива се метода `wait` да се сачека завршетак операције брисања. Ово је блокирајућа операција, што значи да ће спречити скрипту да настави док брисање није завршено
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати званичним и коначним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било какве неспоразуме или погрешна тумачења која произлазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->