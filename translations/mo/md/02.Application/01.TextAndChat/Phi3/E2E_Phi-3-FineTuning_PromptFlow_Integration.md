<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T17:19:54+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "mo"
}
-->
# 微調及整合自訂 Phi-3 模型與 Prompt flow

本端對端 (E2E) 範例基於 Microsoft Tech Community 中的指南「[微調及整合自訂 Phi-3 模型與 Prompt flow：逐步指引](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)」。介紹了微調、部署及整合自訂 Phi-3 模型與 Prompt flow 的流程。

## 概覽

在此 E2E 範例中，您將學習如何微調 Phi-3 模型並與 Prompt flow 整合。透過 Azure 機器學習與 Prompt flow，您將建立一個用於部署及使用自訂 AI 模型的工作流程。本 E2E 範例分為三個情境：

**情境 1：設定 Azure 資源並準備微調**

**情境 2：微調 Phi-3 模型並在 Azure 機器學習工作室部署**

**情境 3：與 Prompt flow 整合並與您的自訂模型聊天**

以下是本 E2E 範例的概覽。

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/zh-MO/00-01-architecture.02fc569e266d468c.webp)

### 目錄

1. **[情境 1：設定 Azure 資源並準備微調](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [建立 Azure 機器學習工作區](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [申請 Azure 訂閱中的 GPU 配額](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [新增角色指派](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [設定專案](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [準備微調所需的資料集](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[情境 2：微調 Phi-3 模型並在 Azure 機器學習工作室部署](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [設定 Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [微調 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署微調後的模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[情境 3：與 Prompt flow 整合並與您的自訂模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [將自訂 Phi-3 模型與 Prompt flow 整合](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [與您的自訂模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 情境 1：設定 Azure 資源並準備微調

### 建立 Azure 機器學習工作區

1. 在入口網站頁面頂部的 **搜尋列** 中輸入 *azure machine learning*，並從出現的選項中選擇 **Azure Machine Learning**。

    ![Type azure machine learning](../../../../../../translated_images/zh-MO/01-01-type-azml.a5116f8454d98c60.webp)

1. 從導覽選單中選擇 **+ 建立**。

1. 從導覽選單中選擇 **新增工作區**。

    ![Select new workspace](../../../../../../translated_images/zh-MO/01-02-select-new-workspace.83e17436f8898dc4.webp)

1. 執行以下工作：

    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的 **資源群組**（如有需要，可建立新的）。
    - 輸入 **工作區名稱**。必須是唯一值。
    - 選擇想使用的 **區域**。
    - 選擇要使用的 **儲存帳戶**（如有需要，可建立新的）。
    - 選擇要使用的 **Key vault**（如有需要，可建立新的）。
    - 選擇要使用的 **應用程式洞察**（如有需要，可建立新的）。
    - 選擇要使用的 **容器登錄站**（如有需要，可建立新的）。

    ![Fill AZML.](../../../../../../translated_images/zh-MO/01-03-fill-AZML.730a5177757bbebb.webp)

1. 選擇 **審閱 + 建立**。

1. 選擇 **建立**。

### 申請 Azure 訂閱中的 GPU 配額

在本 E2E 範例中，您將使用 *Standard_NC24ads_A100_v4 GPU* 進行微調，此項目需要申請配額；而部署時使用 *Standard_E4s_v3* CPU，則不需要申請配額。

> [!NOTE]
>
> 只有按需付費訂閱（標準訂閱類型）有資格分配 GPU；利潤訂閱暫時不支援。
>
> 對於使用利潤訂閱（如 Visual Studio Enterprise Subscription）或想快速測試微調及部署流程的用戶，也提供使用 CPU 和最小資料集進行微調的指引。但請注意，使用 GPU 搭配較大資料集進行微調時，效果明顯更佳。

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 執行以下動作以申請 *Standard NCADSA100v4 Family* 的配額：

    - 從左側頁籤選擇 **配額**。
    - 選擇要使用的 **虛擬機家族**，例如選擇包含 *Standard_NC24ads_A100_v4* GPU 的 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**。
    - 從導覽選單選擇 **申請配額**。

        ![Request quota.](../../../../../../translated_images/zh-MO/01-04-request-quota.3d3670c3221ab834.webp)

    - 在申請配額頁面，輸入想使用的 **新核心數限制**，例如 24。
    - 在申請配額頁面，選擇 **提交** 來申請 GPU 配額。

> [!NOTE]
> 您可參考 [Azure 虛擬機大小](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) 文件，選擇適合您需求的 GPU 或 CPU。

### 新增角色指派

微調及部署模型前，您必須先建立使用者指派型管理識別 (UAI)，並賦予適當的權限。此 UAI 將用於部署時的身份驗證。

#### 建立使用者指派型管理識別 (UAI)

1. 在入口網站頁面頂部的 **搜尋列** 中輸入 *managed identities*，並從出現選項中選擇 **Managed Identities**。

    ![Type managed identities.](../../../../../../translated_images/zh-MO/01-05-type-managed-identities.9297b6039874eff8.webp)

1. 選擇 **+ 建立**。

    ![Select create.](../../../../../../translated_images/zh-MO/01-06-select-create.936d8d66d7144f9a.webp)

1. 執行以下工作：

    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的 **資源群組**（如有需要，可建立新的）。
    - 選擇想使用的 **區域**。
    - 輸入 **名稱**。必須是唯一值。

1. 選擇 **審閱 + 建立**。

1. 選擇 **+ 建立**。

#### 新增「參與者」角色指派給管理識別

1. 導覽至您建立的管理識別資源。

1. 從左側頁籤選擇 **Azure 角色指派**。

1. 從導覽選單選擇 **+ 新增角色指派**。

1. 在新增角色指派頁面，執行以下動作：
    - 將 **範圍**選擇為 **資源群組**。
    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的 **資源群組**。
    - 將 **角色**選擇為 **參與者**。

    ![Fill contributor role.](../../../../../../translated_images/zh-MO/01-07-fill-contributor-role.29ca99b7c9f687e0.webp)

1. 選擇 **儲存**。

#### 新增「Storage Blob Data Reader」角色指派給管理識別

1. 在入口網站頁面頂部的 **搜尋列** 輸入 *storage accounts*，並從選項中選擇 **儲存帳戶**。

    ![Type storage accounts.](../../../../../../translated_images/zh-MO/01-08-type-storage-accounts.1186c8e42933e49b.webp)

1. 選擇與您建立的 Azure 機器學習工作區相關聯的儲存帳戶。例如 *finetunephistorage*。

1. 執行以下操作以進入新增角色指派頁面：

    - 導覽到您建立的 Azure 儲存帳戶。
    - 從左側頁籤選擇 **存取控制 (IAM)**。
    - 從導覽選單選擇 **+ 新增**。
    - 選擇 **新增角色指派**。

    ![Add role.](../../../../../../translated_images/zh-MO/01-09-add-role.d2db22fec1b187f0.webp)

1. 在新增角色指派頁面，執行以下動作：

    - 在角色頁面中，在 **搜尋列** 輸入 *Storage Blob Data Reader*，並從選項中選擇 **Storage Blob Data Reader**。
    - 在角色頁面中，選擇 **下一步**。
    - 在成員頁面中，將 **指派存取給** 選為 **管理識別**。
    - 在成員頁面中，選擇 **+ 選擇成員**。
    - 在選擇管理識別頁面中，選擇您的 Azure **訂閱**。
    - 選擇 **管理識別** 為 **管理識別**（Managed Identity）。
    - 選擇您建立的管理識別。例如 *finetunephi-managedidentity*。
    - 選擇 **選擇**。

    ![Select managed identity.](../../../../../../translated_images/zh-MO/01-10-select-managed-identity.5ce5ba181f72a4df.webp)

1. 選擇 **審閱 + 指派**。

#### 新增「AcrPull」角色指派給管理識別

1. 在入口網站頁面頂部的 **搜尋列** 輸入 *container registries*，並從選項中選擇 **容器登錄站**。

    ![Type container registries.](../../../../../../translated_images/zh-MO/01-11-type-container-registries.ff3b8bdc49dc596c.webp)

1. 選擇與 Azure 機器學習工作區相關聯的容器登錄站。例如 *finetunephicontainerregistries*。

1. 執行以下動作以進入新增角色指派頁面：

    - 從左側頁籤選擇 **存取控制 (IAM)**。
    - 從導覽選單選擇 **+ 新增**。
    - 選擇 **新增角色指派**。

1. 在新增角色指派頁面，執行以下動作：

    - 在角色頁面，於 **搜尋列** 輸入 *AcrPull*，並從選項中選擇 **AcrPull**。
    - 在角色頁面，選擇 **下一步**。
    - 在成員頁面，將 **指派存取給** 設定為 **管理識別**。
    - 在成員頁面，選擇 **+ 選擇成員**。
    - 在選擇管理識別頁面，選擇您的 Azure **訂閱**。
    - 選擇 **管理識別** 為 **管理識別**。
    - 選擇您建立的管理識別。例如 *finetunephi-managedidentity*。
    - 選擇 **選擇**。
    - 選擇 **審閱 + 指派**。

### 設定專案

現在，您將建立一個資料夾用於工作，並設定一個虛擬環境來開發一個與使用者互動、以及利用 Azure Cosmos DB 中儲存的聊天記錄提供回應的應用程式。

#### 建立工作資料夾

1. 開啟終端機視窗，並輸入以下指令，在預設路徑下建立名為 *finetune-phi* 的資料夾。

    ```console
    mkdir finetune-phi
    ```

1. 在終端機中輸入以下指令，導覽到您所建立的 *finetune-phi* 資料夾。

    ```console
    cd finetune-phi
    ```

#### 建立虛擬環境

1. 在終端機中輸入以下指令，建立一個名為 *.venv* 的虛擬環境。

    ```console
    python -m venv .venv
    ```

1. 在終端機中輸入以下指令以啟動虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> 若成功啟動，您會在命令提示字元前看到 *(.venv)* 標示。

#### 安裝所需套件

1. 在終端機中輸入以下指令安裝所需的套件。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 建立專案檔案
在此練習中，您將建立我們專案所需的基本檔案。這些檔案包括下載資料集的腳本、設定 Azure 機器學習環境、微調 Phi-3 模型以及部署微調後的模型。您還將建立一個 *conda.yml* 檔案以設定微調環境。

在此練習中，您將：

- 建立一個 *download_dataset.py* 檔案以下載資料集。
- 建立一個 *setup_ml.py* 檔案以設定 Azure 機器學習環境。
- 在 *finetuning_dir* 資料夾中建立 *fine_tune.py* 檔案，以使用資料集微調 Phi-3 模型。
- 建立一個 *conda.yml* 檔案以設定微調環境。
- 建立一個 *deploy_model.py* 檔案以部署微調後的模型。
- 建立一個 *integrate_with_promptflow.py* 檔案，以整合微調模型並使用 Prompt flow 執行該模型。
- 建立一個 flow.dag.yml 檔案，以設定 Prompt flow 的工作流程結構。
- 建立一個 *config.py* 檔案以輸入 Azure 資訊。

> [!NOTE]
>
> 完整資料夾結構：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. 開啟 **Visual Studio Code**。

1. 從功能表列選擇 **檔案**。

1. 選擇 **開啟資料夾**。

1. 選擇您建立的 *finetune-phi* 資料夾，位於 *C:\Users\yourUserName\finetune-phi*。

    ![開啟專案資料夾。](../../../../../../translated_images/zh-MO/01-12-open-project-folder.1fff9c7f41dd1639.webp)

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **新增檔案**，建立名為 *download_dataset.py* 的新檔案。

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **新增檔案**，建立名為 *setup_ml.py* 的新檔案。

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **新增檔案**，建立名為 *deploy_model.py* 的新檔案。

    ![建立新檔案。](../../../../../../translated_images/zh-MO/01-13-create-new-file.c17c150fff384a39.webp)

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **新增資料夾**，建立名為 *finetuning_dir* 的新資料夾。

1. 在 *finetuning_dir* 資料夾中，建立名為 *fine_tune.py* 的新檔案。

#### 建立及設定 *conda.yml* 檔案

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **新增檔案**，建立名為 *conda.yml* 的新檔案。

1. 在 *conda.yml* 檔案中新增以下程式碼，以設定 Phi-3 模型的微調環境。

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### 建立及設定 *config.py* 檔案

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **新增檔案**，建立名為 *config.py* 的新檔案。

1. 在 *config.py* 檔案中新增以下程式碼，以輸入您的 Azure 資訊。

    ```python
    # Azure 設定
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure 機器學習設定
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure 託管身份設定
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # 數據集檔案路徑
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # 微調模型設定
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### 新增 Azure 環境變數

1. 執行下列步驟以新增 Azure 訂閱 ID：

    - 在入口網站頁面頂部的 **搜尋列** 輸入 *subscriptions*，並從顯示的選項中選擇 **訂閱**。
    - 選擇您目前使用的 Azure 訂閱。
    - 將您的訂閱 ID 複製並貼到 *config.py* 檔案中。

    ![尋找訂閱 ID。](../../../../../../translated_images/zh-MO/01-14-find-subscriptionid.4f4ca33555f1e637.webp)

1. 執行下列步驟以新增 Azure 工作區名稱：

    - 導航到您建立的 Azure 機器學習資源。
    - 將您的帳戶名稱複製並貼到 *config.py* 檔案中。

    ![尋找 Azure 機器學習名稱。](../../../../../../translated_images/zh-MO/01-15-find-AZML-name.1975f0422bca19a7.webp)

1. 執行下列步驟以新增 Azure 資源群組名稱：

    - 導航到您建立的 Azure 機器學習資源。
    - 將您的 Azure 資源群組名稱複製並貼到 *config.py* 檔案中。

    ![尋找資源群組名稱。](../../../../../../translated_images/zh-MO/01-16-find-AZML-resourcegroup.855a349d0af134a3.webp)

2. 執行下列步驟以新增 Azure 托管身分名稱：

    - 導航到您建立的受管身分資源。
    - 將您的 Azure 托管身分名稱複製並貼到 *config.py* 檔案中。

    ![尋找 UAI。](../../../../../../translated_images/zh-MO/01-17-find-uai.3529464f53499827.webp)

### 準備微調資料集

在此練習中，您將執行 *download_dataset.py* 檔案以將 *ULTRACHAT_200k* 資料集下載到本地環境，然後使用該資料集在 Azure 機器學習中微調 Phi-3 模型。

#### 使用 *download_dataset.py* 下載資料集

1. 在 Visual Studio Code 開啟 *download_dataset.py* 檔案。

1. 將以下程式碼新增到 *download_dataset.py*。

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # 載入指定名稱、配置及切割比例嘅數據集
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # 將數據集切割成訓練集同測試集（80%訓練，20%測試）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 如果資料夾唔存在，就建立佢
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 用寫入模式開啟檔案
        with open(filepath, 'w', encoding='utf-8') as f:
            # 遍歷數據集入面嘅每條紀錄
            for record in dataset:
                # 將紀錄轉成 JSON 物件並寫入檔案
                json.dump(record, f)
                # 寫入換行字元以分隔紀錄
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 用特定配置同切割比例載入同切割 ULTRACHAT_200k 數據集
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 從切割中提取訓練集同測試集數據
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 將訓練集數據保存到 JSONL 檔案
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # 將測試集數據保存到另一個 JSONL 檔案
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **使用最小資料集及 CPU 進行微調的指導**
>
> 如果您想使用 CPU 進行微調，此方法適合擁有優惠訂閱（如 Visual Studio Enterprise Subscription）或想快速測試微調與部署流程的人士。
>
> 將 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` 替換為 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. 在終端機輸入以下指令，執行腳本並將資料集下載到本地環境。

    ```console
    python download_data.py
    ```

1. 確認資料集是否成功儲存至本地的 *finetune-phi/data* 目錄。

> [!NOTE]
>
> **資料集大小與微調時間**
>
> 在此 E2E 範例中，您只使用 1% 的資料集（`train_sft[:1%]`）。這大幅減少資料量，加快上傳和微調速度。您可以調整百分比以尋找訓練時間與模型效能間的最佳平衡。使用較小的子集可減少微調所需時間，令流程更適合用於 E2E 範例。

## 情境 2：在 Azure Machine Learning Studio 中微調 Phi-3 模型並部署

### 設定 Azure CLI

您需要設定 Azure CLI 來驗證您的環境。Azure CLI 允許您直接從命令列管理 Azure 資源，並提供 Azure 機器學習存取這些資源所需的認證。開始前請安裝 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. 開啟終端機視窗，輸入以下指令來登入您的 Azure 帳戶。

    ```console
    az login
    ```

1. 選擇要使用的 Azure 帳戶。

1. 選擇要使用的 Azure 訂閱。

    ![尋找資源群組名稱。](../../../../../../translated_images/zh-MO/02-01-login-using-azure-cli.dfde31cb75e58a87.webp)

> [!TIP]
>
> 如果您登入 Azure 遇到困難，試試使用裝置代碼登入。開啟終端機視窗並輸入以下指令登入 Azure 帳戶：
>
> ```console
> az login --use-device-code
> ```
>

### 微調 Phi-3 模型

在此練習中，您將使用提供的資料集微調 Phi-3 模型。首先，您會在 *fine_tune.py* 檔案中定義微調流程。接著，您將設定 Azure 機器學習環境並透過執行 *setup_ml.py* 檔案啟動微調。此腳本確保微調程序在 Azure 機器學習環境中進行。

執行 *setup_ml.py* 後，您將在 Azure 機器學習環境中執行微調過程。

#### 在 *fine_tune.py* 檔案新增程式碼

1. 導航到 *finetuning_dir* 資料夾，於 Visual Studio Code 開啟 *fine_tune.py* 檔案。

1. 將以下程式碼新增到 *fine_tune.py*。

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # 為避免 MLflow 中的 INVALID_PARAMETER_VALUE 錯誤，請禁用 MLflow 集成
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # 日誌設置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. 儲存並關閉 *fine_tune.py* 檔案。

> [!TIP]
> **您可以微調 Phi-3.5 模型**
>
> 在 *fine_tune.py* 檔案中，您可以將 `pretrained_model_name` 從 `"microsoft/Phi-3-mini-4k-instruct"` 改為任何您想微調的模型。例如，若改為 `"microsoft/Phi-3.5-mini-instruct"`，則會使用 Phi-3.5-mini-instruct 模型進行微調。您可先到 [Hugging Face](https://huggingface.co/) 搜尋喜歡的模型名稱，然後將該名稱複製貼到腳本中的 `pretrained_model_name` 欄位。
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="微調 Phi-3.5。">
>

#### 在 *setup_ml.py* 檔案新增程式碼

1. 在 Visual Studio Code 中開啟 *setup_ml.py* 檔案。

1. 將以下程式碼新增到 *setup_ml.py*。

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # 常數

    # 取消註解以下行以使用 CPU 實例進行訓練
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # 取消註解以下行以使用 GPU 實例進行訓練
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # 替換為您的計算集群位置
    FINETUNING_DIR = "./finetuning_dir" # 微調腳本的路徑
    TRAINING_ENV_NAME = "phi-3-training-environment" # 訓練環境名稱
    MODEL_OUTPUT_DIR = "./model_output" # 在 azure ml 中模型輸出目錄的路徑

    # 設置日誌以跟蹤過程
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # 環境的 Docker 映像
            conda_file=CONDA_FILE,  # Conda 環境檔案
            name=TRAINING_ENV_NAME,  # 環境名稱
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # 計算集群的等級
                min_instances=0,  # 最小實例數
                max_instances=1  # 最大實例數
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # 等待集群建立完成
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # fine_tune.py 的路徑
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # 訓練環境
            compute=compute_name,  # 使用的計算集群
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # 訓練數據檔案的路徑
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # 評估數據檔案的路徑
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # 初始化 ML 用戶端
        ml_client = get_ml_client()

        # 建立環境
        env = create_or_get_environment(ml_client)
        
        # 建立或獲取現有的計算集群
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # 建立並提交微調作業
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # 提交作業
        ml_client.jobs.stream(returned_job.name)  # 流式顯示作業日誌
        
        # 擷取作業名稱
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. 將 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `LOCATION` 替換成您的具體資訊。

    ```python
   # 取消註解以下行以使用 GPU 實例進行訓練
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # 替換為你的計算集群位置
    ```

> [!TIP]
>
> **使用最小資料集及 CPU 進行微調的指導**
>
> 如果您想使用 CPU 進行微調，此方法適合擁有優惠訂閱（如 Visual Studio Enterprise Subscription）或想快速測試微調與部署流程的人士。
>
> 1. 開啟 *setup_ml* 檔案。
> 1. 將 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `DOCKER_IMAGE_NAME` 改為以下設定。如您無法使用 *Standard_E16s_v3*，可改用相當的 CPU 實例或請求新額度。
> 1. 將 `LOCATION` 替換為您的具體資訊。
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. 輸入以下指令執行 *setup_ml.py* 腳本，開始在 Azure 機器學習中進行微調。

    ```python
    python setup_ml.py
    ```

1. 在此練習中，您已成功使用 Azure 機器學習微調 Phi-3 模型。透過執行 *setup_ml.py*，您完成了 Azure 機器學習環境設定並啟動 *fine_tune.py* 中定義的微調流程。請注意，微調過程可能需要相當長的時間。在執行 `python setup_ml.py` 指令後，您需等待流程完成。您可以透過終端機提供之連結，前往 Azure 機器學習入口網站監控微調作業狀態。

    ![查看微調作業。](../../../../../../translated_images/zh-MO/02-02-see-finetuning-job.59393bc3b143871e.webp)

### 部署微調後的模型

為將微調後的 Phi-3 模型與 Prompt Flow 整合，您需要部署該模型，使其能進行即時推論。此流程包含模型註冊、建立線上端點，以及部署模型。

#### 設定模型名稱、端點名稱及部署名稱

1. 開啟 *config.py* 檔案。

1. 將 `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` 替換成您想要的模型名稱。

1. 將 `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` 替換成您想要的端點名稱。

1. 將 `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` 替換成您想要的部署名稱。

#### 在 *deploy_model.py* 檔案新增程式碼

執行 *deploy_model.py* 檔案可自動完成整個部署過程。該檔案會根據 *config.py* 中的設定（包含模型名稱、端點名稱與部署名稱），註冊模型、創建端點並執行部署。

1. 在 Visual Studio Code 中開啟 *deploy_model.py* 檔案。

1. 將以下程式碼新增到 *deploy_model.py*。

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # 配置匯入
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # 常數
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # 日誌設置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # 獲取當前端點詳情
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # 記錄當前流量分配以便調試
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # 設置部署的流量分配
            endpoint.traffic = {deployment_name: 100}
            
            # 使用新的流量分配更新端點
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # 記錄更新後的流量分配以便調試
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # 記錄過程中發生的任何錯誤
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. 執行下列步驟以取得 `JOB_NAME`：

    - 導航至您建立的 Azure 機器學習資源。
    - 選擇 **Studio web URL** 以開啟 Azure 機器學習工作區。
    - 從左側選單選擇 **Jobs**。
    - 選擇用於微調的實驗，例如 *finetunephi*。
    - 選擇您所建立的該工作。
- 將您的工作名稱複製並貼上到 *deploy_model.py* 檔案中的 `JOB_NAME = "your-job-name"`。

1. 將 `COMPUTE_INSTANCE_TYPE` 替換為您的具體細節。

1. 輸入以下指令以執行 *deploy_model.py* 腳本，並在 Azure 機器學習中啟動部署流程。

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> 為避免對您的帳戶產生額外費用，請務必刪除在 Azure 機器學習工作區中建立的端點。
>

#### 在 Azure 機器學習工作區中檢查部署狀態

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 導覽至您所建立的 Azure 機器學習工作區。

1. 選擇 **Studio web URL** 以開啟 Azure 機器學習工作區。

1. 從左側標籤選擇 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/zh-MO/02-03-select-endpoints.c3136326510baff1.webp)

2. 選擇您所建立的端點。

    ![Select endpoints that you created.](../../../../../../translated_images/zh-MO/02-04-select-endpoint-created.0363e7dca51dabb4.webp)

3. 在此頁面中，您可以管理部署流程中建立的端點。

## 情境 3：與 Prompt flow 集成並與您的自訂模型聊天

### 與 Prompt flow 集成自訂 Phi-3 模型

成功部署您的微調模型後，您現在可以將其與 Prompt flow 集成，以在即時應用中使用您的模型，從而使用您的自訂 Phi-3 模型執行多種互動任務。

#### 設定微調後 Phi-3 模型的 API 金鑰與端點 URI

1. 導覽至您所建立的 Azure 機器學習工作區。
1. 從左側標籤選擇 **Endpoints**。
1. 選擇您所建立的端點。
1. 從導覽選單選擇 **Consume**。
1. 將您的 **REST endpoint** 複製並貼上至 *config.py* 檔案，替換 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` 為您的 **REST endpoint**。
1. 將您的 **Primary key** 複製並貼上至 *config.py* 檔案，替換 `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` 為您的 **Primary key**。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/zh-MO/02-05-copy-apikey-endpoint.88b5a92e6462c53b.webp)

#### 新增程式碼至 *flow.dag.yml* 檔案

1. 在 Visual Studio Code 中開啟 *flow.dag.yml* 檔案。

1. 將下列程式碼新增至 *flow.dag.yml*。

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

#### 新增程式碼至 *integrate_with_promptflow.py* 檔案

1. 在 Visual Studio Code 中開啟 *integrate_with_promptflow.py* 檔案。

1. 將下列程式碼新增至 *integrate_with_promptflow.py*。

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # 日誌設置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### 與您的自訂模型聊天

1. 輸入以下指令以執行 *deploy_model.py* 腳本，並在 Azure 機器學習中啟動部署流程。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 這是一個結果示例：現在您可以與您的自訂 Phi-3 模型聊天。建議根據用於微調的數據提出問題。

    ![Prompt flow example.](../../../../../../translated_images/zh-MO/02-06-promptflow-example.89384abaf3ad71f6.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之原文版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引起之任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->