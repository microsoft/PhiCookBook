<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:56:52+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "fi"
}
-->
### Esimerkkitilanne

Kuvittele, että sinulla on kuva (`demo.png`) ja haluat luoda Python-koodin, joka käsittelee tätä kuvaa ja tallentaa siitä uuden version (`phi-3-vision.jpg`).

Yllä oleva koodi automatisoi tämän prosessin seuraavasti:

1. Ympäristön ja tarvittavien asetusten määrittäminen.
2. Kehittää kehotteen, joka ohjeistaa mallia luomaan tarvittavan Python-koodin.
3. Lähettää kehotteen mallille ja kerää luodun koodin.
4. Erottaa ja suorittaa luodun koodin.
5. Näyttää alkuperäisen ja käsitellyn kuvan.

Tämä lähestymistapa hyödyntää tekoälyn voimaa kuvankäsittelytehtävien automatisointiin, mikä tekee tavoitteiden saavuttamisesta helpompaa ja nopeampaa.

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
    Nämä tuonnit tuovat tarvittavat moduulit NVIDIA AI -päätepisteiden kanssa työskentelyyn, salasanojen turvalliseen käsittelyyn, käyttöjärjestelmän kanssa vuorovaikutukseen sekä base64-koodauksen ja -dekoodauksen hallintaan.

3. **Aseta API-avain**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Tämä koodi tarkistaa, onko `NVIDIA_API_KEY`-ympäristömuuttuja asetettu. Jos ei ole, se pyytää käyttäjää syöttämään API-avaimensa turvallisesti.

4. **Määritä malli ja kuvan polku**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Tässä asetetaan käytettävä malli, luodaan `ChatNVIDIA`-instanssi määritetyllä mallilla ja määritellään kuvatiedoston polku.

5. **Luo tekstikehote**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Tämä määrittelee tekstikehotteen, joka ohjeistaa mallia luomaan Python-koodin kuvan käsittelyä varten.

6. **Koodaa kuva base64-muotoon**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Tämä koodi lukee kuvatiedoston, koodaa sen base64-muotoon ja luo HTML-kuvatagin koodatulla datalla.

7. **Yhdistä teksti ja kuva kehotteeksi**:
    ```python
    prompt = f"{text} {image}"
    ```
    Tämä yhdistää tekstikehotteen ja HTML-kuvatagin yhdeksi merkkijonoksi.

8. **Luo koodi ChatNVIDIA:n avulla**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Tämä koodi lähettää kehotteen `ChatNVIDIA`-mallille ja kerää luodun koodin paloina, tulostaen ja liittäen jokaisen palan `code`-merkkijonoon.

9. **Erottele Python-koodi luodusta sisällöstä**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Tämä erottaa varsinaisen Python-koodin luodusta sisällöstä poistamalla markdown-muotoilun.

10. **Suorita luotu koodi**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Tämä suorittaa erotellun Python-koodin aliohjelmana ja tallentaa sen tulosteen.

11. **Näytä kuvat**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Nämä rivit näyttävät kuvat `IPython.display`-moduulin avulla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.