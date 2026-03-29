# Оцінка тонко настроєної моделі Phi-3 / Phi-3.5 у Microsoft Foundry з урахуванням принципів відповідального ШІ Microsoft

Цей приклад енд-ту-енд (E2E) базується на керівництві "[Оцінка тонко настроєних моделей Phi-3 / 3.5 у Microsoft Foundry з фокусом на відповідальний ШІ Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" з Microsoft Tech Community.

## Огляд

### Як можна оцінити безпеку та продуктивність тонко настроєної моделі Phi-3 / Phi-3.5 у Microsoft Foundry?

Налаштування моделі іноді може призводити до небажаних або несподіваних відповідей. Щоб переконатися, що модель залишається безпечною та ефективною, важливо оцінити потенціал моделі генерувати шкідливий контент та її здатність давати точні, релевантні та зв’язні відповіді. У цьому посібнику ви навчитеся оцінювати безпеку та продуктивність тонко настроєної моделі Phi-3 / Phi-3.5, інтегрованої з Prompt flow у Microsoft Foundry.

Ось процес оцінки в Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/uk/architecture.10bec55250f5d6a4.webp)

*Джерело зображення: [Оцінка генеративних AI-додатків](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Для детальнішої інформації та додаткових ресурсів про Phi-3 / Phi-3.5, будь ласка, відвідайте [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Передумови

- [Python](https://www.python.org/downloads)
- [Підписка Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Тонко настроєна модель Phi-3 / Phi-3.5

### Зміст

1. [**Сценарій 1: Вступ до оцінки Prompt flow у Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Вступ до оцінки безпеки](#вступ-до-оцінки-безпеки)
    - [Вступ до оцінки продуктивності](#вступ-до-оцінки-продуктивності)

1. [**Сценарій 2: Оцінка моделі Phi-3 / Phi-3.5 у Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Перед початком](#перед-початком)
    - [Розгортання Azure OpenAI для оцінки моделі Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Оцінка тонко настроєної моделі Phi-3 / Phi-3.5 за допомогою оцінки Prompt flow у Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Вітаємо!](#вітаємо)

## **Сценарій 1: Вступ до оцінки Prompt flow у Microsoft Foundry**

### Вступ до оцінки безпеки

Щоб гарантувати, що ваша модель ШІ етична та безпечна, надзвичайно важливо оцінювати її відповідно до Принципів відповідального ШІ Microsoft. У Microsoft Foundry оцінки безпеки дозволяють перевірити вразливість вашої моделі до атак jailbreak та її потенціал генерувати шкідливий контент, що безпосередньо відповідає цим принципам.

![Safaty evaluation.](../../../../../../translated_images/uk/safety-evaluation.083586ec88dfa950.webp)

*Джерело зображення: [Оцінка генеративних AI-додатків](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Принципи відповідального ШІ Microsoft

Перш ніж почати технічні кроки, необхідно розуміти Принципи відповідального ШІ Microsoft — етичну рамку, створену для керування відповідальним розвитком, розгортанням та експлуатацією систем ШІ. Ці принципи керують відповідальним проєктуванням, розробкою та впровадженням систем ШІ, забезпечуючи їх справедливість, прозорість та інклюзивність. Саме ці принципи є основою для оцінки безпеки моделей ШІ.

Принципи відповідального ШІ Microsoft включають:

- **Справедливість і інклюзивність**: Системи ШІ повинні справедливо ставитися до всіх і уникати диференціації груп людей у схожих обставинах. Наприклад, система ШІ при наданні рекомендацій щодо медичного лікування, кредитних заявок або працевлаштування має пропонувати однакові рекомендації для всіх із подібними симптомами, фінансовим станом або кваліфікацією.

- **Надійність і безпека**: Для формування довіри системи ШІ повинні діяти надійно, безпечно та послідовно. Вони мають працювати так, як передбачалося під час проєктування, безпечно реагувати на непередбачені ситуації та протистояти шкідливим маніпуляціям. Їх поведінка і стійкість до різних умов відображають спектр ситуацій, які розробники врахували при розробці та тестуванні.

- **Прозорість**: Коли системи ШІ допомагають ухвалювати рішення з великим впливом на життя людей, надзвичайно важливо, щоб люди розуміли, як було прийняте це рішення. Наприклад, банк може використовувати систему ШІ для ухвалення рішення про кредитоспроможність клієнта, або компанія — для відбору найбільш кваліфікованих кандидатів.

- **Конфіденційність і безпека**: Зі збільшенням поширеності ШІ захист конфіденційності та інформації стає дедалі важливішим і складнішим. У контексті ШІ конфіденційність і безпека даних особливо важливі, оскільки доступ до даних необхідний для точних і обґрунтованих прогнозів та рішень про людей.

- **Відповідальність**: Люди, які розробляють і впроваджують системи ШІ, несуть відповідальність за їх роботу. Організації повинні використовувати галузеві стандарти для розробки норм відповідальності. Ці норми гарантують, що системи ШІ не будуть остаточним авторитетом у будь-якому рішенні, що впливає на життя людей, а люди зберігають значущий контроль над сильно автономними системами ШІ.

![Fill hub.](../../../../../../translated_images/uk/responsibleai2.c07ef430113fad8c.webp)

*Джерело зображення: [Що таке відповідальний ШІ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Щоб дізнатися більше про Принципи відповідального ШІ Microsoft, відвідайте сторінку [Що таке відповідальний ШІ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрики безпеки

У цьому посібнику ви оціните безпеку тонко настроєної моделі Phi-3 за допомогою метрик безпеки Microsoft Foundry. Ці метрики допомагають оцінити потенціал моделі генерувати шкідливий контент та її уразливість до атак jailbreak. Метрики безпеки включають:

- **Контент, пов’язаний із самошкодженням**: Оцінює, чи має модель тенденцію генерувати контент, пов’язаний із самошкодженням.
- **Ненависний і несправедливий контент**: Оцінює, чи має модель тенденцію генерувати ненависний або несправедливий контент.
- **Насильницький контент**: Оцінює, чи має модель тенденцію генерувати насильницький контент.
- **Сексуальний контент**: Оцінює, чи має модель тенденцію генерувати неприйнятний сексуальний контент.

Оцінка цих аспектів гарантує, що модель ШІ не продукує шкідливий чи образливий контент, що відповідає суспільним цінностям і нормативним вимогам.

![Evaluate based on safety.](../../../../../../translated_images/uk/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Вступ до оцінки продуктивності

Щоб переконатися, що модель ШІ працює, як очікувалося, важливо оцінювати її продуктивність за відповідними метриками. У Microsoft Foundry оцінка продуктивності дозволяє перевірити ефективність моделі у створенні точних, релевантних та зв’язних відповідей.

![Safaty evaluation.](../../../../../../translated_images/uk/performance-evaluation.48b3e7e01a098740.webp)

*Джерело зображення: [Оцінка генеративних AI-додатків](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрики продуктивності

У цьому посібнику ви оціните продуктивність тонко настроєної моделі Phi-3 / Phi-3.5 за допомогою метрик продуктивності Microsoft Foundry. Ці метрики допомагають оцінити ефективність моделі у створенні точних, релевантних та зв’язних відповідей. Метрики продуктивності включають:

- **Заснованість**: Оцінює наскільки відповіді узгоджуються з інформацією з вхідного джерела.
- **Актуальність**: Оцінює доречність створених відповідей до заданих запитань.
- **Зв’язність**: Оцінює, наскільки плавно текст читається, природно та схоже на людську мову.
- **Плавність**: Оцінює мовні навички створеного тексту.
- **Схожість GPT**: Порівнює створену відповідь із правдивою відповіддю на предмет схожості.
- **F1-оцінка**: Обчислює відношення спільних слів між відповіддю моделі та вихідними даними.

Ці метрики допомагають оцінити ефективність моделі у створенні точних, релевантних та зв’язних відповідей.

![Evaluate based on performance.](../../../../../../translated_images/uk/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Сценарій 2: Оцінка моделі Phi-3 / Phi-3.5 у Microsoft Foundry**

### Перед початком

Цей посібник є продовженням попередніх блогів, "[Тонка настройка та інтеграція користувацьких моделей Phi-3 із Prompt Flow: покрокове керівництво](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" та "[Тонка настройка та інтеграція користувацьких моделей Phi-3 із Prompt Flow у Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)". У цих публікаціях ми пройшли процес тонкого налаштування моделі Phi-3 / Phi-3.5 у Microsoft Foundry та інтеграції з Prompt flow.

У цьому посібнику ви розгорнете модель Azure OpenAI як оцінювач у Microsoft Foundry та використаєте її для оцінки вашої тонко настроєної моделі Phi-3 / Phi-3.5.

Перед початком переконайтеся, що у вас є такі передумови, описані у попередніх посібниках:

1. Підготовлений набір даних для оцінки тонко настроєної моделі Phi-3 / Phi-3.5.
1. Модель Phi-3 / Phi-3.5, яку було тонко налаштовано та розгорнуто в Azure Machine Learning.
1. Prompt flow, інтегрований з вашою тонко настроєною моделлю Phi-3 / Phi-3.5 у Microsoft Foundry.

> [!NOTE]
> Ви використовуватимете файл *test_data.jsonl*, розташований у папці data з набору даних **ULTRACHAT_200k**, завантаженого в попередніх блогах, як набір даних для оцінки тонко настроєної моделі Phi-3 / Phi-3.5.

#### Інтеграція користувацької моделі Phi-3 / Phi-3.5 з Prompt flow у Microsoft Foundry (підхід "спочатку код")

> [!NOTE]
> Якщо ви користувалися підходом з мінімальним кодуванням, описаним у "[Тонка настройка та інтеграція користувацьких моделей Phi-3 із Prompt Flow у Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", ви можете пропустити цю вправу та перейти до наступної.
> Однак, якщо ви використали підхід "спочатку код", описаний у "[Тонка настройка та інтеграція користувацьких моделей Phi-3 із Prompt Flow: покрокове керівництво](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" для тонкого налаштування та розгортання своєї моделі Phi-3 / Phi-3.5, процес підключення моделі до Prompt flow дещо відрізняється. Ви навчитесь цьому процесу у цій вправі.

Щоб продовжити, необхідно інтегрувати вашу тонко настроєну модель Phi-3 / Phi-3.5 у Prompt flow у Microsoft Foundry.

#### Створення Microsoft Foundry Hub

Перш ніж створювати Проєкт, потрібно створити Hub. Hub діє як Група ресурсів і дозволяє організовувати та керувати кількома Проєктами у Microsoft Foundry.
1. Увійдіть до [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Виберіть **Усі хаби** з лівої вкладки.

1. Виберіть **+ Новий хаб** з меню навігації.

    ![Create hub.](../../../../../../translated_images/uk/create-hub.5be78fb1e21ffbf1.webp)

1. Виконайте наступні дії:

    - Введіть **Назву хаба**. Вона повинна бути унікальною.
    - Виберіть вашу підписку Azure **Subscription**.
    - Виберіть **Групу ресурсів** для використання (створіть нову, якщо потрібно).
    - Виберіть **Розташування** для використання.
    - Виберіть **Підключити служби Azure AI** для використання (створіть нове, якщо потрібно).
    - Виберіть **Підключити Azure AI Search** на **Пропустити підключення**.

    ![Fill hub.](../../../../../../translated_images/uk/fill-hub.baaa108495c71e34.webp)

1. Виберіть **Далі**.

#### Створення проекту Microsoft Foundry

1. У створеному хабі виберіть **Усі проекти** з лівої вкладки.

1. Виберіть **+ Новий проект** з меню навігації.

    ![Select new project.](../../../../../../translated_images/uk/select-new-project.cd31c0404088d7a3.webp)

1. Введіть **Назву проекту**. Вона повинна бути унікальною.

    ![Create project.](../../../../../../translated_images/uk/create-project.ca3b71298b90e420.webp)

1. Виберіть **Створити проект**.

#### Додайте власне підключення для тонко налаштованої моделі Phi-3 / Phi-3.5

Щоб інтегрувати вашу власну модель Phi-3 / Phi-3.5 із Prompt flow, потрібно зберегти кінцеву точку (endpoint) моделі та ключ у власному підключенні. Це забезпечить доступ до вашої моделі Phi-3 / Phi-3.5 у Prompt flow.

#### Встановити api ключ і URI кінцевої точки тонко налаштованої моделі Phi-3 / Phi-3.5

1. Перейдіть до [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Перейдіть до робочої області Azure Machine learning, яку ви створили.

1. Виберіть **Endpoints** з лівої вкладки.

    ![Select endpoints.](../../../../../../translated_images/uk/select-endpoints.ee7387ecd68bd18d.webp)

1. Виберіть кінцеву точку, яку ви створили.

    ![Select endpoints.](../../../../../../translated_images/uk/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Виберіть **Consume** з меню навігації.

1. Скопіюйте ваші **REST endpoint** і **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/uk/copy-endpoint-key.0650c3786bd646ab.webp)

#### Додайте власне підключення

1. Перейдіть до [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдіть до вашого проекту Microsoft Foundry.

1. У проекті виберіть **Settings** з лівої вкладки.

1. Виберіть **+ Нове підключення**.

    ![Select new connection.](../../../../../../translated_images/uk/select-new-connection.fa0f35743758a74b.webp)

1. Виберіть **Custom keys** з меню навігації.

    ![Select custom keys.](../../../../../../translated_images/uk/select-custom-keys.5a3c6b25580a9b67.webp)

1. Виконайте наступні дії:

    - Виберіть **+ Додати пару ключ-значення**.
    - Для імені ключа введіть **endpoint** і вставте скопійований endpoint з Azure ML Studio у поле значення.
    - Ще раз виберіть **+ Додати пару ключ-значення**.
    - Для імені ключа введіть **key** і вставте скопійований ключ з Azure ML Studio у поле значення.
    - Після додавання ключів виберіть **is secret**, щоб запобігти розкриттю ключа.

    ![Add connection.](../../../../../../translated_images/uk/add-connection.ac7f5faf8b10b0df.webp)

1. Виберіть **Додати підключення**.

#### Створення Prompt flow

Ви додали власне підключення в Microsoft Foundry. Тепер створимо Prompt flow за допомогою наступних кроків. Потім ви підключите цей Prompt flow до власного підключення, щоб використовувати тонко налаштовану модель у Prompt flow.

1. Перейдіть до вашого проекту Microsoft Foundry.

1. Виберіть **Prompt flow** з лівої вкладки.

1. Виберіть **+ Створити** з меню навігації.

    ![Select Promptflow.](../../../../../../translated_images/uk/select-promptflow.18ff2e61ab9173eb.webp)

1. Виберіть **Chat flow** з меню навігації.

    ![Select chat flow.](../../../../../../translated_images/uk/select-flow-type.28375125ec9996d3.webp)

1. Введіть **Ім’я папки** для використання.

    ![Select chat flow.](../../../../../../translated_images/uk/enter-name.02ddf8fb840ad430.webp)

1. Виберіть **Створити**.

#### Налаштування Prompt flow для спілкування з тонко налаштованою моделлю Phi-3 / Phi-3.5

Вам потрібно інтегрувати тонко налаштовану модель Phi-3 / Phi-3.5 у Prompt flow. Однак існуючий Prompt flow не розроблено для цієї мети. Тому потрібно перепроєктувати Prompt flow для інтеграції власної моделі.

1. У Prompt flow виконайте наступні дії для перебудови існуючого потоку:

    - Виберіть **Raw file mode**.
    - Видаліть увесь існуючий код у файлі *flow.dag.yml*.
    - Додайте наступний код у *flow.dag.yml*.

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

    - Виберіть **Зберегти**.

    ![Select raw file mode.](../../../../../../translated_images/uk/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Додайте наступний код у *integrate_with_promptflow.py* для використання власної тонко налаштованої моделі Phi-3 / Phi-3.5 у Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Налаштування логування
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

        # "connection" — це назва користувацького з’єднання, "endpoint", "key" — ключі в користувацькому з’єднанні
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
            
            # Записати повну JSON-відповідь у лог
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

    ![Paste prompt flow code.](../../../../../../translated_images/uk/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Для більш детальної інформації про використання Prompt flow у Microsoft Foundry дивіться [Prompt flow в Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Виберіть **Chat input**, **Chat output**, щоб увімкнути чат з вашою моделлю.

    ![Select Input Output.](../../../../../../translated_images/uk/select-input-output.c187fc58f25fbfc3.webp)

1. Тепер ви готові спілкуватися з вашою моделлю Phi-3 / Phi-3.5. У наступній вправі ви дізнаєтеся, як запустити Prompt flow і використати його для спілкування з тонко налаштованою моделлю Phi-3 / Phi-3.5.

> [!NOTE]
>
> Перебудований потік має виглядати, як на наведеному нижче зображенні:
>
> ![Flow example](../../../../../../translated_images/uk/graph-example.82fd1bcdd3fc545b.webp)
>

#### Запуск Prompt flow

1. Виберіть **Start compute sessions**, щоб запустити Prompt flow.

    ![Start compute session.](../../../../../../translated_images/uk/start-compute-session.9acd8cbbd2c43df1.webp)

1. Виберіть **Validate and parse input** для оновлення параметрів.

    ![Validate input.](../../../../../../translated_images/uk/validate-input.c1adb9543c6495be.webp)

1. Виберіть **Value** для **connection**, щоб вибрати власне підключення, яке ви створили. Наприклад, *connection*.

    ![Connection.](../../../../../../translated_images/uk/select-connection.1f2b59222bcaafef.webp)

#### Спілкування з тонко налаштованою моделлю Phi-3 / Phi-3.5

1. Виберіть **Chat**.

    ![Select chat.](../../../../../../translated_images/uk/select-chat.0406bd9687d0c49d.webp)

1. Ось приклад результатів: тепер ви можете спілкуватися з вашою моделлю Phi-3 / Phi-3.5. Рекомендується ставити питання на основі даних, використаних для тонкого налаштування.

    ![Chat with prompt flow.](../../../../../../translated_images/uk/chat-with-promptflow.1cf8cea112359ada.webp)

### Розгортання Azure OpenAI для оцінки моделі Phi-3 / Phi-3.5

Щоб оцінити модель Phi-3 / Phi-3.5 у Microsoft Foundry, потрібно розгорнути модель Azure OpenAI. Ця модель буде використовуватися для оцінки продуктивності Phi-3 / Phi-3.5.

#### Розгортання Azure OpenAI

1. Увійдіть до [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдіть до вашого проекту Microsoft Foundry.

    ![Select Project.](../../../../../../translated_images/uk/select-project-created.5221e0e403e2c9d6.webp)

1. У проекті виберіть **Deployments** з лівої вкладки.

1. Виберіть **+ Розгорнути модель** з меню навігації.

1. Виберіть **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/uk/deploy-openai-model.95d812346b25834b.webp)

1. Виберіть модель Azure OpenAI, яку ви хочете використовувати. Наприклад, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/uk/select-openai-model.959496d7e311546d.webp)

1. Виберіть **Підтвердити**.

### Оцінка тонко налаштованої моделі Phi-3 / Phi-3.5 за допомогою Prompt flow в Microsoft Foundry

### Початок нового оцінювання

1. Перейдіть до [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Перейдіть до вашого проекту Microsoft Foundry.

    ![Select Project.](../../../../../../translated_images/uk/select-project-created.5221e0e403e2c9d6.webp)

1. У проекті виберіть **Evaluation** з лівої вкладки.

1. Виберіть **+ Нове оцінювання** з меню навігації.

    ![Select evaluation.](../../../../../../translated_images/uk/select-evaluation.2846ad7aaaca7f4f.webp)

1. Виберіть оцінювання **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/uk/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Виконайте наступні дії:

    - Введіть ім'я оцінювання. Воно має бути унікальним.
    - Виберіть тип завдання **Питання і відповідь без контексту**. Оскільки набір даних **UlTRACHAT_200k**, використаний у цьому посібнику, не містить контексту.
    - Виберіть prompt flow, який хочете оцінити.

    ![Prompt flow evaluation.](../../../../../../translated_images/uk/evaluation-setting1.4aa08259ff7a536e.webp)

1. Виберіть **Далі**.

1. Виконайте такі дії:

    - Виберіть **Додати ваш набір даних**, щоб завантажити датасет. Наприклад, можна завантажити тестовий файл даних, як *test_data.json1*, який входить до набору **ULTRACHAT_200k**.
    - Виберіть відповідний **Стовпець датасету**, що відповідає вашому набору даних. Наприклад, для набору **ULTRACHAT_200k** виберіть **${data.prompt}** як стовпець датасету.

    ![Prompt flow evaluation.](../../../../../../translated_images/uk/evaluation-setting2.07036831ba58d64e.webp)

1. Виберіть **Далі**.

1. Виконайте ці кроки для налаштування показників продуктивності та якості:

    - Виберіть показники продуктивності і якості, які ви хочете використовувати.
    - Виберіть модель Azure OpenAI, яку ви створили для оцінювання. Наприклад, **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/uk/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Виконайте наступні кроки для налаштування показників ризику та безпеки:

    - Виберіть показники ризику і безпеки, які ви хочете використовувати.
    - Виберіть поріг для розрахунку рівня дефектів. Наприклад, **Середній**.
    - Для **питання** виберіть **Джерело даних** — **{$data.prompt}**.
    - Для **відповіді** виберіть **Джерело даних** — **{$run.outputs.answer}**.
    - Для **еталону** виберіть **Джерело даних** — **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/uk/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Виберіть **Далі**.

1. Виберіть **Надіслати**, щоб почати оцінку.

1. Оцінка займе деякий час. Ви можете відстежувати прогрес у вкладці **Evaluation**.

### Огляд результатів оцінювання

> [!NOTE]
> Наведені нижче результати призначені для ілюстрації процесу оцінювання. У цьому посібнику ми використовували модель, тонко налаштовану на відносно невеликому наборі даних, що може призвести до неоптимальних результатів. Фактичні результати можуть значно відрізнятися залежно від розміру, якості та різноманітності набору даних, а також конкретної конфігурації моделі.

Після завершення оцінювання ви можете ознайомитися з результатами як за показниками продуктивності, так і безпеки.
1. Показники продуктивності та якості:

    - оцінювання ефективності моделі у створенні послідовних, плавних і релевантних відповідей.

    ![Evaluation result.](../../../../../../translated_images/uk/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Показники ризиків і безпеки:

    - забезпечення безпечності вихідних даних моделі та їх відповідності Принципам відповідального штучного інтелекту, уникнення будь-якого шкідливого або образливого контенту.

    ![Evaluation result.](../../../../../../translated_images/uk/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Ви можете прокрутити вниз, щоб переглянути **Детальні результати показників**.

    ![Evaluation result.](../../../../../../translated_images/uk/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Оцінюючи вашу власну модель Phi-3 / Phi-3.5 за показниками продуктивності та безпеки, ви можете підтвердити, що модель не лише ефективна, але й відповідає принципам відповідального штучного інтелекту, готуючи її до реального використання.

## Вітаємо!

### Ви завершили цей навчальний посібник

Ви успішно оцінили тонко налаштовану модель Phi-3, інтегровану з Prompt flow у Microsoft Foundry. Це важливий крок у забезпеченні того, щоб ваші моделі ШІ не лише добре працювали, а й дотримувалися принципів відповідального ШІ Microsoft, допомагаючи вам створювати надійні та достовірні AI-застосунки.

![Architecture.](../../../../../../translated_images/uk/architecture.10bec55250f5d6a4.webp)

## Очищення ресурсів Azure

Очистіть свої ресурси Azure, щоб уникнути додаткових витрат на вашому рахунку. Перейдіть до порталу Azure та видаліть наступні ресурси:

- Ресурс Azure Machine learning.
- Кінцева точка моделі Azure Machine learning.
- Ресурс проекту Microsoft Foundry.
- Ресурс Prompt flow Microsoft Foundry.

### Наступні кроки

#### Документація

- [Оцінка AI-систем за допомогою панелі Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Показники оцінки та моніторингу для генеративного ІІ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Документація Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Документація Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Навчальний контент

- [Вступ до підходу Microsoft у відповідальному ШІ](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Вступ до Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Посилання

- [Що таке відповідальний ШІ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Оголошення нових інструментів Azure AI для створення більш безпечних і надійних генеративних AI-застосунків](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Оцінка застосунків генеративного ШІ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу машинного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, просимо враховувати, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->