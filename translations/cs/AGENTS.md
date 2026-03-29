# AGENTS.md

## Přehled projektu

PhiCookBook je komplexní repozitář kuchařek obsahující praktické příklady, návody a dokumentaci pro práci s rodinou malých jazykových modelů (SLM) od Microsoftu Phi. Repozitář demonstruje různé případy použití včetně inferencí, doladění, kvantizace, implementací RAG a multimodálních aplikací na různých platformách a rámcích.

**Klíčové technologie:**
- **Jazyky:** Python, C#/.NET, JavaScript/Node.js
- **Rámce:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformy:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Typy modelů:** Phi-3, Phi-3.5, Phi-4 (textové, vizuální, multimodální, varianty pro uvažování)

**Struktura repozitáře:**
- `/code/` - Pracovní příklady kódu a ukázkové implementace
- `/md/` - Podrobná dokumentace, návody a průvodce  
- `/translations/` - Překlady do více jazyků (50+ jazyků pomocí automatizovaného workflow)
- `/.devcontainer/` - Konfigurace vývojového kontejneru (Python 3.12 s Ollama)

## Nastavení vývojového prostředí

### Použití GitHub Codespaces nebo Dev kontejnerů (doporučeno)

1. Otevřete v GitHub Codespaces (nejrychlejší):
   - Klikněte na odznak „Open in GitHub Codespaces“ v README
   - Kontejner se automaticky nakonfiguruje s Python 3.12 a Ollama s Phi-3

2. Otevřete ve VS Code Dev kontejnerech:
   - Použijte odznak „Open in Dev Containers“ z README
   - Kontejner vyžaduje minimálně 16 GB paměti na hostitelském počítači

### Lokální nastavení

**Požadavky:**
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
Přejděte do konkrétních adresářů příkladů a nainstalujte závislosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # pokud existuje requirements.txt
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
npm run dev  # Spustit vývojový server
npm run build  # Vytvořit pro produkci
```

## Organizace repozitáře

### Příklady kódu (`/code/`)

- **01.Introduce/** - Základní úvodní a startovací příklady
- **03.Finetuning/** a **04.Finetuning/** - Příklady doladění s různými metodami
- **03.Inference/** - Příklady inferencí na různém hardware (AIPC, MLX)
- **06.E2E/** - Ukázky kompletních aplikací
- **07.Lab/** - Laboratorní/experimentální implementace
- **08.RAG/** - Příklady Retrieval-Augmented Generation
- **09.UpdateSamples/** - Nejnovější aktualizované příklady

### Dokumentace (`/md/`)

- **01.Introduction/** - Úvodní průvodce, nastavení prostředí, průvodce platformami
- **02.Application/** - Ukázky aplikací podle typu (Text, Kód, Vize, Audio atd.)
- **02.QuickStart/** - Rychlé startovací průvodce pro Microsoft Foundry a GitHub Models
- **03.FineTuning/** - Dokumentace a tutoriály k doladění
- **04.HOL/** - Praktické laboratoře (včetně příkladů v .NET)

### Formáty souborů

- **Jupyter Notebooks (`.ipynb`)** - Interaktivní tutoriály v Pythonu označené 📓 v README
- **Python skripty (`.py`)** - Samostatné příklady v Pythonu
- **C# projekty (`.csproj`, `.sln`)** - .NET aplikace a příklady
- **JavaScript (`.js`, `package.json`)** - Webové a Node.js příklady
- **Markdown (`.md`)** - Dokumentace a průvodci

## Práce s příklady

### Spuštění Jupyter Notebooks

Většina příkladů je poskytována jako Jupyter notebooky:
```bash
pip install jupyter notebook
jupyter notebook  # Otevře rozhraní prohlížeče
# Přejděte na požadovaný soubor .ipynb
```

### Spuštění Python skriptů

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Spuštění .NET příkladů

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Nebo sestavte celé řešení:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Spuštění JavaScript/Web příkladů

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Vývoj s horkým načítáním
```

## Testování

Tento repozitář obsahuje ukázkový kód a návody spíše než tradiční softwarový projekt s unit testy. Validace se obvykle provádí:

1. **Spuštěním příkladů** - Každý příklad by měl běžet bez chyb
2. **Ověřením výstupů** - Zkontrolujte, že odpovědi modelu jsou vhodné
3. **Následováním tutoriálů** - Krokové návody by měly fungovat dle dokumentace

**Běžný způsob ověřování:**
- Testování spuštění příkladů v cílovém prostředí
- Ověření správné instalace závislostí
- Kontrola úspěšného stažení/nahrání modelů
- Potvrzení, že chování odpovídá dokumentaci

## Styl kódu a konvence

### Obecné pokyny

- Příklady by měly být přehledné, dobře okomentované a vzdělávací
- Dodržujte jazykové konvence (PEP 8 pro Python, standardy C# pro .NET)
- Zaměřte příklady na demonstraci konkrétních schopností modelů Phi
- Zahrňte komentáře vysvětlující klíčové koncepty a parametry modelů

### Standardy dokumentace

**Formát URL:**
- Používejte formát `[text](../../url)` bez mezer navíc
- Relativní odkazy: Používejte `./` pro aktuální složku, `../` pro nadřazenou
- Vyvarujte se zeměspecifických lokalizací v URL (např. `/en-us/`, `/en/`)

**Obrázky:**
- Ukládejte všechny obrázky do adresáře `/imgs/`
- Používejte popisná jména s anglickými znaky, čísly a pomlčkami
- Příklad: `phi-3-architecture.png`

**Markdown soubory:**
- Odkazujte na skutečné funkční příklady v adresáři `/code/`
- Udržujte dokumentaci synchronizovanou se změnami kódu
- Používejte emoji 📓 k označení odkazů na Jupyter notebooky v README

### Organizace souborů

- Příklady kódu v `/code/` uspořádané podle témat/funkcí
- Dokumentace v `/md/` odpovídá struktuře kódu, kde je to možné
- Uchovávejte související soubory (notebooky, skripty, konfigurace) pohromadě v podsložkách

## Pokyny k pull requestům

### Před odesláním

1. **Rozvětvěte repozitář** do svého účtu
2. **Oddělte PR podle typu:**
   - Opravy chyb v jednom PR
   - Aktualizace dokumentace v jiném
   - Nové příklady v samostatných PR
   - Opravy překlepů lze slučovat

3. **Řešte konflikty slučování:**
   - Nejprve aktualizujte svou lokální `main` větev
   - Pravidelně synchronizujte s upstream

4. **Překladové PR:**
   - Musí obsahovat překlady VŠECH souborů ve složce
   - Zachovejte konzistentní strukturu s původním jazykem

### Požadované kontroly

PR automaticky spouští GitHub workflow pro validaci:

1. **Validace relativních cest** - Všechny interní odkazy musí fungovat
   - Testujte odkazy lokálně: Ctrl+klik ve VS Code
   - Používejte návrhy cest z VS Code (`./` nebo `../`)

2. **Kontrola lokality URL** - Webové URL nesmí obsahovat lokality zemí
   - Odstraňte `/en-us/`, `/en/` či jiné jazykové kódy
   - Používejte obecné mezinárodní URL

3. **Kontrola nefunkčních URL** - Všechny URL musí vracet stav 200
   - Ověřte dostupnost odkazů před odesláním
   - Některé chyby mohou být způsobeny omezeními sítě

### Formát názvu PR

```
[component] Brief description
```

Příklady:
- `[docs] Přidat návod na inferenci Phi-4`
- `[code] Opravit příklad integrace ONNX Runtime`
- `[translation] Přidat japonský překlad úvodních průvodců`

## Běžné vývojové vzory

### Práce s modely Phi

**Načítání modelů:**
- Příklady využívají různé rámce: Transformers, ONNX Runtime, MLX, OpenVINO
- Modely se obvykle stahují z Hugging Face, Azure nebo GitHub Models
- Zkontrolujte kompatibilitu modelu s vaším hardwarem (CPU, GPU, NPU)

**Vzory inference:**
- Generování textu: Většina příkladů používá chat/instruct varianty
- Vize: Phi-3-vision a Phi-4-multimodal pro porozumění obrázkům
- Audio: Phi-4-multimodal podporuje audio vstupy
- Uvažování: Phi-4-reasoning varianty pro pokročilé uvažovací úlohy

### Poznámky k platformám

**Microsoft Foundry:**
- Vyžaduje Azure předplatné a API klíče
- Viz `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Zdarma dostupný tier pro testování
- Viz `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokální inference:**
- ONNX Runtime: Multiplatformní, optimalizovaná inference
- Ollama: Snadná lokální správa modelů (přednastaveno ve vývojovém kontejneru)
- Apple MLX: Optimalizováno pro Apple Silicon

## Řešení problémů

### Nejčastější problémy

**Problémy s pamětí:**
- Modely Phi vyžadují značnou RAM (zejména vizuální/multimodální varianty)
- Používejte kvantizované modely pro prostředí s omezenými zdroji
- Viz `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikty závislostí:**
- Python příklady mohou mít specifické požadavky na verze
- Používejte virtuální prostředí pro každý příklad
- Zkontrolujte konkrétní soubory `requirements.txt`

**Selhání stahování modelů:**
- Velké modely mohou spadnout při pomalém připojení
- Uvažujte o použití cloud prostředí (Codespaces, Azure)
- Kontrola cache Hugging Face: `~/.cache/huggingface/`

**Problémy s projekty .NET:**
- Ujistěte se, že máte nainstalované .NET 8.0 SDK
- Použijte `dotnet restore` před sestavením
- Některé projekty mají specifické konfigurace pro CUDA (Debug_Cuda)

**JavaScript/Web příklady:**
- Používejte Node.js 18+ kvůli kompatibilitě
- Vyčistěte `node_modules` a reinstallujte, pokud problémy přetrvávají
- Zkontrolujte konzoli prohlížeče kvůli problémům s kompatibilitou WebGPU

### Jak získat pomoc

- **Discord:** Připojte se do Microsoft Foundry Community Discordu
- **GitHub Issues:** Hlaste chyby a problémy v repozitáři
- **GitHub Discussions:** Ptejte se a sdílejte znalosti

## Další kontext

### Responsible AI

Veškeré používání modelů Phi by mělo dodržovat principy odpovědné AI od Microsoftu:
- Spravedlnost, spolehlivost, bezpečnost
- Ochrana soukromí a bezpečnost  
- Inkluzivita, transparentnost, odpovědnost
- Používejte Azure AI Content Safety pro produkční aplikace
- Viz `/md/01.Introduction/01/01.AISafety.md`

### Překlady

- Podporováno 50+ jazyků pomocí automatizovaného GitHub Action
- Překlady v adresáři `/translations/`
- Udržováno workflow co-op-translator
- Nepřepisujte ručně překládané soubory (generováno automaticky)

### Přispívání

- Řiďte se pokyny v `CONTRIBUTING.md`
- Souhlaste s licenční smlouvou přispěvatele (CLA)
- Dodržujte Microsoft Open Source Code of Conduct
- Uchovávejte bezpečnost a přihlašovací údaje mimo commity

### Podpora více jazyků

Toto je polyglotní repozitář s příklady v:
- **Python** - ML/AI workflow, Jupyter notebooky, doladění
- **C#/.NET** - Podnikové aplikace, integrace ONNX Runtime
- **JavaScript** - Webové AI, inference v prohlížeči s WebGPU

Vyberte jazyk, který nejlépe vyhovuje vašemu použití a cílové implementaci.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za žádné nedorozumění nebo nesprávné interpretace, které mohou vzniknout použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->