<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:57:16+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "pl"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo prezentujący WebGPU i wzorzec RAG

Wzorzec RAG z modelem Phi-3.5 Onnx Hosted wykorzystuje podejście Retrieval-Augmented Generation, łącząc moc modeli Phi-3.5 z hostingiem ONNX dla efektywnych wdrożeń AI. Ten wzorzec jest kluczowy w dostrajaniu modeli do zadań specyficznych dla danej dziedziny, oferując połączenie jakości, opłacalności i rozumienia długich kontekstów. Jest częścią pakietu Azure AI, który oferuje szeroki wybór modeli łatwych do znalezienia, wypróbowania i użycia, odpowiadając na potrzeby personalizacji w różnych branżach.

## Czym jest WebGPU  
WebGPU to nowoczesne API graficzne dla sieci, zaprojektowane tak, aby zapewnić efektywny dostęp do procesora graficznego (GPU) urządzenia bezpośrednio z przeglądarek internetowych. Ma zastąpić WebGL, oferując kilka kluczowych ulepszeń:

1. **Kompatybilność z nowoczesnymi GPU**: WebGPU działa płynnie z współczesnymi architekturami GPU, wykorzystując systemowe API takie jak Vulkan, Metal i Direct3D 12.
2. **Zwiększona wydajność**: Obsługuje obliczenia ogólnego przeznaczenia na GPU oraz szybsze operacje, co czyni go odpowiednim zarówno do renderowania grafiki, jak i zadań uczenia maszynowego.
3. **Zaawansowane funkcje**: WebGPU daje dostęp do bardziej zaawansowanych możliwości GPU, umożliwiając tworzenie bardziej skomplikowanych i dynamicznych grafik oraz obciążeń obliczeniowych.
4. **Zmniejszenie obciążenia JavaScript**: Przekazując więcej zadań do GPU, WebGPU znacząco zmniejsza obciążenie JavaScript, co przekłada się na lepszą wydajność i płynniejsze działanie.

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

Po włączeniu flagi musisz ponownie uruchomić przeglądarkę, aby zmiany zaczęły działać. Kliknij przycisk Relaunch, który pojawi się na dole strony.

- W systemie Linux uruchom przeglądarkę z `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ma WebGPU włączone domyślnie.  
- W Firefox Nightly wpisz about:config w pasku adresu i `set dom.webgpu.enabled to true`.

### Konfiguracja GPU dla Microsoft Edge  

Oto kroki konfiguracji wydajnego GPU dla Microsoft Edge na Windows:

- **Otwórz Ustawienia:** Kliknij menu Start i wybierz Ustawienia.  
- **Ustawienia systemowe:** Przejdź do System, a następnie Ekran.  
- **Ustawienia grafiki:** Przewiń w dół i kliknij Ustawienia grafiki.  
- **Wybierz aplikację:** W sekcji „Wybierz aplikację, aby ustawić preferencje” wybierz Aplikacja pulpitowa, a następnie Przeglądaj.  
- **Wybierz Edge:** Przejdź do folderu instalacyjnego Edge (zazwyczaj `C:\Program Files (x86)\Microsoft\Edge\Application`) i wybierz `msedge.exe`.  
- **Ustaw preferencje:** Kliknij Opcje, wybierz Wysoka wydajność, a następnie kliknij Zapisz.  
To zapewni, że Microsoft Edge będzie korzystać z Twojego wydajnego GPU dla lepszej wydajności.  
- **Uruchom ponownie** komputer, aby ustawienia zaczęły działać.

### Przykłady : Proszę [kliknij ten link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uważany za źródło wiarygodne. W przypadku informacji o istotnym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.