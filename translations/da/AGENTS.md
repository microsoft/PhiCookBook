<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:56:25+00:00",
  "source_file": "AGENTS.md",
  "language_code": "da"
}
-->
# AGENTS.md

## Projektoversigt

PhiCookBook er et omfattende opskriftsbibliotek, der indeholder praktiske eksempler, vejledninger og dokumentation til arbejde med Microsofts Phi-familie af små sprogmodeller (SLMs). Repositoriet demonstrerer forskellige anvendelser, herunder inferens, finjustering, kvantisering, RAG-implementeringer og multimodale applikationer på tværs af forskellige platforme og rammer.

**Nøgleteknologier:**
- **Sprog:** Python, C#/.NET, JavaScript/Node.js
- **Rammer:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Modeltyper:** Phi-3, Phi-3.5, Phi-4 (tekst, vision, multimodal, ræsonnement-varianter)

**Repository-struktur:**
- `/code/` - Arbejdseksempler og prøveimplementeringer
- `/md/` - Detaljeret dokumentation, vejledninger og how-to guides  
- `/translations/` - Oversættelser til flere sprog (50+ sprog via automatiseret workflow)
- `/.devcontainer/` - Dev container-konfiguration (Python 3.12 med Ollama)

## Opsætning af udviklingsmiljø

### Brug af GitHub Codespaces eller Dev Containers (anbefales)

1. Åbn i GitHub Codespaces (hurtigst):
   - Klik på "Open in GitHub Codespaces"-mærket i README
   - Containeren konfigureres automatisk med Python 3.12 og Ollama med Phi-3

2. Åbn i VS Code Dev Containers:
   - Brug "Open in Dev Containers"-mærket fra README
   - Containeren kræver minimum 16GB host-hukommelse

### Lokal opsætning

**Forudsætninger:**
- Python 3.12 eller nyere
- .NET 8.0 SDK (til C#-eksempler)
- Node.js 18+ og npm (til JavaScript-eksempler)
- Minimum anbefalet 16GB RAM

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**For Python-eksempler:**
Naviger til specifikke eksempeldirektorier og installer afhængigheder:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**For .NET-eksempler:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**For JavaScript/Web-eksempler:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Repository-organisation

### Kodeeksempler (`/code/`)

- **01.Introduce/** - Grundlæggende introduktioner og kom godt i gang-eksempler
- **03.Finetuning/** og **04.Finetuning/** - Eksempler på finjustering med forskellige metoder
- **03.Inference/** - Inferens-eksempler på forskellig hardware (AIPC, MLX)
- **06.E2E/** - End-to-end applikationseksempler
- **07.Lab/** - Laboratorie-/eksperimentelle implementeringer
- **08.RAG/** - Eksempler på Retrieval-Augmented Generation
- **09.UpdateSamples/** - Senest opdaterede eksempler

### Dokumentation (`/md/`)

- **01.Introduction/** - Introduktionsguider, miljøopsætning, platformsguider
- **02.Application/** - Applikationseksempler organiseret efter type (Tekst, Kode, Vision, Audio, osv.)
- **02.QuickStart/** - Hurtigstartsguider til Azure AI Foundry og GitHub Models
- **03.FineTuning/** - Dokumentation og vejledninger om finjustering
- **04.HOL/** - Hands-on labs (inkluderer .NET-eksempler)

### Filformater

- **Jupyter Notebooks (`.ipynb`)** - Interaktive Python-vejledninger markeret med 📓 i README
- **Python Scripts (`.py`)** - Selvstændige Python-eksempler
- **C# Projects (`.csproj`, `.sln`)** - .NET-applikationer og eksempler
- **JavaScript (`.js`, `package.json`)** - Webbaserede og Node.js-eksempler
- **Markdown (`.md`)** - Dokumentation og vejledninger

## Arbejde med eksempler

### Kørsel af Jupyter Notebooks

De fleste eksempler leveres som Jupyter-notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Kørsel af Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Kørsel af .NET-eksempler

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Eller byg hele løsningen:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Kørsel af JavaScript/Web-eksempler

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testning

Dette repository indeholder eksempelkode og vejledninger frem for et traditionelt softwareprojekt med enhedstests. Validering udføres typisk ved:

1. **Kørsel af eksempler** - Hvert eksempel skal køre uden fejl
2. **Verificering af output** - Tjek, at modelresponsen er passende
3. **Følge vejledninger** - Trin-for-trin guider skal fungere som dokumenteret

**Almindelig valideringsmetode:**
- Test eksemplets udførelse i målmiljøet
- Verificer, at afhængigheder installeres korrekt
- Tjek, at modeller downloades/indlæses succesfuldt
- Bekræft, at forventet adfærd stemmer overens med dokumentationen

## Kodestil og konventioner

### Generelle retningslinjer

- Eksempler skal være klare, velkommenterede og pædagogiske
- Følg sprog-specifikke konventioner (PEP 8 for Python, C#-standarder for .NET)
- Hold eksempler fokuseret på at demonstrere specifikke Phi-modelkapaciteter
- Inkluder kommentarer, der forklarer nøglebegreber og model-specifikke parametre

### Dokumentationsstandarder

**URL-format:**
- Brug `[text](../../url)` format uden ekstra mellemrum
- Relative links: Brug `./` for nuværende mappe, `../` for overliggende
- Ingen landespecifikke lokaliteter i URL'er (undgå `/en-us/`, `/en/`)

**Billeder:**
- Gem alle billeder i `/imgs/`-mappen
- Brug beskrivende navne med engelske tegn, tal og bindestreger
- Eksempel: `phi-3-architecture.png`

**Markdown-filer:**
- Referer til faktiske arbejdseksempler i `/code/`-mappen
- Hold dokumentationen synkroniseret med kodeændringer
- Brug 📓 emoji til at markere Jupyter-notebook-links i README

### Filorganisation

- Kodeeksempler i `/code/` organiseret efter emne/funktion
- Dokumentation i `/md/` spejler kodestrukturen, hvor det er relevant
- Hold relaterede filer (notebooks, scripts, konfigurationer) samlet i undermapper

## Retningslinjer for Pull Requests

### Før indsendelse

1. **Fork repositoryet** til din konto
2. **Adskil PR'er efter type:**
   - Fejlrettelser i én PR
   - Dokumentationsopdateringer i en anden
   - Nye eksempler i separate PR'er
   - Typografiske rettelser kan kombineres

3. **Håndter merge-konflikter:**
   - Opdater din lokale `main`-gren før ændringer
   - Synkroniser ofte med upstream

4. **Oversættelses-PR'er:**
   - Skal inkludere oversættelser for ALLE filer i mappen
   - Bevar konsistent struktur med originalt sprog

### Påkrævede checks

PR'er kører automatisk GitHub-workflows for at validere:

1. **Validering af relative stier** - Alle interne links skal fungere
   - Test links lokalt: Ctrl+Klik i VS Code
   - Brug sti-forslag fra VS Code (`./` eller `../`)

2. **URL-lokalitetscheck** - Web-URL'er må ikke indeholde landelokaliteter
   - Fjern `/en-us/`, `/en/` eller andre sprogkoder
   - Brug generiske internationale URL'er

3. **Check for brudte URL'er** - Alle URL'er skal returnere status 200
   - Verificer, at links er tilgængelige før indsendelse
   - Bemærk: Nogle fejl kan skyldes netværksbegrænsninger

### PR-titelformat

```
[component] Brief description
```

Eksempler:
- `[docs] Tilføj Phi-4 inferensvejledning`
- `[code] Ret ONNX Runtime integrations-eksempel`
- `[translation] Tilføj japansk oversættelse for introduktionsguider`

## Almindelige udviklingsmønstre

### Arbejde med Phi-modeller

**Modelindlæsning:**
- Eksempler bruger forskellige rammer: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeller downloades typisk fra Hugging Face, Azure eller GitHub Models
- Tjek modelkompatibilitet med din hardware (CPU, GPU, NPU)

**Inferensmønstre:**
- Tekstgenerering: De fleste eksempler bruger chat/instruct-varianter
- Vision: Phi-3-vision og Phi-4-multimodal til billedforståelse
- Audio: Phi-4-multimodal understøtter lydinput
- Ræsonnement: Phi-4-reasoning-varianter til avancerede ræsonnementopgaver

### Platforms-specifikke noter

**Azure AI Foundry:**
- Kræver Azure-abonnement og API-nøgler
- Se `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratis niveau tilgængeligt til test
- Se `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokal inferens:**
- ONNX Runtime: Platformuafhængig, optimeret inferens
- Ollama: Nem lokal modelstyring (forudkonfigureret i dev container)
- Apple MLX: Optimeret til Apple Silicon

## Fejlfinding

### Almindelige problemer

**Hukommelsesproblemer:**
- Phi-modeller kræver betydelig RAM (især vision/multimodal-varianter)
- Brug kvantiserede modeller til ressourcebegrænsede miljøer
- Se `/md/01.Introduction/04/QuantifyingPhi.md`

**Afhængighedskonflikter:**
- Python-eksempler kan have specifikke versionskrav
- Brug virtuelle miljøer til hvert eksempel
- Tjek individuelle `requirements.txt`-filer

**Model-downloadfejl:**
- Store modeller kan time ud på langsomme forbindelser
- Overvej at bruge cloud-miljøer (Codespaces, Azure)
- Tjek Hugging Face-cache: `~/.cache/huggingface/`

**.NET-projektproblemer:**
- Sørg for, at .NET 8.0 SDK er installeret
- Brug `dotnet restore` før bygning
- Nogle projekter har CUDA-specifikke konfigurationer (Debug_Cuda)

**JavaScript/Web-eksempler:**
- Brug Node.js 18+ for kompatibilitet
- Ryd `node_modules` og geninstaller, hvis der opstår problemer
- Tjek browserkonsollen for WebGPU-kompatibilitetsproblemer

### Få hjælp

- **Discord:** Deltag i Azure AI Foundry Community Discord
- **GitHub Issues:** Rapportér fejl og problemer i repositoryet
- **GitHub Discussions:** Stil spørgsmål og del viden

## Yderligere kontekst

### Ansvarlig AI

Al brug af Phi-modeller skal følge Microsofts principper for ansvarlig AI:
- Retfærdighed, pålidelighed, sikkerhed
- Privatliv og sikkerhed  
- Inklusion, gennemsigtighed, ansvarlighed
- Brug Azure AI Content Safety til produktionsapplikationer
- Se `/md/01.Introduction/01/01.AISafety.md`

### Oversættelser

- 50+ sprog understøttes via automatiseret GitHub Action
- Oversættelser i `/translations/`-mappen
- Vedligeholdes af co-op-translator workflow
- Rediger ikke manuelt oversatte filer (auto-genereret)

### Bidrag

- Følg retningslinjerne i `CONTRIBUTING.md`
- Accepter Contributor License Agreement (CLA)
- Overhold Microsoft Open Source Code of Conduct
- Hold sikkerhed og legitimationsoplysninger ude af commits

### Understøttelse af flere sprog

Dette er et polyglot-repository med eksempler i:
- **Python** - ML/AI-arbejdsgange, Jupyter-notebooks, finjustering
- **C#/.NET** - Enterprise-applikationer, ONNX Runtime-integration
- **JavaScript** - Webbaseret AI, browser-inferens med WebGPU

Vælg det sprog, der bedst passer til din anvendelse og implementeringsmål.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.