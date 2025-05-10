<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:59:00+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "sl"
}
-->
### Example Scenario

Pretvarajmo, da imate sliko (`demo.png`) in želite ustvariti Python kodo, ki obdela to sliko ter shrani novo različico (`phi-3-vision.jpg`).

Zgornja koda avtomatizira ta postopek tako, da:

1. Nastavi okolje in potrebne konfiguracije.
2. Ustvari poziv, ki modelu naroči, naj generira zahtevano Python kodo.
3. Pošlje poziv modelu in zbere generirano kodo.
4. Izvleče in zažene generirano kodo.
5. Prikaže izvirno in obdelano sliko.

Ta pristop izkorišča moč umetne inteligence za avtomatizacijo opravil obdelave slik, kar omogoča lažje in hitrejše doseganje vaših ciljev.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Razčlenimo, kaj celotna koda počne, korak za korakom:

1. **Namesti potrebni paket**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Ta ukaz namesti paket `langchain_nvidia_ai_endpoints` in zagotovi, da je najnovejša različica.

2. **Uvozi potrebne module**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Ti uvozi priskrbijo potrebne module za delo z NVIDIA AI končnimi točkami, varno upravljanje gesel, delo z operacijskim sistemom ter kodiranje/dekodiranje v base64 formatu.

3. **Nastavi API ključ**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Ta koda preveri, ali je okoljska spremenljivka `NVIDIA_API_KEY` nastavljena. Če ni, uporabnika varno pozove, da vnese svoj API ključ.

4. **Določi model in pot do slike**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Določi model, ki se bo uporabljal, ustvari primerek `ChatNVIDIA` z določenim modelom in nastavi pot do slikovne datoteke.

5. **Ustvari besedilni poziv**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Določi besedilni poziv, ki modelu naroča, naj generira Python kodo za obdelavo slike.

6. **Kodira sliko v base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Ta koda prebere slikovno datoteko, jo kodira v base64 in ustvari HTML `<img>` tag z vključenimi podatki.

7. **Združi besedilo in sliko v poziv**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Združi besedilni poziv in HTML `<img>` tag v en sam niz.

8. **Generira kodo z uporabo ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Ta koda pošlje poziv modelu `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` nizu.

9. **Izvleče Python kodo iz generirane vsebine**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Ta del izvleče dejansko Python kodo iz generirane vsebine, tako da odstrani markdown oblikovanje.

10. **Zažene generirano kodo**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Zažene izvlečeno Python kodo kot podproces in zajame njen izhod.

11. **Prikaže slike**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Te vrstice prikažejo slike z uporabo modula `IPython.display`.

**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.