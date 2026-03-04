# AGENTS.md

## Pregled projekta

PhiCookBook je obsežna zbirka kuharskih receptov, ki vsebuje praktične primere, vadnice in dokumentacijo za delo z Microsoftovo družino malih jezikovnih modelov (SLM) Phi. Zbirka prikazuje različne primere uporabe, vključno z inferenco, prilagajanjem, kvantizacijo, implementacijami RAG in multimodalnimi aplikacijami na različnih platformah in okvirjih.

**Ključne tehnologije:**
- **Jeziki:** Python, C#/.NET, JavaScript/Node.js
- **Okviri:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Vrste modelov:** Phi-3, Phi-3.5, Phi-4 (tekst, vizija, multimodalni, varianti za razmišljanje)

**Struktura repozitorija:**
- `/code/` - Delujoči primeri kode in vzorčne implementacije
- `/md/` - Podrobna dokumentacija, vadnice in navodila  
- `/translations/` - Večjezične prevode (50+ jezikov prek avtomatiziranega delovnega toka)
- `/.devcontainer/` - Konfiguracija razvojnega okolja (Python 3.12 z Ollama)

## Nastavitev razvojnega okolja

### Uporaba GitHub Codespaces ali razvojnih okolij (priporočeno)

1. Odprite v GitHub Codespaces (najhitreje):
   - Kliknite značko "Open in GitHub Codespaces" v README
   - Kontejner se samodejno konfigurira s Python 3.12 in Ollama s Phi-3

2. Odprite v VS Code Dev Containers:
   - Uporabite značko "Open in Dev Containers" iz README
   - Kontejner zahteva najmanj 16 GB pomnilnika gostitelja

### Lokalna nastavitev

**Predpogoji:**
- Python 3.12 ali novejši
- .NET 8.0 SDK (za primere v C#)
- Node.js 18+ in npm (za primere v JavaScriptu)
- Priporočeno najmanj 16 GB RAM-a

**Namestitev:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Za primere v Pythonu:**
Pomaknite se do specifičnih direktorijev primerov in namestite odvisnosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Za primere v .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Za primere v JavaScriptu/spletu:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organizacija repozitorija

### Primeri kode (`/code/`)

- **01.Introduce/** - Osnovni uvodi in vzorci za začetek
- **03.Finetuning/** in **04.Finetuning/** - Primeri prilagajanja z različnimi metodami
- **03.Inference/** - Primeri inferenc na različni strojni opremi (AIPC, MLX)
- **06.E2E/** - Vzorci aplikacij od začetka do konca
- **07.Lab/** - Laboratorijske/eksperimentalne implementacije
- **08.RAG/** - Primeri generacije z iskanjem (RAG)
- **09.UpdateSamples/** - Najnovejši posodobljeni vzorci

### Dokumentacija (`/md/`)

- **01.Introduction/** - Uvodni vodiči, nastavitev okolja, vodiči za platforme
- **02.Application/** - Vzorci aplikacij, organizirani po vrsti (tekst, koda, vizija, zvok itd.)
- **02.QuickStart/** - Hitri vodiči za Microsoft Foundry in GitHub Models
- **03.FineTuning/** - Dokumentacija in vadnice za prilagajanje
- **04.HOL/** - Praktične delavnice (vključuje primere v .NET)

### Oblike datotek

- **Jupyter zvezki (`.ipynb`)** - Interaktivne vadnice v Pythonu, označene z 📓 v README
- **Python skripte (`.py`)** - Samostojni primeri v Pythonu
- **C# projekti (`.csproj`, `.sln`)** - .NET aplikacije in vzorci
- **JavaScript (`.js`, `package.json`)** - Spletni in Node.js primeri
- **Markdown (`.md`)** - Dokumentacija in vodiči

## Delo s primeri

### Zagon Jupyter zvezkov

Večina primerov je na voljo kot Jupyter zvezki:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Zagon Python skriptov

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Zagon primerov v .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ali zgradite celotno rešitev:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Zagon primerov v JavaScriptu/spletu

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testiranje

Ta repozitorij vsebuje primeri kode in vadnice, ne pa tradicionalnega programskega projekta z enotnimi testi. Validacija se običajno izvaja z:

1. **Zagon primerov** - Vsak primer naj se izvede brez napak
2. **Preverjanje izhodov** - Preverite, ali so odzivi modela ustrezni
3. **Sledenje vadnicam** - Vodiči po korakih naj delujejo, kot je dokumentirano

**Pogost pristop k validaciji:**
- Testirajte izvedbo primerov v ciljnem okolju
- Preverite, ali se odvisnosti pravilno namestijo
- Preverite, ali se modeli uspešno prenesejo/naložijo
- Potrdite, da pričakovano vedenje ustreza dokumentaciji

## Slog kode in konvencije

### Splošne smernice

- Primeri naj bodo jasni, dobro komentirani in poučni
- Upoštevajte jezikovno specifične konvencije (PEP 8 za Python, standardi C# za .NET)
- Ohranite primere osredotočene na prikaz specifičnih zmogljivosti modelov Phi
- Vključite komentarje, ki pojasnjujejo ključne koncepte in parametre specifične za model

### Standardi dokumentacije

**Oblikovanje URL-jev:**
- Uporabite format `[text](../../url)` brez dodatnih presledkov
- Relativne povezave: Uporabite `./` za trenutni direktorij, `../` za nadrejeni
- Brez lokaliziranih URL-jev (izogibajte se `/en-us/`, `/en/`)

**Slike:**
- Vse slike shranite v direktorij `/imgs/`
- Uporabite opisna imena z angleškimi znaki, številkami in vezaji
- Primer: `phi-3-architecture.png`

**Markdown datoteke:**
- Sklicujte se na dejanske delujoče primere v direktoriju `/code/`
- Dokumentacijo sinhronizirajte s spremembami kode
- Uporabite emoji 📓 za označevanje povezav do Jupyter zvezkov v README

### Organizacija datotek

- Primeri kode v `/code/` organizirani po temi/funkciji
- Dokumentacija v `/md/` zrcali strukturo kode, kadar je to primerno
- Povezane datoteke (zvezki, skripte, konfiguracije) hranite skupaj v poddirektorijih

## Smernice za zahteve za združitev (Pull Request)

### Pred oddajo

1. **Forkajte repozitorij** na svoj račun
2. **Ločite PR-je po vrsti:**
   - Popravki napak v enem PR-ju
   - Posodobitve dokumentacije v drugem
   - Novi primeri v ločenih PR-jih
   - Popravki tipk lahko združite

3. **Obravnavajte konflikte pri združevanju:**
   - Posodobite svojo lokalno vejo `main` pred spremembami
   - Pogosto sinhronizirajte z izvorno vejo

4. **Prevajalski PR-ji:**
   - Vključevati morajo prevode za VSE datoteke v mapi
   - Ohranite dosledno strukturo z izvirnim jezikom

### Zahtevani pregledi

PR-ji samodejno izvajajo GitHub delovne tokove za validacijo:

1. **Validacija relativnih poti** - Vse notranje povezave morajo delovati
   - Testirajte povezave lokalno: Ctrl+Klik v VS Code
   - Uporabite predloge poti iz VS Code (`./` ali `../`)

2. **Preverjanje lokalizacije URL-jev** - Spletni URL-ji ne smejo vsebovati jezikovnih kod
   - Odstranite `/en-us/`, `/en/` ali druge jezikovne kode
   - Uporabite generične mednarodne URL-je

3. **Preverjanje pokvarjenih URL-jev** - Vsi URL-ji morajo vrniti status 200
   - Preverite, ali so povezave dostopne pred oddajo
   - Opomba: Nekatere napake so lahko posledica omrežnih omejitev

### Format naslova PR-ja

```
[component] Brief description
```

Primeri:
- `[docs] Dodaj vadnico za inferenco Phi-4`
- `[code] Popravi primer integracije ONNX Runtime`
- `[translation] Dodaj prevod uvodnih vodičev v japonščino`

## Pogosti vzorci razvoja

### Delo z modeli Phi

**Nalaganje modelov:**
- Primeri uporabljajo različne okvire: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeli se običajno prenesejo iz Hugging Face, Azure ali GitHub Models
- Preverite združljivost modelov z vašo strojno opremo (CPU, GPU, NPU)

**Vzorce inferenc:**
- Generacija besedila: Večina primerov uporablja chat/instruct variante
- Vizija: Phi-3-vision in Phi-4-multimodal za razumevanje slik
- Zvok: Phi-4-multimodal podpira zvočne vnose
- Razmišljanje: Phi-4-reasoning variante za napredne naloge razmišljanja

### Opombe specifične za platformo

**Microsoft Foundry:**
- Zahteva naročnino na Azure in API ključe
- Glejte `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Na voljo brezplačna stopnja za testiranje
- Glejte `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokalna inferenca:**
- ONNX Runtime: Večplatformna, optimizirana inferenca
- Ollama: Enostavno lokalno upravljanje modelov (predkonfigurirano v razvojnem okolju)
- Apple MLX: Optimizirano za Apple Silicon

## Odpravljanje težav

### Pogoste težave

**Težave s pomnilnikom:**
- Phi modeli zahtevajo veliko RAM-a (zlasti vizualne/multimodalne variante)
- Uporabite kvantizirane modele za okolja z omejenimi viri
- Glejte `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikti odvisnosti:**
- Primeri v Pythonu imajo lahko specifične zahteve glede različic
- Uporabite virtualna okolja za vsak primer
- Preverite posamezne datoteke `requirements.txt`

**Napake pri prenosu modelov:**
- Veliki modeli lahko prekinejo povezavo pri počasnih povezavah
- Razmislite o uporabi oblačnih okolij (Codespaces, Azure)
- Preverite predpomnilnik Hugging Face: `~/.cache/huggingface/`

**Težave s projekti v .NET:**
- Prepričajte se, da je nameščen .NET 8.0 SDK
- Uporabite `dotnet restore` pred gradnjo
- Nekateri projekti imajo konfiguracije specifične za CUDA (Debug_Cuda)

**JavaScript/spletni primeri:**
- Uporabite Node.js 18+ za združljivost
- Počistite `node_modules` in ponovno namestite, če se pojavijo težave
- Preverite konzolo brskalnika za težave z združljivostjo WebGPU

### Pomoč

- **Discord:** Pridružite se skupnosti Microsoft Foundry na Discordu
- **GitHub Issues:** Prijavite napake in težave v repozitoriju
- **GitHub Discussions:** Postavljajte vprašanja in delite znanje

## Dodatni kontekst

### Odgovorna umetna inteligenca

Vsa uporaba modelov Phi naj sledi Microsoftovim načelom odgovorne umetne inteligence:
- Poštenost, zanesljivost, varnost
- Zasebnost in varnost  
- Vključenost, preglednost, odgovornost
- Uporabite Azure AI Content Safety za produkcijske aplikacije
- Glejte `/md/01.Introduction/01/01.AISafety.md`

### Prevajanja

- Podpora za več kot 50 jezikov prek avtomatiziranega GitHub Action
- Prevajanja v direktoriju `/translations/`
- Vzdržuje delovni tok co-op-translator
- Ročno ne urejajte prevedenih datotek (samodejno generirane)

### Prispevanje

- Upoštevajte smernice v `CONTRIBUTING.md`
- Strinjajte se s pogodbo o licenciranju prispevkov (CLA)
- Upoštevajte Microsoftov kodeks ravnanja za odprto kodo
- V zavezah ne vključujte varnostnih podatkov ali poverilnic

### Podpora za več jezikov

To je večjezični repozitorij s primeri v:
- **Python** - Delovni tokovi ML/AI, Jupyter zvezki, prilagajanje
- **C#/.NET** - Poslovne aplikacije, integracija ONNX Runtime
- **JavaScript** - Spletna umetna inteligenca, inferenca v brskalniku z WebGPU

Izberite jezik, ki najbolje ustreza vašemu primeru uporabe in cilju implementacije.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.