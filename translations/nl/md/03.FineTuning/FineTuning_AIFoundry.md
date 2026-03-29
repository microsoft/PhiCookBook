# Fijn afstemmen van Phi-3 met Microsoft Foundry

 Laten we verkennen hoe we het Phi-3 Mini-taalmodel van Microsoft kunnen fijn afstemmen met behulp van Microsoft Foundry. Fijn afstemmen stelt je in staat om Phi-3 Mini aan te passen aan specifieke taken, waardoor het nog krachtiger en contextbewuster wordt.

## Overwegingen

- **Mogelijkheden:** Welke modellen kunnen fijn afgestemd worden? Wat kan het basismodel leren doen door fijn afstemmen?
- **Kosten:** Wat is het prijsmodel voor fijn afstemmen?
- **Aanpasbaarheid:** Hoeveel kan ik het basismodel wijzigen – en op welke manieren?
- **Gemak:** Hoe vindt het fijn afstemmen werkelijk plaats – moet ik eigen code schrijven? Moet ik mijn eigen rekenkracht meenemen?
- **Veiligheid:** Fijn afgestemde modellen hebben bekende veiligheidsrisico’s – zijn er beschermingen aanwezig tegen onbedoelde schade?

![AIFoundry Models](../../../../translated_images/nl/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Voorbereiding op fijn afstemmen

### Vereisten

> [!NOTE]
> Voor Phi-3 familie modellen is het pay-as-you-go model fijn afstemmen alleen beschikbaar voor hubs aangemaakt in de **East US 2** regio's.

- Een Azure-abonnement. Als je geen Azure-abonnement hebt, maak dan een [betaald Azure-account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) aan om te beginnen.

- Een [AI Foundry project](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Toegangsbeheersystemen op basis van rollen in Azure (Azure RBAC) worden gebruikt om toegang tot operaties in Microsoft Foundry te verlenen. Om de stappen in dit artikel uit te voeren, moet je gebruikersaccount de __Azure AI Developer-rol__ toegewezen krijgen op de resourcegroep.

### Registratie van abonnementsprovider

Controleer of het abonnement is geregistreerd bij de `Microsoft.Network` resource provider.

1. Meld je aan bij de [Azure-portal](https://portal.azure.com).
1. Selecteer **Abonnementen** in het linker menu.
1. Selecteer het abonnement dat je wilt gebruiken.
1. Selecteer **AI-projectinstellingen** > **Resource providers** in het linker menu.
1. Controleer of **Microsoft.Network** in de lijst met resource providers staat. Voeg het anders toe.

### Voorbereiding van data

Bereid je trainings- en validatiegegevens voor om je model fijn af te stemmen. Je trainings- en validatiesets bestaan uit invoer- en uitvoer voorbeelden van hoe je wilt dat het model presteert.

Zorg dat al je trainingsvoorbeelden voldoen aan het verwachte format voor inferentie. Om modellen effectief te fijn af te stemmen, zorg voor een uitgebalanceerde en diverse dataset.

Dit houdt in dat je de databalans behoudt, verschillende scenario’s opneemt en periodiek de trainingsdata verfijnt om aan te sluiten bij verwachtingen uit de echte wereld, wat uiteindelijk leidt tot nauwkeurigere en meer gebalanceerde modelantwoorden.

Verschillende modeltypes vereisen een ander format voor trainingsdata.

### Chat Completion

De trainings- en validatiedata die je gebruikt **moeten** geformatteerd zijn als een JSON Lines (JSONL) document. Voor `Phi-3-mini-128k-instruct` moet de fijn afstemmingsdataset geformatteerd zijn in het gespreksformaat dat gebruikt wordt door de Chat completions API.

### Voorbeeld bestandsformaat

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Het ondersteunde bestandstype is JSON Lines. Bestanden worden geüpload naar de standaard dataopslag en beschikbaar gemaakt in je project.

## Fijn afstemmen van Phi-3 met Microsoft Foundry

Microsoft Foundry stelt je in staat om grote taalmodellen af te stemmen op je persoonlijke datasets via een proces dat bekend staat als fijn afstemmen. Fijn afstemmen biedt aanzienlijke waarde door maatwerk en optimalisatie voor specifieke taken en toepassingen mogelijk te maken. Dit leidt tot verbeterde prestaties, kostenefficiëntie, verminderde latentie en op maat gemaakte outputs.

![Finetune AI Foundry](../../../../translated_images/nl/AIFoundryfinetune.193aaddce48d553c.webp)

### Maak een nieuw project aan

1. Meld je aan bij [Microsoft Foundry](https://ai.azure.com).

1. Selecteer **+New project** om een nieuw project te maken in Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/nl/select-new-project.cd31c0404088d7a3.webp)

1. Voer de volgende taken uit:

    - Project **Hub naam**. Dit moet een unieke waarde zijn.
    - Selecteer de **Hub** die je wilt gebruiken (maak een nieuwe aan indien nodig).

    ![FineTuneSelect](../../../../translated_images/nl/create-project.ca3b71298b90e420.webp)

1. Voer de volgende taken uit om een nieuwe hub te creëren:

    - Voer een **Hub naam** in. Dit moet een unieke waarde zijn.
    - Selecteer je Azure **Abonnement**.
    - Selecteer de **Resourcegroep** die je wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer de **Locatie** die je wilt gebruiken.
    - Selecteer de **Connect Azure AI Services** die je wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer **Connect Azure AI Search** op **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/nl/create-hub.49e53d235e80779e.webp)

1. Selecteer **Next**.
1. Selecteer **Create a project**.

### Voorbereiding van data

Voor je gaat fijn afstemmen, verzamel of maak een dataset die relevant is voor je taak, zoals chatinstructies, vraag-en-antwoordparen of andere relevante tekstdata. Maak deze data schoon en preprocess ze door ruis te verwijderen, ontbrekende waarden te behandelen en de tekst te tokeniseren.

### Fijn afstemmen van Phi-3 modellen in Microsoft Foundry

> [!NOTE]
> Fijn afstemmen van Phi-3 modellen wordt momenteel ondersteund in projecten die zich bevinden in East US 2.

1. Selecteer **Model catalog** in het linker zijpaneel.

1. Typ *phi-3* in de **zoekbalk** en selecteer het phi-3 model dat je wilt gebruiken.

    ![FineTuneSelect](../../../../translated_images/nl/select-model.60ef2d4a6a3cec57.webp)

1. Selecteer **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/nl/select-finetune.a976213b543dd9d8.webp)

1. Voer de **Fine-tuned model name** in.

    ![FineTuneSelect](../../../../translated_images/nl/finetune1.c2b39463f0d34148.webp)

1. Selecteer **Next**.

1. Voer de volgende taken uit:

    - Kies voor **task type** de optie **Chat completion**.
    - Selecteer de **Training data** die je wilt gebruiken. Je kunt deze uploaden via de data van Microsoft Foundry of vanuit je lokale omgeving.

    ![FineTuneSelect](../../../../translated_images/nl/finetune2.43cb099b1a94442d.webp)

1. Selecteer **Next**.

1. Upload de **Validation data** die je wilt gebruiken, of je kunt kiezen voor **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/nl/finetune3.fd96121b67dcdd92.webp)

1. Selecteer **Next**.

1. Voer de volgende taken uit:

    - Selecteer de gewenste **Batch size multiplier**.
    - Kies de **Learning rate** die je wilt gebruiken.
    - Kies het aantal **Epochs** dat je wilt gebruiken.

    ![FineTuneSelect](../../../../translated_images/nl/finetune4.e18b80ffccb5834a.webp)

1. Selecteer **Submit** om het fijn afstemproces te starten.

    ![FineTuneSelect](../../../../translated_images/nl/select-submit.0a3802d581bac271.webp)


1. Zodra je model is fijn afgestemd, wordt de status weergegeven als **Completed**, zoals te zien in de onderstaande afbeelding. Nu kun je het model inzetten en gebruiken in je eigen applicatie, in de sandbox, of in prompt flow. Voor meer informatie, zie [Hoe Phi-3 familie van kleine taalmodellen te deployen met Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/nl/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Voor meer gedetailleerde informatie over fijn afstemmen van Phi-3, bezoek [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Opruimen van je fijn afgestemde modellen

Je kunt een fijn afgestemd model verwijderen uit de lijst van fijn afstem modellen in [Microsoft Foundry](https://ai.azure.com) of vanaf de model details pagina. Selecteer het fijn afgestemde model dat je wilt verwijderen op de pagina Fijn-afstemmen en klik daarna op de Verwijderknop om het model te verwijderen.

> [!NOTE]
> Je kunt een aangepast model niet verwijderen als er een bestaande deployment is. Je moet eerst de modeldeployment verwijderen voordat je het aangepaste model kunt verwijderen.

## Kosten en quota

### Kosten- en quotaregelingen voor Phi-3 modellen fijn afgestemd als een dienst

Phi modellen die als dienst fijn afgestemd zijn worden aangeboden door Microsoft en geïntegreerd met Microsoft Foundry voor gebruik. Je kunt de prijs vinden bij het [deployen](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) of fijn afstemmen van de modellen onder het tabblad Prijzen en voorwaarden in de deploymentwizard.

## Content filtering

Modellen die worden ingezet als dienst met pay-as-you-go worden beschermd door Azure AI Content Safety. Wanneer ingezet op realtime endpoints, kun je ervoor kiezen om deze functionaliteit uit te schakelen. Met Azure AI content safety ingeschakeld worden zowel prompt als completion doorgestuurd via een ensemble van classificatiemodellen die bedoeld zijn om het genereren van schadelijke content te detecteren en te voorkomen. Het content filtering systeem detecteert en treedt op tegen specifieke categorieën van potentieel schadelijke content in zowel input prompts als output completions. Lees meer over [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Fijn afstem configuratie**

Hyperparameters: Definieer hyperparameters zoals learning rate, batchgrootte, en aantal trainings-epochs.

**Lossfunctie**

Kies een geschikte lossfunctie voor je taak (bijv. cross-entropy).

**Optimizer**

Selecteer een optimizer (bijv. Adam) voor gradient updates tijdens training.

**Fijn afstem proces**

- Laad vooraf getraind model: laad de Phi-3 Mini checkpoint.
- Voeg aangepaste lagen toe: voeg taak-specifieke lagen toe (bijv. classificatiekop voor chatinstructies).

**Train het model**
Fijn stem het model af met je voorbereide dataset. Bewaak de trainingsvoortgang en pas hyperparameters aan indien nodig.

**Evaluatie en validatie**

Validatieset: Verdeel je data in trainings- en validatiesets.

**Evalueer prestaties**

Gebruik metrics zoals nauwkeurigheid, F1-score, of perplexity om de modelprestaties te beoordelen.

## Bewaar het fijn afgestemde model

**Checkpoint**
Bewaar de fijn afgestemde modelcheckpoint voor toekomstig gebruik.

## Inzet

- Zet in als webservice: Zet je fijn afgestemde model in als webservice in Microsoft Foundry.
- Test de endpoint: Stuur testaanvragen naar de ingezet endpoint om de functionaliteit te verifiëren.

## Itereren en verbeteren

Itereer: Als de prestaties niet bevredigend zijn, ga dan door met aanpassen van hyperparameters, toevoegen van meer data, of het fijn afstemmen gedurende meer epochs.

## Monitor en verfijn

Blijf het gedrag van het model monitoren en verfijn waar nodig.

## Personaliseer en breid uit

Aangepaste taken: Phi-3 Mini kan fijn afgestemd worden voor diverse taken buiten chatinstructies. Verken andere gebruiksmogelijkheden!
Experimenteer: Probeer verschillende architecturen, laagcombinaties en technieken om de prestaties te verbeteren.

> [!NOTE]
> Fijn afstemmen is een iteratief proces. Experimenteer, leer en pas je model aan om de beste resultaten te bereiken voor jouw specifieke taak!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de moedertaal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->