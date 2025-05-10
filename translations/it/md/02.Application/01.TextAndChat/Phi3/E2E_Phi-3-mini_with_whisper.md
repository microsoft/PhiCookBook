<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:30:31+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "it"
}
-->
# Chatbot Interattivo Phi 3 Mini 4K Instruct con Whisper

## Panoramica

Il chatbot interattivo Phi 3 Mini 4K Instruct è uno strumento che permette agli utenti di interagire con la demo Microsoft Phi 3 Mini 4K instruct utilizzando input testuali o audio. Il chatbot può essere utilizzato per vari compiti, come traduzioni, aggiornamenti meteo e raccolta di informazioni generali.

### Come Iniziare

Per utilizzare questo chatbot, segui semplicemente queste istruzioni:

1. Apri un nuovo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Nella finestra principale del notebook, vedrai un'interfaccia chat con una casella di input testuale e un pulsante "Send".
3. Per usare il chatbot basato su testo, digita semplicemente il tuo messaggio nella casella di input e clicca sul pulsante "Send". Il chatbot risponderà con un file audio che può essere riprodotto direttamente all'interno del notebook.

**Nota**: Questo strumento richiede una GPU e l'accesso ai modelli Microsoft Phi-3 e OpenAI Whisper, utilizzati per il riconoscimento vocale e la traduzione.

### Requisiti GPU

Per eseguire questa demo è necessario avere 12GB di memoria GPU.

I requisiti di memoria per eseguire la demo **Microsoft-Phi-3-Mini-4K instruct** su GPU dipendono da diversi fattori, come la dimensione dei dati in input (audio o testo), la lingua usata per la traduzione, la velocità del modello e la memoria disponibile sulla GPU.

In generale, il modello Whisper è progettato per funzionare su GPU. La quantità minima raccomandata di memoria GPU per eseguire il modello Whisper è di 8 GB, ma può gestire quantità maggiori di memoria se necessario.

È importante notare che l'elaborazione di grandi quantità di dati o un alto volume di richieste sul modello potrebbe richiedere più memoria GPU e/o causare problemi di prestazioni. Si consiglia di testare il proprio caso d'uso con diverse configurazioni e monitorare l'uso della memoria per determinare le impostazioni ottimali in base alle proprie esigenze specifiche.

## Esempio E2E per Chatbot Interattivo Phi 3 Mini 4K Instruct con Whisper

Il notebook jupyter intitolato [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) mostra come usare la demo Microsoft Phi 3 Mini 4K instruct per generare testo da input audio o testuale. Il notebook definisce diverse funzioni:

1. `tts_file_name(text)`: Questa funzione genera un nome file basato sul testo di input per salvare il file audio generato.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Questa funzione usa l'API Edge TTS per generare un file audio da una lista di segmenti di testo in input. I parametri di input sono la lista di segmenti, la velocità del parlato, il nome della voce e il percorso di output per salvare il file audio generato.
1. `talk(input_text)`: Questa funzione genera un file audio usando l'API Edge TTS e lo salva con un nome file casuale nella directory /content/audio. Il parametro di input è il testo da convertire in parlato.
1. `run_text_prompt(message, chat_history)`: Questa funzione utilizza la demo Microsoft Phi 3 Mini 4K instruct per generare un file audio da un messaggio in input e lo aggiunge alla cronologia della chat.
1. `run_audio_prompt(audio, chat_history)`: Questa funzione converte un file audio in testo usando l'API del modello Whisper e lo passa alla funzione `run_text_prompt()`.
1. Il codice avvia un'app Gradio che permette agli utenti di interagire con la demo Phi 3 Mini 4K instruct scrivendo messaggi o caricando file audio. L'output viene mostrato come messaggio testuale all'interno dell'app.

## Risoluzione Problemi

Installazione dei driver GPU Cuda

1. Assicurati che le tue applicazioni Linux siano aggiornate

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

    - Vai alla [pagina delle impostazioni token Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Seleziona **New token**.
    - Inserisci il **Nome** del progetto che vuoi usare.
    - Seleziona **Type** su **Write**.

> **Nota**
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
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.