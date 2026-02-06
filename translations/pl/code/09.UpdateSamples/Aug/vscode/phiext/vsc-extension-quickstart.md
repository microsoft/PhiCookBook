# Witamy w Twoim rozszerzeniu VS Code

## Co znajduje się w folderze

* Ten folder zawiera wszystkie pliki niezbędne do działania Twojego rozszerzenia.
* `package.json` - to plik manifestu, w którym deklarujesz swoje rozszerzenie i komendę.
  * Przykładowy plugin rejestruje komendę i definiuje jej tytuł oraz nazwę. Dzięki tym informacjom VS Code może wyświetlić komendę w palecie poleceń. Nie musi jeszcze ładować pluginu.
* `src/extension.ts` - to główny plik, w którym zaimplementujesz swoją komendę.
  * Plik eksportuje jedną funkcję, `activate`, która jest wywoływana za pierwszym razem, gdy Twoje rozszerzenie zostanie aktywowane (w tym przypadku przez wykonanie komendy). Wewnątrz funkcji `activate` wywołujemy `registerCommand`.
  * Przekazujemy funkcję zawierającą implementację komendy jako drugi parametr do `registerCommand`.

## Konfiguracja

* zainstaluj zalecane rozszerzenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner oraz dbaeumer.vscode-eslint)

## Zacznij od razu

* Naciśnij `F5`, aby otworzyć nowe okno z załadowanym rozszerzeniem.
* Uruchom swoją komendę z palety poleceń, naciskając (`Ctrl+Shift+P` lub `Cmd+Shift+P` na Macu) i wpisując `Hello World`.
* Ustaw punkty przerwania w kodzie w pliku `src/extension.ts`, aby debugować rozszerzenie.
* Znajdź wyjście z rozszerzenia w konsoli debugowania.

## Wprowadzaj zmiany

* Możesz ponownie uruchomić rozszerzenie z paska narzędzi debugowania po zmianie kodu w `src/extension.ts`.
* Możesz także przeładować (`Ctrl+R` lub `Cmd+R` na Macu) okno VS Code z Twoim rozszerzeniem, aby załadować zmiany.

## Poznaj API

* Możesz otworzyć pełny zestaw naszego API, otwierając plik `node_modules/@types/vscode/index.d.ts`.

## Uruchamianie testów

* Zainstaluj [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Uruchom zadanie "watch" za pomocą polecenia **Tasks: Run Task**. Upewnij się, że jest uruchomione, inaczej testy mogą nie zostać wykryte.
* Otwórz widok Testów z paska aktywności i kliknij przycisk "Run Test" lub użyj skrótu `Ctrl/Cmd + ; A`
* Zobacz wyniki testów w widoku Test Results.
* Wprowadzaj zmiany w `src/test/extension.test.ts` lub twórz nowe pliki testowe w folderze `test`.
  * Dostarczony runner testów będzie brał pod uwagę tylko pliki pasujące do wzorca nazwy `**.test.ts`.
  * Możesz tworzyć foldery wewnątrz folderu `test`, aby dowolnie organizować swoje testy.

## Idź dalej

* Zmniejsz rozmiar rozszerzenia i przyspiesz czas uruchamiania, [pakując swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Opublikuj swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na rynku rozszerzeń VS Code.
* Zautomatyzuj budowanie, konfigurując [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.