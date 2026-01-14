<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-07-16T22:42:10+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "nl"
}
-->
# **Introductie van Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) is een visuele workflow-automatiseringstool waarmee gebruikers geautomatiseerde workflows kunnen maken met behulp van vooraf gebouwde sjablonen en aangepaste connectors. Het is ontworpen om ontwikkelaars en businessanalisten in staat te stellen snel geautomatiseerde processen te bouwen voor taken zoals databeheer, samenwerking en procesoptimalisatie. Met Prompt Flow kunnen gebruikers eenvoudig verschillende diensten, applicaties en systemen koppelen en complexe bedrijfsprocessen automatiseren.

Microsoft Prompt Flow is ontworpen om de volledige ontwikkelingscyclus van AI-toepassingen aangedreven door Large Language Models (LLM’s) te stroomlijnen. Of je nu ideeën ontwikkelt, prototypes maakt, test, evalueert of LLM-gebaseerde applicaties implementeert, Prompt Flow vereenvoudigt het proces en stelt je in staat om LLM-apps van productiekwaliteit te bouwen.

## Dit zijn de belangrijkste kenmerken en voordelen van Microsoft Prompt Flow:

**Interactieve Authoring-ervaring**

Prompt Flow biedt een visuele weergave van de structuur van je flow, waardoor het gemakkelijk is om je projecten te begrijpen en te navigeren.  
Het biedt een notebook-achtige codeerervaring voor efficiënte flow-ontwikkeling en debugging.

**Promptvarianten en Afstemming**

Maak en vergelijk meerdere promptvarianten om een iteratief verfijningsproces te ondersteunen. Evalueer de prestaties van verschillende prompts en kies de meest effectieve.

**Ingebouwde Evaluatieflows**  
Beoordeel de kwaliteit en effectiviteit van je prompts en flows met ingebouwde evaluatietools.  
Krijg inzicht in hoe goed je LLM-gebaseerde applicaties presteren.

**Uitgebreide Bronnen**

Prompt Flow bevat een bibliotheek met ingebouwde tools, voorbeelden en sjablonen. Deze bronnen dienen als startpunt voor ontwikkeling, stimuleren creativiteit en versnellen het proces.

**Samenwerking en Enterprise Gereedheid**

Ondersteun teamwerk door meerdere gebruikers samen te laten werken aan prompt engineering-projecten.  
Beheer versiecontrole en deel kennis effectief. Stroomlijn het hele prompt engineering-proces, van ontwikkeling en evaluatie tot implementatie en monitoring.

## Evaluatie in Prompt Flow

In Microsoft Prompt Flow speelt evaluatie een cruciale rol bij het beoordelen van de prestaties van je AI-modellen. Laten we bekijken hoe je evaluatieflows en -metriek binnen Prompt Flow kunt aanpassen:

![PFVizualise](../../../../../translated_images/nl/pfvisualize.c1d9ca75baa2a222.png)

**Begrijpen van Evaluatie in Prompt Flow**

In Prompt Flow vertegenwoordigt een flow een reeks knooppunten die input verwerken en output genereren. Evaluatieflows zijn speciale soorten flows die zijn ontworpen om de prestaties van een run te beoordelen op basis van specifieke criteria en doelen.

**Belangrijkste kenmerken van evaluatieflows**

Ze worden meestal uitgevoerd na de flow die getest wordt, waarbij ze de output daarvan gebruiken. Ze berekenen scores of metriek om de prestaties van de geteste flow te meten. Metriek kan onder andere nauwkeurigheid, relevantiescores of andere relevante meetwaarden omvatten.

### Evaluatieflows aanpassen

**Inputs definiëren**

Evaluatieflows moeten de output van de geteste run als input ontvangen. Definieer inputs op dezelfde manier als bij standaardflows.  
Bijvoorbeeld, als je een QnA-flow evalueert, noem je een input "answer". Bij het evalueren van een classificatieflow noem je een input "category". Ook ground truth inputs (bijv. daadwerkelijke labels) kunnen nodig zijn.

**Outputs en Metriek**

Evaluatieflows leveren resultaten die de prestaties van de geteste flow meten. Metriek kan worden berekend met Python of LLM (Large Language Models). Gebruik de functie log_metric() om relevante metriek te loggen.

**Gebruik van aangepaste evaluatieflows**

Ontwikkel je eigen evaluatieflow die is afgestemd op je specifieke taken en doelen. Pas metriek aan op basis van je evaluatiedoelen.  
Pas deze aangepaste evaluatieflow toe op batchruns voor grootschalige tests.

## Ingebouwde evaluatiemethoden

Prompt Flow biedt ook ingebouwde evaluatiemethoden.  
Je kunt batchruns indienen en deze methoden gebruiken om te beoordelen hoe goed je flow presteert met grote datasets.  
Bekijk evaluatieresultaten, vergelijk metriek en verbeter waar nodig.  
Onthoud dat evaluatie essentieel is om te zorgen dat je AI-modellen voldoen aan de gewenste criteria en doelen. Raadpleeg de officiële documentatie voor gedetailleerde instructies over het ontwikkelen en gebruiken van evaluatieflows in Microsoft Prompt Flow.

Samenvattend stelt Microsoft Prompt Flow ontwikkelaars in staat om hoogwaardige LLM-applicaties te maken door prompt engineering te vereenvoudigen en een robuuste ontwikkelomgeving te bieden. Als je werkt met LLM’s, is Prompt Flow een waardevol hulpmiddel om te verkennen. Bekijk de [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) voor gedetailleerde instructies over het ontwikkelen en gebruiken van evaluatieflows in Microsoft Prompt Flow.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.