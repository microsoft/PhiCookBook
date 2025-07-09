<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-09T19:16:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "uk"
}
-->
# Налаштування та інтеграція кастомних моделей Phi-3 з Prompt flow

Цей покроковий (E2E) приклад базується на керівництві "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" з Microsoft Tech Community. Він демонструє процеси тонкого налаштування, розгортання та інтеграції кастомних моделей Phi-3 з Prompt flow.

## Огляд

У цьому E2E прикладі ви навчитеся тонко налаштовувати модель Phi-3 та інтегрувати її з Prompt flow. Використовуючи Azure Machine Learning та Prompt flow, ви створите робочий процес для розгортання та використання кастомних AI-моделей. Цей E2E приклад поділено на три сценарії:

**Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого налаштування**

**Сценарій 2: Тонке налаштування моделі Phi-3 та розгортання в Azure Machine Learning Studio**

**Сценарій 3: Інтеграція з Prompt flow та спілкування з вашою кастомною моделлю**

Ось загальний огляд цього E2E прикладу.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../imgs/02/FineTuning-PromptFlow/00-01-architecture.png)

### Зміст

1. **[Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого налаштування](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Створення робочої області Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Запит квот на GPU в підписці Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Додавання призначення ролі](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Налаштування проєкту](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Підготовка набору даних для тонкого налаштування](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарій 2: Тонке налаштування моделі Phi-3 та розгортання в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Налаштування Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Тонке налаштування моделі Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Розгортання тонко налаштованої моделі](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарій 3: Інтеграція з Prompt flow та спілкування з вашою кастомною моделлю](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Інтеграція кастомної моделі Phi-3 з Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Спілкування з вашою кастомною моделлю](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого налаштування

### Створення робочої області Azure Machine Learning

1. Введіть *azure machine learning* у **рядку пошуку** у верхній частині порталу та оберіть **Azure Machine Learning** зі списку.

    ![Type azure machine learning](../../../../../../imgs/02/FineTuning-PromptFlow/01-01-type-azml.png)

1. Оберіть **+ Create** у навігаційному меню.

1. Оберіть **New workspace** у навігаційному меню.

    ![Select new workspace](../../../../../../imgs/02/FineTuning-PromptFlow/01-02-select-new-workspace.png)

1. Виконайте наступні дії:

    - Оберіть вашу Azure **Subscription**.
    - Оберіть **Resource group** для використання (створіть нову, якщо потрібно).
    - Введіть **Workspace Name**. Він має бути унікальним.
    - Оберіть **Region**, яку хочете використовувати.
    - Оберіть **Storage account** для використання (створіть новий, якщо потрібно).
    - Оберіть **Key vault** для використання (створіть новий, якщо потрібно).
    - Оберіть **Application insights** для використання (створіть новий, якщо потрібно).
    - Оберіть **Container registry** для використання (створіть новий, якщо потрібно).

    ![Fill AZML.](../../../../../../imgs/02/FineTuning-PromptFlow/01-03-fill-AZML.png)

1. Оберіть **Review + Create**.

1. Оберіть **Create**.

### Запит квот на GPU в підписці Azure

У цьому E2E прикладі ви будете використовувати *Standard_NC24ads_A100_v4 GPU* для тонкого налаштування, що потребує запиту квоти, та *Standard_E4s_v3* CPU для розгортання, який не потребує запиту квоти.

> [!NOTE]
>
> Тільки підписки типу Pay-As-You-Go (стандартний тип підписки) мають право на виділення GPU; підписки з пільгами наразі не підтримуються.
>
> Для користувачів з пільговими підписками (наприклад, Visual Studio Enterprise Subscription) або тих, хто хоче швидко протестувати процес тонкого налаштування та розгортання, цей посібник також містить інструкції для тонкого налаштування з мінімальним набором даних на CPU. Втім, варто пам’ятати, що результати тонкого налаштування значно кращі при використанні GPU з більшими наборами даних.

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виконайте наступні дії, щоб запросити квоту для *Standard NCADSA100v4 Family*:

    - Оберіть **Quota** у лівому меню.
    - Оберіть **Virtual machine family** для використання. Наприклад, оберіть **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, що включає *Standard_NC24ads_A100_v4* GPU.
    - Оберіть **Request quota** у навігаційному меню.

        ![Request quota.](../../../../../../imgs/02/FineTuning-PromptFlow/01-04-request-quota.png)

    - На сторінці Request quota введіть **New cores limit**, який хочете отримати. Наприклад, 24.
    - На сторінці Request quota оберіть **Submit** для подання запиту на квоту GPU.

> [!NOTE]
> Ви можете обрати відповідний GPU або CPU, орієнтуючись на документ [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Додавання призначення ролі

Для тонкого налаштування та розгортання моделей спочатку потрібно створити User Assigned Managed Identity (UAI) та надати їй відповідні дозволи. Ця UAI буде використовуватися для автентифікації під час розгортання.

#### Створення User Assigned Managed Identity (UAI)

1. Введіть *managed identities* у **рядку пошуку** у верхній частині порталу та оберіть **Managed Identities** зі списку.

    ![Type managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow/01-05-type-managed-identities.png)

1. Оберіть **+ Create**.

    ![Select create.](../../../../../../imgs/02/FineTuning-PromptFlow/01-06-select-create.png)

1. Виконайте наступні дії:

    - Оберіть вашу Azure **Subscription**.
    - Оберіть **Resource group** для використання (створіть нову, якщо потрібно).
    - Оберіть **Region**, яку хочете використовувати.
    - Введіть **Name**. Він має бути унікальним.

1. Оберіть **Review + create**.

1. Оберіть **+ Create**.

#### Додавання ролі Contributor до Managed Identity

1. Перейдіть до ресурсу Managed Identity, який ви створили.

1. Оберіть **Azure role assignments** у лівому меню.

1. Оберіть **+Add role assignment** у навігаційному меню.

1. На сторінці Add role assignment виконайте наступні дії:
    - Оберіть **Scope** як **Resource group**.
    - Оберіть вашу Azure **Subscription**.
    - Оберіть **Resource group** для використання.
    - Оберіть роль **Contributor**.

    ![Fill contributor role.](../../../../../../imgs/02/FineTuning-PromptFlow/01-07-fill-contributor-role.png)

1. Оберіть **Save**.

#### Додавання ролі Storage Blob Data Reader до Managed Identity

1. Введіть *storage accounts* у **рядку пошуку** у верхній частині порталу та оберіть **Storage accounts** зі списку.

    ![Type storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow/01-08-type-storage-accounts.png)

1. Оберіть обліковий запис зберігання, пов’язаний з робочою областю Azure Machine Learning, яку ви створили. Наприклад, *finetunephistorage*.

1. Виконайте наступні дії, щоб перейти на сторінку додавання ролі:

    - Перейдіть до облікового запису Azure Storage, який ви створили.
    - Оберіть **Access Control (IAM)** у лівому меню.
    - Оберіть **+ Add** у навігаційному меню.
    - Оберіть **Add role assignment** у навігаційному меню.

    ![Add role.](../../../../../../imgs/02/FineTuning-PromptFlow/01-09-add-role.png)

1. На сторінці Add role assignment виконайте наступні дії:

    - У полі ролі введіть *Storage Blob Data Reader* у **рядку пошуку** та оберіть **Storage Blob Data Reader** зі списку.
    - Оберіть **Next**.
    - На сторінці Members оберіть **Assign access to** **Managed identity**.
    - Оберіть **+ Select members**.
    - На сторінці вибору Managed identities оберіть вашу Azure **Subscription**.
    - Оберіть **Managed identity** як **Manage Identity**.
    - Оберіть створену Managed Identity. Наприклад, *finetunephi-managedidentity*.
    - Оберіть **Select**.

    ![Select managed identity.](../../../../../../imgs/02/FineTuning-PromptFlow/01-10-select-managed-identity.png)

1. Оберіть **Review + assign**.

#### Додавання ролі AcrPull до Managed Identity

1. Введіть *container registries* у **рядку пошуку** у верхній частині порталу та оберіть **Container registries** зі списку.

    ![Type container registries.](../../../../../../imgs/02/FineTuning-PromptFlow/01-11-type-container-registries.png)

1. Оберіть контейнерний реєстр, пов’язаний з робочою областю Azure Machine Learning. Наприклад, *finetunephicontainerregistries*.

1. Виконайте наступні дії, щоб перейти на сторінку додавання ролі:

    - Оберіть **Access Control (IAM)** у лівому меню.
    - Оберіть **+ Add** у навігаційному меню.
    - Оберіть **Add role assignment** у навігаційному меню.

1. На сторінці Add role assignment виконайте наступні дії:

    - У полі ролі введіть *AcrPull* у **рядку пошуку** та оберіть **AcrPull** зі списку.
    - Оберіть **Next**.
    - На сторінці Members оберіть **Assign access to** **Managed identity**.
    - Оберіть **+ Select members**.
    - На сторінці вибору Managed identities оберіть вашу Azure **Subscription**.
    - Оберіть **Managed identity** як **Manage Identity**.
    - Оберіть створену Managed Identity. Наприклад, *finetunephi-managedidentity*.
    - Оберіть **Select**.
    - Оберіть **Review + assign**.

### Налаштування проєкту

Тепер ви створите папку для роботи та налаштуєте віртуальне середовище для розробки програми, яка взаємодіятиме з користувачами та використовуватиме збережену історію чатів з Azure Cosmos DB для формування відповідей.

#### Створення папки для роботи

1. Відкрийте термінал і введіть команду для створення папки з назвою *finetune-phi* у стандартному каталозі.

    ```console
    mkdir finetune-phi
    ```

1. Введіть команду в терміналі, щоб перейти до створеної папки *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Створення віртуального середовища

1. Введіть команду в терміналі для створення віртуального середовища з назвою *.venv*.

    ```console
    python -m venv .venv
    ```

1. Введіть команду в терміналі для активації віртуального середовища.

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> Якщо все пройшло успішно, перед командним рядком має з’явитися *(.venv)*.
#### Встановіть необхідні пакети

1. Введіть наступні команди у вашому терміналі, щоб встановити необхідні пакети.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Створіть файли проекту

У цьому завданні ви створите основні файли для нашого проекту. Ці файли включають скрипти для завантаження датасету, налаштування середовища Azure Machine Learning, тонкого налаштування моделі Phi-3 та розгортання тонко налаштованої моделі. Також ви створите файл *conda.yml* для налаштування середовища тонкого налаштування.

У цьому завданні ви:

- Створите файл *download_dataset.py* для завантаження датасету.
- Створите файл *setup_ml.py* для налаштування середовища Azure Machine Learning.
- Створите файл *fine_tune.py* у папці *finetuning_dir* для тонкого налаштування моделі Phi-3 за допомогою датасету.
- Створите файл *conda.yml* для налаштування середовища тонкого налаштування.
- Створите файл *deploy_model.py* для розгортання тонко налаштованої моделі.
- Створите файл *integrate_with_promptflow.py* для інтеграції тонко налаштованої моделі та запуску моделі за допомогою Prompt flow.
- Створите файл flow.dag.yml для налаштування структури робочого процесу для Prompt flow.
- Створите файл *config.py* для введення інформації про Azure.

> [!NOTE]
>
> Повна структура папок:
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

1. Відкрийте **Visual Studio Code**.

1. Виберіть у меню **File**.

1. Виберіть **Open Folder**.

1. Виберіть папку *finetune-phi*, яку ви створили, розташовану за адресою *C:\Users\yourUserName\finetune-phi*.

    ![Відкрити папку проекту.](../../../../../../imgs/02/FineTuning-PromptFlow/01-12-open-project-folder.png)

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші та виберіть **New File**, щоб створити новий файл з назвою *download_dataset.py*.

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші та виберіть **New File**, щоб створити новий файл з назвою *setup_ml.py*.

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші та виберіть **New File**, щоб створити новий файл з назвою *deploy_model.py*.

    ![Створити новий файл.](../../../../../../imgs/02/FineTuning-PromptFlow/01-13-create-new-file.png)

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші та виберіть **New Folder**, щоб створити нову папку з назвою *finetuning_dir*.

1. У папці *finetuning_dir* створіть новий файл з назвою *fine_tune.py*.

#### Створіть і налаштуйте файл *conda.yml*

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші та виберіть **New File**, щоб створити новий файл з назвою *conda.yml*.

1. Додайте наступний код у файл *conda.yml* для налаштування середовища тонкого налаштування моделі Phi-3.

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

#### Створіть і налаштуйте файл *config.py*

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші та виберіть **New File**, щоб створити новий файл з назвою *config.py*.

1. Додайте наступний код у файл *config.py* для введення вашої інформації про Azure.

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

#### Додайте змінні середовища Azure

1. Виконайте наступні дії, щоб додати Azure Subscription ID:

    - Введіть *subscriptions* у **рядок пошуку** у верхній частині порталу та виберіть **Subscriptions** зі списку.
    - Виберіть підписку Azure, яку ви зараз використовуєте.
    - Скопіюйте та вставте ваш Subscription ID у файл *config.py*.

    ![Знайти subscription id.](../../../../../../imgs/02/FineTuning-PromptFlow/01-14-find-subscriptionid.png)

1. Виконайте наступні дії, щоб додати ім’я Azure Workspace:

    - Перейдіть до ресурсу Azure Machine Learning, який ви створили.
    - Скопіюйте та вставте ім’я вашого робочого простору у файл *config.py*.

    ![Знайти ім’я Azure Machine Learning.](../../../../../../imgs/02/FineTuning-PromptFlow/01-15-find-AZML-name.png)

1. Виконайте наступні дії, щоб додати ім’я Azure Resource Group:

    - Перейдіть до ресурсу Azure Machine Learning, який ви створили.
    - Скопіюйте та вставте ім’я вашої групи ресурсів Azure у файл *config.py*.

    ![Знайти ім’я групи ресурсів.](../../../../../../imgs/02/FineTuning-PromptFlow/01-16-find-AZML-resourcegroup.png)

2. Виконайте наступні дії, щоб додати ім’я Azure Managed Identity:

    - Перейдіть до ресурсу Managed Identities, який ви створили.
    - Скопіюйте та вставте ім’я вашої Azure Managed Identity у файл *config.py*.

    ![Знайти UAI.](../../../../../../imgs/02/FineTuning-PromptFlow/01-17-find-uai.png)

### Підготуйте датасет для тонкого налаштування

У цьому завданні ви запустите файл *download_dataset.py*, щоб завантажити датасети *ULTRACHAT_200k* у ваше локальне середовище. Потім ви використаєте ці датасети для тонкого налаштування моделі Phi-3 в Azure Machine Learning.

#### Завантажте ваш датасет за допомогою *download_dataset.py*

1. Відкрийте файл *download_dataset.py* у Visual Studio Code.

1. Додайте наступний код у файл *download_dataset.py*.

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
> **Рекомендації для тонкого налаштування з мінімальним датасетом на CPU**
>
> Якщо ви хочете використовувати CPU для тонкого налаштування, цей підхід ідеально підходить для користувачів з підписками benefit (наприклад, Visual Studio Enterprise Subscription) або для швидкого тестування процесу тонкого налаштування та розгортання.
>
> Замініть `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` на `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Введіть наступну команду у вашому терміналі, щоб запустити скрипт і завантажити датасет у ваше локальне середовище.

    ```console
    python download_data.py
    ```

1. Переконайтеся, що датасети успішно збережені у вашій локальній директорії *finetune-phi/data*.

> [!NOTE]
>
> **Розмір датасету та час тонкого налаштування**
>
> У цьому E2E прикладі ви використовуєте лише 1% датасету (`train_sft[:1%]`). Це значно зменшує обсяг даних, прискорюючи як завантаження, так і процес тонкого налаштування. Ви можете регулювати відсоток, щоб знайти оптимальний баланс між часом навчання та продуктивністю моделі. Використання меншої частини датасету скорочує час, необхідний для тонкого налаштування, роблячи процес більш керованим для E2E прикладу.

## Сценарій 2: Тонке налаштування моделі Phi-3 та розгортання в Azure Machine Learning Studio

### Налаштування Azure CLI

Вам потрібно налаштувати Azure CLI для автентифікації вашого середовища. Azure CLI дозволяє керувати ресурсами Azure безпосередньо з командного рядка та надає облікові дані, необхідні для доступу Azure Machine Learning до цих ресурсів. Щоб почати, встановіть [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Відкрийте вікно терміналу і введіть наступну команду для входу у ваш обліковий запис Azure.

    ```console
    az login
    ```

1. Виберіть ваш обліковий запис Azure для використання.

1. Виберіть підписку Azure для використання.

    ![Знайти ім’я групи ресурсів.](../../../../../../imgs/02/FineTuning-PromptFlow/02-01-login-using-azure-cli.png)

> [!TIP]
>
> Якщо у вас виникають проблеми з входом в Azure, спробуйте використовувати код пристрою. Відкрийте вікно терміналу і введіть наступну команду для входу у ваш обліковий запис Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Тонке налаштування моделі Phi-3

У цьому завданні ви тонко налаштуєте модель Phi-3, використовуючи наданий датасет. Спочатку ви визначите процес тонкого налаштування у файлі *fine_tune.py*. Потім налаштуєте середовище Azure Machine Learning і ініціюєте процес тонкого налаштування, запустивши файл *setup_ml.py*. Цей скрипт забезпечує виконання тонкого налаштування у середовищі Azure Machine Learning.

Запустивши *setup_ml.py*, ви запустите процес тонкого налаштування у середовищі Azure Machine Learning.

#### Додайте код у файл *fine_tune.py*

1. Перейдіть до папки *finetuning_dir* і відкрийте файл *fine_tune.py* у Visual Studio Code.

1. Додайте наступний код у файл *fine_tune.py*.

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

1. Збережіть і закрийте файл *fine_tune.py*.

> [!TIP]
> **Ви можете тонко налаштувати модель Phi-3.5**
>
> У файлі *fine_tune.py* ви можете змінити `pretrained_model_name` з `"microsoft/Phi-3-mini-4k-instruct"` на будь-яку модель, яку хочете тонко налаштувати. Наприклад, якщо змінити на `"microsoft/Phi-3.5-mini-instruct"`, ви будете використовувати модель Phi-3.5-mini-instruct для тонкого налаштування. Щоб знайти та використати потрібну модель, відвідайте [Hugging Face](https://huggingface.co/), знайдіть потрібну модель і скопіюйте її назву у поле `pretrained_model_name` у вашому скрипті.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Тонке налаштування Phi-3.5.":::
>

#### Додайте код у файл *setup_ml.py*

1. Відкрийте файл *setup_ml.py* у Visual Studio Code.

1. Додайте наступний код у файл *setup_ml.py*.

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

1. Замініть `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` та `LOCATION` на ваші конкретні дані.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Рекомендації для тонкого налаштування з мінімальним датасетом на CPU**
>
> Якщо ви хочете використовувати CPU для тонкого налаштування, цей підхід ідеально підходить для користувачів з підписками benefit (наприклад, Visual Studio Enterprise Subscription) або для швидкого тестування процесу тонкого налаштування та розгортання.
>
> 1. Відкрийте файл *setup_ml*.
> 1. Замініть `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` та `DOCKER_IMAGE_NAME` наступним чином. Якщо у вас немає доступу до *Standard_E16s_v3*, ви можете використати еквівалентний CPU-інстанс або запросити нову квоту.
> 1. Замініть `LOCATION` на ваші конкретні дані.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Введіть наступну команду, щоб запустити скрипт *setup_ml.py* і розпочати процес тонкого налаштування в Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. У цьому завданні ви успішно тонко налаштували модель Phi-3 за допомогою Azure Machine Learning. Запустивши скрипт *setup_ml.py*, ви налаштували середовище Azure Machine Learning і ініціювали процес тонкого налаштування, визначений у файлі *fine_tune.py*. Зверніть увагу, що процес тонкого налаштування може зайняти значний час. Після запуску команди `python setup_ml.py` потрібно дочекатися завершення процесу. Ви можете відстежувати статус завдання тонкого налаштування, перейшовши за посиланням, яке з’явиться у терміналі, у портал Azure Machine Learning.

    ![Перегляд завдання тонкого налаштування.](../../../../../../imgs/02/FineTuning-PromptFlow/02-02-see-finetuning-job.png)

### Розгортання тонко налаштованої моделі

Щоб інтегрувати тонко налаштовану модель Phi-3 з Prompt Flow, потрібно розгорнути модель, щоб зробити її доступною для інференсу в реальному часі. Цей процес включає реєстрацію моделі, створення онлайн-ендпоінту та розгортання моделі.

#### Встановіть ім’я моделі, ім’я ендпоінту та ім’я розгортання для розгортання

1. Відкрийте файл *config.py*.

1. Замініть `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` на бажане ім’я вашої моделі.

1. Замініть `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` на бажане ім’я вашого ендпоінту.

1. Замініть `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` на бажане ім’я вашого розгортання.

#### Додайте код у файл *deploy_model.py*

Запуск файлу *deploy_model.py* автоматизує весь процес розгортання. Він реєструє модель, створює ендпоінт і виконує розгортання на основі налаштувань, вказаних у файлі config.py, які включають ім’я моделі, ім’я ендпоінту та ім’я розгортання.

1. Відкрийте файл *deploy_model.py* у Visual Studio Code.

1. Додайте наступний код у файл *deploy_model.py*.

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

1. Виконайте наступні дії, щоб отримати `JOB_NAME`:

    - Перейдіть до ресурсу Azure Machine Learning, який ви створили.
    - Виберіть **Studio web URL**, щоб відкрити робочий простір Azure Machine Learning.
    - Виберіть **Jobs** у лівій панелі.
    - Виберіть експеримент для тонкого налаштування, наприклад, *finetunephi*.
    - Виберіть створене вами завдання.
- Скопіюйте та вставте назву вашої роботи у `JOB_NAME = "your-job-name"` у файлі *deploy_model.py*.

1. Замініть `COMPUTE_INSTANCE_TYPE` на ваші конкретні дані.

1. Введіть наступну команду, щоб запустити скрипт *deploy_model.py* і розпочати процес розгортання в Azure Machine Learning.

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> Щоб уникнути додаткових витрат на вашому рахунку, обов’язково видаліть створений endpoint у робочому просторі Azure Machine Learning.
>

#### Перевірка статусу розгортання в Azure Machine Learning Workspace

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Перейдіть до створеного вами робочого простору Azure Machine Learning.

1. Виберіть **Studio web URL**, щоб відкрити робочий простір Azure Machine Learning.

1. Виберіть **Endpoints** у вкладці зліва.

    ![Select endpoints.](../../../../../../imgs/02/FineTuning-PromptFlow/02-03-select-endpoints.png)

2. Виберіть створений вами endpoint.

    ![Select endpoints that you created.](../../../../../../imgs/02/FineTuning-PromptFlow/02-04-select-endpoint-created.png)

3. На цій сторінці ви можете керувати endpoint, створеними під час процесу розгортання.

## Сценарій 3: Інтеграція з Prompt flow та спілкування з вашим кастомним моделлю

### Інтеграція кастомної моделі Phi-3 з Prompt flow

Після успішного розгортання вашої донавченої моделі, ви можете інтегрувати її з Prompt flow для використання у реальному часі, що дозволяє виконувати різноманітні інтерактивні завдання з вашим кастомним моделлю Phi-3.

#### Встановлення api ключа та URI endpoint до донавченої моделі Phi-3

1. Перейдіть до створеного вами робочого простору Azure Machine Learning.
1. Виберіть **Endpoints** у вкладці зліва.
1. Виберіть створений вами endpoint.
1. Виберіть **Consume** у навігаційному меню.
1. Скопіюйте та вставте ваш **REST endpoint** у файл *config.py*, замінивши `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` на ваш **REST endpoint**.
1. Скопіюйте та вставте ваш **Primary key** у файл *config.py*, замінивши `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` на ваш **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../imgs/02/FineTuning-PromptFlow/02-05-copy-apikey-endpoint.png)

#### Додайте код у файл *flow.dag.yml*

1. Відкрийте файл *flow.dag.yml* у Visual Studio Code.

1. Додайте наступний код у *flow.dag.yml*.

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

#### Додайте код у файл *integrate_with_promptflow.py*

1. Відкрийте файл *integrate_with_promptflow.py* у Visual Studio Code.

1. Додайте наступний код у *integrate_with_promptflow.py*.

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

### Спілкування з вашим кастомним моделлю

1. Введіть наступну команду, щоб запустити скрипт *deploy_model.py* і розпочати процес розгортання в Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Ось приклад результатів: тепер ви можете спілкуватися з вашим кастомним моделлю Phi-3. Рекомендується ставити питання, базуючись на даних, використаних для донавчання.

    ![Prompt flow example.](../../../../../../imgs/02/FineTuning-PromptFlow/02-06-promptflow-example.png)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.