## Как да използваме компоненти за чат-завършване от регистъра на системата Azure ML за донастройка на модел

В този пример ще направим донастройка на модела Phi-3-mini-4k-instruct, за да завърши разговор между 2 души, използвайки набора от данни ultrachat_200k.

![MLFineTune](../../../../translated_images/bg/MLFineTune.928d4c6b3767dd35.webp)

Примерът ще ви покаже как да направите донастройка, използвайки Azure ML SDK и Python, а след това да деплойнете донастроения модел към онлайн крайна точка за извеждане на резултати в реално време.

### Данни за обучение

Ще използваме набора от данни ultrachat_200k. Това е силно филтрирана версия на набора UltraChat и беше използван за обучение на Zephyr-7B-β, съвременен чат модел с 7 милиарда параметъра.

### Модел

Ще използваме модела Phi-3-mini-4k-instruct, за да покажем как потребител може да донастрои модел за задача за чат-завършване. Ако сте отворили този тетрадка от конкретна карта на модел, не забравяйте да замените името на конкретния модел.

### Задачи

- Изберете модел за донастройка.
- Изберете и разгледайте данни за обучение.
- Конфигуриране на задачата за донастройка.
- Стартирайте задачата за донастройка.
- Прегледайте метрики за обучение и оценка.
- Регистрирайте донастроения модел.
- Деплойнете донастроения модел за извеждане на резултати в реално време.
- Почистете ресурсите.

## 1. Настройка на предварителните изисквания

- Инсталирайте зависимости
- Свържете се с AzureML работно пространство. Научете повече за настройване на удостоверяване на SDK. Заменете <WORKSPACE_NAME>, <RESOURCE_GROUP> и <SUBSCRIPTION_ID> по-долу.
- Свържете се с регистъра на системата azureml
- Задайте изборно име на експеримент
- Проверете или създайте изчислителен ресурс.

> [!NOTE]
> Изисквания: Един GPU възел може да има няколко GPU карти. Например, в един възел на Standard_NC24rs_v3 има 4 NVIDIA V100 GPU-та, а в Standard_NC12s_v3 има 2 NVIDIA V100 GPU-та. За тази информация се обърнете към документацията. Броят на GPU картите на възел е зададен в параметъра gpus_per_node по-долу. Коректното задаване на тази стойност ще осигури използването на всички GPU-та в възела. Препоръчаните GPU изчислителни SKU-та могат да се намерят тук и тук.

### Python библиотеки

Инсталирайте зависимостите чрез изпълнение на клетката по-долу. Това не е изборна стъпка, ако работите в нова среда.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Взаимодействие с Azure ML

1. Този Python скрипт се използва за взаимодействие с услугата Azure Machine Learning (Azure ML). Ето какво прави:

    - Импортира необходими модули от пакетите azure.ai.ml, azure.identity и azure.ai.ml.entities. Също така импортира модула time.

    - Опитва се да се удостовери чрез DefaultAzureCredential(), който осигурява опростен опит за удостоверяване, за да стартирате бързо разработка на приложения в облака Azure. Ако това се провали, преминава към InteractiveBrowserCredential(), която осигурява интерактивен прозорец за вписване.

    - След това се опитва да създаде инстанция MLClient с метода from_config, който чете конфигурацията от стандартния конфигурационен файл (config.json). Ако това не успее, създава MLClient, като ръчно предоставя subscription_id, resource_group_name и workspace_name.

    - Създава друга MLClient инстанция, този път за регистъра на Azure ML с име "azureml". Този регистър съхранява модели, pipeline-и за донастройка и среди.

    - Задава experiment_name като "chat_completion_Phi-3-mini-4k-instruct".

    - Генерира уникална времева отметка чрез преобразуване на текущото време (в секунди от епоха, като число с плаваща запетая) в цяло число и след това в низ. Тази отметка може да се използва за създаване на уникални имена и версии.

    ```python
    # Импортирайте необходими модули от Azure ML и Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Импортирайте модула time
    
    # Опитайте се да удостоверите с DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Ако DefaultAzureCredential неуспее, използвайте InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Опитайте се да създадете инстанция на MLClient, използвайки файла с конфигурация по подразбиране
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Ако това не успее, създайте инстанция на MLClient, като ръчно предоставите детайлите
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Създайте друг MLClient за регистъра Azure ML с име "azureml"
    # Този регистър е мястото, където се съхраняват модели, процеси за донастройка и среди
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Задайте името на експеримента
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Генерирайте уникален времеви отпечатък, който може да се използва за имена и версии, които трябва да са уникални
    timestamp = str(int(time.time()))
    ```

## 2. Изберете основен модел за донастройка

1. Phi-3-mini-4k-instruct е лек, с 3.8 милиарда параметъра, съвременен отворен модел, базиран на набори от данни, използвани за Phi-2. Моделът принадлежи към семейството модели Phi-3, а мини версията идва в два варианта — 4K и 128K, което е дължината на контекста (в токени), който може да поддържа. Необходимо е да донастроим модела за специфичната ни цел, за да го използваме. Можете да разгледате тези модели в Каталога на Модели в AzureML Studio, филтрирайки по задача чат-завършване. В този пример използваме Phi-3-mini-4k-instruct модела. Ако сте отворили този тетрадка за друг модел, заменете името на модела и версията съответно.

> [!NOTE]
> идентификаторът на модела (model id) на модела. Той ще се подава като вход за задачата за донастройка. Също така е наличен като поле Asset ID в страницата с детайли за модела в Каталога на Модели в AzureML Studio.

2. Този Python скрипт взаимодейства с услугата Azure Machine Learning (Azure ML). Ето какво прави:

    - Задава model_name на "Phi-3-mini-4k-instruct".

    - Използва метода get на свойството models от обекта registry_ml_client, за да вземе последната версия на модела с даденото име от регистъра Azure ML. Методът get се извиква с два аргумента: името на модела и етикет, указващ, че трябва да се вземе последната версия.

    - Извежда съобщение в конзолата, което показва името, версията и идентификатора на модела, който ще бъде използван за донастройка. Методът format на низа се използва, за да се вмъкнат името, версията и идентификатора на модела в съобщението. Името, версията и идентификаторът се достъпват като свойства на обекта foundation_model.

    ```python
    # Задайте името на модела
    model_name = "Phi-3-mini-4k-instruct"
    
    # Вземете последната версия на модела от регистъра на Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Отпечатайте името на модела, версията и идентификатора
    # Тази информация е полезна за проследяване и отстраняване на грешки
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Създайте изчислителен ресурс за използване със задачата

Задачата за донастройка работи САМО с GPU изчислителен ресурс. Размерът на ресурса зависи от големината на модела и в повечето случаи е трудно да се определи правилният изчислителен ресурс за задачата. В тази клетка насочваме потребителя как да избере правилния изчислителен ресурс за задачата.

> [!NOTE]
> Посочените изчислителни ресурси по-долу работят с най-оптимизираната конфигурация. Всякакви промени в конфигурацията може да доведат до грешка Cuda Out Of Memory. В такива случаи опитайте да ъпгрейднете изчислителния ресурс до по-голям размер.

> [!NOTE]
> При избора на compute_cluster_size по-долу, уверете се, че изчислителният ресурс е наличен в ресурсната ви група. Ако даден изчислителен ресурс не е наличен, можете да поискате достъп до ресурсите.

### Проверка дали моделът поддържа донастройка

1. Този Python скрипт взаимодейства с Azure Machine Learning (Azure ML) модел. Ето какво прави:

    - Импортира модула ast, който предоставя функции за обработка на дървета в абстрактната синтактична граматика на Python.

    - Проверява дали обектът foundation_model (който представлява модел в Azure ML) има тегъл finetune_compute_allow_list. Таговете в Azure ML са двойки ключ-стойност, които можете да създавате и използвате за филтриране и сортиране на модели.

    - Ако тагът finetune_compute_allow_list присъства, използва ast.literal_eval, за да безопасно парсне стойността на тага (низ) в Python списък. Този списък след това се задава на променливата computes_allow_list. Изкарва съобщение, че трябва да се създаде compute от списъка.

    - Ако тагът finetune_compute_allow_list липсва, задава computes_allow_list на None и извежда съобщение, че този таг не е част от таговете на модела.

    - Накратко, този скрипт проверява съществуването на конкретен таг в метаданните на модела, конвертира стойността му в списък, ако съществува, и информира потребителя.

    ```python
    # Импортирайте модула ast, който предоставя функции за обработка на дървета от абстрактната синтактична граматика на Python
    import ast
    
    # Проверете дали маркерът 'finetune_compute_allow_list' е наличен в маркерите на модела
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Ако маркерът е наличен, използвайте ast.literal_eval за безопасно парсиране на стойността на маркера (низ) в Python списък
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # преобразуване от низ към Python списък
        # Изведете съобщение, указващо че трябва да се създаде изчисление от списъка
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ако маркерът не е наличен, задайте computes_allow_list на None
        computes_allow_list = None
        # Изведете съобщение, което показва, че маркерът 'finetune_compute_allow_list' не е част от маркерите на модела
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Проверка на изчислителния инстанс

1. Този Python скрипт взаимодейства със службата Azure Machine Learning (Azure ML) и извършва няколко проверки върху изчислителен инстанс. Ето какво прави:

    - Опитва се да извлече изчислителния инстанс с името, записано в compute_cluster, от работното пространство Azure ML. Ако provisioning състоянието на инстанса е "failed" (неуспешно), вдига ValueError.

    - Проверява дали computes_allow_list не е None. Ако не е, конвертира всички размери на compute в списъка на малки букви и проверява дали размерът на текущия compute е в списъка. Ако не е, вдига ValueError.

    - Ако computes_allow_list е None, проверява дали размерът на compute инстанса е в списък с неподдържани GPU VM размери. Ако е, вдига ValueError.

    - Взима списък с всички налични размери на compute в работното пространство. Преглежда този списък и за всеки compute размер проверява дали името съвпада с размера на текущия compute инстанс. Ако да, взема броя на GPU-та за този размер и задава gpu_count_found на True.

    - Ако gpu_count_found е True, отпечатва броя на GPU-тата в compute инстанса. Ако е False, вдига ValueError.

    - Обобщено, този скрипт извършва няколко проверки върху compute инстанс в Azure ML, включително състояние на provision, размер срещу allow списък или deny списък, и броя на GPU-тата му.

    ```python
    # Изведете съобщението за изключение
    print(e)
    # Повдигнете ValueError, ако размерът на изчислението не е наличен в работното пространство
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Вземете инстанцията за изчисление от Azure ML работното пространство
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Проверете дали състоянието на осигуряване на инстанцията за изчисление е "failed"
    if compute.provisioning_state.lower() == "failed":
        # Повдигнете ValueError, ако състоянието на осигуряване е "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Проверете дали computes_allow_list не е None
    if computes_allow_list is not None:
        # Преобразувайте всички размери изчисления в computes_allow_list в малки букви
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Проверете дали размерът на инстанцията за изчисление е в computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Повдигнете ValueError, ако размерът на инстанцията за изчисление не е в computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Дефинирайте списък с неподдържани GPU VM размери
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Проверете дали размерът на инстанцията за изчисление е в unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Повдигнете ValueError, ако размерът на инстанцията за изчисление е в unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Инициирайте флаг за проверка дали броят на GPU-тата в инстанцията за изчисление е намерен
    gpu_count_found = False
    # Вземете списък на всички налични размери изчисления в работното пространство
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Итерайте през списъка на наличните размери изчисления
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Проверете дали името на размера на изчислението съвпада с размера на инстанцията за изчисление
        if compute_sku.name.lower() == compute.size.lower():
            # Ако е така, вземете броя на GPU-тата за този размер изчисление и задайте gpu_count_found на True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Ако gpu_count_found е True, изведете броя на GPU-тата в инстанцията за изчисление
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Ако gpu_count_found е False, повдигнете ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Изберете набора от данни за донастройка на модела

1. Използваме набора ultrachat_200k. Този набор е разделен на четири части, подходящи за контролирано (Supervised) донастройване (sft).
Генериране на ранкиране (gen). Броят на примерите за всяка част е както следва:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Следващите няколко клетки показват основна подготовка на данните за донастройване:

### Визуализация на някои редове от данните

Искаме този пример да се изпълнява бързо, затова запазваме файловете train_sft, test_sft съдържащи 5% от вече предварително намалените редове. Това означава, че донастроеният модел ще има по-ниска точност, затова не бива да се използва в реална употреба.
download-dataset.py се използва за изтегляне на набора ultrachat_200k и преобразуване на набора в подходящ формат за компонент на донастройващ pipeline. Понеже наборът е голям, тук имаме само част от него.

1. Изпълнението на скрипта по-долу изтегля само 5% от данните. Това може да се увеличи чрез смяна на параметъра dataset_split_pc на желан процент.

> [!NOTE]
> Някои езикови модели имат различни езикови кодове, затова имената на колоните в набора трябва да отразяват това.

1. Ето пример как трябва да изглеждат данните
Наборът за чат-завършване е съхранен във формат parquet, като всяка входна точка използва следния формат:

    - Това е JSON (JavaScript Object Notation) документ, който е популярен формат за обмен на данни. Не е изпълним код, а начин за съхранение и пренасяне на данни. Ето структурата му:

    - "prompt": Този ключ държи низ, който представлява задача или въпрос, поставен на AI асистент.

    - "messages": Този ключ държи масив от обекти. Всеки обект представлява съобщение в разговор между потребител и AI асистент. Всеки обект съобщение има два ключа:

    - "content": Този ключ държи стойност от тип низ, съдържаща съдържанието на съобщението.
    - "role": Този ключ държи низ, който описва ролята на изпращача — "user" или "assistant".
    - "prompt_id": Този ключ държи низ, който представя уникален идентификатор за подадения промпт.

1. В този конкретен JSON документ е представен разговор, в който потребител иска от AI асистента да създаде протагонист за дистопична история. Асистентът отговаря, а след това потребителят иска повече подробности. Асистентът се съгласява да даде повече детайли. Целият разговор е свързан с конкретен идентификатор на промпта.

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

### Изтегляне на данни

1. Този Python скрипт служи за изтегляне на набор от данни чрез помощен скрипт download-dataset.py. Ето какво прави:

    - Импортира модула os, който предоставя портативен начин за използване на зависимости от операционната система.

    - Използва os.system, за да стартира скрипта download-dataset.py с конкретни аргументи в shell. Аргументите посочват кой набор да се изтегли (HuggingFaceH4/ultrachat_200k), директорията за изтегляне (ultrachat_200k_dataset) и процента на разделяне (5). os.system връща статус на изхода от командата, който се съхранява в променливата exit_status.

    - Проверява дали exit_status не е 0. В операционни системи, подобни на Unix, статус 0 означава успешна команда, всяко друго число - грешка. Ако не е 0, вдига Exception с описание за грешка при изтеглянето.

    - Обобщено, този скрипт изпълнява команда за изтегляне на набор от данни чрез помощен скрипт и вдига грешка при провал.

    ```python
    # Импортирайте модула os, който предоставя начин за използване на функционалности, зависещи от операционната система
    import os
    
    # Използвайте функцията os.system, за да стартирате скрипта download-dataset.py в шел с конкретни командни аргументи
    # Аргументите посочват набора от данни за изтегляне (HuggingFaceH4/ultrachat_200k), директорията, в която да бъде изтеглен (ultrachat_200k_dataset), и процента от набора, който да бъде разделен (5)
    # Функцията os.system връща статус на изхода на изпълнената команда; този статус се съхранява в променливата exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Проверете дали exit_status не е 0
    # В операционни системи, подобни на Unix, статус на изход 0 обикновено означава, че командата е изпълнена успешно, докато всяко друго число указва грешка
    # Ако exit_status не е 0, повдигнете Exception с съобщение, указващо, че е имало грешка при изтеглянето на набора от данни
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Зареждане на данни в DataFrame

1. Този Python скрипт зарежда JSON Lines файл в pandas DataFrame и показва първите 5 реда. Ето какво прави:

    - Импортира библиотеката pandas, мощна библиотека за манипулация и анализ на данни.

    - Задава максималната ширина на колоните в настройките за показване на pandas на 0. Това означава, че цялото съдържание на всяка колона ще се показва без съкращаване при отпечатване на DataFrame.
    - Използва функцията pd.read_json, за да зареди файла train_sft.jsonl от директорията ultrachat_200k_dataset в DataFrame. Аргументът lines=True показва, че файлът е във формат JSON Lines, където всеки ред е отделен JSON обект.

    - Използва метода head, за да покаже първите 5 реда от DataFrame. Ако DataFrame има по-малко от 5 реда, ще покаже всички тях.

    - Накратко, този скрипт зарежда JSON Lines файл в DataFrame и показва първите 5 реда с пълен текст за колоните.
    
    ```python
    # Импортирайте библиотеката pandas, която е мощна библиотека за манипулация и анализ на данни
    import pandas as pd
    
    # Задайте максималната ширина на колоните в настройките за показване на pandas на 0
    # Това означава, че пълният текст на всяка колона ще се показва без съкращаване, когато DataFrame се отпечатва
    pd.set_option("display.max_colwidth", 0)
    
    # Използвайте функцията pd.read_json, за да заредите файла train_sft.jsonl от директорията ultrachat_200k_dataset в DataFrame
    # Аргументът lines=True указва, че файлът е във формат JSON Lines, където всеки ред е отделен JSON обект
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Използвайте метода head, за да покажете първите 5 реда от DataFrame
    # Ако DataFrame има по-малко от 5 реда, ще се покажат всички тях
    df.head()
    ```

## 5. Подаване на задачата за фино настройване, използвайки модела и данните като входни параметри

Създайте задачата, която използва компонента pipeline за чат-завършване. Научете повече за всички параметри, поддържани за фино настройване.

### Определяне на параметрите за фино настройване

1. Параметрите за фино настройване могат да се групират в 2 категории - параметри за обучение, параметри за оптимизация

1. Параметрите за обучение дефинират аспектите на обучението, като -

    - Оптимизатора, графика за обучение, който трябва да се използва
    - Метриката, която да се оптимизира при фино настройване
    - Брой обучителни стъпки и размер на батча и др.
    - Параметрите за оптимизация помагат за оптимизиране на GPU паметта и ефективно използване на изчислителните ресурси.

1. По-долу са някои от параметрите, които принадлежат към тази категория. Параметрите за оптимизация се различават за всеки модел и са пакетирани с модела, за да се обработят тези вариации.

    - Активирайте deepspeed и LoRA
    - Активирайте обучение с смесена точност
    - Активирайте многоузлово обучение

> [!NOTE]
> Надзираваното фино настройване може да доведе до загуба на съобразяване или катастрофална амнезия. Препоръчваме да проверите за този проблем и да изпълните етап на съобразяване след финото настройване.

### Параметри за фино настройване

1. Този Python скрипт настройва параметри за фино настройване на модел за машинно обучение. Ето какво прави:

    - Настройва стандартни параметри за обучение като брой епохи, размери на батчовете за обучение и оценка, скорост на обучение и тип график за скоростта на обучение.

    - Настройва стандартни параметри за оптимизация като това дали да се приложи Layer-wise Relevance Propagation (LoRa) и DeepSpeed, и стадия на DeepSpeed.

    - Комбинира параметрите за обучение и оптимизация в един речник, наречен finetune_parameters.

    - Проверява дали foundation_model има някакви специфични за модела стандартни параметри. Ако има, отпечатва предупреждение и обновява речника finetune_parameters с тези параметри. Функцията ast.literal_eval се използва, за да преобразува тези модели-специфични стойности от стринг към Python речник.

    - Отпечатва окончателния комплект параметри за фино настройване, които ще бъдат използвани за изпълнението.

    - Накратко, този скрипт настройва и показва параметрите за фино настройване на модел за машинно обучение, с възможност да се презапишат стандартните параметри със специфични за модела.

    ```python
    # Настройте основните параметри за обучение като брой епохи, размери на партидите за обучение и оценка, скорост на учене и тип на планировчика на скоростта на учене
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Настройте основните параметри за оптимизация като дали да се приложи Layer-wise Relevance Propagation (LoRa) и DeepSpeed, и етапа на DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Комбинирайте параметрите за обучение и оптимизация в един речник, наречен finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Проверете дали foundation_model има някакви модел-специфични основни параметри
    # Ако има, отпечатайте предупредително съобщение и актуализирайте речника finetune_parameters с тези модел-специфични стойности по подразбиране
    # Функцията ast.literal_eval се използва за преобразуване на модел-специфичните стойности по подразбиране от низ в Python речник
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # преобразуване на низ в python речник
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Отпечатайте крайния набор от параметри за фина настройка, които ще се използват за изпълнението
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Обучителен Pipeline

1. Този Python скрипт дефинира функция за генериране на име за показване на обучителен pipeline и след това извиква тази функция, за да генерира и отпечата името за показване. Ето какво прави:

1. Дефинирана е функцията get_pipeline_display_name. Тази функция генерира име за показване на базата на различни параметри, свързани с pipeline за обучение.

1. Вътре в функцията се изчислява общият размер на батча чрез умножаване на батча на устройство, броя стъпки за акумулиране на градиенти, броя GPU-та на възел и броя възли, използвани за фино настройване.

1. Извличат се различни други параметри като тип график за скоростта на обучение, дали е приложен DeepSpeed, стадия на DeepSpeed, дали е приложен Layer-wise Relevance Propagation (LoRa), ограничението на броя запазвани контролни точки на модела и максималната дължина на последователността.

1. Създава се низ, който включва всички тези параметри, разделени с тирета. Ако DeepSpeed или LoRa са приложени, низът включва "ds" с номера на стадия на DeepSpeed или "lora" съответно. Ако не, включва "nods" или "nolora".

1. Функцията връща този низ, който служи като име за показване на обучителния pipeline.

1. След като функцията е дефинирана, тя се извиква за генериране на името за показване, което след това се отпечатва.

1. Накратко, този скрипт генерира име за показване на обучителен pipeline за машинно обучение въз основа на различни параметри и го отпечатва.

    ```python
    # Дефинирайте функция за генериране на показвано име за тренировъчния процес
    def get_pipeline_display_name():
        # Изчислете общия размер на пакета, като умножите размера на пакета на устройство, броя на стъпките за акумулиране на градиенти, броя на GPU-та на възел и броя на възлите за фина настройка
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Вземете типа на планировчика на скоростта на обучение
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Вземете дали е приложен DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Вземете етапа на DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Ако DeepSpeed е приложен, включете "ds", последвано от етапа на DeepSpeed в показваното име; ако не, включете "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Вземете дали е приложена слойна релевантна пропагация (LoRa)
        lora = finetune_parameters.get("apply_lora", "false")
        # Ако LoRa е приложена, включете "lora" в показваното име; ако не, включете "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Вземете ограничението за броя на запазените контролни точки на модела
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Вземете максималната дължина на последователността
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Конструирайте показваното име чрез свързване на всички тези параметри, разделени с тирета
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
    
    # Извикайте функцията за генериране на показвано име
    pipeline_display_name = get_pipeline_display_name()
    # Отпечатайте показваното име
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Конфигуриране на Pipeline

Този Python скрипт дефинира и конфигурира pipeline за машинно обучение, използвайки Azure Machine Learning SDK. Ето какво прави:

1. Импортира необходимите модули от Azure AI ML SDK.

1. Извлича компонент от pipeline с име "chat_completion_pipeline" от регистъра.

1. Дефинира pipeline задача, използвайки декоратора `@pipeline` и функцията `create_pipeline`. Името на pipeline е зададено като `pipeline_display_name`.

1. Във функцията `create_pipeline` инициализира извлечения pipeline компонент с различни параметри, включително пътя до модела, изчислителни клъстъри за различните етапи, деления на набора от данни за обучение и тестване, броя GPU-та за фино настройване и други параметри за фино настройване.

1. Свързва изхода на задачата за фино настройване с изхода на pipeline задачата. Това се прави, за да може фино настроеният модел лесно да бъде регистриран, което е необходимо за публикуване на модела към онлайн или партиден крайна точка.

1. Създава инстанция на pipeline чрез извикване на функцията `create_pipeline`.

1. Задава настройката `force_rerun` на pipeline на `True`, което означава, че кешираните резултати от предишни задачи няма да се използват.

1. Задава настройката `continue_on_step_failure` на pipeline на `False`, което означава, че pipeline ще спре, ако някоя стъпка се провали.

1. Накратко, този скрипт дефинира и конфигурира pipeline за машинно обучение за задача за чат-завършване, използвайки Azure Machine Learning SDK.

    ```python
    # Импортиране на необходимите модули от Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Извличане на компонент на pipeline с име "chat_completion_pipeline" от регистъра
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Дефиниране на pipeline задача с помощта на декоратора @pipeline и функцията create_pipeline
    # Името на pipeline е зададено като pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Инициализиране на извлечения компонент на pipeline с различни параметри
        # Те включват път към модела, изчислителни клъстери за различни етапи, набори от данни за обучение и тестване, брой GPU за дообучение и други параметри за дообучение
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Свързване на наборите от данни с параметрите
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Настройки за обучение
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Зададено е на броя на наличните GPU в изчислителната инфраструктура
            **finetune_parameters
        )
        return {
            # Свързване на изхода от задачата за дообучение с изхода на pipeline задачата
            # Това се прави, за да може лесно да регистрираме дообучения модел
            # Регистрацията на модела е необходима за разгръщане на модела на онлайн или пакетен краен пункт
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Създаване на инстанция на pipeline чрез извикване на функцията create_pipeline
    pipeline_object = create_pipeline()
    
    # Не използвайте кеширани резултати от предишни задачи
    pipeline_object.settings.force_rerun = True
    
    # Задаване на продължаване при грешка в стъпка на False
    # Това означава, че pipeline ще спре, ако някоя стъпка се провали
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Подаване на задачата

1. Този Python скрипт подава задача pipeline за машинно обучение към Azure Machine Learning работна област и след това изчаква задачата да завърши. Ето какво прави:

    - Извиква метода create_or_update на обекта jobs в workspace_ml_client, за да подаде pipeline задачата. Pipeline задачата, която трябва да се изпълни, е зададена чрез pipeline_object, а експериментът, под който задачата се изпълнява, е зададен чрез experiment_name.

    - След това извиква метода stream на обекта jobs в workspace_ml_client, за да изчака завършване на pipeline задачата. Задачата, за която се изчаква, е указана чрез атрибута name на обекта pipeline_job.

    - Накратко, този скрипт подава pipeline задача за машинно обучение към Azure Machine Learning работна област и изчаква задачата да завърши.

    ```python
    # Изпратете задание в pipeline към работното пространство Azure Machine Learning
    # Pipeline за изпълнение е посочен чрез pipeline_object
    # Експериментът, под който се изпълнява заданието, е посочен чрез experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Изчакайте заданието в pipeline да приключи
    # Заданието, за което се изчаква, е посочено чрез атрибута name на обекта pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Регистриране на финно настроения модел в работната област

Ще регистрираме модела от изхода на задачата за фино настройване. Това ще проследи родословието между финно настроения модел и задачата за фино настройване. Допълнително, задачата за фино настройване проследява родословието до основния модел, данните и учебния код.

### Регистриране на ML модела

1. Този Python скрипт регистрира модел за машинно обучение, който е обучен в pipeline на Azure Machine Learning. Ето какво прави:

    - Импортира необходими модули от Azure AI ML SDK.

    - Проверява дали изходът trained_model е наличен от pipeline задачата чрез извикване на метода get на обекта jobs в workspace_ml_client и достъпва неговия атрибут outputs.

    - Формира път към обучението модел чрез форматиране на стринг с името на pipeline задачата и името на изхода ("trained_model").

    - Определя име за финно настроения модел, като добавя "-ultrachat-200k" към оригиналното име на модела и заменя всички наклонени черти със тирета.

    - Подготвя се за регистриране на модел чрез създаване на обект Model с различни параметри, включително път към модела, тип на модела (MLflow модел), име и версия на модела, и описание на модела.

    - Регистрира модела, като извиква метода create_or_update на обекта models в workspace_ml_client с обекта Model като аргумент.

    - Отпечатва регистрирания модел.

1. Накратко, този скрипт регистрира модел за машинно обучение, обучен в pipeline на Azure Machine Learning.
    
    ```python
    # Импортирайте необходимите модули от Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Проверете дали изходът `trained_model` е наличен от pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Създайте път до обучен моделен файл чрез форматиране на стринг с името на pipeline job и името на изхода ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Задайте име за финално настроения модел, като добавите "-ultrachat-200k" към оригиналното име на модела и замените всички наклонени черти с тирета
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Подгответе се за регистриране на модела, като създадете обект Model с различни параметри
    # Те включват пътя до модела, типа на модела (MLflow модел), името и версията на модела и описание на модела
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Използвайте времеви печат като версия, за да избегнете конфликт на версиите
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Регистрирайте модела като извикате метода create_or_update на обекта models в workspace_ml_client с обекта Model като аргумент
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Отпечатайте регистрирания модел
    print("registered model: \n", registered_model)
    ```

## 7. Публикуване на финно настроения модел към онлайн крайна точка

Онлайн крайните точки предоставят издръжлив REST API, който може да се използва за интеграция с приложения, които трябва да използват модела.

### Управление на Крайната Точка

1. Този Python скрипт създава управлявана онлайн крайна точка в Azure Machine Learning за регистриран модел. Ето какво прави:

    - Импортира необходими модули от Azure AI ML SDK.

    - Определя уникално име за онлайн крайната точка, като добавя времеви маркер към низ "ultrachat-completion-".

    - Подготвя създаването на онлайн крайната точка чрез създаване на обект ManagedOnlineEndpoint с различни параметри, включително името на крайната точка, описание и режим на удостоверяване ("key").

    - Създава онлайн крайната точка чрез извикване на метода begin_create_or_update на workspace_ml_client с обекта ManagedOnlineEndpoint като аргумент, след което изчаква завършване на операцията чрез метода wait.

1. Накратко, този скрипт създава управлявана онлайн крайна точка в Azure Machine Learning за регистриран модел.

    ```python
    # Импортирайте необходимите модули от Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Дефинирайте уникално име за онлайн крайна точка, като добавите времеви отпечатък към низа "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Подгответе създаването на онлайн крайната точка, като създадете обект ManagedOnlineEndpoint с различни параметри
    # Те включват името на крайната точка, описание на крайната точка и режим на удостоверяване ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Създайте онлайн крайната точка, като извикате метода begin_create_or_update на workspace_ml_client с обекта ManagedOnlineEndpoint като аргумент
    # След това изчакайте операцията по създаване да завърши, като извикате метода wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Можете да намерите тук списъка на поддържаните SKU за публикуване - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Публикуване на ML Модел

1. Този Python скрипт публикува регистриран модел за машинно обучение в управлявана онлайн крайна точка в Azure Machine Learning. Ето какво прави:

    - Импортира модула ast, който предоставя функции за обработка на дървета от абстрактната синтактична граматика на Python.

    - Определя типа инстанция за публикуване на "Standard_NC6s_v3".

    - Проверява дали тагът inference_compute_allow_list е наличен в основния модел. Ако е, преобразува стойността на тага от стринг към Python лист и го задава на inference_computes_allow_list. Ако не е, задава inference_computes_allow_list на None.

    - Проверява дали определеният тип инстанция е в позволения списък. Ако не е, отпечатва съобщение, което моли потребителя да избере тип инстанция от позволения списък.

    - Подготвя създаването на публикуването чрез създаване на обект ManagedOnlineDeployment с различни параметри, включително името на публикуването, името на крайната точка, ID на модела, тип и брой инстанции, настройки за проверка на живост и заявки.

    - Създава публикуването чрез извикване на метода begin_create_or_update на workspace_ml_client с обекта ManagedOnlineDeployment като аргумент, след което изчаква завършване на операцията с метода wait.

    - Задава трафика на крайната точка да насочва 100% от трафика към публикуването "demo".

    - Обновява крайната точка чрез извикване на метода begin_create_or_update на workspace_ml_client с обекта endpoint като аргумент, след което изчаква завършване на операцията чрез метода result.

1. Накратко, този скрипт публикува регистриран модел за машинно обучение в управлявана онлайн крайна точка в Azure Machine Learning.

    ```python
    # Импортирайте модула ast, който предоставя функции за обработка на дървета на абстрактната синтактична граматика на Python
    import ast
    
    # Задайте типа на инстанцията за разгръщането
    instance_type = "Standard_NC6s_v3"
    
    # Проверете дали тагът `inference_compute_allow_list` присъства във фондационния модел
    if "inference_compute_allow_list" in foundation_model.tags:
        # Ако е така, конвертирайте стойността на тага от низ в Python списък и го присвоете на `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Ако не е, задайте `inference_computes_allow_list` на `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Проверете дали посоченият тип инстанция е в списъка с позволени
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Подгответе създаването на разгръщането чрез създаване на обект `ManagedOnlineDeployment` с различни параметри
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Създайте разгръщането, като извикате метода `begin_create_or_update` на `workspace_ml_client` с обекта `ManagedOnlineDeployment` като аргумент
    # След това изчакайте завършването на операцията по създаване, като извикате метода `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Задайте трафика на крайната точка да насочва 100% от трафика към разгръщането "demo"
    endpoint.traffic = {"demo": 100}
    
    # Актуализирайте крайната точка, като извикате метода `begin_create_or_update` на `workspace_ml_client` с обекта `endpoint` като аргумент
    # След това изчакайте завършването на операцията по актуализация, като извикате метода `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Тест на крайната точка със тестови данни

Ще изтеглим примерни данни от тестовия набор и ще ги подадем към онлайн крайната точка за предсказание. След това ще покажем оценените етикети заедно с реалните етикети

### Четене на резултатите

1. Този Python скрипт чете файл във формат JSON Lines в pandas DataFrame, взема случаен пример и нулира индекса. Ето какво прави:

    - Чете файла ./ultrachat_200k_dataset/test_gen.jsonl в pandas DataFrame. Функцията read_json се използва с аргумент lines=True, тъй като файлът е във формат JSON Lines, където всеки ред е отделен JSON обект.

    - Взема случаен пример от 1 ред от DataFrame. Функцията sample се използва с аргумент n=1, за да се зададе броят случайни редове за избор.

    - Нулира индекса на DataFrame. Функцията reset_index се използва с аргумент drop=True, за да се пропусне оригиналния индекс и да се замени с нов индекс с целочислени стойности по подразбиране.

    - Показва първите 2 реда от DataFrame, използвайки функцията head с аргумент 2. Тъй като обаче DataFrame съдържа само един ред след извадката, ще се покаже само този един ред.

1. Накратко, този скрипт чете JSON Lines файл в pandas DataFrame, взема случаен пример от 1 ред, нулира индекса и показва първия ред.
    
    ```python
    # Импортиране на библиотеката pandas
    import pandas as pd
    
    # Четене на файла JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' в pandas DataFrame
    # Аргументът 'lines=True' указва, че файлът е във формат JSON Lines, където всеки ред е отделен JSON обект
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Вземане на случаен пример от 1 ред от DataFrame
    # Аргументът 'n=1' указва броя случайни редове за избор
    test_df = test_df.sample(n=1)
    
    # Ресетване на индекса на DataFrame
    # Аргументът 'drop=True' указва, че оригиналният индекс трябва да бъде премахнат и заменен с нов индекс от стандартни цели числа
    # Аргументът 'inplace=True' указва, че DataFrame трябва да бъде променен на място (без създаване на нов обект)
    test_df.reset_index(drop=True, inplace=True)
    
    # Показване на първите 2 реда от DataFrame
    # Въпреки това, тъй като DataFrame съдържа само един ред след извадката, това ще покаже само този един ред
    test_df.head(2)
    ```

### Създаване на JSON Обект

1. Този Python скрипт създава JSON обект с конкретни параметри и го записва във файл. Ето какво прави:

    - Импортира модула json, който предоставя функции за работа с JSON данни.
    - Създава речник parameters с ключове и стойности, които представляват параметри за модел на машинно обучение. Ключовете са "temperature", "top_p", "do_sample" и "max_new_tokens", а съответните им стойности са 0.6, 0.9, True и 200.

    - Създава друг речник test_json с два ключа: "input_data" и "params". Стойността на "input_data" е друг речник с ключове "input_string" и "parameters". Стойността на "input_string" е списък, съдържащ първото съобщение от DataFrame-а test_df. Стойността на "parameters" е речника parameters, създаден по-рано. Стойността на "params" е празен речник.

    - Отваря файл на име sample_score.json
    
    ```python
    # Импортирайте модула json, който предоставя функции за работа с JSON данни
    import json
    
    # Създайте речник `parameters` с ключове и стойности, които представляват параметри за модел за машинно обучение
    # Ключовете са "temperature", "top_p", "do_sample" и "max_new_tokens", а съответните им стойности са 0.6, 0.9, True и 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Създайте друг речник `test_json` с два ключа: "input_data" и "params"
    # Стойността на "input_data" е друг речник с ключове "input_string" и "parameters"
    # Стойността на "input_string" е списък, който съдържа първото съобщение от DataFrame `test_df`
    # Стойността на "parameters" е създаденият по-рано речник `parameters`
    # Стойността на "params" е празен речник
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Отворете файл с име `sample_score.json` в директорията `./ultrachat_200k_dataset` в режим за запис
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Запишете речника `test_json` във файла във формат JSON, използвайки функцията `json.dump`
        json.dump(test_json, f)
    ```

### Извикване на крайна точка

1. Този Python скрипт извиква онлайн крайна точка в Azure Machine Learning, за да оцени JSON файл. Ето обяснение на това, което прави:

    - Извиква метода invoke на свойството online_endpoints на обекта workspace_ml_client. Този метод се използва за изпращане на заявка към онлайн крайна точка и получаване на отговор.

    - Задава името на крайната точка и на разгръщането с аргументите endpoint_name и deployment_name. В този случай, името на крайната точка е съхранено в променливата online_endpoint_name, а името на разгръщането е "demo".

    - Задава пътя към JSON файла, който трябва да бъде оценен, с аргумента request_file. В този случай, файлът е ./ultrachat_200k_dataset/sample_score.json.

    - Съхранява отговора от крайната точка в променливата response.

    - Извежда суровия отговор.

1. В обобщение, този скрипт извиква онлайн крайна точка в Azure Machine Learning, за да оцени JSON файл и извежда отговора.

    ```python
    # Извикайте онлайн края в Azure Machine Learning, за да оцените файла `sample_score.json`
    # Методът `invoke` на свойството `online_endpoints` на обекта `workspace_ml_client` се използва за изпращане на заявка към онлайн край и получаване на отговор
    # Аргументът `endpoint_name` указва името на края, което е записано в променливата `online_endpoint_name`
    # Аргументът `deployment_name` указва името на разполагането, което е "demo"
    # Аргументът `request_file` указва пътя към JSON файла за оценяване, който е `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Изведете суровия отговор от края
    print("raw response: \n", response, "\n")
    ```

## 9. Изтриване на онлайн крайната точка

1. Не забравяйте да изтриете онлайн крайната точка, в противен случай ще оставите таксуването да работи за ресурса, използван от крайната точка. Този ред Python код изтрива онлайн крайна точка в Azure Machine Learning. Ето обяснение на това, което прави:

    - Извиква метода begin_delete на свойството online_endpoints на обекта workspace_ml_client. Този метод стартира изтриването на онлайн крайна точка.

    - Задава името на крайната точка, която ще бъде изтрита, с аргумента name. В този случай, името на крайната точка е съхранено в променливата online_endpoint_name.

    - Извиква метода wait, за да изчака операцията по изтриването да завърши. Това е блокираща операция, което означава, че ще предотврати продължаването на скрипта, докато изтриването не приключи.

    - В обобщение, този ред код стартира изтриването на онлайн крайна точка в Azure Machine Learning и чака операцията да бъде завършена.

    ```python
    # Изтрийте онлайн крайна точка в Azure Machine Learning
    # Методът `begin_delete` на свойството `online_endpoints` на обекта `workspace_ml_client` се използва за започване на изтриването на онлайн крайна точка
    # Аргументът `name` указва името на крайна точка, която трябва да бъде изтрита, което е съхранено в променливата `online_endpoint_name`
    # Методът `wait` се извиква, за да изчака завършването на операцията по изтриване. Това е блокираща операция, което означава, че ще попречи на скрипта да продължи, докато изтриването не приключи
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->