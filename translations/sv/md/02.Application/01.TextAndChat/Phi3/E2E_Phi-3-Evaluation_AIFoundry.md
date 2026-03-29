# Utvärdera den finjusterade Phi-3 / Phi-3.5-modellen i Microsoft Foundry med fokus på Microsofts principer för ansvarsfull AI

Detta end-to-end (E2E) exempel är baserat på guiden "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" från Microsoft Tech Community.

## Översikt

### Hur kan du utvärdera säkerheten och prestandan för en finjusterad Phi-3 / Phi-3.5-modell i Microsoft Foundry?

Finjustering av en modell kan ibland leda till oavsiktliga eller oönskade svar. För att säkerställa att modellen förblir säker och effektiv är det viktigt att utvärdera modellens potentiella förmåga att generera skadligt innehåll samt dess förmåga att producera korrekta, relevanta och sammanhängande svar. I denna handledning lär du dig hur du utvärderar säkerheten och prestandan för en finjusterad Phi-3 / Phi-3.5-modell som är integrerad med Prompt flow i Microsoft Foundry.

Här är Microsoft Foundrys utvärderingsprocess.

![Architecture of tutorial.](../../../../../../translated_images/sv/architecture.10bec55250f5d6a4.webp)

*Bildkälla: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> För mer detaljerad information och för att utforska ytterligare resurser om Phi-3 / Phi-3.5, vänligen besök [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Förutsättningar

- [Python](https://www.python.org/downloads)
- [Azure-prenumeration](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Finjusterad Phi-3 / Phi-3.5-modell

### Innehållsförteckning

1. [**Scenario 1: Introduktion till Microsoft Foundrys Prompt flow-utvärdering**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Introduktion till säkerhetsutvärdering](#introduktion-till-säkerhetsutvärdering)
    - [Introduktion till prestandautvärdering](#introduktion-till-prestandautvärdering)

1. [**Scenario 2: Utvärdera Phi-3 / Phi-3.5-modellen i Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Innan du börjar](#innan-du-börjar)
    - [Distribuera Azure OpenAI för att utvärdera Phi-3 / Phi-3.5-modellen](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Utvärdera den finjusterade Phi-3 / Phi-3.5-modellen med Microsoft Foundrys Prompt flow-utvärdering](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Grattis!](#grattis)

## **Scenario 1: Introduktion till Microsoft Foundrys Prompt flow-utvärdering**

### Introduktion till säkerhetsutvärdering

För att säkerställa att din AI-modell är etisk och säker är det avgörande att utvärdera den enligt Microsofts principer för ansvarsfull AI. I Microsoft Foundry gör säkerhetsutvärderingar det möjligt att bedöma din modells sårbarhet för jailbreak-attacker och dess potential att generera skadligt innehåll, vilket är direkt kopplat till dessa principer.

![Safaty evaluation.](../../../../../../translated_images/sv/safety-evaluation.083586ec88dfa950.webp)

*Bildkälla: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsofts principer för ansvarsfull AI

Innan du börjar med de tekniska stegen är det viktigt att förstå Microsofts principer för ansvarsfull AI, en etisk ram designad för att vägleda ansvarsfull utveckling, distribution och drift av AI-system. Dessa principer styr ansvarsfull design, utveckling och implementering av AI-system för att säkerställa att AI-teknologier byggs på ett rättvist, transparent och inkluderande sätt. Dessa principer utgör grunden för att utvärdera säkerheten hos AI-modeller.

Microsofts principer för ansvarsfull AI inkluderar:

- **Rättvisa och inkludering**: AI-system ska behandla alla rättvist och undvika att påverka liknande grupper av människor på olika sätt. Till exempel, när AI-system ger vägledning om medicinsk behandling, låneansökningar eller anställning, ska de ge samma rekommendationer till alla som har liknande symtom, ekonomiska förutsättningar eller yrkesmeriter.

- **Tillförlitlighet och säkerhet**: För att skapa förtroende är det avgörande att AI-system fungerar tillförlitligt, säkert och konsekvent. Dessa system bör kunna fungera som de ursprungligen designades, svara säkert på oförutsedda situationer och motstå skadlig manipulering. Hur de beter sig och vilka olika situationer de kan hantera speglar det spann av omständigheter som utvecklarna förväntade sig vid design och testning.

- **Transparens**: När AI-system hjälper till att informera beslut som har stora konsekvenser för människors liv är det avgörande att människor förstår hur dessa beslut fattades. Till exempel kan en bank använda ett AI-system för att avgöra om en person är kreditvärdig. Ett företag kan använda ett AI-system för att bestämma vilka kandidater som är mest kvalificerade att anställa.

- **Integritet och säkerhet**: När AI blir allt vanligare blir skyddet av integritet och säkring av personlig och affärsrelaterad information allt viktigare och mer komplext. Med AI kräver integritet och datasäkerhet särskild uppmärksamhet eftersom tillgång till data är avgörande för att AI-system ska kunna göra korrekta och välgrundade förutsägelser och beslut om människor.

- **Ansvarsutkrävande**: De personer som designar och distribuerar AI-system måste hållas ansvariga för hur deras system fungerar. Organisationer bör använda sig av branschstandarder för att utveckla normer för ansvarstagande. Dessa normer kan säkerställa att AI-system inte är den sista auktoriteten i beslut som påverkar människors liv. De kan också säkerställa att människor behåller meningsfull kontroll över i övrigt högt autonoma AI-system.

![Fill hub.](../../../../../../translated_images/sv/responsibleai2.c07ef430113fad8c.webp)

*Bildkälla: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> För att lära dig mer om Microsofts principer för ansvarsfull AI, besök [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Säkerhetsmått

I denna handledning kommer du att utvärdera säkerheten hos den finjusterade Phi-3-modellen med hjälp av Microsoft Foundrys säkerhetsmått. Dessa mått hjälper dig att bedöma modellens potential att generera skadligt innehåll och dess sårbarhet för jailbreak-attacker. Säkerhetsmåtten inkluderar:

- **Innehåll relaterat till självskada**: Utvärderar om modellen har en tendens att producera innehåll relaterat till självskada.
- **Hatfullt och orättvist innehåll**: Utvärderar om modellen har en tendens att producera hatfullt eller orättvist innehåll.
- **Våldsamt innehåll**: Utvärderar om modellen har en tendens att producera våldsamt innehåll.
- **Sexuellt innehåll**: Utvärderar om modellen har en tendens att producera olämpligt sexuellt innehåll.

Att utvärdera dessa aspekter säkerställer att AI-modellen inte producerar skadligt eller stötande innehåll, vilket stämmer överens med samhälleliga värderingar och regelverk.

![Evaluate based on safety.](../../../../../../translated_images/sv/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introduktion till prestandautvärdering

För att säkerställa att din AI-modell presterar som förväntat är det viktigt att utvärdera dess prestanda mot prestandamått. I Microsoft Foundry gör prestandautvärderingar det möjligt att utvärdera din modells effektivitet i att generera korrekta, relevanta och sammanhängande svar.

![Safaty evaluation.](../../../../../../translated_images/sv/performance-evaluation.48b3e7e01a098740.webp)

*Bildkälla: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prestandamått

I denna handledning kommer du att utvärdera prestandan hos den finjusterade Phi-3 / Phi-3.5-modellen med Microsoft Foundrys prestandamått. Dessa mått hjälper dig att bedöma modellens effektivitet i att generera korrekta, relevanta och sammanhängande svar. Prestandamåtten inkluderar:

- **Grundlighet**: Utvärdera hur väl de genererade svaren stämmer överens med information från insatskällan.
- **Relevans**: Utvärderar hur pass relevanta de genererade svaren är i förhållande till givna frågor.
- **Sammanhang**: Utvärdera hur smidigt den genererade texten flyter, läses naturligt och liknar mänskligt språk.
- **Flyt**: Utvärdera språkfärdigheten i den genererade texten.
- **GPT-likhet**: Jämför det genererade svaret med den faktiska sanningen för likhet.
- **F1-poäng**: Beräknar andelen ord som delas mellan det genererade svaret och källdata.

Dessa mått hjälper dig att utvärdera modellens effektivitet i att skapa korrekta, relevanta och sammanhängande svar.

![Evaluate based on performance.](../../../../../../translated_images/sv/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenario 2: Utvärdera Phi-3 / Phi-3.5-modellen i Microsoft Foundry**

### Innan du börjar

Denna handledning följer upp de tidigare blogginläggen, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" och "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." I dessa inlägg gick vi igenom processen att finjustera en Phi-3 / Phi-3.5-modell i Microsoft Foundry och integrera den med Prompt flow.

I denna handledning kommer du att distribuera en Azure OpenAI-modell som en bedömare i Microsoft Foundry och använda den för att utvärdera din finjusterade Phi-3 / Phi-3.5-modell.

Innan du börjar denna handledning, se till att du har följande förutsättningar, som beskrivs i de tidigare handledningarna:

1. En förberedd dataset för att utvärdera den finjusterade Phi-3 / Phi-3.5-modellen.
1. En Phi-3 / Phi-3.5-modell som har finjusterats och distribuerats till Azure Machine Learning.
1. En Prompt flow integrerad med din finjusterade Phi-3 / Phi-3.5-modell i Microsoft Foundry.

> [!NOTE]
> Du kommer att använda filen *test_data.jsonl*, som finns i data-mappen från **ULTRACHAT_200k**-datasetet nedladdat i de tidigare blogginläggen, som dataset för att utvärdera den finjusterade Phi-3 / Phi-3.5-modellen.

#### Integrera den anpassade Phi-3 / Phi-3.5-modellen med Prompt flow i Microsoft Foundry (Kod-först-ansats)

> [!NOTE]
> Om du följde lågkodsmetoden som beskrivs i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kan du hoppa över denna övning och fortsätta till nästa.
> Men om du följde kod-först-ansatsen som beskrivs i "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" för att finjustera och distribuera din Phi-3 / Phi-3.5-modell, är processen för att koppla din modell till Prompt flow något annorlunda. Den processen lär du dig i denna övning.

För att gå vidare behöver du integrera din finjusterade Phi-3 / Phi-3.5-modell i Prompt flow i Microsoft Foundry.

#### Skapa Microsoft Foundry Hub

Du behöver skapa en Hub innan du skapar Projektet. En Hub fungerar som en resursgrupp och gör det möjligt att organisera och hantera flera projekt inom Microsoft Foundry.
1. Logga in på [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Välj **All hubs** från fliken till vänster.

1. Välj **+ New hub** från navigationsmenyn.

    ![Create hub.](../../../../../../translated_images/sv/create-hub.5be78fb1e21ffbf1.webp)

1. Utför följande uppgifter:

    - Ange **Hub name**. Det måste vara ett unikt värde.
    - Välj din Azure **Subscription**.
    - Välj **Resource group** att använda (skapa en ny om det behövs).
    - Välj den **Location** du vill använda.
    - Välj **Connect Azure AI Services** att använda (skapa en ny om det behövs).
    - Välj **Connect Azure AI Search** för att **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/sv/fill-hub.baaa108495c71e34.webp)

1. Välj **Next**.

#### Skapa Microsoft Foundry-projekt

1. I hubben som du skapade, välj **All projects** från fliken till vänster.

1. Välj **+ New project** från navigationsmenyn.

    ![Select new project.](../../../../../../translated_images/sv/select-new-project.cd31c0404088d7a3.webp)

1. Ange **Project name**. Det måste vara ett unikt värde.

    ![Create project.](../../../../../../translated_images/sv/create-project.ca3b71298b90e420.webp)

1. Välj **Create a project**.

#### Lägg till en anpassad anslutning för den finjusterade Phi-3 / Phi-3.5 modellen

För att integrera din anpassade Phi-3 / Phi-3.5 modell med Prompt flow måste du spara modellens endpoint och nyckel i en anpassad anslutning. Denna konfiguration säkerställer åtkomst till din anpassade Phi-3 / Phi-3.5 modell i Prompt flow.

#### Ställ in api-nyckeln och endpoint-uri för den finjusterade Phi-3 / Phi-3.5 modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigera till det Azure Machine learning-arbetsytan som du skapade.

1. Välj **Endpoints** från fliken till vänster.

    ![Select endpoints.](../../../../../../translated_images/sv/select-endpoints.ee7387ecd68bd18d.webp)

1. Välj den endpoint du skapade.

    ![Select endpoints.](../../../../../../translated_images/sv/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Välj **Consume** från navigationsmenyn.

1. Kopiera din **REST endpoint** och **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/sv/copy-endpoint-key.0650c3786bd646ab.webp)

#### Lägg till den anpassade anslutningen

1. Besök [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigera till det Microsoft Foundry-projekt som du skapade.

1. I projektet som du skapade, välj **Settings** från fliken till vänster.

1. Välj **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/sv/select-new-connection.fa0f35743758a74b.webp)

1. Välj **Custom keys** från navigationsmenyn.

    ![Select custom keys.](../../../../../../translated_images/sv/select-custom-keys.5a3c6b25580a9b67.webp)

1. Utför följande uppgifter:

    - Välj **+ Add key value pairs**.
    - För nyckelns namn, skriv **endpoint** och klistra in endpointen du kopierade från Azure ML Studio i värdefältet.
    - Välj **+ Add key value pairs** igen.
    - För nyckelns namn, skriv **key** och klistra in nyckeln du kopierade från Azure ML Studio i värdefältet.
    - Efter att ha lagt till nycklarna, välj **is secret** för att förhindra att nyckeln exponeras.

    ![Add connection.](../../../../../../translated_images/sv/add-connection.ac7f5faf8b10b0df.webp)

1. Välj **Add connection**.

#### Skapa Prompt flow

Du har lagt till en anpassad anslutning i Microsoft Foundry. Nu låt oss skapa en Prompt flow med följande steg. Sedan kommer du att ansluta denna Prompt flow till den anpassade anslutningen för att använda den finjusterade modellen inom Prompt flow.

1. Navigera till det Microsoft Foundry-projekt som du skapade.

1. Välj **Prompt flow** från fliken till vänster.

1. Välj **+ Create** från navigationsmenyn.

    ![Select Promptflow.](../../../../../../translated_images/sv/select-promptflow.18ff2e61ab9173eb.webp)

1. Välj **Chat flow** från navigationsmenyn.

    ![Select chat flow.](../../../../../../translated_images/sv/select-flow-type.28375125ec9996d3.webp)

1. Ange **Folder name** att använda.

    ![Select chat flow.](../../../../../../translated_images/sv/enter-name.02ddf8fb840ad430.webp)

1. Välj **Create**.

#### Ställ in Prompt flow för att chatta med din anpassade Phi-3 / Phi-3.5 modell

Du måste integrera den finjusterade Phi-3 / Phi-3.5 modellen i en Prompt flow. Den befintliga Prompt flow som tillhandahålls är dock inte utformad för detta ändamål. Därför måste du omdesigna Prompt flow för att möjliggöra integration av den anpassade modellen.

1. I Prompt flow, utför följande uppgifter för att bygga om den befintliga flowen:

    - Välj **Raw file mode**.
    - Radera all existerande kod i filen *flow.dag.yml*.
    - Lägg till följande kod i *flow.dag.yml*.

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

    - Välj **Save**.

    ![Select raw file mode.](../../../../../../translated_images/sv/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Lägg till följande kod i *integrate_with_promptflow.py* för att använda den anpassade Phi-3 / Phi-3.5 modellen i Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logginställning
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

        # "connection" är namnet på den anpassade anslutningen, "endpoint", "key" är nycklarna i den anpassade anslutningen
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
            
            # Logga hela JSON-svaret
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

    ![Paste prompt flow code.](../../../../../../translated_images/sv/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> För mer detaljerad information om hur man använder Prompt flow i Microsoft Foundry, kan du hänvisa till [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Välj **Chat input**, **Chat output** för att aktivera chatt med din modell.

    ![Select Input Output.](../../../../../../translated_images/sv/select-input-output.c187fc58f25fbfc3.webp)

1. Nu är du redo att chatta med din anpassade Phi-3 / Phi-3.5 modell. I nästa övning kommer du att lära dig hur du startar Prompt flow och använder den för att chatta med din finjusterade Phi-3 / Phi-3.5 modell.

> [!NOTE]
>
> Den ombyggda flowen bör se ut som bilden nedan:
>
> ![Flow example](../../../../../../translated_images/sv/graph-example.82fd1bcdd3fc545b.webp)
>

#### Starta Prompt flow

1. Välj **Start compute sessions** för att starta Prompt flow.

    ![Start compute session.](../../../../../../translated_images/sv/start-compute-session.9acd8cbbd2c43df1.webp)

1. Välj **Validate and parse input** för att förnya parametrarna.

    ![Validate input.](../../../../../../translated_images/sv/validate-input.c1adb9543c6495be.webp)

1. Välj **Value** för **connection** till den anpassade anslutning som du skapade. Till exempel, *connection*.

    ![Connection.](../../../../../../translated_images/sv/select-connection.1f2b59222bcaafef.webp)

#### Chatta med din anpassade Phi-3 / Phi-3.5 modell

1. Välj **Chat**.

    ![Select chat.](../../../../../../translated_images/sv/select-chat.0406bd9687d0c49d.webp)

1. Här är ett exempel på resultaten: Nu kan du chatta med din anpassade Phi-3 / Phi-3.5 modell. Det rekommenderas att ställa frågor baserade på den data som användes för finjustering.

    ![Chat with prompt flow.](../../../../../../translated_images/sv/chat-with-promptflow.1cf8cea112359ada.webp)

### Distribuera Azure OpenAI för att utvärdera Phi-3 / Phi-3.5 modellen

För att utvärdera Phi-3 / Phi-3.5 modellen i Microsoft Foundry måste du distribuera en Azure OpenAI-modell. Denna modell kommer att användas för att utvärdera prestandan hos Phi-3 / Phi-3.5 modellen.

#### Distribuera Azure OpenAI

1. Logga in på [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigera till det Microsoft Foundry-projekt som du skapade.

    ![Select Project.](../../../../../../translated_images/sv/select-project-created.5221e0e403e2c9d6.webp)

1. I projektet som du skapade, välj **Deployments** från fliken till vänster.

1. Välj **+ Deploy model** från navigationsmenyn.

1. Välj **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/sv/deploy-openai-model.95d812346b25834b.webp)

1. Välj vilken Azure OpenAI-modell du vill använda. Till exempel, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/sv/select-openai-model.959496d7e311546d.webp)

1. Välj **Confirm**.

### Utvärdera den finjusterade Phi-3 / Phi-3.5 modellen med Microsoft Foundrys Prompt flow-utvärdering

### Starta en ny utvärdering

1. Besök [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigera till det Microsoft Foundry-projekt som du skapade.

    ![Select Project.](../../../../../../translated_images/sv/select-project-created.5221e0e403e2c9d6.webp)

1. I projektet som du skapade, välj **Evaluation** från fliken till vänster.

1. Välj **+ New evaluation** från navigationsmenyn.

    ![Select evaluation.](../../../../../../translated_images/sv/select-evaluation.2846ad7aaaca7f4f.webp)

1. Välj **Prompt flow**-utvärdering.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/sv/promptflow-evaluation.cb9758cc19b4760f.webp)

1. utför följande uppgifter:

    - Ange utvärderingsnamnet. Det måste vara ett unikt värde.
    - Välj **Question and answer without context** som uppgiftstyp eftersom **ULTRACHAT_200k** datasetet som används i denna handledning inte innehåller kontext.
    - Välj den prompt flow som du vill utvärdera.

    ![Prompt flow evaluation.](../../../../../../translated_images/sv/evaluation-setting1.4aa08259ff7a536e.webp)

1. Välj **Next**.

1. utför följande uppgifter:

    - Välj **Add your dataset** för att ladda upp datasetet. Till exempel kan du ladda upp testdatamängdsfilen, som *test_data.json1*, som ingår när du laddar ner **ULTRACHAT_200k** datasetet.
    - Välj den lämpliga **Dataset column** som matchar ditt dataset. Till exempel, om du använder **ULTRACHAT_200k** datasetet, välj **${data.prompt}** som datasetkolumn.

    ![Prompt flow evaluation.](../../../../../../translated_images/sv/evaluation-setting2.07036831ba58d64e.webp)

1. Välj **Next**.

1. utför följande uppgifter för att konfigurera prestanda- och kvalitetsmått:

    - Välj de prestanda- och kvalitetsmått du vill använda.
    - Välj den Azure OpenAI-modell som du skapade för utvärdering. Till exempel, välj **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sv/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. utför följande uppgifter för att konfigurera risk- och säkerhetsmått:

    - Välj de risk- och säkerhetsmått du vill använda.
    - Välj tröskeln för att beräkna felprocent du vill använda. Till exempel, välj **Medium**.
    - För **question**, välj **Data source** till **{$data.prompt}**.
    - För **answer**, välj **Data source** till **{$run.outputs.answer}**.
    - För **ground_truth**, välj **Data source** till **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/sv/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Välj **Next**.

1. Välj **Submit** för att starta utvärderingen.

1. Utvärderingen kommer att ta lite tid att slutföra. Du kan följa processen i fliken **Evaluation**.

### Granska utvärderingsresultaten

> [!NOTE]
> Resultaten som presenteras nedan är avsedda att illustrera utvärderingsprocessen. I denna handledning har vi använt en modell finjusterad på ett relativt litet dataset, vilket kan leda till mindre optimala resultat. Faktiska resultat kan variera avsevärt beroende på datasetets storlek, kvalitet och mångfald samt den specifika konfigurationen av modellen.

När utvärderingen är klar kan du granska resultaten för både prestanda- och säkerhetsmått.
1. Prestanda- och kvalitetsmått:

    - utvärdera modellens effektivitet i att generera sammanhängande, flytande och relevanta svar.

    ![Evaluation result.](../../../../../../translated_images/sv/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Risk- och säkerhetsmått:

    - Säkerställ att modellens utskrifter är säkra och överensstämmer med principerna för Ansvarsfull AI, och undvik allt skadligt eller stötande innehåll.

    ![Evaluation result.](../../../../../../translated_images/sv/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Du kan scrolla ned för att visa **Detaljerat måttresultat**.

    ![Evaluation result.](../../../../../../translated_images/sv/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Genom att utvärdera din anpassade Phi-3 / Phi-3.5-modell mot både prestanda- och säkerhetsmått kan du bekräfta att modellen inte bara är effektiv utan också följer principerna för ansvarsfull AI, vilket gör den redo för verklig användning.

## Grattis!

### Du har slutfört denna handledning

Du har framgångsrikt utvärderat den finjusterade Phi-3-modellen integrerad med Prompt flow i Microsoft Foundry. Detta är ett viktigt steg för att säkerställa att dina AI-modeller inte bara presterar bra utan också följer Microsofts principer för Ansvarsfull AI för att hjälpa dig bygga pålitliga och trovärdiga AI-applikationer.

![Architecture.](../../../../../../translated_images/sv/architecture.10bec55250f5d6a4.webp)

## Rensa upp Azure-resurser

Rensa upp dina Azure-resurser för att undvika ytterligare avgifter på ditt konto. Gå till Azure-portalen och ta bort följande resurser:

- Azure Machine Learning-resursen.
- Azure Machine Learning-modellendpointen.
- Microsoft Foundry Project-resursen.
- Microsoft Foundry Prompt flow-resursen.

### Nästa steg

#### Dokumentation

- [Bedöm AI-system med hjälp av instrumentpanelen för Ansvarsfull AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Utvärderings- och övervakningsmått för generativ AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry-dokumentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-dokumentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Utbildningsinnehåll

- [Introduktion till Microsofts Ansvarsfulla AI-ansats](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduktion till Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referens

- [Vad är Ansvarsfull AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Tillkännagivande av nya verktyg i Azure AI som hjälper dig bygga säkrare och mer pålitliga generativa AI-applikationer](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Utvärdering av generativa AI-applikationer](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->