# AGENTS.md

## Projekto apžvalga

PhiCookBook yra išsamus receptų knygos saugykla, kurioje yra praktinių pavyzdžių, pamokų ir dokumentacijos darbui su „Microsoft“ Phi šeimos mažaisiais kalbos modeliais (Small Language Models, SLM). Saugykla demonstruoja įvairius naudojimo atvejus, įskaitant spėjimą, tobulinimą (fine-tuning), kiekybinimą (quantization), RAG įgyvendinimus bei multimodalines programas įvairiose platformose ir sistemose.

**Pagrindinės technologijos:**
- **Programavimo kalbos:** Python, C#/.NET, JavaScript/Node.js
- **Sistemos:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformos:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modelių tipai:** Phi-3, Phi-3.5, Phi-4 (teksto, vaizdo, multimodalios, samprotavimo variacijos)

**Saugyklos struktūra:**
- `/code/` - Veikiantys kodo pavyzdžiai ir mėginiai
- `/md/` - Detali dokumentacija, pamokos ir vadovai  
- `/translations/` - Daugiakalbės vertimai (daugiau nei 50 kalbų automatinio darbo eiga)
- `/.devcontainer/` - Dev konteinerio konfigūracija (Python 3.12 su Ollama)

## Aplinkos diegimo instrukcijos

### Naudojant GitHub Codespaces arba Dev konteinerius (rekomenduojama)

1. Atidaryti GitHub Codespaces (greičiausia):
   - Spustelėkite „Open in GitHub Codespaces“ ženklelį README faile
   - Konteineris automatiškai sukonfigūruojamas su Python 3.12 ir Ollama su Phi-3 modeliu

2. Atidaryti VS Code Dev konteinerius:
   - Naudokite „Open in Dev Containers“ ženklelį README faile
   - Konteineriui reikia mažiausiai 16 GB atminties kompiuteryje

### Vietinis diegimas

**Reikalavimai:**
- Python 3.12 ar naujesnė versija
- .NET 8.0 SDK (C# pavyzdžiams)
- Node.js 18+ ir npm (JavaScript pavyzdžiams)
- Rekomenduojama mažiausiai 16 GB RAM

**Diegimas:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python pavyzdžiams:**
Eikite į konkrečių pavyzdžių katalogus ir įdiekite priklausomybes:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # jei yra failas requirements.txt
```

**.NET pavyzdžiams:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript / Web pavyzdžiams:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Paleisti kūrimo serverį
npm run build  # Sukurti gamybai
```

## Saugyklos organizavimas

### Kodo pavyzdžiai (`/code/`)

- **01.Introduce/** - Pagrindiniai įvado ir pradžios pavyzdžiai
- **03.Finetuning/** ir **04.Finetuning/** - Tobulinimo pavyzdžiai su įvairiais metodais
- **03.Inference/** - Spėjimo pavyzdžiai skirtingoje įrangoje (AIPC, MLX)
- **06.E2E/** - Galo iki galo programų pavyzdžiai
- **07.Lab/** - Laboratoriniai / eksperimentiniai įgyvendinimai
- **08.RAG/** - Retrieval-Augmented Generation pavyzdžiai
- **09.UpdateSamples/** - Naujausi atnaujinti pavyzdžiai

### Dokumentacija (`/md/`)

- **01.Introduction/** - Įvado vadovai, aplinkos diegimas, platformų vadovai
- **02.Application/** - Programų pavyzdžiai pagal tipus (Tekstas, Kodas, Vaizdas, Garsas ir kt.)
- **02.QuickStart/** - Greito starto vadovai Microsoft Foundry ir GitHub Models
- **03.FineTuning/** - Tobulinimo dokumentacija ir pamokos
- **04.HOL/** - Praktinės laboratorijos (įskaitant .NET pavyzdžius)

### Failų formatai

- **Jupyter užrašų knygelės (`.ipynb`)** - Interaktyvios Python pamokos, pažymėtos 📓 README
- **Python skriptai (`.py`)** - Atitinkami Python pavyzdžiai
- **C# projektai (`.csproj`, `.sln`)** - .NET programos ir pavyzdžiai
- **JavaScript (`.js`, `package.json`)** - Interneto ir Node.js pavyzdžiai
- **Markdown (`.md`)** - Dokumentacija ir vadovai

## Darbas su pavyzdžiais

### Jupyter užrašų knygelių paleidimas

Dauguma pavyzdžių pateikti kaip Jupyter užrašų knygelės:
```bash
pip install jupyter notebook
jupyter notebook  # Atidaro naršyklės sąsają
# Pereiti prie norimo .ipynb failo
```

### Python skriptų paleidimas

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET pavyzdžių paleidimas

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Arba sukurkite visą sprendimą:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript / Web pavyzdžių paleidimas

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Kūrimas su karštu atnaujinimu
```

## Testavimas

Šioje saugykloje yra pavyzdinis kodas ir pamokos, bet nėra įprasto programinės įrangos projekto su vienetiniais testais. Patikra paprastai atliekama:

1. **Paleidus pavyzdžius** - Kiekvienas pavyzdys turi veikti be klaidų
2. **Patikrinus rezultatus** - Patikrinti, ar modelio atsakymai tinkami
3. **Sekant pamokas** - Žingsnis po žingsnio vadovai turi veikti kaip aprašyta

**Įprasta patikros strategija:**
- Išbandyti pavyzdžių vykdymą tikslinėje aplinkoje
- Patikrinti, ar priklausomybės sėkmingai įdiegtos
- Patikrinti, ar modeliai atsisiunčiami / kraunami sėkmingai
- Patvirtinti, kad elgsena atitinka dokumentaciją

## Kodo stilius ir konvencijos

### Bendros gairės

- Pavyzdžiai turi būti aiškūs, gerai komentuoti ir mokomieji
- Laikytis kalbų specifinių konvencijų (PEP 8 Python, C# standartai .NET)
- Sutelkti dėmesį į specifinių Phi modelio galimybių demonstravimą
- Įtraukti komentarus, paaiškinančius pagrindines sąvokas ir parametrus

### Dokumentacijos standartai

**URL formatavimas:**
- Naudoti `[tekstas](../../url)` formatą be papildomų tarpų
- Santykiniai saitai: naudoti `./` einamam katalogui, `../` tėviniam
- Nevartoti šalių specifinių lokalizacijų URL (vengti `/en-us/`, `/en/`)

**Paveikslėliai:**
- Visus paveikslėlius laikyti kataloge `/imgs/`
- Naudoti aprašomuosius pavadinimus anglų raidėmis, skaičiais ir brūkšniais
- Pavyzdys: `phi-3-architecture.png`

**Markdown failai:**
- Nurodyti realius veikiančius pavyzdžius kataloge `/code/`
- Dokumentaciją sinchronizuoti su kodo pakeitimais
- Naudoti 📓 emociją pažymėti Jupyter užrašų knygelių nuorodas README

### Failų organizavimas

- Kodo pavyzdžiai kataloge `/code/` organizuoti pagal temą / funkciją
- Dokumentacija kataloge `/md/` atspindi kodo struktūrą, kai taikoma
- Susiję failai (užrašų knygos, skriptai, konfigai) laikyti kartu posistemuose

## Pull request gairės

### Prieš pateikiant

1. **Sukurkite saugyklos forką** savo paskyroje
2. **Atskirkite PR pagal tipą:**
   - Klaidų taisymai viename PR
   - Dokumentacijos atnaujinimai kitame
   - Nauji pavyzdžiai atskiruose PR
   - Rašybos pataisymai gali būti kartu

3. **Tvarkykite susijungimo konfliktus:**
   - Pirmiausia atnaujinkite vietinį `main` šaką prieš keitimus
   - Dažnai sinchronizuokitės su viršutiniu saugyklos šaku

4. **Vertimų PR:**
   - Turi apimti VISŲ katalogo failų vertimus
   - Išlaikyti nuoseklią struktūrą su šaltinio kalba

### Privalomi patikrinimai

PR automatiškai paleidžia GitHub darbo eigas, kad patikrintų:

1. **Santykinės nuorodos validavimas** - Visos vidinės nuorodos turi veikti
   - Testuoti nuorodas lokaliai: Ctrl + Spustelėjimas VS Code
   - Naudoti VS Code pateikiamas kelių siūlymus (`./` arba `../`)

2. **URL lokalės patikra** - Interneto URL neturi turėti šalies lokalės
   - Pašalinti `/en-us/`, `/en/` ar kitų kalbų kodus
   - Naudoti bendrinius tarptautinius adresus

3. **Nutrūkusių URL patikra** - Visi URL turi grąžinti 200 statusą
   - Patikrinti nuorodų pasiekiamumą prieš pateikiant
   - Pastaba: kai kurios klaidos gali būti dėl tinklo apribojimų

### PR pavadinimo formatas

```
[component] Brief description
```

Pavyzdžiai:
- `[docs] Pridėti Phi-4 spėjimo pamoką`
- `[code] Ištaisyti ONNX Runtime integracijos pavyzdį`
- `[translation] Pridėti japonų vertimą įvadams`

## Dažni vystymo modeliai

### Darbas su Phi modeliais

**Modelių įkėlimas:**
- Pavyzdžiai naudoja įvairias sistemas: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeliai dažniausiai atsisiunčiami iš Hugging Face, Azure ar GitHub Models
- Patikrinkite modelio suderinamumą su jūsų įranga (CPU, GPU, NPU)

**Spėjimo modeliai:**
- Teksto generavimas: dauguma pavyzdžių naudoja chat/instruction variantus
- Vaizdas: Phi-3-vision ir Phi-4-multimodal vaizdo supratimui
- Garsas: Phi-4-multimodal palaiko garso įvestis
- Samprotavimas: Phi-4-reasoning pažangiems samprotavimo uždaviniams

### Platformų specifinės pastabos

**Microsoft Foundry:**
- Reikia Azure prenumeratos ir API raktų
- Žr. `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Yra nemokama bandomoji versija
- Žr. `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Vietinis spėjimas:**
- ONNX Runtime: tarpplatforminis optimizuotas spėjimas
- Ollama: lengvas vietinis modelių valdymas (iš anksto konfigūruota dev konteineryje)
- Apple MLX: optimizuotas Apple Silicio įrenginiams

## Gedimų šalinimas

### Dažnos problemos

**Atminties problemos:**
- Phi modeliai reikalauja daug RAM (ypač vaizdo / multimodalios variacijos)
- Naudokite kiekybintus (quantized) modelius resursų apribojimams
- Žr. `/md/01.Introduction/04/QuantifyingPhi.md`

**Priklausomybių konfliktai:**
- Python pavyzdžiai gali turėti specifinius versijų reikalavimus
- Naudokite virtualias aplinkas kiekvienam pavyzdžiui
- Patikrinkite atskirus `requirements.txt` failus

**Modelių atsisiuntimo nesėkmės:**
- Dideli modeliai gali laukti ryšio lėtumo atveju
- Apsvarstykite debesų aplinkas (Codespaces, Azure)
- Patikrinkite Hugging Face kešą: `~/.cache/huggingface/`

**.NET projekto problemos:**
- Įsitikinkite, kad įdiegtas .NET 8.0 SDK
- Naudokite `dotnet restore` prieš sudarant sprendimą
- Kai kurie projektai turi CUDA specifines konfigūracijas (Debug_Cuda)

**JavaScript/Web pavyzdžiai:**
- Naudokite Node.js 18+ dėl suderinamumo
- Išvalykite `node_modules` ir perinstaliuokite, jei yra problemų
- Patikrinkite naršyklės konsolę dėl WebGPU suderinamumo problemų

### Pagalba

- **Discord:** Prisijunkite prie Microsoft Foundry bendruomenės Discord
- **GitHub Issues:** Praneškite apie klaidas ir problemas saugykloje
- **GitHub Discussions:** Užduokite klausimus ir dalinkitės žiniomis

## Papildoma informacija

### Atsakingas dirbtinis intelektas

Visi Phi modelių panaudojimai turi atitikti „Microsoft“ atsakingo DI principus:
- Sąžiningumas, patikimumas, saugumas
- Privatumas ir saugumas  
- Įtrauktis, skaidrumas, atskaitomybė
- Naudokite Azure AI Content Safety gamybos programoms
- Žr. `/md/01.Introduction/01/01.AISafety.md`

### Vertimai

- Daugiau nei 50 kalbų, palaikoma automatinė GitHub Action
- Vertimai kataloge `/translations/`
- Prižiūrimi pagal co-op-translator darbo eigą
- Nesitvarkykite vertimų failų rankiniu būdu (automatiškai generuojami)

### Bendradarbiavimas

- Laikykitės gaires faile `CONTRIBUTING.md`
- Sutikite su Bendradarbio licencijos sutartimi (Contributor License Agreement, CLA)
- Laikykitės Microsoft atvirojo kodo elgesio kodekso
- Neskelbkite saugumo informacijos ar prisijungimo duomenų commit'uose

### Daugiakalbė palaikymas

Tai poliglotinė saugykla su pavyzdžiais:
- **Python** - ML/AI darbo eiga, Jupyter užrašų knygelės, tobulinimas
- **C#/.NET** - Verslo programos, ONNX Runtime integracija
- **JavaScript** - Interneto DI, naršyklės spėjimas su WebGPU  

Pasirinkite kalbą, kuri geriausiai atitinka jūsų atvejį ir diegimo tikslą.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neatsakome už jokius nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->