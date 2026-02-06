# AGENTS.md

## Projekt áttekintése

A PhiCookBook egy átfogó szakácskönyv-repozitórium, amely gyakorlati példákat, oktatóanyagokat és dokumentációt tartalmaz a Microsoft Phi kis nyelvi modellek (SLM-ek) használatához. A repozitórium különböző felhasználási eseteket mutat be, beleértve az előrejelzést, finomhangolást, kvantálást, RAG implementációkat és multimodális alkalmazásokat különböző platformokon és keretrendszereken.

**Kulcstechnológiák:**
- **Nyelvek:** Python, C#/.NET, JavaScript/Node.js
- **Keretrendszerek:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformok:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltípusok:** Phi-3, Phi-3.5, Phi-4 (szöveg, látás, multimodális, érvelési változatok)

**Repozitórium felépítése:**
- `/code/` - Működő kódpéldák és mintamegvalósítások
- `/md/` - Részletes dokumentáció, oktatóanyagok és útmutatók  
- `/translations/` - Többnyelvű fordítások (50+ nyelv automatikus munkafolyamat révén)
- `/.devcontainer/` - Fejlesztői konténer konfiguráció (Python 3.12 Ollama-val)

## Fejlesztési környezet beállítása

### GitHub Codespaces vagy fejlesztői konténerek használata (ajánlott)

1. Nyitás GitHub Codespaces-ben (leggyorsabb):
   - Kattintson a "Open in GitHub Codespaces" jelvényre a README-ben
   - A konténer automatikusan konfigurálódik Python 3.12 és Ollama Phi-3-mal

2. Nyitás VS Code fejlesztői konténerekben:
   - Használja az "Open in Dev Containers" jelvényt a README-ből
   - A konténerhez minimum 16GB host memória szükséges

### Helyi beállítás

**Előfeltételek:**
- Python 3.12 vagy újabb
- .NET 8.0 SDK (C# példákhoz)
- Node.js 18+ és npm (JavaScript példákhoz)
- Minimum 16GB RAM ajánlott

**Telepítés:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python példákhoz:**
Navigáljon a konkrét példa könyvtárakba és telepítse a függőségeket:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NET példákhoz:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web példákhoz:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Repozitórium szervezése

### Kódpéldák (`/code/`)

- **01.Introduce/** - Alapvető bevezetők és kezdő minták
- **03.Finetuning/** és **04.Finetuning/** - Finomhangolási példák különböző módszerekkel
- **03.Inference/** - Előrejelzési példák különböző hardvereken (AIPC, MLX)
- **06.E2E/** - Teljes körű alkalmazási minták
- **07.Lab/** - Laboratóriumi/kísérleti megvalósítások
- **08.RAG/** - Visszakeresés-alapú generálási minták
- **09.UpdateSamples/** - Legfrissebb frissített minták

### Dokumentáció (`/md/`)

- **01.Introduction/** - Bevezető útmutatók, környezet beállítása, platform útmutatók
- **02.Application/** - Alkalmazási minták típus szerint (Szöveg, Kód, Látás, Hang, stb.)
- **02.QuickStart/** - Gyors kezdési útmutatók Azure AI Foundry és GitHub Models számára
- **03.FineTuning/** - Finomhangolási dokumentáció és oktatóanyagok
- **04.HOL/** - Gyakorlati laborok (.NET példákat is tartalmaz)

### Fájlformátumok

- **Jupyter Notebookok (`.ipynb`)** - Interaktív Python oktatóanyagok 📓 jelzéssel a README-ben
- **Python szkriptek (`.py`)** - Önálló Python példák
- **C# projektek (`.csproj`, `.sln`)** - .NET alkalmazások és minták
- **JavaScript (`.js`, `package.json`)** - Web-alapú és Node.js példák
- **Markdown (`.md`)** - Dokumentáció és útmutatók

## Példák használata

### Jupyter Notebookok futtatása

A legtöbb példa Jupyter notebookként érhető el:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python szkriptek futtatása

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET példák futtatása

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Vagy az egész megoldás építése:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web példák futtatása

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Tesztelés

Ez a repozitórium példakódot és oktatóanyagokat tartalmaz, nem hagyományos szoftverprojektet egységtesztekkel. Az érvényesítés általában az alábbiak szerint történik:

1. **Példák futtatása** - Minden példa hibamentesen kell, hogy fusson
2. **Kimenetek ellenőrzése** - Ellenőrizze, hogy a modell válaszai megfelelőek-e
3. **Oktatóanyagok követése** - Az útmutatók lépései működjenek a dokumentáció szerint

**Általános érvényesítési megközelítés:**
- Példák futtatása a célkörnyezetben
- Függőségek helyes telepítésének ellenőrzése
- Modell letöltésének/betöltésének sikeressége
- Dokumentációval egyező viselkedés megerősítése

## Kódstílus és konvenciók

### Általános irányelvek

- A példák legyenek érthetőek, jól kommentáltak és oktató jellegűek
- Kövesse a nyelvspecifikus konvenciókat (PEP 8 Pythonhoz, C# szabványok .NET-hez)
- A példák fókuszáljanak a Phi modellek specifikus képességeinek bemutatására
- Tartalmazzon kommenteket, amelyek kulcsfogalmakat és modell-specifikus paramétereket magyaráznak

### Dokumentációs szabványok

**URL formázás:**
- Használja a `[szöveg](../../url)` formátumot extra szóközök nélkül
- Relatív hivatkozások: Használja a `./` az aktuális könyvtárhoz, `../` a szülőhöz
- Ne használjon ország-specifikus lokalizációkat az URL-ekben (kerülje a `/en-us/`, `/en/`)

**Képek:**
- Minden képet az `/imgs/` könyvtárban tároljon
- Használjon leíró neveket angol karakterekkel, számokkal és kötőjelekkel
- Példa: `phi-3-architecture.png`

**Markdown fájlok:**
- Hivatkozzon tényleges működő példákra a `/code/` könyvtárban
- Tartsa a dokumentációt szinkronban a kódváltozásokkal
- Használja a 📓 emojit a Jupyter notebook hivatkozások jelölésére a README-ben

### Fájlszervezés

- Kódpéldák a `/code/` könyvtárban témák/jellemzők szerint szervezve
- Dokumentáció a `/md/` könyvtárban, amely tükrözi a kód szerkezetét, ha alkalmazható
- Kapcsolódó fájlok (notebookok, szkriptek, konfigurációk) együtt tartása az alkönyvtárakban

## Pull Request irányelvek

### Beküldés előtt

1. **Forkolja a repozitóriumot** a saját fiókjába
2. **PR-ok szétválasztása típus szerint:**
   - Hibajavítások egy PR-ban
   - Dokumentáció frissítések egy másikban
   - Új példák külön PR-ban
   - Elírások javítása kombinálható

3. **Ütközések kezelése:**
   - Frissítse a helyi `main` ágat a változtatások előtt
   - Gyakran szinkronizáljon az upstreammel

4. **Fordítási PR-ok:**
   - Tartalmaznia kell az összes fájl fordítását a mappában
   - Tartsa meg az eredeti nyelv szerkezetét

### Kötelező ellenőrzések

A PR-ok automatikusan futtatják a GitHub munkafolyamatokat az érvényesítéshez:

1. **Relatív útvonal érvényesítés** - Minden belső hivatkozásnak működnie kell
   - Helyi hivatkozások tesztelése: Ctrl+Click a VS Code-ban
   - Használja a VS Code útvonaljavaslatait (`./` vagy `../`)

2. **URL lokalizáció ellenőrzése** - A webes URL-ek nem tartalmazhatnak országkódokat
   - Távolítsa el a `/en-us/`, `/en/` vagy más nyelvi kódokat
   - Használjon általános nemzetközi URL-eket

3. **Törött URL ellenőrzés** - Minden URL-nek 200-as státuszt kell visszaadnia
   - Ellenőrizze, hogy a hivatkozások elérhetők-e beküldés előtt
   - Megjegyzés: Néhány hiba hálózati korlátozások miatt lehet

### PR cím formátuma

```
[component] Brief description
```

Példák:
- `[docs] Phi-4 előrejelzési oktatóanyag hozzáadása`
- `[code] ONNX Runtime integrációs példa javítása`
- `[translation] Japán fordítás hozzáadása a bevezető útmutatókhoz`

## Gyakori fejlesztési minták

### Phi modellekkel való munka

**Modell betöltése:**
- A példák különböző keretrendszereket használnak: Transformers, ONNX Runtime, MLX, OpenVINO
- A modellek általában a Hugging Face, Azure vagy GitHub Models oldalról tölthetők le
- Ellenőrizze a modell kompatibilitását a hardverével (CPU, GPU, NPU)

**Előrejelzési minták:**
- Szöveg generálás: A legtöbb példa chat/instruct változatokat használ
- Látás: Phi-3-vision és Phi-4-multimodal képfelismeréshez
- Hang: Phi-4-multimodal támogatja a hangbemeneteket
- Érvelés: Phi-4-reasoning változatok fejlett érvelési feladatokhoz

### Platform-specifikus megjegyzések

**Azure AI Foundry:**
- Azure előfizetést és API kulcsokat igényel
- Lásd: `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Ingyenes szint teszteléshez elérhető
- Lásd: `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Helyi előrejelzés:**
- ONNX Runtime: Keresztplatformos, optimalizált előrejelzés
- Ollama: Könnyű helyi modellkezelés (előre konfigurálva a fejlesztői konténerben)
- Apple MLX: Optimalizált Apple Silicon számára

## Hibakeresés

### Gyakori problémák

**Memória problémák:**
- A Phi modellek jelentős RAM-ot igényelnek (különösen látás/multimodális változatok)
- Használjon kvantált modelleket erőforrás-korlátozott környezetekben
- Lásd: `/md/01.Introduction/04/QuantifyingPhi.md`

**Függőségi konfliktusok:**
- A Python példák specifikus verziókövetelményekkel rendelkezhetnek
- Használjon virtuális környezeteket minden példához
- Ellenőrizze az egyes `requirements.txt` fájlokat

**Modell letöltési hibák:**
- Nagy modellek lassú kapcsolatokon időtúllépést okozhatnak
- Fontolja meg felhőalapú környezetek használatát (Codespaces, Azure)
- Ellenőrizze a Hugging Face cache-t: `~/.cache/huggingface/`

**.NET projekt problémák:**
- Győződjön meg róla, hogy a .NET 8.0 SDK telepítve van
- Használja a `dotnet restore` parancsot az építés előtt
- Néhány projekt CUDA-specifikus konfigurációval rendelkezik (Debug_Cuda)

**JavaScript/Web példák:**
- Használjon Node.js 18+ kompatibilitás érdekében
- Törölje a `node_modules` könyvtárat és telepítse újra, ha problémák merülnek fel
- Ellenőrizze a böngésző konzolt WebGPU kompatibilitási problémák esetén

### Segítség kérése

- **Discord:** Csatlakozzon az Azure AI Foundry Community Discordhoz
- **GitHub Issues:** Jelentsen hibákat és problémákat a repozitóriumban
- **GitHub Discussions:** Tegyen fel kérdéseket és ossza meg tudását

## További információk

### Felelős AI

Minden Phi modell használatának követnie kell a Microsoft Felelős AI elveit:
- Méltányosság, megbízhatóság, biztonság
- Adatvédelem és biztonság  
- Befogadás, átláthatóság, elszámoltathatóság
- Használja az Azure AI Content Safety-t produkciós alkalmazásokhoz
- Lásd: `/md/01.Introduction/01/01.AISafety.md`

### Fordítások

- 50+ nyelv támogatott automatikus GitHub Action révén
- Fordítások a `/translations/` könyvtárban
- A co-op-translator munkafolyamat által karbantartva
- Ne szerkessze manuálisan a fordított fájlokat (automatikusan generált)

### Hozzájárulás

- Kövesse a `CONTRIBUTING.md` irányelveit
- Fogadja el a Contributor License Agreement (CLA)-t
- Tartsa be a Microsoft Open Source Code of Conduct-ot
- Ne tegyen biztonsági adatokat és hitelesítő adatokat a commitokba

### Többnyelvű támogatás

Ez egy többnyelvű repozitórium, amely példákat tartalmaz:
- **Python** - ML/AI munkafolyamatok, Jupyter notebookok, finomhangolás
- **C#/.NET** - Vállalati alkalmazások, ONNX Runtime integráció
- **JavaScript** - Web-alapú AI, böngésző előrejelzés WebGPU-val

Válassza ki azt a nyelvet, amely legjobban megfelel az Ön felhasználási esetének és telepítési céljának.

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.