<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:43:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "fi"
}
-->
# Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryssa keskittyen Microsoftin vastuullisen tekoälyn periaatteisiin

Tämä kokonaisvaltainen (E2E) esimerkki perustuu Microsoft Tech Communityn oppaaseen "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)".

## Yleiskatsaus

### Miten voit arvioida hienosäädetyn Phi-3 / Phi-3.5 -mallin turvallisuutta ja suorituskykyä Azure AI Foundryssa?

Mallin hienosäätö voi joskus johtaa tahattomiin tai ei-toivottuihin vastauksiin. Jotta malli pysyy turvallisena ja tehokkaana, on tärkeää arvioida sen kyky tuottaa haitallista sisältöä sekä sen kyky antaa tarkkoja, asiaankuuluvia ja johdonmukaisia vastauksia. Tässä opetusohjelmassa opit, miten arvioida hienosäädetyn Phi-3 / Phi-3.5 -mallin turvallisuutta ja suorituskykyä, kun se on integroitu Prompt flow -työkaluun Azure AI Foundryssa.

Tässä on Azure AI Foundryn arviointiprosessi.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.fi.png)

*Kuvan lähde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Lisätietoja ja lisäresursseja Phi-3 / Phi-3.5 -malleista löydät [Phi-3CookBookista](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Esivaatimukset

- [Python](https://www.python.org/downloads)
- [Azure-tilaus](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Hienosäädetty Phi-3 / Phi-3.5 -malli

### Sisällysluettelo

1. [**Tapaus 1: Johdatus Azure AI Foundryn Prompt flow -arviointiin**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Johdatus turvallisuusarviointiin](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Johdatus suorituskyvyn arviointiin](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Tapaus 2: Phi-3 / Phi-3.5 -mallin arviointi Azure AI Foundryssa**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Ennen aloittamista](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ota Azure OpenAI käyttöön Phi-3 / Phi-3.5 -mallin arviointia varten](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryn Prompt flow -arvioinnilla](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Onnittelut!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Tapaus 1: Johdatus Azure AI Foundryn Prompt flow -arviointiin**

### Johdatus turvallisuusarviointiin

Jotta tekoälymallisi olisi eettinen ja turvallinen, on tärkeää arvioida sitä Microsoftin vastuullisen tekoälyn periaatteiden mukaisesti. Azure AI Foundryssa turvallisuusarvioinnit mahdollistavat mallin haavoittuvuuden arvioinnin jailbreak-hyökkäyksiä vastaan sekä sen kyvyn tuottaa haitallista sisältöä, mikä on suoraan linjassa näiden periaatteiden kanssa.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.fi.png)

*Kuvan lähde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoftin vastuullisen tekoälyn periaatteet

Ennen teknisten vaiheiden aloittamista on tärkeää ymmärtää Microsoftin vastuullisen tekoälyn periaatteet, eettinen kehys, joka ohjaa tekoälyjärjestelmien vastuullista kehittämistä, käyttöönottoa ja toimintaa. Nämä periaatteet ohjaavat tekoälyjärjestelmien vastuullista suunnittelua, kehitystä ja käyttöönottoa varmistaen, että tekoälyteknologiat rakennetaan oikeudenmukaisesti, läpinäkyvästi ja osallistavasti. Ne muodostavat perustan tekoälymallien turvallisuuden arvioinnille.

Microsoftin vastuullisen tekoälyn periaatteet ovat:

- **Oikeudenmukaisuus ja osallistavuus**: Tekoälyjärjestelmien tulee kohdella kaikkia tasapuolisesti eikä vaikuttaa eri tavoin samankaltaisissa tilanteissa oleviin ryhmiin. Esimerkiksi kun tekoälyjärjestelmät antavat ohjeita lääketieteellisestä hoidosta, lainahakemuksista tai työllistymisestä, niiden tulee antaa samat suositukset kaikille, joilla on samankaltaiset oireet, taloudellinen tilanne tai ammatilliset pätevyydet.

- **Luotettavuus ja turvallisuus**: Luottamuksen rakentamiseksi on olennaista, että tekoälyjärjestelmät toimivat luotettavasti, turvallisesti ja johdonmukaisesti. Näiden järjestelmien tulee pystyä toimimaan suunnitellulla tavalla, reagoimaan turvallisesti odottamattomiin tilanteisiin ja vastustamaan haitallista manipulointia. Niiden käyttäytyminen ja kyky käsitellä erilaisia tilanteita heijastavat kehittäjien suunnittelun ja testauksen aikana ennakoimia tilanteita.

- **Läpinäkyvyys**: Kun tekoälyjärjestelmät auttavat tekemään päätöksiä, joilla on suuri vaikutus ihmisten elämään, on tärkeää, että ihmiset ymmärtävät, miten nämä päätökset on tehty. Esimerkiksi pankki saattaa käyttää tekoälyä arvioidakseen henkilön luottokelpoisuutta. Yritys voi käyttää tekoälyä valitakseen pätevimmät ehdokkaat työhön.

- **Yksityisyys ja turvallisuus**: Tekoälyn yleistyessä yksityisyyden suojaaminen ja henkilö- sekä yritystietojen turvaaminen korostuvat ja monimutkaistuvat. Tekoälyn kohdalla yksityisyyden ja tietoturvan huomioiminen on erityisen tärkeää, koska datan saatavuus on välttämätöntä tekoälyjärjestelmien tarkkojen ja perusteltujen ennusteiden ja päätösten tekemiseksi.

- **Vastuullisuus**: Tekoälyjärjestelmien suunnittelijoiden ja käyttöönottojen tekijöiden tulee olla vastuussa järjestelmiensä toiminnasta. Organisaatioiden tulisi hyödyntää alan standardeja vastuullisuuden normien kehittämiseksi. Nämä normit varmistavat, että tekoälyjärjestelmät eivät ole lopullinen auktoriteetti päätöksissä, jotka vaikuttavat ihmisten elämään, ja että ihmiset säilyttävät merkittävän kontrollin muuten hyvin autonomisten tekoälyjärjestelmien yli.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.fi.png)

*Kuvan lähde: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Lisätietoja Microsoftin vastuullisen tekoälyn periaatteista löydät sivulta [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Turvallisuusmittarit

Tässä opetusohjelmassa arvioit hienosäädetyn Phi-3 -mallin turvallisuutta Azure AI Foundryn turvallisuusmittareilla. Nämä mittarit auttavat sinua arvioimaan mallin kykyä tuottaa haitallista sisältöä ja sen haavoittuvuutta jailbreak-hyökkäyksille. Turvallisuusmittarit sisältävät:

- **Itseä vahingoittava sisältö**: Arvioi, onko mallilla taipumusta tuottaa itseä vahingoittavaan sisältöön liittyvää materiaalia.
- **Vihamielinen ja epäoikeudenmukainen sisältö**: Arvioi, onko mallilla taipumusta tuottaa vihamielistä tai epäoikeudenmukaista sisältöä.
- **Väkivaltainen sisältö**: Arvioi, onko mallilla taipumusta tuottaa väkivaltaista sisältöä.
- **Seksuaalinen sisältö**: Arvioi, onko mallilla taipumusta tuottaa sopimatonta seksuaalista sisältöä.

Näiden osa-alueiden arviointi varmistaa, että tekoälymalli ei tuota haitallista tai loukkaavaa sisältöä, mikä vastaa yhteiskunnallisia arvoja ja sääntelyvaatimuksia.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.fi.png)

### Johdatus suorituskyvyn arviointiin

Jotta tekoälymallisi toimisi odotetusti, on tärkeää arvioida sen suorituskykyä suorituskykymittareiden avulla. Azure AI Foundryssa suorituskyvyn arvioinnit mahdollistavat mallin tehokkuuden arvioinnin tarkkojen, asiaankuuluvien ja johdonmukaisten vastausten tuottamisessa.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.fi.png)

*Kuvan lähde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Suorituskykymittarit

Tässä opetusohjelmassa arvioit hienosäädetyn Phi-3 / Phi-3.5 -mallin suorituskykyä Azure AI Foundryn suorituskykymittareilla. Nämä mittarit auttavat sinua arvioimaan mallin tehokkuutta tarkkojen, asiaankuuluvien ja johdonmukaisten vastausten tuottamisessa. Suorituskykymittarit sisältävät:

- **Perusteltavuus**: Arvioi, kuinka hyvin tuotetut vastaukset vastaavat syötteen lähdetietoa.
- **Asiaankuuluvuus**: Arvioi tuotettujen vastausten merkityksellisyyttä annettuihin kysymyksiin nähden.
- **Johdonmukaisuus**: Arvioi, kuinka sujuvasti tuotettu teksti etenee, lukeutuu luonnollisesti ja muistuttaa ihmismäistä kieltä.
- **Sujuvuus**: Arvioi tuotetun tekstin kielitaitoa.
- **GPT:n samankaltaisuus**: Vertaa tuotettua vastausta totuudenmukaiseen vastaukseen samankaltaisuuden osalta.
- **F1-pistemäärä**: Laskee jaetun sanamäärän suhteen tuotetun vastauksen ja lähdetiedon välillä.

Nämä mittarit auttavat sinua arvioimaan mallin tehokkuutta tarkkojen, asiaankuuluvien ja johdonmukaisten vastausten tuottamisessa.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.fi.png)

## **Tapaus 2: Phi-3 / Phi-3.5 -mallin arviointi Azure AI Foundryssa**

### Ennen aloittamista

Tämä opetusohjelma jatkaa aiempia blogikirjoituksia, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ja "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Näissä kirjoituksissa kävimme läpi Phi-3 / Phi-3.5 -mallin hienosäädön Azure AI Foundryssa ja sen integroinnin Prompt flow -työkaluun.

Tässä opetusohjelmassa otat käyttöön Azure OpenAI -mallin arvioijana Azure AI Foundryssa ja käytät sitä hienosäädetyn Phi-3 / Phi-3.5 -mallisi arviointiin.

Ennen tämän opetusohjelman aloittamista varmista, että sinulla on seuraavat esivaatimukset, kuten aiemmissa opetusohjelmissa kuvattu:

1. Valmis aineisto hienosäädetyn Phi-3 / Phi-3.5 -mallin arviointiin.
1. Phi-3 / Phi-3.5 -malli, joka on hienosäädetty ja otettu käyttöön Azure Machine Learningissä.
1. Prompt flow, joka on integroitu hienosäädettyyn Phi-3 / Phi-3.5 -malliisi Azure AI Foundryssa.

> [!NOTE]
> Käytät *test_data.jsonl* -tiedostoa, joka sijaitsee **ULTRACHAT_200k** -aineiston data-kansiossa ja joka ladattiin aiemmissa blogikirjoituksissa, aineistona hienosäädetyn Phi-3 / Phi-3.5 -mallin arviointiin.

#### Integroi mukautettu Phi-3 / Phi-3.5 -malli Prompt flow -työkaluun Azure AI Foundryssa (koodipohjainen lähestymistapa)
> [!NOTE]
> Jos seurasit vähäkoodista lähestymistapaa, joka on kuvattu artikkelissa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", voit ohittaa tämän harjoituksen ja siirtyä seuraavaan.
> Kuitenkin, jos seurasit koodikeskeistä lähestymistapaa, joka on kuvattu artikkelissa "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" hienosäätääksesi ja ottaaksesi käyttöön Phi-3 / Phi-3.5 -mallisi, mallin yhdistäminen Prompt Flow'hun tapahtuu hieman eri tavalla. Opit tämän prosessin tässä harjoituksessa.
Jatkaaksesi sinun täytyy integroida hienosäädetty Phi-3 / Phi-3.5 -mallisi Prompt flow'hun Azure AI Foundryssa.

#### Luo Azure AI Foundry Hub

Sinun täytyy luoda Hub ennen projektin luomista. Hub toimii kuin resurssiryhmä, jonka avulla voit järjestää ja hallita useita projekteja Azure AI Foundryssa.

1. Kirjaudu sisään [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Valitse vasemman sivupalkin välilehdeltä **All hubs**.

1. Valitse navigaatiovalikosta **+ New hub**.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.fi.png)

1. Suorita seuraavat tehtävät:

    - Syötä **Hub name**. Sen täytyy olla yksilöllinen arvo.
    - Valitse Azure-tilauksesi (**Subscription**).
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Valitse haluamasi **Location**.
    - Valitse käytettävä **Connect Azure AI Services** (luo uusi tarvittaessa).
    - Valitse **Connect Azure AI Search** ja valitse **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.fi.png)

1. Valitse **Next**.

#### Luo Azure AI Foundry -projekti

1. Valitse luomassasi Hubissa vasemman sivupalkin välilehdeltä **All projects**.

1. Valitse navigaatiovalikosta **+ New project**.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.fi.png)

1. Syötä **Project name**. Sen täytyy olla yksilöllinen arvo.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.fi.png)

1. Valitse **Create a project**.

#### Lisää mukautettu yhteys hienosäädetylle Phi-3 / Phi-3.5 -mallille

Jotta voit integroida mukautetun Phi-3 / Phi-3.5 -mallisi Prompt flow'hun, sinun täytyy tallentaa mallin endpoint ja avain mukautettuun yhteyteen. Tämä varmistaa pääsyn mukautettuun Phi-3 / Phi-3.5 -malliisi Prompt flow'ssa.

#### Aseta hienosäädetyn Phi-3 / Phi-3.5 -mallin api-avain ja endpoint-URI

1. Siirry osoitteeseen [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure Machine Learning -työtilaan.

1. Valitse vasemman sivupalkin välilehdeltä **Endpoints**.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.fi.png)

1. Valitse luomasi endpoint.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.fi.png)

1. Valitse navigaatiovalikosta **Consume**.

1. Kopioi **REST endpoint** ja **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.fi.png)

#### Lisää mukautettu yhteys

1. Siirry osoitteeseen [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure AI Foundry -projektiin.

1. Valitse luomassasi projektissa vasemman sivupalkin välilehdeltä **Settings**.

1. Valitse **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.fi.png)

1. Valitse navigaatiovalikosta **Custom keys**.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.fi.png)

1. Suorita seuraavat tehtävät:

    - Valitse **+ Add key value pairs**.
    - Avaimen nimeksi kirjoita **endpoint** ja liitä Azure ML Studiosta kopioimasi endpoint arvokenttään.
    - Valitse uudelleen **+ Add key value pairs**.
    - Avaimen nimeksi kirjoita **key** ja liitä Azure ML Studiosta kopioimasi avain arvokenttään.
    - Kun avaimet on lisätty, valitse **is secret** estääksesi avaimen paljastumisen.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.fi.png)

1. Valitse **Add connection**.

#### Luo Prompt flow

Olet lisännyt mukautetun yhteyden Azure AI Foundryssa. Luodaan nyt Prompt flow seuraavien ohjeiden mukaan. Tämän jälkeen yhdistät Prompt flow'n mukautettuun yhteyteen, jotta voit käyttää hienosäädettyä mallia Prompt flow'ssa.

1. Siirry luomaasi Azure AI Foundry -projektiin.

1. Valitse vasemman sivupalkin välilehdeltä **Prompt flow**.

1. Valitse navigaatiovalikosta **+ Create**.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.fi.png)

1. Valitse navigaatiovalikosta **Chat flow**.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.fi.png)

1. Syötä käytettävä **Folder name**.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.fi.png)

1. Valitse **Create**.

#### Määritä Prompt flow keskustelemaan mukautetun Phi-3 / Phi-3.5 -mallisi kanssa

Sinun täytyy integroida hienosäädetty Phi-3 / Phi-3.5 -malli Prompt flow'hun. Nykyinen Prompt flow ei ole suunniteltu tätä varten, joten sinun täytyy muokata Prompt flow uudelleen, jotta mukautettu malli voidaan integroida.

1. Prompt flow'ssa tee seuraavat toimenpiteet rakentaaksesi olemassa olevan flow'n uudelleen:

    - Valitse **Raw file mode**.
    - Poista kaikki olemassa oleva koodi tiedostosta *flow.dag.yml*.
    - Lisää seuraava koodi tiedostoon *flow.dag.yml*.

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

    - Valitse **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.fi.png)

1. Lisää seuraava koodi tiedostoon *integrate_with_promptflow.py* käyttääksesi mukautettua Phi-3 / Phi-3.5 -mallia Prompt flow'ssa.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.fi.png)

> [!NOTE]
> Lisätietoja Prompt flow'n käytöstä Azure AI Foundryssa löydät osoitteesta [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Valitse **Chat input** ja **Chat output** ottaaksesi keskustelun mallisi kanssa käyttöön.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.fi.png)

1. Nyt olet valmis keskustelemaan mukautetun Phi-3 / Phi-3.5 -mallisi kanssa. Seuraavassa harjoituksessa opit, miten Prompt flow käynnistetään ja miten sitä käytetään keskusteluun hienosäädetyn Phi-3 / Phi-3.5 -mallin kanssa.

> [!NOTE]
>
> Uudelleen rakennettu flow näyttää tältä:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.fi.png)
>

#### Käynnistä Prompt flow

1. Valitse **Start compute sessions** käynnistääksesi Prompt flow'n.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.fi.png)

1. Valitse **Validate and parse input** päivittääksesi parametrit.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.fi.png)

1. Valitse **connection**-arvoksi luomasi mukautettu yhteys, esimerkiksi *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.fi.png)

#### Keskustele mukautetun Phi-3 / Phi-3.5 -mallisi kanssa

1. Valitse **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.fi.png)

1. Tässä esimerkki tuloksista: Nyt voit keskustella mukautetun Phi-3 / Phi-3.5 -mallisi kanssa. On suositeltavaa esittää kysymyksiä, jotka perustuvat hienosäätöön käytettyyn dataan.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.fi.png)

### Ota käyttöön Azure OpenAI Phi-3 / Phi-3.5 -mallin arviointia varten

Phi-3 / Phi-3.5 -mallin arvioimiseksi Azure AI Foundryssa sinun täytyy ottaa käyttöön Azure OpenAI -malli. Tätä mallia käytetään Phi-3 / Phi-3.5 -mallin suorituskyvyn arviointiin.

#### Ota Azure OpenAI käyttöön

1. Kirjaudu sisään [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure AI Foundry -projektiin.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.fi.png)

1. Valitse luomassasi projektissa vasemman sivupalkin välilehdeltä **Deployments**.

1. Valitse navigaatiovalikosta **+ Deploy model**.

1. Valitse **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.fi.png)

1. Valitse käytettävä Azure OpenAI -malli, esimerkiksi **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.fi.png)

1. Valitse **Confirm**.

### Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryn Prompt flow -arvioinnilla

### Aloita uusi arviointi

1. Siirry osoitteeseen [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure AI Foundry -projektiin.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.fi.png)

1. Valitse luomassasi projektissa vasemman sivupalkin välilehdeltä **Evaluation**.

1. Valitse navigaatiovalikosta **+ New evaluation**.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.fi.png)

1. Valitse **Prompt flow** -arviointi.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.fi.png)

1. Suorita seuraavat tehtävät:

    - Syötä arvioinnin nimi. Sen täytyy olla yksilöllinen arvo.
    - Valitse tehtävätyypiksi **Question and answer without context**, koska tässä ohjeistuksessa käytetty **ULTRACHAT_200k** -aineisto ei sisällä kontekstia.
    - Valitse arvioitava prompt flow.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.fi.png)

1. Valitse **Next**.

1. Suorita seuraavat tehtävät:

    - Valitse **Add your dataset** ladataksesi aineiston. Esimerkiksi voit ladata testiaineiston tiedoston, kuten *test_data.json1*, joka sisältyy **ULTRACHAT_200k** -aineistoon.
    - Valitse sopiva **Dataset column**, joka vastaa aineistoasi. Esimerkiksi **ULTRACHAT_200k** -aineiston tapauksessa valitse **${data.prompt}** dataset-sarakkeeksi.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.fi.png)

1. Valitse **Next**.

1. Suorita seuraavat tehtävät suorituskyky- ja laatumittareiden määrittämiseksi:

    - Valitse käytettävät suorituskyky- ja laatumittarit.
    - Valitse arviointiin käyttämäsi Azure OpenAI -malli, esimerkiksi **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.fi.png)

1. Suorita seuraavat tehtävät riskien ja turvallisuusmittareiden määrittämiseksi:

    - Valitse käytettävät riskien ja turvallisuusmittarit.
    - Valitse kynnysarvo vikaprosentin laskemiseen, esimerkiksi **Medium**.
    - Kysymykselle valitse **Data source** arvoksi **{$data.prompt}**.
    - Vastaukselle valitse **Data source** arvoksi **{$run.outputs.answer}**.
    - Totuustiedolle valitse **Data source** arvoksi **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.fi.png)

1. Valitse **Next**.

1. Valitse **Submit** aloittaaksesi arvioinnin.

1. Arviointi kestää hetken. Voit seurata etenemistä **Evaluation**-välilehdellä.

### Tarkastele arvioinnin tuloksia
> [!NOTE]
> Alla esitetyt tulokset on tarkoitettu havainnollistamaan arviointiprosessia. Tässä opetusohjelmassa olemme käyttäneet mallia, joka on hienosäädetty suhteellisen pienellä aineistolla, mikä saattaa johtaa ei-optimaalisiin tuloksiin. Todelliset tulokset voivat vaihdella merkittävästi käytetyn aineiston koon, laadun ja monimuotoisuuden sekä mallin erityisen konfiguraation mukaan.
Kun arviointi on valmis, voit tarkastella tuloksia sekä suorituskyky- että turvallisuusmittareiden osalta.

1. Suorituskyky- ja laatumittarit:

    - arvioi mallin tehokkuutta tuottaa johdonmukaisia, sujuvia ja asiaankuuluvia vastauksia.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.fi.png)

1. Riskien ja turvallisuuden mittarit:

    - Varmista, että mallin tuottamat vastaukset ovat turvallisia ja noudattavat Responsible AI Principles -periaatteita, välttäen haitallista tai loukkaavaa sisältöä.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.fi.png)

1. Voit selata alaspäin nähdäksesi **Yksityiskohtaiset mittaustulokset**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.fi.png)

1. Arvioimalla mukautetun Phi-3 / Phi-3.5 -mallisi sekä suorituskyky- että turvallisuusmittareiden perusteella voit varmistaa, että malli ei ole pelkästään tehokas, vaan myös noudattaa vastuullisen tekoälyn käytäntöjä, tehden siitä valmiin käytettäväksi todellisissa sovelluksissa.

## Onnittelut!

### Olet suorittanut tämän opetusohjelman

Olet onnistuneesti arvioinut hienosäädetyn Phi-3 -mallin, joka on integroitu Prompt flow -työkaluun Azure AI Foundryssa. Tämä on tärkeä askel varmistettaessa, että tekoälymallisi eivät ainoastaan toimi hyvin, vaan myös noudattavat Microsoftin Responsible AI -periaatteita, auttaen sinua rakentamaan luotettavia ja vastuullisia tekoälysovelluksia.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.fi.png)

## Siivoa Azure-resurssit

Siivoa Azure-resurssisi välttääksesi ylimääräiset maksut tilillesi. Mene Azure-portaaliin ja poista seuraavat resurssit:

- Azure Machine learning -resurssi.
- Azure Machine learning -mallin päätepiste.
- Azure AI Foundry Project -resurssi.
- Azure AI Foundry Prompt flow -resurssi.

### Seuraavat askeleet

#### Dokumentaatio

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Koulutusmateriaali

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Viitteet

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.