<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:16:59+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "pl"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo prezentujące WebGPU i wzorzec RAG
Wzorzec RAG z modelem Phi-3 Onnx Hosted wykorzystuje podejście Retrieval-Augmented Generation, łącząc moc modeli Phi-3 z hostingiem ONNX dla efektywnych wdrożeń AI. Ten wzorzec jest kluczowy przy dostrajaniu modeli do zadań specyficznych dla danej dziedziny, oferując połączenie jakości, opłacalności i rozumienia długich kontekstów. Jest częścią pakietu Azure AI, który zapewnia szeroki wybór modeli łatwych do znalezienia, wypróbowania i użycia, odpowiadając na potrzeby personalizacji w różnych branżach. Modele Phi-3, w tym Phi-3-mini, Phi-3-small i Phi-3-medium, są dostępne w Azure AI Model Catalog i mogą być dostrajane oraz wdrażane samodzielnie lub za pośrednictwem platform takich jak HuggingFace i ONNX, co pokazuje zaangażowanie Microsoftu w dostępne i efektywne rozwiązania AI.

## Czym jest WebGPU
WebGPU to nowoczesne API graficzne dla przeglądarek internetowych, zaprojektowane, aby zapewnić efektywny dostęp do procesora graficznego (GPU) urządzenia bezpośrednio z poziomu przeglądarki. Ma zastąpić WebGL, oferując kilka kluczowych usprawnień:

1. **Kompatybilność z nowoczesnymi GPU**: WebGPU jest stworzony, by działać bezproblemowo z współczesnymi architekturami GPU, wykorzystując systemowe API takie jak Vulkan, Metal i Direct3D 12.
2. **Zwiększona wydajność**: Obsługuje obliczenia ogólnego przeznaczenia na GPU oraz szybsze operacje, co czyni go odpowiednim zarówno do renderowania grafiki, jak i zadań związanych z uczeniem maszynowym.
3. **Zaawansowane funkcje**: WebGPU daje dostęp do bardziej zaawansowanych możliwości GPU, umożliwiając realizację bardziej złożonych i dynamicznych zadań graficznych i obliczeniowych.
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

Po włączeniu flagi musisz ponownie uruchomić przeglądarkę, aby zmiany zaczęły działać. Kliknij przycisk Relaunch, który pojawi się na dole strony.

- Na Linuxie uruchom przeglądarkę z parametrem `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ma WebGPU włączone domyślnie.
- W Firefox Nightly wpisz about:config w pasku adresu i ustaw `dom.webgpu.enabled` na true.

### Konfiguracja GPU dla Microsoft Edge

Oto kroki, aby ustawić wysokowydajny GPU dla Microsoft Edge na Windows:

- **Otwórz Ustawienia:** Kliknij menu Start i wybierz Ustawienia.
- **Ustawienia systemowe:** Przejdź do System, a następnie Ekran.
- **Ustawienia grafiki:** Przewiń w dół i kliknij Ustawienia grafiki.
- **Wybierz aplikację:** W sekcji „Wybierz aplikację do ustawienia preferencji” wybierz Aplikacja pulpitu, a następnie Przeglądaj.
- **Wybierz Edge:** Przejdź do folderu instalacyjnego Edge (zazwyczaj `C:\Program Files (x86)\Microsoft\Edge\Application`) i wybierz `msedge.exe`.
- **Ustaw preferencję:** Kliknij Opcje, wybierz Wysoka wydajność, a następnie kliknij Zapisz.  
To zapewni, że Microsoft Edge będzie korzystać z Twojego wysokowydajnego GPU dla lepszej wydajności.  
- **Uruchom ponownie** komputer, aby ustawienia zaczęły działać.

### Otwórz swój Codespace:
Przejdź do swojego repozytorium na GitHub.  
Kliknij przycisk Code i wybierz Open with Codespaces.

Jeśli nie masz jeszcze Codespace, możesz go utworzyć, klikając New codespace.

**Note** Instalacja środowiska Node w Twoim codespace  
Uruchamianie demo npm z GitHub Codespace to świetny sposób na testowanie i rozwijanie projektu. Oto przewodnik krok po kroku, który pomoże Ci zacząć:

### Skonfiguruj środowisko:
Po otwarciu Codespace upewnij się, że masz zainstalowane Node.js i npm. Możesz to sprawdzić, uruchamiając:  
```
node -v
```  
```
npm -v
```

Jeśli nie są zainstalowane, możesz je zainstalować za pomocą:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Przejdź do katalogu projektu:
Użyj terminala, aby przejść do katalogu, w którym znajduje się Twój projekt npm:  
```
cd path/to/your/project
```

### Zainstaluj zależności:
Uruchom następujące polecenie, aby zainstalować wszystkie niezbędne zależności wymienione w pliku package.json:  

```
npm install
```

### Uruchom demo:
Po zainstalowaniu zależności możesz uruchomić skrypt demo. Zazwyczaj jest on określony w sekcji scripts pliku package.json. Na przykład, jeśli Twój skrypt demo nazywa się start, możesz uruchomić:  

```
npm run build
```  
```
npm run dev
```

### Uzyskaj dostęp do demo:
Jeśli demo wymaga serwera WWW, Codespaces udostępni URL do jego otwarcia. Szukaj powiadomienia lub sprawdź zakładkę Ports, aby znaleźć adres.

**Note:** Model musi być zapisany w pamięci podręcznej przeglądarki, więc załadowanie może chwilę potrwać.

### Demo RAG
Prześlij plik markdown `intro_rag.md`, aby ukończyć rozwiązanie RAG. Jeśli korzystasz z codespaces, możesz pobrać plik z lokalizacji `01.InferencePhi3/docs/`

### Wybierz swój plik:
Kliknij przycisk „Choose File”, aby wybrać dokument, który chcesz przesłać.

### Prześlij dokument:
Po wybraniu pliku kliknij przycisk „Upload”, aby załadować dokument do RAG (Retrieval-Augmented Generation).

### Rozpocznij czat:
Po przesłaniu dokumentu możesz rozpocząć sesję czatu wykorzystującą RAG na podstawie zawartości Twojego dokumentu.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło wiarygodne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.