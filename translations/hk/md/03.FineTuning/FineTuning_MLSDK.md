<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:04:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "hk"
}
-->
## 如何使用來自 Azure ML 系統註冊表的 chat-completion 元件來微調模型

在此範例中，我們將對 Phi-3-mini-4k-instruct 模型進行微調，以使用 ultrachat_200k 資料集完成兩人對話。

![MLFineTune](../../../../translated_images/hk/MLFineTune.928d4c6b3767dd35.webp)

此範例將示範如何使用 Azure ML SDK 和 Python 進行微調，然後將微調後的模型部署到線上端點以進行即時推論。

### 訓練資料

我們將使用 ultrachat_200k 資料集。這是 UltraChat 資料集經過嚴格篩選的版本，曾用於訓練 Zephyr-7B-β，一款先進的 7B 聊天模型。

### 模型

我們將使用 Phi-3-mini-4k-instruct 模型，示範如何微調模型以完成 chat-completion 任務。如果你是從特定模型卡開啟此筆記本，請記得替換成該模型名稱。

### 任務

- 選擇要微調的模型。
- 選擇並探索訓練資料。
- 配置微調工作。
- 執行微調工作。
- 檢視訓練與評估指標。
- 註冊微調後的模型。
- 部署微調後的模型以進行即時推論。
- 清理資源。

## 1. 設定前置條件

- 安裝相依套件
- 連接到 AzureML Workspace。詳細說明請參考設定 SDK 認證。請替換下方的 <WORKSPACE_NAME>、<RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>。
- 連接到 azureml 系統註冊表
- 設定可選的實驗名稱
- 檢查或建立計算資源

> [!NOTE]
> 需求為單一 GPU 節點可包含多張 GPU 卡。例如，Standard_NC24rs_v3 節點有 4 張 NVIDIA V100 GPU，而 Standard_NC12s_v3 節點有 2 張 NVIDIA V100 GPU。相關資訊請參考文件。每節點 GPU 卡數量由下方參數 gpus_per_node 設定，正確設定可確保節點內所有 GPU 被充分利用。推薦的 GPU 計算 SKU 可參考此處與此處。

### Python 函式庫

請執行以下程式碼安裝相依套件。若在新環境執行，此步驟不可省略。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### 與 Azure ML 互動

1. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 服務互動，功能說明如下：

    - 從 azure.ai.ml、azure.identity 和 azure.ai.ml.entities 套件匯入必要模組，並匯入 time 模組。

    - 嘗試使用 DefaultAzureCredential() 進行認證，提供簡化的認證體驗以快速開發 Azure 雲端應用。若失敗，則改用 InteractiveBrowserCredential()，提供互動式登入提示。

    - 嘗試使用 from_config 方法建立 MLClient 實例，從預設設定檔 (config.json) 讀取設定。若失敗，則手動提供 subscription_id、resource_group_name 和 workspace_name 建立 MLClient。

    - 建立另一個 MLClient 實例，針對名為 "azureml" 的 Azure ML 註冊表。此註冊表用於存放模型、微調管線與環境。

    - 設定 experiment_name 為 "chat_completion_Phi-3-mini-4k-instruct"。

    - 產生唯一時間戳記，將當前時間（自 Epoch 起的秒數，浮點數）轉為整數再轉為字串。此時間戳可用於建立唯一名稱與版本。

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. 選擇基礎模型進行微調

1. Phi-3-mini-4k-instruct 是一款擁有 38 億參數的輕量級先進開放模型，基於 Phi-2 使用的資料集訓練。該模型屬於 Phi-3 系列，Mini 版本有兩種變體：4K 與 128K，分別代表可支援的上下文長度（以 token 計）。我們需要針對特定用途微調模型。你可以在 AzureML Studio 的模型目錄中瀏覽這些模型，並以 chat-completion 任務篩選。本範例使用 Phi-3-mini-4k-instruct 模型，若你是為其他模型開啟此筆記本，請相應替換模型名稱與版本。

    > [!NOTE]
    > 模型的 id 屬性會作為微調工作的輸入。此 id 也可在 AzureML Studio 模型目錄的模型詳細頁面中，作為資產 ID 欄位查看。

2. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 服務互動，功能說明如下：

    - 設定 model_name 為 "Phi-3-mini-4k-instruct"。

    - 使用 registry_ml_client 物件的 models 屬性中的 get 方法，從 Azure ML 註冊表取得指定名稱模型的最新版本。get 方法帶入兩個參數：模型名稱與標籤（指定取得最新版本）。

    - 在主控台列印訊息，顯示將用於微調的模型名稱、版本與 id。使用字串的 format 方法將模型的名稱、版本與 id 插入訊息中。這些屬性由 foundation_model 物件提供。

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. 建立用於工作的計算資源

微調工作僅支援 GPU 計算資源。計算資源大小取決於模型大小，通常較難判斷適合的計算資源。在此單元中，我們引導使用者選擇合適的計算資源。

> [!NOTE]
> 下方列出的計算資源皆為最佳化配置。若更改配置，可能導致 Cuda 記憶體不足錯誤。遇此情況，請嘗試升級至更大規模的計算資源。

> [!NOTE]
> 選擇 compute_cluster_size 時，請確認該計算資源在你的資源群組中可用。若無法使用，請申請取得計算資源存取權。

### 檢查模型是否支援微調計算資源

1. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 模型互動，功能說明如下：

    - 匯入 ast 模組，提供處理 Python 抽象語法樹的函式。

    - 檢查 foundation_model 物件（代表 Azure ML 中的模型）是否有名為 finetune_compute_allow_list 的標籤。Azure ML 中的標籤為鍵值對，可用於篩選與排序模型。

    - 若存在 finetune_compute_allow_list 標籤，使用 ast.literal_eval 函式安全地將標籤值（字串）解析為 Python 清單，並指派給 computes_allow_list 變數。接著列印訊息，提示應從該清單中建立計算資源。

    - 若不存在該標籤，將 computes_allow_list 設為 None，並列印訊息說明該標籤不在模型標籤中。

    - 總結，此腳本檢查模型元資料中特定標籤，若存在則轉換為清單，並提供使用者回饋。

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### 檢查計算資源實例

1. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 服務互動，並對計算資源實例進行多項檢查，功能說明如下：

    - 嘗試從 Azure ML 工作區取得名稱為 compute_cluster 的計算資源實例。若該實例的配置狀態為 "failed"，則拋出 ValueError。

    - 檢查 computes_allow_list 是否非 None。若是，將清單中所有計算資源大小轉為小寫，並檢查目前計算資源大小是否在清單中。若不在，拋出 ValueError。

    - 若 computes_allow_list 為 None，則檢查計算資源大小是否在不支援的 GPU VM 大小清單中。若是，拋出 ValueError。

    - 取得工作區中所有可用計算資源大小清單。遍歷清單，若名稱與目前計算資源大小相符，取得該計算資源的 GPU 數量，並將 gpu_count_found 設為 True。

    - 若 gpu_count_found 為 True，列印計算資源中 GPU 數量。若為 False，拋出 ValueError。

    - 總結，此腳本對 Azure ML 工作區中的計算資源實例進行多項檢查，包括配置狀態、大小是否符合允許清單或拒絕清單，以及 GPU 數量。

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. 選擇用於微調模型的資料集

1. 我們使用 ultrachat_200k 資料集。該資料集有四個分割，適合用於監督式微調 (sft)。
生成排序 (gen)。每個分割的範例數如下：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 接下來幾個單元示範微調的基本資料準備：

### 視覺化部分資料列

為了讓範例快速執行，我們將 train_sft、test_sft 檔案保存為已篩選資料的 5%。這表示微調後的模型準確度較低，因此不建議用於實際應用。
download-dataset.py 用於下載 ultrachat_200k 資料集，並將資料轉換為微調管線元件可用格式。由於資料集龐大，此處僅使用部分資料。

1. 執行以下腳本僅下載 5% 的資料。可透過調整 dataset_split_pc 參數來增加下載比例。

    > [!NOTE]
    > 部分語言模型使用不同語言代碼，因此資料集中的欄位名稱應相應調整。

1. 以下為資料範例格式
chat-completion 資料集以 parquet 格式儲存，每筆資料遵循以下結構：

    - 這是一份 JSON（JavaScript 物件表示法）文件，是一種流行的資料交換格式。它不是可執行程式碼，而是用於儲存與傳輸資料。結構說明如下：

    - "prompt"：此鍵對應字串，代表向 AI 助理提出的任務或問題。

    - "messages"：此鍵對應物件陣列。每個物件代表使用者與 AI 助理間的對話訊息。每則訊息物件包含兩個鍵：

    - "content"：字串，訊息內容。
    - "role"：字串，發送訊息的角色，可能為 "user" 或 "assistant"。
    - "prompt_id"：字串，該提示的唯一識別碼。

1. 在此 JSON 文件中，對話描述使用者請 AI 助理創作一位反烏托邦故事的主角。助理回應後，使用者要求更多細節，助理同意提供。整段對話關聯至特定 prompt id。

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### 下載資料

1. 此 Python 腳本用於透過輔助腳本 download-dataset.py 下載資料集，功能說明如下：

    - 匯入 os 模組，提供跨平台的作業系統功能。

    - 使用 os.system 函式在 shell 執行 download-dataset.py 腳本，並帶入特定命令列參數。參數指定下載資料集 HuggingFaceH4/ultrachat_200k，下載目錄為 ultrachat_200k_dataset，並設定資料分割比例為 5%。os.system 回傳執行狀態碼，存入 exit_status 變數。

    - 檢查 exit_status 是否不等於 0。在類 Unix 系統中，狀態碼 0 表示成功，其他數字表示錯誤。若非 0，拋出 Exception，提示下載資料集時發生錯誤。

    - 總結，此腳本執行下載指令，若失敗則拋出例外。

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### 將資料載入 DataFrame

1. 此 Python 腳本將 JSON Lines 格式檔案載入 pandas DataFrame，並顯示前 5 列，功能說明如下：

    - 匯入 pandas 函式庫，強大的資料操作與分析工具。

    - 設定 pandas 顯示選項中最大欄寬為 0，表示列印時不截斷欄位內容，完整顯示文字。

    - 使用 pd.read_json 函式載入 ultrachat_200k_dataset 目錄下的 train_sft.jsonl 檔案，lines=True 表示檔案為 JSON Lines 格式，每行為獨立 JSON 物件。
- 它使用 head 方法顯示 DataFrame 的前 5 行。如果 DataFrame 少於 5 行，則會顯示全部行。

- 總結來說，這個腳本是將 JSON Lines 檔案載入到 DataFrame，並顯示前 5 行的完整欄位文字。

```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. 使用模型和數據作為輸入提交微調任務

建立使用 chat-completion pipeline 元件的任務。了解更多關於微調支援的所有參數。

### 定義微調參數

1. 微調參數可分為兩大類別 - 訓練參數、優化參數

1. 訓練參數定義訓練相關的設定，例如 -

    - 使用的優化器、排程器
    - 用來優化微調的指標
    - 訓練步數、批次大小等等
    - 優化參數則有助於優化 GPU 記憶體使用及有效利用計算資源。

1. 以下是屬於此類別的一些參數。優化參數會因模型而異，並隨模型包裝以處理這些差異。

    - 啟用 deepspeed 和 LoRA
    - 啟用混合精度訓練
    - 啟用多節點訓練


> [!NOTE]
> 監督式微調可能導致對齊喪失或災難性遺忘。我們建議檢查此問題，並在微調後執行對齊階段。

### 微調參數

1. 這個 Python 腳本設定用於微調機器學習模型的參數。以下是它的說明：

    - 設定預設的訓練參數，如訓練週期數、訓練與評估的批次大小、學習率及學習率排程器類型。

    - 設定預設的優化參數，如是否啟用 Layer-wise Relevance Propagation (LoRa) 和 DeepSpeed，以及 DeepSpeed 階段。

    - 將訓練參數和優化參數合併成一個名為 finetune_parameters 的字典。

    - 檢查 foundation_model 是否有任何模型特定的預設參數。如果有，會印出警告訊息，並用 ast.literal_eval 將模型特定預設參數（字串格式）轉換成 Python 字典，然後更新 finetune_parameters。

    - 印出將用於執行的最終微調參數集。

    - 總結來說，這個腳本設定並顯示微調機器學習模型的參數，並可用模型特定參數覆蓋預設值。

```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### 訓練流程

1. 這個 Python 腳本定義一個函數用來產生機器學習訓練流程的顯示名稱，然後呼叫該函數產生並印出顯示名稱。以下是它的說明：

1. 定義 get_pipeline_display_name 函數。此函數根據與訓練流程相關的多個參數產生顯示名稱。

1. 函數內計算總批次大小，方法是將每裝置批次大小、梯度累積步數、每節點 GPU 數量及微調使用的節點數相乘。

1. 取得其他參數，如學習率排程器類型、是否啟用 DeepSpeed、DeepSpeed 階段、是否啟用 Layer-wise Relevance Propagation (LoRa)、保留的模型檢查點數量限制，以及最大序列長度。

1. 建構一個字串，包含所有這些參數，以連字號分隔。如果啟用 DeepSpeed 或 LoRa，字串會分別包含 "ds" 加上 DeepSpeed 階段，或 "lora"。若未啟用，則分別包含 "nods" 或 "nolora"。

1. 函數回傳此字串，作為訓練流程的顯示名稱。

1. 定義函數後，呼叫它產生顯示名稱，並印出。

1. 總結來說，這個腳本根據多個參數產生機器學習訓練流程的顯示名稱，並印出該名稱。

```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### 配置流程

這個 Python 腳本使用 Azure Machine Learning SDK 定義並配置機器學習流程。以下是它的說明：

1. 從 Azure AI ML SDK 匯入必要模組。

1. 從註冊表中取得名為 "chat_completion_pipeline" 的流程元件。

1. 使用 `@pipeline` 裝飾器和 `create_pipeline` 函數定義流程作業。流程名稱設定為 `pipeline_display_name`。

1. 在 `create_pipeline` 函數內，初始化取得的流程元件，並傳入多個參數，包括模型路徑、不同階段的計算叢集、訓練與測試的資料集切分、微調使用的 GPU 數量，以及其他微調參數。

1. 將微調任務的輸出映射到流程作業的輸出，方便後續註冊微調後的模型，這是部署模型到線上或批次端點所需。

1. 呼叫 `create_pipeline` 函數建立流程實例。

1. 將流程的 `force_rerun` 設定為 `True`，表示不使用先前任務的快取結果。

1. 將流程的 `continue_on_step_failure` 設定為 `False`，表示若任一步驟失敗，流程將停止。

1. 總結來說，這個腳本使用 Azure Machine Learning SDK 定義並配置一個用於聊天完成任務的機器學習流程。

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### 提交任務

1. 這個 Python 腳本將機器學習流程任務提交到 Azure Machine Learning 工作區，並等待任務完成。以下是它的說明：

    - 呼叫 workspace_ml_client 中 jobs 物件的 create_or_update 方法提交流程任務。要執行的流程由 pipeline_object 指定，任務所屬實驗由 experiment_name 指定。

    - 接著呼叫 workspace_ml_client 中 jobs 物件的 stream 方法，等待流程任務完成。等待的任務由 pipeline_job 物件的 name 屬性指定。

    - 總結來說，這個腳本將機器學習流程任務提交到 Azure Machine Learning 工作區，並等待任務完成。

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. 在工作區註冊微調後的模型

我們將從微調任務的輸出中註冊模型。這會追蹤微調模型與微調任務之間的血緣關係。微調任務則進一步追蹤基礎模型、數據和訓練程式碼的血緣。

### 註冊機器學習模型

1. 這個 Python 腳本註冊在 Azure Machine Learning 流程中訓練的機器學習模型。以下是它的說明：

    - 從 Azure AI ML SDK 匯入必要模組。

    - 透過呼叫 workspace_ml_client 中 jobs 物件的 get 方法並存取 outputs 屬性，檢查 pipeline 任務是否有 trained_model 輸出。

    - 建立訓練後模型的路徑，格式為 pipeline 任務名稱加上輸出名稱 ("trained_model")。

    - 定義微調模型的名稱，方法是在原始模型名稱後加上 "-ultrachat-200k"，並將斜線替換為連字號。

    - 準備註冊模型，建立 Model 物件，包含模型路徑、模型類型（MLflow 模型）、模型名稱與版本，以及模型描述。

    - 呼叫 workspace_ml_client 中 models 物件的 create_or_update 方法，並傳入 Model 物件以註冊模型。

    - 印出已註冊的模型。

1. 總結來說，這個腳本註冊在 Azure Machine Learning 流程中訓練的機器學習模型。

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. 將微調後的模型部署到線上端點

線上端點提供持久的 REST API，可用於整合需要使用模型的應用程式。

### 管理端點

1. 這個 Python 腳本在 Azure Machine Learning 中為已註冊模型建立受管線上端點。以下是它的說明：

    - 從 Azure AI ML SDK 匯入必要模組。

    - 定義線上端點的唯一名稱，方法是在字串 "ultrachat-completion-" 後加上時間戳。

    - 準備建立線上端點，建立 ManagedOnlineEndpoint 物件，包含端點名稱、描述及驗證模式（"key"）。

    - 呼叫 workspace_ml_client 的 begin_create_or_update 方法，傳入 ManagedOnlineEndpoint 物件建立端點，並呼叫 wait 方法等待建立完成。

1. 總結來說，這個腳本在 Azure Machine Learning 中為已註冊模型建立受管線上端點。

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> 你可以在此找到支援部署的 SKU 清單 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署機器學習模型

1. 這個 Python 腳本將已註冊的機器學習模型部署到 Azure Machine Learning 的受管線上端點。以下是它的說明：

    - 匯入 ast 模組，提供處理 Python 抽象語法樹的函式。

    - 將部署的實例類型設定為 "Standard_NC6s_v3"。

    - 檢查 foundation_model 是否有 inference_compute_allow_list 標籤。如果有，將標籤值從字串轉換為 Python 清單，並指派給 inference_computes_allow_list；若無，則設為 None。

    - 檢查指定的實例類型是否在允許清單中。如果不在，印出訊息請使用者從允許清單中選擇實例類型。

    - 準備建立部署，建立 ManagedOnlineDeployment 物件，包含部署名稱、端點名稱、模型 ID、實例類型與數量、活躍度探測設定及請求設定。

    - 呼叫 workspace_ml_client 的 begin_create_or_update 方法，傳入 ManagedOnlineDeployment 物件建立部署，並呼叫 wait 方法等待完成。

    - 將端點流量設定為將 100% 流量導向 "demo" 部署。

    - 呼叫 workspace_ml_client 的 begin_create_or_update 方法更新端點，並呼叫 result 方法等待更新完成。

1. 總結來說，這個腳本將已註冊的機器學習模型部署到 Azure Machine Learning 的受管線上端點。

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. 使用範例資料測試端點

我們將從測試資料集中擷取一些範例資料，並提交到線上端點進行推論。接著會顯示預測標籤與真實標籤。

### 讀取結果

1. 這個 Python 腳本將 JSON Lines 檔案讀入 pandas DataFrame，隨機抽樣，並重設索引。以下是它的說明：

    - 使用 read_json 函式讀取檔案 ./ultrachat_200k_dataset/test_gen.jsonl，並設定 lines=True，因為檔案為 JSON Lines 格式，每行為一個獨立 JSON 物件。

    - 從 DataFrame 中隨機抽取 1 筆資料，使用 sample 函式並設定 n=1。

    - 重設 DataFrame 的索引，使用 reset_index 函式並設定 drop=True，捨棄原索引並以預設整數索引取代。

    - 使用 head 函式顯示 DataFrame 的前 2 行，但因抽樣後只有 1 行，實際只會顯示該行。

1. 總結來說，這個腳本將 JSON Lines 檔案讀入 pandas DataFrame，隨機抽取 1 筆資料，重設索引，並顯示該筆資料。

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### 建立 JSON 物件

1. 這個 Python 腳本建立一個包含特定參數的 JSON 物件，並將其儲存到檔案。以下是它的說明：

    - 匯入 json 模組，提供處理 JSON 資料的函式。

    - 建立一個字典 parameters，包含機器學習模型的參數，鍵為 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，對應值分別為 0.6、0.9、True 和 200。

    - 建立另一個字典 test_json，包含兩個鍵："input_data" 和 "params"。其中 "input_data" 的值是另一個字典，包含鍵 "input_string" 和 "parameters"。 "input_string" 的值是一個列表，裡面包含 test_df DataFrame 的第一則訊息。 "parameters" 的值是先前建立的 parameters 字典。 "params" 的值為空字典。
- 它會打開一個名為 sample_score.json 的檔案

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### 調用 Endpoint

1. 這個 Python 腳本會調用 Azure Machine Learning 中的線上 Endpoint 來對 JSON 檔案進行評分。以下是它的操作說明：

    - 它呼叫 workspace_ml_client 物件中 online_endpoints 屬性的 invoke 方法。此方法用於向線上 Endpoint 發送請求並取得回應。

    - 它透過 endpoint_name 和 deployment_name 參數指定 Endpoint 名稱和部署名稱。這裡 Endpoint 名稱存放在 online_endpoint_name 變數中，部署名稱為 "demo"。

    - 它透過 request_file 參數指定要評分的 JSON 檔案路徑。這裡的檔案是 ./ultrachat_200k_dataset/sample_score.json。

    - 它將 Endpoint 回應存放在 response 變數中。

    - 它會印出原始回應。

1. 總結來說，這個腳本會調用 Azure Machine Learning 的線上 Endpoint 來評分 JSON 檔案，並印出回應。

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. 刪除線上 Endpoint

1. 別忘了刪除線上 Endpoint，否則會持續計費 Endpoint 使用的運算資源。這行 Python 程式碼會刪除 Azure Machine Learning 中的線上 Endpoint。以下是它的操作說明：

    - 它呼叫 workspace_ml_client 物件中 online_endpoints 屬性的 begin_delete 方法。此方法用於開始刪除線上 Endpoint。

    - 它透過 name 參數指定要刪除的 Endpoint 名稱。這裡 Endpoint 名稱存放在 online_endpoint_name 變數中。

    - 它呼叫 wait 方法等待刪除操作完成。這是一個阻塞操作，會阻止腳本繼續執行直到刪除完成。

    - 總結來說，這行程式碼會開始刪除 Azure Machine Learning 中的線上 Endpoint，並等待操作完成。

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。