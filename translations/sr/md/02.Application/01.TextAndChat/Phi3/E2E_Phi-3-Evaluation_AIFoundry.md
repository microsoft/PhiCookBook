<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:57:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "sr"
}
-->
# Оцена фино подешеног Phi-3 / Phi-3.5 модела у Azure AI Foundry са фокусом на Microsoft-ове принципе одговорног AI

Овај крај-до-краја (E2E) пример заснован је на водичу "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" из Microsoft Tech Community.

## Преглед

### Како можете оценити безбедност и перформансе фино подешеног Phi-3 / Phi-3.5 модела у Azure AI Foundry?

Фино подешавање модела понекад може довести до нежељених или непредвиђених одговора. Да бисте осигурали да модел остане безбедан и ефикасан, важно је проценити потенцијал модела да генерише штетан садржај и његову способност да пружи тачне, релевантне и кохерентне одговоре. У овом туторијалу научићете како да оцените безбедност и перформансе фино подешеног Phi-3 / Phi-3.5 модела интегрисаног са Prompt flow у Azure AI Foundry.

Ево процеса евалуације у Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.sr.png)

*Извор слике: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> За детаљније информације и додатне ресурсе о Phi-3 / Phi-3.5, посетите [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Захтеви

- [Python](https://www.python.org/downloads)
- [Azure претплата](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Фино подешен Phi-3 / Phi-3.5 модел

### Садржај

1. [**Сценарио 1: Увод у евалуацију Prompt flow у Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Увод у евалуацију безбедности](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Увод у евалуацију перформанси](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Сценарио 2: Евалуација Phi-3 / Phi-3.5 модела у Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Пре него што почнете](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Деплој Azure OpenAI за евалуацију Phi-3 / Phi-3.5 модела](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Евалуација фино подешеног Phi-3 / Phi-3.5 модела коришћењем Prompt flow евалуације у Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Честитамо!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Сценарио 1: Увод у евалуацију Prompt flow у Azure AI Foundry**

### Увод у евалуацију безбедности

Да бисте осигурали да је ваш AI модел етичан и безбедан, кључно је да га процените у складу са Microsoft-овим принципима одговорног AI. У Azure AI Foundry, евалуације безбедности вам омогућавају да процените рањивост вашег модела на jailbreak нападе и његов потенцијал за генерисање штетног садржаја, што је у директној вези са овим принципима.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.sr.png)

*Извор слике: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft-ови принципи одговорног AI

Пре него што започнете техничке кораке, важно је разумети Microsoft-ове принципе одговорног AI, етички оквир дизајниран да води одговоран развој, имплементацију и рад AI система. Ови принципи усмеравају одговоран дизајн, развој и примену AI система, осигуравајући да су AI технологије изграђене на фер, транспарентан и инклузиван начин. Ови принципи су основа за процену безбедности AI модела.

Microsoft-ови принципи одговорног AI укључују:

- **Праведност и инклузивност**: AI системи треба да поступају праведно према свима и избегавају да различито третирају сличне групе људи. На пример, када AI системи пружају смернице о медицинском лечењу, кредитним апликацијама или запошљавању, треба да дају исте препоруке свима који имају сличне симптоме, финансијске услове или професионалне квалификације.

- **Поузданост и безбедност**: Да би се изградило поверење, критично је да AI системи раде поуздано, безбедно и доследно. Ови системи треба да функционишу онако како су првобитно дизајнирани, да безбедно реагују на непредвиђене услове и да одоле штетним манипулацијама. Њихово понашање и разноврсност услова које могу да поднесу одражавају спектар ситуација и околности које су програмери предвидели током дизајна и тестирања.

- **Транспарентност**: Када AI системи помажу у доношењу одлука које имају велики утицај на животе људи, важно је да људи разумеју како су те одлуке донете. На пример, банка може користити AI систем да одлучи да ли је неко кредитно способан. Компанија може користити AI систем да одреди најквалификованије кандидате за запошљавање.

- **Приватност и безбедност**: Како AI постаје све распрострањенији, заштита приватности и безбедност личних и пословних података постају све важнији и сложенији. Са AI, приватност и безбедност података захтевају посебну пажњу јер је приступ подацима неопходан да би AI системи могли да праве тачне и информисане предикције и одлуке о људима.

- **Одговорност**: Људи који дизајнирају и имплементирају AI системе морају бити одговорни за начин на који ти системи функционишу. Организације треба да користе индустријске стандарде за развој норми одговорности. Ове норме могу осигурати да AI системи нису коначна власт у било којој одлуци која утиче на животе људи. Такође могу осигурати да људи задрже значајну контролу над иначе високо аутономним AI системима.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.sr.png)

*Извор слике: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> За више информација о Microsoft-овим принципима одговорног AI, посетите [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Метрике безбедности

У овом туторијалу ћете оценити безбедност фино подешеног Phi-3 модела користећи метрике безбедности Azure AI Foundry. Ове метрике вам помажу да процените потенцијал модела да генерише штетан садржај и његову рањивост на jailbreak нападе. Метрике безбедности укључују:

- **Садржај повезан са самоповређивањем**: Процењује да ли модел има тенденцију да производи садржај који подстиче самоповређивање.
- **Мржњом и неправедан садржај**: Процењује да ли модел има тенденцију да производи садржај пун мржње или неправде.
- **Насилни садржај**: Процењује да ли модел има тенденцију да производи насилни садржај.
- **Сексуални садржај**: Процењује да ли модел има тенденцију да производи неприкладан сексуални садржај.

Оцењивање ових аспеката осигурава да AI модел не производи штетан или увредљив садржај, у складу са друштвеним вредностима и регулаторним стандардима.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.sr.png)

### Увод у евалуацију перформанси

Да бисте осигурали да ваш AI модел ради како се очекује, важно је да процените његове перформансе у односу на метрике перформанси. У Azure AI Foundry, евалуације перформанси вам омогућавају да процените ефикасност вашег модела у генерисању тачних, релевантних и кохерентних одговора.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.sr.png)

*Извор слике: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Метрике перформанси

У овом туторијалу ћете оценити перформансе фино подешеног Phi-3 / Phi-3.5 модела користећи метрике перформанси Azure AI Foundry. Ове метрике вам помажу да процените ефикасност модела у генерисању тачних, релевантних и кохерентних одговора. Метрике перформанси укључују:

- **Основаност (Groundedness)**: Процењује колико се генерисани одговори поклапају са информацијама из улазног извора.
- **Релевантност**: Процењује колико су генерисани одговори релевантни за постављена питања.
- **Кохерентност**: Процењује колико глатко тече генерисани текст, да ли делује природно и подсећа на људски језик.
- **Флуентност**: Процењује језичку способност генерисаног текста.
- **GPT сличност**: Упоређује генерисани одговор са стварним одговором ради мерења сличности.
- **F1 резултат**: Израчунава однос заједничких речи између генерисаног одговора и изворних података.

Ове метрике вам помажу да процените ефикасност модела у генерисању тачних, релевантних и кохерентних одговора.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.sr.png)

## **Сценарио 2: Евалуација Phi-3 / Phi-3.5 модела у Azure AI Foundry**

### Пре него што почнете

Овај туторијал је наставак претходних блог постова, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" и "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." У тим постовима смо прошли кроз процес фино подешавања Phi-3 / Phi-3.5 модела у Azure AI Foundry и његову интеграцију са Prompt flow.

У овом туторијалу ћете деплојовати Azure OpenAI модел као евалуатор у Azure AI Foundry и користити га за евалуацију вашег фино подешеног Phi-3 / Phi-3.5 модела.

Пре него што започнете овај туторијал, уверите се да имате следеће захтеве, као што је описано у претходним туторијалима:

1. Припремљен скуп података за евалуацију фино подешеног Phi-3 / Phi-3.5 модела.
1. Phi-3 / Phi-3.5 модел који је фино подешен и деплојован у Azure Machine Learning.
1. Prompt flow интегрисан са вашим фино подешеним Phi-3 / Phi-3.5 моделом у Azure AI Foundry.

> [!NOTE]
> Користићете фајл *test_data.jsonl*, који се налази у фасцикли data из **ULTRACHAT_200k** скупа података преузетог у претходним блог постовима, као скуп података за евалуацију фино подешеног Phi-3 / Phi-3.5 модела.

#### Интеграција прилагођеног Phi-3 / Phi-3.5 модела са Prompt flow у Azure AI Foundry (приступ прво кодом)
> [!NOTE]
> Ако сте пратили приступ са мало кода описан у "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", можете прескочити ову вежбу и наставити са следећом.
> Међутим, ако сте пратили приступ прво кодирање описан у "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" за фино подешавање и постављање вашег Phi-3 / Phi-3.5 модела, процес повезивања вашег модела са Prompt flow-ом је мало другачији. Овај процес ћете научити у овој вежби.
Да бисте наставили, потребно је да интегришете свој фино подешени Phi-3 / Phi-3.5 модел у Prompt flow у Azure AI Foundry.

#### Креирање Azure AI Foundry Hub-а

Пре креирања Пројекта, потребно је да направите Hub. Hub функционише као Resource Group, омогућавајући вам да организујете и управљате више Пројеката унутар Azure AI Foundry.

1. Пријавите се на [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Изаберите **All hubs** са леве стране.

1. Изаберите **+ New hub** из навигационог менија.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.sr.png)

1. Извршите следеће кораке:

    - Унесите **Hub name**. Мора бити јединствена вредност.
    - Изаберите своју Azure **Subscription**.
    - Изаберите **Resource group** коју желите да користите (направите нову ако је потребно).
    - Изаберите **Location** коју желите да користите.
    - Изаберите **Connect Azure AI Services** које желите да користите (направите нову ако је потребно).
    - Изаберите **Connect Azure AI Search** и одаберите **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.sr.png)

1. Изаберите **Next**.

#### Креирање Azure AI Foundry Пројекта

1. У Hub-у који сте креирали, изаберите **All projects** са леве стране.

1. Изаберите **+ New project** из навигационог менија.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.sr.png)

1. Унесите **Project name**. Мора бити јединствена вредност.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.sr.png)

1. Изаберите **Create a project**.

#### Додавање прилагођене везе за фино подешени Phi-3 / Phi-3.5 модел

Да бисте интегрисали свој прилагођени Phi-3 / Phi-3.5 модел са Prompt flow, потребно је да сачувате endpoint и key модела у прилагођеној вези. Овај подешавање омогућава приступ вашем прилагођеном Phi-3 / Phi-3.5 моделу у Prompt flow.

#### Подешавање api key и endpoint uri фино подешеног Phi-3 / Phi-3.5 модела

1. Посетите [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Идите у Azure Machine learning workspace који сте креирали.

1. Изаберите **Endpoints** са леве стране.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.sr.png)

1. Изаберите endpoint који сте креирали.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.sr.png)

1. Изаберите **Consume** из навигационог менија.

1. Копирајте свој **REST endpoint** и **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.sr.png)

#### Додавање прилагођене везе

1. Посетите [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Идите у Azure AI Foundry пројекат који сте креирали.

1. У пројекту који сте креирали, изаберите **Settings** са леве стране.

1. Изаберите **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.sr.png)

1. Изаберите **Custom keys** из навигационог менија.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.sr.png)

1. Извршите следеће кораке:

    - Изаберите **+ Add key value pairs**.
    - За име кључа унесите **endpoint** и налепите endpoint који сте копирали из Azure ML Studio у поље за вредност.
    - Поново изаберите **+ Add key value pairs**.
    - За име кључа унесите **key** и налепите key који сте копирали из Azure ML Studio у поље за вредност.
    - Након додавања кључева, означите **is secret** да бисте спречили да кључ буде изложен.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.sr.png)

1. Изаберите **Add connection**.

#### Креирање Prompt flow

Додали сте прилагођену везу у Azure AI Foundry. Сада ћемо креирати Prompt flow пратећи следеће кораке. Након тога ћете повезати овај Prompt flow са прилагођеном везом како бисте користили фино подешени модел унутар Prompt flow-а.

1. Идите у Azure AI Foundry пројекат који сте креирали.

1. Изаберите **Prompt flow** са леве стране.

1. Изаберите **+ Create** из навигационог менија.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.sr.png)

1. Изаберите **Chat flow** из навигационог менија.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.sr.png)

1. Унесите **Folder name** који желите да користите.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.sr.png)

1. Изаберите **Create**.

#### Подешавање Prompt flow за разговор са вашим прилагођеним Phi-3 / Phi-3.5 моделом

Потребно је да интегришете фино подешени Phi-3 / Phi-3.5 модел у Prompt flow. Међутим, постојећи Prompt flow није дизајниран за ову сврху. Због тога морате редизајнирати Prompt flow како бисте омогућили интеграцију прилагођеног модела.

1. У Prompt flow-у извршите следеће кораке да бисте обновили постојећи flow:

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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.sr.png)

1. Додајте следећи код у *integrate_with_promptflow.py* да бисте користили прилагођени Phi-3 / Phi-3.5 модел у Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.sr.png)

> [!NOTE]
> За детаљније информације о коришћењу Prompt flow у Azure AI Foundry, можете погледати [Prompt flow у Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Изаберите **Chat input**, **Chat output** да бисте омогућили разговор са вашим моделом.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.sr.png)

1. Сада сте спремни да разговарате са својим прилагођеним Phi-3 / Phi-3.5 моделом. У следећој вежби ћете научити како да покренете Prompt flow и користите га за разговор са фино подешеним Phi-3 / Phi-3.5 моделом.

> [!NOTE]
>
> Обновљени flow треба да изгледа као на слици испод:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.sr.png)
>

#### Покретање Prompt flow-а

1. Изаберите **Start compute sessions** да бисте покренули Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.sr.png)

1. Изаберите **Validate and parse input** да бисте обновили параметре.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.sr.png)

1. Изаберите **Value** за **connection** која води ка прилагођеној вези коју сте креирали. На пример, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.sr.png)

#### Разговор са вашим прилагођеним Phi-3 / Phi-3.5 моделом

1. Изаберите **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.sr.png)

1. Ево примера резултата: Сада можете разговарати са својим прилагођеним Phi-3 / Phi-3.5 моделом. Препоручује се да постављате питања везана за податке који су коришћени за фино подешавање.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.sr.png)

### Деплој Azure OpenAI за евалуацију Phi-3 / Phi-3.5 модела

Да бисте евалуирали Phi-3 / Phi-3.5 модел у Azure AI Foundry, потребно је да деплојујете Azure OpenAI модел. Овај модел ће се користити за процену перформанси Phi-3 / Phi-3.5 модела.

#### Деплој Azure OpenAI

1. Пријавите се на [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Идите у Azure AI Foundry пројекат који сте креирали.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.sr.png)

1. У пројекту који сте креирали, изаберите **Deployments** са леве стране.

1. Изаберите **+ Deploy model** из навигационог менија.

1. Изаберите **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.sr.png)

1. Изаберите Azure OpenAI модел који желите да користите. На пример, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.sr.png)

1. Изаберите **Confirm**.

### Евалуација фино подешеног Phi-3 / Phi-3.5 модела коришћењем Prompt flow евалуације у Azure AI Foundry

### Покретање нове евалуације

1. Посетите [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Идите у Azure AI Foundry пројекат који сте креирали.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.sr.png)

1. У пројекту који сте креирали, изаберите **Evaluation** са леве стране.

1. Изаберите **+ New evaluation** из навигационог менија.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.sr.png)

1. Изаберите **Prompt flow** евалуацију.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.sr.png)

1. Извршите следеће кораке:

    - Унесите име евалуације. Мора бити јединствено.
    - Изаберите **Question and answer without context** као тип задатка. Јер, **ULTRACHAT_200k** скуп података коришћен у овом туторијалу не садржи контекст.
    - Изаберите prompt flow који желите да евалуирате.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.sr.png)

1. Изаберите **Next**.

1. Извршите следеће кораке:

    - Изаберите **Add your dataset** да отпремите скуп података. На пример, можете отпремити тест скуп података, као што је *test_data.json1*, који је укључен када преузмете **ULTRACHAT_200k** скуп података.
    - Изаберите одговарајућу **Dataset column** која одговара вашем скупу података. На пример, ако користите **ULTRACHAT_200k** скуп података, изаберите **${data.prompt}** као колону скупа података.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.sr.png)

1. Изаберите **Next**.

1. Извршите следеће кораке за подешавање метрика перформанси и квалитета:

    - Изаберите метрике перформанси и квалитета које желите да користите.
    - Изаберите Azure OpenAI модел који сте креирали за евалуацију. На пример, изаберите **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.sr.png)

1. Извршите следеће кораке за подешавање метрика ризика и безбедности:

    - Изаберите метрике ризика и безбедности које желите да користите.
    - Изаберите праг за израчунавање стопе дефеката који желите да користите. На пример, изаберите **Medium**.
    - За **question**, изаберите **Data source** као **{$data.prompt}**.
    - За **answer**, изаберите **Data source** као **{$run.outputs.answer}**.
    - За **ground_truth**, изаберите **Data source** као **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.sr.png)

1. Изаберите **Next**.

1. Изаберите **Submit** да покренете евалуацију.

1. Евалуација ће потрајати неко време. Можете пратити напредак у табу **Evaluation**.

### Преглед резултата евалуације
> [!NOTE]
> Резултати приказани у наставку служе као илустрација процеса процене. У овом туторијалу користили смо модел који је фино подешен на релативно малом скупу података, што може довести до мање оптималних резултата. Стварни резултати могу значајно варирати у зависности од величине, квалитета и разноликости коришћеног скупа података, као и од специфичне конфигурације модела.
Када се процена заврши, можете прегледати резултате за метрике перформанси и безбедности.

1. Метрике перформанси и квалитета:

    - процените ефикасност модела у генерисању кохерентних, течно и релевантних одговора.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.sr.png)

1. Метрике ризика и безбедности:

    - Осигурајте да излази модела буду безбедни и у складу са Responsible AI Principles, избегавајући било какав штетан или увредљив садржај.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.sr.png)

1. Можете скроловати надоле да бисте видели **Детаљне резултате метрика**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.sr.png)

1. Процењујући свој прилагођени Phi-3 / Phi-3.5 модел према метрикама перформанси и безбедности, можете потврдити да модел није само ефикасан, већ и да поштује одговорне праксе у вези са вештачком интелигенцијом, чинећи га спремним за примену у стварном свету.

## Честитамо!

### Завршили сте овај туторијал

Успешно сте проценили фино подешени Phi-3 модел интегрисан са Prompt flow у Azure AI Foundry. Ово је важан корак у осигуравању да ваши AI модели не само да добро раде, већ и да поштују Microsoft-ове принципе Responsible AI, помажући вам да изградите поуздане и сигурне AI апликације.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.sr.png)

## Чишћење Azure ресурса

Очистите своје Azure ресурсе како бисте избегли додатне трошкове на свом налогу. Идите на Azure портал и избришите следеће ресурсе:

- Azure Machine learning ресурс.
- Azure Machine learning модел endpoint.
- Azure AI Foundry Project ресурс.
- Azure AI Foundry Prompt flow ресурс.

### Следећи кораци

#### Документација

- [Оцена AI система коришћењем Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Метрике процене и праћења за генеративни AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry документација](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow документација](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Обука

- [Увод у Microsoft-ов приступ Responsible AI](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Увод у Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Референце

- [Шта је Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Објављени нови алати у Azure AI који вам помажу да изградите безбедније и поузданије генеративне AI апликације](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Процена генеративних AI апликација](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.