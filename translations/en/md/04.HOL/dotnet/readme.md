<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-09T19:36:21+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "en"
}
-->
## Welcome to the Phi labs using C#

Here you’ll find a selection of labs demonstrating how to integrate the powerful different versions of Phi models within a .NET environment.

## Prerequisites

Before running the sample, make sure you have the following installed:

**.NET 9:** Ensure you have the [latest version of .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) installed on your machine.

**(Optional) Visual Studio or Visual Studio Code:** You’ll need an IDE or code editor capable of running .NET projects. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) or [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) are recommended.

**Using git** clone locally one of the available Phi-3, Phi3.5, or Phi-4 versions from [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Download Phi-4 ONNX models** to your local machine:

### Navigate to the folder to store the models

```bash
cd c:\phi\models
```

### Add support for lfs

```bash
git lfs install 
```

### Clone and download Phi-4 mini instruct model and the Phi-4 multi modal model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Download the Phi-3 ONNX models** to your local machine:

### Clone and download Phi-3 mini 4K instruct model and Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Important:** The current demos are designed to use the ONNX versions of the model. The previous steps clone the following models.

## About the Labs

The main solution contains several sample Labs that demonstrate the capabilities of the Phi models using C#.

| Project | Model | Description |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 or Phi-3.5 | Sample console chat that lets the user ask questions. The project loads a local ONNX Phi-3 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that lets the user ask questions. The project loads a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | Sample project that uses a local phi3 vision model to analyze images. The project loads a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | Sample project that uses a local phi3 vision model to analyze images. The project loads a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. It also presents a menu with different options to interact with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that lets the user ask questions. The project loads a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that lets the user ask questions. The project loads a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that lets the user ask questions. The project loads a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that lets the user ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Sample project that uses a local Phi-4 model to analyze images and displays the results in the console. The project loads a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Sample project that uses a local Phi-4 model to analyze an audio file, generate a transcript, and display the result in the console. The project loads a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. For example, let’s run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Run the project with the command

    ```bash
    dotnet run
    ```

1. The sample project will prompt for user input and respond using the local model.

   The running demo looks like this:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.