# AGENTS.md

## Prezentare generală a proiectului

PhiCookBook este un depozit cuprinzător de rețete, care conține exemple practice, tutoriale și documentație pentru lucrul cu familia Phi de modele de limbaj mici (SLMs) de la Microsoft. Depozitul demonstrează diverse cazuri de utilizare, inclusiv inferență, ajustare fină, cuantificare, implementări RAG și aplicații multimodale pe diferite platforme și cadre.

**Tehnologii cheie:**
- **Limbaje:** Python, C#/.NET, JavaScript/Node.js
- **Cadre:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipuri de modele:** Phi-3, Phi-3.5, Phi-4 (text, viziune, multimodal, variante de raționament)

**Structura depozitului:**
- `/code/` - Exemple de cod funcțional și implementări de probă
- `/md/` - Documentație detaliată, tutoriale și ghiduri practice  
- `/translations/` - Traduceri în mai multe limbi (50+ limbi prin flux de lucru automatizat)
- `/.devcontainer/` - Configurație container de dezvoltare (Python 3.12 cu Ollama)

## Configurarea mediului de dezvoltare

### Utilizarea GitHub Codespaces sau Dev Containers (Recomandat)

1. Deschideți în GitHub Codespaces (cel mai rapid):
   - Faceți clic pe insigna "Open in GitHub Codespaces" din README
   - Containerul se configurează automat cu Python 3.12 și Ollama cu Phi-3

2. Deschideți în VS Code Dev Containers:
   - Utilizați insigna "Open in Dev Containers" din README
   - Containerul necesită minimum 16GB memorie gazdă

### Configurare locală

**Cerințe preliminare:**
- Python 3.12 sau mai recent
- .NET 8.0 SDK (pentru exemplele C#)
- Node.js 18+ și npm (pentru exemplele JavaScript)
- Recomandat minimum 16GB RAM

**Instalare:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pentru exemplele Python:**
Navigați la directoarele de exemple specifice și instalați dependențele:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Pentru exemplele .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Pentru exemplele JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organizarea depozitului

### Exemple de cod (`/code/`)

- **01.Introduce/** - Introduceri de bază și exemple pentru început
- **03.Finetuning/** și **04.Finetuning/** - Exemple de ajustare fină cu diverse metode
- **03.Inference/** - Exemple de inferență pe diferite hardware-uri (AIPC, MLX)
- **06.E2E/** - Exemple de aplicații de la început la sfârșit
- **07.Lab/** - Implementări de laborator/experimentale
- **08.RAG/** - Exemple de Generare Augmentată prin Recuperare
- **09.UpdateSamples/** - Cele mai recente exemple actualizate

### Documentație (`/md/`)

- **01.Introduction/** - Ghiduri introductive, configurarea mediului, ghiduri de platformă
- **02.Application/** - Exemple de aplicații organizate pe tipuri (Text, Cod, Viziune, Audio, etc.)
- **02.QuickStart/** - Ghiduri rapide pentru Microsoft Foundry și GitHub Models
- **03.FineTuning/** - Documentație și tutoriale pentru ajustare fină
- **04.HOL/** - Laboratoare practice (include exemple .NET)

### Formate de fișiere

- **Jupyter Notebooks (`.ipynb`)** - Tutoriale interactive Python marcate cu 📓 în README
- **Scripturi Python (`.py`)** - Exemple Python independente
- **Proiecte C# (`.csproj`, `.sln`)** - Aplicații și exemple .NET
- **JavaScript (`.js`, `package.json`)** - Exemple bazate pe web și Node.js
- **Markdown (`.md`)** - Documentație și ghiduri

## Lucrul cu exemplele

### Rularea Jupyter Notebooks

Majoritatea exemplelor sunt furnizate ca notebook-uri Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
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

Sau construiți întreaga soluție:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Rularea exemplelor JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testare

Acest depozit conține cod de exemplu și tutoriale, mai degrabă decât un proiect software tradițional cu teste unitare. Validarea se face, de obicei, prin:

1. **Rularea exemplelor** - Fiecare exemplu ar trebui să se execute fără erori
2. **Verificarea rezultatelor** - Asigurați-vă că răspunsurile modelului sunt adecvate
3. **Urmărirea tutorialelor** - Ghidurile pas cu pas ar trebui să funcționeze conform documentației

**Abordare comună de validare:**
- Testați execuția exemplului în mediul țintă
- Verificați instalarea corectă a dependențelor
- Asigurați-vă că modelele se descarcă/se încarcă cu succes
- Confirmați că comportamentul așteptat corespunde documentației

## Stilul codului și convenții

### Linii directoare generale

- Exemplele ar trebui să fie clare, bine comentate și educative
- Urmați convențiile specifice limbajului (PEP 8 pentru Python, standardele C# pentru .NET)
- Mențineți exemplele concentrate pe demonstrarea capacităților specifice ale modelului Phi
- Includeți comentarii care explică conceptele cheie și parametrii specifici modelului

### Standarde de documentație

**Formatarea URL-urilor:**
- Utilizați formatul `[text](../../url)` fără spații suplimentare
- Linkuri relative: Utilizați `./` pentru directorul curent, `../` pentru părinte
- Evitați localele specifice țării în URL-uri (evitați `/en-us/`, `/en/`)

**Imagini:**
- Stocați toate imaginile în directorul `/imgs/`
- Utilizați nume descriptive cu caractere englezești, numere și liniuțe
- Exemplu: `phi-3-architecture.png`

**Fișiere Markdown:**
- Referiți exemplele funcționale reale din directorul `/code/`
- Mențineți documentația sincronizată cu modificările codului
- Utilizați emoji 📓 pentru a marca linkurile către notebook-uri Jupyter în README

### Organizarea fișierelor

- Exemplele de cod din `/code/` sunt organizate pe subiect/funcționalitate
- Documentația din `/md/` reflectă structura codului, acolo unde este aplicabil
- Păstrați fișierele conexe (notebook-uri, scripturi, configurații) împreună în subdirectoare

## Ghiduri pentru Pull Request

### Înainte de trimitere

1. **Faceți fork la depozit** în contul dvs.
2. **Separați PR-urile după tip:**
   - Remedieri de erori într-un PR
   - Actualizări de documentație într-un alt PR
   - Exemple noi în PR-uri separate
   - Remedierile de tipografie pot fi combinate

3. **Gestionați conflictele de îmbinare:**
   - Actualizați ramura locală `main` înainte de a face modificări
   - Sincronizați frecvent cu upstream

4. **PR-uri de traducere:**
   - Trebuie să includă traduceri pentru TOATE fișierele din folder
   - Mențineți structura consistentă cu limba originală

### Verificări necesare

PR-urile rulează automat fluxuri de lucru GitHub pentru a valida:

1. **Validarea căilor relative** - Toate linkurile interne trebuie să funcționeze
   - Testați linkurile local: Ctrl+Click în VS Code
   - Utilizați sugestiile de cale din VS Code (`./` sau `../`)

2. **Verificarea localei URL** - URL-urile web nu trebuie să conțină locale de țară
   - Eliminați `/en-us/`, `/en/` sau alte coduri de limbă
   - Utilizați URL-uri internaționale generice

3. **Verificarea URL-urilor rupte** - Toate URL-urile trebuie să returneze statusul 200
   - Verificați accesibilitatea linkurilor înainte de trimitere
   - Notă: Unele eșecuri pot fi cauzate de restricții de rețea

### Formatul titlului PR

```
[component] Brief description
```

Exemple:
- `[docs] Adăugare tutorial inferență Phi-4`
- `[code] Remediere exemplu integrare ONNX Runtime`
- `[translation] Adăugare traducere japoneză pentru ghiduri introductive`

## Modele comune de dezvoltare

### Lucrul cu modelele Phi

**Încărcarea modelului:**
- Exemplele utilizează diverse cadre: Transformers, ONNX Runtime, MLX, OpenVINO
- Modelele sunt descărcate, de obicei, de pe Hugging Face, Azure sau GitHub Models
- Verificați compatibilitatea modelului cu hardware-ul dvs. (CPU, GPU, NPU)

**Modele de inferență:**
- Generare text: Majoritatea exemplelor utilizează variante de chat/instruct
- Viziune: Phi-3-vision și Phi-4-multimodal pentru înțelegerea imaginilor
- Audio: Phi-4-multimodal acceptă intrări audio
- Raționament: Variantele Phi-4-reasoning pentru sarcini avansate de raționament

### Note specifice platformei

**Microsoft Foundry:**
- Necesită abonament Azure și chei API
- Consultați `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Nivel gratuit disponibil pentru testare
- Consultați `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferență locală:**
- ONNX Runtime: Inferență optimizată, cross-platform
- Ollama: Gestionare ușoară a modelului local (pre-configurat în containerul de dezvoltare)
- Apple MLX: Optimizat pentru Apple Silicon

## Depanare

### Probleme comune

**Probleme de memorie:**
- Modelele Phi necesită RAM semnificativă (în special variantele de viziune/multimodal)
- Utilizați modele cuantificate pentru medii cu resurse limitate
- Consultați `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflicte de dependențe:**
- Exemplele Python pot avea cerințe specifice de versiune
- Utilizați medii virtuale pentru fiecare exemplu
- Verificați fișierele individuale `requirements.txt`

**Eșecuri la descărcarea modelului:**
- Modelele mari pot expira pe conexiuni lente
- Luați în considerare utilizarea mediilor cloud (Codespaces, Azure)
- Verificați cache-ul Hugging Face: `~/.cache/huggingface/`

**Probleme cu proiectele .NET:**
- Asigurați-vă că SDK-ul .NET 8.0 este instalat
- Utilizați `dotnet restore` înainte de compilare
- Unele proiecte au configurații specifice CUDA (Debug_Cuda)

**Exemple JavaScript/Web:**
- Utilizați Node.js 18+ pentru compatibilitate
- Goliți `node_modules` și reinstalați dacă apar probleme
- Verificați consola browserului pentru probleme de compatibilitate WebGPU

### Obținerea ajutorului

- **Discord:** Alăturați-vă comunității Microsoft Foundry pe Discord
- **GitHub Issues:** Raportați erorile și problemele în depozit
- **GitHub Discussions:** Puneți întrebări și împărtășiți cunoștințe

## Context suplimentar

### AI responsabil

Toate utilizările modelelor Phi ar trebui să respecte principiile de AI responsabil ale Microsoft:
- Echitate, fiabilitate, siguranță
- Confidențialitate și securitate  
- Incluziune, transparență, responsabilitate
- Utilizați Azure AI Content Safety pentru aplicații de producție
- Consultați `/md/01.Introduction/01/01.AISafety.md`

### Traduceri

- Suport pentru 50+ limbi prin GitHub Action automatizat
- Traduceri în directorul `/translations/`
- Menținut de fluxul de lucru co-op-translator
- Nu editați manual fișierele traduse (generate automat)

### Contribuții

- Urmați ghidurile din `CONTRIBUTING.md`
- Acceptați Acordul de Licență pentru Contribuitori (CLA)
- Respectați Codul de Conduită Microsoft Open Source
- Nu includeți informații de securitate sau credențiale în commit-uri

### Suport multilingv

Acesta este un depozit poliglot cu exemple în:
- **Python** - Fluxuri de lucru ML/AI, notebook-uri Jupyter, ajustare fină
- **C#/.NET** - Aplicații enterprise, integrare ONNX Runtime
- **JavaScript** - AI bazat pe web, inferență în browser cu WebGPU

Alegeți limbajul care se potrivește cel mai bine cazului dvs. de utilizare și țintei de implementare.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.