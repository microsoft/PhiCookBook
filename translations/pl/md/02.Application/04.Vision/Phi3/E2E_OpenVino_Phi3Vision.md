Ten demo pokazuje, jak użyć wstępnie wytrenowanego modelu do generowania kodu w Pythonie na podstawie obrazu i tekstowego polecenia.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Oto wyjaśnienie krok po kroku:

1. **Importy i konfiguracja**:
   - Importowane są niezbędne biblioteki i moduły, w tym `requests`, `PIL` do przetwarzania obrazów oraz `transformers` do obsługi modelu i przetwarzania.

2. **Ładowanie i wyświetlanie obrazu**:
   - Plik obrazu (`demo.png`) jest otwierany za pomocą biblioteki `PIL` i wyświetlany.

3. **Definiowanie polecenia**:
   - Tworzona jest wiadomość zawierająca obraz oraz prośbę o wygenerowanie kodu w Pythonie, który przetworzy obraz i zapisze go przy użyciu `plt` (matplotlib).

4. **Ładowanie procesora**:
   - `AutoProcessor` jest ładowany z wstępnie wytrenowanego modelu określonego przez katalog `out_dir`. Ten procesor obsłuży wejścia tekstowe i obrazowe.

5. **Tworzenie polecenia**:
   - Metoda `apply_chat_template` jest używana do sformatowania wiadomości w polecenie odpowiednie dla modelu.

6. **Przetwarzanie wejść**:
   - Polecenie i obraz są przetwarzane na tensory, które model potrafi zinterpretować.

7. **Ustawianie argumentów generowania**:
   - Definiowane są argumenty dla procesu generowania modelu, w tym maksymalna liczba nowych tokenów do wygenerowania oraz czy wynik ma być próbkowany.

8. **Generowanie kodu**:
   - Model generuje kod w Pythonie na podstawie wejść i argumentów generowania. `TextStreamer` jest używany do obsługi wyjścia, pomijając polecenie i specjalne tokeny.

9. **Wynik**:
   - Wygenerowany kod jest wyświetlany, powinien zawierać kod Pythona do przetworzenia obrazu i zapisania go zgodnie z poleceniem.

To demo pokazuje, jak wykorzystać wstępnie wytrenowany model z OpenVino do dynamicznego generowania kodu na podstawie danych wejściowych od użytkownika i obrazów.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.