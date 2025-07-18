<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:12:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "ru"
}
-->
# Оценка дообученной модели Phi-3 / Phi-3.5 в Azure AI Foundry с акцентом на принципы ответственного ИИ Microsoft

Этот сквозной (E2E) пример основан на руководстве "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" из сообщества Microsoft Tech Community.

## Обзор

### Как оценить безопасность и производительность дообученной модели Phi-3 / Phi-3.5 в Azure AI Foundry?

Дообучение модели иногда может привести к непреднамеренным или нежелательным ответам. Чтобы убедиться, что модель остаётся безопасной и эффективной, важно оценить её потенциал к генерации вредоносного контента, а также способность выдавать точные, релевантные и связные ответы. В этом руководстве вы научитесь оценивать безопасность и производительность дообученной модели Phi-3 / Phi-3.5, интегрированной с Prompt flow в Azure AI Foundry.

Ниже представлен процесс оценки в Azure AI Foundry.

![Архитектура руководства.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.ru.png)

*Источник изображения: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Для более подробной информации и дополнительных ресурсов о Phi-3 / Phi-3.5 посетите [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Требования

- [Python](https://www.python.org/downloads)
- [Подписка Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Дообученная модель Phi-3 / Phi-3.5

### Содержание

1. [**Сценарий 1: Введение в оценку Prompt flow в Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Введение в оценку безопасности](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Введение в оценку производительности](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Сценарий 2: Оценка модели Phi-3 / Phi-3.5 в Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Перед началом](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Развертывание Azure OpenAI для оценки модели Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Оценка дообученной модели Phi-3 / Phi-3.5 с помощью Prompt flow в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Поздравляем!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Сценарий 1: Введение в оценку Prompt flow в Azure AI Foundry**

### Введение в оценку безопасности

Чтобы убедиться, что ваша модель ИИ этична и безопасна, важно оценить её в соответствии с принципами ответственного ИИ Microsoft. В Azure AI Foundry оценки безопасности позволяют проверить уязвимость модели к атакам jailbreak и её потенциал к генерации вредоносного контента, что напрямую соответствует этим принципам.

![Оценка безопасности.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.ru.png)

*Источник изображения: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Принципы ответственного ИИ Microsoft

Перед началом технических шагов важно понять принципы ответственного ИИ Microsoft — этическую основу, которая направляет ответственную разработку, внедрение и эксплуатацию систем ИИ. Эти принципы обеспечивают справедливость, прозрачность и инклюзивность при создании ИИ-технологий. Они служат фундаментом для оценки безопасности моделей ИИ.

Принципы ответственного ИИ Microsoft включают:

- **Справедливость и инклюзивность**: Системы ИИ должны относиться ко всем справедливо и избегать различного обращения с группами людей в схожих ситуациях. Например, при предоставлении рекомендаций по медицинскому лечению, кредитным заявкам или трудоустройству ИИ должен давать одинаковые рекомендации всем с похожими симптомами, финансовым положением или квалификацией.

- **Надёжность и безопасность**: Для формирования доверия системы ИИ должны работать надёжно, безопасно и последовательно. Они должны функционировать согласно изначальному замыслу, безопасно реагировать на непредвиденные ситуации и противостоять вредоносным манипуляциям. Их поведение и диапазон условий, с которыми они справляются, отражают ситуации, предусмотренные разработчиками на этапе проектирования и тестирования.

- **Прозрачность**: Когда системы ИИ влияют на решения, существенно меняющие жизнь людей, важно, чтобы люди понимали, как эти решения принимаются. Например, банк может использовать ИИ для оценки кредитоспособности, а компания — для выбора наиболее квалифицированных кандидатов.

- **Конфиденциальность и безопасность**: С ростом распространённости ИИ защита конфиденциальности и безопасности личной и корпоративной информации становится всё более важной и сложной задачей. Для ИИ особенно важно внимательно относиться к этим аспектам, так как доступ к данным необходим для точных и обоснованных прогнозов и решений.

- **Ответственность**: Люди, разрабатывающие и внедряющие системы ИИ, должны нести ответственность за их работу. Организации должны опираться на отраслевые стандарты для формирования норм ответственности. Эти нормы гарантируют, что системы ИИ не являются окончательным авторитетом в решениях, влияющих на жизнь людей, и что человек сохраняет значимый контроль над высокоавтономными системами ИИ.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.ru.png)

*Источник изображения: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Чтобы узнать больше о принципах ответственного ИИ Microsoft, посетите страницу [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрики безопасности

В этом руководстве вы оцените безопасность дообученной модели Phi-3 с помощью метрик безопасности Azure AI Foundry. Эти метрики помогают определить потенциал модели к генерации вредоносного контента и её уязвимость к jailbreak-атакам. Метрики безопасности включают:

- **Контент, связанный с самоповреждением**: Оценивает склонность модели генерировать контент, связанный с самоповреждением.
- **Ненавистнический и несправедливый контент**: Оценивает склонность модели создавать ненавистнический или несправедливый контент.
- **Насильственный контент**: Оценивает склонность модели генерировать насильственный контент.
- **Сексуальный контент**: Оценивает склонность модели создавать неподобающий сексуальный контент.

Оценка этих аспектов помогает убедиться, что модель не генерирует вредоносный или оскорбительный контент, что соответствует общественным ценностям и нормативным требованиям.

![Оценка на основе безопасности.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.ru.png)

### Введение в оценку производительности

Чтобы убедиться, что ваша модель ИИ работает как ожидается, важно оценить её производительность с помощью соответствующих метрик. В Azure AI Foundry оценки производительности позволяют проверить эффективность модели в генерации точных, релевантных и связных ответов.

![Оценка безопасности.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.ru.png)

*Источник изображения: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрики производительности

В этом руководстве вы оцените производительность дообученной модели Phi-3 / Phi-3.5 с помощью метрик производительности Azure AI Foundry. Эти метрики помогают определить эффективность модели в генерации точных, релевантных и связных ответов. Метрики производительности включают:

- **Обоснованность (Groundedness)**: Оценивает, насколько сгенерированные ответы соответствуют информации из исходного источника.
- **Релевантность**: Оценивает уместность сгенерированных ответов по отношению к заданным вопросам.
- **Связность (Coherence)**: Оценивает плавность текста, его естественность и сходство с человеческой речью.
- **Беглость (Fluency)**: Оценивает языковую грамотность сгенерированного текста.
- **Сходство с GPT (GPT Similarity)**: Сравнивает сгенерированный ответ с эталонным для определения степени сходства.
- **F1 Score**: Вычисляет долю общих слов между сгенерированным ответом и исходными данными.

Эти метрики помогают оценить эффективность модели в генерации точных, релевантных и связных ответов.

![Оценка на основе производительности.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.ru.png)

## **Сценарий 2: Оценка модели Phi-3 / Phi-3.5 в Azure AI Foundry**

### Перед началом

Это руководство является продолжением предыдущих публикаций в блоге: "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." В этих публикациях мы подробно рассмотрели процесс дообучения модели Phi-3 / Phi-3.5 в Azure AI Foundry и её интеграцию с Prompt flow.

В этом руководстве вы развернёте модель Azure OpenAI в качестве оценщика в Azure AI Foundry и используете её для оценки вашей дообученной модели Phi-3 / Phi-3.5.

Перед началом убедитесь, что у вас есть следующие требования, описанные в предыдущих руководствах:

1. Подготовленный набор данных для оценки дообученной модели Phi-3 / Phi-3.5.
1. Модель Phi-3 / Phi-3.5, которая была дообучена и развернута в Azure Machine Learning.
1. Prompt flow, интегрированный с вашей дообученной моделью Phi-3 / Phi-3.5 в Azure AI Foundry.

> [!NOTE]
> В качестве набора данных для оценки дообученной модели Phi-3 / Phi-3.5 вы будете использовать файл *test_data.jsonl*, расположенный в папке data из набора данных **ULTRACHAT_200k**, загруженного в предыдущих публикациях.

#### Интеграция кастомной модели Phi-3 / Phi-3.5 с Prompt flow в Azure AI Foundry (подход с кодом)
> [!NOTE]  
> Если вы использовали подход с низким кодом, описанный в "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", вы можете пропустить это упражнение и перейти к следующему.  
> Однако, если вы следовали подходу с приоритетом кода, описанному в "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" для дообучения и развертывания вашей модели Phi-3 / Phi-3.5, процесс подключения модели к Prompt flow будет немного отличаться. Вы изучите этот процесс в этом упражнении.
Чтобы продолжить, необходимо интегрировать вашу дообученную модель Phi-3 / Phi-3.5 в Prompt flow в Azure AI Foundry.

#### Создание Azure AI Foundry Hub

Перед созданием проекта нужно создать Hub. Hub действует как группа ресурсов, позволяя организовывать и управлять несколькими проектами в Azure AI Foundry.

1. Войдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Выберите **All hubs** в левой панели.

1. Выберите **+ New hub** в навигационном меню.

    ![Создание хаба.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.ru.png)

1. Выполните следующие действия:

    - Введите **Hub name**. Имя должно быть уникальным.
    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Resource group** для использования (создайте новую, если нужно).
    - Выберите **Location**, которую хотите использовать.
    - Выберите **Connect Azure AI Services** для подключения (создайте новую, если нужно).
    - Выберите **Connect Azure AI Search** и установите **Skip connecting**.

    ![Заполнение хаба.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.ru.png)

1. Нажмите **Next**.

#### Создание проекта Azure AI Foundry

1. В созданном Hub выберите **All projects** в левой панели.

1. Выберите **+ New project** в навигационном меню.

    ![Выбор нового проекта.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.ru.png)

1. Введите **Project name**. Имя должно быть уникальным.

    ![Создание проекта.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.ru.png)

1. Нажмите **Create a project**.

#### Добавление пользовательского подключения для дообученной модели Phi-3 / Phi-3.5

Чтобы интегрировать вашу кастомную модель Phi-3 / Phi-3.5 с Prompt flow, необходимо сохранить endpoint и ключ модели в пользовательском подключении. Это обеспечит доступ к вашей модели в Prompt flow.

#### Установка api key и endpoint uri для дообученной модели Phi-3 / Phi-3.5

1. Перейдите в [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Откройте рабочее пространство Azure Machine Learning, которое вы создали.

1. Выберите **Endpoints** в левой панели.

    ![Выбор endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.ru.png)

1. Выберите созданный вами endpoint.

    ![Выбор созданного endpoint.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.ru.png)

1. Выберите **Consume** в навигационном меню.

1. Скопируйте ваш **REST endpoint** и **Primary key**.

    ![Копирование api key и endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.ru.png)

#### Добавление пользовательского подключения

1. Перейдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Откройте созданный вами проект Azure AI Foundry.

1. В проекте выберите **Settings** в левой панели.

1. Нажмите **+ New connection**.

    ![Выбор нового подключения.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.ru.png)

1. Выберите **Custom keys** в навигационном меню.

    ![Выбор custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.ru.png)

1. Выполните следующие действия:

    - Нажмите **+ Add key value pairs**.
    - Введите имя ключа **endpoint** и вставьте скопированный endpoint из Azure ML Studio в поле значения.
    - Снова нажмите **+ Add key value pairs**.
    - Введите имя ключа **key** и вставьте скопированный ключ из Azure ML Studio в поле значения.
    - После добавления ключей отметьте **is secret**, чтобы ключи не были видны.

    ![Добавление подключения.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.ru.png)

1. Нажмите **Add connection**.

#### Создание Prompt flow

Вы добавили пользовательское подключение в Azure AI Foundry. Теперь создадим Prompt flow, используя следующие шаги. Затем вы подключите этот Prompt flow к пользовательскому подключению, чтобы использовать дообученную модель внутри Prompt flow.

1. Откройте созданный вами проект Azure AI Foundry.

1. Выберите **Prompt flow** в левой панели.

1. Нажмите **+ Create** в навигационном меню.

    ![Выбор Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.ru.png)

1. Выберите **Chat flow** в навигационном меню.

    ![Выбор chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.ru.png)

1. Введите имя папки (**Folder name**), которую хотите использовать.

    ![Ввод имени папки.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.ru.png)

1. Нажмите **Create**.

#### Настройка Prompt flow для общения с вашей кастомной моделью Phi-3 / Phi-3.5

Необходимо интегрировать дообученную модель Phi-3 / Phi-3.5 в Prompt flow. Однако существующий Prompt flow не предназначен для этого, поэтому его нужно переделать для поддержки кастомной модели.

1. В Prompt flow выполните следующие действия для перестройки существующего потока:

    - Выберите **Raw file mode**.
    - Удалите весь существующий код в файле *flow.dag.yml*.
    - Добавьте следующий код в *flow.dag.yml*.

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

    ![Выбор raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.ru.png)

1. Добавьте следующий код в *integrate_with_promptflow.py* для использования кастомной модели Phi-3 / Phi-3.5 в Prompt flow.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Вставка кода prompt flow.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.ru.png)

> [!NOTE]
> Для более подробной информации по использованию Prompt flow в Azure AI Foundry обратитесь к [Prompt flow в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Выберите **Chat input** и **Chat output**, чтобы включить чат с вашей моделью.

    ![Выбор Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.ru.png)

1. Теперь вы готовы общаться с вашей кастомной моделью Phi-3 / Phi-3.5. В следующем упражнении вы узнаете, как запустить Prompt flow и использовать его для общения с вашей дообученной моделью.

> [!NOTE]
>
> Переделанный поток должен выглядеть примерно так:
>
> ![Пример потока](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.ru.png)
>

#### Запуск Prompt flow

1. Нажмите **Start compute sessions** для запуска Prompt flow.

    ![Запуск compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.ru.png)

1. Нажмите **Validate and parse input** для обновления параметров.

    ![Валидация ввода.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.ru.png)

1. Выберите значение **connection** для пользовательского подключения, которое вы создали. Например, *connection*.

    ![Выбор подключения.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.ru.png)

#### Общение с вашей кастомной моделью Phi-3 / Phi-3.5

1. Нажмите **Chat**.

    ![Выбор чата.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.ru.png)

1. Пример результата: теперь вы можете общаться с вашей кастомной моделью Phi-3 / Phi-3.5. Рекомендуется задавать вопросы, основанные на данных, использованных для дообучения.

    ![Чат с prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.ru.png)

### Развертывание Azure OpenAI для оценки модели Phi-3 / Phi-3.5

Для оценки модели Phi-3 / Phi-3.5 в Azure AI Foundry необходимо развернуть модель Azure OpenAI. Эта модель будет использоваться для оценки производительности Phi-3 / Phi-3.5.

#### Развертывание Azure OpenAI

1. Войдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Откройте созданный вами проект Azure AI Foundry.

    ![Выбор проекта.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.ru.png)

1. В проекте выберите **Deployments** в левой панели.

1. Нажмите **+ Deploy model** в навигационном меню.

1. Выберите **Deploy base model**.

    ![Выбор Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.ru.png)

1. Выберите модель Azure OpenAI, которую хотите использовать. Например, **gpt-4o**.

    ![Выбор модели Azure OpenAI.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.ru.png)

1. Нажмите **Confirm**.

### Оценка дообученной модели Phi-3 / Phi-3.5 с помощью Prompt flow в Azure AI Foundry

### Начало нового оценивания

1. Перейдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Откройте созданный вами проект Azure AI Foundry.

    ![Выбор проекта.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.ru.png)

1. В проекте выберите **Evaluation** в левой панели.

1. Нажмите **+ New evaluation** в навигационном меню.

    ![Выбор оценки.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.ru.png)

1. Выберите оценку **Prompt flow**.

    ![Выбор оценки Prompt flow.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.ru.png)

1. Выполните следующие действия:

    - Введите имя оценки. Оно должно быть уникальным.
    - Выберите тип задачи **Question and answer without context**, так как датасет **ULTRACHAT_200k**, используемый в этом руководстве, не содержит контекста.
    - Выберите Prompt flow, который хотите оценить.

    ![Настройка оценки Prompt flow.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.ru.png)

1. Нажмите **Next**.

1. Выполните следующие действия:

    - Нажмите **Add your dataset** для загрузки датасета. Например, можно загрузить тестовый файл *test_data.json1*, который входит в состав датасета **ULTRACHAT_200k**.
    - Выберите соответствующий **Dataset column**, который соответствует вашему датасету. Например, для **ULTRACHAT_200k** выберите **${data.prompt}**.

    ![Настройка оценки Prompt flow.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.ru.png)

1. Нажмите **Next**.

1. Выполните следующие действия для настройки метрик производительности и качества:

    - Выберите метрики производительности и качества, которые хотите использовать.
    - Выберите модель Azure OpenAI, созданную для оценки. Например, **gpt-4o**.

    ![Настройка оценки Prompt flow.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.ru.png)

1. Выполните следующие действия для настройки метрик риска и безопасности:

    - Выберите метрики риска и безопасности, которые хотите использовать.
    - Выберите порог для расчёта уровня дефектов. Например, **Medium**.
    - Для **question** выберите источник данных **{$data.prompt}**.
    - Для **answer** выберите источник данных **{$run.outputs.answer}**.
    - Для **ground_truth** выберите источник данных **{$data.message}**.

    ![Настройка оценки Prompt flow.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.ru.png)

1. Нажмите **Next**.

1. Нажмите **Submit** для запуска оценки.

1. Оценка займет некоторое время. Вы можете отслеживать прогресс во вкладке **Evaluation**.

### Просмотр результатов оценки
> [!NOTE]
> Представленные ниже результаты служат для иллюстрации процесса оценки. В этом руководстве мы использовали модель, дообученную на относительно небольшом наборе данных, что может привести к не самым оптимальным результатам. Фактические результаты могут значительно отличаться в зависимости от размера, качества и разнообразия используемого набора данных, а также от конкретной конфигурации модели.
После завершения оценки вы можете просмотреть результаты как по показателям производительности, так и по показателям безопасности.

1. Метрики производительности и качества:

    - оцените эффективность модели в генерации связных, плавных и релевантных ответов.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.ru.png)

1. Метрики риска и безопасности:

    - убедитесь, что выводы модели безопасны и соответствуют принципам Ответственного ИИ, избегая любого вредоносного или оскорбительного контента.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.ru.png)

1. Вы можете прокрутить страницу вниз, чтобы увидеть **Подробные результаты метрик**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.ru.png)

1. Оценивая вашу кастомную модель Phi-3 / Phi-3.5 по показателям производительности и безопасности, вы подтверждаете, что модель не только эффективна, но и соответствует принципам ответственного ИИ, что делает её готовой к реальному применению.

## Поздравляем!

### Вы завершили этот учебный курс

Вы успешно оценили дообученную модель Phi-3, интегрированную с Prompt flow в Azure AI Foundry. Это важный шаг для того, чтобы ваши ИИ-модели не только хорошо работали, но и соответствовали принципам Ответственного ИИ Microsoft, помогая создавать надёжные и заслуживающие доверия ИИ-приложения.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.ru.png)

## Очистка ресурсов Azure

Очистите ресурсы Azure, чтобы избежать дополнительных расходов на вашем аккаунте. Перейдите в портал Azure и удалите следующие ресурсы:

- Ресурс Azure Machine learning.
- Конечную точку модели Azure Machine learning.
- Ресурс проекта Azure AI Foundry.
- Ресурс Prompt flow в Azure AI Foundry.

### Следующие шаги

#### Документация

- [Оценка ИИ-систем с помощью панели Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Метрики оценки и мониторинга для генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Документация Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Документация Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Учебные материалы

- [Введение в подход Microsoft к Ответственному ИИ](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Введение в Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Ссылки

- [Что такое Ответственный ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Анонс новых инструментов в Azure AI для создания более безопасных и надёжных генеративных ИИ-приложений](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Оценка генеративных ИИ-приложений](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.