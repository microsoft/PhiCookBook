## Как использовать компоненты chat-completion из системного реестра Azure ML для дообучения модели

В этом примере мы проведём дообучение модели Phi-3-mini-4k-instruct для завершения разговора между 2 людьми с использованием набора данных ultrachat_200k.

![MLFineTune](../../../../translated_images/ru/MLFineTune.928d4c6b3767dd35.webp)

Пример покажет, как выполнить дообучение с помощью Azure ML SDK и Python, а затем развернуть дообученную модель на онлайн-эндпоинте для вывода в реальном времени.

### Данные для обучения

Мы будем использовать набор данных ultrachat_200k. Это сильно отфильтрованная версия набора данных UltraChat, использованная для обучения Zephyr-7B-β, передовой чат-модели с 7 миллиардами параметров.

### Модель

Мы используем модель Phi-3-mini-4k-instruct, чтобы показать как пользователь может дообучить модель для задачи завершения чата. Если вы открыли этот ноутбук из карточки конкретной модели, не забудьте заменить имя модели.

### Задачи

- Выбрать модель для дообучения.
- Выбрать и изучить данные для обучения.
- Настроить задачу дообучения.
- Запустить задачу дообучения.
- Просмотреть метрики обучения и оценки.
- Зарегистрировать дообученную модель.
- Развернуть дообученную модель для вывода в реальном времени.
- Очистить ресурсы.

## 1. Настройка предварительных требований

- Установить зависимости
- Подключиться к рабочему пространству AzureML. Подробнее в статье о настройке аутентификации SDK. Замените <WORKSPACE_NAME>, <RESOURCE_GROUP> и <SUBSCRIPTION_ID> ниже.
- Подключиться к системному реестру azureml
- Установить опциональное имя эксперимента
- Проверить или создать вычислительный ресурс.

> [!NOTE]
> Требуется один узел с GPU, который может содержать несколько видеокарт. Например, в одном узле Standard_NC24rs_v3 установлено 4 GPU NVIDIA V100, в Standard_NC12s_v3 — 2 GPU NVIDIA V100. Дополнительную информацию смотрите в документации. Количество GPU на узел задаётся в параметре gpus_per_node ниже. Правильная настройка гарантирует использование всех GPU узла. Рекомендуемые SKU GPU-компьютеров можно найти здесь и здесь.

### Библиотеки Python

Установите зависимости, выполнив приведённую ниже ячейку. Это обязательный шаг при запуске в новой среде.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Взаимодействие с Azure ML

1. Этот скрипт на Python используется для взаимодействия с сервисом Azure Machine Learning (Azure ML). Вот его разбор:

    - Импортирует необходимые модули из пакетов azure.ai.ml, azure.identity и azure.ai.ml.entities. Также импортирует модуль time.

    - Пытается аутентифицироваться с помощью DefaultAzureCredential(), который обеспечивает упрощённый механизм аутентификации для быстрого начала разработки приложений в облаке Azure. При ошибке использует InteractiveBrowserCredential(), обеспечивающий интерактивный вход.

    - Пытается создать объект MLClient с помощью метода from_config, который читает конфигурацию из файла config.json. При ошибке создаёт MLClient вручную, передавая subscription_id, resource_group_name и workspace_name.

    - Создаёт ещё один экземпляр MLClient для системного реестра Azure ML с именем "azureml". В этом реестре хранятся модели, пайплайны дообучения и среды.

    - Устанавливает имя эксперимента experiment_name в значение "chat_completion_Phi-3-mini-4k-instruct".

    - Генерирует уникальную метку времени, переводя текущее время (секунды с эпохи в формате float) в целое число, а затем в строку. Эта метка используется для создания уникальных имён и версий.

    ```python
    # Импорт необходимых модулей из Azure ML и Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Импорт модуля time
    
    # Попытка аутентификации с помощью DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Если DefaultAzureCredential не сработает, использовать InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Попытка создать экземпляр MLClient с использованием файла конфигурации по умолчанию
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Если это не удастся, создать экземпляр MLClient, предоставив данные вручную
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Создать другой экземпляр MLClient для реестра Azure ML с именем "azureml"
    # В этом реестре хранятся модели, пайплайны тонкой настройки и окружения
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Установить имя эксперимента
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Сгенерировать уникальную временную метку, которая может использоваться для имен и версий, требующих уникальности
    timestamp = str(int(time.time()))
    ```

## 2. Выбор базовой модели для дообучения

1. Phi-3-mini-4k-instruct — это лёгкая открытая модель размером 3.8 млрд параметров, построенная на наборах данных, используемых для Phi-2. Эта модель принадлежит семейству Phi-3, а версия Mini выходит в двух вариантах: 4K и 128K, которые обозначают длину контекста (в токенах), которую модель может поддерживать. Для использования необходимо дообучить модель под нашу задачу. Вы можете изучить эти модели в Каталоге моделей AzureML Studio, отфильтровав по задаче chat-completion. В данном примере мы используем модель Phi-3-mini-4k-instruct. Если вы открыли этот ноутбук под другую модель, замените название и версию модели соответственно.

> [!NOTE]
> свойство model id модели. Оно будет передано как вход в задачу дообучения. Также доступно как Asset ID на странице модели в Каталоге моделей AzureML Studio.

2. Этот скрипт на Python взаимодействует с Azure Machine Learning (Azure ML) сервисом. Вот что он делает:

    - Устанавливает переменную model_name в "Phi-3-mini-4k-instruct".

    - Использует метод get объекта models реестра registry_ml_client для получения последней версии модели с указанным именем из системного реестра Azure ML. Метод вызывается с аргументами: имя модели и метка, указывающая на последнюю версию.

    - Выводит сообщение в консоль с названием, версией и идентификатором модели, которая будет использоваться для дообучения. Метод format строки используется для подстановки этих значений. Данные берутся из свойств объекта foundation_model.

    ```python
    # Установить имя модели
    model_name = "Phi-3-mini-4k-instruct"
    
    # Получить последнюю версию модели из реестра Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Вывести имя модели, версию и идентификатор
    # Эта информация полезна для отслеживания и отладки
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Создание вычислительного ресурса для задачи

Задача дообучения работает ТОЛЬКО с GPU-компьютерами. Размер вычислительного ресурса зависит от размера модели, и часто сложно определить подходящий ресурс. В этой ячейке мы помогаем пользователю выбрать правильный компьютер.

> [!NOTE]
> Перечисленные ниже вычислительные ресурсы работают с максимально оптимальной конфигурацией. Любые изменения могут привести к ошибке Cuda Out Of Memory. В таких случаях попробуйте увеличить размер ресурса.

> [!NOTE]
> При выборе compute_cluster_size убедитесь, что вычислительный ресурс доступен в вашей группе ресурсов. Если нужный ресурс недоступен, можно подать заявку на доступ к вычислительным ресурсам.

### Проверка поддержки дообучения моделью

1. Этот скрипт на Python взаимодействует с моделью Azure Machine Learning. Вот его разбор:

    - Импортирует модуль ast, который предоставляет функции для обработки деревьев абстрактного синтаксиса Python.

    - Проверяет, есть ли у объекта foundation_model (представляющего модель в Azure ML) тег с именем finetune_compute_allow_list. Теги в Azure ML — это пары ключ-значение, которые можно создавать и использовать для фильтрации и сортировки моделей.

    - Если тег finetune_compute_allow_list присутствует, с помощью ast.literal_eval безопасно преобразует строковое значение тега в список Python. Этот список присваивается переменной computes_allow_list. Затем выводит сообщение о том, что нужно создать вычислительный ресурс из списка.

    - Если тега finetune_compute_allow_list нет, переменная computes_allow_list устанавливается в None, и выводится соответствующее сообщение.

    - Итог: скрипт проверяет наличие специфического тега в метаданных модели, преобразует его значение в список, если он есть, и информирует пользователя.

    ```python
    # Импортировать модуль ast, который предоставляет функции для обработки деревьев абстрактного синтаксиса Python
    import ast
    
    # Проверить, присутствует ли тег 'finetune_compute_allow_list' среди тегов модели
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Если тег присутствует, использовать ast.literal_eval для безопасного преобразования значения тега (строки) в список Python
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # преобразовать строку в список Python
        # Вывести сообщение, указывающее на необходимость создания вычисления из списка
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Если тег отсутствует, установить computes_allow_list в None
        computes_allow_list = None
        # Вывести сообщение, что тег 'finetune_compute_allow_list' не является частью тегов модели
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Проверка вычислительного экземпляра

1. Этот скрипт на Python взаимодействует с сервисом Azure Machine Learning и выполняет несколько проверок вычислительного экземпляра. Вот что он делает:

    - Пытается получить вычислительный экземпляр с именем compute_cluster из рабочей области Azure ML. Если состояние provisioning этого экземпляра равно "failed", выбрасывает исключение ValueError.

    - Проверяет, что переменная computes_allow_list не None. Если это так, преобразует все размеры вычислений в списке в нижний регистр и проверяет, есть ли размер текущего вычислительного экземпляра в этом списке. Если нет — выбрасывает ValueError.

    - Если computes_allow_list равно None, проверяет, входит ли размер вычисления в список неподдерживаемых GPU VM. Если входит — выбрасывает ValueError.

    - Получает список всех доступных размеров вычислений в рабочей области. Затем перебирает их и, если имя совпадает с размером текущего экземпляра, получает количество GPU для этого размера и устанавливает флаг gpu_count_found.

    - Если gpu_count_found истинно, выводит количество GPU текущего экземпляра. Иначе выбрасывает ValueError.

    - Итог: скрипт выполняет проверки вычислительного экземпляра в Azure ML: состояние provisioning, размер в списке допустимых/недопустимых, и количество GPU.

    ```python
    # Вывести сообщение об исключении
    print(e)
    # Выбросить ValueError, если размер вычислительного ресурса недоступен в рабочем пространстве
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Получить вычислительный экземпляр из рабочей среды Azure ML
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Проверить, находится ли состояние развертывания вычислительного экземпляра в состоянии "failed"
    if compute.provisioning_state.lower() == "failed":
        # Выбросить ValueError, если состояние развертывания равно "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Проверить, что computes_allow_list не равен None
    if computes_allow_list is not None:
        # Преобразовать все размеры вычислительных ресурсов в computes_allow_list в нижний регистр
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Проверить, что размер вычислительного экземпляра находится в computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Выбросить ValueError, если размер вычислительного экземпляра отсутствует в computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Определить список неподдерживаемых размеров GPU виртуальных машин
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Проверить, что размер вычислительного экземпляра находится в unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Выбросить ValueError, если размер вычислительного экземпляра находится в unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Инициализировать флаг для проверки, найдено ли количество GPU в вычислительном экземпляре
    gpu_count_found = False
    # Получить список всех доступных размеров вычислительных ресурсов в рабочем пространстве
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Перебрать список доступных размеров вычислительных ресурсов
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Проверить, совпадает ли имя размера вычислительного ресурса с размером вычислительного экземпляра
        if compute_sku.name.lower() == compute.size.lower():
            # Если да, получить количество GPU для этого размера и установить gpu_count_found в True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Если gpu_count_found равно True, вывести количество GPU в вычислительном экземпляре
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Если gpu_count_found равно False, выбросить ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Выбор набора данных для дообучения модели

1. Мы используем набор данных ultrachat_200k. Набор содержит четыре сплита, подходящих для контролируемого дообучения (Supervised fine-tuning, sft).
Generation ranking (gen). Количество примеров на сплит показано ниже:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Следующие ячейки показывают базовую подготовку данных для дообучения:

### Визуализация некоторых строк данных

Мы хотим, чтобы образец выполнялся быстро, поэтому сохраняем файлы train_sft, test_sft, содержащие 5% уже отобранных строк. Это значит, что у дообученной модели будет меньшая точность, и её не следует использовать в реальных условиях.
Скрипт download-dataset.py используется для загрузки набора ultrachat_200k и преобразования данных в формат, пригодный для компонента пайплайна дообучения. Поскольку набор большой, здесь используется только его часть.

1. Выполнение следующего скрипта загрузит только 5% данных. Это можно увеличить, изменив параметр dataset_split_pc на нужный процент.

> [!NOTE]
> У некоторых языковых моделей используются разные языковые коды, поэтому имена столбцов в наборе данных должны соответствовать этому.

1. Вот пример того, как должны выглядеть данные
Набор chat-completion хранится в формате parquet, каждая запись имеет следующую схему:

    - Это JSON (JavaScript Object Notation) документ, популярный формат обмена данными. Это не исполняемый код, а способ хранения и передачи данных. Разбор структуры:

    - "prompt": ключ, содержащий строковое значение — задачу или вопрос для AI ассистента.

    - "messages": ключ, содержащий массив объектов. Каждый объект представляет сообщение в разговоре между пользователем и AI ассистентом. Каждый объект сообщения имеет два ключа:

    - "content": строка с содержимым сообщения.
    - "role": строка с ролью отправителя сообщения. Может быть "user" или "assistant".
    - "prompt_id": строка с уникальным идентификатором запроса.

1. В данном JSON-документе представлен диалог, где пользователь просит AI создать главного героя для антиутопической истории. Ассистент отвечает, пользователь просит подробностей, ассистент соглашается их предоставить. Весь разговор связан с конкретным prompt id.

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

### Загрузка данных

1. Этот скрипт на Python используется для загрузки набора данных с помощью вспомогательного скрипта download-dataset.py. Разбор:

    - Импортирует модуль os, предоставляющий функциональность, зависящую от операционной системы.

    - С помощью os.system запускает скрипт download-dataset.py в командной строке с аргументами: имя набора (HuggingFaceH4/ultrachat_200k), директорию для загрузки (ultrachat_200k_dataset) и процент деления набора (5). Возвращаемый код выполнения сохраняется в exit_status.

    - Проверяет, что exit_status не равен 0. В Unix-подобных системах код 0 означает успех, любой другой — ошибку. Если код не 0, выбрасывает исключение Exception с сообщением об ошибке загрузки.

    - Итог: скрипт выполняет команду загрузки набора данных и выбрасывает ошибку при неудаче.

    ```python
    # Импортировать модуль os, который предоставляет способ использования функциональности, зависящей от операционной системы
    import os
    
    # Использовать функцию os.system для запуска сценария download-dataset.py в оболочке с определёнными аргументами командной строки
    # Аргументы указывают набор данных для загрузки (HuggingFaceH4/ultrachat_200k), директорию для загрузки (ultrachat_200k_dataset) и процент разделения набора данных (5)
    # Функция os.system возвращает код завершения выполненной команды; этот код сохраняется в переменной exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Проверить, если exit_status не равен 0
    # В Unix-подобных операционных системах код завершения 0 обычно означает успешное выполнение команды, а любое другое число указывает на ошибку
    # Если exit_status не равен 0, вызвать исключение Exception с сообщением, указывающим на ошибку при загрузке набора данных
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Загрузка данных в DataFrame

1. Этот скрипт загружает файл JSON Lines в pandas DataFrame и выводит первые 5 строк. Обзор:

    - Импортирует библиотеку pandas — мощный инструмент для анализа и обработки данных.

    - Устанавливает максимальную ширину столбца для отображения pandas в 0, что означает отображение полного текста столбцов без усечения при выводе DataFrame.
    - Он использует функцию pd.read_json для загрузки файла train_sft.jsonl из директории ultrachat_200k_dataset в DataFrame. Аргумент lines=True указывает, что файл в формате JSON Lines, где каждая строка — отдельный JSON-объект.

    - Он использует метод head для отображения первых 5 строк DataFrame. Если DataFrame содержит менее 5 строк, будут показаны все строки.

    - Вкратце, этот скрипт загружает файл формата JSON Lines в DataFrame и отображает первые 5 строк с полным текстом столбцов.
    
    ```python
    # Импортируйте библиотеку pandas, которая является мощной библиотекой для манипулирования данными и анализа
    import pandas as pd
    
    # Установите максимальную ширину столбца для опций отображения pandas в 0
    # Это означает, что полный текст каждого столбца будет отображаться без усечения при выводе DataFrame
    pd.set_option("display.max_colwidth", 0)
    
    # Используйте функцию pd.read_json для загрузки файла train_sft.jsonl из директории ultrachat_200k_dataset в DataFrame
    # Аргумент lines=True указывает, что файл имеет формат JSON Lines, где каждая строка является отдельным JSON объектом
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Используйте метод head, чтобы отобразить первые 5 строк DataFrame
    # Если в DataFrame меньше 5 строк, будут отображены все строки
    df.head()
    ```

## 5. Отправьте задание тонкой настройки, используя модель и данные в качестве входных данных

Создайте задание, которое использует компонент pipeline для чат-запросов. Узнайте больше обо всех параметрах, поддерживаемых для тонкой настройки.

### Определение параметров тонкой настройки

1. Параметры тонкой настройки можно разделить на 2 категории — параметры обучения, параметры оптимизации.

1. Параметры обучения определяют аспекты обучения, такие как —

    - используемый оптимизатор, планировщик
    - метрика для оптимизации тонкой настройки
    - количество шагов обучения, размер батча и так далее
    - Параметры оптимизации помогают оптимизировать использование памяти GPU и эффективно использовать вычислительные ресурсы. 

1. Ниже приведены некоторые параметры, относящиеся к этой категории. Параметры оптимизации различаются для каждой модели и поставляются вместе с моделью для обработки этих различий.

    - Включить deepspeed и LoRA
    - Включить обучение с использованием смешанной точности
    - Включить обучение на нескольких узлах

> [!NOTE]
> Супервизированная тонкая настройка может привести к потере согласованности или катастрофическому забвению. Рекомендуем проверять эту проблему и запускать этап выравнивания после тонкой настройки.

### Параметры тонкой настройки

1. Этот скрипт на Python задаёт параметры для тонкой настройки модели машинного обучения. Вот что он делает:

    - Устанавливает параметры обучения по умолчанию, такие как количество эпох обучения, размеры батча для обучения и оценки, скорость обучения и тип планировщика скорости обучения.

    - Устанавливает параметры оптимизации по умолчанию, например, применять ли Layer-wise Relevance Propagation (LoRa) и DeepSpeed, а также этап DeepSpeed.

    - Объединяет параметры обучения и оптимизации в единую словарную переменную finetune_parameters.

    - Проверяет, есть ли у foundation_model какие-либо специфические для модели параметры по умолчанию. Если есть, выводит предупреждение и обновляет словарь finetune_parameters этими параметрами. Функция ast.literal_eval используется для преобразования этих параметров из строки в словарь Python.

    - Выводит окончательный набор параметров тонкой настройки, которые будут использоваться для запуска.

    - Итого, скрипт задаёт и показывает параметры тонкой настройки модели с возможностью переопределить значения параметров по умолчанию специфичными для модели.

    ```python
    # Установите параметры обучения по умолчанию, такие как количество эпох обучения, размеры пакетов для обучения и оценки, скорость обучения и тип планировщика скорости обучения
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Установите параметры оптимизации по умолчанию, такие как применение слой-ориентированной релевантной пропагации (LoRa) и DeepSpeed, а также этап DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Объедините параметры обучения и оптимизации в один словарь под названием finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Проверьте, есть ли у foundation_model какие-либо параметры по умолчанию, специфичные для модели
    # Если есть, выведите предупреждающее сообщение и обновите словарь finetune_parameters этими параметрами по умолчанию, специфичными для модели
    # Функция ast.literal_eval используется для преобразования моделей-специфичных параметров по умолчанию из строки в словарь Python
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # преобразовать строку в словарь Python
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Выведите окончательный набор параметров дообучения, который будет использоваться для запуска
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Тренировочный pipeline

1. Этот скрипт на Python определяет функцию создания отображаемого имени для тренировочного pipeline машинного обучения, а затем вызывает эту функцию и выводит полученное имя. Вот что происходит:

1. Определяется функция get_pipeline_display_name. Эта функция генерирует отображаемое имя на основании разных параметров, связанных с процессом обучения.

1. Внутри функции вычисляется общий размер батча путём умножения размера батча на устройство, количества шагов накопления градиента, количества GPU на узел и количества узлов, использованных для тонкой настройки.

1. Получаются различные другие параметры, такие как тип планировщика скорости обучения, используется ли DeepSpeed, этап DeepSpeed, применяется ли Layer-wise Relevance Propagation (LoRa), ограничение на количество сохраняемых контрольных точек модели и максимальная длина последовательности.

1. Формируется строка, в которую включены все эти параметры, разделённые дефисами. Если используется DeepSpeed или LoRa, в строке присутствует "ds" с указанием этапа DeepSpeed, или "lora" соответственно. Если нет, то "nods" или "nolora" соответственно.

1. Функция возвращает эту строку, которая служит отображаемым именем для тренировочного pipeline.

1. После определения функции, она вызывается для создания отображаемого имени, которое затем выводится.

1. В итоге, этот скрипт создает и показывает отображаемое имя для pipeline машинного обучения на основе различных параметров.

    ```python
    # Определите функцию для генерации отображаемого имени для тренировочного конвейера
    def get_pipeline_display_name():
        # Вычислите общий размер батча, умножив размер батча на устройство, количество шагов накопления градиентов, количество GPU на узел и количество узлов, используемых для дообучения
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Получите тип планировщика скорости обучения
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Получите информацию о применении DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Получите этап DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Если DeepSpeed применяется, включите "ds", за которым следует этап DeepSpeed, в отображаемое имя; если нет, включите "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Получите информацию о применении Layer-wise Relevance Propagation (LoRa)
        lora = finetune_parameters.get("apply_lora", "false")
        # Если LoRa применяется, включите "lora" в отображаемое имя; если нет, включите "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Получите ограничение на количество сохраняемых контрольных точек модели
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Получите максимальную длину последовательности
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Сформируйте отображаемое имя, объединив все эти параметры, разделённые дефисами
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
    
    # Вызовите функцию для генерации отображаемого имени
    pipeline_display_name = get_pipeline_display_name()
    # Выведите отображаемое имя на печать
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Конфигурация Pipeline

Этот скрипт на Python определяет и настраивает pipeline машинного обучения с использованием Azure Machine Learning SDK. Вот что он делает:

1. Импортирует необходимые модули из Azure AI ML SDK.

1. Получает компонент pipeline с именем "chat_completion_pipeline" из реестра.

1. Определяет задание pipeline с помощью декоратора `@pipeline` и функции `create_pipeline`. Имя pipeline задаётся значением `pipeline_display_name`.

1. Внутри функции `create_pipeline` инициализируется полученный компонент pipeline с различными параметрами, включая путь к модели, вычислительные кластеры для разных этапов, разделы данных для обучения и тестирования, количество GPU для тонкой настройки и прочие параметры тонкой настройки.

1. Отображает вывод задания тонкой настройки как вывод задания pipeline. Это сделано для удобной регистрации дообученной модели, что требуется для её развертывания на онлайн или пакетной конечной точке.

1. Создаётся экземпляр pipeline вызовом функции `create_pipeline`.

1. Устанавливается настройка `force_rerun` pipeline в значение `True`, что означает, что кэшированные результаты предыдущих заданий использоваться не будут.

1. Устанавливается настройка `continue_on_step_failure` pipeline в значение `False`, то есть pipeline остановится при сбое любого этапа.

1. В итоге, скрипт определяет и настраивает pipeline машинного обучения для задачи с чат-запросами, используя Azure Machine Learning SDK.

    ```python
    # Импорт необходимых модулей из SDK Azure AI ML
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Получить компонент конвейера с именем "chat_completion_pipeline" из реестра
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Определить задачу конвейера с помощью декоратора @pipeline и функции create_pipeline
    # Имя конвейера установлено в pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Инициализировать полученный компонент конвейера с различными параметрами
        # К ним относятся путь к модели, вычислительные кластеры для разных этапов, разделы датасета для обучения и тестирования, количество GPU для тонкой настройки и другие параметры тонкой настройки
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Отобразить разделы датасета на параметры
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Настройки обучения
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Установлено в количество доступных GPU в вычислительном кластере
            **finetune_parameters
        )
        return {
            # Отобразить вывод задачи тонкой настройки на вывод задачи конвейера
            # Это делается для того, чтобы мы могли легко зарегистрировать тонко настроенную модель
            # Регистрация модели необходима для развертывания модели в онлайн или пакетной конечной точке
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Создать экземпляр конвейера, вызвав функцию create_pipeline
    pipeline_object = create_pipeline()
    
    # Не использовать кэшированные результаты предыдущих задач
    pipeline_object.settings.force_rerun = True
    
    # Установить продолжение при ошибке шага в False
    # Это означает, что конвейер остановится, если какой-либо шаг завершится с ошибкой
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Отправка задания

1. Этот скрипт Python отправляет задание pipeline машинного обучения в рабочее пространство Azure Machine Learning и затем ожидает завершения задания. Вот что происходит:

    - Вызывается метод create_or_update объекта jobs клиента workspace_ml_client для отправки pipeline-задания. Pipeline, который нужно выполнить, указан в pipeline_object, а эксперимент для запуска задания — в experiment_name.

    - Затем вызывается метод stream объекта jobs клиента workspace_ml_client для ожидания завершения pipeline-задания. Задание, за которым следят, указано в атрибуте name объекта pipeline_job.

    - В итогe, скрипт отправляет pipeline-задание в рабочее пространство Azure Machine Learning и ожидает его завершения.

    ```python
    # Отправить задачу конвейера в рабочую область Azure Machine Learning
    # Конвейер для выполнения указан объектом pipeline_object
    # Эксперимент, под которым запускается задача, указан именем experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Ожидать завершения задачи конвейера
    # Задача для ожидания указана в атрибуте name объекта pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Регистрация дообученной модели в рабочем пространстве

Мы зарегистрируем модель из вывода задания тонкой настройки. Это позволит отследить происхождение между дообученной моделью и заданием тонкой настройки. Задание тонкой настройки, в свою очередь, отслеживает происхождение основной модели, данных и кода обучения.

### Регистрация ML-модели

1. Этот скрипт Python регистрирует модель машинного обучения, обученную в Azure Machine Learning pipeline. Вот что происходит:

    - Импортируются необходимые модули из Azure AI ML SDK.

    - Проверяется наличие вывода trained_model от pipeline-задания, вызывая метод get объекта jobs клиента workspace_ml_client и обращаясь к атрибуту outputs.

    - Формируется путь к обученной модели, форматируя строку с названием pipeline-задания и названием вывода ("trained_model").

    - Определяется имя для дообученной модели, добавляя суффикс "-ultrachat-200k" к исходному имени модели и заменяя все слеши на дефисы.

    - Готовится регистрация модели, создавая объект Model с разными параметрами, включая путь к модели, тип модели (MLflow модель), имя и версию модели, а также описание модели.

    - Регистрируется модель вызовом метода create_or_update объекта models клиента workspace_ml_client с объектом Model.

    - Выводится зарегистрированная модель.

1. В итоге, скрипт регистрирует модель машинного обучения, обученную в pipeline Azure Machine Learning.

    ```python
    # Импортировать необходимые модули из Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Проверить, доступен ли вывод `trained_model` из задания конвейера
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Построить путь к обученной модели, форматируя строку с именем задания конвейера и именем вывода ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Определить имя для дообученной модели, добавив "-ultrachat-200k" к исходному имени модели и заменив все слэши на дефисы
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Подготовиться к регистрации модели, создав объект Model с различными параметрами
    # Они включают путь к модели, тип модели (MLflow model), имя и версию модели, а также описание модели
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Использовать метку времени в качестве версии, чтобы избежать конфликта версий
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Зарегистрировать модель, вызвав метод create_or_update объекта models в workspace_ml_client с объектом Model в качестве аргумента
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Вывести зарегистрированную модель на печать
    print("registered model: \n", registered_model)
    ```

## 7. Развертывание дообученной модели на онлайн конечной точке

Онлайн конечные точки предоставляют долговременный REST API, который можно использовать для интеграции с приложениями, которым нужна модель.

### Управление конечной точкой

1. Этот скрипт Python создаёт управляемую онлайн конечную точку в Azure Machine Learning для зарегистрированной модели. Вот что происходит:

    - Импортируются необходимые модули из Azure AI ML SDK.

    - Определяется уникальное имя онлайн конечной точки, добавляя временную метку к строке "ultrachat-completion-".

    - Готовится создание конечной точки, создавая объект ManagedOnlineEndpoint с параметрами, включая имя конечной точки, описание и режим аутентификации ("key").

    - Создаётся онлайн конечная точка вызовом метода begin_create_or_update клиента workspace_ml_client с объектом ManagedOnlineEndpoint, после чего ожидается завершение операции вызовом метода wait.

1. В итогe скрипт создаёт управляемую онлайн конечную точку в Azure Machine Learning для зарегистрированной модели.

    ```python
    # Импортировать необходимые модули из Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Определить уникальное имя для онлайн-конечного пункта, добавив метку времени к строке "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Подготовиться к созданию онлайн-конечного пункта, создав объект ManagedOnlineEndpoint с различными параметрами
    # Включая имя конечного пункта, описание конечного пункта и режим аутентификации ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Создать онлайн-конечный пункт, вызвав метод begin_create_or_update у workspace_ml_client с объектом ManagedOnlineEndpoint в качестве аргумента
    # Затем дождаться завершения операции создания, вызвав метод wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Здесь вы можете найти список поддерживаемых SKU для развертывания — [Список SKU управляемых онлайн конечных точек](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Развертывание ML-модели

1. Этот скрипт Python развертывает зарегистрированную модель машинного обучения на управляемой онлайн конечной точке в Azure Machine Learning. Вот что происходит:

    - Импортируется модуль ast, предоставляющий функции для обработки деревьев абстрактного синтактического дерева Python.

    - Устанавливается тип экземпляра для развертывания — "Standard_NC6s_v3".

    - Проверяется наличие тега inference_compute_allow_list в основной модели. Если тег есть, его значение конвертируется из строки в список Python и присваивается переменной inference_computes_allow_list. Если нет — переменная устанавливается в None.

    - Проверяется, входит ли указанный тип экземпляра в список разрешённых. Если нет, выводится сообщение с просьбой выбрать тип из разрешённого списка.

    - Готовится создание развертывания, создавая объект ManagedOnlineDeployment с параметрами, включая имя развертывания, имя конечной точки, ID модели, тип и количество экземпляров, настройки проверки живучести и настройки запросов.

    - Создаётся развертывание вызовом метода begin_create_or_update клиента workspace_ml_client с объектом ManagedOnlineDeployment, после чего ожидается завершение вызовом wait.

    - Трафик конечной точки направляется на 100% к развертыванию с именем "demo".

    - Обновляется конечная точка вызовом begin_create_or_update клиента workspace_ml_client с объектом endpoint, после чего ожидается завершение вызовом result.

1. В итоге, скрипт развертывает зарегистрированную модель машинного обучения на управляемой онлайн конечной точке Azure Machine Learning.

    ```python
    # Импортируйте модуль ast, который предоставляет функции для обработки деревьев абстрактного синтаксиса Python
    import ast
    
    # Установите тип экземпляра для развертывания
    instance_type = "Standard_NC6s_v3"
    
    # Проверьте, присутствует ли тег `inference_compute_allow_list` в базовой модели
    if "inference_compute_allow_list" in foundation_model.tags:
        # Если да, преобразуйте значение тега из строки в список Python и присвойте его `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Если нет, установите `inference_computes_allow_list` в значение `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Проверьте, находится ли указанный тип экземпляра в списке разрешенных
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Подготовьтесь к созданию развертывания, создав объект `ManagedOnlineDeployment` с различными параметрами
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Создайте развертывание, вызвав метод `begin_create_or_update` у `workspace_ml_client` с объектом `ManagedOnlineDeployment` в качестве аргумента
    # Затем дождитесь завершения операции создания, вызвав метод `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Установите трафик конечной точки так, чтобы 100% трафика направлялось на развертывание "demo"
    endpoint.traffic = {"demo": 100}
    
    # Обновите конечную точку, вызвав метод `begin_create_or_update` у `workspace_ml_client` с объектом `endpoint` в качестве аргумента
    # Затем дождитесь завершения операции обновления, вызвав метод `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Тестирование конечной точки с примерными данными

Мы возьмём некоторые примерные данные из тестового набора и отправим их на онлайн конечную точку для инференса. Затем покажем предсказанные метки вместе с метками истинных значений.

### Чтение результатов

1. Этот скрипт Python читает файл формата JSON Lines в pandas DataFrame, берёт случайную выборку и сбрасывает индекс. Вот что происходит:

    - Считывает файл ./ultrachat_200k_dataset/test_gen.jsonl в pandas DataFrame. Для чтения используется функция read_json с параметром lines=True, так как файл в формате JSON Lines.

    - Берёт случайную выборку из 1 строки DataFrame. Для этого используется функция sample с параметром n=1.

    - Сбрасывает индекс DataFrame. Для этого вызывается reset_index с параметром drop=True, чтобы удалить старый индекс и заменить его новым с целочисленными значениями.

    - Отображает первые 2 строки DataFrame с помощью функции head с аргументом 2. Однако, поскольку после выборки DataFrame содержит одну строку, будет показана только она.

1. Итого, скрипт читает файл JSON Lines в pandas DataFrame, берёт случайную выборку из одной строки, сбрасывает индекс и отображает первую строку.

    ```python
    # Импортировать библиотеку pandas
    import pandas as pd
    
    # Прочитать файл JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' в DataFrame pandas
    # Аргумент 'lines=True' указывает, что файл в формате JSON Lines, где каждая строка является отдельным JSON объектом
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Взять случайную выборку из 1 строки из DataFrame
    # Аргумент 'n=1' задает количество случайных строк для выбора
    test_df = test_df.sample(n=1)
    
    # Сбросить индекс DataFrame
    # Аргумент 'drop=True' указывает, что исходный индекс следует удалить и заменить новым индексом с целочисленными значениями по умолчанию
    # Аргумент 'inplace=True' указывает, что DataFrame должен быть изменен на месте (без создания нового объекта)
    test_df.reset_index(drop=True, inplace=True)
    
    # Отобразить первые 2 строки DataFrame
    # Однако, поскольку в DataFrame после выборки содержится только одна строка, будет отображена только эта одна строка
    test_df.head(2)
    ```

### Создание JSON объекта

1. Этот скрипт Python создает JSON-объект с определёнными параметрами и сохраняет его в файл. Вот что он делает:

    - Импортирует модуль json, который предоставляет функции для работы с JSON-данными.
    - Он создает словарь parameters с ключами и значениями, представляющими параметры для модели машинного обучения. Ключи — "temperature", "top_p", "do_sample" и "max_new_tokens", а соответствующие значения — 0.6, 0.9, True и 200 соответственно.

    - Он создает еще один словарь test_json с двумя ключами: "input_data" и "params". Значение "input_data" — это другой словарь с ключами "input_string" и "parameters". Значение "input_string" — это список, содержащий первое сообщение из DataFrame test_df. Значение "parameters" — это словарь parameters, созданный ранее. Значение "params" — это пустой словарь.

    - Он открывает файл с именем sample_score.json
    
    ```python
    # Импортировать модуль json, который предоставляет функции для работы с данными в формате JSON
    import json
    
    # Создать словарь `parameters` с ключами и значениями, представляющими параметры модели машинного обучения
    # Ключи — "temperature", "top_p", "do_sample" и "max_new_tokens", а соответствующие значения — 0.6, 0.9, True и 200 соответственно
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Создать другой словарь `test_json` с двумя ключами: "input_data" и "params"
    # Значение "input_data" — это другой словарь с ключами "input_string" и "parameters"
    # Значение "input_string" — список, содержащий первое сообщение из DataFrame `test_df`
    # Значение "parameters" — словарь `parameters`, созданный ранее
    # Значение "params" — пустой словарь
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Открыть файл с именем `sample_score.json` в директории `./ultrachat_200k_dataset` в режиме записи
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Записать словарь `test_json` в файл в формате JSON с помощью функции `json.dump`
        json.dump(test_json, f)
    ```

### Вызов конечной точки

1. Этот Python-скрипт вызывает онлайн-конечную точку в Azure Machine Learning для оценки JSON-файла. Вот разбор того, что он делает:

    - Он вызывает метод invoke свойства online_endpoints объекта workspace_ml_client. Этот метод используется для отправки запроса на онлайн-конечную точку и получения ответа.

    - Он указывает имя конечной точки и развертывание с помощью аргументов endpoint_name и deployment_name. В данном случае имя конечной точки хранится в переменной online_endpoint_name, а имя развертывания — "demo".

    - Он указывает путь к JSON-файлу для оценки с помощью аргумента request_file. В данном случае файл — ./ultrachat_200k_dataset/sample_score.json.

    - Он сохраняет ответ от конечной точки в переменную response.

    - Он выводит необработанный ответ.

1. В итоге этот скрипт вызывает онлайн-конечную точку в Azure Machine Learning для оценки JSON-файла и выводит ответ.

    ```python
    # Вызовите онлайн-эндпоинт в Azure Machine Learning для оценки файла `sample_score.json`
    # Метод `invoke` свойства `online_endpoints` объекта `workspace_ml_client` используется для отправки запроса на онлайн-эндпоинт и получения ответа
    # Аргумент `endpoint_name` указывает имя эндпоинта, которое хранится в переменной `online_endpoint_name`
    # Аргумент `deployment_name` указывает имя развертывания, которое равно "demo"
    # Аргумент `request_file` указывает путь к JSON-файлу для оценки, который равен `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Вывести необработанный ответ от эндпоинта
    print("raw response: \n", response, "\n")
    ```

## 9. Удаление онлайн-конечной точки

1. Не забудьте удалить онлайн-конечную точку, иначе счетчик оплаты будет продолжать работать за вычислительные ресурсы, используемые конечной точкой. Эта строка Python-кода удаляет онлайн-конечную точку в Azure Machine Learning. Вот разбор того, что она делает:

    - Она вызывает метод begin_delete свойства online_endpoints объекта workspace_ml_client. Этот метод используется для начала удаления онлайн-конечной точки.

    - Она указывает имя конечной точки, которую нужно удалить, с помощью аргумента name. В данном случае имя конечной точки хранится в переменной online_endpoint_name.

    - Она вызывает метод wait, чтобы дождаться завершения операции удаления. Это блокирующая операция, что означает, что скрипт не продолжит выполнение, пока удаление не будет завершено.

    - В итоге эта строка кода начинает удаление онлайн-конечной точки в Azure Machine Learning и ждет завершения операции.

    ```python
    # Удалить онлайн-конечную точку в Azure Machine Learning
    # Метод `begin_delete` свойства `online_endpoints` объекта `workspace_ml_client` используется для начала удаления онлайн-конечной точки
    # Аргумент `name` указывает имя конечной точки для удаления, которое хранится в переменной `online_endpoint_name`
    # Вызван метод `wait` для ожидания завершения операции удаления. Это блокирующая операция, означающая, что скрипт не продолжит выполнение, пока удаление не завершится
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью автоматического сервиса перевода ИИ [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->