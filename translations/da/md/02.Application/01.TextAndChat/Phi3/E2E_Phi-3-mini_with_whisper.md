<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:19:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "da"
}
-->
# Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

## Oversigt

Den Interaktive Phi 3 Mini 4K Instruct Chatbot er et værktøj, der giver brugere mulighed for at interagere med Microsoft Phi 3 Mini 4K instruct-demoen ved hjælp af tekst- eller lydinput. Chatbotten kan bruges til forskellige opgaver, såsom oversættelse, vejrudsigter og generel informationsindsamling.

### Kom godt i gang

For at bruge denne chatbot skal du blot følge disse instruktioner:

1. Åbn en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I hovedvinduet i notebooken vil du se en chatboks med en tekstindtastningsboks og en "Send"-knap.
3. For at bruge tekstbaseret chatbot skal du blot skrive din besked i tekstfeltet og klikke på "Send"-knappen. Chatbotten vil svare med en lydfil, som kan afspilles direkte i notebooken.

**Note**: Dette værktøj kræver en GPU og adgang til Microsoft Phi-3 og OpenAI Whisper modellerne, som bruges til talegenkendelse og oversættelse.

### GPU-krav

For at køre denne demo skal du have 12 GB GPU-hukommelse.

Hukommelseskravene for at køre **Microsoft-Phi-3-Mini-4K instruct** demoen på en GPU afhænger af flere faktorer, såsom størrelsen på inputdata (lyd eller tekst), sproget der oversættes til, modellens hastighed og den tilgængelige hukommelse på GPU’en.

Generelt er Whisper-modellen designet til at køre på GPU’er. Den anbefalede minimumsmængde GPU-hukommelse til at køre Whisper-modellen er 8 GB, men den kan håndtere større mængder hukommelse, hvis det er nødvendigt.

Det er vigtigt at bemærke, at kørsel af store datamængder eller et højt antal forespørgsler på modellen kan kræve mere GPU-hukommelse og/eller kan forårsage ydelsesproblemer. Det anbefales at teste dit brugsscenarie med forskellige konfigurationer og overvåge hukommelsesforbruget for at finde de optimale indstillinger til dine specifikke behov.

## E2E-eksempel på Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

Jupyter-notebooken med titlen [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) viser, hvordan man bruger Microsoft Phi 3 Mini 4K instruct-demoen til at generere tekst ud fra lyd- eller skriftligt input. Notebooken definerer flere funktioner:

1. `tts_file_name(text)`: Denne funktion genererer et filnavn baseret på inputteksten til at gemme den genererede lydfil.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denne funktion bruger Edge TTS API til at generere en lydfil ud fra en liste af tekststykker. Inputparametrene er listen af tekststykker, taletempo, stemmenavn og outputsti til at gemme den genererede lydfil.
1. `talk(input_text)`: Denne funktion genererer en lydfil ved hjælp af Edge TTS API og gemmer den under et tilfældigt filnavn i /content/audio-mappen. Inputparameteren er den tekst, der skal konverteres til tale.
1. `run_text_prompt(message, chat_history)`: Denne funktion bruger Microsoft Phi 3 Mini 4K instruct-demoen til at generere en lydfil ud fra en besked og tilføjer den til chat-historikken.
1. `run_audio_prompt(audio, chat_history)`: Denne funktion konverterer en lydfil til tekst ved hjælp af Whisper model API’en og sender den videre til `run_text_prompt()` funktionen.
1. Koden starter en Gradio-app, som giver brugere mulighed for at interagere med Phi 3 Mini 4K instruct-demoen ved enten at skrive beskeder eller uploade lydfiler. Output vises som en tekstbesked i appen.

## Fejlfinding

Installation af Cuda GPU-drivere

1. Sørg for, at dine Linux-applikationer er opdaterede

    ```bash
    sudo apt update
    ```

1. Installer Cuda-drivere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrer placeringen af cuda-driveren

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Tjek Nvidia GPU-hukommelsesstørrelse (Kræver 12GB GPU-hukommelse)

    ```bash
    nvidia-smi
    ```

1. Tøm cache: Hvis du bruger PyTorch, kan du kalde torch.cuda.empty_cache() for at frigive al ubrugt cache-hukommelse, så den kan bruges af andre GPU-applikationer

    ```python
    torch.cuda.empty_cache() 
    ```

1. Tjek Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Udfør følgende trin for at oprette en Hugging Face-token.

    - Gå til [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vælg **New token**.
    - Indtast det projekt **Name**, du vil bruge.
    - Vælg **Type** til **Write**.

> **Note**
>
> Hvis du støder på følgende fejl:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> For at løse dette, skriv følgende kommando i din terminal.
>
> ```bash
> sudo ldconfig
> ```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.