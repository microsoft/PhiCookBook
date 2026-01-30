## 歡迎使用 C# 的 Phi 實驗室

這裡有一系列實驗室示範如何在 .NET 環境中整合不同版本的強大 Phi 模型。

## 先決條件

在執行範例之前，請確保您已安裝以下項目：

**.NET 9：** 請確認您的電腦已安裝[最新版本的 .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)。

**（可選）Visual Studio 或 Visual Studio Code：** 您需要一個能執行 .NET 專案的 IDE 或程式碼編輯器。建議使用[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo)或[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)。

**使用 git** 從 [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) 本地克隆 Phi-3、Phi3.5 或 Phi-4 版本之一。

**下載 Phi-4 ONNX 模型** 到您的本機：

### 導航到存放模型的資料夾

```bash
cd c:\phi\models
```

### 新增 lfs 支援

```bash
git lfs install 
```

### 克隆並下載 Phi-4 mini instruct 模型和 Phi-4 多模態模型

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**下載 Phi-3 ONNX 模型** 到您的本機：

### 克隆並下載 Phi-3 mini 4K instruct 模型和 Phi-3 vision 128K 模型

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**重要提示：** 目前的示範設計是使用模型的 ONNX 版本。上述步驟會克隆以下模型。

## 關於實驗室

主解決方案包含多個示範實驗室，展示如何使用 C# 操作 Phi 模型的功能。

| 專案 | 模型 | 說明 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 或 Phi-3.5 | 範例主控台聊天，允許使用者提問。專案使用 `Microsoft.ML.OnnxRuntime` 函式庫載入本地 ONNX Phi-3 模型。 |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 或 Phi-3.5 | 範例主控台聊天，允許使用者提問。專案使用 `Microsoft.Semantic.Kernel` 函式庫載入本地 ONNX Phi-3 模型。 |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 或 Phi-3.5 | 範例專案，使用本地 phi3 視覺模型分析圖片。專案使用 `Microsoft.ML.OnnxRuntime` 函式庫載入本地 ONNX Phi-3 視覺模型。 |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 或 Phi-3.5 | 範例專案，使用本地 phi3 視覺模型分析圖片。專案使用 `Microsoft.ML.OnnxRuntime` 函式庫載入本地 ONNX Phi-3 視覺模型。專案同時提供一個選單，讓使用者進行互動。 | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | 範例主控台聊天，允許使用者提問。專案使用 `Microsoft.ML.OnnxRuntime` 函式庫載入本地 ONNX Phi-4 模型。 |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | 範例主控台聊天，允許使用者提問。專案使用 `Semantic Kernel` 函式庫載入本地 ONNX Phi-4 模型。 |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | 範例主控台聊天，允許使用者提問。專案使用 `Microsoft.ML.OnnxRuntimeGenAI` 函式庫載入本地 ONNX Phi-4 模型，並實作 `Microsoft.Extensions.AI` 的 `IChatClient`。 |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | 範例主控台聊天，允許使用者提問。聊天功能包含記憶體。 |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | 範例專案，使用本地 Phi-4 模型分析圖片並在主控台顯示結果。專案使用 `Microsoft.ML.OnnxRuntime` 函式庫載入本地 Phi-4-`multimodal-instruct-onnx` 模型。 |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | 範例專案，使用本地 Phi-4 模型分析音訊檔案，產生文字稿並在主控台顯示結果。專案使用 `Microsoft.ML.OnnxRuntime` 函式庫載入本地 Phi-4-`multimodal-instruct-onnx` 模型。 |

## 如何執行專案

執行專案請依照以下步驟：

1. 將儲存庫克隆到您的本機。

1. 開啟終端機並切換到想執行的專案資料夾。例如，我們執行 `LabsPhi4-Chat-01OnnxRuntime`。

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 使用以下指令執行專案

    ```bash
    dotnet run
    ```

1. 範例專案會要求使用者輸入，並使用本地模型回覆。

   執行中的示範類似以下畫面：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。