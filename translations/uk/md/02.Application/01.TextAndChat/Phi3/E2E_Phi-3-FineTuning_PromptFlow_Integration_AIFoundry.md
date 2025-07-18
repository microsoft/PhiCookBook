<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T02:11:00+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "uk"
}
-->
# Налаштування та інтеграція кастомних моделей Phi-3 з Prompt flow в Azure AI Foundry

Цей покроковий (E2E) приклад базується на керівництві "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" з Microsoft Tech Community. Він демонструє процеси тонкого налаштування, розгортання та інтеграції кастомних моделей Phi-3 з Prompt flow в Azure AI Foundry.  
На відміну від E2E прикладу "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", де код запускався локально, цей посібник повністю зосереджений на тонкому налаштуванні та інтеграції вашої моделі в Azure AI / ML Studio.

## Огляд

У цьому E2E прикладі ви навчитеся тонко налаштовувати модель Phi-3 та інтегрувати її з Prompt flow в Azure AI Foundry. Використовуючи Azure AI / ML Studio, ви створите робочий процес для розгортання та використання кастомних AI моделей. Цей E2E приклад поділено на три сценарії:

**Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого налаштування**

**Сценарій 2: Тонке налаштування моделі Phi-3 та розгортання в Azure Machine Learning Studio**

**Сценарій 3: Інтеграція з Prompt flow та спілкування з вашою кастомною моделлю в Azure AI Foundry**

Ось загальний огляд цього E2E прикладу.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.uk.png)

### Зміст

1. **[Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого налаштування](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Створення Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Запит квот на GPU в підписці Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Додавання призначення ролі](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Налаштування проєкту](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Підготовка датасету для тонкого налаштування](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарій 2: Тонке налаштування моделі Phi-3 та розгортання в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Тонке налаштування моделі Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Розгортання тонко налаштованої моделі Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарій 3: Інтеграція з Prompt flow та спілкування з вашою кастомною моделлю в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Інтеграція кастомної моделі Phi-3 з Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Спілкування з вашою кастомною моделлю Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого налаштування

### Створення Azure Machine Learning Workspace

1. Введіть *azure machine learning* у **рядок пошуку** у верхній частині порталу та оберіть **Azure Machine Learning** зі списку.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.uk.png)

2. Оберіть **+ Create** у навігаційному меню.

3. Оберіть **New workspace** у навігаційному меню.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.uk.png)

4. Виконайте наступні дії:

    - Оберіть вашу Azure **Subscription**.
    - Оберіть **Resource group** для використання (створіть нову, якщо потрібно).
    - Введіть **Workspace Name**. Ім’я має бути унікальним.
    - Оберіть **Region**, яку хочете використовувати.
    - Оберіть **Storage account** для використання (створіть новий, якщо потрібно).
    - Оберіть **Key vault** для використання (створіть новий, якщо потрібно).
    - Оберіть **Application insights** для використання (створіть новий, якщо потрібно).
    - Оберіть **Container registry** для використання (створіть новий, якщо потрібно).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.uk.png)

5. Оберіть **Review + Create**.

6. Оберіть **Create**.

### Запит квот на GPU в підписці Azure

У цьому посібнику ви навчитеся тонко налаштовувати та розгортати модель Phi-3, використовуючи GPU. Для тонкого налаштування буде використано GPU *Standard_NC24ads_A100_v4*, для якого потрібно подати запит на квоту. Для розгортання буде використано GPU *Standard_NC6s_v3*, для якого також потрібен запит квоти.

> [!NOTE]
>
> Квоти на GPU доступні лише для підписок типу Pay-As-You-Go (стандартний тип підписки); підписки з пільгами наразі не підтримуються.
>

1. Перейдіть на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виконайте наступні дії, щоб подати запит на квоту для *Standard NCADSA100v4 Family*:

    - Оберіть **Quota** у лівому меню.
    - Оберіть **Virtual machine family** для використання. Наприклад, оберіть **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, що включає GPU *Standard_NC24ads_A100_v4*.
    - Оберіть **Request quota** у навігаційному меню.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.uk.png)

    - На сторінці Request quota введіть бажаний **New cores limit**. Наприклад, 24.
    - Натисніть **Submit**, щоб подати запит на квоту GPU.

1. Виконайте наступні дії, щоб подати запит на квоту для *Standard NCSv3 Family*:

    - Оберіть **Quota** у лівому меню.
    - Оберіть **Virtual machine family** для використання. Наприклад, оберіть **Standard NCSv3 Family Cluster Dedicated vCPUs**, що включає GPU *Standard_NC6s_v3*.
    - Оберіть **Request quota** у навігаційному меню.
    - На сторінці Request quota введіть бажаний **New cores limit**. Наприклад, 24.
    - Натисніть **Submit**, щоб подати запит на квоту GPU.

### Додавання призначення ролі

Для тонкого налаштування та розгортання моделей спочатку потрібно створити User Assigned Managed Identity (UAI) та надати їй відповідні дозволи. Ця UAI буде використовуватися для автентифікації під час розгортання.

#### Створення User Assigned Managed Identity (UAI)

1. Введіть *managed identities* у **рядок пошуку** у верхній частині порталу та оберіть **Managed Identities** зі списку.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.uk.png)

1. Оберіть **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.uk.png)

1. Виконайте наступні дії:

    - Оберіть вашу Azure **Subscription**.
    - Оберіть **Resource group** для використання (створіть нову, якщо потрібно).
    - Оберіть **Region**, яку хочете використовувати.
    - Введіть **Name**. Ім’я має бути унікальним.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.uk.png)

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

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.uk.png)

2. Оберіть **Save**.

#### Додавання ролі Storage Blob Data Reader до Managed Identity

1. Введіть *storage accounts* у **рядок пошуку** у верхній частині порталу та оберіть **Storage accounts** зі списку.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.uk.png)

1. Оберіть обліковий запис зберігання, пов’язаний з Azure Machine Learning workspace, який ви створили. Наприклад, *finetunephistorage*.

1. Виконайте наступні дії, щоб перейти на сторінку додавання ролі:

    - Перейдіть до створеного облікового запису Azure Storage.
    - Оберіть **Access Control (IAM)** у лівому меню.
    - Оберіть **+ Add** у навігаційному меню.
    - Оберіть **Add role assignment** у навігаційному меню.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.uk.png)

1. На сторінці Add role assignment виконайте наступні дії:

    - У полі ролей введіть *Storage Blob Data Reader* у **рядок пошуку** та оберіть **Storage Blob Data Reader** зі списку.
    - Оберіть **Next**.
    - На сторінці Members оберіть **Assign access to** — **Managed identity**.
    - Оберіть **+ Select members**.
    - На сторінці вибору Managed identities оберіть вашу Azure **Subscription**.
    - Оберіть **Managed identity** як **Manage Identity**.
    - Оберіть створену Managed Identity. Наприклад, *finetunephi-managedidentity*.
    - Оберіть **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.uk.png)

1. Оберіть **Review + assign**.

#### Додавання ролі AcrPull до Managed Identity

1. Введіть *container registries* у **рядок пошуку** у верхній частині порталу та оберіть **Container registries** зі списку.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.uk.png)

1. Оберіть контейнерний реєстр, пов’язаний з Azure Machine Learning workspace. Наприклад, *finetunephicontainerregistry*.

1. Виконайте наступні дії, щоб перейти на сторінку додавання ролі:

    - Оберіть **Access Control (IAM)** у лівому меню.
    - Оберіть **+ Add** у навігаційному меню.
    - Оберіть **Add role assignment** у навігаційному меню.

1. На сторінці Add role assignment виконайте наступні дії:

    - У полі ролей введіть *AcrPull* у **рядок пошуку** та оберіть **AcrPull** зі списку.
    - Оберіть **Next**.
    - На сторінці Members оберіть **Assign access to** — **Managed identity**.
    - Оберіть **+ Select members**.
    - На сторінці вибору Managed identities оберіть вашу Azure **Subscription**.
    - Оберіть **Managed identity** як **Manage Identity**.
    - Оберіть створену Managed Identity. Наприклад, *finetunephi-managedidentity*.
    - Оберіть **Select**.
    - Оберіть **Review + assign**.

### Налаштування проєкту

Щоб завантажити датасети, необхідні для тонкого налаштування, налаштуйте локальне середовище.

У цьому завданні ви:

- Створите папку для роботи.
- Створите віртуальне середовище.
- Встановите необхідні пакети.
- Створите файл *download_dataset.py* для завантаження датасету.

#### Створення папки для роботи

1. Відкрийте термінал і введіть команду для створення папки з назвою *finetune-phi* у стандартному каталозі.

    ```console
    mkdir finetune-phi
    ```

2. Введіть наступну команду у терміналі, щоб перейти до створеної папки *finetune-phi*.
#### Створення віртуального середовища

1. Введіть наступну команду у вашому терміналі, щоб створити віртуальне середовище з назвою *.venv*.

    ```console
    python -m venv .venv
    ```

2. Введіть наступну команду у вашому терміналі, щоб активувати віртуальне середовище.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Якщо все спрацювало, ви повинні побачити *(.venv)* перед рядком введення команд.

#### Встановлення необхідних пакетів

1. Введіть наступні команди у вашому терміналі, щоб встановити необхідні пакети.

    ```console
    pip install datasets==2.19.1
    ```

#### Створення `download_dataset.py`

> [!NOTE]
> Повна структура папок:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Відкрийте **Visual Studio Code**.

1. Виберіть **File** у меню.

1. Виберіть **Open Folder**.

1. Виберіть папку *finetune-phi*, яку ви створили, розташовану за адресою *C:\Users\yourUserName\finetune-phi*.

    ![Виберіть папку, яку ви створили.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.uk.png)

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші та виберіть **New File**, щоб створити новий файл з назвою *download_dataset.py*.

    ![Створіть новий файл.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.uk.png)

### Підготовка датасету для донавчання

У цьому завданні ви запустите файл *download_dataset.py*, щоб завантажити датасети *ultrachat_200k* у ваше локальне середовище. Потім ви використаєте ці датасети для донавчання моделі Phi-3 в Azure Machine Learning.

У цьому завданні ви:

- Додасте код у файл *download_dataset.py* для завантаження датасетів.
- Запустите файл *download_dataset.py* для завантаження датасетів у локальне середовище.

#### Завантаження датасету за допомогою *download_dataset.py*

1. Відкрийте файл *download_dataset.py* у Visual Studio Code.

1. Додайте наступний код у файл *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

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
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Введіть наступну команду у вашому терміналі, щоб запустити скрипт і завантажити датасет у локальне середовище.

    ```console
    python download_dataset.py
    ```

1. Перевірте, що датасети успішно збережені у локальній директорії *finetune-phi/data*.

> [!NOTE]
>
> #### Примітка щодо розміру датасету та часу донавчання
>
> У цьому посібнику ви використовуєте лише 1% датасету (`split='train[:1%]'`). Це значно зменшує обсяг даних, прискорюючи як завантаження, так і процес донавчання. Ви можете регулювати цей відсоток, щоб знайти оптимальний баланс між часом навчання та продуктивністю моделі. Використання меншої частини датасету скорочує час донавчання, роблячи процес більш зручним для навчального посібника.

## Сценарій 2: Донавчання моделі Phi-3 та розгортання в Azure Machine Learning Studio

### Донавчання моделі Phi-3

У цьому завданні ви донавчите модель Phi-3 в Azure Machine Learning Studio.

У цьому завданні ви:

- Створите кластер обчислювальних ресурсів для донавчання.
- Донавчите модель Phi-3 в Azure Machine Learning Studio.

#### Створення кластера обчислювальних ресурсів для донавчання

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виберіть **Compute** у лівій панелі.

1. Виберіть **Compute clusters** у навігаційному меню.

1. Виберіть **+ New**.

    ![Виберіть compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.uk.png)

1. Виконайте наступні дії:

    - Виберіть **Region**, який хочете використовувати.
    - Виберіть **Virtual machine tier** як **Dedicated**.
    - Виберіть **Virtual machine type** як **GPU**.
    - Виберіть фільтр **Virtual machine size** на **Select from all options**.
    - Виберіть розмір віртуальної машини **Standard_NC24ads_A100_v4**.

    ![Створення кластера.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.uk.png)

1. Виберіть **Next**.

1. Виконайте наступні дії:

    - Введіть унікальне ім’я для **Compute name**.
    - Встановіть **Minimum number of nodes** на **0**.
    - Встановіть **Maximum number of nodes** на **1**.
    - Встановіть **Idle seconds before scale down** на **120**.

    ![Створення кластера.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.uk.png)

1. Виберіть **Create**.

#### Донавчання моделі Phi-3

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виберіть робоче середовище Azure Machine Learning, яке ви створили.

    ![Виберіть створене робоче середовище.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.uk.png)

1. Виконайте наступні дії:

    - Виберіть **Model catalog** у лівій панелі.
    - Введіть *phi-3-mini-4k* у **search bar** і виберіть **Phi-3-mini-4k-instruct** зі списку.

    ![Введіть phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.uk.png)

1. Виберіть **Fine-tune** у навігаційному меню.

    ![Виберіть fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.uk.png)

1. Виконайте наступні дії:

    - Виберіть **Select task type** як **Chat completion**.
    - Виберіть **+ Select data** для завантаження **Training data**.
    - Виберіть тип завантаження Validation data як **Provide different validation data**.
    - Виберіть **+ Select data** для завантаження **Validation data**.

    ![Заповніть сторінку донавчання.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.uk.png)

    > [!TIP]
    >
    > Ви можете вибрати **Advanced settings**, щоб налаштувати параметри, такі як **learning_rate** та **lr_scheduler_type**, для оптимізації процесу донавчання відповідно до ваших потреб.

1. Виберіть **Finish**.

1. У цьому завданні ви успішно донавчили модель Phi-3 за допомогою Azure Machine Learning. Зверніть увагу, що процес донавчання може зайняти значний час. Після запуску завдання донавчання потрібно дочекатися його завершення. Ви можете відстежувати статус завдання у вкладці Jobs у лівій панелі вашого Azure Machine Learning Workspace. У наступній серії ви розгорнете донавчену модель і інтегруєте її з Prompt flow.

    ![Перегляд завдання донавчання.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.uk.png)

### Розгортання донавченої моделі Phi-3

Щоб інтегрувати донавчену модель Phi-3 з Prompt flow, потрібно розгорнути модель, щоб зробити її доступною для інференсу в реальному часі. Цей процес включає реєстрацію моделі, створення онлайн-ендпоінту та розгортання моделі.

У цьому завданні ви:

- Зареєструєте донавчену модель у робочому середовищі Azure Machine Learning.
- Створите онлайн-ендпоінт.
- Розгорнете зареєстровану донавчену модель Phi-3.

#### Реєстрація донавченої моделі

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виберіть робоче середовище Azure Machine Learning, яке ви створили.

    ![Виберіть створене робоче середовище.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.uk.png)

1. Виберіть **Models** у лівій панелі.
1. Виберіть **+ Register**.
1. Виберіть **From a job output**.

    ![Реєстрація моделі.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.uk.png)

1. Виберіть створене вами завдання.

    ![Виберіть завдання.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.uk.png)

1. Виберіть **Next**.

1. Виберіть тип моделі **MLflow**.

1. Переконайтеся, що вибрано **Job output**; це має бути вибрано автоматично.

    ![Виберіть вихідні дані.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.uk.png)

2. Виберіть **Next**.

3. Виберіть **Register**.

    ![Виберіть реєстрацію.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.uk.png)

4. Ви можете переглянути зареєстровану модель, перейшовши до меню **Models** у лівій панелі.

    ![Зареєстрована модель.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.uk.png)

#### Розгортання донавченої моделі

1. Перейдіть до робочого середовища Azure Machine Learning, яке ви створили.

1. Виберіть **Endpoints** у лівій панелі.

1. Виберіть **Real-time endpoints** у навігаційному меню.

    ![Створення ендпоінту.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.uk.png)

1. Виберіть **Create**.

1. Виберіть зареєстровану модель, яку ви створили.

    ![Виберіть зареєстровану модель.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.uk.png)

1. Виберіть **Select**.

1. Виконайте наступні дії:

    - Виберіть **Virtual machine** як *Standard_NC6s_v3*.
    - Виберіть кількість інстансів, яку хочете використовувати, наприклад, *1*.
    - Виберіть **Endpoint** як **New** для створення нового ендпоінту.
    - Введіть унікальне ім’я для **Endpoint name**.
    - Введіть унікальне ім’я для **Deployment name**.

    ![Заповніть налаштування розгортання.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.uk.png)

1. Виберіть **Deploy**.

> [!WARNING]
> Щоб уникнути додаткових витрат, обов’язково видаліть створений ендпоінт у робочому середовищі Azure Machine Learning.
>

#### Перевірка статусу розгортання в Azure Machine Learning Workspace

1. Перейдіть до робочого середовища Azure Machine Learning, яке ви створили.

1. Виберіть **Endpoints** у лівій панелі.

1. Виберіть створений вами ендпоінт.

    ![Виберіть ендпоінти](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.uk.png)

1. На цій сторінці ви можете керувати ендпоінтами під час процесу розгортання.

> [!NOTE]
> Після завершення розгортання переконайтеся, що **Live traffic** встановлено на **100%**. Якщо ні, виберіть **Update traffic**, щоб налаштувати трафік. Зверніть увагу, що тестувати модель неможливо, якщо трафік встановлено на 0%.
>
> ![Налаштування трафіку.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.uk.png)
>

## Сценарій 3: Інтеграція з Prompt flow та спілкування з вашою кастомною моделлю в Azure AI Foundry

### Інтеграція кастомної моделі Phi-3 з Prompt flow

Після успішного розгортання донавченої моделі ви можете інтегрувати її з Prompt Flow, щоб використовувати модель у реальних додатках, що дозволяє виконувати різноманітні інтерактивні завдання з вашою кастомною моделлю Phi-3.

У цьому завданні ви:

- Створите Azure AI Foundry Hub.
- Створите проект Azure AI Foundry.
- Створите Prompt flow.
- Додасте кастомне підключення для донавченої моделі Phi-3.
- Налаштуєте Prompt flow для спілкування з вашою кастомною моделлю Phi-3.
> [!NOTE]
> Ви також можете інтегруватися з Promptflow, використовуючи Azure ML Studio. Той самий процес інтеграції можна застосувати до Azure ML Studio.
#### Створення Azure AI Foundry Hub

Спочатку потрібно створити Hub перед створенням Проєкту. Hub працює як Група ресурсів, дозволяючи організовувати та керувати кількома Проєктами в Azure AI Foundry.

1. Перейдіть на [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Виберіть **All hubs** у лівій вкладці.

1. Виберіть **+ New hub** у навігаційному меню.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.uk.png)

1. Виконайте наступні дії:

    - Введіть **Hub name**. Він має бути унікальним.
    - Виберіть вашу Azure **Subscription**.
    - Виберіть **Resource group** для використання (створіть нову, якщо потрібно).
    - Виберіть **Location**, яку хочете використовувати.
    - Виберіть **Connect Azure AI Services** для підключення (створіть нову, якщо потрібно).
    - Виберіть **Connect Azure AI Search** і оберіть **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.uk.png)

1. Натисніть **Next**.

#### Створення Azure AI Foundry Проєкту

1. У створеному Hub виберіть **All projects** у лівій вкладці.

1. Виберіть **+ New project** у навігаційному меню.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.uk.png)

1. Введіть **Project name**. Він має бути унікальним.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.uk.png)

1. Натисніть **Create a project**.

#### Додавання кастомного підключення для тонко налаштованої моделі Phi-3

Щоб інтегрувати вашу кастомну модель Phi-3 з Prompt flow, потрібно зберегти endpoint і ключ моделі у кастомному підключенні. Це забезпечить доступ до вашої моделі Phi-3 у Prompt flow.

#### Встановлення api key та endpoint uri для тонко налаштованої моделі Phi-3

1. Перейдіть на [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Перейдіть до робочого простору Azure Machine learning, який ви створили.

1. Виберіть **Endpoints** у лівій вкладці.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.uk.png)

1. Виберіть створений вами endpoint.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.uk.png)

1. Виберіть **Consume** у навігаційному меню.

1. Скопіюйте ваш **REST endpoint** та **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.uk.png)

#### Додавання кастомного підключення

1. Перейдіть на [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Перейдіть до створеного вами проєкту Azure AI Foundry.

1. У створеному Проєкті виберіть **Settings** у лівій вкладці.

1. Виберіть **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.uk.png)

1. Виберіть **Custom keys** у навігаційному меню.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.uk.png)

1. Виконайте наступні дії:

    - Виберіть **+ Add key value pairs**.
    - Для імені ключа введіть **endpoint** і вставте скопійований endpoint з Azure ML Studio у поле значення.
    - Знову виберіть **+ Add key value pairs**.
    - Для імені ключа введіть **key** і вставте скопійований ключ з Azure ML Studio у поле значення.
    - Після додавання ключів виберіть **is secret**, щоб приховати ключ від відображення.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.uk.png)

1. Натисніть **Add connection**.

#### Створення Prompt flow

Ви додали кастомне підключення в Azure AI Foundry. Тепер створимо Prompt flow за наступними кроками. Потім ви підключите цей Prompt flow до кастомного підключення, щоб використовувати тонко налаштовану модель у Prompt flow.

1. Перейдіть до створеного вами проєкту Azure AI Foundry.

1. Виберіть **Prompt flow** у лівій вкладці.

1. Виберіть **+ Create** у навігаційному меню.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.uk.png)

1. Виберіть **Chat flow** у навігаційному меню.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.uk.png)

1. Введіть **Folder name** для використання.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.uk.png)

2. Натисніть **Create**.

#### Налаштування Prompt flow для спілкування з вашою кастомною моделлю Phi-3

Потрібно інтегрувати тонко налаштовану модель Phi-3 у Prompt flow. Однак існуючий Prompt flow не призначений для цього, тому його потрібно переробити, щоб забезпечити інтеграцію кастомної моделі.

1. У Prompt flow виконайте наступні дії для перебудови існуючого потоку:

    - Виберіть **Raw file mode**.
    - Видаліть увесь існуючий код у файлі *flow.dag.yml*.
    - Додайте наступний код у файл *flow.dag.yml*.

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

    - Натисніть **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.uk.png)

1. Додайте наступний код у файл *integrate_with_promptflow.py* для використання кастомної моделі Phi-3 у Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.uk.png)

> [!NOTE]
> Для детальнішої інформації про використання Prompt flow в Azure AI Foundry зверніться до [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Виберіть **Chat input**, **Chat output**, щоб увімкнути чат з вашою моделлю.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.uk.png)

1. Тепер ви готові спілкуватися з вашою кастомною моделлю Phi-3. У наступному завданні ви дізнаєтеся, як запустити Prompt flow і використовувати його для спілкування з тонко налаштованою моделлю Phi-3.

> [!NOTE]
>
> Перебудований потік має виглядати, як на зображенні нижче:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.uk.png)
>

### Спілкування з вашою кастомною моделлю Phi-3

Тепер, коли ви тонко налаштували та інтегрували кастомну модель Phi-3 з Prompt flow, ви готові почати взаємодію з нею. Це завдання допоможе вам налаштувати та розпочати чат з моделлю через Prompt flow. Дотримуючись цих кроків, ви зможете повністю використовувати можливості вашої тонко налаштованої моделі Phi-3 для різних завдань і розмов.

- Спілкуйтеся з вашою кастомною моделлю Phi-3 за допомогою Prompt flow.

#### Запуск Prompt flow

1. Виберіть **Start compute sessions**, щоб запустити Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.uk.png)

1. Виберіть **Validate and parse input**, щоб оновити параметри.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.uk.png)

1. Виберіть **Value** для **connection**, що відповідає створеному кастомному підключенню. Наприклад, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.uk.png)

#### Спілкування з вашою кастомною моделлю

1. Виберіть **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.uk.png)

1. Ось приклад результатів: тепер ви можете спілкуватися з вашою кастомною моделлю Phi-3. Рекомендується ставити питання, базуючись на даних, використаних для тонкого налаштування.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.uk.png)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.