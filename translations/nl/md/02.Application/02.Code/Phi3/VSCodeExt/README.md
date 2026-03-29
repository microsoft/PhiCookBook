# **Bouw je eigen Visual Studio Code GitHub Copilot Chat met Microsoft Phi-3 Familie**

Heb je de workspace-agent in GitHub Copilot Chat gebruikt? Wil je je eigen code-agent voor je team bouwen? Dit hands-on lab hoopt het open source-model te combineren om een bedrijfsagent op ondernemingsniveau te bouwen.

## **Basis**

### **Waarom kiezen voor Microsoft Phi-3**

Phi-3 is een familie van modellen, waaronder phi-3-mini, phi-3-small en phi-3-medium, gebaseerd op verschillende trainingsparameters voor tekstgeneratie, dialoogafwerking en codegeneratie. Er is ook phi-3-vision gebaseerd op Vision. Het is geschikt voor ondernemingen of verschillende teams om offline generatieve AI-oplossingen te creëren.

Aanbevolen om deze link te lezen [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

De GitHub Copilot Chat-extensie geeft je een chatinterface waarmee je kunt communiceren met GitHub Copilot en direct binnen VS Code antwoorden op codeer-gerelateerde vragen kunt ontvangen, zonder dat je door documentatie hoeft te navigeren of online forums hoeft te doorzoeken.

Copilot Chat kan syntaxisaccentuering, inspringing en andere opmaakfuncties gebruiken om duidelijkheid aan het gegenereerde antwoord toe te voegen. Afhankelijk van het soort vraag van de gebruiker kan het resultaat links bevatten naar context die Copilot gebruikte om een antwoord te genereren, zoals broncodebestanden of documentatie, of knoppen voor toegang tot VS Code-functionaliteit.

- Copilot Chat integreert in je ontwikkelworkflow en biedt hulp waar je het nodig hebt:

- Begin een inline chatgesprek direct vanuit de editor of de terminal voor hulp tijdens het coderen

- Gebruik de Chat-weergave om een AI-assistent aan de zijkant te hebben die je op elk moment kan helpen

- Start Quick Chat om snel een vraag te stellen en weer verder te gaan met wat je aan het doen bent

Je kunt GitHub Copilot Chat in verschillende scenario's gebruiken, zoals:

- Beantwoorden van programmeervragen over hoe je een probleem het beste kunt oplossen

- Uitleg geven over andermans code en verbeteringen voorstellen

- Voorstellen van codefixes

- Genereren van unittests

- Genereren van code-documentatie

Aanbevolen om deze link te lezen [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Refererend aan **@workspace** in Copilot Chat kun je vragen stellen over je gehele codebase. Afhankelijk van de vraag haalt Copilot intelligent relevante bestanden en symbolen op, die het vervolgens in zijn antwoord vermeldt als links en codevoorbeelden.

Om je vraag te beantwoorden doorzoekt **@workspace** dezelfde bronnen als die een ontwikkelaar zou gebruiken bij het navigeren door een codebase in VS Code:

- Alle bestanden in de workspace, behalve bestanden die worden genegeerd door een .gitignore-bestand

- Mappenstructuur met geneste mappen en bestandsnamen

- GitHub's codezoekindex, als de workspace een GitHub-repository is en geïndexeerd door code search

- Symbolen en definities in de workspace

- Momenteel geselecteerde tekst of zichtbare tekst in de actieve editor

Opmerking: .gitignore wordt genegeerd als je een bestand open hebt of tekst hebt geselecteerd binnen een genegeerd bestand.

Aanbevolen om deze link te lezen [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Meer weten over dit Lab**

GitHub Copilot heeft de programmeerefficiëntie van bedrijven enorm verbeterd en elk bedrijf hoopt de relevante functies van GitHub Copilot aan te passen. Veel bedrijven hebben extensies op maat gemaakt die lijken op GitHub Copilot, gebaseerd op hun eigen bedrijfsomgevingen en open source modellen. Voor ondernemingen zijn aangepaste extensies makkelijker te beheren, maar dit beïnvloedt ook de gebruikerservaring. GitHub Copilot heeft immers sterkere functies bij het omgaan met algemene scenario's en professionaliteit. Als de ervaring consistent kan worden gehouden, is het beter om een aangepaste extensie van de onderneming te maken. GitHub Copilot Chat biedt relevante API's voor ondernemingen om de chatervaring uit te breiden. Een consistente ervaring behouden en aangepaste functies hebben is een betere gebruikerservaring.

Dit lab gebruikt voornamelijk het Phi-3-model gecombineerd met lokale NPU en Azure-hybride om een op maat gemaakte Agent in GitHub Copilot Chat ***@PHI3*** te bouwen, ter assistentie van bedrijfsontwikkelaars bij het voltooien van codegeneratie***(@PHI3 /gen)*** en het genereren van code op basis van afbeeldingen ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/nl/cover.1017ebc9a7c46d09.webp)

### ***Opmerking:*** 

Dit lab is momenteel geïmplementeerd in de AIPC van Intel CPU en Apple Silicon. We blijven doorgaan met het updaten van de Qualcomm-versie van de NPU.


## **Lab**


| Naam | Beschrijving | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installaties(✅) | Configureren en installeren van gerelateerde omgevingen en installatietools | [Ga](./HOL/AIPC/01.Installations.md) |[Ga](./HOL/Apple/01.Installations.md) |
| Lab1 - Promptflow uitvoeren met Phi-3-mini (✅) | Gecombineerd met AIPC / Apple Silicon, gebruikmakend van lokale NPU om codegeneratie te creëren via Phi-3-mini | [Ga](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Ga](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Phi-3-vision uitrollen op Azure Machine Learning Service(✅) | Genereer code door het uitrollen van Azure Machine Learning Service's Model Catalog - Phi-3-vision image | [Ga](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Ga](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Maak een @phi-3 agent in GitHub Copilot Chat(✅)  | Maak een aangepaste Phi-3 agent in GitHub Copilot Chat om codegeneratie, grafiekcode, RAG, etc. te voltooien | [Ga](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Ga](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Voorbeeldcode (✅)  | Download voorbeeldcode | [Ga](../../../../../../../code/07.Lab/01/AIPC) | [Ga](../../../../../../../code/07.Lab/01/Apple) |


## **Bronnen**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Leer meer over GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Leer meer over GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Leer meer over GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Leer meer over Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Leer meer over Microsoft Foundry's Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->