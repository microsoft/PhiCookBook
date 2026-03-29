# 在 Microsoft Foundry 中使用 Prompt flow 微調並整合自訂 Phi-3 模型

此端對端 (E2E) 範例基於 Microsoft Tech Community 的指南「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」。它介紹了微調、部署以及在 Microsoft Foundry 中使用 Prompt flow 整合自訂 Phi-3 模型的流程。
與需要在本機執行程式碼的端對端範例「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」不同，本教學完全聚焦於在 Azure AI / ML Studio 內微調與整合您的模型。

## 概覽

在此端對端範例中，您將學習如何微調 Phi-3 模型並在 Microsoft Foundry 中與 Prompt flow 整合。藉由利用 Azure AI / ML Studio，您將建立部署及使用自訂 AI 模型的工作流程。此端對端範例分為三個場景：

**場景 1：設定 Azure 資源並準備微調**

**場景 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 部署**

**場景 3：與 Prompt flow 整合並在 Microsoft Foundry 中與您的自訂模型聊天**

以下是此端對端範例的概覽。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/zh-HK/00-01-architecture.198ba0f1ae6d841a.webp)

### 目錄

1. **[場景 1：設定 Azure 資源並準備微調](#場景-1：設定-azure-資源並準備微調)**
    - [建立 Azure Machine Learning 工作區](#建立-azure-machine-learning-工作區)
    - [申請 Azure 訂閱的 GPU 配額](#申請-azure-訂閱的-gpu-配額)
    - [新增角色指派](#新增角色指派)
    - [設定專案](#設定專案)
    - [準備微調用資料集](#準備用於微調的資料集)

1. **[場景 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 部署](#情境-2：微調-phi-3-模型並部署於-azure-machine-learning-studio)**
    - [微調 Phi-3 模型](#微調-phi-3-模型)
    - [部署微調後的 Phi-3 模型](#部署微調後的-phi-3-模型)

1. **[場景 3：與 Prompt flow 整合並在 Microsoft Foundry 中與您的自訂模型聊天](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [將自訂 Phi-3 模型與 Prompt flow 整合](#與-prompt-flow-整合自訂-phi-3-模型)
    - [與您的自訂 Phi-3 模型聊天](#與您的自定義-phi-3-模型聊天)

## 場景 1：設定 Azure 資源並準備微調

### 建立 Azure Machine Learning 工作區

1. 在入口網站頁面頂部的 <strong>搜尋列</strong> 輸入 *azure machine learning*，並從出現的選項中選擇 **Azure Machine Learning**。

    ![Type azure machine learning.](../../../../../../translated_images/zh-HK/01-01-type-azml.acae6c5455e67b4b.webp)

2. 從導航選單選擇 **+ 建立**。

3. 從導航選單選擇 <strong>新工作區</strong>。

    ![Select new workspace.](../../../../../../translated_images/zh-HK/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. 執行以下操作：

    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（必要時建立新的）。
    - 輸入 <strong>工作區名稱</strong>，必須是唯一值。
    - 選擇您想使用的 <strong>區域</strong>。
    - 選擇要使用的 <strong>儲存帳戶</strong>（必要時建立新的）。
    - 選擇要使用的 <strong>金鑰保管庫</strong>（必要時建立新的）。
    - 選擇要使用的 <strong>應用程式洞察</strong>（必要時建立新的）。
    - 選擇要使用的 <strong>容器登錄</strong>（必要時建立新的）。

    ![Fill azure machine learning.](../../../../../../translated_images/zh-HK/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. 選擇 <strong>檢閱並建立</strong>。

6. 選擇 <strong>建立</strong>。

### 申請 Azure 訂閱的 GPU 配額

在本教學中，您將學習如何使用 GPU 微調並部署 Phi-3 模型。微調將使用 *Standard_NC24ads_A100_v4* GPU，需要申請配額。部署將使用 *Standard_NC6s_v3* GPU，也需要申請配額。

> [!NOTE]
>
> 僅限按用量付費訂閱（標準訂閱類型）有資格分配 GPU，優惠訂閱目前不支援。
>

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 執行以下操作以申請 *Standard NCADSA100v4 Family* 配額：

    - 從左側標籤選擇 <strong>配額</strong>。
    - 選擇要使用的 <strong>虛擬機家族</strong>。例如，選擇包含 *Standard_NC24ads_A100_v4* GPU 的 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**。
    - 從導航選單選擇 <strong>申請配額</strong>。

        ![Request quota.](../../../../../../translated_images/zh-HK/02-02-request-quota.c0428239a63ffdd5.webp)

    - 在申請配額頁面，輸入您想使用的 <strong>新核心上限</strong>（例如 24）。
    - 在申請配額頁面，選擇 <strong>提交</strong> 以申請 GPU 配額。

1. 執行以下操作以申請 *Standard NCSv3 Family* 配額：

    - 從左側標籤選擇 <strong>配額</strong>。
    - 選擇要使用的 <strong>虛擬機家族</strong>。例如，選擇包含 *Standard_NC6s_v3* GPU 的 **Standard NCSv3 Family Cluster Dedicated vCPUs**。
    - 從導航選單選擇 <strong>申請配額</strong>。
    - 在申請配額頁面，輸入您想使用的 <strong>新核心上限</strong>（例如 24）。
    - 在申請配額頁面，選擇 <strong>提交</strong> 以申請 GPU 配額。

### 新增角色指派

要微調並部署您的模型，您必須先建立使用者指派的受控身分（User Assigned Managed Identity，簡稱 UAI），並授予適當的權限。此 UAI 將於部署身分驗證中使用。

#### 建立 User Assigned Managed Identity (UAI)

1. 在入口網站頁面頂部的 <strong>搜尋列</strong> 輸入 *managed identities*，並從出現的選項中選擇 **Managed Identities**。

    ![Type managed identities.](../../../../../../translated_images/zh-HK/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. 選擇 **+ 建立**。

    ![Select create.](../../../../../../translated_images/zh-HK/03-02-select-create.92bf8989a5cd98f2.webp)

1. 執行以下操作：

    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（必要時建立新的）。
    - 選擇您想使用的 <strong>區域</strong>。
    - 輸入 <strong>名稱</strong>，必須是唯一值。

    ![Select create.](../../../../../../translated_images/zh-HK/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. 選擇 <strong>檢閱並建立</strong>。

1. 選擇 **+ 建立**。

#### 將「貢獻者」角色指派給 Managed Identity

1. 導覽至您建立的 Managed Identity 資源。

1. 從左側標籤選擇 **Azure 角色指派**。

1. 從導航選單選擇 **+新增角色指派**。

1. 在新增角色指派頁面，執行以下操作：
    - 將 <strong>範圍</strong> 設為 <strong>資源群組</strong>。
    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>。
    - 將 <strong>角色</strong> 設為 <strong>貢獻者</strong>。

    ![Fill contributor role.](../../../../../../translated_images/zh-HK/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. 選擇 <strong>儲存</strong>。

#### 將「儲存體 Blob 資料讀取者」角色指派給 Managed Identity

1. 在入口網站頁面頂部的 <strong>搜尋列</strong> 輸入 *storage accounts*，並從出現的選項中選擇 **Storage accounts**。

    ![Type storage accounts.](../../../../../../translated_images/zh-HK/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. 選擇與您建立的 Azure Machine Learning 工作區相關聯的儲存體帳戶。例如，*finetunephistorage*。

1. 執行以下操作以導航至新增角色指派頁面：

    - 導覽至您建立的 Azure 儲存體帳戶。
    - 從左側標籤選擇 **存取控制 (IAM)**。
    - 從導航選單選擇 **+ 新增**。
    - 從導航選單選擇 <strong>新增角色指派</strong>。

    ![Add role.](../../../../../../translated_images/zh-HK/03-06-add-role.353ccbfdcf0789c2.webp)

1. 在新增角色指派頁面，執行以下操作：

    - 在角色頁面，於 <strong>搜尋列</strong> 輸入 *Storage Blob Data Reader* 並從選項中選擇 **Storage Blob Data Reader**。
    - 在角色頁面，選擇 <strong>下一步</strong>。
    - 在成員頁面，設定 <strong>指定存取權給</strong> 為 **Managed identity**。
    - 在成員頁面，選擇 **+ 選取成員**。
    - 在選取 Managed identities 頁面，選擇您的 Azure <strong>訂閱</strong>。
    - 在選取 Managed identities 頁面，選擇 **Managed identity**，類型為 **Manage Identity**。
    - 在選取 Managed identities 頁面，選擇您建立的 Managed Identity。例如，*finetunephi-managedidentity*。
    - 在選取 Managed identities 頁面，選擇 <strong>選取</strong>。

    ![Select managed identity.](../../../../../../translated_images/zh-HK/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. 選擇 <strong>檢閱並指派</strong>。

#### 將「AcrPull」角色指派給 Managed Identity

1. 在入口網站頁面頂部的 <strong>搜尋列</strong> 輸入 *container registries*，並從出現的選項中選擇 **Container registries**。

    ![Type container registries.](../../../../../../translated_images/zh-HK/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. 選擇與 Azure Machine Learning 工作區相關聯的容器登錄。例如，*finetunephicontainerregistry*

1. 執行以下操作以導航至新增角色指派頁面：

    - 從左側標籤選擇 **存取控制 (IAM)**。
    - 從導航選單選擇 **+ 新增**。
    - 從導航選單選擇 <strong>新增角色指派</strong>。

1. 在新增角色指派頁面，執行以下操作：

    - 在角色頁面，於 <strong>搜尋列</strong> 輸入 *AcrPull* 並從選項中選擇 **AcrPull**。
    - 在角色頁面，選擇 <strong>下一步</strong>。
    - 在成員頁面，設定 <strong>指定存取權給</strong> 為 **Managed identity**。
    - 在成員頁面，選擇 **+ 選取成員**。
    - 在選取 Managed identities 頁面，選擇您的 Azure <strong>訂閱</strong>。
    - 在選取 Managed identities 頁面，選擇 **Managed identity**，類型為 **Manage Identity**。
    - 在選取 Managed identities 頁面，選擇您建立的 Managed Identity。例如，*finetunephi-managedidentity*。
    - 在選取 Managed identities 頁面，選擇 <strong>選取</strong>。
    - 選擇 <strong>檢閱並指派</strong>。

### 設定專案

為了下載微調所需的資料集，您將設定本機環境。

在此練習中，您將：

- 建立一個資料夾以在其中工作。
- 建立虛擬環境。
- 安裝所需套件。
- 建立 *download_dataset.py* 檔案來下載資料集。

#### 建立資料夾以在其中工作

1. 開啟終端機視窗，輸入以下指令於預設路徑建立名為 *finetune-phi* 的資料夾。

    ```console
    mkdir finetune-phi
    ```

2. 在終端機中輸入以下指令，切換至您剛建立的 *finetune-phi* 資料夾。

    ```console
    cd finetune-phi
    ```

#### 建立虛擬環境

1. 在終端機中輸入以下指令，建立名為 *.venv* 的虛擬環境。
    ```console
    python -m venv .venv
    ```

2. 在終端機內輸入以下指令以啟用虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 如果成功，您應該會在命令提示符前看到 *(.venv)*。

#### 安裝所需套件

1. 在終端機內輸入以下指令以安裝所需套件。

    ```console
    pip install datasets==2.19.1
    ```

#### 建立 `donload_dataset.py`

> [!NOTE]
> 完整資料夾結構：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. 開啟 **Visual Studio Code**。

1. 從選單列選擇 <strong>檔案</strong>。

1. 選擇 <strong>開啟資料夾</strong>。

1. 選擇您建立的 *finetune-phi* 資料夾，位置位於 *C:\Users\yourUserName\finetune-phi*。

    ![選擇您建立的資料夾。](../../../../../../translated_images/zh-HK/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. 在 Visual Studio Code 左側窗格中，按右鍵並選擇 <strong>新增檔案</strong>，建立一個名為 *download_dataset.py* 的新檔案。

    ![建立新檔案。](../../../../../../translated_images/zh-HK/04-02-create-new-file.cf9a330a3a9cff92.webp)

### 準備用於微調的資料集

在此練習中，您將執行 *download_dataset.py* 檔案以下載 *ultrachat_200k* 資料集至您的本地環境。接著，您將使用該資料集在 Azure Machine Learning 中微調 Phi-3 模型。

在此練習中，您將：

- 將程式碼加入 *download_dataset.py* 檔案以下載資料集。
- 執行 *download_dataset.py* 檔案以將資料集下載至本地環境。

#### 使用 *download_dataset.py* 下載資料集

1. 在 Visual Studio Code 中開啟 *download_dataset.py* 檔案。

1. 將以下程式碼加入 *download_dataset.py* 檔案。

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # 載入指定名稱、配置及分割比例的數據集
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # 將數據集分割為訓練集及測試集（80% 訓練，20% 測試）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 如果目錄不存在，則創建該目錄
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以寫入模式打開檔案
        with open(filepath, 'w', encoding='utf-8') as f:
            # 遍歷數據集中的每條記錄
            for record in dataset:
                # 將記錄序列化為 JSON 物件並寫入檔案
                json.dump(record, f)
                # 寫入換行字元以分隔記錄
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 使用特定配置及分割比例載入並分割 ULTRACHAT_200k 數據集
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 從分割結果中提取訓練集及測試集
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 將訓練集保存到 JSONL 檔案
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # 將測試集保存到另一個 JSONL 檔案
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 在終端機輸入以下指令執行腳本，將資料集下載至本地環境。

    ```console
    python download_dataset.py
    ```

1. 確認資料集已成功儲存至本地的 *finetune-phi/data* 目錄。

> [!NOTE]
>
> #### 有關資料集大小及微調時間的說明
>
> 在本教學中，您僅使用 1% 的資料集（`split='train[:1%]'`）。此舉大幅減少資料量，加快上傳與微調流程。您可以調整該百分比以找到訓練時間與模型效能的最佳平衡。使用較小的資料集子集能縮短微調所需時間，使教學過程更易管理。

## 情境 2：微調 Phi-3 模型並部署於 Azure Machine Learning Studio

### 微調 Phi-3 模型

在此練習中，您將於 Azure Machine Learning Studio 中微調 Phi-3 模型。

在此練習中，您將：

- 建立微調用的計算叢集。
- 在 Azure Machine Learning Studio 中微調 Phi-3 模型。

#### 建立微調用計算叢集

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 從左側標籤選擇 <strong>計算</strong>。

1. 從導航選單選擇 <strong>計算叢集</strong>。

1. 選擇 **+ 新增**。

    ![選擇計算。](../../../../../../translated_images/zh-HK/06-01-select-compute.a29cff290b480252.webp)

1. 執行以下操作：

    - 選擇您想使用的 <strong>地區</strong>。
    - 將 <strong>虛擬機層級</strong> 選為 <strong>專用</strong>。
    - 將 <strong>虛擬機類型</strong> 選為 **GPU**。
    - 將 <strong>虛擬機大小</strong> 篩選器設定為 <strong>從全部選項中選擇</strong>。
    - 選擇 <strong>虛擬機大小</strong> 為 **Standard_NC24ads_A100_v4**。

    ![建立叢集。](../../../../../../translated_images/zh-HK/06-02-create-cluster.f221b65ae1221d4e.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行以下操作：

    - 輸入 <strong>計算名稱</strong>。此名稱必須唯一。
    - 設定 <strong>最小節點數</strong> 為 **0**。
    - 設定 <strong>最大節點數</strong> 為 **1**。
    - 將 <strong>空閒秒數後自動縮減規模</strong> 設為 **120**。

    ![建立叢集。](../../../../../../translated_images/zh-HK/06-03-create-cluster.4a54ba20914f3662.webp)

1. 選擇 <strong>建立</strong>。

#### 微調 Phi-3 模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選取你建立的 Azure Machine Learning 工作區。

    ![選擇你建立的工作區。](../../../../../../translated_images/zh-HK/06-04-select-workspace.a92934ac04f4f181.webp)

1. 執行以下操作：

    - 從左側標籤選擇 <strong>模型目錄</strong>。
    - 在 <strong>搜尋列</strong> 輸入 *phi-3-mini-4k*，並從出現的選項中選擇 **Phi-3-mini-4k-instruct**。

    ![輸入 phi-3-mini-4k。](../../../../../../translated_images/zh-HK/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. 從導航選單選擇 <strong>微調</strong>。

    ![選擇微調。](../../../../../../translated_images/zh-HK/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. 執行以下操作：

    - 將 <strong>選擇任務類型</strong> 設為 <strong>聊天補全</strong>。
    - 選擇 **+ 選擇資料** 上傳 <strong>訓練資料</strong>。
    - 將驗證資料上傳類型設定為 <strong>提供不同的驗證資料</strong>。
    - 選擇 **+ 選擇資料** 上傳 <strong>驗證資料</strong>。

    ![填寫微調頁面。](../../../../../../translated_images/zh-HK/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> 您可以選擇 <strong>進階設定</strong>，自訂如 **learning_rate** 與 **lr_scheduler_type** 等參數，以依需求最佳化微調流程。

1. 選擇 <strong>完成</strong>。

1. 在此練習中，您已成功使用 Azure Machine Learning 微調 Phi-3 模型。請注意，微調過程可能耗時相當長。啟動微調工作後，您需要等待其完成。您可透過在 Azure Machine Learning 工作區左側的「工作」分頁監控微調工作的狀態。後續章節將介紹如何部署微調後的模型並與 Prompt flow 整合。

    ![查看微調工作。](../../../../../../translated_images/zh-HK/06-08-output.2bd32e59930672b1.webp)

### 部署微調後的 Phi-3 模型

為讓微調後的 Phi-3 模型能於即時推論中被存取並與 Prompt flow 整合，需完成模型註冊、建立線上端點與部署模型等步驟。

在此練習中，您將：

- 在 Azure Machine Learning 工作區註冊微調後模型。
- 建立線上端點。
- 部署已註冊的微調後 Phi-3 模型。

#### 註冊微調後模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選取你建立的 Azure Machine Learning 工作區。

    ![選擇你建立的工作區。](../../../../../../translated_images/zh-HK/06-04-select-workspace.a92934ac04f4f181.webp)

1. 從左側標籤選擇 <strong>模型</strong>。
1. 選擇 **+ 註冊**。
1. 選擇 <strong>來自工作輸出</strong>。

    ![註冊模型。](../../../../../../translated_images/zh-HK/07-01-register-model.ad1e7cc05e4b2777.webp)

1. 選擇您建立的工作。

    ![選擇工作。](../../../../../../translated_images/zh-HK/07-02-select-job.3e2e1144cd6cd093.webp)

1. 選擇 <strong>下一步</strong>。

1. 將 <strong>模型類型</strong> 設為 **MLflow**。

1. 確認已選擇 <strong>工作輸出</strong>，系統應自動選擇此項。

    ![選擇輸出。](../../../../../../translated_images/zh-HK/07-03-select-output.4cf1a0e645baea1f.webp)

2. 選擇 <strong>下一步</strong>。

3. 選擇 <strong>註冊</strong>。

    ![選擇註冊。](../../../../../../translated_images/zh-HK/07-04-register.fd82a3b293060bc7.webp)

4. 您可從左側標籤的 <strong>模型</strong> 選單查看已註冊模型。

    ![已註冊模型。](../../../../../../translated_images/zh-HK/07-05-registered-model.7db9775f58dfd591.webp)

#### 部署微調後模型

1. 前往您建立的 Azure Machine Learning 工作區。

1. 從左側標籤選擇 <strong>端點</strong>。

1. 從導航選單選擇 <strong>即時端點</strong>。

    ![建立端點。](../../../../../../translated_images/zh-HK/07-06-create-endpoint.1ba865c606551f09.webp)

1. 選擇 <strong>建立</strong>。

1. 選擇您之前註冊的模型。

    ![選擇已註冊模型。](../../../../../../translated_images/zh-HK/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. 選擇 <strong>選擇</strong>。

1. 執行以下操作：

    - 將 <strong>虛擬機器</strong> 設為 *Standard_NC6s_v3*。
    - 選擇您想使用的 <strong>實例數量</strong>，例如 *1*。
    - 將 <strong>端點</strong> 設為 <strong>建立新端點</strong>。
    - 輸入 <strong>端點名稱</strong>，此名稱必須唯一。
    - 輸入 <strong>部署名稱</strong>，此名稱必須唯一。

    ![填寫部署設定。](../../../../../../translated_images/zh-HK/07-08-deployment-setting.43ddc4209e673784.webp)

1. 選擇 <strong>部署</strong>。

> [!WARNING]
> 為避免額外費用，請確保在 Azure Machine Learning 工作區中刪除建立的端點。
>

#### 在 Azure Machine Learning 工作區檢查部署狀態

1. 前往您建立的 Azure Machine Learning 工作區。

1. 從左側標籤選擇 <strong>端點</strong>。

1. 選擇您建立的端點。

    ![選擇端點](../../../../../../translated_images/zh-HK/07-09-check-deployment.325d18cae8475ef4.webp)

1. 您可以在此頁面管理端點的部署過程。

> [!NOTE]
> 部署完成後，請確保 <strong>現場流量</strong> 設定為 **100%**。若未設定，請選擇 <strong>更新流量</strong> 來調整。若流量設為 0%，將無法測試模型。
>
> ![設定流量。](../../../../../../translated_images/zh-HK/07-10-set-traffic.085b847e5751ff3d.webp)
>

## 情境 3：與 Prompt flow 整合並於 Microsoft Foundry 使用自訂模型聊天

### 與 Prompt flow 整合自訂 Phi-3 模型

成功部署微調後模型後，您可以與 Prompt Flow 整合，將模型用於即時應用，實現與自訂 Phi-3 模型進行各種互動任務。

在此練習中，您將：

- 建立 Microsoft Foundry Hub。
- 建立 Microsoft Foundry 專案。
- 建立 Prompt flow。
- 新增自訂連線用於微調後的 Phi-3 模型。
- 設定 Prompt flow 與您的自訂 Phi-3 模型聊天。

> [!NOTE]
> 您也可以透過 Azure ML Studio 與 Promptflow 整合，同樣的整合流程適用於 Azure ML Studio。

#### 建立 Microsoft Foundry Hub

在建立專案前，您需要先建立 Hub。Hub 類似於資源群組，可讓您在 Microsoft Foundry 內組織並管理多個專案。
1. 訪問 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 從左側標籤選擇 **All hubs**。

1. 從導覽選單選擇 **+ New hub**。

    ![Create hub.](../../../../../../translated_images/zh-HK/08-01-create-hub.8f7dd615bb8d9834.webp)

1. 執行以下操作：

    - 輸入 **Hub name**。此值必須是唯一的。
    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**（如有需要可建立新的）。
    - 選擇您想使用的 **Location**。
    - 選擇要使用的 **Connect Azure AI Services**（如有需要可建立新的）。
    - 選擇 **Connect Azure AI Search** 並選擇 **Skip connecting**。

    ![Fill hub.](../../../../../../translated_images/zh-HK/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. 選擇 **Next**。

#### 建立 Microsoft Foundry 專案

1. 在您建立的 Hub 裡，從左側標籤選擇 **All projects**。

1. 從導覽選單選擇 **+ New project**。

    ![Select new project.](../../../../../../translated_images/zh-HK/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. 輸入 **Project name**。此值必須是唯一的。

    ![Create project.](../../../../../../translated_images/zh-HK/08-05-create-project.4d97f0372f03375a.webp)

1. 選擇 **Create a project**。

#### 為微調過的 Phi-3 模型新增自定義連線

要將您的自定義 Phi-3 模型與 Prompt flow 整合，您需要在自定義連線中保存模型的端點和金鑰。此設定確保在 Prompt flow 中可存取您的自定義 Phi-3 模型。

#### 設定微調過的 Phi-3 模型的 api 金鑰和端點 URI

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 導航至您建立的 Azure 機器學習工作區。

1. 從左側標籤選擇 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/zh-HK/08-06-select-endpoints.aff38d453bcf9605.webp)

1. 選擇您建立的端點。

    ![Select endpoints.](../../../../../../translated_images/zh-HK/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. 從導覽選單選擇 **Consume**。

1. 複製您的 **REST endpoint** 和 **Primary key**。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/zh-HK/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### 新增自定義連線

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 導航至您建立的 Microsoft Foundry 專案。

1. 在您建立的專案中，從左側標籤選擇 **Settings**。

1. 選擇 **+ New connection**。

    ![Select new connection.](../../../../../../translated_images/zh-HK/08-09-select-new-connection.02eb45deadc401fc.webp)

1. 從導覽選單選擇 **Custom keys**。

    ![Select custom keys.](../../../../../../translated_images/zh-HK/08-10-select-custom-keys.856f6b2966460551.webp)

1. 執行以下操作：

    - 選擇 **+ Add key value pairs**。
    - 對於鍵名稱，輸入 **endpoint**，並將您從 Azure ML Studio 複製的端點貼到值欄位。
    - 再次選擇 **+ Add key value pairs**。
    - 對於鍵名稱，輸入 **key**，並將您從 Azure ML Studio 複製的金鑰貼到值欄位。
    - 添加金鑰後，選擇 **is secret** 以防止金鑰被曝光。

    ![Add connection.](../../../../../../translated_images/zh-HK/08-11-add-connection.785486badb4d2d26.webp)

1. 選擇 **Add connection**。

#### 創建 Prompt flow

您已在 Microsoft Foundry 中新增了自定義連線。現在，讓我們使用以下步驟創建一個 Prompt flow。接著，您將連接此 Prompt flow 至自定義連線，讓您在 Prompt flow 中使用微調過的模型。

1. 導航至您建立的 Microsoft Foundry 專案。

1. 從左側標籤選擇 **Prompt flow**。

1. 從導覽選單選擇 **+ Create**。

    ![Select Promptflow.](../../../../../../translated_images/zh-HK/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. 從導覽選單選擇 **Chat flow**。

    ![Select chat flow.](../../../../../../translated_images/zh-HK/08-13-select-flow-type.2ec689b22da32591.webp)

1. 輸入要使用的 **Folder name**。

    ![Enter name.](../../../../../../translated_images/zh-HK/08-14-enter-name.ff9520fefd89f40d.webp)

2. 選擇 **Create**。

#### 設定 Prompt flow 與您的自定義 Phi-3 模型進行聊天

您需要將微調過的 Phi-3 模型整合至 Prompt flow。然而，現有提供的 Prompt flow 不是為此目的設計。因此，您必須重新設計 Prompt flow 以啟用自定義模型的整合。

1. 在 Prompt flow 中，執行以下任務以重建現有流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 檔案中的所有現有代碼。
    - 將以下程式碼新增至 *flow.dag.yml* 檔案。

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - 選擇 **Save**。

    ![Select raw file mode.](../../../../../../translated_images/zh-HK/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. 將以下程式碼加入 *integrate_with_promptflow.py* 檔案，以在 Prompt flow 中使用自定義 Phi-3 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 日誌設置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # 「connection」是自訂連接的名稱，「endpoint」、「key」是自訂連接中的鍵
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # 紀錄完整的 JSON 回應
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/zh-HK/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> 如需更詳細的 Microsoft Foundry 中 Prompt flow 使用資訊，您可參考 [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input**、**Chat output** 以啟用與您的模型聊天。

    ![Input Output.](../../../../../../translated_images/zh-HK/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. 現在您已準備好與自定義 Phi-3 模型聊天。在下一個練習中，您將學習如何啟動 Prompt flow 並使用它與您的微調 Phi-3 模型對話。

> [!NOTE]
>
> 重建後的流程應該如以下圖片所示：
>
> ![Flow example.](../../../../../../translated_images/zh-HK/08-18-graph-example.d6457533952e690c.webp)
>

### 與您的自定義 Phi-3 模型聊天

現在您已微調並將自定義 Phi-3 模型整合到 Prompt flow，您已準備好開始與它互動。本練習將引導您完成設定與啟動模型聊天的過程。透過遵循這些步驟，您將能充分利用已微調 Phi-3 模型在各種任務與對話中的能力。

- 使用 Prompt flow 與您的自定義 Phi-3 模型聊天。

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 以啟動 Prompt flow。

    ![Start compute session.](../../../../../../translated_images/zh-HK/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. 選擇 **Validate and parse input** 以更新參數。

    ![Validate input.](../../../../../../translated_images/zh-HK/09-02-validate-input.317c76ef766361e9.webp)

1. 選擇 **connection** 的 **Value**，選擇您建立的自定義連線。例如，*connection*。

    ![Connection.](../../../../../../translated_images/zh-HK/09-03-select-connection.99bdddb4b1844023.webp)

#### 與您的自定義模型聊天

1. 選擇 **Chat**。

    ![Select chat.](../../../../../../translated_images/zh-HK/09-04-select-chat.61936dce6612a1e6.webp)

1. 以下是結果範例：現在您可以與您的自定義 Phi-3 模型聊天。建議以微調使用的資料為基礎提出問題。

    ![Chat with prompt flow.](../../../../../../translated_images/zh-HK/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->