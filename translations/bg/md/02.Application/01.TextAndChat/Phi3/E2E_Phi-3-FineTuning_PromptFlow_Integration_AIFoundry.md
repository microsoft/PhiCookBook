<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:57:44+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "bg"
}
-->
# Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry

Този краен (E2E) пример е базиран на ръководството "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" от Microsoft Tech Community. Той представя процесите на фина настройка, разгръщане и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry. За разлика от E2E примера "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", който включваше изпълнение на код локално, това ръководство се фокусира изцяло върху фина настройка и интеграция на вашия модел в Azure AI / ML Studio.

## Преглед

В този E2E пример ще научите как да фино настроите Phi-3 модела и да го интегрирате с Prompt flow в Azure AI Foundry. Използвайки Azure AI / ML Studio, ще създадете работен процес за разгръщане и използване на персонализирани AI модели. Този E2E пример е разделен на три сценария:

**Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка**

**Сценарий 2: Фина настройка на Phi-3 модела и разгръщане в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и чат с вашия персонализиран модел в Azure AI Foundry**

Ето един преглед на този E2E пример.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.bg.png)

### Съдържание

1. **[Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Създаване на Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Заявка за GPU квоти в Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Добавяне на ролево назначение](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Настройка на проект](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Подготовка на набор от данни за фина настройка](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 2: Фина настройка на Phi-3 модел и разгръщане в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Фина настройка на Phi-3 модела](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Разгръщане на фино настроения Phi-3 модел](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 3: Интеграция с Prompt flow и чат с вашия персонализиран модел в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Интегриране на персонализирания Phi-3 модел с Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Чат с вашия персонализиран Phi-3 модел](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка

### Създаване на Azure Machine Learning Workspace

1. Въведете *azure machine learning* в **лентата за търсене** в горната част на портала и изберете **Azure Machine Learning** от появилите се опции.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.bg.png)

2. Изберете **+ Create** от навигационното меню.

3. Изберете **New workspace** от навигационното меню.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.bg.png)

4. Изпълнете следните задачи:

    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате (създайте нова, ако е необходимо).
    - Въведете **Workspace Name**. Трябва да е уникално име.
    - Изберете **Region**, която желаете да използвате.
    - Изберете **Storage account**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Key vault**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Application insights**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Container registry**, която да използвате (създайте нова, ако е необходимо).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.bg.png)

5. Изберете **Review + Create**.

6. Изберете **Create**.

### Заявка за GPU квоти в Azure Subscription

В това ръководство ще научите как да фино настроите и разположите Phi-3 модел, използвайки GPU-та. За фина настройка ще използвате *Standard_NC24ads_A100_v4* GPU, който изисква заявка за квота. За разгръщане ще използвате *Standard_NC6s_v3* GPU, който също изисква заявка за квота.

> [!NOTE]
>
> Само абонаментите от тип Pay-As-You-Go (стандартен тип абонамент) имат право на GPU ресурси; абонаментите с ползи в момента не се поддържат.
>

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изпълнете следните стъпки, за да заявите квота за *Standard NCADSA100v4 Family*:

    - Изберете **Quota** от лявата странична лента.
    - Изберете **Virtual machine family**, която да използвате. Например, изберете **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, която включва *Standard_NC24ads_A100_v4* GPU.
    - Изберете **Request quota** от навигационното меню.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.bg.png)

    - В страницата за заявка на квота въведете **New cores limit**, който желаете да използвате. Например, 24.
    - В страницата за заявка на квота изберете **Submit**, за да подадете заявката за GPU квота.

1. Изпълнете следните стъпки, за да заявите квота за *Standard NCSv3 Family*:

    - Изберете **Quota** от лявата странична лента.
    - Изберете **Virtual machine family**, която да използвате. Например, изберете **Standard NCSv3 Family Cluster Dedicated vCPUs**, която включва *Standard_NC6s_v3* GPU.
    - Изберете **Request quota** от навигационното меню.
    - В страницата за заявка на квота въведете **New cores limit**, който желаете да използвате. Например, 24.
    - В страницата за заявка на квота изберете **Submit**, за да подадете заявката за GPU квота.

### Добавяне на ролево назначение

За да фино настроите и разположите моделите си, първо трябва да създадете User Assigned Managed Identity (UAI) и да ѝ присвоите подходящите разрешения. Тази UAI ще се използва за удостоверяване по време на разгръщането.

#### Създаване на User Assigned Managed Identity (UAI)

1. Въведете *managed identities* в **лентата за търсене** в горната част на портала и изберете **Managed Identities** от появилите се опции.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.bg.png)

1. Изберете **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.bg.png)

1. Изпълнете следните задачи:

    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Region**, която желаете да използвате.
    - Въведете **Name**. Трябва да е уникално име.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.bg.png)

1. Изберете **Review + create**.

1. Изберете **+ Create**.

#### Добавяне на роля Contributor към Managed Identity

1. Отидете до ресурса Managed Identity, който създадохте.

1. Изберете **Azure role assignments** от лявата странична лента.

1. Изберете **+Add role assignment** от навигационното меню.

1. В страницата Add role assignment изпълнете следните задачи:
    - Изберете **Scope** на **Resource group**.
    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате.
    - Изберете **Role** на **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.bg.png)

2. Изберете **Save**.

#### Добавяне на роля Storage Blob Data Reader към Managed Identity

1. Въведете *storage accounts* в **лентата за търсене** в горната част на портала и изберете **Storage accounts** от появилите се опции.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.bg.png)

1. Изберете storage акаунта, свързан с Azure Machine Learning workspace, който създадохте. Например, *finetunephistorage*.

1. Изпълнете следните стъпки, за да отидете на страницата Add role assignment:

    - Отидете до Azure Storage акаунта, който създадохте.
    - Изберете **Access Control (IAM)** от лявата странична лента.
    - Изберете **+ Add** от навигационното меню.
    - Изберете **Add role assignment** от навигационното меню.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.bg.png)

1. В страницата Add role assignment изпълнете следните задачи:

    - В страницата Role въведете *Storage Blob Data Reader* в **лентата за търсене** и изберете **Storage Blob Data Reader** от появилите се опции.
    - В страницата Role изберете **Next**.
    - В страницата Members изберете **Assign access to** **Managed identity**.
    - В страницата Members изберете **+ Select members**.
    - В страницата Select managed identities изберете вашия Azure **Subscription**.
    - В страницата Select managed identities изберете **Managed identity** на **Manage Identity**.
    - В страницата Select managed identities изберете Manage Identity, който създадохте. Например, *finetunephi-managedidentity*.
    - В страницата Select managed identities изберете **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.bg.png)

1. Изберете **Review + assign**.

#### Добавяне на роля AcrPull към Managed Identity

1. Въведете *container registries* в **лентата за търсене** в горната част на портала и изберете **Container registries** от появилите се опции.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.bg.png)

1. Изберете container registry, свързан с Azure Machine Learning workspace. Например, *finetunephicontainerregistry*

1. Изпълнете следните стъпки, за да отидете на страницата Add role assignment:

    - Изберете **Access Control (IAM)** от лявата странична лента.
    - Изберете **+ Add** от навигационното меню.
    - Изберете **Add role assignment** от навигационното меню.

1. В страницата Add role assignment изпълнете следните задачи:

    - В страницата Role въведете *AcrPull* в **лентата за търсене** и изберете **AcrPull** от появилите се опции.
    - В страницата Role изберете **Next**.
    - В страницата Members изберете **Assign access to** **Managed identity**.
    - В страницата Members изберете **+ Select members**.
    - В страницата Select managed identities изберете вашия Azure **Subscription**.
    - В страницата Select managed identities изберете **Managed identity** на **Manage Identity**.
    - В страницата Select managed identities изберете Manage Identity, който създадохте. Например, *finetunephi-managedidentity*.
    - В страницата Select managed identities изберете **Select**.
    - Изберете **Review + assign**.

### Настройка на проект

За да изтеглите необходимите набори от данни за фина настройка, ще настроите локална среда.

В това упражнение ще:

- Създадете папка, в която да работите.
- Създадете виртуална среда.
- Инсталирате необходимите пакети.
- Създадете файл *download_dataset.py* за изтегляне на набора от данни.

#### Създаване на папка, в която да работите

1. Отворете терминал и въведете следната команда, за да създадете папка с име *finetune-phi* в подразбиращата се директория.

    ```console
    mkdir finetune-phi
    ```

2. Въведете следната команда в терминала, за да навигирате до папката *finetune-phi*, която създадохте.
#### Създаване на виртуална среда

1. Въведете следната команда в терминала, за да създадете виртуална среда с име *.venv*.

    ```console
    python -m venv .venv
    ```

2. Въведете следната команда в терминала, за да активирате виртуалната среда.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Ако всичко е наред, трябва да видите *(.venv)* преди командния ред.

#### Инсталиране на необходимите пакети

1. Въведете следните команди в терминала, за да инсталирате необходимите пакети.

    ```console
    pip install datasets==2.19.1
    ```

#### Създаване на `download_dataset.py`

> [!NOTE]
> Пълна структура на папките:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Отворете **Visual Studio Code**.

1. Изберете **File** от менюто.

1. Изберете **Open Folder**.

1. Изберете папката *finetune-phi*, която сте създали, намираща се в *C:\Users\yourUserName\finetune-phi*.

    ![Изберете папката, която сте създали.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.bg.png)

1. В лявата част на Visual Studio Code, кликнете с десен бутон и изберете **New File**, за да създадете нов файл с име *download_dataset.py*.

    ![Създайте нов файл.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.bg.png)

### Подготовка на датасета за фино настройване

В това упражнение ще стартирате файла *download_dataset.py*, за да изтеглите датасетите *ultrachat_200k* в локалната си среда. След това ще използвате тези датасети, за да фино настроите модела Phi-3 в Azure Machine Learning.

В това упражнение ще:

- Добавите код във файла *download_dataset.py* за изтегляне на датасетите.
- Стартирате файла *download_dataset.py*, за да изтеглите датасетите в локалната си среда.

#### Изтеглете своя датасет с помощта на *download_dataset.py*

1. Отворете файла *download_dataset.py* във Visual Studio Code.

1. Добавете следния код във файла *download_dataset.py*.

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

1. Въведете следната команда в терминала, за да стартирате скрипта и изтеглите датасета в локалната си среда.

    ```console
    python download_dataset.py
    ```

1. Проверете дали датасетите са запазени успешно в локалната директория *finetune-phi/data*.

> [!NOTE]
>
> #### Забележка относно размера на датасета и времето за фино настройване
>
> В този урок използвате само 1% от датасета (`split='train[:1%]'`). Това значително намалява обема на данните, ускорявайки както качването, така и процеса на фино настройване. Можете да коригирате процента, за да намерите подходящия баланс между времето за обучение и представянето на модела. Използването на по-малък поднабор от датасета намалява времето за фино настройване, което прави процеса по-лесно управляем за урок.

## Сценарий 2: Фино настройване на модела Phi-3 и разгръщане в Azure Machine Learning Studio

### Фино настройване на модела Phi-3

В това упражнение ще фино настроите модела Phi-3 в Azure Machine Learning Studio.

В това упражнение ще:

- Създадете компютърен клъстер за фино настройване.
- Фино настроите модела Phi-3 в Azure Machine Learning Studio.

#### Създаване на компютърен клъстер за фино настройване

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете **Compute** от лявата странична лента.

1. Изберете **Compute clusters** от навигационното меню.

1. Изберете **+ New**.

    ![Изберете compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Region**, който искате да използвате.
    - Изберете **Virtual machine tier** на **Dedicated**.
    - Изберете **Virtual machine type** на **GPU**.
    - Филтрирайте **Virtual machine size** на **Select from all options**.
    - Изберете **Virtual machine size** на **Standard_NC24ads_A100_v4**.

    ![Създаване на клъстер.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.bg.png)

1. Изберете **Next**.

1. Изпълнете следните задачи:

    - Въведете **Compute name**. Трябва да е уникално име.
    - Изберете **Minimum number of nodes** на **0**.
    - Изберете **Maximum number of nodes** на **1**.
    - Изберете **Idle seconds before scale down** на **120**.

    ![Създаване на клъстер.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.bg.png)

1. Изберете **Create**.

#### Фино настройване на модела Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете Azure Machine Learning workspace, който сте създали.

    ![Изберете workspace, който сте създали.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Model catalog** от лявата странична лента.
    - Въведете *phi-3-mini-4k* в **search bar** и изберете **Phi-3-mini-4k-instruct** от появилите се опции.

    ![Въведете phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.bg.png)

1. Изберете **Fine-tune** от навигационното меню.

    ![Изберете fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Select task type** на **Chat completion**.
    - Изберете **+ Select data**, за да качите **Training data**.
    - Изберете типа качване на Validation data на **Provide different validation data**.
    - Изберете **+ Select data**, за да качите **Validation data**.

    ![Попълнете страницата за фино настройване.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.bg.png)

    > [!TIP]
    >
    > Можете да изберете **Advanced settings**, за да персонализирате конфигурации като **learning_rate** и **lr_scheduler_type**, за да оптимизирате процеса на фино настройване според вашите нужди.

1. Изберете **Finish**.

1. В това упражнение успешно фино настроихте модела Phi-3 с помощта на Azure Machine Learning. Моля, имайте предвид, че процесът на фино настройване може да отнеме значително време. След стартиране на задачата за фино настройване, трябва да изчакате тя да завърши. Можете да следите статуса на задачата, като отидете в раздела Jobs в лявата част на Azure Machine Learning Workspace. В следващата серия ще разгърнете фино настроения модел и ще го интегрирате с Prompt flow.

    ![Вижте задачата за фино настройване.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.bg.png)

### Разгръщане на фино настроения модел Phi-3

За да интегрирате фино настроения модел Phi-3 с Prompt flow, трябва да разположите модела, за да бъде достъпен за реално време. Този процес включва регистриране на модела, създаване на онлайн крайна точка и разгръщане на модела.

В това упражнение ще:

- Регистрирате фино настроения модел в Azure Machine Learning workspace.
- Създадете онлайн крайна точка.
- Разгърнете регистрирания фино настроен модел Phi-3.

#### Регистриране на фино настроения модел

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете Azure Machine Learning workspace, който сте създали.

    ![Изберете workspace, който сте създали.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.bg.png)

1. Изберете **Models** от лявата странична лента.

1. Изберете **+ Register**.

1. Изберете **From a job output**.

    ![Регистриране на модел.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.bg.png)

1. Изберете задачата, която сте създали.

    ![Изберете задача.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.bg.png)

1. Изберете **Next**.

1. Изберете **Model type** на **MLflow**.

1. Уверете се, че **Job output** е избрано; това трябва да стане автоматично.

    ![Изберете изход.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.bg.png)

2. Изберете **Next**.

3. Изберете **Register**.

    ![Изберете регистриране.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.bg.png)

4. Можете да видите регистрирания модел, като отидете в менюто **Models** от лявата странична лента.

    ![Регистриран модел.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.bg.png)

#### Разгръщане на фино настроения модел

1. Отидете в Azure Machine Learning workspace, който сте създали.

1. Изберете **Endpoints** от лявата странична лента.

1. Изберете **Real-time endpoints** от навигационното меню.

    ![Създаване на крайна точка.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.bg.png)

1. Изберете **Create**.

1. Изберете регистрирания модел, който сте създали.

    ![Изберете регистриран модел.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.bg.png)

1. Изберете **Select**.

1. Изпълнете следните задачи:

    - Изберете **Virtual machine** на *Standard_NC6s_v3*.
    - Изберете броя на инстанциите, които искате да използвате. Например, *1*.
    - Изберете **Endpoint** на **New**, за да създадете нова крайна точка.
    - Въведете **Endpoint name**. Трябва да е уникално име.
    - Въведете **Deployment name**. Трябва да е уникално име.

    ![Попълнете настройките за разгръщане.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.bg.png)

1. Изберете **Deploy**.

> [!WARNING]
> За да избегнете допълнителни такси по акаунта си, уверете се, че сте изтрили създадената крайна точка в Azure Machine Learning workspace.
>

#### Проверка на статуса на разгръщане в Azure Machine Learning Workspace

1. Отидете в Azure Machine Learning workspace, който сте създали.

1. Изберете **Endpoints** от лявата странична лента.

1. Изберете крайната точка, която сте създали.

    ![Изберете крайни точки](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.bg.png)

1. На тази страница можете да управлявате крайните точки по време на процеса на разгръщане.

> [!NOTE]
> След като разгръщането приключи, уверете се, че **Live traffic** е настроен на **100%**. Ако не е, изберете **Update traffic**, за да коригирате настройките на трафика. Обърнете внимание, че не можете да тествате модела, ако трафикът е настроен на 0%.
>
> ![Настройте трафика.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.bg.png)
>

## Сценарий 3: Интеграция с Prompt flow и чат с вашия персонализиран модел в Azure AI Foundry

### Интегриране на персонализирания модел Phi-3 с Prompt flow

След успешно разгръщане на фино настроения модел, вече можете да го интегрирате с Prompt Flow, за да използвате модела в реално време, позволявайки разнообразни интерактивни задачи с вашия персонализиран модел Phi-3.

В това упражнение ще:

- Създадете Azure AI Foundry Hub.
- Създадете Azure AI Foundry Project.
- Създадете Prompt flow.
- Добавите персонализирана връзка за фино настроения модел Phi-3.
- Настроите Prompt flow за чат с вашия персонализиран модел Phi-3.
> [!NOTE]
> Можете също да интегрирате с Promptflow чрез Azure ML Studio. Същият процес на интеграция може да се приложи и за Azure ML Studio.
#### Създаване на Azure AI Foundry Hub

Трябва да създадете Hub преди да създадете Проект. Hub действа като Resource Group, позволявайки ви да организирате и управлявате множество Проекти в Azure AI Foundry.

1. Посетете [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Изберете **All hubs** от лявото меню.

1. Изберете **+ New hub** от навигационното меню.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.bg.png)

1. Изпълнете следните задачи:

    - Въведете **Hub name**. Трябва да е уникално име.
    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Location**, която желаете да използвате.
    - Изберете **Connect Azure AI Services**, които да използвате (създайте нови, ако е необходимо).
    - Изберете **Connect Azure AI Search** и изберете **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.bg.png)

1. Изберете **Next**.

#### Създаване на Azure AI Foundry Проект

1. В създадения от вас Hub изберете **All projects** от лявото меню.

1. Изберете **+ New project** от навигационното меню.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.bg.png)

1. Въведете **Project name**. Трябва да е уникално име.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.bg.png)

1. Изберете **Create a project**.

#### Добавяне на персонализирана връзка за финно настроения модел Phi-3

За да интегрирате вашия персонализиран модел Phi-3 с Prompt flow, трябва да запазите endpoint-а и ключа на модела в персонализирана връзка. Тази настройка осигурява достъп до вашия персонализиран Phi-3 модел в Prompt flow.

#### Настройване на api ключ и endpoint uri на финно настроения модел Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Отидете в Azure Machine learning workspace, който сте създали.

1. Изберете **Endpoints** от лявото меню.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.bg.png)

1. Изберете endpoint-а, който сте създали.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.bg.png)

1. Изберете **Consume** от навигационното меню.

1. Копирайте вашия **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.bg.png)

#### Добавяне на персонализираната връзка

1. Посетете [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Отидете в Azure AI Foundry проекта, който сте създали.

1. В проекта, който сте създали, изберете **Settings** от лявото меню.

1. Изберете **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.bg.png)

1. Изберете **Custom keys** от навигационното меню.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.bg.png)

1. Изпълнете следните задачи:

    - Изберете **+ Add key value pairs**.
    - За името на ключа въведете **endpoint** и поставете endpoint-а, който копирахте от Azure ML Studio, в полето за стойност.
    - Изберете отново **+ Add key value pairs**.
    - За името на ключа въведете **key** и поставете ключа, който копирахте от Azure ML Studio, в полето за стойност.
    - След добавяне на ключовете, маркирайте **is secret**, за да предотвратите излагането на ключа.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.bg.png)

1. Изберете **Add connection**.

#### Създаване на Prompt flow

Вече добавихте персонализирана връзка в Azure AI Foundry. Сега нека създадем Prompt flow, като следваме следните стъпки. След това ще свържете този Prompt flow с персонализираната връзка, за да можете да използвате финно настроения модел в Prompt flow.

1. Отидете в Azure AI Foundry проекта, който сте създали.

1. Изберете **Prompt flow** от лявото меню.

1. Изберете **+ Create** от навигационното меню.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.bg.png)

1. Изберете **Chat flow** от навигационното меню.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.bg.png)

1. Въведете **Folder name**, който да използвате.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.bg.png)

2. Изберете **Create**.

#### Настройване на Prompt flow за чат с вашия персонализиран модел Phi-3

Трябва да интегрирате финно настроения модел Phi-3 в Prompt flow. Въпреки това, съществуващият Prompt flow не е предназначен за тази цел. Затова трябва да преработите Prompt flow, за да позволите интеграцията на персонализирания модел.

1. В Prompt flow изпълнете следните задачи, за да изградите наново съществуващия flow:

    - Изберете **Raw file mode**.
    - Изтрийте целия съществуващ код във файла *flow.dag.yml*.
    - Добавете следния код във файла *flow.dag.yml*.

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

    - Изберете **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.bg.png)

1. Добавете следния код във файла *integrate_with_promptflow.py*, за да използвате персонализирания модел Phi-3 в Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.bg.png)

> [!NOTE]
> За по-подробна информация относно използването на Prompt flow в Azure AI Foundry, можете да се обърнете към [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изберете **Chat input**, **Chat output**, за да активирате чата с вашия модел.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.bg.png)

1. Сега сте готови да чатите с вашия персонализиран модел Phi-3. В следващото упражнение ще научите как да стартирате Prompt flow и да го използвате за чат с вашия финно настроен модел Phi-3.

> [!NOTE]
>
> Преработеният flow трябва да изглежда като изображението по-долу:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.bg.png)
>

### Чат с вашия персонализиран модел Phi-3

След като сте финно настроили и интегрирали вашия персонализиран модел Phi-3 с Prompt flow, вече сте готови да започнете взаимодействие с него. Това упражнение ще ви преведе през процеса на настройка и стартиране на чат с вашия модел чрез Prompt flow. Следвайки тези стъпки, ще можете да използвате пълноценно възможностите на вашия финно настроен модел Phi-3 за различни задачи и разговори.

- Чат с вашия персонализиран модел Phi-3 чрез Prompt flow.

#### Стартиране на Prompt flow

1. Изберете **Start compute sessions**, за да стартирате Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.bg.png)

1. Изберете **Validate and parse input**, за да обновите параметрите.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.bg.png)

1. Изберете **Value** на **connection** към персонализираната връзка, която създадохте. Например, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.bg.png)

#### Чат с вашия персонализиран модел

1. Изберете **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.bg.png)

1. Ето пример за резултатите: Сега можете да чатите с вашия персонализиран модел Phi-3. Препоръчително е да задавате въпроси, базирани на данните, използвани за финното настройване.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.bg.png)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.