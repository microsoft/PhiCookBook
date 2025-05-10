<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:55:28+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "it"
}
-->
### Scenario di esempio

Immagina di avere un'immagine (`demo.png`) e di voler generare del codice Python che elabori questa immagine e salvi una nuova versione (`phi-3-vision.jpg`).

Il codice sopra automatizza questo processo:

1. Configura l'ambiente e le impostazioni necessarie.
2. Crea un prompt che istruisce il modello a generare il codice Python richiesto.
3. Invia il prompt al modello e raccoglie il codice generato.
4. Estrae ed esegue il codice generato.
5. Mostra le immagini originale ed elaborata.

Questo approccio sfrutta la potenza dell'AI per automatizzare le attività di elaborazione delle immagini, rendendo più semplice e veloce il raggiungimento dei tuoi obiettivi.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Analizziamo passo passo cosa fa l'intero codice:

1. **Installa il pacchetto richiesto**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Questo comando installa il pacchetto `langchain_nvidia_ai_endpoints`, assicurandosi che sia l'ultima versione.

2. **Importa i moduli necessari**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Questi import includono i moduli necessari per interagire con gli endpoint NVIDIA AI, gestire le password in modo sicuro, interagire con il sistema operativo e codificare/decodificare dati in base64.

3. **Imposta la chiave API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Questo codice verifica se la variabile d'ambiente `NVIDIA_API_KEY` è impostata. In caso contrario, chiede all'utente di inserire la chiave API in modo sicuro.

4. **Definisce il modello e il percorso dell'immagine**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Qui viene impostato il modello da usare, creato un oggetto `ChatNVIDIA` con il modello specificato e definito il percorso del file immagine.

5. **Crea il prompt testuale**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Qui viene definito un prompt testuale che istruisce il modello a generare codice Python per elaborare un'immagine.

6. **Codifica l'immagine in base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Questo codice legge il file immagine, lo codifica in base64 e crea un tag HTML `<img>` con i dati codificati.

7. **Combina testo e immagine nel prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Qui testo e tag immagine HTML vengono combinati in un'unica stringa.

8. **Genera il codice usando ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Questo codice invia il prompt a `ChatNVIDIA` e ottiene la stringa di codice generato.

9. **Estrae il codice Python dal contenuto generato**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Qui si estrae il codice Python vero e proprio dal contenuto generato, eliminando la formattazione markdown.

10. **Esegue il codice generato**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Questo esegue il codice Python estratto come subprocess e ne cattura l'output.

11. **Mostra le immagini**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Queste righe mostrano le immagini utilizzando il modulo `IPython.display`.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un esperto umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.