# Suriin ang Fine-tuned Phi-3 / Phi-3.5 Model sa Microsoft Foundry na Nakatuon sa Mga Prinsipyo ng Responsible AI ng Microsoft

Ang end-to-end (E2E) na halimbawang ito ay batay sa gabay na "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" mula sa Microsoft Tech Community.

## Pangkalahatang-ideya

### Paano mo masusuri ang kaligtasan at pagganap ng isang fine-tuned na Phi-3 / Phi-3.5 na modelo sa Microsoft Foundry?

Ang pag-fine-tune ng modelo ay maaaring minsang magdulot ng hindi inaasahan o hindi nais na mga tugon. Upang matiyak na nananatiling ligtas at epektibo ang modelo, mahalagang suriin ang potensyal nito na makagawa ng nakasasamang nilalaman at ang kakayahan nitong magbigay ng tama, may kaugnayan, at magkakaugnay na mga tugon. Sa tutorial na ito, matututunan mo kung paano suriin ang kaligtasan at pagganap ng fine-tuned na Phi-3 / Phi-3.5 na modelo na naka-integrate sa Prompt flow sa Microsoft Foundry.

Narito ang proseso ng pagsusuri ng Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/tl/architecture.10bec55250f5d6a4.webp)

*Pinagmulan ng Imahe: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para sa mas detalyadong impormasyon at upang tuklasin ang karagdagang mga mapagkukunan tungkol sa Phi-3 / Phi-3.5, pakibisita ang [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Mga Kinakailangan

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned na Phi-3 / Phi-3.5 na modelo

### Talaan ng Nilalaman

1. [**Scenario 1: Panimula sa Microsoft Foundry's Prompt flow evaluation**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Panimula sa pagsusuri ng kaligtasan](#panimula-sa-pagsusuri-ng-kaligtasan)
    - [Panimula sa pagsusuri ng pagganap](#panimula-sa-pagsusuri-ng-pagganap)

1. [**Scenario 2: Pagsusuri ng Phi-3 / Phi-3.5 na modelo sa Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Bago ka magsimula](#bago-ka-magsimula)
    - [I-deploy ang Azure OpenAI upang suriin ang Phi-3 / Phi-3.5 na modelo](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Suriin ang fine-tuned na Phi-3 / Phi-3.5 na modelo gamit ang Microsoft Foundry's Prompt flow evaluation](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Congratulations!](#binabati-kita)

## **Scenario 1: Panimula sa Microsoft Foundry's Prompt flow evaluation**

### Panimula sa pagsusuri ng kaligtasan

Upang matiyak na ang iyong AI na modelo ay etikal at ligtas, mahalagang suriin ito batay sa Mga Prinsipyo ng Responsible AI ng Microsoft. Sa Microsoft Foundry, ang pagsusuri sa kaligtasan ay nagbibigay-daan sa iyo upang suriin ang kahinaan ng iyong modelo sa jailbreak attacks at ang potensyal nito na makagawa ng nakasasamang nilalaman, na direktang nakaayon sa mga prinsipyong ito.

![Safaty evaluation.](../../../../../../translated_images/tl/safety-evaluation.083586ec88dfa950.webp)

*Pinagmulan ng Imahe: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Mga Prinsipyo ng Responsible AI ng Microsoft

Bago simulan ang mga teknikal na hakbang, mahalagang maunawaan ang Mga Prinsipyo ng Responsible AI ng Microsoft, isang etikal na balangkas na dinisenyo para gabayan ang responsable na pag-develop, deployment, at operasyon ng mga AI system. Ang mga prinsipyong ito ang gumagabay sa responsableng disenyo, pag-develop, at deployment ng mga AI system, na tinitiyak na ang mga AI teknolohiya ay binuo sa isang paraan na patas, transparent, at inklusibo. Ang mga prinsipyong ito ang pundasyon para sa pagsusuri ng kaligtasan ng mga AI model.

Kabilang sa Mga Prinsipyo ng Responsible AI ng Microsoft ang:

- **Pagkakapantay-pantay at Inklusibidad**: Dapat tratuhin ng mga AI system ang lahat nang patas at iwasan ang pagpapakita ng magkakaibang trato sa mga grupong may magkakatulad na kalagayan. Halimbawa, kapag nagbigay ng gabay ang AI system sa medikal na paggamot, aplikasyon sa pautang, o trabaho, dapat itong magbigay ng parehong rekomendasyon sa lahat ng may kaparehong sintomas, kalagayang pinansyal, o kwalipikasyong propesyonal.

- **Pagkakatiwalaan at Kaligtasan**: Upang makabuo ng tiwala, kritikal na ang mga AI system ay gumana nang maaasahan, ligtas, at pare-pareho. Dapat kaya ng sistemang ito na gumana ayon sa orihinal na disenyo, tumugon nang ligtas sa hindi inaasahang kalagayan, at labanan ang mapaminsalang manipulasyon. Ang kanilang ugali at ang iba't ibang kalagayan na kaya nilang hawakan ay sumasalamin sa saklaw ng mga sitwasyon at kalagayang inasahan ng mga developer noong disenyo at pagsubok.

- **Transparensya**: Kapag tumutulong ang mga AI system sa paggawa ng mga desisyong may malaking epekto sa buhay ng tao, mahalaga na maunawaan ng mga tao kung paano ginawa ang mga desisyong iyon. Halimbawa, maaaring gumamit ang isang bangko ng AI system upang tukuyin kung karapat-dapat ba ang isang tao sa kredito. Maaaring gamitin ng isang kumpanya ang AI upang piliin ang pinaka-kwalipikadong kandidato para sa trabaho.

- **Pribasiya at Seguridad**: Habang lalong dumadami ang paggamit ng AI, ang pagprotekta sa pribasiya at ang seguridad ng personal at pang-negosyong impormasyon ay nagiging mas mahalaga at masalimuot. Sa AI, ang pribasiya at seguridad ng datos ay nangangailangan ng masusing pansin dahil ang pag-access sa datos ay mahalaga para sa AI system upang makagawa ng tumpak at may batayang hula at desisyon tungkol sa mga tao.

- **Panagutan**: Ang mga taong nagdisenyo at nagdeploy ng mga AI system ay dapat managot sa paraan ng kanilang pagpapatakbo. Dapat gamiting ng mga organisasyon ang mga pamantayan sa industriya upang bumuo ng mga norm na panagutan. Ang mga norm na ito ay makasisiguro na ang AI system ay hindi ang huling awtoridad sa anumang desisyon na nakakaapekto sa buhay ng tao. Maaari rin itong masiguro na may makabuluhang kontrol ang tao sa kahit na ang pinaka-autonomous na AI system.

![Fill hub.](../../../../../../translated_images/tl/responsibleai2.c07ef430113fad8c.webp)

*Pinagmulan ng Imahe: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para matuto pa tungkol sa Mga Prinsipyo ng Responsible AI ng Microsoft, bisitahin ang [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Mga sukatan ng kaligtasan

Sa tutorial na ito, susuriin mo ang kaligtasan ng fine-tuned na Phi-3 na modelo gamit ang mga sukatan ng kaligtasan ng Microsoft Foundry. Tinutulungan ka ng mga sukatan na ito na tasahin ang potensyal ng modelo na makagawa ng nakasasamang nilalaman at ang kahinaan nito sa jailbreak attacks. Kabilang sa mga sukatan ng kaligtasan ang:

- **Nilalaman na may kaugnayan sa sariling pinsala**: Tinutukoy kung ang modelo ay may tendensiyang lumikha ng nilalaman na may kinalaman sa self-harm.
- **Mapanirang Nilalaman at Hindi Makatarungang Nilalaman**: Tinutukoy kung ang modelo ay may tendensiyang gumawa ng mapanirang o hindi makatarungang nilalaman.
- **Masantos na Nilalaman**: Tinutukoy kung ang modelo ay may tendensiyang gumawa ng marahas na nilalaman.
- **Seksywal na Nilalaman**: Tinutukoy kung ang modelo ay may tendensiyang gumawa ng hindi angkop na sekswal na nilalaman.

Ang pagsusuri sa mga aspeto na ito ay nagsisiguro na ang AI na modelo ay hindi lumikha ng nakasasama o nakakasakit na nilalaman, na naaayon sa mga pagpapahalaga ng lipunan at mga regulasyong pamantayan.

![Evaluate based on safety.](../../../../../../translated_images/tl/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Panimula sa pagsusuri ng pagganap

Upang matiyak na ang AI na modelo ay gumagana ayon sa inaasahan, mahalagang suriin ang pagganap nito laban sa mga sukatan ng pagganap. Sa Microsoft Foundry, ang mga pagsusuri sa pagganap ay nagbibigay-daan sa iyo na tasahin ang bisa ng iyong modelo sa paggawa ng tama, may kaugnayan, at magkakaugnay na mga tugon.

![Safaty evaluation.](../../../../../../translated_images/tl/performance-evaluation.48b3e7e01a098740.webp)

*Pinagmulan ng Imahe: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Mga sukatan ng pagganap

Sa tutorial na ito, susuriin mo ang pagganap ng fine-tuned na Phi-3 / Phi-3.5 na modelo gamit ang mga sukatan ng pagganap ng Microsoft Foundry. Ang mga sukatan na ito ay tumutulong upang matasa ang bisa ng modelo sa paggawa ng tamang, may kaugnayan, at magkakaugnay na mga tugon. Kabilang sa mga sukatan ng pagganap ang:

- **Groundedness**: Suriin kung gaano kahusay ang mga nilikhang sagot ay nakabatay sa impormasyon mula sa pinagmulan ng input.
- **Relevance**: Suriin ang pagiging angkop ng mga nilikhang tugon sa mga ibinigay na tanong.
- **Coherence**: Suriin kung paano maayos ang daloy ng nilikhang teksto, kung ito ay parang natural na binasa, at kung kahawig ng wika ng tao.
- **Fluency**: Suriin ang kasanayan sa wika ng nilikhang teksto.
- **GPT Similarity**: Ihambing ang nilikhang tugon sa ground truth para sa pagkakapareho.
- **F1 Score**: Kinakalkula ang ratio ng mga salitang magkapareho sa pagitan ng nilikhang tugon at datos ng pinagmulan.

Tinutulungan ka ng mga sukatan na ito na masuri ang bisa ng modelo sa paggawa ng tama, may kaugnayan, at magkakaugnay na mga tugon.

![Evaluate based on performance.](../../../../../../translated_images/tl/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenario 2: Pagsusuri ng Phi-3 / Phi-3.5 na modelo sa Microsoft Foundry**

### Bago ka magsimula

Ang tutorial na ito ay kasunod ng mga naunang blog post, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" at "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Sa mga post na ito, pinuntahan natin ang proseso ng pag-fine-tune ng Phi-3 / Phi-3.5 na modelo sa Microsoft Foundry at ang pag-integrate nito sa Prompt flow.

Sa tutorial na ito, magde-deploy ka ng Azure OpenAI model bilang evaluator sa Microsoft Foundry at gagamitin ito upang suriin ang iyong fine-tuned na Phi-3 / Phi-3.5 na modelo.

Bago simulan ang tutorial na ito, siguraduhing mayroon kang mga sumusunod na kinakailangan, tulad ng inilarawan sa mga naunang tutorial:

1. Isang handang dataset para suriin ang fine-tuned na Phi-3 / Phi-3.5 na modelo.
1. Isang Phi-3 / Phi-3.5 na modelo na na-fine-tune at na-deploy sa Azure Machine Learning.
1. Isang Prompt flow na naka-integrate sa iyong fine-tuned na Phi-3 / Phi-3.5 na modelo sa Microsoft Foundry.

> [!NOTE]
> Gagamitin mo ang *test_data.jsonl* na file, na matatagpuan sa data folder mula sa **ULTRACHAT_200k** dataset na na-download sa mga naunang blog post, bilang dataset para suriin ang fine-tuned na Phi-3 / Phi-3.5 na modelo.

#### I-integrate ang custom na Phi-3 / Phi-3.5 na modelo sa Prompt flow sa Microsoft Foundry (Code first approach)

> [!NOTE]
> Kung sinundan mo ang low-code na paraan na inilarawan sa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", maaari mong laktawan ang pagsasanay na ito at magpatuloy sa susunod.
> Gayunpaman, kung sinundan mo ang code-first na paraan na inilarawan sa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" upang i-fine-tune at i-deploy ang iyong Phi-3 / Phi-3.5 na modelo, ang proseso ng pagkonekta ng iyong modelo sa Prompt flow ay bahagyang naiiba. Matututuhan mo ang prosesong ito sa pagsasanay na ito.

Upang magpatuloy, kailangan mong i-integrate ang fine-tuned na Phi-3 / Phi-3.5 na modelo sa Prompt flow sa Microsoft Foundry.

#### Gumawa ng Microsoft Foundry Hub

Kailangan mong gumawa ng Hub bago gumawa ng Project. Ang Hub ay kumilos na parang isang Resource Group, na nagpapahintulot sa iyo na ayusin at pamahalaan ang maraming Projects sa loob ng Microsoft Foundry.
1. Mag-sign in sa [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Piliin ang **All hubs** mula sa kaliwang tab.

1. Piliin ang **+ New hub** mula sa navigation menu.

    ![Create hub.](../../../../../../translated_images/tl/create-hub.5be78fb1e21ffbf1.webp)

1. Gawin ang mga sumusunod na gawain:

    - Ipasok ang **Hub name**. Dapat ito ay isang natatanging halaga.
    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Location** na nais mong gamitin.
    - Piliin ang **Connect Azure AI Services** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Connect Azure AI Search** sa **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/tl/fill-hub.baaa108495c71e34.webp)

1. Piliin ang **Next**.

#### Gumawa ng Microsoft Foundry Project

1. Sa Hub na iyong ginawa, piliin ang **All projects** mula sa kaliwang tab.

1. Piliin ang **+ New project** mula sa navigation menu.

    ![Select new project.](../../../../../../translated_images/tl/select-new-project.cd31c0404088d7a3.webp)

1. Ipasok ang **Project name**. Dapat ito ay isang natatanging halaga.

    ![Create project.](../../../../../../translated_images/tl/create-project.ca3b71298b90e420.webp)

1. Piliin ang **Create a project**.

#### Magdagdag ng custom connection para sa fine-tuned na Phi-3 / Phi-3.5 model

Upang maisama ang iyong custom na Phi-3 / Phi-3.5 model sa Prompt flow, kailangan mong i-save ang endpoint at key ng model sa isang custom connection. Tinitiyak ng setup na ito ang access sa iyong custom na Phi-3 / Phi-3.5 model sa Prompt flow.

#### Itakda ang api key at endpoint uri ng fine-tuned na Phi-3 / Phi-3.5 model

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure Machine learning workspace na iyong ginawa.

1. Piliin ang **Endpoints** mula sa kaliwang tab.

    ![Select endpoints.](../../../../../../translated_images/tl/select-endpoints.ee7387ecd68bd18d.webp)

1. Piliin ang endpoint na iyong ginawa.

    ![Select endpoints.](../../../../../../translated_images/tl/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Piliin ang **Consume** mula sa navigation menu.

1. Kopyahin ang iyong **REST endpoint** at **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/tl/copy-endpoint-key.0650c3786bd646ab.webp)

#### Idagdag ang Custom Connection

1. Bisitahin ang [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Microsoft Foundry project na iyong ginawa.

1. Sa Project na iyong ginawa, piliin ang **Settings** mula sa kaliwang tab.

1. Piliin ang **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/tl/select-new-connection.fa0f35743758a74b.webp)

1. Piliin ang **Custom keys** mula sa navigation menu.

    ![Select custom keys.](../../../../../../translated_images/tl/select-custom-keys.5a3c6b25580a9b67.webp)

1. Gawin ang mga sumusunod na gawain:

    - Piliin ang **+ Add key value pairs**.
    - Para sa key name, ilagay ang **endpoint** at i-paste ang endpoint na kinopya mo mula sa Azure ML Studio sa value field.
    - Piliin muli ang **+ Add key value pairs**.
    - Para sa key name, ilagay ang **key** at i-paste ang key na kinopya mo mula sa Azure ML Studio sa value field.
    - Pagkatapos magdagdag ng mga key, piliin ang **is secret** upang hindi maipakita ang key.

    ![Add connection.](../../../../../../translated_images/tl/add-connection.ac7f5faf8b10b0df.webp)

1. Piliin ang **Add connection**.

#### Gumawa ng Prompt flow

Nagdagdag ka na ng custom connection sa Microsoft Foundry. Ngayon, gumawa tayo ng Prompt flow gamit ang mga sumusunod na hakbang. Pagkatapos, ikokonekta mo ang Prompt flow na ito sa custom connection para gamitin ang fine-tuned na model sa loob ng Prompt flow.

1. Pumunta sa Microsoft Foundry project na iyong ginawa.

1. Piliin ang **Prompt flow** mula sa kaliwang tab.

1. Piliin ang **+ Create** mula sa navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/tl/select-promptflow.18ff2e61ab9173eb.webp)

1. Piliin ang **Chat flow** mula sa navigation menu.

    ![Select chat flow.](../../../../../../translated_images/tl/select-flow-type.28375125ec9996d3.webp)

1. Ipasok ang **Folder name** na gagamitin.

    ![Select chat flow.](../../../../../../translated_images/tl/enter-name.02ddf8fb840ad430.webp)

1. Piliin ang **Create**.

#### I-setup ang Prompt flow para makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model

Kailangan mong isama ang fine-tuned na Phi-3 / Phi-3.5 model sa isang Prompt flow. Gayunpaman, ang kasalukuyang Prompt flow na ibinigay ay hindi idinisenyo para dito. Kaya, kailangan mong muling idisenyo ang Prompt flow upang paganahin ang pagsasama ng custom na model.

1. Sa Prompt flow, gawin ang mga sumusunod para muling buuin ang kasalukuyang flow:

    - Piliin ang **Raw file mode**.
    - Burahin ang lahat ng umiiral na code sa *flow.dag.yml* na file.
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

    ![Select raw file mode.](../../../../../../translated_images/tl/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Idagdag ang sumusunod na code sa *integrate_with_promptflow.py* upang gamitin ang custom na Phi-3 / Phi-3.5 model sa Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Pagsasaayos ng pag-log
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

        # Ang "connection" ay ang pangalan ng Custom Connection, ang "endpoint", "key" ay mga keys sa Custom Connection
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
            
            # I-log ang buong tugon ng JSON
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

    ![Paste prompt flow code.](../../../../../../translated_images/tl/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Para sa mas detalyadong impormasyon sa paggamit ng Prompt flow sa Microsoft Foundry, maaari mong tingnan ang [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Piliin ang **Chat input**, **Chat output** upang paganahin ang chat sa iyong model.

    ![Select Input Output.](../../../../../../translated_images/tl/select-input-output.c187fc58f25fbfc3.webp)

1. Handa ka nang makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model. Sa susunod na ehersisyo, matututunan mo kung paano simulan ang Prompt flow at gamitin ito upang makipag-chat sa iyong fine-tuned na Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> Ang muling binuong flow ay dapat magmukhang tulad ng larawang ito:
>
> ![Flow example](../../../../../../translated_images/tl/graph-example.82fd1bcdd3fc545b.webp)
>

#### Simulan ang Prompt flow

1. Piliin ang **Start compute sessions** upang simulan ang Prompt flow.

    ![Start compute session.](../../../../../../translated_images/tl/start-compute-session.9acd8cbbd2c43df1.webp)

1. Piliin ang **Validate and parse input** upang i-renew ang mga parameter.

    ![Validate input.](../../../../../../translated_images/tl/validate-input.c1adb9543c6495be.webp)

1. Piliin ang **Value** ng **connection** papunta sa custom connection na iyong ginawa. Halimbawa, *connection*.

    ![Connection.](../../../../../../translated_images/tl/select-connection.1f2b59222bcaafef.webp)

#### Makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model

1. Piliin ang **Chat**.

    ![Select chat.](../../../../../../translated_images/tl/select-chat.0406bd9687d0c49d.webp)

1. Narito ang halimbawa ng mga resulta: Ngayon, maaari ka nang makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model. Inirerekomenda na magtanong base sa data na ginamit para sa fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/tl/chat-with-promptflow.1cf8cea112359ada.webp)

### I-deploy ang Azure OpenAI upang suriin ang Phi-3 / Phi-3.5 model

Upang suriin ang Phi-3 / Phi-3.5 model sa Microsoft Foundry, kailangan mong mag-deploy ng Azure OpenAI model. Ang modelong ito ay gagamitin upang suriin ang performance ng Phi-3 / Phi-3.5 model.

#### I-deploy ang Azure OpenAI

1. Mag-sign in sa [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Microsoft Foundry project na iyong ginawa.

    ![Select Project.](../../../../../../translated_images/tl/select-project-created.5221e0e403e2c9d6.webp)

1. Sa Project na iyong ginawa, piliin ang **Deployments** mula sa kaliwang tab.

1. Piliin ang **+ Deploy model** mula sa navigation menu.

1. Piliin ang **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/tl/deploy-openai-model.95d812346b25834b.webp)

1. Piliin ang Azure OpenAI model na nais mong gamitin. Halimbawa, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/tl/select-openai-model.959496d7e311546d.webp)

1. Piliin ang **Confirm**.

### Suriin ang fine-tuned na Phi-3 / Phi-3.5 model gamit ang Prompt flow evaluation ng Microsoft Foundry

### Magsimula ng bagong pagsusuri

1. Bisitahin ang [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Microsoft Foundry project na iyong ginawa.

    ![Select Project.](../../../../../../translated_images/tl/select-project-created.5221e0e403e2c9d6.webp)

1. Sa Project na iyong ginawa, piliin ang **Evaluation** mula sa kaliwang tab.

1. Piliin ang **+ New evaluation** mula sa navigation menu.

    ![Select evaluation.](../../../../../../translated_images/tl/select-evaluation.2846ad7aaaca7f4f.webp)

1. Piliin ang **Prompt flow** evaluation.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/tl/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Gawin ang mga sumusunod:

    - Ipasok ang pangalan ng pagsusuri. Dapat ito ay isang natatanging halaga.
    - Piliin ang **Question and answer without context** bilang uri ng gawain. Dahil, ang **UlTRACHAT_200k** dataset na ginamit sa tutorial na ito ay walang context.
    - Piliin ang prompt flow na nais mong suriin.

    ![Prompt flow evaluation.](../../../../../../translated_images/tl/evaluation-setting1.4aa08259ff7a536e.webp)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod:

    - Piliin ang **Add your dataset** upang i-upload ang dataset. Halimbawa, maaari mong i-upload ang test dataset file, tulad ng *test_data.json1*, na kasama kapag dina-download mo ang **ULTRACHAT_200k** dataset.
    - Piliin ang angkop na **Dataset column** na tumutugma sa iyong dataset. Halimbawa, kung ginagamit mo ang **ULTRACHAT_200k** dataset, piliin ang **${data.prompt}** bilang dataset column.

    ![Prompt flow evaluation.](../../../../../../translated_images/tl/evaluation-setting2.07036831ba58d64e.webp)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod upang i-configure ang performance at quality metrics:

    - Piliin ang performance at quality metrics na nais mong gamitin.
    - Piliin ang Azure OpenAI model na iyong ginawa para sa pagsusuri. Halimbawa, piliin ang **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/tl/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Gawin ang mga sumusunod upang i-configure ang risk at safety metrics:

    - Piliin ang risk at safety metrics na nais mong gamitin.
    - Piliin ang threshold upang kalkulahin ang defect rate na nais mong gamitin. Halimbawa, piliin ang **Medium**.
    - Para sa **question**, piliin ang **Data source** sa **{$data.prompt}**.
    - Para sa **answer**, piliin ang **Data source** sa **{$run.outputs.answer}**.
    - Para sa **ground_truth**, piliin ang **Data source** sa **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/tl/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Piliin ang **Next**.

1. Piliin ang **Submit** upang simulan ang pagsusuri.

1. Aabutin ng ilang panahon ang pagsusuri upang matapos. Maaari mong subaybayan ang progreso sa tab na **Evaluation**.

### Suriin ang Resulta ng Pagsusuri

> [!NOTE]
> Ang mga resulta na ipinakita sa ibaba ay nilalayong ipakita ang proseso ng pagsusuri. Sa tutorial na ito, gumamit tayo ng model na fine-tuned sa isang medyo maliit na dataset, na maaaring magdulot ng hindi optimal na mga resulta. Ang aktwal na mga resulta ay maaaring magkaiba nang malaki depende sa laki, kalidad, at pagkakaiba-iba ng dataset na ginamit, pati na rin sa espesipikong configuration ng model.  
>
> Kapag natapos na ang pagsusuri, maaari mong repasuhin ang mga resulta para sa parehong performance at safety metrics.
1. Mga metric ng pagganap at kalidad:

    - suriin ang bisa ng modelo sa paglikha ng magkakaugnay, malinis, at may kaugnayang mga tugon.

    ![Evaluation result.](../../../../../../translated_images/tl/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Mga metric ng panganib at kaligtasan:

    - Tiyakin na ang mga output ng modelo ay ligtas at naaayon sa mga Prinsipyo ng Responsable AI, na iniiwasan ang anumang mapanganib o nakakasakit na nilalaman.

    ![Evaluation result.](../../../../../../translated_images/tl/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Maaari kang mag-scroll pababa para makita ang **Detalyadong resulta ng metric**.

    ![Evaluation result.](../../../../../../translated_images/tl/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Sa pamamagitan ng pagsusuri ng iyong custom na Phi-3 / Phi-3.5 na modelo laban sa parehong metric ng pagganap at kaligtasan, makakapagkumpirma ka na ang modelo ay hindi lamang epektibo, kundi sumusunod din sa mga responsableng kasanayan sa AI, na handa nang gamitin sa totoong mundo.

## Binabati kita!

### Nakumpleto mo na ang tutorial na ito

Matagumpay mong nasuri ang fine-tuned na Phi-3 na modelo na isinama sa Prompt flow sa Microsoft Foundry. Ito ay isang mahalagang hakbang upang matiyak na ang iyong mga AI na modelo ay hindi lamang mahusay sa pagganap, kundi sumusunod din sa mga Prinsipyo ng Responsable AI ng Microsoft upang matulungan kang bumuo ng mapagkakatiwalaan at maaasahang mga application ng AI.

![Architecture.](../../../../../../translated_images/tl/architecture.10bec55250f5d6a4.webp)

## Linisin ang mga Azure Resources

Linisin ang iyong mga Azure resources upang maiwasan ang karagdagang singil sa iyong account. Pumunta sa Azure portal at tanggalin ang mga sumusunod na resources:

- Ang Azure Machine learning resource.
- Ang Azure Machine learning model endpoint.
- Ang Microsoft Foundry Project resource.
- Ang Microsoft Foundry Prompt flow resource.

### Mga Susunod na Hakbang

#### Dokumentasyon

- [Suriin ang mga sistema ng AI gamit ang Responsable AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metrics sa pagsusuri at pag-monitor para sa generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentasyon ng Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentasyon ng Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Nilalaman ng Pagsasanay

- [Panimula sa Responsable AI Approach ng Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Panimula sa Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Sanggunian

- [Ano ang Responsable AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Pag-aanunsyo ng mga bagong kagamitan sa Azure AI upang matulungan kang bumuo ng mas secure at mapagkakatiwalaang generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Pagsusuri ng mga generative AI application](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagsisiwalat**:  
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o mga di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang mga maling pagkaunawa o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->