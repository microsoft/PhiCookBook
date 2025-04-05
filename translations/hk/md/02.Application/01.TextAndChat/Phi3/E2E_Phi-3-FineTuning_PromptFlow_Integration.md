<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fbe98d822c2708e9dbc43509bad607ec",
  "translation_date": "2025-04-04T18:10:04+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "hk"
}
-->
# 微調及整合自定 Phi-3 模型與 Prompt flow

此端到端 (E2E) 範例基於 Microsoft Tech Community 的指南 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)"，介紹如何微調、部署及整合自定 Phi-3 模型與 Prompt flow。

## 概述

在這個 E2E 範例中，您將學習如何微調 Phi-3 模型並將其整合到 Prompt flow 中。透過利用 Azure Machine Learning 和 Prompt flow，您將建立一個工作流程，用於部署和使用自定義 AI 模型。此 E2E 範例分為三個情境：

**情境 1: 設定 Azure 資源並準備微調**

**情境 2: 微調 Phi-3 模型並部署到 Azure Machine Learning Studio**

**情境 3: 與 Prompt flow 整合並與您的自定模型互動**

以下是此 E2E 範例的概述。

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.hk.png)

### 目錄

1. **[情境 1: 設定 Azure 資源並準備微調](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [建立 Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [在 Azure 訂閱中請求 GPU 配額](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [新增角色指派](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [設定專案](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [準備微調所需的資料集](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[情境 2: 微調 Phi-3 模型並部署到 Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [設定 Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [微調 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署微調後的模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[情境 3: 與 Prompt flow 整合並與您的自定模型互動](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [將自定 Phi-3 模型整合到 Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [與您的自定模型互動](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 情境 1: 設定 Azure 資源並準備微調

### 建立 Azure Machine Learning Workspace

1. 在入口網站頁面的**搜尋列**輸入 *azure machine learning*，並從出現的選項中選擇 **Azure Machine Learning**。

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.hk.png)

1. 從導航選單中選擇 **+ Create**。

1. 從導航選單中選擇 **New workspace**。

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.hk.png)

1. 完成以下任務：

    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group** (如有需要可新建)。
    - 輸入 **Workspace Name**。必須為唯一值。
    - 選擇您想使用的 **Region**。
    - 選擇要使用的 **Storage account** (如有需要可新建)。
    - 選擇要使用的 **Key vault** (如有需要可新建)。
    - 選擇要使用的 **Application insights** (如有需要可新建)。
    - 選擇要使用的 **Container registry** (如有需要可新建)。

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.hk.png)

1. 點選 **Review + Create**。

1. 點選 **Create**。

### 在 Azure 訂閱中請求 GPU 配額

在此 E2E 範例中，您將使用 *Standard_NC24ads_A100_v4 GPU* 進行微調，這需要配額請求，而部署使用的 *Standard_E4s_v3* CPU 則不需要配額請求。

> [!NOTE]
>
> 只有 Pay-As-You-Go 訂閱（標準訂閱類型）才有資格申請 GPU 配額；福利訂閱目前不支援。
>
> 對於使用福利訂閱（例如 Visual Studio Enterprise Subscription）或希望快速測試微調和部署過程的人，此教程也提供使用 CPU 微調小型資料集的指導。不過需要注意的是，使用 GPU 和較大的資料集進行微調的效果顯著更好。

1. 造訪 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 完成以下任務以請求 *Standard NCADSA100v4 Family* 配額：

    - 從左側選單選擇 **Quota**。
    - 選擇要使用的 **Virtual machine family**。例如，選擇 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**，其中包括 *Standard_NC24ads_A100_v4* GPU。
    - 從導航選單選擇 **Request quota**。

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.hk.png)

    - 在 Request quota 頁面中，輸入您想使用的 **New cores limit**。例如，24。
    - 在 Request quota 頁面中，點選 **Submit** 以請求 GPU 配額。

> [!NOTE]
> 您可以參考 [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) 文件選擇適合您的 GPU 或 CPU。

### 新增角色指派

為了微調和部署您的模型，您必須先建立 User Assigned Managed Identity (UAI)，並指派適當的權限。此 UAI 將在部署期間用於身份驗證。

#### 建立 User Assigned Managed Identity (UAI)

1. 在入口網站頁面的**搜尋列**輸入 *managed identities*，並從出現的選項中選擇 **Managed Identities**。

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.hk.png)

1. 點選 **+ Create**。

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.hk.png)

1. 完成以下任務：

    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group** (如有需要可新建)。
    - 選擇您想使用的 **Region**。
    - 輸入 **Name**。必須為唯一值。

1. 點選 **Review + create**。

1. 點選 **+ Create**。

#### 為 Managed Identity 新增 Contributor 角色指派

1. 導航至您建立的 Managed Identity 資源。

1. 從左側選單選擇 **Azure role assignments**。

1. 從導航選單選擇 **+Add role assignment**。

1. 在 Add role assignment 頁面中，完成以下任務：
    - 將 **Scope** 設定為 **Resource group**。
    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**。
    - 將 **Role** 設定為 **Contributor**。

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.hk.png)

1. 點選 **Save**。

#### 為 Managed Identity 新增 Storage Blob Data Reader 角色指派

1. 在入口網站頁面的**搜尋列**輸入 *storage accounts*，並從出現的選項中選擇 **Storage accounts**。

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.hk.png)

1. 選擇與您建立的 Azure Machine Learning workspace 相關聯的儲存帳戶。例如，*finetunephistorage*。

1. 完成以下任務以導航至 Add role assignment 頁面：

    - 導航至您建立的 Azure Storage 帳戶。
    - 從左側選單選擇 **Access Control (IAM)**。
    - 從導航選單選擇 **+ Add**。
    - 從導航選單選擇 **Add role assignment**。

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.hk.png)

1. 在 Add role assignment 頁面中，完成以下任務：

    - 在 Role 頁面中，於 **搜尋列**輸入 *Storage Blob Data Reader*，並從出現的選項中選擇 **Storage Blob Data Reader**。
    - 在 Role 頁面中，點選 **Next**。
    - 在 Members 頁面中，選擇 **Assign access to** **Managed identity**。
    - 在 Members 頁面中，選擇 **+ Select members**。
    - 在 Select managed identities 頁面中，選擇您的 Azure **Subscription**。
    - 在 Select managed identities 頁面中，選擇 **Managed identity** 為 **Manage Identity**。
    - 在 Select managed identities 頁面中，選擇您建立的 Manage Identity。例如，*finetunephi-managedidentity*。
    - 在 Select managed identities 頁面中，點選 **Select**。

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.hk.png)

1. 點選 **Review + assign**。

#### 為 Managed Identity 新增 AcrPull 角色指派

1. 在入口網站頁面的**搜尋列**輸入 *container registries*，並從出現的選項中選擇 **Container registries**。

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.hk.png)

1. 選擇與 Azure Machine Learning workspace 相關聯的容器登錄。例如，*finetunephicontainerregistries*

1. 完成以下任務以導航至 Add role assignment 頁面：

    - 從左側選單選擇 **Access Control (IAM)**。
    - 從導航選單選擇 **+ Add**。
    - 從導航選單選擇 **Add role assignment**。

1. 在 Add role assignment 頁面中，完成以下任務：

    - 在 Role 頁面中，於 **搜尋列**輸入 *AcrPull*，並從出現的選項中選擇 **AcrPull**。
    - 在 Role 頁面中，點選 **Next**。
    - 在 Members 頁面中，選擇 **Assign access to** **Managed identity**。
    - 在 Members 頁面中，選擇 **+ Select members**。
    - 在 Select managed identities 頁面中，選擇您的 Azure **Subscription**。
    - 在 Select managed identities 頁面中，選擇 **Managed identity** 為 **Manage Identity**。
    - 在 Select managed identities 頁面中，選擇您建立的 Manage Identity。例如，*finetunephi-managedidentity*。
    - 在 Select managed identities 頁面中，點選 **Select**。
    - 點選 **Review + assign**。

### 設定專案

現在，您將建立一個資料夾以供工作使用，並設置虛擬環境來開發一個程式，該程式能與使用者互動並使用來自 Azure Cosmos DB 的儲存聊天記錄來改進其回應。

#### 建立工作資料夾

1. 打開終端窗口，輸入以下指令以在預設路徑中建立名為 *finetune-phi* 的資料夾。

    ```console
    mkdir finetune-phi
    ```

1. 在終端中輸入以下指令以進入您建立的 *finetune-phi* 資料夾。

    ```console
    cd finetune-phi
    ```

#### 建立虛擬環境

1. 在終端中輸入以下指令以建立名為 *.venv* 的虛擬環境。

    ```console
    python -m venv .venv
    ```

1. 在終端中輸入以下指令以啟用虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> 如果成功，您應該在命令提示符前看到 *(.venv)*。

#### 安裝所需套件

1. 在終端中輸入以下指令以安裝所需套件。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 建立專案檔案

在此練習中，您將建立專案所需的基本檔案，包括下載資料集的腳本、設置 Azure Machine Learning 環境的腳本、微調 Phi-3 模型的腳本，以及部署微調後模型的腳本。您還將建立 *conda.yml* 檔案來設置微調環境。

在此練習中，您將：

- 建立 *download_dataset.py* 檔案以下載資料集。
- 建立 *setup_ml.py* 檔案以設置 Azure Machine Learning 環境。
- 在 *finetuning_dir* 資料夾中建立 *fine_tune.py* 檔案以使用資料集微調 Phi-3 模型。
- 建立 *conda.yml* 檔案以設置微調環境。
- 建立 *deploy_model.py* 檔案以部署微調後的模型。
- 建立 *integrate_with_promptflow.py* 檔案以整合微調後模型並使用 Prompt flow 執行模型。
- 建立 flow.dag.yml 檔案以設置 Prompt flow 的工作流程結構。
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

1. 打開 **Visual Studio Code**。

1. 從選單列中選擇 **File**。

1. 選擇 **Open Folder**。

1. 選擇您建立的 *finetune-phi* 資料夾，位於 *C:\Users\yourUserName\finetune-phi*。

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.hk.png)

1. 在 Visual Studio Code 的左側窗格中，右鍵點擊並選擇 **New File**，以建立名為 *download_dataset.py* 的新檔案。

1. 在 Visual Studio Code 的左側窗格中，右鍵點擊並選擇 **New File**，以建立名為 *setup_ml.py* 的新檔案。

1. 在 Visual Studio Code 的左側窗格中，右鍵點擊並選擇 **New File**，以建立名為 *deploy_model.py* 的新檔案。

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.hk.png)

1. 在 Visual Studio Code 的左側窗格中，右鍵點擊並選擇 **New Folder**，以建立名為 *finetuning_dir* 的新資料夾。

1. 在 *finetuning_dir* 資料夾中，建立名為 *fine_tune.py* 的新檔案。

#### 建立並配置 *conda.yml* 檔案

1. 在 Visual Studio Code 的左側窗格中，右鍵點擊並選擇 **New File**，以建立名為 *conda.yml* 的新檔案。

1. 將以下程式碼添加到 *conda.yml* 檔案中，以設置 Phi-3 模型的微調環境。

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

#### 建立並配置 *config.py* 檔案

1. 在 Visual Studio Code 的左側窗格中，右鍵點擊並選擇 **New File**，以建立名為 *config.py* 的新檔案。

1. 將以下程式碼添加到 *config.py* 檔案中，以包括您的 Azure 資訊。

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

#### 添加 Azure 環境變數

1. 完成以下任務以添加 Azure 訂閱 ID：

    - 在入口網站頁面的**搜尋列**輸入 *subscriptions*，並從出現的選項中選擇 **Subscriptions**。
    - 選擇您目前使用的 Azure 訂閱。
    - 將您的訂閱 ID 複製並貼到 *config.py* 檔案中。
![尋找訂閱 ID。](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.hk.png)

1. 按以下步驟新增 Azure Workspace 名稱：

    - 前往你創建的 Azure Machine Learning 資源。
    - 複製你的帳戶名稱並將其貼到 *config.py* 檔案中。

    ![尋找 Azure Machine Learning 名稱。](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.hk.png)

1. 按以下步驟新增 Azure 資源群組名稱：

    - 前往你創建的 Azure Machine Learning 資源。
    - 複製你的 Azure 資源群組名稱並將其貼到 *config.py* 檔案中。

    ![尋找資源群組名稱。](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.hk.png)

2. 按以下步驟新增 Azure Managed Identity 名稱：

    - 前往你創建的 Managed Identities 資源。
    - 複製你的 Azure Managed Identity 名稱並將其貼到 *config.py* 檔案中。

    ![尋找 UAI。](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.hk.png)

### 為微調準備數據集

在這個練習中，你將執行 *download_dataset.py* 檔案，將 *ULTRACHAT_200k* 數據集下載到本地環境。然後，你將使用這些數據集在 Azure Machine Learning 中微調 Phi-3 模型。

#### 使用 *download_dataset.py* 下載數據集

1. 在 Visual Studio Code 中打開 *download_dataset.py* 檔案。

1. 在 *download_dataset.py* 中新增以下代碼。

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
> **使用最小數據集和 CPU 進行微調的指導**
>
> 如果你希望使用 CPU 進行微調，這種方法非常適合擁有訂閱福利（如 Visual Studio Enterprise 訂閱）的人，或者快速測試微調和部署流程。
>
> 替換 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. 在終端中輸入以下命令來執行腳本並將數據集下載到本地環境。

    ```console
    python download_data.py
    ```

1. 確認數據集已成功保存到本地 *finetune-phi/data* 目錄中。

> [!NOTE]
>
> **數據集大小與微調時間**
>
> 在這個端到端範例中，你只使用 1% 的數據集（`train_sft[:1%]`）。這顯著減少了數據量，加快了上傳和微調的過程。你可以調整百分比以找到訓練時間與模型性能之間的平衡。使用較小的數據集子集能減少微調所需的時間，使流程更易於管理。

## 場景 2：微調 Phi-3 模型並在 Azure Machine Learning Studio 中部署

### 設置 Azure CLI

你需要設置 Azure CLI 來驗證你的環境。Azure CLI 允許你直接從命令列管理 Azure 資源，並為 Azure Machine Learning 提供訪問這些資源所需的憑據。開始之前，請安裝 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)。

1. 打開終端視窗，輸入以下命令以登錄你的 Azure 帳戶。

    ```console
    az login
    ```

1. 選擇要使用的 Azure 帳戶。

1. 選擇要使用的 Azure 訂閱。

    ![尋找資源群組名稱。](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.hk.png)

> [!TIP]
>
> 如果你在登錄 Azure 時遇到困難，可以嘗試使用設備代碼。在終端視窗中輸入以下命令以登錄你的 Azure 帳戶：
>
> ```console
> az login --use-device-code
> ```
>

### 微調 Phi-3 模型

在這個練習中，你將使用提供的數據集微調 Phi-3 模型。首先，你將在 *fine_tune.py* 檔案中定義微調過程。然後，你將配置 Azure Machine Learning 環境，並通過執行 *setup_ml.py* 檔案啟動微調過程。這個腳本確保微調在 Azure Machine Learning 環境中進行。

通過執行 *setup_ml.py*，你將在 Azure Machine Learning 環境中運行微調過程。

#### 在 *fine_tune.py* 檔案中新增代碼

1. 前往 *finetuning_dir* 資料夾並在 Visual Studio Code 中打開 *fine_tune.py* 檔案。

1. 在 *fine_tune.py* 中新增以下代碼。

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

1. 保存並關閉 *fine_tune.py* 檔案。

> [!TIP]
> **你可以微調 Phi-3.5 模型**
>
> 在 *fine_tune.py* 檔案中，你可以將 `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` 字段更改為你的腳本。
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="微調 Phi-3.5。":::
>

#### 在 *setup_ml.py* 檔案中新增代碼

1. 在 Visual Studio Code 中打開 *setup_ml.py* 檔案。

1. 在 *setup_ml.py* 中新增以下代碼。

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

1. 替換 `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` 為你的具體資訊。

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **使用最小數據集和 CPU 進行微調的指導**
>
> 如果你希望使用 CPU 進行微調，這種方法非常適合擁有訂閱福利（如 Visual Studio Enterprise 訂閱）的人，或者快速測試微調和部署流程。
>
> 1. 打開 *setup_ml* 檔案。
> 1. 替換 `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` 為你的具體資訊。
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. 輸入以下命令以執行 *setup_ml.py* 腳本並在 Azure Machine Learning 中啟動微調過程。

    ```python
    python setup_ml.py
    ```

1. 在這個練習中，你成功使用 Azure Machine Learning 微調了 Phi-3 模型。通過執行 *setup_ml.py* 腳本，你已設置 Azure Machine Learning 環境並啟動了在 *fine_tune.py* 檔案中定義的微調過程。請注意，微調過程可能需要相當長的時間。執行 `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.hk.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"`，並為你的部署設定所需的名稱。

#### 在 *deploy_model.py* 檔案中新增代碼

執行 *deploy_model.py* 檔案會自動化整個部署過程。它會根據 *config.py* 檔案中指定的設置（包括模型名稱、端點名稱和部署名稱）註冊模型、創建端點並執行部署。

1. 在 Visual Studio Code 中打開 *deploy_model.py* 檔案。

1. 在 *deploy_model.py* 中新增以下代碼。

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

1. 按以下步驟獲取 `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` 並替換為你的具體資訊。

1. 輸入以下命令以執行 *deploy_model.py* 腳本並在 Azure Machine Learning 中啟動部署過程。

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> 為避免帳戶產生額外費用，請確保刪除在 Azure Machine Learning 工作區中創建的端點。
>

#### 在 Azure Machine Learning 工作區中檢查部署狀態

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 前往你創建的 Azure Machine Learning 工作區。

1. 選擇 **Studio web URL** 以打開 Azure Machine Learning 工作區。

1. 從左側選單中選擇 **Endpoints**。

    ![選擇端點。](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.hk.png)

2. 選擇你創建的端點。

    ![選擇你創建的端點。](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.hk.png)

3. 在此頁面上，你可以管理部署過程中創建的端點。

## 場景 3：與 Prompt flow 集成並與自定義模型互動

### 將自定義 Phi-3 模型與 Prompt flow 集成

成功部署微調模型後，你現在可以將其與 Prompt flow 集成，從而在實時應用中使用你的模型，實現各種與自定義 Phi-3 模型的互動任務。

#### 設定微調 Phi-3 模型的 API 金鑰和端點 URI

1. 前往你創建的 Azure Machine Learning 工作區。
1. 從左側選單中選擇 **Endpoints**。
1. 選擇你創建的端點。
1. 從導航選單中選擇 **Consume**。
1. 複製並將你的 **REST endpoint** 貼到 *config.py* 檔案中，替換 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` 為你的 **Primary key**。

    ![複製 API 金鑰和端點 URI。](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.hk.png)

#### 在 *flow.dag.yml* 檔案中新增代碼

1. 在 Visual Studio Code 中打開 *flow.dag.yml* 檔案。

1. 在 *flow.dag.yml* 中新增以下代碼。

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

#### 在 *integrate_with_promptflow.py* 檔案中新增代碼

1. 在 Visual Studio Code 中打開 *integrate_with_promptflow.py* 檔案。

1. 在 *integrate_with_promptflow.py* 中新增以下代碼。

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

### 與你的自定義模型互動

1. 輸入以下命令以執行 *deploy_model.py* 腳本並啟動 Azure Machine Learning 中的部署過程。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 以下是結果範例：現在你可以與你的自定義 Phi-3 模型互動。建議根據微調使用的數據提出問題。

    ![Prompt flow 範例。](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.hk.png)

**免責聲明**:  
此文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。如需關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。