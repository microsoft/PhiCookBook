# Финна настройка и интеграция на персонализирани Phi-3 модели с Prompt flow в Microsoft Foundry

Този образец "от край до край" (E2E) е базиран на ръководството "[Финна настройка и интегриране на персонализирани Phi-3 модели с Prompt Flow в Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" от Microsoft Tech Community. Той представя процесите на финна настройка, разгръщане и интегриране на персонализирани Phi-3 модели с Prompt flow в Microsoft Foundry.
За разлика от образеца E2E, "[Финна настройка и интегриране на персонализирани Phi-3 модели с Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", който включваше изпълнение на код локално, този урок е съсредоточен изцяло върху финната настройка и интегриране на вашия модел в Azure AI / ML Studio.

## Преглед

В този образец E2E ще се научите как да настроите Phi-3 модела и как да го интегрирате с Prompt flow в Microsoft Foundry. Използвайки Azure AI / ML Studio, ще установите работен процес за разгръщане и използване на персонализирани AI модели. Този образец E2E е разделен на три сценария:

**Сценарий 1: Настройка на Azure ресурси и Подготовка за финна настройка**

**Сценарий 2: Финна настройка на Phi-3 модела и разгръщане в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и чат с вашия персонализиран модел в Microsoft Foundry**

Тук е преглед на този образец E2E.

![Phi-3-FineTuning_PromptFlow_Integration Преглед.](../../../../../../translated_images/bg/00-01-architecture.198ba0f1ae6d841a.webp)

### Съдържание

1. **[Сценарий 1: Настройка на Azure ресурси и Подготовка за финна настройка](#сценарий-1-настройка-на-azure-ресурси-и-подготовка-за-финна-настройка)**
    - [Създаване на Azure Machine Learning Workspace](#създаване-на-azure-machine-learning-workspace)
    - [Заявка за GPU квоти в Azure абонамент](#заявка-за-gpu-квоти-в-azure-абонамент)
    - [Добавяне на роля](#добавяне-на-роля)
    - [Настройване на проект](#настройване-на-проект)
    - [Подготовка на набор от данни за финна настройка](#подгответе-датасета-за-допълнително-обучение)

1. **[Сценарий 2: Финна настройка на Phi-3 модел и разгръщане в Azure Machine Learning Studio](#сценарий-2-дообучете-модела-phi-3-и-го-разгърнете-в-azure-machine-learning-studio)**
    - [Финна настройка на Phi-3 модела](#дообучете-модела-phi-3)
    - [Разгръщане на финно настроения Phi-3 модел](#разгръщане-на-дообучения-phi-3-модел)

1. **[Сценарий 3: Интеграция с Prompt flow и Чат с вашия персонализиран модел в Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Интегриране на персонализирания Phi-3 модел с Prompt flow](#интегриране-на-персонализирания-модел-phi-3-с-prompt-flow)
    - [Чат с вашия персонализиран Phi-3 модел](#чат-с-вашия-персонализиран-модел-phi-3)

## Сценарий 1: Настройка на Azure ресурси и Подготовка за финна настройка

### Създаване на Azure Machine Learning Workspace

1. Въведете *azure machine learning* в **лентата за търсене** в горната част на портала и изберете **Azure Machine Learning** от наличните опции.

    ![Въведете azure machine learning.](../../../../../../translated_images/bg/01-01-type-azml.acae6c5455e67b4b.webp)

2. Изберете **+ Създай** от навигационното меню.

3. Изберете **Нов Workspace** от навигационното меню.

    ![Изберете нов workspace.](../../../../../../translated_images/bg/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Извършете следните действия:

    - Изберете вашия Azure **Абонамент**.
    - Изберете **Група ресурси**, която да използвате (създайте нова, ако е необходимо).
    - Въведете **Име на Workspace**. Трябва да е уникална стойност.
    - Изберете **Регион**, който искате да използвате.
    - Изберете **Акаунт за съхранение**, който да използвате (създайте нов, ако е необходимо).
    - Изберете **Key vault**, който да използвате (създайте нов, ако е необходимо).
    - Изберете **Application insights**, който да използвате (създайте нов, ако е необходимо).
    - Изберете **Container registry**, който да използвате (създайте нов, ако е необходимо).

    ![Попълнете azure machine learning.](../../../../../../translated_images/bg/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Изберете **Преглед + Създай**.

6. Изберете **Създай**.

### Заявка за GPU квоти в Azure абонамент

В този урок ще научите как да направите финна настройка и да разположите Phi-3 модел, използвайки GPU. За финна настройка ще използвате GPU *Standard_NC24ads_A100_v4*, което изисква заявка за квота. За разгръщане ще използвате GPU *Standard_NC6s_v3*, което също изисква заявка за квота.

> [!NOTE]
>
> Само абонаментите „Плати каквото ползваш“ (стандартния тип абонамент) са допустими за разпределяне на GPU; абонаментите с ползи към момента не се поддържат.
>

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Извършете следните задачи, за да заявите квота за *Standard NCADSA100v4 Family*:

    - Изберете **Квота** от таба в лявата страна.
    - Изберете **Семейство виртуални машини**, което да използвате. Например, изберете **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, което включва GPU *Standard_NC24ads_A100_v4*.
    - Изберете **Заявка за квота** от навигационното меню.

        ![Заявка за квота.](../../../../../../translated_images/bg/02-02-request-quota.c0428239a63ffdd5.webp)

    - В страницата за Заявка за квота въведете **Нов лимит на ядра**, който желаете да използвате. Например, 24.
    - В страницата за Заявка за квота изберете **Изпрати**, за да заявите GPU квотата.

1. Изпълнете следните задачи, за да заявите квота за *Standard NCSv3 Family*:

    - Изберете **Квота** от таба в лявата страна.
    - Изберете **Семейство виртуални машини**, което да използвате. Например, изберете **Standard NCSv3 Family Cluster Dedicated vCPUs**, което включва GPU *Standard_NC6s_v3*.
    - Изберете **Заявка за квота** от навигационното меню.
    - В страницата за Заявка за квота въведете **Нов лимит на ядра**, който желаете да използвате. Например, 24.
    - В страницата за Заявка за квота изберете **Изпрати**, за да заявите GPU квотата.

### Добавяне на роля

За да направите финна настройка и разгръщане на моделите си, първо трябва да създадете Потребителско Назначена Управлявана Идентичност (UAI) и да ѝ зададете подходящи разрешения. Тази UAI ще се използва за удостоверяване по време на разгръщане.

#### Създаване на Потребителско Назначена Управлявана Идентичност (UAI)

1. Въведете *managed identities* в **лентата за търсене** в горната част на портала и изберете **Managed Identities** от наличните опции.

    ![Въведете managed identities.](../../../../../../translated_images/bg/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Изберете **+ Създай**.

    ![Изберете създай.](../../../../../../translated_images/bg/03-02-select-create.92bf8989a5cd98f2.webp)

1. Извършете следните действия:

    - Изберете вашия Azure **Абонамент**.
    - Изберете **Група ресурси**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Регион**, който искате да използвате.
    - Въведете **Име**. Трябва да е уникална стойност.

    ![Изберете създай.](../../../../../../translated_images/bg/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Изберете **Преглед + създай**.

1. Изберете **+ Създай**.

#### Добавяне на роля Contributor на Управляваната Идентичност

1. Навигирайте до ресурса на Управляваната Идентичност, който създадохте.

1. Изберете **Azure role assignments** от таба в лявата страна.

1. Изберете **+Добави роля** от навигационното меню.

1. В страницата за Добавяне на роля, извършете следните задачи:
    - Изберете **Обхват** на **Група ресурси**.
    - Изберете вашия Azure **Абонамент**.
    - Изберете **Група ресурси**, която да използвате.
    - Изберете **Роля** **Contributor**.

    ![Попълнете роля contributor.](../../../../../../translated_images/bg/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Изберете **Запиши**.

#### Добавяне на роля Storage Blob Data Reader на Управляваната Идентичност

1. Въведете *storage accounts* в **лентата за търсене** в горната част на портала и изберете **Storage accounts** от наличните опции.

    ![Въведете storage accounts.](../../../../../../translated_images/bg/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Изберете акаунта за съхранение, асоцииран с Azure Machine Learning workspace, който сте създали. Например, *finetunephistorage*.

1. Изпълнете следните задачи, за да навигирате до страницата за Добавяне на роля:

    - Отворете Azure Storage акаунта, който сте създали.
    - Изберете **Достъп и контрол (IAM)** от таба в лявата страна.
    - Изберете **+ Добавяне** от навигационното меню.
    - Изберете **Добавяне на роля** от навигационното меню.

    ![Добавяне на роля.](../../../../../../translated_images/bg/03-06-add-role.353ccbfdcf0789c2.webp)

1. В страницата за Добавяне на роля, извършете следните задачи:

    - Във страницата Роли въведете *Storage Blob Data Reader* в **лентата за търсене** и изберете **Storage Blob Data Reader** от възникналите опции.
    - Във страницата Роли изберете **Напред**.
    - В страницата Членове изберете **Задай достъп за** **Управлявана идентичност**.
    - В страницата Членове изберете **+ Избери членове**.
    - В страницата Избор на управлявани идентичности изберете вашия Azure **Абонамент**.
    - В страницата Избор на управлявани идентичности изберете **Управлявана идентичност**.
    - В страницата Избор на управлявани идентичности изберете Управляваната идентичност, която създадохте. Например, *finetunephi-managedidentity*.
    - В страницата Избор на управлявани идентичности изберете **Избери**.

    ![Избор на управлявана идентичност.](../../../../../../translated_images/bg/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Изберете **Преглед + присвои**.

#### Добавяне на роля AcrPull на Управляваната Идентичност

1. Въведете *container registries* в **лентата за търсене** в горната част на портала и изберете **Container registries** от наличните опции.

    ![Въведете container registries.](../../../../../../translated_images/bg/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Изберете контейнерния регистър, асоцииран с Azure Machine Learning workspace. Например, *finetunephicontainerregistry*

1. Изпълнете следните задачи, за да навигирате до страницата за Добавяне на роля:

    - Изберете **Достъп и контрол (IAM)** от таба в лявата страна.
    - Изберете **+ Добавяне** от навигационното меню.
    - Изберете **Добавяне на роля** от навигационното меню.

1. В страницата за Добавяне на роля, извършете следните задачи:

    - В страницата Роли въведете *AcrPull* в **лентата за търсене** и изберете **AcrPull** от наличните опции.
    - В страницата Роли изберете **Напред**.
    - В страницата Членове изберете **Задай достъп за** **Управлявана идентичност**.
    - В страницата Членове изберете **+ Избери членове**.
    - В страницата Избор на управлявани идентичности изберете вашия Azure **Абонамент**.
    - В страницата Избор на управлявани идентичности изберете **Управлявана идентичност**.
    - В страницата Избор на управлявани идентичности изберете Управляваната идентичност, която създадохте. Например, *finetunephi-managedidentity*.
    - В страницата Избор на управлявани идентичности изберете **Избери**.
    - Изберете **Преглед + присвои**.

### Настройване на проект

За да изтеглите наборите от данни, необходими за финна настройка, ще настроите локална среда.

В това упражнение ще

- Създадете папка, в която да работите.
- Създадете виртуална среда.
- Инсталирате необходимите пакети.
- Създадете файл *download_dataset.py* за изтегляне на набора от данни.

#### Създаване на папка за работа в нея

1. Отворете терминален прозорец и въведете следната команда, за да създадете папка с име *finetune-phi* в стандартния път.

    ```console
    mkdir finetune-phi
    ```

2. Въведете следната команда в терминала, за да навигирате до папката *finetune-phi*, която създадохте.

    ```console
    cd finetune-phi
    ```

#### Създаване на виртуална среда

1. Въведете следната команда в терминала си, за да създадете виртуална среда с име *.venv*.
    ```console
    python -m venv .venv
    ```

2. Въведете следната команда във вашия терминал, за да активирате виртуалната среда.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ако е успешно, трябва да видите *(.venv)* преди промпта на командния ред.

#### Инсталирайте необходимите пакети

1. Въведете следните команди във вашия терминал, за да инсталирате необходимите пакети.

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

1. Изберете **File** от меню лентата.

1. Изберете **Open Folder**.

1. Изберете папката *finetune-phi*, която сте създали, намираща се в *C:\Users\yourUserName\finetune-phi*.

    ![Изберете папката, която създадохте.](../../../../../../translated_images/bg/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. В левия панел на Visual Studio Code, кликнете с десния бутон и изберете **New File**, за да създадете нов файл с име *download_dataset.py*.

    ![Създайте нов файл.](../../../../../../translated_images/bg/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Подгответе датасета за допълнително обучение

В това упражнение ще стартирате файла *download_dataset.py*, за да изтеглите *ultrachat_200k* датасетите във вашата локална среда. След това ще използвате тези датасети, за да дообучите модела Phi-3 в Azure Machine Learning.

В това упражнение ще:

- Добавите код във файла *download_dataset.py*, за да изтеглите датасетите.
- Стартирате файла *download_dataset.py*, за да изтеглите датасетите в локалната си среда.

#### Изтеглете вашия датасет с помощта на *download_dataset.py*

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
        # Заредете набора от данни със зададеното име, конфигурация и съотношение за разделяне
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Разделете набора от данни на тренировъчен и тестов комплект (80% тренировка, 20% тест)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Създайте директорията, ако не съществува
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Отворете файла в режим за писане
        with open(filepath, 'w', encoding='utf-8') as f:
            # Итерирайте върху всеки запис в набора от данни
            for record in dataset:
                # Запишете записа като JSON обект и го запишете във файла
                json.dump(record, f)
                # Запишете нов ред, за да разделите записите
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Заредете и разделете ULTRACHAT_200k набора от данни със специфична конфигурация и съотношение за разделяне
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Извлечете тренировъчния и тестовия набор от данни от разделянето
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Запишете тренировъчния набор от данни в JSONL файл
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Запишете тестовия набор от данни в отделен JSONL файл
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Въведете следната команда във вашия терминал, за да стартирате скрипта и изтеглите датасета в локалната си среда.

    ```console
    python download_dataset.py
    ```

1. Проверете дали датасетите са запазени успешно в локалната директория *finetune-phi/data*.

> [!NOTE]
>
> #### Забележка относно размера на датасета и времето за дообучение
>
> В този урок използвате само 1% от датасета (`split='train[:1%]'`). Това значително намалява количеството данни, ускорявайки както качването, така и процеса на дообучение. Можете да регулирате процента, за да намерите баланса между времето за обучение и производителността на модела. Използването на по-малка подмножество от датасета намалява времето за дообучение, което прави процеса по-лесно управляем за урок.

## Сценарий 2: Дообучете модела Phi-3 и го разгърнете в Azure Machine Learning Studio

### Дообучете модела Phi-3

В това упражнение ще дообучите модела Phi-3 в Azure Machine Learning Studio.

В това упражнение ще:

- Създадете компютърен клъстър за дообучаване.
- Дообучите модела Phi-3 в Azure Machine Learning Studio.

#### Създаване на компютърен клъстър за дообучаване

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете **Compute** от таблото в лявата колона.

1. Изберете **Compute clusters** от навигационното меню.

1. Изберете **+ New**.

    ![Изберете compute.](../../../../../../translated_images/bg/06-01-select-compute.a29cff290b480252.webp)

1. Изпълнете следните задачи:

    - Изберете **Region**, който искате да използвате.
    - Изберете **Virtual machine tier** на **Dedicated**.
    - Изберете **Virtual machine type** на **GPU**.
    - Филтрирайте **Virtual machine size** на **Select from all options**.
    - Изберете **Virtual machine size** на **Standard_NC24ads_A100_v4**.

    ![Създайте клъстър.](../../../../../../translated_images/bg/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Изберете **Next**.

1. Изпълнете следните задачи:

    - Въведете **Compute name**. Трябва да е уникално име.
    - Изберете **Minimum number of nodes** на **0**.
    - Изберете **Maximum number of nodes** на **1**.
    - Изберете **Idle seconds before scale down** на **120**.

    ![Създаване на клъстър.](../../../../../../translated_images/bg/06-03-create-cluster.4a54ba20914f3662.webp)

1. Изберете **Create**.

#### Дообучение на модела Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете Azure Machine Learning workspace, който сте създали.

    ![Изберете workspace, който сте създали.](../../../../../../translated_images/bg/06-04-select-workspace.a92934ac04f4f181.webp)

1. Изпълнете следните задачи:

    - Изберете **Model catalog** от таблото в ляво.
    - Въведете *phi-3-mini-4k* в лентата за търсене и изберете **Phi-3-mini-4k-instruct** от опциите, които се появят.

    ![Въведете phi-3-mini-4k.](../../../../../../translated_images/bg/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Изберете **Fine-tune** от навигационното меню.

    ![Изберете fine tune.](../../../../../../translated_images/bg/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Изпълнете следните задачи:

    - Изберете **Select task type** на **Chat completion**.
    - Изберете **+ Select data**, за да качите **Traning data**.
    - Изберете типа качване на валидиращите данни на **Provide different validation data**.
    - Изберете **+ Select data**, за да качите **Validation data**.

    ![Попълнете страницата за дообучаване.](../../../../../../translated_images/bg/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Можете да изберете **Advanced settings**, за да персонализирате конфигурации като **learning_rate** и **lr_scheduler_type**, за да оптимизирате процеса на дообучение според вашите специфични нужди.

1. Изберете **Finish**.

1. В това упражнение успешно дообучихте модела Phi-3, използвайки Azure Machine Learning. Моля, обърнете внимание, че процесът на дообучение може да отнеме значително време. След стартиране на задачата за дообучение, трябва да изчакате тя да приключи. Можете да следите статуса на задачата, като отидете на таба Jobs в лявата част на вашето Azure Machine Learning Workspace. В следващата серия ще разгърнете дообучения модел и ще го интегрирате с Prompt flow.

    ![Вижте задачата за дообучаване.](../../../../../../translated_images/bg/06-08-output.2bd32e59930672b1.webp)

### Разгръщане на дообучения Phi-3 модел

За да интегрирате дообучения Phi-3 модел с Prompt flow, трябва да го разположите, за да бъде достъпен за инференция в реално време. Този процес включва регистриране на модела, създаване на онлайн крайна точка и разполагане на модела.

В това упражнение ще:

- Регистрирате дообучения модел в Azure Machine Learning workspace.
- Създадете онлайн крайна точка.
- Разгърнете регистрирания дообучен Phi-3 модел.

#### Регистриране на дообучения модел

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Изберете Azure Machine Learning workspace, който сте създали.

    ![Изберете workspace, който сте създали.](../../../../../../translated_images/bg/06-04-select-workspace.a92934ac04f4f181.webp)

1. Изберете **Models** от таблото в ляво.
1. Изберете **+ Register**.
1. Изберете **From a job output**.

    ![Регистриране на модел.](../../../../../../translated_images/bg/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Изберете задачата, която сте създали.

    ![Избор на задача.](../../../../../../translated_images/bg/07-02-select-job.3e2e1144cd6cd093.webp)

1. Изберете **Next**.

1. Изберете **Model type** на **MLflow**.

1. Уверете се, че **Job output** е избрано; то трябва да е селектирано автоматично.

    ![Избор на изход.](../../../../../../translated_images/bg/07-03-select-output.4cf1a0e645baea1f.webp)

2. Изберете **Next**.

3. Изберете **Register**.

    ![Изберете Регистриране.](../../../../../../translated_images/bg/07-04-register.fd82a3b293060bc7.webp)

4. Можете да видите регистрирания си модел, като отидете в менюто **Models** от таблото в ляво.

    ![Регистриран модел.](../../../../../../translated_images/bg/07-05-registered-model.7db9775f58dfd591.webp)

#### Разгръщане на дообучения модел

1. Навигирайте до Azure Machine Learning workspace, който сте създали.

1. Изберете **Endpoints** от таблото в ляво.

1. Изберете **Real-time endpoints** от навигационното меню.

    ![Създаване на крайна точка.](../../../../../../translated_images/bg/07-06-create-endpoint.1ba865c606551f09.webp)

1. Изберете **Create**.

1. Изберете регистрирания модел, който сте създали.

    ![Избор на регистриран модел.](../../../../../../translated_images/bg/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Изберете **Select**.

1. Изпълнете следните задачи:

    - Изберете **Virtual machine** на *Standard_NC6s_v3*.
    - Изберете **Instance count**, който искате да използвате. Например, *1*.
    - Изберете **Endpoint** на **New**, за да създадете крайна точка.
    - Въведете **Endpoint name**. Трябва да е уникално име.
    - Въведете **Deployment name**. Трябва да е уникално име.

    ![Попълнете настройките за разполагане.](../../../../../../translated_images/bg/07-08-deployment-setting.43ddc4209e673784.webp)

1. Изберете **Deploy**.

> [!WARNING]
> За да избегнете допълнителни такси по сметката си, уверете се, че сте изтрили създадената крайна точка в Azure Machine Learning workspace.
>

#### Проверка на статуса на разполагането в Azure Machine Learning Workspace

1. Навигирайте до Azure Machine Learning workspace, който сте създали.

1. Изберете **Endpoints** от таблото в ляво.

1. Изберете създадената от вас крайна точка.

    ![Избор на крайни точки](../../../../../../translated_images/bg/07-09-check-deployment.325d18cae8475ef4.webp)

1. На тази страница можете да управлявате крайните точки по време на процеса на разполагане.

> [!NOTE]
> След завършване на разполагането се уверете, че **Live traffic** е настроено на **100%**. Ако не е, изберете **Update traffic**, за да коригирате настройките за трафик. Обърнете внимание, че не можете да тествате модела, ако трафикът е настроен на 0%.
>
> ![Настройване на трафика.](../../../../../../translated_images/bg/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Сценарий 3: Интеграция с Prompt flow и чат с вашия персонализиран модел в Microsoft Foundry

### Интегриране на персонализирания модел Phi-3 с Prompt flow

След успешно разполагане на вашия дообучен модел, можете да го интегрирате с Prompt Flow, за да използвате модела си в приложения в реално време, позволяващи различни интерактивни задачи с вашия персонализиран модел Phi-3.

В това упражнение ще:

- Създадете Microsoft Foundry Hub.
- Създадете Microsoft Foundry Project.
- Създадете Prompt flow.
- Добавите персонализирана връзка за дообучения модел Phi-3.
- Настроите Prompt flow за чат с вашия персонализиран модел Phi-3.

> [!NOTE]
> Можете също да интегрирате с Promptflow, използвайки Azure ML Studio. Същият процес на интеграция може да се приложи и към Azure ML Studio.

#### Създаване на Microsoft Foundry Hub

Трябва да създадете Hub преди да създадете Project. Hub функционира като Resource Group, която ви позволява да организирате и управлявате множество Projects в Microsoft Foundry.
1. Посетете [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Изберете **All hubs** от таба от лявата страна.

1. Изберете **+ New hub** от навигационното меню.

    ![Create hub.](../../../../../../translated_images/bg/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Изпълнете следните задачи:

    - Въведете **Hub name**. Трябва да е уникална стойност.
    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която да използвате (създайте нова, ако е необходимо).
    - Изберете **Location**, която искате да използвате.
    - Изберете **Connect Azure AI Services**, които да използвате (създайте нови, ако е необходимо).
    - Изберете **Connect Azure AI Search** и изберете **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/bg/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Изберете **Next**.

#### Създаване на проект в Microsoft Foundry

1. В създадения от вас Hub изберете **All projects** от таба от лявата страна.

1. Изберете **+ New project** от навигационното меню.

    ![Select new project.](../../../../../../translated_images/bg/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Въведете **Project name**. Трябва да е уникална стойност.

    ![Create project.](../../../../../../translated_images/bg/08-05-create-project.4d97f0372f03375a.webp)

1. Изберете **Create a project**.

#### Добавяне на персонализирана връзка към финално обучен модел Phi-3

За да интегрирате вашия персонализиран Phi-3 модел с Prompt flow, трябва да запишете крайна точка и ключ на модела в персонализирана връзка. Тази настройка осигурява достъп до вашия персонализиран Phi-3 модел в Prompt flow.

#### Задаване на ключ за API и URI на крайна точка на финално обучен модел Phi-3

1. Посетете [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Навигирайте до работното пространство Azure Machine learning, което сте създали.

1. Изберете **Endpoints** от таба от лявата страна.

    ![Select endpoints.](../../../../../../translated_images/bg/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Изберете крайна точка, която сте създали.

    ![Select endpoints.](../../../../../../translated_images/bg/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Изберете **Consume** от навигационното меню.

1. Копирайте вашите **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/bg/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Добавяне на персонализирана връзка

1. Посетете [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Навигирайте до проекта в Microsoft Foundry, който сте създали.

1. В създадения проект изберете **Settings** от таба от лявата страна.

1. Изберете **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/bg/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Изберете **Custom keys** от навигационното меню.

    ![Select custom keys.](../../../../../../translated_images/bg/08-10-select-custom-keys.856f6b2966460551.webp)

1. Изпълнете следните стъпки:

    - Изберете **+ Add key value pairs**.
    - За име на ключ въведете **endpoint** и поставете копираната крайна точка от Azure ML Studio в полето за стойност.
    - Изберете отново **+ Add key value pairs**.
    - За име на ключ въведете **key** и поставете копирания ключ от Azure ML Studio в полето за стойност.
    - След като добавите ключовете, изберете **is secret**, за да не бъде ключът изложен.

    ![Add connection.](../../../../../../translated_images/bg/08-11-add-connection.785486badb4d2d26.webp)

1. Изберете **Add connection**.

#### Създаване на Prompt flow

Вече добавихте персонализирана връзка в Microsoft Foundry. Сега нека създадем Prompt flow, като използваме следните стъпки. След това ще свържете този Prompt flow с персонализираната връзка, за да използвате финално обучен модел в Prompt flow.

1. Навигирайте до проекта в Microsoft Foundry, който сте създали.

1. Изберете **Prompt flow** от таба от лявата страна.

1. Изберете **+ Create** от навигационното меню.

    ![Select Promptflow.](../../../../../../translated_images/bg/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Изберете **Chat flow** от навигационното меню.

    ![Select chat flow.](../../../../../../translated_images/bg/08-13-select-flow-type.2ec689b22da32591.webp)

1. Въведете **Folder name**, която искате да използвате.

    ![Enter name.](../../../../../../translated_images/bg/08-14-enter-name.ff9520fefd89f40d.webp)

2. Изберете **Create**.

#### Настройване на Prompt flow за чат с вашия персонализиран модел Phi-3

Трябва да интегрирате финално обучен модел Phi-3 в Prompt flow. Въпреки това, съществуващият предоставен Prompt flow не е предназначен за тази цел. Поради това трябва да препроектирате Prompt flow, за да позволите интеграцията на персонализирания модел.

1. В Prompt flow изпълнете следните задачи, за да възстановите съществуващия поток:

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

    ![Select raw file mode.](../../../../../../translated_images/bg/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Добавете следния код във файла *integrate_with_promptflow.py*, за да използвате персонализирания модел Phi-3 в Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Настройка на логването
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

        # "connection" е името на потребителската връзка, "endpoint", "key" са ключовете в потребителската връзка
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
            
            # Записване на пълния JSON отговор
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

    ![Paste prompt flow code.](../../../../../../translated_images/bg/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> За повече подробна информация как да използвате Prompt flow в Microsoft Foundry, можете да се обърнете към [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изберете **Chat input**, **Chat output**, за да активирате чат с вашия модел.

    ![Input Output.](../../../../../../translated_images/bg/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Сега сте готови да чатите с вашия персонализиран модел Phi-3. В следващото упражнение ще научите как да стартирате Prompt flow и да го използвате за чат с вашия финално обучен модел Phi-3.

> [!NOTE]
>
> Преконструираният поток трябва да изглежда като на следното изображение:
>
> ![Flow example.](../../../../../../translated_images/bg/08-18-graph-example.d6457533952e690c.webp)
>

### Чат с вашия персонализиран модел Phi-3

Сега, след като сте финално обучили и интегрирали вашия персонализиран модел Phi-3 с Prompt flow, сте готови да започнете взаимодействие с него. Това упражнение ще ви преведе през процеса на настройка и старт на чат с вашия модел чрез Prompt flow. Следвайки тези стъпки, ще можете да използвате пълноценно възможностите на финално обучен модел Phi-3 за различни задачи и разговори.

- Чат с вашия персонализиран модел Phi-3 чрез Prompt flow.

#### Стартиране на Prompt flow

1. Изберете **Start compute sessions**, за да стартирате Prompt flow.

    ![Start compute session.](../../../../../../translated_images/bg/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Изберете **Validate and parse input**, за да обновите параметрите.

    ![Validate input.](../../../../../../translated_images/bg/09-02-validate-input.317c76ef766361e9.webp)

1. Изберете стойността **Value** на **connection** към персонализираната връзка, която сте създали. Например *connection*.

    ![Connection.](../../../../../../translated_images/bg/09-03-select-connection.99bdddb4b1844023.webp)

#### Чат с вашия персонализиран модел

1. Изберете **Chat**.

    ![Select chat.](../../../../../../translated_images/bg/09-04-select-chat.61936dce6612a1e6.webp)

1. Ето пример за резултатите: Сега можете да чатите с вашия персонализиран модел Phi-3. Препоръчително е да задавате въпроси, базирани на данните, използвани за финално обучение.

    ![Chat with prompt flow.](../../../../../../translated_images/bg/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->