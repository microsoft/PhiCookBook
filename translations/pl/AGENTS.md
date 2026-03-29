# AGENTS.md

## Przegląd projektu

PhiCookBook to kompleksowe repozytorium książki kucharskiej zawierające praktyczne przykłady, samouczki i dokumentację do pracy z rodziną małych modeli językowych (SLM) Microsoft Phi. Repozytorium pokazuje różne zastosowania, w tym wnioskowanie, fine-tuning, kwantyzację, implementacje RAG oraz aplikacje multimodalne na różnych platformach i frameworkach.

**Kluczowe technologie:**
- **Języki:** Python, C#/.NET, JavaScript/Node.js
- **Frameworki:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformy:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Typy modeli:** Phi-3, Phi-3.5, Phi-4 (warianty tekstowe, wizualne, multimodalne, rozumowanie)

**Struktura repozytorium:**
- `/code/` - Działający kod i przykładowe implementacje
- `/md/` - Szczegółowa dokumentacja, samouczki i instrukcje  
- `/translations/` - Tłumaczenia na wiele języków (ponad 50 języków przez automatyczny workflow)
- `/.devcontainer/` - Konfiguracja kontenera developerskiego (Python 3.12 z Ollama)

## Konfiguracja środowiska deweloperskiego

### Korzystanie z GitHub Codespaces lub kontenerów deweloperskich (zalecane)

1. Otwórz w GitHub Codespaces (najszybsze):
   - Kliknij odznakę "Open in GitHub Codespaces" w README
   - Kontener automatycznie konfiguruje się z Python 3.12 i Ollama z Phi-3

2. Otwórz w VS Code Dev Containers:
   - Użyj odznaki "Open in Dev Containers" z README
   - Kontener wymaga minimum 16 GB pamięci hosta

### Konfiguracja lokalna

**Wymagania wstępne:**
- Python 3.12 lub nowszy
- .NET 8.0 SDK (do przykładów w C#)
- Node.js 18+ i npm (do przykładów w JavaScript)
- Zalecane minimum 16 GB RAM

**Instalacja:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Dla przykładów w Pythonie:**
Przejdź do konkretnych katalogów z przykładami i zainstaluj zależności:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # jeśli istnieje plik requirements.txt
```

**Dla przykładów w .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Dla przykładów w JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Uruchom serwer deweloperski
npm run build  # Zbuduj do produkcji
```

## Organizacja repozytorium

### Przykłady kodu (`/code/`)

- **01.Introduce/** - Podstawowe wprowadzenia i przykłady startowe
- **03.Finetuning/** oraz **04.Finetuning/** - Przykłady fine-tuningu różnymi metodami
- **03.Inference/** - Przykłady wnioskowania na różnych platformach (AIPC, MLX)
- **06.E2E/** - Przykłady aplikacji end-to-end
- **07.Lab/** - Laboratorium/implementacje eksperymentalne
- **08.RAG/** - Przykłady Retrieval-Augmented Generation
- **09.UpdateSamples/** - Najnowsze zaktualizowane próbki

### Dokumentacja (`/md/`)

- **01.Introduction/** - Wprowadzenia, konfiguracja środowiska, przewodniki po platformach
- **02.Application/** - Przykłady aplikacji uporządkowane wg typów (Tekst, Kod, Wizja, Audio itd.)
- **02.QuickStart/** - Szybkie przewodniki dla Microsoft Foundry i GitHub Models
- **03.FineTuning/** - Dokumentacja i tutoriale dotyczące fine-tuningu
- **04.HOL/** - Pracownie praktyczne (zawiera przykłady .NET)

### Format plików

- **Notatniki Jupyter (`.ipynb`)** - Interaktywne tutoriale w Pythonie oznaczone 📓 w README
- **Skrypty Python (`.py`)** - Samodzielne przykłady w Pythonie
- **Projekty C# (`.csproj`, `.sln`)** - Aplikacje i przykłady .NET
- **JavaScript (`.js`, `package.json`)** - Przykłady webowe i Node.js
- **Markdown (`.md`)** - Dokumentacja i przewodniki

## Praca z przykładami

### Uruchamianie notatników Jupyter

Większość przykładów dostępna jest jako notatniki Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Otwiera interfejs przeglądarki
# Przejdź do żądanego pliku .ipynb
```

### Uruchamianie skryptów Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Uruchamianie przykładów .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Lub zbuduj całe rozwiązanie:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Uruchamianie przykładów JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Programowanie z gorącym przeładowaniem
```

## Testowanie

Repozytorium zawiera przykładowy kod i tutoriale, a nie tradycyjny projekt z testami jednostkowymi. Walidacja odbywa się zwykle poprzez:

1. **Uruchomienie przykładów** - Każdy przykład powinien działać bez błędów
2. **Weryfikację wyników** - Sprawdzenie, czy odpowiedzi modelu są stosowne
3. **Przeprowadzenie tutoriali** - Przewodniki krok po kroku powinny działać zgodnie z dokumentacją

**Typowe podejście do walidacji:**
- Testuj wykonywanie przykładów w docelowym środowisku
- Sprawdź poprawność instalacji zależności
- Upewnij się, że modele są poprawnie pobierane i ładowane
- Potwierdź, że zachowanie modelu jest zgodne z dokumentacją

## Styl kodu i konwencje

### Ogólne wskazówki

- Przykłady powinny być jasne, dobrze komentowane i edukacyjne
- Stosuj się do konwencji specyficznych dla języka (PEP 8 dla Pythona, standardy C# dla .NET)
- Przykłady skupiaj na demonstrowaniu specyficznych możliwości modeli Phi
- Dodawaj komentarze wyjaśniające kluczowe koncepcje i parametry modelu

### Standardy dokumentacji

**Formatowanie URL:**
- Używaj formatu `[text](../../url)` bez dodatkowych spacji
- Linki względne: używaj `./` dla bieżącego katalogu, `../` dla katalogu nadrzędnego
- Unikaj specyficznych lokalizacji krajowych w URL (np. `/en-us/`, `/en/`)

**Obrazy:**
- Przechowuj wszystkie obrazy w katalogu `/imgs/`
- Używaj opisowych nazw zawierających znaki angielskie, cyfry i myślniki
- Przykład: `phi-3-architecture.png`

**Pliki Markdown:**
- Odnoś się do faktycznych działających przykładów w katalogu `/code/`
- Synchronizuj dokumentację z aktualizacjami kodu
- Używaj emoji 📓 do oznaczania linków do notatników Jupyter w README

### Organizacja plików

- Przykłady kodu w `/code/` uporządkowane tematycznie lub według funkcji
- Dokumentacja w `/md/` odzwierciedla strukturę kodu, gdy jest to stosowne
- Przechowuj powiązane pliki (notatniki, skrypty, konfiguracje) razem w podkatalogach

## Wytyczne dotyczące pull requestów

### Przed wysłaniem

1. **Sforkuj repozytorium** do swojego konta
2. **Oddziel PR według typu:**
   - Poprawki błędów w jednym PR
   - Aktualizacje dokumentacji w innym
   - Nowe przykłady osobno
   - Poprawki literówek można łączyć

3. **Radzenie sobie z konfliktami:**
   - Zaktualizuj lokalną gałąź `main` przed zmianami
   - Często synchronizuj się z upstream

4. **PR z tłumaczeniami:**
   - Muszą zawierać tłumaczenia WSZYSTKICH plików w folderze
   - Zachowaj spójną strukturę z oryginałem

### Wymagane kontrole

PR automatycznie uruchamia workflow GitHub do walidacji:

1. **Weryfikacja ścieżek względnych** - Wszystkie linki wewnętrzne muszą działać
   - Testuj linki lokalnie: Ctrl+Kliknięcie w VS Code
   - Korzystaj z sugestii ścieżek w VS Code (`./` lub `../`)

2. **Sprawdzenie lokalizacji URL** - Adresy URL nie mogą zawierać lokalizacji krajowych
   - Usuń `/en-us/`, `/en/` lub inne kody językowe
   - Używaj ogólnych, międzynarodowych URL

3. **Sprawdzenie niedziałających URL** - Wszystkie URL muszą zwracać status 200
   - Sprawdź dostępność linków przed wysłaniem
   - Uwaga: niektóre błędy mogą wynikać z ograniczeń sieci

### Format tytułu PR

```
[component] Brief description
```

Przykłady:
- `[docs] Dodaj tutorial wnioskowania Phi-4`
- `[code] Napraw przykład integracji ONNX Runtime`
- `[translation] Dodaj tłumaczenie na japoński przewodników wprowadzeniowych`

## Typowe wzorce rozwoju

### Praca z modelami Phi

**Ładowanie modeli:**
- Przykłady używają różnych frameworków: Transformers, ONNX Runtime, MLX, OpenVINO
- Modele zwykle pobierane z Hugging Face, Azure lub GitHub Models
- Sprawdź kompatybilność modelu z Twoim sprzętem (CPU, GPU, NPU)

**Wzorce wnioskowania:**
- Generowanie tekstu: większość przykładów używa wariantów chat/instruct
- Wizja: Phi-3-vision i Phi-4-multimodal do rozumienia obrazów
- Audio: Phi-4-multimodal obsługuje wejścia audio
- Rozumowanie: warianty Phi-4-reasoning do zaawansowanych zadań rozumowania

### Informacje specyficzne dla platform

**Microsoft Foundry:**
- Wymaga subskrypcji Azure i kluczy API
- Zobacz `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Dostępna darmowa warstwa do testów
- Zobacz `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokalne wnioskowanie:**
- ONNX Runtime: wieloplatformowy, zoptymalizowany wątek
- Ollama: łatwe lokalne zarządzanie modelami (pre-konfigurowane w kontenerze developerskim)
- Apple MLX: zoptymalizowany dla Apple Silicon

## Rozwiązywanie problemów

### Typowe problemy

**Problemy z pamięcią:**
- Modele Phi wymagają dużo RAM (zwłaszcza warianty wizji/multimodalne)
- Używaj kwantyzowanych modeli w środowiskach o ograniczonych zasobach
- Zobacz `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikty zależności:**
- Przykłady Pythona mogą mieć specyficzne wymagania wersji pakietów
- Używaj środowisk wirtualnych dla każdego przykładu
- Sprawdź osobne pliki `requirements.txt`

**Problemy z pobieraniem modeli:**
- Duże modele mogą się timeoutować na wolnych łączach
- Rozważ użycie środowisk chmurowych (Codespaces, Azure)
- Sprawdź cache Hugging Face: `~/.cache/huggingface/`

**Problemy z projektami .NET:**
- Upewnij się, że SDK .NET 8.0 jest zainstalowane
- Użyj `dotnet restore` przed budowaniem
- Niektóre projekty mają konfiguracje specyficzne dla CUDA (Debug_Cuda)

**Przykłady JavaScript/Web:**
- Używaj Node.js 18+ dla kompatybilności
- Wyczyść `node_modules` i zainstaluj ponownie w razie problemów
- Sprawdź konsolę przeglądarki pod kątem problemów z WebGPU

### Uzyskiwanie pomocy

- **Discord:** Dołącz do społeczności Microsoft Foundry na Discordzie
- **GitHub Issues:** Zgłaszaj błędy i problemy w repozytorium
- **GitHub Discussions:** Zadawaj pytania i dziel się wiedzą

## Dodatkowy kontekst

### Odpowiedzialna AI

Całe korzystanie z modeli Phi powinno przestrzegać zasad Odpowiedzialnej AI Microsoft:
- Sprawiedliwość, niezawodność, bezpieczeństwo
- Prywatność i bezpieczeństwo  
- Włączanie, przejrzystość, odpowiedzialność
- Używaj Azure AI Content Safety w aplikacjach produkcyjnych
- Zobacz `/md/01.Introduction/01/01.AISafety.md`

### Tłumaczenia

- Ponad 50 języków wspieranych przez automatyczny GitHub Action
- Tłumaczenia znajdują się w katalogu `/translations/`
- Utrzymywane przez workflow co-op-translator
- Nie edytuj ręcznie tłumaczonych plików (generowane automatycznie)

### Wkład w projekt

- Przestrzegaj wytycznych w `CONTRIBUTING.md`
- Zaakceptuj Contributor License Agreement (CLA)
- Przestrzegaj Microsoft Open Source Code of Conduct
- Nie umieszczaj informacji poufnych i danych uwierzytelniających w commitach

### Wsparcie wielojęzyczne

To repozytorium poliglotyczne z przykładami w:
- **Python** - workflow ML/AI, notatniki Jupyter, fine-tuning
- **C#/.NET** - aplikacje korporacyjne, integracja ONNX Runtime
- **JavaScript** - AI webowa, inference w przeglądarce z WebGPU

Wybierz język najlepiej dopasowany do Twojego przypadku użycia i docelowego środowiska.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dokładamy starań, aby zapewnić poprawność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikłe z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->