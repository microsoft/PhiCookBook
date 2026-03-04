# AGENTS.md

## Prehľad projektu

PhiCookBook je komplexný repozitár kuchárskej knihy obsahujúci praktické príklady, tutoriály a dokumentáciu na prácu s rodinou malých jazykových modelov (SLM) od Microsoftu. Repozitár demonštruje rôzne použitia vrátane inferencie, jemného doladenia, kvantizácie, implementácií RAG a multimodálnych aplikácií na rôznych platformách a rámcoch.

**Kľúčové technológie:**
- **Jazyky:** Python, C#/.NET, JavaScript/Node.js
- **Rámce:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformy:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Typy modelov:** Phi-3, Phi-3.5, Phi-4 (textové, vizuálne, multimodálne, varianty na uvažovanie)

**Štruktúra repozitára:**
- `/code/` - Pracovné príklady kódu a ukážkové implementácie
- `/md/` - Podrobná dokumentácia, tutoriály a návody  
- `/translations/` - Preklady do viacerých jazykov (50+ jazykov prostredníctvom automatizovaného pracovného toku)
- `/.devcontainer/` - Konfigurácia vývojového kontajnera (Python 3.12 s Ollama)

## Nastavenie vývojového prostredia

### Použitie GitHub Codespaces alebo vývojových kontajnerov (odporúčané)

1. Otvorte v GitHub Codespaces (najrýchlejšie):
   - Kliknite na odznak "Open in GitHub Codespaces" v README
   - Kontajner sa automaticky nakonfiguruje s Python 3.12 a Ollama s Phi-3

2. Otvorte vo VS Code Dev Containers:
   - Použite odznak "Open in Dev Containers" z README
   - Kontajner vyžaduje minimálne 16GB pamäte hostiteľa

### Lokálne nastavenie

**Predpoklady:**
- Python 3.12 alebo novší
- .NET 8.0 SDK (pre príklady v C#)
- Node.js 18+ a npm (pre príklady v JavaScripte)
- Odporúča sa minimálne 16GB RAM

**Inštalácia:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pre Python príklady:**
Prejdite do konkrétnych adresárov s príkladmi a nainštalujte závislosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Pre .NET príklady:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Pre JavaScript/Web príklady:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organizácia repozitára

### Príklady kódu (`/code/`)

- **01.Introduce/** - Základné úvody a ukážky na začiatok
- **03.Finetuning/** a **04.Finetuning/** - Príklady jemného doladenia rôznymi metódami
- **03.Inference/** - Príklady inferencie na rôznom hardvéri (AIPC, MLX)
- **06.E2E/** - Ukážky aplikácií od začiatku do konca
- **07.Lab/** - Laboratórne/experimentálne implementácie
- **08.RAG/** - Ukážky generovania s podporou vyhľadávania
- **09.UpdateSamples/** - Najnovšie aktualizované ukážky

### Dokumentácia (`/md/`)

- **01.Introduction/** - Úvodné príručky, nastavenie prostredia, návody na platformy
- **02.Application/** - Ukážky aplikácií organizované podľa typu (Text, Kód, Vizuál, Audio, atď.)
- **02.QuickStart/** - Rýchle návody pre Microsoft Foundry a GitHub Models
- **03.FineTuning/** - Dokumentácia a tutoriály k jemnému doladeniu
- **04.HOL/** - Praktické laboratóriá (vrátane príkladov v .NET)

### Formáty súborov

- **Jupyter Notebooks (`.ipynb`)** - Interaktívne Python tutoriály označené 📓 v README
- **Python Scripts (`.py`)** - Samostatné Python príklady
- **C# Projects (`.csproj`, `.sln`)** - .NET aplikácie a ukážky
- **JavaScript (`.js`, `package.json`)** - Webové a Node.js príklady
- **Markdown (`.md`)** - Dokumentácia a návody

## Práca s príkladmi

### Spúšťanie Jupyter Notebooks

Väčšina príkladov je poskytovaná ako Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Spúšťanie Python skriptov

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Spúšťanie .NET príkladov

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Alebo zostavte celé riešenie:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Spúšťanie JavaScript/Web príkladov

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testovanie

Tento repozitár obsahuje ukážkový kód a tutoriály, nie tradičný softvérový projekt s jednotkovými testami. Validácia sa zvyčajne vykonáva:

1. **Spúšťaním príkladov** - Každý príklad by mal byť vykonaný bez chýb
2. **Overovaním výstupov** - Skontrolujte, či sú odpovede modelu vhodné
3. **Nasledovaním tutoriálov** - Návody krok za krokom by mali fungovať podľa dokumentácie

**Bežný prístup k validácii:**
- Testujte vykonanie príkladov v cieľovom prostredí
- Overte správnu inštaláciu závislostí
- Skontrolujte, či sa modely správne stiahnu/nahrajú
- Potvrďte, že očakávané správanie zodpovedá dokumentácii

## Štýl kódu a konvencie

### Všeobecné pokyny

- Príklady by mali byť jasné, dobre komentované a edukatívne
- Dodržiavajte konvencie špecifické pre jazyk (PEP 8 pre Python, štandardy C# pre .NET)
- Udržujte príklady zamerané na demonštráciu konkrétnych schopností modelov Phi
- Zahrňte komentáre vysvetľujúce kľúčové koncepty a parametre špecifické pre model

### Štandardy dokumentácie

**Formátovanie URL:**
- Používajte formát `[text](../../url)` bez extra medzier
- Relatívne odkazy: Používajte `./` pre aktuálny adresár, `../` pre nadradený
- Nepoužívajte krajiny špecifické lokály v URL (vyhnite sa `/en-us/`, `/en/`)

**Obrázky:**
- Ukladajte všetky obrázky do adresára `/imgs/`
- Používajte popisné názvy s anglickými znakmi, číslami a pomlčkami
- Príklad: `phi-3-architecture.png`

**Markdown súbory:**
- Odkazujte na skutočné pracovné príklady v adresári `/code/`
- Udržujte dokumentáciu synchronizovanú so zmenami kódu
- Používajte emoji 📓 na označenie odkazov na Jupyter notebooks v README

### Organizácia súborov

- Príklady kódu v `/code/` organizované podľa témy/funkcie
- Dokumentácia v `/md/` zrkadlí štruktúru kódu, ak je to možné
- Udržujte súvisiace súbory (notebooky, skripty, konfigurácie) spolu v podadresároch

## Pokyny pre Pull Requesty

### Pred odoslaním

1. **Forknite repozitár** do svojho účtu
2. **Oddelené PR podľa typu:**
   - Opravy chýb v jednom PR
   - Aktualizácie dokumentácie v inom
   - Nové príklady v samostatných PR
   - Opravy preklepov môžu byť kombinované

3. **Riešenie konfliktov pri zlúčení:**
   - Aktualizujte svoju lokálnu vetvu `main` pred vykonaním zmien
   - Často synchronizujte s upstream

4. **Prekladové PR:**
   - Musia obsahovať preklady pre VŠETKY súbory v priečinku
   - Zachovajte konzistentnú štruktúru s originálnym jazykom

### Požadované kontroly

PR automaticky spúšťajú GitHub pracovné toky na validáciu:

1. **Validácia relatívnych ciest** - Všetky interné odkazy musia fungovať
   - Testujte odkazy lokálne: Ctrl+Klik vo VS Code
   - Používajte návrhy ciest z VS Code (`./` alebo `../`)

2. **Kontrola lokálov URL** - Webové URL nesmú obsahovať jazykové kódy
   - Odstráňte `/en-us/`, `/en/` alebo iné jazykové kódy
   - Používajte generické medzinárodné URL

3. **Kontrola nefunkčných URL** - Všetky URL musia vrátiť stav 200
   - Overte, že odkazy sú prístupné pred odoslaním
   - Poznámka: Niektoré zlyhania môžu byť spôsobené sieťovými obmedzeniami

### Formát názvu PR

```
[component] Brief description
```

Príklady:
- `[docs] Pridať tutoriál inferencie Phi-4`
- `[code] Opraviť príklad integrácie ONNX Runtime`
- `[translation] Pridať japonský preklad úvodných príručiek`

## Bežné vývojové vzory

### Práca s modelmi Phi

**Načítanie modelov:**
- Príklady používajú rôzne rámce: Transformers, ONNX Runtime, MLX, OpenVINO
- Modely sa zvyčajne sťahujú z Hugging Face, Azure alebo GitHub Models
- Skontrolujte kompatibilitu modelov s vaším hardvérom (CPU, GPU, NPU)

**Vzory inferencie:**
- Generovanie textu: Väčšina príkladov používa chat/instruct varianty
- Vizuálne: Phi-3-vision a Phi-4-multimodal na porozumenie obrázkov
- Audio: Phi-4-multimodal podporuje audio vstupy
- Uvažovanie: Phi-4-reasoning varianty na pokročilé úlohy uvažovania

### Poznámky k špecifickým platformám

**Microsoft Foundry:**
- Vyžaduje predplatné Azure a API kľúče
- Pozrite si `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- K dispozícii bezplatná úroveň na testovanie
- Pozrite si `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokálna inferencia:**
- ONNX Runtime: Cross-platform, optimalizovaná inferencia
- Ollama: Jednoduchá lokálna správa modelov (predkonfigurované vo vývojovom kontajneri)
- Apple MLX: Optimalizované pre Apple Silicon

## Riešenie problémov

### Bežné problémy

**Problémy s pamäťou:**
- Modely Phi vyžadujú značné množstvo RAM (najmä vizuálne/multimodálne varianty)
- Používajte kvantizované modely pre prostredia s obmedzenými zdrojmi
- Pozrite si `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikty závislostí:**
- Python príklady môžu mať špecifické požiadavky na verzie
- Používajte virtuálne prostredia pre každý príklad
- Skontrolujte jednotlivé súbory `requirements.txt`

**Zlyhania pri sťahovaní modelov:**
- Veľké modely môžu na pomalých pripojeniach vypršať
- Zvážte použitie cloudových prostredí (Codespaces, Azure)
- Skontrolujte cache Hugging Face: `~/.cache/huggingface/`

**Problémy s .NET projektmi:**
- Uistite sa, že máte nainštalovaný .NET 8.0 SDK
- Použite `dotnet restore` pred zostavením
- Niektoré projekty majú špecifické konfigurácie pre CUDA (Debug_Cuda)

**JavaScript/Web príklady:**
- Použite Node.js 18+ pre kompatibilitu
- Vymažte `node_modules` a znovu nainštalujte, ak sa vyskytnú problémy
- Skontrolujte konzolu prehliadača pre problémy s kompatibilitou WebGPU

### Získanie pomoci

- **Discord:** Pripojte sa k Microsoft Foundry Community Discord
- **GitHub Issues:** Nahláste chyby a problémy v repozitári
- **GitHub Discussions:** Kladenie otázok a zdieľanie poznatkov

## Dodatočný kontext

### Zodpovedná AI

Všetko používanie modelov Phi by malo dodržiavať princípy zodpovednej AI od Microsoftu:
- Spravodlivosť, spoľahlivosť, bezpečnosť
- Ochrana súkromia a bezpečnosť  
- Inkluzívnosť, transparentnosť, zodpovednosť
- Používajte Azure AI Content Safety pre produkčné aplikácie
- Pozrite si `/md/01.Introduction/01/01.AISafety.md`

### Preklady

- Podpora 50+ jazykov prostredníctvom automatizovanej GitHub akcie
- Preklady v adresári `/translations/`
- Udržiavané pracovným tokom co-op-translator
- Manuálne neupravujte preložené súbory (automaticky generované)

### Prispievanie

- Dodržiavajte pokyny v `CONTRIBUTING.md`
- Súhlaste s Contributor License Agreement (CLA)
- Dodržiavajte Microsoft Open Source Code of Conduct
- Uchovávajte bezpečnosť a poverenia mimo commitov

### Podpora viacerých jazykov

Toto je polyglot repozitár s príkladmi v:
- **Python** - ML/AI pracovné postupy, Jupyter notebooks, jemné doladenie
- **C#/.NET** - Podnikové aplikácie, integrácia ONNX Runtime
- **JavaScript** - Webové AI, inferencia v prehliadači s WebGPU

Vyberte jazyk, ktorý najlepšie vyhovuje vášmu použitiu a cieľu nasadenia.

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.