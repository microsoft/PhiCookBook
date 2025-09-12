<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-09-12T14:37:44+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "lt"
}
-->
### Pavyzdinė situacija

Įsivaizduokite, kad turite paveikslėlį (`demo.png`) ir norite sugeneruoti Python kodą, kuris apdoroja šį paveikslėlį ir išsaugo naują jo versiją (`phi-3-vision.jpg`). 

Aukščiau pateiktas kodas automatizuoja šį procesą:

1. Sukuriant aplinką ir reikalingas konfigūracijas.
2. Sukuriant užklausą, kuri nurodo modeliui sugeneruoti reikiamą Python kodą.
3. Siunčiant užklausą modeliui ir surenkant sugeneruotą kodą.
4. Išskiriant ir vykdant sugeneruotą kodą.
5. Parodant originalų ir apdorotą paveikslėlį.

Šis metodas pasitelkia dirbtinio intelekto galią automatizuoti paveikslėlių apdorojimo užduotis, todėl tikslus pasiekti tampa lengviau ir greičiau. 

[Sprendimo kodo pavyzdys](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Pažvelkime, ką visas kodas daro žingsnis po žingsnio:

1. **Įdiegti reikalingą paketą**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ši komanda įdiegia paketą `langchain_nvidia_ai_endpoints`, užtikrinant, kad būtų naudojama naujausia versija.

2. **Importuoti reikalingus modulius**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Šie importai įtraukia reikalingus modulius, skirtus sąveikai su NVIDIA AI galiniais taškais, slaptažodžių saugiam tvarkymui, sąveikai su operacine sistema ir duomenų kodavimui/dekodavimui base64 formatu.

3. **Nustatyti API raktą**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Šis kodas patikrina, ar nustatytas aplinkos kintamasis `NVIDIA_API_KEY`. Jei ne, vartotojas raginamas saugiai įvesti savo API raktą.

4. **Apibrėžti modelį ir paveikslėlio kelią**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Čia nustatomas naudojamas modelis, sukuriamas `ChatNVIDIA` egzempliorius su nurodytu modeliu ir apibrėžiamas kelias iki paveikslėlio failo.

5. **Sukurti tekstinę užklausą**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Čia apibrėžiama tekstinė užklausa, nurodanti modeliui sugeneruoti Python kodą paveikslėlio apdorojimui.

6. **Užkoduoti paveikslėlį base64 formatu**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Šis kodas nuskaito paveikslėlio failą, užkoduoja jį base64 formatu ir sukuria HTML paveikslėlio žymą su užkoduotais duomenimis.

7. **Sujungti tekstą ir paveikslėlį į užklausą**:
    ```python
    prompt = f"{text} {image}"
    ```
    Čia tekstinė užklausa ir HTML paveikslėlio žyma sujungiami į vieną eilutę.

8. **Sugeneruoti kodą naudojant ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Šis kodas siunčia užklausą modeliui `ChatNVIDIA` ir surenka sugeneruotą kodą dalimis, spausdindamas ir pridedant kiekvieną dalį prie `code` eilutės.

9. **Išskirti Python kodą iš sugeneruoto turinio**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Čia iš sugeneruoto turinio išskiriamas tikrasis Python kodas, pašalinant markdown formatavimą.

10. **Vykdyti sugeneruotą kodą**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Šis kodas vykdo išskirtą Python kodą kaip subprocesą ir užfiksuoja jo išvestį.

11. **Parodyti paveikslėlius**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Šios eilutės naudoja modulį `IPython.display`, kad būtų parodyti paveikslėliai.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.