# AGENTS.md

## Projectoverzicht

PhiCookBook is een uitgebreide kookboekrepository met praktische voorbeelden, tutorials en documentatie voor het werken met Microsoft's Phi-familie van Small Language Models (SLMs). De repository toont verschillende gebruiksscenario's, waaronder inferentie, fine-tuning, kwantisatie, RAG-implementaties en multimodale toepassingen op verschillende platforms en frameworks.

**Belangrijke technologieën:**
- **Talen:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforms:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Modeltypes:** Phi-3, Phi-3.5, Phi-4 (tekst, visie, multimodaal, redeneer varianten)

**Repositorystructuur:**
- `/code/` - Werkende codevoorbeelden en voorbeeldimplementaties
- `/md/` - Gedetailleerde documentatie, tutorials en handleidingen  
- `/translations/` - Meertalige vertalingen (50+ talen via geautomatiseerde workflow)
- `/.devcontainer/` - Dev container configuratie (Python 3.12 met Ollama)

## Ontwikkelomgeving instellen

### Gebruik van GitHub Codespaces of Dev Containers (aanbevolen)

1. Open in GitHub Codespaces (snelste optie):
   - Klik op de "Open in GitHub Codespaces" badge in README
   - Container wordt automatisch geconfigureerd met Python 3.12 en Ollama met Phi-3

2. Open in VS Code Dev Containers:
   - Gebruik de "Open in Dev Containers" badge vanuit README
   - Container vereist minimaal 16GB hostgeheugen

### Lokale installatie

**Vereisten:**
- Python 3.12 of hoger
- .NET 8.0 SDK (voor C#-voorbeelden)
- Node.js 18+ en npm (voor JavaScript-voorbeelden)
- Minimaal aanbevolen 16GB RAM

**Installatie:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Voor Python-voorbeelden:**
Navigeer naar specifieke voorbeeldmappen en installeer afhankelijkheden:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Voor .NET-voorbeelden:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Voor JavaScript/Web-voorbeelden:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Repositoryorganisatie

### Codevoorbeelden (`/code/`)

- **01.Introduce/** - Basisintroducties en startvoorbeelden
- **03.Finetuning/** en **04.Finetuning/** - Fine-tuning voorbeelden met verschillende methoden
- **03.Inference/** - Inferentievoorbeelden op verschillende hardware (AIPC, MLX)
- **06.E2E/** - End-to-end applicatievoorbeelden
- **07.Lab/** - Laboratorium/experimentele implementaties
- **08.RAG/** - Retrieval-Augmented Generation voorbeelden
- **09.UpdateSamples/** - Meest recente bijgewerkte voorbeelden

### Documentatie (`/md/`)

- **01.Introduction/** - Introductiegidsen, omgeving instellen, platformgidsen
- **02.Application/** - Applicatievoorbeelden georganiseerd per type (Tekst, Code, Visie, Audio, etc.)
- **02.QuickStart/** - Snelle startgidsen voor Azure AI Foundry en GitHub Models
- **03.FineTuning/** - Fine-tuning documentatie en tutorials
- **04.HOL/** - Hands-on labs (inclusief .NET-voorbeelden)

### Bestandstypen

- **Jupyter Notebooks (`.ipynb`)** - Interactieve Python-tutorials gemarkeerd met 📓 in README
- **Python Scripts (`.py`)** - Zelfstandige Python-voorbeelden
- **C# Projecten (`.csproj`, `.sln`)** - .NET-applicaties en voorbeelden
- **JavaScript (`.js`, `package.json`)** - Webgebaseerde en Node.js-voorbeelden
- **Markdown (`.md`)** - Documentatie en handleidingen

## Werken met voorbeelden

### Jupyter Notebooks uitvoeren

De meeste voorbeelden worden geleverd als Jupyter-notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python-scripts uitvoeren

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET-voorbeelden uitvoeren

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Of bouw de volledige oplossing:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web-voorbeelden uitvoeren

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testen

Deze repository bevat voorbeeldcode en tutorials in plaats van een traditioneel softwareproject met unit tests. Validatie wordt meestal gedaan door:

1. **Het uitvoeren van de voorbeelden** - Elk voorbeeld moet zonder fouten worden uitgevoerd
2. **Controleren van outputs** - Controleer of modelreacties geschikt zijn
3. **Volgen van tutorials** - Stapsgewijze gidsen moeten werken zoals gedocumenteerd

**Algemene validatieaanpak:**
- Test de uitvoering van voorbeelden in de doelomgeving
- Controleer of afhankelijkheden correct worden geïnstalleerd
- Controleer of modellen correct worden gedownload/geladen
- Bevestig dat het verwachte gedrag overeenkomt met de documentatie

## Code stijl en conventies

### Algemene richtlijnen

- Voorbeelden moeten duidelijk, goed becommentarieerd en educatief zijn
- Volg taal-specifieke conventies (PEP 8 voor Python, C#-standaarden voor .NET)
- Houd voorbeelden gericht op het demonstreren van specifieke Phi-modelmogelijkheden
- Voeg opmerkingen toe die belangrijke concepten en model-specifieke parameters uitleggen

### Documentatiestandaarden

**URL-opmaak:**
- Gebruik `[tekst](../../url)` formaat zonder extra spaties
- Relatieve links: Gebruik `./` voor huidige map, `../` voor bovenliggende map
- Geen land-specifieke lokale instellingen in URL's (vermijd `/en-us/`, `/en/`)

**Afbeeldingen:**
- Sla alle afbeeldingen op in de map `/imgs/`
- Gebruik beschrijvende namen met Engelse karakters, cijfers en streepjes
- Voorbeeld: `phi-3-architecture.png`

**Markdown-bestanden:**
- Verwijs naar daadwerkelijk werkende voorbeelden in de map `/code/`
- Houd documentatie gesynchroniseerd met codewijzigingen
- Gebruik 📓 emoji om Jupyter-notebooklinks in README te markeren

### Bestandsorganisatie

- Codevoorbeelden in `/code/` georganiseerd per onderwerp/functionaliteit
- Documentatie in `/md/` weerspiegelt de structuur van de code waar mogelijk
- Houd gerelateerde bestanden (notebooks, scripts, configuraties) bij elkaar in submappen

## Richtlijnen voor pull requests

### Voordat je indient

1. **Fork de repository** naar je account
2. **Scheiding van PR's per type:**
   - Bugfixes in één PR
   - Documentatie-updates in een andere
   - Nieuwe voorbeelden in aparte PR's
   - Typfouten kunnen gecombineerd worden

3. **Omgaan met mergeconflicten:**
   - Werk je lokale `main` branch bij voordat je wijzigingen aanbrengt
   - Synchroniseer regelmatig met upstream

4. **Vertaal-PR's:**
   - Moeten vertalingen bevatten voor ALLE bestanden in de map
   - Houd consistente structuur met de originele taal

### Vereiste controles

PR's voeren automatisch GitHub-workflows uit om te valideren:

1. **Relatieve padvalidatie** - Alle interne links moeten werken
   - Test links lokaal: Ctrl+Klik in VS Code
   - Gebruik padvoorstellen van VS Code (`./` of `../`)

2. **URL-locale controle** - Web-URL's mogen geen landcodes bevatten
   - Verwijder `/en-us/`, `/en/` of andere taalcodes
   - Gebruik generieke internationale URL's

3. **Controle op gebroken URL's** - Alle URL's moeten een 200-status retourneren
   - Controleer of links toegankelijk zijn voordat je indient
   - Opmerking: Sommige fouten kunnen te wijten zijn aan netwerkbeperkingen

### PR-titel formaat

```
[component] Brief description
```

Voorbeelden:
- `[docs] Voeg Phi-4 inferentie tutorial toe`
- `[code] Fix ONNX Runtime integratie voorbeeld`
- `[translation] Voeg Japanse vertaling toe voor introductiegidsen`

## Veelvoorkomende ontwikkelpatronen

### Werken met Phi-modellen

**Model laden:**
- Voorbeelden gebruiken verschillende frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Modellen worden meestal gedownload van Hugging Face, Azure of GitHub Models
- Controleer modelcompatibiliteit met je hardware (CPU, GPU, NPU)

**Inferentiepatronen:**
- Tekstgeneratie: De meeste voorbeelden gebruiken chat/instruct varianten
- Visie: Phi-3-vision en Phi-4-multimodal voor beeldbegrip
- Audio: Phi-4-multimodal ondersteunt audio-invoer
- Redeneren: Phi-4-reasoning varianten voor geavanceerde redeneertaken

### Platformspecifieke opmerkingen

**Azure AI Foundry:**
- Vereist Azure-abonnement en API-sleutels
- Zie `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratis tier beschikbaar voor testen
- Zie `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokale inferentie:**
- ONNX Runtime: Cross-platform, geoptimaliseerde inferentie
- Ollama: Eenvoudig lokaal modelbeheer (voorgeconfigureerd in dev container)
- Apple MLX: Geoptimaliseerd voor Apple Silicon

## Problemen oplossen

### Veelvoorkomende problemen

**Geheugenproblemen:**
- Phi-modellen vereisen veel RAM (vooral visie/multimodale varianten)
- Gebruik gequantiseerde modellen voor omgevingen met beperkte middelen
- Zie `/md/01.Introduction/04/QuantifyingPhi.md`

**Afhankelijkheidsconflicten:**
- Python-voorbeelden kunnen specifieke versievereisten hebben
- Gebruik virtuele omgevingen voor elk voorbeeld
- Controleer individuele `requirements.txt` bestanden

**Model downloadfouten:**
- Grote modellen kunnen time-out geven bij trage verbindingen
- Overweeg het gebruik van cloudomgevingen (Codespaces, Azure)
- Controleer Hugging Face cache: `~/.cache/huggingface/`

**.NET projectproblemen:**
- Zorg ervoor dat .NET 8.0 SDK is geïnstalleerd
- Gebruik `dotnet restore` voordat je bouwt
- Sommige projecten hebben CUDA-specifieke configuraties (Debug_Cuda)

**JavaScript/Web voorbeelden:**
- Gebruik Node.js 18+ voor compatibiliteit
- Wis `node_modules` en installeer opnieuw als er problemen zijn
- Controleer browserconsole voor WebGPU-compatibiliteitsproblemen

### Hulp krijgen

- **Discord:** Word lid van de Azure AI Foundry Community Discord
- **GitHub Issues:** Meld bugs en problemen in de repository
- **GitHub Discussions:** Stel vragen en deel kennis

## Aanvullende context

### Verantwoordelijke AI

Alle gebruik van Phi-modellen moet voldoen aan Microsoft's principes voor Verantwoordelijke AI:
- Eerlijkheid, betrouwbaarheid, veiligheid
- Privacy en beveiliging  
- Inclusiviteit, transparantie, verantwoordelijkheid
- Gebruik Azure AI Content Safety voor productieapplicaties
- Zie `/md/01.Introduction/01/01.AISafety.md`

### Vertalingen

- Ondersteuning voor 50+ talen via geautomatiseerde GitHub Action
- Vertalingen in de map `/translations/`
- Onderhouden door co-op-translator workflow
- Bewerk vertaalde bestanden niet handmatig (automatisch gegenereerd)

### Bijdragen

- Volg richtlijnen in `CONTRIBUTING.md`
- Ga akkoord met Contributor License Agreement (CLA)
- Houd je aan de Microsoft Open Source Code of Conduct
- Houd beveiliging en inloggegevens buiten commits

### Meertalige ondersteuning

Dit is een polyglot repository met voorbeelden in:
- **Python** - ML/AI workflows, Jupyter-notebooks, fine-tuning
- **C#/.NET** - Enterprise applicaties, ONNX Runtime integratie
- **JavaScript** - Webgebaseerde AI, browserinferentie met WebGPU

Kies de taal die het beste past bij jouw gebruiksscenario en implementatiedoel.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.