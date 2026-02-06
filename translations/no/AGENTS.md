# AGENTS.md

## Prosjektoversikt

PhiCookBook er et omfattende oppskriftsarkiv som inneholder praktiske eksempler, veiledninger og dokumentasjon for arbeid med Microsofts Phi-familie av små språkmodeller (SLMs). Arkivet viser ulike bruksområder, inkludert inferens, finjustering, kvantisering, RAG-implementeringer og multimodale applikasjoner på tvers av forskjellige plattformer og rammeverk.

**Nøkkelteknologier:**
- **Språk:** Python, C#/.NET, JavaScript/Node.js
- **Rammeverk:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plattformer:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltyper:** Phi-3, Phi-3.5, Phi-4 (tekst, visjon, multimodal, resonneringsvarianter)

**Arkivstruktur:**
- `/code/` - Arbeidseksempler og prøveimplementeringer
- `/md/` - Detaljert dokumentasjon, veiledninger og bruksanvisninger  
- `/translations/` - Oversettelser til flere språk (50+ språk via automatisert arbeidsflyt)
- `/.devcontainer/` - Konfigurasjon for utviklingscontainer (Python 3.12 med Ollama)

## Oppsett av utviklingsmiljø

### Bruk av GitHub Codespaces eller utviklingscontainere (anbefalt)

1. Åpne i GitHub Codespaces (raskest):
   - Klikk på "Open in GitHub Codespaces"-merket i README
   - Containeren konfigureres automatisk med Python 3.12 og Ollama med Phi-3

2. Åpne i VS Code utviklingscontainere:
   - Bruk "Open in Dev Containers"-merket fra README
   - Containeren krever minimum 16GB minne på vertsmaskinen

### Lokalt oppsett

**Forutsetninger:**
- Python 3.12 eller nyere
- .NET 8.0 SDK (for C#-eksempler)
- Node.js 18+ og npm (for JavaScript-eksempler)
- Minimum anbefalt 16GB RAM

**Installasjon:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**For Python-eksempler:**
Naviger til spesifikke eksempeldirektorier og installer avhengigheter:
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

## Arkivorganisering

### Eksempler på kode (`/code/`)

- **01.Introduce/** - Grunnleggende introduksjoner og kom-i-gang-eksempler
- **03.Finetuning/** og **04.Finetuning/** - Eksempler på finjustering med ulike metoder
- **03.Inference/** - Eksempler på inferens på forskjellig maskinvare (AIPC, MLX)
- **06.E2E/** - Helhetlige applikasjonseksempler
- **07.Lab/** - Laboratorie-/eksperimentelle implementeringer
- **08.RAG/** - Eksempler på Retrieval-Augmented Generation
- **09.UpdateSamples/** - Nyeste oppdaterte eksempler

### Dokumentasjon (`/md/`)

- **01.Introduction/** - Introduksjonsveiledninger, oppsett av miljø, plattformveiledninger
- **02.Application/** - Applikasjonseksempler organisert etter type (Tekst, Kode, Visjon, Lyd, etc.)
- **02.QuickStart/** - Kom-i-gang-veiledninger for Azure AI Foundry og GitHub Models
- **03.FineTuning/** - Dokumentasjon og veiledninger for finjustering
- **04.HOL/** - Praktiske laboratorier (inkluderer .NET-eksempler)

### Filformater

- **Jupyter Notebooks (`.ipynb`)** - Interaktive Python-veiledninger merket med 📓 i README
- **Python-skript (`.py`)** - Frittstående Python-eksempler
- **C#-prosjekter (`.csproj`, `.sln`)** - .NET-applikasjoner og eksempler
- **JavaScript (`.js`, `package.json`)** - Web-baserte og Node.js-eksempler
- **Markdown (`.md`)** - Dokumentasjon og veiledninger

## Arbeid med eksempler

### Kjøre Jupyter Notebooks

De fleste eksempler er tilgjengelige som Jupyter Notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
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
npm run dev  # Development with hot reload
```

## Testing

Dette arkivet inneholder eksempelkode og veiledninger, snarere enn et tradisjonelt programvareprosjekt med enhetstester. Validering gjøres vanligvis ved:

1. **Kjøre eksemplene** - Hvert eksempel skal kjøre uten feil
2. **Verifisere utdata** - Sjekk at modellens svar er passende
3. **Følge veiledninger** - Trinn-for-trinn-veiledninger skal fungere som dokumentert

**Vanlig valideringsmetode:**
- Test eksempelets utførelse i målmiljøet
- Verifiser at avhengigheter installeres korrekt
- Sjekk at modellene lastes ned/lastes inn vellykket
- Bekreft at forventet oppførsel samsvarer med dokumentasjonen

## Kodestil og konvensjoner

### Generelle retningslinjer

- Eksempler skal være klare, godt kommenterte og pedagogiske
- Følg språkspesifikke konvensjoner (PEP 8 for Python, C#-standarder for .NET)
- Hold eksempler fokusert på å demonstrere spesifikke Phi-modellfunksjoner
- Inkluder kommentarer som forklarer viktige konsepter og modellspesifikke parametere

### Dokumentasjonsstandarder

**URL-formattering:**
- Bruk `[tekst](../../url)`-format uten ekstra mellomrom
- Relative lenker: Bruk `./` for nåværende katalog, `../` for overordnet
- Ingen landspesifikke lokaliteter i URL-er (unngå `/en-us/`, `/en/`)

**Bilder:**
- Lagre alle bilder i `/imgs/`-katalogen
- Bruk beskrivende navn med engelske tegn, tall og bindestreker
- Eksempel: `phi-3-architecture.png`

**Markdown-filer:**
- Referer til faktiske arbeidseksempler i `/code/`-katalogen
- Hold dokumentasjonen synkronisert med kodeendringer
- Bruk 📓-emoji for å markere Jupyter Notebook-lenker i README

### Filorganisering

- Kodeeksempler i `/code/` organisert etter tema/funksjon
- Dokumentasjon i `/md/` speiler kodens struktur der det er relevant
- Hold relaterte filer (notebooks, skript, konfigurasjoner) samlet i underkataloger

## Retningslinjer for pull requests

### Før innsending

1. **Fork arkivet** til din konto
2. **Del opp PR-er etter type:**
   - Feilrettinger i én PR
   - Dokumentasjonsoppdateringer i en annen
   - Nye eksempler i separate PR-er
   - Typografiske feil kan kombineres

3. **Håndter merge-konflikter:**
   - Oppdater din lokale `main`-gren før du gjør endringer
   - Synkroniser med upstream ofte

4. **Oversettelses-PR-er:**
   - Må inkludere oversettelser for ALLE filer i mappen
   - Oppretthold konsistent struktur med originalspråket

### Nødvendige kontroller

PR-er kjører automatisk GitHub-arbeidsflyter for å validere:

1. **Validering av relative stier** - Alle interne lenker må fungere
   - Test lenker lokalt: Ctrl+Klikk i VS Code
   - Bruk sti-forslag fra VS Code (`./` eller `../`)

2. **URL-lokalitetskontroll** - Nettadresser må ikke inneholde landlokaliteter
   - Fjern `/en-us/`, `/en/` eller andre språkkoder
   - Bruk generiske internasjonale URL-er

3. **Kontroll av brutte URL-er** - Alle URL-er må returnere status 200
   - Verifiser at lenker er tilgjengelige før innsending
   - Merk: Noen feil kan skyldes nettverksrestriksjoner

### Format for PR-titler

```
[component] Brief description
```

Eksempler:
- `[docs] Legg til Phi-4 inferensveiledning`
- `[code] Fiks ONNX Runtime-integrasjonseksempel`
- `[translation] Legg til japansk oversettelse for introduksjonsveiledninger`

## Vanlige utviklingsmønstre

### Arbeid med Phi-modeller

**Modellinnlasting:**
- Eksempler bruker ulike rammeverk: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeller lastes vanligvis ned fra Hugging Face, Azure eller GitHub Models
- Sjekk modellkompatibilitet med maskinvaren din (CPU, GPU, NPU)

**Inferensmønstre:**
- Tekstgenerering: De fleste eksempler bruker chat/instruct-varianter
- Visjon: Phi-3-vision og Phi-4-multimodal for bildeforståelse
- Lyd: Phi-4-multimodal støtter lydinnspill
- Resonnering: Phi-4-reasoning-varianter for avanserte resonneringsoppgaver

### Plattformspesifikke notater

**Azure AI Foundry:**
- Krever Azure-abonnement og API-nøkler
- Se `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratisnivå tilgjengelig for testing
- Se `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokal inferens:**
- ONNX Runtime: Plattformuavhengig, optimalisert inferens
- Ollama: Enkel lokal modelladministrasjon (forhåndskonfigurert i utviklingscontainer)
- Apple MLX: Optimalisert for Apple Silicon

## Feilsøking

### Vanlige problemer

**Minneproblemer:**
- Phi-modeller krever betydelig RAM (spesielt visjon/multimodal-varianter)
- Bruk kvantiserte modeller for ressursbegrensede miljøer
- Se `/md/01.Introduction/04/QuantifyingPhi.md`

**Avhengighetskonflikter:**
- Python-eksempler kan ha spesifikke versjonskrav
- Bruk virtuelle miljøer for hvert eksempel
- Sjekk individuelle `requirements.txt`-filer

**Feil ved modellnedlasting:**
- Store modeller kan time ut på langsomme tilkoblinger
- Vurder å bruke skybaserte miljøer (Codespaces, Azure)
- Sjekk Hugging Face-cache: `~/.cache/huggingface/`

**.NET-prosjektproblemer:**
- Sørg for at .NET 8.0 SDK er installert
- Bruk `dotnet restore` før bygging
- Noen prosjekter har CUDA-spesifikke konfigurasjoner (Debug_Cuda)

**JavaScript/Web-eksempler:**
- Bruk Node.js 18+ for kompatibilitet
- Tøm `node_modules` og installer på nytt hvis problemer oppstår
- Sjekk nettleserkonsollen for WebGPU-kompatibilitetsproblemer

### Få hjelp

- **Discord:** Bli med i Azure AI Foundry Community Discord
- **GitHub Issues:** Rapporter feil og problemer i arkivet
- **GitHub Discussions:** Still spørsmål og del kunnskap

## Tilleggsinformasjon

### Ansvarlig AI

All bruk av Phi-modeller skal følge Microsofts prinsipper for ansvarlig AI:
- Rettferdighet, pålitelighet, sikkerhet
- Personvern og sikkerhet  
- Inkludering, åpenhet, ansvarlighet
- Bruk Azure AI Content Safety for produksjonsapplikasjoner
- Se `/md/01.Introduction/01/01.AISafety.md`

### Oversettelser

- Støtte for 50+ språk via automatisert GitHub Action
- Oversettelser i `/translations/`-katalogen
- Vedlikeholdt av co-op-translator arbeidsflyt
- Ikke rediger oversatte filer manuelt (automatisk generert)

### Bidrag

- Følg retningslinjene i `CONTRIBUTING.md`
- Godta Contributor License Agreement (CLA)
- Følg Microsoft Open Source Code of Conduct
- Hold sikkerhet og legitimasjon utenfor commits

### Støtte for flere språk

Dette er et flerspråklig arkiv med eksempler i:
- **Python** - ML/AI-arbeidsflyter, Jupyter Notebooks, finjustering
- **C#/.NET** - Bedriftsapplikasjoner, ONNX Runtime-integrasjon
- **JavaScript** - Web-basert AI, nettleserinferens med WebGPU

Velg språket som best passer din brukssituasjon og distribusjonsmål.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.