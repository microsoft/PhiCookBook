# Оценка тонко настроенной модели Phi-3 / Phi-3.5 в Microsoft Foundry с акцентом на принципы ответственного ИИ Microsoft

Этот полный пример (E2E) основан на руководстве "[Оценка тонко настроированных моделей Phi-3 / 3.5 в Microsoft Foundry с акцентом на ответственный ИИ Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" из сообщества Microsoft Tech Community.

## Обзор

### Как оценить безопасность и производительность тонко настроенной модели Phi-3 / Phi-3.5 в Microsoft Foundry?

Тонкая настройка модели иногда может привести к непреднамеренным или нежелательным ответам. Чтобы обеспечить безопасность и эффективность модели, важно оценить её потенциал генерировать вредоносный контент и способность выдавать точные, релевантные и связные ответы. В этом учебном пособии вы научитесь оценивать безопасность и производительность тонко настроенной модели Phi-3 / Phi-3.5, интегрированной с Prompt flow в Microsoft Foundry.

Вот процесс оценки в Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/ru/architecture.10bec55250f5d6a4.webp)

*Источник изображения: [Оценка приложений генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Для получения более подробной информации и изучения дополнительных ресурсов о Phi-3 / Phi-3.5, пожалуйста, посетите [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Требования

- [Python](https://www.python.org/downloads)
- [Подписка Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Тонко настроенная модель Phi-3 / Phi-3.5

### Содержание

1. [**Сценарий 1: Введение в оценку Prompt flow в Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Введение в оценку безопасности](#введение-в-оценку-безопасности)
    - [Введение в оценку производительности](#введение-в-оценку-производительности)

1. [**Сценарий 2: Оценка модели Phi-3 / Phi-3.5 в Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Перед началом](#перед-началом)
    - [Развертывание Azure OpenAI для оценки модели Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Оценка тонко настроенной модели Phi-3 / Phi-3.5 с использованием оценки Prompt flow Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Поздравляем!](#поздравляем)

## **Сценарий 1: Введение в оценку Prompt flow в Microsoft Foundry**

### Введение в оценку безопасности

Чтобы обеспечить этичность и безопасность вашей модели ИИ, важно оценить её в соответствии с принципами ответственного ИИ Microsoft. В Microsoft Foundry оценки безопасности позволяют оценить уязвимость вашей модели к атакам jailbreak и её потенциал к генерации вредоносного контента, что напрямую соответствует этим принципам.

![Safaty evaluation.](../../../../../../translated_images/ru/safety-evaluation.083586ec88dfa950.webp)

*Источник изображения: [Оценка приложений генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Принципы ответственного ИИ Microsoft

Прежде чем начинать технические шаги, важно понять принципы ответственного ИИ Microsoft — этическую основу, призванную направлять ответственную разработку, внедрение и эксплуатацию систем ИИ. Эти принципы направляют ответственное проектирование, разработку и развертывание систем ИИ, обеспечивая создание технологий ИИ справедливо, прозрачно и инклюзивно. Эти принципы являются основой для оценки безопасности моделей ИИ.

Принципы ответственного ИИ Microsoft включают:

- **Справедливость и инклюзивность**: Системы ИИ должны справедливо относиться ко всем и избегать неодинакового влияния на схожие группы людей. Например, когда системы ИИ дают рекомендации по лечению, подаче заявок на кредиты или найму на работу, они должны давать одинаковые рекомендации всем, у кого похожие симптомы, финансовое положение или профессиональные квалификации.

- **Надёжность и безопасность**: Для построения доверия критично, чтобы системы ИИ работали надёжно, безопасно и последовательно. Эти системы должны функционировать так, как было задумано, безопасно реагировать на непредвиденные ситуации и сопротивляться вредоносным попыткам манипуляции. Их поведение и спектр условий, с которыми они справляются, отражают разнообразие ситуаций, предусмотренных разработчиками при проектировании и тестировании.

- **Прозрачность**: Когда системы ИИ помогают принимать решения, которые существенно влияют на жизни людей, важно, чтобы люди понимали, как эти решения были приняты. Например, банк может использовать ИИ для оценки кредитоспособности клиента. Компания может использовать ИИ для выбора наиболее квалифицированных кандидатов.

- **Конфиденциальность и безопасность**: С распространением ИИ защита приватности и безопасность личной и бизнес-информации становятся всё важнее и сложнее. При использовании ИИ конфиденциальность и безопасность данных требуют особого внимания, поскольку доступ к данным необходим для точных и информированных прогнозов и решений о людях.

- **Ответственность**: Люди, разрабатывающие и внедряющие системы ИИ, должны нести ответственность за их работу. Организации должны опираться на отраслевые стандарты для разработки норм ответственности. Эти нормы могут гарантировать, что системы ИИ не являются окончательным органом, принимающим решения, влияющие на жизни людей, а также что люди сохраняют значимый контроль над преимущественно автономными системами ИИ.

![Fill hub.](../../../../../../translated_images/ru/responsibleai2.c07ef430113fad8c.webp)

*Источник изображения: [Что такое ответственный ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Чтобы узнать больше о принципах ответственного ИИ Microsoft, посетите [Что такое ответственный ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрики безопасности

В этом учебном пособии вы оцените безопасность тонко настроенной модели Phi-3 с помощью метрик безопасности Microsoft Foundry. Эти метрики помогают оценить потенциал модели к генерации вредоносного контента и её уязвимость к атакам jailbreak. Метрики безопасности включают:

- **Контент, связанный с самоповреждением**: Оценивает, склонна ли модель генерировать контент, связанный с самоповреждением.
- **Ненавистнический и несправедливый контент**: Оценивает склонность модели к генерации ненавистнического или несправедливого контента.
- **Насильственный контент**: Оценивает склонность модели к генерации насильственного контента.
- **Сексуальный контент**: Оценивает склонность модели к генерации неподобающего сексуального контента.

Оценка этих аспектов помогает гарантировать, что модель ИИ не генерирует вредоносный или оскорбительный контент, согласуясь с общественными ценностями и нормативными требованиями.

![Evaluate based on safety.](../../../../../../translated_images/ru/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Введение в оценку производительности

Чтобы удостовериться, что ваша модель ИИ работает должным образом, важно оценить её производительность с помощью метрик. В Microsoft Foundry оценки производительности позволяют оценить эффективность модели в генерации точных, релевантных и связных ответов.

![Safaty evaluation.](../../../../../../translated_images/ru/performance-evaluation.48b3e7e01a098740.webp)

*Источник изображения: [Оценка приложений генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрики производительности

В этом руководстве вы оцените производительность тонко настроенной модели Phi-3 / Phi-3.5 с помощью метрик производительности Microsoft Foundry. Эти метрики помогают оценить эффективность модели в генерации точных, релевантных и связных ответов. Метрики производительности включают:

- **Основанность (Groundedness)**: Оценивает, насколько сгенерированные ответы соответствуют информации из исходного источника.
- **Релевантность**: Оценивает уместность сгенерированных ответов на заданные вопросы.
- **Связность**: Оценивает плавность текста, насколько он читается естественно и напоминает язык человека.
- **Плавность (Fluency)**: Оценивает языковое мастерство сгенерированного текста.
- **Сходство с GPT (GPT Similarity)**: Сравнивает сгенерированный ответ с эталоном для определения сходства.
- **F1 Score**: Рассчитывает отношение общих слов между сгенерированным ответом и исходными данными.

Эти метрики помогают оценить эффективность модели в генерации точных, релевантных и связных ответов.

![Evaluate based on performance.](../../../../../../translated_images/ru/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Сценарий 2: Оценка модели Phi-3 / Phi-3.5 в Microsoft Foundry**

### Перед началом

Это учебное пособие является продолжением предыдущих публикаций в блоге: "[Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow: пошаговое руководство](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow в Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." В этих публикациях мы рассматривали процесс тонкой настройки модели Phi-3 / Phi-3.5 в Microsoft Foundry и интеграцию её с Prompt flow.

В этом учебном пособии вы развернёте модель Azure OpenAI в качестве оценщика в Microsoft Foundry и используете её для оценки вашей тонко настроенной модели Phi-3 / Phi-3.5.

Перед началом выполнения учебного пособия убедитесь, что у вас есть следующие предпосылки, описанные в предыдущих руководствах:

1. Подготовленный набор данных для оценки тонко настроенной модели Phi-3 / Phi-3.5.
1. Модель Phi-3 / Phi-3.5, которая была тонко настроена и развернута в Azure Machine Learning.
1. Prompt flow, интегрированный с вашей тонко настроенной моделью Phi-3 / Phi-3.5 в Microsoft Foundry.

> [!NOTE]
> Вы будете использовать файл *test_data.jsonl*, расположенный в папке data из набора данных **ULTRACHAT_200k**, скачанного в предыдущих публикациях блога, как набор данных для оценки тонко настроенной модели Phi-3 / Phi-3.5.

#### Интеграция пользовательской модели Phi-3 / Phi-3.5 с Prompt flow в Microsoft Foundry (подход с кодом в первую очередь)

> [!NOTE]
> Если вы использовали low-code подход, описанный в "[Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow в Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", вы можете пропустить это упражнение и перейти к следующему.
> Однако, если вы следовали подходу с кодом в первую очередь, описанному в "[Тонкая настройка и интеграция пользовательских моделей Phi-3 с Prompt Flow: пошаговое руководство](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", для тонкой настройки и развертывания вашей модели Phi-3 / Phi-3.5, процесс подключения вашей модели к Prompt flow немного отличается. Вы познакомитесь с этим процессом в этом упражнении.

Чтобы продолжить, вам нужно интегрировать вашу тонко настроенную модель Phi-3 / Phi-3.5 в Prompt flow в Microsoft Foundry.

#### Создание Microsoft Foundry Hub

Перед созданием проекта необходимо создать Hub. Хаб действует как группа ресурсов, позволяя организовывать и управлять несколькими проектами внутри Microsoft Foundry.
1. Войдите в систему на [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Выберите **Все хабы** в левой панели.

1. Выберите **+ Новый хаб** в навигационном меню.

    ![Create hub.](../../../../../../translated_images/ru/create-hub.5be78fb1e21ffbf1.webp)

1. Выполните следующие действия:

    - Введите **Имя хаба**. Оно должно быть уникальным.
    - Выберите свою подписку Azure **Subscription**.
    - Выберите **Группу ресурсов** для использования (создайте новую при необходимости).
    - Выберите желаемое **Расположение**.
    - Выберите **Подключить Azure AI Services** для использования (создайте новое при необходимости).
    - Выберите **Подключить Azure AI Search** и установите **Пропустить подключение**.

    ![Fill hub.](../../../../../../translated_images/ru/fill-hub.baaa108495c71e34.webp)

1. Выберите **Далее**.

#### Создание проекта Microsoft Foundry

1. В созданном хабе выберите **Все проекты** в левой панели.

1. Выберите **+ Новый проект** в навигационном меню.

    ![Select new project.](../../../../../../translated_images/ru/select-new-project.cd31c0404088d7a3.webp)

1. Введите **Имя проекта**. Оно должно быть уникальным.

    ![Create project.](../../../../../../translated_images/ru/create-project.ca3b71298b90e420.webp)

1. Выберите **Создать проект**.

#### Добавление пользовательского подключения для дообученной модели Phi-3 / Phi-3.5

Для интеграции вашей пользовательской модели Phi-3 / Phi-3.5 с Prompt flow необходимо сохранить конечную точку модели и ключ в пользовательском подключении. Эта настройка обеспечивает доступ к вашей модель в Prompt flow.

#### Установка api ключа и URI конечной точки дообученной модели Phi-3 / Phi-3.5

1. Перейдите в [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Перейдите в рабочее пространство Azure Machine learning, которое вы создали.

1. Выберите **Endpoints** в левой панели.

    ![Select endpoints.](../../../../../../translated_images/ru/select-endpoints.ee7387ecd68bd18d.webp)

1. Выберите созданную конечную точку.

    ![Select endpoints.](../../../../../../translated_images/ru/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Выберите **Consume** в навигационном меню.

1. Скопируйте ваш **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ru/copy-endpoint-key.0650c3786bd646ab.webp)

#### Добавление пользовательского подключения

1. Перейдите на [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдите в созданный проект Microsoft Foundry.

1. В выбранном проекте выберите **Настройки** в левой панели.

1. Выберите **+ Новое подключение**.

    ![Select new connection.](../../../../../../translated_images/ru/select-new-connection.fa0f35743758a74b.webp)

1. Выберите **Пользовательские ключи** в навигационном меню.

    ![Select custom keys.](../../../../../../translated_images/ru/select-custom-keys.5a3c6b25580a9b67.webp)

1. Выполните следующие действия:

    - Нажмите **+ Добавить пару ключ-значение**.
    - В поле имени ключа введите **endpoint** и вставьте скопированный endpoint из Azure ML Studio в поле значения.
    - Снова нажмите **+ Добавить пару ключ-значение**.
    - В поле имени ключа введите **key** и вставьте скопированный ключ из Azure ML Studio в поле значения.
    - После добавления ключей выберите опцию **это секрет** чтобы ключ не отображался открыто.

    ![Add connection.](../../../../../../translated_images/ru/add-connection.ac7f5faf8b10b0df.webp)

1. Выберите **Добавить подключение**.

#### Создание Prompt flow

Вы добавили пользовательское подключение в Microsoft Foundry. Теперь создадим Prompt flow, используя следующие шаги. Затем вы подключите этот Prompt flow к пользовательскому подключению для использования дообученной модели в Prompt flow.

1. Перейдите в созданный проект Microsoft Foundry.

1. Выберите **Prompt flow** в левой панели.

1. Выберите **+ Создать** в навигационном меню.

    ![Select Promptflow.](../../../../../../translated_images/ru/select-promptflow.18ff2e61ab9173eb.webp)

1. Выберите **Чат-флоу** в навигационном меню.

    ![Select chat flow.](../../../../../../translated_images/ru/select-flow-type.28375125ec9996d3.webp)

1. Введите **Имя папки** для использования.

    ![Select chat flow.](../../../../../../translated_images/ru/enter-name.02ddf8fb840ad430.webp)

1. Выберите **Создать**.

#### Настройка Prompt flow для общения с вашей пользовательской моделью Phi-3 / Phi-3.5

Чтобы интегрировать дообученную модель Phi-3 / Phi-3.5 в Prompt flow, необходимо изменить существующий Prompt flow, так как он не предназначен для этой цели. Поэтому вам нужно перепроектировать Prompt flow для поддержания интеграции пользовательской модели.

1. В Prompt flow выполните следующие действия для перестройки существующего потока:

    - Выберите **Режим сырого файла**.
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

    - Выберите **Сохранить**.

    ![Select raw file mode.](../../../../../../translated_images/ru/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Добавьте следующий код в файл *integrate_with_promptflow.py* для использования пользовательской модели Phi-3 / Phi-3.5 в Prompt flow.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" — это имя пользовательского соединения, "endpoint", "key" — ключи в пользовательском соединении
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/ru/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Подробную информацию о работе с Prompt flow в Microsoft Foundry можно найти в статье [Prompt flow в Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Выберите **Ввод чата**, **Вывод чата** для включения общения с вашей моделью.

    ![Select Input Output.](../../../../../../translated_images/ru/select-input-output.c187fc58f25fbfc3.webp)

1. Теперь вы готовы общаться с вашей пользовательской моделью Phi-3 / Phi-3.5. В следующем упражнении вы узнаете, как запустить Prompt flow и использовать его для общения с вашей дообученной моделью Phi-3 / Phi-3.5.

> [!NOTE]
>
> Перестроенный поток должен выглядеть как на изображении ниже:
>
> ![Flow example](../../../../../../translated_images/ru/graph-example.82fd1bcdd3fc545b.webp)
>

#### Запуск Prompt flow

1. Выберите **Запустить вычислительные сессии**, чтобы начать Prompt flow.

    ![Start compute session.](../../../../../../translated_images/ru/start-compute-session.9acd8cbbd2c43df1.webp)

1. Выберите **Проверить и разобрать ввод**, чтобы обновить параметры.

    ![Validate input.](../../../../../../translated_images/ru/validate-input.c1adb9543c6495be.webp)

1. Выберите **Значение** для **подключения** к созданному пользовательскому подключению. Например, *connection*.

    ![Connection.](../../../../../../translated_images/ru/select-connection.1f2b59222bcaafef.webp)

#### Общение с вашей пользовательской моделью Phi-3 / Phi-3.5

1. Выберите **Чат**.

    ![Select chat.](../../../../../../translated_images/ru/select-chat.0406bd9687d0c49d.webp)

1. Вот пример результата: теперь вы можете общаться с вашей пользовательской моделью Phi-3 / Phi-3.5. Рекомендуется задавать вопросы, основанные на данных, использованных для дообучения.

    ![Chat with prompt flow.](../../../../../../translated_images/ru/chat-with-promptflow.1cf8cea112359ada.webp)

### Развертывание Azure OpenAI для оценки модели Phi-3 / Phi-3.5

Для оценки модели Phi-3 / Phi-3.5 в Microsoft Foundry необходимо развернуть модель Azure OpenAI. Эта модель будет использоваться для оценки производительности модели Phi-3 / Phi-3.5.

#### Развертывание Azure OpenAI

1. Войдите в [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдите в созданный проект Microsoft Foundry.

    ![Select Project.](../../../../../../translated_images/ru/select-project-created.5221e0e403e2c9d6.webp)

1. В выбранном проекте выберите **Развертывания** в левой панели.

1. Выберите **+ Развернуть модель** в навигационном меню.

1. Выберите **Развернуть базовую модель**.

    ![Select Deployments.](../../../../../../translated_images/ru/deploy-openai-model.95d812346b25834b.webp)

1. Выберите Azure OpenAI модель, которую хотите использовать. Например, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/ru/select-openai-model.959496d7e311546d.webp)

1. Выберите **Подтвердить**.

### Оценка дообученной модели Phi-3 / Phi-3.5 с помощью Prompt flow в Microsoft Foundry

### Начало нового тестирования

1. Перейдите в [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдите в созданный проект Microsoft Foundry.

    ![Select Project.](../../../../../../translated_images/ru/select-project-created.5221e0e403e2c9d6.webp)

1. В выбранном проекте выберите **Оценка** в левой панели.

1. Выберите **+ Новая оценка** в навигационном меню.

    ![Select evaluation.](../../../../../../translated_images/ru/select-evaluation.2846ad7aaaca7f4f.webp)

1. Выберите оценку **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/ru/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Выполните следующие действия:

    - Введите имя оценки. Оно должно быть уникальным.
    - Выберите тип задачи **Вопрос-ответ без контекста**, так как датасет **ULTRACHAT_200k**, используемый в этом руководстве, не содержит контекста.
    - Выберите Prompt flow, который хотите оценить.

    ![Prompt flow evaluation.](../../../../../../translated_images/ru/evaluation-setting1.4aa08259ff7a536e.webp)

1. Выберите **Далее**.

1. Выполните следующие действия:

    - Выберите **Добавить ваш датасет** для загрузки датасета. Например, вы можете загрузить тестовый набор данных, например *test_data.json1*, входящий в состав датасета **ULTRACHAT_200k**.
    - Выберите соответствующий **Столбец датасета**, который соответствует вашему датасету. Например, если вы используете датасет **ULTRACHAT_200k**, выберите **${data.prompt}** как столбец датасета.

    ![Prompt flow evaluation.](../../../../../../translated_images/ru/evaluation-setting2.07036831ba58d64e.webp)

1. Выберите **Далее**.

1. Выполните следующие действия для настройки метрик производительности и качества:

    - Выберите метрики производительности и качества, которые хотите использовать.
    - Выберите Azure OpenAI модель, созданную для оценки. Например, **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/ru/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Выполните следующие действия для настройки метрик рисков и безопасности:

    - Выберите метрики рисков и безопасности, которые хотите использовать.
    - Выберите порог для расчёта показателя дефектов. Например, выберите **Средний**.
    - Для **вопроса** выберите **Источник данных** как **{$data.prompt}**.
    - Для **ответа** выберите **Источник данных** как **{$run.outputs.answer}**.
    - Для **истинных данных** выберите **Источник данных** как **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/ru/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Выберите **Далее**.

1. Выберите **Отправить**, чтобы начать оценку.

1. Оценка займет некоторое время. Вы можете отслеживать прогресс во вкладке **Оценка**.

### Просмотр результатов оценки

> [!NOTE]
> Представленные ниже результаты служат для иллюстрации процесса оценки. В этом руководстве мы использовали модель, дообученную на относительно небольшом наборе данных, что может привести к неоптимальным результатам. Фактические результаты могут значительно различаться в зависимости от размера, качества и разнообразия используемого набора данных, а также от конкретных параметров настройки модели.

После завершения оценки вы можете ознакомиться с результатами по метрикам производительности и безопасности.
1. Метрики производительности и качества:

    - оценить эффективность модели в генерации последовательных, плавных и релевантных ответов.

    ![Evaluation result.](../../../../../../translated_images/ru/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Метрики риска и безопасности:

    - Обеспечить безопасность выводов модели и их соответствие принципам Ответственного ИИ, избегая любой вредоносный или оскорбительный контент.

    ![Evaluation result.](../../../../../../translated_images/ru/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Вы можете прокрутить вниз, чтобы увидеть **Подробные результаты метрик**.

    ![Evaluation result.](../../../../../../translated_images/ru/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Оценивая вашу кастомную модель Phi-3 / Phi-3.5 по метрикам производительности и безопасности, вы можете подтвердить, что модель не только эффективна, но и соответствует принципам ответственного ИИ, что делает её готовой к реальному использованию.

## Поздравляем!

### Вы завершили этот учебный курс

Вы успешно оценили дообученную модель Phi-3, интегрированную с Prompt flow в Microsoft Foundry. Это важный шаг для обеспечения того, чтобы ваши ИИ-модели не только работали хорошо, но и соответствовали принципам Ответственного ИИ Microsoft, помогая создавать надежные и заслуживающие доверия ИИ-приложения.

![Architecture.](../../../../../../translated_images/ru/architecture.10bec55250f5d6a4.webp)

## Очистка ресурсов Azure

Очистите ресурсы Azure, чтобы избежать дополнительных начислений на ваш счет. Перейдите в портал Azure и удалите следующие ресурсы:

- Ресурс Azure Machine learning.
- Конечную точку модели Azure Machine learning.
- Ресурс проекта Microsoft Foundry.
- Ресурс Prompt flow Microsoft Foundry.

### Следующие шаги

#### Документация

- [Оценка ИИ-систем с использованием панели устойчивого ИИ](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Метрики оценки и мониторинга для генеративного ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Документация Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Документация Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Учебные материалы

- [Введение в подход Microsoft к Ответственному ИИ](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Введение в Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Референс

- [Что такое Ответственный ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Анонс новых инструментов в Azure AI для создания более безопасных и надежных генеративных приложений ИИ](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Оценка генеративных ИИ-приложений](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на родном языке следует считать авторитетным источником. Для важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за какие-либо недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->