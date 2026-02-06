# Interaktiv Phi 3 Mini 4K Veilednings-chatbot med Whisper

## Oversikt

Den interaktive Phi 3 Mini 4K veilednings-chatboten er et verktøy som lar brukere samhandle med Microsoft Phi 3 Mini 4K veiledningsdemo ved hjelp av tekst- eller lydinngang. Chatboten kan brukes til en rekke oppgaver, slik som oversettelse, væroppdateringer og generell informasjonsinnsamling.

### Komme i gang

For å bruke denne chatboten, følg disse instruksjonene:

1. Åpne et nytt [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I hovedvinduet til notatboken vil du se en chatteboks med et tekstinndataboks og en "Send" knapp.
3. For å bruke tekstbasert chatbot, skriv meldingen din i tekstinndataboksen og klikk "Send"-knappen. Chatboten vil svare med en lydfil som kan spilles direkte fra notatboken.

**Merk**: Dette verktøyet krever en GPU og tilgang til Microsoft Phi-3 og OpenAI Whisper-modellene, som brukes til talegjenkjenning og oversettelse.

### GPU-krav

For å kjøre denne demoen trenger du 12 GB GPU-minne.

Minnekravene for å kjøre **Microsoft-Phi-3-Mini-4K instruct** demoen på en GPU avhenger av flere faktorer, slik som størrelsen på inndata (lyd eller tekst), språket som brukes for oversettelse, modellens hastighet og tilgjengelig minne på GPUen.

Generelt er Whisper-modellen designet for å kjøre på GPUer. Anbefalt minimum mengde GPU-minne for å kjøre Whisper-modellen er 8 GB, men den kan håndtere større mengder minne ved behov.

Det er viktig å merke seg at kjøring av store datamengder eller et høyt volum forespørsler til modellen kan kreve mer GPU-minne og/eller kan føre til ytelsesproblemer. Det anbefales å teste din brukstilfelle med ulike konfigurasjoner og overvåke minnebruk for å finne optimale innstillinger for dine spesifikke behov.

## E2E-eksempel for Interaktiv Phi 3 Mini 4K Veilednings-chatbot med Whisper

Jupyter-notatboken med tittelen [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrerer hvordan du bruker Microsoft Phi 3 Mini 4K veiledningsdemo for å generere tekst fra lyd eller skriftlig tekstinngang. Notatboken definerer flere funksjoner:

1. `tts_file_name(text)`: Denne funksjonen genererer et filnavn basert på inndata-teksten for å lagre den genererte lydfilen.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denne funksjonen bruker Edge TTS API til å generere en lydfil fra en liste med tekstbiter. Inndataparamerne er listen med biter, talefart, stemmenavn og utdata-sti for lagring av lydfilen.
1. `talk(input_text)`: Denne funksjonen genererer en lydfil ved å bruke Edge TTS API og lagrer den til et tilfeldig filnavn i /content/audio-katalogen. Inndata er teksten som skal konverteres til tale.
1. `run_text_prompt(message, chat_history)`: Denne funksjonen bruker Microsoft Phi 3 Mini 4K veiledningsdemo til å generere en lydfil fra meldingsinngangen og legger den til i chathistorikken.
1. `run_audio_prompt(audio, chat_history)`: Denne funksjonen konverterer en lydfil til tekst ved hjelp av Whisper-modellens API og sender det til `run_text_prompt()` funksjonen.
1. Koden starter en Gradio-app som lar brukere samhandle med Phi 3 Mini 4K veiledningsdemo ved å enten skrive meldinger eller laste opp lydfiler. Utdata vises som tekstmelding i appen.

## Feilsøking

Installere Cuda GPU-drivere

1. Sørg for at Linux-applikasjonene dine er oppdaterte

    ```bash
    sudo apt update
    ```

1. Installer Cuda-drivere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrer plasseringen til cuda-driveren

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Sjekk Nvidia GPU-minnestørrelse (kreves 12 GB GPU-minne)

    ```bash
    nvidia-smi
    ```

1. Tøm Cache: Hvis du bruker PyTorch, kan du kalle torch.cuda.empty_cache() for å frigjøre alt ubrukt bufret minne slik at det kan brukes av andre GPU-applikasjoner

    ```python
    torch.cuda.empty_cache() 
    ```

1. Sjekk Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Utfør følgende for å lage en Hugging Face-token.

    - Gå til [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Velg **New token**.
    - Skriv inn prosjektets **Navn** du vil bruke.
    - Velg **Type** til **Write**.

> [!NOTE]
>
> Hvis du får følgende feil:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> For å løse dette, skriv inn følgende kommando i terminalen din.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->