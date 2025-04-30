<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76956c0c22e5686908a6d85ec72126af",
  "translation_date": "2025-04-04T17:13:59+00:00",
  "source_file": "code\\04.Finetuning\\olive-lab\\readme.md",
  "language_code": "hk"
}
-->
# 實驗室：優化 AI 模型以進行設備端推理

## 簡介

> [!IMPORTANT]
> 此實驗需要安裝 **Nvidia A10 或 A100 GPU**，並搭配相關驅動程式和 CUDA 工具包（版本 12+）。

> [!NOTE]
> 此實驗約需 **35 分鐘**，將帶您動手學習如何使用 OLIVE 優化模型以進行設備端推理的核心概念。

## 學習目標

完成此實驗後，您將能夠使用 OLIVE：

- 使用 AWQ 量化方法對 AI 模型進行量化。
- 對 AI 模型進行特定任務的微調。
- 生成 LoRA 適配器（微調模型），以便在 ONNX Runtime 上進行高效的設備端推理。

### Olive 是什麼？

Olive (*O*NNX *live*) 是一個模型優化工具包，配有 CLI，可幫助您為 ONNX Runtime +++https://onnxruntime.ai+++ 部署高品質和高效能的模型。

![Olive 流程](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.hk.png)

Olive 的輸入通常是 PyTorch 或 Hugging Face 模型，輸出則是經過優化的 ONNX 模型，該模型可在運行 ONNX Runtime 的設備（部署目標）上執行。Olive 將根據硬體供應商（如 Qualcomm、AMD、Nvidia 或 Intel）提供的 AI 加速器（NPU、GPU、CPU）來優化模型。

Olive 執行一個 *工作流程*，即一系列按順序排列的模型優化任務，稱為 *passes*——例如：模型壓縮、圖形捕捉、量化、圖形優化。每個 pass 都有一組參數，可調整以達到最佳的指標，例如準確度和延遲，並由相應的評估器進行評估。Olive 採用搜尋策略，利用搜尋演算法逐一或成組調整每個 pass。

#### Olive 的優勢

- **減少挫折和時間**，避免手動嘗試錯誤的實驗，使用不同的圖形優化、壓縮和量化技術。定義您的品質和效能約束，讓 Olive 自動為您尋找最佳模型。
- **超過 40 種內建模型優化元件**，涵蓋量化、壓縮、圖形優化和微調的尖端技術。
- **簡易使用的 CLI**，用於常見的模型優化任務，例如：olive quantize、olive auto-opt、olive finetune。
- 模型打包和部署內建。
- 支援生成 **多 LoRA 服務** 模型。
- 使用 YAML/JSON 構建工作流程，以協調模型優化和部署任務。
- 與 **Hugging Face** 和 **Azure AI** 整合。
- 內建 **快取機制**，以 **節省成本**。

## 實驗室指導

> [!NOTE]
> 請確保已按 Lab 1 的指導設定好您的 Azure AI Hub 和專案，並配置 A100 計算資源。

### 步驟 0：連接到 Azure AI 計算資源

您將使用 **VS Code** 的遠端功能連接到 Azure AI 計算資源。

1. 打開您的 **VS Code** 桌面應用程式：
2. 使用 **Shift+Ctrl+P** 打開 **命令面板**。
3. 在命令面板中搜尋 **AzureML - remote: Connect to compute instance in New Window**。
4. 按照螢幕上的指示連接到計算資源，這包括選擇您在 Lab 1 中設置的 Azure 訂閱、資源群組、專案和計算名稱。
5. 連接到 Azure ML 計算節點後，您可以在 **Visual Code 左下角** `><Azure ML: Compute Name` 中看到此連接。

### 步驟 1：克隆此倉庫

在 VS Code 中，您可以使用 **Ctrl+J** 打開新終端，並克隆此倉庫：

在終端中，您應該看到提示：

```
azureuser@computername:~/cloudfiles/code$ 
```
克隆解決方案：

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### 步驟 2：在 VS Code 中打開資料夾

要在 VS Code 中打開相關資料夾，請在終端中執行以下命令，這將打開新視窗：

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

或者，您也可以選擇 **文件** > **打開資料夾** 手動打開資料夾。

### 步驟 3：安裝依賴項

在 Azure AI 計算實例的 VS Code 中打開終端窗口（提示：**Ctrl+J**），並執行以下命令以安裝依賴項：

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> 安裝所有依賴項約需 **5 分鐘**。

在此實驗中，您將下載並上傳模型到 Azure AI 模型目錄。為了訪問模型目錄，您需要使用以下命令登錄 Azure：

```bash
az login
```

> [!NOTE]
> 登錄時，系統會要求您選擇訂閱。請確保選擇實驗提供的訂閱。

### 步驟 4：執行 Olive 命令

在 Azure AI 計算實例的 VS Code 中打開終端窗口（提示：**Ctrl+J**），並確保已啟動 `olive-ai` conda 環境：

```bash
conda activate olive-ai
```

接下來，在命令行中執行以下 Olive 命令：

1. **檢查數據：** 在此示例中，您將微調 Phi-3.5-Mini 模型，使其專注於回答旅行相關問題。以下代碼顯示數據集的前幾條記錄，這些記錄是 JSON lines 格式：

    ```bash
    head data/data_sample_travel.jsonl
    ```
2. **量化模型：** 在訓練模型之前，您首先使用名為 Active Aware Quantization (AWQ) 的技術進行量化 +++https://arxiv.org/abs/2306.00978+++。AWQ 根據推理過程中生成的激活值來量化模型權重，這意味著量化過程考慮了激活值中的實際數據分佈，與傳統權重量化方法相比，能更好地保留模型的準確性。

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    此過程約需 **8 分鐘**，可將模型大小從 **~7.5GB 減少到 ~2.5GB**。

    在此實驗中，我們向您展示如何從 Hugging Face 輸入模型（例如：`microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` 命令微調量化模型）。在微調之前進行量化，而不是之後，可以獲得更好的準確性，因為微調過程能恢復量化造成的部分損失。

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

3. **優化：** 訓練完成後，您可以使用 Olive 的 `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` 參數優化模型——但在此實驗中，我們將使用 CPU。

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

    優化過程約需 **5 分鐘**。

### 步驟 5：快速測試模型推理

要測試模型的推理，請在您的資料夾中創建一個名為 **app.py** 的 Python 文件，並將以下代碼複製並貼上：

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

使用以下命令執行代碼：

```bash
python app.py
```

### 步驟 6：上傳模型到 Azure AI

將模型上傳到 Azure AI 模型倉庫，可以讓模型與開發團隊的其他成員共享，並處理模型的版本控制。要上傳模型，請執行以下命令：

> [!NOTE]
> 更新 `{}` 中的 `resourceGroup` 和 Azure AI 專案名稱，並執行以下命令：

```
az ml workspace show
```

或者，您可以訪問 +++ai.azure.com+++，選擇 **管理中心** > **專案** > **概覽**。

更新 `{}` 占位符，填入您的資源群組名稱和 Azure AI 專案名稱。

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
接著，您可以在 https://ml.azure.com/model/list 查看您上傳的模型並進行部署。

**免責聲明**:  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋負責。