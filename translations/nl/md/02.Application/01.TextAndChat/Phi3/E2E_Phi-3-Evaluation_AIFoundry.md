<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:44:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "nl"
}
-->
# Evalueer het fijn-afgestelde Phi-3 / Phi-3.5 Model in Azure AI Foundry met Focus op Microsoft's Responsible AI Principles

Deze end-to-end (E2E) voorbeeld is gebaseerd op de gids "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" van de Microsoft Tech Community.

## Overzicht

### Hoe kun je de veiligheid en prestaties van een fijn-afgesteld Phi-3 / Phi-3.5 model in Azure AI Foundry evalueren?

Het fijn-afstellen van een model kan soms leiden tot onbedoelde of ongewenste reacties. Om te zorgen dat het model veilig en effectief blijft, is het belangrijk om het model te beoordelen op de mogelijkheid om schadelijke inhoud te genereren en op zijn vermogen om nauwkeurige, relevante en samenhangende antwoorden te geven. In deze tutorial leer je hoe je de veiligheid en prestaties van een fijn-afgesteld Phi-3 / Phi-3.5 model kunt evalueren dat geïntegreerd is met Prompt flow in Azure AI Foundry.

Hier is het evaluatieproces van Azure AI Foundry.

![Architectuur van de tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4.nl.png)

*Afbeeldingsbron: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Voor meer gedetailleerde informatie en om extra bronnen over Phi-3 / Phi-3.5 te verkennen, bezoek de [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Vereisten

- [Python](https://www.python.org/downloads)
- [Azure-abonnement](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fijn-afgesteld Phi-3 / Phi-3.5 model

### Inhoudsopgave

1. [**Scenario 1: Introductie tot Azure AI Foundry's Prompt flow evaluatie**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introductie tot veiligheidsevaluatie](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introductie tot prestatie-evaluatie](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Evaluatie van het Phi-3 / Phi-3.5 model in Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Voordat je begint](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure OpenAI implementeren om het Phi-3 / Phi-3.5 model te evalueren](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evalueer het fijn-afgestelde Phi-3 / Phi-3.5 model met Azure AI Foundry's Prompt flow evaluatie](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Gefeliciteerd!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introductie tot Azure AI Foundry's Prompt flow evaluatie**

### Introductie tot veiligheidsevaluatie

Om te waarborgen dat je AI-model ethisch en veilig is, is het cruciaal om het te toetsen aan Microsoft's Responsible AI Principles. In Azure AI Foundry kun je met veiligheidsevaluaties beoordelen hoe kwetsbaar je model is voor jailbreak-aanvallen en of het schadelijke inhoud kan genereren, wat direct aansluit bij deze principes.

![Veiligheidsevaluatie.](../../../../../../translated_images/safety-evaluation.083586ec88dfa950.nl.png)

*Afbeeldingsbron: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft's Responsible AI Principles

Voordat je aan de technische stappen begint, is het belangrijk om Microsoft's Responsible AI Principles te begrijpen, een ethisch kader dat is ontworpen om de verantwoorde ontwikkeling, implementatie en werking van AI-systemen te begeleiden. Deze principes sturen het verantwoord ontwerpen, ontwikkelen en inzetten van AI-systemen, zodat AI-technologieën op een eerlijke, transparante en inclusieve manier worden gebouwd. Deze principes vormen de basis voor het evalueren van de veiligheid van AI-modellen.

Microsoft's Responsible AI Principles omvatten:

- **Eerlijkheid en Inclusiviteit**: AI-systemen moeten iedereen eerlijk behandelen en voorkomen dat vergelijkbare groepen mensen op verschillende manieren worden benadeeld. Bijvoorbeeld, wanneer AI-systemen advies geven over medische behandelingen, leningaanvragen of werkgelegenheid, moeten ze dezelfde aanbevelingen doen aan iedereen met vergelijkbare symptomen, financiële omstandigheden of professionele kwalificaties.

- **Betrouwbaarheid en Veiligheid**: Om vertrouwen op te bouwen is het essentieel dat AI-systemen betrouwbaar, veilig en consistent functioneren. Deze systemen moeten werken zoals oorspronkelijk ontworpen, veilig reageren op onverwachte situaties en bestand zijn tegen schadelijke manipulatie. Hun gedrag en de variëteit aan omstandigheden die ze aankunnen, weerspiegelen de situaties en omstandigheden die ontwikkelaars tijdens ontwerp en testen hebben voorzien.

- **Transparantie**: Wanneer AI-systemen helpen bij beslissingen die grote impact hebben op het leven van mensen, is het cruciaal dat mensen begrijpen hoe die beslissingen tot stand zijn gekomen. Bijvoorbeeld, een bank kan een AI-systeem gebruiken om te bepalen of iemand kredietwaardig is. Een bedrijf kan een AI-systeem inzetten om de meest gekwalificeerde kandidaten te selecteren.

- **Privacy en Beveiliging**: Naarmate AI steeds vaker wordt toegepast, wordt het beschermen van privacy en het beveiligen van persoonlijke en zakelijke informatie steeds belangrijker en complexer. Bij AI vereisen privacy en gegevensbeveiliging extra aandacht, omdat toegang tot data essentieel is voor AI-systemen om nauwkeurige en geïnformeerde voorspellingen en beslissingen over mensen te maken.

- **Verantwoordingsplicht**: De mensen die AI-systemen ontwerpen en implementeren moeten verantwoordelijk zijn voor hoe hun systemen functioneren. Organisaties moeten gebruikmaken van industriestandaarden om normen voor verantwoordelijkheid te ontwikkelen. Deze normen zorgen ervoor dat AI-systemen niet de uiteindelijke autoriteit zijn bij beslissingen die het leven van mensen beïnvloeden. Ze zorgen er ook voor dat mensen betekenisvolle controle behouden over anderszins zeer autonome AI-systemen.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c.nl.png)

*Afbeeldingsbron: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Voor meer informatie over Microsoft's Responsible AI Principles, bezoek de [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Veiligheidsmetriek

In deze tutorial evalueer je de veiligheid van het fijn-afgestelde Phi-3 model met behulp van Azure AI Foundry's veiligheidsmetriek. Deze metriek helpt je om het potentieel van het model om schadelijke inhoud te genereren en de kwetsbaarheid voor jailbreak-aanvallen te beoordelen. De veiligheidsmetriek omvat:

- **Inhoud gerelateerd aan zelfbeschadiging**: Beoordeelt of het model de neiging heeft om inhoud te produceren die zelfbeschadiging bevordert.
- **Haatdragende en oneerlijke inhoud**: Beoordeelt of het model de neiging heeft om haatdragende of oneerlijke inhoud te produceren.
- **Gewelddadige inhoud**: Beoordeelt of het model de neiging heeft om gewelddadige inhoud te produceren.
- **Seksuele inhoud**: Beoordeelt of het model de neiging heeft om ongepaste seksuele inhoud te produceren.

Door deze aspecten te evalueren, zorg je ervoor dat het AI-model geen schadelijke of aanstootgevende inhoud genereert, wat in lijn is met maatschappelijke waarden en regelgeving.

![Evalueren op basis van veiligheid.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07.nl.png)

### Introductie tot prestatie-evaluatie

Om te waarborgen dat je AI-model presteert zoals verwacht, is het belangrijk om de prestaties te meten aan de hand van prestatie-indicatoren. In Azure AI Foundry kun je met prestatie-evaluaties beoordelen hoe effectief je model is in het genereren van nauwkeurige, relevante en samenhangende antwoorden.

![Veiligheidsevaluatie.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740.nl.png)

*Afbeeldingsbron: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prestatie-metriek

In deze tutorial evalueer je de prestaties van het fijn-afgestelde Phi-3 / Phi-3.5 model met behulp van Azure AI Foundry's prestatie-metriek. Deze metriek helpt je om de effectiviteit van het model te beoordelen in het genereren van nauwkeurige, relevante en samenhangende antwoorden. De prestatie-metriek omvat:

- **Grondslag**: Beoordeelt hoe goed de gegenereerde antwoorden overeenkomen met de informatie uit de bron.
- **Relevantie**: Beoordeelt de relevantie van de gegenereerde antwoorden ten opzichte van de gestelde vragen.
- **Samenhang**: Beoordeelt hoe vloeiend de gegenereerde tekst is, natuurlijk leest en lijkt op menselijke taal.
- **Vlotheid**: Beoordeelt de taalvaardigheid van de gegenereerde tekst.
- **GPT-overeenkomst**: Vergelijkt de gegenereerde reactie met de waarheid om de gelijkenis te meten.
- **F1-score**: Berekent de verhouding van gedeelde woorden tussen de gegenereerde reactie en de brondata.

Deze metriek helpt je om de effectiviteit van het model te beoordelen in het genereren van nauwkeurige, relevante en samenhangende antwoorden.

![Evalueren op basis van prestaties.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e8.nl.png)

## **Scenario 2: Evaluatie van het Phi-3 / Phi-3.5 model in Azure AI Foundry**

### Voordat je begint

Deze tutorial is een vervolg op de eerdere blogposts, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" en "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In deze posts hebben we het proces doorlopen van het fijn-afstellen van een Phi-3 / Phi-3.5 model in Azure AI Foundry en het integreren met Prompt flow.

In deze tutorial ga je een Azure OpenAI-model implementeren als evaluator in Azure AI Foundry en dit gebruiken om je fijn-afgestelde Phi-3 / Phi-3.5 model te evalueren.

Voordat je met deze tutorial begint, zorg dat je de volgende vereisten hebt, zoals beschreven in de eerdere tutorials:

1. Een voorbereide dataset om het fijn-afgestelde Phi-3 / Phi-3.5 model te evalueren.
1. Een Phi-3 / Phi-3.5 model dat is fijn-afgesteld en geïmplementeerd in Azure Machine Learning.
1. Een Prompt flow geïntegreerd met je fijn-afgestelde Phi-3 / Phi-3.5 model in Azure AI Foundry.

> [!NOTE]
> Je gebruikt het *test_data.jsonl* bestand, te vinden in de data map van de **ULTRACHAT_200k** dataset die in de eerdere blogposts is gedownload, als dataset om het fijn-afgestelde Phi-3 / Phi-3.5 model te evalueren.

#### Integreer het aangepaste Phi-3 / Phi-3.5 model met Prompt flow in Azure AI Foundry (Code first aanpak)
> [!NOTE]  
> Als je de low-code aanpak hebt gevolgd die wordt beschreven in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", kun je deze oefening overslaan en doorgaan naar de volgende.  
> Als je echter de code-first aanpak hebt gevolgd die wordt beschreven in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" om je Phi-3 / Phi-3.5 model te fine-tunen en te implementeren, is het proces om je model te koppelen aan Prompt Flow iets anders. Je leert dit proces in deze oefening.
Om verder te gaan, moet je je fijn-afgestelde Phi-3 / Phi-3.5 model integreren in Prompt flow binnen Azure AI Foundry.

#### Maak een Azure AI Foundry Hub aan

Je moet een Hub aanmaken voordat je een Project maakt. Een Hub werkt als een Resource Group, waarmee je meerdere projecten binnen Azure AI Foundry kunt organiseren en beheren.

1. Meld je aan bij [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecteer **All hubs** in het tabblad aan de linkerkant.

1. Selecteer **+ New hub** in het navigatiemenu.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1.nl.png)

1. Voer de volgende taken uit:

    - Voer een **Hub name** in. Dit moet een unieke waarde zijn.
    - Selecteer je Azure **Subscription**.
    - Selecteer de **Resource group** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Location** die je wilt gebruiken.
    - Selecteer de **Connect Azure AI Services** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer **Connect Azure AI Search** en kies **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e34.nl.png)

1. Selecteer **Next**.

#### Maak een Azure AI Foundry Project aan

1. Selecteer in de Hub die je hebt aangemaakt **All projects** in het tabblad aan de linkerkant.

1. Selecteer **+ New project** in het navigatiemenu.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a3.nl.png)

1. Voer een **Project name** in. Dit moet een unieke waarde zijn.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e420.nl.png)

1. Selecteer **Create a project**.

#### Voeg een aangepaste verbinding toe voor het fijn-afgestelde Phi-3 / Phi-3.5 model

Om je aangepaste Phi-3 / Phi-3.5 model te integreren met Prompt flow, moet je de endpoint en sleutel van het model opslaan in een aangepaste verbinding. Deze setup zorgt ervoor dat je toegang hebt tot je aangepaste Phi-3 / Phi-3.5 model binnen Prompt flow.

#### Stel de api key en endpoint uri in van het fijn-afgestelde Phi-3 / Phi-3.5 model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigeer naar de Azure Machine learning workspace die je hebt aangemaakt.

1. Selecteer **Endpoints** in het tabblad aan de linkerkant.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d.nl.png)

1. Selecteer de endpoint die je hebt aangemaakt.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2e.nl.png)

1. Selecteer **Consume** in het navigatiemenu.

1. Kopieer je **REST endpoint** en **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab.nl.png)

#### Voeg de Aangepaste Verbinding toe

1. Bezoek [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Azure AI Foundry project dat je hebt aangemaakt.

1. Selecteer in het project dat je hebt aangemaakt **Settings** in het tabblad aan de linkerkant.

1. Selecteer **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b.nl.png)

1. Selecteer **Custom keys** in het navigatiemenu.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67.nl.png)

1. Voer de volgende taken uit:

    - Selecteer **+ Add key value pairs**.
    - Voer voor de sleutelnaam **endpoint** in en plak de endpoint die je hebt gekopieerd uit Azure ML Studio in het waardeveld.
    - Selecteer opnieuw **+ Add key value pairs**.
    - Voer voor de sleutelnaam **key** in en plak de sleutel die je hebt gekopieerd uit Azure ML Studio in het waardeveld.
    - Nadat je de sleutels hebt toegevoegd, selecteer je **is secret** om te voorkomen dat de sleutel wordt blootgesteld.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0df.nl.png)

1. Selecteer **Add connection**.

#### Maak een Prompt flow aan

Je hebt een aangepaste verbinding toegevoegd in Azure AI Foundry. Laten we nu een Prompt flow maken met de volgende stappen. Daarna verbind je deze Prompt flow met de aangepaste verbinding om het fijn-afgestelde model binnen Prompt flow te gebruiken.

1. Navigeer naar het Azure AI Foundry project dat je hebt aangemaakt.

1. Selecteer **Prompt flow** in het tabblad aan de linkerkant.

1. Selecteer **+ Create** in het navigatiemenu.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb.nl.png)

1. Selecteer **Chat flow** in het navigatiemenu.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d3.nl.png)

1. Voer een **Folder name** in die je wilt gebruiken.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad430.nl.png)

1. Selecteer **Create**.

#### Stel Prompt flow in om te chatten met je aangepaste Phi-3 / Phi-3.5 model

Je moet het fijn-afgestelde Phi-3 / Phi-3.5 model integreren in een Prompt flow. De bestaande Prompt flow is echter niet ontworpen voor dit doel. Daarom moet je de Prompt flow herontwerpen om de integratie van het aangepaste model mogelijk te maken.

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

    - Selecteer **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f53.nl.png)

1. Voeg de volgende code toe aan *integrate_with_promptflow.py* om het aangepaste Phi-3 / Phi-3.5 model in Prompt flow te gebruiken.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec28.nl.png)

> [!NOTE]
> Voor meer gedetailleerde informatie over het gebruik van Prompt flow in Azure AI Foundry, kun je terecht bij [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecteer **Chat input**, **Chat output** om chatten met je model mogelijk te maken.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc3.nl.png)

1. Je bent nu klaar om te chatten met je aangepaste Phi-3 / Phi-3.5 model. In de volgende oefening leer je hoe je Prompt flow start en gebruikt om te chatten met je fijn-afgestelde Phi-3 / Phi-3.5 model.

> [!NOTE]
>
> De herbouwde flow zou eruit moeten zien zoals in de afbeelding hieronder:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545b.nl.png)
>

#### Start Prompt flow

1. Selecteer **Start compute sessions** om Prompt flow te starten.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df1.nl.png)

1. Selecteer **Validate and parse input** om de parameters te vernieuwen.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be.nl.png)

1. Selecteer de **Value** van de **connection** naar de aangepaste verbinding die je hebt aangemaakt. Bijvoorbeeld *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafef.nl.png)

#### Chat met je aangepaste Phi-3 / Phi-3.5 model

1. Selecteer **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d.nl.png)

1. Hier is een voorbeeld van de resultaten: nu kun je chatten met je aangepaste Phi-3 / Phi-3.5 model. Het is aan te raden om vragen te stellen op basis van de data die gebruikt is voor het fijn-afstellen.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada.nl.png)

### Zet Azure OpenAI in om het Phi-3 / Phi-3.5 model te evalueren

Om het Phi-3 / Phi-3.5 model te evalueren in Azure AI Foundry, moet je een Azure OpenAI model inzetten. Dit model wordt gebruikt om de prestaties van het Phi-3 / Phi-3.5 model te beoordelen.

#### Zet Azure OpenAI in

1. Meld je aan bij [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Azure AI Foundry project dat je hebt aangemaakt.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6.nl.png)

1. Selecteer in het project dat je hebt aangemaakt **Deployments** in het tabblad aan de linkerkant.

1. Selecteer **+ Deploy model** in het navigatiemenu.

1. Selecteer **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b.nl.png)

1. Selecteer het Azure OpenAI model dat je wilt gebruiken. Bijvoorbeeld **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d.nl.png)

1. Selecteer **Confirm**.

### Evalueer het fijn-afgestelde Phi-3 / Phi-3.5 model met behulp van de Prompt flow evaluatie van Azure AI Foundry

### Start een nieuwe evaluatie

1. Bezoek [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigeer naar het Azure AI Foundry project dat je hebt aangemaakt.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6.nl.png)

1. Selecteer in het project dat je hebt aangemaakt **Evaluation** in het tabblad aan de linkerkant.

1. Selecteer **+ New evaluation** in het navigatiemenu.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f.nl.png)

1. Selecteer **Prompt flow** evaluatie.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f.nl.png)

1. Voer de volgende taken uit:

    - Voer de naam van de evaluatie in. Dit moet een unieke waarde zijn.
    - Selecteer **Question and answer without context** als taaktype. Dit omdat de **UlTRACHAT_200k** dataset die in deze tutorial wordt gebruikt geen context bevat.
    - Selecteer de prompt flow die je wilt evalueren.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e.nl.png)

1. Selecteer **Next**.

1. Voer de volgende taken uit:

    - Selecteer **Add your dataset** om de dataset te uploaden. Bijvoorbeeld, je kunt het testdatasetbestand uploaden, zoals *test_data.json1*, dat is inbegrepen bij het downloaden van de **ULTRACHAT_200k** dataset.
    - Selecteer de juiste **Dataset column** die overeenkomt met je dataset. Bijvoorbeeld, als je de **ULTRACHAT_200k** dataset gebruikt, selecteer dan **${data.prompt}** als datasetkolom.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64e.nl.png)

1. Selecteer **Next**.

1. Voer de volgende taken uit om de prestatie- en kwaliteitsmetingen te configureren:

    - Selecteer de prestatie- en kwaliteitsmetingen die je wilt gebruiken.
    - Selecteer het Azure OpenAI model dat je hebt aangemaakt voor de evaluatie. Bijvoorbeeld, selecteer **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e.nl.png)

1. Voer de volgende taken uit om de risico- en veiligheidsmetingen te configureren:

    - Selecteer de risico- en veiligheidsmetingen die je wilt gebruiken.
    - Selecteer de drempelwaarde om het defectpercentage te berekenen die je wilt gebruiken. Bijvoorbeeld, selecteer **Medium**.
    - Voor **question**, selecteer **Data source** als **{$data.prompt}**.
    - Voor **answer**, selecteer **Data source** als **{$run.outputs.answer}**.
    - Voor **ground_truth**, selecteer **Data source** als **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2.nl.png)

1. Selecteer **Next**.

1. Selecteer **Submit** om de evaluatie te starten.

1. De evaluatie duurt enige tijd. Je kunt de voortgang volgen in het tabblad **Evaluation**.

### Bekijk de evaluatieresultaten
> [!NOTE]
> De onderstaande resultaten zijn bedoeld om het evaluatieproces te illustreren. In deze tutorial hebben we een model gebruikt dat is fijn afgesteld op een relatief kleine dataset, wat kan leiden tot minder optimale resultaten. De werkelijke resultaten kunnen sterk variëren, afhankelijk van de grootte, kwaliteit en diversiteit van de gebruikte dataset, evenals de specifieke configuratie van het model.
Zodra de evaluatie is voltooid, kunt u de resultaten bekijken voor zowel prestatie- als veiligheidsmetingen.

1. Prestatie- en kwaliteitsmetingen:

    - evalueer de effectiviteit van het model bij het genereren van samenhangende, vloeiende en relevante antwoorden.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb74254.nl.png)

1. Risico- en veiligheidsmetingen:

    - Zorg ervoor dat de output van het model veilig is en in lijn met de Responsible AI Principles, waarbij schadelijke of aanstootgevende inhoud wordt vermeden.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0.nl.png)

1. U kunt naar beneden scrollen om **Gedetailleerde meetresultaten** te bekijken.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f17.nl.png)

1. Door uw aangepaste Phi-3 / Phi-3.5-model te evalueren op zowel prestatie- als veiligheidsmetingen, kunt u bevestigen dat het model niet alleen effectief is, maar ook voldoet aan verantwoordelijke AI-praktijken, waardoor het klaar is voor gebruik in de praktijk.

## Gefeliciteerd!

### U heeft deze tutorial voltooid

U heeft met succes het fijn-afgestelde Phi-3-model geëvalueerd, geïntegreerd met Prompt flow in Azure AI Foundry. Dit is een belangrijke stap om ervoor te zorgen dat uw AI-modellen niet alleen goed presteren, maar ook voldoen aan de Responsible AI-principes van Microsoft, zodat u betrouwbare en vertrouwde AI-toepassingen kunt bouwen.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4.nl.png)

## Azure-resources opruimen

Ruim uw Azure-resources op om extra kosten op uw account te voorkomen. Ga naar het Azure-portaal en verwijder de volgende resources:

- De Azure Machine learning-resource.
- Het Azure Machine learning model endpoint.
- De Azure AI Foundry Project-resource.
- De Azure AI Foundry Prompt flow-resource.

### Volgende stappen

#### Documentatie

- [Beoordeel AI-systemen met behulp van het Responsible AI-dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluatie- en bewakingsmetingen voor generatieve AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry-documentatie](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow-documentatie](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Trainingsmateriaal

- [Introductie tot Microsofts Responsible AI-aanpak](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introductie tot Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referentie

- [Wat is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Aankondiging van nieuwe tools in Azure AI om u te helpen veiligere en betrouwbaardere generatieve AI-toepassingen te bouwen](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluatie van generatieve AI-toepassingen](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.