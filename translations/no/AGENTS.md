# AGENTS.md

## Prosjektoversikt

PhiCookBook er et omfattende kokebokarkiv som inneholder praktiske eksempler, opplæringsprogrammer og dokumentasjon for arbeid med Microsofts Phi-familie av Små Språkmodeller (SLMs). Arkivet demonstrerer ulike bruksområder, inkludert inferens, finjustering, kvantisering, RAG-implementeringer og multimodale applikasjoner på tvers av forskjellige plattformer og rammeverk.

**Nøkkelteknologier:**
- **Språk:** Python, C#/.NET, JavaScript/Node.js
- **Rammeverk:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plattformer:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltyper:** Phi-3, Phi-3.5, Phi-4 (tekst, visjon, multimodal, resonnement-varianter)

**Arkivstruktur:**
- `/code/` - Arbeidende kodeeksempler og prøveimplementeringer
- `/md/` - Detaljert dokumentasjon, opplæringsprogrammer og veiledninger  
- `/translations/` - Flerspråklige oversettelser (50+ språk via automatisert arbeidsflyt)
- `/.devcontainer/` - Dev container-konfigurasjon (Python 3.12 med Ollama)

## Oppsett av utviklingsmiljø

### Bruke GitHub Codespaces eller Dev Containers (anbefalt)

1. Åpne i GitHub Codespaces (raskest):
   - Klikk på "Open in GitHub Codespaces"-merket i README
   - Containeren konfigureres automatisk med Python 3.12 og Ollama med Phi-3

2. Åpne i VS Code Dev Containers:
   - Bruk "Open in Dev Containers"-merket fra README
   - Containeren krever minimum 16 GB RAM på vertsmaskinen

### Lokalt oppsett

**Forutsetninger:**
- Python 3.12 eller nyere
- .NET 8.0 SDK (for C#-eksempler)
- Node.js 18+ og npm (for JavaScript-eksempler)
- Minimum 16 GB RAM anbefales

**Installasjon:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```
  
**For Python-eksempler:**  
Naviger til spesifikke eksempelmapper og installer avhengigheter:  
```bash
cd code/<example-directory>
pip install -r requirements.txt  # hvis requirements.txt finnes
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
npm run dev  # Start utviklingsserver
npm run build  # Bygg for produksjon
```
  
## Arkivorganisering

### Kodeeksempler (`/code/`)

- **01.Introduce/** - Grunnleggende introduksjoner og oppstartseksempler
- **03.Finetuning/** og **04.Finetuning/** - Eksempler på finjustering med ulike metoder
- **03.Inference/** - Inferenseksempler på ulik maskinvare (AIPC, MLX)
- **06.E2E/** - End-to-end applikasjonseksempler
- **07.Lab/** - Laboratorie-/eksperimentelle implementeringer
- **08.RAG/** - Eksempler på Retrieval-Augmented Generation
- **09.UpdateSamples/** - Siste oppdaterte eksempler

### Dokumentasjon (`/md/`)

- **01.Introduction/** - Introduksjonsguider, miljøoppsett, plattformguider
- **02.Application/** - Applikasjonseksempler organisert etter type (Tekst, Kode, Visjon, Lyd osv.)
- **02.QuickStart/** - Hurtigstartguider for Microsoft Foundry og GitHub Models
- **03.FineTuning/** - Dokumentasjon og opplæringsprogrammer for finjustering
- **04.HOL/** - Hands-on-laboratorier (inkluderer .NET-eksempler)

### Filformater

- **Jupyter Notebooks (`.ipynb`)** - Interaktive Python-opplæringsprogrammer merket med 📓 i README
- **Python Scripts (`.py`)** - Frittstående Python-eksempler
- **C# Prosjekter (`.csproj`, `.sln`)** - .NET-applikasjoner og eksempler
- **JavaScript (`.js`, `package.json`)** - Web- og Node.js-eksempler
- **Markdown (`.md`)** - Dokumentasjon og veiledninger

## Arbeide med eksempler

### Kjøre Jupyter Notebooks

De fleste eksemplene tilbys som Jupyter notebooks:  
```bash
pip install jupyter notebook
jupyter notebook  # Åpner nettlesergrensesnitt
# Naviger til ønsket .ipynb-fil
```
  
### Kjøre Python-skript

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```
  
### Kjøre .NET-eksempler

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```
  
Eller bygg hele løsningen:  
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```
  
### Kjøre JavaScript/Web-eksempler

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Utvikling med varm omlasting
```
  
## Testing

Dette arkivet inneholder eksempel-kode og opplæringsprogrammer snarere enn et tradisjonelt programvareprosjekt med enhetstester. Validering gjøres vanligvis ved:

1. **Kjøre eksemplene** - Hvert eksempel bør kjøres uten feil
2. **Verifisere output** - Sjekk at modellresponsene er passende
3. **Følge opplæringsprogrammer** - Trinn-for-trinn-veiledninger bør fungere som dokumentert

**Vanlig valideringsprosess:**
- Test kjøring av eksempler i målmiljøet
- Verifiser at avhengigheter installeres korrekt
- Sjekk at modeller lastes ned/lastes inn vellykket
- Bekreft at forventet atferd samsvarer med dokumentasjonen

## Kode-stil og konvensjoner

### Generelle retningslinjer

- Eksemplene bør være klare, godt kommenterte og pedagogiske
- Følg språkspesifikke konvensjoner (PEP 8 for Python, C# standarder for .NET)
- Hold eksemplene fokusert på å demonstrere spesifikke Phi-modellkapabiliteter
- Inkluder kommentarer som forklarer nøkkelkonsepter og modellspesifikke parametere

### Dokumentasjonsstandarder

**URL-formatering:**
- Bruk `[tekst](../../url)` format uten ekstra mellomrom
- Relative lenker: Bruk `./` for nåværende mappe, `../` for overordnet mappe
- Ingen lands-spesifikke lokaliteter i URL-er (unngå `/en-us/`, `/en/`)

**Bilder:**
- Lagre alle bilder i `/imgs/`-katalogen
- Bruk beskrivende navn med engelske tegn, tall og bindestreker
- Eksempel: `phi-3-architecture.png`

**Markdown-filer:**
- Referer til faktiske fungerende eksempler i `/code/`-katalogen
- Hold dokumentasjonen synkronisert med kodeendringer
- Bruk 📓 emoji for å merke Jupyter notebook-lenker i README

### Filorganisering

- Kodeeksempler i `/code/` organisert etter tema/funksjonalitet
- Dokumentasjon i `/md/` speiler kode-strukturen når relevant
- Hold relaterte filer (notebooks, skript, konfigurasjoner) samlet i undermapper

## Retningslinjer for Pull Requests

### Før innsending

1. **Fork arkivet** til din konto
2. **Skill PR-er etter type:**
   - Bugfikser i en PR
   - Dokumentasjonsoppdateringer i en annen
   - Nye eksempler i separate PR-er
   - Tastefeil kan samles

3. **Håndter sammenslåingskonflikter:**
   - Oppdater din lokale `main`-gren før endringer
   - Synkroniser med upstream ofte

4. **Oversettelse PR-er:**
   - Må inkludere oversettelser for ALLE filer i mappen
   - Oppretthold konsistent struktur med originalspråket

### Obligatoriske sjekker

PR-er kjører automatisk GitHub-arbeidsflyter for validering:

1. **Validering av relative stier** - Alle interne lenker må fungere
   - Test lenker lokalt: Ctrl+Klikk i VS Code
   - Bruk sti-forslag fra VS Code (`./` eller `../`)

2. **Sjekk for URL-lokaliteter** - Web-URL-er må ikke inneholde landskoder
   - Fjern `/en-us/`, `/en/` eller andre språk-koder
   - Bruk generiske internasjonale URL-er

3. **Sjekk for brutte URL-er** - Alle URL-er må returnere status 200
   - Verifiser at lenker er tilgjengelige før innsending
   - Merk: Noen feil kan skyldes nettverksbegrensninger

### PR-tittelformat

```
[component] Brief description
```
  
Eksempler:  
- `[docs] Legg til Phi-4-inferensopplæring`  
- `[code] Fiks ONNX Runtime-integrasjonseksempel`  
- `[translation] Legg til japansk oversettelse for introduksjonsguider`

## Vanlige utviklingsmønstre

### Arbeide med Phi-modeller

**Modelllasting:**
- Eksemplene bruker ulike rammeverk: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeller lastes vanligvis ned fra Hugging Face, Azure eller GitHub Models
- Sjekk modellkompatibilitet med din maskinvare (CPU, GPU, NPU)

**Inferensmønstre:**
- Tekstgenerering: De fleste eksempler bruker chat/instruksjonsvarianter
- Visjon: Phi-3-vision og Phi-4-multimodal for bildeforståelse
- Lyd: Phi-4-multimodal støtter lydinnganger
- Resonnement: Phi-4-resonnement-varianter for avanserte resonnementoppgaver

### Plattformspesifikke notater

**Microsoft Foundry:**
- Krever Azure-abonnement og API-nøkler
- Se `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratis nivå tilgjengelig for testing
- Se `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokal inferens:**
- ONNX Runtime: Plattformuavhengig, optimalisert inferens
- Ollama: Enkel lokal modellhåndtering (forhåndskonfigurert i dev container)
- Apple MLX: Optimalisert for Apple Silicon

## Feilsøking

### Vanlige problemer

**Minneproblemer:**
- Phi-modeller krever betydelig RAM (spesielt visjon/multimodale varianter)
- Bruk kvantiserte modeller for miljøer med begrensede ressurser
- Se `/md/01.Introduction/04/QuantifyingPhi.md`

**Avhengighetskonflikter:**
- Python-eksempler kan ha spesifikke versjonskrav
- Bruk virtuelle miljøer for hvert eksempel
- Sjekk individuelle `requirements.txt`-filer

**Nedlastingsfeil for modeller:**
- Store modeller kan time out på langsomme tilkoblinger
- Vurder å bruke skybaserte miljøer (Codespaces, Azure)
- Sjekk Hugging Face-cache: `~/.cache/huggingface/`

**.NET-prosjektproblemer:**
- Sørg for at .NET 8.0 SDK er installert
- Bruk `dotnet restore` før bygging
- Noen prosjekter har CUDA-spesifikke konfigurasjoner (Debug_Cuda)

**JavaScript/Web-eksempler:**
- Bruk Node.js 18+ for kompatibilitet
- Rydd `node_modules` og installer på nytt ved problemer
- Sjekk nettleserkonsoll for WebGPU-kompatibilitetsproblemer

### Få hjelp

- **Discord:** Bli med i Microsoft Foundry Community Discord
- **GitHub Issues:** Rapporter feil og problemer i arkivet
- **GitHub Discussions:** Still spørsmål og del kunnskap

## Tilleggsinformasjon

### Ansvarlig AI

All bruk av Phi-modeller skal følge Microsofts prinsipper for Ansvarlig AI:  
- Rettferdighet, pålitelighet, sikkerhet  
- Personvern og sikkerhet  
- Inkludering, åpenhet, ansvarlighet  
- Bruk Azure AI Content Safety for produksjonsapplikasjoner  
- Se `/md/01.Introduction/01/01.AISafety.md`

### Oversettelser

- Støtter 50+ språk via automatisert GitHub Action  
- Oversettelser i `/translations/`-katalogen  
- Vedlikeholdt av co-op-translator arbeidsflyt  
- Ikke rediger oversatte filer manuelt (auto-generert)

### Bidra

- Følg retningslinjene i `CONTRIBUTING.md`  
- Aksepter Contributor License Agreement (CLA)  
- Overhold Microsofts åpen kildekode-kodeks  
- Hold sikkerhet og legitimasjon ute av commits

### Flerspråklig støtte

Dette er et polyglott-arkiv med eksempler i:  
- **Python** - ML/AI-arbeidsflyter, Jupyter notebooks, finjustering  
- **C#/.NET** - Enterprise-applikasjoner, ONNX Runtime-integrasjon  
- **JavaScript** - Web-basert AI, nettleserinferens med WebGPU

Velg språket som passer best for ditt brukstilfelle og distribusjonsmål.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi arbeider for å oppnå nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->