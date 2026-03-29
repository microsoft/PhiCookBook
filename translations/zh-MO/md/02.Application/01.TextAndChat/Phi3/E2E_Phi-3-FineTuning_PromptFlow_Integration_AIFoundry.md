# 微調及整合自訂 Phi-3 模型至 Microsoft Foundry 的 Prompt flow

此端到端（E2E）範例基於 Microsoft Tech Community 的指南「[微調及整合自訂 Phi-3 模型與 Microsoft Foundry 中的 Prompt Flow](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」。內容介紹了微調、自訂 Phi-3 模型的部署流程，並將其與 Microsoft Foundry 的 Prompt flow 整合。
不同於需本地執行代碼的端到端範例「[微調並整合自訂 Phi-3 模型與 Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」，本教程專注於在 Azure AI / ML Studio 平台內完成模型微調與整合。

## 概覽

在本 E2E 範例中，你將學會如何微調 Phi-3 模型並將其與 Microsoft Foundry 的 Prompt flow 整合。透過 Azure AI / ML Studio，建立部署和使用自訂 AI 模型的工作流程。本範例分為三個場景：

**場景一：建立 Azure 資源及準備微調**

**場景二：微調 Phi-3 模型並部署於 Azure Machine Learning Studio**

**場景三：整合 Prompt flow，並於 Microsoft Foundry 與自訂模型聊天**

以下為本 E2E 範例的總覽圖。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/zh-MO/00-01-architecture.198ba0f1ae6d841a.webp)

### 目錄

1. **[場景一：建立 Azure 資源及準備微調](#場景一：建立-azure-資源及準備微調)**
    - [建立 Azure Machine Learning 工作區](#建立-azure-machine-learning-工作區)
    - [申請 Azure 訂閱的 GPU 配額](#申請-azure-訂閱的-gpu-配額)
    - [新增角色指派](#新增角色指派)
    - [設定專案](#設定專案)
    - [準備微調資料集](#準備微調數據集)

1. **[場景二：微調 Phi-3 模型並部署於 Azure Machine Learning Studio](#情境二：在-azure-machine-learning-studio-微調-phi-3-模型並部署)**
    - [微調 Phi-3 模型](#微調-phi-3-模型)
    - [部署微調後的 Phi-3 模型](#部署微調後的-phi-3-模型)

1. **[場景三：整合 Prompt flow 並於 Microsoft Foundry 與自訂模型聊天](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [將自訂 Phi-3 模型整合至 Prompt flow](#將自訂-phi-3-模型整合到-prompt-flow)
    - [與自訂 Phi-3 模型聊天](#與您的自訂-phi-3-模型聊天)

## 場景一：建立 Azure 資源及準備微調

### 建立 Azure Machine Learning 工作區

1. 在入口網站頂端的 <strong>搜尋列</strong> 輸入 *azure machine learning*，並從搜尋結果中選擇 **Azure Machine Learning**。

    ![Type azure machine learning.](../../../../../../translated_images/zh-MO/01-01-type-azml.acae6c5455e67b4b.webp)

2. 從導航選單選擇 **+ Create**。

3. 從導航選單選擇 **New workspace**。

    ![Select new workspace.](../../../../../../translated_images/zh-MO/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. 執行以下項目：

    - 選擇你的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如無則建立新群組）。
    - 輸入 <strong>工作區名稱</strong>，必須為唯一值。
    - 選擇欲使用的 <strong>區域</strong>。
    - 選擇要使用的 <strong>儲存帳戶</strong>（如無則建立新帳戶）。
    - 選擇要使用的 <strong>金鑰保管庫</strong>（如無則建立新金鑰保管庫）。
    - 選擇要使用的 <strong>應用程式洞察</strong>（如無則建立新應用程式洞察）。
    - 選擇要使用的 <strong>容器註冊表</strong>（如無則建立新容器註冊表）。

    ![Fill azure machine learning.](../../../../../../translated_images/zh-MO/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. 選擇 **Review + Create**。

6. 選擇 **Create**。

### 申請 Azure 訂閱的 GPU 配額

本教程中將學習如何使用 GPU 微調並部署 Phi-3 模型。微調階段使用 *Standard_NC24ads_A100_v4* GPU，需提出配額申請；部署階段使用 *Standard_NC6s_v3* GPU，同樣需提出配額申請。

> [!NOTE]
>
> 只有按用量付費訂閱（標準訂閱類型）有資格使用 GPU 配額，目前不支援優惠訂閱。
>

1. 造訪 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 申請 *Standard NCADSA100v4 Family* 配額，執行以下操作：

    - 從左側分頁選擇 **Quota**。
    - 選擇所需的 <strong>虛擬機器族群</strong>，例如包含 *Standard_NC24ads_A100_v4* GPU 的 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**。
    - 從導航選單點選 **Request quota**。

        ![Request quota.](../../../../../../translated_images/zh-MO/02-02-request-quota.c0428239a63ffdd5.webp)

    - 在配額申請頁面輸入欲申請的 <strong>新核心數限制</strong>，例如 24。
    - 點選 **Submit** 提交 GPU 配額申請。

1. 申請 *Standard NCSv3 Family* 配額，執行以下操作：

    - 從左側分頁選擇 **Quota**。
    - 選擇所需的 <strong>虛擬機器族群</strong>，例如包含 *Standard_NC6s_v3* GPU 的 **Standard NCSv3 Family Cluster Dedicated vCPUs**。
    - 從導航選單點選 **Request quota**。
    - 在配額申請頁面輸入欲申請的 <strong>新核心數限制</strong>，例如 24。
    - 點選 **Submit** 提交 GPU 配額申請。

### 新增角色指派

為了微調與部署模型，必須先建立一個使用者指定的管理身分（User Assigned Managed Identity, UAI），並為其指派適當的權限。此 UAI 於部署時作為認證依據。

#### 建立使用者指定的管理身分 (UAI)

1. 在入口網站頂端的 <strong>搜尋列</strong> 輸入 *managed identities*，並從搜尋結果中選擇 **Managed Identities**。

    ![Type managed identities.](../../../../../../translated_images/zh-MO/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. 點選 **+ Create**。

    ![Select create.](../../../../../../translated_images/zh-MO/03-02-select-create.92bf8989a5cd98f2.webp)

1. 執行以下設定：

    - 選擇你的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如無則建立新群組）。
    - 選擇欲使用的 <strong>區域</strong>。
    - 輸入 <strong>名稱</strong>，必須為唯一值。

    ![Select create.](../../../../../../translated_images/zh-MO/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. 點選 **Review + create**。

1. 點選 **+ Create**。

#### 為管理身分新增 Contributor 角色指派

1. 導覽至剛剛建立的管理身分資源。

1. 從左側分頁中選擇 **Azure role assignments**。

1. 從導航選單中選擇 **+Add role assignment**。

1. 在新增角色指派頁面中，執行以下設定：
    - 設定 <strong>範圍</strong> 為 **Resource group**。
    - 選擇你的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>。
    - 設定 <strong>角色</strong> 為 **Contributor**。

    ![Fill contributor role.](../../../../../../translated_images/zh-MO/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. 點選 **Save**。

#### 為管理身分新增 Storage Blob Data Reader 角色指派

1. 在入口網站頂端的 <strong>搜尋列</strong> 輸入 *storage accounts*，並從搜尋結果中選擇 **Storage accounts**。

    ![Type storage accounts.](../../../../../../translated_images/zh-MO/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. 選擇與你建立之 Azure Machine Learning 工作區相關聯的儲存帳戶，例如 *finetunephistorage*。

1. 執行以下步驟以進入新增角色指派頁面：

    - 導覽至剛建立的 Azure 儲存帳戶。
    - 從左側分頁選擇 **Access Control (IAM)**。
    - 從導航選單點選 **+ Add**。
    - 再點選 **Add role assignment**。

    ![Add role.](../../../../../../translated_images/zh-MO/03-06-add-role.353ccbfdcf0789c2.webp)

1. 在新增角色指派頁面中，執行以下設定：

    - 在角色搜尋列輸入 *Storage Blob Data Reader*，並從結果選擇 **Storage Blob Data Reader**。
    - 點選 **Next**。
    - 在成員頁中，設定 **Assign access to** 為 **Managed identity**。
    - 點選 **+ Select members**。
    - 選擇你的 Azure <strong>訂閱</strong>。
    - 選擇 **Managed identity** 為 **Manage Identity**。
    - 選擇先前建立的管理身分，例如 *finetunephi-managedidentity*。
    - 點選 **Select**。

    ![Select managed identity.](../../../../../../translated_images/zh-MO/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. 點選 **Review + assign**。

#### 為管理身分新增 AcrPull 角色指派

1. 在入口網站頂端的 <strong>搜尋列</strong> 輸入 *container registries*，並從搜尋結果中選擇 **Container registries**。

    ![Type container registries.](../../../../../../translated_images/zh-MO/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. 選擇與 Azure Machine Learning 工作區相關聯的容器註冊表，例如 *finetunephicontainerregistry*

1. 執行以下步驟以進入新增角色指派頁面：

    - 從左側分頁選擇 **Access Control (IAM)**。
    - 從導航選單點選 **+ Add**。
    - 再點選 **Add role assignment**。

1. 在新增角色指派頁面中，執行以下設定：

    - 在角色搜尋列輸入 *AcrPull*，並從結果選擇 **AcrPull**。
    - 點選 **Next**。
    - 在成員頁中，設定 **Assign access to** 為 **Managed identity**。
    - 點選 **+ Select members**。
    - 選擇你的 Azure <strong>訂閱</strong>。
    - 選擇 **Managed identity** 為 **Manage Identity**。
    - 選擇先前建立的管理身分，例如 *finetunephi-managedidentity*。
    - 點選 **Select**。
    - 點選 **Review + assign**。

### 設定專案

接下來將設置本地環境以下載微調所需的資料集。

本練習中你將執行：

- 建立工作資料夾。
- 創建虛擬環境。
- 安裝必須的套件。
- 建立 *download_dataset.py* 檔案以下載資料集。

#### 建立工作資料夾

1. 開啟終端機視窗，輸入以下指令於預設路徑建立名為 *finetune-phi* 的資料夾。

    ```console
    mkdir finetune-phi
    ```

2. 在終端機輸入以下指令，切換至剛建立的 *finetune-phi* 資料夾。

    ```console
    cd finetune-phi
    ```

#### 創建虛擬環境

1. 在終端機輸入以下指令，建立名為 *.venv* 的虛擬環境。
    ```console
    python -m venv .venv
    ```

2. 在終端機中輸入以下指令以啟動虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 若成功，您應該會在指令提示符號前看到<em>（.venv）</em>。

#### 安裝所需套件

1. 在終端機中輸入以下指令以安裝所需套件。

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

1. 從選單列選擇 **File**。

1. 選擇 **Open Folder**。

1. 選擇您建立的 *finetune-phi* 資料夾，路徑位於 *C:\Users\yourUserName\finetune-phi*。

    ![選取您建立的資料夾。](../../../../../../translated_images/zh-MO/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. 在 Visual Studio Code 左側窗格中，按右鍵並選擇 **New File** 以建立名為 *download_dataset.py* 的新檔案。

    ![建立新檔案。](../../../../../../translated_images/zh-MO/04-02-create-new-file.cf9a330a3a9cff92.webp)

### 準備微調數據集

在本練習中，您將執行 *download_dataset.py* 檔案，將 *ultrachat_200k* 數據集下載到本地環境。然後您將使用該數據集在 Azure Machine Learning 中微調 Phi-3 模型。

在本練習中，您將：

- 在 *download_dataset.py* 檔案中新增代碼以下載數據集。
- 執行 *download_dataset.py* 檔案將數據集下載到本地環境。

#### 使用 *download_dataset.py* 下載您的數據集

1. 在 Visual Studio Code 中開啟 *download_dataset.py* 檔案。

1. 在 *download_dataset.py* 檔案中新增以下代碼。

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # 載入指定名稱、配置及分割比率的數據集
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # 將數據集分割為訓練集及測試集（80%訓練，20%測試）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 如目錄不存在，則建立該目錄
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以寫入模式開啟檔案
        with open(filepath, 'w', encoding='utf-8') as f:
            # 遍歷數據集中的每一筆記錄
            for record in dataset:
                # 將記錄以 JSON 物件格式導出並寫入檔案
                json.dump(record, f)
                # 寫入換行字元以區分記錄
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 載入並分割帶有特定配置及分割比率的 ULTRACHAT_200k 數據集
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 從分割結果中提取訓練集與測試集
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 將訓練集保存為 JSONL 檔案
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # 將測試集保存為另一個 JSONL 檔案
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 在終端機中輸入以下指令以執行腳本，並將數據集下載到本地環境。

    ```console
    python download_dataset.py
    ```

1. 確認數據集已成功儲存至本地 *finetune-phi/data* 目錄。

> [!NOTE]
>
> #### 關於數據集大小及微調時間的說明
>
> 在本教學中，您僅使用數據集的 1%（`split='train[:1%]'`）。此舉大幅減少了資料量，提升了上傳與微調速度。您可調整百分比以達成訓練時間與模型效能間的平衡。使用較小的數據子集可縮短微調所需的時間，使本教學流程更加容易管理。

## 情境二：在 Azure Machine Learning Studio 微調 Phi-3 模型並部署

### 微調 Phi-3 模型

在本練習中，您將在 Azure Machine Learning Studio 中微調 Phi-3 模型。

本練習中，您將：

- 建立用於微調的計算叢集。
- 在 Azure Machine Learning Studio 中微調 Phi-3 模型。

#### 建立用於微調的計算叢集

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 從左側標籤選擇 **Compute**。

1. 從導覽選單中選擇 **Compute clusters**。

1. 選擇 **+ New**。

    ![選取 Compute。](../../../../../../translated_images/zh-MO/06-01-select-compute.a29cff290b480252.webp)

1. 執行以下任務：

    - 選擇您想使用的 **Region**（區域）。
    - 將 **Virtual machine tier** 設為 **Dedicated**。
    - 將 **Virtual machine type** 設為 **GPU**。
    - 將 **Virtual machine size** 篩選器設為 **Select from all options**。
    - 選擇 **Virtual machine size** 為 **Standard_NC24ads_A100_v4**。

    ![建立叢集。](../../../../../../translated_images/zh-MO/06-02-create-cluster.f221b65ae1221d4e.webp)

1. 選擇 **Next**。

1. 執行以下任務：

    - 輸入 **Compute name**，必須是唯一值。
    - 將 **Minimum number of nodes** 設為 **0**。
    - 將 **Maximum number of nodes** 設為 **1**。
    - 將 **Idle seconds before scale down** 設為 **120**。

    ![建立叢集。](../../../../../../translated_images/zh-MO/06-03-create-cluster.4a54ba20914f3662.webp)

1. 選擇 **Create**。

#### 微調 Phi-3 模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇您建立的 Azure Machine Learning 工作區。

    ![選取您建立的工作區。](../../../../../../translated_images/zh-MO/06-04-select-workspace.a92934ac04f4f181.webp)

1. 執行以下任務：

    - 從左側標籤選擇 **Model catalog**。
    - 在 **search bar** 輸入 *phi-3-mini-4k*，並從出現的選項中選擇 **Phi-3-mini-4k-instruct**。

    ![輸入 phi-3-mini-4k。](../../../../../../translated_images/zh-MO/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. 從導覽選單中選擇 **Fine-tune**。

    ![選擇微調。](../../../../../../translated_images/zh-MO/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. 執行以下任務：

    - 將 **Select task type** 設為 **Chat completion**。
    - 選擇 **+ Select data** 來上傳 **Training data**。
    - 將驗證資料的上傳類型選擇為 **Provide different validation data**。
    - 選擇 **+ Select data** 以上傳 **Validation data**。

    ![填寫微調頁面。](../../../../../../translated_images/zh-MO/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> 您可以選擇 **Advanced settings** 自訂配置，如 **learning_rate** 及 **lr_scheduler_type**，以符合您的特定需求，優化微調流程。

1. 選擇 **Finish**。

1. 在本練習中，您成功使用 Azure Machine Learning 微調了 Phi-3 模型。請注意，微調過程可能需要相當長的時間。執行微調工作後，您必須等待其完成。您可以透過 Azure Machine Learning 工作區左側的 Jobs 標籤監控微調工作的狀態。在接下來的系列中，您將部署微調後的模型並將其與 Prompt flow 整合。

    ![觀看微調工作。](../../../../../../translated_images/zh-MO/06-08-output.2bd32e59930672b1.webp)

### 部署微調後的 Phi-3 模型

要將微調後的 Phi-3 模型整合到 Prompt flow，您需要先部署此模型，使其可用於即時推論。此過程包含註冊模型、建立線上端點及部署模型。

在本練習中，您將：

- 在 Azure Machine Learning 工作區中註冊微調後的模型。
- 建立線上端點。
- 部署已註冊的微調後 Phi-3 模型。

#### 註冊微調後的模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇您建立的 Azure Machine Learning 工作區。

    ![選取您建立的工作區。](../../../../../../translated_images/zh-MO/06-04-select-workspace.a92934ac04f4f181.webp)

1. 從左側標籤中選擇 **Models**。
1. 選擇 **+ Register**。
1. 選擇 **From a job output**。

    ![註冊模型。](../../../../../../translated_images/zh-MO/07-01-register-model.ad1e7cc05e4b2777.webp)

1. 選擇您建立的工作。

    ![選擇工作。](../../../../../../translated_images/zh-MO/07-02-select-job.3e2e1144cd6cd093.webp)

1. 選擇 **Next**。

1. 將 **Model type** 設為 **MLflow**。

1. 確認 **Job output** 已被選取，且系統會自動選取。

    ![選擇輸出。](../../../../../../translated_images/zh-MO/07-03-select-output.4cf1a0e645baea1f.webp)

2. 選擇 **Next**。

3. 選擇 **Register**。

    ![選擇註冊。](../../../../../../translated_images/zh-MO/07-04-register.fd82a3b293060bc7.webp)

4. 您可以在左側標籤的 **Models** 選單中查看已註冊的模型。

    ![已註冊的模型。](../../../../../../translated_images/zh-MO/07-05-registered-model.7db9775f58dfd591.webp)

#### 部署微調後的模型

1. 前往您建立的 Azure Machine Learning 工作區。

1. 選擇左側標籤的 **Endpoints**。

1. 從導覽選單選擇 **Real-time endpoints**。

    ![建立端點。](../../../../../../translated_images/zh-MO/07-06-create-endpoint.1ba865c606551f09.webp)

1. 選擇 **Create**。

1. 選擇您已註冊的模型。

    ![選擇已註冊的模型。](../../../../../../translated_images/zh-MO/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. 選擇 **Select**。

1. 執行以下任務：

    - 將 **Virtual machine** 設為 *Standard_NC6s_v3*。
    - 選擇您想使用的 **Instance count**，例如 *1*。
    - 將 **Endpoint** 設為 **New** 以建立新端點。
    - 輸入 **Endpoint name**，必須是唯一值。
    - 輸入 **Deployment name**，必須是唯一值。

    ![填寫部署設定。](../../../../../../translated_images/zh-MO/07-08-deployment-setting.43ddc4209e673784.webp)

1. 選擇 **Deploy**。

> [!WARNING]
> 為避免額外收費，請務必在 Azure Machine Learning 工作區中刪除建立的端點。
>

#### 在 Azure Machine Learning 工作區檢查部署狀態

1. 前往您建立的 Azure Machine Learning 工作區。

1. 選擇左側標籤的 **Endpoints**。

1. 選擇您建立的端點。

    ![選擇端點](../../../../../../translated_images/zh-MO/07-09-check-deployment.325d18cae8475ef4.webp)

1. 在此頁面，您可以在部署過程中管理端點。

> [!NOTE]
> 部署完成後，請確保 **Live traffic** 設為 **100%**。若非如此，請選擇 **Update traffic** 以調整流量設定。若流量設為 0%，您將無法測試模型。
>
> ![設定流量。](../../../../../../translated_images/zh-MO/07-10-set-traffic.085b847e5751ff3d.webp)
>

## 情境三：與 Prompt flow 整合並在 Microsoft Foundry 中與您的自訂模型聊天

### 將自訂 Phi-3 模型整合到 Prompt flow

成功部署微調模型後，您現在可以將它整合到 Prompt Flow，於即時應用中使用您的模型，啟用多樣互動任務與您的自訂 Phi-3 模型。

在本練習中，您將：

- 建立 Microsoft Foundry Hub。
- 建立 Microsoft Foundry 專案。
- 建立 Prompt flow。
- 為微調後的 Phi-3 模型新增自訂連線。
- 設定 Prompt flow 與您的自訂 Phi-3 模型聊天。

> [!NOTE]
> 您也可以使用 Azure ML Studio 與 Prompt flow 整合，兩者使用相同的整合流程。

#### 建立 Microsoft Foundry Hub

您需要先建立 Hub 才能建立專案。Hub 像是一個資源群組，允許您在 Microsoft Foundry 內組織和管理多個專案。
1. 訪問 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 從左側標籤選擇 **All hubs**。

1. 從導航選單中選擇 **+ New hub**。

    ![Create hub.](../../../../../../translated_images/zh-MO/08-01-create-hub.8f7dd615bb8d9834.webp)

1. 執行以下任務：

    - 輸入 **Hub name**。必須是一個唯一的值。
    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**（如有需要可建立新的）。
    - 選擇您想使用的 **Location**。
    - 選擇要使用的 **Connect Azure AI Services**（如有需要可建立新的）。
    - 選擇 **Connect Azure AI Search** 為 **Skip connecting**。

    ![Fill hub.](../../../../../../translated_images/zh-MO/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. 選擇 **Next**。

#### 建立 Microsoft Foundry 專案

1. 在您建立的 Hub 中，從左側標籤選擇 **All projects**。

1. 從導航選單中選擇 **+ New project**。

    ![Select new project.](../../../../../../translated_images/zh-MO/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. 輸入 **Project name**。必須是唯一的值。

    ![Create project.](../../../../../../translated_images/zh-MO/08-05-create-project.4d97f0372f03375a.webp)

1. 選擇 **Create a project**。

#### 為微調後的 Phi-3 模型新增自訂連線

要將您的自訂 Phi-3 模型整合至 Prompt flow 中，您需要將模型的端點與金鑰儲存於自訂連線中。此設定確保您在 Prompt flow 中可以存取您的自訂 Phi-3 模型。

#### 設定微調後的 Phi-3 模型的 api key 與端點 uri

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 導航至您建立的 Azure 機器學習工作區。

1. 從左側標籤選擇 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/zh-MO/08-06-select-endpoints.aff38d453bcf9605.webp)

1. 選擇您建立的端點。

    ![Select endpoints.](../../../../../../translated_images/zh-MO/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. 從導航選單選擇 **Consume**。

1. 複製您的 **REST endpoint** 和 **Primary key**。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/zh-MO/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### 新增自訂連線

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 導航至您建立的 Microsoft Foundry 專案。

1. 在您建立的專案中，從左側標籤選擇 **Settings**。

1. 選擇 **+ New connection**。

    ![Select new connection.](../../../../../../translated_images/zh-MO/08-09-select-new-connection.02eb45deadc401fc.webp)

1. 從導航選單中選擇 **Custom keys**。

    ![Select custom keys.](../../../../../../translated_images/zh-MO/08-10-select-custom-keys.856f6b2966460551.webp)

1. 執行以下任務：

    - 選擇 **+ Add key value pairs**。
    - 在鍵名輸入 **endpoint**，並將您從 Azure ML Studio 複製的端點貼入值欄位。
    - 再次選擇 **+ Add key value pairs**。
    - 鍵名輸入 **key**，並將您從 Azure ML Studio 複製的金鑰貼入值欄位。
    - 新增金鑰後，選擇 **is secret** 以防止金鑰外洩。

    ![Add connection.](../../../../../../translated_images/zh-MO/08-11-add-connection.785486badb4d2d26.webp)

1. 選擇 **Add connection**。

#### 建立 Prompt flow

您已在 Microsoft Foundry 中新增自訂連線，現在讓我們使用以下步驟建立 Prompt flow。之後，您會將此 Prompt flow 連結到自訂連線，從而在 Prompt flow 裡使用微調後的模型。

1. 導航至您建立的 Microsoft Foundry 專案。

1. 從左側標籤選擇 **Prompt flow**。

1. 從導航選單選擇 **+ Create**。

    ![Select Promptflow.](../../../../../../translated_images/zh-MO/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. 從導航選單選擇 **Chat flow**。

    ![Select chat flow.](../../../../../../translated_images/zh-MO/08-13-select-flow-type.2ec689b22da32591.webp)

1. 輸入要使用的 **Folder name**。

    ![Enter name.](../../../../../../translated_images/zh-MO/08-14-enter-name.ff9520fefd89f40d.webp)

2. 選擇 **Create**。

#### 設定 Prompt flow 與您的自訂 Phi-3 模型聊天

您需要將微調後的 Phi-3 模型整合到 Prompt flow 中。由於現有的 Prompt flow 不適用於此目的，您必須重新設計 Prompt flow 以啟用自訂模型的整合。

1. 在 Prompt flow 中，執行以下任務以重建現有的流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 檔案中所有現有程式碼。
    - 將以下程式碼新增到 *flow.dag.yml* 檔案中。

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

    ![Select raw file mode.](../../../../../../translated_images/zh-MO/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. 將以下程式碼新增至 *integrate_with_promptflow.py* 檔案，用於在 Prompt flow 中使用自訂的 Phi-3 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 設置日誌記錄
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
            
            # 記錄完整的 JSON 回應
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

    ![Paste prompt flow code.](../../../../../../translated_images/zh-MO/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> 如需在 Microsoft Foundry 中使用 Prompt flow 的詳細資訊，請參考 [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input**、**Chat output** 以啟用與您的模型聊天。

    ![Input Output.](../../../../../../translated_images/zh-MO/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. 現在您已準備好與自訂的 Phi-3 模型聊天。接下來的練習中，您將學習如何啟動 Prompt flow 並使用它與微調過的 Phi-3 模型聊天。

> [!NOTE]
>
> 重建後的流程應該長得像下面這張圖片：
>
> ![Flow example.](../../../../../../translated_images/zh-MO/08-18-graph-example.d6457533952e690c.webp)
>

### 與您的自訂 Phi-3 模型聊天

現在，您已微調並將自訂 Phi-3 模型整合至 Prompt flow，已可開始與它互動。本練習將引導您設定並啟動與模型聊天。照著步驟操作，您將能充分活用微調後的 Phi-3 模型的多元功能與對話能力。

- 使用 Prompt flow 與您的自訂 Phi-3 模型聊天。

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 啟動 Prompt flow。

    ![Start compute session.](../../../../../../translated_images/zh-MO/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. 選擇 **Validate and parse input** 更新參數。

    ![Validate input.](../../../../../../translated_images/zh-MO/09-02-validate-input.317c76ef766361e9.webp)

1. 選擇 **connection** 的 **Value**，對應您建立的自訂連線。例如，*connection*。

    ![Connection.](../../../../../../translated_images/zh-MO/09-03-select-connection.99bdddb4b1844023.webp)

#### 與您的自訂模型聊天

1. 選擇 **Chat**。

    ![Select chat.](../../../../../../translated_images/zh-MO/09-04-select-chat.61936dce6612a1e6.webp)

1. 以下為結果範例：您現在可以與自訂 Phi-3 模型聊天。建議您根據用於微調的資料提問。

    ![Chat with prompt flow.](../../../../../../translated_images/zh-MO/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能存在錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->