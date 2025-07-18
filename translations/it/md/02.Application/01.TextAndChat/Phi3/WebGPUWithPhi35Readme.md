<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:09:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "it"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo per mostrare WebGPU e il Pattern RAG

Il Pattern RAG con il modello Phi-3.5 Onnx Hosted sfrutta l’approccio Retrieval-Augmented Generation, combinando la potenza dei modelli Phi-3.5 con l’hosting ONNX per implementazioni AI efficienti. Questo pattern è fondamentale per il fine-tuning di modelli su compiti specifici di dominio, offrendo un mix di qualità, convenienza e comprensione di contesti estesi. Fa parte della suite Azure AI, che offre una vasta selezione di modelli facili da trovare, provare e utilizzare, rispondendo alle esigenze di personalizzazione di diversi settori.

## Cos’è WebGPU  
WebGPU è una moderna API grafica web progettata per fornire un accesso efficiente alla GPU (unità di elaborazione grafica) del dispositivo direttamente dai browser web. È pensata per essere il successore di WebGL, offrendo diversi miglioramenti chiave:

1. **Compatibilità con GPU moderne**: WebGPU è costruita per funzionare senza problemi con le architetture GPU contemporanee, sfruttando API di sistema come Vulkan, Metal e Direct3D 12.
2. **Prestazioni migliorate**: Supporta calcoli generali sulla GPU e operazioni più veloci, rendendola adatta sia al rendering grafico che ai compiti di machine learning.
3. **Funzionalità avanzate**: WebGPU consente l’accesso a capacità GPU più avanzate, permettendo carichi di lavoro grafici e computazionali più complessi e dinamici.
4. **Riduzione del carico su JavaScript**: Spostando più compiti sulla GPU, WebGPU riduce significativamente il carico di lavoro su JavaScript, migliorando le prestazioni e garantendo esperienze più fluide.

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
Questo garantirà che Microsoft Edge utilizzi la tua GPU ad alte prestazioni per migliorare le prestazioni.  
- **Riavvia** il computer per applicare queste impostazioni.

### Esempi : Per favore [clicca su questo link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.