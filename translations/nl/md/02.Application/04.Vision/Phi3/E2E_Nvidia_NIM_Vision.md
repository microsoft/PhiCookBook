<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:56:52+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "nl"
}
-->
### Voorbeeldscenario

Stel je voor dat je een afbeelding (`demo.png`) hebt en je wilt Python-code genereren die deze afbeelding verwerkt en een nieuwe versie ervan opslaat (`phi-3-vision.jpg`).

De bovenstaande code automatiseert dit proces door:

1. De omgeving en benodigde configuraties in te stellen.
2. Een prompt te maken die het model instrueert om de benodigde Python-code te genereren.
3. De prompt naar het model te sturen en de gegenereerde code te verzamelen.
4. De gegenereerde code te extraheren en uit te voeren.
5. De originele en verwerkte afbeeldingen weer te geven.

Deze aanpak benut de kracht van AI om taken voor beeldverwerking te automatiseren, waardoor het eenvoudiger en sneller wordt om je doelen te bereiken.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Laten we stap voor stap bekijken wat de hele code doet:

1. **Installeer Vereist Pakket**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Dit commando installeert het `langchain_nvidia_ai_endpoints` pakket en zorgt ervoor dat je de nieuwste versie hebt.

2. **Importeer Nodige Modules**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Deze imports halen de benodigde modules binnen om te communiceren met de NVIDIA AI endpoints, wachtwoorden veilig te behandelen, met het besturingssysteem te werken en data te coderen/decoderen in base64-formaat.

3. **Stel API-sleutel in**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Deze code controleert of de omgevingsvariabele `NVIDIA_API_KEY` is ingesteld. Zo niet, dan wordt de gebruiker gevraagd om zijn API-sleutel veilig in te voeren.

4. **Definieer Model en Afbeeldingspad**:  
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Dit stelt het te gebruiken model in, maakt een instantie van `ChatNVIDIA` met het opgegeven model en definieert het pad naar het afbeeldingsbestand.

5. **Maak Tekstprompt**:  
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Dit definieert een tekstprompt die het model instrueert om Python-code te genereren voor het verwerken van een afbeelding.

6. **Codeer Afbeelding in Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Deze code leest het afbeeldingsbestand, codeert het in base64 en maakt een HTML-afbeeldingstag met de gecodeerde data.

7. **Combineer Tekst en Afbeelding in Prompt**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Dit voegt de tekstprompt en de HTML-afbeeldingstag samen tot één string.

8. **Genereer Code met ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Deze code stuurt de prompt naar `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Extraheer Python-code uit de gegenereerde inhoud**:  
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Dit haalt de daadwerkelijke Python-code uit de gegenereerde inhoud door de markdown-opmaak te verwijderen.

10. **Voer de gegenereerde code uit**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Dit voert de geëxtraheerde Python-code uit als een subprocess en vangt de uitvoer op.

11. **Toon Afbeeldingen**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Deze regels tonen de afbeeldingen met behulp van de `IPython.display` module.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.