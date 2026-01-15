<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:10:25+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "it"
}
-->
## Benvenuto in AI Toolkit per VS Code

[AI Toolkit per VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) riunisce vari modelli dal Catalogo Azure AI Studio e da altri cataloghi come Hugging Face. Il toolkit semplifica le attività comuni di sviluppo per creare app AI con strumenti e modelli di intelligenza artificiale generativa attraverso:
- Inizia con la scoperta dei modelli e il playground.
- Fine-tuning e inferenza dei modelli usando risorse di calcolo locali.
- Fine-tuning e inferenza remoti usando risorse Azure.

[Installa AI Toolkit per VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/it/Aitoolkit.7157953df04812dc.png)


**[Private Preview]** Provisioning con un clic per Azure Container Apps per eseguire fine-tuning e inferenza dei modelli nel cloud.

Ora iniziamo con lo sviluppo della tua app AI:

- [Benvenuto in AI Toolkit per VS Code](../../../../md/03.FineTuning)
- [Sviluppo Locale](../../../../md/03.FineTuning)
  - [Preparativi](../../../../md/03.FineTuning)
  - [Attivare Conda](../../../../md/03.FineTuning)
  - [Solo fine-tuning del modello base](../../../../md/03.FineTuning)
  - [Fine-tuning e inferenza del modello](../../../../md/03.FineTuning)
  - [Fine-tuning del modello](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Esempi e risorse per il fine-tuning](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Sviluppo Remoto](../../../../md/03.FineTuning)
  - [Prerequisiti](../../../../md/03.FineTuning)
  - [Configurazione di un progetto di sviluppo remoto](../../../../md/03.FineTuning)
  - [Provision delle risorse Azure](../../../../md/03.FineTuning)
  - [\[Opzionale\] Aggiungere il token Huggingface al segreto di Azure Container App](../../../../md/03.FineTuning)
  - [Eseguire il fine-tuning](../../../../md/03.FineTuning)
  - [Provision dell’endpoint di inferenza](../../../../md/03.FineTuning)
  - [Distribuire l’endpoint di inferenza](../../../../md/03.FineTuning)
  - [Uso avanzato](../../../../md/03.FineTuning)

## Sviluppo Locale
### Preparativi

1. Assicurati che il driver NVIDIA sia installato sull’host.  
2. Esegui `huggingface-cli login` se utilizzi HF per l’uso di dataset.  
3. Spiegazioni delle impostazioni chiave di `Olive` per tutto ciò che modifica l’uso della memoria.

### Attivare Conda
Poiché stiamo usando l’ambiente WSL condiviso, devi attivare manualmente l’ambiente conda. Dopo questo passaggio puoi eseguire fine-tuning o inferenza.

```bash
conda activate [conda-env-name] 
```

### Solo fine-tuning del modello base
Per provare semplicemente il modello base senza fine-tuning, puoi eseguire questo comando dopo aver attivato conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Fine-tuning e inferenza del modello

Una volta aperto lo spazio di lavoro in un dev container, apri un terminale (il percorso predefinito è la radice del progetto), quindi esegui il comando qui sotto per fare fine-tuning di un LLM sul dataset selezionato.

```bash
python finetuning/invoke_olive.py 
```

I checkpoint e il modello finale saranno salvati nella cartella `models`.

Successivamente esegui l’inferenza con il modello fine-tuned tramite chat in una `console`, `browser web` o `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Per usare `prompt flow` in VS Code, consulta questo [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Fine-tuning del modello

Scarica il modello seguente in base alla disponibilità di una GPU sul tuo dispositivo.

Per avviare la sessione di fine-tuning locale usando QLoRA, seleziona un modello dal nostro catalogo che vuoi affinare.
| Piattaforma | GPU disponibile | Nome modello | Dimensione (GB) |
|---------|---------|--------|--------|
| Windows | Sì | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Sì | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | No | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Nota_** Non è necessario un account Azure per scaricare i modelli.

Il modello Phi3-mini (int4) ha una dimensione di circa 2GB-3GB. A seconda della velocità della tua rete, il download potrebbe richiedere qualche minuto.

Inizia selezionando un nome e una posizione per il progetto.  
Poi scegli un modello dal catalogo. Ti verrà chiesto di scaricare il template del progetto. Puoi quindi cliccare su "Configura Progetto" per modificare varie impostazioni.

### Microsoft Olive

Usiamo [Olive](https://microsoft.github.io/Olive/why-olive.html) per eseguire il fine-tuning QLoRA su un modello PyTorch del nostro catalogo. Tutte le impostazioni sono preimpostate con valori di default per ottimizzare l’esecuzione locale del fine-tuning con un uso efficiente della memoria, ma possono essere adattate al tuo scenario.

### Esempi e risorse per il fine-tuning

- [Guida introduttiva al fine-tuning](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Fine-tuning con un dataset HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Fine-tuning con un dataset semplice](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Sviluppo Remoto

### Prerequisiti

1. Per eseguire il fine-tuning del modello nel tuo ambiente remoto Azure Container App, assicurati che la tua sottoscrizione abbia sufficiente capacità GPU. Invia un [ticket di supporto](https://azure.microsoft.com/support/create-ticket/) per richiedere la capacità necessaria per la tua applicazione. [Ulteriori informazioni sulla capacità GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)  
2. Se usi dataset privati su HuggingFace, assicurati di avere un [account HuggingFace](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) e di [generare un token di accesso](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)  
3. Abilita la feature flag Remote Fine-tuning and Inference in AI Toolkit per VS Code  
   1. Apri le Impostazioni di VS Code selezionando *File -> Preferenze -> Impostazioni*.  
   2. Vai su *Estensioni* e seleziona *AI Toolkit*.  
   3. Seleziona l’opzione *"Enable Remote Fine-tuning And Inference"*.  
   4. Ricarica VS Code per applicare le modifiche.

- [Fine-tuning remoto](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Configurazione di un progetto di sviluppo remoto
1. Esegui il comando `AI Toolkit: Focus on Resource View` dalla palette dei comandi.  
2. Vai su *Model Fine-tuning* per accedere al catalogo modelli. Assegna un nome al progetto e seleziona la sua posizione sul tuo computer. Poi clicca su *"Configura Progetto"*.  
3. Configurazione del progetto  
    1. Evita di abilitare l’opzione *"Fine-tune locally"*.  
    2. Verranno mostrate le impostazioni di configurazione di Olive con valori preimpostati. Modifica e completa queste configurazioni secondo necessità.  
    3. Procedi con *Genera Progetto*. Questa fase utilizza WSL e prevede la creazione di un nuovo ambiente Conda, in preparazione a futuri aggiornamenti che includeranno Dev Containers.  
4. Clicca su *"Riapri finestra nello spazio di lavoro"* per aprire il progetto di sviluppo remoto.

> **Nota:** Il progetto funziona attualmente solo in locale o in remoto all’interno di AI Toolkit per VS Code. Se scegli *"Fine-tune locally"* durante la creazione del progetto, funzionerà esclusivamente in WSL senza capacità di sviluppo remoto. Se invece non abiliti *"Fine-tune locally"*, il progetto sarà limitato all’ambiente remoto Azure Container App.

### Provision delle risorse Azure
Per iniziare, devi effettuare il provisioning della risorsa Azure per il fine-tuning remoto. Fallo eseguendo il comando `AI Toolkit: Provision Azure Container Apps job for fine-tuning` dalla palette dei comandi.

Monitora l’avanzamento del provisioning tramite il link mostrato nel canale output.

### [Opzionale] Aggiungere il token Huggingface al segreto di Azure Container App
Se usi dataset privati HuggingFace, imposta il tuo token HuggingFace come variabile d’ambiente per evitare di dover effettuare il login manuale su Hugging Face Hub.  
Puoi farlo usando il comando `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Con questo comando puoi impostare il nome del segreto come [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) e usare il tuo token Hugging Face come valore del segreto.

### Eseguire il fine-tuning
Per avviare il job di fine-tuning remoto, esegui il comando `AI Toolkit: Run fine-tuning`.

Per visualizzare i log di sistema e della console, puoi visitare il portale Azure tramite il link nel pannello output (ulteriori passaggi su [Visualizzare e interrogare i log su Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Oppure puoi vedere i log della console direttamente nel pannello output di VSCode eseguendo il comando `AI Toolkit: Show the running fine-tuning job streaming logs`.  
> **Nota:** Il job potrebbe essere in coda a causa di risorse insufficienti. Se i log non vengono mostrati, esegui il comando `AI Toolkit: Show the running fine-tuning job streaming logs`, attendi un momento e poi esegui nuovamente il comando per riconnetterti allo streaming dei log.

Durante questo processo, QLoRA sarà usato per il fine-tuning e creerà adattatori LoRA per il modello da usare durante l’inferenza.  
I risultati del fine-tuning saranno salvati in Azure Files.

### Provision dell’endpoint di inferenza
Dopo che gli adattatori sono stati addestrati nell’ambiente remoto, usa una semplice applicazione Gradio per interagire con il modello.  
Come per il fine-tuning, devi configurare le risorse Azure per l’inferenza remota eseguendo il comando `AI Toolkit: Provision Azure Container Apps for inference` dalla palette dei comandi.

Di default, la sottoscrizione e il gruppo di risorse per l’inferenza dovrebbero corrispondere a quelli usati per il fine-tuning. L’inferenza utilizzerà lo stesso ambiente Azure Container App e accederà al modello e agli adattatori modello salvati in Azure Files, generati durante il fine-tuning.

### Distribuire l’endpoint di inferenza
Se vuoi modificare il codice di inferenza o ricaricare il modello di inferenza, esegui il comando `AI Toolkit: Deploy for inference`. Questo sincronizzerà il tuo codice più recente con Azure Container App e riavvierà la replica.

Una volta completata con successo la distribuzione, puoi accedere all’API di inferenza cliccando sul pulsante "*Vai all’endpoint di inferenza*" mostrato nella notifica di VSCode. Oppure, l’endpoint web API si trova sotto `ACA_APP_ENDPOINT` in `./infra/inference.config.json` e nel pannello output. Ora sei pronto per valutare il modello usando questo endpoint.

### Uso avanzato
Per maggiori informazioni sullo sviluppo remoto con AI Toolkit, consulta la documentazione su [Fine-Tuning modelli da remoto](https://aka.ms/ai-toolkit/remote-provision) e [Inferenza con il modello fine-tuned](https://aka.ms/ai-toolkit/remote-inference).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.