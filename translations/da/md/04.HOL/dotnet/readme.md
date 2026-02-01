## Velkommen til Phi labs med C#

Der er et udvalg af labs, der viser, hvordan man integrerer de kraftfulde forskellige versioner af Phi-modeller i et .NET-miljø.

## Forudsætninger

Før du kører eksemplet, skal du sikre dig, at du har følgende installeret:

**.NET 9:** Sørg for, at du har den [nyeste version af .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) installeret på din maskine.

**(Valgfrit) Visual Studio eller Visual Studio Code:** Du skal bruge en IDE eller en kodeeditor, der kan køre .NET-projekter. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) eller [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) anbefales.

**Brug git** til at klone lokalt en af de tilgængelige Phi-3, Phi3.5 eller Phi-4 versioner fra [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Download Phi-4 ONNX modeller** til din lokale maskine:

### naviger til mappen, hvor modellerne skal gemmes

```bash
cd c:\phi\models
```

### tilføj support for lfs

```bash
git lfs install 
```

### klon og download Phi-4 mini instruct modellen og Phi-4 multimodal modellen

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Download Phi-3 ONNX modellerne** til din lokale maskine:

### klon og download Phi-3 mini 4K instruct modellen og Phi-3 vision 128K modellen

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Vigtigt:** De nuværende demoer er designet til at bruge ONNX-versionerne af modellen. De tidligere trin kloner følgende modeller.

## Om Labs

Hovedløsningen indeholder flere eksempler på Labs, der demonstrerer Phi-modellernes muligheder ved brug af C#.

| Projekt | Model | Beskrivelse |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 eller Phi-3.5 | Eksempel på konsolchat, der giver brugeren mulighed for at stille spørgsmål. Projektet indlæser en lokal ONNX Phi-3 model ved hjælp af `Microsoft.ML.OnnxRuntime` bibliotekerne. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 eller Phi-3.5 | Eksempel på konsolchat, der giver brugeren mulighed for at stille spørgsmål. Projektet indlæser en lokal ONNX Phi-3 model ved hjælp af `Microsoft.Semantic.Kernel` bibliotekerne. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 eller Phi-3.5 | Dette er et eksempelprojekt, der bruger en lokal phi3 vision model til at analysere billeder. Projektet indlæser en lokal ONNX Phi-3 Vision model ved hjælp af `Microsoft.ML.OnnxRuntime` bibliotekerne. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 eller Phi-3.5 | Dette er et eksempelprojekt, der bruger en lokal phi3 vision model til at analysere billeder. Projektet indlæser en lokal ONNX Phi-3 Vision model ved hjælp af `Microsoft.ML.OnnxRuntime` bibliotekerne. Projektet præsenterer også en menu med forskellige muligheder for at interagere med brugeren. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Eksempel på konsolchat, der giver brugeren mulighed for at stille spørgsmål. Projektet indlæser en lokal ONNX Phi-4 model ved hjælp af `Microsoft.ML.OnnxRuntime` bibliotekerne. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Eksempel på konsolchat, der giver brugeren mulighed for at stille spørgsmål. Projektet indlæser en lokal ONNX Phi-4 model ved hjælp af `Semantic Kernel` bibliotekerne. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Eksempel på konsolchat, der giver brugeren mulighed for at stille spørgsmål. Projektet indlæser en lokal ONNX Phi-4 model ved hjælp af `Microsoft.ML.OnnxRuntimeGenAI` bibliotekerne og implementerer `IChatClient` fra `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Eksempel på konsolchat, der giver brugeren mulighed for at stille spørgsmål. Chatten implementerer hukommelse. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Dette er et eksempelprojekt, der bruger en lokal Phi-4 model til at analysere billeder og viser resultatet i konsollen. Projektet indlæser en lokal Phi-4-`multimodal-instruct-onnx` model ved hjælp af `Microsoft.ML.OnnxRuntime` bibliotekerne. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Dette er et eksempelprojekt, der bruger en lokal Phi-4 model til at analysere en lydfil, generere en transskription af filen og vise resultatet i konsollen. Projektet indlæser en lokal Phi-4-`multimodal-instruct-onnx` model ved hjælp af `Microsoft.ML.OnnxRuntime` bibliotekerne. |

## Sådan kører du projekterne

For at køre projekterne, følg disse trin:

1. Klon repository til din lokale maskine.

1. Åbn en terminal og naviger til det ønskede projekt. For eksempel, lad os køre `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Kør projektet med kommandoen

    ```bash
    dotnet run
    ```

1. Eksempelprojektet beder om brugerinput og svarer ved hjælp af den lokale model.

   Den kørende demo ligner denne:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.