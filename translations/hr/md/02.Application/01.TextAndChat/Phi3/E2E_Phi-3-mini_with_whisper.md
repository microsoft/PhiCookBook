<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:34:52+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hr"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Pregled

Interactive Phi 3 Mini 4K Instruct Chatbot je alat koji korisnicima omogućuje interakciju s Microsoft Phi 3 Mini 4K instruct demo verzijom putem teksta ili audio unosa. Chatbot se može koristiti za razne zadatke, poput prevođenja, vremenskih informacija i općeg prikupljanja podataka.

### Početak rada

Za korištenje ovog chatbota, jednostavno slijedite ove upute:

1. Otvorite novi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. U glavnom prozoru bilježnice vidjet ćete sučelje chatboxa s tekstualnim unosnim poljem i gumbom "Send".
3. Za korištenje chatbota baziranog na tekstu, jednostavno upišite svoju poruku u tekstualno polje i kliknite gumb "Send". Chatbot će odgovoriti audio datotekom koju možete reproducirati izravno u bilježnici.

**Note**: Ovaj alat zahtijeva GPU i pristup Microsoft Phi-3 i OpenAI Whisper modelima, koji se koriste za prepoznavanje govora i prijevod.

### Zahtjevi za GPU

Za pokretanje ove demo verzije potrebna vam je 12GB GPU memorije.

Zahtjevi za memoriju pri pokretanju **Microsoft-Phi-3-Mini-4K instruct** demo verzije na GPU-u ovise o nekoliko faktora, poput veličine ulaznih podataka (audio ili tekst), jezika koji se koristi za prijevod, brzine modela i dostupne memorije na GPU-u.

Općenito, Whisper model je dizajniran za rad na GPU-ima. Preporučena minimalna količina GPU memorije za pokretanje Whisper modela je 8 GB, ali može podržati i veće količine memorije ako je potrebno.

Važno je napomenuti da pokretanje velikih količina podataka ili velikog broja zahtjeva na modelu može zahtijevati više GPU memorije i/ili može uzrokovati probleme s performansama. Preporučuje se testirati svoj slučaj korištenja s različitim konfiguracijama i pratiti potrošnju memorije kako biste odredili optimalne postavke za svoje specifične potrebe.

## E2E Primjer za Interactive Phi 3 Mini 4K Instruct Chatbot s Whisper

Jupyter bilježnica pod nazivom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) pokazuje kako koristiti Microsoft Phi 3 Mini 4K instruct Demo za generiranje teksta iz audio ili pisanog unosa. Bilježnica definira nekoliko funkcija:

1. `tts_file_name(text)`: Ova funkcija generira ime datoteke na temelju ulaznog teksta za spremanje generirane audio datoteke.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ova funkcija koristi Edge TTS API za generiranje audio datoteke iz liste dijelova ulaznog teksta. Ulazni parametri su lista dijelova, brzina govora, ime glasa i izlazna putanja za spremanje generirane audio datoteke.
1. `talk(input_text)`: Ova funkcija generira audio datoteku koristeći Edge TTS API i sprema je pod nasumičnim imenom u direktorij /content/audio. Ulazni parametar je tekst koji se pretvara u govor.
1. `run_text_prompt(message, chat_history)`: Ova funkcija koristi Microsoft Phi 3 Mini 4K instruct demo za generiranje audio datoteke iz poruke i dodaje je u povijest chata.
1. `run_audio_prompt(audio, chat_history)`: Ova funkcija pretvara audio datoteku u tekst koristeći Whisper model API i prosljeđuje ga funkciji `run_text_prompt()`.
1. Kod pokreće Gradio aplikaciju koja korisnicima omogućuje interakciju s Phi 3 Mini 4K instruct demo verzijom tako da upisuju poruke ili učitavaju audio datoteke. Izlaz se prikazuje kao tekstualna poruka unutar aplikacije.

## Rješavanje problema

Instalacija Cuda GPU drivera

1. Provjerite jesu li vaše Linux aplikacije ažurirane

    ```bash
    sudo apt update
    ```

1. Instalirajte Cuda drivere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrirajte lokaciju cuda drivera

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Provjera veličine Nvidia GPU memorije (potrebno 12GB GPU memorije)

    ```bash
    nvidia-smi
    ```

1. Pražnjenje cachea: Ako koristite PyTorch, možete pozvati torch.cuda.empty_cache() kako biste oslobodili svu neiskorištenu predmemoriranu memoriju da bi je mogle koristiti druge GPU aplikacije

    ```python
    torch.cuda.empty_cache() 
    ```

1. Provjera Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Obavite sljedeće korake za kreiranje Hugging Face tokena.

    - Idite na [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Odaberite **New token**.
    - Unesite naziv projekta **Name** koji želite koristiti.
    - Odaberite **Type** na **Write**.

> **Note**
>
> Ako naiđete na sljedeću grešku:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Da biste to riješili, upišite sljedeću naredbu u terminal.
>
> ```bash
> sudo ldconfig
> ```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.