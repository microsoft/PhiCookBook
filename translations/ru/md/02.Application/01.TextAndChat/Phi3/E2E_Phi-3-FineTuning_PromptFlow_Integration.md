# Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt flow

Этот end-to-end (E2E) пример основан на руководстве "[Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow: пошаговое руководство](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community. В нем представлены процессы тонкой настройки, развертывания и интеграции пользовательских моделей Phi-3 с Prompt flow.

## Обзор

В этом E2E примере вы узнаете, как тонко настроить модель Phi-3 и интегрировать ее с Prompt flow. Используя Azure Machine Learning и Prompt flow, вы создадите рабочий процесс для развертывания и использования пользовательских AI-моделей. Этот E2E пример разделен на три сценария:

**Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке**

**Сценарий 2: Тонкая настройка модели Phi-3 и развертывание в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и общение с вашей пользовательской моделью**

Вот обзор этого E2E примера.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/ru/00-01-architecture.02fc569e266d468c.webp)

### Содержание

1. **[Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Создание Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Запрос лимитов GPU в подписке Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Добавление назначения ролей](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Настройка проекта](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Подготовка набора данных для тонкой настройки](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 2: Тонкая настройка модели Phi-3 и развертывание в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Настройка Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Тонкая настройка модели Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Развертывание тонко настроенной модели](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 3: Интеграция с Prompt flow и общение с вашей пользовательской моделью](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Интеграция пользовательской модели Phi-3 с Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Общение с вашей пользовательской моделью](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке

### Создание Azure Machine Learning Workspace

1. Введите *azure machine learning* в **поисковую строку** в верхней части страницы портала и выберите **Azure Machine Learning** из появившихся вариантов.

    ![Type azure machine learning](../../../../../../translated_images/ru/01-01-type-azml.a5116f8454d98c60.webp)

1. Выберите **+ Создать** из навигационного меню.

1. Выберите **Новое рабочее пространство** из навигационного меню.

    ![Select new workspace](../../../../../../translated_images/ru/01-02-select-new-workspace.83e17436f8898dc4.webp)

1. Выполните следующие действия:

    - Выберите вашу подписку Azure **Subscription**.
    - Выберите **группу ресурсов** для использования (создайте новую, если необходимо).
    - Введите **имя рабочего пространства (Workspace Name)**. Оно должно быть уникальным.
    - Выберите **регион (Region)** для использования.
    - Выберите **учетную запись хранилища (Storage account)** для использования (создайте новую, если необходимо).
    - Выберите **ключевой хранилище (Key vault)** для использования (создайте новое, если необходимо).
    - Выберите **Application insights** для использования (создайте новое, если необходимо).
    - Выберите **реестр контейнеров (Container registry)** для использования (создайте новый, если необходимо).

    ![Fill AZML.](../../../../../../translated_images/ru/01-03-fill-AZML.730a5177757bbebb.webp)

1. Выберите **Проверить + создать (Review + Create)**.

1. Выберите **Создать (Create)**.

### Запрос лимитов GPU в подписке Azure

В этом E2E примере вы будете использовать *Standard_NC24ads_A100_v4 GPU* для тонкой настройки, что требует запроса квоты, и *Standard_E4s_v3* CPU для развертывания, что не требует запроса квоты.

> [!NOTE]
>
> Только подписки Pay-As-You-Go (стандартный тип подписки) имеют право на выделение GPU; подписки с льготами в настоящее время не поддерживаются.
>
> Для тех, кто использует подписки с льготами (например, Visual Studio Enterprise Subscription) или хочет быстро протестировать процесс тонкой настройки и развертывания, это руководство также содержит рекомендации по тонкой настройке с минимальным набором данных, используя CPU. Однако важно отметить, что результаты тонкой настройки значительно лучше при использовании GPU с большими наборами данных.

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выполните следующие действия, чтобы запросить квоту для *Standard NCADSA100v4 Family*:

    - Выберите **Quota** в левой вкладке.
    - Выберите **семейство виртуальных машин (Virtual machine family)** для использования. Например, выберите **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, которое включает *Standard_NC24ads_A100_v4* GPU.
    - Выберите **Request quota** из навигационного меню.

        ![Request quota.](../../../../../../translated_images/ru/01-04-request-quota.3d3670c3221ab834.webp)

    - На странице запроса квоты введите желаемый **New cores limit**. Например, 24.
    - На странице запроса квоты выберите **Отправить (Submit)**, чтобы запросить квоту GPU.

> [!NOTE]
> Вы можете выбрать подходящий GPU или CPU для ваших нужд, обратившись к документу [Размеры виртуальных машин в Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Добавление назначения роли

Для тонкой настройки и развертывания моделей сначала необходимо создать User Assigned Managed Identity (UAI) и назначить ей соответствующие разрешения. Эта UAI будет использоваться для аутентификации во время развертывания.

#### Создание User Assigned Managed Identity (UAI)

1. Введите *managed identities* в **поисковую строку** в верхней части страницы портала и выберите **Managed Identities** из появившихся вариантов.

    ![Type managed identities.](../../../../../../translated_images/ru/01-05-type-managed-identities.9297b6039874eff8.webp)

1. Выберите **+ Создать**.

    ![Select create.](../../../../../../translated_images/ru/01-06-select-create.936d8d66d7144f9a.webp)

1. Выполните следующие действия:

    - Выберите вашу подписку Azure **Subscription**.
    - Выберите **группу ресурсов** для использования (создайте новую, если необходимо).
    - Выберите **регион (Region)** для использования.
    - Введите **имя (Name)**. Оно должно быть уникальным.

1. Выберите **Проверить + создать (Review + create)**.

1. Выберите **+ Создать (Create)**.

#### Назначение роли Contributor для Managed Identity

1. Перейдите к ресурсу Managed Identity, который вы создали.

1. Выберите **Назначения ролей Azure (Azure role assignments)** в левой вкладке.

1. Выберите **+ Добавить назначение роли (+Add role assignment)** из навигационного меню.

1. На странице добавления назначения роли выполните следующие действия:
    - Установите **Область (Scope)** на **Группа ресурсов (Resource group)**.
    - Выберите вашу подписку Azure **Subscription**.
    - Выберите **группу ресурсов (Resource group)** для использования.
    - Выберите роль **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/ru/01-07-fill-contributor-role.29ca99b7c9f687e0.webp)

1. Выберите **Сохранить (Save)**.

#### Назначение роли Storage Blob Data Reader для Managed Identity

1. Введите *storage accounts* в **поисковую строку** в верхней части страницы портала и выберите **Storage accounts** из появившихся вариантов.

    ![Type storage accounts.](../../../../../../translated_images/ru/01-08-type-storage-accounts.1186c8e42933e49b.webp)

1. Выберите учетную запись хранения, связанную с созданным Azure Machine Learning workspace. Например, *finetunephistorage*.

1. Выполните следующие действия, чтобы перейти на страницу добавления назначения роли:

    - Перейдите к учетной записи Azure Storage, которую вы создали.
    - Выберите **Управление доступом (IAM)** в левой вкладке.
    - Выберите **+ Добавить (+ Add)** в навигационном меню.
    - Выберите **Добавить назначение роли (Add role assignment)**.

    ![Add role.](../../../../../../translated_images/ru/01-09-add-role.d2db22fec1b187f0.webp)

1. На странице добавления назначения роли выполните следующие действия:

    - Введите *Storage Blob Data Reader* в **поисковую строку** на странице ролей и выберите **Storage Blob Data Reader** из появившихся вариантов.
    - Выберите **Далее (Next)**.
    - На странице выбора участников установите **Назначить доступ (Assign access to)** как **Управляемая идентичность (Managed identity)**.
    - Выберите **+ Выбрать участников (+ Select members)**.
    - На странице выбора управляемых идентичностей выберите вашу подписку Azure **Subscription**.
    - Выберите **Managed identity**.
    - Выберите управляемую идентичность, которую вы создали, например, *finetunephi-managedidentity*.
    - Нажмите **Выбрать (Select)**.

    ![Select managed identity.](../../../../../../translated_images/ru/01-10-select-managed-identity.5ce5ba181f72a4df.webp)

1. Выберите **Проверить + назначить (Review + assign)**.

#### Назначение роли AcrPull для Managed Identity

1. Введите *container registries* в **поисковую строку** в верхней части страницы портала и выберите **Container registries** из появившихся вариантов.

    ![Type container registries.](../../../../../../translated_images/ru/01-11-type-container-registries.ff3b8bdc49dc596c.webp)

1. Выберите реестр контейнеров, связанный с вашим Azure Machine Learning workspace. Например, *finetunephicontainerregistries*.

1. Выполните следующие действия, чтобы перейти на страницу добавления назначения роли:

    - Выберите **Управление доступом (IAM)** в левой вкладке.
    - Выберите **+ Добавить (+ Add)** в навигационном меню.
    - Выберите **Добавить назначение роли (Add role assignment)**.

1. На странице добавления назначения роли выполните следующие действия:

    - Введите *AcrPull* в **поисковую строку** на странице ролей и выберите **AcrPull** из появившихся вариантов.
    - Выберите **Далее (Next)**.
    - На странице выбора участников установите **Назначить доступ (Assign access to)** как **Управляемая идентичность (Managed identity)**.
    - Выберите **+ Выбрать участников (+ Select members)**.
    - На странице выбора управляемых идентичностей выберите вашу подписку Azure **Subscription**.
    - Выберите **Managed identity**.
    - Выберите управляемую идентичность, которую вы создали, например, *finetunephi-managedidentity*.
    - Нажмите **Выбрать (Select)**.
    - Выберите **Проверить + назначить (Review + assign)**.

### Настройка проекта

Теперь вы создадите папку для работы и настроите виртуальное окружение для разработки программы, которая взаимодействует с пользователями и использует сохраненную историю чата из Azure Cosmos DB для информирования своих ответов.

#### Создание рабочей папки

1. Откройте окно терминала и введите следующую команду для создания папки с именем *finetune-phi* в пути по умолчанию.

    ```console
    mkdir finetune-phi
    ```

1. Введите следующую команду в терминале, чтобы перейти в созданную папку *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Создание виртуального окружения

1. Введите следующую команду в терминале, чтобы создать виртуальное окружение с именем *.venv*.

    ```console
    python -m venv .venv
    ```

1. Введите следующую команду в терминале, чтобы активировать виртуальное окружение.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Если все сработало, вы должны увидеть *(.venv)* перед приглашением командной строки.

#### Установка необходимых пакетов

1. Введите следующие команды в терминале для установки необходимых пакетов.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Создание файлов проекта
В этом упражнении вы создадите необходимые файлы для нашего проекта. Эти файлы включают скрипты для загрузки набора данных, настройки среды Azure Machine Learning, дообучения модели Phi-3 и развертывания дообученной модели. Вы также создадите файл *conda.yml* для настройки среды дообучения.

В этом упражнении вы:

- Создадите файл *download_dataset.py* для загрузки набора данных.
- Создадите файл *setup_ml.py* для настройки среды Azure Machine Learning.
- Создадите файл *fine_tune.py* в папке *finetuning_dir* для дообучения модели Phi-3 с использованием набора данных.
- Создадите файл *conda.yml* для настройки среды дообучения.
- Создадите файл *deploy_model.py* для развертывания дообученной модели.
- Создадите файл *integrate_with_promptflow.py* для интеграции дообученной модели и выполнения модели с помощью Prompt flow.
- Создадите файл flow.dag.yml для настройки структуры рабочего процесса в Prompt flow.
- Создадите файл *config.py* для ввода информации Azure.

> [!NOTE]
>
> Полная структура папок:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. Откройте **Visual Studio Code**.

1. В меню выберите **File**.

1. Выберите **Open Folder**.

1. Выберите папку *finetune-phi*, которую вы создали, расположенную по адресу *C:\Users\yourUserName\finetune-phi*.

    ![Открыть папку проекта.](../../../../../../translated_images/ru/01-12-open-project-folder.1fff9c7f41dd1639.webp)

1. В левой панели Visual Studio Code щелкните правой кнопкой мыши и выберите **New File**, чтобы создать новый файл с именем *download_dataset.py*.

1. В левой панели Visual Studio Code щелкните правой кнопкой мыши и выберите **New File**, чтобы создать новый файл с именем *setup_ml.py*.

1. В левой панели Visual Studio Code щелкните правой кнопкой мыши и выберите **New File**, чтобы создать новый файл с именем *deploy_model.py*.

    ![Создать новый файл.](../../../../../../translated_images/ru/01-13-create-new-file.c17c150fff384a39.webp)

1. В левой панели Visual Studio Code щелкните правой кнопкой мыши и выберите **New Folder**, чтобы создать новую папку с именем *finetuning_dir*.

1. В папке *finetuning_dir* создайте новый файл с именем *fine_tune.py*.

#### Создание и настройка файла *conda.yml*

1. В левой панели Visual Studio Code щелкните правой кнопкой мыши и выберите **New File**, чтобы создать новый файл с именем *conda.yml*.

1. Добавьте следующий код в файл *conda.yml* для настройки среды дообучения модели Phi-3.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### Создание и настройка файла *config.py*

1. В левой панели Visual Studio Code щелкните правой кнопкой мыши и выберите **New File**, чтобы создать новый файл с именем *config.py*.

1. Добавьте следующий код в файл *config.py* для ввода вашей информации Azure.

    ```python
    # Настройки Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Настройки Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Настройки управляемой идентичности Azure
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Пути к файлам набора данных
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Настройки дообученной модели
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Добавление переменных среды Azure

1. Выполните следующие действия, чтобы добавить идентификатор подписки Azure:

    - Введите *subscriptions* в **строку поиска** в верхней части портала и выберите **Subscriptions** из появившихся вариантов.
    - Выберите используемую подписку Azure.
    - Скопируйте и вставьте ваш Subscription ID в файл *config.py*.

    ![Найти ID подписки.](../../../../../../translated_images/ru/01-14-find-subscriptionid.4f4ca33555f1e637.webp)

1. Выполните следующие действия, чтобы добавить имя рабочего пространства Azure:

    - Перейдите к созданному ресурсу Azure Machine Learning.
    - Скопируйте и вставьте имя вашего рабочего пространства в файл *config.py*.

    ![Найти имя Azure Machine Learning.](../../../../../../translated_images/ru/01-15-find-AZML-name.1975f0422bca19a7.webp)

1. Выполните следующие действия, чтобы добавить имя группы ресурсов Azure:

    - Перейдите к созданному ресурсу Azure Machine Learning.
    - Скопируйте и вставьте имя вашей группы ресурсов Azure в файл *config.py*.

    ![Найти имя группы ресурсов.](../../../../../../translated_images/ru/01-16-find-AZML-resourcegroup.855a349d0af134a3.webp)

2. Выполните следующие действия, чтобы добавить имя управляемой идентичности Azure:

    - Перейдите к созданному ресурсу управляемых идентичностей.
    - Скопируйте и вставьте имя вашей управляемой идентичности Azure в файл *config.py*.

    ![Найти UAI.](../../../../../../translated_images/ru/01-17-find-uai.3529464f53499827.webp)

### Подготовка набора данных для дообучения

В этом упражнении вы выполните запуск файла *download_dataset.py* для загрузки набора данных *ULTRACHAT_200k* в вашу локальную среду. После этого вы будете использовать этот набор данных для дообучения модели Phi-3 в Azure Machine Learning.

#### Загрузка вашего набора данных с помощью *download_dataset.py*

1. Откройте файл *download_dataset.py* в Visual Studio Code.

1. Добавьте следующий код в файл *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Загрузите набор данных с указанным именем, конфигурацией и коэффициентом разделения
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Разделите набор данных на обучающую и тестовую выборки (80% обучение, 20% тест)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Создайте директорию, если она не существует
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Откройте файл в режиме записи
        with open(filepath, 'w', encoding='utf-8') as f:
            # Итерация по каждой записи в наборе данных
            for record in dataset:
                # Сохраните запись как JSON-объект и запишите её в файл
                json.dump(record, f)
                # Запишите символ новой строки для разделения записей
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Загрузите и разделите набор данных ULTRACHAT_200k с определённой конфигурацией и коэффициентом разделения
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Извлеките обучающую и тестовую выборки из разделения
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Сохраните обучающую выборку в файл JSONL
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Сохраните тестовую выборку в отдельный файл JSONL
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Рекомендации по дообучению минимальным набором данных с использованием CPU**
>
> Если вы хотите использовать CPU для дообучения, этот подход подходит тем, у кого есть подписки с преимуществами (например, Visual Studio Enterprise Subscription), или для быстрой проверки процессов дообучения и развертывания.
>
> Замените `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` на `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Введите следующую команду в терминале, чтобы запустить скрипт и скачать набор данных в локальную среду.

    ```console
    python download_data.py
    ```

1. Проверьте, что наборы данных успешно сохранены в локальной директории *finetune-phi/data*.

> [!NOTE]
>
> **Размер набора данных и время дообучения**
>
> В этом E2E примере используется только 1% набора данных (`train_sft[:1%]`). Это значительно уменьшает объем данных, ускоряя процесс загрузки и дообучения. Вы можете скорректировать процентное значение, чтобы найти оптимальный баланс между временем обучения и качеством модели. Использование меньшей части набора данных сокращает время, необходимое для дообучения, делая процесс более управляемым для E2E примера.

## Сценарий 2: Дообучение модели Phi-3 и развертывание в Azure Machine Learning Studio

### Настройка Azure CLI

Вам необходимо настроить Azure CLI для аутентификации вашей среды. Azure CLI позволяет управлять ресурсами Azure непосредственно из командной строки и предоставляет учетные данные, необходимые Azure Machine Learning для доступа к этим ресурсам. Чтобы начать, установите [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Откройте терминал и введите следующую команду для входа в вашу учетную запись Azure.

    ```console
    az login
    ```

1. Выберите учетную запись Azure для использования.

1. Выберите подписку Azure для использования.

    ![Найти имя группы ресурсов.](../../../../../../translated_images/ru/02-01-login-using-azure-cli.dfde31cb75e58a87.webp)

> [!TIP]
>
> Если у вас возникают проблемы с входом в Azure, попробуйте использовать код устройства. Откройте терминал и введите следующую команду для входа:
>
> ```console
> az login --use-device-code
> ```
>

### Дообучение модели Phi-3

В этом упражнении вы дообучите модель Phi-3, используя предоставленный набор данных. Сначала вы определите процесс дообучения в файле *fine_tune.py*. Затем настроите среду Azure Machine Learning и запустите процесс дообучения, выполнив файл *setup_ml.py*. Этот скрипт гарантирует, что дообучение будет происходить в среде Azure Machine Learning.

Запустив *setup_ml.py*, вы выполните процесс дообучения в среде Azure Machine Learning.

#### Добавление кода в файл *fine_tune.py*

1. Перейдите в папку *finetuning_dir* и откройте файл *fine_tune.py* в Visual Studio Code.

1. Добавьте следующий код в файл *fine_tune.py*.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # Чтобы избежать ошибки INVALID_PARAMETER_VALUE в MLflow, отключите интеграцию MLflow
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Настройка логирования
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. Сохраните и закройте файл *fine_tune.py*.

> [!TIP]
> **Вы можете дообучить модель Phi-3.5**
>
> В файле *fine_tune.py* вы можете изменить значение `pretrained_model_name` с `"microsoft/Phi-3-mini-4k-instruct"` на любую модель, которую хотите дообучить. Например, если изменить на `"microsoft/Phi-3.5-mini-instruct"`, вы будете использовать модель Phi-3.5-mini-instruct для дообучения. Чтобы найти и использовать нужное имя модели, посетите [Hugging Face](https://huggingface.co/), найдите интересующую модель и скопируйте ее имя в поле `pretrained_model_name` в вашем скрипте.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Дообучение Phi-3.5.">
>

#### Добавление кода в файл *setup_ml.py*

1. Откройте файл *setup_ml.py* в Visual Studio Code.

1. Добавьте следующий код в файл *setup_ml.py*.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Константы

    # Раскомментируйте следующие строки для использования CPU-инстанса при обучении
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Раскомментируйте следующие строки для использования GPU-инстанса при обучении
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Замените на расположение вашего вычислительного кластера
    FINETUNING_DIR = "./finetuning_dir" # Путь к скрипту дообучения
    TRAINING_ENV_NAME = "phi-3-training-environment" # Название среды для обучения
    MODEL_OUTPUT_DIR = "./model_output" # Путь к директории вывода модели в Azure ML

    # Настройка логирования для отслеживания процесса
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker-образ для среды
            conda_file=CONDA_FILE,  # Файл среды Conda
            name=TRAINING_ENV_NAME,  # Название среды
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Уровень вычислительного кластера
                min_instances=0,  # Минимальное количество инстансов
                max_instances=1  # Максимальное количество инстансов
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Ожидание создания кластера
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Путь к fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Среда обучения
            compute=compute_name,  # Используемый вычислительный кластер
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Путь к файлу обучающих данных
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Путь к файлу оценочных данных
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Инициализация ML Client
        ml_client = get_ml_client()

        # Создание среды
        env = create_or_get_environment(ml_client)
        
        # Создание или получение существующего вычислительного кластера
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Создание и отправка задачи дообучения
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Отправка задачи
        ml_client.jobs.stream(returned_job.name)  # Поток логов задачи
        
        # Получение имени задачи
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Замените `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` и `LOCATION` на ваши конкретные данные.

    ```python
   # Раскомментируйте следующие строки, чтобы использовать экземпляр GPU для обучения
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Замените местоположение на адрес вашего вычислительного кластера
    ```

> [!TIP]
>
> **Рекомендации по дообучению минимальным набором данных с использованием CPU**
>
> Если вы хотите использовать CPU для дообучения, этот подход подходит тем, у кого есть подписки с преимуществами (например, Visual Studio Enterprise Subscription), или чтобы быстро протестировать процессы дообучения и развертывания.
>
> 1. Откройте файл *setup_ml*.
> 1. Замените `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` и `DOCKER_IMAGE_NAME` на следующие значения. Если у вас нет доступа к *Standard_E16s_v3*, вы можете использовать эквивалентный CPU-инстанс или запросить новую квоту.
> 1. Замените `LOCATION` на ваши данные.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Введите следующую команду, чтобы выполнить скрипт *setup_ml.py* и начать процесс дообучения в Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. В этом упражнении вы успешно дообучили модель Phi-3 с помощью Azure Machine Learning. Запустив скрипт *setup_ml.py*, вы настроили среду Azure Machine Learning и инициировали процесс дообучения, определенный в файле *fine_tune.py*. Обратите внимание, что процесс дообучения может занять значительное время. После выполнения команды `python setup_ml.py` необходимо дождаться завершения процесса. Вы можете отслеживать статус задачи дообучения, перейдя по ссылке, указанной в терминале, в портал Azure Machine Learning.

    ![Просмотр задачи дообучения.](../../../../../../translated_images/ru/02-02-see-finetuning-job.59393bc3b143871e.webp)

### Развертывание дообученной модели

Для интеграции дообученной модели Phi-3 с Prompt Flow необходимо развернуть модель, чтобы сделать ее доступной для инференса в реальном времени. Этот процесс включает регистрацию модели, создание онлайн эндпоинта и развертывание модели.

#### Установка имени модели, имени эндпоинта и имени развертывания

1. Откройте файл *config.py*.

1. Замените `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` на желаемое имя вашей модели.

1. Замените `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` на желаемое имя вашего эндпоинта.

1. Замените `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` на желаемое имя вашего развертывания.

#### Добавление кода в файл *deploy_model.py*

Запуск файла *deploy_model.py* автоматизирует весь процесс развертывания. Он регистрирует модель, создает эндпоинт и выполняет развертывание на основе настроек, указанных в файле *config.py*, включающем имя модели, имя эндпоинта и имя развертывания.

1. Откройте файл *deploy_model.py* в Visual Studio Code.

1. Добавьте следующий код в файл *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Импорт конфигурации
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Константы
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Настройка логирования
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Получить текущие детали конечной точки
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Записать в лог текущее распределение трафика для отладки
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Установить распределение трафика для развертывания
            endpoint.traffic = {deployment_name: 100}
            
            # Обновить конечную точку с новым распределением трафика
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Записать в лог обновленное распределение трафика для отладки
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Записать в лог любые ошибки, возникающие в процессе
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. Выполните следующие действия, чтобы получить `JOB_NAME`:

    - Перейдите к созданному ресурсу Azure Machine Learning.
    - Выберите **Studio web URL**, чтобы открыть рабочее пространство Azure Machine Learning.
    - В левом меню выберите **Jobs**.
    - Выберите эксперимент для дообучения, например, *finetunephi*.
    - Выберите созданную вами задачу.
- Скопируйте и вставьте имя вашей работы в `JOB_NAME = "your-job-name"` в файле *deploy_model.py*.

1. Замените `COMPUTE_INSTANCE_TYPE` на ваши конкретные данные.

1. Введите следующую команду, чтобы запустить скрипт *deploy_model.py* и начать процесс развертывания в Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Чтобы избежать дополнительных расходов на вашем аккаунте, убедитесь, что вы удалили созданную конечную точку в рабочем пространстве Azure Machine Learning.
>

#### Проверьте статус развертывания в рабочем пространстве Azure Machine Learning

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Перейдите в рабочее пространство Azure Machine Learning, которое вы создали.

1. Выберите **Studio web URL**, чтобы открыть рабочее пространство Azure Machine Learning.

1. Выберите **Endpoints** на левой панели.

    ![Выберите конечные точки.](../../../../../../translated_images/ru/02-03-select-endpoints.c3136326510baff1.webp)

2. Выберите конечную точку, которую вы создали.

    ![Выберите созданные конечные точки.](../../../../../../translated_images/ru/02-04-select-endpoint-created.0363e7dca51dabb4.webp)

3. На этой странице вы можете управлять конечными точками, созданными во время процесса развертывания.

## Сценарий 3: Интеграция с Prompt flow и чат с вашим кастомным моделью

### Интеграция кастомной модели Phi-3 с Prompt flow

После успешного развертывания вашей доработанной модели, вы можете интегрировать её с Prompt flow для использования модели в приложениях в реальном времени, что позволяет выполнять различные интерактивные задачи с вашей кастомной моделью Phi-3.

#### Установка api ключа и URI конечной точки доработанной модели Phi-3

1. Перейдите в рабочее пространство Azure Machine Learning, которое вы создали.
1. Выберите **Endpoints** на левой панели.
1. Выберите созданную конечную точку.
1. Выберите **Consume** в навигационном меню.
1. Скопируйте и вставьте ваш **REST endpoint** в файл *config.py*, заменяя `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` на ваш **REST endpoint**.
1. Скопируйте и вставьте ваш **Primary key** в файл *config.py*, заменяя `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` на ваш **Primary key**.

    ![Скопируйте api ключ и uri конечной точки.](../../../../../../translated_images/ru/02-05-copy-apikey-endpoint.88b5a92e6462c53b.webp)

#### Добавление кода в файл *flow.dag.yml*

1. Откройте файл *flow.dag.yml* в Visual Studio Code.

1. Добавьте следующий код в *flow.dag.yml*.

    ```yml
    inputs:
      input_data:
        type: string
        default: "Who founded Microsoft?"

    outputs:
      answer:
        type: string
        reference: ${integrate_with_promptflow.output}

    nodes:
    - name: integrate_with_promptflow
      type: python
      source:
        type: code
        path: integrate_with_promptflow.py
      inputs:
        input_data: ${inputs.input_data}
    ```

#### Добавление кода в файл *integrate_with_promptflow.py*

1. Откройте файл *integrate_with_promptflow.py* в Visual Studio Code.

1. Добавьте следующий код в *integrate_with_promptflow.py*.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Настройка логирования
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Общение с вашей кастомной моделью

1. Введите следующую команду, чтобы запустить скрипт *deploy_model.py* и начать процесс развертывания в Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Вот пример результатов: теперь вы можете общаться с вашей кастомной моделью Phi-3. Рекомендуется задавать вопросы, основанные на данных, использованных для дообучения.

    ![Пример Prompt flow.](../../../../../../translated_images/ru/02-06-promptflow-example.89384abaf3ad71f6.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->