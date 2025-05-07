<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-07T10:59:03+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "de"
}
-->
### Beispiel-Szenario

Stellen Sie sich vor, Sie haben ein Bild (`demo.png`) und möchten Python-Code generieren, der dieses Bild verarbeitet und eine neue Version davon speichert (`phi-3-vision.jpg`).

Der obige Code automatisiert diesen Prozess, indem er:

1. Die Umgebung und erforderliche Konfigurationen einrichtet.
2. Einen Prompt erstellt, der das Modell anweist, den benötigten Python-Code zu generieren.
3. Den Prompt an das Modell sendet und den generierten Code sammelt.
4. Den generierten Code extrahiert und ausführt.
5. Das Originalbild und das verarbeitete Bild anzeigt.

Dieser Ansatz nutzt die Kraft von KI, um Bildverarbeitungsaufgaben zu automatisieren und so die Erreichung Ihrer Ziele einfacher und schneller zu machen.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Lassen Sie uns Schritt für Schritt durchgehen, was der gesamte Code macht:

1. **Benötigtes Paket installieren**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Dieser Befehl installiert das Paket `langchain_nvidia_ai_endpoints` und stellt sicher, dass die neueste Version verwendet wird.

2. **Notwendige Module importieren**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Diese Importe bringen die erforderlichen Module mit, um mit den NVIDIA AI-Endpunkten zu interagieren, Passwörter sicher zu handhaben, mit dem Betriebssystem zu arbeiten und Daten im base64-Format zu kodieren/dekodieren.

3. **API-Schlüssel einrichten**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Dieser Code prüft, ob die Umgebungsvariable `NVIDIA_API_KEY` gesetzt ist. Falls nicht, wird der Nutzer aufgefordert, seinen API-Schlüssel sicher einzugeben.

4. **Modell und Bildpfad definieren**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Hier wird das zu verwendende Modell festgelegt, eine Instanz von `ChatNVIDIA` mit dem angegebenen Modell erstellt und der Pfad zur Bilddatei definiert.

5. **Text-Prompt erstellen**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Dieser Abschnitt definiert einen Text-Prompt, der das Modell anweist, Python-Code zur Bildverarbeitung zu generieren.

6. **Bild in Base64 kodieren**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Dieser Code liest die Bilddatei ein, kodiert sie in base64 und erstellt ein HTML-Bild-Tag mit den kodierten Daten.

7. **Text und Bild zum Prompt kombinieren**:
    ```python
    prompt = f"{text} {image}"
    ```
    Hier werden der Text-Prompt und das HTML-Bild-Tag zu einem einzigen String kombiniert.

8. **Code mit ChatNVIDIA generieren**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Dieser Code sendet den Prompt an die `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-Zeichenkette.

9. **Python-Code aus generiertem Inhalt extrahieren**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Hier wird der tatsächliche Python-Code aus dem generierten Inhalt extrahiert, indem die Markdown-Formatierung entfernt wird.

10. **Generierten Code ausführen**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Dieser Schritt führt den extrahierten Python-Code als Subprozess aus und fängt dessen Ausgabe ab.

11. **Bilder anzeigen**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Diese Zeilen zeigen die Bilder mit dem Modul `IPython.display` an.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.