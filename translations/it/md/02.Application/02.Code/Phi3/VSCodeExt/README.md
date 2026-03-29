# **Costruisci il tuo Visual Studio Code GitHub Copilot Chat con la Famiglia Microsoft Phi-3**

Hai mai utilizzato l'agente di workspace in GitHub Copilot Chat? Vuoi costruire il agente di codice del tuo team? Questo laboratorio pratico spera di combinare il modello open source per costruire un agente aziendale di codice a livello enterprise.

## **Fondamenti**

### **Perché scegliere Microsoft Phi-3**

Phi-3 è una serie di famiglia, che include phi-3-mini, phi-3-small e phi-3-medium basati su diversi parametri di addestramento per la generazione di testo, completamento del dialogo e generazione di codice. Esiste anche phi-3-vision basato su Vision. È adatto per imprese o diversi team per creare soluzioni AI generative offline.

Si consiglia di leggere questo link [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

L'estensione GitHub Copilot Chat ti offre un'interfaccia di chat che ti consente di interagire con GitHub Copilot e ricevere risposte a domande correlate alla programmazione direttamente all'interno di VS Code, senza la necessità di navigare la documentazione o cercare nei forum online.

Copilot Chat potrebbe utilizzare evidenziazione della sintassi, indentazione e altre funzionalità di formattazione per aggiungere chiarezza alla risposta generata. A seconda del tipo di domanda dell'utente, il risultato può contenere link a contesti utilizzati da Copilot per generare una risposta, come file di codice sorgente o documentazione, oppure pulsanti per accedere a funzionalità di VS Code.

- Copilot Chat si integra nel tuo flusso di sviluppo e ti assiste dove ne hai bisogno:

- Avvia una conversazione chat inline direttamente dall'editor o dal terminale per ricevere aiuto mentre stai programmando

- Usa la vista Chat per avere un assistente AI a lato che ti aiuta in qualsiasi momento

- Avvia Quick Chat per fare una domanda rapida e tornare subito a quello che stavi facendo

Puoi usare GitHub Copilot Chat in diversi scenari, come:

- Rispondere a domande di programmazione su come risolvere al meglio un problema

- Spiegare codice scritto da altri e suggerire miglioramenti

- Proporre correzioni al codice

- Generare casi di test unitari

- Generare documentazione del codice

Si consiglia di leggere questo link [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Riferirsi a **@workspace** in Copilot Chat ti permette di fare domande sull'intero codice sorgente. In base alla domanda, Copilot recupera intelligentemente file e simboli rilevanti, che poi include nella sua risposta come link ed esempi di codice.

Per rispondere alla tua domanda, **@workspace** cerca attraverso le stesse fonti che un sviluppatore utilizza per navigare un codice sorgente in VS Code:

- Tutti i file nel workspace, tranne quelli ignorati da un file .gitignore

- Struttura delle directory con cartelle e nomi dei file nidificati

- Indice di ricerca codice di GitHub, se il workspace è un repository GitHub e indicizzato dalla ricerca codice

- Simboli e definizioni nel workspace

- Testo attualmente selezionato o testo visibile nell'editor attivo

Nota: il .gitignore viene ignorato se hai un file aperto o hai selezionato testo all'interno di un file ignorato.

Si consiglia di leggere questo link [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Conoscere meglio questo laboratorio**

GitHub Copilot ha notevolmente migliorato l’efficienza di programmazione nelle imprese, e ogni impresa spera di personalizzare le funzioni rilevanti di GitHub Copilot. Molte imprese hanno personalizzato estensioni simili a GitHub Copilot basate sui propri scenari aziendali e modelli open source. Per le imprese, le estensioni personalizzate sono più facili da controllare, ma ciò influisce anche sull’esperienza utente. Dopotutto, GitHub Copilot ha funzioni più potenti nel gestire scenari generali e professionalità. Se l’esperienza può restare coerente, sarebbe meglio personalizzare l’estensione propria dell’impresa. GitHub Copilot Chat fornisce API rilevanti per le imprese per espandere l’esperienza di Chat. Mantenere un’esperienza coerente ed avere funzioni personalizzate è una migliore esperienza utente.

Questo laboratorio usa principalmente il modello Phi-3 combinato con NPU locale e Azure ibrido per costruire un Agente personalizzato in GitHub Copilot Chat ***@PHI3*** per assistere gli sviluppatori aziendali nel completamento di generazione codice***(@PHI3 /gen)*** e generazione di codice basata su immagini ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/it/cover.1017ebc9a7c46d09.webp)

### ***Nota:*** 

Questo laboratorio è attualmente implementato in AIPC su CPU Intel e Apple Silicon. Continueremo ad aggiornare la versione Qualcomm di NPU.


## **Laboratorio**


| Nome | Descrizione | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | Configurare e installare ambienti correlati e strumenti di installazione | [Vai](./HOL/AIPC/01.Installations.md) |[Vai](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | Combinato con AIPC / Apple Silicon, utilizza NPU locale per creare generazione codice tramite Phi-3-mini | [Vai](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Vai](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Genera codice distribuendo il Catalogo Modelli di Azure Machine Learning Service - immagine Phi-3-vision | [Vai](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Vai](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | Crea un agente Phi-3 personalizzato in GitHub Copilot Chat per completare generazione codice, generazione codice grafico, RAG, ecc. | [Vai](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Vai](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Codice di esempio (✅)  | Scarica codice di esempio | [Vai](../../../../../../../code/07.Lab/01/AIPC) | [Vai](../../../../../../../code/07.Lab/01/Apple) |


## **Risorse**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Ulteriori informazioni su GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Ulteriori informazioni su GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Ulteriori informazioni sull’API di GitHub Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Ulteriori informazioni su Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Ulteriori informazioni sul Catalogo Modelli di Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di essere consapevoli che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->