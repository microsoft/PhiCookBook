<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T11:00:51+00:00",
  "source_file": "AGENTS.md",
  "language_code": "cs"
}
-->
# AGENTS.md

## Přehled projektu

PhiCookBook je komplexní úložiště kuchařek obsahující praktické příklady, tutoriály a dokumentaci pro práci s rodinou malých jazykových modelů (SLMs) od Microsoftu Phi. Úložiště demonstruje různé případy použití, včetně inferencí, jemného ladění, kvantizace, implementací RAG a multimodálních aplikací na různých platformách a v různých rámcích.

**Klíčové technologie:**
- **Jazyky:** Python, C#/.NET, JavaScript/Node.js
- **Rámce:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformy:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Typy modelů:** Phi-3, Phi-3.5, Phi-4 (textové, vizuální, multimodální, varianty pro uvažování)

**Struktura úložiště:**
- `/code/` - Funkční příklady kódu a ukázkové implementace
- `/md/` - Podrobná dokumentace, tutoriály a návody  
- `/translations/` - Překlady do více jazyků (50+ jazyků prostřednictvím automatizovaného workflow)
- `/.devcontainer/` - Konfigurace vývojového kontejneru (Python 3.12 s Ollama)

## Nastavení vývojového prostředí

### Použití GitHub Codespaces nebo vývojových kontejnerů (doporučeno)

1. Otevřete v GitHub Codespaces (nejrychlejší):
   - Klikněte na odznak "Open in GitHub Codespaces" v README
   - Kontejner se automaticky nakonfiguruje s Pythonem 3.12 a Ollama s Phi-3

2. Otevřete ve vývojových kontejnerech VS Code:
   - Použijte odznak "Open in Dev Containers" z README
   - Kontejner vyžaduje minimálně 16 GB paměti hostitele

### Lokální nastavení

**Předpoklady:**
- Python 3.12 nebo novější
- .NET 8.0 SDK (pro příklady v C#)
- Node.js 18+ a npm (pro příklady v JavaScriptu)
- Doporučeno minimálně 16 GB RAM

**Instalace:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pro příklady v Pythonu:**
Přejděte do konkrétních adresářů s příklady a nainstalujte závislosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Pro příklady v .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Pro příklady v JavaScriptu/webu:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organizace úložiště

### Příklady kódu (`/code/`)

- **01.Introduce/** - Základní úvod a ukázkové příklady pro začátek
- **03.Finetuning/** a **04.Finetuning/** - Příklady jemného ladění různými metodami
- **03.Inference/** - Příklady inferencí na různém hardwaru (AIPC, MLX)
- **06.E2E/** - Ukázky aplikací od začátku do konce
- **07.Lab/** - Laboratorní/experimentální implementace
- **08.RAG/** - Ukázky generování s podporou vyhledávání
- **09.UpdateSamples/** - Nejnovější aktualizované příklady

### Dokumentace (`/md/`)

- **01.Introduction/** - Úvodní průvodce, nastavení prostředí, průvodce platformami
- **02.Application/** - Ukázky aplikací organizované podle typu (Text, Kód, Vize, Audio, atd.)
- **02.QuickStart/** - Rychlé startovací průvodce pro Azure AI Foundry a GitHub Models
- **03.FineTuning/** - Dokumentace a tutoriály k jemnému ladění
- **04.HOL/** - Praktické laboratoře (včetně příkladů v .NET)

### Formáty souborů

- **Jupyter Notebooks (`.ipynb`)** - Interaktivní tutoriály v Pythonu označené 📓 v README
- **Python Scripts (`.py`)** - Samostatné příklady v Pythonu
- **C# Projects (`.csproj`, `.sln`)** - Aplikace a příklady v .NET
- **JavaScript (`.js`, `package.json`)** - Webové a Node.js příklady
- **Markdown (`.md`)** - Dokumentace a průvodce

## Práce s příklady

### Spouštění Jupyter Notebooks

Většina příkladů je poskytována jako Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Spouštění Python skriptů

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Spouštění příkladů v .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Nebo sestavte celé řešení:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Spouštění příkladů v JavaScriptu/webu

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testování

Toto úložiště obsahuje ukázkový kód a tutoriály, spíše než tradiční softwarový projekt s jednotkovými testy. Validace se obvykle provádí:

1. **Spouštěním příkladů** - Každý příklad by měl být spuštěn bez chyb
2. **Ověřením výstupů** - Zkontrolujte, zda jsou odpovědi modelu vhodné
3. **Dodržováním tutoriálů** - Průvodce krok za krokem by měl fungovat podle dokumentace

**Běžný přístup k validaci:**
- Testování spuštění příkladů v cílovém prostředí
- Ověření správné instalace závislostí
- Kontrola, zda se modely správně stahují/nahrávají
- Potvrzení, že očekávané chování odpovídá dokumentaci

## Styl kódu a konvence

### Obecné pokyny

- Příklady by měly být jasné, dobře komentované a vzdělávací
- Dodržujte konvence specifické pro jazyk (PEP 8 pro Python, standardy C# pro .NET)
- Udržujte příklady zaměřené na demonstraci konkrétních schopností modelů Phi
- Zahrňte komentáře vysvětlující klíčové koncepty a parametry specifické pro modely

### Standardy dokumentace

**Formátování URL:**
- Používejte formát `[text](../../url)` bez dalších mezer
- Relativní odkazy: Používejte `./` pro aktuální adresář, `../` pro nadřazený
- Nepoužívejte URL s lokalizací země (vyhněte se `/en-us/`, `/en/`)

**Obrázky:**
- Ukládejte všechny obrázky do adresáře `/imgs/`
- Používejte popisné názvy s anglickými znaky, čísly a pomlčkami
- Příklad: `phi-3-architecture.png`

**Markdown soubory:**
- Odkazujte na skutečné funkční příklady v adresáři `/code/`
- Udržujte dokumentaci synchronizovanou se změnami kódu
- Používejte emoji 📓 k označení odkazů na Jupyter notebooks v README

### Organizace souborů

- Příklady kódu v `/code/` organizované podle tématu/funkce
- Dokumentace v `/md/` zrcadlí strukturu kódu, pokud je to možné
- Uchovávejte související soubory (notebooky, skripty, konfigurace) pohromadě v podadresářích

## Pokyny pro Pull Requesty

### Před odesláním

1. **Forkněte úložiště** do svého účtu
2. **Oddělte PR podle typu:**
   - Opravy chyb v jednom PR
   - Aktualizace dokumentace v jiném
   - Nové příklady v samostatných PR
   - Opravy překlepů lze kombinovat

3. **Řešení konfliktů při slučování:**
   - Aktualizujte svou lokální větev `main` před provedením změn
   - Často synchronizujte s upstreamem

4. **Překladové PR:**
   - Musí obsahovat překlady pro VŠECHNY soubory ve složce
   - Zachovejte konzistentní strukturu s původním jazykem

### Požadované kontroly

PR automaticky spouští GitHub workflow pro validaci:

1. **Validace relativních cest** - Všechny interní odkazy musí fungovat
   - Testujte odkazy lokálně: Ctrl+Klik ve VS Code
   - Používejte návrhy cest z VS Code (`./` nebo `../`)

2. **Kontrola lokalizace URL** - Webové URL nesmí obsahovat lokalizace zemí
   - Odstraňte `/en-us/`, `/en/` nebo jiné jazykové kódy
   - Používejte obecné mezinárodní URL

3. **Kontrola nefunkčních URL** - Všechny URL musí vracet stav 200
   - Ověřte, že odkazy jsou přístupné před odesláním
   - Poznámka: Některé chyby mohou být způsobeny síťovými omezeními

### Formát názvu PR

```
[component] Brief description
```

Příklady:
- `[docs] Přidání tutoriálu pro inferenci Phi-4`
- `[code] Oprava příkladu integrace ONNX Runtime`
- `[translation] Přidání japonského překladu úvodních průvodců`

## Běžné vývojové vzory

### Práce s modely Phi

**Načítání modelů:**
- Příklady používají různé rámce: Transformers, ONNX Runtime, MLX, OpenVINO
- Modely jsou obvykle stahovány z Hugging Face, Azure nebo GitHub Models
- Zkontrolujte kompatibilitu modelu s vaším hardwarem (CPU, GPU, NPU)

**Vzory inferencí:**
- Generování textu: Většina příkladů používá varianty chat/instruct
- Vize: Phi-3-vision a Phi-4-multimodal pro porozumění obrazu
- Audio: Phi-4-multimodal podporuje zvukové vstupy
- Uvažování: Varianty Phi-4-reasoning pro pokročilé úkoly uvažování

### Poznámky k platformám

**Azure AI Foundry:**
- Vyžaduje předplatné Azure a API klíče
- Viz `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- K dispozici je bezplatná verze pro testování
- Viz `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokální inference:**
- ONNX Runtime: Multiplatformní, optimalizovaná inference
- Ollama: Snadná správa lokálních modelů (předkonfigurováno ve vývojovém kontejneru)
- Apple MLX: Optimalizováno pro Apple Silicon

## Řešení problémů

### Běžné problémy

**Problémy s pamětí:**
- Modely Phi vyžadují značné množství RAM (zejména vizuální/multimodální varianty)
- Používejte kvantizované modely pro prostředí s omezenými zdroji
- Viz `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikty závislostí:**
- Příklady v Pythonu mohou mít specifické požadavky na verze
- Používejte virtuální prostředí pro každý příklad
- Zkontrolujte jednotlivé soubory `requirements.txt`

**Problémy se stahováním modelů:**
- Velké modely mohou při pomalém připojení vypršet
- Zvažte použití cloudových prostředí (Codespaces, Azure)
- Zkontrolujte cache Hugging Face: `~/.cache/huggingface/`

**Problémy s projekty v .NET:**
- Ujistěte se, že máte nainstalovaný .NET 8.0 SDK
- Použijte `dotnet restore` před sestavením
- Některé projekty mají specifické konfigurace pro CUDA (Debug_Cuda)

**Příklady v JavaScriptu/webu:**
- Používejte Node.js 18+ pro kompatibilitu
- Vymažte `node_modules` a znovu nainstalujte, pokud problémy přetrvávají
- Zkontrolujte konzoli prohlížeče kvůli problémům s kompatibilitou WebGPU

### Získání pomoci

- **Discord:** Připojte se k Azure AI Foundry Community Discord
- **GitHub Issues:** Nahlaste chyby a problémy v úložišti
- **GitHub Discussions:** Pokládejte otázky a sdílejte znalosti

## Další kontext

### Odpovědná AI

Veškeré použití modelů Phi by mělo dodržovat principy odpovědné AI od Microsoftu:
- Spravedlnost, spolehlivost, bezpečnost
- Ochrana soukromí a bezpečnost  
- Inkluzivita, transparentnost, odpovědnost
- Používejte Azure AI Content Safety pro produkční aplikace
- Viz `/md/01.Introduction/01/01.AISafety.md`

### Překlady

- Podpora více než 50 jazyků prostřednictvím automatizované GitHub Action
- Překlady ve složce `/translations/`
- Udržováno workflow co-op-translator
- Nepřepisujte ručně přeložené soubory (automaticky generované)

### Přispívání

- Dodržujte pokyny v `CONTRIBUTING.md`
- Souhlaste s Contributor License Agreement (CLA)
- Dodržujte Microsoft Open Source Code of Conduct
- Nezahrnujte bezpečnostní údaje a přihlašovací údaje do commitů

### Podpora více jazyků

Toto je polyglotní úložiště s příklady v:
- **Python** - ML/AI workflow, Jupyter notebooks, jemné ladění
- **C#/.NET** - Podnikové aplikace, integrace ONNX Runtime
- **JavaScript** - Webová AI, inference v prohlížeči s WebGPU

Vyberte jazyk, který nejlépe odpovídá vašemu případu použití a cílovému nasazení.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.