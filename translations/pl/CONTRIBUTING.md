<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:28:24+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pl"
}
-->
# Contributing

Ten projekt zachęca do wkładu i sugestii. Większość wkładów wymaga zgody na
Contributor License Agreement (CLA), w którym oświadczasz, że masz prawo i faktycznie udzielasz nam
praw do korzystania z Twojego wkładu. Szczegóły znajdziesz na [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Podczas zgłaszania pull requesta, bot CLA automatycznie sprawdzi, czy musisz dostarczyć
CLA i odpowiednio oznaczy PR (np. sprawdzenie statusu, komentarz). Wystarczy, że wykonasz to raz dla wszystkich repozytoriów korzystających z naszego CLA.

## Code of Conduct

Projekt przyjął [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Więcej informacji znajdziesz w [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) lub skontaktuj się pod adresem [opencode@microsoft.com](mailto:opencode@microsoft.com) w razie dodatkowych pytań lub uwag.

## Cautions for creating issues

Prosimy nie otwierać zgłoszeń na GitHub w celu uzyskania ogólnego wsparcia, ponieważ lista GitHub powinna służyć do zgłaszania propozycji funkcji i błędów. Dzięki temu łatwiej będzie nam śledzić rzeczywiste problemy lub błędy w kodzie i oddzielić ogólną dyskusję od faktycznego kodu.

## How to Contribute

### Pull Requests Guidelines

Podczas wysyłania pull requesta (PR) do repozytorium Phi-3 CookBook, prosimy stosować się do poniższych wytycznych:

- **Forkuj repozytorium**: Zawsze forkij repozytorium na swoje konto zanim wprowadzisz zmiany.

- **Oddzielne pull requesty (PR)**:
  - Każdy rodzaj zmiany zgłaszaj w osobnym pull requeście. Na przykład poprawki błędów i aktualizacje dokumentacji powinny być zgłaszane w oddzielnych PR.
  - Poprawki literówek i drobne aktualizacje dokumentacji można łączyć w jednym PR, jeśli to stosowne.

- **Radzenie sobie z konfliktami scalania**: Jeśli w Twoim pull requeście pojawią się konflikty scalania, zaktualizuj lokalną gałąź `main`, aby odzwierciedlała główne repozytorium przed wprowadzeniem zmian.

- **Zgłoszenia tłumaczeń**: Przy zgłaszaniu PR z tłumaczeniem, upewnij się, że folder z tłumaczeniem zawiera tłumaczenia wszystkich plików z oryginalnego folderu.

### Translation Guidelines

> [!IMPORTANT]
>
> Podczas tłumaczenia tekstu w tym repozytorium nie używaj tłumaczeń maszynowych. Tłumaczenia wykonuj tylko, jeśli dobrze znasz dany język.

Jeśli znasz dobrze język inny niż angielski, możesz pomóc w tłumaczeniu treści. Postępuj zgodnie z poniższymi wskazówkami, aby zapewnić poprawną integrację Twoich tłumaczeń:

- **Utwórz folder tłumaczeń**: Przejdź do odpowiedniego folderu sekcji i utwórz folder z tłumaczeniem dla języka, na który tłumaczysz. Na przykład:
  - Dla sekcji wprowadzenia: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Dla sekcji szybkiego startu: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Kontynuuj ten wzór dla innych sekcji (03.Inference, 04.Finetuning itd.)

- **Aktualizuj ścieżki względne**: Podczas tłumaczenia dostosuj strukturę folderów, dodając `../../` na początku ścieżek względnych w plikach markdown, aby linki działały poprawnie. Na przykład zmień:
  - `(../../imgs/01/phi3aisafety.png)` na `(../../../../imgs/01/phi3aisafety.png)`

- **Organizuj tłumaczenia**: Każdy przetłumaczony plik powinien znajdować się w odpowiadającym folderze tłumaczeń danej sekcji. Na przykład, jeśli tłumaczysz sekcję wprowadzenia na hiszpański, stwórz folder jak poniżej:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Prześlij kompletny PR**: Upewnij się, że wszystkie przetłumaczone pliki dla danej sekcji znajdują się w jednym PR. Nie akceptujemy częściowych tłumaczeń sekcji. Przy zgłaszaniu PR z tłumaczeniem, upewnij się, że folder z tłumaczeniem zawiera tłumaczenia wszystkich plików z oryginalnego folderu.

### Writing Guidelines

Aby zapewnić spójność we wszystkich dokumentach, prosimy stosować się do poniższych wytycznych:

- **Formatowanie URL**: Zawijaj wszystkie adresy URL w nawiasy kwadratowe, a następnie w nawiasy okrągłe, bez dodatkowych spacji wokół lub wewnątrz nich. Na przykład: `[example](https://www.microsoft.com)`.

- **Linki względne**: Używaj `./` dla linków względnych wskazujących na pliki lub foldery w bieżącym katalogu oraz `../` dla tych w katalogu nadrzędnym. Na przykład: `[example](../../path/to/file)` lub `[example](../../../path/to/file)`.

- **Nie używaj lokalizacji specyficznych dla kraju**: Upewnij się, że Twoje linki nie zawierają lokalizacji specyficznych dla kraju. Na przykład unikaj `/en-us/` lub `/en/`.

- **Przechowywanie obrazów**: Przechowuj wszystkie obrazy w folderze `./imgs`.

- **Opisowe nazwy obrazów**: Nazwy obrazów powinny być opisowe, używając znaków angielskich, cyfr i myślników. Na przykład: `example-image.jpg`.

## GitHub Workflows

Po zgłoszeniu pull requesta, następujące workflow zostaną uruchomione, aby zweryfikować zmiany. Postępuj zgodnie z poniższymi instrukcjami, aby zapewnić pomyślne przejście kontroli workflow:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Ten workflow sprawdza, czy wszystkie ścieżki względne w Twoich plikach są poprawne.

1. Aby upewnić się, że Twoje linki działają prawidłowo, wykonaj następujące czynności w VS Code:
    - Najedź kursorem na dowolny link w plikach.
    - Naciśnij **Ctrl + Kliknięcie**, aby przejść do linku.
    - Jeśli klikniesz link i nie działa on lokalnie, workflow zostanie wywołany i nie zadziała na GitHub.

1. Aby naprawić ten problem, wykonaj następujące czynności, korzystając z sugestii ścieżek oferowanych przez VS Code:
    - Wpisz `./` lub `../`.
    - VS Code zaproponuje wybór spośród dostępnych opcji na podstawie wpisanego tekstu.
    - Podążaj za ścieżką, klikając wybrany plik lub folder, aby upewnić się, że ścieżka jest poprawna.

Po dodaniu poprawnej ścieżki względnej, zapisz i wypchnij zmiany.

### Check URLs Don't Have Locale

Ten workflow sprawdza, czy żaden adres URL nie zawiera lokalizacji specyficznej dla kraju. Ponieważ repozytorium jest dostępne globalnie, ważne jest, aby adresy URL nie zawierały lokalizacji Twojego kraju.

1. Aby zweryfikować, że Twoje adresy URL nie zawierają lokalizacji kraju, wykonaj następujące czynności:

    - Sprawdź, czy w adresach URL nie ma tekstu takiego jak `/en-us/`, `/en/` lub innej lokalizacji językowej.
    - Jeśli ich nie ma, przejdziesz ten test.

1. Aby naprawić ten problem, wykonaj następujące czynności:
    - Otwórz plik wskazany przez workflow.
    - Usuń lokalizację kraju z adresów URL.

Po usunięciu lokalizacji kraju, zapisz i wypchnij zmiany.

### Check Broken Urls

Ten workflow sprawdza, czy każdy adres URL w Twoich plikach działa i zwraca kod statusu 200.

1. Aby zweryfikować, że Twoje adresy URL działają poprawnie, wykonaj następujące czynności:
    - Sprawdź status adresów URL w Twoich plikach.

2. Aby naprawić uszkodzone adresy URL, wykonaj następujące czynności:
    - Otwórz plik zawierający uszkodzony adres URL.
    - Zaktualizuj adres URL na poprawny.

Po naprawieniu adresów URL, zapisz i wypchnij zmiany.

> [!NOTE]
>
> Mogą zdarzyć się sytuacje, w których sprawdzenie adresu URL zakończy się niepowodzeniem, mimo że link jest dostępny. Może to wynikać z kilku powodów, w tym:
>
> - **Ograniczenia sieciowe:** Serwery GitHub Actions mogą mieć ograniczenia sieciowe uniemożliwiające dostęp do niektórych adresów URL.
> - **Problemy z timeoutem:** Adresy URL, które odpowiadają zbyt długo, mogą wywołać błąd timeout w workflow.
> - **Tymczasowe problemy serwera:** Okazjonalne przerwy w działaniu lub konserwacja serwera mogą sprawić, że adres URL będzie tymczasowo niedostępny podczas walidacji.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym należy traktować jako źródło autorytatywne. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.