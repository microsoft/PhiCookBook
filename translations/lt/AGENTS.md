<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T11:05:32+00:00",
  "source_file": "AGENTS.md",
  "language_code": "lt"
}
-->
# AGENTS.md

## Projekto apžvalga

PhiCookBook yra išsamus receptų saugyklos rinkinys, kuriame pateikiami praktiniai pavyzdžiai, mokymai ir dokumentacija, skirta dirbti su „Microsoft“ Phi mažųjų kalbos modelių (SLM) šeima. Saugykla demonstruoja įvairius naudojimo atvejus, įskaitant išvedimą, smulkiąją derinimą, kvantavimą, RAG įgyvendinimus ir daugiarūšes programas įvairiose platformose ir sistemose.

**Pagrindinės technologijos:**
- **Kalbos:** Python, C#/.NET, JavaScript/Node.js
- **Sistemos:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformos:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Modelių tipai:** Phi-3, Phi-3.5, Phi-4 (teksto, vaizdo, daugiarūšiai, loginio mąstymo variantai)

**Saugyklos struktūra:**
- `/code/` - Veikiantys kodo pavyzdžiai ir pavyzdinės įgyvendinimo versijos
- `/md/` - Išsami dokumentacija, mokymai ir vadovai  
- `/translations/` - Daugiakalbiai vertimai (50+ kalbų per automatizuotą darbo eigą)
- `/.devcontainer/` - Dev konteinerio konfigūracija (Python 3.12 su Ollama)

## Kūrimo aplinkos nustatymas

### Naudojant GitHub Codespaces arba Dev konteinerius (rekomenduojama)

1. Atidarykite GitHub Codespaces (greičiausias būdas):
   - Spustelėkite „Open in GitHub Codespaces“ ženkliuką README faile
   - Konteineris automatiškai sukonfigūruojamas su Python 3.12 ir Ollama su Phi-3

2. Atidarykite VS Code Dev konteineriuose:
   - Naudokite „Open in Dev Containers“ ženkliuką iš README
   - Konteineriui reikalinga mažiausiai 16GB RAM

### Vietinis nustatymas

**Reikalavimai:**
- Python 3.12 ar naujesnė versija
- .NET 8.0 SDK (C# pavyzdžiams)
- Node.js 18+ ir npm (JavaScript pavyzdžiams)
- Rekomenduojama mažiausiai 16GB RAM

**Įdiegimas:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python pavyzdžiams:**
Eikite į konkrečių pavyzdžių katalogus ir įdiekite priklausomybes:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NET pavyzdžiams:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web pavyzdžiams:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Saugyklos organizacija

### Kodo pavyzdžiai (`/code/`)

- **01.Introduce/** - Pagrindiniai įvado ir pradžios pavyzdžiai
- **03.Finetuning/** ir **04.Finetuning/** - Smulkiojo derinimo pavyzdžiai su įvairiais metodais
- **03.Inference/** - Išvedimo pavyzdžiai skirtingoje aparatinėje įrangoje (AIPC, MLX)
- **06.E2E/** - Pilnos programos pavyzdžiai
- **07.Lab/** - Laboratoriniai/eksperimentiniai įgyvendinimai
- **08.RAG/** - Informacijos paieškos ir generavimo pavyzdžiai
- **09.UpdateSamples/** - Naujausi atnaujinti pavyzdžiai

### Dokumentacija (`/md/`)

- **01.Introduction/** - Įvadiniai vadovai, aplinkos nustatymas, platformų vadovai
- **02.Application/** - Programų pavyzdžiai, suskirstyti pagal tipą (Tekstas, Kodas, Vaizdas, Garsas ir kt.)
- **02.QuickStart/** - Greito starto vadovai Azure AI Foundry ir GitHub Models
- **03.FineTuning/** - Smulkiojo derinimo dokumentacija ir mokymai
- **04.HOL/** - Praktiniai laboratoriniai darbai (įskaitant .NET pavyzdžius)

### Failų formatai

- **Jupyter užrašų knygelės (`.ipynb`)** - Interaktyvūs Python mokymai, pažymėti 📓 README faile
- **Python scenarijai (`.py`)** - Savarankiški Python pavyzdžiai
- **C# projektai (`.csproj`, `.sln`)** - .NET programos ir pavyzdžiai
- **JavaScript (`.js`, `package.json`)** - Web pagrindu ir Node.js pavyzdžiai
- **Markdown (`.md`)** - Dokumentacija ir vadovai

## Darbas su pavyzdžiais

### Jupyter užrašų knygelių paleidimas

Dauguma pavyzdžių pateikiami kaip Jupyter užrašų knygelės:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python scenarijų paleidimas

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

### JavaScript/Web pavyzdžių paleidimas

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testavimas

Ši saugykla apima pavyzdinį kodą ir mokymus, o ne tradicinį programinės įrangos projektą su vieneto testais. Tikrinimas paprastai atliekamas:

1. **Paleidžiant pavyzdžius** - Kiekvienas pavyzdys turėtų veikti be klaidų
2. **Rezultatų tikrinimas** - Patikrinkite, ar modelio atsakymai yra tinkami
3. **Vadovų laikymasis** - Vadovai turėtų veikti kaip dokumentuota

**Bendras tikrinimo metodas:**
- Testuokite pavyzdžių vykdymą tikslinėje aplinkoje
- Patikrinkite, ar priklausomybės tinkamai įdiegtos
- Patikrinkite, ar modeliai sėkmingai atsisiunčiami/įkeliami
- Patvirtinkite, kad tikėtinas elgesys atitinka dokumentaciją

## Kodo stilius ir konvencijos

### Bendros gairės

- Pavyzdžiai turėtų būti aiškūs, gerai komentuoti ir edukaciniai
- Laikykitės kalbai specifinių konvencijų (PEP 8 Python, C# standartai .NET)
- Pavyzdžiai turėtų būti orientuoti į konkrečių Phi modelių galimybių demonstravimą
- Įtraukite komentarus, paaiškinančius pagrindines sąvokas ir modelio specifinius parametrus

### Dokumentacijos standartai

**URL formatavimas:**
- Naudokite `[text](../../url)` formatą be papildomų tarpų
- Santykinės nuorodos: naudokite `./` dabartiniam katalogui, `../` tėviniam
- URL neturėtų turėti šalių specifinių lokalizacijų (vengti `/en-us/`, `/en/`)

**Vaizdai:**
- Visus vaizdus saugokite `/imgs/` kataloge
- Naudokite aprašomuosius pavadinimus su angliškais simboliais, skaičiais ir brūkšneliais
- Pavyzdys: `phi-3-architecture.png`

**Markdown failai:**
- Nurodykite faktinius veikiančius pavyzdžius iš `/code/` katalogo
- Dokumentaciją sinchronizuokite su kodo pakeitimais
- Naudokite 📓 jaustuką, kad pažymėtumėte Jupyter užrašų knygelių nuorodas README

### Failų organizavimas

- Kodo pavyzdžiai `/code/` kataloge, suskirstyti pagal temą/funkciją
- Dokumentacija `/md/` kataloge atspindi kodo struktūrą, kai tai įmanoma
- Susijusius failus (užrašų knygeles, scenarijus, konfigūracijas) laikykite kartu poaplankiuose

## Pasiūlymų pateikimo gairės

### Prieš pateikiant

1. **Forkinkite saugyklą** į savo paskyrą
2. **Atskirkite PR pagal tipą:**
   - Klaidų taisymai viename PR
   - Dokumentacijos atnaujinimai kitame
   - Nauji pavyzdžiai atskiruose PR
   - Rašybos klaidų taisymai gali būti sujungti

3. **Spręskite susijungimo konfliktus:**
   - Atnaujinkite savo vietinę `main` šaką prieš atlikdami pakeitimus
   - Dažnai sinchronizuokite su pagrindine saugykla

4. **Vertimo PR:**
   - Turi apimti visų failų vertimus aplanke
   - Išlaikykite originalios kalbos struktūrą

### Būtini patikrinimai

PR automatiškai vykdo GitHub darbo eigas, kad patikrintų:

1. **Santykinių kelių patikrinimas** - Visos vidinės nuorodos turi veikti
   - Testuokite nuorodas vietoje: Ctrl+Click VS Code
   - Naudokite VS Code kelių pasiūlymus (`./` arba `../`)

2. **URL lokalizacijos patikrinimas** - Interneto URL neturi turėti šalių lokalizacijų
   - Pašalinkite `/en-us/`, `/en/` ar kitus kalbos kodus
   - Naudokite bendrus tarptautinius URL

3. **Sugedusių URL patikrinimas** - Visi URL turi grąžinti 200 statusą
   - Patikrinkite, ar nuorodos yra pasiekiamos prieš pateikdami
   - Pastaba: Kai kurie gedimai gali būti dėl tinklo apribojimų

### PR pavadinimo formatas

```
[component] Brief description
```

Pavyzdžiai:
- `[docs] Pridėtas Phi-4 išvedimo vadovas`
- `[code] Pataisytas ONNX Runtime integracijos pavyzdys`
- `[translation] Pridėtas japonų kalbos vertimas įvadiniams vadovams`

## Bendri kūrimo modeliai

### Darbas su Phi modeliais

**Modelio įkėlimas:**
- Pavyzdžiai naudoja įvairias sistemas: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeliai paprastai atsisiunčiami iš Hugging Face, Azure arba GitHub Models
- Patikrinkite modelio suderinamumą su savo aparatine įranga (CPU, GPU, NPU)

**Išvedimo modeliai:**
- Teksto generavimas: Dauguma pavyzdžių naudoja pokalbių/instrukcijų variantus
- Vaizdas: Phi-3-vision ir Phi-4-multimodal vaizdų supratimui
- Garsas: Phi-4-multimodal palaiko garso įvestis
- Loginis mąstymas: Phi-4-reasoning variantai pažangiems loginio mąstymo užduotims

### Pastabos apie platformas

**Azure AI Foundry:**
- Reikalinga Azure prenumerata ir API raktai
- Žr. `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Nemokama versija testavimui
- Žr. `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Vietinis išvedimas:**
- ONNX Runtime: Kryžminė platforma, optimizuotas išvedimas
- Ollama: Lengvas vietinis modelių valdymas (iš anksto sukonfigūruotas dev konteineryje)
- Apple MLX: Optimizuotas Apple Silicon

## Trikčių šalinimas

### Dažnos problemos

**Atminties problemos:**
- Phi modeliams reikalinga didelė RAM (ypač vaizdo/daugiarūšiams variantams)
- Naudokite kvantuotus modelius ribotų resursų aplinkose
- Žr. `/md/01.Introduction/04/QuantifyingPhi.md`

**Priklausomybių konfliktai:**
- Python pavyzdžiai gali turėti specifinius versijų reikalavimus
- Naudokite virtualias aplinkas kiekvienam pavyzdžiui
- Patikrinkite individualius `requirements.txt` failus

**Modelio atsisiuntimo klaidos:**
- Dideli modeliai gali nutrūkti lėtuose ryšiuose
- Apsvarstykite debesų aplinkas (Codespaces, Azure)
- Patikrinkite Hugging Face talpyklą: `~/.cache/huggingface/`

**.NET projekto problemos:**
- Įsitikinkite, kad įdiegta .NET 8.0 SDK
- Naudokite `dotnet restore` prieš kurdami
- Kai kurie projektai turi CUDA specifines konfigūracijas (Debug_Cuda)

**JavaScript/Web pavyzdžiai:**
- Naudokite Node.js 18+ suderinamumui
- Išvalykite `node_modules` ir iš naujo įdiekite, jei kyla problemų
- Patikrinkite naršyklės konsolę dėl WebGPU suderinamumo problemų

### Pagalbos gavimas

- **Discord:** Prisijunkite prie Azure AI Foundry bendruomenės Discord
- **GitHub Issues:** Praneškite apie klaidas ir problemas saugykloje
- **GitHub Discussions:** Užduokite klausimus ir dalinkitės žiniomis

## Papildomas kontekstas

### Atsakingas AI

Visas Phi modelių naudojimas turėtų atitikti „Microsoft“ atsakingo AI principus:
- Teisingumas, patikimumas, saugumas
- Privatumas ir saugumas  
- Įtrauktis, skaidrumas, atskaitomybė
- Naudokite Azure AI Content Safety gamybinėms programoms
- Žr. `/md/01.Introduction/01/01.AISafety.md`

### Vertimai

- Palaikoma 50+ kalbų per automatizuotą GitHub veiksmą
- Vertimai `/translations/` kataloge
- Prižiūrima co-op-translator darbo eiga
- Neredaguokite rankiniu būdu išverstų failų (automatiškai generuojami)

### Prisidėjimas

- Laikykitės gairių `CONTRIBUTING.md`
- Sutikite su Contributor License Agreement (CLA)
- Laikykitės Microsoft Open Source Code of Conduct
- Neįtraukite saugumo ir prisijungimo duomenų į commit'us

### Daugiakalbė parama

Tai yra daugiakalbė saugykla su pavyzdžiais:
- **Python** - ML/AI darbo eigos, Jupyter užrašų knygelės, smulkusis derinimas
- **C#/.NET** - Verslo programos, ONNX Runtime integracija
- **JavaScript** - Web pagrindu AI, naršyklės išvedimas su WebGPU

Pasirinkite kalbą, kuri geriausiai atitinka jūsų naudojimo atvejį ir diegimo tikslą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingą interpretaciją, atsiradusią naudojant šį vertimą.