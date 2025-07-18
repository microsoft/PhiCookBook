<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:23:54+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "sl"
}
-->
# Interaktivni Phi 3 Mini 4K Instruct Chatbot z Whisper

## Pregled

Interaktivni Phi 3 Mini 4K Instruct Chatbot je orodje, ki uporabnikom omogoča interakcijo z Microsoft Phi 3 Mini 4K instruct demo preko besedilnega ali zvočnega vnosa. Chatbot se lahko uporablja za različne naloge, kot so prevajanje, vremenske napovedi in zbiranje splošnih informacij.

### Začetek

Za uporabo tega chatbota sledite naslednjim navodilom:

1. Odprite nov [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V glavnem oknu zvezka boste videli vmesnik klepetalnice z besedilnim vnosnim poljem in gumbom "Send".
3. Za uporabo besedilnega chatbota preprosto vnesite svoje sporočilo v besedilno polje in kliknite gumb "Send". Chatbot bo odgovoril z zvočno datoteko, ki jo lahko predvajate neposredno znotraj zvezka.

**Note**: To orodje zahteva GPU in dostop do Microsoft Phi-3 ter OpenAI Whisper modelov, ki se uporabljata za prepoznavanje govora in prevajanje.

### Zahteve za GPU

Za zagon te predstavitve potrebujete 12 GB pomnilnika na GPU.

Zahteve po pomnilniku za zagon **Microsoft-Phi-3-Mini-4K instruct** demo na GPU bodo odvisne od več dejavnikov, kot so velikost vhodnih podatkov (zvok ali besedilo), jezik prevajanja, hitrost modela in razpoložljivi pomnilnik na GPU.

Na splošno je Whisper model zasnovan za delovanje na GPU-jih. Priporočena minimalna količina pomnilnika za zagon Whisper modela je 8 GB, vendar lahko obvladuje tudi večje količine pomnilnika, če je potrebno.

Pomembno je vedeti, da lahko obdelava velike količine podatkov ali veliko število zahtevkov povzroči potrebo po več pomnilnika na GPU in/ali vpliva na zmogljivost. Priporočamo, da preizkusite svoj primer uporabe z različnimi nastavitvami in spremljate porabo pomnilnika, da določite optimalne nastavitve za vaše specifične potrebe.

## E2E primer za Interaktivni Phi 3 Mini 4K Instruct Chatbot z Whisper

Jupyter zvezek z naslovom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) prikazuje, kako uporabiti Microsoft Phi 3 Mini 4K instruct Demo za generiranje besedila iz zvočnega ali pisnega vnosa. Zvezek definira več funkcij:

1. `tts_file_name(text)`: Ta funkcija ustvari ime datoteke na podlagi vhodnega besedila za shranjevanje generirane zvočne datoteke.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ta funkcija uporablja Edge TTS API za generiranje zvočne datoteke iz seznama delov vhodnega besedila. Vhodni parametri so seznam delov, hitrost govora, ime glasu in pot za shranjevanje generirane zvočne datoteke.
1. `talk(input_text)`: Ta funkcija generira zvočno datoteko z uporabo Edge TTS API in jo shrani pod naključno ime v imenik /content/audio. Vhodni parameter je besedilo, ki ga želimo pretvoriti v govor.
1. `run_text_prompt(message, chat_history)`: Ta funkcija uporablja Microsoft Phi 3 Mini 4K instruct demo za generiranje zvočne datoteke iz sporočila in jo doda v zgodovino klepeta.
1. `run_audio_prompt(audio, chat_history)`: Ta funkcija pretvori zvočno datoteko v besedilo z uporabo Whisper model API in ga posreduje funkciji `run_text_prompt()`.
1. Koda zažene Gradio aplikacijo, ki uporabnikom omogoča interakcijo z Phi 3 Mini 4K instruct demo tako, da vnašajo sporočila ali nalagajo zvočne datoteke. Izhod se prikaže kot besedilno sporočilo znotraj aplikacije.

## Reševanje težav

Namestitev Cuda GPU gonilnikov

1. Poskrbite, da so vaše Linux aplikacije posodobljene

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

1. Počistite predpomnilnik: Če uporabljate PyTorch, lahko pokličete torch.cuda.empty_cache(), da sprostite ves neuporabljen predpomnilnik, ki ga lahko nato uporabljajo druge GPU aplikacije

    ```python
    torch.cuda.empty_cache() 
    ```

1. Preverjanje Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Izvedite naslednje korake za ustvarjanje Hugging Face žetona.

    - Obiščite [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Izberite **New token**.
    - Vnesite ime projekta, ki ga želite uporabiti.
    - Izberite **Type** na **Write**.

> **Note**
>
> Če naletite na naslednjo napako:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Za rešitev vnesite naslednji ukaz v terminal.
>
> ```bash
> sudo ldconfig
> ```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.