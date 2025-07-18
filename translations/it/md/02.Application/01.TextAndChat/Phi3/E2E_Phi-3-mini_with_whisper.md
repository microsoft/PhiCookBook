<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:18:02+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "it"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot con Whisper

## Panoramica

L'Interactive Phi 3 Mini 4K Instruct Chatbot è uno strumento che permette agli utenti di interagire con la demo Microsoft Phi 3 Mini 4K instruct utilizzando input testuali o audio. Il chatbot può essere utilizzato per diverse attività, come traduzioni, aggiornamenti meteo e raccolta di informazioni generali.

### Come Iniziare

Per utilizzare questo chatbot, segui semplicemente queste istruzioni:

1. Apri un nuovo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Nella finestra principale del notebook, vedrai un’interfaccia chat con una casella di testo e un pulsante "Send".
3. Per usare il chatbot basato su testo, digita semplicemente il tuo messaggio nella casella di testo e clicca sul pulsante "Send". Il chatbot risponderà con un file audio che può essere riprodotto direttamente all’interno del notebook.

**Note**: Questo strumento richiede una GPU e l’accesso ai modelli Microsoft Phi-3 e OpenAI Whisper, utilizzati per il riconoscimento vocale e la traduzione.

### Requisiti GPU

Per eseguire questa demo è necessario avere 12 GB di memoria GPU.

I requisiti di memoria per eseguire la demo **Microsoft-Phi-3-Mini-4K instruct** su GPU dipendono da diversi fattori, come la dimensione dei dati di input (audio o testo), la lingua usata per la traduzione, la velocità del modello e la memoria disponibile sulla GPU.

In generale, il modello Whisper è progettato per funzionare su GPU. La quantità minima raccomandata di memoria GPU per eseguire il modello Whisper è di 8 GB, ma può gestire quantità maggiori se necessario.

È importante notare che l’elaborazione di grandi quantità di dati o un alto volume di richieste sul modello potrebbe richiedere più memoria GPU e/o causare problemi di prestazioni. Si consiglia di testare il proprio caso d’uso con diverse configurazioni e monitorare l’utilizzo della memoria per determinare le impostazioni ottimali per le proprie esigenze specifiche.

## Esempio E2E per Interactive Phi 3 Mini 4K Instruct Chatbot con Whisper

Il notebook Jupyter intitolato [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) mostra come utilizzare la demo Microsoft Phi 3 Mini 4K instruct per generare testo da input audio o scritto. Il notebook definisce diverse funzioni:

1. `tts_file_name(text)`: Questa funzione genera un nome file basato sul testo di input per salvare il file audio generato.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Questa funzione utilizza l’API Edge TTS per generare un file audio da una lista di frammenti di testo. I parametri di input sono la lista di frammenti, la velocità del parlato, il nome della voce e il percorso di salvataggio del file audio generato.
1. `talk(input_text)`: Questa funzione genera un file audio usando l’API Edge TTS e lo salva con un nome file casuale nella directory /content/audio. Il parametro di input è il testo da convertire in parlato.
1. `run_text_prompt(message, chat_history)`: Questa funzione utilizza la demo Microsoft Phi 3 Mini 4K instruct per generare un file audio da un messaggio di input e lo aggiunge alla cronologia della chat.
1. `run_audio_prompt(audio, chat_history)`: Questa funzione converte un file audio in testo usando l’API del modello Whisper e lo passa alla funzione `run_text_prompt()`.
1. Il codice avvia un’app Gradio che permette agli utenti di interagire con la demo Phi 3 Mini 4K instruct digitando messaggi o caricando file audio. L’output viene mostrato come messaggio di testo all’interno dell’app.

## Risoluzione dei Problemi

Installazione dei driver Cuda GPU

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

1. Controlla la dimensione della memoria GPU Nvidia (Richiesti 12GB di memoria GPU)

    ```bash
    nvidia-smi
    ```

1. Svuota la cache: Se usi PyTorch, puoi chiamare torch.cuda.empty_cache() per liberare tutta la memoria cache inutilizzata in modo che possa essere usata da altre applicazioni GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Controlla Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Esegui le seguenti operazioni per creare un token Hugging Face.

    - Vai alla [pagina delle impostazioni token di Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Seleziona **New token**.
    - Inserisci il **Nome** del progetto che vuoi usare.
    - Seleziona il **Tipo** su **Write**.

> **Note**
>
> Se incontri il seguente errore:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Per risolverlo, digita il seguente comando nel terminale.
>
> ```bash
> sudo ldconfig
> ```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.