<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ed86d361ac6d4cc8bfb47428e6a2a247",
  "translation_date": "2025-04-04T18:14:45+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hk"
}
-->
# 微調及整合自訂 Phi-3 模型與 Azure AI Foundry 中的 Prompt Flow

這個端到端（E2E）範例基於 Microsoft Tech Community 的指南「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」，介紹如何在 Azure AI Foundry 中微調、部署及整合自訂 Phi-3 模型與 Prompt Flow。與端到端範例「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」不同的是，本教程完全專注於在 Azure AI / ML Studio 中微調和整合模型，而不涉及本地執行代碼。

## 概述

在此端到端範例中，您將學習如何微調 Phi-3 模型並將其整合到 Azure AI Foundry 的 Prompt Flow 中。藉助 Azure AI / ML Studio，您將建立一個工作流程來部署和使用自訂 AI 模型。此端到端範例分為三個場景：

**場景 1：設置 Azure 資源並準備微調**

**場景 2：微調 Phi-3 模型並部署到 Azure Machine Learning Studio**

**場景 3：整合到 Prompt Flow 並在 Azure AI Foundry 中與您的自訂模型進行交互**

以下是此端到端範例的概述。

![Phi-3-FineTuning_PromptFlow_Integration 概述.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.hk.png)

### 目錄

1. **[場景 1：設置 Azure 資源並準備微調](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [創建 Azure Machine Learning 工作區](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [在 Azure 訂閱中申請 GPU 配額](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [添加角色分配](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [設置項目](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [準備微調所需的數據集](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[場景 2：微調 Phi-3 模型並部署到 Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [微調 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署微調後的 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[場景 3：整合到 Prompt Flow 並在 Azure AI Foundry 中與您的自訂模型進行交互](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [將自訂 Phi-3 模型整合到 Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [與您的自訂 Phi-3 模型進行交互](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 場景 1：設置 Azure 資源並準備微調

### 創建 Azure Machine Learning 工作區

1. 在入口網站頁面的**搜索欄**中輸入 *azure machine learning*，並從出現的選項中選擇 **Azure Machine Learning**。

    ![輸入 azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.hk.png)

2. 從導航菜單中選擇 **+ 創建**。

3. 從導航菜單中選擇 **新工作區**。

    ![選擇新工作區.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.hk.png)

4. 完成以下任務：

    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的**資源組**（如有需要可創建新的）。
    - 輸入 **工作區名稱**，需為唯一值。
    - 選擇您希望使用的**區域**。
    - 選擇要使用的**存儲帳戶**（如有需要可創建新的）。
    - 選擇要使用的**密鑰保管庫**（如有需要可創建新的）。
    - 選擇要使用的**應用洞察**（如有需要可創建新的）。
    - 選擇要使用的**容器註冊表**（如有需要可創建新的）。

    ![填寫 azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.hk.png)

5. 選擇 **檢查 + 創建**。

6. 選擇 **創建**。

### 在 Azure 訂閱中申請 GPU 配額

在本教程中，您將使用 GPU 微調並部署 Phi-3 模型。微調使用 *Standard_NC24ads_A100_v4* GPU，部署使用 *Standard_NC6s_v3* GPU，兩者均需要申請配額。

> [!NOTE]
>
> 只有「按需付費」訂閱（標準訂閱類型）才有資格分配 GPU；目前不支持福利訂閱。
>

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 執行以下任務以申請 *Standard NCADSA100v4 Family* 配額：

    - 從左側選項卡中選擇 **配額**。
    - 選擇要使用的**虛擬機系列**，例如 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**，其中包含 *Standard_NC24ads_A100_v4* GPU。
    - 從導航菜單中選擇 **申請配額**。

        ![申請配額.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.hk.png)

    - 在申請配額頁面中，輸入您希望使用的**新核心限制**，例如 24。
    - 在申請配額頁面中，選擇 **提交**以申請 GPU 配額。

1. 執行以下任務以申請 *Standard NCSv3 Family* 配額：

    - 從左側選項卡中選擇 **配額**。
    - 選擇要使用的**虛擬機系列**，例如 **Standard NCSv3 Family Cluster Dedicated vCPUs**，其中包含 *Standard_NC6s_v3* GPU。
    - 從導航菜單中選擇 **申請配額**。
    - 在申請配額頁面中，輸入您希望使用的**新核心限制**，例如 24。
    - 在申請配額頁面中，選擇 **提交**以申請 GPU 配額。

### 添加角色分配

要微調和部署您的模型，您需要先創建一個「用戶分配的托管身份」（UAI），並為其分配適當的權限。此 UAI 將在部署期間用於身份驗證。

#### 創建用戶分配的托管身份（UAI）

1. 在入口網站頁面的**搜索欄**中輸入 *managed identities*，並從出現的選項中選擇 **Managed Identities**。

    ![輸入 managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.hk.png)

1. 選擇 **+ 創建**。

    ![選擇創建.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.hk.png)

1. 完成以下任務：

    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的**資源組**（如有需要可創建新的）。
    - 選擇您希望使用的**區域**。
    - 輸入 **名稱**，需為唯一值。

    ![選擇創建.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.hk.png)

1. 選擇 **檢查 + 創建**。

1. 選擇 **+ 創建**。

#### 為托管身份添加 Contributor 角色分配

1. 導航到您創建的托管身份資源。

1. 從左側選項卡中選擇 **Azure 角色分配**。

1. 從導航菜單中選擇 **+ 添加角色分配**。

1. 在添加角色分配頁面中，完成以下任務：
    - 將**範圍**設置為 **資源組**。
    - 選擇您的 Azure **訂閱**。
    - 選擇要使用的**資源組**。
    - 將**角色**設置為 **Contributor**。

    ![填寫 Contributor 角色.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.hk.png)

2. 選擇 **保存**。

#### 為托管身份添加 Storage Blob Data Reader 角色分配

1. 在入口網站頁面的**搜索欄**中輸入 *storage accounts*，並從出現的選項中選擇 **Storage accounts**。

    ![輸入 storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.hk.png)

1. 選擇與您創建的 Azure Machine Learning 工作區相關聯的存儲帳戶。例如，*finetunephistorage*。

1. 執行以下任務以導航到添加角色分配頁面：

    - 導航到您創建的 Azure 存儲帳戶。
    - 從左側選項卡中選擇 **訪問控制（IAM）**。
    - 從導航菜單中選擇 **+ 添加**。
    - 從導航菜單中選擇 **添加角色分配**。

    ![添加角色.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.hk.png)

1. 在添加角色分配頁面中，完成以下任務：

    - 在角色頁面中，在**搜索欄**中輸入 *Storage Blob Data Reader*，並從出現的選項中選擇 **Storage Blob Data Reader**。
    - 在角色頁面中，選擇 **下一步**。
    - 在成員頁面中，選擇 **分配訪問給** **托管身份**。
    - 在成員頁面中，選擇 **+ 選擇成員**。
    - 在選擇托管身份頁面中，選擇您的 Azure **訂閱**。
    - 在選擇托管身份頁面中，選擇 **托管身份**至 **托管身份**。
    - 在選擇托管身份頁面中，選擇您創建的托管身份。例如，*finetunephi-managedidentity*。
    - 在選擇托管身份頁面中，選擇 **選擇**。

    ![選擇托管身份.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.hk.png)

1. 選擇 **檢查 + 分配**。

#### 為托管身份添加 AcrPull 角色分配

1. 在入口網站頁面的**搜索欄**中輸入 *container registries*，並從出現的選項中選擇 **Container registries**。

    ![輸入 container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.hk.png)

1. 選擇與 Azure Machine Learning 工作區相關聯的容器註冊表。例如，*finetunephicontainerregistry*。

1. 執行以下任務以導航到添加角色分配頁面：

    - 從左側選項卡中選擇 **訪問控制（IAM）**。
    - 從導航菜單中選擇 **+ 添加**。
    - 從導航菜單中選擇 **添加角色分配**。

1. 在添加角色分配頁面中，完成以下任務：

    - 在角色頁面中，在**搜索欄**中輸入 *AcrPull*，並從出現的選項中選擇 **AcrPull**。
    - 在角色頁面中，選擇 **下一步**。
    - 在成員頁面中，選擇 **分配訪問給** **托管身份**。
    - 在成員頁面中，選擇 **+ 選擇成員**。
    - 在選擇托管身份頁面中，選擇您的 Azure **訂閱**。
    - 在選擇托管身份頁面中，選擇 **托管身份**至 **托管身份**。
    - 在選擇托管身份頁面中，選擇您創建的托管身份。例如，*finetunephi-managedidentity*。
    - 在選擇托管身份頁面中，選擇 **選擇**。
    - 選擇 **檢查 + 分配**。

### 設置項目

為下載微調所需的數據集，您需要設置本地環境。

在此操作中，您將：

- 創建一個工作文件夾。
- 創建虛擬環境。
- 安裝所需的套件。
- 創建 *download_dataset.py* 文件以下載數據集。

#### 創建工作文件夾

1. 打開終端窗口，輸入以下命令以在默認路徑中創建名為 *finetune-phi* 的文件夾。

    ```console
    mkdir finetune-phi
    ```

2. 在終端中輸入以下命令以進入您創建的 *finetune-phi* 文件夾。

    ```console
    cd finetune-phi
    ```

#### 創建虛擬環境

1. 在終端中輸入以下命令以創建名為 *.venv* 的虛擬環境。

    ```console
    python -m venv .venv
    ```

2. 在終端中輸入以下命令以激活虛擬環境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 如果成功，您應該能在命令提示符前看到 *(.venv)*。

#### 安裝所需的套件

1. 在終端中輸入以下命令以安裝所需的套件。

    ```console
    pip install datasets==2.19.1
    ```

#### 創建 `download_dataset.py`

> [!NOTE]
> 完整文件夾結構：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. 打開 **Visual Studio Code**。

1. 從菜單欄中選擇 **文件**。

1. 選擇 **打開文件夾**。

1. 選擇您創建的 *finetune-phi* 文件夾，位於 *C:\Users\yourUserName\finetune-phi*。

    ![選擇您創建的文件夾.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.hk.png)

1. 在 Visual Studio Code 的左側窗格中右鍵點擊並選擇 **新建文件**，以創建名為 *download_dataset.py* 的新文件。

    ![創建新文件.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.hk.png)

### 準備微調所需的數據集

在此操作中，您將運行 *download_dataset.py* 文件以將 *ultrachat_200k* 數據集下載到您的本地環境。您將使用此數據集在 Azure Machine Learning 中微調 Phi-3 模型。

在此操作中，您將：

- 在 *download_dataset.py* 文件中添加代碼以下載數據集。
- 運行 *download_dataset.py* 文件以將數據集下載到您的本地環境。

#### 使用 *download_dataset.py* 下載您的數據集

1. 在 Visual Studio Code 中打開 *download_dataset.py* 文件。

1. 在 *download_dataset.py* 文件中添加以下代碼。

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

1. 在終端中輸入以下命令以運行腳本並將數據集下載到您的本地環境。

    ```console
    python download_dataset.py
    ```

1. 驗證數據集是否成功保存到您的本地 *finetune-phi/data* 目錄。

> [!NOTE]
>
> #### 關於數據集大小及微調時間的注意事項
>
> 在本教程中，您僅使用數據集的 1%（`split='train[:1%]'`）。這顯著減少了數據量，加快了上傳和微調過程。您可以調整百分比以找到訓練時間和模型性能之間的最佳平衡。使用較小的數據集子集能減少微調所需時間，使教程過程更易管理。

## 場景 2：微調 Phi-3 模型並部署到 Azure Machine Learning Studio


1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 從左側選單選擇 **Compute**。

1. 在導航欄中選擇 **Compute clusters**。

1. 點擊 **+ New**。

    ![選擇計算資源。](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.hk.png)

1. 完成以下操作：

    - 選擇你想使用的 **Region**。
    - 將 **Virtual machine tier** 設置為 **Dedicated**。
    - 將 **Virtual machine type** 設置為 **GPU**。
    - 將 **Virtual machine size** 篩選設置為 **Select from all options**。
    - 將 **Virtual machine size** 設置為 **Standard_NC24ads_A100_v4**。

    ![創建集群。](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.hk.png)

1. 點擊 **Next**。

1. 完成以下操作：

    - 輸入 **Compute name**，必須是唯一值。
    - 將 **Minimum number of nodes** 設置為 **0**。
    - 將 **Maximum number of nodes** 設置為 **1**。
    - 將 **Idle seconds before scale down** 設置為 **120**。

    ![創建集群。](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.hk.png)

1. 點擊 **Create**。

#### 微調 Phi-3 模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇你創建的 Azure Machine Learning 工作區。

    ![選擇你創建的工作區。](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hk.png)

1. 完成以下操作：

    - 從左側選單選擇 **Model catalog**。
    - 在 **搜索欄**中輸入 *phi-3-mini-4k*，並從出現的選項中選擇 **Phi-3-mini-4k-instruct**。

    ![輸入 phi-3-mini-4k。](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.hk.png)

1. 從導航欄選擇 **Fine-tune**。

    ![選擇微調。](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.hk.png)

1. 完成以下操作：

    - 將 **Select task type** 設置為 **Chat completion**。
    - 點擊 **+ Select data** 上傳 **Training data**。
    - 將驗證數據上傳類型設置為 **Provide different validation data**。
    - 點擊 **+ Select data** 上傳 **Validation data**。

    ![填寫微調頁面。](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.hk.png)

    > [!TIP]
    >
    > 你可以選擇 **Advanced settings** 自定義配置，例如 **learning_rate** 和 **lr_scheduler_type**，以根據你的特定需求優化微調過程。

1. 點擊 **Finish**。

1. 在本練習中，你成功使用 Azure Machine Learning 微調了 Phi-3 模型。請注意，微調過程可能需要較長時間。運行微調任務後，你需要等待其完成。你可以通過導航到 Azure Machine Learning 工作區左側的 Jobs 標籤來監控微調任務的狀態。在下一系列中，你將部署微調模型並與 Prompt flow 集成。

    ![查看微調任務。](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.hk.png)

### 部署微調後的 Phi-3 模型

要將微調後的 Phi-3 模型與 Prompt flow 集成，你需要部署模型以便進行實時推斷。此過程包括註冊模型、創建在線端點以及部署模型。

在本練習中，你將：

- 在 Azure Machine Learning 工作區註冊微調模型。
- 創建在線端點。
- 部署已註冊的微調 Phi-3 模型。

#### 註冊微調模型

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 選擇你創建的 Azure Machine Learning 工作區。

    ![選擇你創建的工作區。](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.hk.png)

1. 從左側選單選擇 **Models**。
1. 點擊 **+ Register**。
1. 選擇 **From a job output**。

    ![註冊模型。](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.hk.png)

1. 選擇你創建的任務。

    ![選擇任務。](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.hk.png)

1. 點擊 **Next**。

1. 將 **Model type** 設置為 **MLflow**。

1. 確保 **Job output** 被選中；它應該自動被選中。

    ![選擇輸出。](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.hk.png)

2. 點擊 **Next**。

3. 點擊 **Register**。

    ![選擇註冊。](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.hk.png)

4. 你可以通過導航到左側選單的 **Models** 來查看已註冊的模型。

    ![已註冊模型。](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.hk.png)

#### 部署微調模型

1. 導航到你創建的 Azure Machine Learning 工作區。

1. 從左側選單選擇 **Endpoints**。

1. 在導航欄中選擇 **Real-time endpoints**。

    ![創建端點。](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.hk.png)

1. 點擊 **Create**。

1. 選擇你創建的已註冊模型。

    ![選擇已註冊模型。](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.hk.png)

1. 點擊 **Select**。

1. 完成以下操作：

    - 將 **Virtual machine** 設置為 *Standard_NC6s_v3*。
    - 選擇你想使用的 **Instance count**，例如 *1*。
    - 將 **Endpoint** 設置為 **New** 以創建端點。
    - 輸入 **Endpoint name**，必須是唯一值。
    - 輸入 **Deployment name**，必須是唯一值。

    ![填寫部署設置。](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.hk.png)

1. 點擊 **Deploy**。

> [!WARNING]
> 為避免額外費用，請確保在 Azure Machine Learning 工作區中刪除已創建的端點。
>

#### 在 Azure Machine Learning 工作區中檢查部署狀態

1. 導航到你創建的 Azure Machine Learning 工作區。

1. 從左側選單選擇 **Endpoints**。

1. 選擇你創建的端點。

    ![選擇端點](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.hk.png)

1. 在此頁面，你可以在部署過程中管理端點。

> [!NOTE]
> 部署完成後，請確保 **Live traffic** 設置為 **100%**。如果不是，請選擇 **Update traffic** 調整流量設置。注意，如果流量設置為 0%，則無法測試模型。
>
> ![設置流量。](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.hk.png)
>

## 場景 3：與 Prompt flow 集成並在 Azure AI Foundry 中與自定義模型交互

### 將自定義 Phi-3 模型與 Prompt flow 集成

成功部署你的微調模型後，你現在可以將其與 Prompt Flow 集成，以在實時應用中使用你的模型，從而實現與自定義 Phi-3 模型的多種交互任務。

在本練習中，你將：

- 創建 Azure AI Foundry Hub。
- 創建 Azure AI Foundry Project。
- 創建 Prompt flow。
- 為微調 Phi-3 模型添加自定義連接。
- 設置 Prompt flow 與你的自定義 Phi-3 模型交互。

> [!NOTE]
> 你也可以使用 Azure ML Studio 與 Promptflow 集成。相同的集成過程適用於 Azure ML Studio。

#### 創建 Azure AI Foundry Hub

在創建 Project 之前，你需要創建 Hub。Hub 類似於資源組，允許你在 Azure AI Foundry 中組織和管理多個 Project。

1. 訪問 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 從左側選單選擇 **All hubs**。

1. 在導航欄中選擇 **+ New hub**。

    ![創建 Hub。](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.hk.png)

1. 完成以下操作：

    - 輸入 **Hub name**，必須是唯一值。
    - 選擇你的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**（如有需要，創建一個新的）。
    - 選擇你想使用的 **Location**。
    - 選擇要使用的 **Connect Azure AI Services**（如有需要，創建一個新的）。
    - 將 **Connect Azure AI Search** 設置為 **Skip connecting**。

    ![填寫 Hub。](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.hk.png)

1. 點擊 **Next**。

#### 創建 Azure AI Foundry Project

1. 在你創建的 Hub 中，從左側選單選擇 **All projects**。

1. 在導航欄中選擇 **+ New project**。

    ![選擇新 Project。](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.hk.png)

1. 輸入 **Project name**，必須是唯一值。

    ![創建 Project。](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.hk.png)

1. 點擊 **Create a project**。

#### 為微調 Phi-3 模型添加自定義連接

要將你的自定義 Phi-3 模型與 Prompt flow 集成，你需要在自定義連接中保存模型的端點和密鑰。此設置確保在 Prompt flow 中訪問你的自定義 Phi-3 模型。

#### 設置微調 Phi-3 模型的 API 密鑰和端點 URI

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 導航到你創建的 Azure Machine Learning 工作區。

1. 從左側選單選擇 **Endpoints**。

    ![選擇端點。](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.hk.png)

1. 選擇你創建的端點。

    ![選擇已創建的端點。](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.hk.png)

1. 從導航欄選擇 **Consume**。

1. 複製你的 **REST endpoint** 和 **Primary key**。
![複製 API key 同 endpoint URI。](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.hk.png)

#### 加入自訂連接

1. 瀏覽 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 前往你已建立嘅 Azure AI Foundry 項目。

1. 喺你建立嘅項目中，揀選左邊嘅 **Settings**。

1. 選擇 **+ New connection**。

    ![選擇新連接。](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.hk.png)

1. 喺導航選單揀選 **Custom keys**。

    ![選擇自訂密鑰。](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.hk.png)

1. 執行以下操作：

    - 選擇 **+ Add key value pairs**。
    - 喺密鑰名稱輸入 **endpoint**，並將你喺 Azure ML Studio 複製嘅 endpoint 貼到值字段。
    - 再次選擇 **+ Add key value pairs**。
    - 喺密鑰名稱輸入 **key**，並將你喺 Azure ML Studio 複製嘅 key 貼到值字段。
    - 加入密鑰後，選擇 **is secret**，防止密鑰被暴露。

    ![新增連接。](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.hk.png)

1. 選擇 **Add connection**。

#### 建立 Prompt flow

你已經喺 Azure AI Foundry 中加入咗自訂連接。接住落嚟，我哋會利用以下步驟建立 Prompt flow。然後，你會將呢個 Prompt flow 連接到自訂連接，咁你就可以喺 Prompt flow 中使用經微調嘅模型。

1. 前往你已建立嘅 Azure AI Foundry 項目。

1. 喺左邊選擇 **Prompt flow**。

1. 喺導航選單選擇 **+ Create**。

    ![選擇 Promptflow。](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.hk.png)

1. 喺導航選單選擇 **Chat flow**。

    ![選擇 Chat flow。](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.hk.png)

1. 輸入 **Folder name**。

    ![輸入名稱。](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.hk.png)

2. 選擇 **Create**。

#### 設置 Prompt flow 同你嘅自訂 Phi-3 模型聊天

你需要將經微調嘅 Phi-3 模型整合到 Prompt flow 中。不過，現有嘅 Prompt flow 並唔係為此目的設計嘅。因此，你需要重新設計 Prompt flow，令其可以整合自訂模型。

1. 喺 Prompt flow 中，執行以下操作以重建現有流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 文件中所有現有代碼。
    - 喺 *flow.dag.yml* 文件中加入以下代碼：

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

    ![選擇 Raw file mode。](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.hk.png)

1. 喺 *integrate_with_promptflow.py* 文件中加入以下代碼，以喺 Prompt flow 中使用自訂 Phi-3 模型。

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

    ![貼上 Prompt flow 代碼。](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.hk.png)

> [!NOTE]
> 如需更詳細嘅 Azure AI Foundry 中使用 Prompt flow 嘅資訊，你可以參考 [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input** 同 **Chat output** 以啟用同你嘅模型聊天。

    ![輸入輸出。](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.hk.png)

1. 而家你已準備好同自訂 Phi-3 模型聊天。喺下一個練習中，你會學習如何啟動 Prompt flow 並利用其同經微調嘅 Phi-3 模型聊天。

> [!NOTE]
>
> 重建後嘅流程應該如下圖所示：
>
> ![流程示例。](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.hk.png)
>

### 同你嘅自訂 Phi-3 模型聊天

而家你已微調並整合咗自訂 Phi-3 模型到 Prompt flow，你可以開始同模型互動。呢個練習會指導你如何設置同啟動 Prompt flow，同模型進行聊天。跟住呢啲步驟，你就可以充分利用經微調嘅 Phi-3 模型進行各種任務同對話。

- 使用 Prompt flow 同你嘅自訂 Phi-3 模型聊天。

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 以啟動 Prompt flow。

    ![啟動計算會話。](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.hk.png)

1. 選擇 **Validate and parse input** 以更新參數。

    ![驗證輸入。](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.hk.png)

1. 選擇 **connection** 嘅 **Value**，指向你創建嘅自訂連接。例如，*connection*。

    ![連接。](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.hk.png)

#### 同你嘅自訂模型聊天

1. 選擇 **Chat**。

    ![選擇 Chat。](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.hk.png)

1. 以下係結果示例：而家你可以同你嘅自訂 Phi-3 模型聊天。建議根據用於微調嘅數據問問題。

    ![使用 Prompt flow 聊天。](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.hk.png)

**免責聲明**：  
本文檔已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。雖然我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文檔應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或錯誤解釋承擔責任。