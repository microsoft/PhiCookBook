# Interaktiivne Phi 3 Mini 4K juhendav vestlusrobot Whisperiga

## Ülevaade

Interaktiivne Phi 3 Mini 4K juhendav vestlusrobot on tööriist, mis võimaldab kasutajatel suhelda Microsoft Phi 3 Mini 4K juhendatud demoga, kasutades tekstisisendit või helisisendit. Vestlusrobotit saab kasutada erinevate ülesannete jaoks, näiteks tõlkimiseks, ilmateate uuendusteks ja üldiseks teabe kogumiseks.

### Alustamine

Selle vestlusroboti kasutamiseks järgige lihtsalt järgmisi juhiseid:

1. Avage uus [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Märkmiku põhivaates näete vestlusakna liidest, kus on tekstisisestuskast ja nupp „Saada“.
3. Tekstipõhise vestlusroboti kasutamiseks tippige lihtsalt oma sõnum tekstisisestuskasti ja klõpsake nuppu „Saada“. Vestlusrobot vastab helifailiga, mida saab otse märkmikust esitada.

**Märkus**: Selle tööriista kasutamine nõuab GPU-d ja juurdepääsu Microsoft Phi-3 ning OpenAI Whisper mudelitele, mida kasutatakse kõnetuvastuseks ja tõlkimiseks.

### GPU nõuded

Selle demo jooksutamiseks on vaja 12 GB GPU mälu.

Mälu nõuded **Microsoft-Phi-3-Mini-4K juhendatud** demod GPU-s jooksutamiseks sõltuvad mitmetest teguritest, nagu sisendi andmete (heli või teksti) suurus, tõlkel kasutatav keel, mudeli kiirus ja GPU-l saadaval olev mälu.

Üldiselt on Whisper mudel mõeldud tööle GPU-del. Soovitatav minimaalne GPU mälu maht Whisper mudeli jooksutamiseks on 8 GB, kuid see suudab vajadusel hallata ka suuremaid mälumahtusid.

Oluline on märkida, et suurte andmemahtude või paljude päringute töötlemine mudelil võib nõuda rohkem GPU mälu ja/või põhjustada jõudlusprobleeme. Soovitatav on testida oma kasutusjuhtumit erinevate konfiguratsioonidega ning jälgida mälu kasutust, et leida konkreetsetele vajadustele optimaalne seadistus.

## Interaktiivse Phi 3 Mini 4K juhendava vestlusroboti Whisperiga E2E näidis

Jupyteri märkmik pealkirjaga [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstreerib, kuidas kasutada Microsoft Phi 3 Mini 4K juhendatud demot heli- või tekstitulemuse loomiseks. Märkmik defineerib mitu funktsiooni:

1. `tts_file_name(text)`: See funktsioon genereerib sisendtekstist faili nime genereeritud helifaili salvestamiseks.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: See funktsioon kasutab Edge TTS API-d helifaili loomiseks sisendi tekstitükkide loendist. Sisendparameetrid on tükkide loend, kõne kiirus, hääle nimi ja väljundi tee genereeritud helifaili salvestamiseks.
1. `talk(input_text)`: See funktsioon genereerib helifaili, kasutades Edge TTS API-d ja salvestab selle juhuslikku faili nimega kausta /content/audio. Sisendiks on kõneks teisendatav tekst.
1. `run_text_prompt(message, chat_history)`: See funktsioon kasutab Microsoft Phi 3 Mini 4K juhendatud demot helifaili genereerimiseks sõnumi sisendi põhjal ja lisab selle vestluse ajaloole.
1. `run_audio_prompt(audio, chat_history)`: See funktsioon teisendab helifaili tekstiks Whisper mudeli API abil ja edastab selle funktsioonile `run_text_prompt()`.
1. Kood käivitab Gradio rakenduse, mis võimaldab kasutajatel vestelda Phi 3 Mini 4K juhendatud demoga, kas sõnumeid tippides või helifaile üles laadides. Väljund kuvatakse rakenduses tekstisõnumina.

## Võrguühendusprobleemide lahendamine

Cuda GPU draiverite paigaldamine

1. Veenduge, et teie Linuxi rakendused oleksid ajakohased

    ```bash
    sudo apt update
    ```

1. Paigaldage Cuda draiverid

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registreerige cuda draiveri asukoht

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU mälu suuruse kontrollimine (nõutav 12GB GPU mälu)

    ```bash
    nvidia-smi
    ```

1. Vahemälu tühjendamine: Kui kasutate PyTorchi, võite kutsuda välja torch.cuda.empty_cache(), et vabastada kogu kasutamata vahemälu mälu selleks, et seda saaksid kasutada teised GPU rakendused

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda kontrollimine

    ```bash
    nvcc --version
    ```

1. Tehke järgmised toimingud, et luua Hugging Face token.

    - Minge aadressile [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Valige **Uus token**.
    - Sisestage projekti **Nimi**, mida soovite kasutada.
    - Valige **Tüüp** väärtuseks **Kirjutamine**.

> [!NOTE]
>
> Kui ilmneb järgmine viga:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Probleemi lahendamiseks tippige oma terminali järgmine käsk.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüdleme täpsuse poole, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma emakeeles tuleks pidada usaldusväärseks allikaks. Olulise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tekkivate arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->