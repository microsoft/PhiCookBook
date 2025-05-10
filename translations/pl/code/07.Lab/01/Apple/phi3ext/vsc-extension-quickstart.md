<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:07:31+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "pl"
}
-->
# Witamy w Twoim rozszerzeniu VS Code

## Co znajduje się w folderze

* Ten folder zawiera wszystkie pliki niezbędne do działania Twojego rozszerzenia.
* `package.json` - to plik manifestu, w którym deklarujesz swoje rozszerzenie i polecenie.
  * Przykładowy plugin rejestruje polecenie oraz definiuje jego tytuł i nazwę polecenia. Dzięki tym informacjom VS Code może wyświetlić polecenie w palecie poleceń. Nie musi jeszcze ładować pluginu.
* `src/extension.ts` - to główny plik, w którym zaimplementujesz swoje polecenie.
  * Plik eksportuje jedną funkcję, `activate`, która jest wywoływana za pierwszym razem, gdy Twoje rozszerzenie zostanie aktywowane (w tym przypadku przez wykonanie polecenia). Wewnątrz funkcji `activate` wywołujemy `registerCommand`.
  * Przekazujemy funkcję zawierającą implementację polecenia jako drugi parametr do `registerCommand`.

## Konfiguracja

* zainstaluj zalecane rozszerzenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner oraz dbaeumer.vscode-eslint)


## Zacznij od razu

* Naciśnij `F5`, aby otworzyć nowe okno z załadowanym rozszerzeniem.
* Uruchom polecenie z palety poleceń, naciskając (`Ctrl+Shift+P` lub `Cmd+Shift+P` na Macu) i wpisując `Hello World`.
* Ustaw punkty przerwania w kodzie w `src/extension.ts`, aby debugować rozszerzenie.
* Znajdź wynik działania rozszerzenia w konsoli debugowania.

## Wprowadzaj zmiany

* Możesz ponownie uruchomić rozszerzenie z paska narzędzi debugowania po zmianach w `src/extension.ts`.
* Możesz też przeładować (`Ctrl+R` lub `Cmd+R` na Macu) okno VS Code z Twoim rozszerzeniem, aby załadować zmiany.


## Poznaj API

* Pełny zestaw naszego API możesz otworzyć, otwierając plik `node_modules/@types/vscode/index.d.ts`.

## Uruchamianie testów

* Zainstaluj [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Uruchom zadanie "watch" za pomocą polecenia **Tasks: Run Task**. Upewnij się, że jest ono uruchomione, bo inaczej testy mogą nie zostać wykryte.
* Otwórz widok Testowanie z paska aktywności i kliknij przycisk Run Test lub użyj skrótu klawiszowego `Ctrl/Cmd + ; A`
* Zobacz wynik testów w widoku Test Results.
* Wprowadzaj zmiany w `src/test/extension.test.ts` lub twórz nowe pliki testowe w folderze `test`.
  * Dostarczony runner testów będzie uwzględniał tylko pliki pasujące do wzorca nazwy `**.test.ts`.
  * Możesz tworzyć podfoldery w folderze `test`, aby dowolnie organizować swoje testy.

## Idź dalej

* Zmniejsz rozmiar rozszerzenia i przyspiesz jego uruchamianie, [pakując swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Opublikuj swoje rozszerzenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) w marketplace VS Code.
* Zautomatyzuj budowanie, konfigurując [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o istotnym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.