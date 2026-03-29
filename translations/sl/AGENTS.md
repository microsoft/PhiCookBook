# AGENTS.md

## Pregled projekta

PhiCookBook je obsežen repozitorij kuharske knjige, ki vsebuje praktične primere, vodiče in dokumentacijo za delo z družino majhnih jezikovnih modelov (SLM) podjetja Microsoft. Repozitorij prikazuje različne primere uporabe, vključno z inferenco, fino nastavitvijo, kvantizacijo, implementacijami RAG in multimodalnimi aplikacijami na različnih platformah in ogrodjih.

**Ključne tehnologije:**
- **Jeziki:** Python, C#/.NET, JavaScript/Node.js
- **Ogrodja:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Vrste modelov:** Phi-3, Phi-3.5, Phi-4 (besedilo, vid, multimodalni, različice za sklepanja)

**Struktura repozitorija:**
- `/code/` - Delujoči primeri kode in vzorčne implementacije
- `/md/` - Podrobna dokumentacija, vodiči in navodila  
- `/translations/` - Večjezični prevodi (50+ jezikov prek avtomatiziranega poteka)
- `/.devcontainer/` - Konfiguracija razvojnega kontejnerja (Python 3.12 z Ollama)

## Namestitev razvojnega okolja

### Uporaba GitHub Codespaces ali razvojnih kontejnerjev (priporočeno)

1. Odpri v GitHub Codespaces (najhitreje):
   - Klikni na značko "Open in GitHub Codespaces" v README
   - Kontejner se samodejno konfigurira s Python 3.12 in Ollama ter Phi-3

2. Odpri v VS Code razvojnem kontejnerju:
   - Uporabi značko "Open in Dev Containers" v README
   - Kontejner zahteva vsaj 16 GB pomnilnika gostitelja

### Lokalna namestitev

**Zahteve:**
- Python 3.12 ali novejši
- .NET 8.0 SDK (za C# primere)
- Node.js 18+ in npm (za JavaScript primere)
- Priporočen je najmanj 16 GB RAM

**Namestitev:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Za Python primere:**
Pomaknite se do posameznih map primerov in namestite odvisnosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # če datoteka requirements.txt obstaja
```

**Za .NET primere:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Za JavaScript/Web primere:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Zaženi razvojni strežnik
npm run build  # Zgradi za produkcijo
```

## Organizacija repozitorija

### Primeri kode (`/code/`)

- **01.Introduce/** - Osnovni uvodni in prvi vzorci
- **03.Finetuning/** in **04.Finetuning/** - Primeri fine tuninga z raznimi metodami
- **03.Inference/** - Primeri inferenc na različnih strojnih platformah (AIPC, MLX)
- **06.E2E/** - Vzorci celostnih aplikacij
- **07.Lab/** - Laboratorijske/eksperimentalne implementacije
- **08.RAG/** - Primeri generiranja z nadgradnjo pridobivanja (RAG)
- **09.UpdateSamples/** - Najnovejši posodobljeni primeri

### Dokumentacija (`/md/`)

- **01.Introduction/** - Uvodni vodiči, namestitev okolja, vodniki za platforme
- **02.Application/** - Primeri aplikacij, organizirani po vrstah (Besedilo, Koda, Vid, Zvok itd.)
- **02.QuickStart/** - Hitri začetni vodiči za Microsoft Foundry in GitHub Models
- **03.FineTuning/** - Dokumentacija in tutoriali za fine tuning
- **04.HOL/** - Hands-on laboratoriji (vključuje .NET primere)

### Formati datotek

- **Jupyter zvezki (`.ipynb`)** - Interaktivni Python tutoriali označeni z 📓 v README
- **Python skripte (`.py`)** - Samostojni Python primeri
- **C# projekti (`.csproj`, `.sln`)** - .NET aplikacije in primeri
- **JavaScript (`.js`, `package.json`)** - Spletni in Node.js primeri
- **Markdown (`.md`)** - Dokumentacija in vodiči

## Delo s primeri

### Zagon Jupyter zvezkov

Večina primerov je na voljo kot Jupyter zvezki:
```bash
pip install jupyter notebook
jupyter notebook  # Odpre brskalniški vmesnik
# Premakni se do želene .ipynb datoteke
```

### Zagon Python skript

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Zagon .NET primerov

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ali zgradi celotno rešitev:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Zagon JavaScript/Web primerov

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Razvoj s hkratnim nalaganjem sprememb
```

## Testiranje

Repozitorij vsebuje primere kode in vodiče namesto tradicionalnega programska projekta z enotnimi testi. Validacija običajno poteka z:

1. **Zagon primerov** - Vsak primer mora teči brez napak
2. **Preverjanjem izhodov** - Preveri, da so odzivi modela ustrezni
3. **Sledenjem tutorialom** - Korak-po-korak vodiči morajo delovati kot opisano

**Pogosti pristop validacije:**
- Testiranje delovanja primerov v ciljnem okolju
- Preverjanje pravilne namestitve odvisnosti
- Preverjanje, da se modeli uspešno prenesejo/naložijo
- Potrditev, da pričakovano vedenje ustreza dokumentaciji

## Slog kode in konvencije

### Splošna navodila

- Primeri naj bodo jasni, dobro komentirani in izobraževalni
- Sledi jezikovno specifičnim konvencijam (PEP 8 za Python, C# standardi za .NET)
- Primeri naj se osredotočijo na predstavitev specifičnih zmogljivosti Phi modelov
- Vključi komentarje, ki pojasnjujejo ključne koncepte in parametre modela

### Standardi dokumentacije

**Formatiranje URL-jev:**
- Uporabljaj format `[text](../../url)` brez dodatnih presledkov
- Relativne povezave: uporabljaj `./` za trenutno mapo, `../` za nadrejeno
- Brez državnih lokal za URL-je (izogibaj se `/en-us/`, `/en/`)

**Slike:**
- Shranjuj vse slike v mapo `/imgs/`
- Imeti morajo opisna imena z angleškimi znaki, številkami in pomišljaji
- Primer: `phi-3-architecture.png`

**Markdown datoteke:**
- Navajaj dejanske delujoče primere v mapi `/code/`
- Dokumentacijo vzdržuj usklajeno s spremembami kode
- Uporabi emoji 📓 za označitev povezav do Jupyter zvezkov v README

### Organizacija datotek

- Primeri kode v `/code/` organizirani po temah/funkcijah
- Dokumentacija v `/md/` zrcali strukturo kode, kjer je to mogoče
- Sorodne datoteke (zvezki, skripte, konfiguracije) naj bodo skupaj v podmapah

## Navodila za pull requeste

### Pred oddajo

1. **Razvij fork repozitorija** na svoj račun
2. **Loči PR-je po tipu:**
   - Popravki napak v enem PR-ju
   - Posodobitve dokumentacije v drugem
   - Novi primeri v ločenih PR-jih
   - Popravki tipk so lahko združeni

3. **Reševanje konfliktov združevanja:**
   - Posodobi lokalno vejo `main` pred spremembami
   - Pogosto sinhroniziraj z zgornjim repozitorijem

4. **Prevajalski PR-ji:**
   - Morajo vključevati prevode za VSE datoteke v mapi
   - Ohrani dosledno strukturo z izvirnim jezikom

### Zahtevane kontrole

PR-ji samodejno zaženeta GitHub delovne procese, ki preverjajo:

1. **Validacija relativnih poti** - Vse notranje povezave morajo delovati
   - Testiraj povezave lokalno: Ctrl+Click v VS Code
   - Uporabi predloge poti iz VS Code (`./` ali `../`)

2. **Preverjanje jezika v URL-jih** - Spletne URL povezave naj ne vsebujejo državnih lokalizacij
   - Odstrani `/en-us/`, `/en/` ali druge jezikovne kode
   - Uporabljaj generične mednarodne URL-je

3. **Preverjanje pokvarjenih URL-jev** - Vsi URL-ji morajo vračati status 200
   - Pred oddajo preveri dostopnost povezav
   - Opomba: Nekatere napake so lahko posledica omrežnih omejitev

### Format naslova PR

```
[component] Brief description
```

Primeri:
- `[docs] Dodaj tutorial za inferenco Phi-4`
- `[code] Popravi primer integracije ONNX Runtime`
- `[translation] Dodaj japonski prevod uvodnih vodičev`

## Pogosti razvojni vzorci

### Delo s Phi modeli

**Nalaganje modelov:**
- Primeri uporabljajo različna ogrodja: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeli so ponavadi preneseni z Hugging Face, Azure ali GitHub Models
- Preveri združljivost modela s tvojim strojno-opremo (CPU, GPU, NPU)

**Vzorce inferenc:**
- Generiranje besedila: Večina primerov uporablja klepet/instruction variante
- Vid: Phi-3-vision in Phi-4-multimodal za razumevanje slik
- Zvok: Phi-4-multimodal podpira avdio vhode
- Sklepanje: Phi-4-reasoning različice za napredne naloge sklepanja

### Platformno specifične opombe

**Microsoft Foundry:**
- Zahteva Azure naročnino in API ključe
- Glej `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Brezplačni sloj za testiranje
- Glej `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokalna inferenca:**
- ONNX Runtime: večplatformska, optimizirana inferenca
- Ollama: enostavno lokalno upravljanje modelov (prednastavljeno v razvojnem kontejnerju)
- Apple MLX: optimizirano za Apple Silicon

## Odpravljanje težav

### Pogoste težave

**Težave s pomnilnikom:**
- Phi modeli zahtevajo veliko RAM-a (še posebej vid/multimodalne različice)
- Uporabi kvantizirane modele za okolja z omejenimi viri
- Glej `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikti odvisnosti:**
- Python primeri imajo lahko specifične zahteve po različicah
- Uporabljaj virtualna okolja za vsak primer posebej
- Preveri posamezne datoteke `requirements.txt`

**Napake pri prenosu modela:**
- Veliki modeli se lahko zaradi počasne povezave prekinejo
- Razmisli o uporabi oblačnih okolij (Codespaces, Azure)
- Preveri predpomnilnik Hugging Face: `~/.cache/huggingface/`

**Težave s .NET projekti:**
- Poskrbi, da je nameščen .NET 8.0 SDK
- Uporabi `dotnet restore` pred gradnjo
- Nekateri projekti imajo konfiguracije specifične za CUDA (Debug_Cuda)

**JavaScript/Web primeri:**
- Za kompatibilnost uporabljaj Node.js 18+
- Počisti `node_modules` in ponovno namesti, če težave obstajajo
- Preveri konzolo brskalnika za težave z WebGPU

### Iskanje pomoči

- **Discord:** Pridruži se Microsoft Foundry Community Discordu
- **GitHub Issues:** Prijavljaj napake in težave v repozitorij
- **GitHub Discussions:** Postavljaj vprašanja in deli znanje

## Dodatni kontekst

### Odgovorna AI

Vsa uporaba Phi modelov naj sledi načelom odgovorne umetne inteligence podjetja Microsoft:
- Poštenost, zanesljivost, varnost
- Zasebnost in varovanje podatkov  
- Vključenost, preglednost, odgovornost
- Za produkcijske aplikacije uporabljaj Azure AI Content Safety
- Glej `/md/01.Introduction/01/01.AISafety.md`

### Prevodi

- Podprto več kot 50 jezikov prek avtomatiziranega GitHub Action
- Prevodi v mapi `/translations/`
- Vzdržujejo jih v delovnem toku co-op-translator
- Ne urejaj ročno prevedenih datotek (samodejno generirane)

### Prispevki

- Sledi navodilom v `CONTRIBUTING.md`
- Strinjaj se s Pogodbo o licenciranju prispevkov (CLA)
- Drži se Microsoftovega kodeksa ravnanja za odprtokodno kodo
- Vključi varnost in poverilnice izključno zunaj commitov

### Podpora za več jezikov

To je poliglotski repozitorij z vzorci v:
- **Python** - ML/AI poteki, Jupyter zvezki, fine tuning
- **C#/.NET** - Podjetniške aplikacije, integracija ONNX Runtime
- **JavaScript** - Spletna umetna inteligenca, inferenca v brskalniku z WebGPU

Izberi jezik, ki najbolj ustreza tvojemu primeru uporabe in ciljni implementaciji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->