<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-08T05:23:57+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "tw"
}
-->
# Lab. 優化 AI 模型以利裝置端推論

## 介紹

> [!IMPORTANT]
> 本實驗室需要配備 **Nvidia A10 或 A100 GPU**，並安裝相應的驅動程式及 CUDA 工具包（版本 12 以上）。

> [!NOTE]
> 這是一個 **35 分鐘** 的實驗室，將帶你動手體驗使用 OLIVE 進行裝置端推論模型優化的核心概念。

## 學習目標

完成本實驗室後，你將能使用 OLIVE：

- 使用 AWQ 量化方法對 AI 模型進行量化。
- 針對特定任務微調 AI 模型。
- 產生 LoRA 適配器（微調後模型），以便在 ONNX Runtime 上進行高效的裝置端推論。

### 什麼是 Olive

Olive (*O*NNX *live*) 是一套模型優化工具包，搭配 CLI 使用，可讓你針對 ONNX runtime +++https://onnxruntime.ai+++ 部署模型，同時兼顧品質與效能。

![Olive Flow](../../../../../translated_images/olive-flow.5daf97340275f8b61397e91430ff02724a2547937b352e7fdfc2f669c56dcd35.tw.png)

Olive 的輸入通常是 PyTorch 或 Hugging Face 模型，輸出則是優化後的 ONNX 模型，會在執行 ONNX runtime 的裝置（部署目標）上運行。Olive 會根據硬體廠商（如 Qualcomm、AMD、Nvidia 或 Intel）提供的 AI 加速器（NPU、GPU、CPU）優化模型。

Olive 執行一個 *workflow*，也就是一連串有序的模型優化任務，稱為 *passes*，範例有模型壓縮、圖形擷取、量化、圖形優化等。每個 pass 都有一組可調整的參數，用以達成最佳指標，例如準確率和延遲，這些指標會由對應的評估器評估。Olive 採用搜尋策略，利用搜尋演算法自動調整每個 pass，或同時調整多個 passes。

#### Olive 的好處

- **減少挫折與時間浪費**，免去手動試錯不同圖形優化、壓縮和量化技術的繁瑣。設定你的品質和效能限制，讓 Olive 自動幫你找出最佳模型。
- **內建 40+ 個模型優化元件**，涵蓋量化、壓縮、圖形優化和微調的前沿技術。
- **易用的 CLI**，用於常見模型優化任務，例如 olive quantize、olive auto-opt、olive finetune。
- 內建模型封裝與部署功能。
- 支援產生 **多 LoRA 服務** 的模型。
- 使用 YAML/JSON 建構 workflow，協調模型優化與部署任務。
- 整合 **Hugging Face** 與 **Azure AI**。
- 內建 **快取** 機制，幫助 **節省成本**。

## 實驗室指引

> [!NOTE]
> 請確保你已建立 Azure AI Hub 與專案，並依照實驗室 1 設定好 A100 計算資源。

### 步驟 0：連接 Azure AI 計算資源

你將使用 **VS Code** 的遠端功能連接 Azure AI 計算資源。

1. 開啟你的 **VS Code** 桌面應用程式：
2. 使用 **Shift+Ctrl+P** 開啟 **指令面板**。
3. 在指令面板搜尋 **AzureML - remote: Connect to compute instance in New Window**。
4. 按照畫面指示操作，選擇你的 Azure 訂閱、資源群組、專案與你在實驗室 1 中設定的計算資源名稱。
5. 成功連線後，會在 **Visual Code 左下角** 顯示你的 Azure ML 計算節點 `><Azure ML: Compute Name`。

### 步驟 1：Clone 此 repo

在 VS Code 中，你可以按 **Ctrl+J** 開啟新終端機，並 clone 此 repo：

終端機會出現提示：

```
azureuser@computername:~/cloudfiles/code$ 
```  
Clone the solution  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### 步驟 2：在 VS Code 開啟資料夾

執行下列指令以在 VS Code 中開啟相關資料夾，會另開新視窗：

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

或者你也可以透過選單 **File** > **Open Folder** 開啟資料夾。

### 步驟 3：安裝相依套件

在 VS Code 的 Azure AI 計算節點中開啟終端機（提示：**Ctrl+J**），執行以下指令安裝相依套件：

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> 安裝所有相依套件約需 5 分鐘。

本實驗室會下載並上傳模型至 Azure AI 模型目錄。要存取模型目錄，你需要登入 Azure：

```bash
az login
```

> [!NOTE]
> 登入時會要求選擇訂閱，請確定選擇本實驗室提供的訂閱。

### 步驟 4：執行 Olive 指令

在 VS Code 的 Azure AI 計算節點中開啟終端機（提示：**Ctrl+J**），並確保已啟動 `olive-ai` conda 環境：

```bash
conda activate olive-ai
```

接著在命令列執行以下 Olive 指令。

1. **檢視資料：** 這個範例中，你將微調 Phi-3.5-Mini 模型，使其專精於回答旅遊相關問題。以下程式碼會顯示資料集前幾筆記錄，格式為 JSON lines：

    ```bash
    head data/data_sample_travel.jsonl
    ```

2. **量化模型：** 在訓練模型前，先使用 Active Aware Quantization (AWQ) 技術 +++https://arxiv.org/abs/2306.00978+++ 進行量化。AWQ 會考慮推論時產生的激活值，量化模型權重。這代表量化過程會根據激活的實際資料分布，較傳統權重量化能更好保留模型準確度。

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ 量化約需 **8 分鐘**，會將模型大小從約 7.5GB 降到約 2.5GB。

    在本實驗室示範如何從 Hugging Face 輸入模型（例如：`microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` 指令會微調量化後的模型。先量化再微調能取得較佳準確度，因為微調過程會回復部分量化造成的損失。

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    微調（100 步）約需 **6 分鐘**。

3. **優化：** 模型訓練完成後，使用 Olive 的 `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` 參數優化模型，不過本實驗室以 CPU 為例。

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    優化約需 **5 分鐘**。

### 步驟 5：模型推論快速測試

要測試模型推論，在資料夾中建立一個名為 **app.py** 的 Python 檔案，並貼上以下程式碼：

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

執行程式：

```bash
python app.py
```

### 步驟 6：上傳模型至 Azure AI

將模型上傳至 Azure AI 模型庫，可以與團隊成員共享，並管理模型版本。執行以下指令上傳模型：

> [!NOTE]
> 請更新 `{}` ` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group ` 中的 resourceGroup 與 Azure AI 專案名稱，然後執行以下指令：

```
az ml workspace show
```

或前往 +++ai.azure.com+++，選擇 **management center** > **project** > **overview**

請將 `{}` 佔位符更新為你的資源群組名稱與 Azure AI 專案名稱。

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

之後你就可以在 https://ml.azure.com/model/list 查看並部署你的模型。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤釋負責。