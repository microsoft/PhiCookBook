<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:38:07+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "no"
}
-->
## Velkommen til Phi-laboratoriene med C#

Her finner du et utvalg laboratorier som viser hvordan du kan integrere de kraftige forskjellige versjonene av Phi-modellene i et .NET-miljø.

## Forutsetninger

Før du kjører eksempelet, sørg for at du har følgende installert:

**.NET 9:** Sørg for at du har [nyeste versjon av .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) installert på maskinen din.

**(Valgfritt) Visual Studio eller Visual Studio Code:** Du trenger et IDE eller en kodeeditor som kan kjøre .NET-prosjekter. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) eller [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) anbefales.

**Bruk git** for å klone lokalt en av de tilgjengelige Phi-3, Phi3.5 eller Phi-4 versjonene fra [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Last ned Phi-4 ONNX-modeller** til din lokale maskin:

### naviger til mappen der modellene skal lagres

```bash
cd c:\phi\models
```

### legg til støtte for lfs

```bash
git lfs install 
```

### klon og last ned Phi-4 mini instruct-modellen og Phi-4 multimodal-modellen

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Last ned Phi-3 ONNX-modeller** til din lokale maskin:

### klon og last ned Phi-3 mini 4K instruct-modellen og Phi-3 vision 128K-modellen

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Viktig:** De nåværende demoene er designet for å bruke ONNX-versjonene av modellen. De forrige stegene kloner følgende modeller.

## Om laboratoriene

Hovedløsningen har flere eksempellaboratorier som demonstrerer mulighetene til Phi-modellene ved bruk av C#.

| Prosjekt | Modell | Beskrivelse |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 eller Phi-3.5 | Eksempel på konsollchat som lar brukeren stille spørsmål. Prosjektet laster en lokal ONNX Phi-3-modell ved hjelp av `Microsoft.ML.OnnxRuntime`-bibliotekene. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 eller Phi-3.5 | Eksempel på konsollchat som lar brukeren stille spørsmål. Prosjektet laster en lokal ONNX Phi-3-modell ved hjelp av `Microsoft.Semantic.Kernel`-bibliotekene. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 eller Phi-3.5 | Dette er et eksempelprosjekt som bruker en lokal phi3 vision-modell for å analysere bilder. Prosjektet laster en lokal ONNX Phi-3 Vision-modell ved hjelp av `Microsoft.ML.OnnxRuntime`-bibliotekene. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 eller Phi-3.5 | Dette er et eksempelprosjekt som bruker en lokal phi3 vision-modell for å analysere bilder. Prosjektet laster en lokal ONNX Phi-3 Vision-modell ved hjelp av `Microsoft.ML.OnnxRuntime`-bibliotekene. Prosjektet viser også en meny med ulike alternativer for å samhandle med brukeren. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Eksempel på konsollchat som lar brukeren stille spørsmål. Prosjektet laster en lokal ONNX Phi-4-modell ved hjelp av `Microsoft.ML.OnnxRuntime`-bibliotekene. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Eksempel på konsollchat som lar brukeren stille spørsmål. Prosjektet laster en lokal ONNX Phi-4-modell ved hjelp av `Semantic Kernel`-bibliotekene. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Eksempel på konsollchat som lar brukeren stille spørsmål. Prosjektet laster en lokal ONNX Phi-4-modell ved hjelp av `Microsoft.ML.OnnxRuntimeGenAI`-bibliotekene og implementerer `IChatClient` fra `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Eksempel på konsollchat som lar brukeren stille spørsmål. Chatten har minnefunksjon. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Dette er et eksempelprosjekt som bruker en lokal Phi-4-modell for å analysere bilder og viser resultatet i konsollen. Prosjektet laster en lokal Phi-4-`multimodal-instruct-onnx`-modell ved hjelp av `Microsoft.ML.OnnxRuntime`-bibliotekene. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Dette er et eksempelprosjekt som bruker en lokal Phi-4-modell for å analysere en lydfil, generere transkripsjon av filen og vise resultatet i konsollen. Prosjektet laster en lokal Phi-4-`multimodal-instruct-onnx`-modell ved hjelp av `Microsoft.ML.OnnxRuntime`-bibliotekene. |

## Hvordan kjøre prosjektene

For å kjøre prosjektene, følg disse stegene:

1. Klon repositoriet til din lokale maskin.

1. Åpne en terminal og naviger til ønsket prosjekt. For eksempel, la oss kjøre `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Kjør prosjektet med kommandoen

    ```bash
    dotnet run
    ```

1. Eksempelprosjektet spør om brukerinput og svarer ved hjelp av den lokale modellen.

   Den kjørende demoen ser omtrent slik ut:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.