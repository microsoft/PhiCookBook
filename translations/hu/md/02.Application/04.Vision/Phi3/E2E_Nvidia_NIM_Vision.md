<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:58:17+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "hu"
}
-->
### Példa Forgatókönyv

Képzelj el egy képet (`demo.png`), és szeretnél Python kódot generálni, amely feldolgozza ezt a képet, majd elment egy új verziót (`phi-3-vision.jpg`).

A fenti kód ezt a folyamatot automatizálja az alábbi módon:

1. Beállítja a környezetet és a szükséges konfigurációkat.
2. Létrehoz egy promptot, amely utasítja a modellt a szükséges Python kód generálására.
3. Elküldi a promptot a modellnek, és összegyűjti a generált kódot.
4. Kinyeri és futtatja a generált kódot.
5. Megjeleníti az eredeti és a feldolgozott képet.

Ez a megközelítés kihasználja a mesterséges intelligencia erejét a képfeldolgozási feladatok automatizálására, így könnyebbé és gyorsabbá téve a célok elérését.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Nézzük meg lépésről lépésre, mit csinál az egész kód:

1. **Szükséges csomag telepítése**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ez a parancs telepíti a `langchain_nvidia_ai_endpoints` csomagot, biztosítva, hogy a legfrissebb verzió legyen.

2. **Szükséges modulok importálása**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ezek az importok betöltik a szükséges modulokat az NVIDIA AI végpontokkal való kommunikációhoz, a jelszavak biztonságos kezeléséhez, az operációs rendszerrel való interakcióhoz, valamint az adatok base64-es kódolásához és dekódolásához.

3. **API kulcs beállítása**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ez a kód ellenőrzi, hogy be van-e állítva a `NVIDIA_API_KEY` környezeti változó. Ha nincs, akkor biztonságosan kéri be a felhasználótól az API kulcsot.

4. **Modell és kép elérési útjának meghatározása**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Itt állítjuk be a használni kívánt modellt, létrehozunk egy `ChatNVIDIA` példányt a megadott modellel, és definiáljuk a kép fájl elérési útját.

5. **Szöveges prompt létrehozása**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Ez egy szöveges promptot definiál, amely utasítja a modellt, hogy generáljon Python kódot egy kép feldolgozásához.

6. **Kép base64-es kódolása**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ez a kód beolvassa a képfájlt, base64 formátumba kódolja, és létrehoz egy HTML kép taget az így kapott adatokkal.

7. **Szöveg és kép egyesítése a promptban**:
    ```python
    prompt = f"{text} {image}"
    ```
    Ez összefűzi a szöveges promptot és a HTML kép taget egyetlen stringgé.

8. **Kód generálása a ChatNVIDIA segítségével**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ez a kód elküldi a promptot a `ChatNVIDIA` modellnek, és darabokban gyűjti össze a generált kódot, miközben kiírja és hozzáfűzi a `code` változóhoz.

9. **Python kód kinyerése a generált tartalomból**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Ez eltávolítja a markdown formázást, és kinyeri a tényleges Python kódot a generált tartalomból.

10. **A generált kód futtatása**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ez a kód egy alfolyamatként futtatja a kinyert Python kódot, és rögzíti annak kimenetét.

11. **Képek megjelenítése**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ezek a sorok az `IPython.display` modult használva jelenítik meg a képeket.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.