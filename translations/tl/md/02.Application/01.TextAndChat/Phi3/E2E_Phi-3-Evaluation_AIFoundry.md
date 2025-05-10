<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T17:05:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "tl"
}
-->
# Evaluate the Fine-tuned Phi-3 / Phi-3.5 Model in Azure AI Foundry Focusing on Microsoft's Responsible AI Principles

This end-to-end (E2E) sample is based on the guide "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" from the Microsoft Tech Community.

## Overview

### Paano mo masusuri ang kaligtasan at performance ng fine-tuned Phi-3 / Phi-3.5 model sa Azure AI Foundry?

Ang fine-tuning ng isang modelo ay minsan nagreresulta sa hindi inaasahan o hindi kanais-nais na mga sagot. Para matiyak na nananatiling ligtas at epektibo ang modelo, mahalagang suriin ang potensyal nito na gumawa ng mapanganib na nilalaman at ang kakayahan nitong magbigay ng tama, may kaugnayan, at magkakaugnay na mga sagot. Sa tutorial na ito, matututuhan mo kung paano suriin ang kaligtasan at performance ng fine-tuned Phi-3 / Phi-3.5 model na naka-integrate sa Prompt flow sa Azure AI Foundry.

Narito ang proseso ng pagsusuri ng Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tl.png)

*Pinagmulan ng Larawan: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para sa mas detalyadong impormasyon at karagdagang resources tungkol sa Phi-3 / Phi-3.5, bisitahin ang [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Mga Kinakailangan

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 model

### Talaan ng Nilalaman

1. [**Scenario 1: Panimula sa Azure AI Foundry's Prompt flow evaluation**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Panimula sa safety evaluation](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Panimula sa performance evaluation](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Pagsusuri ng Phi-3 / Phi-3.5 model sa Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Bago ka magsimula](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [I-deploy ang Azure OpenAI para suriin ang Phi-3 / Phi-3.5 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Suriin ang fine-tuned Phi-3 / Phi-3.5 model gamit ang Azure AI Foundry's Prompt flow evaluation](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Congratulations!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Panimula sa Azure AI Foundry's Prompt flow evaluation**

### Panimula sa safety evaluation

Para matiyak na ang iyong AI model ay etikal at ligtas, mahalagang suriin ito batay sa Microsoft's Responsible AI Principles. Sa Azure AI Foundry, pinapayagan ka ng safety evaluations na suriin ang kahinaan ng iyong modelo sa jailbreak attacks at ang potensyal nitong gumawa ng mapanganib na nilalaman, na direktang nakaayon sa mga prinsipyong ito.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.tl.png)

*Pinagmulan ng Larawan: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft’s Responsible AI Principles

Bago simulan ang mga teknikal na hakbang, mahalagang maunawaan ang Microsoft's Responsible AI Principles, isang etikal na balangkas na dinisenyo para gabayan ang responsable na pag-develop, pag-deploy, at operasyon ng mga AI system. Ang mga prinsipyong ito ang naggagabay sa responsable na disenyo, pagbuo, at pag-deploy ng AI systems, na tinitiyak na ang mga AI teknolohiya ay ginawa nang patas, transparent, at inklusibo. Ang mga prinsipyong ito ang pundasyon sa pagsusuri ng kaligtasan ng mga AI model.

Kasama sa Microsoft's Responsible AI Principles ang:

- **Fairness and Inclusiveness**: Dapat patas ang pagtrato ng AI systems sa lahat at iwasan ang diskriminasyon sa magkakaparehong grupo ng tao. Halimbawa, kapag nagbibigay ang AI systems ng gabay sa medikal na paggamot, aplikasyon sa pautang, o trabaho, dapat pareho ang rekomendasyon sa lahat ng may katulad na sintomas, kalagayang pinansyal, o kwalipikasyon sa trabaho.

- **Reliability and Safety**: Para magkaroon ng tiwala, kritikal na ang AI systems ay gumana nang maaasahan, ligtas, at tuloy-tuloy. Dapat kaya nilang mag-operate ayon sa disenyo, tumugon nang ligtas sa hindi inaasahang kondisyon, at labanan ang mapanirang manipulasyon. Ang kanilang kilos at ang iba't ibang kondisyon na kaya nilang harapin ay sumasalamin sa mga sitwasyon na inasahan ng mga developer sa disenyo at pagsubok.

- **Transparency**: Kapag tumutulong ang AI systems sa mga desisyong may malaking epekto sa buhay ng tao, mahalaga na maintindihan ng mga tao kung paano ginawa ang mga desisyong iyon. Halimbawa, maaaring gamitin ng bangko ang AI system para tukuyin kung karapat-dapat ang isang tao sa kredito. Maaaring gamitin ng kumpanya ang AI para piliin ang pinaka-angkop na kandidato sa trabaho.

- **Privacy and Security**: Habang lumalaganap ang AI, nagiging mas mahalaga at kumplikado ang pagprotekta sa privacy at seguridad ng personal at pangnegosyong impormasyon. Sa AI, kinakailangan ng masusing pansin sa privacy at seguridad dahil mahalaga ang access sa data para makagawa ang AI ng tama at may batayang prediksyon at desisyon tungkol sa mga tao.

- **Accountability**: Ang mga taong nagdisenyo at nag-deploy ng AI systems ay dapat managot sa kung paano gumagana ang kanilang mga sistema. Dapat gumamit ang mga organisasyon ng mga pamantayan sa industriya para bumuo ng mga patakaran sa pananagutan. Pinapangalagaan nito na ang AI systems ay hindi ang huling awtoridad sa anumang desisyong may epekto sa buhay ng tao. Pinapanatili rin nito na may makabuluhang kontrol ang tao sa mga highly autonomous na AI systems.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.tl.png)

*Pinagmulan ng Larawan: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para matuto pa tungkol sa Microsoft's Responsible AI Principles, bisitahin ang [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Safety metrics

Sa tutorial na ito, susuriin mo ang kaligtasan ng fine-tuned Phi-3 model gamit ang safety metrics ng Azure AI Foundry. Tinutulungan ka ng mga metrics na ito na tasahin ang potensyal ng modelo na gumawa ng mapanganib na nilalaman at ang kahinaan nito sa jailbreak attacks. Kasama sa safety metrics ang:

- **Self-harm-related Content**: Sinusuri kung may tendensiya ang modelo na gumawa ng nilalaman na may kinalaman sa pananakit sa sarili.
- **Hateful and Unfair Content**: Sinusuri kung may tendensiya ang modelo na gumawa ng mapanirang o hindi patas na nilalaman.
- **Violent Content**: Sinusuri kung may tendensiya ang modelo na gumawa ng marahas na nilalaman.
- **Sexual Content**: Sinusuri kung may tendensiya ang modelo na gumawa ng hindi angkop na sekswal na nilalaman.

Ang pagsusuri sa mga aspetong ito ay tinitiyak na ang AI model ay hindi gumagawa ng mapanganib o nakakasakit na nilalaman, na naaayon sa mga pagpapahalagang panlipunan at mga regulasyon.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.tl.png)

### Panimula sa performance evaluation

Para matiyak na gumagana ang iyong AI model ayon sa inaasahan, mahalagang suriin ang performance nito gamit ang mga performance metrics. Sa Azure AI Foundry, pinapayagan ka ng performance evaluations na tasahin ang bisa ng iyong modelo sa paggawa ng tama, may kaugnayan, at magkakaugnay na mga sagot.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.tl.png)

*Pinagmulan ng Larawan: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Performance metrics

Sa tutorial na ito, susuriin mo ang performance ng fine-tuned Phi-3 / Phi-3.5 model gamit ang performance metrics ng Azure AI Foundry. Tinutulungan ka ng mga metrics na ito na tasahin ang bisa ng modelo sa paggawa ng tama, may kaugnayan, at magkakaugnay na mga sagot. Kasama sa performance metrics ang:

- **Groundedness**: Sinusuri kung gaano kahusay na nakaayon ang mga sagot sa impormasyon mula sa input source.
- **Relevance**: Sinusuri ang kaugnayan ng mga sagot sa mga ibinigay na tanong.
- **Coherence**: Sinusuri kung gaano kakinis ang daloy ng teksto, kung ito ay natural basahin, at kahawig ng wika ng tao.
- **Fluency**: Sinusuri ang kahusayan sa wika ng nilikhang teksto.
- **GPT Similarity**: Kinukumpara ang nilikhang sagot sa ground truth para sa pagkakapareho.
- **F1 Score**: Kinakalkula ang proporsyon ng mga salitang pareho sa pagitan ng nilikhang sagot at source data.

Tinutulungan ka ng mga metrics na ito na tasahin ang bisa ng modelo sa paggawa ng tama, may kaugnayan, at magkakaugnay na mga sagot.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.tl.png)

## **Scenario 2: Pagsusuri ng Phi-3 / Phi-3.5 model sa Azure AI Foundry**

### Bago ka magsimula

Ang tutorial na ito ay karugtong ng mga naunang blog post, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" at "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Sa mga post na ito, tinalakay namin ang proseso ng fine-tuning ng Phi-3 / Phi-3.5 model sa Azure AI Foundry at ang pag-integrate nito sa Prompt flow.

Sa tutorial na ito, magde-deploy ka ng Azure OpenAI model bilang evaluator sa Azure AI Foundry at gagamitin ito para suriin ang fine-tuned Phi-3 / Phi-3.5 model mo.

Bago simulan ang tutorial na ito, tiyaking mayroon kang mga sumusunod na kinakailangan, ayon sa mga naunang tutorial:

1. Isang handang dataset para suriin ang fine-tuned Phi-3 / Phi-3.5 model.
1. Isang Phi-3 / Phi-3.5 model na na-fine-tune at na-deploy sa Azure Machine Learning.
1. Isang Prompt flow na naka-integrate sa fine-tuned Phi-3 / Phi-3.5 model mo sa Azure AI Foundry.

> [!NOTE]
> Gagamitin mo ang *test_data.jsonl* file, na nasa data folder mula sa **ULTRACHAT_200k** dataset na na-download sa mga naunang blog post, bilang dataset para suriin ang fine-tuned Phi-3 / Phi-3.5 model.

#### I-integrate ang custom Phi-3 / Phi-3.5 model sa Prompt flow sa Azure AI Foundry (Code first approach)

> [!NOTE]
> Kung sinunod mo ang low-code approach na inilalarawan sa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", maaari mo nang laktawan ang exercise na ito at magpatuloy sa susunod.
> Ngunit, kung sinunod mo ang code-first approach na inilalarawan sa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para i-fine-tune at i-deploy ang Phi-3 / Phi-3.5 model mo, medyo iba ang proseso ng pagkonekta ng modelo mo sa Prompt flow. Matututuhan mo ang prosesong ito sa exercise na ito.

Para magpatuloy, kailangan mong i-integrate ang fine-tuned Phi-3 / Phi-3.5 model mo sa Prompt flow sa Azure AI Foundry.

#### Gumawa ng Azure AI Foundry Hub

Kailangan mong gumawa ng Hub bago gumawa ng Project. Ang Hub ay parang Resource Group, na nagbibigay-daan sa iyo na ayusin at pamahalaan ang maraming Project sa loob ng Azure AI Foundry.

1. Mag-sign in sa [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Piliin ang **All hubs** mula sa kaliwang tab.

1. Piliin ang **+ New hub** mula sa navigation menu.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.tl.png)

1. Gawin ang mga sumusunod:

    - Ilagay ang **Hub name**. Dapat ito ay natatangi.
    - Piliin ang Azure **Subscription** mo.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Location** na nais mong gamitin.
    - Piliin ang **Connect Azure AI Services** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Connect Azure AI Search** at piliin ang **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.tl.png)

1. Piliin ang **Next**.

#### Gumawa ng Azure AI Foundry Project

1. Sa Hub na ginawa mo, piliin ang **All projects** mula sa kaliwang tab.

1. Piliin ang **+ New project** mula sa navigation menu.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.tl.png)

1. Ilagay ang **Project name**. Dapat ito ay natatanging pangalan.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.tl.png)

1. Piliin ang **Create a project**.

#### Magdagdag ng custom connection para sa fine-tuned Phi-3 / Phi-3.5 model

Para ma-integrate ang custom mong Phi-3 / Phi-3.5 model sa Prompt flow, kailangan mong i-save ang endpoint at key ng model sa isang custom connection. Ang setup na ito ay nagsisiguro ng access sa iyong custom Phi-3 / Phi-3.5 model sa Prompt flow.

#### Itakda ang api key at endpoint uri ng fine-tuned Phi-3 / Phi-3.5 model

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure Machine learning workspace na ginawa mo.

1. Piliin ang **Endpoints** mula sa kaliwang tab.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.tl.png)

1. Piliin ang endpoint na ginawa mo.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.tl.png)

1. Piliin ang **Consume** mula sa navigation menu.

1. Kopyahin ang iyong **REST endpoint** at **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.tl.png)

#### Magdagdag ng Custom Connection

1. Bisitahin ang [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure AI Foundry project na ginawa mo.

1. Sa Project na ginawa mo, piliin ang **Settings** mula sa kaliwang tab.

1. Piliin ang **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.tl.png)

1. Piliin ang **Custom keys** mula sa navigation menu.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.tl.png)

1. Gawin ang mga sumusunod:

    - Piliin ang **+ Add key value pairs**.
    - Para sa key name, ilagay ang **endpoint** at i-paste ang endpoint na kinopya mo mula sa Azure ML Studio sa value field.
    - Piliin muli ang **+ Add key value pairs**.
    - Para sa key name, ilagay ang **key** at i-paste ang key na kinopya mo mula sa Azure ML Studio sa value field.
    - Pagkatapos maidagdag ang mga keys, piliin ang **is secret** para hindi makita ang key.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.tl.png)

1. Piliin ang **Add connection**.

#### Gumawa ng Prompt flow

Nagdagdag ka na ng custom connection sa Azure AI Foundry. Ngayon, gumawa tayo ng Prompt flow gamit ang mga sumusunod na hakbang. Pagkatapos, iko-connect mo ang Prompt flow na ito sa custom connection para magamit ang fine-tuned model sa loob ng Prompt flow.

1. Pumunta sa Azure AI Foundry project na ginawa mo.

1. Piliin ang **Prompt flow** mula sa kaliwang tab.

1. Piliin ang **+ Create** mula sa navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.tl.png)

1. Piliin ang **Chat flow** mula sa navigation menu.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.tl.png)

1. Ilagay ang **Folder name** na gagamitin.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.tl.png)

1. Piliin ang **Create**.

#### I-set up ang Prompt flow para makipag-chat sa iyong custom Phi-3 / Phi-3.5 model

Kailangan mong i-integrate ang fine-tuned Phi-3 / Phi-3.5 model sa Prompt flow. Pero, ang kasalukuyang Prompt flow na ibinigay ay hindi ginawa para dito. Kaya kailangan mong baguhin ang Prompt flow para maisama ang custom model.

1. Sa Prompt flow, gawin ang mga sumusunod para buuin muli ang kasalukuyang flow:

    - Piliin ang **Raw file mode**.
    - Burahin lahat ng code sa *flow.dag.yml* file.
    - Idagdag ang sumusunod na code sa *flow.dag.yml*.

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

    - Piliin ang **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.tl.png)

1. Idagdag ang sumusunod na code sa *integrate_with_promptflow.py* para magamit ang custom Phi-3 / Phi-3.5 model sa Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.tl.png)

> [!NOTE]
> Para sa mas detalyadong impormasyon tungkol sa paggamit ng Prompt flow sa Azure AI Foundry, maaari mong bisitahin ang [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Piliin ang **Chat input**, **Chat output** para paganahin ang chat gamit ang iyong model.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.tl.png)

1. Handa ka na ngayong makipag-chat sa iyong custom Phi-3 / Phi-3.5 model. Sa susunod na gawain, matututuhan mo kung paano simulan ang Prompt flow at gamitin ito para makipag-chat sa iyong fine-tuned Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> Ang binuong flow ay dapat magmukhang ganito:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.tl.png)
>

#### Simulan ang Prompt flow

1. Piliin ang **Start compute sessions** para simulan ang Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.tl.png)

1. Piliin ang **Validate and parse input** para i-update ang mga parameter.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.tl.png)

1. Piliin ang **Value** ng **connection** sa custom connection na ginawa mo. Halimbawa, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.tl.png)

#### Makipag-chat sa iyong custom Phi-3 / Phi-3.5 model

1. Piliin ang **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.tl.png)

1. Narito ang halimbawa ng resulta: Ngayon ay maaari ka nang makipag-chat sa iyong custom Phi-3 / Phi-3.5 model. Inirerekomenda na magtanong base sa data na ginamit sa fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.tl.png)

### I-deploy ang Azure OpenAI para suriin ang Phi-3 / Phi-3.5 model

Para masuri ang Phi-3 / Phi-3.5 model sa Azure AI Foundry, kailangan mong i-deploy ang isang Azure OpenAI model. Gagamitin ang modelong ito para i-evaluate ang performance ng Phi-3 / Phi-3.5 model.

#### I-deploy ang Azure OpenAI

1. Mag-sign in sa [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure AI Foundry project na ginawa mo.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tl.png)

1. Sa Project na ginawa mo, piliin ang **Deployments** mula sa kaliwang tab.

1. Piliin ang **+ Deploy model** mula sa navigation menu.

1. Piliin ang **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.tl.png)

1. Piliin ang Azure OpenAI model na gusto mong gamitin. Halimbawa, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.tl.png)

1. Piliin ang **Confirm**.

### Suriin ang fine-tuned Phi-3 / Phi-3.5 model gamit ang Azure AI Foundry's Prompt flow evaluation

### Magsimula ng bagong evaluation

1. Bisitahin ang [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure AI Foundry project na ginawa mo.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.tl.png)

1. Sa Project na ginawa mo, piliin ang **Evaluation** mula sa kaliwang tab.

1. Piliin ang **+ New evaluation** mula sa navigation menu.
![Piliin ang pagsusuri.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.tl.png)

1. Piliin ang **Prompt flow** na pagsusuri.

    ![Piliin ang Prompt flow na pagsusuri.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.tl.png)

1. Gawin ang mga sumusunod na gawain:

    - Ilagay ang pangalan ng pagsusuri. Dapat ito ay isang natatanging halaga.
    - Piliin ang **Question and answer without context** bilang uri ng gawain. Dahil ang dataset na **UlTRACHAT_200k** na ginamit sa tutorial na ito ay walang konteksto.
    - Piliin ang prompt flow na nais mong suriin.

    ![Prompt flow na pagsusuri.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.tl.png)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod na gawain:

    - Piliin ang **Add your dataset** upang i-upload ang dataset. Halimbawa, maaari mong i-upload ang test dataset file, tulad ng *test_data.json1*, na kasama kapag dina-download mo ang **ULTRACHAT_200k** dataset.
    - Piliin ang angkop na **Dataset column** na tumutugma sa iyong dataset. Halimbawa, kung ginagamit mo ang **ULTRACHAT_200k** dataset, piliin ang **${data.prompt}** bilang dataset column.

    ![Prompt flow na pagsusuri.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.tl.png)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod na gawain upang i-configure ang performance at quality metrics:

    - Piliin ang performance at quality metrics na nais mong gamitin.
    - Piliin ang Azure OpenAI model na ginawa mo para sa pagsusuri. Halimbawa, piliin ang **gpt-4o**.

    ![Prompt flow na pagsusuri.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.tl.png)

1. Gawin ang mga sumusunod na gawain upang i-configure ang risk at safety metrics:

    - Piliin ang risk at safety metrics na nais mong gamitin.
    - Piliin ang threshold para kalkulahin ang defect rate na nais mong gamitin. Halimbawa, piliin ang **Medium**.
    - Para sa **question**, piliin ang **Data source** sa **{$data.prompt}**.
    - Para sa **answer**, piliin ang **Data source** sa **{$run.outputs.answer}**.
    - Para sa **ground_truth**, piliin ang **Data source** sa **{$data.message}**.

    ![Prompt flow na pagsusuri.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.tl.png)

1. Piliin ang **Next**.

1. Piliin ang **Submit** upang simulan ang pagsusuri.

1. Aabutin ng ilang sandali ang pagsusuri bago matapos. Maaari mong subaybayan ang progreso sa tab na **Evaluation**.

### Suriin ang Mga Resulta ng Pagsusuri

> [!NOTE]
> Ang mga resulta na ipinapakita sa ibaba ay para ipakita ang proseso ng pagsusuri. Sa tutorial na ito, gumamit kami ng modelong fine-tuned sa isang medyo maliit na dataset, kaya maaaring hindi ito magbigay ng pinakamainam na resulta. Ang aktwal na resulta ay maaaring mag-iba nang malaki depende sa laki, kalidad, at pagkakaiba-iba ng dataset na ginamit, pati na rin sa partikular na konfigurasyon ng modelo.

Kapag natapos na ang pagsusuri, maaari mong tingnan ang mga resulta para sa parehong performance at safety metrics.

1. Performance at quality metrics:

    - suriin ang pagiging epektibo ng modelo sa paggawa ng magkakaugnay, maayos, at may kaugnayang mga sagot.

    ![Resulta ng pagsusuri.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.tl.png)

1. Risk at safety metrics:

    - Siguraduhin na ang mga output ng modelo ay ligtas at sumusunod sa Responsible AI Principles, na iniiwasan ang anumang mapanganib o nakakasakit na nilalaman.

    ![Resulta ng pagsusuri.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.tl.png)

1. Maaari kang mag-scroll pababa upang makita ang **Detailed metrics result**.

    ![Resulta ng pagsusuri.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.tl.png)

1. Sa pamamagitan ng pagsusuri ng iyong custom na Phi-3 / Phi-3.5 model laban sa parehong performance at safety metrics, maaari mong matiyak na ang modelo ay hindi lamang epektibo, kundi sumusunod din sa mga responsableng AI na gawain, kaya handa na ito para sa aktwal na paggamit.

## Congratulations!

### Natapos mo na ang tutorial na ito

Matagumpay mong nasuri ang fine-tuned na Phi-3 model na naka-integrate sa Prompt flow sa Azure AI Foundry. Ito ay isang mahalagang hakbang upang matiyak na ang iyong mga AI model ay hindi lamang mahusay ang pagganap, kundi sumusunod din sa Microsoft's Responsible AI principles upang matulungan kang makabuo ng mapagkakatiwalaan at maaasahang AI na mga aplikasyon.

![Arkitektura.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.tl.png)

## Linisin ang Azure Resources

Linisin ang iyong Azure resources upang maiwasan ang karagdagang singil sa iyong account. Pumunta sa Azure portal at tanggalin ang mga sumusunod na resources:

- Ang Azure Machine learning resource.
- Ang Azure Machine learning model endpoint.
- Ang Azure AI Foundry Project resource.
- Ang Azure AI Foundry Prompt flow resource.

### Mga Susunod na Hakbang

#### Dokumentasyon

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Training Content

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Sanggunian

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Pagtatakwil**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagsisikapan ang katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.