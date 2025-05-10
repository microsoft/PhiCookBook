<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:00:06+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "pl"
}
-->
To demo pokazuje, jak użyć wstępnie wytrenowanego modelu do generowania kodu w Pythonie na podstawie obrazu i tekstowego promptu.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Oto wyjaśnienie krok po kroku:

1. **Importy i konfiguracja**:
   - Importowane są niezbędne biblioteki i moduły, w tym `requests`, `PIL` do przetwarzania obrazów oraz `transformers` do obsługi modelu i przetwarzania.

2. **Ładowanie i wyświetlanie obrazu**:
   - Plik z obrazem (`demo.png`) jest otwierany za pomocą biblioteki `PIL` i wyświetlany.

3. **Definiowanie promptu**:
   - Tworzona jest wiadomość zawierająca obraz oraz prośbę o wygenerowanie kodu w Pythonie do przetworzenia obrazu i zapisania go za pomocą `plt` (matplotlib).

4. **Ładowanie procesora**:
   - `AutoProcessor` jest ładowany z wstępnie wytrenowanego modelu wskazanego przez katalog `out_dir`. Ten procesor obsłuży tekst i obrazy.

5. **Tworzenie promptu**:
   - Metoda `apply_chat_template` służy do sformatowania wiadomości w prompt odpowiedni dla modelu.

6. **Przetwarzanie danych wejściowych**:
   - Prompt i obraz są przetwarzane na tensory zrozumiałe dla modelu.

7. **Ustawianie argumentów generowania**:
   - Definiowane są argumenty dla procesu generowania modelu, w tym maksymalna liczba nowych tokenów do wygenerowania oraz czy próbować losowego próbkowania wyniku.

8. **Generowanie kodu**:
   - Model generuje kod w Pythonie na podstawie danych wejściowych i argumentów generowania. `TextStreamer` służy do obsługi wyjścia, pomijając prompt i specjalne tokeny.

9. **Wynik**:
   - Wygenerowany kod jest wypisywany, powinien zawierać kod w Pythonie do przetworzenia obrazu i zapisania go zgodnie z promptem.

Ten demo pokazuje, jak wykorzystać wstępnie wytrenowany model z OpenVino do dynamicznego generowania kodu na podstawie danych wejściowych użytkownika i obrazów.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.