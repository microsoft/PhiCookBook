## 如何使用來自 Azure ML 系統註冊表的 chat-completion 元件進行模型微調

在此範例中，我們將對 Phi-3-mini-4k-instruct 模型進行微調，以使用 ultrachat_200k 資料集完成兩人對話。

![MLFineTune](../../../../translated_images/zh-MO/MLFineTune.928d4c6b3767dd35.webp)

此範例將示範如何使用 Azure ML SDK 和 Python 進行微調，然後將微調後的模型部署至線上端點以進行即時推論。

### 訓練資料

我們將使用 ultrachat_200k 資料集。這是 UltraChat 資料集的高度篩選版本，並用於訓練 Zephyr-7B-β，一個最先進的 7b 聊天模型。

### 模型

我們將使用 Phi-3-mini-4k-instruct 模型示範如何為 chat-completion 任務進行模型微調。如果您是從特定模型卡中打開此筆記本，請記得替換特定模型名稱。

### 任務

- 選擇要微調的模型。
- 選擇並探索訓練資料。
- 配置微調工作。
- 執行微調工作。
- 檢視訓練和評估指標。
- 註冊微調後的模型。
- 部署微調後的模型進行即時推論。
- 清理資源。

## 1. 設置前置條件

- 安裝相依性套件
- 連接到 AzureML 工作區。了解更多請參閱設置 SDK 驗證。替換下方的 <WORKSPACE_NAME>、<RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>。
- 連接到 azureml 系統註冊表
- 設定可選的實驗名稱
- 檢查或建立計算資源。

> [!NOTE]
> 需求是一個 GPU 節點可以擁有多個 GPU 卡。例如，Standard_NC24rs_v3 節點中有 4 個 NVIDIA V100 GPU，而 Standard_NC12s_v3 節點中有 2 個 NVIDIA V100 GPU。有關此資訊請參考說明文件。每節點的 GPU 數量參數設定在以下的 gpus_per_node。正確設定此值可以確保節點內所有 GPU 的利用。推薦使用的 GPU 計算 SKU 可參考此處和此處。

### Python 函式庫

透過執行以下程式碼區塊安裝相依性。如果是在新環境中執行，這是不可或缺的步驟。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### 與 Azure ML 互動

1. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 服務互動。以下為功能說明：

    - 匯入 azure.ai.ml、azure.identity 和 azure.ai.ml.entities 套件中的必要模組，同時匯入 time 模組。

    - 嘗試使用 DefaultAzureCredential() 進行驗證，該方法提供簡化的驗證體驗以快速開始開發於 Azure 雲端運行的應用程式。若失敗，則回退到 InteractiveBrowserCredential()，提供互動式登入提示。

    - 隨後嘗試使用 from_config 方法建立 MLClient 實例，該方法會從預設的設定檔（config.json）中讀取設定。若失敗，則手動提供 subscription_id、resource_group_name 和 workspace_name 建立 MLClient 實例。

    - 建立另一個 MLClient 實例，針對 Azure ML 註冊表名稱 "azureml"。該註冊表用於存放模型、微調管線以及環境。

    - 設定 experiment_name 為 "chat_completion_Phi-3-mini-4k-instruct"。

    - 產生唯一的時間戳記，方法是將目前時間（以自 Epoch 起的秒數表示，浮點數）轉為整數，然後轉為字串。此時間戳可用於創建唯一名稱及版本。

    ```python
    # 從 Azure ML 與 Azure Identity 匯入必要的模組
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # 匯入時間模組
    
    # 嘗試使用 DefaultAzureCredential 進行身份驗證
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # 如果 DefaultAzureCredential 失敗，則使用 InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # 嘗試使用預設設定檔建立 MLClient 實例
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # 如果失敗，則手動提供詳細資訊建立 MLClient 實例
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # 為名為 "azureml" 的 Azure ML 註冊表建立另一個 MLClient 實例
    # 該註冊表用於存放模型、微調管道和環境
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # 設定實驗名稱
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # 生成一個唯 timestamp，可用於需要唯一性的名稱和版本
    timestamp = str(int(time.time()))
    ```

## 2. 選擇要微調的基礎模型

1. Phi-3-mini-4k-instruct 為一個擁有 3.8B 參數的輕量且最先進的開放模型，建構於用於 Phi-2 的資料集上。該模型屬於 Phi-3 模型家族，Mini 版本有兩種變體：4K 和 128K，分別代表可支援的上下文長度（以詞元計）。我們需要對模型進行微調以符合特定應用。您可以在 AzureML Studio 的模型目錄中瀏覽這些模型，並透過 chat-completion 任務進行篩選。此範例使用 Phi-3-mini-4k-instruct 模型。如果您是為其他模型打開本筆記本，請相應替換模型名稱及版本。

> [!NOTE]
> 模型的 model id 屬性會傳遞為微調工作的輸入。該 id 亦可在 AzureML Studio 模型目錄的模型詳情頁面中找到資產 ID 欄位。

2. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 服務互動。以下為功能說明：

    - 設定 model_name 為 "Phi-3-mini-4k-instruct"。

    - 透過 registry_ml_client 物件的 models 屬性之 get 方法，從 Azure ML 註冊表取得指定名稱模型的最新版本。該 get 方法接收兩個參數：模型名稱及標籤，標示要取得最新版本。

    - 在主控台輸出將用於微調的模型名稱、版本及 id。透過字串的 format 方法，將這些屬性置入訊息中。名稱、版本及 id 來自 foundation_model 物件的屬性。

    ```python
    # 設定模型名稱
    model_name = "Phi-3-mini-4k-instruct"
    
    # 從 Azure ML 註冊表取得模型的最新版本
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # 列印模型名稱、版本及 ID
    # 此資訊對追蹤及除錯很有用
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. 建立微調工作所需計算資源

微調作業只能在 GPU 計算資源上執行。計算資源的大小依模型大小而定，通常較難判斷合適的計算資源。在此單元格中，我們將引導使用者選擇合適的計算資源。

> [!NOTE]
> 以下列出的計算資源均已針對最佳配置優化。任何配置更改可能導致 Cuda 記憶體不足錯誤。遇此情況，請嘗試升級至更大規模的計算資源。

> [!NOTE]
> 選擇下方的 compute_cluster_size 時，請確保該計算資源在您的資源群組中可用。若某計算資源不可用，您可申請取得該計算資源的存取權。

### 檢查模型是否支援微調

1. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 模型互動。以下為功能說明：

    - 匯入 ast 模組，提供處理 Python 抽象語法樹的功能。

    - 檢查 foundation_model 物件（代表 Azure ML 中的模型）是否有名為 finetune_compute_allow_list 的標籤。Azure ML 中標籤為鍵值對，可用於過濾和排序模型。

    - 若存在 finetune_compute_allow_list 標籤，使用 ast.literal_eval 函數安全地將標籤值（字串）解析為 Python 列表，並將其賦值給 computes_allow_list。並提示必須從此列表建立計算資源。

    - 若不存在該標籤，則將 computes_allow_list 設為 None，並提示該標籤不在模型標籤中。

    - 總結，此腳本檢查模型元資料中是否有特定標籤，若有則將其值轉換為列表，並提供相應訊息。

    ```python
    # 匯入 ast 模組，該模組提供處理 Python 抽象語法樹的函數
    import ast
    
    # 檢查模型的標籤中是否存在 'finetune_compute_allow_list' 標籤
    if "finetune_compute_allow_list" in foundation_model.tags:
        # 如果標籤存在，使用 ast.literal_eval 安全地將標籤的值（字串）解析為 Python 清單
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # 將字串轉換為 Python 清單
        # 輸出訊息表示應該從該清單創建一個 compute
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # 如果標籤不存在，將 computes_allow_list 設為 None
        computes_allow_list = None
        # 輸出訊息表示 'finetune_compute_allow_list' 標籤不在模型的標籤中
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### 檢查計算實例

1. 此 Python 腳本用於與 Azure Machine Learning (Azure ML) 服務互動，並對計算實例執行多項檢查。以下為功能說明：

    - 嘗試從 Azure ML 工作區中取得名為 compute_cluster 的計算實例。若該計算實例的佈建狀態為「failed」，則拋出 ValueError。

    - 若 computes_allow_list 不為 None，則將其內的所有計算大小轉為小寫，並檢查目前計算實例大小是否在清單中。若不在其中，則拋出 ValueError。

    - 若 computes_allow_list 為 None，則檢查此計算實例大小是否在不支援的 GPU VM 尺寸清單中。若是，則拋出 ValueError。

    - 取得工作區內所有可用的計算大小清單，遍歷該清單，並比對其名稱是否與目前計算實例大小相符。若相符，取得該計算大小的 GPU 數量，並設定 gpu_count_found 為 True。

    - 若 gpu_count_found 為 True，輸出計算實例中 GPU 數量；若為 False，則拋出 ValueError。

    - 總結，本腳本執行多項對計算實例的檢查，包括佈建狀態、是否在允許清單或拒絕清單中，以及 GPU 數量。

    ```python
    # 列印異常訊息
    print(e)
    # 如果工作區內沒有可用的計算大小，則引發 ValueError
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # 從 Azure ML 工作區檢索計算實例
    compute = workspace_ml_client.compute.get(compute_cluster)
    # 檢查計算實例的佈建狀態是否為「失敗」
    if compute.provisioning_state.lower() == "failed":
        # 如果佈建狀態為「失敗」，則引發 ValueError
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # 檢查 computes_allow_list 是否不為 None
    if computes_allow_list is not None:
        # 將 computes_allow_list 中所有的計算大小轉換為小寫
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # 檢查計算實例的大小是否在 computes_allow_list_lower_case 中
        if compute.size.lower() not in computes_allow_list_lower_case:
            # 如果計算實例的大小不在 computes_allow_list_lower_case 中，則引發 ValueError
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # 定義一個不支援的 GPU VM 大小列表
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # 檢查計算實例的大小是否在 unsupported_gpu_vm_list 中
        if compute.size.lower() in unsupported_gpu_vm_list:
            # 如果計算實例的大小在 unsupported_gpu_vm_list 中，則引發 ValueError
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # 初始化一個標誌以檢查是否已找到計算實例中的 GPU 數量
    gpu_count_found = False
    # 檢索工作區中所有可用的計算大小列表
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # 對可用的計算大小列表進行迭代
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # 檢查計算大小的名稱是否與計算實例的大小匹配
        if compute_sku.name.lower() == compute.size.lower():
            # 若匹配，檢索該計算大小的 GPU 數量並將 gpu_count_found 設為 True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # 如果 gpu_count_found 為 True，列印計算實例中的 GPU 數量
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # 如果 gpu_count_found 為 False，則引發 ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. 選擇用於微調模型的資料集

1. 我們使用 ultrachat_200k 資料集。該資料集分為四個子集，適合進行監督式微調（sft）。
生成排名（gen）。每個子集的範例數如下所示：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 接下來的幾個單元格示範微調的基本資料準備：

### 視覺化一些資料列

為使此示例能快速執行，我們將存儲 train_sft 與 test_sft 檔案，包含已修剪資料的 5%。這表示微調後的模型準確度較低，不宜用於實際應用。
download-dataset.py 用來下載 ultrachat_200k 資料集並將其轉換為微調管線元件可用的格式。由於資料集龐大，此處僅使用部分資料。

1. 執行以下指令只會下載 5% 的資料。可藉由更改 dataset_split_pc 參數為所需百分比來增加下載量。

> [!NOTE]
> 部分語言模型語系代碼不同，資料集中欄位名稱應相對應。

1. 以下為資料應呈現的範例
chat-completion 資料集以 parquet 格式儲存，每個條目遵循下列結構：

    - 此為 JSON (JavaScript 物件符號) 文件，是一種流行的資料交換格式。它非可執行程式碼，而是用來存儲和傳輸資料。其架構說明如下：

    - "prompt"：該鍵保存一個字串，代表交給 AI 助手的任務或問題。

    - "messages"：該鍵保存一個物件陣列。每個物件代表用戶和 AI 助手間的對話訊息。每個訊息物件有兩個鍵：

    - "content"：該鍵保存訊息內容字串。
    - "role"：該鍵保存發送該訊息實體的角色字串，可能是 "user" 或 "assistant"。
    - "prompt_id"：該鍵保存提示的唯一識別碼字串。

1. 在此 JSON 文件中，展示了一段對話：用戶請 AI 助手為反烏托邦故事創作主角，助手回應後，用戶要求更多細節，助手同意提供。整個對話附屬於特定 prompt_id。

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

1. 此 Python 腳本用於透過輔助腳本 download-dataset.py 下載資料集。以下為功能說明：

    - 匯入 os 模組，提供操作作業系統功能的跨平台方法。

    - 使用 os.system 函數在 shell 中執行 download-dataset.py 腳本，附帶特定命令列參數。參數指定下載資料集 HuggingFaceH4/ultrachat_200k，下載目錄為 ultrachat_200k_dataset，並將資料集分割為 5%。os.system 會回傳所執行指令的退出狀態碼，儲存於 exit_status 變數。

    - 檢查 exit_status 是否非 0。於類 Unix 作業系統中，狀態碼 0 通常代表指令成功完成，其他數字表示錯誤。若 exit_status 非 0，拋出 Exception，並提示下載資料集發生錯誤。

    - 總結，此腳本透過執行命令下載資料集，若失敗則拋出例外。

    ```python
    # 匯入 os 模組，提供使用作業系統相關功能的方法
    import os
    
    # 使用 os.system 函式在 shell 中執行 download-dataset.py 腳本，並帶入特定的命令行參數
    # 參數指定要下載的數據集（HuggingFaceH4/ultrachat_200k）、下載目錄（ultrachat_200k_dataset）以及分割數據集的百分比（5）
    # os.system 函式會返回其執行的命令的退出狀態；該狀態被存入 exit_status 變數
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # 檢查 exit_status 是否不等於 0
    # 在類 Unix 的作業系統中，退出狀態為 0 通常表示命令成功執行，其他數字表示錯誤
    # 如果 exit_status 不等於 0，則拋出一個異常，並顯示下載數據集時發生錯誤的訊息
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### 載入資料至 DataFrame

1. 此 Python 腳本用於將 JSON Lines 格式檔案載入 pandas DataFrame 並顯示前 5 筆資料。以下為功能說明：

    - 匯入 pandas 函式庫，一個功能強大的資料操作與分析函式庫。

    - 設定 pandas 顯示選項中欄位最大寬度為 0，表示列印 DataFrame 時完整顯示每欄資料，不進行截斷。
- 它使用 pd.read_json 函數從 ultrachat_200k_dataset 目錄載入 train_sft.jsonl 文件到 DataFrame。lines=True 參數表示該文件是 JSON Lines 格式，每行是一個獨立的 JSON 物件。

- 它使用 head 方法顯示 DataFrame 的前 5 行。如果 DataFrame 少於 5 行，則會顯示全部行。

- 總結而言，這個腳本將 JSON Lines 文件載入到 DataFrame 並顯示前 5 行的完整欄位文本。

    ```python
    # 導入 pandas 函式庫，一個強大的數據操作和分析函式庫
    import pandas as pd
    
    # 將 pandas 顯示選項的最大欄寬設置為 0
    # 這表示列印 DataFrame 時會完整顯示每一欄的文字而不會截斷
    pd.set_option("display.max_colwidth", 0)
    
    # 使用 pd.read_json 函數從 ultrachat_200k_dataset 目錄載入 train_sft.jsonl 檔案到 DataFrame
    # lines=True 參數表示該檔案為 JSON Lines 格式，每一行都是一個獨立的 JSON 物件
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # 使用 head 方法顯示 DataFrame 的前 5 行
    # 如果 DataFrame 的行數少於 5，則會顯示全部行數
    df.head()
    ```

## 5. 使用模型和數據作為輸入提交微調任務

建立使用 chat-completion pipeline 元件的作業。進一步了解所有支持的微調參數。

### 定義微調參數

1. 微調參數可分為兩類 - 訓練參數、優化參數

1. 訓練參數定義訓練的各個方面，例如 -

    - 使用的優化器、排程器
    - 用於優化微調的指標
    - 訓練步數、批次大小等等
    - 優化參數有助於優化 GPU 記憶體並有效使用計算資源。

1. 以下是屬於此類別的一些參數。優化參數因模型而異，並與模型一起封裝以處理這些變化。

    - 啟用 deepspeed 和 LoRA
    - 啟用混合精度訓練
    - 啟用多節點訓練

> [!NOTE]
> 監督式微調可能導致對齊丟失或災難性遺忘。我們建議檢查此問題並在微調後執行對齊階段。

### 微調參數

1. 這個 Python 腳本設置了微調機器學習模型的參數。以下是它的解析：

    - 它設定預設的訓練參數，如訓練週期數、訓練和評估的批次大小、學習率及學習率排程器類型。

    - 它設定預設的優化參數，如是否應用層次相關性傳播（LoRa）和 DeepSpeed 以及 DeepSpeed 階段。

    - 它將訓練和優化參數合併到一個名為 finetune_parameters 的字典中。

    - 它檢查 foundation_model 是否有任何模型特定的預設參數。如果有，則打印警告訊息並用 ast.literal_eval 函數將模型專屬預設的字串轉換為 Python 字典，更新 finetune_parameters 字典。

    - 它打印最終用於執行的微調參數集。

    - 總結而言，這個腳本設置並顯示微調機器學習模型的參數，且能用模型特定參數覆蓋預設設定。

    ```python
    # 設置預設訓練參數，例如訓練周期數、訓練和評估的批次大小、學習率以及學習率調度器類型
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # 設置預設優化參數，例如是否使用層相關性傳播（LoRa）及 DeepSpeed，及 DeepSpeed 階段
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # 將訓練和優化參數合併到名為 finetune_parameters 的字典中
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # 檢查 foundation_model 是否有任何模型特定的預設參數
    # 如果有，打印警告訊息並使用這些模型特定的預設值更新 finetune_parameters 字典
    # ast.literal_eval 函數用於將模型特定的預設值從字串轉換為 Python 字典
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # 將字串轉換為 python 字典
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # 列印將用於執行的最終微調參數集
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### 訓練流水線

1. 這個 Python 腳本定義了一個函數以產生機器學習訓練流水線的顯示名稱，並呼叫該函數生成並打印顯示名稱。以下是解析：

1. 定義了 get_pipeline_display_name 函數，該函數根據訓練流水線的各種參數生成顯示名稱。

1. 在函數中，計算了總批次大小，為每設備批次大小乘以梯度累積步數、每節點 GPU 數和微調節點數。

1. 它檢索其他參數，如學習率排程器類型、是否應用 DeepSpeed、DeepSpeed 階段、是否應用層次相關性傳播（LoRa）、模型檢查點保存數量限制以及最大序列長度。

1. 它構造一個包含這些參數的字串，並用連字號分隔。如果有應用 DeepSpeed 或 LoRa，則字串分別包含 "ds" 後跟 DeepSpeed 階段，或 "lora"。否則，分別包含 "nods" 或 "nolora"。

1. 函數返回字串，此字串作為訓練流水線的顯示名稱。

1. 函數定義完成後被呼叫生成顯示名稱，並打印該名稱。

1. 總結而言，這個腳本根據多個參數生成機器學習訓練流水線的顯示名稱，並打印出該名稱。

    ```python
    # 定義一個函數以產生訓練流程的顯示名稱
    def get_pipeline_display_name():
        # 通過將每個裝置的批次大小、梯度累積步驟數、每個節點的 GPU 數量，以及用於微調的節點數相乘來計算總批次大小
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # 取得學習率調度器的類型
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # 取得是否應用 DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # 取得 DeepSpeed 階段
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # 如果應用 DeepSpeed，於顯示名稱中包含 "ds" 並跟隨 DeepSpeed 階段；如果沒有，則包含 "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # 取得是否應用分層相關傳遞（Layer-wise Relevance Propagation, LoRa）
        lora = finetune_parameters.get("apply_lora", "false")
        # 如果應用 LoRa，則於顯示名稱中包含 "lora"；如果沒有，則包含 "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # 取得所保留的模型檢查點數量限制
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # 取得最大序列長度
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # 通過連接所有這些參數並以連字號分隔，構造顯示名稱
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
    
    # 呼叫函數以產生顯示名稱
    pipeline_display_name = get_pipeline_display_name()
    # 輸出顯示名稱
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### 配置流水線

這個 Python 腳本使用 Azure Machine Learning SDK 定義和配置機器學習流水線。以下是它的解析：

1. 從 Azure AI ML SDK 匯入必要的模組。

1. 從註冊中心抓取名為 "chat_completion_pipeline" 的流水線元件。

1. 使用 `@pipeline` 裝飾器和函數 `create_pipeline` 定義流水線作業。流水線名稱設定為 `pipeline_display_name`。

1. 在 `create_pipeline` 函數中，初始化抓取到的流水線元件，並設定各種參數，包括模型路徑、不同階段的運算集群、訓練和測試的資料集切分、微調使用的 GPU 數量及其他微調參數。

1. 將微調作業的輸出映射到流水線作業的輸出，方便註冊微調後的模型，這是部署模型到線上或批次端點所需。

1. 呼叫 `create_pipeline` 函數建立流水線實例。

1. 設置流水線的 `force_rerun` 為 `True`，意即不使用先前作業的快取結果。

1. 設置流水線的 `continue_on_step_failure` 為 `False`，意即若有任何步驟失敗即停止流水線。

1. 總結而言，這個腳本使用 Azure Machine Learning SDK 定義並配置適用於聊天補全任務的機器學習流水線。

    ```python
    # 從 Azure AI ML SDK 匯入必要的模組
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # 從註冊中心獲取名為 "chat_completion_pipeline" 的管道元件
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # 使用 @pipeline 裝飾器和 create_pipeline 函數定義管道作業
    # 管道的名稱設為 pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # 使用各種參數初始化獲取的管道元件
        # 包括模型路徑、不同階段的計算集群、用於訓練和測試的數據集分割、微調所用的 GPU 數量及其他微調參數
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # 將數據集分割映射到參數
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # 訓練設置
            number_of_gpu_to_use_finetuning=gpus_per_node,  # 設為計算資源中可用的 GPU 數量
            **finetune_parameters
        )
        return {
            # 將微調作業的輸出映射到管道作業的輸出
            # 如此一來我們可以輕鬆註冊微調後的模型
            # 註冊模型是部署到線上或批次端點所必需的
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # 呼叫 create_pipeline 函數創建管道實例
    pipeline_object = create_pipeline()
    
    # 不使用之前作業的快取結果
    pipeline_object.settings.force_rerun = True
    
    # 將步驟失敗時繼續執行設定為 False
    # 表示若任何步驟失敗，管道將停止執行
    pipeline_object.settings.continue_on_step_failure = False
    ```

### 提交作業

1. 這個 Python 腳本將機器學習流水線作業提交至 Azure Machine Learning 工作區，並等待作業完成。以下是解析：

    - 呼叫 workspace_ml_client 的 jobs 物件的 create_or_update 方法提交流水線作業。指定要執行的流水線為 pipeline_object，作業所屬實驗名稱為 experiment_name。

    - 呼叫 workspace_ml_client 的 jobs 物件的 stream 方法等待流水線作業完成。需等待的作業由 pipeline_job 物件的 name 屬性指定。

    - 總結而言，該腳本將機器學習流水線作業提交至 Azure Machine Learning 工作區，並等待作業完成。

    ```python
    # 將管道作業提交到 Azure 機器學習工作區
    # 要運行的管道由 pipeline_object 指定
    # 運行該作業的實驗由 experiment_name 指定
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # 等待管道作業完成
    # 要等待的作業由 pipeline_job 物件的 name 屬性指定
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. 在工作區註冊微調後的模型

我們將從微調任務的輸出中註冊模型。這將追蹤微調模型與微調任務之間的血緣關係。微調任務進一步追蹤到基礎模型、數據和訓練代碼的血緣。

### 註冊 ML 模型

1. 這個 Python 腳本註冊在 Azure Machine Learning 流水線中訓練的機器學習模型。以下是解析：

    - 從 Azure AI ML SDK 匯入必要模組。

    - 呼叫 workspace_ml_client 的 jobs 物件的 get 方法取得流水線作業，並訪問其 outputs 屬性檢查是否有 trained_model 輸出。

    - 建構一個指向訓練模型的路徑，格式化字串包含流水線作業名稱和輸出名稱（"trained_model"）。

    - 定義微調模型名稱，將原模型名稱附加 "-ultrachat-200k"，並將任何斜線替換為連字號。

    - 準備註冊模型，建立 Model 物件，包含模型路徑、模型類型（MLflow 模型）、名稱、版本及描述。

    - 呼叫 workspace_ml_client 的 models 物件的 create_or_update 方法，並以 Model 物件作為參數註冊模型。

    - 打印已註冊的模型。

1. 總結而言，這個腳本在 Azure Machine Learning 流水線中訓練的機器學習模型進行註冊。

    ```python
    # 從 Azure AI ML SDK 匯入必要的模組
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # 檢查管道工作中是否有 `trained_model` 輸出
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # 透過格式化字串構造已訓練模型的路徑，使用管道工作名稱及輸出名稱（"trained_model"）
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # 定義微調模型的名稱，方法是將 "-ultrachat-200k" 附加到原始模型名稱並將所有斜線替換成連字號
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # 準備註冊模型，透過建立具有多個參數的 Model 物件
    # 包含模型路徑、模型類型（MLflow 模型）、模型名稱和版本，以及模型描述
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # 使用時間戳記作為版本以避免版本衝突
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # 透過 workspace_ml_client 中的 models 物件的 create_or_update 方法，以 Model 物件作為引數來註冊模型
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # 輸出已註冊的模型
    print("registered model: \n", registered_model)
    ```

## 7. 將微調模型部署至線上端點

線上端點提供持久的 REST API，可用於與需要調用模型的應用程式整合。

### 管理端點

1. 這個 Python 腳本在 Azure Machine Learning 中為已註冊模型創建託管線上端點。以下是解析：

    - 從 Azure AI ML SDK 匯入必要模組。

    - 定義線上端點的唯一名稱，通過在字串 "ultrachat-completion-" 後加上時間戳。

    - 準備創建線上端點，建立 ManagedOnlineEndpoint 物件，含端點名稱、描述及驗證模式（"key"）。

    - 呼叫 workspace_ml_client 的 begin_create_or_update 方法以 ManagedOnlineEndpoint 物件為參數創建端點，並呼叫 wait 方法等待創建完成。

1. 總結而言，該腳本在 Azure Machine Learning 中為已註冊模型創建託管線上端點。

    ```python
    # 從 Azure AI ML SDK 匯入必要的模組
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # 定義一個獨特的線上端點名稱，方法是在字串 "ultrachat-completion-" 後附加時間戳
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # 準備建立線上端點，透過建立帶有各種參數的 ManagedOnlineEndpoint 物件
    # 這些參數包括端點名稱、端點描述及身份驗證模式（"key"）
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # 透過 workspace_ml_client 的 begin_create_or_update 方法，並以 ManagedOnlineEndpoint 物件作為參數來建立線上端點
    # 然後透過呼叫 wait 方法等待建立操作完成
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> 這裡可以找到部署支持的 SKU 列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署 ML 模型

1. 這個 Python 腳本將已註冊的機器學習模型部署至 Azure Machine Learning 託管線上端點。以下是解析：

    - 匯入 ast 模組，該模組提供處理 Python 抽象語法樹相關函數。

    - 將部署的實例類型設為 "Standard_NC6s_v3"。

    - 檢查 foundation model 是否含有 inference_compute_allow_list 標籤。如果存在，將標籤值由字串轉為 Python list，並設定給 inference_computes_allow_list；否則設為 None。

    - 檢查指定的實例類型是否包含於允許列表中。如果未包含，則打印訊息要求使用者選擇允許列表中的實例類型。

    - 準備建立部署，建立 ManagedOnlineDeployment 物件，包含部署名稱、端點名稱、模型 ID、實例類型和數量、存活探針設定及請求設定。

    - 呼叫 workspace_ml_client 的 begin_create_or_update 方法並以 ManagedOnlineDeployment 物件為參數創建部署，並呼叫 wait 方法等待操作完成。

    - 將端點的流量設定為 100% 指向 "demo" 部署。

    - 呼叫 workspace_ml_client 的 begin_create_or_update 方法，並以端點物件為參數更新端點，然後呼叫 result 方法等待更新完成。

1. 總結而言，這個腳本將已註冊的機器學習模型部署至 Azure Machine Learning 託管線上端點。

    ```python
    # 匯入 ast 模組，該模組提供處理 Python 抽象語法樹的功能
    import ast
    
    # 設定部署的實例類型
    instance_type = "Standard_NC6s_v3"
    
    # 檢查 foundation model 中是否存在 `inference_compute_allow_list` 標籤
    if "inference_compute_allow_list" in foundation_model.tags:
        # 若存在，將標籤值從字串轉換為 Python 清單，並指派給 `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # 若不存在，則將 `inference_computes_allow_list` 設為 `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # 檢查指定的實例類型是否在允許清單中
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # 準備建立部署，透過各種參數建立 `ManagedOnlineDeployment` 物件
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # 呼叫 `workspace_ml_client` 的 `begin_create_or_update` 方法，使用 `ManagedOnlineDeployment` 物件來建立部署
    # 接著呼叫 `wait` 方法，等待建立操作完成
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # 設定端點流量，將 100% 流量導向 "demo" 部署
    endpoint.traffic = {"demo": 100}
    
    # 呼叫 `workspace_ml_client` 的 `begin_create_or_update` 方法，使用 `endpoint` 物件更新端點
    # 接著呼叫 `result` 方法，等待更新操作完成
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. 使用範例資料測試端點

我們將從測試資料集中抓取一些範例資料並提交至線上端點進行推論。之後會顯示推論標籤與真實標籤。

### 讀取結果

1. 這個 Python 腳本將 JSON Lines 文件讀取到 pandas DataFrame，隨機抽樣並重置索引。以下解析：

    - 使用 read_json 函數並搭配 lines=True 參數讀取檔案 ./ultrachat_200k_dataset/test_gen.jsonl，因為檔案為 JSON Lines 格式，每行為一個 JSON 物件。

    - 從 DataFrame 中隨機抽取 1 筆資料。使用 sample 函數並指定 n=1。

    - 使用 reset_index 並指定 drop=True 重置 DataFrame 索引，拋棄原有索引，改以預設整數索引。

    - 使用 head 函數並傳入參數 2 顯示前 2 行資料。但由於抽樣後 DataFrame 僅有 1 行資料，實際只顯示那 1 行。

1. 總結而言，腳本從 JSON Lines 文件讀取資料到 pandas DataFrame，抽取 1 筆隨機樣本，重置索引並顯示該筆資料。

    ```python
    # 匯入 pandas 函式庫
    import pandas as pd
    
    # 將 JSON 連線檔案 './ultrachat_200k_dataset/test_gen.jsonl' 讀取為 pandas DataFrame
    # 'lines=True' 參數表示檔案是以 JSON 連線格式，每一行都是一個獨立的 JSON 物件
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # 從 DataFrame 中隨機抽取 1 行樣本
    # 'n=1' 參數指定隨機選取的行數為 1
    test_df = test_df.sample(n=1)
    
    # 重設 DataFrame 的索引
    # 'drop=True' 參數表示原本的索引會被捨棄，用預設的整數索引來取代
    # 'inplace=True' 參數表示直接在原 DataFrame 中修改（不建立新物件）
    test_df.reset_index(drop=True, inplace=True)
    
    # 顯示 DataFrame 的前 2 行
    # 但因為抽樣後的 DataFrame 只有 1 行，所以這只會顯示那一行
    test_df.head(2)
    ```

### 建立 JSON 物件

1. 這個 Python 腳本建立帶有特定參數的 JSON 物件並將其儲存為文件。以下是解析：

    - 匯入 json 模組，提供處理 JSON 資料的函數。
    - 它建立了一個名為 parameters 的字典，鍵和值分別代表機器學習模型的參數。鍵為 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，其對應的值分別是 0.6、0.9、True 和 200。

    - 它建立了另一個字典 test_json，有兩個鍵："input_data" 和 "params"。其中 "input_data" 的值是另一個字典，包含鍵 "input_string" 和 "parameters"。鍵 "input_string" 的值是一個包含 test_df DataFrame 中第一條訊息的清單。鍵 "parameters" 的值是前面建立的 parameters 字典。鍵 "params" 的值則是空字典。

    - 它打開了一個名為 sample_score.json 的檔案
    
    ```python
    # 匯入 json 模組，該模組提供處理 JSON 資料的函數
    import json
    
    # 建立一個字典 `parameters`，其鍵和值代表機器學習模型的參數
    # 鍵為 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，對應的值分別為 0.6、0.9、True 和 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # 建立另一個字典 `test_json`，有兩個鍵："input_data" 和 "params"
    # "input_data" 的值是另一個字典，具有鍵 "input_string" 和 "parameters"
    # "input_string" 的值是一個清單，包含 `test_df` 資料框中的第一則訊息
    # "parameters" 的值是先前建立的 `parameters` 字典
    # "params" 的值是一個空字典
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # 以寫入模式開啟位於 `./ultrachat_200k_dataset` 目錄中名為 `sample_score.json` 的檔案
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # 使用 `json.dump` 函數將 `test_json` 字典以 JSON 格式寫入檔案
        json.dump(test_json, f)
    ```

### 調用 Endpoint

1. 這段 Python 腳本正在調用 Azure Machine Learning 的線上端點來評分一個 JSON 檔案。以下是它的操作細節：

    - 它呼叫 workspace_ml_client 物件的 online_endpoints 屬性的 invoke 方法。此方法用於發送請求給線上端點並獲取回應。

    - 它使用 endpoint_name 和 deployment_name 參數指定端點名稱及部署名稱。在這裡，端點名稱儲存在 online_endpoint_name 變數中，部署名稱為 "demo"。

    - 它使用 request_file 參數指定要評分的 JSON 檔案路徑，該檔案為 ./ultrachat_200k_dataset/sample_score.json。

    - 它將端點回應存入 response 變數。

    - 它列印原始回應。

1. 總結而言，這段腳本調用了 Azure Machine Learning 的線上端點來評分一個 JSON 檔案，並打印回應結果。

    ```python
    # 調用 Azure 機器學習中的線上端點來對 `sample_score.json` 檔案進行評分
    # 使用 `workspace_ml_client` 物件的 `online_endpoints` 屬性的 `invoke` 方法向線上端點發送請求並獲取回應
    # `endpoint_name` 參數指定端點的名稱，該名稱儲存在 `online_endpoint_name` 變量中
    # `deployment_name` 參數指定部署的名稱，為 "demo"
    # `request_file` 參數指定要評分的 JSON 檔案路徑，為 `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # 列印來自端點的原始回應
    print("raw response: \n", response, "\n")
    ```

## 9. 刪除線上端點

1. 別忘了刪除線上端點，否則將繼續為端點使用的計算資源計費。這行 Python 程式碼是在 Azure Machine Learning 中刪除一個線上端點。以下是詳解：

    - 它呼叫 workspace_ml_client 物件的 online_endpoints 屬性的 begin_delete 方法。此方法用於開始刪除線上端點。

    - 它使用 name 參數指定要刪除的端點名稱，該名稱儲存在 online_endpoint_name 變數中。

    - 它呼叫 wait 方法等待刪除作業完成。這是一個阻塞操作，將阻止腳本繼續執行直到刪除完成。

    - 總結來說，這行程式碼啟動了 Azure Machine Learning 線上端點的刪除作業，並等待該作業完成。

    ```python
    # 刪除 Azure 機器學習中的在線端點
    # `workspace_ml_client` 物件的 `online_endpoints` 屬性的 `begin_delete` 方法用於開始刪除在線端點
    # `name` 參數指定要刪除的端點名稱，該名稱存儲在 `online_endpoint_name` 變量中
    # 呼叫 `wait` 方法以等待刪除操作完成。這是一個阻塞操作，意味著在刪除完成之前，腳本將無法繼續執行
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，請注意自動翻譯可能含有錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而引致之任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->