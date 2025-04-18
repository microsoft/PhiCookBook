<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0e3a4453db505856d5d991285dd6001",
  "translation_date": "2025-04-04T19:13:56+00:00",
  "source_file": "md\\04.HOL\\dotnet\\readme.md",
  "language_code": "hk"
}
-->
## 歡迎使用 Phi 實驗室的 C#

這裡有一系列的實驗室示範，展示如何在 .NET 環境中整合不同版本的強大 Phi 模型。

## 先決條件

在運行範例之前，請確保已安裝以下內容：

**.NET 9:** 確保你的機器上已安裝[最新版本的 .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)。

**（可選）Visual Studio 或 Visual Studio Code:** 你需要一個能運行 .NET 專案的 IDE 或程式碼編輯器。推薦使用 [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) 或 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)。

**使用 git** 從 [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) 本地克隆其中一個可用的 Phi-3、Phi3.5 或 Phi-4 版本。

**下載 Phi-4 ONNX 模型** 到你的本地機器：

### 導航到存儲模型的資料夾

```bash
cd c:\phi\models
```

### 添加 lfs 支援

```bash
git lfs install 
```

### 克隆並下載 Phi-4 mini instruct 模型和 Phi-4 multi modal 模型

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**下載 Phi-3 ONNX 模型** 到你的本地機器：

### 克隆並下載 Phi-3 mini 4K instruct 模型和 Phi-3 vision 128K 模型

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**重要提示:** 當前的演示設計用於使用模型的 ONNX 版本。以上步驟克隆了以下模型。

## 關於實驗室

主要解決方案包含多個範例實驗室，展示使用 C# 的 Phi 模型的功能。

| 專案 | 模型 | 描述 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 或 Phi-3.5 | 範例主控台聊天，允許使用者提出問題。專案使用 `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` 加載本地 ONNX Phi-3 模型。

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 使用以下命令運行專案

    ```bash
    dotnet run
    ```

1. 範例專案會要求使用者輸入問題並使用本地模式回覆。

   運行中的演示類似於以下內容：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免責聲明**:  
本文件使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文作為權威來源。如涉及關鍵信息，建議尋求專業人工翻譯。我們對於因使用本翻譯而引起的任何誤解或誤讀概不負責。