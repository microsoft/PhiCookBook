<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T00:59:45+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ru"
}
-->
# Тонкая настройка и интеграция кастомных моделей Phi-3 с Prompt flow в Azure AI Foundry

Этот сквозной (E2E) пример основан на руководстве "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community. В нем описываются процессы тонкой настройки, развертывания и интеграции кастомных моделей Phi-3 с Prompt flow в Azure AI Foundry. В отличие от E2E примера "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", где код запускался локально, этот туториал полностью сосредоточен на тонкой настройке и интеграции модели внутри Azure AI / ML Studio.

## Обзор

В этом E2E примере вы научитесь тонко настраивать модель Phi-3 и интегрировать её с Prompt flow в Azure AI Foundry. Используя Azure AI / ML Studio, вы создадите рабочий процесс для развертывания и использования кастомных AI моделей. Пример разделён на три сценария:

**Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке**

**Сценарий 2: Тонкая настройка модели Phi-3 и развертывание в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и общение с вашей кастомной моделью в Azure AI Foundry**

Ниже представлен обзор этого E2E примера.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a.ru.png)

### Содержание

1. **[Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Создание рабочего пространства Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Запрос квот на GPU в подписке Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Добавление назначения роли](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Настройка проекта](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Подготовка набора данных для тонкой настройки](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 2: Тонкая настройка модели Phi-3 и развертывание в Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Тонкая настройка модели Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Развертывание тонко настроенной модели Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Сценарий 3: Интеграция с Prompt flow и общение с вашей кастомной моделью в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Интеграция кастомной модели Phi-3 с Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Общение с вашей кастомной моделью Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке

### Создание рабочего пространства Azure Machine Learning

1. Введите *azure machine learning* в **строке поиска** в верхней части портала и выберите **Azure Machine Learning** из появившихся вариантов.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b.ru.png)

2. Выберите **+ Create** в навигационном меню.

3. Выберите **New workspace** в навигационном меню.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2.ru.png)

4. Выполните следующие действия:

    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Resource group** для использования (создайте новую, если нужно).
    - Введите **Workspace Name**. Имя должно быть уникальным.
    - Выберите регион (**Region**), который хотите использовать.
    - Выберите **Storage account** для использования (создайте новый, если нужно).
    - Выберите **Key vault** для использования (создайте новый, если нужно).
    - Выберите **Application insights** для использования (создайте новый, если нужно).
    - Выберите **Container registry** для использования (создайте новый, если нужно).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090f.ru.png)

5. Нажмите **Review + Create**.

6. Нажмите **Create**.

### Запрос квот на GPU в подписке Azure

В этом туториале вы научитесь тонко настраивать и развертывать модель Phi-3 с использованием GPU. Для тонкой настройки будет использоваться GPU *Standard_NC24ads_A100_v4*, для которого требуется запрос квоты. Для развертывания будет использоваться GPU *Standard_NC6s_v3*, для которого также необходим запрос квоты.

> [!NOTE]
>
> Квоты на GPU доступны только для подписок Pay-As-You-Go (стандартный тип подписки); подписки с льготами пока не поддерживаются.
>

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выполните следующие действия для запроса квоты *Standard NCADSA100v4 Family*:

    - Выберите **Quota** в левой панели.
    - Выберите семейство виртуальных машин (**Virtual machine family**), например, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, которое включает GPU *Standard_NC24ads_A100_v4*.
    - Выберите **Request quota** в навигационном меню.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd5.ru.png)

    - На странице запроса квоты введите желаемый **New cores limit**, например, 24.
    - Нажмите **Submit** для отправки запроса квоты на GPU.

1. Выполните следующие действия для запроса квоты *Standard NCSv3 Family*:

    - Выберите **Quota** в левой панели.
    - Выберите семейство виртуальных машин, например, **Standard NCSv3 Family Cluster Dedicated vCPUs**, которое включает GPU *Standard_NC6s_v3*.
    - Выберите **Request quota** в навигационном меню.
    - Введите желаемый **New cores limit**, например, 24.
    - Нажмите **Submit** для отправки запроса квоты на GPU.

### Добавление назначения роли

Для тонкой настройки и развертывания моделей необходимо сначала создать User Assigned Managed Identity (UAI) и назначить ей соответствующие разрешения. Эта UAI будет использоваться для аутентификации при развертывании.

#### Создание User Assigned Managed Identity (UAI)

1. Введите *managed identities* в **строке поиска** в верхней части портала и выберите **Managed Identities** из появившихся вариантов.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e5.ru.png)

1. Нажмите **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f2.ru.png)

1. Выполните следующие действия:

    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Resource group** для использования (создайте новую, если нужно).
    - Выберите регион (**Region**), который хотите использовать.
    - Введите имя (**Name**). Имя должно быть уникальным.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0.ru.png)

1. Нажмите **Review + create**.

1. Нажмите **+ Create**.

#### Назначение роли Contributor для Managed Identity

1. Перейдите к ресурсу Managed Identity, который вы создали.

1. Выберите **Azure role assignments** в левой панели.

1. Нажмите **+Add role assignment** в навигационном меню.

1. На странице добавления назначения роли выполните следующие действия:
    - В поле **Scope** выберите **Resource group**.
    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Resource group** для использования.
    - В поле **Role** выберите **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d.ru.png)

2. Нажмите **Save**.

#### Назначение роли Storage Blob Data Reader для Managed Identity

1. Введите *storage accounts* в **строке поиска** в верхней части портала и выберите **Storage accounts** из появившихся вариантов.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e5.ru.png)

1. Выберите аккаунт хранения, связанный с вашим рабочим пространством Azure Machine Learning. Например, *finetunephistorage*.

1. Выполните следующие действия, чтобы перейти на страницу добавления назначения роли:

    - Перейдите в созданный аккаунт хранения Azure.
    - Выберите **Access Control (IAM)** в левой панели.
    - Нажмите **+ Add** в навигационном меню.
    - Выберите **Add role assignment**.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c2.ru.png)

1. На странице добавления назначения роли выполните следующие действия:

    - В поле поиска ролей введите *Storage Blob Data Reader* и выберите **Storage Blob Data Reader** из списка.
    - Нажмите **Next**.
    - На странице участников выберите **Assign access to** — **Managed identity**.
    - Нажмите **+ Select members**.
    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Managed identity**.
    - Выберите созданную Managed Identity, например, *finetunephi-managedidentity*.
    - Нажмите **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25.ru.png)

1. Нажмите **Review + assign**.

#### Назначение роли AcrPull для Managed Identity

1. Введите *container registries* в **строке поиска** в верхней части портала и выберите **Container registries** из появившихся вариантов.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a6.ru.png)

1. Выберите реестр контейнеров, связанный с вашим рабочим пространством Azure Machine Learning. Например, *finetunephicontainerregistry*.

1. Выполните следующие действия, чтобы перейти на страницу добавления назначения роли:

    - Выберите **Access Control (IAM)** в левой панели.
    - Нажмите **+ Add** в навигационном меню.
    - Выберите **Add role assignment**.

1. На странице добавления назначения роли выполните следующие действия:

    - В поле поиска ролей введите *AcrPull* и выберите **AcrPull** из списка.
    - Нажмите **Next**.
    - На странице участников выберите **Assign access to** — **Managed identity**.
    - Нажмите **+ Select members**.
    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Managed identity**.
    - Выберите созданную Managed Identity, например, *finetunephi-managedidentity*.
    - Нажмите **Select**.
    - Нажмите **Review + assign**.

### Настройка проекта

Для загрузки наборов данных, необходимых для тонкой настройки, вы настроите локальное окружение.

В этом упражнении вы:

- Создадите папку для работы.
- Создадите виртуальное окружение.
- Установите необходимые пакеты.
- Создадите файл *download_dataset.py* для загрузки набора данных.

#### Создание папки для работы

1. Откройте терминал и выполните команду для создания папки с именем *finetune-phi* в стандартном пути.

    ```console
    mkdir finetune-phi
    ```

2. Введите следующую команду в терминале, чтобы перейти в созданную папку *finetune-phi*.
#### Создание виртуального окружения

1. Введите следующую команду в терминале, чтобы создать виртуальное окружение с именем *.venv*.

    ```console
    python -m venv .venv
    ```

2. Введите следующую команду в терминале, чтобы активировать виртуальное окружение.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Если всё прошло успешно, перед приглашением командной строки вы увидите *(.venv)*.

#### Установка необходимых пакетов

1. Введите следующие команды в терминале для установки необходимых пакетов.

    ```console
    pip install datasets==2.19.1
    ```

#### Создание файла `download_dataset.py`

> [!NOTE]
> Полная структура папок:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Откройте **Visual Studio Code**.

1. В меню выберите **File**.

1. Выберите **Open Folder**.

1. Выберите папку *finetune-phi*, которую вы создали, расположенную по пути *C:\Users\yourUserName\finetune-phi*.

    ![Выберите созданную папку.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6.ru.png)

1. В левой панели Visual Studio Code кликните правой кнопкой мыши и выберите **New File**, чтобы создать новый файл с именем *download_dataset.py*.

    ![Создайте новый файл.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff92.ru.png)

### Подготовка датасета для дообучения

В этом упражнении вы запустите файл *download_dataset.py*, чтобы скачать датасеты *ultrachat_200k* в локальное окружение. Затем вы используете эти датасеты для дообучения модели Phi-3 в Azure Machine Learning.

В этом упражнении вы:

- Добавите код в файл *download_dataset.py* для скачивания датасетов.
- Запустите файл *download_dataset.py* для загрузки датасетов в локальное окружение.

#### Скачивание датасета с помощью *download_dataset.py*

1. Откройте файл *download_dataset.py* в Visual Studio Code.

1. Добавьте следующий код в файл *download_dataset.py*.

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

1. Введите следующую команду в терминале, чтобы запустить скрипт и скачать датасет в локальное окружение.

    ```console
    python download_dataset.py
    ```

1. Проверьте, что датасеты успешно сохранились в локальной папке *finetune-phi/data*.

> [!NOTE]
>
> #### Примечание о размере датасета и времени дообучения
>
> В этом руководстве используется только 1% датасета (`split='train[:1%]'`). Это значительно уменьшает объем данных, ускоряя загрузку и процесс дообучения. Вы можете изменить этот процент, чтобы найти оптимальный баланс между временем обучения и качеством модели. Использование меньшей части датасета сокращает время дообучения, что делает процесс более удобным для учебных целей.

## Сценарий 2: Дообучение модели Phi-3 и развертывание в Azure Machine Learning Studio

### Дообучение модели Phi-3

В этом упражнении вы дообучите модель Phi-3 в Azure Machine Learning Studio.

В этом упражнении вы:

- Создадите вычислительный кластер для дообучения.
- Дообучите модель Phi-3 в Azure Machine Learning Studio.

#### Создание вычислительного кластера для дообучения

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите **Compute** в левой панели.

1. Выберите **Compute clusters** в навигационном меню.

1. Нажмите **+ New**.

    ![Выберите compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252.ru.png)

1. Выполните следующие действия:

    - Выберите **Region** (регион), который хотите использовать.
    - Выберите **Virtual machine tier** — **Dedicated**.
    - Выберите **Virtual machine type** — **GPU**.
    - В фильтре **Virtual machine size** выберите **Select from all options**.
    - Выберите размер виртуальной машины **Standard_NC24ads_A100_v4**.

    ![Создание кластера.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e.ru.png)

1. Нажмите **Next**.

1. Выполните следующие действия:

    - Введите уникальное имя в поле **Compute name**.
    - Установите **Minimum number of nodes** в значение **0**.
    - Установите **Maximum number of nodes** в значение **1**.
    - Установите **Idle seconds before scale down** в **120**.

    ![Создание кластера.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662.ru.png)

1. Нажмите **Create**.

#### Дообучение модели Phi-3

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите созданное вами рабочее пространство Azure Machine Learning.

    ![Выберите созданное рабочее пространство.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.ru.png)

1. Выполните следующие действия:

    - Выберите **Model catalog** в левой панели.
    - Введите *phi-3-mini-4k* в строку поиска и выберите **Phi-3-mini-4k-instruct** из появившихся вариантов.

    ![Введите phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.ru.png)

1. Выберите **Fine-tune** в навигационном меню.

    ![Выберите fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeec.ru.png)

1. Выполните следующие действия:

    - Выберите **Select task type** — **Chat completion**.
    - Нажмите **+ Select data** для загрузки **Training data**.
    - Для загрузки валидационных данных выберите тип загрузки **Provide different validation data**.
    - Нажмите **+ Select data** для загрузки **Validation data**.

    ![Заполните страницу дообучения.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0b.ru.png)

    > [!TIP]
    >
    > Вы можете выбрать **Advanced settings** для настройки параметров, таких как **learning_rate** и **lr_scheduler_type**, чтобы оптимизировать процесс дообучения под ваши задачи.

1. Нажмите **Finish**.

1. В этом упражнении вы успешно дообучили модель Phi-3 с помощью Azure Machine Learning. Обратите внимание, что процесс дообучения может занять значительное время. После запуска задачи дообучения необходимо дождаться её завершения. Статус задачи можно отслеживать во вкладке Jobs в левой панели вашего рабочего пространства Azure Machine Learning. В следующем разделе вы развернете дообученную модель и интегрируете её с Prompt flow.

    ![Просмотр задачи дообучения.](../../../../../../translated_images/06-08-output.2bd32e59930672b1.ru.png)

### Развертывание дообученной модели Phi-3

Для интеграции дообученной модели Phi-3 с Prompt flow необходимо развернуть модель, чтобы обеспечить доступ к ней для инференса в реальном времени. Этот процесс включает регистрацию модели, создание онлайн-эндпоинта и развертывание модели.

В этом упражнении вы:

- Зарегистрируете дообученную модель в рабочем пространстве Azure Machine Learning.
- Создадите онлайн-эндпоинт.
- Развернете зарегистрированную дообученную модель Phi-3.

#### Регистрация дообученной модели

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите созданное вами рабочее пространство Azure Machine Learning.

    ![Выберите созданное рабочее пространство.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.ru.png)

1. Выберите **Models** в левой панели.
1. Нажмите **+ Register**.
1. Выберите **From a job output**.

    ![Регистрация модели.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777.ru.png)

1. Выберите созданную вами задачу.

    ![Выберите задачу.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd093.ru.png)

1. Нажмите **Next**.

1. Выберите **Model type** — **MLflow**.

1. Убедитесь, что выбран пункт **Job output**; он должен быть выбран автоматически.

    ![Выберите вывод.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f.ru.png)

2. Нажмите **Next**.

3. Нажмите **Register**.

    ![Нажмите зарегистрировать.](../../../../../../translated_images/07-04-register.fd82a3b293060bc7.ru.png)

4. Вы можете просмотреть зарегистрированную модель, перейдя в меню **Models** в левой панели.

    ![Зарегистрированная модель.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591.ru.png)

#### Развертывание дообученной модели

1. Перейдите в созданное вами рабочее пространство Azure Machine Learning.

1. Выберите **Endpoints** в левой панели.

1. Выберите **Real-time endpoints** в навигационном меню.

    ![Создание эндпоинта.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09.ru.png)

1. Нажмите **Create**.

1. Выберите зарегистрированную модель, которую вы создали.

    ![Выберите зарегистрированную модель.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4.ru.png)

1. Нажмите **Select**.

1. Выполните следующие действия:

    - Выберите **Virtual machine** — *Standard_NC6s_v3*.
    - Укажите желаемое количество экземпляров (**Instance count**), например, *1*.
    - Выберите **Endpoint** — **New** для создания нового эндпоинта.
    - Введите уникальное имя для **Endpoint name**.
    - Введите уникальное имя для **Deployment name**.

    ![Заполните настройки развертывания.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e673784.ru.png)

1. Нажмите **Deploy**.

> [!WARNING]
> Чтобы избежать дополнительных расходов, не забудьте удалить созданный эндпоинт в рабочем пространстве Azure Machine Learning.
>

#### Проверка статуса развертывания в Azure Machine Learning Workspace

1. Перейдите в созданное вами рабочее пространство Azure Machine Learning.

1. Выберите **Endpoints** в левой панели.

1. Выберите созданный вами эндпоинт.

    ![Выберите эндпоинты](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4.ru.png)

1. На этой странице вы можете управлять эндпоинтами во время процесса развертывания.

> [!NOTE]
> После завершения развертывания убедитесь, что **Live traffic** установлен на **100%**. Если это не так, выберите **Update traffic** для корректировки настроек трафика. Обратите внимание, что тестировать модель нельзя, если трафик установлен в 0%.
>
> ![Настройка трафика.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d.ru.png)
>

## Сценарий 3: Интеграция с Prompt flow и общение с вашей кастомной моделью в Azure AI Foundry

### Интеграция кастомной модели Phi-3 с Prompt flow

После успешного развертывания дообученной модели вы можете интегрировать её с Prompt Flow для использования в приложениях в реальном времени, что позволит выполнять различные интерактивные задачи с вашей кастомной моделью Phi-3.

В этом упражнении вы:

- Создадите Azure AI Foundry Hub.
- Создадите проект Azure AI Foundry.
- Создадите Prompt flow.
- Добавите кастомное подключение для дообученной модели Phi-3.
- Настроите Prompt flow для общения с вашей кастомной моделью Phi-3.
> [!NOTE]
> Вы также можете интегрироваться с Promptflow, используя Azure ML Studio. Тот же процесс интеграции применим и к Azure ML Studio.
#### Создание Azure AI Foundry Hub

Перед созданием проекта необходимо создать Hub. Hub действует как группа ресурсов, позволяя организовывать и управлять несколькими проектами в Azure AI Foundry.

1. Перейдите на [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Выберите **All hubs** в левой панели.

1. Выберите **+ New hub** в навигационном меню.

    ![Создание хаба.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834.ru.png)

1. Выполните следующие действия:

    - Введите **Hub name**. Значение должно быть уникальным.
    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Resource group** для использования (создайте новую, если нужно).
    - Выберите **Location**, которую хотите использовать.
    - Выберите **Connect Azure AI Services** для подключения (создайте новое, если нужно).
    - Для **Connect Azure AI Search** выберите **Skip connecting**.

    ![Заполнение хаба.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c.ru.png)

1. Нажмите **Next**.

#### Создание проекта Azure AI Foundry

1. В созданном Hub выберите **All projects** в левой панели.

1. Выберите **+ New project** в навигационном меню.

    ![Выбор нового проекта.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f12.ru.png)

1. Введите **Project name**. Имя должно быть уникальным.

    ![Создание проекта.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a.ru.png)

1. Нажмите **Create a project**.

#### Добавление пользовательского подключения для дообученной модели Phi-3

Чтобы интегрировать вашу дообученную модель Phi-3 с Prompt flow, необходимо сохранить endpoint и ключ модели в пользовательском подключении. Это обеспечит доступ к вашей модели Phi-3 в Prompt flow.

#### Установка api key и endpoint uri для дообученной модели Phi-3

1. Перейдите в [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Откройте рабочее пространство Azure Machine learning, которое вы создали.

1. Выберите **Endpoints** в левой панели.

    ![Выбор endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf9605.ru.png)

1. Выберите созданный вами endpoint.

    ![Выбор созданного endpoint.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275e.ru.png)

1. В навигационном меню выберите **Consume**.

1. Скопируйте ваш **REST endpoint** и **Primary key**.

    ![Копирование api key и endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cb.ru.png)

#### Добавление пользовательского подключения

1. Перейдите на [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Откройте созданный вами проект Azure AI Foundry.

1. В проекте выберите **Settings** в левой панели.

1. Нажмите **+ New connection**.

    ![Выбор нового подключения.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc.ru.png)

1. В навигационном меню выберите **Custom keys**.

    ![Выбор custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b2966460551.ru.png)

1. Выполните следующие действия:

    - Нажмите **+ Add key value pairs**.
    - В поле имени ключа введите **endpoint** и вставьте скопированный из Azure ML Studio endpoint в поле значения.
    - Снова нажмите **+ Add key value pairs**.
    - Введите имя ключа **key** и вставьте скопированный ключ из Azure ML Studio в поле значения.
    - После добавления ключей отметьте **is secret**, чтобы ключи не были видны.

    ![Добавление подключения.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26.ru.png)

1. Нажмите **Add connection**.

#### Создание Prompt flow

Вы добавили пользовательское подключение в Azure AI Foundry. Теперь создадим Prompt flow, используя следующие шаги. Затем вы подключите этот Prompt flow к пользовательскому подключению, чтобы использовать дообученную модель внутри Prompt flow.

1. Откройте созданный проект Azure AI Foundry.

1. Выберите **Prompt flow** в левой панели.

1. Нажмите **+ Create** в навигационном меню.

    ![Выбор Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5b.ru.png)

1. В навигационном меню выберите **Chat flow**.

    ![Выбор chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591.ru.png)

1. Введите имя папки (**Folder name**).

    ![Ввод имени.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d.ru.png)

2. Нажмите **Create**.

#### Настройка Prompt flow для общения с вашей дообученной моделью Phi-3

Необходимо интегрировать дообученную модель Phi-3 в Prompt flow. Однако существующий Prompt flow не предназначен для этого, поэтому его нужно переработать для поддержки пользовательской модели.

1. В Prompt flow выполните следующие действия для перестройки текущего потока:

    - Выберите **Raw file mode**.
    - Удалите весь существующий код в файле *flow.dag.yml*.
    - Добавьте следующий код в файл *flow.dag.yml*.

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

    - Нажмите **Save**.

    ![Выбор raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985.ru.png)

1. Добавьте следующий код в файл *integrate_with_promptflow.py* для использования пользовательской модели Phi-3 в Prompt flow.

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

    ![Вставка кода prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d09777.ru.png)

> [!NOTE]
> Для более подробной информации по использованию Prompt flow в Azure AI Foundry обратитесь к [Prompt flow в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Выберите **Chat input** и **Chat output**, чтобы включить чат с вашей моделью.

    ![Выбор input и output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03b.ru.png)

1. Теперь вы готовы общаться с вашей дообученной моделью Phi-3. В следующем упражнении вы узнаете, как запустить Prompt flow и использовать его для общения с вашей моделью.

> [!NOTE]
>
> Перестроенный поток должен выглядеть примерно так:
>
> ![Пример потока.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c.ru.png)
>

### Общение с вашей дообученной моделью Phi-3

Теперь, когда вы дообучили и интегрировали вашу модель Phi-3 с Prompt flow, вы готовы начать взаимодействие с ней. В этом упражнении вы пройдёте процесс настройки и запуска чата с моделью через Prompt flow. Следуя этим шагам, вы сможете полноценно использовать возможности вашей дообученной модели Phi-3 для различных задач и диалогов.

- Общайтесь с вашей дообученной моделью Phi-3 через Prompt flow.

#### Запуск Prompt flow

1. Нажмите **Start compute sessions** для запуска Prompt flow.

    ![Запуск compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b.ru.png)

1. Нажмите **Validate and parse input** для обновления параметров.

    ![Проверка ввода.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e9.ru.png)

1. Выберите значение **Value** для **connection**, соответствующее созданному вами пользовательскому подключению, например *connection*.

    ![Выбор подключения.](../../../../../../translated_images/09-03-select-connection.99bdddb4b1844023.ru.png)

#### Общение с вашей пользовательской моделью

1. Нажмите **Chat**.

    ![Выбор чата.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e6.ru.png)

1. Пример результата: теперь вы можете общаться с вашей дообученной моделью Phi-3. Рекомендуется задавать вопросы, основанные на данных, использованных для дообучения.

    ![Чат с prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126f.ru.png)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.