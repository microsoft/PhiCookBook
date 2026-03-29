# Tathmini ya Mfano uliobinafsishwa wa Phi-3 / Phi-3.5 katika Microsoft Foundry ukiangazia Kanuni za AI Zinazowajibika za Microsoft

Mfano huu wa mwisho hadi mwisho (E2E) unatokana na mwongozo "[Tathmini ya Modeli zilizobinafsishwa za Phi-3 / 3.5 katika Microsoft Foundry ukiangazia AI inayowajibika ya Microsoft](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" kutoka Microsoft Tech Community.

## Muhtasari

### Unawezaje kutathmini usalama na utendaji wa mfano uliobinafsishwa wa Phi-3 / Phi-3.5 katika Microsoft Foundry?

Kusawazisha mfano kunaweza wakati mwingine kusababisha majibu yasiyotakiwa au yasiyotarajiwa. Ili kuhakikisha kuwa mfano unabaki salama na mzuri, ni muhimu kutathmini uwezo wa mfano kutoa maudhui hatarishi na uwezo wake wa kutoa majibu sahihi, yanayohusiana, na yenye uthabiti. Katika mafunzo haya, utajifunza jinsi ya kutathmini usalama na utendaji wa mfano uliobinafsishwa wa Phi-3 / Phi-3.5 uliounganishwa na Prompt flow katika Microsoft Foundry.

Hapa kuna mchakato wa tathmini wa Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/sw/architecture.10bec55250f5d6a4.webp)

*Chanzo cha Picha: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Kwa taarifa za kina zaidi na kuchunguza rasilimali za ziada kuhusu Phi-3 / Phi-3.5, tafadhali tembelea [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Mahitaji ya Awali

- [Python](https://www.python.org/downloads)
- [Usajili wa Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Mfano uliobinafsishwa wa Phi-3 / Phi-3.5

### Jedwali la Yaliyomo

1. [**Kitendo 1: Utangulizi wa tathmini ya Prompt flow ya Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Utangulizi wa tathmini ya usalama](#utangulizi-wa-tathmini-ya-usalama)
    - [Utangulizi wa tathmini ya utendaji](#utangulizi-wa-tathmini-ya-utendaji)

1. [**Kitendo 2: Kutathmini mfano wa Phi-3 / Phi-3.5 katika Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Kabla ya kuanza](#kabla-ya-kuanza)
    - [Tangaza Azure OpenAI kutathmini mfano wa Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Tathmini mfano uliobinafsishwa wa Phi-3 / Phi-3.5 ukitumia tathmini ya Prompt flow ya Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Hongera!](#hongera)

## **Kitendo 1: Utangulizi wa tathmini ya Prompt flow ya Microsoft Foundry**

### Utangulizi wa tathmini ya usalama

Ili kuhakikisha mfano wako wa AI ni wa kimaadili na salama, ni muhimu kutathmini dhidi ya Kanuni za AI Zinazowajibika za Microsoft. Katika Microsoft Foundry, tathmini za usalama zinakuwezesha kutathmini udhaifu wa mfano wako dhidi ya mashambulizi ya jailbreak na uwezekano wake wa kutoa maudhui hatarishi, jambo ambalo linaendana moja kwa moja na kanuni hizi.

![Safaty evaluation.](../../../../../../translated_images/sw/safety-evaluation.083586ec88dfa950.webp)

*Chanzo cha Picha: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Kanuni za AI Zinazowajibika za Microsoft

Kabla ya kuanza hatua za kiufundi, ni muhimu kuelewa Kanuni za AI Zinazowajibika za Microsoft, mfumo wa maadili ulioundwa kuongoza maendeleo, utoaji huduma, na uendeshaji wa mifumo ya AI kwa uwajibikaji. Kanuni hizi huongoza muundo, maendeleo, na utoaji huduma wa mifumo ya AI kwa njia inayowajibika, kuhakikisha teknolojia za AI zinajengwa kwa njia ya haki, uwazi, na ujumuishaji. Kanuni hizi ni misingi ya kutathmini usalama wa mifano ya AI.

Kanuni za AI Zinazowajibika za Microsoft ni pamoja na:

- **Haki na Ujumuishaji**: Mifumo ya AI inapaswa kutendea watu wote haki na kuepuka kuathiri makundi yenye hali sawa kwa njia tofauti. Kwa mfano, wakati mifumo ya AI inatoa mwongozo juu ya matibabu ya afya, maombi ya mkopo, au ajira, inapaswa kutoa mapendekezo sawa kwa kila mtu mwenye dalili sawa, hali ya kifedha, au sifa za kitaaluma.

- **Uaminifu na Usalama**: Ili kujenga uaminifu, ni muhimu mifumo ya AI ifanye kazi kwa kuaminika, salama, na kwa uthabiti. Mifumo hii inapaswa kuweza kufanya kazi kama ilivyokusudiwa awali, kujibu kwa usalama hali zisizotarajiwa, na kuzuia udanganyifu hatari. Tabia na hali mbalimbali zinazoweza kushughulikiwa zinaakisi aina ya mazingira na hali zilizoangaliwa na waendelezaji wakati wa muundo na majaribio.

- **Uwazi**: Wakati mifumo ya AI inasaidia kuamua maamuzi yenye athari kubwa kwa maisha ya watu, ni muhimu watu kuelewa jinsi maamuzi hayo yalivyofanywa. Kwa mfano, benki inaweza kutumia mfumo wa AI kuamua utayari wa mkopo wa mtu. Kampuni inaweza kutumia mfumo wa AI kuamua wagombea bora wa ajira.

- **Faragha na Usalama**: Kadiri AI inavyoenea zaidi, kulinda faragha na usalama wa taarifa binafsi na biashara kunakuwa muhimu na changamoto zaidi. Kwa AI, faragha na usalama wa data vinahitaji umakini mkubwa kwa sababu ufikiaji wa data ni muhimu kwa mifumo ya AI kutoa utabiri sahihi na maamuzi ya watu.

- **Uwajibikaji**: Watu wanaotengeneza na kutoa mifumo ya AI wanapaswa kuwajibika kwa jinsi mifumo yao inavyofanya kazi. Mashirika yanapaswa kutumia viwango vya sekta kuendeleza kanuni za uwajibikaji. Kanuni hizi zinaweza kuhakikisha kwamba mifumo ya AI si mamlaka ya mwisho juu ya maamuzi yanayoathiri maisha ya watu. Pia zinaweza kuhakikisha kuwa binadamu wanabaki na udhibiti unaofaa juu ya mifumo ya AI yenye uhuru mkubwa.

![Fill hub.](../../../../../../translated_images/sw/responsibleai2.c07ef430113fad8c.webp)

*Chanzo cha Picha: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Ili kujifunza zaidi kuhusu Kanuni za AI Zinazowajibika za Microsoft, tembelea [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Vipimo vya usalama

Katika mafunzo haya, utapima usalama wa mfano uliobinafsishwa wa Phi-3 ukitumia vipimo vya usalama vya Microsoft Foundry. Vipimo hivi hukusaidia kutathmini uwezo wa mfano kutoa maudhui hatarishi na udhaifu wake dhidi ya mashambulizi ya jailbreak. Vipimo vya usalama ni pamoja na:

- **Maudhui yanayohusiana na kujidhuru binafsi**: Hupima kama mfano una mwelekeo wa kutoa maudhui yanayohusiana na kujidhuru binafsi.
- **Maudhui ya Uadui na Hayahakiki**: Hupima kama mfano una mwelekeo wa kutoa maudhui ya uadui au ambayo si haki.
- **Maudhui ya Vurugu**: Hupima kama mfano una mwelekeo wa kutoa maudhui ya vurugu.
- **Maudhui ya Ngono**: Hupima kama mfano una mwelekeo wa kutoa maudhui ya ngono yasiyotakiwa.

Kutathmini vipengele hivi kunahakikisha kuwa mfano wa AI hauzalishi maudhui hatarishi au ya kuudhi, na kuendana na maadili ya jamii na viwango vya udhibiti.

![Evaluate based on safety.](../../../../../../translated_images/sw/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Utangulizi wa tathmini ya utendaji

Ili kuhakikisha kuwa mfano wako wa AI unaendeshwa kama inavyotarajiwa, ni muhimu kutathmini utendaji wake dhidi ya vipimo vya utendaji. Katika Microsoft Foundry, tathmini za utendaji zinakuwezesha kutathmini ufanisi wa mfano wako katika kutoa majibu sahihi, yanayohusiana, na yenye uthabiti.

![Safaty evaluation.](../../../../../../translated_images/sw/performance-evaluation.48b3e7e01a098740.webp)

*Chanzo cha Picha: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Vipimo vya utendaji

Katika mafunzo haya, utapima utendaji wa mfano uliobinafsishwa wa Phi-3 / Phi-3.5 ukitumia vipimo vya utendaji vya Microsoft Foundry. Vipimo hivi hukusaidia kutathmini ufanisi wa mfano katika kutoa majibu sahihi, yanayohusiana, na yenye uthabiti. Vipimo vya utendaji ni pamoja na:

- **Uthibitisho**: Tathmini jinsi majibu yaliyotolewa yanavyolingana na taarifa kutoka chanzo cha kuingia.
- **Uhusiano**: Hupima umuhimu wa majibu yaliyotolewa kwa maswali yaliyotolewa.
- **Uthabiti**: Tathmini jinsi maandishi yaliyotolewa yanavyopita kwa mpangilio mzuri, kusomeka kwa asili, na kufanana na lugha ya binadamu.
- **Umahiri wa Lugha**: Tathmini ufanisi wa lugha katika maandishi yaliyotolewa.
- **Ulinganifu na GPT**: Linganisha jibu lililotolewa na ukweli wa msingi kwa kufanana.
- **Alama ya F1**: Hesabu uwiano wa maneno yanayoshirikiana kati ya jibu lililotolewa na data ya chanzo.

Vipimo hivi hukusaidia kutathmini ufanisi wa mfano katika kutoa majibu sahihi, yanayohusiana, na yenye uthabiti.

![Evaluate based on performance.](../../../../../../translated_images/sw/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Kitendo 2: Kutathmini mfano wa Phi-3 / Phi-3.5 katika Microsoft Foundry**

### Kabla ya kuanza

Mafunzo haya ni muendelezo wa machapisho yaliyotangulia, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" na "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Katika machapisho haya, tulipitia mchakato wa kubinafsisha mfano wa Phi-3 / Phi-3.5 katika Microsoft Foundry na kuunganisha na Prompt flow.

Katika mafunzo haya, utatangaza mfano wa Azure OpenAI kama mtathmini katika Microsoft Foundry na kulitumia kutathmini mfano wako uliobinafsishwa wa Phi-3 / Phi-3.5.

Kabla haujaanza mafunzo haya, hakikisha una mahitaji yafuatayo, kama ilivyoelezwa katika mafunzo yaliyopita:

1. Dataseti iliyotayarishwa kutathmini mfano uliobinafsishwa wa Phi-3 / Phi-3.5.
1. Mfano wa Phi-3 / Phi-3.5 uliobinafsishwa na kutangazwa katika Azure Machine Learning.
1. Prompt flow iliyounganishwa na mfano uliobinafsishwa wa Phi-3 / Phi-3.5 katika Microsoft Foundry.

> [!NOTE]
> Utatumia faili *test_data.jsonl*, iliyoko katika folda ya data kutoka dataseti ya **ULTRACHAT_200k** iliyopakuliwa katika machapisho yaliyopita ya blogu, kama dataseti ya kutathmini mfano uliobinafsishwa wa Phi-3 / Phi-3.5.

#### Unganisha mfano wa Phi-3 / Phi-3.5 uliobinafsishwa na Prompt flow katika Microsoft Foundry (Njia ya kwanza kutumia msimbo)

> [!NOTE]
> Ikiwa ulifuata njia ya msimbo mdogo iliyotajwa katika "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", unaweza kuruka zoezi hili na kuendelea kwenye linalofuata.
> Hata hivyo, ikiwa ulifuata njia ya kwanza kutumia msimbo uliotajwa katika "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" kubinafsisha na kutangaza mfano wako wa Phi-3 / Phi-3.5, mchakato wa kuunganisha mfano wako na Prompt flow ni tofauti kidogo. Utajifunza mchakato huu katika zoezi hili.

Ili kuendelea, unahitaji kuunganisha mfano wako uliobinafsishwa wa Phi-3 / Phi-3.5 katika Prompt flow katika Microsoft Foundry.

#### Unda Microsoft Foundry Hub

Unahitaji kuunda Hub kabla ya kuunda Mradi (Project). Hub hufanya kazi kama Resource Group, ikikuruhusu kupanga na kusimamia Miradi mingi ndani ya Microsoft Foundry.
1. Ingia kwenye [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Chagua **All hubs** kutoka kwenye kidirisha cha upande wa kushoto.

1. Chagua **+ New hub** kutoka kwenye menyu ya urambazaji.

    ![Create hub.](../../../../../../translated_images/sw/create-hub.5be78fb1e21ffbf1.webp)

1. Fanya kazi zifuatazo:

    - Ingiza **Hub name**. Lazima iwe thamani ya kipekee.
    - Chagua Akaunti yako ya Azure **Subscription**.
    - Chagua **Resource group** utakayotumia (unda mpya ikiwa inahitajika).
    - Chagua **Location** unayotaka kutumia.
    - Chagua **Connect Azure AI Services** utakazotumia (unda mpya ikiwa inahitajika).
    - Chagua **Connect Azure AI Search** ili **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/sw/fill-hub.baaa108495c71e34.webp)

1. Chagua **Next**.

#### Unda Mradi wa Microsoft Foundry

1. Katika Hub uliounda, chagua **All projects** kutoka kwenye kidirisha cha upande wa kushoto.

1. Chagua **+ New project** kutoka kwenye menyu ya urambazaji.

    ![Select new project.](../../../../../../translated_images/sw/select-new-project.cd31c0404088d7a3.webp)

1. Ingiza **Project name**. Lazima iwe thamani ya kipekee.

    ![Create project.](../../../../../../translated_images/sw/create-project.ca3b71298b90e420.webp)

1. Chagua **Create a project**.

#### Ongeza muunganisho maalum kwa mfano uliobinafsishwa wa Phi-3 / Phi-3.5

Ili kuunganisha mfano wako maalum wa Phi-3 / Phi-3.5 na Prompt flow, unahitaji kuhifadhi kiungo na ufunguo wa mfano kwenye muunganisho maalum. Mpangilio huu unahakikisha upatikanaji wa mfano wako maalum wa Phi-3 / Phi-3.5 ndani ya Prompt flow.

#### Weka api key na endpoint uri ya mfano uliobinafsishwa wa Phi-3 / Phi-3.5

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Elekea kwenye eneo la kazi la Azure Machine learning ulilounda.

1. Chagua **Endpoints** kutoka kwenye kidirisha cha upande wa kushoto.

    ![Select endpoints.](../../../../../../translated_images/sw/select-endpoints.ee7387ecd68bd18d.webp)

1. Chagua kiungo (endpoint) ulichochagua.

    ![Select endpoints.](../../../../../../translated_images/sw/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Chagua **Consume** kutoka kwenye menyu ya urambazaji.

1. Nakili **REST endpoint** yako na **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sw/copy-endpoint-key.0650c3786bd646ab.webp)

#### Ongeza Muunganisho Maalum

1. Tembelea [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Elekea kwenye mradi wa Microsoft Foundry uliounda.

1. Katika Mradi uliounda, chagua **Settings** kutoka kwenye kidirisha cha upande wa kushoto.

1. Chagua **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/sw/select-new-connection.fa0f35743758a74b.webp)

1. Chagua **Custom keys** kutoka kwenye menyu ya urambazaji.

    ![Select custom keys.](../../../../../../translated_images/sw/select-custom-keys.5a3c6b25580a9b67.webp)

1. Fanya kazi zifuatazo:

    - Chagua **+ Add key value pairs**.
    - Kwa jina la ufunguo, ingiza **endpoint** na bandika kiungo ulichonakili kutoka Azure ML Studio kwenye sehemu ya thamani.
    - Chagua tena **+ Add key value pairs**.
    - Kwa jina la ufunguo, ingiza **key** na bandika ufunguo ulichonakili kutoka Azure ML Studio kwenye sehemu ya thamani.
    - Baada ya kuongeza funguo, chagua **is secret** ili kuzuia ufunguo kuonekana wazi.

    ![Add connection.](../../../../../../translated_images/sw/add-connection.ac7f5faf8b10b0df.webp)

1. Chagua **Add connection**.

#### Unda Prompt flow

Umeongeza muunganisho maalum katika Microsoft Foundry. Sasa, hebu tuunde Prompt flow kwa kutumia hatua zifuatazo. Kisha, utahusisha Prompt flow hii na muunganisho maalum ili kutumia mfano uliobinafsishwa ndani ya Prompt flow.

1. Elekea kwenye mradi wa Microsoft Foundry uliounda.

1. Chagua **Prompt flow** kutoka kwenye kidirisha cha upande wa kushoto.

1. Chagua **+ Create** kutoka kwenye menyu ya urambazaji.

    ![Select Promptflow.](../../../../../../translated_images/sw/select-promptflow.18ff2e61ab9173eb.webp)

1. Chagua **Chat flow** kutoka kwenye menyu ya urambazaji.

    ![Select chat flow.](../../../../../../translated_images/sw/select-flow-type.28375125ec9996d3.webp)

1. Ingiza **Folder name** utakayotumia.

    ![Select chat flow.](../../../../../../translated_images/sw/enter-name.02ddf8fb840ad430.webp)

1. Chagua **Create**.

#### Sanidi Prompt flow kuzungumza na mfano wako maalum wa Phi-3 / Phi-3.5

Unahitaji kuingiza mfano uliobinafsishwa wa Phi-3 / Phi-3.5 katika Prompt flow. Hata hivyo, Prompt flow iliyopo haina muundo wa kutosha kwa madhumuni haya. Kwa hiyo, lazima ubadilishe Prompt flow ili kuwezesha kuingiza mfano maalum.

1. Katika Prompt flow, fanya kazi zifuatazo kujenga upya mtiririko uliopo:

    - Chagua **Raw file mode**.
    - Futa msimbo wote uliopo katika faili ya *flow.dag.yml*.
    - Ongeza msimbo ufuatao kwenye *flow.dag.yml*.

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

    - Chagua **Save**.

    ![Select raw file mode.](../../../../../../translated_images/sw/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Ongeza msimbo ufuatao kwenye *integrate_with_promptflow.py* kuitumia mfano maalum wa Phi-3 / Phi-3.5 ndani ya Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Usanidi wa uingizaji kumbukumbu
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

        # "connection" ni jina la Muunganisho Maalum, "endpoint", "key" ni vifunguo katika Muunganisho Maalum
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
            
            # Ingiza kumbukumbu jibu kamili la JSON
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

    ![Paste prompt flow code.](../../../../../../translated_images/sw/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Kwa maelezo ya kina zaidi juu ya matumizi ya Prompt flow katika Microsoft Foundry, unaweza rejelea [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chagua **Chat input**, **Chat output** kuwezesha mazungumzo na mfano wako.

    ![Select Input Output.](../../../../../../translated_images/sw/select-input-output.c187fc58f25fbfc3.webp)

1. Sasa uko tayari kuzungumza na mfano maalum wa Phi-3 / Phi-3.5. Katika zoezi lijalo, utajifunza jinsi ya kuanzisha Prompt flow na kuitumia kuzungumza na mfano wako uliobinafsishwa wa Phi-3 / Phi-3.5.

> [!NOTE]
>
> Mtiririko uliobuniwa upya unapaswa kuonekana kama picha hapo chini:
>
> ![Flow example](../../../../../../translated_images/sw/graph-example.82fd1bcdd3fc545b.webp)
>

#### Anzisha Prompt flow

1. Chagua **Start compute sessions** kuanzisha Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sw/start-compute-session.9acd8cbbd2c43df1.webp)

1. Chagua **Validate and parse input** ili kufufua vigezo.

    ![Validate input.](../../../../../../translated_images/sw/validate-input.c1adb9543c6495be.webp)

1. Chagua **Value** ya **connection** kwa muunganisho maalum uliounda. Kwa mfano, *connection*.

    ![Connection.](../../../../../../translated_images/sw/select-connection.1f2b59222bcaafef.webp)

#### Zungumza na mfano wako maalum wa Phi-3 / Phi-3.5

1. Chagua **Chat**.

    ![Select chat.](../../../../../../translated_images/sw/select-chat.0406bd9687d0c49d.webp)

1. Hapa ni mfano wa matokeo: Sasa unaweza kuzungumza na mfano wako maalum wa Phi-3 / Phi-3.5. Inashauriwa kuuliza maswali yanayotegemea data iliyotumika kwa kufinyangwa.

    ![Chat with prompt flow.](../../../../../../translated_images/sw/chat-with-promptflow.1cf8cea112359ada.webp)

### Sambaza (Deploy) Azure OpenAI ili kutathmini mfano wa Phi-3 / Phi-3.5

Ili kutathmini mfano wa Phi-3 / Phi-3.5 katika Microsoft Foundry, unahitaji kusambaza mfano wa Azure OpenAI. Mfano huu utatumika kutathmini utendaji wa mfano wa Phi-3 / Phi-3.5.

#### Sambaza Azure OpenAI

1. Ingia kwenye [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Elekea kwenye mradi wa Microsoft Foundry uliounda.

    ![Select Project.](../../../../../../translated_images/sw/select-project-created.5221e0e403e2c9d6.webp)

1. Katika Mradi uliounda, chagua **Deployments** kutoka kwenye kidirisha cha upande wa kushoto.

1. Chagua **+ Deploy model** kutoka kwenye menyu ya urambazaji.

1. Chagua **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/sw/deploy-openai-model.95d812346b25834b.webp)

1. Chagua mfano wa Azure OpenAI utakayotaka kutumia. Kwa mfano, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/sw/select-openai-model.959496d7e311546d.webp)

1. Chagua **Confirm**.

### Tathmini mfano uliobinafsishwa wa Phi-3 / Phi-3.5 kwa kutumia tathmini ya Prompt flow ya Microsoft Foundry

### Anzisha tathmini mpya

1. Tembelea [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Elekea kwenye mradi wa Microsoft Foundry uliounda.

    ![Select Project.](../../../../../../translated_images/sw/select-project-created.5221e0e403e2c9d6.webp)

1. Katika Mradi uliounda, chagua **Evaluation** kutoka kwenye kidirisha cha upande wa kushoto.

1. Chagua **+ New evaluation** kutoka kwenye menyu ya urambazaji.

    ![Select evaluation.](../../../../../../translated_images/sw/select-evaluation.2846ad7aaaca7f4f.webp)

1. Chagua tathmini ya **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/sw/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Fanya kazi zifuatazo:

    - Ingiza jina la tathmini. Lazima iwe thamani ya kipekee.
    - Chagua **Question and answer without context** kama aina ya kazi. Kwa sababu, dataset ya **UlTRACHAT_200k** inayotumika katika mafunzo haya haina muktadha.
    - Chagua prompt flow utakayotaka kutathmini.

    ![Prompt flow evaluation.](../../../../../../translated_images/sw/evaluation-setting1.4aa08259ff7a536e.webp)

1. Chagua **Next**.

1. Fanya kazi zifuatazo:

    - Chagua **Add your dataset** kuingiza dataset. Kwa mfano, unaweza kupakia faili la dataset ya majaribio, kama vile *test_data.json1*, ambalo linaambatana unakapopakua dataset ya **ULTRACHAT_200k**.
    - Chagua safu inayofaa ya **Dataset column** inayolingana na dataset yako. Kwa mfano, ikiwa unatumia dataset ya **ULTRACHAT_200k**, chagua **${data.prompt}** kama safu ya dataset.

    ![Prompt flow evaluation.](../../../../../../translated_images/sw/evaluation-setting2.07036831ba58d64e.webp)

1. Chagua **Next**.

1. Fanya kazi zifuatazo kuandaa vigezo vya utendaji na ubora:

    - Chagua viashiria vya utendaji na ubora unavyotaka kutumia.
    - Chagua mfano wa Azure OpenAI ulioanzisha kwa tathmini. Kwa mfano, chagua **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sw/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Fanya kazi zifuatazo kuandaa vigezo vya hatari na usalama:

    - Chagua vigezo vya hatari na usalama unavyotaka kutumia.
    - Chagua kikomo cha kuhesabu kiwango cha matatizo unayotaka kutumia. Kwa mfano, chagua **Medium**.
    - Kwa **question**, chagua **Data source** kuwa **{$data.prompt}**.
    - Kwa **answer**, chagua **Data source** kuwa **{$run.outputs.answer}**.
    - Kwa **ground_truth**, chagua **Data source** kuwa **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sw/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Chagua **Next**.

1. Chagua **Submit** kuanzisha tathmini.

1. Tathmini itachukua muda kidogo kumalizika. Unaweza kufuatilia maendeleo katika kichupo cha **Evaluation**.

### Kagua Matokeo ya Tathmini

> [!NOTE]
> Matokeo yaliyotolewa hapa chini yanakusudiwa kuonyesha mchakato wa tathmini. Katika mafunzo haya, tumetumia mfano uliobinafsishwa kwa dataset ndogo kiasi, jambo linaloweza kusababisha matokeo yasiyofikia kiwango kikubwa. Matokeo halisi yanaweza kutofautiana sana kulingana na ukubwa, ubora, na utofauti wa dataset iliyotumika, pamoja na usanidi maalum wa mfano.  

Baada ya tathmini kukamilika, unaweza kupitia matokeo ya viashiria vya utendaji na usalama.
1. Vipimo vya utendaji na ubora:

    - tathmini ufanisi wa mfano katika kutoa majibu yaliyo na muktadha, rahisi kusoma, na yanayohusiana.

    ![Evaluation result.](../../../../../../translated_images/sw/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Vipimo vya hatari na usalama:

    - Hakikisha kuwa matokeo ya mfano ni salama na yanaendana na Kanuni za AI Yenye Uwajibikaji, kuepuka maudhui yoyote yenye madhara au ya kuburudisha.

    ![Evaluation result.](../../../../../../translated_images/sw/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Unaweza kusogeza chini kuona **Matokeo ya vipimo vya kina**.

    ![Evaluation result.](../../../../../../translated_images/sw/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Kwa kutathmini mfano wako maalum wa Phi-3 / Phi-3.5 dhidi ya vipimo vya utendaji na usalama, unaweza kuthibitisha kwamba mfano sio tu una ufanisi, bali pia unazingatia mazoea ya AI yenye uwajibikaji, ukifanya uwe tayari kwa utekelezaji halisi.

## Hongera!

### Umehitimisha mafunzo haya

Umefanikiwa kutathmini mfano uliobadilishwa wa Phi-3 ulioingizwa na Prompt flow katika Microsoft Foundry. Huu ni hatua muhimu katika kuhakikisha kuwa mifano yako ya AI haitendeki vyema tu, bali pia inazingatia kanuni za AI za Uwajibikaji za Microsoft kusaidia kujenga programu za AI za kuaminika na za kuaminika.

![Architecture.](../../../../../../translated_images/sw/architecture.10bec55250f5d6a4.webp)

## Safisha Rasilimali za Azure

Safisha rasilimali zako za Azure ili kuepuka malipo ya ziada kwa akaunti yako. Nenda kwenye portal ya Azure na futa rasilimali zifuatazo:

- Rasilimali ya mafunzo ya mashine ya Azure.
- Utawala wa mfano wa mafunzo ya mashine ya Azure.
- Rasilimali ya Mradi wa Microsoft Foundry.
- Rasilimali ya Prompt flow ya Microsoft Foundry.

### Hatua Zifuatazo

#### Nyaraka

- [Tathmini mifumo ya AI kwa kutumia dashibodi ya AI yenye Uwajibikaji](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Vipimo vya tathmini na ufuatiliaji kwa AI ya kizazi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Nyaraka za Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Nyaraka za Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Maudhui ya Mafunzo

- [Utangulizi wa Mbinu ya AI Yenye Uwajibikaji ya Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Utangulizi wa Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Marejeleo

- [AI Yenye Uwajibikaji ni nini?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Kutangaza zana mpya katika Azure AI kusaidia kujenga programu za AI ya kizazi zilizo salama na za kuaminika](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Tathmini ya programu za AI ya kizazi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Maelezo ya Kionyo**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au ukosefu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->