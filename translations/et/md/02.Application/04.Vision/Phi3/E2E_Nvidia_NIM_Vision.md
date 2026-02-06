### Näitesituatsioon

Kujutlege, et teil on pilt (`demo.png`) ja soovite luua Python-koodi, mis töötleb seda pilti ja salvestab uue versiooni sellest (`phi-3-vision.jpg`).

Ülaltoodud kood automatiseerib selle protsessi järgmiselt:

1. Keskkonna ja vajalike seadistuste ettevalmistamine.
2. Teksti loomine, mis juhendab mudelit genereerima vajalikku Python-koodi.
3. Teksti saatmine mudelile ja genereeritud koodi kogumine.
4. Genereeritud koodi eraldamine ja käivitamine.
5. Algse ja töödeldud pildi kuvamine.

See lähenemine kasutab AI võimekust, et automatiseerida pilditöötlusülesandeid, muutes eesmärkide saavutamise lihtsamaks ja kiiremaks.

[Näidiskoodi lahendus](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Vaatame, mida kogu kood samm-sammult teeb:

1. **Nõutava paketi installimine**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    See käsk installib `langchain_nvidia_ai_endpoints` paketi, tagades, et see on uusim versioon.

2. **Vajalike moodulite importimine**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Need impordid toovad sisse vajalikud moodulid NVIDIA AI lõpp-punktidega suhtlemiseks, paroolide turvaliseks käsitlemiseks, operatsioonisüsteemiga suhtlemiseks ja andmete kodeerimiseks/dekodeerimiseks base64 formaadis.

3. **API-võtme seadistamine**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    See kood kontrollib, kas `NVIDIA_API_KEY` keskkonnamuutuja on seadistatud. Kui ei, palub see kasutajal sisestada API-võti turvaliselt.

4. **Mudel ja pildi tee määramine**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    See määrab kasutatava mudeli, loob `ChatNVIDIA` eksemplari määratud mudeliga ja määrab pildifaili tee.

5. **Teksti loomine**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    See määratleb teksti, mis juhendab mudelit genereerima Python-koodi pildi töötlemiseks.

6. **Pildi kodeerimine base64 formaadis**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    See kood loeb pildifaili, kodeerib selle base64 formaadis ja loob HTML-pildisildi kodeeritud andmetega.

7. **Teksti ja pildi ühendamine üheks tekstiks**:
    ```python
    prompt = f"{text} {image}"
    ```
    See ühendab teksti ja HTML-pildisildi üheks stringiks.

8. **Koodi genereerimine ChatNVIDIA abil**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    See kood saadab teksti `ChatNVIDIA` mudelile ja kogub genereeritud koodi osadena, printides ja lisades iga osa `code` stringi.

9. **Python-koodi eraldamine genereeritud sisust**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    See eraldab tegeliku Python-koodi genereeritud sisust, eemaldades markdown-formaadi.

10. **Genereeritud koodi käivitamine**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    See käivitab eraldatud Python-koodi alamprotsessina ja salvestab selle väljundi.

11. **Piltide kuvamine**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Need read kuvavad pilte, kasutades `IPython.display` moodulit.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.