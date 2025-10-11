<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-10-11T12:07:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "et"
}
-->
# Interaktiivne Phi 3 Mini 4K Instruct Chatbot koos Whisperiga

## Ülevaade

Interaktiivne Phi 3 Mini 4K Instruct Chatbot on tööriist, mis võimaldab kasutajatel suhelda Microsoft Phi 3 Mini 4K instruct demo abil, kasutades teksti või heli sisendit. Chatboti saab kasutada mitmesugusteks ülesanneteks, nagu tõlkimine, ilmateate saamine ja üldise teabe kogumine.

### Alustamine

Chatboti kasutamiseks järgige neid juhiseid:

1. Avage uus [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Märkmiku põhivaates näete vestlusakent, kus on tekstisisendi kast ja nupp "Saada".
3. Tekstipõhise chatboti kasutamiseks sisestage oma sõnum tekstikasti ja klõpsake nuppu "Saada". Chatbot vastab helifailiga, mida saab otse märkmikust esitada.

**Märkus**: Selle tööriista kasutamiseks on vaja GPU-d ja juurdepääsu Microsoft Phi-3 ja OpenAI Whisper mudelitele, mida kasutatakse kõnetuvastuseks ja tõlkimiseks.

### GPU nõuded

Selle demo käivitamiseks on vaja 12 GB GPU mälu.

**Microsoft-Phi-3-Mini-4K instruct** demo GPU-l käitamise mälunõuded sõltuvad mitmest tegurist, nagu sisendi suurus (heli või tekst), tõlkimiseks kasutatav keel, mudeli kiirus ja GPU saadaval olev mälu.

Üldiselt on Whisper mudel loodud töötama GPU-del. Whisper mudeli käitamiseks soovitatav minimaalne GPU mälu on 8 GB, kuid vajadusel saab kasutada suuremat mälu.

Oluline on märkida, et suure hulga andmete või suure mahuga päringute käitamine mudelil võib nõuda rohkem GPU mälu ja/või põhjustada jõudlusprobleeme. Soovitatav on testida oma kasutusjuhtumit erinevate konfiguratsioonidega ja jälgida mälukasutust, et määrata teie konkreetsete vajaduste jaoks optimaalsed seaded.

## E2E näidis Interaktiivse Phi 3 Mini 4K Instruct Chatbotiga koos Whisperiga

Jupyter märkmik pealkirjaga [Interaktiivne Phi 3 Mini 4K Instruct Chatbot koos Whisperiga](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) näitab, kuidas kasutada Microsoft Phi 3 Mini 4K instruct demo, et genereerida teksti heli või kirjutatud teksti sisendist. Märkmik määratleb mitmeid funktsioone:

1. `tts_file_name(text)`: See funktsioon genereerib failinime sisendteksti põhjal, et salvestada loodud helifail.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: See funktsioon kasutab Edge TTS API-d, et genereerida helifail sisendteksti tükkide loendist. Sisendparameetrid on tükkide loend, kõnekiirus, hääle nimi ja väljundtee loodud helifaili salvestamiseks.
1. `talk(input_text)`: See funktsioon genereerib helifaili, kasutades Edge TTS API-d ja salvestades selle juhusliku failinimega kausta /content/audio. Sisendparameeter on sisendtekst, mida tuleb kõneks teisendada.
1. `run_text_prompt(message, chat_history)`: See funktsioon kasutab Microsoft Phi 3 Mini 4K instruct demo, et genereerida helifail sõnumi sisendist ja lisab selle vestluse ajalukku.
1. `run_audio_prompt(audio, chat_history)`: See funktsioon teisendab helifaili tekstiks, kasutades Whisper mudeli API-d, ja edastab selle funktsioonile `run_text_prompt()`.
1. Kood käivitab Gradio rakenduse, mis võimaldab kasutajatel suhelda Phi 3 Mini 4K instruct demo abil, kas sisestades sõnumeid või üles laadides helifaile. Väljund kuvatakse rakenduses tekstisõnumina.

## Tõrkeotsing

Cuda GPU draiverite installimine

1. Veenduge, et teie Linuxi rakendused on ajakohased

    ```bash
    sudo apt update
    ```

1. Installige Cuda draiverid

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registreerige Cuda draiveri asukoht

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU mälu suuruse kontrollimine (vajalik 12 GB GPU mälu)

    ```bash
    nvidia-smi
    ```

1. Vahemälu tühjendamine: Kui kasutate PyTorchi, saate kutsuda torch.cuda.empty_cache(), et vabastada kõik kasutamata vahemälu mälu, et seda saaks kasutada teised GPU rakendused

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda kontrollimine

    ```bash
    nvcc --version
    ```

1. Tehke järgmised toimingud, et luua Hugging Face token.

    - Navigeerige [Hugging Face Token Settings lehele](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Valige **Uus token**.
    - Sisestage projekti **Nimi**, mida soovite kasutada.
    - Valige **Tüüp** väärtuseks **Kirjutamine**.

> **Märkus**
>
> Kui ilmneb järgmine viga:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Selle lahendamiseks sisestage oma terminali järgmine käsk.
>
> ```bash
> sudo ldconfig
> ```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.