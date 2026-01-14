<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7f72d7981ed3640865700f51ae407da4",
  "translation_date": "2026-01-14T16:01:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "hu"
}
-->
# Interaktív Phi 3 Mini 4K Instrukciós Chatbot Whisper-rel

## Áttekintés

Az Interaktív Phi 3 Mini 4K Instrukciós Chatbot egy eszköz, amely lehetővé teszi a felhasználók számára, hogy szöveges vagy hangbemenettel lépjenek kapcsolatba a Microsoft Phi 3 Mini 4K instrukciós demóval. A chatbot különféle feladatokra használható, mint például fordítás, időjárás-frissítések és általános információgyűjtés.

### Kezdés

A chatbot használatához egyszerűen kövesse ezeket az utasításokat:

1. Nyissa meg az új [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) fájlt.
2. A jegyzetfüzet fő ablakában egy chatbox felületet fog látni, szövegbeviteli mezővel és egy "Küldés" gombbal.
3. A szöveges chatbot használatához egyszerűen írja be az üzenetét a szövegbeviteli mezőbe, majd kattintson a "Küldés" gombra. A chatbot hangfájllal válaszol, amely közvetlenül a jegyzetfüzetből lejátszható.

**Megjegyzés**: Ez az eszköz GPU-t és hozzáférést igényel a Microsoft Phi-3 és az OpenAI Whisper modellekhez, amelyeket beszédfelismerésre és fordításra használnak.

### GPU követelmények

A demó futtatásához 12 Gb GPU memóriára van szükség.

A **Microsoft-Phi-3-Mini-4K instrukciós** demó GPU-n történő futtatásához szükséges memória több tényezőtől függ, például a bemeneti adatok méretétől (hang vagy szöveg), a fordításhoz használt nyelvtől, a modell sebességétől és a GPU rendelkezésre álló memóriájától.

Általánosságban elmondható, hogy a Whisper modellt GPU-kon futtatásra tervezték. A Whisper modell ajánlott minimális GPU memóriaigénye 8 GB, de nagyobb memória esetén is képes működni.

Fontos megjegyezni, hogy nagy mennyiségű adat vagy sok kérések egyidejű futtatása a modellen több GPU memóriát igényelhet, illetve teljesítménybeli problémákat okozhat. Javasolt különböző konfigurációkkal tesztelni az esettanulmányt, és figyelni a memóriahasználatot a specifikus igényeihez legmegfelelőbb beállítások meghatározásához.

## Interaktív Phi 3 Mini 4K Instrukciós Chatbot Whisper-rel E2E példa

A [Interaktív Phi 3 Mini 4K Instrukciós Chatbot Whisper-rel](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) címet viselő jupyter jegyzetfüzet bemutatja, hogyan használható a Microsoft Phi 3 Mini 4K instrukciós demó szöveg vagy hangbemenetből származó szöveg generálására. A jegyzetfüzet több funkciót definiál:

1. `tts_file_name(text)`: Ez a függvény a bemeneti szöveg alapján generál fájlnevet a létrehozott hangfájl mentéséhez.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ez a függvény az Edge TTS API-t használja, hogy egy szövegmorzsákból álló listából hangfájlt generáljon. A bemeneti paraméterek a morzsák listája, a beszéd sebessége, a hang neve és a kimeneti elérési út a mentéshez.
1. `talk(input_text)`: Ez a függvény az Edge TTS API-t használva generál hangfájlt, amelyet véletlenszerű fájlnévvel ment a /content/audio könyvtárba. A bemenet a beszéddé alakítandó szöveg.
1. `run_text_prompt(message, chat_history)`: Ez a függvény a Microsoft Phi 3 Mini 4K instrukciós demót használva generál hangfájlt egy üzenetből, és hozzáfűzi azt a chat előzményekhez.
1. `run_audio_prompt(audio, chat_history)`: Ez a függvény a Whisper modell API-ját használva hangfájlból szöveget generál, majd továbbadja a `run_text_prompt()` függvénynek.
1. A kód elindít egy Gradio alkalmazást, amely lehetővé teszi a felhasználók számára, hogy a Phi 3 Mini 4K instrukciós demóval interaktívan lépjenek kapcsolatba üzenetek gépelésével vagy hangfájlok feltöltésével. A kimenet a szöveges üzenetek formájában jelenik meg az alkalmazáson belül.

## Hibakeresés

Cuda GPU driverek telepítése

1. Győződjön meg arról, hogy Linux alkalmazásai naprakészek

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

1. Cache ürítése: Ha PyTorch-ot használ, meghívhatja a torch.cuda.empty_cache() függvényt, amely felszabadít minden nem használt gyorsítótárban lévő memóriát, hogy más GPU alkalmazások használhassák.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda ellenőrzése

    ```bash
    nvcc --version
    ```

1. Az alábbi feladatokat végezze el egy Hugging Face token létrehozásához.

    - Navigáljon a [Hugging Face Token beállítások oldalára](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Válassza az **Új token** lehetőséget.
    - Adja meg a használni kívánt projekt **Nevét**.
    - Válassza a **Típus**-nak a **Write** opciót.

> [!NOTE]
>
> Ha a következő hibával találkozik:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ehhez oldja meg a problémát a következő parancs terminálba való begépelésével.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekintendő hivatalos forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->