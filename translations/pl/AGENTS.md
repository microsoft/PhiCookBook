<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:54:21+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pl"
}
-->
# AGENTS.md

## Przegląd projektu

PhiCookBook to kompleksowe repozytorium przepisów zawierające praktyczne przykłady, samouczki i dokumentację dotyczącą pracy z rodziną małych modeli językowych (SLM) Microsoftu Phi. Repozytorium prezentuje różne przypadki użycia, w tym wnioskowanie, dostrajanie, kwantyzację, implementacje RAG oraz aplikacje multimodalne na różnych platformach i w różnych ramach.

**Kluczowe technologie:**
- **Języki:** Python, C#/.NET, JavaScript/Node.js
- **Frameworki:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platformy:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Typy modeli:** Phi-3, Phi-3.5, Phi-4 (tekst, wizja, multimodalność, warianty rozumowania)

**Struktura repozytorium:**
- `/code/` - Przykłady kodu i implementacje
- `/md/` - Szczegółowa dokumentacja, samouczki i przewodniki  
- `/translations/` - Tłumaczenia na wiele języków (ponad 50 języków dzięki zautomatyzowanemu przepływowi pracy)
- `/.devcontainer/` - Konfiguracja kontenera deweloperskiego (Python 3.12 z Ollama)

## Konfiguracja środowiska deweloperskiego

### Korzystanie z GitHub Codespaces lub kontenerów deweloperskich (zalecane)

1. Otwórz w GitHub Codespaces (najszybsze):
   - Kliknij odznakę "Open in GitHub Codespaces" w README
   - Kontener automatycznie skonfiguruje się z Pythonem 3.12 i Ollama z Phi-3

2. Otwórz w kontenerach deweloperskich VS Code:
   - Użyj odznaki "Open in Dev Containers" z README
   - Kontener wymaga minimum 16GB pamięci RAM hosta

### Konfiguracja lokalna

**Wymagania wstępne:**
- Python 3.12 lub nowszy
- .NET 8.0 SDK (dla przykładów w C#)
- Node.js 18+ i npm (dla przykładów w JavaScript)
- Zalecane minimum 16GB RAM

**Instalacja:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Dla przykładów w Pythonie:**
Przejdź do odpowiednich katalogów z przykładami i zainstaluj zależności:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
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
npm run dev  # Start development server
npm run build  # Build for production
```

## Organizacja repozytorium

### Przykłady kodu (`/code/`)

- **01.Introduce/** - Podstawowe wprowadzenia i przykłady na start
- **03.Finetuning/** i **04.Finetuning/** - Przykłady dostrajania różnymi metodami
- **03.Inference/** - Przykłady wnioskowania na różnych sprzętach (AIPC, MLX)
- **06.E2E/** - Przykłady aplikacji end-to-end
- **07.Lab/** - Implementacje laboratoryjne/eksperymentalne
- **08.RAG/** - Przykłady generacji wspomaganej wyszukiwaniem
- **09.UpdateSamples/** - Najnowsze zaktualizowane przykłady

### Dokumentacja (`/md/`)

- **01.Introduction/** - Przewodniki wprowadzające, konfiguracja środowiska, przewodniki po platformach
- **02.Application/** - Przykłady aplikacji zorganizowane według typu (Tekst, Kod, Wizja, Audio, itd.)
- **02.QuickStart/** - Przewodniki szybkiego startu dla Azure AI Foundry i GitHub Models
- **03.FineTuning/** - Dokumentacja i samouczki dotyczące dostrajania
- **04.HOL/** - Laboratoria praktyczne (zawiera przykłady .NET)

### Format plików

- **Notatniki Jupyter (`.ipynb`)** - Interaktywne samouczki w Pythonie oznaczone 📓 w README
- **Skrypty Python (`.py`)** - Samodzielne przykłady w Pythonie
- **Projekty C# (`.csproj`, `.sln`)** - Aplikacje i przykłady w .NET
- **JavaScript (`.js`, `package.json`)** - Przykłady oparte na sieci i Node.js
- **Markdown (`.md`)** - Dokumentacja i przewodniki

## Praca z przykładami

### Uruchamianie notatników Jupyter

Większość przykładów jest dostarczana jako notatniki Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
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
npm run dev  # Development with hot reload
```

## Testowanie

To repozytorium zawiera kod przykładowy i samouczki, a nie tradycyjny projekt oprogramowania z testami jednostkowymi. Walidacja jest zazwyczaj przeprowadzana poprzez:

1. **Uruchamianie przykładów** - Każdy przykład powinien działać bez błędów
2. **Weryfikację wyników** - Sprawdź, czy odpowiedzi modelu są odpowiednie
3. **Przestrzeganie samouczków** - Przewodniki krok po kroku powinny działać zgodnie z dokumentacją

**Typowe podejście do walidacji:**
- Testowanie wykonania przykładów w docelowym środowisku
- Weryfikacja poprawności instalacji zależności
- Sprawdzenie, czy modele są pobierane/ładowane poprawnie
- Potwierdzenie, że oczekiwane zachowanie odpowiada dokumentacji

## Styl kodu i konwencje

### Ogólne wytyczne

- Przykłady powinny być jasne, dobrze skomentowane i edukacyjne
- Przestrzegaj konwencji specyficznych dla języka (PEP 8 dla Pythona, standardy C# dla .NET)
- Skup się na demonstrowaniu konkretnych możliwości modeli Phi
- Dodawaj komentarze wyjaśniające kluczowe koncepcje i parametry specyficzne dla modelu

### Standardy dokumentacji

**Formatowanie URL:**
- Używaj formatu `[tekst](../../url)` bez dodatkowych spacji
- Linki względne: Używaj `./` dla bieżącego katalogu, `../` dla nadrzędnego
- Nie używaj lokalizacji specyficznych dla kraju w URL (unikaj `/en-us/`, `/en/`)

**Obrazy:**
- Przechowuj wszystkie obrazy w katalogu `/imgs/`
- Używaj opisowych nazw z angielskimi znakami, cyframi i myślnikami
- Przykład: `phi-3-architecture.png`

**Pliki Markdown:**
- Odnoś się do rzeczywistych przykładów w katalogu `/code/`
- Synchronizuj dokumentację ze zmianami w kodzie
- Używaj emoji 📓 do oznaczania linków do notatników Jupyter w README

### Organizacja plików

- Przykłady kodu w `/code/` zorganizowane według tematu/funkcji
- Dokumentacja w `/md/` odzwierciedla strukturę kodu, gdy to możliwe
- Przechowuj powiązane pliki (notatniki, skrypty, konfiguracje) razem w podkatalogach

## Wytyczne dotyczące Pull Requestów

### Przed przesłaniem

1. **Sforkuj repozytorium** na swoje konto
2. **Oddziel PR-y według typu:**
   - Poprawki błędów w jednym PR
   - Aktualizacje dokumentacji w innym
   - Nowe przykłady w oddzielnych PR
   - Poprawki literówek można łączyć

3. **Rozwiąż konflikty scalania:**
   - Zaktualizuj lokalną gałąź `main` przed wprowadzeniem zmian
   - Często synchronizuj z upstream

4. **PR-y tłumaczeniowe:**
   - Muszą zawierać tłumaczenia WSZYSTKICH plików w folderze
   - Zachowaj spójną strukturę z oryginalnym językiem

### Wymagane kontrole

PR-y automatycznie uruchamiają przepływy pracy GitHub w celu walidacji:

1. **Walidacja ścieżek względnych** - Wszystkie wewnętrzne linki muszą działać
   - Testuj linki lokalnie: Ctrl+Klik w VS Code
   - Używaj sugestii ścieżek z VS Code (`./` lub `../`)

2. **Sprawdzenie lokalizacji URL** - URL-e internetowe nie mogą zawierać kodów językowych
   - Usuń `/en-us/`, `/en/` lub inne kody językowe
   - Używaj ogólnych międzynarodowych URL-i

3. **Sprawdzenie uszkodzonych URL-i** - Wszystkie URL-e muszą zwracać status 200
   - Zweryfikuj dostępność linków przed przesłaniem
   - Uwaga: Niektóre błędy mogą wynikać z ograniczeń sieciowych

### Format tytułu PR

```
[component] Brief description
```

Przykłady:
- `[docs] Dodaj samouczek wnioskowania Phi-4`
- `[code] Popraw przykład integracji ONNX Runtime`
- `[translation] Dodaj tłumaczenie na japoński dla przewodników wprowadzających`

## Typowe wzorce rozwoju

### Praca z modelami Phi

**Ładowanie modelu:**
- Przykłady wykorzystują różne frameworki: Transformers, ONNX Runtime, MLX, OpenVINO
- Modele są zazwyczaj pobierane z Hugging Face, Azure lub GitHub Models
- Sprawdź kompatybilność modelu z Twoim sprzętem (CPU, GPU, NPU)

**Wzorce wnioskowania:**
- Generowanie tekstu: Większość przykładów wykorzystuje warianty chat/instruct
- Wizja: Phi-3-vision i Phi-4-multimodal do analizy obrazów
- Audio: Phi-4-multimodal obsługuje dane wejściowe audio
- Rozumowanie: Warianty Phi-4-reasoning do zaawansowanych zadań rozumowania

### Uwagi specyficzne dla platformy

**Azure AI Foundry:**
- Wymaga subskrypcji Azure i kluczy API
- Zobacz `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Dostępny darmowy poziom do testowania
- Zobacz `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Wnioskowanie lokalne:**
- ONNX Runtime: Wieloplatformowe, zoptymalizowane wnioskowanie
- Ollama: Łatwe zarządzanie modelami lokalnymi (wstępnie skonfigurowane w kontenerze deweloperskim)
- Apple MLX: Zoptymalizowane dla Apple Silicon

## Rozwiązywanie problemów

### Typowe problemy

**Problemy z pamięcią:**
- Modele Phi wymagają dużej ilości RAM (szczególnie warianty wizji/multimodalne)
- Używaj modeli kwantyzowanych w środowiskach o ograniczonych zasobach
- Zobacz `/md/01.Introduction/04/QuantifyingPhi.md`

**Konflikty zależności:**
- Przykłady w Pythonie mogą mieć specyficzne wymagania wersji
- Używaj wirtualnych środowisk dla każdego przykładu
- Sprawdź indywidualne pliki `requirements.txt`

**Problemy z pobieraniem modelu:**
- Duże modele mogą się nie pobrać przy wolnym połączeniu
- Rozważ użycie środowisk chmurowych (Codespaces, Azure)
- Sprawdź pamięć podręczną Hugging Face: `~/.cache/huggingface/`

**Problemy z projektami .NET:**
- Upewnij się, że zainstalowano .NET 8.0 SDK
- Użyj `dotnet restore` przed budowaniem
- Niektóre projekty mają specyficzne konfiguracje CUDA (Debug_Cuda)

**Przykłady JavaScript/Web:**
- Używaj Node.js 18+ dla kompatybilności
- Wyczyść `node_modules` i ponownie zainstaluj, jeśli wystąpią problemy
- Sprawdź konsolę przeglądarki pod kątem problemów z kompatybilnością WebGPU

### Uzyskiwanie pomocy

- **Discord:** Dołącz do społeczności Azure AI Foundry na Discordzie
- **GitHub Issues:** Zgłaszaj błędy i problemy w repozytorium
- **GitHub Discussions:** Zadawaj pytania i dziel się wiedzą

## Dodatkowy kontekst

### Odpowiedzialna AI

Wszystkie zastosowania modeli Phi powinny być zgodne z zasadami odpowiedzialnej AI Microsoftu:
- Sprawiedliwość, niezawodność, bezpieczeństwo
- Prywatność i bezpieczeństwo  
- Włączanie, przejrzystość, odpowiedzialność
- Używaj Azure AI Content Safety w aplikacjach produkcyjnych
- Zobacz `/md/01.Introduction/01/01.AISafety.md`

### Tłumaczenia

- Obsługa ponad 50 języków dzięki zautomatyzowanemu działaniu GitHub Action
- Tłumaczenia w katalogu `/translations/`
- Utrzymywane przez przepływ pracy co-op-translator
- Nie edytuj ręcznie tłumaczonych plików (automatycznie generowane)

### Wkład

- Przestrzegaj wytycznych w `CONTRIBUTING.md`
- Zgódź się na Umowę Licencyjną Współtwórcy (CLA)
- Przestrzegaj Kodeksu Postępowania Microsoft Open Source
- Nie umieszczaj w commitach danych uwierzytelniających ani informacji o bezpieczeństwie

### Obsługa wielu języków

To repozytorium wielojęzyczne z przykładami w:
- **Python** - Przepływy pracy ML/AI, notatniki Jupyter, dostrajanie
- **C#/.NET** - Aplikacje korporacyjne, integracja ONNX Runtime
- **JavaScript** - AI oparte na sieci, wnioskowanie w przeglądarce z WebGPU

Wybierz język, który najlepiej pasuje do Twojego przypadku użycia i celu wdrożenia.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.