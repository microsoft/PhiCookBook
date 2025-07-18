<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:19:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "no"
}
-->
# Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

## Oversikt

Den interaktive Phi 3 Mini 4K Instruct Chatbot er et verktøy som lar brukere samhandle med Microsoft Phi 3 Mini 4K instruct-demoen ved hjelp av tekst- eller lydinngang. Chatboten kan brukes til ulike oppgaver, som oversettelse, væroppdateringer og generell informasjonsinnhenting.

### Komme i gang

For å bruke denne chatboten, følg disse instruksjonene:

1. Åpne en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I hovedvinduet i notatboken vil du se et chattegrensesnitt med en tekstboks og en "Send"-knapp.
3. For å bruke tekstbasert chatbot, skriv meldingen din i tekstboksen og klikk på "Send"-knappen. Chatboten vil svare med en lydfil som kan spilles av direkte i notatboken.

**Note**: Dette verktøyet krever en GPU og tilgang til Microsoft Phi-3 og OpenAI Whisper-modellene, som brukes til talegjenkjenning og oversettelse.

### GPU-krav

For å kjøre denne demoen trenger du 12 GB GPU-minne.

Minnekravene for å kjøre **Microsoft-Phi-3-Mini-4K instruct** demoen på en GPU avhenger av flere faktorer, som størrelsen på inndata (lyd eller tekst), språket som brukes til oversettelse, modellens hastighet og tilgjengelig minne på GPU-en.

Generelt er Whisper-modellen designet for å kjøre på GPU-er. Anbefalt minimum GPU-minne for å kjøre Whisper-modellen er 8 GB, men den kan håndtere større mengder minne om nødvendig.

Det er viktig å merke seg at kjøring av store datamengder eller et høyt volum av forespørsler til modellen kan kreve mer GPU-minne og/eller føre til ytelsesproblemer. Det anbefales å teste bruken din med ulike konfigurasjoner og overvåke minnebruken for å finne optimale innstillinger for dine spesifikke behov.

## E2E-eksempel for Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

Jupyter-notatboken med tittelen [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) viser hvordan man bruker Microsoft Phi 3 Mini 4K instruct-demoen for å generere tekst fra lyd- eller skriftlig tekstinngang. Notatboken definerer flere funksjoner:

1. `tts_file_name(text)`: Denne funksjonen genererer et filnavn basert på inndatateksten for å lagre den genererte lydfilen.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denne funksjonen bruker Edge TTS API for å generere en lydfil fra en liste med tekstbiter. Inndataparamentrene er listen med biter, taletempo, stemmenavn og lagringssted for den genererte lydfilen.
1. `talk(input_text)`: Denne funksjonen genererer en lydfil ved å bruke Edge TTS API og lagrer den til et tilfeldig filnavn i /content/audio-mappen. Inndataparameteren er teksten som skal konverteres til tale.
1. `run_text_prompt(message, chat_history)`: Denne funksjonen bruker Microsoft Phi 3 Mini 4K instruct-demoen for å generere en lydfil fra en melding og legger den til i chatthistorikken.
1. `run_audio_prompt(audio, chat_history)`: Denne funksjonen konverterer en lydfil til tekst ved hjelp av Whisper-modellens API og sender den videre til `run_text_prompt()`-funksjonen.
1. Koden starter en Gradio-app som lar brukere samhandle med Phi 3 Mini 4K instruct-demoen ved enten å skrive meldinger eller laste opp lydfiler. Resultatet vises som en tekstmelding i appen.

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

1. Sjekk Nvidia GPU-minnestørrelse (krever 12 GB GPU-minne)

    ```bash
    nvidia-smi
    ```

1. Tøm cache: Hvis du bruker PyTorch, kan du kalle torch.cuda.empty_cache() for å frigjøre all ubrukt bufret minne slik at det kan brukes av andre GPU-applikasjoner

    ```python
    torch.cuda.empty_cache() 
    ```

1. Sjekk Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Utfør følgende for å opprette en Hugging Face-token.

    - Gå til [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Velg **New token**.
    - Skriv inn prosjektets **Name** du ønsker å bruke.
    - Velg **Type** til **Write**.

> **Note**
>
> Hvis du får følgende feil:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> For å løse dette, skriv følgende kommando i terminalen din.
>
> ```bash
> sudo ldconfig
> ```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.