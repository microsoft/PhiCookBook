<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:56:33+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "no"
}
-->
### Eksempelscenario

Tenk deg at du har et bilde (`demo.png`) og ønsker å generere Python-kode som behandler dette bildet og lagrer en ny versjon av det (`phi-3-vision.jpg`).

Koden over automatiserer denne prosessen ved å:

1. Sette opp miljøet og nødvendige konfigurasjoner.
2. Lage en prompt som instruerer modellen til å generere den nødvendige Python-koden.
3. Sende prompten til modellen og hente den genererte koden.
4. Ekstrahere og kjøre den genererte koden.
5. Vise det originale og det behandlede bildet.

Denne tilnærmingen utnytter AI sin kraft til å automatisere bildebehandlingsoppgaver, noe som gjør det enklere og raskere å nå målene dine.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

La oss gå gjennom hva hele koden gjør steg for steg:

1. **Installer nødvendig pakke**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Denne kommandoen installerer `langchain_nvidia_ai_endpoints`-pakken og sikrer at det er den nyeste versjonen.

2. **Importer nødvendige moduler**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Disse importene henter inn nødvendige moduler for å kommunisere med NVIDIA AI-endepunkter, håndtere passord sikkert, samhandle med operativsystemet og kode/dekode data i base64-format.

3. **Sett opp API-nøkkel**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Denne koden sjekker om miljøvariabelen `NVIDIA_API_KEY` er satt. Hvis ikke, ber den brukeren om å taste inn API-nøkkelen sikkert.

4. **Definer modell og bildefil**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Her settes modellen som skal brukes, en instans av `ChatNVIDIA` opprettes med den valgte modellen, og banen til bildefilen defineres.

5. **Lag tekstprompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Denne definerer en tekstprompt som instruerer modellen til å generere Python-kode for bildebehandling.

6. **Koding av bilde i base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Denne koden leser bildefilen, koder den i base64, og lager en HTML-bildetag med den kodede dataen.

7. **Kombiner tekst og bilde til prompt**:
    ```python
    prompt = f"{text} {image}"
    ```  
    Her kombineres tekstprompten og HTML-bildet i en enkelt streng.

8. **Generer kode med ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Denne koden sender prompten til `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-strengen.

9. **Ekstraher Python-kode fra generert innhold**:
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Denne delen trekker ut den faktiske Python-koden fra det genererte innholdet ved å fjerne markdown-formateringen.

10. **Kjør den genererte koden**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Denne kjører den ekstraherte Python-koden som en subprocess og fanger opp resultatet.

11. **Vis bilder**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Disse linjene viser bildene ved hjelp av `IPython.display`-modulen.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.