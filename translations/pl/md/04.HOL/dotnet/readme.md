<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:43:31+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "pl"
}
-->
## Witamy w laboratoriach Phi z użyciem C#

Dostępny jest zestaw laboratoriów, które pokazują, jak zintegrować różne wersje potężnych modeli Phi w środowisku .NET.

## Wymagania wstępne

Przed uruchomieniem przykładu upewnij się, że masz zainstalowane:

**.NET 9:** Upewnij się, że masz na swoim komputerze [najnowszą wersję .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Opcjonalnie) Visual Studio lub Visual Studio Code:** Będziesz potrzebować IDE lub edytora kodu, który potrafi uruchamiać projekty .NET. Zalecane są [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) lub [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

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

### sklonuj i pobierz model Phi-4 mini instruct oraz model Phi-4 multi modal

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

**Ważne:** Obecne dema zostały zaprojektowane do korzystania z wersji ONNX modelu. Wcześniejsze kroki klonują następujące modele.

## O laboratoriach

Główne rozwiązanie zawiera kilka przykładowych laboratoriów, które demonstrują możliwości modeli Phi z użyciem C#.

| Projekt | Model | Opis |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 lub Phi-3.5 | Przykładowy czat konsolowy, który pozwala użytkownikowi zadawać pytania. Projekt ładuje lokalny model ONNX Phi-3, korzystając z `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Uruchom projekt za pomocą polecenia

    ```bash
    dotnet run
    ```

1. Przykładowy projekt prosi o dane od użytkownika i odpowiada, korzystając z lokalnego modelu.

   Uruchomione demo wygląda podobnie do tego:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło wiążące. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.