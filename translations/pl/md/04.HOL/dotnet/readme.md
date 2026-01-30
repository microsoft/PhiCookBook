## Witamy w laboratoriach Phi z użyciem C#

Dostępny jest zestaw laboratoriów, które pokazują, jak zintegrować różne wersje potężnych modeli Phi w środowisku .NET.

## Wymagania wstępne

Przed uruchomieniem przykładu upewnij się, że masz zainstalowane:

**.NET 9:** Upewnij się, że masz na swoim komputerze [najnowszą wersję .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Opcjonalnie) Visual Studio lub Visual Studio Code:** Potrzebujesz IDE lub edytora kodu, który pozwoli na uruchamianie projektów .NET. Zalecane są [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) lub [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**Używając git** sklonuj lokalnie jedną z dostępnych wersji Phi-3, Phi3.5 lub Phi-4 z [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Pobierz modele Phi-4 ONNX** na swój lokalny komputer:

### przejdź do folderu, w którym chcesz przechowywać modele

```bash
cd c:\phi\models
```

### dodaj wsparcie dla lfs

```bash
git lfs install 
```

### sklonuj i pobierz model Phi-4 mini instruct oraz model Phi-4 multimodalny

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Pobierz modele Phi-3 ONNX** na swój lokalny komputer:

### sklonuj i pobierz model Phi-3 mini 4K instruct oraz model Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Ważne:** Obecne dema są zaprojektowane do używania wersji modeli ONNX. Powyższe kroki klonują następujące modele.

## O laboratoriach

Główne rozwiązanie zawiera kilka przykładowych laboratoriów, które demonstrują możliwości modeli Phi z użyciem C#.

| Projekt | Model | Opis |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 lub Phi-3.5 | Przykładowy czat konsolowy, który pozwala użytkownikowi zadawać pytania. Projekt ładuje lokalny model ONNX Phi-3 za pomocą bibliotek `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 lub Phi-3.5 | Przykładowy czat konsolowy, który pozwala użytkownikowi zadawać pytania. Projekt ładuje lokalny model ONNX Phi-3 za pomocą bibliotek `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 lub Phi-3.5 | To przykładowy projekt, który używa lokalnego modelu phi3 vision do analizy obrazów. Projekt ładuje lokalny model ONNX Phi-3 Vision za pomocą bibliotek `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 lub Phi-3.5 | To przykładowy projekt, który używa lokalnego modelu phi3 vision do analizy obrazów. Projekt ładuje lokalny model ONNX Phi-3 Vision za pomocą bibliotek `Microsoft.ML.OnnxRuntime`. Projekt prezentuje również menu z różnymi opcjami interakcji z użytkownikiem. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Przykładowy czat konsolowy, który pozwala użytkownikowi zadawać pytania. Projekt ładuje lokalny model ONNX Phi-4 za pomocą bibliotek `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Przykładowy czat konsolowy, który pozwala użytkownikowi zadawać pytania. Projekt ładuje lokalny model ONNX Phi-4 za pomocą bibliotek `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Przykładowy czat konsolowy, który pozwala użytkownikowi zadawać pytania. Projekt ładuje lokalny model ONNX Phi-4 za pomocą bibliotek `Microsoft.ML.OnnxRuntimeGenAI` i implementuje `IChatClient` z `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Przykładowy czat konsolowy, który pozwala użytkownikowi zadawać pytania. Czat posiada zaimplementowaną pamięć. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | To przykładowy projekt, który używa lokalnego modelu Phi-4 do analizy obrazów i wyświetla wynik w konsoli. Projekt ładuje lokalny model Phi-4-`multimodal-instruct-onnx` za pomocą bibliotek `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | To przykładowy projekt, który używa lokalnego modelu Phi-4 do analizy pliku audio, generuje transkrypcję pliku i wyświetla wynik w konsoli. Projekt ładuje lokalny model Phi-4-`multimodal-instruct-onnx` za pomocą bibliotek `Microsoft.ML.OnnxRuntime`. |

## Jak uruchomić projekty

Aby uruchomić projekty, wykonaj następujące kroki:

1. Sklonuj repozytorium na swój lokalny komputer.

1. Otwórz terminal i przejdź do wybranego projektu. Na przykład, uruchommy `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Uruchom projekt poleceniem

    ```bash
    dotnet run
    ```

1. Przykładowy projekt poprosi o dane wejściowe od użytkownika i odpowie, korzystając z lokalnego modelu.

   Uruchomione demo wygląda podobnie do tego:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.