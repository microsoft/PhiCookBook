<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0e3a4453db505856d5d991285dd6001",
  "translation_date": "2025-04-04T07:21:54+00:00",
  "source_file": "md\\04.HOL\\dotnet\\readme.md",
  "language_code": "tw"
}
-->
## 歡迎使用 C# 的 Phi 實驗室

這裡有一系列實驗，展示如何在 .NET 環境中整合不同版本的強大 Phi 模型。

## 先決條件

在執行範例之前，請確保已安裝以下內容：

**.NET 9:** 確保您的機器上已安裝 [最新版本的 .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)。

**（可選）Visual Studio 或 Visual Studio Code:** 您需要一個能夠執行 .NET 專案的 IDE 或程式碼編輯器。[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) 或 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) 是推薦選擇。

**使用 git** 從 [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) 本地克隆任一 Phi-3、Phi3.5 或 Phi-4 版本。

**下載 Phi-4 ONNX 模型** 到您的本地機器：

### 導航到存放模型的資料夾

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

**下載 Phi-3 ONNX 模型** 到您的本地機器：

### 克隆並下載 Phi-3 mini 4K instruct 模型和 Phi-3 vision 128K 模型

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**重要提示：** 目前的演示是為使用模型的 ONNX 版本而設計的。以上步驟會克隆以下模型。

## 關於實驗室

主要解決方案包含多個範例實驗室，展示如何使用 C# 利用 Phi 模型的功能。

| 專案 | 模型 | 描述 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 或 Phi-3.5 | 範例控制台聊天，允許使用者提出問題。專案載入本地 ONNX Phi-3 模型，使用 `Microsoft.ML.OnnxRuntime` libraries. |
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

1. 使用以下命令運行專案

    ```bash
    dotnet run
    ```

1. 範例專案會要求使用者輸入問題，並使用本地模型進行回答。

   運行中的演示類似於以下內容：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免責聲明**:  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文檔應被視為權威來源。對於關鍵信息，建議使用專業的人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。