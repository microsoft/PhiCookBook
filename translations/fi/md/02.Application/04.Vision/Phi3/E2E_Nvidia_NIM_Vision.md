<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:56:43+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "fi"
}
-->
### Esimerkkitilanne

Kuvittele, että sinulla on kuva (`demo.png`) ja haluat luoda Python-koodin, joka käsittelee tätä kuvaa ja tallentaa siitä uuden version (`phi-3-vision.jpg`).

Yllä oleva koodi automatisoi tämän prosessin seuraavasti:

1. Ympäristön ja tarvittavien asetusten määrittäminen.
2. Kehitetään kehotus, joka ohjeistaa mallia tuottamaan tarvittava Python-koodi.
3. Lähetetään kehotus mallille ja kerätään tuotettu koodi.
4. Erotetaan ja suoritetaan tuotettu koodi.
5. Näytetään alkuperäinen ja käsitelty kuva.

Tämä lähestymistapa hyödyntää tekoälyn voimaa kuvankäsittelytehtävien automatisointiin, mikä tekee tavoitteidesi saavuttamisesta helpompaa ja nopeampaa.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Käydään läpi, mitä koko koodi tekee vaihe vaiheelta:

1. **Asenna tarvittava paketti**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Tämä komento asentaa `langchain_nvidia_ai_endpoints`-paketin varmistaen, että se on uusin versio.

2. **Tuo tarvittavat moduulit**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Nämä tuonnit sisältävät moduulit, jotka mahdollistavat vuorovaikutuksen NVIDIA AI -päätepisteiden kanssa, salasanojen turvallisen käsittelyn, käyttöjärjestelmän kanssa työskentelyn sekä datan base64-koodauksen ja -dekoodauksen.

3. **Määritä API-avain**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Tämä koodi tarkistaa, onko `NVIDIA_API_KEY`-ympäristömuuttuja asetettu. Jos ei, se pyytää käyttäjää syöttämään API-avaimen turvallisesti.

4. **Määritä malli ja kuvan polku**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Tässä asetetaan käytettävä malli, luodaan `ChatNVIDIA`-instanssi määritetyllä mallilla ja määritellään kuvatiedoston polku.

5. **Luo tekstikehotus**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Tämä määrittelee tekstikehotuksen, joka ohjeistaa mallia tuottamaan Python-koodin kuvan käsittelyyn.

6. **Koodaa kuva base64-muotoon**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Tämä koodi lukee kuvatiedoston, koodaa sen base64-muotoon ja luo HTML-kuvatunnisteen koodatulla datalla.

7. **Yhdistä teksti ja kuva kehotukseksi**:
    ```python
    prompt = f"{text} {image}"
    ```  
    Tämä yhdistää tekstikehotuksen ja HTML-kuvatunnisteen yhdeksi merkkijonoksi.

8. **Luo koodi ChatNVIDIA:n avulla**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Tämä koodi lähettää kehotuksen `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-merkkijonolle.

9. **Erottele Python-koodi tuotetusta sisällöstä**:
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Tämä erottaa varsinaisen Python-koodin tuotetusta sisällöstä poistamalla markdown-muotoilun.

10. **Suorita tuotettu koodi**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Tämä suorittaa erotetun Python-koodin aliprosessina ja tallentaa sen tulosteen.

11. **Näytä kuvat**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Nämä rivit näyttävät kuvat `IPython.display`-moduulin avulla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.