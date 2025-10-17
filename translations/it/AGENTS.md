<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:54:01+00:00",
  "source_file": "AGENTS.md",
  "language_code": "it"
}
-->
# AGENTS.md

## Panoramica del Progetto

PhiCookBook è un repository completo di ricette che contiene esempi pratici, tutorial e documentazione per lavorare con la famiglia Phi di Small Language Models (SLMs) di Microsoft. Il repository dimostra vari casi d'uso, tra cui inferenza, fine-tuning, quantizzazione, implementazioni RAG e applicazioni multimodali su diverse piattaforme e framework.

**Tecnologie Chiave:**
- **Linguaggi:** Python, C#/.NET, JavaScript/Node.js
- **Framework:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Piattaforme:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Tipi di Modelli:** Phi-3, Phi-3.5, Phi-4 (varianti testuali, visive, multimodali, di ragionamento)

**Struttura del Repository:**
- `/code/` - Esempi di codice funzionanti e implementazioni di esempio
- `/md/` - Documentazione dettagliata, tutorial e guide pratiche  
- `/translations/` - Traduzioni in più lingue (oltre 50 lingue tramite workflow automatizzato)
- `/.devcontainer/` - Configurazione del container di sviluppo (Python 3.12 con Ollama)

## Configurazione dell'Ambiente di Sviluppo

### Utilizzo di GitHub Codespaces o Dev Containers (Consigliato)

1. Apri in GitHub Codespaces (il più veloce):
   - Clicca sul badge "Open in GitHub Codespaces" nel README
   - Il container si configura automaticamente con Python 3.12 e Ollama con Phi-3

2. Apri in Dev Containers di VS Code:
   - Usa il badge "Open in Dev Containers" dal README
   - Il container richiede almeno 16GB di memoria host

### Configurazione Locale

**Prerequisiti:**
- Python 3.12 o successivo
- .NET 8.0 SDK (per esempi in C#)
- Node.js 18+ e npm (per esempi in JavaScript)
- Consigliati almeno 16GB di RAM

**Installazione:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Per esempi in Python:**
Naviga nelle directory degli esempi specifici e installa le dipendenze:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Per esempi in .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Per esempi in JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organizzazione del Repository

### Esempi di Codice (`/code/`)

- **01.Introduce/** - Introduzioni di base e esempi per iniziare
- **03.Finetuning/** e **04.Finetuning/** - Esempi di fine-tuning con vari metodi
- **03.Inference/** - Esempi di inferenza su diversi hardware (AIPC, MLX)
- **06.E2E/** - Esempi di applicazioni end-to-end
- **07.Lab/** - Implementazioni di laboratorio/sperimentali
- **08.RAG/** - Esempi di generazione aumentata da recupero (RAG)
- **09.UpdateSamples/** - Ultimi esempi aggiornati

### Documentazione (`/md/`)

- **01.Introduction/** - Guide introduttive, configurazione dell'ambiente, guide alle piattaforme
- **02.Application/** - Esempi di applicazioni organizzati per tipo (Testo, Codice, Visione, Audio, ecc.)
- **02.QuickStart/** - Guide rapide per Azure AI Foundry e GitHub Models
- **03.FineTuning/** - Documentazione e tutorial sul fine-tuning
- **04.HOL/** - Laboratori pratici (inclusi esempi in .NET)

### Formati dei File

- **Notebook Jupyter (`.ipynb`)** - Tutorial interattivi in Python contrassegnati con 📓 nel README
- **Script Python (`.py`)** - Esempi Python autonomi
- **Progetti C# (`.csproj`, `.sln`)** - Applicazioni e esempi .NET
- **JavaScript (`.js`, `package.json`)** - Esempi basati sul web e Node.js
- **Markdown (`.md`)** - Documentazione e guide

## Lavorare con gli Esempi

### Esecuzione dei Notebook Jupyter

La maggior parte degli esempi è fornita come notebook Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Esecuzione degli Script Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Esecuzione degli Esempi .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Oppure costruisci l'intera soluzione:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Esecuzione degli Esempi JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testing

Questo repository contiene codice di esempio e tutorial piuttosto che un progetto software tradizionale con test unitari. La validazione viene generalmente effettuata tramite:

1. **Esecuzione degli esempi** - Ogni esempio dovrebbe essere eseguito senza errori
2. **Verifica dei risultati** - Controlla che le risposte del modello siano appropriate
3. **Seguire i tutorial** - Le guide passo-passo dovrebbero funzionare come documentato

**Approccio comune alla validazione:**
- Testa l'esecuzione degli esempi nell'ambiente target
- Verifica che le dipendenze siano installate correttamente
- Controlla che i modelli vengano scaricati/caricati con successo
- Conferma che il comportamento previsto corrisponda alla documentazione

## Stile del Codice e Convenzioni

### Linee Guida Generali

- Gli esempi devono essere chiari, ben commentati ed educativi
- Segui le convenzioni specifiche del linguaggio (PEP 8 per Python, standard C# per .NET)
- Mantieni gli esempi focalizzati sulla dimostrazione delle capacità specifiche dei modelli Phi
- Includi commenti che spiegano concetti chiave e parametri specifici del modello

### Standard di Documentazione

**Formattazione URL:**
- Usa il formato `[testo](../../url)` senza spazi extra
- Link relativi: Usa `./` per la directory corrente, `../` per la directory superiore
- Evita localizzazioni specifiche nei URL (evita `/en-us/`, `/en/`)

**Immagini:**
- Archivia tutte le immagini nella directory `/imgs/`
- Usa nomi descrittivi con caratteri inglesi, numeri e trattini
- Esempio: `phi-3-architecture.png`

**File Markdown:**
- Fai riferimento agli esempi funzionanti nella directory `/code/`
- Mantieni la documentazione sincronizzata con le modifiche al codice
- Usa l'emoji 📓 per contrassegnare i link ai notebook Jupyter nel README

### Organizzazione dei File

- Esempi di codice in `/code/` organizzati per argomento/funzione
- Documentazione in `/md/` che rispecchia la struttura del codice quando applicabile
- Mantieni i file correlati (notebook, script, configurazioni) insieme nelle sottodirectory

## Linee Guida per le Pull Request

### Prima di Inviare

1. **Forka il repository** sul tuo account
2. **Separa le PR per tipo:**
   - Correzioni di bug in una PR
   - Aggiornamenti alla documentazione in un'altra
   - Nuovi esempi in PR separate
   - Correzioni di errori tipografici possono essere combinate

3. **Gestisci i conflitti di merge:**
   - Aggiorna il tuo branch `main` locale prima di apportare modifiche
   - Sincronizza frequentemente con l'upstream

4. **PR di traduzione:**
   - Devono includere traduzioni per TUTTI i file nella cartella
   - Mantieni una struttura coerente con la lingua originale

### Controlli Richiesti

Le PR eseguono automaticamente i workflow di GitHub per validare:

1. **Validazione dei percorsi relativi** - Tutti i link interni devono funzionare
   - Testa i link localmente: Ctrl+Click in VS Code
   - Usa i suggerimenti di percorso di VS Code (`./` o `../`)

2. **Controllo dei locali URL** - Gli URL web non devono contenere codici di lingua
   - Rimuovi `/en-us/`, `/en/` o altri codici di lingua
   - Usa URL internazionali generici

3. **Controllo degli URL non funzionanti** - Tutti gli URL devono restituire lo stato 200
   - Verifica che i link siano accessibili prima di inviare
   - Nota: Alcuni fallimenti potrebbero essere dovuti a restrizioni di rete

### Formato del Titolo della PR

```
[component] Brief description
```

Esempi:
- `[docs] Aggiungi tutorial di inferenza Phi-4`
- `[code] Correggi esempio di integrazione ONNX Runtime`
- `[translation] Aggiungi traduzione giapponese per le guide introduttive`

## Modelli di Sviluppo Comuni

### Lavorare con i Modelli Phi

**Caricamento del Modello:**
- Gli esempi utilizzano vari framework: Transformers, ONNX Runtime, MLX, OpenVINO
- I modelli vengono generalmente scaricati da Hugging Face, Azure o GitHub Models
- Controlla la compatibilità del modello con il tuo hardware (CPU, GPU, NPU)

**Pattern di Inferenza:**
- Generazione di testo: La maggior parte degli esempi utilizza varianti chat/instruct
- Visione: Phi-3-vision e Phi-4-multimodal per la comprensione delle immagini
- Audio: Phi-4-multimodal supporta input audio
- Ragionamento: Varianti Phi-4-reasoning per compiti di ragionamento avanzato

### Note Specifiche per Piattaforma

**Azure AI Foundry:**
- Richiede abbonamento Azure e chiavi API
- Vedi `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Disponibile un livello gratuito per i test
- Vedi `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferenza Locale:**
- ONNX Runtime: Inferenza ottimizzata e cross-platform
- Ollama: Gestione facile dei modelli locali (preconfigurato nel container di sviluppo)
- Apple MLX: Ottimizzato per Apple Silicon

## Risoluzione dei Problemi

### Problemi Comuni

**Problemi di Memoria:**
- I modelli Phi richiedono molta RAM (soprattutto le varianti visive/multimodali)
- Usa modelli quantizzati per ambienti con risorse limitate
- Vedi `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflitti di Dipendenze:**
- Gli esempi Python potrebbero avere requisiti di versione specifici
- Usa ambienti virtuali per ogni esempio
- Controlla i singoli file `requirements.txt`

**Errori di Download del Modello:**
- I modelli di grandi dimensioni potrebbero andare in timeout su connessioni lente
- Considera l'uso di ambienti cloud (Codespaces, Azure)
- Controlla la cache di Hugging Face: `~/.cache/huggingface/`

**Problemi con Progetti .NET:**
- Assicurati che il SDK .NET 8.0 sia installato
- Usa `dotnet restore` prima di costruire
- Alcuni progetti hanno configurazioni specifiche per CUDA (Debug_Cuda)

**Esempi JavaScript/Web:**
- Usa Node.js 18+ per la compatibilità
- Cancella `node_modules` e reinstalla se si verificano problemi
- Controlla la console del browser per problemi di compatibilità WebGPU

### Ottenere Aiuto

- **Discord:** Unisciti alla Community Discord di Azure AI Foundry
- **GitHub Issues:** Segnala bug e problemi nel repository
- **GitHub Discussions:** Fai domande e condividi conoscenze

## Contesto Aggiuntivo

### AI Responsabile

Tutto l'uso dei modelli Phi dovrebbe seguire i principi di AI Responsabile di Microsoft:
- Equità, affidabilità, sicurezza
- Privacy e sicurezza  
- Inclusività, trasparenza, responsabilità
- Usa Azure AI Content Safety per applicazioni di produzione
- Vedi `/md/01.Introduction/01/01.AISafety.md`

### Traduzioni

- Supporto per oltre 50 lingue tramite GitHub Action automatizzato
- Traduzioni nella directory `/translations/`
- Mantenute dal workflow co-op-translator
- Non modificare manualmente i file tradotti (generati automaticamente)

### Contributi

- Segui le linee guida in `CONTRIBUTING.md`
- Accetta il Contributor License Agreement (CLA)
- Rispetta il Codice di Condotta Open Source di Microsoft
- Non includere credenziali o informazioni sensibili nei commit

### Supporto Multilingue

Questo è un repository poliglotta con esempi in:
- **Python** - Workflow ML/AI, notebook Jupyter, fine-tuning
- **C#/.NET** - Applicazioni aziendali, integrazione ONNX Runtime
- **JavaScript** - AI basata sul web, inferenza nel browser con WebGPU

Scegli il linguaggio che meglio si adatta al tuo caso d'uso e obiettivo di distribuzione.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.