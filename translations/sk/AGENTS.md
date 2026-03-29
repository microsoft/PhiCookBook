# AGENTS.md

## Prehľad projektu

PhiCookBook je komplexné repozitár kuchárskych receptov obsahujúci praktické príklady, návody a dokumentáciu pre prácu s rodinou malých jazykových modelov spoločnosti Microsoft Phi (SLMs). Repozitár demonštruje rôzne použitia vrátane inferencie, doladenia, kvantizácie, implementácií RAG a multimodálnych aplikácií naprieč rôznymi platformami a rámcami.

**Kľúčové technológie:**
- **Jazyky:** Python, C#/.NET, JavaScript/Node.js
- **Rámce:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformy:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Typy modelov:** Phi-3, Phi-3.5, Phi-4 (text, videnie, multimodálne, varianty pre uvažovanie)

**Štruktúra repozitára:**
- `/code/` - Pracovné príklady kódu a vzorové implementácie
- `/md/` - Podrobná dokumentácia, návody a sprievodcovia  
- `/translations/` - Viacjazyčné preklady (viac ako 50 jazykov cez automatizovaný workflow)
- `/.devcontainer/` - Konfigurácia vývojového kontajnera (Python 3.12 s Ollama)

## Nastavenie vývojového prostredia

### Použitie GitHub Codespaces alebo Dev Containers (odporúčané)

1. Otvorte v GitHub Codespaces (najrýchlejšie):
   - Kliknite na odznak „Open in GitHub Codespaces“ v README
   - Kontajner sa automaticky nakonfiguruje s Python 3.12 a Ollama s Phi-3

2. Otvorte vo VS Code Dev Containers:
   - Použite odznak „Open in Dev Containers“ z README
   - Kontajner vyžaduje minimálne 16 GB pamäte hostiteľa

### Lokálne nastavenie

**Predpoklady:**
- Python 3.12 alebo novší
- .NET 8.0 SDK (pre príklady v C#)
- Node.js 18+ a npm (pre príklady v JavaScripte)
- Odporúča sa minimálne 16 GB RAM

**Inštalácia:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pre príklady v Pythone:**
Prejdite do konkrétnych adresárov príkladov a nainštalujte závislosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # ak existuje requirements.txt
```

**Pre príklady v .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Pre príklady v JavaScripte/webe:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Spustiť vývojový server
npm run build  # Vytvoriť zostavu pre produkciu
```

## Organizácia repozitára

### Príklady kódu (`/code/`)

- **01.Introduce/** - Základné úvody a vzorové štarty
- **03.Finetuning/** a **04.Finetuning/** - Príklady doladenia s rôznymi metódami
- **03.Inference/** - Príklady inferencie na rôznom hardvéri (AIPC, MLX)
- **06.E2E/** - Vzorky end-to-end aplikácií
- **07.Lab/** - Laboratórne/experimentálne implementácie
- **08.RAG/** - Príklady Retrieval-Augmented Generation
- **09.UpdateSamples/** - Najnovšie aktualizované vzorky

### Dokumentácia (`/md/`)

- **01.Introduction/** - Úvodné návody, nastavenie prostredia, sprievodcovia platformami
- **02.Application/** - Vzorky aplikácií organizované podľa typu (Text, Kód, Videnie, Audio, atď.)
- **02.QuickStart/** - Rýchle štarty pre Microsoft Foundry a GitHub Models
- **03.FineTuning/** - Dokumentácia a návody na doladenie
- **04.HOL/** - Hands-on laboratóriá (vrátane príkladov v .NET)

### Formáty súborov

- **Jupyter Notebooks (`.ipynb`)** - Interaktívne návody v Pythone označené 📓 v README
- **Python skripty (`.py`)** - Samostatné Python príklady
- **C# projekty (`.csproj`, `.sln`)** - .NET aplikácie a vzorky
- **JavaScript (`.js`, `package.json`)** - Webové a Node.js príklady
- **Markdown (`.md`)** - Dokumentácia a návody

## Práca s príkladmi

### Spustenie Jupyter Notebookov

Väčšina príkladov je dostupná ako Jupyter notebooky:
```bash
pip install jupyter notebook
jupyter notebook  # Otvára rozhranie prehliadača
# Prejdite na požadovaný súbor .ipynb
```

### Spustenie Python skriptov

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Spustenie .NET príkladov

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Alebo zostavte celé riešenie:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Spustenie JavaScript/Web príkladov

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Vývoj s automatickým obnovením
```

## Testovanie

Tento repozitár obsahuje príkladový kód a návody namiesto tradičného softvérového projektu s jednotkovými testami. Overovanie prebieha typicky:

1. **Spustením príkladov** - Každý príklad by mal bežať bez chýb
2. **Overením výsledkov** - Skontrolujte, či sú odpovede modelu primerané
3. **Sledovaním návodov** - Sprievodcovia krok za krokom by mali fungovať podľa dokumentácie

**Bežný prístup k overovaniu:**
- Testujte spustenie príkladov v cieľovom prostredí
- Overte správnu inštaláciu závislostí
- Skontrolujte úspešné stiahnutie/nahratie modelov
- Potvrďte, že očakávané správanie zodpovedá dokumentácii

## Štýl kódu a konvencie

### Všeobecné pokyny

- Príklady by mali byť jasné, dobre komentované a vzdelávacie
- Dodržiavajte jazykovo špecifické konvencie (PEP 8 pre Python, štandardy C# pre .NET)
- Zamerajte príklady na demonštráciu špecifických schopností modelov Phi
- Zahrňte komentáre vysvetľujúce kľúčové koncepty a parametre špecifické pre model

### Štandardy dokumentácie

**Formátovanie URL:**
- Používajte formát `[text](../../url)` bez medzier navyše
- Relatívne odkazy: použite `./` pre aktuálny adresár, `../` pre nadradený
- Nepoužívajte krajinné lokály v URL (vyhnite sa `/en-us/`, `/en/`)

**Obrázky:**
- Ukladajte všetky obrázky v adresári `/imgs/`
- Používajte popisné názvy s anglickými znakmi, číslicami a pomlčkami
- Príklad: `phi-3-architecture.png`

**Markdown súbory:**
- Odkazujte na skutočné fungujúce príklady v adresári `/code/`
- Udržiavajte dokumentáciu synchronizovanú so zmenami kódu
- Používajte emoji 📓 na označenie odkazov na Jupyter notebooky v README

### Organizácia súborov

- Príklady kódu v `/code/` usporiadané podľa témy/funkcie
- Dokumentácia v `/md/` kopíruje štruktúru kódu, ak to je vhodné
- Uchovávajte súvisiace súbory (notebooky, skripty, konfigurácie) spolu v podadresároch

## Pokyny pre pull requesty

### Pred odoslaním

1. **Vytvorte fork** repozitára do vášho účtu
2. **Rozdeľte PR podľa typu:**
   - Opravy chýb v jednom PR
   - Aktualizácie dokumentácie v inom
   - Nové príklady v samostatných PR
   - Opravy preklepov možno spojiť

3. **Riešte konflikty zlúčenia:**
   - Aktualizujte lokálnu vetvu `main` pred zmenami
   - Často synchronizujte s upstreamom

4. **PR s prekladmi:**
   - Musia obsahovať preklady pre VŠETKY súbory vo foldri
   - Zachovajte konzistentnú štruktúru s originálnym jazykom

### Povinné kontroly

PRy automaticky spúšťajú GitHub workflow na validáciu:

1. **Overenie relatívnych ciest** - Všetky interné odkazy musia fungovať
   - Testujte odkazy lokálne: Ctrl+Klik vo VS Code
   - Používajte návrhy ciest od VS Code (`./` alebo `../`)

2. **Kontrola URL lokalizácie** - Webové URL nesmú obsahovať krajinné lokály
   - Odstraňte `/en-us/`, `/en/` alebo iné jazykové kódy
   - Používajte generické medzinárodné URL

3. **Kontrola nefunkčných URL** - Všetky URL musia vracať stav 200
   - Overte prístupnosť odkazov pred odoslaním
   - Poznámka: Niektoré zlyhania môžu byť spôsobené sieťovými obmedzeniami

### Formát názvu PR

```
[component] Brief description
```

Príklady:
- `[docs] Pridanie návodu na inferenciu Phi-4`
- `[code] Oprava príkladu integrácie ONNX Runtime`
- `[translation] Pridanie japonského prekladu úvodných návodov`

## Bežné vývojové vzory

### Práca s Phi modelmi

**Načítanie modelov:**
- Príklady používajú rôzne rámce: Transformers, ONNX Runtime, MLX, OpenVINO
- Modely sa zvyčajne sťahujú z Hugging Face, Azure alebo GitHub Models
- Skontrolujte kompatibilitu modelu s vaším hardvérom (CPU, GPU, NPU)

**Vzory inferencie:**
- Generovanie textu: väčšina príkladov používa chat/instruct varianty
- Vízia: Phi-3-vision a Phi-4-multimodal pre pochopenie obrazu
- Audio: Phi-4-multimodal podporuje audio vstupy
- Uvažovanie: Phi-4-reasoning varianty pre pokročilé uvažovacie úlohy

### Poznámky k platformám

**Microsoft Foundry:**
- Vyžaduje predplatné Azure a API kľúče
- Pozri `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- K dispozícii bezplatná vrstva pre testovanie
- Pozri `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokálna inferencia:**
- ONNX Runtime: multiplatformová, optimalizovaná inferencia
- Ollama: jednoduchá lokálna správa modelov (predkonfigurované v dev kontejnery)
- Apple MLX: optimalizované pre Apple Silicon

## Riešenie problémov

### Bežné problémy

**Problémy s pamäťou:**
- Phi modely vyžadujú značnú RAM (najmä varianty pre víziu a multimodálne)
- Používajte kvantizované modely pre prostredia s obmedzenými zdrojmi
- Pozri `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikty závislostí:**
- Python príklady môžu mať špecifické požiadavky na verzie
- Používajte virtuálne prostredia pre každý príklad
- Kontrolujte individuálne súbory `requirements.txt`

**Zlyhanie sťahovania modelu:**
- Veľké modely môžu vypršať na pomalých pripojeniach
- Zvážte použitie cloud prostredí (Codespaces, Azure)
- Skontrolujte cache Hugging Face: `~/.cache/huggingface/`

**Problémy s .NET projektom:**
- Uistite sa, že .NET 8.0 SDK je nainštalovaný
- Použite `dotnet restore` pred zostavením
- Niektoré projekty majú konfigurácie špecifické pre CUDA (Debug_Cuda)

**JavaScript/Web príklady:**
- Používajte Node.js 18+ pre kompatibilitu
- Vymažte `node_modules` a preinštalujte, ak problémy pretrvávajú
- Skontrolujte konzolu prehliadača pre problémy s WebGPU

### Získanie pomoci

- **Discord:** Pripojte sa k Microsoft Foundry Community Discord
- **GitHub Issues:** Nahláste chyby a problémy v repozitári
- **GitHub Discussions:** Pýtajte sa otázky a zdieľajte vedomosti

## Dodatočný kontext

### Zodpovedné AI

Všetko používanie modelov Phi by malo nasledovať princípy zodpovedného AI spoločnosti Microsoft:
- Spravodlivosť, spoľahlivosť, bezpečnosť
- Ochrana súkromia a zabezpečenie  
- Inkluzívnosť, transparentnosť, zodpovednosť
- Používajte Azure AI Content Safety pre produkčné aplikácie
- Pozri `/md/01.Introduction/01/01.AISafety.md`

### Preklady

- Podpora viac ako 50 jazykov cez automatizovaný GitHub Action
- Preklady v adresári `/translations/`
- Udržiava ich workflow co-op-translator
- Needitujte manuálne preložené súbory (automaticky generované)

### Príspevky

- Dodržiavajte pokyny v `CONTRIBUTING.md`
- Súhlas s Contributor License Agreement (CLA)
- Dodržiavajte Microsoft Open Source Code of Conduct
- Neposielajte bezpečnostné údaje a prihlasovacie údaje v commitoch

### Podpora viacerých jazykov

Toto je polyglot repozitár s príkladmi v:
- **Python** - ML/AI workflowy, Jupyter notebooky, doladenie
- **C#/.NET** - Podnikové aplikácie, integrácia ONNX Runtime
- **JavaScript** - Webové AI, inferencia prehliadača s WebGPU

Vyberte jazyk, ktorý najlepšie vyhovuje vášmu prípadu použitia a nasadeniu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho originálnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z používania tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->