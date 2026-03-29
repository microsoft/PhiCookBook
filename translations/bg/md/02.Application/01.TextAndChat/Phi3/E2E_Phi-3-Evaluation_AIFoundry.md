# Оценка на финно-настроения модел Phi-3 / Phi-3.5 в Microsoft Foundry с фокус върху принципите за отговорен ИИ на Microsoft

Този пример от край до край (E2E) е базиран на ръководството "[Оценка на финно-настроени модели Phi-3 / 3.5 в Microsoft Foundry с фокус върху отговорен ИИ на Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" от Microsoft Tech Community.

## Преглед

### Как можете да оцените безопасността и производителността на финно-настроен модел Phi-3 / Phi-3.5 в Microsoft Foundry?

Финно-настройването на модел понякога може да доведе до нежелани или непредвидени отговори. За да се гарантира, че моделът остава безопасен и ефективен, е важно да се оценят потенциалът му да генерира вредно съдържание и способността му да предоставя точни, релевантни и съгласувани отговори. В това ръководство ще научите как да оцените безопасността и производителността на финно-настроен модел Phi-3 / Phi-3.5, интегриран с Prompt flow в Microsoft Foundry.

Ето процеса за оценка на Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/bg/architecture.10bec55250f5d6a4.webp)

*Източник на изображението: [Оценка на приложения за генеративен ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> За по-подробна информация и за да разгледате допълнителни ресурси за Phi-3 / Phi-3.5, моля посетете [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Предварителни изисквания

- [Python](https://www.python.org/downloads)
- [Абонамент за Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Финно-настроен модел Phi-3 / Phi-3.5

### Съдържание

1. [**Сценарий 1: Въведение в оценката с Prompt flow на Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Въведение в оценката на безопасността](#въведение-в-оценката-на-безопасността)
    - [Въведение в оценката на производителността](#въведение-в-оценката-на-производителността)

1. [**Сценарий 2: Оценка на модел Phi-3 / Phi-3.5 в Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Преди да започнете](#преди-да-започнете)
    - [Деплойване на Azure OpenAI за оценка на модела Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Оценка на финно-настроения модел Phi-3 / Phi-3.5 с оценката Prompt flow на Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Поздравления!](#поздравления)

## **Сценарий 1: Въведение в оценката с Prompt flow на Microsoft Foundry**

### Въведение в оценката на безопасността

За да осигурите, че вашият ИИ модел е етичен и безопасен, е от съществено значение да го оцените спрямо принципите за отговорен ИИ на Microsoft. В Microsoft Foundry оценката на безопасността ви позволява да оцените уязвимостта на вашия модел към атаки за заобикаляне (jailbreak) и потенциала му да генерира вредно съдържание, което е пряко свързано с тези принципи.

![Safaty evaluation.](../../../../../../translated_images/bg/safety-evaluation.083586ec88dfa950.webp)

*Източник на изображението: [Оценка на приложения за генеративен ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Принципите за отговорен ИИ на Microsoft

Преди да започнете техническите стъпки, е важно да разберете принципите за отговорен ИИ на Microsoft — етична рамка, предназначена да насочва отговорното разработване, внедряване и експлоатация на ИИ системи. Тези принципи ръководят отговорното проектиране, разработване и внедряване на ИИ системи, гарантирайки, че технологиите са създадени по начин, който е справедлив, прозрачен и включващ. Те са основата за оценка на безопасността на ИИ моделите.

Принципите за отговорен ИИ на Microsoft включват:

- **Справедливост и приобщаване**: ИИ системите трябва да третират всички справедливо и да избягват да влияят по различен начин на групи със сходно положение. Например, когато ИИ системи предоставят насоки за медицинско лечение, кандидатстване за заем или заетост, те трябва да правят същите препоръки на всеки с подобни симптоми, финансови обстоятелства или професионални квалификации.

- **Надеждност и безопасност**: За да се изгради доверие, е критично ИИ системите да работят надеждно, безопасно и постоянно. Тези системи трябва да функционират според първоначалното си проектиране, да реагират безопасно на непредвидени условия и да устояват на вредни манипулации. Поведението им и разнообразието от условия, които могат да обработват, отразяват диапазона от ситуации и обстоятелства, които разработчиците са предвидили по време на проектиране и тестване.

- **Прозрачност**: Когато ИИ системите подпомагат взимането на решения с огромно въздействие върху живота на хората, е от съществено значение хората да разбират как тези решения са били взети. Например, банка може да използва ИИ система, за да определи дали дадено лице е кредитоспособно. Компания може да използва ИИ система, за да определи най-квалифицираните кандидати за наемане.

- **Поверителност и сигурност**: С разпространението на ИИ защитата на поверителността и сигурността на личната и бизнес информация стават все по-важни и сложни. При ИИ поверителността и сигурността на данните изискват специално внимание, тъй като достъпът до данни е от съществено значение за точните и информирани прогнози и решения на системите.

- **Отговорност**: Хората, които проектират и внедряват ИИ системи, трябва да носят отговорност за начина, по който системите работят. Организациите трябва да се позовават на индустриални стандарти за разработване на норми за отговорност. Тези норми могат да гарантират, че ИИ системите не са окончателна инстанция по решения, които засягат живота на хората. Те също така могат да гарантират, че хората запазват значим контрол върху иначе високо автономни ИИ системи.

![Fill hub.](../../../../../../translated_images/bg/responsibleai2.c07ef430113fad8c.webp)

*Източник на изображението: [Какво е отговорен ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> За да научите повече за принципите за отговорен ИИ на Microsoft, посетете [Какво е отговорен ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрики за безопасност

В това ръководство ще оцените безопасността на финно-настроения модел Phi-3, използвайки метриките за безопасност на Microsoft Foundry. Тези метрики ви помагат да прецените потенциала на модела да генерира вредно съдържание и уязвимостта му към jailbreak атаки. Метриките за безопасност включват:

- **Съдържание, свързано с самонараняване**: Оценява дали моделът има склонност да генерира съдържание, свързано със самонараняване.
- **Омразно и несправедливо съдържание**: Оценява дали моделът има склонност да генерира омразно или несправедливо съдържание.
- **Насилствено съдържание**: Оценява дали моделът има склонност да генерира насилствено съдържание.
- **Сексуално съдържание**: Оценява дали моделът има склонност да генерира неподходящо сексуално съдържание.

Оценявайки тези аспекти, се гарантира, че ИИ моделът не създава вредно или обидно съдържание, което е в съответствие с обществените ценности и регулаторните изисквания.

![Evaluate based on safety.](../../../../../../translated_images/bg/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Въведение в оценката на производителността

За да сте сигурни, че вашият ИИ модел работи според очакванията, е важно да оцените неговата производителност спрямо метрики за производителност. В Microsoft Foundry оценките на производителността позволяват да прецените ефективността на вашия модел при генериране на точни, релевантни и съгласувани отговори.

![Safaty evaluation.](../../../../../../translated_images/bg/performance-evaluation.48b3e7e01a098740.webp)

*Източник на изображението: [Оценка на приложения за генеративен ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрики за производителност

В това ръководство ще оцените производителността на финно-настроения модел Phi-3 / Phi-3.5, използвайки метриките за производителност на Microsoft Foundry. Тези метрики ви помагат да прецените ефективността на модела да генерира точни, релевантни и съгласувани отговори. Метриките за производителност включват:

- **Закрепеност (Groundedness)**: Оценява доколко отговорите, които се генерират, съответстват на информацията от изходния източник.
- **Релевантност**: Оценява уместността на генерираните отговори спрямо зададените въпроси.
- **Кохерентност**: Оценява колко плавно текства, чете се естествено и прилича на човешки език.
- **Плавност**: Оценява езиковата компетентност на генерирания текст.
- **Съпоставимост с GPT**: Сравнява генерирания отговор с реалните данни за подобност.
- **F1 резултат**: Изчислява съотношението на споделени думи между генерирания отговор и изходните данни.

Тези метрики ви помагат да оцените ефективността на модела при генериране на точни, релевантни и съгласувани отговори.

![Evaluate based on performance.](../../../../../../translated_images/bg/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Сценарий 2: Оценка на модел Phi-3 / Phi-3.5 в Microsoft Foundry**

### Преди да започнете

Това ръководство е продължение на предишните блог публикации, "[Финно-настройване и интегриране на персонализирани Phi-3 модели с Prompt Flow: Стъпка по стъпка](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Финно-настройване и интегриране на персонализирани Phi-3 модели с Prompt Flow в Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." В тези публикации описахме процеса на финно-настройване на модел Phi-3 / Phi-3.5 в Microsoft Foundry и интегрирането му с Prompt flow.

В това ръководство ще деплойнете Azure OpenAI модел като оценяващ в Microsoft Foundry и ще го използвате за оценка на вашия финно-настроен модел Phi-3 / Phi-3.5.

Преди да започнете това ръководство, уверете се, че разполагате със следните предварителни изисквания, описани в предишните ръководства:

1. Подготвен набор от данни за оценка на финно-настроения модел Phi-3 / Phi-3.5.  
1. Модел Phi-3 / Phi-3.5, който е финно-настроен и деплойнат в Azure Machine Learning.  
1. Prompt flow, интегриран с вашия финно-настроен модел Phi-3 / Phi-3.5 в Microsoft Foundry.

> [!NOTE]
> Ще използвате файла *test_data.jsonl*, намиращ се в папката с данни от набора **ULTRACHAT_200k**, изтеглен в предишните блог постове, като набор от данни за оценка на финно-настроения модел Phi-3 / Phi-3.5.

#### Интегриране на персонализирания модел Phi-3 / Phi-3.5 с Prompt flow в Microsoft Foundry (Подход с първо кодиране)

> [!NOTE]
> Ако следвахте подход с нисък код, описан в "[Финно-настройване и интегриране на персонализирани Phi-3 модели с Prompt Flow в Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", можете да пропуснете това упражнение и да преминете към следващото.  
> Въпреки това, ако следвахте подход с първо кодиране, описан в "[Финно-настройване и интегриране на персонализирани Phi-3 модели с Prompt Flow: Стъпка по стъпка](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)", за да финно-настроите и деплойнете вашия модел Phi-3 / Phi-3.5, процесът на свързване на модела с Prompt flow е леко различен. Ще научите този процес в това упражнение.

За да продължите, трябва да интегрирате финно-настроения си модел Phi-3 / Phi-3.5 в Prompt flow в Microsoft Foundry.

#### Създаване на Microsoft Foundry Hub

Трябва да създадете Hub преди да създадете Проект. Hub функционира като Resource Group, позволявайки ви да организирате и управлявате няколко проекта в Microsoft Foundry.
1. Влезте в [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Изберете **All hubs** от таба вляво.

1. Изберете **+ New hub** от навигационното меню.

    ![Create hub.](../../../../../../translated_images/bg/create-hub.5be78fb1e21ffbf1.webp)

1. Изпълнете следните задачи:

    - Въведете **Hub name**. Трябва да е уникална стойност.
    - Изберете своя Azure **Subscription**.
    - Изберете **Resource group**, която ще използвате (създайте нова, ако е необходимо).
    - Изберете **Location**, която желаете да използвате.
    - Изберете **Connect Azure AI Services**, която искате да използвате (създайте нова, ако е необходимо).
    - Изберете **Connect Azure AI Search** и **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/bg/fill-hub.baaa108495c71e34.webp)

1. Изберете **Next**.

#### Създаване на Microsoft Foundry проект

1. В хъба, който създадохте, изберете **All projects** от таба вляво.

1. Изберете **+ New project** от навигационното меню.

    ![Select new project.](../../../../../../translated_images/bg/select-new-project.cd31c0404088d7a3.webp)

1. Въведете **Project name**. Трябва да е уникална стойност.

    ![Create project.](../../../../../../translated_images/bg/create-project.ca3b71298b90e420.webp)

1. Изберете **Create a project**.

#### Добавяне на персонална връзка за фино настроения модел Phi-3 / Phi-3.5

За да интегрирате персонализирания си модел Phi-3 / Phi-3.5 с Prompt flow, трябва да запазите крайна точка и ключ на модела в персонална връзка. Тази настройка осигурява достъп до вашия персонализиран модел Phi-3 / Phi-3.5 в Prompt flow.

#### Задаване на api key и endpoint uri за фино настроения модел Phi-3 / Phi-3.5

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Навигирайте до работното пространство за Azure Machine learning, което създадохте.

1. Изберете **Endpoints** от таба вляво.

    ![Select endpoints.](../../../../../../translated_images/bg/select-endpoints.ee7387ecd68bd18d.webp)

1. Изберете крайната точка, която създадохте.

    ![Select endpoints.](../../../../../../translated_images/bg/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Изберете **Consume** от навигационното меню.

1. Копирайте своя **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/bg/copy-endpoint-key.0650c3786bd646ab.webp)

#### Добавяне на персоналната връзка

1. Посетете [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Навигирайте до Microsoft Foundry проекта, който създадохте.

1. В проекта, който създадохте, изберете **Settings** от таба вляво.

1. Изберете **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/bg/select-new-connection.fa0f35743758a74b.webp)

1. Изберете **Custom keys** от навигационното меню.

    ![Select custom keys.](../../../../../../translated_images/bg/select-custom-keys.5a3c6b25580a9b67.webp)

1. Изпълнете следните задачи:

    - Изберете **+ Add key value pairs**.
    - За името на ключа въведете **endpoint** и поставете крайна точка, която копирахте от Azure ML Studio, в полето за стойност.
    - Отново изберете **+ Add key value pairs**.
    - За името на ключа въведете **key** и поставете ключа, който копирахте от Azure ML Studio, в полето за стойност.
    - След добавянето на ключовете, изберете **is secret**, за да предотвратите разкриването на ключа.

    ![Add connection.](../../../../../../translated_images/bg/add-connection.ac7f5faf8b10b0df.webp)

1. Изберете **Add connection**.

#### Създаване на Prompt flow

Вече добавихте персонална връзка в Microsoft Foundry. Сега нека създадем Prompt flow, използвайки следните стъпки. След това ще свържете този Prompt flow с персоналната връзка, за да използвате фино настроения модел в Prompt flow.

1. Навигирайте до Microsoft Foundry проекта, който създадохте.

1. Изберете **Prompt flow** от таба вляво.

1. Изберете **+ Create** от навигационното меню.

    ![Select Promptflow.](../../../../../../translated_images/bg/select-promptflow.18ff2e61ab9173eb.webp)

1. Изберете **Chat flow** от навигационното меню.

    ![Select chat flow.](../../../../../../translated_images/bg/select-flow-type.28375125ec9996d3.webp)

1. Въведете име за **Folder name**.

    ![Select chat flow.](../../../../../../translated_images/bg/enter-name.02ddf8fb840ad430.webp)

1. Изберете **Create**.

#### Настройване на Prompt flow за чат с вашия персонализиран модел Phi-3 / Phi-3.5

Трябва да интегрирате фино настроения модел Phi-3 / Phi-3.5 в Prompt flow. Въпреки това, съществуващият Prompt flow, който е предоставен, не е предназначен за тази цел. Затова трябва да преработите Prompt flow, за да позволите интеграция на персонализирания модел.

1. В Prompt flow изпълнете следните задачи, за да пресъздадете съществуващия flow:

    - Изберете **Raw file mode**.
    - Изтрийте целия съществуващ код във файла *flow.dag.yml*.
    - Добавете следния код в *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/bg/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Добавете следния код в *integrate_with_promptflow.py*, за да използвате персонализирания модел Phi-3 / Phi-3.5 в Prompt flow.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" е името на Персонализираната Връзка, "endpoint", "key" са ключовете в Персонализираната Връзка
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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/bg/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> За по-подробна информация относно използването на Prompt flow в Microsoft Foundry, можете да се обърнете към [Prompt flow в Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изберете **Chat input**, **Chat output**, за да активирате чат с вашия модел.

    ![Select Input Output.](../../../../../../translated_images/bg/select-input-output.c187fc58f25fbfc3.webp)

1. Сега сте готови да чатите с персонализирания си модел Phi-3 / Phi-3.5. В следващото упражнение ще научите как да стартирате Prompt flow и да го използвате за чат с фино настроения модел Phi-3 / Phi-3.5.

> [!NOTE]
>
> Преработеният flow трябва да изглежда като изображението по-долу:
>
> ![Flow example](../../../../../../translated_images/bg/graph-example.82fd1bcdd3fc545b.webp)
>

#### Стартиране на Prompt flow

1. Изберете **Start compute sessions**, за да стартирате Prompt flow.

    ![Start compute session.](../../../../../../translated_images/bg/start-compute-session.9acd8cbbd2c43df1.webp)

1. Изберете **Validate and parse input**, за да обновите параметрите.

    ![Validate input.](../../../../../../translated_images/bg/validate-input.c1adb9543c6495be.webp)

1. Изберете стойността на **connection** към персоналната връзка, която създадохте. Например, *connection*.

    ![Connection.](../../../../../../translated_images/bg/select-connection.1f2b59222bcaafef.webp)

#### Чат с персонализирания модел Phi-3 / Phi-3.5

1. Изберете **Chat**.

    ![Select chat.](../../../../../../translated_images/bg/select-chat.0406bd9687d0c49d.webp)

1. Ето пример за резултатите: Сега можете да чатите с персонализирания си модел Phi-3 / Phi-3.5. Препоръчително е да задавате въпроси, базирани на данните, използвани за финото настройване.

    ![Chat with prompt flow.](../../../../../../translated_images/bg/chat-with-promptflow.1cf8cea112359ada.webp)

### Деплойване на Azure OpenAI за оценка на модела Phi-3 / Phi-3.5

За да оцените модела Phi-3 / Phi-3.5 в Microsoft Foundry, трябва да разположите модел Azure OpenAI. Този модел ще се използва за оценяване на производителността на модела Phi-3 / Phi-3.5.

#### Деплойване на Azure OpenAI

1. Влезте в [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Навигирайте до Microsoft Foundry проекта, който създадохте.

    ![Select Project.](../../../../../../translated_images/bg/select-project-created.5221e0e403e2c9d6.webp)

1. В проекта, който създадохте, изберете **Deployments** от таба вляво.

1. Изберете **+ Deploy model** от навигационното меню.

1. Изберете **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/bg/deploy-openai-model.95d812346b25834b.webp)

1. Изберете Azure OpenAI модела, който искате да използвате. Например, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/bg/select-openai-model.959496d7e311546d.webp)

1. Изберете **Confirm**.

### Оценка на фино настроения модел Phi-3 / Phi-3.5 с помощта на Prompt flow оценка в Microsoft Foundry

### Стартиране на нова оценка

1. Посетете [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Навигирайте до Microsoft Foundry проекта, който създадохте.

    ![Select Project.](../../../../../../translated_images/bg/select-project-created.5221e0e403e2c9d6.webp)

1. В проекта, който създадохте, изберете **Evaluation** от таба вляво.

1. Изберете **+ New evaluation** от навигационното меню.

    ![Select evaluation.](../../../../../../translated_images/bg/select-evaluation.2846ad7aaaca7f4f.webp)

1. Изберете оценката **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/bg/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Изпълнете следните задачи:

    - Въведете име на оценката. Трябва да е уникална стойност.
    - Изберете **Question and answer without context** като тип задача. Това е така, защото наборът от данни **ULTRACHAT_200k**, използван в този урок, не съдържа контекст.
    - Изберете prompt flow, който искате да оцените.

    ![Prompt flow evaluation.](../../../../../../translated_images/bg/evaluation-setting1.4aa08259ff7a536e.webp)

1. Изберете **Next**.

1. Изпълнете следните задачи:

    - Изберете **Add your dataset**, за да качите набора от данни. Например, можете да качите тестовия файл, като *test_data.json1*, който е включен при изтегляне на набора данни **ULTRACHAT_200k**.
    - Изберете подходящата **Dataset column**, която съвпада с вашия набор от данни. Например, ако използвате набора от данни **ULTRACHAT_200k**, изберете **${data.prompt}** като колоната на набора от данни.

    ![Prompt flow evaluation.](../../../../../../translated_images/bg/evaluation-setting2.07036831ba58d64e.webp)

1. Изберете **Next**.

1. Изпълнете следните задачи за конфигуриране на метриките за производителност и качество:

    - Изберете метриките за производителност и качество, които искате да използвате.
    - Изберете Azure OpenAI модела, който създадохте за оценка. Например, изберете **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/bg/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Изпълнете следните задачи за конфигуриране на метриките за риск и безопасност:

    - Изберете метриките за риск и безопасност, които искате да използвате.
    - Изберете праговата стойност за изчисляване на степента на дефекти, която искате да използвате. Например, изберете **Medium**.
    - За **question**, изберете **Data source** на **{$data.prompt}**.
    - За **answer**, изберете **Data source** на **{$run.outputs.answer}**.
    - За **ground_truth**, изберете **Data source** на **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/bg/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Изберете **Next**.

1. Изберете **Submit**, за да стартирате оценката.

1. Оценката ще отнеме известно време. Можете да следите напредъка в таба **Evaluation**.

### Преглед на резултатите от оценката

> [!NOTE]
> Представените по-долу резултати имат за цел да илюстрират процеса на оценка. В този урок използвахме модел, фино настроен на сравнително малък набор от данни, което може да доведе до не оптимални резултати. Реалните резултати могат да варират значително в зависимост от размера, качеството и разнообразието на използвания набор от данни, както и от конкретната конфигурация на модела.

След като оценката приключи, можете да прегледате резултатите както за метриките за производителност, така и за безопасност.
1. Метрики за представяне и качество:

    - оценете ефективността на модела при генериране на свързани, гладко изречени и релевантни отговори.

    ![Evaluation result.](../../../../../../translated_images/bg/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Метрики за риск и безопасност:

    - Уверете се, че изходите на модела са безопасни и съответстват на принципите за отговорен изкуствен интелект, избягвайки всякакво вредно или обидно съдържание.

    ![Evaluation result.](../../../../../../translated_images/bg/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Можете да превъртите надолу, за да видите **Подробен резултат от метриките**.

    ![Evaluation result.](../../../../../../translated_images/bg/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Чрез оценяване на вашия персонализиран модел Phi-3 / Phi-3.5 спрямо метрики за представяне и безопасност, можете да потвърдите, че моделът е не само ефективен, но и спазва практиките за отговорен ИИ, което го прави готов за внедряване в реалния свят.

## Поздравления!

### Вие успешно завършихте този урок

Успешно оценихте фино настроения модел Phi-3, интегриран с Prompt flow в Microsoft Foundry. Това е важна стъпка за осигуряване, че вашите AI модели не само работят добре, но и спазват принципите на Microsoft за отговорен изкуствен интелект, за да ви помогнат да изградите надеждни и доверени AI приложения.

![Architecture.](../../../../../../translated_images/bg/architecture.10bec55250f5d6a4.webp)

## Почистване на Azure ресурси

Почистете вашите Azure ресурси, за да избегнете допълнителни такси по сметката си. Отидете в Azure портала и изтрийте следните ресурси:

- Ресурсът за Azure Machine Learning.
- Крайна точка на модела в Azure Machine Learning.
- Ресурсът Microsoft Foundry Project.
- Ресурсът Microsoft Foundry Prompt flow.

### Следващи стъпки

#### Документация

- [Оценка на AI системи чрез таблото за отговорен ИИ](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Метрики за оценяване и мониторинг при генеративен ИИ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Документация за Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Документация за Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Обучителни материали

- [Въведение в подхода на Microsoft за отговорен ИИ](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Въведение в Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Референции

- [Какво е отговорен ИИ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Обявяване на нови инструменти в Azure AI за създаване на по-сигурни и надеждни генеративни AI приложения](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Оценка на генеративни AI приложения](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, имайте предвид, че автоматичните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->