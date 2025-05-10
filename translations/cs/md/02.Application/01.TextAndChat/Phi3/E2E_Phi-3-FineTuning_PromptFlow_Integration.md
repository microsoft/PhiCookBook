<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:46:33+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "cs"
}
-->
# Настройка и интеграция кастомных моделей Phi-3 с Prompt flow

Этот комплексный (E2E) пример основан на руководстве "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community. В нем описываются процессы дообучения, развертывания и интеграции кастомных моделей Phi-3 с Prompt flow.

## Обзор

В этом E2E примере вы узнаете, как дообучить модель Phi-3 и интегрировать её с Prompt flow. Используя Azure Machine Learning и Prompt flow, вы создадите рабочий процесс для развертывания и использования кастомных AI-моделей. Пример разделен на три сценария:

**Сценарий 1: Настройка ресурсов Azure и подготовка к дообучению**

**Сценарий 2: Дообучение модели Phi-3 и развертывание в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и общение с вашей кастомной моделью**

Ниже представлен обзор этого E2E примера.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.cs.png)

### Содержание

1. **[Сценарий 1: Настройка ресурсов Azure и подготовка к дообучению](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Создание рабочей области Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Запрос квот GPU в подписке Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Добавление назначения роли](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Настройка проекта](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Подготовка набора данных для дообучения](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 2: Дообучение модели Phi-3 и развертывание в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Настройка Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Дообучение модели Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Развертывание дообученной модели](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 3: Интеграция с Prompt flow и общение с вашей кастомной моделью](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Интеграция кастомной модели Phi-3 с Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Общение с вашей кастомной моделью](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарий 1: Настройка ресурсов Azure и подготовка к дообучению

### Создание рабочей области Azure Machine Learning

1. Введите *azure machine learning* в **строке поиска** в верхней части портала и выберите **Azure Machine Learning** из появившихся вариантов.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.cs.png)

1. Выберите **+ Create** в навигационном меню.

1. Выберите **New workspace** в навигационном меню.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.cs.png)

1. Выполните следующие действия:

    - Выберите вашу Azure **Подписку**.
    - Выберите **Группу ресурсов** (создайте новую при необходимости).
    - Введите **Имя рабочей области**. Оно должно быть уникальным.
    - Выберите **Регион**.
    - Выберите **Учётную запись хранения** (создайте новую при необходимости).
    - Выберите **Key vault** (создайте новый при необходимости).
    - Выберите **Application insights** (создайте новый при необходимости).
    - Выберите **Регистр контейнеров** (создайте новый при необходимости).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.cs.png)

1. Выберите **Review + Create**.

1. Выберите **Create**.

### Запрос квот GPU в подписке Azure

В этом примере вы будете использовать *Standard_NC24ads_A100_v4 GPU* для дообучения, для которого требуется запрос квоты, и *Standard_E4s_v3* CPU для развертывания, для которого запрос квоты не требуется.

> [!NOTE]
>
> Только подписки Pay-As-You-Go (стандартный тип подписки) имеют право на выделение GPU; подписки с льготами в настоящее время не поддерживаются.
>
> Для тех, кто использует подписки с льготами (например, Visual Studio Enterprise Subscription) или хочет быстро протестировать процесс дообучения и развертывания, в этом руководстве также есть рекомендации по дообучению с минимальным набором данных на CPU. Однако стоит отметить, что результаты дообучения значительно лучше при использовании GPU с большими наборами данных.

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выполните следующие действия для запроса квоты *Standard NCADSA100v4 Family*:

    - Выберите **Quota** в левой панели.
    - Выберите **Семейство виртуальных машин**. Например, выберите **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, которое включает *Standard_NC24ads_A100_v4* GPU.
    - Выберите **Request quota** в навигационном меню.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.cs.png)

    - На странице запроса квоты введите желаемое значение **New cores limit**. Например, 24.
    - Нажмите **Submit** для отправки запроса на квоту GPU.

> [!NOTE]
> Вы можете выбрать подходящий GPU или CPU, ознакомившись с документом [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Добавление назначения роли

Для дообучения и развертывания моделей необходимо создать User Assigned Managed Identity (UAI) и назначить ей соответствующие права. Эта UAI будет использоваться для аутентификации при развертывании.

#### Создание User Assigned Managed Identity (UAI)

1. Введите *managed identities* в **строке поиска** в верхней части портала и выберите **Managed Identities** из появившихся вариантов.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.cs.png)

1. Выберите **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.cs.png)

1. Выполните следующие действия:

    - Выберите вашу Azure **Подписку**.
    - Выберите **Группу ресурсов** (создайте новую при необходимости).
    - Выберите **Регион**.
    - Введите **Имя**. Оно должно быть уникальным.

1. Выберите **Review + create**.

1. Выберите **+ Create**.

#### Назначение роли Contributor для Managed Identity

1. Перейдите к ресурсу Managed Identity, который вы создали.

1. Выберите **Azure role assignments** в левой панели.

1. Выберите **+Add role assignment** в навигационном меню.

1. На странице добавления назначения роли выполните следующие действия:
    - В разделе **Scope** выберите **Resource group**.
    - Выберите вашу Azure **Подписку**.
    - Выберите **Группу ресурсов**.
    - В разделе **Role** выберите **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.cs.png)

1. Выберите **Save**.

#### Назначение роли Storage Blob Data Reader для Managed Identity

1. Введите *storage accounts* в **строке поиска** в верхней части портала и выберите **Storage accounts** из появившихся вариантов.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.cs.png)

1. Выберите учетную запись хранения, связанную с рабочей областью Azure Machine Learning, которую вы создали. Например, *finetunephistorage*.

1. Выполните следующие действия для перехода на страницу добавления назначения роли:

    - Перейдите к учетной записи хранения Azure, которую вы создали.
    - Выберите **Access Control (IAM)** в левой панели.
    - Выберите **+ Add** в навигационном меню.
    - Выберите **Add role assignment**.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.cs.png)

1. На странице добавления роли выполните следующие действия:

    - В поле поиска ролей введите *Storage Blob Data Reader* и выберите эту роль из списка.
    - Нажмите **Next**.
    - На странице участников выберите **Assign access to** → **Managed identity**.
    - Нажмите **+ Select members**.
    - Выберите вашу Azure **Подписку**.
    - Выберите **Managed identity**.
    - Выберите созданную вами Managed Identity, например *finetunephi-managedidentity*.
    - Нажмите **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.cs.png)

1. Нажмите **Review + assign**.

#### Назначение роли AcrPull для Managed Identity

1. Введите *container registries* в **строке поиска** в верхней части портала и выберите **Container registries** из появившихся вариантов.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.cs.png)

1. Выберите регистр контейнеров, связанный с рабочей областью Azure Machine Learning. Например, *finetunephicontainerregistries*.

1. Выполните следующие действия для перехода на страницу добавления роли:

    - Выберите **Access Control (IAM)** в левой панели.
    - Нажмите **+ Add**.
    - Выберите **Add role assignment**.

1. На странице добавления роли выполните следующие действия:

    - В поле поиска ролей введите *AcrPull* и выберите эту роль.
    - Нажмите **Next**.
    - На странице участников выберите **Assign access to** → **Managed identity**.
    - Нажмите **+ Select members**.
    - Выберите вашу Azure **Подписку**.
    - Выберите **Managed identity**.
    - Выберите созданную Managed Identity, например *finetunephi-managedidentity*.
    - Нажмите **Select**.
    - Нажмите **Review + assign**.

### Настройка проекта

Теперь создайте папку для работы и настройте виртуальное окружение для разработки программы, которая будет взаимодействовать с пользователем и использовать сохраненную историю чата из Azure Cosmos DB для формирования ответов.

#### Создание рабочей папки

1. Откройте терминал и выполните команду для создания папки с именем *finetune-phi* в стандартном пути.

    ```console
    mkdir finetune-phi
    ```

1. В терминале перейдите в папку *finetune-phi*, которую вы создали.

    ```console
    cd finetune-phi
    ```

#### Создание виртуального окружения

1. В терминале выполните команду для создания виртуального окружения с именем *.venv*.

    ```console
    python -m venv .venv
    ```

1. Активируйте виртуальное окружение.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Если всё прошло успешно, перед приглашением командной строки появится *(.venv)*.

#### Установка необходимых пакетов

1. В терминале выполните команды для установки необходимых пакетов.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Создание файлов проекта

В этом упражнении создайте основные файлы проекта. В них будут скрипты для загрузки набора данных, настройки среды Azure Machine Learning, дообучения модели Phi-3 и развертывания дообученной модели. Также создайте файл *conda.yml* для настройки окружения дообучения.

В этом упражнении вы:

- Создадите файл *download_dataset.py* для загрузки набора данных.
- Создадите файл *setup_ml.py* для настройки среды Azure Machine Learning.
- Создадите файл *fine_tune.py* в папке *finetuning_dir* для дообучения модели Phi-3 на основе набора данных.
- Создадите файл *conda.yml* для настройки окружения дообучения.
- Создадите файл *deploy_model.py* для развертывания дообученной модели.
- Создадите файл *integrate_with_promptflow.py* для интеграции дообученной модели и запуска её через Prompt flow.
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

1. Выберите папку *finetune-phi*, которую вы создали, расположенную по пути *C:\Users\yourUserName\finetune-phi*.

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.cs.png)

1. В левой панели Visual Studio Code кликните правой кнопкой мыши и выберите **New File** для создания файла *download_dataset.py*.

1. Аналогично создайте файлы *setup_ml.py* и *deploy_model.py*.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.cs.png)

1. В левой панели создайте новую папку с именем *finetuning_dir*.

1. В папке *finetuning_dir* создайте файл *fine_tune.py*.

#### Создание и настройка файла *conda.yml*

1. В левой панели Visual Studio Code создайте новый файл *conda.yml*.

1. Добавьте следующий код в файл *conda.yml* для настройки окружения дообучения модели Phi-3.

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

1. В левой панели Visual Studio Code создайте новый файл *config.py*.

1. Добавьте следующий код в файл *config.py* с вашей информацией Azure.

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Добавление переменных окружения Azure

1. Выполните следующие действия для добавления ID подписки Azure:

    - Введите *subscriptions* в **строке поиска** в верхней части портала и выберите **Subscriptions**.
    - Выберите используемую Azure подписку.
    - Скопируйте и вставьте Subscription ID в файл *config.py*.
![Find subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.cs.png)

1. Выполните следующие действия, чтобы добавить имя рабочего пространства Azure:

    - Перейдите к созданному ресурсу Azure Machine Learning.
    - Скопируйте и вставьте имя вашей учетной записи в файл *config.py*.

    ![Find Azure Machine Learning name.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.cs.png)

1. Выполните следующие действия, чтобы добавить имя группы ресурсов Azure:

    - Перейдите к созданному ресурсу Azure Machine Learning.
    - Скопируйте и вставьте имя вашей группы ресурсов Azure в файл *config.py*.

    ![Find resource group name.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.cs.png)

2. Выполните следующие действия, чтобы добавить имя управляемой идентичности Azure

    - Перейдите к созданному ресурсу Managed Identities.
    - Скопируйте и вставьте имя вашей управляемой идентичности Azure в файл *config.py*.

    ![Find UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.cs.png)

### Подготовка набора данных для дообучения

В этом упражнении вы запустите файл *download_dataset.py* для загрузки наборов данных *ULTRACHAT_200k* в вашу локальную среду. Затем вы используете эти наборы данных для дообучения модели Phi-3 в Azure Machine Learning.

#### Загрузка набора данных с помощью *download_dataset.py*

1. Откройте файл *download_dataset.py* в Visual Studio Code.

1. Добавьте следующий код в *download_dataset.py*.

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
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Рекомендации по дообучению с минимальным набором данных на CPU**
>
> Если вы хотите использовать CPU для дообучения, этот подход подходит для пользователей с подписками с преимуществами (например, Visual Studio Enterprise Subscription) или для быстрой проверки процесса дообучения и развертывания.
>
> Замените `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Введите следующую команду в терминале, чтобы запустить скрипт и загрузить набор данных в вашу локальную среду.

    ```console
    python download_data.py
    ```

1. Убедитесь, что наборы данных успешно сохранились в локальной директории *finetune-phi/data*.

> [!NOTE]
>
> **Размер набора данных и время дообучения**
>
> В этом примере E2E используется только 1% набора данных (`train_sft[:1%]`). Это значительно уменьшает объем данных, ускоряя загрузку и процесс дообучения. Вы можете изменить процент, чтобы найти оптимальный баланс между временем обучения и качеством модели. Использование меньшей части набора данных сокращает время дообучения, делая процесс более удобным для примера E2E.

## Сценарий 2: Дообучение модели Phi-3 и развертывание в Azure Machine Learning Studio

### Настройка Azure CLI

Для аутентификации вашей среды необходимо настроить Azure CLI. Azure CLI позволяет управлять ресурсами Azure напрямую из командной строки и предоставляет учетные данные, необходимые для доступа Azure Machine Learning к этим ресурсам. Для начала установите [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Откройте окно терминала и введите следующую команду для входа в вашу учетную запись Azure.

    ```console
    az login
    ```

1. Выберите учетную запись Azure для использования.

1. Выберите подписку Azure для использования.

    ![Find resource group name.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.cs.png)

> [!TIP]
>
> Если возникают проблемы с входом в Azure, попробуйте использовать код устройства. Откройте терминал и введите следующую команду для входа:
>
> ```console
> az login --use-device-code
> ```
>

### Дообучение модели Phi-3

В этом упражнении вы дообучите модель Phi-3 с использованием предоставленного набора данных. Сначала определите процесс дообучения в файле *fine_tune.py*. Затем настройте среду Azure Machine Learning и запустите процесс дообучения с помощью файла *setup_ml.py*. Этот скрипт гарантирует, что дообучение будет выполнено в среде Azure Machine Learning.

Запустив *setup_ml.py*, вы выполните процесс дообучения в среде Azure Machine Learning.

#### Добавление кода в файл *fine_tune.py*

1. Перейдите в папку *finetuning_dir* и откройте файл *fine_tune.py* в Visual Studio Code.

1. Добавьте следующий код в *fine_tune.py*.

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

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
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
> В файле *fine_tune.py* вы можете изменить поле `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` на нужное значение.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Дообучение Phi-3.5.":::
>

#### Добавление кода в файл *setup_ml.py*

1. Откройте файл *setup_ml.py* в Visual Studio Code.

1. Добавьте следующий код в *setup_ml.py*.

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

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
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
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
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
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Замените `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` на ваши конкретные данные.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Рекомендации по дообучению с минимальным набором данных на CPU**
>
> Если вы хотите использовать CPU для дообучения, этот подход подходит для пользователей с подписками с преимуществами (например, Visual Studio Enterprise Subscription) или для быстрой проверки процесса дообучения и развертывания.
>
> 1. Откройте файл *setup_ml*.
> 1. Замените `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` на ваши конкретные данные.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Введите следующую команду для запуска скрипта *setup_ml.py* и начала процесса дообучения в Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. В этом упражнении вы успешно дообучили модель Phi-3 с помощью Azure Machine Learning. Запустив скрипт *setup_ml.py*, вы настроили среду Azure Machine Learning и инициировали процесс дообучения, определенный в файле *fine_tune.py*. Обратите внимание, что процесс дообучения может занять значительное время. После запуска `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.cs.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` используйте желаемые имена для вашего развертывания.

#### Добавление кода в файл *deploy_model.py*

Запуск файла *deploy_model.py* автоматизирует весь процесс развертывания. Он регистрирует модель, создает конечную точку и выполняет развертывание на основе настроек, указанных в файле config.py, который содержит имя модели, имя конечной точки и имя развертывания.

1. Откройте файл *deploy_model.py* в Visual Studio Code.

1. Добавьте следующий код в *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
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

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
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
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
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

1. Выполните следующие действия, чтобы указать `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` с вашими конкретными данными.

1. Введите следующую команду для запуска скрипта *deploy_model.py* и начала процесса развертывания в Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Чтобы избежать дополнительных расходов, обязательно удалите созданную конечную точку в рабочем пространстве Azure Machine Learning.
>

#### Проверка статуса развертывания в рабочем пространстве Azure Machine Learning

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Перейдите в созданное вами рабочее пространство Azure Machine Learning.

1. Выберите **Studio web URL**, чтобы открыть рабочее пространство Azure Machine Learning.

1. Выберите **Endpoints** в меню слева.

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.cs.png)

2. Выберите созданную конечную точку.

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.cs.png)

3. На этой странице вы можете управлять конечными точками, созданными в процессе развертывания.

## Сценарий 3: Интеграция с Prompt flow и общение с вашей кастомной моделью

### Интеграция кастомной модели Phi-3 с Prompt flow

После успешного развертывания вашей дообученной модели вы можете интегрировать её с Prompt flow для использования в реальных приложениях, что позволит выполнять различные интерактивные задачи с вашей кастомной моделью Phi-3.

#### Установка api ключа и URI конечной точки дообученной модели Phi-3

1. Перейдите в созданное рабочее пространство Azure Machine Learning.
1. Выберите **Endpoints** в меню слева.
1. Выберите созданную конечную точку.
1. Выберите **Consume** в навигационном меню.
1. Скопируйте и вставьте **REST endpoint** в файл *config.py*, заменив `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` на ваши значения **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.cs.png)

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

    # Logging setup
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

1. Введите следующую команду для запуска скрипта *deploy_model.py* и начала процесса развертывания в Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Вот пример результата: теперь вы можете общаться с вашей кастомной моделью Phi-3. Рекомендуется задавать вопросы, основанные на данных, использованных для дообучения.

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.cs.png)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.