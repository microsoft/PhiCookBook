<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:34:41+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sr"
}
-->
# Interaktivni Phi 3 Mini 4K Instruct Chatbot sa Whisper-om

## Pregled

Interaktivni Phi 3 Mini 4K Instruct Chatbot je alat koji korisnicima omogućava da komuniciraju sa Microsoft Phi 3 Mini 4K instruct demo-om koristeći tekstualni ili audio unos. Chatbot se može koristiti za razne zadatke, kao što su prevođenje, vremenske prognoze i prikupljanje opštih informacija.

### Početak rada

Da biste koristili ovaj chatbot, pratite sledeća uputstva:

1. Otvorite novi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. U glavnom prozoru beležnice videćete interfejs chatbox-a sa poljem za unos teksta i dugmetom "Send".
3. Za korišćenje chatbota baziranog na tekstu, jednostavno unesite poruku u polje za unos teksta i kliknite na dugme "Send". Chatbot će odgovoriti audio fajlom koji može biti direktno pušten iz same beležnice.

**Note**: Ovaj alat zahteva GPU i pristup Microsoft Phi-3 i OpenAI Whisper modelima, koji se koriste za prepoznavanje govora i prevođenje.

### Zahtevi za GPU

Za pokretanje ovog demo-a potrebno je 12GB memorije na GPU.

Zahtevi za memoriju prilikom pokretanja **Microsoft-Phi-3-Mini-4K instruct** demo-a na GPU-u zavise od nekoliko faktora, kao što su veličina ulaznih podataka (audio ili tekst), jezik koji se koristi za prevođenje, brzina modela i dostupna memorija na GPU-u.

Generalno, Whisper model je dizajniran da radi na GPU-ima. Preporučena minimalna količina memorije za pokretanje Whisper modela je 8 GB, ali može podržati i veće količine memorije po potrebi.

Važno je napomenuti da obrada velikih količina podataka ili veliki broj zahteva na model može zahtevati više GPU memorije i/ili može izazvati probleme sa performansama. Preporučuje se da testirate svoj slučaj upotrebe sa različitim konfiguracijama i pratite korišćenje memorije kako biste odredili optimalna podešavanja za vaše specifične potrebe.

## E2E primer za Interaktivni Phi 3 Mini 4K Instruct Chatbot sa Whisper-om

Jupyter beležnica pod nazivom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) pokazuje kako koristiti Microsoft Phi 3 Mini 4K instruct Demo za generisanje teksta iz audio ili pisanog teksta. Beležnica definiše nekoliko funkcija:

1. `tts_file_name(text)`: Ova funkcija generiše ime fajla na osnovu ulaznog teksta za čuvanje generisanog audio fajla.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ova funkcija koristi Edge TTS API za generisanje audio fajla iz liste delova ulaznog teksta. Ulazni parametri su lista delova, brzina govora, ime glasa i putanja za čuvanje generisanog audio fajla.
1. `talk(input_text)`: Ova funkcija generiše audio fajl koristeći Edge TTS API i čuva ga pod slučajnim imenom u direktorijumu /content/audio. Ulazni parametar je tekst koji se konvertuje u govor.
1. `run_text_prompt(message, chat_history)`: Ova funkcija koristi Microsoft Phi 3 Mini 4K instruct demo za generisanje audio fajla iz unosa poruke i dodaje ga u istoriju četa.
1. `run_audio_prompt(audio, chat_history)`: Ova funkcija pretvara audio fajl u tekst koristeći Whisper model API i prosleđuje ga funkciji `run_text_prompt()`.
1. Kod pokreće Gradio aplikaciju koja omogućava korisnicima da komuniciraju sa Phi 3 Mini 4K instruct demo-om bilo unošenjem poruka ili otpremanjem audio fajlova. Izlaz se prikazuje kao tekstualna poruka unutar aplikacije.

## Rešavanje problema

Instalacija Cuda GPU drajvera

1. Proverite da li su vaše Linux aplikacije ažurirane

    ```bash
    sudo apt update
    ```

1. Instalirajte Cuda drajvere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrujte lokaciju cuda drajvera

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Provera veličine Nvidia GPU memorije (Potrebno 12GB GPU memorije)

    ```bash
    nvidia-smi
    ```

1. Pražnjenje keša: Ako koristite PyTorch, možete pozvati torch.cuda.empty_cache() da oslobodite svu neiskorišćenu keš memoriju kako bi je mogle koristiti druge GPU aplikacije

    ```python
    torch.cuda.empty_cache() 
    ```

1. Provera Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Obavite sledeće korake da biste kreirali Hugging Face token.

    - Idite na [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Izaberite **New token**.
    - Unesite naziv projekta (**Name**) koji želite da koristite.
    - Izaberite **Type** na **Write**.

> **Note**
>
> Ako dobijete sledeću grešku:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Da biste rešili ovaj problem, unesite sledeću komandu u terminal.
>
> ```bash
> sudo ldconfig
> ```

**Ограничење одговорности**:  
Овај документ је преведен помоћу AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из употребе овог превода.