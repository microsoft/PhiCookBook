# AGENTS.md

## Projekt áttekintése

A PhiCookBook egy átfogó szakácskönyvgyűjtemény, amely gyakorlati példákat, oktatóanyagokat és dokumentációt tartalmaz a Microsoft Phi családjába tartozó Kis Nyelvi Modellekkel (SLM-ek) való munkához. A tároló különféle felhasználási eseteket mutat be, beleértve az inferenciát, finomhangolást, kvantálást, RAG megvalósításokat és multimodális alkalmazásokat különböző platformokon és keretrendszerekben.

**Kulcs technológiák:**
- **Nyelvek:** Python, C#/.NET, JavaScript/Node.js
- **Keretrendszerek:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformok:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltípusok:** Phi-3, Phi-3.5, Phi-4 (szöveges, képi, multimodális, érvelő változatok)

**Tároló struktúrája:**
- `/code/` - Működő kód példák és mintamegvalósítások
- `/md/` - Részletes dokumentáció, oktatóanyagok és útmutatók  
- `/translations/` - Többnyelvű fordítások (50+ nyelv automatizált munkafolyamattal)
- `/.devcontainer/` - Dev konténer konfiguráció (Python 3.12 Ollamával)

## Fejlesztői környezet beállítása

### GitHub Codespaces vagy Dev Containerek használata (ajánlott)

1. Megnyitás GitHub Codespaces-ben (leggyorsabb):
   - Kattintson a README-ben található "Open in GitHub Codespaces" jelvényre
   - A konténer automatikusan konfigurálódik Python 3.12-vel és Ollamával Phi-3-mal

2. Megnyitás VS Code Dev Containerekben:
   - Használja a README-ben található "Open in Dev Containers" jelvényt
   - A konténerhez legalább 16 GB memória szükséges a hoszton

### Helyi beállítás

**Előfeltételek:**
- Python 3.12 vagy újabb
- .NET 8.0 SDK (C# példákhoz)
- Node.js 18+ és npm (JavaScript példákhoz)
- Legalább 16 GB RAM javasolt

**Telepítés:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python példákhoz:**
Lépjen az adott példakönyvtárakba, és telepítse a függőségeket:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # ha a requirements.txt létezik
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
npm run dev  # Indítsa el a fejlesztői szervert
npm run build  # Fordítás éles környezetre
```

## Tároló szervezése

### Kódpéldák (`/code/`)

- **01.Introduce/** - Alap bevezetők és kezdőminták
- **03.Finetuning/** és **04.Finetuning/** - Finomhangoló példák különböző módszerekkel
- **03.Inference/** - Inferencia példák különböző hardveren (AIPC, MLX)
- **06.E2E/** - Végponttól végpontig alkalmazás minták
- **07.Lab/** - Labor/ kísérleti megvalósítások
- **08.RAG/** - Retrieval-Augmented Generation minták
- **09.UpdateSamples/** - Legújabb frissített példák

### Dokumentáció (`/md/`)

- **01.Introduction/** - Bevezető útmutatók, környezet beállítás, platform útmutatók
- **02.Application/** - Alkalmazási példák típus szerint (szöveg, kód, látás, hang, stb.)
- **02.QuickStart/** - Gyors kezdési útmutatók Microsoft Foundry és GitHub Models számára
- **03.FineTuning/** - Finomhangolási dokumentáció és oktatóanyagok
- **04.HOL/** - Gyakorlati laborok (tartalmaz .NET példákat)

### Fájlformátumok

- **Jupyter Notebookok (`.ipynb`)** - Interaktív Python oktatóanyagok 📓 jelöléssel a README-ben
- **Python szkriptek (`.py`)** - Önálló Python példák
- **C# projektek (`.csproj`, `.sln`)** - .NET alkalmazások és minták
- **JavaScript (`.js`, `package.json`)** - Webes és Node.js példák
- **Markdown (`.md`)** - Dokumentáció és útmutatók

## Példák használata

### Jupyter Notebookok futtatása

A legtöbb példa Jupyter notebook formájában érhető el:
```bash
pip install jupyter notebook
jupyter notebook  # Megnyitja a böngésző felületét
# Navigáljon a kívánt .ipynb fájlhoz
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

Vagy az egész megoldás buildelése:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web példák futtatása

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Fejlesztés forró újratöltéssel
```

## Tesztelés

Ez a tároló példakódokat és oktatóanyagokat tartalmaz, nem egy hagyományos egységtesztekkel rendelkező szoftverprojektet. Az érvényesítés általában a következők alapján történik:

1. **Példák futtatása** - Minden példának hibamentesen kell lefutnia
2. **Eredmények ellenőrzése** - Ellenőrizze, hogy a modell válaszai megfelelők-e
3. **Útmutatók követése** - Az oktatóanyagokat lépésről lépésre kell tudni követni dokumentált módon

**Gyakori érvényesítési mód:**
- Tesztelje a példák futását a célkörnyezetben
- Ellenőrizze, hogy a függőségek helyesen települnek-e
- Győződjön meg arról, hogy a modellek letöltése/betöltése sikeres
- Ellenőrizze, hogy az elvárt működés megfelel a dokumentációnak

## Kódstílus és szokások

### Általános irányelvek

- A példák legyenek világosak, jól kommentáltak és oktató jellegűek
- Kövesse az adott nyelv specifikus konvencióit (PEP 8 Pythonhoz, C# szabványok .NET-hez)
- A példák fókuszáljanak konkrét Phi modell képességek bemutatására
- Tartalmazzanak megjegyzéseket a kulcsfogalmakról és modell-specifikus paraméterekről

### Dokumentációs standardok

**URL formázás:**
- Használja a `[szöveg](../../url)` formátumot szóközök nélkül
- Relatív linkek: használja a `./` az aktuális könyvtárhoz, `../` a szülőhöz
- Ne használjon ország-specifikus lokalizációt az URL-ekben (kerülje az `/en-us/`, `/en/`)

**Képek:**
- Minden képet a `/imgs/` könyvtárban tároljon
- Használjon leíró neveket angol karakterekkel, számokkal és kötőjelekkel
- Példa: `phi-3-architecture.png`

**Markdown fájlok:**
- Hivatkozzanak ténylegesen működő példákra a `/code/` könyvtárból
- Tartsa szinkronban a dokumentációt és a kódbeli változásokat
- Használja a 📓 emojit a Jupyter notebook hivatkozások jelölésére README-ben

### Fájlok szervezése

- A kódpéldák a `/code/` alatt témák/funkciók szerint vannak rendszerezve
- A dokumentáció a `/md/` alatt tükrözi a kód struktúráját, ha lehetséges
- Tartsa együtt a kapcsolódó fájlokat (notebookok, szkriptek, konfigurációk) az alkönyvtárakban

## Pull Request (PR) irányelvek

### Beküldés előtt

1. **Forkolja a tárolót** saját fiókjába
2. **Külön PR-k típusa szerint:**
   - Hibajavítások külön PR-ben
   - Dokumentáció frissítések másikban
   - Új példák külön PR-kben
   - Gépelési hibajavítások összevonhatók

3. **Merge konfliktusok kezelése:**
   - Frissítse helyi `main` ágát a változtatások előtt
   - Gyakran szinkronizáljon az upstream-pel

4. **Fordítási PR-ek:**
   - Minden fájl fordítását tartalmazniuk kell az adott mappában
   - Eredeti nyelv szerkezetét meg kell tartani

### Kötelező ellenőrzések

A PR-ek automatikusan futtatnak GitHub munkafolyamatokat az érvényesítéshez:

1. **Relatív elérési út ellenőrzése** - Minden belső link működjön
   - Linkeket helyileg tesztelje: Ctrl+Kattintás VS Code-ban
   - Használja a VS Code által javasolt útvonalakat (`./` vagy `../`)

2. **URL lokalizáció ellenőrzése** - Webes URL-ek nem tartalmazhatnak országkódot
   - Távolítsa el az `/en-us/`, `/en/` vagy egyéb nyelvi kódokat
   - Használjon általános, nemzetközi URL-eket

3. **Broken URL ellenőrzés** - Az összes URL 200-as státuszt adjon vissza
   - Ellenőrizze a linkek elérhetőségét beküldés előtt
   - Megjegyzés: Néhány hiba hálózati korlátozás miatt lehet

### PR cím formátum

```
[component] Brief description
```

Példák:
- `[docs] Add Phi-4 inference tutorial`  
- `[code] Fix ONNX Runtime integration example`  
- `[translation] Add Japanese translation for intro guides`  

## Gyakori fejlesztési mintázatok

### Phi modellekkel való munka

**Modell betöltés:**
- A példák különböző keretrendszereket használnak: Transformers, ONNX Runtime, MLX, OpenVINO
- A modelleket általában Hugging Face-ről, Azure-ról vagy GitHub Models-ről töltik le
- Ellenőrizze a modell kompatibilitását a hardverével (CPU, GPU, NPU)

**Inferencia minták:**
- Szöveg generálás: Többnyire chat/utasítás változatokat használnak
- Látás: Phi-3-vision és Phi-4-multimodal képfelismeréshez
- Hang: Phi-4-multimodal hangbemenetekhez támogatott
- Érvelés: Phi-4-reasoning változatok fejlett érvelési feladatokhoz

### Platform specifikus megjegyzések

**Microsoft Foundry:**
- Azure előfizetés és API kulcsok szükségesek
- Lásd `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Ingyenes szint teszteléshez elérhető
- Lásd `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Helyi Inferencia:**
- ONNX Runtime: Többplatformos, optimalizált inferencia
- Ollama: Egyszerű helyi modellkezelés (előre konfigurált dev konténerben)
- Apple MLX: Optimalizált Apple Siliconhoz

## Hibakeresés

### Gyakori problémák

**Memória problémák:**
- A Phi modellek jelentős RAM-ot igényelnek (különösen látás/multimodális változatok)
- Használjon kvantált modelleket erőforrás-korlátos környezetben
- Lásd `/md/01.Introduction/04/QuantifyingPhi.md`

**Függőségi konfliktusok:**
- A Python példáknál előfordulhatnak specifikus verziókövetelmények
- Minden példához külön virtuális környezet javasolt
- Ellenőrizze az egyes `requirements.txt` fájlokat

**Modell letöltési hibák:**
- Nagy modellek lassú kapcsolaton időtúllépést okozhatnak
- Érdemes felhő alapú környezeteket használni (Codespaces, Azure)
- Ellenőrizze a Hugging Face gyorsítótárat: `~/.cache/huggingface/`

**.NET projekt problémák:**
- Győződjön meg róla, hogy telepítve van a .NET 8.0 SDK
- Használja a `dotnet restore` parancsot build előtt
- Néhány projekt CUDA-specifikus konfigurációkat használ (Debug_Cuda)

**JavaScript/Web példák:**
- Használjon Node.js 18+ verziót kompatibilitás miatt
- Ha problémák vannak, törölje a `node_modules` mappát és telepítse újra
- Ellenőrizze a böngésző konzolt WebGPU kompatibilitási problémák miatt

### Segítségkérés

- **Discord:** Csatlakozzon a Microsoft Foundry Community Discord szerverhez
- **GitHub Issues:** Jelentsen hibákat és problémákat a tárolóban
- **GitHub Discussions:** Tegyen fel kérdéseket és ossza meg tudását

## További háttér

### Felelős mesterséges intelligencia

Minden Phi modell használat során kövesse a Microsoft Felelős MI elveit:
- Méltányosság, megbízhatóság, biztonság
- Adatvédelem és biztonság  
- Befogadás, átláthatóság, elszámoltathatóság
- Használja az Azure AI Content Safety szolgáltatást éles alkalmazásokhoz
- Lásd `/md/01.Introduction/01/01.AISafety.md`

### Fordítások

- Több mint 50 nyelven támogatott automatizált GitHub Action segítségével
- A fordítások a `/translations/` könyvtárban találhatók
- A közösségi fordító munkafolyamat tartja karban
- Ne szerkessze kézzel a lefordított fájlokat (automatikusan generáltak)

### Közreműködés

- Kövesse a `CONTRIBUTING.md` irányelveit
- Fogadja el a Contributor License Agreement-et (CLA)
- Tartsa be a Microsoft nyílt forráskódú viselkedési kódexét
- Ne tegyen közzé biztonsági kulcsokat vagy hitelesítő adatokat commitokban

### Többnyelvű támogatás

Ez egy poliglott tároló, amely példákat tartalmaz:

- **Python** - ML/AI munkafolyamatok, Jupyter notebookok, finomhangolás
- **C#/.NET** - Vállalati alkalmazások, ONNX Runtime integráció
- **JavaScript** - Webes MI, böngészős inferencia WebGPU-vel

Válassza ki a nyelvet, amely leginkább megfelel az eseteinek és telepítési céljainak.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Amíg a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítás hibákat vagy pontatlanságokat tartalmazhat. Az eredeti dokumentum a saját nyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén professzionális emberi fordítás ajánlott. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->