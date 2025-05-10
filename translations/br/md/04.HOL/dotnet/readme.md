<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:43:14+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "br"
}
-->
﻿## Degemer mat Phi labs o implij C#

Bez' ez eus ur roll laboratoarioù a ginnig penaos lakaat da vevañ meur a stumm eus ar modleoù Phi kreñv e un endro .NET.

## Reolennoù Goude

A-raok kenderc'hel gant ar sampl, surit ez eus ar pezh da-heul staliet war ho urzhiataer:

**.NET 9:** Gwirit e vez staliet war ho urzhiataer ar [stumm diwezhañ eus .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo).

**(Dibabet) Visual Studio pe Visual Studio Code:** Bez' ez eus ezhomm eus un IDE pe ur stumm kodennoù a c'hell kenderc'hel raktresoù .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) pe [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) a vez kinniget.

**Gant git** klonañ en ho lec'h-stad unan eus ar Phi-3, Phi3.5 pe Phi-4 a zo war [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Pellgargañ modleoù Phi-4 ONNX** war ho urzhiataer:

### mont d'ar c'havlec'h evit enrollañ ar modleoù

```bash
cd c:\phi\models
```

### ouzhpennañ skoazell evit lfs

```bash
git lfs install 
```

### klonañ ha pellgargañ ar model Phi-4 mini instruct ha Phi-4 multimodal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Pellgargañ modleoù Phi-3 ONNX** war ho urzhiataer:

### klonañ ha pellgargañ ar model Phi-3 mini 4K instruct hag ar model Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Pelec'h a bouez:** An demoù a-vremañ zo bet krouet evit implij ar stummoù ONNX eus ar model. Ar poentoù a-raok a glonañ an modleoù da-heul.

## War-benn ar Laboratoarioù

Ar raktres pennañ en deus meur a laboratoar sampl a zispleg galloudoù ar modleoù Phi o implij C#.

| Raktres | Model | Deskrivadur |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 pe Phi-3.5 | Sampl evit komz e konsolel a ro an tu d'ar user goulenn goulennoù. Ar raktres a karg ur model ONNX Phi-3 lec'hel o implij `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Kenderc'hel ar raktres gant ar komand

    ```bash
    dotnet run
    ```

1. Ar raktres sampl a c'houlenn ur gemennadenn digant ar user ha respont a ra o implij ar model lec'hel.

   An demo o kenderc'hel a zo heñvel ouzh hini-mañ:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.