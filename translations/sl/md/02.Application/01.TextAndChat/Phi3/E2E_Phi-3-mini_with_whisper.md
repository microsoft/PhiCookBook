<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T16:13:51+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sl"
}
-->
# Interaktivni Phi 3 Mini 4K Instruct klepetalnik z Whisper

## Pregled

Interaktivni Phi 3 Mini 4K Instruct klepetalnik je orodje, ki uporabnikom omogoča interakcijo z Microsoft Phi 3 Mini 4K instruct demo preko besedilnega ali zvočnega vnosa. Klepetalnik se lahko uporablja za različne naloge, kot so prevajanje, vremenske napovedi in zbiranje splošnih informacij.

### Začetek

Za uporabo tega klepetalnika preprosto sledite tem navodilom:

1. Odprite nov [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V glavnem oknu zvezka boste videli vmesnik klepetalnika z vnosnim poljem za besedilo in gumbom "Send".
3. Za uporabo klepetalnika na osnovi besedila preprosto vtipkajte svoje sporočilo v vnosno polje in kliknite gumb "Send". Klepetalnik bo odgovoril z zvočno datoteko, ki jo lahko predvajate neposredno znotraj zvezka.

**Opomba**: To orodje zahteva GPU in dostop do Microsoft Phi-3 ter OpenAI Whisper modelov, ki se uporabljajo za prepoznavanje govora in prevajanje.

### Zahteve za GPU

Za zagon te predstavitve potrebujete 12 GB grafičnega pomnilnika.

Zahteve po pomnilniku za zagon **Microsoft-Phi-3-Mini-4K instruct** predstavitve na GPU bodo odvisne od več dejavnikov, kot so velikost vhodnih podatkov (zvok ali besedilo), jezik, ki se uporablja za prevajanje, hitrost modela in razpoložljivi pomnilnik na GPU.

Na splošno je Whisper model zasnovan za delovanje na GPU-jih. Priporočena minimalna količina GPU pomnilnika za zagon Whisper modela je 8 GB, vendar lahko obvladuje tudi večje količine pomnilnika, če je potrebno.

Pomembno je opozoriti, da zagon velike količine podatkov ali velika uporaba modela morda zahteva več GPU pomnilnika in/ali lahko povzroči težave z zmogljivostjo. Priporočljivo je preizkusiti svoj primer uporabe z različnimi konfiguracijami in spremljati uporabo pomnilnika, da določite optimalne nastavitve za vaše posebne potrebe.

## E2E primer za Interaktivni Phi 3 Mini 4K Instruct klepetalnik z Whisper

Jupyter zvezek z naslovom [Interaktivni Phi 3 Mini 4K Instruct klepetalnik z Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) prikazuje, kako uporabiti Microsoft Phi 3 Mini 4K instruct demo za generiranje besedila iz zvoka ali pisanega besedilnega vnosa. Zvezek definira več funkcij:

1. `tts_file_name(text)`: Ta funkcija generira ime datoteke na podlagi vhodnega besedila za shranjevanje generirane zvočne datoteke.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ta funkcija uporablja Edge TTS API za generiranje zvočne datoteke iz seznama delcev vhodnega besedila. Vhodni parametri so seznam delcev, hitrost govora, ime glasu in izhodna pot za shranjevanje generirane zvočne datoteke.
1. `talk(input_text)`: Ta funkcija generira zvočno datoteko z uporabo Edge TTS API in jo shrani v naključno ime datoteke v imeniku /content/audio. Vhodni parameter je vhodno besedilo za pretvorbo v govor.
1. `run_text_prompt(message, chat_history)`: Ta funkcija uporablja Microsoft Phi 3 Mini 4K instruct demo za generiranje zvočne datoteke iz vnosnega sporočila in jo doda v zgodovino klepeta.
1. `run_audio_prompt(audio, chat_history)`: Ta funkcija pretvori zvočno datoteko v besedilo z uporabo Whisper model API in jo posreduje funkciji `run_text_prompt()`.
1. Koda zažene aplikacijo Gradio, ki uporabnikom omogoča interakcijo z Phi 3 Mini 4K instruct demo z vnašanjem sporočil ali nalaganjem zvočnih datotek. Izhod se prikaže kot besedilno sporočilo znotraj aplikacije.

## Odpravljanje težav

Namestitev gonilnikov Cuda GPU

1. Prepričajte se, da so vaše Linux aplikacije posodobljene

    ```bash
    sudo apt update
    ```

1. Namestite Cuda gonilnike

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrirajte lokacijo cuda gonilnika

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Preverjanje velikosti Nvidia GPU pomnilnika (zahtevano 12GB GPU pomnilnika)

    ```bash
    nvidia-smi
    ```

1. Praznjenje predpomnilnika: Če uporabljate PyTorch, lahko pokličete torch.cuda.empty_cache(), da sprostite ves neuporabljeni predpomnilnik, ki ga lahko uporabijo druge GPU aplikacije

    ```python
    torch.cuda.empty_cache() 
    ```

1. Preverjanje Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Za ustvarjanje žetona Hugging Face izvedite naslednja opravila.

    - Obiščite stran [Hugging Face Token Settings](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Izberite **New token**.
    - Vnesite ime projekta, ki ga želite uporabiti.
    - Izberite **Type** na **Write**.

> [!NOTE]
>
> Če naletite na naslednjo napako:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Za rešitev vnosa v terminal vtipkajte naslednji ukaz.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvornem jeziku velja za zavezujoč vir. Za kritične informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->