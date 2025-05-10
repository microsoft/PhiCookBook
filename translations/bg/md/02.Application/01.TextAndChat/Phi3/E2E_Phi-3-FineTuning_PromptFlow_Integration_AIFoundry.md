<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:25:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "bg"
}
-->
# Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry

Този краен (E2E) пример е базиран на ръководството "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" от Microsoft Tech Community. То представя процесите по фина настройка, внедряване и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry. За разлика от E2E примера "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", който включваше локално изпълнение на код, това ръководство е изцяло фокусирано върху фина настройка и интеграция на вашия модел в Azure AI / ML Studio.

## Преглед

В този E2E пример ще научите как да фино настроите Phi-3 модел и да го интегрирате с Prompt flow в Azure AI Foundry. Използвайки Azure AI / ML Studio, ще създадете работен процес за внедряване и използване на персонализирани AI модели. Този E2E пример е разделен на три сценария:

**Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка**

**Сценарий 2: Фина настройка на Phi-3 модела и внедряване в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и чат с вашия персонализиран модел в Azure AI Foundry**

Ето преглед на този E2E пример.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.bg.png)

### Съдържание

1. **[Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Създаване на Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Заявка за GPU квоти в Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Добавяне на ролево назначение](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Настройка на проект](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Подготовка на набор от данни за фина настройка](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 2: Фина настройка на Phi-3 модел и внедряване в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Фина настройка на Phi-3 модела](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Внедряване на фино настроения Phi-3 модел](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 3: Интеграция с Prompt flow и чат с вашия персонализиран модел в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Интеграция на персонализирания Phi-3 модел с Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Чат с вашия персонализиран Phi-3 модел](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарий 1: Настройка на Azure ресурси и подготовка за фина настройка

### Създаване на Azure Machine Learning Workspace

1. Въведете *azure machine learning* в **лентата за търсене** в горната част на портала и изберете **Azure Machine Learning** от показаните опции.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.bg.png)

2. Изберете **+ Create** от навигационното меню.

3. Изберете **New workspace** от навигационното меню.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.bg.png)

4. Изпълнете следните задачи:

    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате (създайте нова, ако е необходимо).
    - Въведете **Workspace Name**. Трябва да е уникално име.
    - Изберете **Region**, която желаете да използвате.
    - Изберете **Storage account**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Key vault**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Application insights**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Container registry**, която да използвате (създайте нова, ако е необходимо).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.bg.png)

5. Изберете **Review + Create**.

6. Изберете **Create**.

### Заявка за GPU квоти в Azure Subscription

В това ръководство ще научите как да фино настроите и внедрите Phi-3 модел, използвайки GPU. За фина настройка ще използвате GPU *Standard_NC24ads_A100_v4*, който изисква заявка за квота. За внедряване ще използвате GPU *Standard_NC6s_v3*, който също изисква заявка за квота.

> [!NOTE]
>
> Само абонаменти от тип Pay-As-You-Go (стандартен тип абонамент) имат право на GPU ресурси; абонаментите с ползи не се поддържат в момента.
>

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изпълнете следните стъпки, за да заявите квота за *Standard NCADSA100v4 Family*:

    - Изберете **Quota** от лявата странична лента.
    - Изберете **Virtual machine family**, която искате да използвате. Например, изберете **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, която включва GPU *Standard_NC24ads_A100_v4*.
    - Изберете **Request quota** от навигационното меню.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.bg.png)

    - В страницата за заявка на квота въведете **New cores limit**, който желаете да използвате. Например, 24.
    - В страницата за заявка на квота изберете **Submit**, за да изпратите заявката за GPU квота.

1. Изпълнете следните стъпки, за да заявите квота за *Standard NCSv3 Family*:

    - Изберете **Quota** от лявата странична лента.
    - Изберете **Virtual machine family**, която искате да използвате. Например, изберете **Standard NCSv3 Family Cluster Dedicated vCPUs**, която включва GPU *Standard_NC6s_v3*.
    - Изберете **Request quota** от навигационното меню.
    - В страницата за заявка на квота въведете **New cores limit**, който желаете да използвате. Например, 24.
    - В страницата за заявка на квота изберете **Submit**, за да изпратите заявката за GPU квота.

### Добавяне на ролево назначение

За да фино настроите и внедрите моделите си, първо трябва да създадете User Assigned Managed Identity (UAI) и да ѝ присвоите подходящите разрешения. Тази UAI ще се използва за удостоверяване по време на внедряването.

#### Създаване на User Assigned Managed Identity (UAI)

1. Въведете *managed identities* в **лентата за търсене** в горната част на портала и изберете **Managed Identities** от показаните опции.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.bg.png)

1. Изберете **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.bg.png)

1. Изпълнете следните задачи:

    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Region**, която желаете да използвате.
    - Въведете **Name**. Трябва да е уникално име.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.bg.png)

1. Изберете **Review + create**.

1. Изберете **+ Create**.

#### Добавяне на роля Contributor към Managed Identity

1. Отидете до създадения от вас Managed Identity ресурс.

1. Изберете **Azure role assignments** от лявата странична лента.

1. Изберете **+Add role assignment** от навигационното меню.

1. В страницата Add role assignment изпълнете следните задачи:
    - Изберете **Scope** на **Resource group**.
    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате.
    - Изберете **Role** на **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.bg.png)

2. Изберете **Save**.

#### Добавяне на роля Storage Blob Data Reader към Managed Identity

1. Въведете *storage accounts* в **лентата за търсене** в горната част на портала и изберете **Storage accounts** от показаните опции.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.bg.png)

1. Изберете storage акаунта, асоцииран с Azure Machine Learning workspace, който сте създали. Например, *finetunephistorage*.

1. Изпълнете следните стъпки, за да стигнете до страницата Add role assignment:

    - Отидете до създадения Azure Storage акаунт.
    - Изберете **Access Control (IAM)** от лявата странична лента.
    - Изберете **+ Add** от навигационното меню.
    - Изберете **Add role assignment** от навигационното меню.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.bg.png)

1. В страницата Add role assignment изпълнете следните задачи:

    - В полето Role въведете *Storage Blob Data Reader* в **лентата за търсене** и изберете **Storage Blob Data Reader** от показаните опции.
    - Изберете **Next**.
    - В страницата Members изберете **Assign access to** **Managed identity**.
    - Изберете **+ Select members**.
    - В страницата Select managed identities изберете вашия Azure **Subscription**.
    - Изберете **Managed identity** на **Manage Identity**.
    - Изберете създадената Manage Identity. Например, *finetunephi-managedidentity*.
    - Изберете **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.bg.png)

1. Изберете **Review + assign**.

#### Добавяне на роля AcrPull към Managed Identity

1. Въведете *container registries* в **лентата за търсене** в горната част на портала и изберете **Container registries** от показаните опции.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.bg.png)

1. Изберете container registry, асоцииран с Azure Machine Learning workspace. Например, *finetunephicontainerregistry*

1. Изпълнете следните стъпки, за да стигнете до страницата Add role assignment:

    - Изберете **Access Control (IAM)** от лявата странична лента.
    - Изберете **+ Add** от навигационното меню.
    - Изберете **Add role assignment** от навигационното меню.

1. В страницата Add role assignment изпълнете следните задачи:

    - В полето Role въведете *AcrPull* в **лентата за търсене** и изберете **AcrPull** от показаните опции.
    - Изберете **Next**.
    - В страницата Members изберете **Assign access to** **Managed identity**.
    - Изберете **+ Select members**.
    - В страницата Select managed identities изберете вашия Azure **Subscription**.
    - Изберете **Managed identity** на **Manage Identity**.
    - Изберете създадената Manage Identity. Например, *finetunephi-managedidentity*.
    - Изберете **Select**.
    - Изберете **Review + assign**.

### Настройка на проект

За да изтеглите необходимите набори от данни за фина настройка, ще настроите локална среда.

В това упражнение ще:

- Създадете папка, в която да работите.
- Създадете виртуална среда.
- Инсталирате необходимите пакети.
- Създадете файл *download_dataset.py* за изтегляне на набора от данни.

#### Създаване на папка, в която да работите

1. Отворете терминал и въведете следната команда, за да създадете папка с име *finetune-phi* в стандартната директория.

    ```console
    mkdir finetune-phi
    ```

2. Въведете следната команда в терминала, за да навигирате до създадената папка *finetune-phi*.

    ```console
    cd finetune-phi
    ```

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

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.bg.png)

1. В лявата част на Visual Studio Code, кликнете с десен бутон и изберете **New File**, за да създадете нов файл с име *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.bg.png)

### Подготовка на набор от данни за фина настройка

В това упражнение ще стартирате файла *download_dataset.py*, за да изтеглите набора от данни *ultrachat_200k* в локалната си среда. След това ще използвате този набор от данни за фина настройка на Phi-3 модела в Azure Machine Learning.

В това упражнение ще:

- Добавите код във файла *download_dataset.py* за изтегляне на набора от данни.
- Стартирате файла *download_dataset.py*, за да изтеглите набора от данни в локалната си среда.

#### Изтегляне на набора от данни с помощта на *download_dataset.py*

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

1. Въведете следната команда в терминала, за да стартирате скрипта и изтеглите набора от данни в локалната си среда.

    ```console
    python download_dataset.py
    ```

1. Проверете дали наборите от данни са запазени успешно в локалната директория *finetune-phi/data*.

> [!NOTE]
>
> #### Забележка относно размера на наб
1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете **Compute** от таба вляво.

1. Изберете **Compute clusters** от навигационното меню.

1. Изберете **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Region**, който искате да използвате.
    - Изберете **Virtual machine tier** на **Dedicated**.
    - Изберете **Virtual machine type** на **GPU**.
    - Филтрирайте **Virtual machine size** на **Select from all options**.
    - Изберете **Virtual machine size** на **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.bg.png)

1. Изберете **Next**.

1. Изпълнете следните задачи:

    - Въведете **Compute name**. Трябва да е уникално име.
    - Изберете **Minimum number of nodes** на **0**.
    - Изберете **Maximum number of nodes** на **1**.
    - Изберете **Idle seconds before scale down** на **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.bg.png)

1. Изберете **Create**.

#### Финна настройка на модела Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете създаденото Azure Machine Learning работно пространство.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Model catalog** от таба вляво.
    - Въведете *phi-3-mini-4k* в **search bar** и изберете **Phi-3-mini-4k-instruct** от появилите се опции.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.bg.png)

1. Изберете **Fine-tune** от навигационното меню.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.bg.png)

1. Изпълнете следните задачи:

    - Изберете **Select task type** на **Chat completion**.
    - Изберете **+ Select data** за качване на **Traning data**.
    - Изберете типа качване на Validation data на **Provide different validation data**.
    - Изберете **+ Select data** за качване на **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.bg.png)

    > [!TIP]
    >
    > Можете да изберете **Advanced settings**, за да персонализирате конфигурации като **learning_rate** и **lr_scheduler_type**, за да оптимизирате процеса на финна настройка според вашите нужди.

1. Изберете **Finish**.

1. В това упражнение успешно финно настроихте модела Phi-3 с помощта на Azure Machine Learning. Имайте предвид, че процесът на финна настройка може да отнеме значително време. След стартиране на задачата за финна настройка трябва да изчакате тя да завърши. Можете да следите статуса на задачата, като отидете в раздел Jobs вляво в работното пространство на Azure Machine Learning. В следващата серия ще разгледаме как да разположите финно настроения модел и да го интегрирате с Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.bg.png)

### Разполагане на финно настроения модел Phi-3

За да интегрирате финно настроения модел Phi-3 с Prompt flow, трябва да го разположите, за да бъде достъпен за реално време инференция. Този процес включва регистриране на модела, създаване на онлайн крайна точка и разполагане на модела.

В това упражнение ще:

- Регистрирате финно настроения модел в Azure Machine Learning работното пространство.
- Създадете онлайн крайна точка.
- Разположите регистрирания финно настроен модел Phi-3.

#### Регистриране на финно настроения модел

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете създаденото Azure Machine Learning работно пространство.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.bg.png)

1. Изберете **Models** от таба вляво.
1. Изберете **+ Register**.
1. Изберете **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.bg.png)

1. Изберете създадената от вас задача.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.bg.png)

1. Изберете **Next**.

1. Изберете **Model type** на **MLflow**.

1. Уверете се, че **Job output** е избрано; това трябва да стане автоматично.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.bg.png)

2. Изберете **Next**.

3. Изберете **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.bg.png)

4. Можете да видите регистрирания модел, като отидете в менюто **Models** от таба вляво.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.bg.png)

#### Разполагане на финно настроения модел

1. Отидете в създаденото Azure Machine Learning работно пространство.

1. Изберете **Endpoints** от таба вляво.

1. Изберете **Real-time endpoints** от навигационното меню.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.bg.png)

1. Изберете **Create**.

1. Изберете регистрирания модел, който създадохте.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.bg.png)

1. Изберете **Select**.

1. Изпълнете следните задачи:

    - Изберете **Virtual machine** на *Standard_NC6s_v3*.
    - Изберете броя на инстанциите, които искате да използвате, например *1*.
    - Изберете **Endpoint** на **New**, за да създадете крайна точка.
    - Въведете **Endpoint name**. Трябва да е уникално име.
    - Въведете **Deployment name**. Трябва да е уникално име.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.bg.png)

1. Изберете **Deploy**.

> [!WARNING]
> За да избегнете допълнителни такси, не забравяйте да изтриете създадената крайна точка в Azure Machine Learning работното пространство.
>

#### Проверка на статуса на разполагането в Azure Machine Learning Workspace

1. Отидете в създаденото Azure Machine Learning работно пространство.

1. Изберете **Endpoints** от таба вляво.

1. Изберете създадената крайна точка.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.bg.png)

1. На тази страница можете да управлявате крайните точки по време на процеса на разполагане.

> [!NOTE]
> След като разполагането приключи, уверете се, че **Live traffic** е настроен на **100%**. Ако не е, изберете **Update traffic**, за да коригирате настройките за трафик. Имайте предвид, че не можете да тествате модела, ако трафикът е зададен на 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.bg.png)
>

## Сценарий 3: Интегриране с Prompt flow и чат с вашия персонализиран модел в Azure AI Foundry

### Интегриране на персонализирания модел Phi-3 с Prompt flow

След успешното разполагане на финно настроения модел, вече можете да го интегрирате с Prompt Flow, за да използвате модела в реални приложения, позволявайки разнообразни интерактивни задачи с вашия персонализиран Phi-3 модел.

В това упражнение ще:

- Създадете Azure AI Foundry Hub.
- Създадете Azure AI Foundry Project.
- Създадете Prompt flow.
- Добавите персонализирана връзка за финно настроения модел Phi-3.
- Настроите Prompt flow за чат с вашия персонализиран модел Phi-3.

> [!NOTE]
> Можете също да интегрирате с Promptflow чрез Azure ML Studio. Същият процес на интеграция важи и за Azure ML Studio.

#### Създаване на Azure AI Foundry Hub

Трябва да създадете Hub преди да създадете Project. Hub действа като Resource Group, позволявайки ви да организирате и управлявате няколко проекта в Azure AI Foundry.

1. Посетете [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Изберете **All hubs** от таба вляво.

1. Изберете **+ New hub** от навигационното меню.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.bg.png)

1. Изпълнете следните задачи:

    - Въведете **Hub name**. Трябва да е уникално име.
    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която искате да използвате (създайте нова, ако е необходимо).
    - Изберете **Location**, която искате да използвате.
    - Изберете **Connect Azure AI Services**, която искате да използвате (създайте нова, ако е необходимо).
    - Изберете **Connect Azure AI Search** на **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.bg.png)

1. Изберете **Next**.

#### Създаване на Azure AI Foundry Project

1. В създадения от вас Hub изберете **All projects** от таба вляво.

1. Изберете **+ New project** от навигационното меню.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.bg.png)

1. Въведете **Project name**. Трябва да е уникално име.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.bg.png)

1. Изберете **Create a project**.

#### Добавяне на персонализирана връзка за финно настроения модел Phi-3

За да интегрирате персонализирания модел Phi-3 с Prompt flow, трябва да запишете крайна точка и ключ на модела в персонализирана връзка. Това осигурява достъп до вашия персонализиран Phi-3 модел в Prompt flow.

#### Настройка на api ключ и endpoint uri на финно настроения модел Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Отидете в създаденото Azure Machine Learning работно пространство.

1. Изберете **Endpoints** от таба вляво.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.bg.png)

1. Изберете създадената крайна точка.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.bg.png)

1. Изберете **Consume** от навигационното меню.

1. Копирайте вашия **REST endpoint** и **Primary key**.
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.bg.png)

#### Добавяне на персонализирана връзка

1. Посетете [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Отидете в проекта в Azure AI Foundry, който сте създали.

1. В проекта, който сте създали, изберете **Settings** от таба вляво.

1. Изберете **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.bg.png)

1. Изберете **Custom keys** от навигационното меню.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.bg.png)

1. Изпълнете следните задачи:

    - Изберете **+ Add key value pairs**.
    - За името на ключа въведете **endpoint** и поставете endpoint-а, който копирахте от Azure ML Studio, в полето за стойност.
    - Отново изберете **+ Add key value pairs**.
    - За името на ключа въведете **key** и поставете ключа, който копирахте от Azure ML Studio, в полето за стойност.
    - След като добавите ключовете, изберете **is secret**, за да предотвратите излагането на ключа.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.bg.png)

1. Изберете **Add connection**.

#### Създаване на Prompt flow

Вече добавихте персонализирана връзка в Azure AI Foundry. Сега нека създадем Prompt flow, като следвате стъпките по-долу. След това ще свържете този Prompt flow с персонализираната връзка, за да можете да използвате финно настроения модел в Prompt flow.

1. Отидете в проекта в Azure AI Foundry, който сте създали.

1. Изберете **Prompt flow** от таба вляво.

1. Изберете **+ Create** от навигационното меню.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.bg.png)

1. Изберете **Chat flow** от навигационното меню.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.bg.png)

1. Въведете **Folder name**, който искате да използвате.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.bg.png)

2. Изберете **Create**.

#### Настройване на Prompt flow за чат с вашия персонализиран Phi-3 модел

Трябва да интегрирате финно настроения Phi-3 модел в Prompt flow. Въпреки това, съществуващият Prompt flow не е предназначен за тази цел. Затова трябва да преработите Prompt flow, за да позволите интеграцията на персонализирания модел.

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.bg.png)

1. Добавете следния код във файла *integrate_with_promptflow.py*, за да използвате персонализирания Phi-3 модел в Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.bg.png)

> [!NOTE]
> За по-подробна информация относно използването на Prompt flow в Azure AI Foundry, може да се обърнете към [Prompt flow в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изберете **Chat input**, **Chat output**, за да активирате чата с вашия модел.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.bg.png)

1. Сега сте готови да чатите с вашия персонализиран Phi-3 модел. В следващото упражнение ще научите как да стартирате Prompt flow и да го използвате за чат с вашия финно настроен Phi-3 модел.

> [!NOTE]
>
> Преработеният flow трябва да изглежда като на следващата снимка:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.bg.png)
>

### Чат с вашия персонализиран Phi-3 модел

След като сте финно настроили и интегрирали вашия персонализиран Phi-3 модел с Prompt flow, вече сте готови да започнете взаимодействие с него. Това упражнение ще ви преведе през процеса на настройка и стартиране на чат с вашия модел чрез Prompt flow. Следвайки тези стъпки, ще можете пълноценно да използвате възможностите на финно настроения Phi-3 модел за различни задачи и разговори.

- Чат с вашия персонализиран Phi-3 модел чрез Prompt flow.

#### Стартиране на Prompt flow

1. Изберете **Start compute sessions**, за да стартирате Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.bg.png)

1. Изберете **Validate and parse input**, за да обновите параметрите.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.bg.png)

1. Изберете стойността на **connection** към персонализираната връзка, която сте създали. Например, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.bg.png)

#### Чат с вашия персонализиран модел

1. Изберете **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.bg.png)

1. Ето пример за резултатите: Сега можете да чатите с вашия персонализиран Phi-3 модел. Препоръчително е да задавате въпроси, базирани на данните, използвани за финно настройване.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.bg.png)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.