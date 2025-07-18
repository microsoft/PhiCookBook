<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:59:23+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "hr"
}
-->
### Primjer scenarija

Zamislite da imate sliku (`demo.png`) i želite generirati Python kod koji obrađuje tu sliku i sprema novu verziju (`phi-3-vision.jpg`).

Gornji kod automatizira ovaj proces na sljedeći način:

1. Postavlja okruženje i potrebne konfiguracije.
2. Kreira prompt koji modelu daje upute za generiranje potrebnog Python koda.
3. Šalje prompt modelu i prikuplja generirani kod.
4. Izvlači i izvršava generirani kod.
5. Prikazuje originalnu i obrađenu sliku.

Ovaj pristup koristi snagu AI-ja za automatizaciju zadataka obrade slika, čineći postizanje ciljeva jednostavnijim i bržim.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Razložimo što cijeli kod radi korak po korak:

1. **Instaliraj potrebni paket**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ova naredba instalira paket `langchain_nvidia_ai_endpoints`, osiguravajući da je verzija najnovija.

2. **Uvezi potrebne module**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ovi uvozi donose potrebne module za interakciju s NVIDIA AI endpointima, sigurno rukovanje lozinkama, rad s operativnim sustavom i kodiranje/dekodiranje podataka u base64 formatu.

3. **Postavi API ključ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ovaj kod provjerava je li postavljena varijabla okruženja `NVIDIA_API_KEY`. Ako nije, sigurno traži od korisnika da unese svoj API ključ.

4. **Definiraj model i putanju do slike**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Ovdje se postavlja model koji će se koristiti, kreira se instanca `ChatNVIDIA` s navedenim modelom i definira putanja do slikovne datoteke.

5. **Kreiraj tekstualni prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Ovdje se definira tekstualni prompt koji modelu daje upute za generiranje Python koda za obradu slike.

6. **Kodiraj sliku u Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ovaj kod čita slikovnu datoteku, kodira je u base64 i kreira HTML `<img>` tag s kodiranim podacima.

7. **Spoji tekst i sliku u prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Ovdje se tekstualni prompt i HTML `<img>` tag spajaju u jedan string.

8. **Generiraj kod koristeći ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ovaj kod šalje prompt modelu `ChatNVIDIA` i prikuplja generirani kod u dijelovima, ispisujući i dodajući svaki dio u varijablu `code`.

9. **Izvuci Python kod iz generiranog sadržaja**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Ovdje se iz generiranog sadržaja izvlači stvarni Python kod uklanjanjem markdown formata.

10. **Pokreni generirani kod**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ovaj dio izvršava izdvojeni Python kod kao podproces i hvata njegov izlaz.

11. **Prikaži slike**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ove linije prikazuju slike koristeći modul `IPython.display`.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.