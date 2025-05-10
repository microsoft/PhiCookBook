<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:58:06+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "cs"
}
-->
### Example Scenario

Stel je voor dat je een afbeelding (`demo.png`) hebt en je wilt Python-code genereren die deze afbeelding verwerkt en een nieuwe versie ervan opslaat (`phi-3-vision.jpg`).

De bovenstaande code automatiseert dit proces door:

1. De omgeving en benodigde configuraties in te stellen.  
2. Een prompt te maken die het model instrueert om de benodigde Python-code te genereren.  
3. De prompt naar het model te sturen en de gegenereerde code te verzamelen.  
4. De gegenereerde code te extraheren en uit te voeren.  
5. De originele en verwerkte afbeeldingen weer te geven.

Deze aanpak benut de kracht van AI om beeldverwerkingstaken te automatiseren, waardoor het makkelijker en sneller wordt om je doelen te bereiken.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Laten we stap voor stap bekijken wat de hele code doet:

1. **Installeer Vereist Pakket**:  
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Dit commando installeert het `langchain_nvidia_ai_endpoints` pakket en zorgt ervoor dat je de nieuwste versie hebt.

2. **Importeer Benodigde Modules**:  
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Deze imports halen de benodigde modules binnen om te communiceren met de NVIDIA AI endpoints, wachtwoorden veilig te verwerken, met het besturingssysteem te werken en data in base64 te coderen/decoderen.

3. **Stel API-sleutel in**:  
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Deze code controleert of de `NVIDIA_API_KEY` omgevingsvariabele is ingesteld. Zo niet, dan vraagt het de gebruiker om de API-sleutel veilig in te voeren.

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

6. **Encodeer Afbeelding in Base64**:  
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Deze code leest het afbeeldingsbestand, codeert het in base64 en maakt een HTML `<img>`-tag met de gecodeerde data.

7. **Combineer Tekst en Afbeelding in Prompt**:  
    ```python
    prompt = f"{text} {image}"
    ```  
    Dit voegt de tekstprompt en de HTML-afbeeldingstag samen in één string.

8. **Genereer Code met ChatNVIDIA**:  
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Deze code stuurt de prompt naar de `ChatNVIDIA` en slaat de gegenereerde code op in de variabele `code`.

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

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.