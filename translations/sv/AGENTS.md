# AGENTS.md

## Projektöversikt

PhiCookBook är ett omfattande receptarkiv som innehåller praktiska exempel, handledningar och dokumentation för att arbeta med Microsofts Phi-familj av små språkmodeller (SLMs). Arkivet visar olika användningsområden, inklusive inferens, finjustering, kvantisering, RAG-implementeringar och multimodala applikationer över olika plattformar och ramverk.

**Nyckelteknologier:**
- **Språk:** Python, C#/.NET, JavaScript/Node.js
- **Ramverk:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plattformar:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltyper:** Phi-3, Phi-3.5, Phi-4 (text, vision, multimodal, resonemangsvarianter)

**Arkivstruktur:**
- `/code/` - Arbetskodexempel och provimplementeringar
- `/md/` - Detaljerad dokumentation, handledningar och guider  
- `/translations/` - Översättningar till flera språk (50+ språk via automatiserat arbetsflöde)
- `/.devcontainer/` - Konfiguration för utvecklingscontainer (Python 3.12 med Ollama)

## Inställning av utvecklingsmiljö

### Använda GitHub Codespaces eller utvecklingscontainers (rekommenderas)

1. Öppna i GitHub Codespaces (snabbast):
   - Klicka på "Open in GitHub Codespaces"-märket i README
   - Containern konfigureras automatiskt med Python 3.12 och Ollama med Phi-3

2. Öppna i VS Code Dev Containers:
   - Använd "Open in Dev Containers"-märket från README
   - Containern kräver minst 16GB RAM på värddatorn

### Lokal installation

**Förutsättningar:**
- Python 3.12 eller senare
- .NET 8.0 SDK (för C#-exempel)
- Node.js 18+ och npm (för JavaScript-exempel)
- Minst 16GB RAM rekommenderas

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**För Python-exempel:**
Navigera till specifika exempelmappar och installera beroenden:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**För .NET-exempel:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**För JavaScript/webbexempel:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Arkivorganisation

### Kodexempel (`/code/`)

- **01.Introduce/** - Grundläggande introduktioner och kom igång-exempel
- **03.Finetuning/** och **04.Finetuning/** - Exempel på finjustering med olika metoder
- **03.Inference/** - Exempel på inferens på olika hårdvara (AIPC, MLX)
- **06.E2E/** - Exempel på helhetsapplikationer
- **07.Lab/** - Laboratorie-/experimentella implementeringar
- **08.RAG/** - Exempel på Retrieval-Augmented Generation
- **09.UpdateSamples/** - Senast uppdaterade exempel

### Dokumentation (`/md/`)

- **01.Introduction/** - Introduktionsguider, miljöinställningar, plattformsanvisningar
- **02.Application/** - Applikationsexempel organiserade efter typ (Text, Code, Vision, Audio, etc.)
- **02.QuickStart/** - Snabbstartsguider för Microsoft Foundry och GitHub Models
- **03.FineTuning/** - Dokumentation och handledningar för finjustering
- **04.HOL/** - Praktiska labbar (inklusive .NET-exempel)

### Filformat

- **Jupyter Notebooks (`.ipynb`)** - Interaktiva Python-handledningar markerade med 📓 i README
- **Python-skript (`.py`)** - Fristående Python-exempel
- **C#-projekt (`.csproj`, `.sln`)** - .NET-applikationer och exempel
- **JavaScript (`.js`, `package.json`)** - Webb- och Node.js-exempel
- **Markdown (`.md`)** - Dokumentation och guider

## Arbeta med exempel

### Köra Jupyter Notebooks

De flesta exempel tillhandahålls som Jupyter-notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Köra Python-skript

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Köra .NET-exempel

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Eller bygg hela lösningen:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Köra JavaScript/webbexempel

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testning

Detta arkiv innehåller exempel på kod och handledningar snarare än ett traditionellt mjukvaruprojekt med enhetstester. Validering görs vanligtvis genom att:

1. **Köra exemplen** - Varje exempel ska köras utan fel
2. **Verifiera utdata** - Kontrollera att modellens svar är lämpliga
3. **Följa handledningar** - Steg-för-steg-guider ska fungera som dokumenterat

**Vanlig valideringsmetod:**
- Testa att köra exempel i målmiljön
- Verifiera att beroenden installeras korrekt
- Kontrollera att modeller laddas ner/laddas framgångsrikt
- Bekräfta att förväntat beteende överensstämmer med dokumentationen

## Kodstil och konventioner

### Allmänna riktlinjer

- Exempel ska vara tydliga, välkommenterade och utbildande
- Följ språksspecifika konventioner (PEP 8 för Python, C#-standarder för .NET)
- Håll exemplen fokuserade på att demonstrera specifika funktioner hos Phi-modeller
- Inkludera kommentarer som förklarar nyckelkoncept och modell-specifika parametrar

### Dokumentationsstandarder

**URL-format:**
- Använd `[text](../../url)`-format utan extra mellanslag
- Relativa länkar: Använd `./` för aktuell katalog, `../` för överordnad
- Inga landsspecifika lokaler i URL:er (undvik `/en-us/`, `/en/`)

**Bilder:**
- Lagra alla bilder i `/imgs/`-katalogen
- Använd beskrivande namn med engelska tecken, siffror och bindestreck
- Exempel: `phi-3-architecture.png`

**Markdown-filer:**
- Referera till faktiska arbets-exempel i `/code/`-katalogen
- Håll dokumentationen synkroniserad med kodändringar
- Använd 📓 emoji för att markera Jupyter-notebook-länkar i README

### Filorganisation

- Kodexempel i `/code/` organiserade efter ämne/funktion
- Dokumentation i `/md/` speglar kodstrukturen när det är tillämpligt
- Håll relaterade filer (notebooks, skript, konfigurationer) tillsammans i undermappar

## Riktlinjer för pull requests

### Innan du skickar in

1. **Forka arkivet** till ditt konto
2. **Separera PRs efter typ:**
   - Bugfixar i en PR
   - Dokumentationsuppdateringar i en annan
   - Nya exempel i separata PRs
   - Stavfel kan kombineras

3. **Hantera merge-konflikter:**
   - Uppdatera din lokala `main`-gren innan du gör ändringar
   - Synkronisera med upstream ofta

4. **Översättnings-PRs:**
   - Måste inkludera översättningar för ALLA filer i mappen
   - Behåll konsekvent struktur med originalspråket

### Obligatoriska kontroller

PRs kör automatiskt GitHub-arbetsflöden för att validera:

1. **Validering av relativa sökvägar** - Alla interna länkar måste fungera
   - Testa länkar lokalt: Ctrl+Klick i VS Code
   - Använd sökvägsförslag från VS Code (`./` eller `../`)

2. **Kontroll av URL-lokaler** - Webbadresser får inte innehålla landskoder
   - Ta bort `/en-us/`, `/en/` eller andra språkkoder
   - Använd generiska internationella URL:er

3. **Kontroll av brutna URL:er** - Alla URL:er måste returnera status 200
   - Verifiera att länkar är tillgängliga innan du skickar in
   - Obs: Vissa fel kan bero på nätverksbegränsningar

### Format för PR-titel

```
[component] Brief description
```

Exempel:
- `[docs] Lägg till Phi-4 inferenshandledning`
- `[code] Fixa ONNX Runtime-integreringsexempel`
- `[translation] Lägg till japansk översättning för introduktionsguider`

## Vanliga utvecklingsmönster

### Arbeta med Phi-modeller

**Modellinläsning:**
- Exempel använder olika ramverk: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeller laddas vanligtvis ner från Hugging Face, Azure eller GitHub Models
- Kontrollera modellens kompatibilitet med din hårdvara (CPU, GPU, NPU)

**Inferensmönster:**
- Textgenerering: De flesta exempel använder chat-/instruktionsvarianter
- Vision: Phi-3-vision och Phi-4-multimodal för bildförståelse
- Audio: Phi-4-multimodal stöder ljudinmatningar
- Resonemang: Phi-4-reasoning-varianter för avancerade resonemangsuppgifter

### Plattformsspecifika anteckningar

**Microsoft Foundry:**
- Kräver Azure-abonnemang och API-nycklar
- Se `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratisnivå tillgänglig för testning
- Se `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokal inferens:**
- ONNX Runtime: Plattformoberoende, optimerad inferens
- Ollama: Enkel lokal modellhantering (förkonfigurerad i utvecklingscontainern)
- Apple MLX: Optimerad för Apple Silicon

## Felsökning

### Vanliga problem

**Minnesproblem:**
- Phi-modeller kräver mycket RAM (särskilt vision/multimodal-varianter)
- Använd kvantiserade modeller för resursbegränsade miljöer
- Se `/md/01.Introduction/04/QuantifyingPhi.md`

**Beroendekonflikter:**
- Python-exempel kan ha specifika versionskrav
- Använd virtuella miljöer för varje exempel
- Kontrollera individuella `requirements.txt`-filer

**Problem med modellnedladdning:**
- Stora modeller kan timeouta på långsamma anslutningar
- Överväg att använda molnmiljöer (Codespaces, Azure)
- Kontrollera Hugging Face-cache: `~/.cache/huggingface/`

**.NET-projektproblem:**
- Säkerställ att .NET 8.0 SDK är installerat
- Använd `dotnet restore` innan du bygger
- Vissa projekt har CUDA-specifika konfigurationer (Debug_Cuda)

**JavaScript/webbexempel:**
- Använd Node.js 18+ för kompatibilitet
- Rensa `node_modules` och installera om vid problem
- Kontrollera webbläsarkonsolen för WebGPU-kompatibilitetsproblem

### Få hjälp

- **Discord:** Gå med i Microsoft Foundry Community Discord
- **GitHub Issues:** Rapportera buggar och problem i arkivet
- **GitHub Discussions:** Ställ frågor och dela kunskap

## Ytterligare kontext

### Ansvarsfull AI

All användning av Phi-modeller bör följa Microsofts principer för ansvarsfull AI:
- Rättvisa, tillförlitlighet, säkerhet
- Integritet och säkerhet  
- Inkludering, transparens, ansvarighet
- Använd Azure AI Content Safety för produktionsapplikationer
- Se `/md/01.Introduction/01/01.AISafety.md`

### Översättningar

- 50+ språk stöds via automatiserad GitHub Action
- Översättningar i `/translations/`-katalogen
- Underhålls av co-op-translator-arbetsflöde
- Redigera inte översatta filer manuellt (automatiskt genererade)

### Bidra

- Följ riktlinjerna i `CONTRIBUTING.md`
- Godkänn Contributor License Agreement (CLA)
- Följ Microsoft Open Source Code of Conduct
- Håll säkerhet och autentiseringsuppgifter utanför commits

### Stöd för flera språk

Detta är ett flerspråkigt arkiv med exempel i:
- **Python** - ML/AI-arbetsflöden, Jupyter-notebooks, finjustering
- **C#/.NET** - Företagsapplikationer, ONNX Runtime-integrering
- **JavaScript** - Webbaserad AI, webbläsarinferens med WebGPU

Välj det språk som bäst passar din användning och distributionsmål.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.