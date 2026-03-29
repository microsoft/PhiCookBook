# AGENTS.md

## Projektöversikt

PhiCookBook är ett omfattande kokboksförråd som innehåller praktiska exempel, handledningar och dokumentation för att arbeta med Microsofts Phi-familj av små språkmodeller (SLM). Förrådet demonstrerar olika användningsfall, inklusive inferens, finjustering, kvantisering, RAG-implementationer och multimodala applikationer över olika plattformar och ramverk.

**Nyckelteknologier:**
- **Språk:** Python, C#/.NET, JavaScript/Node.js
- **Ramverk:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plattformar:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltyper:** Phi-3, Phi-3.5, Phi-4 (text, vision, multimodala, resonemangsvarianter)

**Förrådsstruktur:**
- `/code/` - Arbetskodexempel och provimplementationer
- `/md/` - Detaljerad dokumentation, handledningar och instruktionsguider  
- `/translations/` - Flerspråkiga översättningar (50+ språk via automatiserat arbetsflöde)
- `/.devcontainer/` - Konfiguration för utvecklingscontainer (Python 3.12 med Ollama)

## Uppställning av utvecklingsmiljö

### Använda GitHub Codespaces eller Dev Containers (Rekommenderat)

1. Öppna i GitHub Codespaces (snabbast):
   - Klicka på "Open in GitHub Codespaces"-märket i README
   - Containern konfigureras automatiskt med Python 3.12 och Ollama med Phi-3

2. Öppna i VS Code Dev Containers:
   - Använd "Open in Dev Containers"-märket från README
   - Containern kräver minst 16 GB värdminne

### Lokalt uppställning

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
Navigera till specifika exempelkataloger och installera beroenden:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # om requirements.txt finns
```

**För .NET-exempel:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**För JavaScript/Webb-exempel:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Starta utvecklingsserver
npm run build  # Bygg för produktion
```

## Förrådsorganisation

### Kodexempel (`/code/`)

- **01.Introduce/** - Grundläggande introduktioner och startexempel
- **03.Finetuning/** och **04.Finetuning/** - Exempel på finjustering med olika metoder
- **03.Inference/** - Inferensexempel på olika hårdvaror (AIPC, MLX)
- **06.E2E/** - End-to-end applikationsexempel
- **07.Lab/** - Laboratorie-/experimentella implementationer
- **08.RAG/** - Retrieval-Augmented Generation-exempel
- **09.UpdateSamples/** - Senaste uppdaterade exempel

### Dokumentation (`/md/`)

- **01.Introduction/** - Introduktionsguider, miljöuppställning, plattformsanvisningar
- **02.Application/** - Applikationsexempel organiserade per typ (Text, Kod, Syn, Ljud etc.)
- **02.QuickStart/** - Snabbstartsguider för Microsoft Foundry och GitHub Models
- **03.FineTuning/** - Dokumentation och handledningar för finjustering
- **04.HOL/** - Praktiska labb (inklusive .NET-exempel)

### Filformat

- **Jupyter Notebooks (`.ipynb`)** - Interaktiva Python-handledningar markerade med 📓 i README
- **Python-skript (`.py`)** - Självständiga Python-exempel
- **C#-projekt (`.csproj`, `.sln`)** - .NET-applikationer och exempel
- **JavaScript (`.js`, `package.json`)** - Webb- och Node.js-exempel
- **Markdown (`.md`)** - Dokumentation och guider

## Arbeta med exempel

### Köra Jupyter Notebooks

De flesta exempel tillhandahålls som Jupyter-notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Öppnar webbläsargränssnitt
# Navigera till önskad .ipynb-fil
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

### Köra JavaScript/Webb-exempel

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Utveckling med varm omladdning
```

## Testning

Detta förråd innehåller exempel på kod och handledningar snarare än ett traditionellt mjukvaruprojekt med enhetstester. Validering sker vanligtvis genom:

1. **Köra exemplen** - Varje exempel ska köras utan fel
2. **Verifiera utdata** - Kontrollera att modellens svar är lämpliga
3. **Följa handledningar** - Steg-för-steg-guider ska fungera enligt dokumentation

**Vanligt valideringssätt:**
- Testa exekvering i målmiljön
- Verifiera att beroenden installeras korrekt
- Kontrollera att modeller laddas och hämtas framgångsrikt
- Bekräfta att förväntat beteende stämmer med dokumentationen

## Kodstil och konventioner

### Allmänna riktlinjer

- Exempel ska vara tydliga, välkommenterade och pedagogiska
- Följ språkspecifika konventioner (PEP 8 för Python, C#-standarder för .NET)
- Håll exemplen fokuserade på att demonstrera specifika Phi-modellfunktioner
- Inkludera kommentarer som förklarar nyckelkoncept och modell-specifika parametrar

### Dokumentationsstandarder

**URL-formattering:**
- Använd formatet `[text](../../url)` utan extra mellanslag
- Relativa länkar: Använd `./` för nuvarande katalog, `../` för överordnad
- Inga landspecifika lokaler i URL:er (undvik `/en-us/`, `/en/`)

**Bilder:**
- Spara alla bilder i `/imgs/`-katalogen
- Använd beskrivande namn med engelska tecken, siffror och bindestreck
- Exempel: `phi-3-architecture.png`

**Markdown-filer:**
- Referera till faktiska fungerande exempel i `/code/`-katalogen
- Håll dokumentationen synkroniserad med kodändringar
- Använd 📓 emoji för att markera Jupyter-notebooklänkar i README

### Filorganisation

- Kodexempel i `/code/` organiserade efter ämne/funktion
- Dokumentation i `/md/` speglar kodstrukturen när det är tillämpligt
- Håll relaterade filer (notebooks, skript, konfigurationer) tillsammans i undermappar

## Riktlinjer för Pull Requests

### Innan inskickning

1. **Fork:a förrådet** till ditt konto
2. **Separera PR:er efter typ:**
   - Buggfixar i en PR
   - Dokumentationsuppdateringar i en annan
   - Nya exempel i separata PR:er
   - Stavningskorrigeringar kan kombineras

3. **Hantera sammanslagningskonflikter:**
   - Uppdatera din lokala `main`-gren innan ändringar görs
   - Synkronisera ofta med upstream

4. **Översättnings-PR:er:**
   - Måste inkludera översättningar för ALLA filer i mappen
   - Behåll konsekvent struktur med originalspråket

### Obligatoriska kontroller

PR:er kör automatiskt GitHub-arbetsflöden för att validera:

1. **Validering av relativa stigar** - Alla interna länkar måste fungera
   - Testa länkar lokalt: Ctrl+Klick i VS Code
   - Använd vägförslag från VS Code (`./` eller `../`)

2. **Kontroll av URL-lokal** - Webbadresser får inte innehålla landslokaler
   - Ta bort `/en-us/`, `/en/` eller andra språkkoder
   - Använd generiska internationella URL:er

3. **Kontroll av brutna URL:er** - Alla URL:er måste ge status 200
   - Verifiera att länkar är tillgängliga innan inskick
   - Observera: Vissa fel kan bero på nätverksrestriktioner

### PR-titelformat

```
[component] Brief description
```

Exempel:
- `[docs] Lägg till Phi-4 inferenshandledning`
- `[code] Åtgärda ONNX Runtime integrations-exempel`
- `[translation] Lägg till japansk översättning för introduktionsguider`

## Vanliga utvecklingsmönster

### Arbeta med Phi-modeller

**Modellinladdning:**
- Exempel använder olika ramverk: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeller hämtas oftast från Hugging Face, Azure eller GitHub Models
- Kontrollera modellkompatibilitet med din hårdvara (CPU, GPU, NPU)

**Inferensmönster:**
- Textgenerering: De flesta exempel använder chat-/instruktionsvarianter
- Vision: Phi-3-vision och Phi-4-multimodal för bildförståelse
- Ljud: Phi-4-multimodal stödjer ljudinmatningar
- Resonemang: Phi-4-resonemangsvarianter för avancerade resonemangsuppgifter

### Plattformspecifika noteringar

**Microsoft Foundry:**
- Kräver Azure-prenumeration och API-nycklar
- Se `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Gratis nivå tillgänglig för testning
- Se `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokal inferens:**
- ONNX Runtime: Plattformoberoende, optimerad inferens
- Ollama: Enkel lokal modellhantering (förkonfigurerad i utvecklingscontainer)
- Apple MLX: Optimerad för Apple Silicon

## Felsökning

### Vanliga problem

**Minnesproblem:**
- Phi-modeller kräver betydande RAM (speciellt vision/multimodala varianter)
- Använd kvantiserade modeller för resurssvaga miljöer
- Se `/md/01.Introduction/04/QuantifyingPhi.md`

**Beroendekonflikter:**
- Python-exempel kan ha specifika versionskrav
- Använd virtuella miljöer för varje exempel
- Kontrollera individuella `requirements.txt`-filer

**Misslyckade modellnedladdningar:**
- Stora modeller kan tidsavbrytas vid långsamma anslutningar
- Överväg att använda molnmiljöer (Codespaces, Azure)
- Kontrollera Hugging Face-cache: `~/.cache/huggingface/`

**Problem med .NET-projekt:**
- Säkerställ att .NET 8.0 SDK är installerat
- Använd `dotnet restore` innan byggning
- Vissa projekt har CUDA-specifika konfigurationer (Debug_Cuda)

**JavaScript/Webb-exempel:**
- Använd Node.js 18+ för kompatibilitet
- Rensa `node_modules` och installera om vid problem
- Kontrollera webbläsarkonsolen för WebGPU-kompatibilitetsproblem

### Få hjälp

- **Discord:** Gå med i Microsoft Foundry Community Discord
- **GitHub Issues:** Rapportera buggar och problem i förrådet
- **GitHub Discussions:** Ställ frågor och dela kunskap

## Ytterligare sammanhang

### Ansvarsfull AI

All användning av Phi-modeller bör följa Microsofts principer för ansvarsfull AI:
- Rättvisa, tillförlitlighet, säkerhet
- Integritet och säkerhet  
- Inkludering, transparens, ansvarsskyldighet
- Använd Azure AI Content Safety för produktionsapplikationer
- Se `/md/01.Introduction/01/01.AISafety.md`

### Översättningar

- 50+ språk stöds via automatiserad GitHub Action
- Översättningar finns i `/translations/`-katalogen
- Underhålls av co-op-översättararbetsflöde
- Redigera inte manuellt översatta filer (auto-genererade)

### Bidra

- Följ riktlinjer i `CONTRIBUTING.md`
- Acceptera Contributor License Agreement (CLA)
- Följ Microsoft Open Source Code of Conduct
- Håll säkerhet och autentiseringsuppgifter utanför commits

### Flerspråkigt stöd

Detta är ett polyglott förråd med exempel i:
- **Python** - ML/AI-arbetsflöden, Jupyter-notebooks, finjustering
- **C#/.NET** - Företagsapplikationer, ONNX Runtime-integration
- **JavaScript** - Webbaserad AI, webbläsarinferens med WebGPU

Välj det språk som bäst passar ditt användningsfall och mål för distribution.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->