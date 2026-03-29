# **Microsoft Foundry gebruiken voor evaluatie**

![aistudo](../../../../../translated_images/nl/AIFoundry.9e0b513e999a1c5a.webp)

Hoe u uw generatieve AI-toepassing evalueert met [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Of u nu enkele-ronde- of meer-ronde-gesprekken beoordeelt, Microsoft Foundry biedt tools voor het evalueren van modelprestaties en veiligheid.

![aistudo](../../../../../translated_images/nl/AIPortfolio.69da59a8e1eaa70f.webp)

## Hoe generatieve AI-apps te evalueren met Microsoft Foundry
Voor meer gedetailleerde instructies zie de [Microsoft Foundry Documentatie](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Hier zijn de stappen om te beginnen:

## Generatieve AI-modellen evalueren in Microsoft Foundry

**Vereisten**

- Een testdataset in CSV- of JSON-formaat.
- Een ingezet generatief AI-model (zoals Phi-3, GPT 3.5, GPT 4, of Davinci-modellen).
- Een runtime met een compute-instance om de evaluatie uit te voeren.

## Ingebouwde evaluatiemetrieken

Microsoft Foundry stelt u in staat zowel enkele-ronde als complexe, meer-ronde-gesprekken te evalueren.
Voor Retrieval Augmented Generation (RAG) scenario's, waarbij het model is gebaseerd op specifieke data, kunt u prestaties beoordelen met ingebouwde evaluatiemetrieken.
Daarnaast kunt u algemene enkele-ronde vraag-en-antwoord scenario's (niet-RAG) evalueren.

## Een evaluatieronde aanmaken

Navigeer vanuit de Microsoft Foundry UI naar de pagina Evaluate of de pagina Prompt Flow.
Volg de wizard voor het aanmaken van een evaluatie om een evaluatieronde op te zetten. Geef optioneel een naam voor uw evaluatie op.
Selecteer het scenario dat aansluit bij de doelstellingen van uw applicatie.
Kies een of meer evaluatiemetrieken om de output van het model te beoordelen.

## Aangepaste evaluatiestroom (optioneel)

Voor meer flexibiliteit kunt u een aangepaste evaluatiestroom opzetten. Pas het evaluatieproces aan op basis van uw specifieke vereisten.

## Resultaten bekijken

Na het uitvoeren van de evaluatie kunt u de gedetailleerde evaluatiemetrieken loggen, bekijken en analyseren in Microsoft Foundry. Krijg inzicht in de mogelijkheden en beperkingen van uw toepassing.

**Opmerking** Microsoft Foundry bevindt zich momenteel in publieke preview, dus gebruik het voor experimenteren en ontwikkelingsdoeleinden. Voor productiewerkzaamheden kunt u andere opties overwegen. Verken de officiële [AI Foundry documentatie](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) voor meer details en stapsgewijze instructies.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->