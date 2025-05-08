<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-08T05:44:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hk"
}
-->
# Fine-tune 同整合自訂 Phi-3 模型喺 Azure AI Foundry 嘅 Prompt flow

呢個端到端 (E2E) 範例係根據 Microsoft Tech Community 嘅指引「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」而嚟，介紹點樣喺 Azure AI Foundry 用 Prompt flow 去微調、部署同整合自訂 Phi-3 模型。唔同於需要本地運行代碼嘅 E2E 範例「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」，呢個教學完全專注喺 Azure AI / ML Studio 入面微調同整合你嘅模型。

## 概覽

喺呢個 E2E 範例，你會學識點樣微調 Phi-3 模型，同喺 Azure AI Foundry 用 Prompt flow 整合佢。利用 Azure AI / ML Studio，你會建立一個工作流程去部署同使用自訂 AI 模型。呢個 E2E 範例分為三個場景：

**場景 1：設定 Azure 資源同準備微調**

**場景 2：微調 Phi-3 模型同喺 Azure Machine Learning Studio 部署**

**場景 3：整合同 Prompt flow 聊天，喺 Azure AI Foundry 用你嘅自訂模型**

以下係呢個 E2E 範例嘅概覽。

![Phi-3-FineTuning_PromptFlow_Integration 概覽.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.hk.png)

### 目錄

1. **[場景 1：設定 Azure 資源同準備微調](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [建立 Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [申請 Azure 訂閱嘅 GPU 配額](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [新增角色指派](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [設定專案](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [準備微調用嘅資料集](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[場景 2：微調 Phi-3 模型同喺 Azure Machine Learning Studio 部署](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [微調 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署微調後嘅 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[場景 3：整合同 Prompt flow 聊天，喺 Azure AI Foundry 用你嘅自訂模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [整合自訂 Phi-3 模型到 Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [用你嘅自訂 Phi-3 模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 場景 1：設定 Azure 資源同準備微調

### 建立 Azure Machine Learning Workspace

1. 喺入口網站頁面頂部嘅 **搜尋欄** 入面打 *azure machine learning*，然後喺選項中揀 **Azure Machine Learning**。

    ![打 azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.hk.png)

2. 喺導航欄揀 **+ Create**。

3. 喺導航欄揀 **New workspace**。

    ![揀 new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.hk.png)

4. 跟住做以下嘢：

    - 揀你嘅 Azure **Subscription**。
    - 揀用嘅 **Resource group**（需要嘅話可以新建）。
    - 入你嘅 **Workspace Name**，必須係唯一。
    - 揀你想用嘅 **Region**。
    - 揀用嘅 **Storage account**（需要嘅話可以新建）。
    - 揀用嘅 **Key vault**（需要嘅話可以新建）。
    - 揀用嘅 **Application insights**（需要嘅話可以新建）。
    - 揀用嘅 **Container registry**（需要嘅話可以新建）。

    ![填寫 azure machine learning 資料.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.hk.png)

5. 揀 **Review + Create**。

6. 揀 **Create**。

### 申請 Azure 訂閱嘅 GPU 配額

今次教學會用 GPU 去微調同部署 Phi-3 模型。微調會用 *Standard_NC24ads_A100_v4* GPU，需要申請配額；部署會用 *Standard_NC6s_v3* GPU，同樣需要申請配額。

> [!NOTE]
>
> 只有 Pay-As-You-Go 訂閱（標準訂閱類型）先有資格申請 GPU 配額，福利訂閱而家未支援。
>

1. 去 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 跟住做以下嘢去申請 *Standard NCADSA100v4 Family* 配額：

    - 喺左側選單揀 **Quota**。
    - 揀用嘅 **Virtual machine family**，例如揀 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**，入面有 *Standard_NC24ads_A100_v4* GPU。
    - 喺導航欄揀 **Request quota**。

        ![申請配額.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.hk.png)

    - 喺申請配額頁面入你想要嘅 **New cores limit**，例如 24。
    - 喺申請配額頁面揀 **Submit** 去申請 GPU 配額。

1. 跟住做以下嘢去申請 *Standard NCSv3 Family* 配額：

    - 喺左側選單揀 **Quota**。
    - 揀用嘅 **Virtual machine family**，例如揀 **Standard NCSv3 Family Cluster Dedicated vCPUs**，入面有 *Standard_NC6s_v3* GPU。
    - 喺導航欄揀 **Request quota**。
    - 喺申請配額頁面入你想要嘅 **New cores limit**，例如 24。
    - 喺申請配額頁面揀 **Submit** 去申請 GPU 配額。

### 新增角色指派

要微調同部署你嘅模型，首先要建立一個 User Assigned Managed Identity (UAI)，並賦予佢適當嘅權限。部署期間會用呢個 UAI 做認證。

#### 建立 User Assigned Managed Identity(UAI)

1. 喺入口網站頁面頂部嘅 **搜尋欄** 入面打 *managed identities*，然後喺選項中揀 **Managed Identities**。

    ![打 managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.hk.png)

1. 揀 **+ Create**。

    ![揀 create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.hk.png)

1. 跟住做以下嘢：

    - 揀你嘅 Azure **Subscription**。
    - 揀用嘅 **Resource group**（需要嘅話可以新建）。
    - 揀你想用嘅 **Region**。
    - 入你嘅 **Name**，必須係唯一。

    ![填寫 Managed Identities 資料.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.hk.png)

1. 揀 **Review + create**。

1. 揀 **+ Create**。

#### 賦予 Managed Identity Contributor 角色

1. 去你剛建立嘅 Managed Identity 資源。

1. 喺左側選單揀 **Azure role assignments**。

1. 喺導航欄揀 **+Add role assignment**。

1. 喺新增角色指派頁面做以下設定：
    - 將 **Scope** 設為 **Resource group**。
    - 揀你嘅 Azure **Subscription**。
    - 揀用嘅 **Resource group**。
    - 將 **Role** 設為 **Contributor**。

    ![填寫 Contributor 角色資料.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.hk.png)

2. 揀 **Save**。

#### 賦予 Managed Identity Storage Blob Data Reader 角色

1. 喺入口網站頁面頂部嘅 **搜尋欄** 入面打 *storage accounts*，然後揀 **Storage accounts**。

    ![打 storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.hk.png)

1. 揀同你建立嘅 Azure Machine Learning workspace 有關聯嘅儲存帳戶，例如 *finetunephistorage*。

1. 跟住做以下嘢去新增角色指派頁面：

    - 去你建立嘅 Azure Storage 帳戶。
    - 喺左側選單揀 **Access Control (IAM)**。
    - 喺導航欄揀 **+ Add**。
    - 揀 **Add role assignment**。

    ![新增角色.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.hk.png)

1. 喺新增角色指派頁面做以下設定：

    - 喺角色頁面嘅 **搜尋欄** 入面打 *Storage Blob Data Reader*，揀 **Storage Blob Data Reader**。
    - 揀 **Next**。
    - 喺成員頁面揀 **Assign access to** 為 **Managed identity**。
    - 揀 **+ Select members**。
    - 喺選擇 Managed identities 頁面揀你嘅 Azure **Subscription**。
    - 揀 **Managed identity** 類型。
    - 揀你剛建立嘅 Managed Identity，例如 *finetunephi-managedidentity*。
    - 揀 **Select**。

    ![揀 Managed Identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.hk.png)

1. 揀 **Review + assign**。

#### 賦予 Managed Identity AcrPull 角色

1. 喺入口網站頁面頂部嘅 **搜尋欄** 入面打 *container registries*，然後揀 **Container registries**。

    ![打 container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.hk.png)

1. 揀同你嘅 Azure Machine Learning workspace 有關聯嘅容器登記處，例如 *finetunephicontainerregistry*。

1. 跟住做以下嘢去新增角色指派頁面：

    - 喺左側選單揀 **Access Control (IAM)**。
    - 喺導航欄揀 **+ Add**。
    - 揀 **Add role assignment**。

1. 喺新增角色指派頁面做以下設定：

    - 喺角色頁面嘅 **搜尋欄** 入面打 *AcrPull*，揀 **AcrPull**。
    - 揀 **Next**。
    - 喺成員頁面揀 **Assign access to** 為 **Managed identity**。
    - 揀 **+ Select members**。
    - 喺選擇 Managed identities 頁面揀你嘅 Azure **Subscription**。
    - 揀 **Managed identity** 類型。
    - 揀你剛建立嘅 Managed Identity，例如 *finetunephi-managedidentity*。
    - 揀 **Select**。
    - 揀 **Review + assign**。

### 設定專案

要下載微調所需嘅資料集，你會先設定本地環境。

呢個練習你會：

- 建立一個資料夾作工作用。
- 建立虛擬環境。
- 安裝所需嘅套件。
- 建立 *download_dataset.py* 檔案去下載資料集。

#### 建立工作資料夾

1. 開啟終端機視窗，輸入以下指令喺預設路徑建立一個叫 *finetune-phi* 嘅資料夾。

    ```console
    mkdir finetune-phi
    ```

2. 喺終端機入以下指令去切換到剛建立嘅 *finetune-phi* 資料夾。

    ```console
    cd finetune-phi
    ```

#### 建立虛擬環境

1. 喺終端機入以下指令建立一個叫 *.venv* 嘅虛擬環境。

    ```console
    python -m venv .venv
    ```

2. 喺終端機入以下指令啟動虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 如果成功，你會見到命令提示符前面有 *(.venv)*。

#### 安裝所需套件

1. 喺終端機入以下指令安裝所需套件。

    ```console
    pip install datasets==2.19.1
    ```

#### 建立 `download_dataset.py`

> [!NOTE]
> 完整嘅資料夾結構：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. 開啟 **Visual Studio Code**。

1. 喺功能表欄揀 **File**。

1. 揀 **Open Folder**。

1. 揀剛建立嘅 *finetune-phi* 資料夾，路徑係 *C:\Users\yourUserName\finetune-phi*。

    ![揀你建立嘅資料夾.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.hk.png)

1. 喺 Visual Studio Code 左側窗格右鍵，揀 **New File**，建立一個新檔案，叫 *download_dataset.py*。

    ![建立新檔案.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.hk.png)

### 準備微調用嘅資料集

呢個練習你會執行 *download_dataset.py* 去下載 *ultrachat_200k* 資料集到本地環境，之後用呢個資料集去微調 Phi-3 模型喺 Azure Machine Learning。

呢個練習你會：

- 喺 *download_dataset.py* 加入下載資料集嘅代碼。
- 執行 *download_dataset.py* 去下載資料集到本地環境。

#### 用 *download_dataset.py* 下載資料集

1. 喺 Visual Studio Code 開啟 *download_dataset.py*。

1. 將以下代碼加入 *download_dataset.py*。

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 喺終端機入以下指令執行腳本，將資料集下載到本地環境。

    ```console
    python download_dataset.py
    ```

1. 確認資料集已成功儲存喺本地嘅 *finetune-phi/data* 目錄。

> [!NOTE]
>
> #### 關於資料集大小同微調時間嘅說明
>
> 呢個教學只用咗資料集嘅 1%（`split='train[:1%]'`），大大減少咗數據量，加快咗上載同微調嘅速度。你可以調整呢個百分比，搵到訓練時間同模型表現之間嘅最佳平衡。用細啲嘅資料子集可以縮短微調時間，令教學更易管理。

## 場景 2：微調 Phi-3 模型同喺 Azure Machine Learning Studio 部署

### 微調 Phi-3 模型

呢個練習你會喺 Azure Machine Learning Studio 微調 Phi-3 模型。

呢個練習你會：

- 建立用嚟微調嘅計算叢集。
- 喺 Azure Machine Learning Studio 微調 Phi-3 模型。

#### 建立用嚟微調嘅計算叢集
1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 從左側標籤選擇 **Compute**。

1. 從導航選單選擇 **Compute clusters**。

1. 選擇 **+ New**。

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.hk.png)

1. 執行以下操作：

    - 選擇你想使用的 **Region**。
    - 將 **Virtual machine tier** 設為 **Dedicated**。
    - 將 **Virtual machine type** 設為 **GPU**。
    - 將 **Virtual machine size** 篩選條件設為 **Select from all options**。
    - 選擇 **Virtual machine size** 為 **Standard_NC24ads_A100_v4**。

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.hk.png)

1. 選擇 **Next**。

1. 執行以下操作：

    - 輸入 **Compute name**，必須是唯一名稱。
    - 將 **Minimum number of nodes** 設為 **0**。
    - 將 **Maximum number of nodes** 設為 **1**。
    - 將 **Idle seconds before scale down** 設為 **120**。

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.hk.png)

1. 選擇 **Create**。

#### 微調 Phi-3 模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇你建立的 Azure Machine Learning 工作區。

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hk.png)

1. 執行以下操作：

    - 從左側標籤選擇 **Model catalog**。
    - 在 **search bar** 輸入 *phi-3-mini-4k*，然後從出現的選項中選擇 **Phi-3-mini-4k-instruct**。

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.hk.png)

1. 從導航選單選擇 **Fine-tune**。

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.hk.png)

1. 執行以下操作：

    - 將 **Select task type** 設為 **Chat completion**。
    - 選擇 **+ Select data** 上傳 **Traning data**。
    - 將驗證資料上傳類型設為 **Provide different validation data**。
    - 選擇 **+ Select data** 上傳 **Validation data**。

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.hk.png)

    > [!TIP]
    >
    > 你可以選擇 **Advanced settings** 來自訂設定，例如 **learning_rate** 和 **lr_scheduler_type**，以根據你的需求優化微調流程。

1. 選擇 **Finish**。

1. 在這個練習中，你已成功使用 Azure Machine Learning 微調了 Phi-3 模型。請注意，微調過程可能需要較長時間。提交微調工作後，你需要等待完成。可以透過在 Azure Machine Learning 工作區左側標籤的 Jobs 頁籤來監控微調工作的狀態。下一個系列中，你將部署微調後的模型並與 Prompt flow 整合。

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.hk.png)

### 部署微調後的 Phi-3 模型

要將微調後的 Phi-3 模型與 Prompt flow 整合，需要部署模型以便實時推論。此過程包括註冊模型、建立線上端點及部署模型。

在此練習中，你將：

- 在 Azure Machine Learning 工作區註冊微調後的模型。
- 建立線上端點。
- 部署已註冊的微調後 Phi-3 模型。

#### 註冊微調後的模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇你建立的 Azure Machine Learning 工作區。

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hk.png)

1. 從左側標籤選擇 **Models**。
1. 選擇 **+ Register**。
1. 選擇 **From a job output**。

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.hk.png)

1. 選擇你建立的工作。

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.hk.png)

1. 選擇 **Next**。

1. 將 **Model type** 設為 **MLflow**。

1. 確認已選擇 **Job output**，通常會自動選取。

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.hk.png)

2. 選擇 **Next**。

3. 選擇 **Register**。

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.hk.png)

4. 你可以透過左側標籤的 **Models** 選單查看已註冊的模型。

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.hk.png)

#### 部署微調後的模型

1. 前往你建立的 Azure Machine Learning 工作區。

1. 從左側標籤選擇 **Endpoints**。

1. 從導航選單選擇 **Real-time endpoints**。

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.hk.png)

1. 選擇 **Create**。

1. 選擇你已註冊的模型。

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.hk.png)

1. 選擇 **Select**。

1. 執行以下操作：

    - 將 **Virtual machine** 設為 *Standard_NC6s_v3*。
    - 選擇你想使用的 **Instance count**，例如 *1*。
    - 將 **Endpoint** 設為 **New** 以建立新端點。
    - 輸入 **Endpoint name**，必須是唯一名稱。
    - 輸入 **Deployment name**，必須是唯一名稱。

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.hk.png)

1. 選擇 **Deploy**。

> [!WARNING]
> 為避免額外費用，請務必在 Azure Machine Learning 工作區刪除已建立的端點。
>

#### 在 Azure Machine Learning 工作區檢查部署狀態

1. 前往你建立的 Azure Machine Learning 工作區。

1. 從左側標籤選擇 **Endpoints**。

1. 選擇你建立的端點。

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.hk.png)

1. 在此頁面，你可以管理部署過程中的端點。

> [!NOTE]
> 部署完成後，請確保 **Live traffic** 設為 **100%**。如果不是，請選擇 **Update traffic** 來調整流量設定。流量設為 0% 時，無法測試模型。
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.hk.png)
>

## 情境 3：與 Prompt flow 整合並使用自訂模型在 Azure AI Foundry 聊天

### 將自訂 Phi-3 模型與 Prompt flow 整合

成功部署微調模型後，現在可以將它與 Prompt Flow 整合，在即時應用中使用你的模型，實現多種互動任務。

在此練習中，你將：

- 建立 Azure AI Foundry Hub。
- 建立 Azure AI Foundry 專案。
- 建立 Prompt flow。
- 為微調後的 Phi-3 模型新增自訂連線。
- 設定 Prompt flow 與你的自訂 Phi-3 模型聊天。

> [!NOTE]
> 你也可以使用 Azure ML Studio 與 Promptflow 整合。相同的整合流程同樣適用於 Azure ML Studio。

#### 建立 Azure AI Foundry Hub

在建立專案前，你需要先建立 Hub。Hub 類似資源群組，可幫助你在 Azure AI Foundry 中組織和管理多個專案。

1. 訪問 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 從左側標籤選擇 **All hubs**。

1. 從導航選單選擇 **+ New hub**。

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.hk.png)

1. 執行以下操作：

    - 輸入 **Hub name**，必須是唯一名稱。
    - 選擇你的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**（如需要可新建）。
    - 選擇你想使用的 **Location**。
    - 選擇要使用的 **Connect Azure AI Services**（如需要可新建）。
    - 將 **Connect Azure AI Search** 設為 **Skip connecting**。

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.hk.png)

1. 選擇 **Next**。

#### 建立 Azure AI Foundry 專案

1. 在你建立的 Hub 中，從左側標籤選擇 **All projects**。

1. 從導航選單選擇 **+ New project**。

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.hk.png)

1. 輸入 **Project name**，必須是唯一名稱。

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.hk.png)

1. 選擇 **Create a project**。

#### 為微調後的 Phi-3 模型新增自訂連線

要將自訂 Phi-3 模型與 Prompt flow 整合，需要將模型的端點和金鑰儲存在自訂連線中，確保 Prompt flow 能存取你的自訂模型。

#### 設定微調後 Phi-3 模型的 api key 和 endpoint uri

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 前往你建立的 Azure Machine Learning 工作區。

1. 從左側標籤選擇 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.hk.png)

1. 選擇你建立的端點。

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.hk.png)

1. 從導航選單選擇 **Consume**。

1. 複製你的 **REST endpoint** 和 **Primary key**。
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.hk.png)

#### 加入自訂連線

1. 前往 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 進入你建立的 Azure AI Foundry 專案。

1. 在你建立的專案中，從左側標籤選擇 **Settings**。

1. 選擇 **+ New connection**。

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.hk.png)

1. 從導覽選單中選擇 **Custom keys**。

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.hk.png)

1. 執行以下操作：

    - 選擇 **+ Add key value pairs**。
    - 在鍵名欄輸入 **endpoint**，並將你從 Azure ML Studio 複製的 endpoint 貼到值欄。
    - 再次選擇 **+ Add key value pairs**。
    - 在鍵名欄輸入 **key**，並將你從 Azure ML Studio 複製的 key 貼到值欄。
    - 加入鍵值後，勾選 **is secret**，避免金鑰外洩。

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.hk.png)

1. 選擇 **Add connection**。

#### 建立 Prompt flow

你已經在 Azure AI Foundry 加入了自訂連線。接著，按照以下步驟建立 Prompt flow，然後將此 Prompt flow 連接到自訂連線，讓你可以在 Prompt flow 中使用微調後的模型。

1. 進入你建立的 Azure AI Foundry 專案。

1. 從左側標籤選擇 **Prompt flow**。

1. 從導覽選單選擇 **+ Create**。

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.hk.png)

1. 從導覽選單選擇 **Chat flow**。

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.hk.png)

1. 輸入要使用的 **Folder name**。

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.hk.png)

2. 選擇 **Create**。

#### 設定 Prompt flow 與你的自訂 Phi-3 模型聊天

你需要將微調好的 Phi-3 模型整合到 Prompt flow 中。不過，現有的 Prompt flow 並非為此設計，因此你必須重新設計 Prompt flow，才能順利整合自訂模型。

1. 在 Prompt flow 中，執行以下操作來重建現有流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 檔案中所有現有程式碼。
    - 將以下程式碼加入 *flow.dag.yml* 檔案。

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

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.hk.png)

1. 將以下程式碼加入 *integrate_with_promptflow.py* 檔案，以便在 Prompt flow 中使用自訂的 Phi-3 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.hk.png)

> [!NOTE]
> 如需更詳細的 Azure AI Foundry 中 Prompt flow 使用說明，可參考 [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input**、**Chat output** 以啟用與模型的聊天功能。

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.hk.png)

1. 現在你已準備好與自訂 Phi-3 模型聊天。下一個練習將教你如何啟動 Prompt flow 並用它與微調後的 Phi-3 模型互動。

> [!NOTE]
>
> 重建後的流程應該長得像下面這張圖：
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.hk.png)
>

### 與你的自訂 Phi-3 模型聊天

現在你已經完成微調並將自訂的 Phi-3 模型整合到 Prompt flow，接下來就可以開始與模型互動。這個練習會引導你設定並啟動與模型的聊天，透過這些步驟，你能充分發揮微調後 Phi-3 模型的各種功能和對話能力。

- 使用 Prompt flow 與你的自訂 Phi-3 模型聊天。

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 以啟動 Prompt flow。

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.hk.png)

1. 選擇 **Validate and parse input** 以更新參數。

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.hk.png)

1. 選擇你建立的自訂連線的 **connection** 值，例如 *connection*。

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.hk.png)

#### 與你的自訂模型聊天

1. 選擇 **Chat**。

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.hk.png)

1. 以下是範例結果：現在你可以開始與自訂 Phi-3 模型聊天。建議根據用於微調的資料來提問。

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.hk.png)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋盡力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應被視為權威來源。對於重要資訊，建議使用專業人手翻譯。我哋對因使用此翻譯而引致嘅任何誤解或誤釋概不負責。