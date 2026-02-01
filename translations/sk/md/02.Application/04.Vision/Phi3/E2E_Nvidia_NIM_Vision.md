### Príklad Scenára

Predstavte si, že máte obrázok (`demo.png`) a chcete vygenerovať Python kód, ktorý tento obrázok spracuje a uloží jeho novú verziu (`phi-3-vision.jpg`).

Kód vyššie automatizuje tento proces takto:

1. Nastaví prostredie a potrebné konfigurácie.
2. Vytvorí prompt, ktorý modelu zadá úlohu vygenerovať požadovaný Python kód.
3. Pošle prompt modelu a zozbiera vygenerovaný kód.
4. Extrahuje a spustí vygenerovaný kód.
5. Zobrazí pôvodný a spracovaný obrázok.

Tento prístup využíva silu AI na automatizáciu úloh spracovania obrázkov, čo uľahčuje a zrýchľuje dosiahnutie vašich cieľov.

[Ukážkový kód riešenia](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Poďme si krok po kroku rozobrať, čo celý kód robí:

1. **Inštalácia potrebného balíka**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Tento príkaz nainštaluje balík `langchain_nvidia_ai_endpoints` a zabezpečí, že máte jeho najnovšiu verziu.

2. **Import potrebných modulov**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Tieto importy načítajú moduly potrebné na komunikáciu s NVIDIA AI endpointmi, bezpečné zadávanie hesiel, prácu s operačným systémom a kódovanie/dekódovanie dát v base64 formáte.

3. **Nastavenie API kľúča**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Tento kód skontroluje, či je nastavená premenná prostredia `NVIDIA_API_KEY`. Ak nie je, vyzve používateľa na bezpečné zadanie API kľúča.

4. **Definovanie modelu a cesty k obrázku**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Tu sa nastaví model, vytvorí sa inštancia `ChatNVIDIA` s daným modelom a definuje sa cesta k súboru s obrázkom.

5. **Vytvorenie textového promptu**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Tento prompt modelu zadáva úlohu vygenerovať Python kód na spracovanie obrázka.

6. **Kódovanie obrázka do base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Tento kód načíta obrázok, zakóduje ho do base64 a vytvorí HTML tag obrázka s týmto zakódovaným obsahom.

7. **Spojenie textu a obrázka do promptu**:
    ```python
    prompt = f"{text} {image}"
    ```
    Tu sa textový prompt a HTML tag obrázka spoja do jedného reťazca.

8. **Generovanie kódu pomocou ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Tento kód pošle prompt modelu `ChatNVIDIA` a postupne zbiera vygenerovaný kód po častiach, ktoré zároveň vypisuje a pridáva do premennej `code`.

9. **Extrahovanie Python kódu z vygenerovaného obsahu**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Tento krok vyberie samotný Python kód z vygenerovaného obsahu odstránením markdown formátovania.

10. **Spustenie vygenerovaného kódu**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Tu sa extrahovaný Python kód spustí ako podproces a zachytí sa jeho výstup.

11. **Zobrazenie obrázkov**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Tieto riadky zobrazia obrázky pomocou modulu `IPython.display`.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.