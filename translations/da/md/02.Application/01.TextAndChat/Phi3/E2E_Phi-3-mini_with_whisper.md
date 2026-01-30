# Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

## Oversigt

Den Interaktive Phi 3 Mini 4K Instruct Chatbot er et værktøj, der gør det muligt for brugere at interagere med Microsoft Phi 3 Mini 4K instruct demo ved hjælp af tekst- eller lydinput. Chatbotten kan bruges til en række opgaver, såsom oversættelse, vejropdateringer og generel informationsindsamling.

### Kom Godt i Gang

For at bruge denne chatbot skal du blot følge disse instruktioner:

1. Åbn en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I hovedvinduet af notebook'en vil du se en chatboksgrænseflade med en tekstindtastningsboks og en "Send" knap.
3. For at bruge den tekstbaserede chatbot skal du blot skrive din besked i tekstindtastningsboksen og klikke på "Send" knappen. Chatbotten vil svare med en lydfil, der kan afspilles direkte i notebook'en.

**Bemærk**: Dette værktøj kræver en GPU og adgang til Microsoft Phi-3 og OpenAI Whisper modellerne, som bruges til talegenkendelse og oversættelse.

### GPU Krav

For at køre denne demo har du brug for 12Gb GPU-hukommelse.

Hukommelseskravene for at køre **Microsoft-Phi-3-Mini-4K instruct** demoen på en GPU afhænger af flere faktorer, såsom størrelsen af inputdataene (lyd eller tekst), sproget der bruges til oversættelse, modellens hastighed og den tilgængelige hukommelse på GPU'en.

Generelt er Whisper-modellen designet til at køre på GPU'er. Den anbefalede minimumsmængde GPU-hukommelse for at køre Whisper-modellen er 8 GB, men den kan håndtere større mængder hukommelse, hvis nødvendigt.

Det er vigtigt at bemærke, at kørsel af store datamængder eller høj volumen af forespørgsler på modellen kan kræve mere GPU-hukommelse og/eller forårsage ydelsesproblemer. Det anbefales at teste din brugssag med forskellige konfigurationer og overvåge hukommelsesforbruget for at bestemme de optimale indstillinger til dine specifikke behov.

## E2E Eksempel på Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

Jupyter notebooken med titlen [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrerer, hvordan man bruger Microsoft Phi 3 Mini 4K instruct Demo til at generere tekst fra lyd- eller tekstinput. Notebooken definerer flere funktioner:

1. `tts_file_name(text)`: Denne funktion genererer et filnavn baseret på inputteksten til at gemme den genererede lydfil.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denne funktion bruger Edge TTS API'en til at generere en lydfil ud fra en liste af tekststykker. Inputparametrene er listen af tekststykker, taletempoet, stemmenavnet og output-stien til at gemme den genererede lydfil.
1. `talk(input_text)`: Denne funktion genererer en lydfil ved hjælp af Edge TTS API'en og gemmer den under et tilfældigt filnavn i /content/audio mappen. Inputparameteren er den tekst, der skal konverteres til tale.
1. `run_text_prompt(message, chat_history)`: Denne funktion bruger Microsoft Phi 3 Mini 4K instruct demoen til at generere en lydfil ud fra en beskedinput og tilføjer den til chat-historikken.
1. `run_audio_prompt(audio, chat_history)`: Denne funktion konverterer en lydfil til tekst ved hjælp af Whisper model API'en og sender teksten videre til `run_text_prompt()` funktionen.
1. Koden starter en Gradio-app, der tillader brugere at interagere med Phi 3 Mini 4K instruct demoen ved enten at skrive beskeder eller uploade lydfiler. Output vises som en tekstbesked inden for appen.

## Fejlfinding

Installation af Cuda GPU drivere

1. Sørg for, at dine Linux-applikationer er opdaterede

    ```bash
    sudo apt update
    ```

1. Installer Cuda Drivere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrer cuda-driverens placering

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Tjek Nvidia GPU hukommelsesstørrelse (Kræver 12GB GPU Hukommelse)

    ```bash
    nvidia-smi
    ```

1. Tøm Cache: Hvis du bruger PyTorch, kan du kalde torch.cuda.empty_cache() for at frigive al ubrugt cache-hukommelse, så den kan bruges af andre GPU-applikationer

    ```python
    torch.cuda.empty_cache() 
    ```

1. Tjek Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Udfør følgende for at oprette et Hugging Face-token.

    - Naviger til [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vælg **New token**.
    - Indtast projektets **Navn**, som du vil bruge.
    - Vælg **Type** til **Write**.

> [!NOTE]
>
> Hvis du støder på følgende fejl:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> For at løse dette skal du skrive følgende kommando i din terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget skal betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->