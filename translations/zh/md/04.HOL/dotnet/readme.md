<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-07T13:09:54+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "zh"
}
-->
﻿## 欢迎使用 C# 的 Phi 实验室

这里有一系列实验室示例，展示了如何在 .NET 环境中集成强大的不同版本的 Phi 模型。

## 前提条件

在运行示例之前，请确保已安装以下内容：

**.NET 9：** 确保你的机器上安装了[最新版本的 .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)。

**（可选）Visual Studio 或 Visual Studio Code：** 你需要一个能够运行 .NET 项目的 IDE 或代码编辑器。推荐使用[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo)或[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)。

**使用 git** 从 [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) 本地克隆可用的 Phi-3、Phi3.5 或 Phi-4 版本。

**下载 Phi-4 ONNX 模型** 到本地机器：

### 进入存放模型的文件夹

```bash
cd c:\phi\models
```

### 添加 lfs 支持

```bash
git lfs install 
```

### 克隆并下载 Phi-4 mini instruct 模型和 Phi-4 多模态模型

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**下载 Phi-3 ONNX 模型** 到本地机器：

### 克隆并下载 Phi-3 mini 4K instruct 模型和 Phi-3 vision 128K 模型

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**重要提示：** 当前演示设计为使用模型的 ONNX 版本。上述步骤克隆了以下模型。

## 关于实验室

主解决方案包含多个示例实验室，展示了使用 C# 调用 Phi 模型的功能。

| 项目 | 模型 | 描述 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 或 Phi-3.5 | 示例控制台聊天，允许用户提问。该项目使用 `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` 加载本地 ONNX Phi-3 模型。

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 使用以下命令运行项目

    ```bash
    dotnet run
    ```

1. 示例项目会提示用户输入，并使用本地模型进行回复。

   运行中的演示类似于：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。