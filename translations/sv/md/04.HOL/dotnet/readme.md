## Välkommen till Phi-laboratorierna med C#

Här finns ett urval av laboratorier som visar hur man integrerar de kraftfulla olika versionerna av Phi-modeller i en .NET-miljö.

## Förutsättningar

Innan du kör exemplet, se till att du har följande installerat:

**.NET 9:** Kontrollera att du har [senaste versionen av .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) installerad på din dator.

**(Valfritt) Visual Studio eller Visual Studio Code:** Du behöver en IDE eller kodredigerare som kan köra .NET-projekt. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) eller [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) rekommenderas.

**Använd git** för att klona lokalt någon av de tillgängliga Phi-3, Phi3.5 eller Phi-4 versionerna från [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Ladda ner Phi-4 ONNX-modeller** till din lokala dator:

### navigera till mappen där modellerna ska sparas

```bash
cd c:\phi\models
```

### lägg till stöd för lfs

```bash
git lfs install 
```

### klona och ladda ner Phi-4 mini instruct-modellen och Phi-4 multimodal-modellen

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Ladda ner Phi-3 ONNX-modeller** till din lokala dator:

### klona och ladda ner Phi-3 mini 4K instruct-modellen och Phi-3 vision 128K-modellen

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Viktigt:** De nuvarande demonstrationerna är designade för att använda ONNX-versionerna av modellen. Stegen ovan klonar följande modeller.

## Om laboratorierna

Huvudlösningen innehåller flera exempel på laboratorier som visar Phi-modellernas kapacitet med C#.

| Projekt | Modell | Beskrivning |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 eller Phi-3.5 | Exempel på konsolchatt som låter användaren ställa frågor. Projektet laddar en lokal ONNX Phi-3-modell med hjälp av `Microsoft.ML.OnnxRuntime`-biblioteken. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 eller Phi-3.5 | Exempel på konsolchatt som låter användaren ställa frågor. Projektet laddar en lokal ONNX Phi-3-modell med hjälp av `Microsoft.Semantic.Kernel`-biblioteken. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 eller Phi-3.5 | Detta är ett exempelprojekt som använder en lokal phi3 vision-modell för att analysera bilder. Projektet laddar en lokal ONNX Phi-3 Vision-modell med hjälp av `Microsoft.ML.OnnxRuntime`-biblioteken. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 eller Phi-3.5 | Detta är ett exempelprojekt som använder en lokal phi3 vision-modell för att analysera bilder. Projektet laddar en lokal ONNX Phi-3 Vision-modell med hjälp av `Microsoft.ML.OnnxRuntime`-biblioteken. Projektet visar också en meny med olika alternativ för att interagera med användaren. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Exempel på konsolchatt som låter användaren ställa frågor. Projektet laddar en lokal ONNX Phi-4-modell med hjälp av `Microsoft.ML.OnnxRuntime`-biblioteken. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Exempel på konsolchatt som låter användaren ställa frågor. Projektet laddar en lokal ONNX Phi-4-modell med hjälp av `Semantic Kernel`-biblioteken. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Exempel på konsolchatt som låter användaren ställa frågor. Projektet laddar en lokal ONNX Phi-4-modell med hjälp av `Microsoft.ML.OnnxRuntimeGenAI`-biblioteken och implementerar `IChatClient` från `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Exempel på konsolchatt som låter användaren ställa frågor. Chatten har minnesfunktion. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Detta är ett exempelprojekt som använder en lokal Phi-4-modell för att analysera bilder och visa resultatet i konsolen. Projektet laddar en lokal Phi-4-`multimodal-instruct-onnx`-modell med hjälp av `Microsoft.ML.OnnxRuntime`-biblioteken. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Detta är ett exempelprojekt som använder en lokal Phi-4-modell för att analysera en ljudfil, generera en transkription av filen och visa resultatet i konsolen. Projektet laddar en lokal Phi-4-`multimodal-instruct-onnx`-modell med hjälp av `Microsoft.ML.OnnxRuntime`-biblioteken. |

## Hur man kör projekten

För att köra projekten, följ dessa steg:

1. Klona repositoryt till din lokala dator.

1. Öppna en terminal och navigera till önskat projekt. Till exempel, låt oss köra `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Kör projektet med kommandot

    ```bash
    dotnet run
    ```

1. Exempelprojektet frågar efter användarinput och svarar med hjälp av den lokala modellen.

   Den körande demon liknar denna:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.