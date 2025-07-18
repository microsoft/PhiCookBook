<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:09:32+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "pl"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo prezentujące WebGPU i wzorzec RAG

Wzorzec RAG z modelem Phi-3.5 Onnx Hosted wykorzystuje podejście Retrieval-Augmented Generation, łącząc moc modeli Phi-3.5 z hostingiem ONNX dla efektywnych wdrożeń AI. Ten wzorzec jest kluczowy przy dostrajaniu modeli do zadań specyficznych dla danej dziedziny, oferując połączenie jakości, opłacalności i rozumienia długich kontekstów. Jest częścią pakietu Azure AI, zapewniając szeroki wybór modeli, które łatwo znaleźć, wypróbować i używać, odpowiadając na potrzeby personalizacji w różnych branżach.

## Czym jest WebGPU  
WebGPU to nowoczesne API graficzne dla przeglądarek internetowych, zaprojektowane, aby zapewnić efektywny dostęp do procesora graficznego (GPU) urządzenia bezpośrednio z poziomu przeglądarki. Ma zastąpić WebGL, oferując kilka kluczowych usprawnień:

1. **Kompatybilność z nowoczesnymi GPU**: WebGPU działa płynnie z współczesnymi architekturami GPU, wykorzystując systemowe API takie jak Vulkan, Metal i Direct3D 12.
2. **Zwiększona wydajność**: Obsługuje obliczenia ogólnego przeznaczenia na GPU oraz szybsze operacje, co czyni go odpowiednim zarówno do renderowania grafiki, jak i zadań związanych z uczeniem maszynowym.
3. **Zaawansowane funkcje**: WebGPU udostępnia bardziej zaawansowane możliwości GPU, umożliwiając realizację bardziej złożonych i dynamicznych zadań graficznych oraz obliczeniowych.
4. **Zmniejszenie obciążenia JavaScript**: Przenosząc więcej zadań na GPU, WebGPU znacząco zmniejsza obciążenie JavaScript, co przekłada się na lepszą wydajność i płynniejsze działanie.

WebGPU jest obecnie wspierany w przeglądarkach takich jak Google Chrome, a prace nad rozszerzeniem wsparcia na inne platformy są w toku.

### 03.WebGPU  
Wymagane środowisko:

**Obsługiwane przeglądarki:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Włączanie WebGPU:

- W Chrome/Microsoft Edge  

Włącz flagę `chrome://flags/#enable-unsafe-webgpu`.

#### Otwórz przeglądarkę:  
Uruchom Google Chrome lub Microsoft Edge.

#### Wejdź na stronę z flagami:  
W pasku adresu wpisz `chrome://flags` i naciśnij Enter.

#### Wyszukaj flagę:  
W polu wyszukiwania u góry strony wpisz 'enable-unsafe-webgpu'

#### Włącz flagę:  
Znajdź flagę #enable-unsafe-webgpu na liście wyników.

Kliknij menu rozwijane obok niej i wybierz Enabled.

#### Uruchom ponownie przeglądarkę:  

Po włączeniu flagi musisz zrestartować przeglądarkę, aby zmiany zaczęły działać. Kliknij przycisk Relaunch, który pojawi się na dole strony.

- Na Linuxie uruchom przeglądarkę z parametrem `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ma WebGPU włączone domyślnie.  
- W Firefox Nightly wpisz about:config w pasku adresu i ustaw `dom.webgpu.enabled` na true.

### Konfiguracja GPU dla Microsoft Edge  

Oto kroki, aby skonfigurować wysokowydajny GPU dla Microsoft Edge na Windows:

- **Otwórz Ustawienia:** Kliknij menu Start i wybierz Ustawienia.  
- **Ustawienia systemowe:** Przejdź do System, a następnie Ekran.  
- **Ustawienia grafiki:** Przewiń w dół i kliknij Ustawienia grafiki.  
- **Wybierz aplikację:** W sekcji „Wybierz aplikację do ustawienia preferencji” wybierz Aplikacja pulpitu, a następnie Przeglądaj.  
- **Wybierz Edge:** Przejdź do folderu instalacyjnego Edge (zazwyczaj `C:\Program Files (x86)\Microsoft\Edge\Application`) i wybierz `msedge.exe`.  
- **Ustaw preferencję:** Kliknij Opcje, wybierz Wysoka wydajność, a następnie kliknij Zapisz.  
To zapewni, że Microsoft Edge będzie korzystać z Twojego wysokowydajnego GPU dla lepszej wydajności.  
- **Uruchom ponownie** komputer, aby ustawienia zaczęły działać.

### Przykłady: Proszę [kliknij ten link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.