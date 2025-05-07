<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-07T14:22:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "ru"
}
-->
# Оценка дообученной модели Phi-3 / Phi-3.5 в Azure AI Foundry с акцентом на принципы ответственного ИИ Microsoft

Этот пошаговый пример основан на руководстве "[Оценка дообученных моделей Phi-3 / 3.5 в Azure AI Foundry с акцентом на ответственный ИИ Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" из сообщества Microsoft Tech Community.

## Обзор

### Как оценить безопасность и производительность дообученной модели Phi-3 / Phi-3.5 в Azure AI Foundry?

Дообучение модели иногда может привести к непреднамеренным или нежелательным ответам. Чтобы убедиться, что модель остается безопасной и эффективной, важно оценить её способность генерировать вредоносный контент, а также создавать точные, релевантные и связные ответы. В этом руководстве вы научитесь оценивать безопасность и производительность дообученной модели Phi-3 / Phi-3.5, интегрированной с Prompt flow в Azure AI Foundry.

Ниже представлен процесс оценки в Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.ru.png)

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

Для того чтобы ваш ИИ-модель была этичной и безопасной, важно оценивать её в соответствии с принципами ответственного ИИ Microsoft. В Azure AI Foundry оценка безопасности позволяет проверить уязвимость модели к атакам jailbreak и её потенциал для генерации вредоносного контента, что напрямую соответствует этим принципам.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.ru.png)

*Источник изображения: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Принципы ответственного ИИ Microsoft

Перед началом технических шагов важно понять Принципы ответственного ИИ Microsoft — этическую основу, которая направляет разработку, внедрение и эксплуатацию ИИ-систем. Эти принципы обеспечивают справедливость, прозрачность и инклюзивность при создании ИИ-технологий. Они служат фундаментом для оценки безопасности ИИ-моделей.

Принципы ответственного ИИ Microsoft включают:

- **Справедливость и инклюзивность**: ИИ-системы должны одинаково справедливо относиться ко всем и не допускать различий в отношении к схожим группам людей. Например, при рекомендациях по медицинскому лечению, кредитным заявкам или трудоустройству ИИ должен давать одинаковые советы всем с похожими симптомами, финансовым положением или квалификацией.

- **Надежность и безопасность**: Для завоевания доверия ИИ-системы должны работать надежно, безопасно и последовательно. Они должны функционировать согласно своему первоначальному замыслу, безопасно реагировать на неожиданные ситуации и противостоять вредоносным воздействиям. Их поведение и спектр обрабатываемых условий отражают ситуации, предусмотренные разработчиками на этапе проектирования и тестирования.

- **Прозрачность**: Когда ИИ помогает принимать решения, существенно влияющие на жизнь людей, важно, чтобы люди понимали, как эти решения были приняты. Например, банк может использовать ИИ для оценки кредитоспособности, а компания — для выбора наиболее подходящих кандидатов на работу.

- **Конфиденциальность и безопасность**: С ростом распространенности ИИ защита конфиденциальности и безопасность личной и корпоративной информации становятся всё более важными и сложными. Для ИИ критично внимательно относиться к этим вопросам, поскольку доступ к данным необходим для точных и обоснованных предсказаний и решений.

- **Ответственность**: Люди, разрабатывающие и внедряющие ИИ-системы, должны нести ответственность за их работу. Организации должны использовать отраслевые стандарты для разработки норм ответственности. Эти нормы гарантируют, что ИИ-системы не будут единственным авторитетом в решениях, влияющих на жизнь людей, и что человек сохраняет значимый контроль над высокоавтономными ИИ.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.ru.png)

*Источник изображения: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Чтобы узнать больше о принципах ответственного ИИ Microsoft, посетите страницу [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрики безопасности

В этом руководстве вы оцените безопасность дообученной модели Phi-3 с помощью метрик безопасности Azure AI Foundry. Эти метрики помогают определить потенциал модели к генерации вредоносного контента и её уязвимость к атакам jailbreak. Метрики безопасности включают:

- **Контент, связанный с самоповреждением**: Оценивает склонность модели к созданию контента, связанного с самоповреждением.
- **Ненавистнический и несправедливый контент**: Оценивает склонность модели к генерации ненавистнического или несправедливого контента.
- **Насильственный контент**: Оценивает склонность модели к созданию насильственного контента.
- **Сексуальный контент**: Оценивает склонность модели к созданию неподобающего сексуального контента.

Оценка этих аспектов помогает убедиться, что ИИ-модель не генерирует вредоносный или оскорбительный контент, что соответствует общественным ценностям и нормативным требованиям.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.ru.png)

### Введение в оценку производительности

Чтобы убедиться, что ваша ИИ-модель работает как задумано, важно оценить её производительность с помощью соответствующих метрик. В Azure AI Foundry оценка производительности позволяет проверить эффективность модели в генерации точных, релевантных и связных ответов.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.ru.png)

*Источник изображения: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрики производительности

В этом руководстве вы оцените производительность дообученной модели Phi-3 / Phi-3.5 с помощью метрик производительности Azure AI Foundry. Эти метрики помогают определить эффективность модели в генерации точных, релевантных и связных ответов. Метрики производительности включают:

- **Основанность (Groundedness)**: Оценивает, насколько сгенерированные ответы соответствуют информации из исходного источника.
- **Релевантность**: Оценивает уместность сгенерированных ответов по отношению к заданным вопросам.
- **Связность (Coherence)**: Оценивает плавность и естественность текста, а также его сходство с человеческой речью.
- **Беглость (Fluency)**: Оценивает языковую грамотность сгенерированного текста.
- **Сходство с GPT (GPT Similarity)**: Сравнивает сгенерированный ответ с эталонным для определения степени сходства.
- **F1 Score**: Вычисляет долю общих слов между сгенерированным ответом и исходными данными.

Эти метрики помогают оценить эффективность модели в создании точных, релевантных и связных ответов.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.ru.png)

## **Сценарий 2: Оценка модели Phi-3 / Phi-3.5 в Azure AI Foundry**

### Перед началом

Это руководство является продолжением предыдущих публикаций в блоге: "[Дообучение и интеграция кастомных моделей Phi-3 с Prompt Flow: пошаговое руководство](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Дообучение и интеграция кастомных моделей Phi-3 с Prompt Flow в Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)". В этих статьях мы рассмотрели процесс дообучения модели Phi-3 / Phi-3.5 в Azure AI Foundry и её интеграцию с Prompt flow.

В этом руководстве вы развернете модель Azure OpenAI в качестве оценщика в Azure AI Foundry и используете её для оценки вашей дообученной модели Phi-3 / Phi-3.5.

Перед началом убедитесь, что у вас есть следующие необходимые компоненты, описанные в предыдущих руководствах:

1. Подготовленный набор данных для оценки дообученной модели Phi-3 / Phi-3.5.
1. Модель Phi-3 / Phi-3.5, дообученная и развернутая в Azure Machine Learning.
1. Prompt flow, интегрированный с вашей дообученной моделью Phi-3 / Phi-3.5 в Azure AI Foundry.

> [!NOTE]
> В качестве набора данных для оценки дообученной модели Phi-3 / Phi-3.5 вы будете использовать файл *test_data.jsonl*, который находится в папке data из набора данных **ULTRACHAT_200k**, загруженного в предыдущих публикациях.

#### Интеграция кастомной модели Phi-3 / Phi-3.5 с Prompt flow в Azure AI Foundry (подход с кодом в первую очередь)

> [!NOTE]
> Если вы использовали подход low-code, описанный в "[Дообучение и интеграция кастомных моделей Phi-3 с Prompt Flow в Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", вы можете пропустить это упражнение и перейти к следующему.
> Однако если вы использовали подход с кодом в первую очередь, описанный в "[Дообучение и интеграция кастомных моделей Phi-3 с Prompt Flow: пошаговое руководство](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", процесс подключения модели к Prompt flow будет немного другим. Вы узнаете этот процесс в этом упражнении.

Для продолжения вам нужно интегрировать вашу дообученную модель Phi-3 / Phi-3.5 в Prompt flow в Azure AI Foundry.

#### Создание Azure AI Foundry Hub

Перед созданием проекта необходимо создать Hub. Hub действует как группа ресурсов, позволяя организовывать и управлять несколькими проектами в Azure AI Foundry.

1. Войдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Выберите **All hubs** в левой панели.

1. Нажмите **+ New hub** в навигационном меню.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.ru.png)

1. Выполните следующие действия:

    - Введите **Hub name**. Имя должно быть уникальным.
    - Выберите вашу подписку Azure (**Subscription**).
    - Выберите **Resource group** (создайте новую при необходимости).
    - Выберите желаемое **Location**.
    - Выберите **Connect Azure AI Services** (создайте новую при необходимости).
    - Для **Connect Azure AI Search** выберите **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.ru.png)

1. Выберите **Next**.

#### Создание проекта Azure AI Foundry

1. В созданном вами Hub выберите **All projects** в левой вкладке.

1. Выберите **+ New project** в навигационном меню.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.ru.png)

1. Введите **Project name**. Имя должно быть уникальным.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.ru.png)

1. Нажмите **Create a project**.

#### Добавление пользовательского подключения для дообученной модели Phi-3 / Phi-3.5

Для интеграции вашей дообученной модели Phi-3 / Phi-3.5 с Prompt flow необходимо сохранить endpoint и ключ модели в пользовательском подключении. Это обеспечит доступ к вашей модели Phi-3 / Phi-3.5 в Prompt flow.

#### Установка api key и endpoint uri для дообученной модели Phi-3 / Phi-3.5

1. Перейдите в [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Откройте созданное вами рабочее пространство Azure Machine learning.

1. Выберите **Endpoints** в левой вкладке.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.ru.png)

1. Выберите созданный вами endpoint.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.ru.png)

1. Выберите **Consume** в навигационном меню.

1. Скопируйте ваш **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.ru.png)

#### Добавление пользовательского подключения

1. Перейдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Откройте созданный вами проект Azure AI Foundry.

1. В проекте выберите **Settings** в левой вкладке.

1. Нажмите **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.ru.png)

1. Выберите **Custom keys** в навигационном меню.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.ru.png)

1. Выполните следующие действия:

    - Нажмите **+ Add key value pairs**.
    - Введите для имени ключа **endpoint** и вставьте скопированный из Azure ML Studio endpoint в поле значения.
    - Снова нажмите **+ Add key value pairs**.
    - Введите для имени ключа **key** и вставьте скопированный из Azure ML Studio ключ в поле значения.
    - После добавления ключей отметьте **is secret**, чтобы ключи не были видны.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.ru.png)

1. Нажмите **Add connection**.

#### Создание Prompt flow

Вы добавили пользовательское подключение в Azure AI Foundry. Теперь создадим Prompt flow по следующим шагам. Затем подключим этот Prompt flow к пользовательскому подключению, чтобы использовать дообученную модель внутри Prompt flow.

1. Откройте созданный вами проект Azure AI Foundry.

1. Выберите **Prompt flow** в левой вкладке.

1. Нажмите **+ Create** в навигационном меню.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.ru.png)

1. Выберите **Chat flow** в навигационном меню.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.ru.png)

1. Введите **Folder name** для использования.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.ru.png)

1. Нажмите **Create**.

#### Настройка Prompt flow для общения с вашей дообученной моделью Phi-3 / Phi-3.5

Необходимо интегрировать дообученную модель Phi-3 / Phi-3.5 в Prompt flow. Однако, существующий Prompt flow не предназначен для этого, поэтому его нужно перепроектировать для поддержки пользовательской модели.

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.ru.png)

1. Добавьте следующий код в *integrate_with_promptflow.py* для использования пользовательской модели Phi-3 / Phi-3.5 в Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.ru.png)

> [!NOTE]
> Более подробную информацию о работе с Prompt flow в Azure AI Foundry можно найти в [Prompt flow в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Выберите **Chat input**, **Chat output** для включения общения с вашей моделью.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.ru.png)

1. Теперь вы готовы общаться с вашей дообученной моделью Phi-3 / Phi-3.5. В следующем упражнении вы узнаете, как запустить Prompt flow и использовать его для общения с моделью.

> [!NOTE]
>
> Перестроенный поток должен выглядеть так, как на изображении ниже:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.ru.png)
>

#### Запуск Prompt flow

1. Нажмите **Start compute sessions** для запуска Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.ru.png)

1. Нажмите **Validate and parse input** для обновления параметров.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.ru.png)

1. Выберите значение **Value** для **connection**, соответствующее созданному вами пользовательскому подключению, например *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.ru.png)

#### Общение с вашей дообученной моделью Phi-3 / Phi-3.5

1. Нажмите **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.ru.png)

1. Пример результата: теперь вы можете общаться с вашей дообученной моделью Phi-3 / Phi-3.5. Рекомендуется задавать вопросы на основе данных, использованных для дообучения.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.ru.png)

### Развертывание Azure OpenAI для оценки модели Phi-3 / Phi-3.5

Для оценки модели Phi-3 / Phi-3.5 в Azure AI Foundry необходимо развернуть модель Azure OpenAI. Эта модель будет использоваться для оценки производительности модели Phi-3 / Phi-3.5.

#### Развертывание Azure OpenAI

1. Войдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Откройте созданный вами проект Azure AI Foundry.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.ru.png)

1. В проекте выберите **Deployments** в левой вкладке.

1. Нажмите **+ Deploy model** в навигационном меню.

1. Выберите **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.ru.png)

1. Выберите модель Azure OpenAI, которую хотите использовать, например, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.ru.png)

1. Нажмите **Confirm**.

### Оценка дообученной модели Phi-3 / Phi-3.5 с помощью Prompt flow в Azure AI Foundry

### Начало нового оценивания

1. Перейдите в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Откройте созданный вами проект Azure AI Foundry.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.ru.png)

1. В проекте выберите **Evaluation** в левой вкладке.

1. Нажмите **+ New evaluation** в навигационном меню.
![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.ru.png)

1. Выберите оценку **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.ru.png)

1. Выполните следующие действия:

    - Введите имя оценки. Оно должно быть уникальным.
    - Выберите тип задачи **Question and answer without context**, так как в используемом в этом руководстве наборе данных **UlTRACHAT_200k** отсутствует контекст.
    - Выберите prompt flow, который хотите оценить.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.ru.png)

1. Нажмите **Next**.

1. Выполните следующие действия:

    - Выберите **Add your dataset** для загрузки набора данных. Например, вы можете загрузить тестовый файл набора данных, такой как *test_data.json1*, который входит в состав набора **ULTRACHAT_200k**.
    - Выберите соответствующий **Dataset column**, который соответствует вашему набору данных. Например, если вы используете набор **ULTRACHAT_200k**, выберите **${data.prompt}** в качестве столбца набора данных.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.ru.png)

1. Нажмите **Next**.

1. Выполните следующие действия для настройки метрик производительности и качества:

    - Выберите метрики производительности и качества, которые хотите использовать.
    - Выберите модель Azure OpenAI, созданную для оценки. Например, выберите **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.ru.png)

1. Выполните следующие действия для настройки метрик риска и безопасности:

    - Выберите метрики риска и безопасности, которые хотите использовать.
    - Выберите порог для расчёта уровня дефектов. Например, выберите **Medium**.
    - Для **question** выберите источник данных **{$data.prompt}**.
    - Для **answer** выберите источник данных **{$run.outputs.answer}**.
    - Для **ground_truth** выберите источник данных **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.ru.png)

1. Нажмите **Next**.

1. Нажмите **Submit**, чтобы начать оценку.

1. Оценка займёт некоторое время. Вы можете отслеживать прогресс во вкладке **Evaluation**.

### Просмотр результатов оценки

> [!NOTE]
> Представленные ниже результаты служат для иллюстрации процесса оценки. В этом руководстве использовалась модель, дообученная на относительно небольшом наборе данных, что может привести к не оптимальным результатам. Фактические результаты могут значительно отличаться в зависимости от размера, качества и разнообразия используемого набора данных, а также от конкретной настройки модели.

После завершения оценки вы сможете просмотреть результаты по метрикам производительности и безопасности.

1. Метрики производительности и качества:

    - оцените эффективность модели в генерации связных, плавных и релевантных ответов.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.ru.png)

1. Метрики риска и безопасности:

    - убедитесь, что результаты модели безопасны и соответствуют принципам Responsible AI, избегая вредоносного или оскорбительного контента.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.ru.png)

1. Прокрутите вниз, чтобы просмотреть **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.ru.png)

1. Оценивая вашу кастомную модель Phi-3 / Phi-3.5 по метрикам производительности и безопасности, вы можете убедиться, что модель не только эффективна, но и соответствует принципам ответственного ИИ, что делает её готовой к реальному использованию.

## Поздравляем!

### Вы завершили это руководство

Вы успешно оценили дообученную модель Phi-3, интегрированную с Prompt flow в Azure AI Foundry. Это важный шаг для того, чтобы ваши модели ИИ не только хорошо работали, но и соответствовали принципам Responsible AI от Microsoft, помогая создавать надёжные и заслуживающие доверия приложения ИИ.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.ru.png)

## Очистка ресурсов Azure

Очистите ресурсы Azure, чтобы избежать дополнительных затрат. Перейдите в портал Azure и удалите следующие ресурсы:

- Ресурс Azure Machine learning.
- Endpoint модели Azure Machine learning.
- Ресурс проекта Azure AI Foundry.
- Ресурс Prompt flow Azure AI Foundry.

### Следующие шаги

#### Документация

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Учебные материалы

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Ссылки

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.