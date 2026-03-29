# 在 Microsoft Foundry 中使用 Prompt flow 微調並整合自訂 Phi-3 模型

此端對端（E2E）範例基於 Microsoft 技術社群中的指南「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」。本指南介紹微調、部署及整合自訂 Phi-3 模型與 Microsoft Foundry 中的 Prompt flow 流程。
與需要本地執行程式碼的 E2E 範例「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」不同，本教學專注於在 Azure AI / ML Studio 內部的模型微調及整合。

## 概述

在此 E2E 範例中，您將學習如何微調 Phi-3 模型，並整合到 Microsoft Foundry 中的 Prompt flow。透過 Azure AI / ML Studio，您將建立部署及使用自訂 AI 模型的工作流程。此 E2E 範例分為三個場景：

**場景 1：設定 Azure 資源及準備微調**

**場景 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 部署**

**場景 3：與 Prompt flow 整合並在 Microsoft Foundry 中與您的自訂模型聊天**

以下是本 E2E 範例的總覽。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/zh-TW/00-01-architecture.198ba0f1ae6d841a.webp)

### 目錄

1. **[場景 1：設定 Azure 資源及準備微調](#場景-1：設定-azure-資源及準備微調)**
    - [建立 Azure Machine Learning 工作區](#建立-azure-machine-learning-工作區)
    - [申請 Azure 訂閱的 GPU 配額](#申請-azure-訂閱的-gpu-配額)
    - [新增角色指派](#新增角色指派)
    - [設定專案](#設定專案)
    - [準備微調的資料集](#準備微調用的資料集)

1. **[場景 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 部署](#情境-2：在-azure-machine-learning-studio-微調-phi-3-模型並部署)**
    - [微調 Phi-3 模型](#微調-phi-3-模型)
    - [部署微調後的 Phi-3 模型](#部署微調後的-phi-3-模型)

1. **[場景 3：與 Prompt flow 整合並在 Microsoft Foundry 中與您的自訂模型聊天](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [將自訂 Phi-3 模型與 Prompt flow 整合](#將自訂的-phi-3-模型與-prompt-flow-整合)
    - [與自訂 Phi-3 模型聊天](#與您的自訂-phi-3-模型聊天)

## 場景 1：設定 Azure 資源及準備微調

### 建立 Azure Machine Learning 工作區

1. 在入口網站頁面頂端的<strong>搜尋列</strong>中輸入 *azure machine learning*，並在出現的選項中選擇 **Azure Machine Learning**。

    ![Type azure machine learning.](../../../../../../translated_images/zh-TW/01-01-type-azml.acae6c5455e67b4b.webp)

2. 從導覽選單中選擇 **+ 建立**。

3. 從導覽選單中選擇 <strong>新工作區</strong>。

    ![Select new workspace.](../../../../../../translated_images/zh-TW/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. 執行以下操作：

    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如有需要可新建）。
    - 輸入 <strong>工作區名稱</strong>，必須是唯一值。
    - 選擇您想使用的 <strong>區域</strong>。
    - 選擇要使用的 <strong>儲存帳戶</strong>（如有需要可新建）。
    - 選擇要使用的 <strong>金鑰保管庫</strong>（如有需要可新建）。
    - 選擇要使用的 <strong>應用程式監控</strong>（如有需要可新建）。
    - 選擇要使用的 <strong>容器登錄庫</strong>（如有需要可新建）。

    ![Fill azure machine learning.](../../../../../../translated_images/zh-TW/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. 選擇 **審查 + 建立**。

6. 選擇 <strong>建立</strong>。

### 申請 Azure 訂閱的 GPU 配額

在本教學中，您將學習如何使用 GPU 來微調及部署 Phi-3 模型。微調時會使用 *Standard_NC24ads_A100_v4* GPU，需申請配額。部署時會使用 *Standard_NC6s_v3* GPU，也需申請配額。

> [!NOTE]
>
> 只有按使用量付費的訂閱（標準訂閱類型）可獲得 GPU 配額，目前效益訂閱不支援。
>

1. 造訪 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 申請 *Standard NCADSA100v4 Family* 配額，請執行以下步驟：

    - 從左側標籤選擇 <strong>配額</strong>。
    - 選擇要使用的 <strong>虛擬機器系列</strong>，例如選擇包含 *Standard_NC24ads_A100_v4* GPU 的 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**。
    - 從導覽列選擇 <strong>申請配額</strong>。

        ![Request quota.](../../../../../../translated_images/zh-TW/02-02-request-quota.c0428239a63ffdd5.webp)

    - 在申請配額頁面中，輸入您想使用的 <strong>新核心限制</strong>，例如 24。
    - 在申請配額頁面中選擇 <strong>提交</strong> 以申請 GPU 配額。

1. 申請 *Standard NCSv3 Family* 配額，請執行以下步驟：

    - 從左側標籤選擇 <strong>配額</strong>。
    - 選擇要使用的 <strong>虛擬機器系列</strong>，例如選擇包含 *Standard_NC6s_v3* GPU 的 **Standard NCSv3 Family Cluster Dedicated vCPUs**。
    - 從導覽列選擇 <strong>申請配額</strong>。
    - 在申請配額頁面中，輸入您想使用的 <strong>新核心限制</strong>，例如 24。
    - 在申請配額頁面中選擇 <strong>提交</strong> 以申請 GPU 配額。

### 新增角色指派

為了微調及部署您的模型，您必須先建立使用者指派的託管識別（User Assigned Managed Identity，UAI），並指派適當權限。此 UAI 將用於部署期間的身分驗證。

#### 建立使用者指派的託管識別（UAI）

1. 在入口網站頁面頂端的<strong>搜尋列</strong>中輸入 *managed identities*，並在出現的選項中選擇 **Managed Identities**。

    ![Type managed identities.](../../../../../../translated_images/zh-TW/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. 選擇 **+ 建立**。

    ![Select create.](../../../../../../translated_images/zh-TW/03-02-select-create.92bf8989a5cd98f2.webp)

1. 執行以下操作：

    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如有需要可新建）。
    - 選擇您想使用的 <strong>區域</strong>。
    - 輸入 <strong>名稱</strong>，必須是唯一值。

    ![Select create.](../../../../../../translated_images/zh-TW/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. 選擇 **審查 + 建立**。

1. 選擇 **+ 建立**。

#### 新增貢獻者角色指派至託管識別

1. 導覽至您建立的託管識別資源。

1. 從左側標籤選擇 **Azure 角色指派**。

1. 從導覽列選擇 **+新增角色指派**。

1. 在新增角色指派頁面中執行以下操作：
    - 將 <strong>範圍</strong>設為 <strong>資源群組</strong>。
    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>。
    - 將 <strong>角色</strong>設為 **貢獻者 (Contributor)**。

    ![Fill contributor role.](../../../../../../translated_images/zh-TW/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. 選擇 <strong>儲存</strong>。

#### 新增 Storage Blob Data Reader 角色指派至託管識別

1. 在入口網站頁面頂端的<strong>搜尋列</strong>中輸入 *storage accounts*，並在出現的選項中選擇 **Storage accounts**。

    ![Type storage accounts.](../../../../../../translated_images/zh-TW/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. 選擇與您建立的 Azure Machine Learning 工作區關聯的儲存帳戶。例如，*finetunephistorage*。

1. 執行以下操作以進入新增角色指派頁面：

    - 導覽至您建立的 Azure 儲存帳戶。
    - 從左側標籤選擇 **存取控制 (IAM)**。
    - 從導覽列選擇 **+ 新增**。
    - 選擇 <strong>新增角色指派</strong>。

    ![Add role.](../../../../../../translated_images/zh-TW/03-06-add-role.353ccbfdcf0789c2.webp)

1. 在新增角色指派頁面中執行以下操作：

    - 在角色頁面的<strong>搜尋列</strong>輸入 *Storage Blob Data Reader*，並從出現的選項中選擇 **Storage Blob Data Reader**。
    - 在角色頁面選擇 <strong>下一步</strong>。
    - 在成員頁面，將 <strong>指派存取權給</strong> 設為 <strong>託管識別</strong>。
    - 在成員頁面選擇 **+ 選取成員**。
    - 在選取託管識別頁面選擇您的 Azure <strong>訂閱</strong>。
    - 在選取託管識別頁面選擇 <strong>託管識別</strong> 類別。
    - 在選取託管識別頁面選擇您建立的託管識別。例如，*finetunephi-managedidentity*。
    - 在選取託管識別頁面選擇 <strong>選取</strong>。

    ![Select managed identity.](../../../../../../translated_images/zh-TW/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. 選擇 **審查 + 指派**。

#### 新增 AcrPull 角色指派至託管識別

1. 在入口網站頁面頂端的<strong>搜尋列</strong>中輸入 *container registries*，並在出現的選項中選擇 **Container registries**。

    ![Type container registries.](../../../../../../translated_images/zh-TW/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. 選擇與 Azure Machine Learning 工作區相關聯的容器登錄庫。例如，*finetunephicontainerregistry*

1. 執行以下操作以進入新增角色指派頁面：

    - 從左側標籤選擇 **存取控制 (IAM)**。
    - 從導覽列選擇 **+ 新增**。
    - 選擇 <strong>新增角色指派</strong>。

1. 在新增角色指派頁面中執行以下操作：

    - 在角色頁面的<strong>搜尋列</strong>輸入 *AcrPull*，並從出現的選項中選擇 **AcrPull**。
    - 在角色頁面選擇 <strong>下一步</strong>。
    - 在成員頁面，將 <strong>指派存取權給</strong> 設為 <strong>託管識別</strong>。
    - 在成員頁面選擇 **+ 選取成員**。
    - 在選取託管識別頁面選擇您的 Azure <strong>訂閱</strong>。
    - 在選取託管識別頁面選擇 <strong>託管識別</strong> 類別。
    - 在選取託管識別頁面選擇您建立的託管識別。例如，*finetunephi-managedidentity*。
    - 在選取託管識別頁面選擇 <strong>選取</strong>。
    - 選擇 **審查 + 指派**。

### 設定專案

為下載微調所需的資料集，您將設定本地環境。

在此練習中，您將

- 建立工作資料夾
- 建立虛擬環境
- 安裝必須的套件
- 建立 *download_dataset.py* 檔案以下載資料集

#### 建立工作資料夾

1. 開啟終端機視窗，輸入以下指令，在預設路徑建立名為 *finetune-phi* 的資料夾。

    ```console
    mkdir finetune-phi
    ```

2. 在終端機輸入以下指令，切換到您建立的 *finetune-phi* 資料夾。

    ```console
    cd finetune-phi
    ```

#### 建立虛擬環境

1. 在終端機輸入以下指令，建立名為 *.venv* 的虛擬環境。
    ```console
    python -m venv .venv
    ```

2. 在終端機中輸入以下命令以啟用虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 如果成功，您應該會在命令提示字元前看到 *(.venv)*。

#### 安裝所需的套件

1. 在終端機中輸入以下命令以安裝所需的套件。

    ```console
    pip install datasets==2.19.1
    ```

#### 建立 `donload_dataset.py`

> [!NOTE]
> 完整的資料夾結構：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. 開啟 **Visual Studio Code**。

1. 從功能表列選擇 <strong>檔案</strong>。

1. 選擇 <strong>開啟資料夾</strong>。

1. 選擇您已建立的 *finetune-phi* 資料夾，位於 *C:\Users\yourUserName\finetune-phi*。

    ![選擇您建立的資料夾。](../../../../../../translated_images/zh-TW/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. 在 Visual Studio Code 的左側窗格中，按右鍵並選擇 <strong>新增檔案</strong>，建立一個名稱為 *download_dataset.py* 的新檔案。

    ![建立新檔案。](../../../../../../translated_images/zh-TW/04-02-create-new-file.cf9a330a3a9cff92.webp)

### 準備微調用的資料集

在本練習中，您將執行 *download_dataset.py* 檔案以下載 *ultrachat_200k* 資料集到您的本地環境。接著，您將使用此資料集在 Azure Machine Learning 中微調 Phi-3 模型。

本練習中，您將：

- 在 *download_dataset.py* 檔案中新增程式碼以下載資料集。
- 執行 *download_dataset.py* 檔案以下載資料集到本地環境。

#### 使用 *download_dataset.py* 下載資料集

1. 在 Visual Studio Code 中打開 *download_dataset.py* 檔案。

1. 在 *download_dataset.py* 檔案中加入以下程式碼。

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # 載入具有指定名稱、配置和切分比例的資料集
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # 將資料集分割為訓練集和測試集（80%訓練，20%測試）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 如果目錄不存在則建立目錄
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以寫入模式打開檔案
        with open(filepath, 'w', encoding='utf-8') as f:
            # 迭代資料集中的每一筆紀錄
            for record in dataset:
                # 將紀錄以 JSON 物件格式轉出並寫入檔案
                json.dump(record, f)
                # 寫入換行字元以分隔紀錄
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 載入並切分帶有特定配置和切分比例的 ULTRACHAT_200k 資料集
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 從切分中擷取訓練集和測試集
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 將訓練集儲存為 JSONL 檔案
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # 將測試集儲存為另一個 JSONL 檔案
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 在終端機中輸入以下命令，以執行腳本並將資料集下載到您的本地環境。

    ```console
    python download_dataset.py
    ```

1. 確認資料集已成功儲存到您本地的 *finetune-phi/data* 目錄中。

> [!NOTE]
>
> #### 關於資料集大小與微調時間的說明
>
> 在本教學中，您僅使用資料集的 1% (`split='train[:1%]'`)，這大幅減少了資料量，加快上傳及微調的速度。您可以調整此百分比，以取得訓練時間與模型效能的最佳平衡。使用較小的資料子集，可減少微調所需的時間，使教學過程更加容易掌控。

## 情境 2：在 Azure Machine Learning Studio 微調 Phi-3 模型並部署

### 微調 Phi-3 模型

在本練習中，您將在 Azure Machine Learning Studio 中微調 Phi-3 模型。

本練習中，您將：

- 建立用於微調的計算叢集。
- 在 Azure Machine Learning Studio 中微調 Phi-3 模型。

#### 建立用於微調的計算叢集

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 從左側分頁中選擇 <strong>計算</strong>。

1. 從導航選單中選擇 <strong>計算叢集</strong>。

1. 選擇 **+ 新增**。

    ![選擇計算。](../../../../../../translated_images/zh-TW/06-01-select-compute.a29cff290b480252.webp)

1. 執行下列操作：

    - 選擇您要使用的 <strong>地區</strong>。
    - 將 <strong>虛擬機層級</strong> 設定為 <strong>專用</strong>。
    - 將 <strong>虛擬機類型</strong> 選為 **GPU**。
    - 在 <strong>虛擬機大小</strong> 過濾器中選擇 <strong>從所有選項中選擇</strong>。
    - 將 <strong>虛擬機大小</strong> 設定為 **Standard_NC24ads_A100_v4**。

    ![建立叢集。](../../../../../../translated_images/zh-TW/06-02-create-cluster.f221b65ae1221d4e.webp)

1. 選擇 <strong>下一步</strong>。

1. 執行下列操作：

    - 輸入 <strong>計算名稱</strong>，名稱必須是唯一的。
    - 將 <strong>節點最小數量</strong> 設為 **0**。
    - 將 <strong>節點最大數量</strong> 設為 **1**。
    - 將 <strong>閒置秒數後縮減擴展</strong> 設為 **120**。

    ![建立叢集。](../../../../../../translated_images/zh-TW/06-03-create-cluster.4a54ba20914f3662.webp)

1. 選擇 <strong>建立</strong>。

#### 微調 Phi-3 模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇您建立的 Azure Machine Learning 工作區。

    ![選擇您建立的工作區。](../../../../../../translated_images/zh-TW/06-04-select-workspace.a92934ac04f4f181.webp)

1. 執行以下操作：

    - 從左側選單選擇 <strong>模型目錄</strong>。
    - 在 <strong>搜尋列</strong> 輸入 *phi-3-mini-4k*，並從出現的選項中選擇 **Phi-3-mini-4k-instruct**。

    ![輸入 phi-3-mini-4k。](../../../../../../translated_images/zh-TW/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. 從導航選單選擇 <strong>微調</strong>。

    ![選擇微調。](../../../../../../translated_images/zh-TW/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. 執行以下操作：

    - 將 <strong>選擇任務類型</strong> 設為 <strong>聊天完成</strong>。
    - 選擇 **+ 選擇資料** 來上傳 <strong>訓練資料</strong>。
    - 將驗證資料上傳類型設為 <strong>提供不同的驗證資料</strong>。
    - 選擇 **+ 選擇資料** 以上傳 <strong>驗證資料</strong>。

    ![填寫微調頁面。](../../../../../../translated_images/zh-TW/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> 您可以選擇 <strong>進階設定</strong>，自訂例如 **learning_rate** 與 **lr_scheduler_type** 等參數，以根據您的需求優化微調過程。

1. 選擇 <strong>完成</strong>。

1. 在本練習中，您已成功利用 Azure Machine Learning 進行 Phi-3 模型的微調。請注意，微調過程可能需要相當長的時間。執行微調任務後，您需要等待其完成。您可以透過 Azure Machine Learning 工作區左側的「工作」分頁監控微調任務狀態。在接下來的系列中，您將部署微調後的模型並將其整合至 Prompt flow。

    ![查看微調工作。](../../../../../../translated_images/zh-TW/06-08-output.2bd32e59930672b1.webp)

### 部署微調後的 Phi-3 模型

為了將微調後的 Phi-3 模型整合至 Prompt flow，您需要部署該模型，使其能被實時推論存取。此流程包含註冊模型、建立線上端點，以及部署模型。

本練習中，您將：

- 在 Azure Machine Learning 工作區註冊微調後的模型。
- 建立線上端點。
- 部署已註冊的微調 Phi-3 模型。

#### 註冊微調後的模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇您建立的 Azure Machine Learning 工作區。

    ![選擇您建立的工作區。](../../../../../../translated_images/zh-TW/06-04-select-workspace.a92934ac04f4f181.webp)

1. 從左側分頁選擇 <strong>模型</strong>。
1. 選擇 **+ 註冊**。
1. 選擇 <strong>從工作輸出</strong>。

    ![註冊模型。](../../../../../../translated_images/zh-TW/07-01-register-model.ad1e7cc05e4b2777.webp)

1. 選擇您建立的工作。

    ![選擇工作。](../../../../../../translated_images/zh-TW/07-02-select-job.3e2e1144cd6cd093.webp)

1. 選擇 <strong>下一步</strong>。

1. 將 <strong>模型類型</strong> 設為 **MLflow**。

1. 確認已選擇 <strong>工作輸出</strong>，此選項應自動勾選。

    ![選擇輸出。](../../../../../../translated_images/zh-TW/07-03-select-output.4cf1a0e645baea1f.webp)

2. 選擇 <strong>下一步</strong>。

3. 選擇 <strong>註冊</strong>。

    ![選擇註冊。](../../../../../../translated_images/zh-TW/07-04-register.fd82a3b293060bc7.webp)

4. 您可以透過左側分頁中的 <strong>模型</strong> 功能表查看您已註冊的模型。

    ![已註冊模型。](../../../../../../translated_images/zh-TW/07-05-registered-model.7db9775f58dfd591.webp)

#### 部署微調後的模型

1. 前往您建立的 Azure Machine Learning 工作區。

1. 從左側分頁選擇 <strong>端點</strong>。

1. 從導航選單中選擇 <strong>即時端點</strong>。

    ![建立端點。](../../../../../../translated_images/zh-TW/07-06-create-endpoint.1ba865c606551f09.webp)

1. 選擇 <strong>建立</strong>。

1. 選擇您之前註冊的模型。

    ![選擇已註冊模型。](../../../../../../translated_images/zh-TW/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. 選擇 <strong>選擇</strong>。

1. 執行以下設置：

    - 將 <strong>虛擬機器</strong> 設定為 *Standard_NC6s_v3*。
    - 選擇您想使用的 <strong>實例數量</strong>，例如 *1*。
    - 將 <strong>端點</strong> 設定為 <strong>新建</strong>，來建立新的端點。
    - 輸入 <strong>端點名稱</strong>，必須是唯一值。
    - 輸入 <strong>部署名稱</strong>，必須是唯一值。

    ![填寫部署設定。](../../../../../../translated_images/zh-TW/07-08-deployment-setting.43ddc4209e673784.webp)

1. 選擇 <strong>部署</strong>。

> [!WARNING]
> 為避免產生額外費用，請務必在 Azure Machine Learning 工作區中刪除您建立的端點。
>

#### 在 Azure Machine Learning 工作區中檢查部署狀態

1. 前往您建立的 Azure Machine Learning 工作區。

1. 從左側分頁選擇 <strong>端點</strong>。

1. 選取您建立的端點。

    ![選擇端點](../../../../../../translated_images/zh-TW/07-09-check-deployment.325d18cae8475ef4.webp)

1. 在此頁面上，您可以管理部署過程中的端點。

> [!NOTE]
> 部署完成後，請確保 <strong>即時流量</strong> 設定為 **100%**。如果不是，請選擇 <strong>更新流量</strong> 來調整流量設定。若流量設定為 0%，將無法測試模型。
>
> ![設定流量。](../../../../../../translated_images/zh-TW/07-10-set-traffic.085b847e5751ff3d.webp)
>

## 情境 3：與 Prompt flow 整合並在 Microsoft Foundry 中使用您的自訂模型聊天

### 將自訂的 Phi-3 模型與 Prompt flow 整合

成功部署微調模型後，您可以將它整合到 Prompt Flow，以便在實時應用程式中使用您的模型，實現各種互動任務，搭配您的自訂 Phi-3 模型。

本練習中，您將：

- 建立 Microsoft Foundry Hub。
- 建立 Microsoft Foundry 專案。
- 建立 Prompt flow。
- 為微調後的 Phi-3 模型新增自訂連線。
- 設定 Prompt flow 與您的自訂 Phi-3 模型進行聊天。

> [!NOTE]
> 您也可以透過 Azure ML Studio 進行 Promptflow 的整合，相同的整合流程同樣適用於 Azure ML Studio。

#### 建立 Microsoft Foundry Hub

在建立專案之前，您需要先建立一個 Hub。Hub 就像資源群組，可讓您在 Microsoft Foundry 中組織和管理多個專案。
1. 訪問 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 從左側標籤選擇 <strong>所有中心</strong>。

1. 從導覽選單選擇 **+ 新增中心**。

    ![建立中心。](../../../../../../translated_images/zh-TW/08-01-create-hub.8f7dd615bb8d9834.webp)

1. 執行以下任務：

    - 輸入 <strong>中心名稱</strong>，必須是唯一值。
    - 選擇您的 Azure <strong>訂閱</strong>。
    - 選擇要使用的 <strong>資源群組</strong>（如有需要可建立新的）。
    - 選擇您想要使用的 <strong>位置</strong>。
    - 選擇要使用的 **連接 Azure AI 服務**（如有需要可建立新的）。
    - 選擇 **連接 Azure AI 搜尋**，選擇 <strong>跳過連接</strong>。

    ![填寫中心資訊。](../../../../../../translated_images/zh-TW/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. 選擇 <strong>下一步</strong>。

#### 建立 Microsoft Foundry 專案

1. 在您建立的中心中，從左側標籤選擇 <strong>所有專案</strong>。

1. 從導覽選單選擇 **+ 新增專案**。

    ![選擇新增專案。](../../../../../../translated_images/zh-TW/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. 輸入 <strong>專案名稱</strong>，必須是唯一值。

    ![建立專案。](../../../../../../translated_images/zh-TW/08-05-create-project.4d97f0372f03375a.webp)

1. 選擇 <strong>建立專案</strong>。

#### 新增自訂連接以使用微調後的 Phi-3 模型

要將您的自訂 Phi-3 模型整合進 Prompt flow，您需要將模型的端點與金鑰儲存在自訂連接中。此設定可確保您在 Prompt flow 中存取自訂的 Phi-3 模型。

#### 設定微調後 Phi-3 模型的 api 金鑰與端點 URI

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 導覽至您建立的 Azure 機器學習工作區。

1. 從左側標籤選擇 <strong>端點</strong>。

    ![選擇端點。](../../../../../../translated_images/zh-TW/08-06-select-endpoints.aff38d453bcf9605.webp)

1. 選擇您建立的端點。

    ![選擇已建立的端點。](../../../../../../translated_images/zh-TW/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. 從導覽選單選擇 <strong>使用</strong>。

1. 複製您的 **REST 端點** 及 <strong>主要金鑰</strong>。

    ![複製 api 金鑰及端點 URI。](../../../../../../translated_images/zh-TW/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### 新增自訂連接

1. 訪問 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 導覽至您建立的 Microsoft Foundry 專案。

1. 在您建立的專案中，從左側標籤選擇 <strong>設定</strong>。

1. 選擇 **+ 新增連接**。

    ![選擇新增連接。](../../../../../../translated_images/zh-TW/08-09-select-new-connection.02eb45deadc401fc.webp)

1. 從導覽選單選擇 <strong>自訂金鑰</strong>。

    ![選擇自訂金鑰。](../../../../../../translated_images/zh-TW/08-10-select-custom-keys.856f6b2966460551.webp)

1. 執行以下操作：

    - 選擇 **+ 新增鍵值對**。
    - 鍵名稱輸入 **endpoint**，並將您從 Azure ML Studio 複製的端點貼到值欄位。
    - 再次選擇 **+ 新增鍵值對**。
    - 鍵名稱輸入 **key**，並將您從 Azure ML Studio 複製的金鑰貼到值欄位。
    - 新增鍵值後，選擇 <strong>是秘密</strong>，以防止金鑰被外洩。

    ![新增連接。](../../../../../../translated_images/zh-TW/08-11-add-connection.785486badb4d2d26.webp)

1. 選擇 <strong>新增連接</strong>。

#### 建立 Prompt flow

您已在 Microsoft Foundry 新增自訂連接。現在，我們進行以下步驟來建立 Prompt flow。之後，您會將此 Prompt flow 連接至自訂連接，以便在 Prompt flow 中使用微調後的模型。

1. 導覽至您建立的 Microsoft Foundry 專案。

1. 從左側標籤選擇 **Prompt flow**。

1. 從導覽選單選擇 **+ 建立**。

    ![選擇 Prompt flow。](../../../../../../translated_images/zh-TW/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. 從導覽選單選擇 <strong>聊天流程</strong>。

    ![選擇聊天流程。](../../../../../../translated_images/zh-TW/08-13-select-flow-type.2ec689b22da32591.webp)

1. 輸入要使用的 <strong>資料夾名稱</strong>。

    ![輸入名稱。](../../../../../../translated_images/zh-TW/08-14-enter-name.ff9520fefd89f40d.webp)

2. 選擇 <strong>建立</strong>。

#### 設定 Prompt flow 與您的自訂 Phi-3 模型聊天

您需要將微調後的 Phi-3 模型整合進 Prompt flow。然而，現有的 Prompt flow 並非為此設計。因此，您必須重新設計 Prompt flow，以啟用自訂模型整合。

1. 在 Prompt flow 中，執行以下任務以重建現有流程：

    - 選擇 <strong>原始檔案模式</strong>。
    - 刪除 *flow.dag.yml* 檔案中的所有現有程式碼。
    - 在 *flow.dag.yml* 檔案中加入以下程式碼。

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

    - 選擇 <strong>儲存</strong>。

    ![選擇原始檔案模式。](../../../../../../translated_images/zh-TW/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. 在 *integrate_with_promptflow.py* 檔案中加入以下程式碼，以便在 Prompt flow 中使用自訂的 Phi-3 模型。

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

        # "connection" 是自定義連線的名稱，"endpoint"、"key" 是自定義連線中的鍵
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

    ![貼上 Prompt flow 程式碼。](../../../../../../translated_images/zh-TW/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> 有關在 Microsoft Foundry 中使用 Prompt flow 的詳細資訊，請參閱 [Microsoft Foundry 中的 Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 <strong>聊天輸入</strong>、<strong>聊天輸出</strong>，以啟用與模型的聊天。

    ![輸入與輸出。](../../../../../../translated_images/zh-TW/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. 現在您已準備好與自訂的 Phi-3 模型聊天。在下一個練習中，您將學習如何啟動 Prompt flow 並使用它與微調後的 Phi-3 模型聊天。

> [!NOTE]
>
> 重建的流程應如下圖所示：
>
> ![流程示例。](../../../../../../translated_images/zh-TW/08-18-graph-example.d6457533952e690c.webp)
>

### 與您的自訂 Phi-3 模型聊天

現在您已微調並將自訂 Phi-3 模型整合到 Prompt flow，即可開始與它互動。本練習將指導您如何設定並啟動與模型的聊天。依照步驟操作，您將能充分發揮微調後 Phi-3 模型在各種任務和對話中的能力。

- 使用 Prompt flow 與您的自訂 Phi-3 模型聊天。

#### 啟動 Prompt flow

1. 選擇 <strong>啟動計算會話</strong> 以啟動 Prompt flow。

    ![啟動計算會話。](../../../../../../translated_images/zh-TW/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. 選擇 <strong>驗證並解析輸入</strong> 以更新參數。

    ![驗證輸入。](../../../../../../translated_images/zh-TW/09-02-validate-input.317c76ef766361e9.webp)

1. 選擇 **connection** 的 <strong>值</strong>，該連接為您所建立的自訂連接。例如，*connection*。

    ![連接。](../../../../../../translated_images/zh-TW/09-03-select-connection.99bdddb4b1844023.webp)

#### 與自訂模型聊天

1. 選擇 <strong>聊天</strong>。

    ![選擇聊天。](../../../../../../translated_images/zh-TW/09-04-select-chat.61936dce6612a1e6.webp)

1. 以下是結果範例：現在您可以與自訂的 Phi-3 模型聊天。建議根據用於微調的資料來提問。

    ![與 Prompt flow 聊天。](../../../../../../translated_images/zh-TW/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->