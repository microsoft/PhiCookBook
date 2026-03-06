# AGENTS.md

## Projektoversigt

PhiCookBook er et omfattende opskriftsbibliotek, der indeholder praktiske eksempler, vejledninger og dokumentation til arbejde med Microsofts Phi-familie af Små Sprogmodeller (SLMs). Repositoriet demonstrerer forskellige brugstilfælde, herunder inferens, finjustering, kvantisering, RAG-implementeringer og multimodale applikationer på tværs af forskellige platforme og frameworks.

**Nøgleteknologier:**
- **Sprog:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modeltyper:** Phi-3, Phi-3.5, Phi-4 (tekst, vision, multimodal, ræsonneringsvarianter)

**Repositoriumsstruktur:**
- `/code/` - Arbejdende kodeeksempler og prøveimplementeringer
- `/md/` - Detaljeret dokumentation, vejledninger og how-to guides  
- `/translations/` - Flersprogede oversættelser (50+ sprog via automatiseret workflow)
- `/.devcontainer/` - Dev container konfiguration (Python 3.12 med Ollama)

## Opsætning af udviklingsmiljø

### Brug af GitHub Codespaces eller Dev Containers (anbefalet)

1. Åbn i GitHub Codespaces (hurtigst):
   - Klik på "Open in GitHub Codespaces" badge i README
   - Containeren konfigureres automatisk med Python 3.12 og Ollama med Phi-3

2. Åbn i VS Code Dev Containers:
   - Brug "Open in Dev Containers" badge fra README
   - Containeren kræver mindst 16GB værts-hukommelse

### Lokal opsætning

**Forudsætninger:**
- Python 3.12 eller nyere
- .NET 8.0 SDK (til C# eksempler)
- Node.js 18+ og npm (til JavaScript eksempler)
- Minimum 16GB RAM anbefales

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Til Python Eksempler:**
Naviger til specifikke eksempelmapper og installer afhængigheder:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # hvis requirements.txt findes
```

**Til .NET Eksempler:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Til JavaScript/Web Eksempler:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start udviklingsserver
npm run build  # Byg til produktion
```

## Repository Organisation

### Kodeeksempler (`/code/`)

- **01.Introduce/** - Grundlæggende introduktioner og begyndersamples
- **03.Finetuning/** og **04.Finetuning/** - Finjusteringseksempler med forskellige metoder
- **03.Inference/** - Inferenseksempler på forskellige hardware (AIPC, MLX)
- **06.E2E/** - End-to-end applikationssamples
- **07.Lab/** - Laboratorie-/eksperimentelle implementeringer
- **08.RAG/** - Retrieval-Augmented Generation eksempler
- **09.UpdateSamples/** - Senest opdaterede samples

### Dokumentation (`/md/`)

- **01.Introduction/** - Introduktionsguider, miljøopsætning, platformsguider
- **02.Application/** - Applikationseksempler organiseret efter type (Tekst, Kode, Vision, Audio osv.)
- **02.QuickStart/** - Quick start guides til Microsoft Foundry og GitHub Models
- **03.FineTuning/** - Dokumentation og vejledninger for finjustering
- **04.HOL/** - Hands-on labs (inkluderer .NET eksempler)

### Filformater

- **Jupyter Notebooks (`.ipynb`)** - Interaktive Python tutorials markeret med 📓 i README
- **Python Scripts (`.py`)** - Selvstændige Python eksempler
- **C# Projekter (`.csproj`, `.sln`)** - .NET applikationer og samples
- **JavaScript (`.js`, `package.json`)** - Web- og Node.js eksempler
- **Markdown (`.md`)** - Dokumentation og vejledninger

## Arbejde med eksempler

### Køre Jupyter Notebooks

De fleste eksempler leveres som Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Åbner browsergrænseflade
# Naviger til ønsket .ipynb-fil
```

### Køre Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Køre .NET Eksempler

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Eller byg hele løsningen:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Køre JavaScript/Web Eksempler

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Udvikling med hot reload
```

## Testning

Dette repository indeholder kodeeksempler og vejledninger fremfor et traditionelt softwareprojekt med unittests. Validering sker typisk ved:

1. **Køre eksemplerne** - Hvert eksempel bør køre uden fejl
2. **Verificere output** - Tjek at modelrespons er passende
3. **Følge vejledninger** - Trin-for-trin guides skal virke som dokumenteret

**Typisk valideringsmetode:**
- Test af eksekvering i målmiljø
- Verificer at afhængigheder installeres korrekt
- Tjek at modeldownload/-loading fungerer
- Bekræft at forventet adfærd stemmer overens med dokumentationen

## Kodestil og konventioner

### Generelle retningslinjer

- Eksempler skal være klare, velkommenterede og undervisende
- Følg sprog-specifikke konventioner (PEP 8 for Python, C# standarder for .NET)
- Hold eksempler fokuseret på at demonstrere specifikke Phi modelfunktionaliteter
- Inkluder kommentarer, der forklarer nøglebegreber og model-specifikke parametre

### Dokumentationsstandarder

**URL-formatering:**
- Brug `[text](../../url)` syntax uden ekstra mellemrum
- Relative links: Brug `./` for aktuel mappe, `../` for overordnet mappe
- Ingen landespecifikke lokaliteter i URLs (undgå `/en-us/`, `/en/`)

**Billeder:**
- Læg alle billeder i `/imgs/` folderen
- Brug beskrivende navne med engelske tegn, tal og bindestreger
- Eksempel: `phi-3-architecture.png`

**Markdown-filer:**
- Reference til faktiske arbejdseksempler i `/code/` mappen
- Hold dokumentation synkroniseret med kodeændringer
- Brug 📓 emoji til at markere Jupyter notebook-links i README

### Filorganisation

- Kodeeksempler i `/code/` ordnet efter emne/funktion
- Dokumentation i `/md/` spejler kode-struktur hvor relevant
- Hold relaterede filer (notebooks, scripts, konfigurationer) samlet i undermapper

## Pull Request Retningslinjer

### Før indsendelse

1. **Fork repositoriet** til din egen konto
2. **Adskil PR'er efter type:**
   - Fejlrettelser i én PR
   - Dokumentationsopdateringer i en anden
   - Nye eksempler i separate PR'er
   - Tastefejl kan kombineres

3. **Håndter merge-konflikter:**
   - Opdater din lokale `main` gren før ændringer
   - Synkroniser med upstream regelmæssigt

4. **Oversættelses PR'er:**
   - Skal inkludere oversættelser for ALLE filer i mappen
   - Opdater strukturen i overensstemmelse med originalsprog

### Krævede tjek

PR'er kører automatisk GitHub workflows for at validere:

1. **Validering af relative stier** - Alle interne links skal fungere
   - Test links lokalt: Ctrl+Klik i VS Code
   - Brug forslag til sti i VS Code (`./` eller `../`)

2. **Tjek for URL-lokalitet** - Web-URLs må ikke indeholde landskoder
   - Fjern `/en-us/`, `/en/` eller andre sproglige koder
   - Brug generelle internationale URLs

3. **Tjek for ødelagte URLs** - Alle URLs skal returnere status 200
   - Verificer tilgængelighed før indsendelse
   - Bemærk: Nogle fejl kan skyldes netværksbegrænsninger

### PR titelformat

```
[component] Brief description
```

Eksempler:
- `[docs] Tilføj Phi-4 inferensvejledning`
- `[code] Ret ONNX Runtime integrations-eksempel`
- `[translation] Tilføj japansk oversættelse for introduktionsguider`

## Almindelige udviklingsmønstre

### Arbejde med Phi modeller

**Modelindlæsning:**
- Eksempler bruger flere frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeller hentes typisk fra Hugging Face, Azure eller GitHub Models
- Tjek modelkompatibilitet med dit hardware (CPU, GPU, NPU)

**Inferensmønstre:**
- Tekstgenerering: De fleste eksempler bruger chat-/instruktionsvarianter
- Vision: Phi-3-vision og Phi-4-multimodal til billedforståelse
- Audio: Phi-4-multimodal understøtter lydinput
- Ræsonnering: Phi-4-reasoning varianter til avancerede ræsonneringsopgaver

### Platformsspecifikke noter

**Microsoft Foundry:**
- Kræver Azure abonnement og API-nøgler
- Se `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratis niveau til test
- Se `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokal Inferens:**
- ONNX Runtime: Cross-platform, optimeret inferens
- Ollama: Nem lokal modelstyring (forkonfigureret i dev container)
- Apple MLX: Optimeret til Apple Silicon

## Fejlfinding

### Almindelige problemer

**Hukommelsesproblemer:**
- Phi modeller kræver betydelig RAM (især vision/multimodale varianter)
- Brug kvantiserede modeller i ressourcebegrænsede miljøer
- Se `/md/01.Introduction/04/QuantifyingPhi.md`

**Afhængighedskonflikter:**
- Python eksempler kan have specifikke versionkrav
- Brug virtuelle miljøer for hvert eksempel
- Tjek individuelle `requirements.txt` filer

**Modeldownload fejl:**
- Store modeller kan timeoute ved langsomme forbindelser
- Overvej cloud-miljøer (Codespaces, Azure)
- Tjek Hugging Face cache: `~/.cache/huggingface/`

**.NET projektproblemer:**
- Sørg for .NET 8.0 SDK er installeret
- Brug `dotnet restore` før bygning
- Nogle projekter har CUDA-specifikke konfigurationer (Debug_Cuda)

**JavaScript/Web eksempler:**
- Brug Node.js 18+ for kompatibilitet
- Ryd `node_modules` og geninstaller ved problemer
- Tjek browserkonsol for WebGPU kompatibilitetsproblemer

### Få hjælp

- **Discord:** Deltag i Microsoft Foundry Community Discord
- **GitHub Issues:** Rapportér fejl og problemer i repositoriet
- **GitHub Discussions:** Stil spørgsmål og del viden

## Yderligere kontekst

### Ansvarlig AI

Al brug af Phi modeller bør følge Microsofts principper for ansvarlig AI:
- Retfærdighed, pålidelighed, sikkerhed
- Privatliv og sikkerhed  
- Inklusion, gennemsigtighed, ansvarlighed
- Brug Azure AI Content Safety til produktionsapplikationer
- Se `/md/01.Introduction/01/01.AISafety.md`

### Oversættelser

- 50+ sprog understøttet via automatiseret GitHub Action
- Oversættelser i `/translations/` mappen
- Vedligeholdes af co-op-translator workflow
- Rediger ikke manuelt oversatte filer (automatisk genereret)

### Bidrag

- Følg retningslinjer i `CONTRIBUTING.md`
- Accepter Contributor License Agreement (CLA)
- Overhold Microsoft Open Source Code of Conduct
- Hold sikkerhed og adgangsoplysninger ude af commits

### Flersproget support

Dette er et polyglot repository med eksempler i:
- **Python** - ML/AI workflows, Jupyter notebooks, finjustering
- **C#/.NET** - Enterprise applikationer, ONNX Runtime integration
- **JavaScript** - Webbaseret AI, browserinferens med WebGPU

Vælg det sprog der passer bedst til dit brugstilfælde og deploymentsmål.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->