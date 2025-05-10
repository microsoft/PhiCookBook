<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-09T19:58:24+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "ro"
}
-->
### Scenariu Exemplu

Imaginează-ți că ai o imagine (`demo.png`) și vrei să generezi cod Python care să proceseze această imagine și să salveze o versiune nouă a ei (`phi-3-vision.jpg`).

Codul de mai sus automatizează acest proces prin:

1. Configurarea mediului și setările necesare.
2. Crearea unui prompt care îi spune modelului să genereze codul Python necesar.
3. Trimiterea promptului către model și colectarea codului generat.
4. Extracția și rularea codului generat.
5. Afișarea imaginilor originale și procesate.

Această abordare folosește puterea AI pentru a automatiza sarcinile de procesare a imaginilor, făcându-le mai ușoare și mai rapide de realizat.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Să analizăm pas cu pas ce face întregul cod:

1. **Instalează Pachetul Necesare**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
    Această comandă instalează pachetul `langchain_nvidia_ai_endpoints`, asigurându-se că este versiunea cea mai recentă.

2. **Importă Modulele Necesare**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
    Aceste importuri aduc modulele necesare pentru interacțiunea cu endpoint-urile NVIDIA AI, gestionarea sigură a parolelor, interacțiunea cu sistemul de operare și codarea/decodarea datelor în format base64.

3. **Setează Cheia API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
    Acest cod verifică dacă variabila de mediu `NVIDIA_API_KEY` este setată. Dacă nu, solicită utilizatorului să introducă cheia API în mod securizat.

4. **Definește Modelul și Calea Imagini**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
    Aici se setează modelul ce va fi folosit, se creează o instanță a clasei `ChatNVIDIA` cu modelul specificat și se definește calea către fișierul imaginii.

5. **Creează Promptul Text**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
    Se definește un prompt text care instruiește modelul să genereze cod Python pentru procesarea unei imagini.

6. **Encodează Imaginea în Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
    Codul citește fișierul imaginii, îl encodează în base64 și creează un tag HTML de tip imagine cu datele codificate.

7. **Combină Textul și Imaginea în Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```  
    Aceasta combină promptul text și tag-ul HTML al imaginii într-un singur șir de caractere.

8. **Generează Cod folosind ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
    Codul trimite promptul către metoda `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`.

9. **Extrage Codul Python din Conținutul Generat**:
    ```python
    begin = code.index('```python') + 9  
    code = code[begin:]  
    end = code.index('```')
    code = code[:end]
    ```  
    Acest pas extrage codul Python efectiv din conținutul generat, eliminând formatarea markdown.

10. **Rulează Codul Generat**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    Codul extras este rulat ca un subprocess, iar output-ul său este capturat.

11. **Afișează Imaginile**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    Aceste linii afișează imaginile folosind modulul `IPython.display`.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.