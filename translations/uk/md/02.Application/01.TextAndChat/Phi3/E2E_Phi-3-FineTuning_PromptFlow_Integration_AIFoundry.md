# Налаштування тонкого донавчання та інтеграція власних моделей Phi-3 з Prompt flow у Microsoft Foundry

Цей покроковий (E2E) приклад базується на посібнику "[Налаштування тонкого донавчання та інтеграція власних моделей Phi-3 з Prompt flow у Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" з Microsoft Tech Community. Він вводить у процеси тонкого донавчання, розгортання та інтеграції власних моделей Phi-3 з Prompt flow у Microsoft Foundry.
На відміну від E2E прикладу "[Налаштування тонкого донавчання та інтеграція власних моделей Phi-3 з Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", що передбачав запуск коду локально, цей підручник повністю зосереджений на тонкому донавчанні та інтеграції вашої моделі в Azure AI / ML Studio.

## Огляд

У цьому покроковому прикладі ви навчитеся налаштовувати тонке донавчання моделі Phi-3 і інтегрувати її з Prompt flow у Microsoft Foundry. Використовуючи Azure AI / ML Studio, ви створите робочий процес для розгортання та використання власних моделей ШІ. Цей покроковий приклад поділений на три сценарії:

**Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого донавчання**

**Сценарій 2: Тонке донавчання моделі Phi-3 і розгортання в Azure Machine Learning Studio**

**Сценарій 3: Інтеграція з Prompt flow та чат з вашою власною моделлю у Microsoft Foundry**

Ось огляд цього покрокового прикладу.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/uk/00-01-architecture.198ba0f1ae6d841a.webp)

### Зміст

1. **[Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого донавчання](#сценарій-1-налаштування-ресурсів-azure-та-підготовка-до-тонкого-донавчання)**
    - [Створення Azure Machine Learning Workspace](#створення-azure-machine-learning-workspace)
    - [Запит квот на GPU в підписці Azure](#запит-квот-на-gpu-в-підписці-azure)
    - [Додавання призначення ролі](#додавання-призначення-ролі)
    - [Налаштування проекту](#налаштування-проекту)
    - [Підготовка набору даних для тонкого донавчання](#підготування-набору-даних-для-донавчання)

1. **[Сценарій 2: Тонке донавчання моделі Phi-3 і розгортання в Azure Machine Learning Studio](#сценарій-2-донавчання-моделі-phi-3-та-розгортання-в-azure-machine-learning-studio)**
    - [Тонке донавчання моделі Phi-3](#донавчання-моделі-phi-3)
    - [Розгортання моделі Phi-3 після тонкого донавчання](#розгортання-донавченої-моделі-phi-3)

1. **[Сценарій 3: Інтеграція з Prompt flow та чат з вашою власною моделлю у Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Інтеграція власної моделі Phi-3 з Prompt flow](#інтеграція-користувацької-моделі-phi-3-з-prompt-flow)
    - [Чат з вашою власною моделлю Phi-3](#спілкування-з-вашим-кастомним-моделлю-phi-3)

## Сценарій 1: Налаштування ресурсів Azure та підготовка до тонкого донавчання

### Створення Azure Machine Learning Workspace

1. Введіть *azure machine learning* у **рядку пошуку** у верхній частині порталу та виберіть **Azure Machine Learning** серед запропонованих варіантів.

    ![Type azure machine learning.](../../../../../../translated_images/uk/01-01-type-azml.acae6c5455e67b4b.webp)

2. Виберіть **+ Створити** у меню навігації.

3. Виберіть **Новий робочий простір** у меню навігації.

    ![Select new workspace.](../../../../../../translated_images/uk/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Виконайте такі дії:

    - Оберіть вашу підписку Azure (**Subscription**).
    - Оберіть **Групу ресурсів** для використання (створіть нову, якщо потрібно).
    - Введіть **Назву робочого простору**. Вона має бути унікальною.
    - Оберіть **Регіон**, який хочете використовувати.
    - Оберіть **Обліковий запис зберігання** (в разі потреби створіть новий).
    - Оберіть **Хранилище ключів** (Key vault) (в разі потреби створіть нове).
    - Оберіть **Application insights** (в разі потреби створіть новий).
    - Оберіть **Регістр контейнерів** (Container registry) (в разі потреби створіть новий).

    ![Fill azure machine learning.](../../../../../../translated_images/uk/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Оберіть **Перевірити + Створити**.

6. Оберіть **Створити**.

### Запит квот на GPU в підписці Azure

У цьому підручнику ви навчитеся тонкому донавчанню та розгортанню моделі Phi-3 з використанням GPU. Для тонкого донавчання ви використаєте GPU *Standard_NC24ads_A100_v4*, для якого потрібно зробити запит квоти. Для розгортання використовується GPU *Standard_NC6s_v3*, для якого також необхідний запит квоти.

> [!NOTE]
>
> Тільки підписки типу Pay-As-You-Go (стандартний тип підписки) мають право на виділення GPU; підписки з пільгами наразі не підтримуються.
>

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виконайте такі дії для запиту квоти *Standard NCADSA100v4 Family*:

    - Виберіть **Квота** (Quota) у лівому меню.
    - Виберіть сімейство віртуальних машин. Наприклад, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, до якого входить GPU *Standard_NC24ads_A100_v4*.
    - Оберіть **Запитати квоту** з меню.

        ![Request quota.](../../../../../../translated_images/uk/02-02-request-quota.c0428239a63ffdd5.webp)

    - На сторінці запиту квоти введіть **Новий ліміт ядер** (New cores limit), який хочете встановити. Наприклад, 24.
    - Натисніть **Відправити** (Submit) для запиту квоти на GPU.

1. Виконайте такі дії для запиту квоти *Standard NCSv3 Family*:

    - Виберіть **Квота** у лівому меню.
    - Виберіть сімейство віртуальних машин. Наприклад, **Standard NCSv3 Family Cluster Dedicated vCPUs**, до якого входить GPU *Standard_NC6s_v3*.
    - Оберіть **Запитати квоту** з меню.
    - На сторінці запиту квоти введіть **Новий ліміт ядер**. Наприклад, 24.
    - Натисніть **Відправити**.

### Додавання призначення ролі

Для тонкого донавчання і розгортання моделей необхідно створити користувацьку керовану ідентичність (User Assigned Managed Identity — UAI) і призначити їй відповідні дозволи. Ця UAI буде використовуватись для автентифікації під час розгортання.

#### Створення користувацької керованої ідентичності (UAI)

1. Введіть *managed identities* у **рядку пошуку** у верхній частині порталу і виберіть **Managed Identities** зі списку.

    ![Type managed identities.](../../../../../../translated_images/uk/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Виберіть **+ Створити**.

    ![Select create.](../../../../../../translated_images/uk/03-02-select-create.92bf8989a5cd98f2.webp)

1. Виконайте такі дії:

    - Оберіть вашу підписку Azure.
    - Оберіть групу ресурсів (створіть нову, якщо потрібно).
    - Виберіть потрібний регіон.
    - Введіть унікальне ім’я.

    ![Select create.](../../../../../../translated_images/uk/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Оберіть **Перевірити + Створити**.

1. Оберіть **+ Створити**.

#### Призначення ролі Contributor керованій ідентичності

1. Перейдіть до ресурсу керованої ідентичності, який ви створили.

1. Оберіть **Призначення ролей Azure** (Azure role assignments) у лівому меню.

1. Оберіть **+ Додати призначення ролі** у навігаційному меню.

1. На сторінці додавання призначення ролі виконайте такі дії:
    - Оберіть **Область** (Scope) — **Група ресурсів**.
    - Оберіть підписку Azure.
    - Оберіть потрібну групу ресурсів.
    - Оберіть роль **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/uk/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Оберіть **Зберегти**.

#### Призначення ролі Storage Blob Data Reader керованій ідентичності

1. Введіть *storage accounts* у рядку пошуку і виберіть **Storage accounts** зі списку.

    ![Type storage accounts.](../../../../../../translated_images/uk/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Виберіть обліковий запис зберігання, пов’язаний з вашим Azure Machine Learning workspace. Наприклад, *finetunephistorage*.

1. Виконайте дії для переходу на сторінку додавання призначення ролі:

    - Перейдіть до облікового запису Azure Storage, який створено.
    - Оберіть **Контроль доступу (IAM)** у лівому меню.
    - Оберіть **+ Додати** у навігаційному меню.
    - Оберіть **Додати призначення ролі**.

    ![Add role.](../../../../../../translated_images/uk/03-06-add-role.353ccbfdcf0789c2.webp)

1. На сторінці додавання призначення ролі виконайте такі дії:

    - На сторінці Ролі введіть *Storage Blob Data Reader* у рядку пошуку і виберіть цю роль.
    - Натисніть **Далі**.
    - На сторінці Учасники оберіть **Призначити доступ** — **Керована ідентичність**.
    - Натисніть **+ Вибрати учасників**.
    - Виберіть вашу підписку Azure.
    - Виберіть керовану ідентичність.
    - Оберіть керовану ідентичність, яку створили. Наприклад, *finetunephi-managedidentity*.
    - Оберіть **Вибрати**.

    ![Select managed identity.](../../../../../../translated_images/uk/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Оберіть **Перевірити + Призначити**.

#### Призначення ролі AcrPull керованій ідентичності

1. Введіть *container registries* у рядку пошуку і виберіть **Container registries** зі списку.

    ![Type container registries.](../../../../../../translated_images/uk/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Виберіть реєстр контейнерів, пов’язаний з вашим Azure Machine Learning workspace. Наприклад, *finetunephicontainerregistry*.

1. Виконайте дії для переходу на сторінку додавання призначення ролі:

    - Оберіть **Контроль доступу (IAM)**.
    - Оберіть **+ Додати**.
    - Оберіть **Додати призначення ролі**.

1. На сторінці додавання ролі виконайте такі дії:

    - У рядку пошуку введіть *AcrPull* і виберіть цю роль.
    - Оберіть **Далі**.
    - На сторінці Учасники оберіть **Призначити доступ** — **Керована ідентичність**.
    - Оберіть **+ Вибрати учасників**.
    - Виберіть вашу підписку Azure.
    - Виберіть керовану ідентичність.
    - Оберіть керовану ідентичність, яку створили. Наприклад, *finetunephi-managedidentity*.
    - Оберіть **Вибрати**.
    - Оберіть **Перевірити + Призначити**.

### Налаштування проекту

Для завантаження наборів даних, необхідних для тонкого донавчання, налаштуйте локальне середовище.

У цій вправі ви

- Створите папку для роботи.
- Створите віртуальне середовище.
- Встановите потрібні пакунки.
- Створите файл *download_dataset.py* для завантаження набору даних.

#### Створення папки для роботи

1. Відкрийте термінал і введіть команду для створення папки з ім’ям *finetune-phi* у стандартному розташуванні.

    ```console
    mkdir finetune-phi
    ```

2. Введіть команду для переходу до папки *finetune-phi*, яку ви створили.

    ```console
    cd finetune-phi
    ```

#### Створення віртуального середовища

1. Введіть команду для створення віртуального середовища з ім’ям *.venv*.


    ```console
    python -m venv .venv
    ```

2. Введіть наступну команду у вашому терміналі, щоб активувати віртуальне середовище.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Якщо це спрацювало, ви повинні бачити *(.venv)* перед командним рядком.

#### Встановіть необхідні пакети

1. Введіть наступні команди у вашому терміналі, щоб встановити необхідні пакети.

    ```console
    pip install datasets==2.19.1
    ```

#### Створіть `donload_dataset.py`

> [!NOTE]
> Повна структура папок:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Відкрийте **Visual Studio Code**.

1. Виберіть **File** з меню.

1. Виберіть **Open Folder**.

1. Виберіть папку *finetune-phi*, яку ви створили, розташовану за шляхом *C:\Users\yourUserName\finetune-phi*.

    ![Виберіть папку, яку ви створили.](../../../../../../translated_images/uk/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. У лівій панелі Visual Studio Code клацніть правою кнопкою миші і виберіть **New File**, щоб створити новий файл з ім’ям *download_dataset.py*.

    ![Створіть новий файл.](../../../../../../translated_images/uk/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Підготування набору даних для донавчання

У цьому завданні ви запустите файл *download_dataset.py*, щоб завантажити набори даних *ultrachat_200k* у ваше локальне середовище. Потім ви використаєте ці набори даних для донавчання моделі Phi-3 в Azure Machine Learning.

У цьому завданні ви:

- Додасте код у файл *download_dataset.py* для завантаження наборів даних.
- Запустите файл *download_dataset.py*, щоб завантажити набори даних у ваше локальне середовище.

#### Завантажте ваш набір даних за допомогою *download_dataset.py*

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
        # Завантажте набір даних з вказаною назвою, конфігурацією та коефіцієнтом розподілу
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Розділіть набір даних на тренувальний та тестовий набори (80% тренувальний, 20% тестовий)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Створіть директорію, якщо вона не існує
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Відкрийте файл у режимі запису
        with open(filepath, 'w', encoding='utf-8') as f:
            # Ітеруйте кожен запис у наборі даних
            for record in dataset:
                # Запишіть запис у форматі JSON і збережіть у файл
                json.dump(record, f)
                # Запишіть символ нового рядка, щоб розділити записи
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Завантажте та розділіть набір даних ULTRACHAT_200k з певною конфігурацією та коефіцієнтом розподілу
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Витягніть тренувальний та тестовий набори даних із розподілу
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Збережіть тренувальний набір даних у файл JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Збережіть тестовий набір даних у окремий файл JSONL
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Введіть наступну команду у вашому терміналі, щоб запустити скрипт і завантажити набір даних у ваше локальне середовище.

    ```console
    python download_dataset.py
    ```

1. Перевірте, чи набори даних успішно збережені у вашій локальній директорії *finetune-phi/data*.

> [!NOTE]
>
> #### Примітка щодо розміру набору даних та часу донавчання
>
> У цьому навчальному посібнику ви використовуєте лише 1% набору даних (`split='train[:1%]'`). Це значно зменшує обсяг даних, прискорюючи завантаження й процес донавчання. Ви можете регулювати відсоток, щоб знайти оптимальний баланс між часом навчання та продуктивністю моделі. Використання меншої частини набору даних зменшує час, необхідний для донавчання, роблячи процес більш керованим для посібника.

## Сценарій 2: Донавчання моделі Phi-3 та розгортання в Azure Machine Learning Studio

### Донавчання моделі Phi-3

У цьому завданні ви донавчите модель Phi-3 в Azure Machine Learning Studio.

У цьому завданні ви:

- Створите кластер обчислювальних ресурсів для донавчання.
- Донавчите модель Phi-3 в Azure Machine Learning Studio.

#### Створення кластеру для донавчання

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виберіть **Compute** у лівому меню.

1. Виберіть **Compute clusters** у навігаційному меню.

1. Виберіть **+ New**.

    ![Виберіть обчислювальні ресурси.](../../../../../../translated_images/uk/06-01-select-compute.a29cff290b480252.webp)

1. Виконайте наступні дії:

    - Виберіть регіон (**Region**), який хочете використовувати.
    - Виберіть рівень віртуальної машини (**Virtual machine tier**) – **Dedicated**.
    - Виберіть тип віртуальної машини (**Virtual machine type**) – **GPU**.
    - Відфільтруйте розмір віртуальної машини (**Virtual machine size**) на **Select from all options**.
    - Виберіть розмір віртуальної машини **Standard_NC24ads_A100_v4**.

    ![Створення кластеру.](../../../../../../translated_images/uk/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Виберіть **Next**.

1. Виконайте наступні дії:

    - Введіть назву обчислювального кластеру (**Compute name**). Вона має бути унікальною.
    - Виберіть мінімальну кількість вузлів (**Minimum number of nodes**) – **0**.
    - Виберіть максимальну кількість вузлів (**Maximum number of nodes**) – **1**.
    - Встановіть час очікування перед масштабуванням вниз (**Idle seconds before scale down**) – **120**.

    ![Створення кластеру.](../../../../../../translated_images/uk/06-03-create-cluster.4a54ba20914f3662.webp)

1. Виберіть **Create**.

#### Донавчання моделі Phi-3

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виберіть робоче середовище Azure Machine Learning, яке ви створили.

    ![Виберіть створене робоче середовище.](../../../../../../translated_images/uk/06-04-select-workspace.a92934ac04f4f181.webp)

1. Виконайте наступні дії:

    - Виберіть **Model catalog** у лівому меню.
    - Введіть *phi-3-mini-4k* у **рядку пошуку** та виберіть **Phi-3-mini-4k-instruct** із запропонованих варіантів.

    ![Введіть phi-3-mini-4k.](../../../../../../translated_images/uk/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Виберіть **Fine-tune** у навігаційному меню.

    ![Виберіть донавчання.](../../../../../../translated_images/uk/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Виконайте наступні дії:

    - Виберіть тип завдання (**Select task type**) – **Chat completion**.
    - Виберіть **+ Select data** для завантаження тренувальних даних (**Traning data**).
    - Виберіть тип завантаження перевірочних даних (**Validation data upload type**) – **Provide different validation data**.
    - Виберіть **+ Select data** для завантаження перевірочних даних (**Validation data**).

    ![Заповніть сторінку донавчання.](../../../../../../translated_images/uk/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Ви можете вибрати **Advanced settings**, щоб налаштувати конфігурації, такі як **learning_rate** та **lr_scheduler_type** для оптимізації процесу донавчання відповідно до ваших потреб.

1. Виберіть **Finish**.

1. У цьому завданні ви успішно донавчили модель Phi-3 за допомогою Azure Machine Learning. Зверніть увагу, що процес донавчання може зайняти значний час. Після запуску завдання донавчання потрібно почекати його завершення. Ви можете стежити за статусом завдання в розділі Jobs зліва у вашому робочому середовищі Azure Machine Learning. У наступній серії ви розгорнете донавчену модель і інтегруєте її з Prompt flow.

    ![Перегляньте результат донавчання.](../../../../../../translated_images/uk/06-08-output.2bd32e59930672b1.webp)

### Розгортання донавченої моделі Phi-3

Щоб інтегрувати донавчену модель Phi-3 з Prompt flow, потрібно розгорнути модель, зробивши її доступною для інференсу в режимі реального часу. Цей процес включає реєстрацію моделі, створення онлайн-ендпойнту та розгортання моделі.

У цьому завданні ви:

- Зареєструєте донавчену модель у робочому середовищі Azure Machine Learning.
- Створите онлайн-ендпойнт.
- Розгорнете зареєстровану донавчену модель Phi-3.

#### Реєстрація донавченої моделі

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Виберіть робоче середовище Azure Machine Learning, яке ви створили.

    ![Виберіть створене робоче середовище.](../../../../../../translated_images/uk/06-04-select-workspace.a92934ac04f4f181.webp)

1. Виберіть **Models** у лівому меню.
1. Виберіть **+ Register**.
1. Виберіть **From a job output**.

    ![Зареєструйте модель.](../../../../../../translated_images/uk/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Виберіть завдання, яке ви створили.

    ![Виберіть завдання.](../../../../../../translated_images/uk/07-02-select-job.3e2e1144cd6cd093.webp)

1. Виберіть **Next**.

1. Виберіть тип моделі (**Model type**) – **MLflow**.

1. Переконайтеся, що вибрано **Job output**; він має бути вибраний автоматично.

    ![Виберіть вихідні дані.](../../../../../../translated_images/uk/07-03-select-output.4cf1a0e645baea1f.webp)

2. Виберіть **Next**.

3. Виберіть **Register**.

    ![Виберіть реєстрацію.](../../../../../../translated_images/uk/07-04-register.fd82a3b293060bc7.webp)

4. Ви можете переглянути зареєстровану модель у меню **Models** зліва.

    ![Зареєстрована модель.](../../../../../../translated_images/uk/07-05-registered-model.7db9775f58dfd591.webp)

#### Розгортання донавченої моделі

1. Перейдіть до робочого середовища Azure Machine Learning, яке ви створили.

1. Виберіть **Endpoints** у лівому меню.

1. Виберіть **Real-time endpoints** у навігаційному меню.

    ![Створення ендпойнту.](../../../../../../translated_images/uk/07-06-create-endpoint.1ba865c606551f09.webp)

1. Виберіть **Create**.

1. Виберіть зареєстровану модель, яку ви створили.

    ![Виберіть зареєстровану модель.](../../../../../../translated_images/uk/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Виберіть **Select**.

1. Виконайте наступні дії:

    - Виберіть віртуальну машину (**Virtual machine**) – *Standard_NC6s_v3*.
    - Виберіть кількість інстансів (**Instance count**), яку хочете використовувати. Наприклад, *1*.
    - Виберіть **Endpoint** – **New** для створення нового ендпойнту.
    - Введіть назву ендпойнту (**Endpoint name**). Вона має бути унікальною.
    - Введіть назву розгортання (**Deployment name**). Вона має бути унікальною.

    ![Заповніть налаштування розгортання.](../../../../../../translated_images/uk/07-08-deployment-setting.43ddc4209e673784.webp)

1. Виберіть **Deploy**.

> [!WARNING]
> Щоб уникнути додаткових витрат на ваш рахунок, обов’язково видаліть створений ендпойнт у робочому середовищі Azure Machine Learning.
>

#### Перевірка статусу розгортання в Azure Machine Learning Workspace

1. Перейдіть до робочого середовища Azure Machine Learning, яке ви створили.

1. Виберіть **Endpoints** у лівому меню.

1. Виберіть ендпойнт, який ви створили.

    ![Виберіть ендпойнти](../../../../../../translated_images/uk/07-09-check-deployment.325d18cae8475ef4.webp)

1. На цій сторінці ви можете керувати ендпойнтами під час процесу розгортання.

> [!NOTE]
> Після завершення розгортання переконайтеся, що **Live traffic** встановлено на **100%**. Якщо ні, виберіть **Update traffic** для коригування налаштувань трафіку. Зверніть увагу, що тестувати модель неможливо, якщо трафік встановлено на 0%.
>
> ![Встановіть трафік.](../../../../../../translated_images/uk/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Сценарій 3: Інтеграція з Prompt flow та чат з вашою користувацькою моделлю в Microsoft Foundry

### Інтеграція користувацької моделі Phi-3 з Prompt flow

Після успішного розгортання донавченої моделі тепер ви можете інтегрувати її з Prompt Flow, щоб використовувати модель у реальних застосунках, забезпечуючи різноманітні інтерактивні завдання з вашою користувацькою моделлю Phi-3.

У цьому завданні ви:

- Створите Microsoft Foundry Hub.
- Створите проект Microsoft Foundry.
- Створите Prompt flow.
- Додасте користувацьке підключення для донавченої моделі Phi-3.
- Налаштуєте Prompt flow для чату з вашою користувацькою моделлю Phi-3.

> [!NOTE]
> Ви також можете інтегруватися з Promptflow за допомогою Azure ML Studio. Такий самий процес інтеграції застосовується і для Azure ML Studio.

#### Створення Microsoft Foundry Hub

Вам потрібно створити Hub перед створенням Проекту. Hub працює як Група ресурсів, дозволяючи вам організовувати та керувати кількома Проектами в Microsoft Foundry.
1. Відвідайте [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Виберіть **All hubs** у вкладці зліва.

1. Виберіть **+ New hub** у навігаційному меню.

    ![Create hub.](../../../../../../translated_images/uk/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Виконайте наступні дії:

    - Введіть **Hub name**. Воно має бути унікальним значенням.
    - Виберіть вашу підписку Azure **Subscription**.
    - Виберіть **Resource group** для використання (створіть нову, якщо потрібно).
    - Виберіть **Location**, яку ви бажаєте використовувати.
    - Виберіть **Connect Azure AI Services** для використання (створіть нову, якщо потрібно).
    - Виберіть **Connect Azure AI Search** і оберіть **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/uk/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Виберіть **Next**.

#### Створення проекту Microsoft Foundry

1. У створеному хабі виберіть **All projects** у вкладці зліва.

1. Виберіть **+ New project** у навігаційному меню.

    ![Select new project.](../../../../../../translated_images/uk/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Введіть **Project name**. Воно має бути унікальним значенням.

    ![Create project.](../../../../../../translated_images/uk/08-05-create-project.4d97f0372f03375a.webp)

1. Виберіть **Create a project**.

#### Додайте кастомне з’єднання для донавченого моделі Phi-3

Щоб інтегрувати вашу кастомну модель Phi-3 із Prompt flow, необхідно зберегти endpoint і ключ моделі у кастомному з’єднанні. Це налаштування гарантує доступ до вашої кастомної моделі Phi-3 у Prompt flow.

#### Встановіть api key і endpoint uri донавченої моделі Phi-3

1. Відвідайте [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Перейдіть до створеного вами Azure Machine learning workspace.

1. Виберіть **Endpoints** у вкладці зліва.

    ![Select endpoints.](../../../../../../translated_images/uk/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Виберіть створений endpoint.

    ![Select endpoints.](../../../../../../translated_images/uk/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Виберіть **Consume** у навігаційному меню.

1. Скопіюйте ваш **REST endpoint** і **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/uk/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Додайте кастомне з’єднання

1. Відвідайте [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Перейдіть до проекту Microsoft Foundry, який ви створили.

1. У створеному проекті виберіть **Settings** у вкладці зліва.

1. Виберіть **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/uk/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Виберіть **Custom keys** у навігаційному меню.

    ![Select custom keys.](../../../../../../translated_images/uk/08-10-select-custom-keys.856f6b2966460551.webp)

1. Виконайте наступні дії:

    - Виберіть **+ Add key value pairs**.
    - Для назви ключа введіть **endpoint** та вставте скопійований із Azure ML Studio endpoint у поле значення.
    - Знову виберіть **+ Add key value pairs**.
    - Для назви ключа введіть **key** і вставте скопійований ключ із Azure ML Studio у поле значення.
    - Після додавання ключів виберіть **is secret**, щоб запобігти їхньому розкриттю.

    ![Add connection.](../../../../../../translated_images/uk/08-11-add-connection.785486badb4d2d26.webp)

1. Виберіть **Add connection**.

#### Створення Prompt flow

Ви додали кастомне з’єднання в Microsoft Foundry. Тепер створимо Prompt flow за наступними кроками. Потім ви під’єднаєте цей Prompt flow до кастомного з’єднання, щоб мати змогу використовувати донавчену модель усередині Prompt flow.

1. Перейдіть до проекту Microsoft Foundry, який ви створили.

1. Виберіть **Prompt flow** у вкладці зліва.

1. Виберіть **+ Create** у навігаційному меню.

    ![Select Promptflow.](../../../../../../translated_images/uk/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Виберіть тип потоку **Chat flow** у навігаційному меню.

    ![Select chat flow.](../../../../../../translated_images/uk/08-13-select-flow-type.2ec689b22da32591.webp)

1. Введіть ім’я **Folder name** для використання.

    ![Enter name.](../../../../../../translated_images/uk/08-14-enter-name.ff9520fefd89f40d.webp)

2. Виберіть **Create**.

#### Налаштування Prompt flow для спілкування з вашим кастомним моделлю Phi-3

Вам потрібно інтегрувати донавчену модель Phi-3 у Prompt flow. Проте існуючий Prompt flow не призначений для цього. Отже, необхідно перепроектувати Prompt flow, щоб дозволити інтеграцію кастомної моделі.

1. У Prompt flow виконайте наступні дії для перебудови існуючого потоку:

    - Виберіть **Raw file mode**.
    - Видаліть весь існуючий код у файлі *flow.dag.yml*.
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

    - Виберіть **Save**.

    ![Select raw file mode.](../../../../../../translated_images/uk/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Додайте наступний код у файл *integrate_with_promptflow.py* для використання кастомної моделі Phi-3 у Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Налаштування ведення журналу
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

        # "connection" — це назва користувацького з'єднання, "endpoint", "key" — це ключі у користувацькому з'єднанні
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
            
            # Записати повну JSON-відповідь у журнал
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

    ![Paste prompt flow code.](../../../../../../translated_images/uk/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Для детальнішої інформації про використання Prompt flow у Microsoft Foundry, ви можете звернутися до [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Виберіть **Chat input**, **Chat output**, щоб увімкнути чат з вашою моделлю.

    ![Input Output.](../../../../../../translated_images/uk/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Тепер ви готові спілкуватися зі своєю кастомною моделлю Phi-3. У наступному вправі ви навчитеся, як запустити Prompt flow і використати його для чату з вашим донавченим моделлю Phi-3.

> [!NOTE]
>
> Перебудований потік має виглядати, як на зображенні нижче:
>
> ![Flow example.](../../../../../../translated_images/uk/08-18-graph-example.d6457533952e690c.webp)
>

### Спілкування з вашим кастомним моделлю Phi-3

Тепер, коли ви донавчили і інтегрували кастомну модель Phi-3 із Prompt flow, ви готові почати взаємодію з нею. Ця вправа провести вас через процес налаштування і запуску чату з вашою моделлю за допомогою Prompt flow. Слідуючи цим крокам, ви зможете повністю використати можливості вашої донавченої моделі Phi-3 для різних завдань і розмов.

- Спілкуйтеся з вашим кастомним моделлю Phi-3 через Prompt flow.

#### Запуск Prompt flow

1. Виберіть **Start compute sessions** для запуску Prompt flow.

    ![Start compute session.](../../../../../../translated_images/uk/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Виберіть **Validate and parse input** для оновлення параметрів.

    ![Validate input.](../../../../../../translated_images/uk/09-02-validate-input.317c76ef766361e9.webp)

1. Виберіть **Value** для **connection**, щоб відзначити кастомне з’єднання, яке ви створили. Наприклад, *connection*.

    ![Connection.](../../../../../../translated_images/uk/09-03-select-connection.99bdddb4b1844023.webp)

#### Спілкування з вашим кастомним моделлю

1. Виберіть **Chat**.

    ![Select chat.](../../../../../../translated_images/uk/09-04-select-chat.61936dce6612a1e6.webp)

1. Приклад результатів: тепер ви можете спілкуватися зі своїм кастомним Phi-3 моделлю. Рекомендується ставити питання, базуючись на даних, які використовувалися для донавчання.

    ![Chat with prompt flow.](../../../../../../translated_images/uk/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ був перекладений за допомогою сервісу машинного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоч ми і прагнемо до точності, будь ласка, майте на увазі, що автоматизовані переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->