<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:20:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "nl"
}
-->
# Interactieve Phi 3 Mini 4K Instruct Chatbot met Whisper

## Overzicht

De Interactieve Phi 3 Mini 4K Instruct Chatbot is een tool waarmee gebruikers kunnen communiceren met de Microsoft Phi 3 Mini 4K instructie-demo via tekst- of audio-invoer. De chatbot kan voor verschillende taken worden gebruikt, zoals vertalingen, weersupdates en algemene informatieverzameling.

### Aan de slag

Volg deze stappen om de chatbot te gebruiken:

1. Open een nieuw [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. In het hoofdvenster van de notebook zie je een chatbox-interface met een tekstinvoerveld en een "Send" knop.
3. Om de tekstgebaseerde chatbot te gebruiken, typ je eenvoudig je bericht in het tekstinvoerveld en klik je op de "Send" knop. De chatbot reageert met een audiobestand dat direct binnen de notebook kan worden afgespeeld.

**Note**: Deze tool vereist een GPU en toegang tot de Microsoft Phi-3 en OpenAI Whisper modellen, die worden gebruikt voor spraakherkenning en vertaling.

### GPU-vereisten

Voor het draaien van deze demo heb je 12 GB GPU-geheugen nodig.

De geheugeneisen voor het uitvoeren van de **Microsoft-Phi-3-Mini-4K instruct** demo op een GPU hangen af van verschillende factoren, zoals de grootte van de invoergegevens (audio of tekst), de taal die voor vertaling wordt gebruikt, de snelheid van het model en het beschikbare geheugen op de GPU.

Over het algemeen is het Whisper-model ontworpen om op GPU's te draaien. De aanbevolen minimale hoeveelheid GPU-geheugen voor het draaien van het Whisper-model is 8 GB, maar het kan grotere hoeveelheden geheugen aan indien nodig.

Het is belangrijk om te weten dat het verwerken van grote hoeveelheden data of een hoog volume aan verzoeken het GPU-geheugen kan belasten en/of prestatieproblemen kan veroorzaken. Het is aan te raden je gebruikssituatie te testen met verschillende configuraties en het geheugengebruik te monitoren om zo de optimale instellingen voor jouw specifieke behoeften te bepalen.

## E2E Voorbeeld voor Interactieve Phi 3 Mini 4K Instruct Chatbot met Whisper

De Jupyter-notebook met de titel [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) laat zien hoe je de Microsoft Phi 3 Mini 4K instructie-demo kunt gebruiken om tekst te genereren vanuit audio- of geschreven tekstinvoer. De notebook definieert verschillende functies:

1. `tts_file_name(text)`: Deze functie genereert een bestandsnaam op basis van de invoertekst om het gegenereerde audiobestand op te slaan.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Deze functie gebruikt de Edge TTS API om een audiobestand te genereren uit een lijst met tekstfragmenten. De invoerparameters zijn de lijst met fragmenten, de spreeksnelheid, de naam van de stem en het pad waar het gegenereerde audiobestand wordt opgeslagen.
1. `talk(input_text)`: Deze functie genereert een audiobestand met behulp van de Edge TTS API en slaat dit op onder een willekeurige bestandsnaam in de /content/audio map. De invoerparameter is de tekst die omgezet moet worden naar spraak.
1. `run_text_prompt(message, chat_history)`: Deze functie gebruikt de Microsoft Phi 3 Mini 4K instructie-demo om een audiobestand te genereren op basis van een berichtinvoer en voegt dit toe aan de chatgeschiedenis.
1. `run_audio_prompt(audio, chat_history)`: Deze functie zet een audiobestand om in tekst met behulp van de Whisper model API en geeft dit door aan de functie `run_text_prompt()`.
1. De code start een Gradio-app waarmee gebruikers kunnen communiceren met de Phi 3 Mini 4K instructie-demo door berichten te typen of audiobestanden te uploaden. De output wordt als tekstbericht binnen de app weergegeven.

## Problemen oplossen

Cuda GPU drivers installeren

1. Zorg dat je Linux-applicaties up-to-date zijn

    ```bash
    sudo apt update
    ```

1. Installeer Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registreer de locatie van de cuda driver

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Controleer de grootte van het Nvidia GPU-geheugen (Vereist 12GB GPU-geheugen)

    ```bash
    nvidia-smi
    ```

1. Cache legen: Als je PyTorch gebruikt, kun je torch.cuda.empty_cache() aanroepen om alle ongebruikte gecachte geheugen vrij te maken zodat het door andere GPU-applicaties gebruikt kan worden

    ```python
    torch.cuda.empty_cache() 
    ```

1. Controleer Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Voer de volgende stappen uit om een Hugging Face token aan te maken.

    - Ga naar de [Hugging Face Token Settings pagina](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecteer **New token**.
    - Voer de project **Naam** in die je wilt gebruiken.
    - Kies **Type** als **Write**.

> **Note**
>
> Als je de volgende foutmelding tegenkomt:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Om dit op te lossen, typ je het volgende commando in je terminal.
>
> ```bash
> sudo ldconfig
> ```

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.