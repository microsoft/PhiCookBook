<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-05-09T18:33:38+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hu"
}
-->
# Interactive Phi 3 Mini 4K Instruct Chatbot Whisperrel

## Áttekintés

Az Interactive Phi 3 Mini 4K Instruct Chatbot egy eszköz, amely lehetővé teszi a felhasználók számára, hogy szöveges vagy hangbemenet segítségével kommunikáljanak a Microsoft Phi 3 Mini 4K instruct demóval. A chatbot különféle feladatokra használható, például fordításra, időjárás-frissítésekre és általános információgyűjtésre.

### Kezdés

A chatbot használatához egyszerűen kövesse az alábbi lépéseket:

1. Nyissa meg az új [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) fájlt
2. A jegyzetfüzet főablakában egy chatbox felületet lát, amely tartalmaz egy szövegbeviteli mezőt és egy „Send” gombot.
3. A szöveges chatbot használatához egyszerűen írja be az üzenetét a szövegmezőbe, majd kattintson a „Send” gombra. A chatbot egy hangfájllal válaszol, amelyet közvetlenül a jegyzetfüzetben lejátszhat.

**Megjegyzés**: Ez az eszköz GPU-t igényel, valamint hozzáférést a Microsoft Phi-3 és OpenAI Whisper modellekhez, amelyeket beszédfelismerésre és fordításra használnak.

### GPU követelmények

A demó futtatásához legalább 12 GB GPU memória szükséges.

A **Microsoft-Phi-3-Mini-4K instruct** demó GPU-n történő futtatásához szükséges memória mennyisége több tényezőtől függ, például a bemeneti adat (hang vagy szöveg) méretétől, a fordításhoz használt nyelvtől, a modell sebességétől és a GPU rendelkezésre álló memóriájától.

Általánosságban a Whisper modellt GPU-n való futtatásra tervezték. A Whisper modell futtatásához ajánlott minimális GPU memória 8 GB, de szükség esetén nagyobb memória is kezelhető.

Fontos megjegyezni, hogy nagy mennyiségű adat vagy nagy számú kérés futtatása esetén több GPU memória és/vagy teljesítményproblémák jelentkezhetnek. Ajánlott különböző konfigurációkkal tesztelni a használati esetet, és figyelni a memóriahasználatot az optimális beállítások meghatározásához.

## E2E példa az Interactive Phi 3 Mini 4K Instruct Chatbot Whisperrel

A [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) nevű jupyter jegyzetfüzet bemutatja, hogyan használható a Microsoft Phi 3 Mini 4K instruct Demo hang- vagy írott szöveg alapú szöveg generálására. A jegyzetfüzet több funkciót definiál:

1. `tts_file_name(text)`: Ez a függvény a bemeneti szöveg alapján generál fájlnevet a létrehozott hangfájl mentéséhez.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ez a függvény az Edge TTS API-t használja, hogy egy szövegrészletekből álló listából hangfájlt generáljon. A bemeneti paraméterek a szövegrészletek listája, a beszédsebesség, a hang neve és a létrehozott hangfájl mentési útvonala.
1. `talk(input_text)`: Ez a függvény az Edge TTS API-t használva generál hangfájlt, amelyet véletlenszerű névvel ment a /content/audio könyvtárba. A bemeneti paraméter a beszéddé alakítandó szöveg.
1. `run_text_prompt(message, chat_history)`: Ez a függvény a Microsoft Phi 3 Mini 4K instruct demót használja, hogy egy üzenet alapján hangfájlt generáljon, és hozzáfűzi azt a chat előzményekhez.
1. `run_audio_prompt(audio, chat_history)`: Ez a függvény egy hangfájlt szöveggé alakít a Whisper modell API segítségével, majd átadja a `run_text_prompt()` függvénynek.
1. A kód elindít egy Gradio alkalmazást, amely lehetővé teszi a felhasználók számára, hogy üzenetek gépelésével vagy hangfájlok feltöltésével kommunikáljanak a Phi 3 Mini 4K instruct demóval. A kimenet szöveges üzenetként jelenik meg az alkalmazáson belül.

## Hibakeresés

Cuda GPU driverek telepítése

1. Győződjön meg róla, hogy a Linux rendszere naprakész

    ```bash
    sudo apt update
    ```

1. Telepítse a Cuda drivereket

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Regisztrálja a cuda driver helyét

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Nvidia GPU memória méretének ellenőrzése (Szükséges 12GB GPU memória)

    ```bash
    nvidia-smi
    ```

1. Cache ürítése: Ha PyTorch-ot használ, hívja meg a torch.cuda.empty_cache() függvényt, hogy felszabadítsa az összes nem használt gyorsítótárazott memóriát, amely így más GPU alkalmazások számára is elérhetővé válik

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda ellenőrzése

    ```bash
    nvcc --version
    ```

1. A következő lépéseket végezze el egy Hugging Face token létrehozásához.

    - Navigáljon a [Hugging Face Token Settings oldalra](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Válassza az **Új token** lehetőséget.
    - Adja meg a projekt **nevét**, amelyet használni szeretne.
    - Válassza ki a **típust**: **Write**.

> **Megjegyzés**
>
> Ha a következő hibát tapasztalja:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ennek megoldásához írja be a következő parancsot a terminálban.
>
> ```bash
> sudo ldconfig
> ```

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.