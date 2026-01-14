<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:42:03+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sv"
}
-->
# Interaktiv Phi 3 Mini 4K Instruktionschatbot med Whisper

## Översikt

Den interaktiva Phi 3 Mini 4K instruktionschatboten är ett verktyg som låter användare interagera med Microsoft Phi 3 Mini 4K instruktionsdemo via text- eller ljudinmatning. Chatboten kan användas för olika uppgifter, såsom översättning, väderuppdateringar och allmän informationsinsamling.

### Kom igång

För att använda denna chatbot, följ helt enkelt dessa instruktioner:

1. Öppna en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I huvudfönstret i notebooken ser du ett chattgränssnitt med en textinmatningsruta och en "Send"-knapp.
3. För att använda textbaserad chatbot, skriv helt enkelt ditt meddelande i textinmatningsrutan och klicka på "Send"-knappen. Chatboten svarar med en ljudfil som kan spelas upp direkt i notebooken.

**Notera**: Detta verktyg kräver en GPU och tillgång till Microsoft Phi-3 och OpenAI Whisper-modellerna, vilka används för taligenkänning och översättning.

### GPU-krav

För att köra denna demo behöver du 12 GB GPU-minne.

Minneskraven för att köra **Microsoft-Phi-3-Mini-4K instruct** demot på en GPU beror på flera faktorer, såsom storleken på indata (ljud eller text), språket som används för översättning, modellens hastighet och tillgängligt minne på GPU:n.

Generellt är Whisper-modellen designad för att köras på GPU:er. Den rekommenderade minsta mängden GPU-minne för att köra Whisper-modellen är 8 GB, men den kan hantera större mängder minne vid behov.

Det är viktigt att notera att vid körning av stora datamängder eller en hög volym av förfrågningar på modellen kan mer GPU-minne krävas och/eller prestandaproblem kan uppstå. Det rekommenderas att testa ditt användningsfall med olika konfigurationer och övervaka minnesanvändningen för att bestämma optimala inställningar efter dina specifika behov.

## E2E-exempel för interaktiv Phi 3 Mini 4K Instruktionschatbot med Whisper

Jupyter notebooken med titeln [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) visar hur man använder Microsoft Phi 3 Mini 4K instruktionsdemo för att generera text från ljud- eller skriven textinmatning. Notebooken definierar flera funktioner:

1. `tts_file_name(text)`: Denna funktion genererar ett filnamn baserat på inmatad text för att spara den genererade ljudfilen.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denna funktion använder Edge TTS API för att generera en ljudfil från en lista av textbitar. Indata är listan med bitar, talhastighet, röstnamn och sökvägen för att spara den genererade ljudfilen.
1. `talk(input_text)`: Denna funktion genererar en ljudfil med Edge TTS API och sparar den med ett slumpmässigt filnamn i /content/audio katalogen. Indata är texten som ska konverteras till tal.
1. `run_text_prompt(message, chat_history)`: Denna funktion använder Microsoft Phi 3 Mini 4K instruktionsdemo för att generera en ljudfil från ett meddelande och lägger till det i chattloggen.
1. `run_audio_prompt(audio, chat_history)`: Denna funktion konverterar en ljudfil till text med Whisper-modellens API och skickar texten till `run_text_prompt()` funktionen.
1. Koden startar en Gradio-app som tillåter användare att interagera med Phi 3 Mini 4K instruktionsdemo antingen genom att skriva meddelanden eller ladda upp ljudfiler. Utdata visas som ett textmeddelande i appen.

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

1. Kontrollera Nvidia GPU-minnets storlek (Krävs 12GB GPU-minne)

    ```bash
    nvidia-smi
    ```

1. Rensa cache: Om du använder PyTorch kan du anropa torch.cuda.empty_cache() för att frigöra allt oanvänt cache-minne så att det kan användas av andra GPU-applikationer

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kontrollera Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Utför följande steg för att skapa en Hugging Face-token.

    - Navigera till [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Välj **New token**.
    - Ange projektets **Namn** du vill använda.
    - Välj **Typ** till **Write**.

> [!NOTE]
>
> Om du får följande fel:
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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell human översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->