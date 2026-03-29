# AGENTS.md

## Projectoverzicht

PhiCookBook is een uitgebreide kookboekrepository die praktische voorbeelden, tutorials en documentatie bevat voor het werken met Microsofts Phi-familie van kleine taalmodellen (SLM's). De repository demonstreert verschillende use-cases, waaronder inferentie, fine-tuning, kwantisatie, RAG-implementaties en multimodale toepassingen op verschillende platforms en frameworks.

**Belangrijke technologieën:**
- **Talen:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforms:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modeltypen:** Phi-3, Phi-3.5, Phi-4 (tekst-, vision-, multimodaal-, reasoningvarianten)

**Repositorystructuur:**
- `/code/` - Werkende codevoorbeelden en voorbeeldimplementaties
- `/md/` - Gedetailleerde documentatie, tutorials en how-to guides  
- `/translations/` - Meertalige vertalingen (50+ talen via geautomatiseerde workflow)
- `/.devcontainer/` - Dev containerconfiguratie (Python 3.12 met Ollama)

## Ontwikkelomgeving Installatie

### Gebruik van GitHub Codespaces of Dev Containers (aanbevolen)

1. Open in GitHub Codespaces (snelste):
   - Klik op de badge "Open in GitHub Codespaces" in de README
   - Container configureert automatisch met Python 3.12 en Ollama met Phi-3

2. Open in VS Code Dev Containers:
   - Gebruik de badge "Open in Dev Containers" uit de README
   - Container vereist minimaal 16GB hostgeheugen

### Lokale Installatie

**Vereisten:**
- Python 3.12 of hoger
- .NET 8.0 SDK (voor C# voorbeelden)
- Node.js 18+ en npm (voor JavaScript voorbeelden)
- Minimaal 16GB RAM aanbevolen

**Installatie:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Voor Python Voorbeelden:**
Navigeer naar specifieke mapjes met voorbeelden en installeer dependencies:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # als requirements.txt bestaat
```

**Voor .NET Voorbeelden:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Voor JavaScript/Web Voorbeelden:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start de ontwikkelserver
npm run build  # Bouw voor productie
```

## Repository Organisatie

### Codevoorbeelden (`/code/`)

- **01.Introduce/** - Basisintroducties en opstartvoorbeelden
- **03.Finetuning/** en **04.Finetuning/** - Voorbeelden van fine-tuning met verschillende methoden
- **03.Inference/** - Inferentievoorbeelden op verschillende hardware (AIPC, MLX)
- **06.E2E/** - End-to-end toepassingsvoorbeelden
- **07.Lab/** - Laboratorium-/experimentele implementaties
- **08.RAG/** - Retrieval-Augmented Generation voorbeelden
- **09.UpdateSamples/** - Laatst geüpdatete voorbeelden

### Documentatie (`/md/`)

- **01.Introduction/** - Introductiegidsen, omgevingsinstellingen, platformgidsen
- **02.Application/** - Toepassingsvoorbeelden georganiseerd per type (Tekst, Code, Vision, Audio, etc.)
- **02.QuickStart/** - Snelle startgidsen voor Microsoft Foundry en GitHub Models
- **03.FineTuning/** - Documentatie en tutorials voor fine-tuning
- **04.HOL/** - Hands-on labs (inclusief .NET voorbeelden)

### Bestandsformaten

- **Jupyter Notebooks (`.ipynb`)** - Interactieve Python tutorials gemarkeerd met 📓 in README
- **Python Scripts (`.py`)** - Standalone Python voorbeelden
- **C# Projecten (`.csproj`, `.sln`)** - .NET applicaties en voorbeelden
- **JavaScript (`.js`, `package.json`)** - Webgebaseerde en Node.js voorbeelden
- **Markdown (`.md`)** - Documentatie en handleidingen

## Werken met Voorbeelden

### Jupyter Notebooks uitvoeren

De meeste voorbeelden zijn beschikbaar als Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opent browserinterface
# Navigeer naar het gewenste .ipynb-bestand
```

### Python Scripts uitvoeren

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET Voorbeelden uitvoeren

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Of bouw de hele oplossing:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web Voorbeelden uitvoeren

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Ontwikkeling met hot reload
```

## Testen

Deze repository bevat voorbeeldcode en tutorials in plaats van een traditioneel softwareproject met unittests. Validatie gebeurt meestal door:

1. **Voorbeelden uitvoeren** - Elk voorbeeld moet zonder fouten draaien
2. **Outputs verifiëren** - Controleren of modelantwoorden passend zijn
3. **Tutorials volgen** - Stapsgewijze gidsen moeten werken zoals beschreven

**Veelgebruikte validatieaanpak:**
- Voorbeelden testen in de doelsysteemomgeving
- Controleren of dependencies correct installeren
- Controleren of modellen succesvol downloaden/laden
- Bevestigen dat het verwachte gedrag overeenkomt met documentatie

## Code Stijl en Conventies

### Algemene Richtlijnen

- Voorbeelden moeten duidelijk, goed van commentaar voorzien en educatief zijn
- Volg taalspecifieke conventies (PEP 8 voor Python, C# standaarden voor .NET)
- Houd voorbeelden gefocust op het demonstreren van specifieke Phi modelcapaciteiten
- Voeg commentaren toe die sleutelconcepten en modelspecifieke parameters uitleggen

### Documentatiestandaarden

**URL-formatering:**
- Gebruik het formaat `[tekst](../../url)` zonder extra spaties
- Relatieve links: Gebruik `./` voor huidige map, `../` voor bovenliggende map
- Geen taalspecifieke locaties in URLs (vermijd `/en-us/`, `/en/`)

**Afbeeldingen:**
- Bewaar alle afbeeldingen in de map `/imgs/`
- Gebruik beschrijvende namen met Engelse letters, cijfers en koppeltekens
- Voorbeeld: `phi-3-architecture.png`

**Markdown-bestanden:**
- Verwijs naar werkende voorbeelden in `/code/`
- Houd documentatie synchroon met codewijzigingen
- Gebruik 📓 emoji om Jupyter notebook-links in README te markeren

### Bestandsorganisatie

- Codevoorbeelden in `/code/` georganiseerd per onderwerp/functie
- Documentatie in `/md/` weerspiegelt de codestructuur waar mogelijk
- Houd gerelateerde bestanden (notebooks, scripts, configs) samen in submappen

## Richtlijnen voor Pull Requests

### Voor indienen

1. **Fork de repository** naar je eigen account
2. **Scheid PR's op type:**
   - Bugfixes in aparte PR
   - Documentatie-updates in een andere PR
   - Nieuwe voorbeelden in aparte PR's
   - Typfouten kunnen gecombineerd

3. **Omgaan met mergeconflicten:**
   - Werk je lokale `main` branch bij vóór wijzigingen
   - Synchroniseer regelmatig met upstream

4. **Vertalingen-PR's:**
   - Moeten vertalingen bevatten voor ALLE bestanden in de map
   - Behoud consistente structuur met originele taal

### Vereiste controles

PR's draaien automatisch GitHub workflows om te valideren:

1. **Relatieve padvalidatie** - Alle interne links moeten werken
   - Test links lokaal: Ctrl+klik in VS Code
   - Gebruik padvoorstellen uit VS Code (`./` of `../`)

2. **URL locale check** - Web-URLs mogen geen land- of taalcodes bevatten
   - Verwijder `/en-us/`, `/en/` of andere taalcodes
   - Gebruik generieke internationale URLs

3. **Broken URL check** - Alle URLs moeten status 200 teruggeven
   - Controleer links op toegankelijkheid vóór indienen
   - Opmerking: sommige fouten kunnen door netwerkrestricties komen

### PR Titel Formaat

```
[component] Brief description
```

Voorbeelden:
- `[docs] Voeg Phi-4 inferentie tutorial toe`
- `[code] Fix ONNX Runtime integratie voorbeeld`
- `[translation] Voeg Japanse vertaling toe voor intro guides`

## Veelvoorkomende Ontwikkelpatronen

### Werken met Phi Modellen

**Model Laden:**
- Voorbeelden gebruiken verschillende frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Modellen worden meestal gedownload van Hugging Face, Azure of GitHub Models
- Controleer modelcompatibiliteit met je hardware (CPU, GPU, NPU)

**Inferentiepatronen:**
- Tekstgeneratie: De meeste voorbeelden gebruiken chat-/instruct-varianten
- Vision: Phi-3-vision en Phi-4-multimodal voor beeldbegrip
- Audio: Phi-4-multimodal ondersteunt audio-inputs
- Reasoning: Phi-4-reasoning varianten voor geavanceerde redeneertaken

### Platformspecifieke Notities

**Microsoft Foundry:**
- Vereist Azure-abonnement en API keys
- Zie `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratis laag beschikbaar voor testen
- Zie `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokale Inferentie:**
- ONNX Runtime: Cross-platform, geoptimaliseerde inferentie
- Ollama: Makkelijk lokaal modelbeheer (voorgeconfigureerd in dev container)
- Apple MLX: Geoptimaliseerd voor Apple Silicon

## Problemen oplossen

### Veelvoorkomende Problemen

**Geheugenproblemen:**
- Phi modellen vereisen veel RAM (vooral vision/multimodaal varianten)
- Gebruik gequantiseerde modellen in omgevingen met beperkte middelen
- Zie `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependencyconflicten:**
- Python voorbeelden kunnen specifieke versievereisten hebben
- Gebruik virtuele omgevingen per voorbeeld
- Controleer individuele `requirements.txt` bestanden

**Model Download Problemen:**
- Grote modellen kunnen timeout geven bij langzame verbindingen
- Overweeg cloudomgevingen te gebruiken (Codespaces, Azure)
- Controleer Hugging Face cache: `~/.cache/huggingface/`

**.NET Projectproblemen:**
- Zorg dat .NET 8.0 SDK geïnstalleerd is
- Gebruik `dotnet restore` vóór builden
- Sommige projecten hebben CUDA-specifieke configuraties (Debug_Cuda)

**JavaScript/Web Voorbeelden:**
- Gebruik Node.js 18+ voor compatibiliteit
- Verwijder `node_modules` en installeer opnieuw bij problemen
- Controleer browserconsole op WebGPU compatibiliteitsproblemen

### Hulp krijgen

- **Discord:** Word lid van de Microsoft Foundry Community Discord
- **GitHub Issues:** Meld bugs en problemen in de repository
- **GitHub Discussions:** Stel vragen en deel kennis

## Aanvullende Context

### Verantwoordelijke AI

Alle Phi modelgebruik moet voldoen aan Microsofts Responsible AI principes:
- Eerlijkheid, betrouwbaarheid, veiligheid
- Privacy en beveiliging  
- Inclusiviteit, transparantie, verantwoordelijkheid
- Gebruik Azure AI Content Safety voor productieapplicaties
- Zie `/md/01.Introduction/01/01.AISafety.md`

### Vertalingen

- 50+ talen ondersteund via geautomatiseerde GitHub Action
- Vertalingen in map `/translations/`
- Beheerd door co-op-translator workflow
- Vertaalde bestanden niet handmatig aanpassen (automatisch gegenereerd)

### Bijdragen

- Volg richtlijnen in `CONTRIBUTING.md`
- Stem in met Contributor License Agreement (CLA)
- Houd je aan Microsoft Open Source Gedragscode
- Houd beveiliging en inloggegevens uit commits

### Meertalige Ondersteuning

Dit is een polyglot repository met voorbeelden in:
- **Python** - ML/AI workflows, Jupyter notebooks, fine-tuning
- **C#/.NET** - Enterprise applicaties, ONNX Runtime integratie
- **JavaScript** - Webgebaseerde AI, browserinferentie met WebGPU

Kies de taal die het beste past bij je use-case en doelsysteem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, kan een automatische vertaling fouten of onnauwkeurigheden bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->