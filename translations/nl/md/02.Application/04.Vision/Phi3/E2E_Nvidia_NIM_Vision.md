### Voorbeeldscenario

Stel je voor dat je een afbeelding hebt (`demo.png`) en je wilt Python-code genereren die deze afbeelding verwerkt en een nieuwe versie opslaat (`phi-3-vision.jpg`).

De bovenstaande code automatiseert dit proces door:

1. De omgeving en benodigde configuraties op te zetten.
2. Een prompt te maken die het model instrueert om de benodigde Python-code te genereren.
3. De prompt naar het model te sturen en de gegenereerde code te verzamelen.
4. De gegenereerde code te extraheren en uit te voeren.
5. De originele en verwerkte afbeeldingen weer te geven.

Deze aanpak maakt gebruik van de kracht van AI om beeldverwerkingstaken te automatiseren, waardoor het makkelijker en sneller wordt om je doelen te bereiken.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Laten we stap voor stap bekijken wat de hele code doet:

1. **Vereist pakket installeren**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Dit commando installeert het `langchain_nvidia_ai_endpoints` pakket en zorgt ervoor dat het de nieuwste versie is.

2. **Benodigde modules importeren**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Deze imports halen de benodigde modules binnen om te communiceren met de NVIDIA AI endpoints, wachtwoorden veilig te verwerken, met het besturingssysteem te werken en data in base64 te coderen/decoderen.

3. **API-sleutel instellen**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Deze code controleert of de omgevingsvariabele `NVIDIA_API_KEY` is ingesteld. Zo niet, dan vraagt het de gebruiker om de API-sleutel veilig in te voeren.

4. **Model en afbeeldingspad definiëren**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Hiermee wordt het te gebruiken model ingesteld, een instantie van `ChatNVIDIA` gemaakt met het opgegeven model, en het pad naar het afbeeldingsbestand gedefinieerd.

5. **Tekstprompt maken**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Dit definieert een tekstprompt die het model instrueert om Python-code te genereren voor het verwerken van een afbeelding.

6. **Afbeelding coderen in Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Deze code leest het afbeeldingsbestand, codeert het in base64 en maakt een HTML-afbeeldingstag met de gecodeerde data.

7. **Tekst en afbeelding combineren in prompt**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Dit combineert de tekstprompt en de HTML-afbeeldingstag tot één string.

8. **Code genereren met ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Deze code stuurt de prompt naar het `ChatNVIDIA` model en verzamelt de gegenereerde code in stukjes, print en voegt elk stuk toe aan de `code` string.

9. **Python-code uit gegenereerde inhoud halen**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Dit haalt de daadwerkelijke Python-code uit de gegenereerde inhoud door de markdown-opmaak te verwijderen.

10. **De gegenereerde code uitvoeren**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Dit voert de geëxtraheerde Python-code uit als een subprocess en vangt de output op.

11. **Afbeeldingen weergeven**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Deze regels tonen de afbeeldingen met behulp van de `IPython.display` module.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.