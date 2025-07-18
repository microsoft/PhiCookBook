<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:16:45+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "it"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo per mostrare WebGPU e il Pattern RAG
Il Pattern RAG con il modello Phi-3 Onnx Hosted sfrutta l’approccio Retrieval-Augmented Generation, combinando la potenza dei modelli Phi-3 con l’hosting ONNX per implementazioni AI efficienti. Questo pattern è fondamentale per il fine-tuning di modelli per compiti specifici di dominio, offrendo un mix di qualità, convenienza e comprensione di contesti lunghi. Fa parte della suite Azure AI, che offre una vasta selezione di modelli facili da trovare, provare e utilizzare, rispondendo alle esigenze di personalizzazione di vari settori. I modelli Phi-3, inclusi Phi-3-mini, Phi-3-small e Phi-3-medium, sono disponibili nel Catalogo Modelli Azure AI e possono essere affinati e distribuiti in modo autonomo o tramite piattaforme come HuggingFace e ONNX, dimostrando l’impegno di Microsoft per soluzioni AI accessibili ed efficienti.

## Cos’è WebGPU
WebGPU è una moderna API grafica web progettata per fornire un accesso efficiente alla GPU (unità di elaborazione grafica) di un dispositivo direttamente dai browser web. È pensata per essere il successore di WebGL, offrendo diversi miglioramenti chiave:

1. **Compatibilità con GPU moderne**: WebGPU è costruita per funzionare senza problemi con le architetture GPU contemporanee, sfruttando API di sistema come Vulkan, Metal e Direct3D 12.
2. **Prestazioni migliorate**: Supporta calcoli generali sulla GPU e operazioni più veloci, rendendola adatta sia al rendering grafico che ai compiti di machine learning.
3. **Funzionalità avanzate**: WebGPU consente l’accesso a capacità GPU più avanzate, permettendo carichi di lavoro grafici e computazionali più complessi e dinamici.
4. **Riduzione del carico su JavaScript**: Spostando più compiti sulla GPU, WebGPU riduce significativamente il carico su JavaScript, migliorando le prestazioni e garantendo esperienze più fluide.

WebGPU è attualmente supportata in browser come Google Chrome, con lavori in corso per estendere il supporto ad altre piattaforme.

### 03.WebGPU
Ambiente richiesto:

**Browser supportati:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Abilitare WebGPU:

- In Chrome/Microsoft Edge

Abilita il flag `chrome://flags/#enable-unsafe-webgpu`.

#### Apri il tuo browser:
Avvia Google Chrome o Microsoft Edge.

#### Accedi alla pagina Flags:
Nella barra degli indirizzi, digita `chrome://flags` e premi Invio.

#### Cerca il flag:
Nella casella di ricerca in alto, digita 'enable-unsafe-webgpu'

#### Abilita il flag:
Trova il flag #enable-unsafe-webgpu nella lista dei risultati.

Clicca sul menu a tendina accanto e seleziona Enabled.

#### Riavvia il browser:

Dopo aver abilitato il flag, dovrai riavviare il browser per applicare le modifiche. Clicca sul pulsante Relaunch che appare in fondo alla pagina.

- Per Linux, avvia il browser con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ha WebGPU abilitato di default.
- In Firefox Nightly, digita about:config nella barra degli indirizzi e imposta `dom.webgpu.enabled` su true.

### Configurare la GPU per Microsoft Edge

Ecco i passaggi per configurare una GPU ad alte prestazioni per Microsoft Edge su Windows:

- **Apri Impostazioni:** Clicca sul menu Start e seleziona Impostazioni.
- **Impostazioni di sistema:** Vai su Sistema e poi su Schermo.
- **Impostazioni grafiche:** Scorri verso il basso e clicca su Impostazioni grafiche.
- **Scegli app:** Sotto “Scegli un’app per impostare la preferenza,” seleziona App desktop e poi Sfoglia.
- **Seleziona Edge:** Naviga nella cartella di installazione di Edge (di solito `C:\Program Files (x86)\Microsoft\Edge\Application`) e seleziona `msedge.exe`.
- **Imposta preferenza:** Clicca su Opzioni, scegli Prestazioni elevate, quindi clicca su Salva.  
Questo garantirà che Microsoft Edge utilizzi la tua GPU ad alte prestazioni per migliori prestazioni.  
- **Riavvia** il computer per applicare queste impostazioni.

### Apri il tuo Codespace:
Vai al tuo repository su GitHub.  
Clicca sul pulsante Code e seleziona Open with Codespaces.

Se non hai ancora un Codespace, puoi crearne uno cliccando su New codespace.

**Nota** Installare l’ambiente Node nel tuo codespace  
Eseguire una demo npm da un GitHub Codespace è un ottimo modo per testare e sviluppare il tuo progetto. Ecco una guida passo-passo per iniziare:

### Configura il tuo ambiente:
Una volta aperto il Codespace, assicurati di avere Node.js e npm installati. Puoi verificarlo eseguendo:  
```
node -v
```  
```
npm -v
```

Se non sono installati, puoi installarli usando:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Naviga nella directory del progetto:
Usa il terminale per spostarti nella directory dove si trova il tuo progetto npm:  
```
cd path/to/your/project
```

### Installa le dipendenze:
Esegui il comando seguente per installare tutte le dipendenze necessarie elencate nel file package.json:  

```
npm install
```

### Esegui la demo:
Una volta installate le dipendenze, puoi eseguire lo script della demo. Di solito è specificato nella sezione scripts del tuo package.json. Per esempio, se lo script della demo si chiama start, puoi eseguire:  

```
npm run build
```  
```
npm run dev
```

### Accedi alla demo:
Se la demo prevede un server web, Codespaces fornirà un URL per accedervi. Cerca una notifica o controlla la scheda Ports per trovare l’URL.

**Nota:** Il modello deve essere memorizzato nella cache del browser, quindi potrebbe richiedere un po’ di tempo per il caricamento.

### Demo RAG
Carica il file markdown `intro_rag.md` per completare la soluzione RAG. Se usi Codespaces, puoi scaricare il file che si trova in `01.InferencePhi3/docs/`

### Seleziona il tuo file:
Clicca sul pulsante “Choose File” per scegliere il documento da caricare.

### Carica il documento:
Dopo aver selezionato il file, clicca su “Upload” per caricare il documento per RAG (Retrieval-Augmented Generation).

### Avvia la chat:
Una volta caricato il documento, puoi iniziare una sessione di chat usando RAG basata sul contenuto del documento.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.