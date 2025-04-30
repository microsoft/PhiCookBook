<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0e3a4453db505856d5d991285dd6001",
  "translation_date": "2025-04-04T13:38:38+00:00",
  "source_file": "md\\04.HOL\\dotnet\\readme.md",
  "language_code": "mo"
}
-->
## Phi-labs ka soo dhawow adoo isticmaalaya C#

Waxaa jira xulasho maktabado muujinaya sida loo dhexgeliyo noocyada kala duwan ee awoodda leh ee Phi moodallo ku dhex jira deegaanka .NET.

## Shuruudaha Hore

Ka hor inta aadan orodsiin tusaalaha, hubi inaad ku rakibtay waxyaabaha soo socda:

**.NET 9:** Hubi inaad ku rakibtay [nooca ugu dambeeya ee .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ee ku shaqeynaya qalabkaaga.

**(Ikhtiyaari) Visual Studio ama Visual Studio Code:** Waxaad u baahan doontaa IDE ama tifaftire kood oo awood u leh orodsiinta mashruucyada .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ama [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ayaa lagu talinayaa.

**Isticmaal git** si aad u soo rogto mid ka mid ah noocyada Phi-3, Phi3.5 ama Phi-4 ee laga heli karo [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Soo dejiso moodallada Phi-4 ONNX** qalabkaaga maxalliga ah:

### u dhaadhac folderka lagu kaydinayo moodallada

```bash
cd c:\phi\models
```

### ku dar taageerada lfs

```bash
git lfs install 
```

### soo rog oo soo dejiso Phi-4 mini instruct model iyo Phi-4 multi modal model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Soo dejiso moodallada Phi-3 ONNX** qalabkaaga maxalliga ah:

### soo rog oo soo dejiso Phi-3 mini 4K instruct model iyo Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Muhiim:** Muuqaalada hadda jira waxay loogu talagalay isticmaalka noocyada ONNX ee moodallada. Tallaabooyinkii hore waxay soo rogaan moodallada soo socda.

## Ku saabsan Maktabadaha

Xalka ugu weyn wuxuu leeyahay dhowr maktabado tusaale ah oo muujinaya awoodaha moodallada Phi iyadoo la isticmaalayo C#.

| Mashruuc | Model | Sharaxaad |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ama Phi-3.5 | Tusaale console chat oo u oggolaanaya isticmaalaha inuu su'aalo weydiiyo. Mashruucu wuxuu soo rogayaa moodalka ONNX ee maxalliga ah ee Phi-3 isagoo isticmaalaya `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Mashruuca ku orodsiin amarka

    ```bash
    dotnet run
    ```

1. Mashruuca tusaalaha wuxuu weydiisanayaa isticmaalaha wax gelin ah oo ka jawaabaya isagoo isticmaalaya habka maxalliga ah.

   Tusaalaha orodaya wuxuu u eg yahay midkan:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

It seems like you want the text translated to "mo," but could you clarify what "mo" refers to? Are you referring to a specific language or dialect? For example, Maori, Mongolian, or something else?