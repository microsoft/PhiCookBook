<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:13:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "tw"
}
-->
# 微調並整合自訂 Phi-3 模型與 Prompt flow

此端對端 (E2E) 範例基於 Microsoft Tech Community 的指南「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)」，介紹如何微調、部署及整合自訂 Phi-3 模型與 Prompt flow。

## 概覽

在此 E2E 範例中，您將學習如何微調 Phi-3 模型並將其整合到 Prompt flow。透過 Azure Machine Learning 與 Prompt flow，您將建立一個部署及使用自訂 AI 模型的工作流程。此 E2E 範例分為三個情境：

**情境 1：設定 Azure 資源並準備微調**

**情境 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 部署**

**情境 3：整合 Prompt flow 並與您的自訂模型聊天**

以下是此 E2E 範例的概覽。

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468cf3bbb3158cf273380cbdf7fcec042c7328e1559c6b2e2632.tw.png)

### 目錄

1. **[情境 1：設定 Azure 資源並準備微調](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [建立 Azure Machine Learning 工作區](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [申請 Azure 訂閱中的 GPU 配額](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [新增角色指派](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [設定專案](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [準備微調用資料集](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[情境 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 部署](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [設定 Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [微調 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署微調後的模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[情境 3：整合 Prompt flow 並與您的自訂模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [將自訂 Phi-3 模型整合到 Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [與您的自訂模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 情境 1：設定 Azure 資源並準備微調

### 建立 Azure Machine Learning 工作區

1. 在入口網站頁面頂端的 **搜尋列** 輸入 *azure machine learning*，並從出現的選項中選擇 **Azure Machine Learning**。

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c600d87008fb78206d2cf90c0b920c231618a8ec8baaa6f46c3.tw.png)

1. 從導覽選單選擇 **+ 建立**。

1. 從導覽選單選擇 **新工作區**。

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4fbb808d1bbcd92962692b1fa687f4c5d3952f453177825bc.tw.png)

1. 執行以下操作：

    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的 **資源群組**（如有需要可建立新的）。
    - 輸入 **工作區名稱**，必須是唯一值。
    - 選擇您想使用的 **區域**。
    - 選擇要使用的 **儲存帳戶**（如有需要可建立新的）。
    - 選擇要使用的 **金鑰保管庫**（如有需要可建立新的）。
    - 選擇要使用的 **應用程式洞察**（如有需要可建立新的）。
    - 選擇要使用的 **容器登錄**（如有需要可建立新的）。

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb141b9e8c16f31834e82e831275bd9faad0b70343f46255de.tw.png)

1. 選擇 **檢閱 + 建立**。

1. 選擇 **建立**。

### 申請 Azure 訂閱中的 GPU 配額

在此 E2E 範例中，您將使用 *Standard_NC24ads_A100_v4 GPU* 進行微調，這需要申請配額；而部署時使用的 *Standard_E4s_v3* CPU 則不需申請配額。

> [!NOTE]
>
> 只有「隨用隨付」訂閱（標準訂閱類型）有資格申請 GPU 配額，福利訂閱目前不支援。
>
> 對於使用福利訂閱（例如 Visual Studio Enterprise 訂閱）或想快速測試微調與部署流程的使用者，本教學也提供使用 CPU 及最小資料集進行微調的指引。但請注意，使用 GPU 且搭配較大資料集時，微調效果會明顯更佳。

1. 前往 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 執行以下操作以申請 *Standard NCADSA100v4 Family* 配額：

    - 從左側標籤選擇 **配額**。
    - 選擇要使用的 **虛擬機器系列**，例如選擇包含 *Standard_NC24ads_A100_v4* GPU 的 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**。
    - 從導覽選單選擇 **申請配額**。

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab8348515fcfba9d0279114f04065df8bd6fb78e3d3704e627545.tw.png)

    - 在申請配額頁面中，輸入您想使用的 **新核心限制**，例如 24。
    - 在申請配額頁面中，選擇 **提交** 以申請 GPU 配額。

> [!NOTE]
> 您可以參考 [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) 文件，選擇適合您需求的 GPU 或 CPU。

### 新增角色指派

要微調並部署模型，您必須先建立一個使用者指派的管理身分 (User Assigned Managed Identity, UAI)，並賦予適當權限。此 UAI 將用於部署時的身份驗證。

#### 建立使用者指派的管理身分 (UAI)

1. 在入口網站頁面頂端的 **搜尋列** 輸入 *managed identities*，並從出現的選項中選擇 **Managed Identities**。

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8a95d6e7762f1b087275a9634677f0a4e355717550ace3c02.tw.png)

1. 選擇 **+ 建立**。

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a8c70af922bf28a573c0744fb642f8228d62214b010a070d9.tw.png)

1. 執行以下操作：

    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的 **資源群組**（如有需要可建立新的）。
    - 選擇您想使用的 **區域**。
    - 輸入 **名稱**，必須是唯一值。

1. 選擇 **檢閱 + 建立**。

1. 選擇 **+ 建立**。

#### 新增 Contributor 角色指派給管理身分

1. 導覽至您建立的管理身分資源。

1. 從左側標籤選擇 **Azure 角色指派**。

1. 從導覽選單選擇 **+ 新增角色指派**。

1. 在新增角色指派頁面中，執行以下操作：
    - 將 **範圍** 設為 **資源群組**。
    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的 **資源群組**。
    - 將 **角色** 設為 **Contributor**。

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e008e224cf336687c04c9fe24740e47e34ce041b50b47e0ed1.tw.png)

1. 選擇 **儲存**。

#### 新增 Storage Blob Data Reader 角色指派給管理身分

1. 在入口網站頁面頂端的 **搜尋列** 輸入 *storage accounts*，並從出現的選項中選擇 **Storage accounts**。

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49bcd9cce3ffd1b6218afb6e5c3700b628da7b7c294be71b911.tw.png)

1. 選擇與您建立的 Azure Machine Learning 工作區相關聯的儲存帳戶，例如 *finetunephistorage*。

1. 執行以下操作以導覽至新增角色指派頁面：

    - 導覽至您建立的 Azure 儲存帳戶。
    - 從左側標籤選擇 **存取控制 (IAM)**。
    - 從導覽選單選擇 **+ 新增**。
    - 選擇 **新增角色指派**。

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0ae84790d65dc5726a9b57c496d916b8700d41e0b3b468451.tw.png)

1. 在新增角色指派頁面中，執行以下操作：

    - 在角色頁面中，於 **搜尋列** 輸入 *Storage Blob Data Reader*，並從選項中選擇 **Storage Blob Data Reader**。
    - 在角色頁面中，選擇 **下一步**。
    - 在成員頁面中，將 **指派存取權給** 設為 **Managed identity**。
    - 在成員頁面中，選擇 **+ 選擇成員**。
    - 在選擇管理身分頁面中，選擇您的 Azure **訂閱**。
    - 在選擇管理身分頁面中，將 **管理身分** 設為 **Manage Identity**。
    - 在選擇管理身分頁面中，選擇您建立的管理身分，例如 *finetunephi-managedidentity*。
    - 在選擇管理身分頁面中，選擇 **選擇**。

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df788963e1dc0a68c39ee297363aabe979b487c60b3037662f.tw.png)

1. 選擇 **檢閱 + 指派**。

#### 新增 AcrPull 角色指派給管理身分

1. 在入口網站頁面頂端的 **搜尋列** 輸入 *container registries*，並從出現的選項中選擇 **Container registries**。

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c64c0f778633c652ce08e4ac28f142a17afc10de81bb8c336.tw.png)

1. 選擇與 Azure Machine Learning 工作區相關聯的容器登錄，例如 *finetunephicontainerregistries*。

1. 執行以下操作以導覽至新增角色指派頁面：

    - 從左側標籤選擇 **存取控制 (IAM)**。
    - 從導覽選單選擇 **+ 新增**。
    - 選擇 **新增角色指派**。

1. 在新增角色指派頁面中，執行以下操作：

    - 在角色頁面中，於 **搜尋列** 輸入 *AcrPull*，並從選項中選擇 **AcrPull**。
    - 在角色頁面中，選擇 **下一步**。
    - 在成員頁面中，將 **指派存取權給** 設為 **Managed identity**。
    - 在成員頁面中，選擇 **+ 選擇成員**。
    - 在選擇管理身分頁面中，選擇您的 Azure **訂閱**。
    - 在選擇管理身分頁面中，將 **管理身分** 設為 **Manage Identity**。
    - 在選擇管理身分頁面中，選擇您建立的管理身分，例如 *finetunephi-managedidentity*。
    - 在選擇管理身分頁面中，選擇 **選擇**。
    - 選擇 **檢閱 + 指派**。

### 設定專案

接下來，您將建立一個資料夾作為工作目錄，並設定虛擬環境來開發一個與使用者互動的程式，該程式會使用來自 Azure Cosmos DB 的聊天歷史記錄來輔助回應。

#### 建立工作資料夾

1. 開啟終端機視窗，輸入以下指令，在預設路徑下建立名為 *finetune-phi* 的資料夾。

    ```console
    mkdir finetune-phi
    ```

1. 在終端機中輸入以下指令，切換到您剛建立的 *finetune-phi* 資料夾。

    ```console
    cd finetune-phi
    ```

#### 建立虛擬環境

1. 在終端機中輸入以下指令，建立名為 *.venv* 的虛擬環境。

    ```console
    python -m venv .venv
    ```

1. 在終端機中輸入以下指令，啟動虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> 如果成功，你應該會在命令提示符前看到 *(.venv)*。
#### 安裝所需套件

1. 在終端機中輸入以下指令以安裝所需套件。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 建立專案檔案

在本練習中，您將建立專案所需的基本檔案。這些檔案包含下載資料集的腳本、設定 Azure Machine Learning 環境、微調 Phi-3 模型，以及部署微調後模型的腳本。您還會建立一個 *conda.yml* 檔案來設定微調環境。

在本練習中，您將：

- 建立 *download_dataset.py* 檔案來下載資料集。
- 建立 *setup_ml.py* 檔案來設定 Azure Machine Learning 環境。
- 在 *finetuning_dir* 資料夾中建立 *fine_tune.py* 檔案，使用資料集微調 Phi-3 模型。
- 建立 *conda.yml* 檔案來設定微調環境。
- 建立 *deploy_model.py* 檔案來部署微調後的模型。
- 建立 *integrate_with_promptflow.py* 檔案，將微調後模型整合並透過 Prompt flow 執行模型。
- 建立 flow.dag.yml 檔案，設定 Prompt flow 的工作流程結構。
- 建立 *config.py* 檔案以輸入 Azure 資訊。

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

1. 從選單列選擇 **File**。

1. 選擇 **Open Folder**。

1. 選擇您建立的 *finetune-phi* 資料夾，路徑位於 *C:\Users\yourUserName\finetune-phi*。

    ![開啟專案資料夾。](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639c12e7da258ac8b3deca260786edb07598e206725cd1593ce.tw.png)

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **New File**，建立名為 *download_dataset.py* 的新檔案。

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **New File**，建立名為 *setup_ml.py* 的新檔案。

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **New File**，建立名為 *deploy_model.py* 的新檔案。

    ![建立新檔案。](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a398766a39eac9f15240a9a4da566bd8dca86f471e78eadc69e.tw.png)

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **New Folder**，建立名為 *finetuning_dir* 的新資料夾。

1. 在 *finetuning_dir* 資料夾中，建立名為 *fine_tune.py* 的新檔案。

#### 建立並設定 *conda.yml* 檔案

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **New File**，建立名為 *conda.yml* 的新檔案。

1. 將以下程式碼加入 *conda.yml* 檔案，以設定 Phi-3 模型的微調環境。

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

#### 建立並設定 *config.py* 檔案

1. 在 Visual Studio Code 左側窗格中，右鍵點擊並選擇 **New File**，建立名為 *config.py* 的新檔案。

1. 將以下程式碼加入 *config.py* 檔案，填入您的 Azure 資訊。

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### 新增 Azure 環境變數

1. 執行以下步驟以新增 Azure 訂閱 ID：

    - 在入口網站頁面頂端的 **搜尋列** 輸入 *subscriptions*，並從選項中選擇 **Subscriptions**。
    - 選擇您目前使用的 Azure 訂閱。
    - 複製並貼上您的訂閱 ID 至 *config.py* 檔案中。

    ![尋找訂閱 ID。](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637e01163bfdd2a606e7d06f05455ab56e05cb5107e938e7a90.tw.png)

1. 執行以下步驟以新增 Azure 工作區名稱：

    - 前往您建立的 Azure Machine Learning 資源。
    - 複製並貼上您的帳戶名稱至 *config.py* 檔案中。

    ![尋找 Azure Machine Learning 名稱。](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a702b1bb5e9d8e9f5e5424abe066a0ff310da980582e65721f.tw.png)

1. 執行以下步驟以新增 Azure 資源群組名稱：

    - 前往您建立的 Azure Machine Learning 資源。
    - 複製並貼上您的 Azure 資源群組名稱至 *config.py* 檔案中。

    ![尋找資源群組名稱。](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a399243d7c94d5aabd86070ab6535d3cf2ec38c78538626666.tw.png)

2. 執行以下步驟以新增 Azure 管理身分名稱：

    - 前往您建立的 Managed Identities 資源。
    - 複製並貼上您的 Azure 管理身分名稱至 *config.py* 檔案中。

    ![尋找 UAI。](../../../../../../translated_images/01-17-find-uai.3529464f534998271ea7c5aebafa887051567417f3b4244ff58fdd443192b6d7.tw.png)

### 準備微調資料集

在本練習中，您將執行 *download_dataset.py* 檔案，將 *ULTRACHAT_200k* 資料集下載到本地環境。接著，您將使用此資料集在 Azure Machine Learning 中微調 Phi-3 模型。

#### 使用 *download_dataset.py* 下載資料集

1. 在 Visual Studio Code 中開啟 *download_dataset.py* 檔案。

1. 將以下程式碼加入 *download_dataset.py*。

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
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **使用 CPU 以最小資料集進行微調的建議**
>
> 如果您想使用 CPU 進行微調，此方法適合擁有福利訂閱（例如 Visual Studio Enterprise 訂閱）或想快速測試微調與部署流程的使用者。
>
> 將 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` 替換為 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. 在終端機中輸入以下指令，執行腳本並將資料集下載到本地環境。

    ```console
    python download_data.py
    ```

1. 確認資料集已成功儲存至本地 *finetune-phi/data* 目錄。

> [!NOTE]
>
> **資料集大小與微調時間**
>
> 在此端對端範例中，您只使用資料集的 1% (`train_sft[:1%]`)。這大幅減少資料量，加快上傳與微調速度。您可以調整百分比，以取得訓練時間與模型效能的最佳平衡。使用較小的資料子集能縮短微調所需時間，使端對端範例更易於操作。

## 情境 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 部署

### 設定 Azure CLI

您需要設定 Azure CLI 以驗證您的環境。Azure CLI 允許您直接從命令列管理 Azure 資源，並提供 Azure Machine Learning 存取這些資源所需的憑證。開始前請安裝 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. 開啟終端機視窗，輸入以下指令登入您的 Azure 帳戶。

    ```console
    az login
    ```

1. 選擇您要使用的 Azure 帳戶。

1. 選擇您要使用的 Azure 訂閱。

    ![尋找資源群組名稱。](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a8792c687d36e4fc4f4ee37fd76640e6e4e5aed3329513f2328.tw.png)

> [!TIP]
>
> 如果您登入 Azure 時遇到困難，試試使用裝置代碼登入。開啟終端機視窗，輸入以下指令登入您的 Azure 帳戶：
>
> ```console
> az login --use-device-code
> ```
>

### 微調 Phi-3 模型

在本練習中，您將使用提供的資料集微調 Phi-3 模型。首先，您會在 *fine_tune.py* 檔案中定義微調流程。接著，您會設定 Azure Machine Learning 環境並執行 *setup_ml.py* 檔案以啟動微調流程。此腳本確保微調在 Azure Machine Learning 環境中進行。

執行 *setup_ml.py* 後，微調流程將在 Azure Machine Learning 環境中執行。

#### 在 *fine_tune.py* 檔案中加入程式碼

1. 前往 *finetuning_dir* 資料夾，並在 Visual Studio Code 中開啟 *fine_tune.py* 檔案。

1. 將以下程式碼加入 *fine_tune.py*。

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

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
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
> **您也可以微調 Phi-3.5 模型**
>
> 在 *fine_tune.py* 檔案中，您可以將 `pretrained_model_name` 從 `"microsoft/Phi-3-mini-4k-instruct"` 改成任何您想微調的模型名稱。例如，若改成 `"microsoft/Phi-3.5-mini-instruct"`，就會使用 Phi-3.5-mini-instruct 模型進行微調。您可以造訪 [Hugging Face](https://huggingface.co/)，搜尋您感興趣的模型，然後將其名稱複製貼上到腳本中的 `pretrained_model_name` 欄位。
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="微調 Phi-3.5。":::
>

#### 在 *setup_ml.py* 檔案中加入程式碼

1. 在 Visual Studio Code 中開啟 *setup_ml.py* 檔案。

1. 將以下程式碼加入 *setup_ml.py*。

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

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
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
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
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
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. 將 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `LOCATION` 替換成您的具體資訊。

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **使用 CPU 以最小資料集進行微調的建議**
>
> 如果您想使用 CPU 進行微調，此方法適合擁有福利訂閱（例如 Visual Studio Enterprise 訂閱）或想快速測試微調與部署流程的使用者。
>
> 1. 開啟 *setup_ml* 檔案。
> 1. 將 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `DOCKER_IMAGE_NAME` 替換為以下內容。如果您無法使用 *Standard_E16s_v3*，可以使用等效的 CPU 實例或申請新的配額。
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

1. 輸入以下指令執行 *setup_ml.py* 腳本，並在 Azure Machine Learning 中啟動微調流程。

    ```python
    python setup_ml.py
    ```

1. 在本練習中，您已成功使用 Azure Machine Learning 微調 Phi-3 模型。執行 *setup_ml.py* 腳本後，您已設定 Azure Machine Learning 環境並啟動 *fine_tune.py* 中定義的微調流程。請注意，微調過程可能需要相當長的時間。執行 `python setup_ml.py` 指令後，請耐心等待流程完成。您可以透過終端機中提供的連結，前往 Azure Machine Learning 入口網站監控微調工作的狀態。

    ![查看微調工作。](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871ee8ba32fa508cc4018c0f04e51ad14b95c421ad77151f768f.tw.png)

### 部署微調後的模型

為了將微調後的 Phi-3 模型與 Prompt Flow 整合，您需要部署模型，使其可用於即時推論。此流程包含註冊模型、建立線上端點，以及部署模型。

#### 設定模型名稱、端點名稱與部署名稱

1. 開啟 *config.py* 檔案。

1. 將 `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` 替換為您想要的模型名稱。

1. 將 `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` 替換為您想要的端點名稱。

1. 將 `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` 替換為您想要的部署名稱。

#### 在 *deploy_model.py* 檔案中加入程式碼

執行 *deploy_model.py* 檔案會自動化整個部署流程。它會根據 *config.py* 中設定的模型名稱、端點名稱與部署名稱，註冊模型、建立端點並執行部署。

1. 在 Visual Studio Code 中開啟 *deploy_model.py* 檔案。

1. 將以下程式碼加入 *deploy_model.py*。

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
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

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
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
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
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

1. 執行以下步驟取得 `JOB_NAME`：

    - 前往您建立的 Azure Machine Learning 資源。
    - 選擇 **Studio web URL** 開啟 Azure Machine Learning 工作區。
    - 從左側標籤選擇 **Jobs**。
    - 選擇微調實驗，例如 *finetunephi*。
    - 選擇您建立的工作。
- 將您的工作名稱複製並貼到 *deploy_model.py* 檔案中的 `JOB_NAME = "your-job-name"`。

1. 將 `COMPUTE_INSTANCE_TYPE` 替換為您的具體資訊。

1. 輸入以下指令來執行 *deploy_model.py* 腳本，並開始在 Azure Machine Learning 中部署。

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> 為避免產生額外費用，請務必刪除在 Azure Machine Learning 工作區中建立的端點。
>

#### 在 Azure Machine Learning 工作區檢查部署狀態

1. 前往 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 進入您建立的 Azure Machine Learning 工作區。

1. 選擇 **Studio web URL** 開啟 Azure Machine Learning 工作區。

1. 從左側標籤選擇 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff109f3b7a6b6e4e9689f99b2d7bf021b057f6c0ecbd1ba90c0.tw.png)

2. 選擇您建立的端點。

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4b726505fcfb7d262b0510de029dcbaf36422bb75b77f25dd.tw.png)

3. 在此頁面，您可以管理部署過程中建立的端點。

## 情境 3：與 Prompt flow 整合並與您的自訂模型聊天

### 將自訂 Phi-3 模型整合到 Prompt flow

成功部署微調模型後，您現在可以將它整合到 Prompt flow，讓您的模型能在即時應用中使用，實現多種與自訂 Phi-3 模型的互動任務。

#### 設定微調 Phi-3 模型的 api key 與 endpoint uri

1. 進入您建立的 Azure Machine Learning 工作區。
1. 從左側標籤選擇 **Endpoints**。
1. 選擇您建立的端點。
1. 從導覽選單選擇 **Consume**。
1. 複製並貼上您的 **REST endpoint** 到 *config.py* 檔案中，將 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` 替換為您的 **REST endpoint**。
1. 複製並貼上您的 **Primary key** 到 *config.py* 檔案中，將 `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` 替換為您的 **Primary key**。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53bf44401e184f65a0a088daa76a65f5df5eb4489ae40b890f6.tw.png)

#### 將程式碼加入 *flow.dag.yml* 檔案

1. 在 Visual Studio Code 中開啟 *flow.dag.yml* 檔案。

1. 將以下程式碼加入 *flow.dag.yml*。

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

#### 將程式碼加入 *integrate_with_promptflow.py* 檔案

1. 在 Visual Studio Code 中開啟 *integrate_with_promptflow.py* 檔案。

1. 將以下程式碼加入 *integrate_with_promptflow.py*。

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

    # Logging setup
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

1. 輸入以下指令來執行 *deploy_model.py* 腳本，並開始在 Azure Machine Learning 中部署。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 以下是結果範例：現在您可以與自訂的 Phi-3 模型聊天。建議根據用於微調的資料來提問。

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6412447c9786c562be969a8c3b19791eadffce725fa84f014.tw.png)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。