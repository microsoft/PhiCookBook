<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:58:29+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "cs"
}
-->
### Příklad scénáře

Představte si, že máte obrázek (`demo.png`) a chcete vygenerovat Python kód, který tento obrázek zpracuje a uloží jeho novou verzi (`phi-3-vision.jpg`).

Výše uvedený kód tento proces automatizuje takto:

1. Nastaví prostředí a potřebné konfigurace.
2. Vytvoří prompt, který modelu zadá úkol vygenerovat požadovaný Python kód.
3. Odešle prompt modelu a shromáždí vygenerovaný kód.
4. Extrahuje a spustí vygenerovaný kód.
5. Zobrazí původní a zpracované obrázky.

Tento přístup využívá sílu AI k automatizaci úloh zpracování obrázků, což usnadňuje a urychluje dosažení vašich cílů.

[Ukázkové řešení kódu](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Pojďme si krok za krokem rozebrat, co celý kód dělá:

1. **Nainstalujte požadovaný balíček**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Tento příkaz nainstaluje balíček `langchain_nvidia_ai_endpoints` a zajistí, že máte jeho nejnovější verzi.

2. **Importujte potřebné moduly**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Tyto importy přinášejí moduly potřebné pro komunikaci s NVIDIA AI endpointy, bezpečné zadávání hesel, práci s operačním systémem a kódování/dekódování dat v base64 formátu.

3. **Nastavte API klíč**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Tento kód zkontroluje, zda je nastavena proměnná prostředí `NVIDIA_API_KEY`. Pokud ne, bezpečně vyzve uživatele k zadání API klíče.

4. **Definujte model a cestu k obrázku**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Zde se nastaví model, vytvoří instance `ChatNVIDIA` s daným modelem a definuje se cesta k souboru s obrázkem.

5. **Vytvořte textový prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Tento prompt instruuje model, aby vygeneroval Python kód pro zpracování obrázku.

6. **Zakódujte obrázek do base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Tento kód načte obrázek, zakóduje ho do base64 a vytvoří HTML tag obrázku s tímto zakódovaným obsahem.

7. **Spojte text a obrázek do promptu**:
    ```python
    prompt = f"{text} {image}"
    ```
    Tento krok kombinuje textový prompt a HTML tag obrázku do jednoho řetězce.

8. **Vygenerujte kód pomocí ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Tento kód odešle prompt modelu `ChatNVIDIA` a sbírá vygenerovaný kód po částech, přičemž každou část vypisuje a přidává do proměnné `code`.

9. **Extrahujte Python kód z vygenerovaného obsahu**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Tento krok odstraní markdown formátování a získá čistý Python kód z vygenerovaného textu.

10. **Spusťte vygenerovaný kód**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Tento příkaz spustí extrahovaný Python kód jako podproces a zachytí jeho výstup.

11. **Zobrazte obrázky**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Tyto řádky zobrazí obrázky pomocí modulu `IPython.display`.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.