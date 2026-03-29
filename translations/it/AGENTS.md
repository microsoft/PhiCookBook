# AGENTS.md

## Panoramica del Progetto

PhiCookBook è un repository completo di ricette contenente esempi pratici, tutorial e documentazione per lavorare con la famiglia Phi di Small Language Models (SLM) di Microsoft. Il repository dimostra vari casi d'uso tra cui inferenza, fine-tuning, quantizzazione, implementazioni RAG e applicazioni multimodali su diverse piattaforme e framework.

**Tecnologie Chiave:**
- **Linguaggi:** Python, C#/.NET, JavaScript/Node.js
- **Framework:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Piattaforme:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipi di Modelli:** Phi-3, Phi-3.5, Phi-4 (varianti testo, visione, multimodale, ragionamento)

**Struttura del Repository:**
- `/code/` - Esempi di codice funzionante e implementazioni di esempio
- `/md/` - Documentazione dettagliata, tutorial e guide pratiche  
- `/translations/` - Traduzioni multilingue (oltre 50 lingue tramite workflow automatizzato)
- `/.devcontainer/` - Configurazione del contenitore di sviluppo (Python 3.12 con Ollama)

## Configurazione Ambiente di Sviluppo

### Uso di GitHub Codespaces o Dev Containers (Consigliato)

1. Aprire in GitHub Codespaces (più veloce):
   - Cliccare sul badge "Open in GitHub Codespaces" nel README
   - Il contenitore si configura automaticamente con Python 3.12 e Ollama con Phi-3

2. Aprire in VS Code Dev Containers:
   - Usare il badge "Open in Dev Containers" dal README
   - Il contenitore richiede almeno 16GB di memoria host

### Configurazione Locale

**Prerequisiti:**
- Python 3.12 o successivo
- SDK .NET 8.0 (per esempi C#)
- Node.js 18+ e npm (per esempi JavaScript)
- Consigliati almeno 16GB di RAM

**Installazione:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Per esempi Python:**
Navigare nelle directory degli esempi specifici e installare le dipendenze:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # se requirements.txt esiste
```

**Per esempi .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Per esempi JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Avvia il server di sviluppo
npm run build  # Compila per la produzione
```

## Organizzazione del Repository

### Esempi di Codice (`/code/`)

- **01.Introduce/** - Introduzioni di base e campioni per iniziare
- **03.Finetuning/** e **04.Finetuning/** - Esempi di fine-tuning con vari metodi
- **03.Inference/** - Esempi di inferenza su hardware differente (AIPC, MLX)
- **06.E2E/** - Campioni di applicazioni end-to-end
- **07.Lab/** - Implementazioni di laboratorio/sperimentali
- **08.RAG/** - Esempi di Retrieval-Augmented Generation
- **09.UpdateSamples/** - Campioni aggiornati più recenti

### Documentazione (`/md/`)

- **01.Introduction/** - Guide introduttive, setup ambiente, guide piattaforma
- **02.Application/** - Esempi applicativi organizzati per tipo (Testo, Codice, Visione, Audio, ecc.)
- **02.QuickStart/** - Guide di avvio rapido per Microsoft Foundry e GitHub Models
- **03.FineTuning/** - Documentazione e tutorial per fine-tuning
- **04.HOL/** - Laboratori pratici (include esempi .NET)

### Formati dei File

- **Jupyter Notebooks (`.ipynb`)** - Tutorial Python interattivi contrassegnati con 📓 nel README
- **Script Python (`.py`)** - Esempi Python autonomi
- **Progetti C# (`.csproj`, `.sln`)** - Applicazioni e campioni .NET
- **JavaScript (`.js`, `package.json`)** - Esempi Web e Node.js
- **Markdown (`.md`)** - Documentazione e guide

## Lavorare con gli Esempi

### Esecuzione di Jupyter Notebooks

La maggior parte degli esempi è fornita come notebook Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Apre l'interfaccia del browser
# Naviga al file .ipynb desiderato
```

### Esecuzione di Script Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Esecuzione di Esempi .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Oppure compilare l'intero progetto:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Esecuzione di Esempi JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Sviluppo con ricarica a caldo
```

## Testing

Questo repository contiene esempi di codice e tutorial piuttosto che un progetto software tradizionale con unit test. La validazione viene solitamente eseguita tramite:

1. **Esecuzione degli esempi** - Ogni esempio dovrebbe eseguire senza errori
2. **Verifica dei risultati** - Controllare che le risposte del modello siano appropriate
3. **Seguire i tutorial** - Le guide passo-passo devono funzionare come documentato

**Approccio comune di validazione:**
- Testare l'esecuzione degli esempi nell'ambiente target
- Verificare che le dipendenze si installino correttamente
- Controllare che i modelli si scarichino/carichino con successo
- Confermare che il comportamento atteso corrisponda alla documentazione

## Stile di Codice e Convenzioni

### Linee Guida Generali

- Gli esempi devono essere chiari, ben commentati e didattici
- Seguire le convenzioni specifiche del linguaggio (PEP 8 per Python, standard C# per .NET)
- Mantenere gli esempi focalizzati sulla dimostrazione di capacità specifiche dei modelli Phi
- Includere commenti che spiegano concetti chiave e parametri specifici del modello

### Standard di Documentazione

**Formattazione URL:**
- Usare il formato `[text](../../url)` senza spazi extra
- Link relativi: usare `./` per la directory corrente, `../` per quella superiore
- No localizzazioni nazionali negli URL (evitare `/en-us/`, `/en/`)

**Immagini:**
- Salvare tutte le immagini nella directory `/imgs/`
- Usare nomi descrittivi con caratteri inglesi, numeri e trattini
- Esempio: `phi-3-architecture.png`

**File Markdown:**
- Fare riferimento a esempi funzionanti reali nella directory `/code/`
- Mantenere la documentazione sincronizzata con le modifiche del codice
- Usare l'emoji 📓 per contrassegnare i link ai notebook Jupyter nel README

### Organizzazione dei File

- Esempi di codice in `/code/` organizzati per argomento/funzionalità
- Documentazione in `/md/` rispecchia la struttura del codice quando applicabile
- Mantenere insieme i file correlati (notebook, script, config) nelle sottodirectory

## Linee Guida per le Pull Request

### Prima di Inviare

1. **Forkare il repository** nel proprio account
2. **Dividere le PR per tipo:**
   - Correzioni bug in una PR
   - Aggiornamenti documentazione in un'altra
   - Nuovi esempi in PR separate
   - Correzioni di refusi possono essere combinate

3. **Gestire conflitti di merge:**
   - Aggiornare il ramo `main` locale prima di fare modifiche
   - Sincronizzarsi frequentemente con l'upstream

4. **PR di traduzioni:**
   - Devono includere traduzioni per TUTTI i file della cartella
   - Mantenere struttura coerente con la lingua originale

### Verifiche Richieste

Le PR eseguono automaticamente workflow GitHub per convalidare:

1. **Validazione percorsi relativi** - Tutti i link interni devono funzionare
   - Testare i link localmente: Ctrl+Click in VS Code
   - Usare suggerimenti di percorso da VS Code (`./` o `../`)

2. **Controllo locale URL** - Gli URL web non devono contenere localizzazioni nazionali
   - Rimuovere `/en-us/`, `/en/` o altri codici di lingua
   - Usare URL internazionali generici

3. **Controllo URL non funzionanti** - Tutti gli URL devono restituire stato 200
   - Verificare che i link siano accessibili prima di inviare
   - Nota: Alcuni fallimenti possono essere dovuti a restrizioni di rete

### Formato del Titolo PR

```
[component] Brief description
```

Esempi:
- `[docs] Aggiungi tutorial inferenza Phi-4`
- `[code] Correggi esempio integrazione ONNX Runtime`
- `[translation] Aggiungi traduzione giapponese per guide introduttive`

## Schemi Comuni di Sviluppo

### Lavorare con Modelli Phi

**Caricamento Modello:**
- Gli esempi usano vari framework: Transformers, ONNX Runtime, MLX, OpenVINO
- I modelli vengono tipicamente scaricati da Hugging Face, Azure o GitHub Models
- Verificare compatibilità modello con l'hardware (CPU, GPU, NPU)

**Schemi di Inferenza:**
- Generazione di testo: La maggior parte degli esempi usa varianti chat/instruct
- Visione: Phi-3-vision e Phi-4-multimodale per comprensione immagine
- Audio: Phi-4-multimodale supporta input audio
- Ragionamento: Varianti Phi-4-reasoning per compiti di ragionamento avanzato

### Note Specifiche per Piattaforma

**Microsoft Foundry:**
- Richiede abbonamento Azure e chiavi API
- Vedi `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Livello gratuito disponibile per test
- Vedi `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferenza Locale:**
- ONNX Runtime: Cross-platform, inferenza ottimizzata
- Ollama: Gestione locale del modello facilitata (preconfigurata nel dev container)
- Apple MLX: Ottimizzato per Apple Silicon

## Risoluzione Problemi

### Problemi Comuni

**Problemi di Memoria:**
- I modelli Phi richiedono molta RAM (specialmente varianti visione/multimodale)
- Usare modelli quantizzati per ambienti con risorse limitate
- Vedi `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflitti di Dipendenze:**
- Gli esempi Python possono avere requisiti specifici di versione
- Usare ambienti virtuali per ogni esempio
- Controllare file `requirements.txt` specifici

**Fallimenti di Download Modello:**
- Modelli grandi possono scadere su connessioni lente
- Considerare ambienti cloud (Codespaces, Azure)
- Controllare cache Hugging Face: `~/.cache/huggingface/`

**Problematiche Progetti .NET:**
- Assicurarsi che SDK .NET 8.0 sia installato
- Usare `dotnet restore` prima di compilare
- Alcuni progetti hanno configurazioni specifiche CUDA (Debug_Cuda)

**Esempi JavaScript/Web:**
- Usare Node.js 18+ per compatibilità
- Pulire `node_modules` e reinstallare in caso di problemi
- Controllare console browser per problemi di compatibilità WebGPU

### Come Ottenere Aiuto

- **Discord:** Unirsi alla Community Discord di Microsoft Foundry
- **GitHub Issues:** Segnalare bug e problemi nel repository
- **GitHub Discussions:** Fare domande e condividere conoscenze

## Contesto Aggiuntivo

### AI Responsabile

Tutto l'uso dei modelli Phi deve seguire i principi di AI Responsabile di Microsoft:
- Equità, affidabilità, sicurezza
- Privacy e protezione  
- Inclusività, trasparenza, responsabilità
- Usare Azure AI Content Safety per applicazioni di produzione
- Vedi `/md/01.Introduction/01/01.AISafety.md`

### Traduzioni

- Oltre 50 lingue supportate tramite GitHub Action automatizzata
- Traduzioni nella directory `/translations/`
- Mantenute dal workflow co-op-translator
- Non modificare manualmente i file tradotti (generati automaticamente)

### Contributi

- Seguire le linee guida in `CONTRIBUTING.md`
- Accettare il Contributor License Agreement (CLA)
- Attenersi al Codice di Condotta Open Source di Microsoft
- Tenere fuori dai commit sicurezza e credenziali

### Supporto Multilingue

Questo è un repository poliglotta con esempi in:
- **Python** - Flussi ML/AI, notebook Jupyter, fine-tuning
- **C#/.NET** - Applicazioni aziendali, integrazione ONNX Runtime
- **JavaScript** - AI web, inferenza in browser con WebGPU

Scegli il linguaggio più adatto al tuo caso d'uso e target di distribuzione.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o errate interpretazioni derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->