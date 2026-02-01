## Welcome to the Phi labs wey dey use C#

There is a selection of labs wey dey show how to integrate the powerful different versions of Phi models in a .NET environment.

## Wetin you need

Before running the sample, make sure say you don install the following:

**.NET 9:** Make sure say you get the [latest version of .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) installed on your machine.

**(Optional) Visual Studio or Visual Studio Code:** You go need an IDE or code editor wey fit run .NET projects. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) or [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) na dem we recommend.

**Using git** clone locally one of the available Phi-3, Phi3.5 or Phi-4 versions from [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Download Phi-4 ONNX models** to your local machine:

### navigate to the folder to store the models

```bash
cd c:\phi\models
```

### add support for lfs

```bash
git lfs install 
```

### clone and download Phi-4 mini instruct model and the Phi-4 multi modal model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Download the Phi-3 ONNX models** to your local machine:

### clone and download Phi-3 mini 4K instruct model and Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Important:** These demos dey designed to use the ONNX versions of the model. The previous steps don clone the following models.

## About the Labs

The main solution get several sample Labs wey dey demonstrate the capabilities of the Phi models wey dey use C#.

| Project | Model | Description |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 or Phi-3.5 | Sample console chat wey allow user to ask questions. The project dey load a local ONNX Phi-3 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat wey allow user to ask questions. The project dey load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | Na sample project wey dey use a local phi3 vision model to analyze images. The project dey load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | Na sample project wey dey use a local phi3 vision model to analyze images.. The project dey load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat wey allow user to ask questions. The project dey load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat wey allow user to ask questions. The project dey load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat wey allow user to ask questions. The project dey load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat wey allow user to ask questions. The chat get memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Na sample project wey dey use a local Phi-4 model to analyze images and show the result for the console. The project dey load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Na sample project wey dey use a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result for the console. The project dey load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Run the project with the command

    ```bash
    dotnet run
    ```

1. The sample project go ask for a user input and reply using the local model. 

   The running demo dey similar to this one:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:

Dis document na AI translate using Co‑op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get mistakes or wrong parts. The original document for im local language na di correct/official source. If na important or serious information, make you use professional human translator. We no dey responsible for any misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->