# Contributing

Ten projekt zachęca do zgłaszania wkładów i sugestii. Większość wkładów wymaga zgody na Contributor License Agreement (CLA), w którym oświadczasz, że masz prawo i faktycznie udzielasz nam praw do korzystania z Twojego wkładu. Szczegóły znajdziesz na [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Po przesłaniu pull requesta, bot CLA automatycznie sprawdzi, czy musisz dostarczyć CLA i odpowiednio oznaczy PR (np. status check, komentarz). Wystarczy, że wykonasz to raz dla wszystkich repozytoriów korzystających z naszego CLA.

## Code of Conduct

Projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Więcej informacji znajdziesz w [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) lub skontaktuj się pod adresem [opencode@microsoft.com](mailto:opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Cautions for creating issues

Prosimy, aby nie otwierać zgłoszeń na GitHub w sprawie ogólnych pytań dotyczących wsparcia, ponieważ lista na GitHub powinna służyć do zgłaszania propozycji funkcji i błędów. Dzięki temu łatwiej jest nam śledzić rzeczywiste problemy lub błędy w kodzie i oddzielić ogólną dyskusję od kwestii związanych z kodem.

## How to Contribute

### Pull Requests Guidelines

Przy przesyłaniu pull requesta (PR) do repozytorium Phi-3 CookBook, prosimy o stosowanie się do poniższych zasad:

- **Forkuj repozytorium**: Zawsze wykonaj fork repozytorium na swoje konto przed wprowadzeniem zmian.

- **Oddzielne pull requesty (PR)**:
  - Każdy rodzaj zmiany zgłaszaj w osobnym pull requeście. Na przykład poprawki błędów i aktualizacje dokumentacji powinny być zgłaszane oddzielnie.
  - Poprawki literówek i drobne aktualizacje dokumentacji można łączyć w jednym PR, jeśli to stosowne.

- **Rozwiązywanie konfliktów scalania**: Jeśli Twój pull request pokazuje konflikty scalania, zaktualizuj lokalną gałąź `main`, aby odzwierciedlała główne repozytorium, zanim wprowadzisz zmiany.

- **Zgłaszanie tłumaczeń**: Przy przesyłaniu PR z tłumaczeniem upewnij się, że folder z tłumaczeniem zawiera przekłady wszystkich plików z oryginalnego folderu.

### Writing Guidelines

Aby zapewnić spójność dokumentów, prosimy o stosowanie się do poniższych wytycznych:

- **Formatowanie URL**: Umieszczaj wszystkie adresy URL w nawiasach kwadratowych, po których następują nawiasy okrągłe, bez dodatkowych spacji wokół lub wewnątrz. Na przykład: `[example](https://www.microsoft.com)`.

- **Linki względne**: Używaj `./` dla linków względnych wskazujących na pliki lub foldery w bieżącym katalogu oraz `../` dla tych w katalogu nadrzędnym. Na przykład: `[example](../../path/to/file)` lub `[example](../../../path/to/file)`.

- **Nie używaj lokalizacji specyficznych dla kraju**: Upewnij się, że Twoje linki nie zawierają lokalizacji specyficznych dla kraju. Na przykład unikaj `/en-us/` lub `/en/`.

- **Przechowywanie obrazów**: Wszystkie obrazy przechowuj w folderze `./imgs`.

- **Opisowe nazwy obrazów**: Nazwy obrazów powinny być opisowe i używać znaków angielskich, cyfr oraz myślników. Na przykład: `example-image.jpg`.

## GitHub Workflows

Po przesłaniu pull requesta uruchamiane są następujące workflow, które weryfikują zmiany. Postępuj zgodnie z poniższymi instrukcjami, aby Twój pull request przeszedł pomyślnie kontrole workflow:

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Ten workflow sprawdza, czy wszystkie ścieżki względne w Twoich plikach są poprawne.

1. Aby upewnić się, że Twoje linki działają prawidłowo, wykonaj następujące czynności w VS Code:
    - Najedź kursorem na dowolny link w plikach.
    - Naciśnij **Ctrl + Kliknięcie**, aby przejść do linku.
    - Jeśli kliknięcie linku nie działa lokalnie, workflow zostanie uruchomiony i link nie zadziała również na GitHub.

1. Aby naprawić ten problem, wykonaj następujące czynności, korzystając z podpowiedzi ścieżek w VS Code:
    - Wpisz `./` lub `../`.
    - VS Code zaproponuje dostępne opcje na podstawie wpisanego tekstu.
    - Wybierz odpowiedni plik lub folder, klikając, aby upewnić się, że ścieżka jest poprawna.

Po dodaniu poprawnej ścieżki względnej zapisz i wypchnij zmiany.

### Check URLs Don't Have Locale

Ten workflow sprawdza, czy adresy URL nie zawierają lokalizacji specyficznej dla kraju. Ponieważ repozytorium jest dostępne globalnie, ważne jest, aby adresy URL nie zawierały lokalizacji Twojego kraju.

1. Aby zweryfikować, że Twoje adresy URL nie zawierają lokalizacji kraju, wykonaj następujące czynności:

    - Sprawdź, czy w adresach URL nie ma tekstu takiego jak `/en-us/`, `/en/` lub innych lokalizacji językowych.
    - Jeśli ich nie ma, test zostanie zaliczony.

1. Aby naprawić ten problem, wykonaj następujące czynności:
    - Otwórz plik wskazany przez workflow.
    - Usuń lokalizację kraju z adresów URL.

Po usunięciu lokalizacji kraju zapisz i wypchnij zmiany.

### Check Broken Urls

Ten workflow sprawdza, czy wszystkie adresy URL w Twoich plikach działają i zwracają kod statusu 200.

1. Aby zweryfikować, że Twoje adresy URL działają poprawnie, wykonaj następujące czynności:
    - Sprawdź status adresów URL w swoich plikach.

2. Aby naprawić uszkodzone adresy URL, wykonaj następujące czynności:
    - Otwórz plik zawierający uszkodzony adres URL.
    - Zaktualizuj adres URL na poprawny.

Po naprawieniu adresów URL zapisz i wypchnij zmiany.

> [!NOTE]
>
> Mogą zdarzyć się sytuacje, w których sprawdzanie adresów URL zakończy się niepowodzeniem, mimo że link jest dostępny. Może się tak zdarzyć z kilku powodów, w tym:
>
> - **Ograniczenia sieciowe:** Serwery GitHub Actions mogą mieć ograniczenia sieciowe uniemożliwiające dostęp do niektórych adresów URL.
> - **Problemy z czasem oczekiwania:** Adresy URL, które odpowiadają zbyt długo, mogą wywołać błąd timeout w workflow.
> - **Tymczasowe problemy serwera:** Okazjonalne przerwy w działaniu serwera lub prace konserwacyjne mogą sprawić, że adres URL będzie chwilowo niedostępny podczas weryfikacji.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.