<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:21:55+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hu"
}
-->
# Interaktív Phi 3 Mini 4K Instruct Chatbot Whisper-rel

## Áttekintés

Az Interaktív Phi 3 Mini 4K Instruct Chatbot egy olyan eszköz, amely lehetővé teszi a felhasználók számára, hogy szöveges vagy hangalapú bemenettel kommunikáljanak a Microsoft Phi 3 Mini 4K instruct demóval. A chatbot különféle feladatokra használható, például fordításra, időjárás-frissítésekre és általános információgyűjtésre.

### Kezdés

A chatbot használatához egyszerűen kövesse az alábbi lépéseket:

1. Nyissa meg az új [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) fájlt
2. A jegyzetfüzet fő ablakában egy chatbox felületet fog látni, amely tartalmaz egy szövegbeviteli mezőt és egy "Send" gombot.
3. A szöveges chatbot használatához egyszerűen írja be az üzenetét a szövegbeviteli mezőbe, majd kattintson a "Send" gombra. A chatbot egy hangfájllal válaszol, amely közvetlenül a jegyzetfüzetből lejátszható.

**Megjegyzés**: Ez az eszköz GPU-t és hozzáférést igényel a Microsoft Phi-3 és OpenAI Whisper modellekhez, amelyeket beszédfelismerésre és fordításra használnak.

### GPU követelmények

A demó futtatásához legalább 12 GB GPU memóriára van szükség.

A **Microsoft-Phi-3-Mini-4K instruct** demó GPU-n való futtatásához szükséges memória mennyisége több tényezőtől függ, például a bemeneti adatok méretétől (hang vagy szöveg), a fordítás nyelvétől, a modell sebességétől és a GPU rendelkezésre álló memóriájától.

Általánosságban elmondható, hogy a Whisper modellt GPU-kon tervezték futtatni. A Whisper modell futtatásához ajánlott minimális GPU memória 8 GB, de szükség esetén nagyobb memóriát is képes kezelni.

Fontos megjegyezni, hogy nagy mennyiségű adat vagy sok kérés feldolgozása esetén több GPU memória szükséges, illetve előfordulhatnak teljesítménybeli problémák. Ajánlott különböző konfigurációkkal tesztelni az adott felhasználási esetet, és figyelni a memóriahasználatot a legoptimálisabb beállítások megtalálásához.

## E2E példa az Interaktív Phi 3 Mini 4K Instruct Chatbot Whisper-rel

Az [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) című Jupyter jegyzetfüzet bemutatja, hogyan használható a Microsoft Phi 3 Mini 4K instruct demó szöveg generálására hang vagy írott szöveg alapján. A jegyzetfüzet több függvényt definiál:

1. `tts_file_name(text)`: Ez a függvény a bemeneti szöveg alapján generál fájlnevet a létrehozott hangfájl mentéséhez.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ez a függvény az Edge TTS API-t használja, hogy egy szövegtöredékekből álló listából hangfájlt generáljon. A bemeneti paraméterek a töredékek listája, a beszéd sebessége, a hang neve és a mentési útvonal.
1. `talk(input_text)`: Ez a függvény az Edge TTS API segítségével generál hangfájlt, amelyet véletlenszerű néven ment a /content/audio könyvtárba. A bemeneti paraméter a beszéddé alakítandó szöveg.
1. `run_text_prompt(message, chat_history)`: Ez a függvény a Microsoft Phi 3 Mini 4K instruct demót használja, hogy egy üzenetből hangfájlt generáljon, majd hozzáfűzi a chat előzményekhez.
1. `run_audio_prompt(audio, chat_history)`: Ez a függvény a Whisper modell API-ját használja egy hangfájl szöveggé alakítására, majd továbbítja a `run_text_prompt()` függvénynek.
1. A kód elindít egy Gradio alkalmazást, amely lehetővé teszi a felhasználók számára, hogy üzenetek gépelésével vagy hangfájlok feltöltésével kommunikáljanak a Phi 3 Mini 4K instruct demóval. A kimenet szöveges üzenetként jelenik meg az alkalmazáson belül.

## Hibakeresés

Cuda GPU driverek telepítése

1. Győződjön meg róla, hogy Linux alkalmazásai naprakészek

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

1. Cache ürítése: Ha PyTorch-ot használ, hívja meg a torch.cuda.empty_cache() függvényt, hogy felszabadítsa az összes nem használt cache memóriát, így az más GPU alkalmazások számára elérhetővé válik

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda ellenőrzése

    ```bash
    nvcc --version
    ```

1. A következő lépéseket végezze el egy Hugging Face token létrehozásához.

    - Lépjen a [Hugging Face Token beállítások oldalára](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Válassza az **Új token** lehetőséget.
    - Adja meg a projekt **Nevét**, amelyet használni szeretne.
    - Állítsa a **Típust** **Write**-ra.

> **Megjegyzés**
>
> Ha a következő hibát tapasztalja:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> A megoldáshoz írja be a következő parancsot a terminálban.
>
> ```bash
> sudo ldconfig
> ```

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.