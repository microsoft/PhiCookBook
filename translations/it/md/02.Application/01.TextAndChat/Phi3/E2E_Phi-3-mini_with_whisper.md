<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:32:03+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "it"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot con Whisper

## Panoramica

L'Interactive Phi 3 Mini 4K Instruct Chatbot è uno strumento che permette agli utenti di interagire con la demo Microsoft Phi 3 Mini 4K instruct utilizzando input testuali o audio. Il chatbot può essere usato per una varietà di compiti, come traduzioni, aggiornamenti meteo e raccolta di informazioni generali.

### Per Iniziare

Per usare questo chatbot, segui semplicemente queste istruzioni:

1. Apri un nuovo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Nella finestra principale del notebook, vedrai un'interfaccia chatbox con una casella di input testuale e un pulsante "Send".
3. Per usare il chatbot basato su testo, digita semplicemente il tuo messaggio nella casella di input testuale e clicca sul pulsante "Send". Il chatbot risponderà con un file audio che può essere riprodotto direttamente all'interno del notebook.

**Nota**: Questo strumento richiede una GPU e l'accesso ai modelli Microsoft Phi-3 e OpenAI Whisper, che sono utilizzati per il riconoscimento vocale e la traduzione.

### Requisiti GPU

Per eseguire questa demo è necessario avere 12 GB di memoria GPU.

I requisiti di memoria per eseguire la demo **Microsoft-Phi-3-Mini-4K instruct** su una GPU dipendono da diversi fattori, come la dimensione dei dati in input (audio o testo), la lingua utilizzata per la traduzione, la velocità del modello e la memoria disponibile sulla GPU.

In generale, il modello Whisper è progettato per funzionare su GPU. La quantità minima raccomandata di memoria GPU per eseguire il modello Whisper è di 8 GB, ma può gestire quantità maggiori di memoria se necessario.

È importante notare che l'esecuzione di una grande quantità di dati o un alto volume di richieste sul modello potrebbe richiedere più memoria GPU e/o causare problemi di prestazioni. Si consiglia di testare il proprio caso d’uso con diverse configurazioni e monitorare l’uso della memoria per determinare le impostazioni ottimali per le proprie esigenze specifiche.

## Esempio E2E per Interactive Phi 3 Mini 4K Instruct Chatbot con Whisper

Il notebook jupyter intitolato [Interactive Phi 3 Mini 4K Instruct Chatbot con Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) dimostra come usare la demo Microsoft Phi 3 Mini 4K instruct per generare testo da input audio o scritto. Il notebook definisce varie funzioni:

1. `tts_file_name(text)`: Questa funzione genera un nome file basato sul testo di input per salvare il file audio generato.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Questa funzione usa l’API Edge TTS per generare un file audio da una lista di frammenti di testo in input. I parametri di input sono la lista di frammenti, la velocità del parlato, il nome della voce e il percorso di output per salvare il file audio generato.
1. `talk(input_text)`: Questa funzione genera un file audio usando l’API Edge TTS e lo salva con un nome file casuale nella directory /content/audio. Il parametro di input è il testo da convertire in parlato.
1. `run_text_prompt(message, chat_history)`: Questa funzione usa la demo Microsoft Phi 3 Mini 4K instruct per generare un file audio da un messaggio in input e lo aggiunge alla cronologia della chat.
1. `run_audio_prompt(audio, chat_history)`: Questa funzione converte un file audio in testo usando l’API del modello Whisper e lo passa alla funzione `run_text_prompt()`.
1. Il codice avvia un’app Gradio che permette agli utenti di interagire con la demo Phi 3 Mini 4K instruct digitando messaggi o caricando file audio. L’output viene mostrato come messaggio di testo nell’app.

## Risoluzione dei Problemi

Installazione dei driver GPU Cuda

1. Assicurati che la tua applicazione Linux sia aggiornata

    ```bash
    sudo apt update
    ```

1. Installa i driver Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registra la posizione del driver cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verifica la dimensione della memoria GPU Nvidia (Richiesti 12GB di memoria GPU)

    ```bash
    nvidia-smi
    ```

1. Cache vuota: Se stai usando PyTorch, puoi chiamare torch.cuda.empty_cache() per liberare tutta la memoria cache inutilizzata così che possa essere usata da altre applicazioni GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verifica Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Esegui le seguenti operazioni per creare un token Hugging Face.

    - Vai alla [pagina delle impostazioni token di Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Seleziona **Nuovo token**.
    - Inserisci il **Nome** del progetto che desideri usare.
    - Seleziona **Tipo** su **Scrittura**.

> [!NOTE]
>
> Se incontri il seguente errore:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Per risolverlo, digita il seguente comando nel tuo terminale.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur lavorando per garantire l'accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non ci assumiamo responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->