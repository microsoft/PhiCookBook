<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T17:15:43+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "bg"
}
-->
# Оценка на фино-настроения модел Phi-3 / Phi-3.5 в Azure AI Foundry с фокус върху принципите за отговорен AI на Microsoft

Този краен (E2E) пример е базиран на ръководството "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" от Microsoft Tech Community.

## Преглед

### Как можете да оцените безопасността и производителността на фино-настроен модел Phi-3 / Phi-3.5 в Azure AI Foundry?

Финото настройване на модел понякога може да доведе до нежелани или неочаквани отговори. За да се гарантира, че моделът остава безопасен и ефективен, е важно да се оцени потенциалът му да генерира вредно съдържание и способността му да предоставя точни, релевантни и последователни отговори. В този урок ще научите как да оцените безопасността и производителността на фино-настроен модел Phi-3 / Phi-3.5, интегриран с Prompt flow в Azure AI Foundry.

Ето процеса на оценка в Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.bg.png)

*Източник на изображението: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> За по-подробна информация и допълнителни ресурси за Phi-3 / Phi-3.5, моля посетете [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Предварителни изисквания

- [Python](https://www.python.org/downloads)
- [Абонамент в Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Фино-настроен модел Phi-3 / Phi-3.5

### Съдържание

1. [**Сценарий 1: Въведение в оценката с Prompt flow на Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Въведение в оценката на безопасността](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Въведение в оценката на производителността](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Сценарий 2: Оценка на модел Phi-3 / Phi-3.5 в Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Преди да започнете](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Деплой на Azure OpenAI за оценка на модел Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Оценка на фино-настроения модел Phi-3 / Phi-3.5 с помощта на Prompt flow в Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Поздравления!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Сценарий 1: Въведение в оценката с Prompt flow на Azure AI Foundry**

### Въведение в оценката на безопасността

За да сте сигурни, че вашият AI модел е етичен и безопасен, е от съществено значение да го оцените спрямо принципите за отговорен AI на Microsoft. В Azure AI Foundry, оценките за безопасност ви позволяват да прецените уязвимостта на модела към jailbreak атаки и потенциала му да генерира вредно съдържание, което е в пълно съответствие с тези принципи.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.bg.png)

*Източник на изображението: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Принципи за отговорен AI на Microsoft

Преди да започнете техническите стъпки, е важно да разберете принципите за отговорен AI на Microsoft – етична рамка, предназначена да насочва отговорното разработване, внедряване и експлоатация на AI системи. Тези принципи ръководят отговорния дизайн, разработка и внедряване на AI системи, като гарантират, че AI технологиите са създадени по справедлив, прозрачен и приобщаващ начин. Те са основата за оценка на безопасността на AI моделите.

Принципите за отговорен AI на Microsoft включват:

- **Справедливост и приобщаване**: AI системите трябва да третират всички справедливо и да избягват различно третиране на сходни групи хора. Например, когато AI системи предоставят насоки за медицинско лечение, кредитни заявки или наемане на работа, те трябва да дават еднакви препоръки на всички с подобни симптоми, финансово положение или професионални квалификации.

- **Надеждност и безопасност**: За да се изгради доверие, е критично AI системите да работят надеждно, безопасно и последователно. Те трябва да функционират според първоначалния дизайн, да реагират безопасно при неочаквани условия и да устояват на вредни манипулации. Начинът, по който се държат и разнообразието от условия, които могат да управляват, отразяват спектъра от ситуации, които разработчиците са предвидили по време на проектиране и тестване.

- **Прозрачност**: Когато AI системи подпомагат вземането на решения с голямо въздействие върху живота на хората, е важно хората да разбират как са взети тези решения. Например, банка може да използва AI система, за да реши дали дадено лице е кредитоспособно. Компания може да използва AI система, за да определи най-подходящите кандидати за работа.

- **Поверителност и сигурност**: С разрастването на AI, защитата на поверителността и сигурността на лична и бизнес информация става все по-важна и сложна. При AI, поверителността и сигурността на данните изискват специално внимание, тъй като достъпът до данни е съществен за правилните и информирани прогнози и решения за хората.

- **Отговорност**: Хората, които проектират и внедряват AI системи, трябва да носят отговорност за начина, по който тези системи функционират. Организациите трябва да се основават на индустриални стандарти, за да разработят норми за отговорност. Тези норми могат да гарантират, че AI системите не са окончателният авторитет при решения, които влияят на живота на хората. Те също така гарантират, че хората запазват смислен контрол върху иначе силно автономни AI системи.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.bg.png)

*Източник на изображението: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> За повече информация за принципите за отговорен AI на Microsoft, посетете [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрики за безопасност

В този урок ще оцените безопасността на фино-настроения модел Phi-3, използвайки метриките за безопасност на Azure AI Foundry. Тези метрики ви помагат да прецените потенциала на модела да генерира вредно съдържание и уязвимостта му към jailbreak атаки. Метриките за безопасност включват:

- **Съдържание, свързано с самонараняване**: Оценява дали моделът има склонност да генерира съдържание, свързано с самонараняване.
- **Ненавистно и несправедливо съдържание**: Оценява дали моделът има склонност да генерира ненавистно или несправедливо съдържание.
- **Насилствено съдържание**: Оценява дали моделът има склонност да генерира насилствено съдържание.
- **Сексуално съдържание**: Оценява дали моделът има склонност да генерира неподходящо сексуално съдържание.

Оценката на тези аспекти гарантира, че AI моделът не генерира вредно или обидно съдържание, съобразено със социалните ценности и регулаторните изисквания.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.bg.png)

### Въведение в оценката на производителността

За да сте сигурни, че AI моделът ви работи според очакванията, е важно да оцените производителността му спрямо метрики за ефективност. В Azure AI Foundry, оценките на производителността ви позволяват да прецените доколко моделът е ефективен при генерирането на точни, релевантни и последователни отговори.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.bg.png)

*Източник на изображението: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрики за производителност

В този урок ще оцените производителността на фино-настроения модел Phi-3 / Phi-3.5, използвайки метриките за производителност на Azure AI Foundry. Тези метрики ви помагат да прецените ефективността на модела при генериране на точни, релевантни и последователни отговори. Метриките за производителност включват:

- **Основаност (Groundedness)**: Оценява доколко генерираните отговори съответстват на информацията от входния източник.
- **Релевантност**: Оценява уместността на генерираните отговори спрямо зададените въпроси.
- **Кохерентност**: Оценява плавността на генерирания текст, естественото му звучене и приличането му на човешки език.
- **Плавност (Fluency)**: Оценява езиковата компетентност на генерирания текст.
- **Сходство с GPT (GPT Similarity)**: Сравнява генерирания отговор с истината за сходство.
- **F1 Score**: Изчислява съотношението на общите думи между генерирания отговор и изходните данни.

Тези метрики ви помагат да оцените ефективността на модела при генериране на точни, релевантни и последователни отговори.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.bg.png)

## **Сценарий 2: Оценка на модел Phi-3 / Phi-3.5 в Azure AI Foundry**

### Преди да започнете

Този урок е продължение на предишните блог постове, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." В тях разгледахме процеса на фино настройване на модел Phi-3 / Phi-3.5 в Azure AI Foundry и интегрирането му с Prompt flow.

В този урок ще деплойнете Azure OpenAI модел като оценител в Azure AI Foundry и ще го използвате за оценка на вашия фино-настроен модел Phi-3 / Phi-3.5.

Преди да започнете този урок, уверете се, че имате следните предварителни условия, описани в предишните уроци:

1. Подготвен набор от данни за оценка на фино-настроения модел Phi-3 / Phi-3.5.
1. Модел Phi-3 / Phi-3.5, който е фино настроен и деплойнат в Azure Machine Learning.
1. Prompt flow, интегриран с вашия фино-настроен модел Phi-3 / Phi-3.5 в Azure AI Foundry.

> [!NOTE]
> Като набор от данни за оценка на фино-настроения модел Phi-3 / Phi-3.5 ще използвате файла *test_data.jsonl*, намиращ се в папката data от набора **ULTRACHAT_200k**, изтеглен в предишните блог постове.

#### Интегриране на персонализирания модел Phi-3 / Phi-3.5 с Prompt flow в Azure AI Foundry (подход с код на първо място)

> [!NOTE]
> Ако сте следвали подхода с нисък код, описан в "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", можете да пропуснете това упражнение и да преминете към следващото.
> Ако обаче сте следвали подхода с код на първо място, описан в "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" за фино настройване и деплой на вашия модел Phi-3 / Phi-3.5, процесът за свързване на модела с Prompt flow е малко по-различен. Ще научите този процес в това упражнение.

За да продължите, трябва да интегрирате вашия фино-настроен модел Phi-3 / Phi-3.5 в Prompt flow в Azure AI Foundry.

#### Създаване на Azure AI Foundry Hub

Трябва да създадете Hub преди да създадете Проект. Hub действа като Resource Group, позволявайки ви да организирате и управлявате множество Проекти в Azure AI Foundry.

1. Влезте в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Изберете **All hubs** от лявата странична лента.

1. Изберете **+ New hub** от навигационното меню.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.bg.png)

1. Изпълнете следните стъпки:

    - Въведете **Hub name**. Той трябва да е уникално име.
    - Изберете вашия Azure **Subscription**.
    - Изберете **Resource group**, която искате да използвате (създайте нова, ако е необходимо).
    - Изберете **Location**, която искате да използвате.
    - Изберете **Connect Azure AI Services**, които искате да използвате (създайте нови, ако е необходимо).
    - Изберете **Connect Azure AI Search** и изберете **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.bg.png)

1. Изберете **Next**.

#### Създаване на проект в Azure AI Foundry

1. В Hub-а, който създадохте, изберете **All projects** от лявата странична лента.

1. Изберете **+ New project** от навигационното меню.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.bg.png)

1. Въведете **Project name**. Трябва да е уникално име.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.bg.png)

1. Изберете **Create a project**.

#### Добавяне на персонализирана връзка за финно настроения модел Phi-3 / Phi-3.5

За да интегрирате вашия персонализиран модел Phi-3 / Phi-3.5 с Prompt flow, трябва да запазите крайна точка и ключ на модела в персонализирана връзка. Тази настройка осигурява достъп до вашия модел Phi-3 / Phi-3.5 в Prompt flow.

#### Настройка на api ключ и endpoint uri за финно настроения модел Phi-3 / Phi-3.5

1. Посетете [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Навигирайте до създаденото от вас Azure Machine learning работно пространство.

1. Изберете **Endpoints** от лявата странична лента.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.bg.png)

1. Изберете крайна точка, която сте създали.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.bg.png)

1. Изберете **Consume** от навигационното меню.

1. Копирайте вашия **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.bg.png)

#### Добавяне на персонализирана връзка

1. Посетете [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Навигирайте до създадения от вас Azure AI Foundry проект.

1. В проекта, който създадохте, изберете **Settings** от лявата странична лента.

1. Изберете **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.bg.png)

1. Изберете **Custom keys** от навигационното меню.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.bg.png)

1. Изпълнете следните стъпки:

    - Изберете **+ Add key value pairs**.
    - За име на ключа въведете **endpoint** и поставете копирания endpoint от Azure ML Studio в полето за стойност.
    - Отново изберете **+ Add key value pairs**.
    - За име на ключа въведете **key** и поставете копирания ключ от Azure ML Studio в полето за стойност.
    - След добавяне на ключовете, маркирайте **is secret**, за да се предотврати показването на ключа.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.bg.png)

1. Изберете **Add connection**.

#### Създаване на Prompt flow

Вече добавихте персонализирана връзка в Azure AI Foundry. Сега нека създадем Prompt flow, като следваме следните стъпки. След това ще свържете този Prompt flow с персонализираната връзка, за да използвате финно настроения модел в Prompt flow.

1. Навигирайте до създадения от вас Azure AI Foundry проект.

1. Изберете **Prompt flow** от лявата странична лента.

1. Изберете **+ Create** от навигационното меню.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.bg.png)

1. Изберете **Chat flow** от навигационното меню.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.bg.png)

1. Въведете **Folder name**, който искате да използвате.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.bg.png)

1. Изберете **Create**.

#### Настройване на Prompt flow за чат с вашия персонализиран модел Phi-3 / Phi-3.5

Трябва да интегрирате финно настроения модел Phi-3 / Phi-3.5 в Prompt flow. Въпреки това, предоставеният съществуващ Prompt flow не е проектиран за тази цел. Затова трябва да преработите Prompt flow, за да позволите интеграцията на персонализирания модел.

1. В Prompt flow изпълнете следните стъпки, за да изградите отново съществуващия flow:

    - Изберете **Raw file mode**.
    - Изтрийте целия съществуващ код във файла *flow.dag.yml*.
    - Добавете следния код във *flow.dag.yml*.

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.bg.png)

1. Добавете следния код в *integrate_with_promptflow.py*, за да използвате персонализирания модел Phi-3 / Phi-3.5 в Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.bg.png)

> [!NOTE]
> За по-подробна информация относно използването на Prompt flow в Azure AI Foundry, може да се консултирате с [Prompt flow в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изберете **Chat input**, **Chat output**, за да активирате чата с вашия модел.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.bg.png)

1. Сега сте готови да чатите с вашия персонализиран модел Phi-3 / Phi-3.5. В следващото упражнение ще научите как да стартирате Prompt flow и да го използвате за чат с вашия финно настроен модел Phi-3 / Phi-3.5.

> [!NOTE]
>
> Преработеният flow трябва да изглежда като изображението по-долу:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.bg.png)
>

#### Стартиране на Prompt flow

1. Изберете **Start compute sessions**, за да стартирате Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.bg.png)

1. Изберете **Validate and parse input**, за да обновите параметрите.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.bg.png)

1. Изберете стойността на **connection** към персонализираната връзка, която сте създали. Например, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.bg.png)

#### Чат с вашия персонализиран модел Phi-3 / Phi-3.5

1. Изберете **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.bg.png)

1. Ето пример за резултати: Сега можете да чатите с вашия персонализиран модел Phi-3 / Phi-3.5. Препоръчително е да задавате въпроси, базирани на данните, използвани за финното настройване.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.bg.png)

### Деплойване на Azure OpenAI за оценка на модела Phi-3 / Phi-3.5

За да оцените модела Phi-3 / Phi-3.5 в Azure AI Foundry, трябва да деплойнете Azure OpenAI модел. Този модел ще се използва за оценка на представянето на модела Phi-3 / Phi-3.5.

#### Деплойване на Azure OpenAI

1. Влезте в [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Навигирайте до създадения от вас Azure AI Foundry проект.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.bg.png)

1. В проекта, който създадохте, изберете **Deployments** от лявата странична лента.

1. Изберете **+ Deploy model** от навигационното меню.

1. Изберете **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.bg.png)

1. Изберете Azure OpenAI модела, който искате да използвате. Например, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.bg.png)

1. Изберете **Confirm**.

### Оценка на финно настроения модел Phi-3 / Phi-3.5 чрез оценката на Prompt flow в Azure AI Foundry

### Стартиране на нова оценка

1. Посетете [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Навигирайте до създадения от вас Azure AI Foundry проект.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.bg.png)

1. В проекта, който създадохте, изберете **Evaluation** от лявата странична лента.

1. Изберете **+ New evaluation** от навигационното меню.
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.bg.png)

1. Изберете оценка **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.bg.png)

1. Изпълнете следните задачи:

    - Въведете името на оценката. Трябва да е уникална стойност.
    - Изберете **Question and answer without context** като тип задача. Това е така, защото наборът от данни **UlTRACHAT_200k**, използван в този урок, не съдържа контекст.
    - Изберете prompt flow, който искате да оцените.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.bg.png)

1. Изберете **Next**.

1. Изпълнете следните задачи:

    - Изберете **Add your dataset**, за да качите набора от данни. Например, можете да качите тестовия файл, като *test_data.json1*, който е включен при изтегляне на **ULTRACHAT_200k**.
    - Изберете подходящата **Dataset column**, която съответства на вашия набор от данни. Например, ако използвате **ULTRACHAT_200k**, изберете **${data.prompt}** като колона на набора от данни.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.bg.png)

1. Изберете **Next**.

1. Изпълнете следните задачи, за да конфигурирате метриките за производителност и качество:

    - Изберете метриките за производителност и качество, които искате да използвате.
    - Изберете Azure OpenAI модела, който сте създали за оценката. Например, изберете **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.bg.png)

1. Изпълнете следните задачи, за да конфигурирате метриките за риск и безопасност:

    - Изберете метриките за риск и безопасност, които искате да използвате.
    - Изберете прага за изчисляване на процента на дефекти, който искате да използвате. Например, изберете **Medium**.
    - За **question** изберете **Data source** на **{$data.prompt}**.
    - За **answer** изберете **Data source** на **{$run.outputs.answer}**.
    - За **ground_truth** изберете **Data source** на **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.bg.png)

1. Изберете **Next**.

1. Изберете **Submit**, за да стартирате оценката.

1. Оценката ще отнеме известно време. Можете да следите напредъка в раздела **Evaluation**.

### Преглед на резултатите от оценката

> [!NOTE]
> Представените по-долу резултати са с илюстративна цел за процеса на оценка. В този урок използвахме модел, фино настроен върху сравнително малък набор от данни, което може да доведе до по-слаби резултати. Реалните резултати могат да варират значително в зависимост от размера, качеството и разнообразието на използвания набор от данни, както и от конкретната конфигурация на модела.

След като оценката приключи, можете да прегледате резултатите както за метриките за производителност, така и за безопасност.

1. Метрики за производителност и качество:

    - оценяват ефективността на модела при генериране на свързани, плавни и релевантни отговори.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.bg.png)

1. Метрики за риск и безопасност:

    - Гарантират, че изходните данни на модела са безопасни и съответстват на Принципите за отговорен AI, като избягват вредно или обидно съдържание.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.bg.png)

1. Можете да превъртите надолу, за да видите **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.bg.png)

1. Като оцените вашия персонализиран Phi-3 / Phi-3.5 модел спрямо метриките за производителност и безопасност, можете да потвърдите, че моделът не само е ефективен, но и спазва отговорните практики за AI, което го прави готов за реално използване.

## Поздравления!

### Завършихте този урок

Успешно оценихте фино настроения Phi-3 модел, интегриран с Prompt flow в Azure AI Foundry. Това е важна стъпка за гарантиране, че вашите AI модели не само работят добре, но и спазват принципите на Microsoft за отговорен AI, което ви помага да създавате надеждни и доверени AI приложения.

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.bg.png)

## Почистване на ресурсите в Azure

Почистете ресурсите в Azure, за да избегнете допълнителни такси по вашия акаунт. Отидете в Azure портала и изтрийте следните ресурси:

- Ресурсът Azure Machine learning.
- Крайна точка на модела Azure Machine learning.
- Ресурсът Azure AI Foundry Project.
- Ресурсът Azure AI Foundry Prompt flow.

### Следващи стъпки

#### Документация

- [Оценка на AI системи с помощта на таблото за отговорен AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Метрики за оценка и мониторинг на генеративен AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Документация на Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Документация за Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Обучителни материали

- [Въведение в подхода на Microsoft за отговорен AI](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Въведение в Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Референции

- [Какво е отговорен AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Обявяване на нови инструменти в Azure AI за създаване на по-сигурни и надеждни генеративни AI приложения](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Оценка на генеративни AI приложения](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.