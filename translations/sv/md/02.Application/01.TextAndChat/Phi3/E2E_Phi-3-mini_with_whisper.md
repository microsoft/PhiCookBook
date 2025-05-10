<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:31:36+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sv"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot med Whisper

## Översikt

Interactive Phi 3 Mini 4K Instruct Chatbot är ett verktyg som låter användare interagera med Microsoft Phi 3 Mini 4K instruct-demo via text- eller ljudinmatning. Chatboten kan användas för olika uppgifter, såsom översättning, väderuppdateringar och allmän informationsinhämtning.

### Kom igång

För att använda denna chatbot, följ helt enkelt dessa instruktioner:

1. Öppna en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I huvudfönstret i notebooken ser du ett chattfönster med en textruta och en "Send"-knapp.
3. För att använda textbaserad chatbot, skriv ditt meddelande i textrutan och klicka på "Send". Chatboten svarar med en ljudfil som kan spelas upp direkt i notebooken.

**Note**: Detta verktyg kräver en GPU och tillgång till Microsoft Phi-3 och OpenAI Whisper-modellerna, som används för taligenkänning och översättning.

### GPU-krav

För att köra denna demo behöver du 12 GB GPU-minne.

Minne som krävs för att köra **Microsoft-Phi-3-Mini-4K instruct**-demot på en GPU beror på flera faktorer, såsom storleken på indata (ljud eller text), språket som används för översättning, modellens hastighet och tillgängligt minne på GPU:n.

Generellt är Whisper-modellen designad för att köras på GPU:er. Rekommenderat minimalt GPU-minne för Whisper är 8 GB, men den kan hantera större mängder minne vid behov.

Det är viktigt att notera att hantering av stora datamängder eller hög volym av förfrågningar kan kräva mer GPU-minne och/eller orsaka prestandaproblem. Det rekommenderas att testa ditt användningsfall med olika konfigurationer och övervaka minnesanvändningen för att hitta optimala inställningar för dina behov.

## E2E-exempel för Interactive Phi 3 Mini 4K Instruct Chatbot med Whisper

Jupyter-notebooken med titeln [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) visar hur man använder Microsoft Phi 3 Mini 4K instruct Demo för att generera text från ljud- eller textinmatning. Notebooken definierar flera funktioner:

1. `tts_file_name(text)`: Denna funktion genererar ett filnamn baserat på inmatad text för att spara den genererade ljudfilen.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denna funktion använder Edge TTS API för att skapa en ljudfil från en lista med textdelar. Indataparametrarna är listan med delar, talhastighet, röstnamn och sökväg för att spara ljudfilen.
1. `talk(input_text)`: Denna funktion genererar en ljudfil med Edge TTS API och sparar den till ett slumpmässigt filnamn i /content/audio-katalogen. Indataparametern är texten som ska konverteras till tal.
1. `run_text_prompt(message, chat_history)`: Denna funktion använder Microsoft Phi 3 Mini 4K instruct-demo för att skapa en ljudfil från ett meddelande och lägger till den i chattloggen.
1. `run_audio_prompt(audio, chat_history)`: Denna funktion konverterar en ljudfil till text med Whisper-modellens API och skickar den vidare till `run_text_prompt()`-funktionen.
1. Koden startar en Gradio-app som låter användare interagera med Phi 3 Mini 4K instruct-demo genom att skriva meddelanden eller ladda upp ljudfiler. Utdata visas som textmeddelanden i appen.

## Felsökning

Installation av Cuda GPU-drivrutiner

1. Se till att dina Linux-applikationer är uppdaterade

    ```bash
    sudo apt update
    ```

1. Installera Cuda-drivrutiner

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrera platsen för cuda-drivrutinen

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kontrollera Nvidia GPU-minnesstorlek (Krävs 12GB GPU-minne)

    ```bash
    nvidia-smi
    ```

1. Töm cache: Om du använder PyTorch kan du anropa torch.cuda.empty_cache() för att frigöra oanvänt cacheminne så att det kan användas av andra GPU-applikationer

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kontrollera Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Utför följande steg för att skapa en Hugging Face-token.

    - Gå till [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Välj **New token**.
    - Ange projektets **Name** som du vill använda.
    - Välj **Type** till **Write**.

> **Note**
>
> Om du stöter på följande fel:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> För att lösa detta, skriv följande kommando i din terminal.
>
> ```bash
> sudo ldconfig
> ```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.