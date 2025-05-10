<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:44:49+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "pl"
}
-->
# **Inference Phi-3 w Androidzie**

Przyjrzyjmy się, jak można przeprowadzać inference z Phi-3-mini na urządzeniach z Androidem. Phi-3-mini to nowa seria modeli od Microsoft, która umożliwia wdrażanie dużych modeli językowych (LLM) na urządzeniach brzegowych i IoT.

## Semantic Kernel i Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) to framework aplikacyjny, który pozwala tworzyć aplikacje kompatybilne z Azure OpenAI Service, modelami OpenAI, a nawet lokalnymi modelami. Jeśli dopiero zaczynasz z Semantic Kernel, polecamy zapoznać się z [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Dostęp do Phi-3-mini za pomocą Semantic Kernel

Możesz połączyć go z Hugging Face Connector w Semantic Kernel. Odwołaj się do tego [przykładowego kodu](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Domyślnie odpowiada to ID modelu na Hugging Face, ale możesz też połączyć się z lokalnie uruchomionym serwerem modelu Phi-3-mini.

### Wywoływanie modeli kwantyzowanych za pomocą Ollama lub LlamaEdge

Wielu użytkowników woli korzystać z modeli kwantyzowanych, aby uruchamiać modele lokalnie. [Ollama](https://ollama.com/) i [LlamaEdge](https://llamaedge.com) pozwalają indywidualnym użytkownikom na wywoływanie różnych modeli kwantyzowanych:

#### Ollama

Możesz uruchomić `ollama run Phi-3` bezpośrednio lub skonfigurować go offline, tworząc `Modelfile` z ścieżką do pliku `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Przykładowy kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jeśli chcesz korzystać z plików `.gguf` jednocześnie w chmurze i na urządzeniach brzegowych, LlamaEdge będzie świetnym wyborem. Możesz zacząć od tego [przykładowego kodu](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Instalacja i uruchomienie na telefonach z Androidem

1. **Pobierz aplikację MLC Chat** (darmową) na telefony z Androidem.  
2. Pobierz plik APK (148MB) i zainstaluj go na swoim urządzeniu.  
3. Uruchom aplikację MLC Chat. Zobaczysz listę modeli AI, w tym Phi-3-mini.

Podsumowując, Phi-3-mini otwiera ekscytujące możliwości dla generatywnej AI na urządzeniach brzegowych i możesz zacząć eksplorować jego możliwości na Androidzie.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za wiarygodne źródło informacji. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.