# Interaktywny Phi 3 Mini 4K Instruct Chatbot z Whisper

## Przegląd

Interaktywny Phi 3 Mini 4K Instruct Chatbot to narzędzie pozwalające użytkownikom na interakcję z demonstracją Microsoft Phi 3 Mini 4K instruct za pomocą tekstu lub dźwięku. Chatbot może być używany do różnych zadań, takich jak tłumaczenia, prognoza pogody oraz ogólne pozyskiwanie informacji.

### Pierwsze kroki

Aby korzystać z tego chatbota, wystarczy postępować zgodnie z poniższymi instrukcjami:

1. Otwórz nowy [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. W głównym oknie notatnika zobaczysz interfejs czatu z polem tekstowym oraz przyciskiem "Send".
3. Aby korzystać z chatbota opartego na tekście, po prostu wpisz wiadomość w polu tekstowym i kliknij przycisk "Send". Chatbot odpowie plikiem audio, który można odtworzyć bezpośrednio w notatniku.

**Uwaga**: To narzędzie wymaga GPU oraz dostępu do modeli Microsoft Phi-3 i OpenAI Whisper, które są wykorzystywane do rozpoznawania mowy i tłumaczenia.

### Wymagania dotyczące GPU

Aby uruchomić tę demonstrację, potrzebujesz 12 GB pamięci GPU.

Wymagania dotyczące pamięci do uruchomienia demonstracji **Microsoft-Phi-3-Mini-4K instruct** na GPU zależą od kilku czynników, takich jak rozmiar danych wejściowych (audio lub tekst), język używany do tłumaczenia, szybkość modelu oraz dostępna pamięć na GPU.

Generalnie, model Whisper jest zaprojektowany do pracy na GPU. Zalecana minimalna ilość pamięci GPU do uruchomienia modelu Whisper to 8 GB, ale może on obsługiwać większe ilości pamięci, jeśli to konieczne.

Ważne jest, aby zauważyć, że przetwarzanie dużych ilości danych lub wysoki wolumen zapytań do modelu może wymagać większej pamięci GPU i/lub powodować problemy z wydajnością. Zaleca się testowanie swojego przypadku użycia z różnymi konfiguracjami oraz monitorowanie wykorzystania pamięci, aby określić optymalne ustawienia dla konkretnego zastosowania.

## Przykład E2E dla Interaktywnego Phi 3 Mini 4K Instruct Chatbot z Whisper

Notatnik Jupyter zatytułowany [Interaktywny Phi 3 Mini 4K Instruct Chatbot z Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstruje, jak używać demonstracji Microsoft Phi 3 Mini 4K instruct do generowania tekstu z dźwięku lub pisanego tekstu. Notatnik definiuje kilka funkcji:

1. `tts_file_name(text)`: Ta funkcja generuje nazwę pliku na podstawie wprowadzonego tekstu do zapisu wygenerowanego pliku audio.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ta funkcja korzysta z API Edge TTS, aby wygenerować plik audio z listy fragmentów tekstu wejściowego. Parametry wejściowe to lista fragmentów, prędkość mowy, nazwa głosu oraz ścieżka wyjściowa do zapisania wygenerowanego pliku audio.
1. `talk(input_text)`: Ta funkcja generuje plik audio za pomocą API Edge TTS i zapisuje go pod losową nazwą pliku w katalogu /content/audio. Parametr wejściowy to tekst wejściowy, który ma zostać przekształcony na mowę.
1. `run_text_prompt(message, chat_history)`: Ta funkcja korzysta z demonstracji Microsoft Phi 3 Mini 4K instruct, aby wygenerować plik audio na podstawie wprowadzonej wiadomości i dopisuje go do historii czatu.
1. `run_audio_prompt(audio, chat_history)`: Ta funkcja konwertuje plik audio na tekst za pomocą API modelu Whisper i przekazuje go do funkcji `run_text_prompt()`.
1. Kod uruchamia aplikację Gradio, która pozwala użytkownikom wchodzić w interakcję z demonstracją Phi 3 Mini 4K instruct, wpisując wiadomości lub przesyłając pliki audio. Wynik jest wyświetlany jako wiadomość tekstowa w aplikacji.

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

1. Sprawdzenie rozmiaru pamięci GPU Nvidia (wymagane 12 GB pamięci GPU)

    ```bash
    nvidia-smi
    ```

1. Opróżnij pamięć podręczną: Jeśli używasz PyTorch, możesz wywołać torch.cuda.empty_cache(), aby zwolnić całą nieużywaną pamięć podręczną, aby mogły korzystać z niej inne aplikacje GPU

    ```python
    torch.cuda.empty_cache() 
    ```

1. Sprawdzenie Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Wykonaj następujące czynności, aby utworzyć token Hugging Face.

    - Przejdź do [Strony Ustawień Tokenów Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Wybierz **New token**.
    - Wprowadź nazwę projektu, której chcesz użyć.
    - Wybierz **Type** na **Write**.

> [!NOTE]
>
> Jeśli napotkasz następujący błąd:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Aby rozwiązać ten problem, wpisz następujące polecenie w terminalu.
>
> ```bash
> sudo ldconfig
> ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i nadrzędne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za ewentualne nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->