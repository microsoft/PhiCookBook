# Процените фино подешен Phi-3 / Phi-3.5 модел у Microsoft Foundry са фокусом на Microsoft-ове принципе одговорног AI

Овај end-to-end (E2E) пример заснован је на водичу "[Оцена фино подешених Phi-3 / 3.5 модела у Microsoft Foundry са фокусом на Microsoft-ове принципе одговорног AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community.

## Преглед

### Како можете проценити безбедност и перформансе фино подешеног Phi-3 / Phi-3.5 модела у Microsoft Foundry?

Фино подешавање модела понекад може довести до непредвиђених или нежељених одговора. Да би се осигурало да модел остане безбедан и ефикасан, важно је проценити потенцијал модела да генерише штетан садржај и његову способност да пружи тачне, релевантне и кохерентне одговоре. У овом туторијалу ћете научити како проценити безбедност и перформансе фино подешеног Phi-3 / Phi-3.5 модела интегрисаног са Prompt flow у Microsoft Foundry.

Ево процеса евалуације у Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/sr/architecture.10bec55250f5d6a4.webp)

*Извор слике: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> За детаљније информације и додатне ресурсе о Phi-3 / Phi-3.5, посетите [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Предуслови

- [Python](https://www.python.org/downloads)
- [Azure претплата](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Фино подешен Phi-3 / Phi-3.5 модел

### Садржај

1. [**Сценарио 1: Увод у евалуацију Prompt flow у Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Увод у процену безбедности](#увод-у-процену-безбедности)
    - [Увод у процену перформанси](#увод-у-процену-перформанси)

1. [**Сценарио 2: Процена Phi-3 / Phi-3.5 модела у Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Пре него што почнете](#пре-него-што-почнете)
    - [Деплој Azure OpenAI за процену Phi-3 / Phi-3.5 модела](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Процените фино подешен Phi-3 / Phi-3.5 модел коришћењем евалуације Prompt flow у Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Честитамо!](#честитамо)

## **Сценарио 1: Увод у евалуацију Prompt flow у Microsoft Foundry**

### Увод у процену безбедности

Да бисте осигурали да је ваш AI модел етичан и безбедан, важно је проценити га у складу са Microsoft-овим принципима одговорног AI. У Microsoft Foundry, процена безбедности вам омогућава да процените рањивост вашег модела на jailbreak нападе и његов потенцијал за генерисање штетног садржаја, што је директно усклађено са овим принципима.

![Safaty evaluation.](../../../../../../translated_images/sr/safety-evaluation.083586ec88dfa950.webp)

*Извор слике: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft-ови принципи одговорног AI

Пре него што започнете техничке кораке, важно је разумети Microsoft-ове принципе одговорног AI, етички оквир дизајниран да усмери одговоран развој, имплементацију и рад AI система. Ови принципи воде одговоран дизајн, развој и имплементацију AI система, осигуравајући да се AI технологије развијају на правичан, транспарентан и инклузиван начин. Ови принципи су основа за процену безбедности AI модела.

Microsoft-ови принципи одговорног AI укључују:

- **Правичност и инклузивност**: AI системи треба да поступају праведно према свима и избегавају да различито утичу на слично позициониране групе људи. На пример, када AI системи пружају смернице о медицинском лечењу, кредитним пријавама или запошљавању, треба да дају исте препоруке свима који имају сличне симптоме, финансијске услове или професионалне квалификације.

- **Поузданост и безбедност**: За изградњу поверења, критично је да AI системи раде поуздано, безбедно и конзистентно. Ови системи треба да функционишу онако како су првобитно дизајнирани, безбедно реагују на непредвиђене услове и одолеју штетним манипулацијама. Начин на који се понашају и спектар услова које могу превазићи одражавају разне ситуације које су развијачи предвидели током дизајна и тестирања.

- **Транспарентност**: Када AI системи помажу у доношењу одлука које имају велики утицај на животе људи, критично је да људи схвате како су те одлуке донете. На пример, банка може користити AI систем да одлучи да ли је особа кредитно способна. Компанија може користити AI систем да утврди најприкладније кандидате за запошљавање.

- **Приватност и безбедност**: Како AI постаје све распрострањенији, заштита приватности и безбедност личних и пословних података постају важнији и комплекснији. Са AI, приватност и безбедност података захтевају посебну пажњу јер приступ подацима је кључан за тачне и информисане предикције и одлуке везане за људе.

- **Одговорност**: Особе које дизајнирају и имплементирају AI системе морају бити одговорне за начин рада својих система. Организације треба да примењују индустријске стандарде како би развиле норме одговорности. Ове норме могу осигурати да AI системи нису коначна власт у одлукама које утичу на живote људи. Такође могу обезбедити да људи задрже значајну контролу над иначе веома аутономним AI системима.

![Fill hub.](../../../../../../translated_images/sr/responsibleai2.c07ef430113fad8c.webp)

*Извор слике: [Шта је одговоран AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Да бисте сазнали више о Microsoft-овим принципима одговорног AI, посетите страницу [Шта је одговоран AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрике безбедности

У овом туторијалу проценићете безбедност фино подешеног Phi-3 модела користећи Microsoft Foundry метрике безбедности. Ове метрике помажу да се процени потенцијал модела да генерише штетан садржај и његова рањивост на jailbreak нападе. Метрике безбедности укључују:

- **Садржај везан за самоповређивање**: Процена да ли модел има тенденцију да производи садржај повезан са самоповређивањем.
- **Мржњом и неправедан садржај**: Процена да ли модел има тенденцију да производи садржај пун мржње или неправде.
- **Насилни садржај**: Процена да ли модел има тенденцију да производи насилни садржај.
- **Сексуални садржај**: Процена да ли модел има тенденцију да производи неприкладан сексуални садржај.

Процена ових аспеката осигурава да AI модел не производи штетан или увредљив садржај, у складу са друштвеним вредностима и регулаторним стандардима.

![Evaluate based on safety.](../../../../../../translated_images/sr/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Увод у процену перформанси

Да бисте осигурали да ваш AI модел ради како се очекује, важно је проценити његове перформансе у односу на метрике перформанси. У Microsoft Foundry, процене перформанси омогућавају вам да процените ефикасност вашег модела у генерисању тачних, релевантних и кохерентних одговора.

![Safaty evaluation.](../../../../../../translated_images/sr/performance-evaluation.48b3e7e01a098740.webp)

*Извор слике: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрике перформанси

У овом туторијалу проценићете перформансе фино подешеног Phi-3 / Phi-3.5 модела користећи Microsoft Foundry метрике перформанси. Ове метрике помажу да се процени ефикасност модела у генерисању тачних, релевантних и кохерентних одговора. Метрике перформанси укључују:

- **Основање на чињеницама**: Процена колико добро генерисани одговори одговарају информацијама из извора улаза.
- **Релевантност**: Процена релевантности генерисаних одговора у односу на дата питања.
- **Кохерентност**: Процена колико глатко тече генерисани текст, колико природно чита и личи на људски језик.
- **Флуентност**: Процена језичке стручности генерисаног текста.
- **GPT сличност**: Упоређује генерисани одговор са стварним подацима ради сличности.
- **F1 скор**: Израчунава однос заједничких речи између генерисаног одговора и изворних података.

Ове метрике вам помажу да процените ефикасност модела у генерисању тачних, релевантних и кохерентних одговора.

![Evaluate based on performance.](../../../../../../translated_images/sr/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Сценарио 2: Процена Phi-3 / Phi-3.5 модела у Microsoft Foundry**

### Пре него што почнете

Овај туторијал је наставак претходних блогова, "[Фино подесите и интегришите прилагођене Phi-3 моделе са Prompt Flow: Водич корак по корак](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Фино подесите и интегришите прилагођене Phi-3 моделе са Prompt Flow у Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)". У тим постовима смо прошли кроз процес фино подешавања Phi-3 / Phi-3.5 модела у Microsoft Foundry и његову интеграцију са Prompt flow.

У овом туторијалу ћете поставити Azure OpenAI модел као евалуатора у Microsoft Foundry и користити га за процену вашег фино подешеног Phi-3 / Phi-3.5 модела.

Пре него што започнете овај туторијал, уверите се да имате следеће предуслове, описане у претходним туторијалима:

1. Припремљен скуп података за процену фино подешеног Phi-3 / Phi-3.5 модела.
1. Phi-3 / Phi-3.5 модел који је фино подешен и распоређен на Azure Machine Learning.
1. Prompt flow интегрисан са вашим фино подешеним Phi-3 / Phi-3.5 моделом у Microsoft Foundry.

> [!NOTE]
> Користићете фајл *test_data.jsonl*, који се налази у фасцикли data из **ULTRACHAT_200k** скупa података преузетих у претходним блоговима, као скуп података за процену фино подешеног Phi-3 / Phi-3.5 модела.

#### Интегрисање прилагођеног Phi-3 / Phi-3.5 модела са Prompt flow у Microsoft Foundry (приступ прво кодом)

> [!NOTE]
> Ако сте пратили low-code приступ описан у "[Фино подесите и интегришите прилагођене Phi-3 моделе са Prompt Flow у Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", овај задатак можете прескочити и наставити даље.
> Међутим, ако сте користили приступ прво кодом описан у "[Фино подесите и интегришите прилагођене Phi-3 моделе са Prompt Flow: Водич корак по корак](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" за фино подешавање и распоређивање Phi-3 / Phi-3.5 модела, процес повезивања вашег модела са Prompt flow је мало другачији. Научићете овај процес у овом задатку.

Да бисте наставили, потребно је да интегришете ваш фино подешени Phi-3 / Phi-3.5 модел у Prompt flow у Microsoft Foundry.

#### Креирајте Microsoft Foundry Hub

Морате да креирате Hub пре креирања Пројекта. Hub функционише као Resource Group, омогућавајући да организујете и управљате више Пројеката унутар Microsoft Foundry.
1. Пријавите се на [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Изаберите **All hubs** са леве бочне траке.

1. Изаберите **+ New hub** из навигационог менија.

    ![Create hub.](../../../../../../translated_images/sr/create-hub.5be78fb1e21ffbf1.webp)

1. Извршите следеће задатке:

    - Унесите **Hub name**. Мора бити јединствена вредност.
    - Изаберите вашу Azure **Subscription**.
    - Изаберите **Resource group** коју желите да користите (направите нову ако је потребно).
    - Изаберите **Location** коју желите да користите.
    - Изаберите **Connect Azure AI Services** које желите да користите (направите нову ако је потребно).
    - Изаберите **Connect Azure AI Search** да бисте **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/sr/fill-hub.baaa108495c71e34.webp)

1. Изаберите **Next**.

#### Креирање Microsoft Foundry пројекта

1. У хабу који сте направили, изаберите **All projects** са леве стране.

1. Изаберите **+ New project** из навигационог менија.

    ![Select new project.](../../../../../../translated_images/sr/select-new-project.cd31c0404088d7a3.webp)

1. Унесите **Project name**. Мора бити јединствена вредност.

    ![Create project.](../../../../../../translated_images/sr/create-project.ca3b71298b90e420.webp)

1. Изаберите **Create a project**.

#### Додавање прилагођене везе за фино подешени Phi-3 / Phi-3.5 модел

Да бисте интегрисали свој прилагођени Phi-3 / Phi-3.5 модел са Prompt flow, потребно је да сачувате крајњу тачку модела и кључ у прилагођеној вези. Овај подешавање обезбеђује приступ вашем прилагођеном Phi-3 / Phi-3.5 моделу у Prompt flow.

#### Подешавање api кључа и URI крајње тачке за фино подешени Phi-3 / Phi-3.5 модел

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Идите у Azure Machine learning workspace који сте направили.

1. Изаберите **Endpoints** са леве бочне траке.

    ![Select endpoints.](../../../../../../translated_images/sr/select-endpoints.ee7387ecd68bd18d.webp)

1. Изаберите крајњу тачку коју сте креирали.

    ![Select endpoints.](../../../../../../translated_images/sr/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Изаберите **Consume** из навигационог менија.

1. Копирајте свој **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sr/copy-endpoint-key.0650c3786bd646ab.webp)

#### Додавање прилагођене везе

1. Посетите [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Идите у Microsoft Foundry пројекат који сте креирали.

1. У пројекту који сте направили, изаберите **Settings** са леве бочне траке.

1. Изаберите **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/sr/select-new-connection.fa0f35743758a74b.webp)

1. Изаберите **Custom keys** из навигационог менија.

    ![Select custom keys.](../../../../../../translated_images/sr/select-custom-keys.5a3c6b25580a9b67.webp)

1. Извршите следеће кораке:

    - Изаберите **+ Add key value pairs**.
    - За име кључа унесите **endpoint** и налепите крајњу тачку коју сте копирали из Azure ML Studio у поље вредности.
    - Поново изаберите **+ Add key value pairs**.
    - За име кључа унесите **key** и налепите кључ који сте копирали из Azure ML Studio у поље вредности.
    - Након додавања кључева, означите **is secret** да бисте спречили отворену изложеност кључа.

    ![Add connection.](../../../../../../translated_images/sr/add-connection.ac7f5faf8b10b0df.webp)

1. Изаберите **Add connection**.

#### Креирање Prompt flow

Додали сте прилагођену везу у Microsoft Foundry. Сада креирајте Prompt flow користећи следеће кораке. Затим ћете повезати овај Prompt flow са прилагођеном везом да бисте користили фино подешени модел у Prompt flow.

1. Идите у Microsoft Foundry пројекат који сте креирали.

1. Изаберите **Prompt flow** са леве бочне траке.

1. Изаберите **+ Create** из навигационог менија.

    ![Select Promptflow.](../../../../../../translated_images/sr/select-promptflow.18ff2e61ab9173eb.webp)

1. Изаберите **Chat flow** из навигационог менија.

    ![Select chat flow.](../../../../../../translated_images/sr/select-flow-type.28375125ec9996d3.webp)

1. Унесите **Folder name** који желите да користите.

    ![Select chat flow.](../../../../../../translated_images/sr/enter-name.02ddf8fb840ad430.webp)

1. Изаберите **Create**.

#### Подешавање Prompt flow за ћаскање са вашим прилагођеним Phi-3 / Phi-3.5 моделом

Потребно је интегрисати фино подешени Phi-3 / Phi-3.5 модел у Prompt flow. Међутим, постојећи Prompt flow није намењен за ову сврху. Стога морате дизајнирати Prompt flow да омогући интеграцију прилагођеног модела.

1. У Prompt flow-у извршите следеће кораке за обнову постојећег флоуа:

    - Изаберите **Raw file mode**.
    - Обришите сав постојећи код у фајлу *flow.dag.yml*.
    - Додајте следећи код у *flow.dag.yml*.

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

    - Изаберите **Save**.

    ![Select raw file mode.](../../../../../../translated_images/sr/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Додајте следећи код у *integrate_with_promptflow.py* да бисте користили прилагођени Phi-3 / Phi-3.5 модел у Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Подешавање евиденције
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

        # "connection" је име Прилагођене Везе, "endpoint", "key" су кључеви у Прилагођеној Вези
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
            
            # Евидентирајте пун JSON одговор
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

    ![Paste prompt flow code.](../../../../../../translated_images/sr/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> За детаљније информације о коришћењу Prompt flow-а у Microsoft Foundry, можете погледати [Prompt flow у Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изаберите **Chat input**, **Chat output** да бисте омогућили ћаскање са вашим моделом.

    ![Select Input Output.](../../../../../../translated_images/sr/select-input-output.c187fc58f25fbfc3.webp)

1. Сада сте спремни за ћаскање са вашим прилагођеним Phi-3 / Phi-3.5 моделом. У следећој вежби научићете како да покренете Prompt flow и користите га за ћаскање са фино подешеним Phi-3 / Phi-3.5 моделом.

> [!NOTE]
>
> Обновљени flow би требало да изгледа као на слици испод:
>
> ![Flow example](../../../../../../translated_images/sr/graph-example.82fd1bcdd3fc545b.webp)
>

#### Покретање Prompt flow

1. Изаберите **Start compute sessions** да покренете Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sr/start-compute-session.9acd8cbbd2c43df1.webp)

1. Изаберите **Validate and parse input** да обновите параметре.

    ![Validate input.](../../../../../../translated_images/sr/validate-input.c1adb9543c6495be.webp)

1. Изаберите **Value** за **connection** који води ка прилагођеној вези коју сте креирали. На пример, *connection*.

    ![Connection.](../../../../../../translated_images/sr/select-connection.1f2b59222bcaafef.webp)

#### Ћаскање са вашим прилагођеним Phi-3 / Phi-3.5 моделом

1. Изаберите **Chat**.

    ![Select chat.](../../../../../../translated_images/sr/select-chat.0406bd9687d0c49d.webp)

1. Ево примера резултата: Сада можете ћаскати са вашим прилагођеним Phi-3 / Phi-3.5 моделом. Препоручује се да постављате питања базирана на подацима коришћеним за фино подешавање.

    ![Chat with prompt flow.](../../../../../../translated_images/sr/chat-with-promptflow.1cf8cea112359ada.webp)

### Деплоy Azure OpenAI за евалуацију Phi-3 / Phi-3.5 модела

Да бисте евалуирали Phi-3 / Phi-3.5 модел у Microsoft Foundry, потребно је да деплојујете Azure OpenAI модел. Овај модел ће се користити за процену перформанси Phi-3 / Phi-3.5 модела.

#### Деплоy Azure OpenAI

1. Пријавите се на [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Идите у Microsoft Foundry пројекат који сте направили.

    ![Select Project.](../../../../../../translated_images/sr/select-project-created.5221e0e403e2c9d6.webp)

1. У пројекту који сте направили, изаберите **Deployments** са леве бочне траке.

1. Изаберите **+ Deploy model** из навигационог менија.

1. Изаберите **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/sr/deploy-openai-model.95d812346b25834b.webp)

1. Изаберите Azure OpenAI модел који желите да користите. На пример, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/sr/select-openai-model.959496d7e311546d.webp)

1. Изаберите **Confirm**.

### Евалуирање фино подешеног Phi-3 / Phi-3.5 модела користећи Microsoft Foundry-ев Prompt flow

### Започните нову евалуацију

1. Посетите [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Идите у Microsoft Foundry пројекат који сте направили.

    ![Select Project.](../../../../../../translated_images/sr/select-project-created.5221e0e403e2c9d6.webp)

1. У пројекту који сте направили, изаберите **Evaluation** са леве бочне траке.

1. Изаберите **+ New evaluation** из навигационог менија.

    ![Select evaluation.](../../../../../../translated_images/sr/select-evaluation.2846ad7aaaca7f4f.webp)

1. Изаберите **Prompt flow** евалуацију.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/sr/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Извршите следеће задатке:

    - Унесите име евалуације. Мора бити јединствено.
    - Изаберите **Question and answer without context** као тип задатка. Јер, скуп података **ULTRACHAT_200k** коришћен у овом упутству не садржи контекст.
    - Изаберите prompt flow који желите да евалуирате.

    ![Prompt flow evaluation.](../../../../../../translated_images/sr/evaluation-setting1.4aa08259ff7a536e.webp)

1. Изаберите **Next**.

1. Извршите следеће задатке:

    - Изаберите **Add your dataset** да отпремите скуп података. На пример, можете отпремити датотеку тест сета података, као што је *test_data.json1*, укључену када преузмете скуп података **ULTRACHAT_200k**.
    - Изаберите одговарајућу **Dataset column** која одговара вашем скупу података. На пример, ако користите скуп података **ULTRACHAT_200k**, изаберите **${data.prompt}** као колону сета података.

    ![Prompt flow evaluation.](../../../../../../translated_images/sr/evaluation-setting2.07036831ba58d64e.webp)

1. Изаберите **Next**.

1. Извршите следеће задатке за подешавање метрика перформанси и квалитета:

    - Изаберите метрике перформанси и квалитета које желите да користите.
    - Изаберите Azure OpenAI модел који сте креирали за евалуацију. На пример, изаберите **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sr/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Извршите следеће задатке за подешавање метрика ризика и безбедности:

    - Изаберите метрике ризика и безбедности које желите да користите.
    - Изаберите праг за израчунавање стопе дефеката који желите да користите. На пример, изаберите **Medium**.
    - За **question**, подесите **Data source** на **{$data.prompt}**.
    - За **answer**, подесите **Data source** на **{$run.outputs.answer}**.
    - За **ground_truth**, подесите **Data source** на **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sr/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Изаберите **Next**.

1. Изаберите **Submit** да започнете евалуацију.

1. Евалуација ће потрајати. Можете пратити напредак у картици **Evaluation**.

### Преглед резултата евалуације

> [!NOTE]
> Резултати приказани у наставку имају за циљ да илуструју процес евалуације. У овом упутству коришћен је модел фино подешен на релативно малом скупу података, што може довести до субоптималних резултата. Стварни резултати могу значајно варирати у зависности од величине, квалитета и разноврсности скупa података који се користи, као и специфичне конфигурације модела.

Након завршетка евалуације, можете прегледати резултате за метрике перформанси и безбедности.
1. Метричке перформанси и квалитета:

    - процените ефикасност модела у генерисању кохерентних, флуентних и релевантних одговора.

    ![Evaluation result.](../../../../../../translated_images/sr/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Метричке ризика и безбедности:

    - Осигурајте да излази модела буду безбедни и у складу са Принципима одговорне вештачке интелигенције, избегавајући било какав штетан или увредљив садржај.

    ![Evaluation result.](../../../../../../translated_images/sr/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Можете се спустити да бисте видели **Детаљан резултат метрика**.

    ![Evaluation result.](../../../../../../translated_images/sr/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Процењујући ваш прилагођени Phi-3 / Phi-3.5 модел према обе метрике перформанси и безбедности, можете потврдити да модел није само ефикасан, већ и да се придржава пракси одговорне вештачке интелигенције, чинећи га спремним за примену у стварном свету.

## Честитамо!

### Завршили сте овај туторијал

Успешно сте проценили модификовани Phi-3 модел интегрисан са Prompt flow у Microsoft Foundry. Ово је важан корак у обезбеђивању да ваши AI модели не само да добро функционишу, већ и да се придржавају Microsoft-ових принципа одговорне AI, помажући вам да изградите поуздане и веродостојне AI апликације.

![Architecture.](../../../../../../translated_images/sr/architecture.10bec55250f5d6a4.webp)

## Очистите Azure ресурсе

Очистите своје Azure ресурсе како бисте избегли додатне трошкове на свом налогу. Идите на Azure портал и обришите следеће ресурсе:

- Ресурс Azure Machine learning.
- Крајњу тачку модела Azure Machine learning.
- Ресурс Microsoft Foundry пројекта.
- Ресурс Microsoft Foundry Prompt flow.

### Следећи кораци

#### Документација

- [Процените AI системе коришћењем одговорне AI контролне табле](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Метрике процене и надзора за генеративну AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Документација Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Документација за Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Тренинг садржај

- [Увод у Microsoft-ов приступ одговорној AI](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Увод у Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Референце

- [Шта је одговорна AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Објављивање нових алата у Azure AI-у који вам помажу да изградите безбедније и поузданије генеративне AI апликације](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Процена генеративних AI апликација](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом изворном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било какве неспоразуме или погрешне тумачења која произилазе из употребе овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->