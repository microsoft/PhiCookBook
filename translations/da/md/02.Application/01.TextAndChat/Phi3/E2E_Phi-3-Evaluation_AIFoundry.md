<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:44:45+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "da"
}
-->
# Evaluer den finjusterede Phi-3 / Phi-3.5 model i Azure AI Foundry med fokus på Microsofts Responsible AI-principper

Dette end-to-end (E2E) eksempel er baseret på guiden "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community.

## Oversigt

### Hvordan kan du evaluere sikkerheden og ydeevnen af en finjusteret Phi-3 / Phi-3.5 model i Azure AI Foundry?

Finjustering af en model kan nogle gange føre til utilsigtede eller uønskede svar. For at sikre, at modellen forbliver sikker og effektiv, er det vigtigt at evaluere modellens potentiale for at generere skadeligt indhold samt dens evne til at levere præcise, relevante og sammenhængende svar. I denne vejledning lærer du, hvordan du evaluerer sikkerheden og ydeevnen af en finjusteret Phi-3 / Phi-3.5 model integreret med Prompt flow i Azure AI Foundry.

Her er en evalueringsproces i Azure AI Foundry.

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.da.png)

*Billedkilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> For mere detaljeret information og for at udforske yderligere ressourcer om Phi-3 / Phi-3.5, besøg venligst [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Forudsætninger

- [Python](https://www.python.org/downloads)
- [Azure abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Finjusteret Phi-3 / Phi-3.5 model

### Indholdsfortegnelse

1. [**Scenario 1: Introduktion til Azure AI Foundrys Prompt flow evaluering**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduktion til sikkerhedsevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduktion til ydeevneevaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Evaluering af Phi-3 / Phi-3.5 modellen i Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Før du går i gang](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Deploy Azure OpenAI til evaluering af Phi-3 / Phi-3.5 modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluer den finjusterede Phi-3 / Phi-3.5 model ved hjælp af Azure AI Foundrys Prompt flow evaluering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Tillykke!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduktion til Azure AI Foundrys Prompt flow evaluering**

### Introduktion til sikkerhedsevaluering

For at sikre, at din AI-model er etisk forsvarlig og sikker, er det afgørende at evaluere den i forhold til Microsofts Responsible AI-principper. I Azure AI Foundry giver sikkerhedsevalueringer dig mulighed for at vurdere modellens sårbarhed over for jailbreak-angreb og dens potentiale til at generere skadeligt indhold, hvilket er direkte i tråd med disse principper.

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.da.png)

*Billedkilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts Responsible AI-principper

Før du går i gang med de tekniske trin, er det vigtigt at forstå Microsofts Responsible AI-principper, som er et etisk rammeværk designet til at vejlede ansvarlig udvikling, implementering og drift af AI-systemer. Disse principper styrer den ansvarlige design, udvikling og implementering af AI-systemer og sikrer, at AI-teknologier bygges på en måde, der er retfærdig, gennemsigtig og inkluderende. Disse principper danner grundlaget for evalueringen af AI-modellers sikkerhed.

Microsofts Responsible AI-principper omfatter:

- **Retfærdighed og inklusion**: AI-systemer bør behandle alle retfærdigt og undgå at påvirke lignende grupper forskelligt. For eksempel, når AI-systemer giver vejledning om medicinsk behandling, låneansøgninger eller ansættelse, bør de give de samme anbefalinger til alle med lignende symptomer, økonomiske forhold eller faglige kvalifikationer.

- **Pålidelighed og sikkerhed**: For at opbygge tillid er det afgørende, at AI-systemer fungerer pålideligt, sikkert og konsekvent. Disse systemer skal kunne fungere som oprindeligt designet, reagere sikkert på uforudsete situationer og modstå skadelig manipulation. Deres adfærd og de forskellige betingelser, de kan håndtere, afspejler de situationer og omstændigheder, som udviklerne havde forudset under design og test.

- **Gennemsigtighed**: Når AI-systemer hjælper med beslutninger, der har stor indflydelse på folks liv, er det vigtigt, at folk forstår, hvordan beslutningerne blev truffet. For eksempel kan en bank bruge et AI-system til at afgøre, om en person er kreditværdig. En virksomhed kan bruge et AI-system til at finde de mest kvalificerede kandidater til ansættelse.

- **Privatliv og sikkerhed**: Efterhånden som AI bliver mere udbredt, bliver beskyttelse af privatliv og sikring af personlige og forretningsmæssige oplysninger mere vigtigt og komplekst. Med AI kræver privatliv og datasikkerhed særlig opmærksomhed, fordi adgang til data er afgørende for, at AI-systemer kan lave præcise og velinformerede forudsigelser og beslutninger om mennesker.

- **Ansvarlighed**: De personer, der designer og implementerer AI-systemer, skal holdes ansvarlige for, hvordan deres systemer fungerer. Organisationer bør anvende branchestandarder for at udvikle ansvarlighedsnormer. Disse normer kan sikre, at AI-systemer ikke er den endelige myndighed i beslutninger, der påvirker menneskers liv. De kan også sikre, at mennesker bevarer meningsfuld kontrol over ellers meget autonome AI-systemer.

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.da.png)

*Billedkilde: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> For at lære mere om Microsofts Responsible AI-principper, besøg [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Sikkerhedsmålinger

I denne vejledning vil du evaluere sikkerheden af den finjusterede Phi-3 model ved hjælp af Azure AI Foundrys sikkerhedsmålinger. Disse målinger hjælper dig med at vurdere modellens potentiale for at generere skadeligt indhold og dens sårbarhed over for jailbreak-angreb. Sikkerhedsmålingerne inkluderer:

- **Indhold relateret til selvskade**: Vurderer om modellen har en tendens til at producere indhold relateret til selvskade.
- **Hadefuldt og uretfærdigt indhold**: Vurderer om modellen har en tendens til at producere hadefuldt eller uretfærdigt indhold.
- **Voldeligt indhold**: Vurderer om modellen har en tendens til at producere voldeligt indhold.
- **Seksuelt indhold**: Vurderer om modellen har en tendens til at producere upassende seksuelt indhold.

Ved at evaluere disse aspekter sikrer du, at AI-modellen ikke producerer skadeligt eller stødende indhold, hvilket bringer den i overensstemmelse med samfundsmæssige værdier og lovgivningsmæssige standarder.

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.da.png)

### Introduktion til ydeevneevaluering

For at sikre, at din AI-model præsterer som forventet, er det vigtigt at evaluere dens ydeevne i forhold til ydeevnemålinger. I Azure AI Foundry giver ydeevneevalueringer dig mulighed for at vurdere modellens effektivitet i at generere præcise, relevante og sammenhængende svar.

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.da.png)

*Billedkilde: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Ydeevnemålinger

I denne vejledning vil du evaluere ydeevnen af den finjusterede Phi-3 / Phi-3.5 model ved hjælp af Azure AI Foundrys ydeevnemålinger. Disse målinger hjælper dig med at vurdere modellens effektivitet i at generere præcise, relevante og sammenhængende svar. Ydeevnemålingerne inkluderer:

- **Groundedness**: Vurderer hvor godt de genererede svar stemmer overens med informationen fra inputkilden.
- **Relevans**: Vurderer hvor relevante de genererede svar er i forhold til de stillede spørgsmål.
- **Sammenhæng**: Vurderer hvor flydende den genererede tekst er, om den læses naturligt og ligner menneskelig sprogbrug.
- **Flydende sprog**: Vurderer sprogfærdigheden i den genererede tekst.
- **GPT-lighed**: Sammenligner det genererede svar med sandheden for lighed.
- **F1-score**: Beregner andelen af fælles ord mellem det genererede svar og kildedataene.

Disse målinger hjælper dig med at vurdere modellens effektivitet i at levere præcise, relevante og sammenhængende svar.

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.da.png)

## **Scenario 2: Evaluering af Phi-3 / Phi-3.5 modellen i Azure AI Foundry**

### Før du går i gang

Denne vejledning er en opfølgning på de tidligere blogindlæg, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" og "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." I disse indlæg gennemgik vi processen med at finjustere en Phi-3 / Phi-3.5 model i Azure AI Foundry og integrere den med Prompt flow.

I denne vejledning vil du deployere en Azure OpenAI-model som evaluator i Azure AI Foundry og bruge den til at evaluere din finjusterede Phi-3 / Phi-3.5 model.

Før du går i gang med denne vejledning, skal du sikre dig, at du har følgende forudsætninger, som beskrevet i de tidligere vejledninger:

1. Et forberedt datasæt til evaluering af den finjusterede Phi-3 / Phi-3.5 model.
1. En Phi-3 / Phi-3.5 model, der er finjusteret og deployeret til Azure Machine Learning.
1. En Prompt flow integreret med din finjusterede Phi-3 / Phi-3.5 model i Azure AI Foundry.

> [!NOTE]
> Du vil bruge filen *test_data.jsonl*, som findes i data-mappen fra **ULTRACHAT_200k** datasættet, der blev downloadet i de tidligere blogindlæg, som datasæt til evaluering af den finjusterede Phi-3 / Phi-3.5 model.

#### Integrer den tilpassede Phi-3 / Phi-3.5 model med Prompt flow i Azure AI Foundry (Kode-først tilgang)

> [!NOTE]
> Hvis du fulgte den low-code tilgang, som er beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kan du springe denne øvelse over og gå videre til den næste.
> Hvis du derimod fulgte kode-først tilgangen, som er beskrevet i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" for at finjustere og deployere din Phi-3 / Phi-3.5 model, er processen til at forbinde din model med Prompt flow en smule anderledes. Du vil lære denne proces i denne øvelse.

For at fortsætte skal du integrere din finjusterede Phi-3 / Phi-3.5 model i Prompt flow i Azure AI Foundry.

#### Opret Azure AI Foundry Hub

Du skal oprette et Hub, før du opretter et Projekt. Et Hub fungerer som en Resource Group og giver dig mulighed for at organisere og administrere flere Projekter inden for Azure AI Foundry.

1. Log ind på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Vælg **All hubs** fra venstre sidepanel.

1. Vælg **+ New hub** i navigationsmenuen.

    ![Create hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.da.png)

1. Udfør følgende opgaver:

    - Indtast **Hub name**. Det skal være en unik værdi.
    - Vælg dit Azure **Subscription**.
    - Vælg den **Resource group**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg den **Location**, du ønsker at bruge.
    - Vælg **Connect Azure AI Services** (opret en ny, hvis nødvendigt).
    - Vælg **Connect Azure AI Search** og vælg **Skip connecting**.
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.da.png)

1. Vælg **Next**.

#### Opret Azure AI Foundry-projekt

1. I det Hub, du har oprettet, vælg **All projects** i fanen til venstre.

1. Vælg **+ New project** i navigationsmenuen.

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.da.png)

1. Indtast **Project name**. Det skal være en unik værdi.

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.da.png)

1. Vælg **Create a project**.

#### Tilføj en brugerdefineret forbindelse til den finjusterede Phi-3 / Phi-3.5 model

For at integrere din brugerdefinerede Phi-3 / Phi-3.5 model med Prompt flow, skal du gemme modellens endpoint og nøgle i en brugerdefineret forbindelse. Denne opsætning sikrer adgang til din brugerdefinerede Phi-3 / Phi-3.5 model i Prompt flow.

#### Indstil api-nøgle og endpoint-uri for den finjusterede Phi-3 / Phi-3.5 model

1. Besøg [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviger til det Azure Machine learning workspace, du har oprettet.

1. Vælg **Endpoints** i fanen til venstre.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.da.png)

1. Vælg det endpoint, du har oprettet.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.da.png)

1. Vælg **Consume** i navigationsmenuen.

1. Kopiér din **REST endpoint** og **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.da.png)

#### Tilføj den brugerdefinerede forbindelse

1. Besøg [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til det Azure AI Foundry-projekt, du har oprettet.

1. I det projekt, du har oprettet, vælg **Settings** i fanen til venstre.

1. Vælg **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.da.png)

1. Vælg **Custom keys** i navigationsmenuen.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.da.png)

1. Udfør følgende opgaver:

    - Vælg **+ Add key value pairs**.
    - For nøglens navn indtast **endpoint** og indsæt det endpoint, du kopierede fra Azure ML Studio, i værdifeltet.
    - Vælg **+ Add key value pairs** igen.
    - For nøglens navn indtast **key** og indsæt den nøgle, du kopierede fra Azure ML Studio, i værdifeltet.
    - Efter tilføjelse af nøglerne, vælg **is secret** for at forhindre, at nøglen bliver synlig.

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.da.png)

1. Vælg **Add connection**.

#### Opret Prompt flow

Du har tilføjet en brugerdefineret forbindelse i Azure AI Foundry. Lad os nu oprette en Prompt flow ved hjælp af følgende trin. Derefter forbinder du denne Prompt flow til den brugerdefinerede forbindelse for at bruge den finjusterede model i Prompt flow.

1. Naviger til det Azure AI Foundry-projekt, du har oprettet.

1. Vælg **Prompt flow** i fanen til venstre.

1. Vælg **+ Create** i navigationsmenuen.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.da.png)

1. Vælg **Chat flow** i navigationsmenuen.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.da.png)

1. Indtast **Folder name**, som du vil bruge.

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.da.png)

1. Vælg **Create**.

#### Opsæt Prompt flow til at chatte med din brugerdefinerede Phi-3 / Phi-3.5 model

Du skal integrere den finjusterede Phi-3 / Phi-3.5 model i en Prompt flow. Den eksisterende Prompt flow, der leveres, er dog ikke designet til dette formål. Derfor skal du redesigne Prompt flow for at muliggøre integration af den brugerdefinerede model.

1. I Prompt flow skal du udføre følgende opgaver for at genopbygge den eksisterende flow:

    - Vælg **Raw file mode**.
    - Slet al eksisterende kode i filen *flow.dag.yml*.
    - Tilføj følgende kode til *flow.dag.yml*.

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

    - Vælg **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.da.png)

1. Tilføj følgende kode til *integrate_with_promptflow.py* for at bruge den brugerdefinerede Phi-3 / Phi-3.5 model i Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.da.png)

> [!NOTE]
> For mere detaljeret information om brug af Prompt flow i Azure AI Foundry, kan du se [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vælg **Chat input**, **Chat output** for at aktivere chat med din model.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.da.png)

1. Nu er du klar til at chatte med din brugerdefinerede Phi-3 / Phi-3.5 model. I den næste øvelse lærer du, hvordan du starter Prompt flow og bruger det til at chatte med din finjusterede Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> Den genopbyggede flow bør se ud som på billedet nedenfor:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.da.png)
>

#### Start Prompt flow

1. Vælg **Start compute sessions** for at starte Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.da.png)

1. Vælg **Validate and parse input** for at opdatere parametre.

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.da.png)

1. Vælg **Value** for **connection** til den brugerdefinerede forbindelse, du har oprettet. For eksempel *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.da.png)

#### Chat med din brugerdefinerede Phi-3 / Phi-3.5 model

1. Vælg **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.da.png)

1. Her er et eksempel på resultaterne: Nu kan du chatte med din brugerdefinerede Phi-3 / Phi-3.5 model. Det anbefales at stille spørgsmål baseret på de data, der er brugt til finjustering.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.da.png)

### Udrul Azure OpenAI for at evaluere Phi-3 / Phi-3.5 modellen

For at evaluere Phi-3 / Phi-3.5 modellen i Azure AI Foundry, skal du udrulle en Azure OpenAI-model. Denne model vil blive brugt til at evaluere Phi-3 / Phi-3.5 modellens ydeevne.

#### Udrul Azure OpenAI

1. Log ind på [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til det Azure AI Foundry-projekt, du har oprettet.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.da.png)

1. I det projekt, du har oprettet, vælg **Deployments** i fanen til venstre.

1. Vælg **+ Deploy model** i navigationsmenuen.

1. Vælg **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.da.png)

1. Vælg den Azure OpenAI-model, du ønsker at bruge. For eksempel **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.da.png)

1. Vælg **Confirm**.

### Evaluer den finjusterede Phi-3 / Phi-3.5 model ved hjælp af Azure AI Foundrys Prompt flow evaluering

### Start en ny evaluering

1. Besøg [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Naviger til det Azure AI Foundry-projekt, du har oprettet.

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.da.png)

1. I det projekt, du har oprettet, vælg **Evaluation** i fanen til venstre.

1. Vælg **+ New evaluation** i navigationsmenuen.
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.da.png)

1. Vælg **Prompt flow** evaluering.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.da.png)

1. Udfør følgende opgaver:

    - Indtast evalueringsnavnet. Det skal være en unik værdi.
    - Vælg **Question and answer without context** som opgavetype. Fordi datasættet **UlTRACHAT_200k**, der bruges i denne vejledning, ikke indeholder kontekst.
    - Vælg den prompt flow, du ønsker at evaluere.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.da.png)

1. Vælg **Next**.

1. Udfør følgende opgaver:

    - Vælg **Add your dataset** for at uploade datasættet. For eksempel kan du uploade testdatasættet, som *test_data.json1*, der følger med, når du downloader **ULTRACHAT_200k** datasættet.
    - Vælg den relevante **Dataset column**, som matcher dit datasæt. For eksempel, hvis du bruger **ULTRACHAT_200k** datasættet, vælg **${data.prompt}** som datasøjle.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.da.png)

1. Vælg **Next**.

1. Udfør følgende opgaver for at konfigurere performance- og kvalitetsmålinger:

    - Vælg de performance- og kvalitetsmålinger, du ønsker at bruge.
    - Vælg den Azure OpenAI-model, du har oprettet til evalueringen. For eksempel vælg **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.da.png)

1. Udfør følgende opgaver for at konfigurere risikio- og sikkerhedsmål:

    - Vælg de risikio- og sikkerhedsmål, du ønsker at bruge.
    - Vælg tærsklen for at beregne fejlprocenten, som du vil bruge. For eksempel vælg **Medium**.
    - For **question**, vælg **Data source** til **{$data.prompt}**.
    - For **answer**, vælg **Data source** til **{$run.outputs.answer}**.
    - For **ground_truth**, vælg **Data source** til **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.da.png)

1. Vælg **Next**.

1. Vælg **Submit** for at starte evalueringen.

1. Evalueringen vil tage noget tid at gennemføre. Du kan følge fremskridtet under fanen **Evaluation**.

### Gennemgå evalueringsresultaterne

> [!NOTE]
> Resultaterne vist nedenfor er til illustration af evalueringsprocessen. I denne vejledning har vi brugt en model finjusteret på et relativt lille datasæt, hvilket kan føre til suboptimale resultater. Faktiske resultater kan variere betydeligt afhængigt af størrelsen, kvaliteten og mangfoldigheden af det anvendte datasæt samt den specifikke konfiguration af modellen.

Når evalueringen er færdig, kan du gennemgå resultaterne for både performance- og sikkerhedsmål.

1. Performance- og kvalitetsmålinger:

    - vurder modellens effektivitet i at generere sammenhængende, flydende og relevante svar.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.da.png)

1. Risiko- og sikkerhedsmål:

    - Sørg for, at modellens output er sikre og overholder Responsible AI-principperne, og undgår skadeligt eller stødende indhold.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.da.png)

1. Du kan scrolle ned for at se **Detailed metrics result**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.da.png)

1. Ved at evaluere din tilpassede Phi-3 / Phi-3.5 model på både performance- og sikkerhedsmål, kan du bekræfte, at modellen ikke kun er effektiv, men også følger ansvarlige AI-principper og dermed er klar til anvendelse i praksis.

## Tillykke!

### Du har gennemført denne vejledning

Du har med succes evalueret den finjusterede Phi-3 model integreret med Prompt flow i Azure AI Foundry. Dette er et vigtigt skridt for at sikre, at dine AI-modeller ikke kun præsterer godt, men også overholder Microsofts Responsible AI-principper, så du kan bygge pålidelige og troværdige AI-applikationer.

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.da.png)

## Ryd op i Azure-ressourcer

Ryd op i dine Azure-ressourcer for at undgå yderligere omkostninger på din konto. Gå til Azure-portalen og slet følgende ressourcer:

- Azure Machine learning-ressourcen.
- Azure Machine learning model-endpoint.
- Azure AI Foundry Project-ressourcen.
- Azure AI Foundry Prompt flow-ressourcen.

### Næste skridt

#### Dokumentation

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Træningsindhold

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Reference

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.