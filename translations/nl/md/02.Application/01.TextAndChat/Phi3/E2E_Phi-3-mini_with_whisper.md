<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T15:50:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "nl"
}
-->
# Interactieve Phi 3 Mini 4K Instruct Chatbot met Whisper

## Overzicht

De Interactieve Phi 3 Mini 4K Instruct Chatbot is een hulpmiddel waarmee gebruikers kunnen communiceren met de Microsoft Phi 3 Mini 4K instructie-demo via tekst- of audio-invoer. De chatbot kan worden gebruikt voor diverse taken, zoals vertalen, weersupdates en algemene informatieverzameling.

### Aan de slag

Om deze chatbot te gebruiken, volgt u gewoon deze instructies:

1. Open een nieuwe [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. In het hoofdvenster van de notebook ziet u een chatboxinterface met een tekstinvoerveld en een "Verzenden" knop.
3. Om de tekstgebaseerde chatbot te gebruiken, typt u eenvoudig uw bericht in het tekstinvoerveld en klikt u op de knop "Verzenden". De chatbot reageert met een audio bestand dat direct vanuit de notebook kan worden afgespeeld.

**Opmerking**: Dit hulpmiddel vereist een GPU en toegang tot de Microsoft Phi-3 en OpenAI Whisper-modellen, die worden gebruikt voor spraakherkenning en vertaling.

### GPU Vereisten

Om deze demo uit te voeren heeft u 12 GB GPU-geheugen nodig.

De geheugeneisen voor het uitvoeren van de **Microsoft-Phi-3-Mini-4K instruct** demo op een GPU zijn afhankelijk van verschillende factoren, zoals de grootte van de invoergegevens (audio of tekst), de gebruikte taal voor vertaling, de snelheid van het model en het beschikbare geheugen op de GPU.

Over het algemeen is het Whisper-model ontworpen om op GPU's te draaien. De aanbevolen minimumhoeveelheid GPU-geheugen voor het draaien van het Whisper-model is 8 GB, maar het kan grotere hoeveelheden geheugen verwerken indien nodig.

Het is belangrijk op te merken dat het verwerken van een grote hoeveelheid gegevens of een hoog volume aan verzoeken op het model mogelijk meer GPU-geheugen vereist en/of prestatieproblemen kan veroorzaken. Het wordt aanbevolen uw gebruikssituatie met verschillende configuraties te testen en het geheugengebruik te monitoren om de optimale instellingen voor uw specifieke behoeften te bepalen.

## E2E Voorbeeld voor Interactieve Phi 3 Mini 4K Instruct Chatbot met Whisper

De jupyter notebook met de titel [Interactieve Phi 3 Mini 4K Instruct Chatbot met Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstreert hoe u de Microsoft Phi 3 Mini 4K instructie Demo kunt gebruiken om tekst te genereren vanuit audio- of geschreven tekstinvoer. De notebook definieert verschillende functies:

1. `tts_file_name(text)`: Deze functie genereert een bestandsnaam op basis van de invoertekst voor het opslaan van het gegenereerde audiobestand.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Deze functie gebruikt de Edge TTS API om een audiobestand te genereren vanuit een lijst met tekststukken. De invoerparameters zijn de lijst met stukken, de spreeksnelheid, de naam van de stem en het uitvoerpad voor het opslaan van het gegenereerde audiobestand.
1. `talk(input_text)`: Deze functie genereert een audiobestand door gebruik te maken van de Edge TTS API en slaat het op onder een willekeurige bestandsnaam in de map /content/audio. De invoerparameter is de tekst die naar spraak moet worden omgezet.
1. `run_text_prompt(message, chat_history)`: Deze functie gebruikt de Microsoft Phi 3 Mini 4K instructie-demo om een audiobestand te genereren op basis van een berichtinvoer en voegt dit toe aan de chatgeschiedenis.
1. `run_audio_prompt(audio, chat_history)`: Deze functie zet een audiobestand om in tekst met behulp van de Whisper model API en geeft dit door aan de functie `run_text_prompt()`.
1. De code start een Gradio-app die gebruikers in staat stelt te communiceren met de Phi 3 Mini 4K instructie-demo door berichten te typen of audiobestanden te uploaden. De output wordt weergegeven als een tekstbericht binnen de app.

## Problemen oplossen

Cuda GPU drivers installeren

1. Zorg ervoor dat uw Linux-applicaties up-to-date zijn

    ```bash
    sudo apt update
    ```

1. Installeer Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registreer de locatie van de cuda-driver

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Controleer de grootte van het Nvidia GPU-geheugen (12GB GPU-geheugen vereist)

    ```bash
    nvidia-smi
    ```

1. Cache legen: Als u PyTorch gebruikt, kunt u torch.cuda.empty_cache() aanroepen om alle ongebruikte gecachte geheugen vrij te geven zodat het door andere GPU-toepassingen kan worden gebruikt

    ```python
    torch.cuda.empty_cache() 
    ```

1. Controleren Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Voer de volgende taken uit om een Hugging Face-token aan te maken.

    - Ga naar de [Hugging Face Token Settings pagina](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecteer **Nieuwe token**.
    - Voer de project **Naam** in die u wilt gebruiken.
    - Selecteer **Type** op **Schrijven**.

> [!NOTE]
>
> Als u de volgende foutmelding tegenkomt:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Om dit op te lossen, voert u de volgende opdracht uit in uw terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->