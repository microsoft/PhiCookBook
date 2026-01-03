<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:32:15+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "nl"
}
-->
# **Gebruik van Azure AI Foundry voor evaluatie**

![aistudo](../../../../../translated_images/AIFoundry.9e0b513e999a1c5a.nl.png)

Hoe je je generatieve AI-toepassing kunt evalueren met [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Of je nu enkelvoudige of meervoudige gesprekken beoordeelt, Azure AI Foundry biedt tools om de prestaties en veiligheid van modellen te evalueren.

![aistudo](../../../../../translated_images/AIPortfolio.69da59a8e1eaa70f.nl.png)

## Hoe generatieve AI-apps te evalueren met Azure AI Foundry
Voor meer gedetailleerde instructies, zie de [Azure AI Foundry Documentatie](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Hier zijn de stappen om te beginnen:

## Evalueren van Generatieve AI-modellen in Azure AI Foundry

**Vereisten**

- Een testdataset in CSV- of JSON-formaat.
- Een gedeployed generatief AI-model (zoals Phi-3, GPT 3.5, GPT 4 of Davinci-modellen).
- Een runtime met een compute instance om de evaluatie uit te voeren.

## Ingebouwde evaluatiemaatstaven

Azure AI Foundry stelt je in staat om zowel enkelvoudige als complexe, meervoudige gesprekken te evalueren.  
Voor Retrieval Augmented Generation (RAG)-scenario’s, waarbij het model is gebaseerd op specifieke data, kun je de prestaties beoordelen met ingebouwde evaluatiemaatstaven.  
Daarnaast kun je ook algemene enkelvoudige vraag-en-antwoord scenario’s (niet-RAG) evalueren.

## Een evaluatierun aanmaken

Ga in de Azure AI Foundry UI naar de Evaluate-pagina of de Prompt Flow-pagina.  
Volg de wizard voor het aanmaken van een evaluatie om een evaluatierun op te zetten. Geef desgewenst een naam aan je evaluatie.  
Selecteer het scenario dat aansluit bij de doelstellingen van je toepassing.  
Kies één of meerdere evaluatiemaatstaven om de output van het model te beoordelen.

## Aangepaste evaluatiestroom (optioneel)

Voor meer flexibiliteit kun je een aangepaste evaluatiestroom opzetten. Pas het evaluatieproces aan op basis van je specifieke wensen.

## Resultaten bekijken

Na het uitvoeren van de evaluatie kun je gedetailleerde evaluatiemaatstaven loggen, bekijken en analyseren in Azure AI Foundry. Krijg inzicht in de mogelijkheden en beperkingen van je toepassing.

**Note** Azure AI Foundry bevindt zich momenteel in publieke preview, gebruik het daarom voor experimenten en ontwikkelingsdoeleinden. Voor productieomgevingen kun je beter andere opties overwegen. Bekijk de officiële [AI Foundry documentatie](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) voor meer details en stapsgewijze instructies.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.