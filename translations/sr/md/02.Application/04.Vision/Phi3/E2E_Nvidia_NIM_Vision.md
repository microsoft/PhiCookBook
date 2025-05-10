<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:58:41+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "sr"
}
-->
### Primer Scenarija

Zamislite da imate sliku (`demo.png`) i želite da generišete Python kod koji obrađuje tu sliku i sačuva novu verziju (`phi-3-vision.jpg`).

Gore navedeni kod automatizuje ovaj proces tako što:

1. Podešava okruženje i potrebne konfiguracije.
2. Kreira prompt koji modelu daje instrukcije da generiše neophodan Python kod.
3. Šalje prompt modelu i prikuplja generisani kod.
4. Izvlači i izvršava generisani kod.
5. Prikazuje originalne i obrađene slike.

Ovaj pristup koristi moć veštačke inteligencije da automatizuje zadatke obrade slika, čineći ih lakšim i bržim za postizanje željenih rezultata.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Hajde da korak po korak objasnimo šta ceo kod radi:

1. **Instalirajte Potreban Paket**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ova komanda instalira paket `langchain_nvidia_ai_endpoints`, osiguravajući da imate najnoviju verziju.

2. **Uvezi Potrebne Module**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ovi importi donose potrebne module za interakciju sa NVIDIA AI endpoint-ima, sigurno rukovanje lozinkama, rad sa operativnim sistemom i enkodiranje/dekodiranje podataka u base64 formatu.

3. **Postavite API Ključ**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ovaj kod proverava da li je environment varijabla `NVIDIA_API_KEY` postavljena. Ako nije, traži od korisnika da unese svoj API ključ na siguran način.

4. **Definišite Model i Putanju do Slike**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Ovim se postavlja model koji će se koristiti, kreira instanca `ChatNVIDIA` sa zadatim modelom i definiše putanja do fajla sa slikom.

5. **Kreirajte Tekstualni Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Ovim se definiše tekstualni prompt koji modelu daje instrukcije da generiše Python kod za obradu slike.

6. **Kodirajte Sliku u Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ovaj kod učitava fajl slike, kodira ga u base64 i kreira HTML image tag sa enkodiranim podacima.

7. **Kombinujte Tekst i Sliku u Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Ovim se tekstualni prompt i HTML image tag kombinuju u jedan string.

8. **Generišite Kod Koristeći ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ovaj kod šalje prompt u `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Izvucite Python Kod iz Generisanog Sadržaja**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Ovim se iz generisanog sadržaja izvlači stvarni Python kod uklanjanjem markdown formata.

10. **Pokrenite Generisani Kod**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ovim se pokreće izvučeni Python kod kao podproces i hvata njegov izlaz.

11. **Prikažite Slike**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ove linije prikazuju slike koristeći `IPython.display` modul.

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења настала коришћењем овог превода.