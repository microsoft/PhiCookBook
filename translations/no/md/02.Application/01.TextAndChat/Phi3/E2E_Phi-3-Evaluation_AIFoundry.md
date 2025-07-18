<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:42:29+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "no"
}
-->
# Evaluer den finjusterte Phi-3 / Phi-3.5-modellen i Azure AI Foundry med fokus på Microsofts prinsipper for ansvarlig AI

Dette ende-til-ende (E2E) eksempelet er basert på guiden "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community.

## Oversikt

### Hvordan kan du evaluere sikkerheten og ytelsen til en finjustert Phi-3 / Phi-3.5-modell i Azure AI Foundry?

Finjustering av en modell kan noen ganger føre til utilsiktede eller uønskede svar. For å sikre at modellen forblir trygg og effektiv, er det viktig å evaluere modellens potensial for å generere skadelig innhold og dens evne til å produsere nøyaktige, relevante og sammenhengende svar. I denne veiledningen vil du lære hvordan du evaluerer sikkerheten og ytelsen til en finjustert Phi-3 / Phi-3.5-modell integrert med Prompt flow i Azure AI Foundry.

Her er en evalueringprosess i Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.no.png)

*Bildekilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> For mer detaljert informasjon og for å utforske flere ressurser om Phi-3 / Phi-3.5, besøk [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

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

For å sikre at AI-modellen din er etisk og trygg, er det avgjørende å evaluere den opp mot Microsofts prinsipper for ansvarlig AI. I Azure AI Foundry gir sikkerhetsevalueringer deg mulighet til å vurdere modellens sårbarhet for jailbreak-angrep og dens potensial til å generere skadelig innhold, noe som er direkte i tråd med disse prinsippene.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.no.png)

*Bildekilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts prinsipper for ansvarlig AI

Før du begynner med de tekniske stegene, er det viktig å forstå Microsofts prinsipper for ansvarlig AI, et etisk rammeverk designet for å veilede ansvarlig utvikling, distribusjon og drift av AI-systemer. Disse prinsippene styrer ansvarlig design, utvikling og implementering av AI-systemer, og sikrer at AI-teknologier bygges på en måte som er rettferdig, gjennomsiktig og inkluderende. Disse prinsippene er grunnlaget for å evaluere sikkerheten til AI-modeller.

Microsofts prinsipper for ansvarlig AI inkluderer:

- **Rettferdighet og inkludering**: AI-systemer skal behandle alle rettferdig og unngå å påvirke grupper med lignende situasjon ulikt. For eksempel, når AI-systemer gir veiledning om medisinsk behandling, lånesøknader eller ansettelser, skal de gi de samme anbefalingene til alle med lignende symptomer, økonomiske forhold eller faglige kvalifikasjoner.

- **Pålitelighet og sikkerhet**: For å bygge tillit er det avgjørende at AI-systemer fungerer pålitelig, trygt og konsekvent. Disse systemene skal kunne operere som opprinnelig designet, svare trygt på uforutsette situasjoner og motstå skadelig manipulering. Hvordan de oppfører seg og hvilke situasjoner de kan håndtere, reflekterer de forholdene utviklerne forventet under design og testing.

- **Åpenhet**: Når AI-systemer hjelper til med beslutninger som har stor innvirkning på folks liv, er det viktig at folk forstår hvordan disse beslutningene ble tatt. For eksempel kan en bank bruke et AI-system for å avgjøre om en person er kredittverdig. Et selskap kan bruke et AI-system for å finne de mest kvalifiserte kandidatene til ansettelse.

- **Personvern og sikkerhet**: Etter hvert som AI blir mer utbredt, blir det stadig viktigere og mer komplekst å beskytte personvern og sikre personlig og forretningsinformasjon. Med AI krever personvern og datasikkerhet nøye oppmerksomhet fordi tilgang til data er essensielt for at AI-systemer skal kunne gjøre nøyaktige og informerte prediksjoner og beslutninger om mennesker.

- **Ansvarlighet**: De som designer og distribuerer AI-systemer må holdes ansvarlige for hvordan systemene deres fungerer. Organisasjoner bør bruke bransjestandarder for å utvikle normer for ansvarlighet. Disse normene kan sikre at AI-systemer ikke er den endelige autoriteten i beslutninger som påvirker folks liv. De kan også sikre at mennesker beholder meningsfull kontroll over ellers svært autonome AI-systemer.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.no.png)

*Bildekilde: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> For å lære mer om Microsofts prinsipper for ansvarlig AI, besøk [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Sikkerhetsmålinger

I denne veiledningen vil du evaluere sikkerheten til den finjusterte Phi-3-modellen ved hjelp av Azure AI Foundrys sikkerhetsmålinger. Disse målingene hjelper deg med å vurdere modellens potensial til å generere skadelig innhold og dens sårbarhet for jailbreak-angrep. Sikkerhetsmålingene inkluderer:

- **Innhold relatert til selvskading**: Vurderer om modellen har en tendens til å produsere innhold relatert til selvskading.
- **Hatfullt og urettferdig innhold**: Vurderer om modellen har en tendens til å produsere hatfullt eller urettferdig innhold.
- **Voldelig innhold**: Vurderer om modellen har en tendens til å produsere voldelig innhold.
- **Seksuelt innhold**: Vurderer om modellen har en tendens til å produsere upassende seksuelt innhold.

Å evaluere disse aspektene sikrer at AI-modellen ikke produserer skadelig eller støtende innhold, og at den er i tråd med samfunnsverdier og regulatoriske standarder.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.no.png)

### Introduksjon til ytelsesevaluering

For å sikre at AI-modellen din presterer som forventet, er det viktig å evaluere ytelsen mot ytelsesmålinger. I Azure AI Foundry gir ytelsesevalueringer deg mulighet til å vurdere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.no.png)

*Bildekilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Ytelsesmålinger

I denne veiledningen vil du evaluere ytelsen til den finjusterte Phi-3 / Phi-3.5-modellen ved hjelp av Azure AI Foundrys ytelsesmålinger. Disse målingene hjelper deg med å vurdere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar. Ytelsesmålingene inkluderer:

- **Forankring (Groundedness)**: Vurderer hvor godt de genererte svarene samsvarer med informasjonen fra inngangskilden.
- **Relevans**: Vurderer hvor relevante de genererte svarene er i forhold til de gitte spørsmålene.
- **Sammenheng (Coherence)**: Vurderer hvor jevnt den genererte teksten flyter, om den leses naturlig og ligner menneskelig språk.
- **Flyt (Fluency)**: Vurderer språkferdigheten i den genererte teksten.
- **GPT-likhet (GPT Similarity)**: Sammenligner det genererte svaret med sannhetsgrunnlaget for likhet.
- **F1-score**: Beregner andelen delte ord mellom det genererte svaret og kildedataene.

Disse målingene hjelper deg med å evaluere modellens effektivitet i å generere nøyaktige, relevante og sammenhengende svar.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.no.png)

## **Scenario 2: Evaluering av Phi-3 / Phi-3.5-modellen i Azure AI Foundry**

### Før du begynner

Denne veiledningen er en oppfølging av de tidligere blogginnleggene, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" og "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." I disse innleggene gikk vi gjennom prosessen med å finjustere en Phi-3 / Phi-3.5-modell i Azure AI Foundry og integrere den med Prompt flow.

I denne veiledningen vil du distribuere en Azure OpenAI-modell som evaluator i Azure AI Foundry og bruke den til å evaluere din finjusterte Phi-3 / Phi-3.5-modell.

Før du begynner denne veiledningen, sørg for at du har følgende forutsetninger, som beskrevet i de tidligere veiledningene:

1. Et forberedt datasett for å evaluere den finjusterte Phi-3 / Phi-3.5-modellen.
1. En Phi-3 / Phi-3.5-modell som er finjustert og distribuert til Azure Machine Learning.
1. En Prompt flow integrert med din finjusterte Phi-3 / Phi-3.5-modell i Azure AI Foundry.

> [!NOTE]
> Du vil bruke filen *test_data.jsonl*, som ligger i data-mappen fra **ULTRACHAT_200k**-datasettet lastet ned i de tidligere blogginnleggene, som datasett for å evaluere den finjusterte Phi-3 / Phi-3.5-modellen.

#### Integrer den tilpassede Phi-3 / Phi-3.5-modellen med Prompt flow i Azure AI Foundry (Kode-først-tilnærming)
> [!NOTE]  
> Hvis du fulgte lavkode-tilnærmingen beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kan du hoppe over denne øvelsen og gå videre til neste.  
> Men hvis du fulgte kode-først-tilnærmingen beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" for å finjustere og distribuere din Phi-3 / Phi-3.5-modell, er prosessen for å koble modellen til Prompt flow litt annerledes. Du vil lære denne prosessen i denne øvelsen.
For å fortsette, må du integrere din finjusterte Phi-3 / Phi-3.5-modell i Prompt flow i Azure AI Foundry.

#### Opprett Azure AI Foundry Hub

Du må opprette en Hub før du oppretter prosjektet. En Hub fungerer som en Resource Group, og lar deg organisere og administrere flere prosjekter innen Azure AI Foundry.

1. Logg inn på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Velg **All hubs** fra fanen på venstre side.

1. Velg **+ New hub** fra navigasjonsmenyen.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.no.png)

1. Utfør følgende oppgaver:

    - Skriv inn **Hub name**. Det må være en unik verdi.
    - Velg din Azure **Subscription**.
    - Velg **Resource group** som skal brukes (opprett en ny om nødvendig).
    - Velg **Location** du ønsker å bruke.
    - Velg **Connect Azure AI Services** som skal brukes (opprett en ny om nødvendig).
    - Velg **Connect Azure AI Search** og velg **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.no.png)

1. Velg **Next**.

#### Opprett Azure AI Foundry-prosjekt

1. I Huben du opprettet, velg **All projects** fra fanen på venstre side.

1. Velg **+ New project** fra navigasjonsmenyen.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.no.png)

1. Skriv inn **Project name**. Det må være en unik verdi.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.no.png)

1. Velg **Create a project**.

#### Legg til en egendefinert tilkobling for den finjusterte Phi-3 / Phi-3.5-modellen

For å integrere din egendefinerte Phi-3 / Phi-3.5-modell med Prompt flow, må du lagre modellens endepunkt og nøkkel i en egendefinert tilkobling. Denne oppsettet sikrer tilgang til din egendefinerte Phi-3 / Phi-3.5-modell i Prompt flow.

#### Sett api-nøkkel og endepunkt-URI for den finjusterte Phi-3 / Phi-3.5-modellen

1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviger til Azure Machine learning-arbeidsområdet du opprettet.

1. Velg **Endpoints** fra fanen på venstre side.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.no.png)

1. Velg endepunktet du opprettet.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.no.png)

1. Velg **Consume** fra navigasjonsmenyen.

1. Kopier din **REST endpoint** og **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.no.png)

#### Legg til den egendefinerte tilkoblingen

1. Besøk [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. I prosjektet du opprettet, velg **Settings** fra fanen på venstre side.

1. Velg **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.no.png)

1. Velg **Custom keys** fra navigasjonsmenyen.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.no.png)

1. Utfør følgende oppgaver:

    - Velg **+ Add key value pairs**.
    - For nøkkelnavnet, skriv **endpoint** og lim inn endepunktet du kopierte fra Azure ML Studio i verdifeltet.
    - Velg **+ Add key value pairs** igjen.
    - For nøkkelnavnet, skriv **key** og lim inn nøkkelen du kopierte fra Azure ML Studio i verdifeltet.
    - Etter å ha lagt til nøklene, velg **is secret** for å hindre at nøkkelen blir eksponert.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.no.png)

1. Velg **Add connection**.

#### Opprett Prompt flow

Du har lagt til en egendefinert tilkobling i Azure AI Foundry. Nå skal vi opprette en Prompt flow ved å følge disse stegene. Deretter kobler du denne Prompt flow til den egendefinerte tilkoblingen for å bruke den finjusterte modellen i Prompt flow.

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

1. Velg **Prompt flow** fra fanen på venstre side.

1. Velg **+ Create** fra navigasjonsmenyen.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.no.png)

1. Velg **Chat flow** fra navigasjonsmenyen.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.no.png)

1. Skriv inn **Folder name** som skal brukes.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.no.png)

1. Velg **Create**.

#### Sett opp Prompt flow for å chatte med din egendefinerte Phi-3 / Phi-3.5-modell

Du må integrere den finjusterte Phi-3 / Phi-3.5-modellen i en Prompt flow. Den eksisterende Prompt flow som følger med er ikke laget for dette formålet. Derfor må du redesigne Prompt flow for å muliggjøre integrasjon av den egendefinerte modellen.

1. I Prompt flow, utfør følgende for å bygge opp den eksisterende flyten på nytt:

    - Velg **Raw file mode**.
    - Slett all eksisterende kode i *flow.dag.yml*-filen.
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

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.no.png)

1. Legg til følgende kode i *integrate_with_promptflow.py* for å bruke den egendefinerte Phi-3 / Phi-3.5-modellen i Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.no.png)

> [!NOTE]
> For mer detaljert informasjon om bruk av Prompt flow i Azure AI Foundry, kan du se [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Velg **Chat input**, **Chat output** for å aktivere chat med modellen din.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.no.png)

1. Nå er du klar til å chatte med din egendefinerte Phi-3 / Phi-3.5-modell. I neste øvelse vil du lære hvordan du starter Prompt flow og bruker den til å chatte med din finjusterte Phi-3 / Phi-3.5-modell.

> [!NOTE]
>
> Den ombygde flyten skal se ut som bildet under:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.no.png)
>

#### Start Prompt flow

1. Velg **Start compute sessions** for å starte Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.no.png)

1. Velg **Validate and parse input** for å oppdatere parametere.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.no.png)

1. Velg **Value** for **connection** til den egendefinerte tilkoblingen du opprettet. For eksempel, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.no.png)

#### Chat med din egendefinerte Phi-3 / Phi-3.5-modell

1. Velg **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.no.png)

1. Her er et eksempel på resultatene: Nå kan du chatte med din egendefinerte Phi-3 / Phi-3.5-modell. Det anbefales å stille spørsmål basert på dataene som ble brukt til finjustering.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.no.png)

### Distribuer Azure OpenAI for å evaluere Phi-3 / Phi-3.5-modellen

For å evaluere Phi-3 / Phi-3.5-modellen i Azure AI Foundry, må du distribuere en Azure OpenAI-modell. Denne modellen vil bli brukt til å evaluere ytelsen til Phi-3 / Phi-3.5-modellen.

#### Distribuer Azure OpenAI

1. Logg inn på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.no.png)

1. I prosjektet du opprettet, velg **Deployments** fra fanen på venstre side.

1. Velg **+ Deploy model** fra navigasjonsmenyen.

1. Velg **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.no.png)

1. Velg Azure OpenAI-modellen du ønsker å bruke. For eksempel, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.no.png)

1. Velg **Confirm**.

### Evaluer den finjusterte Phi-3 / Phi-3.5-modellen ved hjelp av Azure AI Foundrys Prompt flow-evaluering

### Start en ny evaluering

1. Besøk [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til Azure AI Foundry-prosjektet du opprettet.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.no.png)

1. I prosjektet du opprettet, velg **Evaluation** fra fanen på venstre side.

1. Velg **+ New evaluation** fra navigasjonsmenyen.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.no.png)

1. Velg **Prompt flow** evaluering.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.no.png)

1. Utfør følgende oppgaver:

    - Skriv inn evalueringsnavnet. Det må være en unik verdi.
    - Velg **Question and answer without context** som oppgavetype. Fordi datasettet **ULTRACHAT_200k** som brukes i denne veiledningen ikke inneholder kontekst.
    - Velg prompt flow du ønsker å evaluere.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.no.png)

1. Velg **Next**.

1. Utfør følgende oppgaver:

    - Velg **Add your dataset** for å laste opp datasettet. For eksempel kan du laste opp testdatasettet, som *test_data.json1*, som følger med når du laster ned **ULTRACHAT_200k** datasettet.
    - Velg riktig **Dataset column** som passer til datasettet ditt. For eksempel, hvis du bruker **ULTRACHAT_200k** datasettet, velg **${data.prompt}** som dataset-kolonne.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.no.png)

1. Velg **Next**.

1. Utfør følgende oppgaver for å konfigurere ytelses- og kvalitetsmålinger:

    - Velg ytelses- og kvalitetsmålingene du ønsker å bruke.
    - Velg Azure OpenAI-modellen du opprettet for evaluering. For eksempel, velg **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.no.png)

1. Utfør følgende oppgaver for å konfigurere risikio- og sikkerhetsmålinger:

    - Velg risikio- og sikkerhetsmålingene du ønsker å bruke.
    - Velg terskelen for å beregne feilrate du ønsker å bruke. For eksempel, velg **Medium**.
    - For **question**, velg **Data source** til **{$data.prompt}**.
    - For **answer**, velg **Data source** til **{$run.outputs.answer}**.
    - For **ground_truth**, velg **Data source** til **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.no.png)

1. Velg **Next**.

1. Velg **Submit** for å starte evalueringen.

1. Evalueringen vil ta litt tid å fullføre. Du kan følge fremdriften i **Evaluation**-fanen.

### Gå gjennom evalueringsresultatene
> [!NOTE]
> Resultatene som presenteres nedenfor er ment å illustrere evalueringsprosessen. I denne veiledningen har vi brukt en modell som er finjustert på et relativt lite datasett, noe som kan føre til suboptimale resultater. Faktiske resultater kan variere betydelig avhengig av størrelsen, kvaliteten og mangfoldet i datasettet som brukes, samt den spesifikke konfigurasjonen av modellen.
Når evalueringen er fullført, kan du gå gjennom resultatene for både ytelse og sikkerhetsmålinger.

1. Ytelses- og kvalitetsmålinger:

    - vurder modellens evne til å generere sammenhengende, flytende og relevante svar.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.no.png)

1. Risiko- og sikkerhetsmålinger:

    - Sørg for at modellens output er trygt og i tråd med Responsible AI Principles, og unngå skadelig eller støtende innhold.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.no.png)

1. Du kan bla ned for å se **Detaljerte måleresultater**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.no.png)

1. Ved å evaluere din tilpassede Phi-3 / Phi-3.5-modell mot både ytelses- og sikkerhetsmålinger, kan du bekrefte at modellen ikke bare er effektiv, men også følger ansvarlige AI-prinsipper, noe som gjør den klar for bruk i praksis.

## Gratulerer!

### Du har fullført denne veiledningen

Du har nå evaluert den finjusterte Phi-3-modellen integrert med Prompt flow i Azure AI Foundry. Dette er et viktig steg for å sikre at AI-modellene dine ikke bare presterer godt, men også følger Microsofts Responsible AI-prinsipper, slik at du kan bygge pålitelige og troverdige AI-applikasjoner.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.no.png)

## Rydd opp i Azure-ressursene

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

#### Opplæringsinnhold

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referanser

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.