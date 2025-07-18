<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:09:47+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "pl"
}
-->
W kontekście Phi-3-mini, inferencja odnosi się do procesu wykorzystania modelu do dokonywania predykcji lub generowania wyników na podstawie danych wejściowych. Pozwól, że przedstawię więcej szczegółów na temat Phi-3-mini i jego możliwości inferencyjnych.

Phi-3-mini jest częścią serii modeli Phi-3 wydanych przez Microsoft. Modele te zostały zaprojektowane, aby na nowo zdefiniować możliwości Małych Modeli Językowych (SLM).

Oto kilka kluczowych informacji o Phi-3-mini i jego możliwościach inferencyjnych:

## **Przegląd Phi-3-mini:**
- Phi-3-mini ma rozmiar parametrów wynoszący 3,8 miliarda.
- Może działać nie tylko na tradycyjnych urządzeniach komputerowych, ale także na urządzeniach brzegowych, takich jak urządzenia mobilne i IoT.
- Wydanie Phi-3-mini umożliwia osobom prywatnym i przedsiębiorstwom wdrażanie SLM na różnych urządzeniach sprzętowych, zwłaszcza w środowiskach o ograniczonych zasobach.
- Obsługuje różne formaty modeli, w tym tradycyjny format PyTorch, skwantowany format gguf oraz skwantowaną wersję opartą na ONNX.

## **Dostęp do Phi-3-mini:**
Aby uzyskać dostęp do Phi-3-mini, możesz użyć [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) w aplikacji Copilot. Semantic Kernel jest generalnie kompatybilny z Azure OpenAI Service, modelami open-source na Hugging Face oraz modelami lokalnymi.  
Możesz także użyć [Ollama](https://ollama.com) lub [LlamaEdge](https://llamaedge.com) do wywoływania skwantowanych modeli. Ollama pozwala indywidualnym użytkownikom na korzystanie z różnych skwantowanych modeli, natomiast LlamaEdge zapewnia dostępność GGUF na różnych platformach.

## **Modele skwantowane:**
Wielu użytkowników woli korzystać z modeli skwantowanych do lokalnej inferencji. Na przykład, możesz bezpośrednio uruchomić Ollama run Phi-3 lub skonfigurować go offline za pomocą Modelfile. Plik Modelfile określa ścieżkę do pliku GGUF oraz format promptu.

## **Możliwości generatywnej AI:**
Połączenie SLM, takich jak Phi-3-mini, otwiera nowe możliwości dla generatywnej AI. Inferencja to tylko pierwszy krok; modele te mogą być wykorzystywane do różnych zadań w środowiskach o ograniczonych zasobach, niskich opóźnieniach i ograniczonych kosztach.

## **Odblokowanie generatywnej AI z Phi-3-mini: przewodnik po inferencji i wdrożeniu**  
Dowiedz się, jak korzystać z Semantic Kernel, Ollama/LlamaEdge oraz ONNX Runtime, aby uzyskać dostęp do modeli Phi-3-mini i przeprowadzać inferencję, a także poznaj możliwości generatywnej AI w różnych scenariuszach zastosowań.

**Funkcje**  
Inferencja modelu phi3-mini w:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Podsumowując, Phi-3-mini pozwala programistom eksplorować różne formaty modeli i wykorzystywać generatywną AI w różnych scenariuszach zastosowań.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.