<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:23:38+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hr"
}
-->
# Interaktivni Phi 3 Mini 4K Instruct Chatbot s Whisperom

## Pregled

Interaktivni Phi 3 Mini 4K Instruct Chatbot je alat koji korisnicima omogućuje interakciju s Microsoft Phi 3 Mini 4K instruct demo verzijom putem tekstualnog ili audio unosa. Chatbot se može koristiti za razne zadatke, poput prevođenja, vremenskih prognoza i općeg prikupljanja informacija.

### Početak rada

Za korištenje ovog chatbota, jednostavno slijedite ove upute:

1. Otvorite novi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. U glavnom prozoru bilježnice vidjet ćete sučelje chatboxa s tekstualnim unosom i gumbom "Send".
3. Za korištenje tekstualnog chatbota, jednostavno upišite svoju poruku u tekstualni okvir i kliknite gumb "Send". Chatbot će odgovoriti audio datotekom koju možete reproducirati izravno unutar bilježnice.

**Note**: Ovaj alat zahtijeva GPU i pristup Microsoft Phi-3 i OpenAI Whisper modelima, koji se koriste za prepoznavanje govora i prevođenje.

### Zahtjevi za GPU

Za pokretanje ove demo verzije potrebna vam je 12 GB GPU memorije.

Zahtjevi za memoriju pri pokretanju **Microsoft-Phi-3-Mini-4K instruct** demo verzije na GPU-u ovise o nekoliko faktora, poput veličine ulaznih podataka (audio ili tekst), jezika koji se koristi za prevođenje, brzine modela i dostupne memorije na GPU-u.

Općenito, Whisper model je dizajniran za rad na GPU-ima. Preporučena minimalna količina GPU memorije za pokretanje Whisper modela je 8 GB, ali može podržati i veće količine memorije ako je potrebno.

Važno je napomenuti da pokretanje velikih količina podataka ili velikog broja zahtjeva na model može zahtijevati više GPU memorije i/ili može uzrokovati probleme s performansama. Preporučuje se testirati vaš slučaj korištenja s različitim konfiguracijama i pratiti korištenje memorije kako biste odredili optimalne postavke za vaše specifične potrebe.

## E2E Primjer za Interaktivni Phi 3 Mini 4K Instruct Chatbot s Whisperom

Jupyter bilježnica pod nazivom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) prikazuje kako koristiti Microsoft Phi 3 Mini 4K instruct demo za generiranje teksta iz audio ili pisanog unosa. Bilježnica definira nekoliko funkcija:

1. `tts_file_name(text)`: Ova funkcija generira ime datoteke na temelju unesenog teksta za spremanje generirane audio datoteke.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ova funkcija koristi Edge TTS API za generiranje audio datoteke iz liste dijelova unesenog teksta. Ulazni parametri su lista dijelova, brzina govora, ime glasa i put za spremanje generirane audio datoteke.
1. `talk(input_text)`: Ova funkcija generira audio datoteku koristeći Edge TTS API i sprema je pod nasumičnim imenom u direktorij /content/audio. Ulazni parametar je tekst koji se pretvara u govor.
1. `run_text_prompt(message, chat_history)`: Ova funkcija koristi Microsoft Phi 3 Mini 4K instruct demo za generiranje audio datoteke iz unesene poruke i dodaje je u povijest chata.
1. `run_audio_prompt(audio, chat_history)`: Ova funkcija pretvara audio datoteku u tekst koristeći Whisper model API i prosljeđuje ga funkciji `run_text_prompt()`.
1. Kod pokreće Gradio aplikaciju koja korisnicima omogućuje interakciju s Phi 3 Mini 4K instruct demo verzijom bilo unosom poruka ili učitavanjem audio datoteka. Izlaz se prikazuje kao tekstualna poruka unutar aplikacije.

## Rješavanje problema

Instalacija Cuda GPU drajvera

1. Provjerite jesu li vaše Linux aplikacije ažurirane

    ```bash
    sudo apt update
    ```

1. Instalirajte Cuda drajvere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrirajte lokaciju cuda drajvera

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Provjera veličine Nvidia GPU memorije (potrebno 12GB GPU memorije)

    ```bash
    nvidia-smi
    ```

1. Pražnjenje cachea: Ako koristite PyTorch, možete pozvati torch.cuda.empty_cache() za oslobađanje sve neiskorištene predmemorirane memorije kako bi je mogle koristiti druge GPU aplikacije

    ```python
    torch.cuda.empty_cache() 
    ```

1. Provjera Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Izvršite sljedeće korake za kreiranje Hugging Face tokena.

    - Posjetite [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Odaberite **New token**.
    - Unesite naziv projekta koji želite koristiti.
    - Odaberite **Type** na **Write**.

> **Note**
>
> Ako naiđete na sljedeću grešku:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Za rješavanje problema, upišite sljedeću naredbu u terminal.
>
> ```bash
> sudo ldconfig
> ```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.