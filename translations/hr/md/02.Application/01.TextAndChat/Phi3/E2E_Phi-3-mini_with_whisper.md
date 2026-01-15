<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T16:12:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hr"
}
-->
# Interaktivni Phi 3 Mini 4K Instruct Chatbot s Whisperom

## Pregled

Interaktivni Phi 3 Mini 4K Instruct Chatbot je alat koji korisnicima omogućava interakciju s Microsoft Phi 3 Mini 4K instruct demo verzijom pomoću tekstualnog ili audio unosa. Chatbot se može koristiti za razne zadatke, kao što su prevođenje, vremenske prognoze i općenito prikupljanje informacija.

### Početak rada

Za korištenje ovog chatbota jednostavno slijedite ove upute:

1. Otvorite novi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. U glavnom prozoru bilježnice vidjet ćete sučelje chatboxa s tekstualnim unosom i gumbom "Send".
3. Za korištenje chatbota temeljenog na tekstu, jednostavno upišite svoju poruku u tekstualno polje za unos i kliknite gumb "Send". Chatbot će odgovoriti audio datotekom koju je moguće reproducirati izravno unutar bilježnice.

**Napomena**: Ovaj alat zahtijeva GPU i pristup modelima Microsoft Phi-3 i OpenAI Whisper, koji se koriste za prepoznavanje govora i prijevod.

### Zahtjevi za GPU

Za pokretanje ovog demo primjera potrebna vam je 12GB GPU memorije.

Zahtjevi za memoriju pri pokretanju **Microsoft-Phi-3-Mini-4K instruct** demo verzije na GPU-u ovise o nekoliko čimbenika, kao što su veličina ulaznih podataka (audio ili tekst), jezik koji se koristi za prijevod, brzina modela i dostupna memorija na GPU-u.

Općenito, Whisper model je dizajniran za rad na GPU-ima. Preporučena minimalna količina GPU memorije za pokretanje Whisper modela jest 8 GB, ali može podnijeti veće količine memorije ako je potrebno.

Važno je napomenuti da pokretanje velikih količina podataka ili velikog volumena zahtjeva na model može zahtijevati više GPU memorije i/ili može uzrokovati probleme s izvedbom. Preporučuje se testirati svoj slučaj korištenja s različitim konfiguracijama i pratiti korištenje memorije kako biste odredili optimalne postavke za vaše specifične potrebe.

## E2E Primjer za Interaktivni Phi 3 Mini 4K Instruct Chatbot s Whisperom

Jupyter bilježnica pod nazivom [Interaktivni Phi 3 Mini 4K Instruct Chatbot s Whisperom](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) pokazuje kako koristiti Microsoft Phi 3 Mini 4K instruct demo za generiranje teksta iz audio ili pisanog tekstualnog unosa. Bilježnica definira nekoliko funkcija:

1. `tts_file_name(text)`: Ova funkcija generira ime datoteke na temelju unesenog teksta za spremanje generirane audio datoteke.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ova funkcija koristi Edge TTS API za generiranje audio datoteke iz liste dijelova unesenog teksta. Ulazni parametri su lista dijelova, brzina govora, ime glasa i putanja za spremanje generirane audio datoteke.
1. `talk(input_text)`: Ova funkcija generira audio datoteku koristeći Edge TTS API i sprema ju pod slučajnim imenom u direktorij /content/audio. Ulazni parametar je tekst koji se pretvara u govor.
1. `run_text_prompt(message, chat_history)`: Ova funkcija koristi Microsoft Phi 3 Mini 4K instruct demo za generiranje audio datoteke iz unesene poruke i dodaje je u povijest chata.
1. `run_audio_prompt(audio, chat_history)`: Ova funkcija pretvara audio datoteku u tekst koristeći Whisper model API i prosljeđuje ga funkciji `run_text_prompt()`.
1. Kod pokreće Gradio aplikaciju koja omogućava korisnicima interakciju s Phi 3 Mini 4K instruct demo verzijom tako da unose poruke ili prenose audio datoteke. Izlaz se prikazuje kao tekstualna poruka unutar aplikacije.

## Rješavanje problema

Instalacija Cuda GPU drajvera

1. Provjerite jesu li vaši Linux sustavi ažurirani

    ```bash
    sudo apt update
    ```

1. Instalirajte Cuda drajvere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrirajte lokaciju Cuda drajvera

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Provjerite veličinu Nvidia GPU memorije (potrebno 12GB GPU memorije)

    ```bash
    nvidia-smi
    ```

1. Pražnjenje predmemorije: Ako koristite PyTorch, možete pozvati torch.cuda.empty_cache() kako biste oslobodili svu neiskorištenu predmemoriju i omogućili njezino korištenje drugim GPU aplikacijama

    ```python
    torch.cuda.empty_cache() 
    ```

1. Provjera Nvidia Cuda verzije

    ```bash
    nvcc --version
    ```

1. Izvršite sljedeće korake da biste kreirali Hugging Face token.

    - Otvorite [Hugging Face Token Settings stranica](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Odaberite **New token**.
    - Unesite naziv projekta pod **Name** koji želite koristiti.
    - Odaberite **Type** na **Write**.

> [!NOTE]
>
> Ako se pojavi sljedeća pogreška:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Da biste to riješili, unesite sljedeću naredbu u svoj terminal.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->