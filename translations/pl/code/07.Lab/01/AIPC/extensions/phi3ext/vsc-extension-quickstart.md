<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:55:45+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "pl"
}
-->
# Witamy w Twoim rozszerzeniu VS Code

## Co znajduje się w folderze

* Ten folder zawiera wszystkie pliki niezbędne do Twojego rozszerzenia.
* `package.json` - to jest plik manifestu, w którym deklarujesz swoje rozszerzenie i komendę.
  * Przykładowy plugin rejestruje komendę oraz definiuje jej tytuł i nazwę. Dzięki tym informacjom VS Code może wyświetlić komendę w palecie poleceń. Nie musi jeszcze ładować pluginu.
* `src/extension.ts` - to jest główny plik, w którym zaimplementujesz swoją komendę.
  * Plik eksportuje jedną funkcję, `activate`, która jest wywoływana przy pierwszej aktywacji rozszerzenia (w tym przypadku po wykonaniu komendy). Wewnątrz funkcji `activate` wywołujemy `registerCommand`.
  * Przekazujemy funkcję zawierającą implementację komendy jako drugi parametr do `registerCommand`.

## Konfiguracja

* zainstaluj zalecane rozszerzenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner oraz dbaeumer.vscode-eslint)


## Zacznij od razu

* Naciśnij `F5`, aby otworzyć nowe okno z załadowanym rozszerzeniem.
* Uruchom swoją komendę z palety poleceń, naciskając (`Ctrl+Shift+P` lub `Cmd+Shift+P` na Macu) i wpisując `Hello World`.
* Ustaw punkty przerwania w swoim kodzie w pliku `src/extension.ts`, aby debugować rozszerzenie.
* Znajdź wyjście z rozszerzenia w konsoli debugowania.

## Wprowadzanie zmian

* Możesz ponownie uruchomić rozszerzenie z paska narzędzi debugowania po zmianie kodu w `src/extension.ts`.
* Możesz także przeładować (`Ctrl+R` lub `Cmd+R` na Macu) okno VS Code z rozszerzeniem, aby załadować zmiany.


## Poznaj API

* Pełny zestaw naszego API możesz otworzyć, otwierając plik `node_modules/@types/vscode/index.d.ts`.

## Uruchamianie testów

* Zainstaluj [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Uruchom zadanie "watch" za pomocą polecenia **Tasks: Run Task**. Upewnij się, że działa, bo inaczej testy mogą nie zostać wykryte.
* Otwórz widok Testów na pasku aktywności i kliknij przycisk Run Test lub użyj skrótu `Ctrl/Cmd + ; A`
* Zobacz wyniki testów w widoku Test Results.
* Wprowadzaj zmiany w `src/test/extension.test.ts` lub twórz nowe pliki testowe w folderze `test`.
  * Dostarczony runner będzie brał pod uwagę tylko pliki pasujące do wzorca nazwy `**.test.ts`.
  * Możesz tworzyć podfoldery w folderze `test`, aby dowolnie organizować swoje testy.

## Idź dalej

* Zmniejsz rozmiar rozszerzenia i przyspiesz czas uruchamiania, [pakując swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Opublikuj swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) w marketplace rozszerzeń VS Code.
* Zautomatyzuj budowanie, konfigurując [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako autorytatywne źródło. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.