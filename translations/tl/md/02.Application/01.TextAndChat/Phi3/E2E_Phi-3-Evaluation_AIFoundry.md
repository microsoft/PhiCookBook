<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:49:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "tl"
}
-->
# Evaluate the Fine-tuned Phi-3 / Phi-3.5 Model in Azure AI Foundry Focusing on Microsoft's Responsible AI Principles

Ang end-to-end (E2E) na halimbawa na ito ay batay sa gabay na "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" mula sa Microsoft Tech Community.

## Pangkalahatang-ideya

### Paano mo masusuri ang kaligtasan at pagganap ng fine-tuned na Phi-3 / Phi-3.5 na modelo sa Azure AI Foundry?

Ang fine-tuning ng isang modelo ay maaaring magdulot ng hindi inaasahan o hindi kanais-nais na mga tugon. Upang matiyak na nananatiling ligtas at epektibo ang modelo, mahalagang suriin ang potensyal nito na makabuo ng mapanganib na nilalaman at ang kakayahan nitong magbigay ng tumpak, may kaugnayan, at magkakaugnay na mga sagot. Sa tutorial na ito, matututuhan mo kung paano suriin ang kaligtasan at pagganap ng fine-tuned na Phi-3 / Phi-3.5 na modelo na naka-integrate sa Prompt flow sa Azure AI Foundry.

Narito ang proseso ng pagsusuri ng Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.tl.png)

*Pinagmulan ng Larawan: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para sa mas detalyadong impormasyon at upang tuklasin ang karagdagang mga mapagkukunan tungkol sa Phi-3 / Phi-3.5, bisitahin ang [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Mga Kinakailangan

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned na Phi-3 / Phi-3.5 na modelo

### Talaan ng Nilalaman

1. [**Scenario 1: Panimula sa Azure AI Foundry's Prompt flow evaluation**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Panimula sa pagsusuri ng kaligtasan](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Panimula sa pagsusuri ng pagganap](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Pagsusuri sa Phi-3 / Phi-3.5 na modelo sa Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Bago ka magsimula](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [I-deploy ang Azure OpenAI para suriin ang Phi-3 / Phi-3.5 na modelo](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Suriin ang fine-tuned na Phi-3 / Phi-3.5 na modelo gamit ang Azure AI Foundry's Prompt flow evaluation](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Congratulations!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Panimula sa Azure AI Foundry's Prompt flow evaluation**

### Panimula sa pagsusuri ng kaligtasan

Upang matiyak na ang iyong AI na modelo ay etikal at ligtas, mahalagang suriin ito batay sa Microsoft's Responsible AI Principles. Sa Azure AI Foundry, pinapayagan ka ng pagsusuri sa kaligtasan na suriin ang kahinaan ng iyong modelo sa jailbreak attacks at ang potensyal nito na makabuo ng mapanganib na nilalaman, na direktang nakaayon sa mga prinsipyong ito.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.tl.png)

*Pinagmulan ng Larawan: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft's Responsible AI Principles

Bago simulan ang mga teknikal na hakbang, mahalagang maunawaan ang Microsoft's Responsible AI Principles, isang etikal na balangkas na dinisenyo upang gabayan ang responsableng pagbuo, pag-deploy, at operasyon ng mga AI system. Ang mga prinsipyong ito ang gumagabay sa responsableng disenyo, pagbuo, at pag-deploy ng mga AI system, na tinitiyak na ang mga teknolohiyang AI ay ginawa sa paraang patas, transparent, at inklusibo. Ang mga prinsipyong ito ang pundasyon sa pagsusuri ng kaligtasan ng mga AI na modelo.

Kasama sa Microsoft's Responsible AI Principles ang:

- **Katarungan at Pagkakasama**: Dapat tratuhin ng mga AI system ang lahat nang patas at iwasang makaapekto nang magkakaiba sa mga grupong may katulad na kalagayan. Halimbawa, kapag nagbibigay ang mga AI system ng gabay sa medikal na paggamot, aplikasyon sa pautang, o trabaho, dapat silang magbigay ng parehong rekomendasyon sa lahat ng may katulad na sintomas, kalagayang pinansyal, o kwalipikasyong propesyonal.

- **Pagkakatiwalaan at Kaligtasan**: Upang makabuo ng tiwala, mahalaga na ang mga AI system ay gumana nang maaasahan, ligtas, at pare-pareho. Dapat nilang magampanan ang kanilang orihinal na disenyo, tumugon nang ligtas sa mga hindi inaasahang kondisyon, at labanan ang mapanirang manipulasyon. Ang kanilang kilos at ang iba't ibang kondisyon na kaya nilang harapin ay sumasalamin sa mga sitwasyon at kalagayan na inasahan ng mga developer sa panahon ng disenyo at pagsubok.

- **Kalinawan**: Kapag tumutulong ang mga AI system sa paggawa ng mga desisyong may malaking epekto sa buhay ng mga tao, mahalagang maunawaan ng mga tao kung paano ginawa ang mga desisyong iyon. Halimbawa, maaaring gumamit ang isang bangko ng AI system upang tukuyin kung karapat-dapat ba ang isang tao sa kredito. Maaaring gumamit ang isang kumpanya ng AI system upang piliin ang pinaka-karapat-dapat na mga kandidato para sa trabaho.

- **Pribasiya at Seguridad**: Habang lumalaganap ang AI, ang pagprotekta sa pribasiya at seguridad ng personal at pang-negosyong impormasyon ay nagiging mas mahalaga at masalimuot. Sa AI, nangangailangan ng masusing pansin ang pribasiya at seguridad ng datos dahil mahalaga ang access sa datos para makagawa ang mga AI system ng tumpak at may kaalamang mga prediksyon at desisyon tungkol sa mga tao.

- **Panagutan**: Ang mga taong nagdisenyo at nag-deploy ng mga AI system ay dapat managot sa kung paano gumagana ang kanilang mga sistema. Dapat gumamit ang mga organisasyon ng mga pamantayan sa industriya upang bumuo ng mga normang panagutan. Ang mga normang ito ay makasisiguro na ang mga AI system ay hindi ang huling awtoridad sa anumang desisyong nakakaapekto sa buhay ng mga tao. Makasisiguro rin ito na nananatili ang makabuluhang kontrol ng tao sa mga AI system na mataas ang antas ng awtonomiya.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.tl.png)

*Pinagmulan ng Larawan: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para matuto pa tungkol sa Microsoft's Responsible AI Principles, bisitahin ang [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Mga sukatan sa kaligtasan

Sa tutorial na ito, susuriin mo ang kaligtasan ng fine-tuned na Phi-3 na modelo gamit ang mga safety metrics ng Azure AI Foundry. Tinutulungan ka ng mga sukatan na ito na tasahin ang potensyal ng modelo na makabuo ng mapanganib na nilalaman at ang kahinaan nito sa jailbreak attacks. Kasama sa mga safety metrics ang:

- **Nilalaman na may kaugnayan sa self-harm**: Sinusuri kung may tendensiya ang modelo na gumawa ng nilalaman na may kaugnayan sa self-harm.
- **Mapanirang Nilalaman at Hindi Makatarungang Nilalaman**: Sinusuri kung may tendensiya ang modelo na gumawa ng mapanirang o hindi makatarungang nilalaman.
- **Marahas na Nilalaman**: Sinusuri kung may tendensiya ang modelo na gumawa ng marahas na nilalaman.
- **Nilalamang Sekswal**: Sinusuri kung may tendensiya ang modelo na gumawa ng hindi angkop na nilalamang sekswal.

Ang pagsusuri sa mga aspetong ito ay nagsisiguro na ang AI na modelo ay hindi makabubuo ng mapanganib o nakakasakit na nilalaman, na naaayon sa mga panlipunang halaga at mga regulasyong pamantayan.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.tl.png)

### Panimula sa pagsusuri ng pagganap

Upang matiyak na ang iyong AI na modelo ay gumaganap ayon sa inaasahan, mahalagang suriin ang pagganap nito batay sa mga performance metrics. Sa Azure AI Foundry, pinapayagan ka ng pagsusuri sa pagganap na tasahin ang bisa ng iyong modelo sa paggawa ng tumpak, may kaugnayan, at magkakaugnay na mga tugon.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.tl.png)

*Pinagmulan ng Larawan: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Mga sukatan sa pagganap

Sa tutorial na ito, susuriin mo ang pagganap ng fine-tuned na Phi-3 / Phi-3.5 na modelo gamit ang mga performance metrics ng Azure AI Foundry. Tinutulungan ka ng mga sukatan na ito na tasahin ang bisa ng modelo sa paggawa ng tumpak, may kaugnayan, at magkakaugnay na mga tugon. Kasama sa mga performance metrics ang:

- **Groundedness**: Sinusuri kung gaano kahusay ang mga sagot na ginawa ay nakaayon sa impormasyon mula sa pinanggalingang datos.
- **Relevance**: Sinusuri ang kaugnayan ng mga sagot sa mga ibinigay na tanong.
- **Coherence**: Sinusuri kung gaano kakinis ang daloy ng teksto, kung ito ay natural na binabasa, at kung kahawig ng wikang ginagamit ng tao.
- **Fluency**: Sinusuri ang kahusayan sa wika ng teksto na ginawa.
- **GPT Similarity**: Kinukumpara ang sagot na ginawa sa totoong datos para sa pagkakatulad.
- **F1 Score**: Kinakalkula ang proporsyon ng mga salitang pareho sa sagot na ginawa at sa pinanggalingang datos.

Tinutulungan ka ng mga sukatan na ito na tasahin ang bisa ng modelo sa paggawa ng tumpak, may kaugnayan, at magkakaugnay na mga tugon.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.tl.png)

## **Scenario 2: Pagsusuri sa Phi-3 / Phi-3.5 na modelo sa Azure AI Foundry**

### Bago ka magsimula

Ang tutorial na ito ay karugtong ng mga naunang blog post, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" at "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Sa mga post na ito, tinahak natin ang proseso ng fine-tuning ng Phi-3 / Phi-3.5 na modelo sa Azure AI Foundry at ang pag-integrate nito sa Prompt flow.

Sa tutorial na ito, magde-deploy ka ng Azure OpenAI na modelo bilang evaluator sa Azure AI Foundry at gagamitin ito upang suriin ang iyong fine-tuned na Phi-3 / Phi-3.5 na modelo.

Bago simulan ang tutorial na ito, siguraduhing mayroon kang mga sumusunod na kinakailangan, tulad ng inilalarawan sa mga naunang tutorial:

1. Isang handang dataset para suriin ang fine-tuned na Phi-3 / Phi-3.5 na modelo.
1. Isang Phi-3 / Phi-3.5 na modelo na na-fine-tune at na-deploy sa Azure Machine Learning.
1. Isang Prompt flow na naka-integrate sa iyong fine-tuned na Phi-3 / Phi-3.5 na modelo sa Azure AI Foundry.

> [!NOTE]
> Gagamitin mo ang *test_data.jsonl* na file, na matatagpuan sa data folder mula sa **ULTRACHAT_200k** dataset na na-download sa mga naunang blog post, bilang dataset para suriin ang fine-tuned na Phi-3 / Phi-3.5 na modelo.

#### I-integrate ang custom na Phi-3 / Phi-3.5 na modelo sa Prompt flow sa Azure AI Foundry (Code first approach)
> [!NOTE]
> Kung sinunod mo ang low-code na paraan na inilarawan sa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", maaari mong laktawan ang pagsasanay na ito at magpatuloy sa susunod.
> Ngunit, kung sinunod mo ang code-first na paraan na inilarawan sa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para i-fine-tune at i-deploy ang iyong Phi-3 / Phi-3.5 na modelo, bahagyang iba ang proseso ng pagkonekta ng iyong modelo sa Prompt flow. Malalaman mo ang prosesong ito sa pagsasanay na ito.
Para magpatuloy, kailangan mong i-integrate ang iyong fine-tuned na Phi-3 / Phi-3.5 model sa Prompt flow sa Azure AI Foundry.

#### Gumawa ng Azure AI Foundry Hub

Kailangan mong gumawa ng Hub bago gumawa ng Project. Ang Hub ay parang Resource Group, na nagbibigay-daan sa iyo upang ayusin at pamahalaan ang maraming Projects sa loob ng Azure AI Foundry.

1. Mag-sign in sa [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Piliin ang **All hubs** mula sa kaliwang tab.

1. Piliin ang **+ New hub** mula sa navigation menu.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.tl.png)

1. Gawin ang mga sumusunod na hakbang:

    - Ilagay ang **Hub name**. Dapat ito ay natatanging pangalan.
    - Piliin ang iyong Azure **Subscription**.
    - Piliin ang **Resource group** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Location** na nais mong gamitin.
    - Piliin ang **Connect Azure AI Services** na gagamitin (gumawa ng bago kung kinakailangan).
    - Piliin ang **Connect Azure AI Search** sa **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.tl.png)

1. Piliin ang **Next**.

#### Gumawa ng Azure AI Foundry Project

1. Sa Hub na ginawa mo, piliin ang **All projects** mula sa kaliwang tab.

1. Piliin ang **+ New project** mula sa navigation menu.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.tl.png)

1. Ilagay ang **Project name**. Dapat ito ay natatanging pangalan.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.tl.png)

1. Piliin ang **Create a project**.

#### Magdagdag ng custom connection para sa fine-tuned na Phi-3 / Phi-3.5 model

Para i-integrate ang iyong custom na Phi-3 / Phi-3.5 model sa Prompt flow, kailangan mong i-save ang endpoint at key ng model sa isang custom connection. Tinitiyak ng setup na ito ang access sa iyong custom na Phi-3 / Phi-3.5 model sa Prompt flow.

#### Itakda ang api key at endpoint uri ng fine-tuned na Phi-3 / Phi-3.5 model

1. Bisitahin ang [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure Machine learning workspace na ginawa mo.

1. Piliin ang **Endpoints** mula sa kaliwang tab.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.tl.png)

1. Piliin ang endpoint na ginawa mo.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.tl.png)

1. Piliin ang **Consume** mula sa navigation menu.

1. Kopyahin ang iyong **REST endpoint** at **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.tl.png)

#### Idagdag ang Custom Connection

1. Bisitahin ang [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure AI Foundry project na ginawa mo.

1. Sa Project na ginawa mo, piliin ang **Settings** mula sa kaliwang tab.

1. Piliin ang **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.tl.png)

1. Piliin ang **Custom keys** mula sa navigation menu.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.tl.png)

1. Gawin ang mga sumusunod:

    - Piliin ang **+ Add key value pairs**.
    - Para sa pangalan ng key, ilagay ang **endpoint** at i-paste ang endpoint na kinopya mo mula sa Azure ML Studio sa value field.
    - Piliin muli ang **+ Add key value pairs**.
    - Para sa pangalan ng key, ilagay ang **key** at i-paste ang key na kinopya mo mula sa Azure ML Studio sa value field.
    - Pagkatapos maidagdag ang mga keys, piliin ang **is secret** upang hindi makita ang key.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.tl.png)

1. Piliin ang **Add connection**.

#### Gumawa ng Prompt flow

Nagdagdag ka na ng custom connection sa Azure AI Foundry. Ngayon, gumawa tayo ng Prompt flow gamit ang mga sumusunod na hakbang. Pagkatapos, ikokonekta mo ang Prompt flow na ito sa custom connection para magamit ang fine-tuned na model sa loob ng Prompt flow.

1. Pumunta sa Azure AI Foundry project na ginawa mo.

1. Piliin ang **Prompt flow** mula sa kaliwang tab.

1. Piliin ang **+ Create** mula sa navigation menu.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.tl.png)

1. Piliin ang **Chat flow** mula sa navigation menu.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.tl.png)

1. Ilagay ang **Folder name** na gagamitin.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.tl.png)

1. Piliin ang **Create**.

#### I-setup ang Prompt flow para makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model

Kailangan mong i-integrate ang fine-tuned na Phi-3 / Phi-3.5 model sa isang Prompt flow. Ngunit, ang kasalukuyang Prompt flow na ibinigay ay hindi disenyo para dito. Kaya, kailangan mong baguhin ang Prompt flow para payagan ang integration ng custom na model.

1. Sa Prompt flow, gawin ang mga sumusunod upang muling buuin ang kasalukuyang flow:

    - Piliin ang **Raw file mode**.
    - Burahin lahat ng umiiral na code sa *flow.dag.yml* na file.
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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.tl.png)

1. Idagdag ang sumusunod na code sa *integrate_with_promptflow.py* para magamit ang custom na Phi-3 / Phi-3.5 model sa Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.tl.png)

> [!NOTE]
> Para sa mas detalyadong impormasyon tungkol sa paggamit ng Prompt flow sa Azure AI Foundry, maaari mong tingnan ang [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Piliin ang **Chat input**, **Chat output** para paganahin ang chat sa iyong model.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.tl.png)

1. Handa ka na ngayong makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model. Sa susunod na ehersisyo, matututuhan mo kung paano simulan ang Prompt flow at gamitin ito para makipag-chat sa iyong fine-tuned na Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> Ang muling binuong flow ay dapat magmukhang ganito:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.tl.png)
>

#### Simulan ang Prompt flow

1. Piliin ang **Start compute sessions** para simulan ang Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.tl.png)

1. Piliin ang **Validate and parse input** para i-renew ang mga parameter.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.tl.png)

1. Piliin ang **Value** ng **connection** sa custom connection na ginawa mo. Halimbawa, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.tl.png)

#### Makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model

1. Piliin ang **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.tl.png)

1. Narito ang halimbawa ng resulta: Ngayon ay maaari ka nang makipag-chat sa iyong custom na Phi-3 / Phi-3.5 model. Inirerekomenda na magtanong base sa data na ginamit sa fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.tl.png)

### I-deploy ang Azure OpenAI para suriin ang Phi-3 / Phi-3.5 model

Para suriin ang Phi-3 / Phi-3.5 model sa Azure AI Foundry, kailangan mong i-deploy ang isang Azure OpenAI model. Gagamitin ang modelong ito para suriin ang performance ng Phi-3 / Phi-3.5 model.

#### I-deploy ang Azure OpenAI

1. Mag-sign in sa [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure AI Foundry project na ginawa mo.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.tl.png)

1. Sa Project na ginawa mo, piliin ang **Deployments** mula sa kaliwang tab.

1. Piliin ang **+ Deploy model** mula sa navigation menu.

1. Piliin ang **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.tl.png)

1. Piliin ang Azure OpenAI model na nais mong gamitin. Halimbawa, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.tl.png)

1. Piliin ang **Confirm**.

### Suriin ang fine-tuned na Phi-3 / Phi-3.5 model gamit ang Prompt flow evaluation ng Azure AI Foundry

### Magsimula ng bagong pagsusuri

1. Bisitahin ang [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pumunta sa Azure AI Foundry project na ginawa mo.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.tl.png)

1. Sa Project na ginawa mo, piliin ang **Evaluation** mula sa kaliwang tab.

1. Piliin ang **+ New evaluation** mula sa navigation menu.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.tl.png)

1. Piliin ang **Prompt flow** evaluation.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.tl.png)

1. Gawin ang mga sumusunod:

    - Ilagay ang pangalan ng evaluation. Dapat ito ay natatanging pangalan.
    - Piliin ang **Question and answer without context** bilang uri ng gawain. Dahil, ang **ULTRACHAT_200k** dataset na ginamit sa tutorial na ito ay walang context.
    - Piliin ang prompt flow na nais mong suriin.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.tl.png)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod:

    - Piliin ang **Add your dataset** para i-upload ang dataset. Halimbawa, maaari mong i-upload ang test dataset file, tulad ng *test_data.json1*, na kasama kapag dine-download mo ang **ULTRACHAT_200k** dataset.
    - Piliin ang angkop na **Dataset column** na tumutugma sa iyong dataset. Halimbawa, kung ginagamit mo ang **ULTRACHAT_200k** dataset, piliin ang **${data.prompt}** bilang dataset column.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.tl.png)

1. Piliin ang **Next**.

1. Gawin ang mga sumusunod para i-configure ang performance at quality metrics:

    - Piliin ang performance at quality metrics na nais mong gamitin.
    - Piliin ang Azure OpenAI model na ginawa mo para sa pagsusuri. Halimbawa, piliin ang **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.tl.png)

1. Gawin ang mga sumusunod para i-configure ang risk at safety metrics:

    - Piliin ang risk at safety metrics na nais mong gamitin.
    - Piliin ang threshold para kalkulahin ang defect rate na nais mong gamitin. Halimbawa, piliin ang **Medium**.
    - Para sa **question**, piliin ang **Data source** sa **{$data.prompt}**.
    - Para sa **answer**, piliin ang **Data source** sa **{$run.outputs.answer}**.
    - Para sa **ground_truth**, piliin ang **Data source** sa **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.tl.png)

1. Piliin ang **Next**.

1. Piliin ang **Submit** para simulan ang pagsusuri.

1. Aabutin ng ilang sandali ang pagsusuri bago matapos. Maaari mong subaybayan ang progreso sa tab na **Evaluation**.

### Suriin ang Resulta ng Pagsusuri
> [!NOTE]
> Ang mga resulta na ipinakita sa ibaba ay layuning ipakita ang proseso ng pagsusuri. Sa tutorial na ito, gumamit kami ng modelong na-fine-tune sa isang medyo maliit na dataset, kaya maaaring magdulot ito ng hindi ganap na pinakamainam na mga resulta. Ang aktwal na mga resulta ay maaaring mag-iba nang malaki depende sa laki, kalidad, at pagkakaiba-iba ng dataset na ginamit, pati na rin sa partikular na konfigurasyon ng modelo.
Kapag natapos na ang pagsusuri, maaari mong tingnan ang mga resulta para sa parehong performance at safety metrics.

1. Mga sukatan ng performance at kalidad:

    - suriin ang bisa ng modelo sa pagbuo ng magkakaugnay, maayos, at may kaugnayang mga sagot.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.tl.png)

1. Mga sukatan ng panganib at kaligtasan:

    - Tiyakin na ang mga output ng modelo ay ligtas at sumusunod sa Responsible AI Principles, iwasan ang anumang mapanganib o nakakasakit na nilalaman.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.tl.png)

1. Maaari kang mag-scroll pababa upang makita ang **Detalyadong resulta ng mga sukatan**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.tl.png)

1. Sa pamamagitan ng pagsusuri ng iyong custom na Phi-3 / Phi-3.5 na modelo laban sa parehong performance at safety metrics, makukumpirma mo na ang modelo ay hindi lamang epektibo, kundi sumusunod din sa mga responsableng AI na praktis, kaya handa na itong gamitin sa totoong mundo.

## Binabati kita!

### Natapos mo na ang tutorial na ito

Matagumpay mong nasuri ang fine-tuned na Phi-3 na modelo na isinama sa Prompt flow sa Azure AI Foundry. Ito ay isang mahalagang hakbang upang matiyak na ang iyong mga AI na modelo ay hindi lamang mahusay ang performance, kundi sumusunod din sa mga prinsipyo ng Responsible AI ng Microsoft upang matulungan kang bumuo ng mapagkakatiwalaan at maaasahang mga AI application.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.tl.png)

## Linisin ang mga Azure Resources

Linisin ang iyong mga Azure resources upang maiwasan ang karagdagang singil sa iyong account. Pumunta sa Azure portal at tanggalin ang mga sumusunod na resources:

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

#### Nilalaman ng Pagsasanay

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Sanggunian

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.