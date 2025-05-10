<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:47:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "no"
}
-->
# Evaluer den finjusterte Phi-3 / Phi-3.5-modellen i Azure AI Foundry med fokus på Microsofts prinsipper for ansvarlig AI

Dette ende-til-ende (E2E) eksempelet er basert på veiledningen "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community.

## Oversikt

### Hvordan kan du evaluere sikkerheten og ytelsen til en finjustert Phi-3 / Phi-3.5-modell i Azure AI Foundry?

Finjustering av en modell kan noen ganger føre til uønskede eller utilsiktede svar. For å sikre at modellen forblir trygg og effektiv, er det viktig å evaluere modellens potensial for å generere skadelig innhold og dens evne til å produsere nøyaktige, relevante og sammenhengende svar. I denne veiledningen lærer du hvordan du evaluerer sikkerheten og ytelsen til en finjustert Phi-3 / Phi-3.5-modell integrert med Prompt flow i Azure AI Foundry.

Her er en evalueringprosess for Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.no.png)

*Bildekilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> For mer detaljert informasjon og flere ressurser om Phi-3 / Phi-3.5, besøk [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Forutsetninger

- [Python](https://www.python.org/downloads)
- [Azure-abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Finjustert Phi-3 / Phi-3.5-modell

### Innholdsfortegnelse

1. [**Scenario 1: Introduksjon til Azure AI Foundrys Prompt flow-evaluering**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduksjon til sikkerhetsevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduksjon til ytelsesevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Evaluering av Phi-3 / Phi-3.5-modellen i Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Før du begynner](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuer Azure OpenAI for å evaluere Phi-3 / Phi-3.5-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluer den finjusterte Phi-3 / Phi-3.5-modellen ved hjelp av Azure AI Foundrys Prompt flow-evaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gratulerer!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduksjon til Azure AI Foundrys Prompt flow-evaluering**

### Introduksjon til sikkerhetsevaluering

For å sikre at AI-modellen din er etisk og trygg, er det avgjørende å evaluere den i forhold til Microsofts prinsipper for ansvarlig AI. I Azure AI Foundry gir sikkerhetsevalueringer deg mulighet til å vurdere modellens sårbarhet for jailbreak-angrep og dens potensial for å generere skadelig innhold, noe som er direkte i tråd med disse prinsippene.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.no.png)

*Bildekilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts prinsipper for ansvarlig AI

Før du begynner med de tekniske stegene, er det viktig å forstå Microsofts prinsipper for ansvarlig AI, et etisk rammeverk som skal veilede ansvarlig utvikling, distribusjon og drift av AI-systemer. Disse prinsippene styrer hvordan AI-systemer skal designes, utvikles og implementeres på en rettferdig, gjennomsiktig og inkluderende måte. De utgjør grunnlaget for å evaluere sikkerheten til AI-modeller.

Microsofts prinsipper for ansvarlig AI inkluderer:

- **Rettferdighet og inkludering**: AI-systemer skal behandle alle rettferdig og unngå å påvirke lignende grupper på ulike måter. For eksempel, når AI-systemer gir veiledning om medisinsk behandling, lånesøknader eller ansettelser, skal de gi samme anbefaling til alle med lignende symptomer, økonomiske forhold eller yrkesmessige kvalifikasjoner.

- **Pålitelighet og sikkerhet**: For å bygge tillit er det avgjørende at AI-systemer fungerer pålitelig, trygt og konsekvent. Disse systemene skal kunne fungere som opprinnelig designet, svare trygt på uventede situasjoner og motstå skadelig manipulasjon. Hvordan de oppfører seg og hvilke situasjoner de kan håndtere, reflekterer de forholdene utviklerne har tatt høyde for under design og testing.

- **Åpenhet**: Når AI-systemer bidrar til beslutninger som har stor innvirkning på folks liv, er det viktig at folk forstår hvordan beslutningene ble tatt. For eksempel kan en bank bruke AI for å avgjøre om en person er kredittverdig. Et selskap kan bruke AI til å finne de mest kvalifiserte kandidatene til en stilling.

- **Personvern og sikkerhet**: Etter hvert som AI blir mer utbredt, blir det viktigere og mer komplekst å beskytte personvern og sikre personlig og bedriftsinformasjon. Med AI krever personvern og datasikkerhet ekstra oppmerksomhet fordi tilgang til data er nødvendig for at AI-systemer skal kunne gjøre nøyaktige og informerte prediksjoner og beslutninger om mennesker.

- **Ansvarlighet**: De som designer og distribuerer AI-systemer må være ansvarlige for hvordan systemene fungerer. Organisasjoner bør bruke bransjestandarder for å utvikle normer for ansvarlighet. Disse normene kan sikre at AI-systemer ikke er den endelige autoriteten i beslutninger som påvirker folks liv, og at mennesker beholder meningsfull kontroll over ellers svært autonome AI-systemer.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.no.png)

*Bildekilde: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> For mer informasjon om Microsofts prinsipper for ansvarlig AI, besøk [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Sikkerhetsmetrikker

I denne veiledningen vil du evaluere sikkerheten til den finjusterte Phi-3-modellen ved hjelp av Azure AI Foundrys sikkerhetsmetrikker. Disse metrikene hjelper deg å vurdere modellens potensial for å generere skadelig innhold og dens sårbarhet for jailbreak-angrep. Sikkerhetsmetrikker inkluderer:

- **Innhold relatert til selvskading**: Vurderer om modellen har en tendens til å produsere innhold relatert til selvskading.
- **Hatfullt og urettferdig innhold**: Vurderer om modellen har en tendens til å produsere hatfullt eller urettferdig innhold.
- **Voldelig innhold**: Vurderer om modellen har en tendens til å produsere voldelig innhold.
- **Seksuelt innhold**: Vurderer om modellen har en tendens til å produsere upassende seksuelt innhold.

Å evaluere disse aspektene sikrer at AI-modellen ikke produserer skadelig eller støtende innhold, og samsvarer med samfunnets verdier og regulatoriske krav.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.no.png)

### Introduksjon til ytelsesevaluering

For å sikre at AI-modellen din yter som forventet, er det viktig å evaluere ytelsen basert på ytelsesmetrikker. I Azure AI Foundry gir ytelsesevalueringer deg mulighet til å vurdere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.no.png)

*Bildekilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Ytelsesmetrikker

I denne veiledningen vil du evaluere ytelsen til den finjusterte Phi-3 / Phi-3.5-modellen ved hjelp av Azure AI Foundrys ytelsesmetrikker. Disse metrikene hjelper deg å vurdere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar. Ytelsesmetrikker inkluderer:

- **Forankring (Groundedness)**: Vurderer hvor godt de genererte svarene samsvarer med informasjonen fra inndatakilden.
- **Relevans**: Vurderer hvor relevante de genererte svarene er i forhold til de stilte spørsmålene.
- **Sammenheng (Coherence)**: Vurderer hvor jevnt teksten flyter, om den leses naturlig og ligner menneskelig språk.
- **Flyt (Fluency)**: Vurderer språkferdigheten i den genererte teksten.
- **GPT-likhet (GPT Similarity)**: Sammenligner det genererte svaret med grunnsannheten for likhet.
- **F1-score**: Beregner andelen delte ord mellom det genererte svaret og kildedataene.

Disse metrikene hjelper deg å evaluere modellens evne til å generere nøyaktige, relevante og sammenhengende svar.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.no.png)

## **Scenario 2: Evaluering av Phi-3 / Phi-3.5-modellen i Azure AI Foundry**

### Før du begynner

Denne veiledningen bygger videre på tidligere blogginnlegg, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" og "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." I disse innleggene gikk vi gjennom prosessen med å finjustere en Phi-3 / Phi-3.5-modell i Azure AI Foundry og integrere den med Prompt flow.

I denne veiledningen vil du distribuere en Azure OpenAI-modell som evaluator i Azure AI Foundry og bruke den til å evaluere din finjusterte Phi-3 / Phi-3.5-modell.

Før du begynner, sørg for at du har følgende forutsetninger, som beskrevet i de tidligere veiledningene:

1. Et forberedt datasett for å evaluere den finjusterte Phi-3 / Phi-3.5-modellen.
1. En Phi-3 / Phi-3.5-modell som er finjustert og distribuert til Azure Machine Learning.
1. En Prompt flow integrert med din finjusterte Phi-3 / Phi-3.5-modell i Azure AI Foundry.

> [!NOTE]
> Du vil bruke *test_data.jsonl*-filen, som ligger i data-mappen fra **ULTRACHAT_200k** datasettet lastet ned i de tidligere blogginnleggene, som datasett for evaluering av den finjusterte Phi-3 / Phi-3.5-modellen.

#### Integrer den tilpassede Phi-3 / Phi-3.5-modellen med Prompt flow i Azure AI Foundry (Kode-først-tilnærming)

> [!NOTE]
> Hvis du fulgte lavkode-tilnærmingen beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kan du hoppe over denne øvelsen og gå videre til neste.
> Men hvis du fulgte kode-først-tilnærmingen beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" for å finjustere og distribuere din Phi-3 / Phi-3.5-modell, er prosessen for å koble modellen til Prompt flow litt annerledes. Du vil lære denne prosessen i denne øvelsen.

For å fortsette må du integrere din finjusterte Phi-3 / Phi-3.5-modell i Prompt flow i Azure AI Foundry.

#### Opprett Azure AI Foundry Hub

Du må opprette en Hub før du oppretter prosjektet. En Hub fungerer som en ressursgruppe, og lar deg organisere og administrere flere prosjekter innen Azure AI Foundry.

1. Logg inn på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Velg **All hubs** fra venstre sidepanel.

1. Velg **+ New hub** fra navigasjonsmenyen.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.no.png)

1. Utfør følgende oppgaver:

    - Skriv inn **Hub name**. Det må være et unikt navn.
    - Velg din Azure **Subscription**.
    - Velg **Resource group** som skal brukes (opprett en ny om nødvendig).
    - Velg **Location** du ønsker å bruke.
    - Velg **Connect Azure AI Services** som skal brukes (opprett en ny om nødvendig).
    - Velg **Connect Azure AI Search** og velg **Skip connecting**.
![Fyll hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.no.png)

1. Velg **Next**.

#### Opprett Azure AI Foundry-prosjekt

1. I huben du opprettet, velg **All projects** fra venstre side-fanen.

1. Velg **+ New project** fra navigasjonsmenyen.

    ![Velg nytt prosjekt.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.no.png)

1. Skriv inn **Project name**. Den må være unik.

    ![Opprett prosjekt.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.no.png)

1. Velg **Create a project**.

#### Legg til en tilpasset tilkobling for den finjusterte Phi-3 / Phi-3.5-modellen

For å integrere din tilpassede Phi-3 / Phi-3.5-modell med Prompt flow, må du lagre modellens endepunkt og nøkkel i en tilpasset tilkobling. Denne konfigurasjonen sikrer tilgang til din tilpassede Phi-3 / Phi-3.5-modell i Prompt flow.

#### Sett api-nøkkel og endepunkt-URI for den finjusterte Phi-3 / Phi-3.5-modellen

1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviger til Azure Machine learning-arbeidsområdet du opprettet.

1. Velg **Endpoints** fra venstre side-fanen.

    ![Velg endepunkter.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.no.png)

1. Velg endepunktet du opprettet.

    ![Velg opprettet endepunkt.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.no.png)

1. Velg **Consume** fra navigasjonsmenyen.

1. Kopier din **REST endpoint** og **Primary key**.

    ![Kopier api-nøkkel og endepunkt-URI.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.no.png)

#### Legg til den tilpassede tilkoblingen

1. Besøk [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. I prosjektet du opprettet, velg **Settings** fra venstre side-fanen.

1. Velg **+ New connection**.

    ![Velg ny tilkobling.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.no.png)

1. Velg **Custom keys** fra navigasjonsmenyen.

    ![Velg tilpassede nøkler.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.no.png)

1. Utfør følgende oppgaver:

    - Velg **+ Add key value pairs**.
    - For nøkkelnavn, skriv inn **endpoint** og lim inn endepunktet du kopierte fra Azure ML Studio i verdifeltet.
    - Velg **+ Add key value pairs** igjen.
    - For nøkkelnavn, skriv inn **key** og lim inn nøkkelen du kopierte fra Azure ML Studio i verdifeltet.
    - Etter å ha lagt til nøklene, velg **is secret** for å hindre at nøkkelen blir synlig.

    ![Legg til tilkobling.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.no.png)

1. Velg **Add connection**.

#### Opprett Prompt flow

Du har nå lagt til en tilpasset tilkobling i Azure AI Foundry. La oss nå opprette en Prompt flow ved å følge disse trinnene. Deretter kobler du denne Prompt flow til den tilpassede tilkoblingen for å bruke den finjusterte modellen i Prompt flow.

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. Velg **Prompt flow** fra venstre side-fanen.

1. Velg **+ Create** fra navigasjonsmenyen.

    ![Velg Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.no.png)

1. Velg **Chat flow** fra navigasjonsmenyen.

    ![Velg chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.no.png)

1. Skriv inn **Folder name** som skal brukes.

    ![Velg chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.no.png)

1. Velg **Create**.

#### Konfigurer Prompt flow for å chatte med din tilpassede Phi-3 / Phi-3.5-modell

Du må integrere den finjusterte Phi-3 / Phi-3.5-modellen i en Prompt flow. Den eksisterende Prompt flowen som følger med, er ikke designet for dette formålet. Derfor må du redesigne Prompt flow for å muliggjøre integrasjon av den tilpassede modellen.

1. I Prompt flow, utfør følgende for å bygge opp eksisterende flyt på nytt:

    - Velg **Raw file mode**.
    - Slett all eksisterende kode i filen *flow.dag.yml*.
    - Legg til følgende kode i *flow.dag.yml*.

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

    - Velg **Save**.

    ![Velg rå filmodus.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.no.png)

1. Legg til følgende kode i *integrate_with_promptflow.py* for å bruke den tilpassede Phi-3 / Phi-3.5-modellen i Prompt flow.

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

    ![Lim inn prompt flow-kode.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.no.png)

> [!NOTE]
> For mer detaljert informasjon om bruk av Prompt flow i Azure AI Foundry, kan du se [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Velg **Chat input**, **Chat output** for å aktivere chat med modellen din.

    ![Velg input og output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.no.png)

1. Nå er du klar til å chatte med din tilpassede Phi-3 / Phi-3.5-modell. I neste øvelse vil du lære hvordan du starter Prompt flow og bruker den til å chatte med din finjusterte Phi-3 / Phi-3.5-modell.

> [!NOTE]
>
> Den ombygde flyten skal se ut som bildet under:
>
> ![Flyt-eksempel](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.no.png)
>

#### Start Prompt flow

1. Velg **Start compute sessions** for å starte Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.no.png)

1. Velg **Validate and parse input** for å fornye parametrene.

    ![Valider input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.no.png)

1. Velg **Value** for **connection** til den tilpassede tilkoblingen du opprettet. For eksempel, *connection*.

    ![Tilkobling.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.no.png)

#### Chat med din tilpassede Phi-3 / Phi-3.5-modell

1. Velg **Chat**.

    ![Velg chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.no.png)

1. Her er et eksempel på resultatene: Nå kan du chatte med din tilpassede Phi-3 / Phi-3.5-modell. Det anbefales å stille spørsmål basert på dataene som ble brukt til finjustering.

    ![Chat med prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.no.png)

### Distribuer Azure OpenAI for å evaluere Phi-3 / Phi-3.5-modellen

For å evaluere Phi-3 / Phi-3.5-modellen i Azure AI Foundry, må du distribuere en Azure OpenAI-modell. Denne modellen vil brukes til å evaluere ytelsen til Phi-3 / Phi-3.5-modellen.

#### Distribuer Azure OpenAI

1. Logg inn på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

    ![Velg prosjekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.no.png)

1. I prosjektet du opprettet, velg **Deployments** fra venstre side-fanen.

1. Velg **+ Deploy model** fra navigasjonsmenyen.

1. Velg **Deploy base model**.

    ![Velg distribusjoner.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.no.png)

1. Velg Azure OpenAI-modellen du ønsker å bruke. For eksempel, **gpt-4o**.

    ![Velg Azure OpenAI-modell du vil bruke.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.no.png)

1. Velg **Confirm**.

### Evaluer den finjusterte Phi-3 / Phi-3.5-modellen med Azure AI Foundrys Prompt flow-evaluering

### Start en ny evaluering

1. Besøk [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

    ![Velg prosjekt.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.no.png)

1. I prosjektet du opprettet, velg **Evaluation** fra venstre side-fanen.

1. Velg **+ New evaluation** fra navigasjonsmenyen.
![Velg evaluering.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.no.png)

1. Velg **Prompt flow** evaluering.

    ![Velg Prompt flow evaluering.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.no.png)

1. utfør følgende oppgaver:

    - Skriv inn evalueringsnavnet. Det må være en unik verdi.
    - Velg **Question and answer without context** som oppgavetype. Fordi datasettet **UlTRACHAT_200k** som brukes i denne veiledningen ikke inneholder kontekst.
    - Velg prompt flow du ønsker å evaluere.

    ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.no.png)

1. Velg **Neste**.

1. utfør følgende oppgaver:

    - Velg **Add your dataset** for å laste opp datasettet. For eksempel kan du laste opp testdatasettfilen, som *test_data.json1*, som følger med når du laster ned **ULTRACHAT_200k** datasettet.
    - Velg riktig **Dataset column** som matcher datasettet ditt. For eksempel, hvis du bruker **ULTRACHAT_200k** datasettet, velg **${data.prompt}** som datasettskolonne.

    ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.no.png)

1. Velg **Neste**.

1. utfør følgende oppgaver for å konfigurere ytelses- og kvalitetsmålinger:

    - Velg ytelses- og kvalitetsmålingene du ønsker å bruke.
    - Velg Azure OpenAI-modellen du opprettet for evaluering. For eksempel, velg **gpt-4o**.

    ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.no.png)

1. utfør følgende oppgaver for å konfigurere risikiovervåkning og sikkerhetsmålinger:

    - Velg risikiovervåkning og sikkerhetsmålingene du ønsker å bruke.
    - Velg terskelen for å beregne feilrate du ønsker å bruke. For eksempel, velg **Medium**.
    - For **question**, velg **Data source** til **{$data.prompt}**.
    - For **answer**, velg **Data source** til **{$run.outputs.answer}**.
    - For **ground_truth**, velg **Data source** til **{$data.message}**.

    ![Prompt flow evaluering.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.no.png)

1. Velg **Neste**.

1. Velg **Submit** for å starte evalueringen.

1. Evalueringen vil ta litt tid å fullføre. Du kan følge med på fremdriften under fanen **Evaluation**.

### Gjennomgå evalueringsresultatene

> [!NOTE]
> Resultatene som vises nedenfor er ment å illustrere evalueringsprosessen. I denne veiledningen har vi brukt en modell finjustert på et relativt lite datasett, noe som kan føre til suboptimale resultater. Faktiske resultater kan variere betydelig avhengig av størrelse, kvalitet og variasjon i datasettet som brukes, samt den spesifikke konfigurasjonen av modellen.

Når evalueringen er fullført, kan du gjennomgå resultatene for både ytelses- og sikkerhetsmålinger.

1. Ytelses- og kvalitetsmålinger:

    - vurderer modellens effektivitet i å generere sammenhengende, flytende og relevante svar.

    ![Evalueringsresultat.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.no.png)

1. Risiko- og sikkerhetsmålinger:

    - Sikrer at modellens output er trygt og i samsvar med Responsible AI-prinsippene, og unngår skadelig eller støtende innhold.

    ![Evalueringsresultat.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.no.png)

1. Du kan bla ned for å se **Detaljerte måleresultater**.

    ![Evalueringsresultat.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.no.png)

1. Ved å evaluere din tilpassede Phi-3 / Phi-3.5-modell mot både ytelses- og sikkerhetsmålinger, kan du bekrefte at modellen ikke bare er effektiv, men også følger ansvarlige AI-praksiser, og dermed er klar for reell bruk.

## Gratulerer!

### Du har fullført denne veiledningen

Du har nå evaluert den finjusterte Phi-3-modellen integrert med Prompt flow i Azure AI Foundry. Dette er et viktig steg for å sikre at AI-modellene dine ikke bare presterer godt, men også følger Microsofts Responsible AI-prinsipper for å hjelpe deg med å bygge pålitelige og troverdige AI-applikasjoner.

![Arkitektur.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.no.png)

## Rydd opp i Azure-ressurser

Rydd opp i Azure-ressursene dine for å unngå ekstra kostnader på kontoen din. Gå til Azure-portalen og slett følgende ressurser:

- Azure Machine learning-ressursen.
- Azure Machine learning-modellendepunktet.
- Azure AI Foundry Project-ressursen.
- Azure AI Foundry Prompt flow-ressursen.

### Neste steg

#### Dokumentasjon

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Treningsinnhold

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referanser

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.