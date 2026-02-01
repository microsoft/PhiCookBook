### Przykładowy scenariusz

Wyobraź sobie, że masz obraz (`demo.png`) i chcesz wygenerować kod w Pythonie, który przetworzy ten obraz i zapisze nową wersję (`phi-3-vision.jpg`).

Powyższy kod automatyzuje ten proces poprzez:

1. Konfigurację środowiska i niezbędnych ustawień.
2. Utworzenie promptu, który instruuje model, aby wygenerował potrzebny kod w Pythonie.
3. Wysłanie promptu do modelu i zebranie wygenerowanego kodu.
4. Wyodrębnienie i uruchomienie wygenerowanego kodu.
5. Wyświetlenie oryginalnego i przetworzonego obrazu.

To podejście wykorzystuje moc AI do automatyzacji zadań związanych z przetwarzaniem obrazów, co ułatwia i przyspiesza osiąganie celów.

[Przykładowe rozwiązanie kodu](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Przeanalizujmy krok po kroku, co robi cały kod:

1. **Zainstaluj wymagany pakiet**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    To polecenie instaluje pakiet `langchain_nvidia_ai_endpoints`, zapewniając, że jest to najnowsza wersja.

2. **Importuj niezbędne moduły**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Te importy wprowadzają potrzebne moduły do interakcji z punktami końcowymi NVIDIA AI, bezpiecznego obsługiwania haseł, pracy z systemem operacyjnym oraz kodowania/odkodowywania danych w formacie base64.

3. **Ustaw klucz API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ten fragment kodu sprawdza, czy zmienna środowiskowa `NVIDIA_API_KEY` jest ustawiona. Jeśli nie, prosi użytkownika o bezpieczne wprowadzenie klucza API.

4. **Zdefiniuj model i ścieżkę do obrazu**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Tutaj ustawiany jest model do użycia, tworzona jest instancja `ChatNVIDIA` z określonym modelem oraz definiowana jest ścieżka do pliku obrazu.

5. **Utwórz tekstowy prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Definiuje prompt tekstowy, który instruuje model, aby wygenerował kod Pythona do przetwarzania obrazu.

6. **Zakoduj obraz w base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ten kod odczytuje plik obrazu, koduje go w base64 i tworzy tag HTML obrazu z zakodowanymi danymi.

7. **Połącz tekst i obraz w jeden prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Łączy prompt tekstowy i tag HTML obrazu w jeden ciąg znaków.

8. **Wygeneruj kod za pomocą ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ten kod wysyła prompt do modelu `ChatNVIDIA` i zbiera wygenerowany kod w kawałkach, drukując i dopisując każdy fragment do zmiennej `code`.

9. **Wyodrębnij kod Pythona z wygenerowanej zawartości**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Ten fragment wyciąga właściwy kod Pythona z wygenerowanej zawartości, usuwając formatowanie markdown.

10. **Uruchom wygenerowany kod**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Uruchamia wyodrębniony kod Pythona jako podproces i przechwytuje jego wyjście.

11. **Wyświetl obrazy**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Te linie wyświetlają obrazy za pomocą modułu `IPython.display`.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.