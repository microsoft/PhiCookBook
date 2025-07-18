<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:10:19+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "zh"
}
-->
# 使用 Prompt flow 微调并集成自定义 Phi-3 模型

本端到端（E2E）示例基于微软技术社区的指南“[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)”。介绍了微调、部署及通过 Prompt flow 集成自定义 Phi-3 模型的流程。

## 概述

在本 E2E 示例中，您将学习如何微调 Phi-3 模型并将其与 Prompt flow 集成。通过利用 Azure 机器学习和 Prompt flow，您将建立一个用于部署和使用自定义 AI 模型的工作流。本示例分为三个场景：

**场景 1：设置 Azure 资源并准备微调**

**场景 2：微调 Phi-3 模型并在 Azure 机器学习工作室中部署**

**场景 3：与 Prompt flow 集成并与您的自定义模型聊天**

以下是本 E2E 示例的整体架构。

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468cf3bbb3158cf273380cbdf7fcec042c7328e1559c6b2e2632.zh.png)

### 目录

1. **[场景 1：设置 Azure 资源并准备微调](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [创建 Azure 机器学习工作区](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [申请 Azure 订阅中的 GPU 配额](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [添加角色分配](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [设置项目](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [准备微调数据集](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[场景 2：微调 Phi-3 模型并在 Azure 机器学习工作室中部署](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [设置 Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [微调 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署微调后的模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[场景 3：与 Prompt flow 集成并与您的自定义模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [将自定义 Phi-3 模型集成到 Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [与您的自定义模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 场景 1：设置 Azure 资源并准备微调

### 创建 Azure 机器学习工作区

1. 在门户页面顶部的**搜索栏**中输入 *azure machine learning*，然后从出现的选项中选择 **Azure Machine Learning**。

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c600d87008fb78206d2cf90c0b920c231618a8ec8baaa6f46c3.zh.png)

1. 从导航菜单中选择 **+ 创建**。

1. 从导航菜单中选择 **新建工作区**。

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4fbb808d1bbcd92962692b1fa687f4c5d3952f453177825bc.zh.png)

1. 执行以下操作：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要可新建）。
    - 输入 **工作区名称**，必须唯一。
    - 选择您想使用的 **区域**。
    - 选择要使用的 **存储帐户**（如有需要可新建）。
    - 选择要使用的 **密钥保管库**（如有需要可新建）。
    - 选择要使用的 **应用程序洞察**（如有需要可新建）。
    - 选择要使用的 **容器注册表**（如有需要可新建）。

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb141b9e8c16f31834e82e831275bd9faad0b70343f46255de.zh.png)

1. 选择 **查看 + 创建**。

1. 选择 **创建**。

### 申请 Azure 订阅中的 GPU 配额

在本 E2E 示例中，您将使用 *Standard_NC24ads_A100_v4 GPU* 进行微调，该 GPU 需要申请配额；部署时使用 *Standard_E4s_v3* CPU，无需申请配额。

> [!NOTE]
>
> 只有按需付费订阅（标准订阅类型）有资格申请 GPU 配额，福利订阅目前不支持。
>
> 对于使用福利订阅（如 Visual Studio Enterprise 订阅）或希望快速测试微调和部署流程的用户，本教程也提供了使用 CPU 和最小数据集进行微调的指导。但需要注意的是，使用 GPU 和更大数据集时微调效果会显著更好。

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 执行以下操作申请 *Standard NCADSA100v4 Family* 配额：

    - 从左侧标签选择 **配额**。
    - 选择要使用的 **虚拟机系列**，例如选择包含 *Standard_NC24ads_A100_v4* GPU 的 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**。
    - 从导航菜单选择 **申请配额**。

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab8348515fcfba9d0279114f04065df8bd6fb78e3d3704e627545.zh.png)

    - 在申请配额页面中，输入您想使用的 **新核心限制**，例如 24。
    - 在申请配额页面中，选择 **提交** 以申请 GPU 配额。

> [!NOTE]
> 您可以参考文档 [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) 选择适合您需求的 GPU 或 CPU。

### 添加角色分配

要微调和部署模型，您必须先创建一个用户分配托管身份（User Assigned Managed Identity，UAI），并为其分配相应权限。该 UAI 将用于部署时的身份验证。

#### 创建用户分配托管身份（UAI）

1. 在门户页面顶部的**搜索栏**中输入 *managed identities*，然后从出现的选项中选择 **Managed Identities**。

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8a95d6e7762f1b087275a9634677f0a4e355717550ace3c02.zh.png)

1. 选择 **+ 创建**。

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a8c70af922bf28a573c0744fb642f8228d62214b010a070d9.zh.png)

1. 执行以下操作：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要可新建）。
    - 选择您想使用的 **区域**。
    - 输入 **名称**，必须唯一。

1. 选择 **查看 + 创建**。

1. 选择 **+ 创建**。

#### 为托管身份添加 Contributor 角色分配

1. 导航到您创建的托管身份资源。

1. 从左侧标签选择 **Azure 角色分配**。

1. 从导航菜单选择 **+ 添加角色分配**。

1. 在添加角色分配页面，执行以下操作：
    - 将 **作用域** 设置为 **资源组**。
    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**。
    - 将 **角色** 设置为 **Contributor**。

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e008e224cf336687c04c9fe24740e47e34ce041b50b47e0ed1.zh.png)

1. 选择 **保存**。

#### 为托管身份添加 Storage Blob Data Reader 角色分配

1. 在门户页面顶部的**搜索栏**中输入 *storage accounts*，然后从出现的选项中选择 **Storage accounts**。

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49bcd9cce3ffd1b6218afb6e5c3700b628da7b7c294be71b911.zh.png)

1. 选择与您创建的 Azure 机器学习工作区关联的存储帐户，例如 *finetunephistorage*。

1. 执行以下操作进入添加角色分配页面：

    - 导航到您创建的 Azure 存储帐户。
    - 从左侧标签选择 **访问控制 (IAM)**。
    - 从导航菜单选择 **+ 添加**。
    - 选择 **添加角色分配**。

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0ae84790d65dc5726a9b57c496d916b8700d41e0b3b468451.zh.png)

1. 在添加角色分配页面，执行以下操作：

    - 在角色页面的**搜索栏**中输入 *Storage Blob Data Reader*，并从选项中选择 **Storage Blob Data Reader**。
    - 选择 **下一步**。
    - 在成员页面，选择 **分配访问权限给** **托管身份**。
    - 选择 **+ 选择成员**。
    - 在选择托管身份页面，选择您的 Azure **订阅**。
    - 选择 **托管身份** 类型。
    - 选择您创建的托管身份，例如 *finetunephi-managedidentity*。
    - 选择 **选择**。

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df788963e1dc0a68c39ee297363aabe979b487c60b3037662f.zh.png)

1. 选择 **查看 + 分配**。

#### 为托管身份添加 AcrPull 角色分配

1. 在门户页面顶部的**搜索栏**中输入 *container registries*，然后从出现的选项中选择 **Container registries**。

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c64c0f778633c652ce08e4ac28f142a17afc10de81bb8c336.zh.png)

1. 选择与 Azure 机器学习工作区关联的容器注册表，例如 *finetunephicontainerregistries*。

1. 执行以下操作进入添加角色分配页面：

    - 从左侧标签选择 **访问控制 (IAM)**。
    - 从导航菜单选择 **+ 添加**。
    - 选择 **添加角色分配**。

1. 在添加角色分配页面，执行以下操作：

    - 在角色页面的**搜索栏**中输入 *AcrPull*，并从选项中选择 **AcrPull**。
    - 选择 **下一步**。
    - 在成员页面，选择 **分配访问权限给** **托管身份**。
    - 选择 **+ 选择成员**。
    - 在选择托管身份页面，选择您的 Azure **订阅**。
    - 选择 **托管身份** 类型。
    - 选择您创建的托管身份，例如 *finetunephi-managedidentity*。
    - 选择 **选择**。
    - 选择 **查看 + 分配**。

### 设置项目

现在，您将创建一个文件夹用于工作，并设置一个虚拟环境来开发一个程序，该程序与用户交互并使用来自 Azure Cosmos DB 的存储聊天记录来辅助回答。

#### 创建工作文件夹

1. 打开终端窗口，输入以下命令在默认路径下创建一个名为 *finetune-phi* 的文件夹。

    ```console
    mkdir finetune-phi
    ```

1. 在终端中输入以下命令，进入您刚创建的 *finetune-phi* 文件夹。

    ```console
    cd finetune-phi
    ```

#### 创建虚拟环境

1. 在终端中输入以下命令，创建一个名为 *.venv* 的虚拟环境。

    ```console
    python -m venv .venv
    ```

1. 在终端中输入以下命令，激活虚拟环境。

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> 如果成功，你应该会在命令提示符前看到 *(.venv)*。
#### 安装所需的软件包

1. 在终端中输入以下命令以安装所需的软件包。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 创建项目文件

在本练习中，您将创建项目的核心文件。这些文件包括用于下载数据集、设置 Azure 机器学习环境、微调 Phi-3 模型以及部署微调模型的脚本。您还将创建一个 *conda.yml* 文件来配置微调环境。

在本练习中，您将：

- 创建一个 *download_dataset.py* 文件用于下载数据集。
- 创建一个 *setup_ml.py* 文件用于设置 Azure 机器学习环境。
- 在 *finetuning_dir* 文件夹中创建一个 *fine_tune.py* 文件，使用数据集微调 Phi-3 模型。
- 创建一个 *conda.yml* 文件来配置微调环境。
- 创建一个 *deploy_model.py* 文件用于部署微调后的模型。
- 创建一个 *integrate_with_promptflow.py* 文件，将微调模型集成并通过 Prompt flow 执行模型。
- 创建一个 flow.dag.yml 文件，设置 Prompt flow 的工作流结构。
- 创建一个 *config.py* 文件，填写 Azure 相关信息。

> [!NOTE]
>
> 完整的文件夹结构：
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

1. 打开 **Visual Studio Code**。

1. 从菜单栏选择 **文件**。

1. 选择 **打开文件夹**。

1. 选择您创建的 *finetune-phi* 文件夹，路径为 *C:\Users\yourUserName\finetune-phi*。

    ![打开项目文件夹。](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639c12e7da258ac8b3deca260786edb07598e206725cd1593ce.zh.png)

1. 在 Visual Studio Code 左侧面板中右键点击，选择 **新建文件**，创建名为 *download_dataset.py* 的文件。

1. 在左侧面板中右键点击，选择 **新建文件**，创建名为 *setup_ml.py* 的文件。

1. 在左侧面板中右键点击，选择 **新建文件**，创建名为 *deploy_model.py* 的文件。

    ![创建新文件。](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a398766a39eac9f15240a9a4da566bd8dca86f471e78eadc69e.zh.png)

1. 在左侧面板中右键点击，选择 **新建文件夹**，创建名为 *finetuning_dir* 的文件夹。

1. 在 *finetuning_dir* 文件夹中，创建一个名为 *fine_tune.py* 的新文件。

#### 创建并配置 *conda.yml* 文件

1. 在左侧面板中右键点击，选择 **新建文件**，创建名为 *conda.yml* 的文件。

1. 将以下代码添加到 *conda.yml* 文件中，用于配置 Phi-3 模型的微调环境。

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

#### 创建并配置 *config.py* 文件

1. 在左侧面板中右键点击，选择 **新建文件**，创建名为 *config.py* 的文件。

1. 将以下代码添加到 *config.py* 文件中，填写您的 Azure 信息。

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

#### 添加 Azure 环境变量

1. 按照以下步骤添加 Azure 订阅 ID：

    - 在门户页面顶部的 **搜索栏** 输入 *subscriptions*，并从出现的选项中选择 **Subscriptions**。
    - 选择您当前使用的 Azure 订阅。
    - 将订阅 ID 复制并粘贴到 *config.py* 文件中。

    ![查找订阅 ID。](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637e01163bfdd2a606e7d06f05455ab56e05cb5107e938e7a90.zh.png)

1. 按照以下步骤添加 Azure 工作区名称：

    - 进入您创建的 Azure 机器学习资源。
    - 将您的账户名称复制并粘贴到 *config.py* 文件中。

    ![查找 Azure 机器学习名称。](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a702b1bb5e9d8e9f5e5424abe066a0ff310da980582e65721f.zh.png)

1. 按照以下步骤添加 Azure 资源组名称：

    - 进入您创建的 Azure 机器学习资源。
    - 将您的 Azure 资源组名称复制并粘贴到 *config.py* 文件中。

    ![查找资源组名称。](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a399243d7c94d5aabd86070ab6535d3cf2ec38c78538626666.zh.png)

2. 按照以下步骤添加 Azure 托管身份名称：

    - 进入您创建的托管身份资源。
    - 将您的 Azure 托管身份名称复制并粘贴到 *config.py* 文件中。

    ![查找 UAI。](../../../../../../translated_images/01-17-find-uai.3529464f534998271ea7c5aebafa887051567417f3b4244ff58fdd443192b6d7.zh.png)

### 准备微调数据集

在本练习中，您将运行 *download_dataset.py* 文件，将 *ULTRACHAT_200k* 数据集下载到本地环境。然后，您将使用该数据集在 Azure 机器学习中微调 Phi-3 模型。

#### 使用 *download_dataset.py* 下载数据集

1. 在 Visual Studio Code 中打开 *download_dataset.py* 文件。

1. 将以下代码添加到 *download_dataset.py* 中。

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
> **使用 CPU 进行最小数据集微调的指导**
>
> 如果您想使用 CPU 进行微调，这种方法适合拥有福利订阅（如 Visual Studio Enterprise 订阅）或想快速测试微调和部署流程的用户。
>
> 将 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` 替换为 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. 在终端中输入以下命令运行脚本，将数据集下载到本地环境。

    ```console
    python download_data.py
    ```

1. 确认数据集已成功保存到本地的 *finetune-phi/data* 目录。

> [!NOTE]
>
> **数据集大小与微调时间**
>
> 在此端到端示例中，您仅使用了数据集的 1%（`train_sft[:1%]`）。这大大减少了数据量，加快了上传和微调的速度。您可以调整百分比，以在训练时间和模型性能之间找到合适的平衡。使用较小的数据子集可以缩短微调所需时间，使端到端示例更易于管理。

## 场景 2：微调 Phi-3 模型并在 Azure 机器学习工作室中部署

### 设置 Azure CLI

您需要设置 Azure CLI 来验证您的环境。Azure CLI 允许您直接从命令行管理 Azure 资源，并为 Azure 机器学习提供访问这些资源所需的凭据。开始前请安装 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. 打开终端窗口，输入以下命令登录您的 Azure 账户。

    ```console
    az login
    ```

1. 选择您要使用的 Azure 账户。

1. 选择您要使用的 Azure 订阅。

    ![查找资源组名称。](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a8792c687d36e4fc4f4ee37fd76640e6e4e5aed3329513f2328.zh.png)

> [!TIP]
>
> 如果登录 Azure 时遇到问题，可以尝试使用设备代码登录。打开终端窗口，输入以下命令登录您的 Azure 账户：
>
> ```console
> az login --use-device-code
> ```
>

### 微调 Phi-3 模型

在本练习中，您将使用提供的数据集微调 Phi-3 模型。首先，您将在 *fine_tune.py* 文件中定义微调流程。然后，您将配置 Azure 机器学习环境，并通过运行 *setup_ml.py* 文件启动微调过程。该脚本确保微调在 Azure 机器学习环境中进行。

通过运行 *setup_ml.py*，您将在 Azure 机器学习环境中执行微调过程。

#### 向 *fine_tune.py* 文件添加代码

1. 进入 *finetuning_dir* 文件夹，在 Visual Studio Code 中打开 *fine_tune.py* 文件。

1. 将以下代码添加到 *fine_tune.py* 中。

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

1. 保存并关闭 *fine_tune.py* 文件。

> [!TIP]
> **您可以微调 Phi-3.5 模型**
>
> 在 *fine_tune.py* 文件中，您可以将 `pretrained_model_name` 从 `"microsoft/Phi-3-mini-4k-instruct"` 更改为任何您想微调的模型。例如，将其改为 `"microsoft/Phi-3.5-mini-instruct"`，即可使用 Phi-3.5-mini-instruct 模型进行微调。要查找并使用您喜欢的模型名称，请访问 [Hugging Face](https://huggingface.co/)，搜索感兴趣的模型，然后将其名称复制粘贴到脚本中的 `pretrained_model_name` 字段。
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="微调 Phi-3.5。":::
>

#### 向 *setup_ml.py* 文件添加代码

1. 在 Visual Studio Code 中打开 *setup_ml.py* 文件。

1. 将以下代码添加到 *setup_ml.py* 中。

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

1. 用您的具体信息替换 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `LOCATION`。

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **使用 CPU 进行最小数据集微调的指导**
>
> 如果您想使用 CPU 进行微调，这种方法适合拥有福利订阅（如 Visual Studio Enterprise 订阅）或想快速测试微调和部署流程的用户。
>
> 1. 打开 *setup_ml* 文件。
> 2. 将 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `DOCKER_IMAGE_NAME` 替换为以下内容。如果您无法使用 *Standard_E16s_v3*，可以使用等效的 CPU 实例或申请新的配额。
> 3. 将 `LOCATION` 替换为您的具体信息。
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. 输入以下命令运行 *setup_ml.py* 脚本，启动 Azure 机器学习中的微调过程。

    ```python
    python setup_ml.py
    ```

1. 在本练习中，您已成功使用 Azure 机器学习微调了 Phi-3 模型。通过运行 *setup_ml.py* 脚本，您设置了 Azure 机器学习环境并启动了 *fine_tune.py* 文件中定义的微调过程。请注意，微调过程可能需要较长时间。运行 `python setup_ml.py` 命令后，您需要等待过程完成。您可以通过终端中提供的链接，进入 Azure 机器学习门户监控微调作业状态。

    ![查看微调作业。](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871ee8ba32fa508cc4018c0f04e51ad14b95c421ad77151f768f.zh.png)

### 部署微调模型

为了将微调后的 Phi-3 模型与 Prompt Flow 集成，您需要部署模型，使其可用于实时推理。此过程包括注册模型、创建在线端点以及部署模型。

#### 设置模型名称、端点名称和部署名称

1. 打开 *config.py* 文件。

1. 将 `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` 替换为您想要的模型名称。

1. 将 `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` 替换为您想要的端点名称。

1. 将 `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` 替换为您想要的部署名称。

#### 向 *deploy_model.py* 文件添加代码

运行 *deploy_model.py* 文件将自动完成整个部署流程。它会根据 *config.py* 文件中指定的模型名称、端点名称和部署名称，注册模型、创建端点并执行部署。

1. 在 Visual Studio Code 中打开 *deploy_model.py* 文件。

1. 将以下代码添加到 *deploy_model.py* 中。

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

1. 按照以下步骤获取 `JOB_NAME`：

    - 进入您创建的 Azure 机器学习资源。
    - 选择 **Studio web URL** 打开 Azure 机器学习工作区。
    - 从左侧标签中选择 **Jobs**。
    - 选择微调实验，例如 *finetunephi*。
    - 选择您创建的作业。
- 将您的作业名称复制并粘贴到 *deploy_model.py* 文件中的 `JOB_NAME = "your-job-name"`。

1. 将 `COMPUTE_INSTANCE_TYPE` 替换为您的具体信息。

1. 输入以下命令运行 *deploy_model.py* 脚本，开始在 Azure 机器学习中部署。

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> 为避免产生额外费用，请确保删除在 Azure 机器学习工作区中创建的端点。
>

#### 在 Azure 机器学习工作区检查部署状态

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 进入您创建的 Azure 机器学习工作区。

1. 选择 **Studio web URL** 打开 Azure 机器学习工作区。

1. 从左侧标签中选择 **Endpoints**。

    ![选择端点。](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff109f3b7a6b6e4e9689f99b2d7bf021b057f6c0ecbd1ba90c0.zh.png)

2. 选择您创建的端点。

    ![选择您创建的端点。](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4b726505fcfb7d262b0510de029dcbaf36422bb75b77f25dd.zh.png)

3. 在此页面，您可以管理部署过程中创建的端点。

## 场景 3：与 Prompt flow 集成并与您的自定义模型聊天

### 将自定义 Phi-3 模型与 Prompt flow 集成

成功部署微调模型后，您现在可以将其与 Prompt flow 集成，在实时应用中使用您的模型，实现多种交互式任务，充分发挥自定义 Phi-3 模型的能力。

#### 设置微调 Phi-3 模型的 api key 和 endpoint uri

1. 进入您创建的 Azure 机器学习工作区。
1. 从左侧标签中选择 **Endpoints**。
1. 选择您创建的端点。
1. 从导航菜单中选择 **Consume**。
1. 将您的 **REST endpoint** 复制并粘贴到 *config.py* 文件中，替换 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` 为您的 **REST endpoint**。
1. 将您的 **Primary key** 复制并粘贴到 *config.py* 文件中，替换 `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` 为您的 **Primary key**。

    ![复制 api key 和 endpoint uri。](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53bf44401e184f65a0a088daa76a65f5df5eb4489ae40b890f6.zh.png)

#### 向 *flow.dag.yml* 文件添加代码

1. 在 Visual Studio Code 中打开 *flow.dag.yml* 文件。

1. 将以下代码添加到 *flow.dag.yml* 中。

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

#### 向 *integrate_with_promptflow.py* 文件添加代码

1. 在 Visual Studio Code 中打开 *integrate_with_promptflow.py* 文件。

1. 将以下代码添加到 *integrate_with_promptflow.py* 中。

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

### 与您的自定义模型聊天

1. 输入以下命令运行 *deploy_model.py* 脚本，开始在 Azure 机器学习中部署。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 以下是结果示例：现在您可以与自定义 Phi-3 模型聊天。建议基于用于微调的数据提问。

    ![Prompt flow 示例。](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6412447c9786c562be969a8c3b19791eadffce725fa84f014.zh.png)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。