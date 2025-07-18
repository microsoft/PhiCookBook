<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-07-17T04:56:21+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "sv"
}
-->
### Exempelscenario

Föreställ dig att du har en bild (`demo.png`) och vill generera Python-kod som bearbetar denna bild och sparar en ny version av den (`phi-3-vision.jpg`).

Koden ovan automatiserar denna process genom att:

1. Ställa in miljön och nödvändiga konfigurationer.
2. Skapa en prompt som instruerar modellen att generera den önskade Python-koden.
3. Skicka prompten till modellen och samla in den genererade koden.
4. Extrahera och köra den genererade koden.
5. Visa originalbilden och den bearbetade bilden.

Denna metod utnyttjar AI:s kraft för att automatisera bildbehandlingsuppgifter, vilket gör det enklare och snabbare att nå dina mål.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Låt oss gå igenom vad hela koden gör steg för steg:

1. **Installera nödvändigt paket**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Detta kommando installerar paketet `langchain_nvidia_ai_endpoints` och säkerställer att det är den senaste versionen.

2. **Importera nödvändiga moduler**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Dessa importeringar hämtar de moduler som behövs för att interagera med NVIDIA AI-endpoints, hantera lösenord säkert, interagera med operativsystemet och koda/avkoda data i base64-format.

3. **Ställ in API-nyckel**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Denna kod kontrollerar om miljövariabeln `NVIDIA_API_KEY` är satt. Om inte, uppmanas användaren att ange sin API-nyckel på ett säkert sätt.

4. **Definiera modell och bildsökväg**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Här sätts modellen som ska användas, en instans av `ChatNVIDIA` skapas med den angivna modellen, och sökvägen till bildfilen definieras.

5. **Skapa textprompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Detta definierar en textprompt som instruerar modellen att generera Python-kod för att bearbeta en bild.

6. **Koda bilden i base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Denna kod läser in bildfilen, kodar den i base64 och skapar en HTML-bildtagg med den kodade datan.

7. **Kombinera text och bild till prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Här kombineras textprompten och HTML-bildtaggen till en enda sträng.

8. **Generera kod med ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Denna kod skickar prompten till `ChatNVIDIA`-modellen och samlar in den genererade koden i delar, skriver ut och lägger till varje del i strängen `code`.

9. **Extrahera Python-kod från genererat innehåll**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Detta extraherar den faktiska Python-koden från det genererade innehållet genom att ta bort markdown-formateringen.

10. **Kör den genererade koden**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Denna kör den extraherade Python-koden som en subprocess och fångar dess output.

11. **Visa bilderna**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Dessa rader visar bilderna med hjälp av modulen `IPython.display`.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.