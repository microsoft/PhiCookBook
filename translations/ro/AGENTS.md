# AGENTS.md

## Prezentare generală a proiectului

PhiCookBook este un depozit complet de rețete ce conține exemple practice, tutoriale și documentație pentru lucrul cu familia de modele mici de limbaj (SLM) Phi de la Microsoft. Depozitul demonstrează diverse scenarii de utilizare, inclusiv inferență, fine-tuning, cuantificare, implementări RAG și aplicații multimodale pe diferite platforme și cadre.

**Tehnologii cheie:**
- **Limbaje:** Python, C#/.NET, JavaScript/Node.js
- **Cadre:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipuri de modele:** Phi-3, Phi-3.5, Phi-4 (variante text, viziune, multimodale, raționament)

**Structura depozitului:**
- `/code/` - Exemple de cod funcțional și implementări de referință
- `/md/` - Documentație detaliată, tutoriale și ghiduri practice  
- `/translations/` - Traduceri în mai multe limbi (50+ limbi prin flux de lucru automatizat)
- `/.devcontainer/` - Configurare container pentru dezvoltare (Python 3.12 cu Ollama)

## Configurarea mediului de dezvoltare

### Utilizarea GitHub Codespaces sau Dev Containers (Recomandat)

1. Deschide în GitHub Codespaces (cea mai rapidă metodă):
   - Apasă badge-ul „Open in GitHub Codespaces” din README
   - Containerul se configurează automat cu Python 3.12 și Ollama cu Phi-3

2. Deschide în VS Code Dev Containers:
   - Folosește badge-ul „Open in Dev Containers” din README
   - Containerul necesită minimum 16GB memorie gazdă

### Configurare locală

**Precondiții:**
- Python 3.12 sau versiune ulterioară
- SDK .NET 8.0 (pentru exemplele C#)
- Node.js 18+ și npm (pentru exemplele JavaScript)
- Minim recomandat 16GB RAM

**Instalare:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pentru exemple Python:**
Accesați directoarele specifice exemplelor și instalați dependențele:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # dacă requirements.txt există
```

**Pentru exemple .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Pentru exemple JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Porniți serverul de dezvoltare
npm run build  # Construiți pentru producție
```

## Organizarea depozitului

### Exemple de cod (`/code/`)

- **01.Introduce/** - Introduceri de bază și exemple de început
- **03.Finetuning/** și **04.Finetuning/** - Exemple de fine-tuning cu diverse metode
- **03.Inference/** - Exemple de inferență pe hardware diferit (AIPC, MLX)
- **06.E2E/** - Exemple complete de aplicații
- **07.Lab/** - Implementări experimentale/laborator
- **08.RAG/** - Exemple Retrieval-Augmented Generation
- **09.UpdateSamples/** - Exemple actualizate recent

### Documentație (`/md/`)

- **01.Introduction/** - Ghiduri introductive, configurare mediu, ghiduri platformă
- **02.Application/** - Exemple de aplicații organizate pe tipuri (Text, Code, Vision, Audio etc.)
- **02.QuickStart/** - Ghiduri rapide pentru Microsoft Foundry și GitHub Models
- **03.FineTuning/** - Documentație și tutoriale pentru fine-tuning
- **04.HOL/** - Laboratoare practice (include exemple .NET)

### Formate de fișiere

- **Jupyter Notebooks (`.ipynb`)** - Tutoriale interactive Python marcate cu 📓 în README
- **Scripturi Python (`.py`)** - Exemple Python autonome
- **Proiecte C# (`.csproj`, `.sln`)** - Aplicații și exemple .NET
- **JavaScript (`.js`, `package.json`)** - Exemple web și Node.js
- **Markdown (`.md`)** - Documentație și ghiduri

## Lucrul cu exemplele

### Rularea Jupyter Notebooks

Majoritatea exemplelor sunt furnizate ca notebook-uri Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Deschide interfața browserului
# Navighează la fișierul .ipynb dorit
```

### Rularea scripturilor Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Rularea exemplelor .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Sau construiește soluția completă:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Rularea exemplelor JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Dezvoltare cu reîncărcare la cald
```

## Testare

Acest depozit conține cod exemplu și tutoriale, nu un proiect software tradițional cu teste unitare. Validarea se face de obicei prin:

1. **Executarea exemplelor** - Fiecare exemplu trebuie să ruleze fără erori
2. **Verificarea rezultatelor** - Confirmați că răspunsurile modelelor sunt adecvate
3. **Urmarea tutorialelor** - Ghidurile pas-cu-pas trebuie să funcționeze conform documentației

**Abordare comună de validare:**
- Testarea execuției exemplelor în mediul țintă
- Verificarea instalării corecte a dependențelor
- Confirmarea descărcării și încărcării cu succes a modelelor
- Confirmarea comportamentului așteptat conform documentației

## Stilul de cod și convenții

### Linii directoare generale

- Exemplele trebuie să fie clare, bine comentate și educaționale
- Urmați convențiile specifice limbajului (PEP 8 pentru Python, standarde C# pentru .NET)
- Exemplele să se concentreze pe demonstrararea capabilităților specifice modelelor Phi
- Includeți comentarii explicative pentru conceptele cheie și parametrii specifici modelelor

### Standardele de documentație

**Formatarea URL-urilor:**
- Folosiți formatul `[text](../../url)` fără spații suplimentare
- Linkuri relative: folosiți `./` pentru directorul curent, `../` pentru cel părinte
- Nu folosiți locale specifice țărilor în URL-uri (evitați `/en-us/`, `/en/`)

**Imagini:**
- Salvați toate imaginile în directorul `/imgs/`
- Folosiți nume descriptive, cu caractere englezești, cifre și liniute
- Exemplu: `phi-3-architecture.png`

**Fișiere Markdown:**
- Faceți referire la exemplele funcționale reale din directorul `/code/`
- Mențineți documentația sincronizată cu modificările din cod
- Folosiți emoji-ul 📓 pentru a marca linkurile către notebook-uri Jupyter în README

### Organizarea fișierelor

- Exemplele de cod în `/code/` organizate după subiect/funcționalitate
- Documentația în `/md/` oglindește structura codului dacă este cazul
- Mențineți fișierele conexe (notebook-uri, scripturi, configuri) împreună în subdirectoare

## Ghiduri pentru Pull Requests

### Înainte de a trimite

1. **Fork-uiți depozitul** în contul dvs.
2. **Separă Pull Requests după tip:**
   - Corecturi de bug-uri într-un PR
   - Actualizări de documentație în alt PR
   - Exemple noi în PR-uri separate
   - Corecturi de tipar pot fi combinate

3. **Gestionați conflictele de merge:**
   - Actualizați ramura locală `main` înainte de a face modificări
   - Sincronizați frecvent cu upstream

4. **PR-urile de traduceri:**
   - Trebuie să includă traducerea pentru TOATE fișierele din folder
   - Mențineți structura consecventă cu limba originală

### Verificări obligatorii

PR-urile rulează automat workflow-uri GitHub pentru validare:

1. **Validarea căilor relative** – Toate linkurile interne trebuie să funcționeze
   - Testați linkurile local: Ctrl+Click în VS Code
   - Folosiți sugestiile de cale din VS Code (`./` sau `../`)

2. **Verificare URL locale** – URL-urile web nu trebuie să conțină locale de țară
   - Eliminați `/en-us/`, `/en/` sau alte coduri de limbă
   - Folosiți URL-uri internaționale generice

3. **Verificare URL-uri rupte** – Toate URL-urile trebuie să returneze status 200
   - Verificați accesibilitatea linkurilor înainte de trimitere
   - Atenție: unele eșecuri pot fi cauzate de restricții de rețea

### Formatul titlului PR

```
[component] Brief description
```

Exemple:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## Modele comune de dezvoltare

### Lucrul cu modelele Phi

**Încărcarea modelului:**
- Exemplele folosesc diferite cadre: Transformers, ONNX Runtime, MLX, OpenVINO
- Modelele sunt de obicei descărcate de pe Hugging Face, Azure sau GitHub Models
- Verificați compatibilitatea modelului cu hardware-ul dvs. (CPU, GPU, NPU)

**Tipare de inferență:**
- Generare text: Majoritatea exemplelor utilizează variante chat/instruct
- Viziune: Phi-3-vision și Phi-4-multimodal pentru înțelegere imagini
- Audio: Phi-4-multimodal suportă input audio
- Raționament: variante Phi-4-reasoning pentru sarcini avansate

### Note specifice platformei

**Microsoft Foundry:**
- Necesită abonament Azure și chei API
- Vezi `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Tier gratuit disponibil pentru testare
- Vezi `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferență locală:**
- ONNX Runtime: inferență optimizată cross-platform
- Ollama: management ușor al modelelor locale (preconfigurat în containerul de dezvoltare)
- Apple MLX: optimizat pentru Apple Silicon

## Depanare

### Probleme comune

**Probleme de memorie:**
- Modelele Phi necesită RAM semnificativă (în special variantele viziune/multimodale)
- Folosiți modele cuantificate pentru medii cu resurse limitate
- Vezi `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflicte de dependențe:**
- Exemplele Python pot avea cerințe specifice de versiune
- Folosiți medii virtuale pentru fiecare exemplu
- Verificați fișierele `requirements.txt` individuale

**Eșecuri la descărcarea modelului:**
- Modelele mari pot expire pe conexiuni lente
- Luați în considerare utilizarea mediilor cloud (Codespaces, Azure)
- Verificați cache-ul Hugging Face: `~/.cache/huggingface/`

**Probleme proiect .NET:**
- Asigurați-vă că SDK .NET 8.0 este instalat
- Folosiți `dotnet restore` înainte de build
- Unele proiecte au configurații specifice CUDA (Debug_Cuda)

**Exemple JavaScript/Web:**
- Folosiți Node.js 18+ pentru compatibilitate
- Ștergeți `node_modules` și reinstalați dacă problemele persistă
- Verificați consola browserului pentru probleme WebGPU

### Obținerea ajutorului

- **Discord:** Alăturați-vă comunității Microsoft Foundry pe Discord
- **GitHub Issues:** Raportați bug-uri și probleme în depozit
- **GitHub Discussions:** Puneți întrebări și împărtășiți cunoștințe

## Context suplimentar

### AI responsabil

Toată utilizarea modelelor Phi trebuie să urmeze principiile AI responsabile ale Microsoft:
- Corectitudine, fiabilitate, securitate
- Confidențialitate și protecție  
- Incluziune, transparență, responsabilitate
- Folosiți Azure AI Content Safety pentru aplicații în producție
- Vezi `/md/01.Introduction/01/01.AISafety.md`

### Traduceri

- Suport pentru 50+ limbi prin GitHub Action automatizat
- Traduceri în directorul `/translations/`
- Menținute prin fluxul de lucru co-op-translator
- Nu editați manual fișierele traduse (auto-generate)

### Contribuții

- Urmați ghidurile din `CONTRIBUTING.md`
- Acceptați Acordul de Licență al Contribuitorului (CLA)
- Respectați Codul de Conduită Open Source Microsoft
- Nu includeți date de securitate sau credențiale în commit-uri

### Suport multi-limbaj

Acesta este un depozit poliglot cu exemple în:
- **Python** - fluxuri ML/AI, notebook-uri Jupyter, fine-tuning
- **C#/.NET** - aplicații enterprise, integrare ONNX Runtime
- **JavaScript** - AI web, inferență în browser cu WebGPU

Alegeți limbajul care se potrivește cel mai bine cazului și țintei dvs. de implementare.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite apărute din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->