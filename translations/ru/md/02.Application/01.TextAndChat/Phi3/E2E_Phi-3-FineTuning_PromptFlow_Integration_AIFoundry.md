# Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt flow в Microsoft Foundry

Этот пошаговый (E2E) пример основан на руководстве "[Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow в Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community. В нем представлены процессы тонкой настройки, развертывания и интеграции пользовательских моделей Phi-3 с Prompt flow в Microsoft Foundry.
В отличие от E2E примера, "[Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", который подразумевал запуск кода локально, этот учебник полностью сосредоточен на тонкой настройке и интеграции вашей модели в Azure AI / ML Studio.

## Обзор

В этом E2E примере вы научитесь тонко настраивать модель Phi-3 и интегрировать ее с Prompt flow в Microsoft Foundry. Используя Azure AI / ML Studio, вы создадите рабочий процесс для развертывания и использования пользовательских моделей ИИ. Этот E2E пример разделен на три сценария:

**Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке**

**Сценарий 2: Тонкая настройка модели Phi-3 и развертывание в Azure Machine Learning Studio**

**Сценарий 3: Интеграция с Prompt flow и общение с вашей пользовательской моделью в Microsoft Foundry**

Вот обзор этого E2E примера.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ru/00-01-architecture.198ba0f1ae6d841a.webp)

### Содержание

1. **[Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке](#сценарий-1-настройка-ресурсов-azure-и-подготовка-к-тонкой-настройке)**
    - [Создание рабочей области Azure Machine Learning](#создание-рабочей-области-azure-machine-learning)
    - [Запрос квот на GPU в подписке Azure](#запрос-квот-на-gpu-в-подписке-azure)
    - [Добавление назначения роли](#добавление-назначения-роли)
    - [Настройка проекта](#настройка-проекта)
    - [Подготовка набора данных для тонкой настройки](#подготовка-набора-данных-для-тонкой-настройки)

1. **[Сценарий 2: Тонкая настройка модели Phi-3 и развертывание в Azure Machine Learning Studio](#сценарий-2-тонкая-настройка-модели-phi-3-и-развертывание-в-azure-machine-learning-studio)**
    - [Тонкая настройка модели Phi-3](#тонкая-настройка-модели-phi-3)
    - [Развертывание тонко настроенной модели Phi-3](#развертывание-тонко-настроенной-модели-phi-3)

1. **[Сценарий 3: Интеграция с Prompt flow и общение с вашей пользовательской моделью в Microsoft Foundry](#сценарий-3-интеграция-с-prompt-flow-и-общение-с-вашей-пользовательской-моделью-в-azure-ai-studio)**
    - [Интеграция пользовательской модели Phi-3 с Prompt flow](#интеграция-пользовательской-модели-phi-3-с-prompt-flow)
    - [Общение с вашей пользовательской моделью Phi-3](#общение-с-вашей-пользовательской-моделью-phi-3)

## Сценарий 1: Настройка ресурсов Azure и подготовка к тонкой настройке

### Создание рабочей области Azure Machine Learning

1. Введите *azure machine learning* в **строке поиска** в верхней части страницы портала и выберите **Azure Machine Learning** из появившихся вариантов.

    ![Type azure machine learning.](../../../../../../translated_images/ru/01-01-type-azml.acae6c5455e67b4b.webp)

2. Выберите **+ Create** в навигационном меню.

3. Выберите **New workspace** в навигационном меню.

    ![Select new workspace.](../../../../../../translated_images/ru/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Выполните следующие действия:

    - Выберите вашу подписку Azure **Subscription**.
    - Выберите **Resource group** для использования (создайте новую при необходимости).
    - Введите **Workspace Name**. Значение должно быть уникальным.
    - Выберите регион **Region**, который вы хотите использовать.
    - Выберите **Storage account** для использования (создайте новый, если нужно).
    - Выберите **Key vault** для использования (создайте новый, если нужно).
    - Выберите **Application insights** для использования (создайте новый, если нужно).
    - Выберите **Container registry** для использования (создайте новый, если нужно).

    ![Fill azure machine learning.](../../../../../../translated_images/ru/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Нажмите **Review + Create**.

6. Нажмите **Create**.

### Запрос квот на GPU в подписке Azure

В этом учебнике вы узнаете, как тонко настраивать и развертывать модель Phi-3 с использованием GPU. Для тонкой настройки вы будете использовать GPU *Standard_NC24ads_A100_v4*, для которого требуется запрос квоты. Для развертывания используется GPU *Standard_NC6s_v3*, для которого также требуется запрос квоты.

> [!NOTE]
>
> GPU выделяются только для подписок типа Pay-As-You-Go (стандартный тип подписки); подписки с льготами в настоящее время не поддерживаются.
>

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выполните следующие действия для запроса квоты *Standard NCADSA100v4 Family*:

    - Выберите **Quota** в левой боковой вкладке.
    - Выберите семейство виртуальных машин (**Virtual machine family**) для использования. Например, **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, которое включает GPU *Standard_NC24ads_A100_v4*.
    - Выберите **Request quota** в навигационном меню.

        ![Request quota.](../../../../../../translated_images/ru/02-02-request-quota.c0428239a63ffdd5.webp)

    - Внутри страницы запроса квоты введите **New cores limit** (новый лимит ядер), который вы хотите использовать. Например, 24.
    - Нажмите **Submit**, чтобы отправить запрос квоты на GPU.

1. Выполните следующие действия для запроса квоты *Standard NCSv3 Family*:

    - Выберите **Quota** в левой боковой вкладке.
    - Выберите семейство виртуальных машин (**Virtual machine family**) для использования. Например, **Standard NCSv3 Family Cluster Dedicated vCPUs**, которое включает GPU *Standard_NC6s_v3*.
    - Выберите **Request quota** в навигационном меню.
    - Введите желаемый новый лимит ядер (**New cores limit**). Например, 24.
    - Нажмите **Submit**, чтобы запросить квоту на GPU.

### Добавление назначения роли

Для тонкой настройки и развертывания моделей необходимо создать Управляемую Идентичность Пользователя (User Assigned Managed Identity, UAI) и назначить ей соответствующие разрешения. Эта UAI будет использоваться для аутентификации при развертывании.

#### Создание User Assigned Managed Identity (UAI)

1. Введите *managed identities* в **строке поиска** в верхней части страницы портала и выберите **Managed Identities** из появившихся вариантов.

    ![Type managed identities.](../../../../../../translated_images/ru/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Выберите **+ Create**.

    ![Select create.](../../../../../../translated_images/ru/03-02-select-create.92bf8989a5cd98f2.webp)

1. Выполните следующие действия:

    - Выберите вашу подписку Azure **Subscription**.
    - Выберите **Resource group** для использования (создайте новую при необходимости).
    - Выберите регион **Region**, который хотите использовать.
    - Введите **Name**. Значение должно быть уникальным.

    ![Select create.](../../../../../../translated_images/ru/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Выберите **Review + create**.

1. Выберите **+ Create**.

#### Назначение роли Contributor для Managed Identity

1. Перейдите в ресурс Управляемой Идентичности, который вы создали.

1. Выберите **Azure role assignments** в левом меню.

1. Выберите **+ Add role assignment** в навигационном меню.

1. На странице назначения роли выполните следующие действия:
    - Выберите область (**Scope**) как **Resource group**.
    - Выберите подписку Azure **Subscription**.
    - Выберите группу ресурсов **Resource group** для использования.
    - Выберите роль **Role** как **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/ru/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Нажмите **Save**.

#### Назначение роли Storage Blob Data Reader для Managed Identity

1. Введите *storage accounts* в **строке поиска** в верхней части страницы портала и выберите **Storage accounts** из появившихся вариантов.

    ![Type storage accounts.](../../../../../../translated_images/ru/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Выберите учетную запись хранения, связанную с рабочей областью Azure Machine Learning, которую вы создали. Например, *finetunephistorage*.

1. Выполните следующие действия для перехода на страницу назначения роли:

    - Перейдите в созданную вами учетную запись Azure Storage.
    - Выберите **Access Control (IAM)** в левом меню.
    - Нажмите **+ Add** в навигационном меню.
    - Выберите **Add role assignment**.

    ![Add role.](../../../../../../translated_images/ru/03-06-add-role.353ccbfdcf0789c2.webp)

1. На странице назначения роли выполните следующие действия:

    - В поле поиска на странице ролей введите *Storage Blob Data Reader* и выберите **Storage Blob Data Reader** из появившихся вариантов.
    - Нажмите **Next**.
    - На странице участников выберите **Assign access to** как **Managed identity**.
    - Выберите **+ Select members**.
    - На странице выбора управляемых идентичностей выберите вашу подписку Azure **Subscription**.
    - Выберите **Managed identity** как **Manage Identity**.
    - Выберите созданную вами управляемую идентичность. Например, *finetunephi-managedidentity*.
    - Нажмите **Select**.

    ![Select managed identity.](../../../../../../translated_images/ru/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Нажмите **Review + assign**.

#### Назначение роли AcrPull для Managed Identity

1. Введите *container registries* в **строке поиска** в верхней части страницы портала и выберите **Container registries** из появившихся вариантов.

    ![Type container registries.](../../../../../../translated_images/ru/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Выберите реестр контейнеров, связанный с рабочей областью Azure Machine Learning. Например, *finetunephicontainerregistry*

1. Выполните следующие действия для перехода на страницу назначения роли:

    - Выберите **Access Control (IAM)** в левом меню.
    - Нажмите **+ Add** в навигационном меню.
    - Выберите **Add role assignment**.

1. На странице назначения роли выполните следующие действия:

    - Введите *AcrPull* в поле поиска и выберите **AcrPull** из появившихся вариантов.
    - Нажмите **Next**.
    - На странице участников выберите **Assign access to** как **Managed identity**.
    - Нажмите **+ Select members**.
    - Выберите вашу подписку Azure **Subscription**.
    - Выберите **Managed identity** как **Manage Identity**.
    - Выберите созданную вами управляему идентичность. Например, *finetunephi-managedidentity*.
    - Нажмите **Select**.
    - Нажмите **Review + assign**.

### Настройка проекта

Для загрузки наборов данных, необходимых для тонкой настройки, вы настроите локальное окружение.

В этом упражнении вам предстоит:

- Создать папку для работы внутри нее.
- Создать виртуальное окружение.
- Установить необходимые пакеты.
- Создать файл *download_dataset.py* для загрузки набора данных.

#### Создание папки для работы внутри нее

1. Откройте терминал и введите следующую команду для создания папки с именем *finetune-phi* в стандартном пути.

    ```console
    mkdir finetune-phi
    ```

2. Введите следующую команду в терминале, чтобы перейти в созданную папку *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Создание виртуального окружения

1. Введите следующую команду в терминале для создания виртуального окружения с именем *.venv*.
    ```console
    python -m venv .venv
    ```

2. Введите следующую команду в терминале, чтобы активировать виртуальное окружение.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Если все прошло успешно, перед приглашением командной строки должно появиться *(.venv)*.

#### Установите необходимые пакеты

1. Введите следующие команды в терминале для установки необходимых пакетов.

    ```console
    pip install datasets==2.19.1
    ```

#### Создайте файл `donload_dataset.py`

> [!NOTE]
> Полная структура папок:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Откройте **Visual Studio Code**.

1. Выберите в меню **Файл**.

1. Выберите **Открыть папку**.

1. Выберите папку *finetune-phi*, которую вы создали, расположенную по пути *C:\Users\yourUserName\finetune-phi*.

    ![Выберите созданную папку.](../../../../../../translated_images/ru/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. В левой панели Visual Studio Code кликните правой кнопкой мыши и выберите **Новый файл**, чтобы создать новый файл с именем *download_dataset.py*.

    ![Создайте новый файл.](../../../../../../translated_images/ru/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Подготовьте набор данных для дообучения

В этом упражнении вы запустите файл *download_dataset.py*, чтобы загрузить наборы данных *ultrachat_200k* в вашу локальную среду. Затем вы использовали эти наборы данных для дообучения модели Phi-3 в Azure Machine Learning.

В этом упражнении вы:

- Добавите код в файл *download_dataset.py* для загрузки наборов данных.
- Запустите файл *download_dataset.py*, чтобы скачать наборы данных в локальную среду.

#### Скачайте набор данных с помощью *download_dataset.py*

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
        # Загрузить набор данных с указанным именем, конфигурацией и долей разделения
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Разделить набор данных на тренировочную и тестовую выборки (80% тренировка, 20% тест)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Создать директорию, если она не существует
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Открыть файл в режиме записи
        with open(filepath, 'w', encoding='utf-8') as f:
            # Итеративно пройтись по каждой записи в наборе данных
            for record in dataset:
                # Сохранить запись в формате JSON и записать её в файл
                json.dump(record, f)
                # Записать символ новой строки для разделения записей
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Загрузить и разделить набор данных ULTRACHAT_200k с конкретной конфигурацией и долей разделения
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Извлечь тренировочные и тестовые наборы данных из разделения
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Сохранить тренировочный набор данных в файл формата JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Сохранить тестовый набор данных в отдельный файл формата JSONL
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Введите следующую команду в терминале, чтобы запустить скрипт и скачать набор данных в вашу локальную среду.

    ```console
    python download_dataset.py
    ```

1. Убедитесь, что наборы данных были успешно сохранены в локальной директории *finetune-phi/data*.

> [!NOTE]
>
> #### Примечание о размере набора данных и времени дообучения
>
> В этом учебном руководстве используется только 1% набора данных (`split='train[:1%]'`). Это значительно сокращает объем данных, ускоряя загрузку и процесс дообучения. Вы можете настроить процентное соотношение, чтобы найти оптимальный баланс между временем обучения и качеством модели. Использование меньшей части набора данных сокращает время дообучения, делая процесс более управляемым для учебного примера.

## Сценарий 2: Дообучение модели Phi-3 и развёртывание в Azure Machine Learning Studio

### Дообучение модели Phi-3

В этом упражнении вы дообучите модель Phi-3 в Azure Machine Learning Studio.

В этом упражнении вы:

- Создадите вычислительный кластер для дообучения.
- Дообучите модель Phi-3 в Azure Machine Learning Studio.

#### Создание вычислительного кластера для дообучения

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите **Вычисления** (Compute) в левой панели.

1. Выберите **Вычислительные кластеры** в меню навигации.

1. Нажмите **+ Новый**.

    ![Выберите вычисления.](../../../../../../translated_images/ru/06-01-select-compute.a29cff290b480252.webp)

1. Выполните следующие действия:

    - Выберите **Регион** для использования.
    - Выберите **Уровень виртуальной машины** — **Dedicated**.
    - Выберите **Тип виртуальной машины** — **GPU**.
    - В фильтре **Размер виртуальной машины** выберите **Выбрать из всех опций**.
    - Выберите размер виртуальной машины **Standard_NC24ads_A100_v4**.

    ![Создайте кластер.](../../../../../../translated_images/ru/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Нажмите **Далее**.

1. Выполните следующие действия:

    - Введите имя кластера (**Compute name**). Имя должно быть уникальным.
    - Установите **Минимальное количество узлов** на **0**.
    - Установите **Максимальное количество узлов** на **1**.
    - Установите время бездействия до масштабирования вниз (**Idle seconds before scale down**) на **120**.

    ![Создайте кластер.](../../../../../../translated_images/ru/06-03-create-cluster.4a54ba20914f3662.webp)

1. Нажмите **Создать**.

#### Дообучение модели Phi-3

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите рабочее пространство Azure Machine Learning, которое вы создали.

    ![Выберите созданное рабочее пространство.](../../../../../../translated_images/ru/06-04-select-workspace.a92934ac04f4f181.webp)

1. Выполните следующие действия:

    - Выберите **Каталог моделей** (Model catalog) в левой панели.
    - В строке поиска введите *phi-3-mini-4k* и выберите **Phi-3-mini-4k-instruct** из появившихся вариантов.

    ![Введите phi-3-mini-4k.](../../../../../../translated_images/ru/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Выберите **Дообучить** (Fine-tune) в меню навигации.

    ![Выберите дообучение.](../../../../../../translated_images/ru/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Выполните следующие действия:

    - В разделе **Выбрать тип задачи** выберите **Chat completion**.
    - Нажмите **+ Выбрать данные**, чтобы загрузить **Обучающие данные**.
    - Для загрузки **Валидационных данных** выберите тип загрузки **Предоставить отдельные данные для проверки**.
    - Нажмите **+ Выбрать данные**, чтобы загрузить **Валидационные данные**.

    ![Заполните страницу дообучения.](../../../../../../translated_images/ru/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Вы можете открыть **Расширенные настройки** для настройки параметров, таких как **learning_rate** и **lr_scheduler_type**, чтобы оптимизировать процесс дообучения согласно вашим требованиям.

1. Нажмите **Завершить**.

1. В этом упражнении вы успешно дообучили модель Phi-3 с помощью Azure Machine Learning. Обратите внимание, что процесс дообучения может занять значительное время. После запуска задания по дообучению необходимо дождаться его завершения. Статус задания можно отслеживать на вкладке Jobs в левой панели вашего рабочего пространства Azure Machine Learning. В следующей серии вы развернете дообученную модель и интегрируете ее с Prompt flow.

    ![Просмотр задания дообучения.](../../../../../../translated_images/ru/06-08-output.2bd32e59930672b1.webp)

### Развертывание дообученной модели Phi-3

Для интеграции дообученной модели Phi-3 с Prompt flow необходимо развернуть модель, чтобы она была доступна для инференса в реальном времени. Этот процесс включает регистрацию модели, создание онлайн-эндпоинта и развертывание модели.

В этом упражнении вы:

- Зарегистрируете дообученную модель в рабочем пространстве Azure Machine Learning.
- Создадите онлайн-эндпоинт.
- Развернете зарегистрированную дообученную модель Phi-3.

#### Регистрация дообученной модели

1. Перейдите на [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Выберите рабочее пространство Azure Machine Learning, которое вы создали.

    ![Выберите созданное рабочее пространство.](../../../../../../translated_images/ru/06-04-select-workspace.a92934ac04f4f181.webp)

1. Выберите **Модели** в левой панели.

1. Нажмите **+ Зарегистрировать**.

1. Выберите **Из вывода задания**.

    ![Регистрация модели.](../../../../../../translated_images/ru/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Выберите созданное вами задание.

    ![Выберите задание.](../../../../../../translated_images/ru/07-02-select-job.3e2e1144cd6cd093.webp)

1. Нажмите **Далее**.

1. Выберите тип модели **MLflow**.

1. Проверьте, что выбрано **Выход задания**; это должно быть выбрано автоматически.

    ![Выберите выход.](../../../../../../translated_images/ru/07-03-select-output.4cf1a0e645baea1f.webp)

2. Нажмите **Далее**.

3. Нажмите **Зарегистрировать**.

    ![Нажмите зарегистрировать.](../../../../../../translated_images/ru/07-04-register.fd82a3b293060bc7.webp)

4. Просмотреть зарегистрированную модель можно через меню **Модели** в левой панели.

    ![Зарегистрированная модель.](../../../../../../translated_images/ru/07-05-registered-model.7db9775f58dfd591.webp)

#### Развертывание дообученной модели

1. Перейдите в рабочее пространство Azure Machine Learning, которое вы создали.

1. Выберите **Эндпоинты** в левой панели.

1. Выберите **Эндпоинты в реальном времени** в меню навигации.

    ![Создать эндпоинт.](../../../../../../translated_images/ru/07-06-create-endpoint.1ba865c606551f09.webp)

1. Нажмите **Создать**.

1. Выберите зарегистрированную модель, которую вы создали.

    ![Выберите зарегистрированную модель.](../../../../../../translated_images/ru/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Нажмите **Выбрать**.

1. Выполните следующие действия:

    - В разделе **Виртуальная машина** выберите *Standard_NC6s_v3*.
    - Укажите количество экземпляров (**Instance count**), например, *1*.
    - В разделе **Эндпоинт** выберите **Новый** для создания эндпоинта.
    - Введите имя эндпоинта (**Endpoint name**). Имя должно быть уникальным.
    - Введите имя развертывания (**Deployment name**). Имя должно быть уникальным.

    ![Заполните настройки развертывания.](../../../../../../translated_images/ru/07-08-deployment-setting.43ddc4209e673784.webp)

1. Нажмите **Развернуть**.

> [!WARNING]
> Чтобы избежать дополнительных расходов на вашем аккаунте, убедитесь, что удалили созданный эндпоинт в рабочем пространстве Azure Machine Learning.
>

#### Проверка состояния развертывания в Azure Machine Learning Workspace

1. Перейдите в рабочее пространство Azure Machine Learning, которое вы создали.

1. Выберите **Эндпоинты** в левой панели.

1. Выберите созданный вами эндпоинт.

    ![Выберите эндпоинты](../../../../../../translated_images/ru/07-09-check-deployment.325d18cae8475ef4.webp)

1. На этой странице вы можете управлять эндпоинтами в процессе развертывания.

> [!NOTE]
> После завершения развертывания убедитесь, что **Live traffic** установлен на **100%**. Если это не так, выберите **Обновить трафик** (Update traffic), чтобы скорректировать настройки трафика. Обратите внимание, что тестировать модель нельзя, если трафик установлен на 0%.
>
> ![Установите трафик.](../../../../../../translated_images/ru/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Сценарий 3: Интеграция с Prompt flow и чат с вашей кастомной моделью в Microsoft Foundry

### Интеграция кастомной модели Phi-3 с Prompt flow

После успешного развёртывания вашей дообученной модели вы можете интегрировать её с Prompt Flow, чтобы использовать модель в приложениях реального времени и выполнять различные интерактивные задачи с вашей кастомной моделью Phi-3.

В этом упражнении вы:

- Создадите Microsoft Foundry Hub.
- Создадите проект Microsoft Foundry.
- Создадите Prompt flow.
- Добавите пользовательское подключение для дообученной модели Phi-3.
- Настроите Prompt flow для общения с вашей кастомной моделью Phi-3.

> [!NOTE]
> Также вы можете интегрироваться с Promptflow через Azure ML Studio. Тот же процесс интеграции применим и для Azure ML Studio.

#### Создание Microsoft Foundry Hub

Перед созданием проекта необходимо создать Hub. Hub действует подобно группе ресурсов, позволяя организовывать и управлять несколькими проектами внутри Microsoft Foundry.
1. Перейдите на [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Выберите **All hubs** на вкладке слева.

1. Выберите **+ New hub** в навигационном меню.

    ![Create hub.](../../../../../../translated_images/ru/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Выполните следующие действия:

    - Введите **Hub name**. Оно должно быть уникальным значением.
    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Resource group** для использования (создайте новую при необходимости).
    - Выберите **Location**, которую хотите использовать.
    - Выберите **Connect Azure AI Services** для использования (создайте новую при необходимости).
    - Выберите **Connect Azure AI Search** и **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/ru/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Нажмите **Next**.

#### Создание проекта Microsoft Foundry

1. В созданном вами хабе выберите **All projects** на вкладке слева.

1. Выберите **+ New project** в навигационном меню.

    ![Select new project.](../../../../../../translated_images/ru/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Введите **Project name**. Оно должно быть уникальным значением.

    ![Create project.](../../../../../../translated_images/ru/08-05-create-project.4d97f0372f03375a.webp)

1. Нажмите **Create a project**.

#### Добавление пользовательского подключения для дообученной модели Phi-3

Чтобы интегрировать вашу пользовательскую модель Phi-3 с Prompt flow, необходимо сохранить конечную точку модели и ключ в пользовательском подключении. Такая настройка обеспечивает доступ к вашей пользовательской модели Phi-3 в Prompt flow.

#### Установка ключа api и URI конечной точки дообученной модели Phi-3

1. Перейдите в [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Перейдите в рабочее пространство Azure Machine learning, которое вы создали.

1. Выберите **Endpoints** на вкладке слева.

    ![Select endpoints.](../../../../../../translated_images/ru/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Выберите созданную вами конечную точку.

    ![Select endpoints.](../../../../../../translated_images/ru/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Выберите **Consume** в навигационном меню.

1. Скопируйте ваш **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ru/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Добавление пользовательского подключения

1. Перейдите на [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Перейдите в созданный вами проект Microsoft Foundry.

1. В созданном проекте выберите **Settings** на вкладке слева.

1. Нажмите **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/ru/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Выберите **Custom keys** в навигационном меню.

    ![Select custom keys.](../../../../../../translated_images/ru/08-10-select-custom-keys.856f6b2966460551.webp)

1. Выполните следующие шаги:

    - Нажмите **+ Add key value pairs**.
    - Введите в поле имени ключа **endpoint** и вставьте скопированный из Azure ML Studio endpoint в поле значения.
    - Снова нажмите **+ Add key value pairs**.
    - Введите в поле имени ключа **key** и вставьте скопированный из Azure ML Studio ключ в поле значения.
    - После добавления ключей выберите **is secret**, чтобы защитить ключ от отображения.

    ![Add connection.](../../../../../../translated_images/ru/08-11-add-connection.785486badb4d2d26.webp)

1. Нажмите **Add connection**.

#### Создание Prompt flow

Вы добавили пользовательское подключение в Microsoft Foundry. Теперь создадим Prompt flow, используя следующие шаги. Затем вы подключите этот Prompt flow к пользовательскому подключению, чтобы использовать дообученную модель в Prompt flow.

1. Перейдите в созданный вами проект Microsoft Foundry.

1. Выберите **Prompt flow** на вкладке слева.

1. Нажмите **+ Create** в навигационном меню.

    ![Select Promptflow.](../../../../../../translated_images/ru/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Выберите **Chat flow** в навигационном меню.

    ![Select chat flow.](../../../../../../translated_images/ru/08-13-select-flow-type.2ec689b22da32591.webp)

1. Введите имя папки, которую хотите использовать (**Folder name**).

    ![Enter name.](../../../../../../translated_images/ru/08-14-enter-name.ff9520fefd89f40d.webp)

2. Нажмите **Create**.

#### Настройка Prompt flow для общения с вашей пользовательской моделью Phi-3

Вам необходимо интегрировать дообученную модель Phi-3 в Prompt flow. Однако существующий Prompt flow не предназначен для этой цели, поэтому необходимо переделать Prompt flow, чтобы обеспечить интеграцию пользовательской модели.

1. В Prompt flow выполните следующие действия для перестройки существующего потока:

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

    ![Select raw file mode.](../../../../../../translated_images/ru/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Добавьте следующий код в файл *integrate_with_promptflow.py* для использования вашей пользовательской модели Phi-3 в Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Настройка логирования
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

        # "connection" — это имя Пользовательского подключения, "endpoint", "key" — ключи в Пользовательском подключении
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
            
            # Записать полный JSON-ответ в лог
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

    ![Paste prompt flow code.](../../../../../../translated_images/ru/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Для получения более подробной информации по использованию Prompt flow в Microsoft Foundry обратитесь к [Prompt flow в Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Включите **Chat input** и **Chat output** для общения с вашей моделью.

    ![Input Output.](../../../../../../translated_images/ru/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Теперь вы готовы общаться с вашей пользовательской моделью Phi-3. В следующем упражнении вы узнаете, как запустить Prompt flow и использовать его для общения с вашей дообученной моделью Phi-3.

> [!NOTE]
>
> Переделанный поток должен выглядеть как на изображении ниже:
>
> ![Flow example.](../../../../../../translated_images/ru/08-18-graph-example.d6457533952e690c.webp)
>

### Общение с вашей пользовательской моделью Phi-3

Теперь, когда вы дообучили и интегрировали свою пользовательскую модель Phi-3 с Prompt flow, вы готовы начать взаимодействие с ней. Это упражнение проведет вас через процесс настройки и запуска чата с вашей моделью с использованием Prompt flow. Следуя этим шагам, вы сможете полностью использовать возможности вашей дообученной модели Phi-3 для различных задач и бесед.

- Общайтесь с вашей пользовательской моделью Phi-3 с помощью Prompt flow.

#### Запуск Prompt flow

1. Нажмите **Start compute sessions**, чтобы запустить Prompt flow.

    ![Start compute session.](../../../../../../translated_images/ru/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Нажмите **Validate and parse input**, чтобы обновить параметры.

    ![Validate input.](../../../../../../translated_images/ru/09-02-validate-input.317c76ef766361e9.webp)

1. Выберите значение **Value** для **connection** — это ваше созданное пользовательское подключение. Например, *connection*.

    ![Connection.](../../../../../../translated_images/ru/09-03-select-connection.99bdddb4b1844023.webp)

#### Общение с вашей пользовательской моделью

1. Нажмите **Chat**.

    ![Select chat.](../../../../../../translated_images/ru/09-04-select-chat.61936dce6612a1e6.webp)

1. Вот пример результата: теперь вы можете общаться с вашей пользовательской моделью Phi-3. Рекомендуется задавать вопросы, основанные на данных, использованных для обучения.

    ![Chat with prompt flow.](../../../../../../translated_images/ru/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, пожалуйста, учтите, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется использовать профессиональный перевод, выполненный человеком. Мы не несем ответственности за любые недоразумения или искажения, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->