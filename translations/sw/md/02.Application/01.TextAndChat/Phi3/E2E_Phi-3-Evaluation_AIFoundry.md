<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:50:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "sw"
}
-->
# Tathmini ya Mfano wa Phi-3 / Phi-3.5 ulioboreshwa katika Azure AI Foundry ukiangazia Kanuni za AI Zinazowajibika za Microsoft

Mfano huu wa mwisho hadi mwisho (E2E) unategemea mwongozo "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" kutoka kwa Microsoft Tech Community.

## Muhtasari

### Unawezaje kutathmini usalama na utendaji wa mfano wa Phi-3 / Phi-3.5 ulioboreshwa katika Azure AI Foundry?

Kufanya fine-tuning kwa mfano kunaweza wakati mwingine kusababisha majibu yasiyotarajiwa au yasiyotakikana. Ili kuhakikisha kwamba mfano unabaki salama na wenye ufanisi, ni muhimu kutathmini uwezo wa mfano kutoa maudhui hatarishi na uwezo wake wa kutoa majibu sahihi, yanayohusiana, na yenye muktadha mzuri. Katika mafunzo haya, utajifunza jinsi ya kutathmini usalama na utendaji wa mfano wa Phi-3 / Phi-3.5 ulioboreshwa uliounganishwa na Prompt flow katika Azure AI Foundry.

Hapa kuna mchakato wa tathmini wa Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.sw.png)

*Chanzo cha Picha: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Kwa maelezo zaidi na kuchunguza rasilimali za ziada kuhusu Phi-3 / Phi-3.5, tafadhali tembelea [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Mahitaji ya awali

- [Python](https://www.python.org/downloads)
- [Usajili wa Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Mfano wa Phi-3 / Phi-3.5 ulioboreshwa

### Jedwali la Yaliyomo

1. [**Hali ya Kwanza: Utangulizi wa tathmini ya Prompt flow ya Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Utangulizi wa tathmini ya usalama](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Utangulizi wa tathmini ya utendaji](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Hali ya Pili: Kutathmini mfano wa Phi-3 / Phi-3.5 katika Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Kabla hujaanza](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Tumia Azure OpenAI kutathmini mfano wa Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Tathmini mfano ulioboreshwa wa Phi-3 / Phi-3.5 kwa kutumia tathmini ya Prompt flow ya Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Hongera!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Hali ya Kwanza: Utangulizi wa tathmini ya Prompt flow ya Azure AI Foundry**

### Utangulizi wa tathmini ya usalama

Ili kuhakikisha kwamba mfano wako wa AI ni wa maadili na salama, ni muhimu kuutathmini dhidi ya Kanuni za AI Zinazowajibika za Microsoft. Katika Azure AI Foundry, tathmini za usalama zinakuwezesha kutathmini udhaifu wa mfano wako dhidi ya mashambulizi ya jailbreak na uwezo wake wa kutoa maudhui hatarishi, ambayo ni sambamba moja kwa moja na kanuni hizi.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.sw.png)

*Chanzo cha Picha: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Kanuni za AI Zinazowajibika za Microsoft

Kabla ya kuanza hatua za kiufundi, ni muhimu kuelewa Kanuni za AI Zinazowajibika za Microsoft, mfumo wa maadili ulioundwa kuongoza maendeleo, utekelezaji, na uendeshaji wa mifumo ya AI kwa uwajibikaji. Kanuni hizi zinaongoza muundo, maendeleo, na utekelezaji wa mifumo ya AI kwa njia ambayo ni ya haki, wazi, na jumuishi. Kanuni hizi ni msingi wa kutathmini usalama wa mifano ya AI.

Kanuni za AI Zinazowajibika za Microsoft ni pamoja na:

- **Haki na Ujumuishaji**: Mifumo ya AI inapaswa kuwahudumia watu wote kwa haki na kuepuka kuathiri makundi yanayofanana kwa njia tofauti. Kwa mfano, wakati mifumo ya AI inatoa mwongozo juu ya matibabu ya afya, maombi ya mkopo, au ajira, inapaswa kutoa mapendekezo sawa kwa kila mtu mwenye dalili, hali za kifedha, au sifa za kitaaluma zinazofanana.

- **Uaminifu na Usalama**: Ili kujenga imani, ni muhimu mifumo ya AI ifanye kazi kwa kuaminika, salama, na kwa uthabiti. Mifumo hii inapaswa kuweza kufanya kazi kama ilivyoundwa awali, kujibu kwa usalama hali zisizotarajiwa, na kuzuia udanganyifu hatarishi. Tabia zao na aina ya hali wanazoweza kushughulikia zinaonyesha aina ya mazingira na hali ambazo waendelezaji walitarajia wakati wa muundo na majaribio.

- **Uwazi**: Wakati mifumo ya AI inasaidia kufanya maamuzi yenye athari kubwa kwa maisha ya watu, ni muhimu watu kuelewa jinsi maamuzi hayo yalivyofanywa. Kwa mfano, benki inaweza kutumia mfumo wa AI kuamua kama mtu anastahili mkopo. Kampuni inaweza kutumia mfumo wa AI kuamua wagombea bora zaidi waajiri.

- **Faragha na Usalama**: Kadiri AI inavyoongezeka, kulinda faragha na usalama wa taarifa binafsi na za biashara kunazidi kuwa muhimu na changamoto. Kwa AI, faragha na usalama wa data vinahitaji umakini mkubwa kwa sababu upatikanaji wa data ni muhimu kwa mifumo ya AI kutoa utabiri sahihi na maamuzi ya taarifa kuhusu watu.

- **Uwajibikaji**: Watu wanaounda na kuanzisha mifumo ya AI wanapaswa kuwajibika kwa jinsi mifumo yao inavyofanya kazi. Mashirika yanapaswa kutumia viwango vya sekta kuendeleza kanuni za uwajibikaji. Kanuni hizi zinaweza kuhakikisha kwamba mifumo ya AI si mamlaka ya mwisho katika maamuzi yoyote yanayoathiri maisha ya watu. Pia zinaweza kuhakikisha kwamba binadamu wanadumisha udhibiti wa maana juu ya mifumo ya AI yenye uhuru mkubwa.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.sw.png)

*Chanzo cha Picha: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Ili kujifunza zaidi kuhusu Kanuni za AI Zinazowajibika za Microsoft, tembelea [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Vipimo vya usalama

Katika mafunzo haya, utatathmini usalama wa mfano wa Phi-3 ulioboreshwa kwa kutumia vipimo vya usalama vya Azure AI Foundry. Vipimo hivi vinakusaidia kutathmini uwezo wa mfano kutoa maudhui hatarishi na udhaifu wake dhidi ya mashambulizi ya jailbreak. Vipimo vya usalama ni pamoja na:

- **Maudhui yanayohusiana na kujiua au kujiumiza**: Hupima kama mfano una mwelekeo wa kutoa maudhui yanayohusiana na kujiua au kujiumiza.
- **Maudhui ya chuki na yasiyo ya haki**: Hupima kama mfano una mwelekeo wa kutoa maudhui ya chuki au yasiyo ya haki.
- **Maudhui ya vurugu**: Hupima kama mfano una mwelekeo wa kutoa maudhui ya vurugu.
- **Maudhui ya ngono yasiyofaa**: Hupima kama mfano una mwelekeo wa kutoa maudhui ya ngono yasiyofaa.

Kutathmini vipengele hivi kunahakikisha kwamba mfano wa AI hauzalishi maudhui hatarishi au ya kuudhi, na kuendana na maadili ya jamii na viwango vya udhibiti.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.sw.png)

### Utangulizi wa tathmini ya utendaji

Ili kuhakikisha kwamba mfano wako wa AI unafanya kazi kama inavyotarajiwa, ni muhimu kutathmini utendaji wake dhidi ya vipimo vya utendaji. Katika Azure AI Foundry, tathmini za utendaji zinakuwezesha kutathmini ufanisi wa mfano wako katika kutoa majibu sahihi, yanayohusiana, na yenye muktadha mzuri.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.sw.png)

*Chanzo cha Picha: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Vipimo vya utendaji

Katika mafunzo haya, utatathmini utendaji wa mfano wa Phi-3 / Phi-3.5 ulioboreshwa kwa kutumia vipimo vya utendaji vya Azure AI Foundry. Vipimo hivi vinakusaidia kutathmini ufanisi wa mfano katika kutoa majibu sahihi, yanayohusiana, na yenye muktadha mzuri. Vipimo vya utendaji ni pamoja na:

- **Uthibitisho wa Msingi (Groundedness)**: Tathmini jinsi majibu yaliyotolewa yanavyolingana na taarifa kutoka chanzo cha ingizo.
- **Uhusiano (Relevance)**: Hupima umuhimu wa majibu yaliyotolewa kwa maswali yaliyoulizwa.
- **Muendelezo (Coherence)**: Tathmini jinsi maandishi yaliyotolewa yanavyosogea kwa urahisi, kusomeka kwa asili, na kuonekana kama lugha ya binadamu.
- **Ufasaha (Fluency)**: Tathmini ujuzi wa lugha wa maandishi yaliyotolewa.
- **Ulinganifu na GPT (GPT Similarity)**: Linganisha jibu lililotolewa na ukweli wa msingi kwa ulinganifu.
- **Alama ya F1 (F1 Score)**: Hisa ya maneno yanayoshirikiwa kati ya jibu lililotolewa na data ya chanzo.

Vipimo hivi vinakusaidia kutathmini ufanisi wa mfano katika kutoa majibu sahihi, yanayohusiana, na yenye muktadha mzuri.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.sw.png)

## **Hali ya Pili: Kutathmini mfano wa Phi-3 / Phi-3.5 katika Azure AI Foundry**

### Kabla hujaanza

Mafunzo haya ni muendelezo wa machapisho ya blogu yaliyopita, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" na "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Katika machapisho haya, tulipitia mchakato wa kufanya fine-tuning ya mfano wa Phi-3 / Phi-3.5 katika Azure AI Foundry na kuunganisha na Prompt flow.

Katika mafunzo haya, utatekeleza mfano wa Azure OpenAI kama mtathmini katika Azure AI Foundry na kuutumia kutathmini mfano wako wa Phi-3 / Phi-3.5 ulioboreshwa.

Kabla hujaanza mafunzo haya, hakikisha una mahitaji yafuatayo, kama ilivyoelezwa katika mafunzo yaliyopita:

1. Seti ya data iliyotayarishwa kutathmini mfano wa Phi-3 / Phi-3.5 ulioboreshwa.
1. Mfano wa Phi-3 / Phi-3.5 ulioboreshwa na kupelekwa kwenye Azure Machine Learning.
1. Prompt flow iliyounganishwa na mfano wako wa Phi-3 / Phi-3.5 ulioboreshwa katika Azure AI Foundry.

> [!NOTE]
> Utatumia faili *test_data.jsonl*, iliyoko katika folda ya data kutoka kwa seti ya data ya **ULTRACHAT_200k** iliyopakuliwa katika machapisho ya blogu yaliyopita, kama seti ya data ya kutathmini mfano wa Phi-3 / Phi-3.5 ulioboreshwa.

#### Unganisha mfano wa Phi-3 / Phi-3.5 uliobinafsishwa na Prompt flow katika Azure AI Foundry (Njia ya kwanza kwa kutumia msimbo)
> [!NOTE]
> Ikiwa ulifuata njia ya low-code iliyoelezwa katika "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", unaweza kuruka zoezi hili na kuendelea na lile linalofuata.
> Hata hivyo, ikiwa ulifuata njia ya code-first iliyoelezwa katika "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ili kufanyia marekebisho na kupeleka mfano wako wa Phi-3 / Phi-3.5, mchakato wa kuunganisha mfano wako na Prompt flow ni tofauti kidogo. Utajifunza mchakato huu katika zoezi hili.
Ili kuendelea, unahitaji kuunganisha modeli yako ya Phi-3 / Phi-3.5 iliyoboreshwa ndani ya Prompt flow katika Azure AI Foundry.

#### Unda Azure AI Foundry Hub

Unahitaji kuunda Hub kabla ya kuunda Mradi. Hub hufanya kazi kama Resource Group, ikikuruhusu kupanga na kusimamia Miradi mingi ndani ya Azure AI Foundry.

1. Ingia kwenye [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Chagua **All hubs** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New hub** kutoka kwenye menyu ya urambazaji.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.sw.png)

1. Fanya kazi zifuatazo:

    - Weka **Hub name**. Lazima iwe jina la kipekee.
    - Chagua **Subscription** yako ya Azure.
    - Chagua **Resource group** utakayotumia (unda mpya ikiwa inahitajika).
    - Chagua **Location** unayotaka kutumia.
    - Chagua **Connect Azure AI Services** utakayotumia (unda mpya ikiwa inahitajika).
    - Chagua **Connect Azure AI Search** kisha **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.sw.png)

1. Chagua **Next**.

#### Unda Mradi wa Azure AI Foundry

1. Katika Hub uliyounda, chagua **All projects** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New project** kutoka kwenye menyu ya urambazaji.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.sw.png)

1. Weka **Project name**. Lazima iwe jina la kipekee.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.sw.png)

1. Chagua **Create a project**.

#### Ongeza muunganisho maalum kwa modeli ya Phi-3 / Phi-3.5 iliyoboreshwa

Ili kuunganisha modeli yako maalum ya Phi-3 / Phi-3.5 na Prompt flow, unahitaji kuhifadhi endpoint na ufunguo wa modeli katika muunganisho maalum. Mpangilio huu unahakikisha upatikanaji wa modeli yako maalum ya Phi-3 / Phi-3.5 ndani ya Prompt flow.

#### Weka api key na endpoint uri ya modeli ya Phi-3 / Phi-3.5 iliyoboreshwa

1. Tembelea [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Nenda kwenye eneo la kazi la Azure Machine learning ulilounda.

1. Chagua **Endpoints** kutoka kwenye kichupo cha upande wa kushoto.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.sw.png)

1. Chagua endpoint uliyounda.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.sw.png)

1. Chagua **Consume** kutoka kwenye menyu ya urambazaji.

1. Nakili **REST endpoint** na **Primary key** zako.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.sw.png)

#### Ongeza Muunganisho Maalum

1. Tembelea [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Nenda kwenye mradi wa Azure AI Foundry ulilounda.

1. Katika Mradi ulilounda, chagua **Settings** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.sw.png)

1. Chagua **Custom keys** kutoka kwenye menyu ya urambazaji.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.sw.png)

1. Fanya kazi zifuatazo:

    - Chagua **+ Add key value pairs**.
    - Kwa jina la ufunguo, andika **endpoint** na bandika endpoint uliyokopa kutoka Azure ML Studio kwenye sehemu ya thamani.
    - Chagua tena **+ Add key value pairs**.
    - Kwa jina la ufunguo, andika **key** na bandika ufunguo uliyokopa kutoka Azure ML Studio kwenye sehemu ya thamani.
    - Baada ya kuongeza funguo, chagua **is secret** ili kuzuia ufunguo kuonekana wazi.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.sw.png)

1. Chagua **Add connection**.

#### Unda Prompt flow

Umeongeza muunganisho maalum katika Azure AI Foundry. Sasa, hebu tuunde Prompt flow kwa kutumia hatua zifuatazo. Kisha, utaunganisha Prompt flow hii na muunganisho maalum ili kutumia modeli iliyoboreshwa ndani ya Prompt flow.

1. Nenda kwenye mradi wa Azure AI Foundry ulilounda.

1. Chagua **Prompt flow** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ Create** kutoka kwenye menyu ya urambazaji.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.sw.png)

1. Chagua **Chat flow** kutoka kwenye menyu ya urambazaji.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.sw.png)

1. Weka **Folder name** utakayotumia.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.sw.png)

1. Chagua **Create**.

#### Sanidi Prompt flow kuzungumza na modeli yako maalum ya Phi-3 / Phi-3.5

Unahitaji kuunganisha modeli iliyoboreshwa ya Phi-3 / Phi-3.5 ndani ya Prompt flow. Hata hivyo, Prompt flow iliyopo haijaundwa kwa madhumuni haya. Kwa hivyo, lazima ubadilishe Prompt flow ili kuwezesha kuunganishwa kwa modeli maalum.

1. Katika Prompt flow, fanya kazi zifuatazo ili kujenga upya mtiririko uliopo:

    - Chagua **Raw file mode**.
    - Futa msimbo wote uliopo katika faili *flow.dag.yml*.
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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.sw.png)

1. Ongeza msimbo ufuatao kwenye *integrate_with_promptflow.py* ili kutumia modeli maalum ya Phi-3 / Phi-3.5 katika Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.sw.png)

> [!NOTE]
> Kwa maelezo zaidi kuhusu kutumia Prompt flow katika Azure AI Foundry, unaweza rejelea [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Chagua **Chat input**, **Chat output** kuwezesha mazungumzo na modeli yako.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.sw.png)

1. Sasa uko tayari kuzungumza na modeli yako maalum ya Phi-3 / Phi-3.5. Katika zoezi lijalo, utajifunza jinsi ya kuanzisha Prompt flow na kuitumia kuzungumza na modeli yako iliyoboreshwa ya Phi-3 / Phi-3.5.

> [!NOTE]
>
> Mtiririko ulioumbwa upya unapaswa kuonekana kama picha iliyo hapa chini:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.sw.png)
>

#### Anzisha Prompt flow

1. Chagua **Start compute sessions** kuanzisha Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.sw.png)

1. Chagua **Validate and parse input** ili kusasisha vigezo.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.sw.png)

1. Chagua **Value** ya **connection** kwa muunganisho maalum uliouunda. Kwa mfano, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.sw.png)

#### Zungumza na modeli yako maalum ya Phi-3 / Phi-3.5

1. Chagua **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.sw.png)

1. Hapa kuna mfano wa matokeo: Sasa unaweza kuzungumza na modeli yako maalum ya Phi-3 / Phi-3.5. Inashauriwa kuuliza maswali yanayotegemea data iliyotumika kwa ajili ya kuboresha modeli.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.sw.png)

### Sambaza Azure OpenAI ili kutathmini modeli ya Phi-3 / Phi-3.5

Ili kutathmini modeli ya Phi-3 / Phi-3.5 katika Azure AI Foundry, unahitaji kusambaza modeli ya Azure OpenAI. Modeli hii itatumika kutathmini utendaji wa modeli ya Phi-3 / Phi-3.5.

#### Sambaza Azure OpenAI

1. Ingia kwenye [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Nenda kwenye mradi wa Azure AI Foundry ulilounda.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.sw.png)

1. Katika Mradi ulilounda, chagua **Deployments** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ Deploy model** kutoka kwenye menyu ya urambazaji.

1. Chagua **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.sw.png)

1. Chagua modeli ya Azure OpenAI unayotaka kutumia. Kwa mfano, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.sw.png)

1. Chagua **Confirm**.

### Tathmini modeli iliyoboreshwa ya Phi-3 / Phi-3.5 kwa kutumia tathmini ya Prompt flow ya Azure AI Foundry

### Anzisha tathmini mpya

1. Tembelea [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Nenda kwenye mradi wa Azure AI Foundry ulilounda.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.sw.png)

1. Katika Mradi ulilounda, chagua **Evaluation** kutoka kwenye kichupo cha upande wa kushoto.

1. Chagua **+ New evaluation** kutoka kwenye menyu ya urambazaji.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.sw.png)

1. Chagua tathmini ya **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.sw.png)

1. Fanya kazi zifuatazo:

    - Weka jina la tathmini. Lazima liwe la kipekee.
    - Chagua **Question and answer without context** kama aina ya kazi. Kwa sababu, dataset ya **ULTRACHAT_200k** inayotumika katika mafunzo haya haina muktadha.
    - Chagua prompt flow unayotaka kutathmini.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.sw.png)

1. Chagua **Next**.

1. Fanya kazi zifuatazo:

    - Chagua **Add your dataset** kupakia dataset. Kwa mfano, unaweza kupakia faili ya dataset ya mtihani, kama *test_data.json1*, ambayo inajumuishwa unapo download dataset ya **ULTRACHAT_200k**.
    - Chagua safu sahihi ya **Dataset column** inayolingana na dataset yako. Kwa mfano, ikiwa unatumia dataset ya **ULTRACHAT_200k**, chagua **${data.prompt}** kama safu ya dataset.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.sw.png)

1. Chagua **Next**.

1. Fanya kazi zifuatazo kusanidi vipimo vya utendaji na ubora:

    - Chagua vipimo vya utendaji na ubora unavyotaka kutumia.
    - Chagua modeli ya Azure OpenAI uliyounda kwa ajili ya tathmini. Kwa mfano, chagua **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.sw.png)

1. Fanya kazi zifuatazo kusanidi vipimo vya hatari na usalama:

    - Chagua vipimo vya hatari na usalama unavyotaka kutumia.
    - Chagua kikomo cha kuhesabu kiwango cha kasoro unachotaka kutumia. Kwa mfano, chagua **Medium**.
    - Kwa **question**, chagua **Data source** kuwa **{$data.prompt}**.
    - Kwa **answer**, chagua **Data source** kuwa **{$run.outputs.answer}**.
    - Kwa **ground_truth**, chagua **Data source** kuwa **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.sw.png)

1. Chagua **Next**.

1. Chagua **Submit** kuanza tathmini.

1. Tathmini itachukua muda kidogo kukamilika. Unaweza kufuatilia maendeleo kwenye kichupo cha **Evaluation**.

### Pitia Matokeo ya Tathmini
> [!NOTE]
> Matokeo yaliyoonyeshwa hapa chini yamekusudiwa kuonyesha mchakato wa tathmini. Katika mafunzo haya, tumetumia mfano ulioboreshwa kwa dataset ndogo kidogo, ambayo inaweza kusababisha matokeo yasiyokuwa bora kabisa. Matokeo halisi yanaweza kutofautiana sana kulingana na ukubwa, ubora, na utofauti wa dataset iliyotumika, pamoja na usanidi maalum wa mfano.
Mara baada ya tathmini kukamilika, unaweza kupitia matokeo kwa vigezo vya utendaji na usalama.

1. Vigezo vya utendaji na ubora:

    - tathmini ufanisi wa modeli katika kutoa majibu yanayofanana, yenye mtiririko mzuri, na yanayohusiana.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.sw.png)

1. Vigezo vya hatari na usalama:

    - Hakikisha matokeo ya modeli ni salama na yanaendana na Kanuni za AI Zinazowajibika, kuepuka maudhui yoyote hatarishi au ya kuudhi.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.sw.png)

1. Unaweza kusogeza chini kuona **Matokeo ya vigezo kwa undani**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.sw.png)

1. Kwa kutathmini modeli yako maalum ya Phi-3 / Phi-3.5 dhidi ya vigezo vya utendaji na usalama, unaweza kuthibitisha kuwa modeli si tu ina ufanisi, bali pia inazingatia mazoea ya AI yanayowajibika, na hivyo kuifanya kuwa tayari kwa matumizi halisi.

## Hongera!

### Umehitimisha mafunzo haya

Umefanikiwa kutathmini modeli ya Phi-3 iliyoboreshwa na kuunganishwa na Prompt flow katika Azure AI Foundry. Huu ni hatua muhimu kuhakikisha kuwa modeli zako za AI si tu zinafanya kazi vizuri, bali pia zinafuata kanuni za AI Zinazowajibika za Microsoft kusaidia kujenga programu za AI zinazotegemewa na kuaminika.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.sw.png)

## Safisha Rasilimali za Azure

Safisha rasilimali zako za Azure ili kuepuka malipo ya ziada kwenye akaunti yako. Nenda kwenye portal ya Azure na futa rasilimali zifuatazo:

- Rasilimali ya Azure Machine learning.
- Kituo cha modeli ya Azure Machine learning.
- Rasilimali ya Mradi wa Azure AI Foundry.
- Rasilimali ya Prompt flow ya Azure AI Foundry.

### Hatua Zifuatazo

#### Nyaraka

- [Tathmini mifumo ya AI kwa kutumia dashibodi ya AI Zinazowajibika](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Vigezo vya tathmini na ufuatiliaji kwa AI ya kizazi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Nyaraka za Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Nyaraka za Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Maudhui ya Mafunzo

- [Utangulizi wa Mbinu ya AI Zinazowajibika ya Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Utangulizi wa Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Marejeleo

- [AI Zinazowajibika ni Nini?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Kutangaza zana mpya katika Azure AI kusaidia kujenga programu za AI za kizazi zilizo salama na za kuaminika zaidi](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Tathmini ya programu za AI za kizazi](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.