<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:38:43+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "nl"
}
-->
## Welkom bij de Phi labs met C#

Er is een selectie labs die laat zien hoe je de krachtige verschillende versies van Phi-modellen kunt integreren in een .NET-omgeving.

## Vereisten

Voordat je de voorbeeldcode uitvoert, zorg dat je het volgende hebt geïnstalleerd:

**.NET 9:** Zorg dat je de [laatste versie van .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) op je computer hebt staan.

**(Optioneel) Visual Studio of Visual Studio Code:** Je hebt een IDE of code-editor nodig die .NET-projecten kan uitvoeren. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) of [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) worden aanbevolen.

**Gebruik git** om lokaal een van de beschikbare Phi-3, Phi3.5 of Phi-4 versies te clonen van [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Download Phi-4 ONNX modellen** naar je lokale machine:

### navigeer naar de map om de modellen op te slaan

```bash
cd c:\phi\models
```

### voeg ondersteuning toe voor lfs

```bash
git lfs install 
```

### clone en download het Phi-4 mini instruct model en het Phi-4 multimodaal model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Download de Phi-3 ONNX modellen** naar je lokale machine:

### clone en download het Phi-3 mini 4K instruct model en het Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Belangrijk:** De huidige demo’s zijn ontworpen om de ONNX-versies van het model te gebruiken. De vorige stappen clonen de volgende modellen.

## Over de Labs

De hoofdoplossing bevat verschillende voorbeeldlabs die de mogelijkheden van de Phi-modellen met C# demonstreren.

| Project | Model | Beschrijving |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 of Phi-3.5 | Voorbeeld console chat waarmee de gebruiker vragen kan stellen. Het project laadt een lokaal ONNX Phi-3 model met behulp van de `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 of Phi-3.5 | Voorbeeld console chat waarmee de gebruiker vragen kan stellen. Het project laadt een lokaal ONNX Phi-3 model met behulp van de `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 of Phi-3.5 | Dit is een voorbeeldproject dat een lokaal phi3 vision model gebruikt om afbeeldingen te analyseren. Het project laadt een lokaal ONNX Phi-3 Vision model met behulp van de `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 of Phi-3.5 | Dit is een voorbeeldproject dat een lokaal phi3 vision model gebruikt om afbeeldingen te analyseren. Het project laadt een lokaal ONNX Phi-3 Vision model met behulp van de `Microsoft.ML.OnnxRuntime` libraries. Het project toont ook een menu met verschillende opties om met de gebruiker te communiceren. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Voorbeeld console chat waarmee de gebruiker vragen kan stellen. Het project laadt een lokaal ONNX Phi-4 model met behulp van de `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Voorbeeld console chat waarmee de gebruiker vragen kan stellen. Het project laadt een lokaal ONNX Phi-4 model met behulp van de `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Voorbeeld console chat waarmee de gebruiker vragen kan stellen. Het project laadt een lokaal ONNX Phi-4 model met behulp van de `Microsoft.ML.OnnxRuntimeGenAI` libraries en implementeert de `IChatClient` van `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Voorbeeld console chat waarmee de gebruiker vragen kan stellen. De chat maakt gebruik van geheugen. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Dit is een voorbeeldproject dat een lokaal Phi-4 model gebruikt om afbeeldingen te analyseren en het resultaat in de console toont. Het project laadt een lokaal Phi-4-`multimodal-instruct-onnx` model met behulp van de `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Dit is een voorbeeldproject dat een lokaal Phi-4 model gebruikt om een audiobestand te analyseren, een transcriptie van het bestand te genereren en het resultaat in de console te tonen. Het project laadt een lokaal Phi-4-`multimodal-instruct-onnx` model met behulp van de `Microsoft.ML.OnnxRuntime` libraries. |

## Hoe de projecten uit te voeren

Volg deze stappen om de projecten uit te voeren:

1. Clone de repository naar je lokale machine.

1. Open een terminal en navigeer naar het gewenste project. Bijvoorbeeld, laten we `LabsPhi4-Chat-01OnnxRuntime` uitvoeren.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Voer het project uit met het commando

    ```bash
    dotnet run
    ```

1. Het voorbeeldproject vraagt om invoer van de gebruiker en reageert met het lokale model.

   De lopende demo ziet er ongeveer zo uit:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.