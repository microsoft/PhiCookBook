<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "006e8cf75211d3297f24e1b22e38955f",
  "translation_date": "2025-07-17T02:18:15+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md",
  "language_code": "pl"
}
-->
# Interaktywny Phi 3 Mini 4K Instruct Chatbot z Whisper

## Przegląd

Interaktywny Phi 3 Mini 4K Instruct Chatbot to narzędzie, które pozwala użytkownikom na interakcję z demonstracją Microsoft Phi 3 Mini 4K instruct za pomocą tekstu lub dźwięku. Chatbot może być wykorzystywany do różnych zadań, takich jak tłumaczenia, prognozy pogody czy ogólne zbieranie informacji.

### Pierwsze kroki

Aby skorzystać z tego chatbota, wykonaj następujące kroki:

1. Otwórz nowy [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. W głównym oknie notatnika zobaczysz interfejs czatu z polem do wpisywania tekstu oraz przyciskiem „Send”.
3. Aby korzystać z chatbota tekstowego, wpisz swoją wiadomość w pole tekstowe i kliknij „Send”. Chatbot odpowie plikiem audio, który można odtworzyć bezpośrednio w notatniku.

**Note**: To narzędzie wymaga GPU oraz dostępu do modeli Microsoft Phi-3 i OpenAI Whisper, które są wykorzystywane do rozpoznawania mowy i tłumaczenia.

### Wymagania dotyczące GPU

Aby uruchomić tę demonstrację, potrzebujesz 12 GB pamięci GPU.

Wymagania pamięciowe do uruchomienia demonstracji **Microsoft-Phi-3-Mini-4K instruct** na GPU zależą od kilku czynników, takich jak rozmiar danych wejściowych (audio lub tekst), język tłumaczenia, szybkość modelu oraz dostępna pamięć GPU.

Model Whisper jest zaprojektowany do działania na GPU. Zalecana minimalna ilość pamięci GPU do uruchomienia modelu Whisper to 8 GB, ale model może obsłużyć większą ilość pamięci, jeśli jest to potrzebne.

Warto pamiętać, że przetwarzanie dużej ilości danych lub wysoki wolumen zapytań może wymagać więcej pamięci GPU i/lub może powodować problemy z wydajnością. Zaleca się testowanie swojego przypadku użycia z różnymi konfiguracjami oraz monitorowanie zużycia pamięci, aby określić optymalne ustawienia dla konkretnych potrzeb.

## Przykład E2E dla Interaktywnego Phi 3 Mini 4K Instruct Chatbot z Whisper

Notatnik Jupyter zatytułowany [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) pokazuje, jak używać demonstracji Microsoft Phi 3 Mini 4K instruct do generowania tekstu z dźwięku lub tekstu pisanego. Notatnik definiuje kilka funkcji:

1. `tts_file_name(text)`: Funkcja generuje nazwę pliku na podstawie tekstu wejściowego do zapisu wygenerowanego pliku audio.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Funkcja korzysta z API Edge TTS do wygenerowania pliku audio z listy fragmentów tekstu. Parametry wejściowe to lista fragmentów, szybkość mowy, nazwa głosu oraz ścieżka do zapisu wygenerowanego pliku audio.
1. `talk(input_text)`: Funkcja generuje plik audio, korzystając z API Edge TTS i zapisuje go pod losową nazwą w katalogu /content/audio. Parametrem wejściowym jest tekst do konwersji na mowę.
1. `run_text_prompt(message, chat_history)`: Funkcja wykorzystuje demonstrację Microsoft Phi 3 Mini 4K instruct do wygenerowania pliku audio na podstawie wiadomości i dodaje go do historii czatu.
1. `run_audio_prompt(audio, chat_history)`: Funkcja konwertuje plik audio na tekst za pomocą API modelu Whisper i przekazuje go do funkcji `run_text_prompt()`.
1. Kod uruchamia aplikację Gradio, która pozwala użytkownikom na interakcję z demonstracją Phi 3 Mini 4K instruct poprzez wpisywanie wiadomości lub przesyłanie plików audio. Wynik jest wyświetlany jako wiadomość tekstowa w aplikacji.

## Rozwiązywanie problemów

Instalacja sterowników Cuda GPU

1. Upewnij się, że Twoja aplikacja Linux jest aktualna

    ```bash
    sudo apt update
    ```

1. Zainstaluj sterowniki Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Zarejestruj lokalizację sterownika cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Sprawdzenie rozmiaru pamięci Nvidia GPU (wymagane 12 GB pamięci GPU)

    ```bash
    nvidia-smi
    ```

1. Opróżnienie pamięci podręcznej: Jeśli używasz PyTorch, możesz wywołać torch.cuda.empty_cache(), aby zwolnić całą nieużywaną pamięć podręczną, tak aby mogła być wykorzystana przez inne aplikacje GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Sprawdzenie Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Wykonaj następujące kroki, aby utworzyć token Hugging Face.

    - Przejdź do [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Wybierz **New token**.
    - Wprowadź nazwę projektu, której chcesz użyć.
    - Wybierz **Type** na **Write**.

> **Note**
>
> Jeśli pojawi się następujący błąd:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Aby to rozwiązać, wpisz następujące polecenie w terminalu.
>
> ```bash
> sudo ldconfig
> ```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.