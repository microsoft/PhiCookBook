# Evalueer het fijn-afgestelde Phi-3 / Phi-3.5-model in Microsoft Foundry met focus op Microsofts Principle of Responsible AI

Deze end-to-end (E2E) voorbeeld is gebaseerd op de gids "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" van de Microsoft Tech Community.

## Overzicht

### Hoe kunt u de veiligheid en prestaties van een fijn-afgesteld Phi-3 / Phi-3.5-model in Microsoft Foundry evalueren?

Het fijn-afstellen van een model kan soms leiden tot onbedoelde of ongewenste reacties. Om te waarborgen dat het model veilig en effectief blijft, is het belangrijk om het potentieel van het model te beoordelen om schadelijke inhoud te genereren en zijn vermogen om nauwkeurige, relevante en coherente antwoorden te produceren. In deze tutorial leert u hoe u de veiligheid en prestaties van een fijn-afgesteld Phi-3 / Phi-3.5-model kunt evalueren dat geïntegreerd is met Prompt flow in Microsoft Foundry.

Hier is het evaluatieproces van Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/nl/architecture.10bec55250f5d6a4.webp)

*Afbeeldingsbron: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Voor meer gedetailleerde informatie en om aanvullende bronnen over Phi-3 / Phi-3.5 te verkennen, bezoek de [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Vereisten

- [Python](https://www.python.org/downloads)
- [Azure-abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fijn-afgesteld Phi-3 / Phi-3.5-model

### Inhoudsopgave

1. [**Scenario 1: Introductie tot Microsoft Foundry's Prompt flow evaluatie**](#scenario-1-introductie-tot-azure-ai-studios-prompt-flow-evaluatie)

    - [Introductie tot veiligheidsevaluatie](#introductie-tot-veiligheidsevaluatie)
    - [Introductie tot prestatie-evaluatie](#introductie-tot-prestatie-evaluatie)

1. [**Scenario 2: Evaluatie van het Phi-3 / Phi-3.5-model in Microsoft Foundry**](#scenario-2-evaluatie-van-het-phi-3--phi-35-model-in-azure-ai-studio)

    - [Voordat je begint](#voordat-je-begint)
    - [Azure OpenAI implementeren om het Phi-3 / Phi-3.5-model te evalueren](#azure-openai-implementeren-om-het-phi-3--phi-35-model-te-evalueren)
    - [Evalueer het fijn-afgestelde Phi-3 / Phi-3.5-model met Microsoft Foundry's Prompt flow evaluatie](#evalueer-het-fijn-afgestelde-phi-3--phi-35-model-met-azure-ai-studios-prompt-flow-evaluatie)

1. [Gefeliciteerd!](#gefeliciteerd)

## **Scenario 1: Introductie tot Microsoft Foundry's Prompt flow evaluatie**

### Introductie tot veiligheidsevaluatie

Om ervoor te zorgen dat uw AI-model ethisch en veilig is, is het cruciaal om het te evalueren aan de hand van Microsofts Responsible AI Principles. In Microsoft Foundry kunt u met veiligheidsevaluaties beoordelen hoe kwetsbaar uw model is voor jailbreak-aanvallen en zijn potentieel om schadelijke inhoud te genereren, wat direct aansluit bij deze principes.

![Safaty evaluation.](../../../../../../translated_images/nl/safety-evaluation.083586ec88dfa950.webp)

*Afbeeldingsbron: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft’s Responsible AI Principles

Voordat u begint met de technische stappen, is het essentieel om Microsofts Responsible AI Principles te begrijpen, een ethisch kader dat is ontworpen om de verantwoorde ontwikkeling, implementatie en werking van AI-systemen te begeleiden. Deze principes sturen het verantwoorde ontwerp, de ontwikkeling en uitrol van AI-systemen, waarmee wordt gegarandeerd dat AI-technologieën op een eerlijke, transparante en inclusieve manier worden gebouwd. Deze principes vormen de basis voor het evalueren van de veiligheid van AI-modellen.

Microsoft's Responsible AI Principles omvatten:

- **Eerlijkheid en Inclusiviteit**: AI-systemen moeten iedereen eerlijk behandelen en moeten vermijden dat gelijksoortige groepen mensen op verschillende manieren worden beïnvloed. Bijvoorbeeld, wanneer AI-systemen advies geven over medische behandeling, leningaanvragen of werkgelegenheid, moeten ze dezelfde aanbevelingen doen aan iedereen die vergelijkbare symptomen, financiële omstandigheden of professionele kwalificaties heeft.

- **Betrouwbaarheid en Veiligheid**: Om vertrouwen op te bouwen is het van cruciaal belang dat AI-systemen betrouwbaar, veilig en consistent werken. Deze systemen moeten in staat zijn te functioneren zoals oorspronkelijk ontworpen, veilig reageren op onvoorziene omstandigheden en schadelijke manipulatie weerstaan. Hoe ze zich gedragen en de verscheidenheid aan omstandigheden die ze aankunnen weerspiegelen de reeks situaties en omstandigheden die ontwikkelaars tijdens het ontwerp en testen hebben voorzien.

- **Transparantie**: Wanneer AI-systemen helpen bij beslissingen met enorme impact op het leven van mensen, is het belangrijk dat mensen begrijpen hoe die beslissingen tot stand zijn gekomen. Bijvoorbeeld, een bank kan een AI-systeem gebruiken om te bepalen of iemand kredietwaardig is. Een bedrijf kan een AI-systeem gebruiken om de meest gekwalificeerde kandidaten te selecteren.

- **Privacy en Beveiliging**: Nu AI meer en meer aanwezig is, wordt het beschermen van privacy en het beveiligen van persoonlijke en zakelijke informatie steeds belangrijker en complexer. Bij AI vereisen privacy en gegevensbeveiliging nauwgezette aandacht omdat toegang tot data essentieel is voor AI-systemen om nauwkeurige en goed geïnformeerde voorspellingen en beslissingen over mensen te maken.

- **Verantwoordingsplicht**: Personen die AI-systemen ontwerpen en implementeren moeten verantwoordelijk gehouden worden voor hoe hun systemen functioneren. Organisaties moeten industriestandaarden gebruiken om normen voor verantwoordelijkheid te ontwikkelen. Deze normen kunnen ervoor zorgen dat AI-systemen niet de eindautoriteit zijn bij beslissingen die het leven van mensen beïnvloeden. Ze kunnen ook garanderen dat mensen betekenisvol controle houden over anderszins zeer autonome AI-systemen.

![Fill hub.](../../../../../../translated_images/nl/responsibleai2.c07ef430113fad8c.webp)

*Afbeeldingsbron: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Voor meer informatie over Microsoft’s Responsible AI Principles, bezoek [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Veiligheidsstatistieken

In deze tutorial evalueert u de veiligheid van het fijn-afgestelde Phi-3-model met de veiligheidsstatistieken van Microsoft Foundry. Deze statistieken helpen u bij het beoordelen van het potentieel van het model om schadelijke inhoud te genereren en zijn kwetsbaarheid voor jailbreak-aanvallen. De veiligheidsstatistieken omvatten:

- **Inhoud met zelfbeschadiging**: Beoordeelt of het model de neiging heeft om inhoud te produceren die verband houdt met zelfbeschadiging.
- **Haatdragende en oneerlijke inhoud**: Beoordeelt of het model de neiging heeft om haatdragende of oneerlijke inhoud te produceren.
- **Gewelddadige inhoud**: Beoordeelt of het model de neiging heeft om gewelddadige inhoud te produceren.
- **Seksuele inhoud**: Beoordeelt of het model de neiging heeft om ongepaste seksuele inhoud te produceren.

Het evalueren van deze aspecten zorgt ervoor dat het AI-model geen schadelijke of aanstootgevende inhoud produceert, waarmee het aansluit bij maatschappelijke waarden en regelgeving.

![Evaluate based on safety.](../../../../../../translated_images/nl/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introductie tot prestatie-evaluatie

Om te garanderen dat uw AI-model presteert zoals verwacht, is het belangrijk om de prestaties te evalueren aan de hand van prestatiestatistieken. In Microsoft Foundry kunt u met prestatie-evaluaties de effectiviteit van uw model beoordelen in het genereren van nauwkeurige, relevante en coherente antwoorden.

![Safaty evaluation.](../../../../../../translated_images/nl/performance-evaluation.48b3e7e01a098740.webp)

*Afbeeldingsbron: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prestatiestatistieken

In deze tutorial evalueert u de prestaties van het fijn-afgestelde Phi-3 / Phi-3.5-model met de prestatiestatistieken van Microsoft Foundry. Deze statistieken helpen u bij het beoordelen van de effectiviteit van het model om nauwkeurige, relevante en coherente antwoorden te genereren. De prestatiestatistieken omvatten:

- **Gegrondheid**: Beoordeelt hoe goed de gegenereerde antwoorden overeenkomen met de informatie uit de bron.
- **Relevantie**: Beoordeelt de pertinentie van de gegenereerde antwoorden ten opzichte van de gestelde vragen.
- **Coherentie**: Beoordeelt hoe vloeiend de gegenereerde tekst is, of het natuurlijk leest en lijkt op menselijke taal.
- **Vlotheid**: Beoordeelt de taalvaardigheid van de gegenereerde tekst.
- **GPT Gelijkenis**: Vergelijkt het gegenereerde antwoord met de grondwaarheid op gelijkenis.
- **F1-score**: Berekent de verhouding van gedeelde woorden tussen het gegenereerde antwoord en de brongegevens.

Deze statistieken helpen u bij het evalueren van de effectiviteit van het model in het genereren van nauwkeurige, relevante en coherente antwoorden.

![Evaluate based on performance.](../../../../../../translated_images/nl/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scenario 2: Evaluatie van het Phi-3 / Phi-3.5-model in Microsoft Foundry**

### Voordat je begint

Deze tutorial is een vervolg op de eerdere blogposts, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" en "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In deze posts doorliepen we het proces van het fijn-afstellen van een Phi-3 / Phi-3.5-model in Microsoft Foundry en het integreren ervan met Prompt flow.

In deze tutorial implementeert u een Azure OpenAI-model als evaluator in Microsoft Foundry en gebruikt u dit om uw fijn-afgestelde Phi-3 / Phi-3.5-model te evalueren.

Voordat u aan deze tutorial begint, zorgt u ervoor dat u over de volgende vereisten beschikt, zoals beschreven in de eerdere tutorials:

1. Een voorbereide dataset om het fijn-afgestelde Phi-3 / Phi-3.5-model te evalueren.
1. Een Phi-3 / Phi-3.5-model dat is fijn-afgesteld en geïmplementeerd in Azure Machine Learning.
1. Een Prompt flow geïntegreerd met uw fijn-afgestelde Phi-3 / Phi-3.5-model in Microsoft Foundry.

> [!NOTE]
> U zult het *test_data.jsonl*-bestand gebruiken, dat zich bevindt in de data map van de **ULTRACHAT_200k** dataset die werd gedownload in de eerdere blogs, als dataset om het fijn-afgestelde Phi-3 / Phi-3.5-model te evalueren.

#### Integreer het aangepaste Phi-3 / Phi-3.5-model met Prompt flow in Microsoft Foundry (Code first benadering)

> [!NOTE]
> Als u de low-code benadering hebt gevolgd die wordt beschreven in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kunt u deze oefening overslaan en doorgaan met de volgende.
> Als u echter de code-first benadering hebt gevolgd zoals beschreven in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" om uw Phi-3 / Phi-3.5-model fijn af te stellen en te implementeren, is het proces om uw model te verbinden met Prompt flow iets anders. U leert dit proces in deze oefening.

Om verder te gaan, moet u uw fijn-afgestelde Phi-3 / Phi-3.5-model integreren in Prompt flow in Microsoft Foundry.

#### Maak Microsoft Foundry Hub aan

U moet eerst een Hub aanmaken voordat u een Project aanmaakt. Een Hub fungeert als een Resource Group en stelt u in staat meerdere Projecten binnen Microsoft Foundry te organiseren en beheren.
1. Meld u aan bij [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecteer **Alle hubs** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuwe hub** in het navigatiemenu.

    ![Create hub.](../../../../../../translated_images/nl/create-hub.5be78fb1e21ffbf1.webp)

1. Voer de volgende taken uit:

    - Voer **Hub-naam** in. Dit moet een unieke waarde zijn.
    - Selecteer uw Azure **Abonnement**.
    - Selecteer de **Resourcegroep** die u wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer de **Locatie** die u wilt gebruiken.
    - Selecteer de **Connect Azure AI Services** die u wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer **Connect Azure AI Search** om **Verbinding overslaan** te kiezen.

    ![Fill hub.](../../../../../../translated_images/nl/fill-hub.baaa108495c71e34.webp)

1. Selecteer **Volgende**.

#### Maak een Microsoft Foundry-project aan

1. Selecteer in de gemaakte Hub **Alle projecten** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuw project** in het navigatiemenu.

    ![Select new project.](../../../../../../translated_images/nl/select-new-project.cd31c0404088d7a3.webp)

1. Voer een **Projectnaam** in. Dit moet een unieke waarde zijn.

    ![Create project.](../../../../../../translated_images/nl/create-project.ca3b71298b90e420.webp)

1. Selecteer **Maak een project aan**.

#### Voeg een aangepaste verbinding toe voor het fijn-afgestelde Phi-3 / Phi-3.5 model

Om uw aangepaste Phi-3 / Phi-3.5 model te integreren met Prompt flow, moet u de endpoint en sleutel van het model opslaan in een aangepaste verbinding. Deze instelling zorgt ervoor dat u toegang hebt tot uw aangepaste Phi-3 / Phi-3.5 model in Prompt flow.

#### Stel api-sleutel en endpoint-URI in van het fijn-afgestelde Phi-3 / Phi-3.5 model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigeer naar de Azure Machine Learning-werkruimte die u hebt aangemaakt.

1. Selecteer **Endpoints** in het tabblad aan de linkerkant.

    ![Select endpoints.](../../../../../../translated_images/nl/select-endpoints.ee7387ecd68bd18d.webp)

1. Selecteer de endpoint die u hebt aangemaakt.

    ![Select endpoints.](../../../../../../translated_images/nl/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Selecteer **Consume** in het navigatiemenu.

1. Kopieer uw **REST-endpoint** en **Primaire sleutel**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/nl/copy-endpoint-key.0650c3786bd646ab.webp)

#### Voeg de aangepaste verbinding toe

1. Bezoek [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Microsoft Foundry-project dat u hebt aangemaakt.

1. Selecteer in het project dat u hebt aangemaakt **Instellingen** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuwe verbinding**.

    ![Select new connection.](../../../../../../translated_images/nl/select-new-connection.fa0f35743758a74b.webp)

1. Selecteer **Aangepaste sleutels** in het navigatiemenu.

    ![Select custom keys.](../../../../../../translated_images/nl/select-custom-keys.5a3c6b25580a9b67.webp)

1. Voer de volgende taken uit:

    - Selecteer **+ Voeg sleutel-waarde paren toe**.
    - Voer voor de sleutelnaam **endpoint** in en plak de endpoint die u van Azure ML Studio hebt gekopieerd in het waardeveld.
    - Selecteer opnieuw **+ Voeg sleutel-waarde paren toe**.
    - Voer voor de sleutelnaam **key** in en plak de sleutel die u van Azure ML Studio hebt gekopieerd in het waardeveld.
    - Na het toevoegen van de sleutels selecteert u **is geheim** om te voorkomen dat de sleutel wordt weergegeven.

    ![Add connection.](../../../../../../translated_images/nl/add-connection.ac7f5faf8b10b0df.webp)

1. Selecteer **Verbinding toevoegen**.

#### Maak Prompt flow aan

U hebt een aangepaste verbinding toegevoegd in Microsoft Foundry. Laten we nu een Prompt flow maken met de volgende stappen. Daarna koppelt u deze Prompt flow aan de aangepaste verbinding om het fijn-afgestelde model binnen Prompt flow te gebruiken.

1. Navigeer naar het Microsoft Foundry-project dat u hebt aangemaakt.

1. Selecteer **Prompt flow** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuwe maken** in het navigatiemenu.

    ![Select Promptflow.](../../../../../../translated_images/nl/select-promptflow.18ff2e61ab9173eb.webp)

1. Selecteer **Chat flow** in het navigatiemenu.

    ![Select chat flow.](../../../../../../translated_images/nl/select-flow-type.28375125ec9996d3.webp)

1. Voer een **Mapnaam** in die u wilt gebruiken.

    ![Select chat flow.](../../../../../../translated_images/nl/enter-name.02ddf8fb840ad430.webp)

1. Selecteer **Maken**.

#### Stel Prompt flow in om te chatten met uw aangepaste Phi-3 / Phi-3.5 model

U moet het fijn-afgestelde Phi-3 / Phi-3.5 model integreren in een Prompt flow. De bestaande Prompt flow is hiervoor echter niet ontworpen. Daarom moet u de Prompt flow opnieuw ontwerpen om de integratie van het aangepaste model mogelijk te maken.

1. Voer in de Prompt flow de volgende taken uit om de bestaande flow opnieuw op te bouwen:

    - Selecteer **Raw file mode**.
    - Verwijder alle bestaande code in het *flow.dag.yml* bestand.
    - Voeg de volgende code toe aan *flow.dag.yml*.

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

    - Selecteer **Opslaan**.

    ![Select raw file mode.](../../../../../../translated_images/nl/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Voeg de volgende code toe aan *integrate_with_promptflow.py* om het aangepaste Phi-3 / Phi-3.5 model in Prompt flow te gebruiken.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging instellingen
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

        # "connection" is de naam van de aangepaste verbinding, "endpoint", "key" zijn de sleutels in de aangepaste verbinding
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
            
            # Log de volledige JSON-respons
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

    ![Paste prompt flow code.](../../../../../../translated_images/nl/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Voor meer gedetailleerde informatie over het gebruik van Prompt flow in Microsoft Foundry kunt u terecht op [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecteer **Chat input**, **Chat output** om chatten met uw model in te schakelen.

    ![Select Input Output.](../../../../../../translated_images/nl/select-input-output.c187fc58f25fbfc3.webp)

1. Nu bent u klaar om te chatten met uw aangepaste Phi-3 / Phi-3.5 model. In de volgende oefening leert u hoe u Prompt flow start en het gebruikt om te chatten met uw fijn-afgestelde Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> De herbouwde flow zou er ongeveer zo uit moeten zien als de afbeelding hieronder:
>
> ![Flow example](../../../../../../translated_images/nl/graph-example.82fd1bcdd3fc545b.webp)
>

#### Start Prompt flow

1. Selecteer **Start compute sessions** om Prompt flow te starten.

    ![Start compute session.](../../../../../../translated_images/nl/start-compute-session.9acd8cbbd2c43df1.webp)

1. Selecteer **Validate and parse input** om parameters te vernieuwen.

    ![Validate input.](../../../../../../translated_images/nl/validate-input.c1adb9543c6495be.webp)

1. Selecteer de **Waarde** van de **verbinding** naar de aangepaste verbinding die u hebt aangemaakt. Bijvoorbeeld *connection*.

    ![Connection.](../../../../../../translated_images/nl/select-connection.1f2b59222bcaafef.webp)

#### Chat met uw aangepaste Phi-3 / Phi-3.5 model

1. Selecteer **Chatten**.

    ![Select chat.](../../../../../../translated_images/nl/select-chat.0406bd9687d0c49d.webp)

1. Hier is een voorbeeld van de resultaten: Nu kunt u chatten met uw aangepaste Phi-3 / Phi-3.5 model. Het is aan te raden vragen te stellen op basis van de gegevens die zijn gebruikt voor het fijn-afstellen.

    ![Chat with prompt flow.](../../../../../../translated_images/nl/chat-with-promptflow.1cf8cea112359ada.webp)

### Implementeer Azure OpenAI om het Phi-3 / Phi-3.5 model te evalueren

Om het Phi-3 / Phi-3.5 model in Microsoft Foundry te evalueren, moet u een Azure OpenAI model implementeren. Dit model wordt gebruikt om de prestaties van het Phi-3 / Phi-3.5 model te beoordelen.

#### Implementeer Azure OpenAI

1. Meld u aan bij [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Microsoft Foundry-project dat u hebt aangemaakt.

    ![Select Project.](../../../../../../translated_images/nl/select-project-created.5221e0e403e2c9d6.webp)

1. Selecteer in het project dat u hebt aangemaakt **Deployments** in het tabblad aan de linkerkant.

1. Selecteer **+ Model implementeren** in het navigatiemenu.

1. Selecteer **Basis model implementeren**.

    ![Select Deployments.](../../../../../../translated_images/nl/deploy-openai-model.95d812346b25834b.webp)

1. Selecteer het Azure OpenAI-model dat u wilt gebruiken. Bijvoorbeeld **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/nl/select-openai-model.959496d7e311546d.webp)

1. Selecteer **Bevestigen**.

### Evalueer het fijn-afgestelde Phi-3 / Phi-3.5 model met de Prompt flow-evaluatie van Microsoft Foundry

### Start een nieuwe evaluatie

1. Bezoek [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Microsoft Foundry-project dat u hebt aangemaakt.

    ![Select Project.](../../../../../../translated_images/nl/select-project-created.5221e0e403e2c9d6.webp)

1. Selecteer in het project dat u hebt aangemaakt **Evaluatie** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuwe evaluatie** in het navigatiemenu.

    ![Select evaluation.](../../../../../../translated_images/nl/select-evaluation.2846ad7aaaca7f4f.webp)

1. Selecteer **Prompt flow** evaluatie.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/nl/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Voer de volgende taken uit:

    - Voer de evaluatienaam in. Dit moet een unieke waarde zijn.
    - Selecteer **Vraag en antwoord zonder context** als taaktype. Omdat de dataset **UlTRACHAT_200k** die in deze tutorial wordt gebruikt geen context bevat.
    - Selecteer de prompt flow die u wilt evalueren.

    ![Prompt flow evaluation.](../../../../../../translated_images/nl/evaluation-setting1.4aa08259ff7a536e.webp)

1. Selecteer **Volgende**.

1. Voer de volgende taken uit:

    - Selecteer **Voeg uw dataset toe** om de dataset te uploaden. Bijvoorbeeld, u kunt het testdatasetbestand uploaden, zoals *test_data.json1*, dat is inbegrepen bij het downloaden van de **ULTRACHAT_200k** dataset.
    - Selecteer de juiste **Dataset-kolom** die overeenkomt met uw dataset. Bijvoorbeeld, als u de **ULTRACHAT_200k** dataset gebruikt, selecteer **${data.prompt}** als dataset-kolom.

    ![Prompt flow evaluation.](../../../../../../translated_images/nl/evaluation-setting2.07036831ba58d64e.webp)

1. Selecteer **Volgende**.

1. Voer de volgende taken uit om de prestatie- en kwaliteitsmetingen te configureren:

    - Selecteer de prestatie- en kwaliteitsmetingen die u wilt gebruiken.
    - Selecteer het Azure OpenAI-model dat u hebt aangemaakt voor evaluatie. Bijvoorbeeld, selecteer **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/nl/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Voer de volgende taken uit om de risico- en veiligheidsmetingen te configureren:

    - Selecteer de risico- en veiligheidsmetingen die u wilt gebruiken.
    - Selecteer de drempel voor het berekenen van het defectpercentage die u wilt gebruiken. Bijvoorbeeld, selecteer **Medium**.
    - Voor **vraag**, selecteer **Databron** naar **{$data.prompt}**.
    - Voor **antwoord**, selecteer **Databron** naar **{$run.outputs.answer}**.
    - Voor **waarheid**, selecteer **Databron** naar **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/nl/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Selecteer **Volgende**.

1. Selecteer **Indienen** om de evaluatie te starten.

1. De evaluatie duurt enige tijd. U kunt de voortgang volgen in het tabblad **Evaluatie**.

### Bekijk de evaluatieresultaten

> [!NOTE]
> De onderstaande resultaten dienen ter illustratie van het evaluatieproces. In deze tutorial hebben we een model gebruikt dat fijn-afgesteld is op een relatief kleine dataset, wat kan leiden tot suboptimale resultaten. Werkelijke resultaten kunnen sterk variëren afhankelijk van de grootte, kwaliteit en diversiteit van de gebruikte dataset, evenals de specifieke configuratie van het model.

Zodra de evaluatie is voltooid, kunt u de resultaten bekijken voor zowel prestatie- als veiligheidsmetingen.
1. Prestatie- en kwaliteitsmetingen:

    - evalueer de effectiviteit van het model bij het genereren van coherente, vloeiende en relevante responses.

    ![Evaluation result.](../../../../../../translated_images/nl/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Risico- en veiligheidsmetingen:

    - Zorg ervoor dat de output van het model veilig is en in overeenstemming met de Responsible AI Principles, en voorkom schadelijke of aanstootgevende inhoud.

    ![Evaluation result.](../../../../../../translated_images/nl/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Je kunt naar beneden scrollen om **Gedetailleerde metriekresultaten** te bekijken.

    ![Evaluation result.](../../../../../../translated_images/nl/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Door je aangepaste Phi-3 / Phi-3.5-model te evalueren aan de hand van zowel prestatie- als veiligheidsmetingen, kun je bevestigen dat het model niet alleen effectief is, maar ook voldoet aan verantwoordelijke AI-praktijken en klaar is voor gebruik in de praktijk.

## Gefeliciteerd!

### Je hebt deze tutorial voltooid

Je hebt het fijn-afgestelde Phi-3-model succesvol geëvalueerd dat geïntegreerd is met Prompt flow in Microsoft Foundry. Dit is een belangrijke stap om ervoor te zorgen dat je AI-modellen niet alleen goed presteren, maar ook voldoen aan de Responsible AI-principes van Microsoft, zodat je betrouwbare en vertrouwde AI-toepassingen kunt bouwen.

![Architecture.](../../../../../../translated_images/nl/architecture.10bec55250f5d6a4.webp)

## Azure-resources opruimen

Ruim je Azure-resources op om bijkomende kosten op je account te voorkomen. Ga naar de Azure-portal en verwijder de volgende resources:

- De Azure Machine Learning-resource.
- De Azure Machine Learning model endpoint.
- De Microsoft Foundry Project-resource.
- De Microsoft Foundry Prompt flow-resource.

### Volgende stappen

#### Documentatie

- [Beoordeel AI-systemen met behulp van het Responsible AI-dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluatie- en monitoringmetriek voor generatieve AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry-documentatie](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-documentatie](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Trainingsinhoud

- [Introductie tot de Responsible AI-aanpak van Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introductie tot Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referentie

- [Wat is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Aankondiging van nieuwe tools in Azure AI om je te helpen veiligere en betrouwbaardere generatieve AI-applicaties te bouwen](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluatie van generatieve AI-toepassingen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vrijwaring**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel wij streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de originele taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->