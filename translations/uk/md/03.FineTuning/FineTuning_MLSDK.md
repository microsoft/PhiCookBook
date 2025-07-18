<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:54:36+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "uk"
}
-->
## Як використовувати компоненти chat-completion із системного реєстру Azure ML для донавчання моделі

У цьому прикладі ми проведемо донавчання моделі Phi-3-mini-4k-instruct для завершення розмови між двома людьми, використовуючи датасет ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.uk.png)

Приклад покаже, як виконати донавчання за допомогою Azure ML SDK і Python, а потім розгорнути донавчену модель на онлайн-ендпоінті для інференсу в реальному часі.

### Дані для навчання

Ми використаємо датасет ultrachat_200k. Це сильно відфільтрована версія датасету UltraChat, яка використовувалась для навчання Zephyr-7B-β — передової чат-моделі з 7 млрд параметрів.

### Модель

Ми використаємо модель Phi-3-mini-4k-instruct, щоб показати, як користувач може донавчити модель для задачі chat-completion. Якщо ви відкрили цей ноутбук із конкретної картки моделі, не забудьте замінити назву моделі на відповідну.

### Завдання

- Обрати модель для донавчання.
- Обрати та дослідити дані для навчання.
- Налаштувати завдання донавчання.
- Запустити завдання донавчання.
- Переглянути метрики навчання та оцінки.
- Зареєструвати донавчену модель.
- Розгорнути донавчену модель для інференсу в реальному часі.
- Очистити ресурси.

## 1. Налаштування передумов

- Встановити залежності
- Підключитися до AzureML Workspace. Детальніше дивіться у розділі налаштування автентифікації SDK. Замініть <WORKSPACE_NAME>, <RESOURCE_GROUP> та <SUBSCRIPTION_ID> нижче.
- Підключитися до системного реєстру azureml
- Встановити необов’язкову назву експерименту
- Перевірити або створити обчислювальний ресурс.

> [!NOTE]
> Вимоги: один вузол GPU може містити кілька графічних карт. Наприклад, у вузлі Standard_NC24rs_v3 є 4 NVIDIA V100 GPU, а у Standard_NC12s_v3 — 2 NVIDIA V100 GPU. Детальніше дивіться у документації. Кількість GPU на вузол задається параметром gpus_per_node нижче. Правильне встановлення цього значення забезпечить використання всіх GPU у вузлі. Рекомендовані SKU для GPU-комп’ютерів можна знайти тут і тут.

### Бібліотеки Python

Встановіть залежності, виконавши наступну клітинку. Це не опційний крок, якщо ви працюєте в новому середовищі.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Взаємодія з Azure ML

1. Цей Python-скрипт використовується для взаємодії з сервісом Azure Machine Learning (Azure ML). Ось що він робить:

    - Імпортує необхідні модулі з пакетів azure.ai.ml, azure.identity та azure.ai.ml.entities. Також імпортує модуль time.

    - Прагне автентифікуватися за допомогою DefaultAzureCredential(), що забезпечує спрощений спосіб автентифікації для швидкого початку розробки додатків у хмарі Azure. Якщо це не вдається, переходить до InteractiveBrowserCredential(), який відкриває інтерактивний вхід через браузер.

    - Потім намагається створити екземпляр MLClient за допомогою методу from_config, який зчитує конфігурацію з файлу config.json. Якщо це не вдається, створює MLClient вручну, передаючи subscription_id, resource_group_name та workspace_name.

    - Створює ще один екземпляр MLClient для системного реєстру Azure ML з назвою "azureml". Саме тут зберігаються моделі, пайплайни донавчання та середовища.

    - Встановлює назву експерименту "chat_completion_Phi-3-mini-4k-instruct".

    - Генерує унікальний часовий штамп, конвертуючи поточний час (у секундах з початку епохи) у ціле число, а потім у рядок. Цей штамп можна використовувати для створення унікальних імен і версій.

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

## 2. Обрати базову модель для донавчання

1. Phi-3-mini-4k-instruct — це легка, передова відкрита модель з 3.8 млрд параметрів, побудована на основі датасетів, які використовувалися для Phi-2. Модель належить до сімейства Phi-3, а версія Mini має два варіанти: 4K і 128K — це довжина контексту (у токенах), яку вона підтримує. Для використання моделі під наші цілі її потрібно донавчити. Ви можете переглянути ці моделі в Каталозі моделей AzureML Studio, відфільтрувавши за завданням chat-completion. У цьому прикладі ми використовуємо модель Phi-3-mini-4k-instruct. Якщо ви відкрили цей ноутбук для іншої моделі, замініть назву та версію моделі відповідно.

    > [!NOTE]
    > властивість model id моделі. Вона передається як вхідний параметр до завдання донавчання. Також доступна як поле Asset ID на сторінці деталей моделі в Каталозі моделей AzureML Studio.

2. Цей Python-скрипт взаємодіє з сервісом Azure Machine Learning (Azure ML). Ось що він робить:

    - Встановлює model_name як "Phi-3-mini-4k-instruct".

    - Використовує метод get об’єкта models реєстру registry_ml_client, щоб отримати останню версію моделі з вказаною назвою з реєстру Azure ML. Метод get викликається з двома аргументами: назвою моделі та міткою, що вказує на отримання останньої версії.

    - Виводить у консоль повідомлення з назвою, версією та id моделі, яка буде використана для донавчання. Метод format рядка вставляє ці значення у повідомлення. Назва, версія та id моделі доступні як властивості об’єкта foundation_model.

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

## 3. Створити обчислювальний ресурс для завдання

Завдання донавчання працює ЛИШЕ з GPU-комп’ютерами. Розмір обчислювального ресурсу залежить від розміру моделі, і часто буває складно підібрати правильний ресурс. У цій клітинці ми допомагаємо користувачу обрати відповідний ресурс.

> [!NOTE]
> Нижче наведені обчислювальні ресурси працюють з оптимальною конфігурацією. Будь-які зміни можуть призвести до помилки Cuda Out Of Memory. У таких випадках спробуйте збільшити розмір обчислювального ресурсу.

> [!NOTE]
> При виборі compute_cluster_size переконайтеся, що обчислювальний ресурс доступний у вашій групі ресурсів. Якщо потрібний ресурс недоступний, можна подати запит на доступ до нього.

### Перевірка підтримки донавчання моделі

1. Цей Python-скрипт взаємодіє з моделлю Azure Machine Learning (Azure ML). Ось що він робить:

    - Імпортує модуль ast, який надає функції для обробки дерев абстрактного синтаксису Python.

    - Перевіряє, чи має об’єкт foundation_model (модель у Azure ML) тег finetune_compute_allow_list. Теги в Azure ML — це пари ключ-значення, які можна створювати для фільтрації та сортування моделей.

    - Якщо тег finetune_compute_allow_list присутній, він безпечно розбирає його значення (рядок) у список Python за допомогою ast.literal_eval. Цей список присвоюється змінній computes_allow_list. Потім виводить повідомлення, що обчислювальний ресурс слід створювати зі списку.

    - Якщо тег відсутній, встановлює computes_allow_list у None і виводить повідомлення, що тег finetune_compute_allow_list не входить до тегів моделі.

    - Загалом, цей скрипт перевіряє наявність певного тегу в метаданих моделі, конвертує його значення у список, якщо він існує, і надає відповідний зворотний зв’язок користувачу.

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

### Перевірка обчислювального інстансу

1. Цей Python-скрипт взаємодіє з сервісом Azure Machine Learning (Azure ML) і виконує кілька перевірок обчислювального інстансу. Ось що він робить:

    - Прагне отримати обчислювальний інстанс з назвою, що зберігається в compute_cluster, з робочого простору Azure ML. Якщо стан провізії інстансу "failed", викликає ValueError.

    - Перевіряє, чи змінна computes_allow_list не є None. Якщо ні, конвертує всі розміри обчислювальних ресурсів у списку в нижній регістр і перевіряє, чи розмір поточного інстансу є у списку. Якщо ні — викликає ValueError.

    - Якщо computes_allow_list дорівнює None, перевіряє, чи розмір інстансу входить до списку непідтримуваних GPU VM розмірів. Якщо так — викликає ValueError.

    - Отримує список усіх доступних розмірів обчислювальних ресурсів у робочому просторі. Ітерує цей список, і для кожного розміру перевіряє, чи співпадає його назва з розміром поточного інстансу. Якщо так, отримує кількість GPU для цього розміру і встановлює gpu_count_found у True.

    - Якщо gpu_count_found дорівнює True, виводить кількість GPU в інстансі. Якщо ні — викликає ValueError.

    - Загалом, цей скрипт виконує кілька перевірок обчислювального інстансу в робочому просторі Azure ML, включно зі станом провізії, розміром щодо дозволеного списку або забороненого списку, а також кількістю GPU.

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

## 4. Обрати датасет для донавчання моделі

1. Ми використовуємо датасет ultrachat_200k. Датасет має чотири розділи, придатні для Supervised fine-tuning (sft).
Generation ranking (gen). Кількість прикладів у кожному розділі наведена нижче:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Наступні кілька клітинок показують базову підготовку даних для донавчання:

### Візуалізація деяких рядків даних

Ми хочемо, щоб цей приклад працював швидко, тому збережемо файли train_sft, test_sft, що містять 5% вже відфільтрованих рядків. Це означає, що донавчена модель матиме нижчу точність, тому її не слід використовувати у реальних застосунках.
Скрипт download-dataset.py використовується для завантаження датасету ultrachat_200k і перетворення його у формат, придатний для компонента пайплайну донавчання. Оскільки датасет великий, тут наведена лише частина датасету.

1. Запуск наведеного нижче скрипта завантажує лише 5% даних. Цей відсоток можна збільшити, змінивши параметр dataset_split_pc на потрібне значення.

    > [!NOTE]
    > Деякі мовні моделі мають різні коди мов, тому назви колонок у датасеті мають відповідати цим кодам.

1. Ось приклад того, як мають виглядати дані.
Датасет chat-completion зберігається у форматі parquet, кожен запис має таку схему:

    - Це JSON (JavaScript Object Notation) документ — популярний формат обміну даними. Це не виконуваний код, а спосіб зберігання і передачі даних. Ось структура:

    - "prompt": ключ, що містить рядок із завданням або питанням, поставленим AI-асистенту.

    - "messages": ключ, що містить масив об’єктів. Кожен об’єкт — це повідомлення у розмові між користувачем і AI-асистентом. Кожне повідомлення має два ключі:

    - "content": рядок із текстом повідомлення.
    - "role": рядок, що вказує роль відправника повідомлення — "user" або "assistant".
    - "prompt_id": рядок, що є унікальним ідентифікатором запиту.

1. У цьому конкретному JSON-документі представлена розмова, де користувач просить AI-асистента створити головного героя для дистопічної історії. Асистент відповідає, а користувач просить більше деталей. Асистент погоджується надати додаткову інформацію. Вся розмова пов’язана з конкретним prompt_id.

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

### Завантаження даних

1. Цей Python-скрипт використовується для завантаження датасету за допомогою допоміжного скрипта download-dataset.py. Ось що він робить:

    - Імпортує модуль os, який надає портативний доступ до функцій операційної системи.

    - Використовує os.system для запуску скрипта download-dataset.py у shell з певними аргументами командного рядка. Аргументи вказують, який датасет завантажувати (HuggingFaceH4/ultrachat_200k), куди його зберігати (ultrachat_200k_dataset) і який відсоток датасету завантажувати (5). os.system повертає код завершення команди, який зберігається у змінній exit_status.

    - Перевіряє, чи exit_status не дорівнює 0. У Unix-подібних системах код 0 означає успішне виконання, інші значення — помилку. Якщо exit_status не 0, викликає Exception з повідомленням про помилку завантаження датасету.

    - Загалом, цей скрипт запускає команду для завантаження датасету за допомогою допоміжного скрипта і викликає помилку, якщо команда не вдалася.

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

### Завантаження даних у DataFrame

1. Цей Python-скрипт завантажує файл у форматі JSON Lines у pandas DataFrame і виводить перші 5 рядків. Ось що він робить:

    - Імпортує бібліотеку pandas, потужний інструмент для обробки та аналізу даних.

    - Встановлює максимальну ширину колонки для відображення pandas у 0, що означає повне відображення тексту без обрізання.

    - Використовує функцію pd.read_json для завантаження файлу train_sft.jsonl з директорії ultrachat_200k_dataset у DataFrame. Параметр lines=True вказує, що файл у форматі JSON Lines, де кожен рядок — окремий JSON-об’єкт.
- Він використовує метод head, щоб показати перші 5 рядків DataFrame. Якщо у DataFrame менше 5 рядків, він покаже всі.

- Підсумовуючи, цей скрипт завантажує файл у форматі JSON Lines у DataFrame і відображає перші 5 рядків з повним текстом стовпців.

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

## 5. Надіслати завдання тонкого налаштування, використовуючи модель і дані як вхідні параметри

Створіть завдання, яке використовує компонент pipeline для chat-completion. Дізнайтеся більше про всі параметри, які підтримуються для тонкого налаштування.

### Визначення параметрів тонкого налаштування

1. Параметри тонкого налаштування можна поділити на 2 категорії — параметри навчання та параметри оптимізації.

1. Параметри навчання визначають аспекти тренування, такі як:

    - Оптимізатор, scheduler, який буде використовуватися
    - Метрика для оптимізації тонкого налаштування
    - Кількість кроків навчання, розмір батчу тощо
    - Параметри оптимізації допомагають оптимізувати використання пам’яті GPU та ефективно використовувати обчислювальні ресурси.

1. Нижче наведено кілька параметрів, що належать до цієї категорії. Параметри оптимізації відрізняються для кожної моделі і постачаються разом із моделлю для врахування цих відмінностей.

    - Увімкнення deepspeed та LoRA
    - Увімкнення навчання з мішаною точністю
    - Увімкнення навчання на кількох вузлах


> [!NOTE]
> Навчання з наглядом може призвести до втрати узгодженості або катастрофічного забування. Рекомендуємо перевірити цю проблему та виконати етап узгодження після тонкого налаштування.

### Параметри тонкого налаштування

1. Цей Python-скрипт налаштовує параметри для тонкого налаштування моделі машинного навчання. Ось що він робить:

    - Встановлює стандартні параметри навчання, такі як кількість епох, розмір батчів для навчання та оцінки, швидкість навчання та тип scheduler для швидкості навчання.

    - Встановлює стандартні параметри оптимізації, такі як застосування Layer-wise Relevance Propagation (LoRa) та DeepSpeed, а також стадію DeepSpeed.

    - Об’єднує параметри навчання та оптимізації в один словник finetune_parameters.

    - Перевіряє, чи має foundation_model якісь специфічні для моделі стандартні параметри. Якщо так, виводить попередження і оновлює словник finetune_parameters цими параметрами. Функція ast.literal_eval використовується для перетворення рядка з параметрами у словник Python.

    - Виводить остаточний набір параметрів тонкого налаштування, які будуть використані під час запуску.

    - Підсумовуючи, цей скрипт налаштовує і відображає параметри для тонкого налаштування моделі машинного навчання з можливістю заміни стандартних параметрів специфічними для моделі.

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

### Навчальний pipeline

1. Цей Python-скрипт визначає функцію для генерації відображуваного імені для навчального pipeline машинного навчання, а потім викликає цю функцію для генерації і виводить це ім’я. Ось що він робить:

1. Визначена функція get_pipeline_display_name, яка генерує відображуване ім’я на основі різних параметрів, пов’язаних з навчальним pipeline.

1. Усередині функції обчислюється загальний розмір батчу шляхом множення розміру батчу на пристрій, кількості кроків накопичення градієнта, кількості GPU на вузол і кількості вузлів, що використовуються для тонкого налаштування.

1. Отримуються інші параметри, такі як тип scheduler для швидкості навчання, чи застосовується DeepSpeed, стадія DeepSpeed, чи застосовується Layer-wise Relevance Propagation (LoRa), обмеження на кількість збережених контрольних точок моделі та максимальна довжина послідовності.

1. Формується рядок, що включає всі ці параметри, розділені дефісами. Якщо застосовується DeepSpeed або LoRa, рядок містить "ds" з номером стадії DeepSpeed або "lora" відповідно. Якщо ні — "nods" або "nolora" відповідно.

1. Функція повертає цей рядок, який слугує відображуваним ім’ям для навчального pipeline.

1. Після визначення функції вона викликається для генерації відображуваного імені, яке потім виводиться.

1. Підсумовуючи, цей скрипт генерує відображуване ім’я для навчального pipeline машинного навчання на основі різних параметрів і виводить його.

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

### Налаштування pipeline

Цей Python-скрипт визначає та налаштовує pipeline машинного навчання за допомогою Azure Machine Learning SDK. Ось що він робить:

1. Імпортує необхідні модулі з Azure AI ML SDK.

1. Отримує компонент pipeline з реєстру з ім’ям "chat_completion_pipeline".

1. Визначає pipeline job за допомогою декоратора `@pipeline` та функції `create_pipeline`. Ім’я pipeline встановлено як `pipeline_display_name`.

1. Усередині функції `create_pipeline` ініціалізує отриманий компонент pipeline з різними параметрами, включно з шляхом до моделі, обчислювальними кластерами для різних етапів, розподілом датасету для навчання та тестування, кількістю GPU для тонкого налаштування та іншими параметрами тонкого налаштування.

1. Відповідь fine-tuning job відображається як вихід pipeline job, щоб тонко налаштована модель могла бути легко зареєстрована, що необхідно для розгортання моделі на онлайн або пакетному endpoint.

1. Створює екземпляр pipeline, викликаючи функцію `create_pipeline`.

1. Встановлює параметр `force_rerun` pipeline в `True`, що означає, що кешовані результати попередніх завдань не будуть використовуватися.

1. Встановлює параметр `continue_on_step_failure` pipeline в `False`, що означає, що pipeline зупиниться, якщо якийсь крок зазнає невдачі.

1. Підсумовуючи, цей скрипт визначає та налаштовує pipeline машинного навчання для задачі chat completion за допомогою Azure Machine Learning SDK.

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

### Надіслати завдання

1. Цей Python-скрипт надсилає завдання pipeline машинного навчання до робочого простору Azure Machine Learning і чекає на завершення завдання. Ось що він робить:

    - Викликає метод create_or_update об’єкта jobs у workspace_ml_client для надсилання pipeline job. Pipeline, який потрібно виконати, вказаний у pipeline_object, а експеримент, під яким запускається завдання, — у experiment_name.

    - Потім викликає метод stream об’єкта jobs у workspace_ml_client, щоб чекати на завершення pipeline job. Завдання, на яке чекають, визначається атрибутом name об’єкта pipeline_job.

    - Підсумовуючи, цей скрипт надсилає завдання pipeline машинного навчання до робочого простору Azure Machine Learning і чекає на його завершення.

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

## 6. Зареєструвати тонко налаштовану модель у робочому просторі

Ми зареєструємо модель, отриману на виході завдання тонкого налаштування. Це дозволить відстежувати походження між тонко налаштованою моделлю та завданням тонкого налаштування. Завдання тонкого налаштування, у свою чергу, відстежує походження до базової моделі, даних і коду навчання.

### Реєстрація ML-моделі

1. Цей Python-скрипт реєструє модель машинного навчання, яка була навчена в pipeline Azure Machine Learning. Ось що він робить:

    - Імпортує необхідні модулі з Azure AI ML SDK.

    - Перевіряє, чи доступний вихід trained_model з pipeline job, викликаючи метод get об’єкта jobs у workspace_ml_client і звертаючись до атрибуту outputs.

    - Формує шлях до навченої моделі, форматуючи рядок з ім’ям pipeline job та ім’ям виходу ("trained_model").

    - Визначає ім’я для тонко налаштованої моделі, додаючи "-ultrachat-200k" до оригінального імені моделі та замінюючи всі слеші на дефіси.

    - Готується до реєстрації моделі, створюючи об’єкт Model з різними параметрами, включно з шляхом до моделі, типом моделі (MLflow model), ім’ям і версією моделі, а також описом.

    - Реєструє модель, викликаючи метод create_or_update об’єкта models у workspace_ml_client з об’єктом Model як аргументом.

    - Виводить зареєстровану модель.

1. Підсумовуючи, цей скрипт реєструє модель машинного навчання, яка була навчена в pipeline Azure Machine Learning.

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

## 7. Розгорнути тонко налаштовану модель на онлайн endpoint

Онлайн endpoint надають надійний REST API, який можна використовувати для інтеграції з додатками, що потребують використання моделі.

### Керування Endpoint

1. Цей Python-скрипт створює керований онлайн endpoint в Azure Machine Learning для зареєстрованої моделі. Ось що він робить:

    - Імпортує необхідні модулі з Azure AI ML SDK.

    - Визначає унікальне ім’я для онлайн endpoint, додаючи часову позначку до рядка "ultrachat-completion-".

    - Готується створити онлайн endpoint, створюючи об’єкт ManagedOnlineEndpoint з різними параметрами, включно з ім’ям endpoint, описом та режимом автентифікації ("key").

    - Створює онлайн endpoint, викликаючи метод begin_create_or_update об’єкта workspace_ml_client з об’єктом ManagedOnlineEndpoint як аргументом. Потім чекає на завершення операції, викликаючи метод wait.

1. Підсумовуючи, цей скрипт створює керований онлайн endpoint в Azure Machine Learning для зареєстрованої моделі.

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
> Тут ви можете знайти список SKU, які підтримуються для розгортання — [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Розгортання ML-моделі

1. Цей Python-скрипт розгортає зареєстровану модель машинного навчання на керованому онлайн endpoint в Azure Machine Learning. Ось що він робить:

    - Імпортує модуль ast, який надає функції для обробки дерев абстрактного синтаксису Python.

    - Встановлює тип інстансу для розгортання як "Standard_NC6s_v3".

    - Перевіряє, чи присутній тег inference_compute_allow_list у foundation model. Якщо так, конвертує значення тегу з рядка у список Python і присвоює його inference_computes_allow_list. Якщо ні — встановлює inference_computes_allow_list у None.

    - Перевіряє, чи вказаний тип інстансу є у списку дозволених. Якщо ні, виводить повідомлення з проханням вибрати тип інстансу зі списку дозволених.

    - Готується створити розгортання, створюючи об’єкт ManagedOnlineDeployment з різними параметрами, включно з ім’ям розгортання, ім’ям endpoint, ID моделі, типом і кількістю інстансів, налаштуваннями liveness probe та налаштуваннями запитів.

    - Створює розгортання, викликаючи метод begin_create_or_update об’єкта workspace_ml_client з об’єктом ManagedOnlineDeployment як аргументом. Потім чекає на завершення операції, викликаючи метод wait.

    - Встановлює трафік endpoint так, щоб 100% трафіку йшло на розгортання "demo".

    - Оновлює endpoint, викликаючи метод begin_create_or_update об’єкта workspace_ml_client з об’єктом endpoint як аргументом. Потім чекає на завершення оновлення, викликаючи метод result.

1. Підсумовуючи, цей скрипт розгортає зареєстровану модель машинного навчання на керованому онлайн endpoint в Azure Machine Learning.

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

## 8. Тестування endpoint на прикладі даних

Ми візьмемо деякі приклади даних з тестового датасету і надішлемо їх на онлайн endpoint для інференсу. Потім відобразимо отримані оцінені мітки разом із правильними мітками.

### Читання результатів

1. Цей Python-скрипт читає файл у форматі JSON Lines у pandas DataFrame, бере випадкову вибірку і скидає індекс. Ось що він робить:

    - Читає файл ./ultrachat_200k_dataset/test_gen.jsonl у pandas DataFrame. Функція read_json використовується з аргументом lines=True, оскільки файл у форматі JSON Lines, де кожен рядок — окремий JSON-об’єкт.

    - Бере випадкову вибірку з 1 рядка з DataFrame. Функція sample використовується з аргументом n=1, щоб вказати кількість випадкових рядків.

    - Скидає індекс DataFrame. Функція reset_index використовується з аргументом drop=True, щоб видалити оригінальний індекс і замінити його на новий індекс з цілими числами за замовчуванням.

    - Відображає перші 2 рядки DataFrame за допомогою функції head з аргументом 2. Однак, оскільки після вибірки DataFrame містить лише один рядок, буде показано лише цей один рядок.

1. Підсумовуючи, цей скрипт читає файл у форматі JSON Lines у pandas DataFrame, бере випадкову вибірку з 1 рядка, скидає індекс і відображає перший рядок.

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

### Створення JSON-об’єкта

1. Цей Python-скрипт створює JSON-об’єкт з певними параметрами і зберігає його у файл. Ось що він робить:

    - Імпортує модуль json, який надає функції для роботи з JSON-даними.

    - Створює словник parameters з ключами і значеннями, що представляють параметри для моделі машинного навчання. Ключі — "temperature", "top_p", "do_sample" і "max_new_tokens", а відповідні значення — 0.6, 0.9, True і 200.

    - Створює інший словник test_json з двома ключами: "input_data" і "params". Значення "input_data" — це інший словник з ключами "input_string" і "parameters". Значення "input_string" — це список, що містить перше повідомлення з DataFrame test_df. Значення "parameters" — це словник parameters, створений раніше. Значення "params" — порожній словник.
- Відкриває файл з назвою sample_score.json

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

### Виклик кінцевої точки

1. Цей скрипт на Python виконує виклик онлайн кінцевої точки в Azure Machine Learning для оцінки JSON-файлу. Ось що він робить:

    - Викликає метод invoke властивості online_endpoints об'єкта workspace_ml_client. Цей метод використовується для надсилання запиту до онлайн кінцевої точки та отримання відповіді.

    - Вказує ім'я кінцевої точки та розгортання за допомогою аргументів endpoint_name і deployment_name. У цьому випадку ім'я кінцевої точки зберігається у змінній online_endpoint_name, а ім'я розгортання — "demo".

    - Вказує шлях до JSON-файлу для оцінки через аргумент request_file. У цьому випадку файл знаходиться за адресою ./ultrachat_200k_dataset/sample_score.json.

    - Зберігає відповідь від кінцевої точки у змінній response.

    - Виводить сирий результат відповіді.

1. Підсумовуючи, цей скрипт виконує виклик онлайн кінцевої точки в Azure Machine Learning для оцінки JSON-файлу та виводить отриману відповідь.

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

## 9. Видалення онлайн кінцевої точки

1. Не забудьте видалити онлайн кінцеву точку, інакше ви залишите працюючий лічильник оплати за ресурси, які використовує кінцева точка. Цей рядок коду на Python видаляє онлайн кінцеву точку в Azure Machine Learning. Ось що він робить:

    - Викликає метод begin_delete властивості online_endpoints об'єкта workspace_ml_client. Цей метод запускає процес видалення онлайн кінцевої точки.

    - Вказує ім'я кінцевої точки, яку потрібно видалити, через аргумент name. У цьому випадку ім'я кінцевої точки зберігається у змінній online_endpoint_name.

    - Викликає метод wait, щоб дочекатися завершення операції видалення. Це блокуюча операція, тобто скрипт не продовжить виконання, поки видалення не завершиться.

    - Підсумовуючи, цей рядок коду запускає видалення онлайн кінцевої точки в Azure Machine Learning і чекає на завершення операції.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.