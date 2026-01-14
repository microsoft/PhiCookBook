<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T17:14:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "zh"
}
-->
# 使用 Prompt flow 微调和集成自定义 Phi-3 模型

此端到端（E2E）示例基于 Microsoft 技术社区的指南《[使用 Prompt flow 微调和集成自定义 Phi-3 模型：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)》。介绍了微调、自定义 Phi-3 模型部署及与 Prompt flow 集成的流程。

## 概述

在本 E2E 示例中，您将学习如何微调 Phi-3 模型并将其集成到 Prompt flow 中。通过利用 Azure 机器学习和 Prompt flow，您将建立一个用于部署和使用自定义 AI 模型的工作流。该 E2E 示例分为三个场景：

**场景 1：设置 Azure 资源并准备微调**

**场景 2：微调 Phi-3 模型并在 Azure 机器学习工作室中部署**

**场景 3：与 Prompt flow 集成并与自定义模型聊天**

以下是本 E2E 示例的概览。

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/zh/00-01-architecture.02fc569e266d468c.png)

### 目录

1. **[场景 1：设置 Azure 资源并准备微调](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [创建 Azure 机器学习工作区](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [在 Azure 订阅中请求 GPU 配额](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [添加角色分配](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [设置项目](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [准备微调数据集](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[场景 2：微调 Phi-3 模型并在 Azure 机器学习工作室中部署](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [设置 Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [微调 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署微调模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[场景 3：与 Prompt flow 集成并与自定义模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [将自定义 Phi-3 模型集成到 Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [与自定义模型聊天](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 场景 1：设置 Azure 资源并准备微调

### 创建 Azure 机器学习工作区

1. 在门户页面顶部的 **搜索栏** 中输入 *azure machine learning*，然后从出现的选项中选择 **Azure Machine Learning**。

    ![Type azure machine learning](../../../../../../translated_images/zh/01-01-type-azml.a5116f8454d98c60.png)

1. 从导航菜单中选择 **+ 创建**。

1. 从导航菜单中选择 **新建工作区**。

    ![Select new workspace](../../../../../../translated_images/zh/01-02-select-new-workspace.83e17436f8898dc4.png)

1. 执行以下操作：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要，则创建新的）。
    - 输入 **工作区名称**。必须是唯一值。
    - 选择您想使用的 **区域**。
    - 选择要使用的 **存储帐户**（如有需要，则创建新的）。
    - 选择要使用的 **密钥保管库**（如有需要，则创建新的）。
    - 选择要使用的 **应用程序洞察**（如有需要，则创建新的）。
    - 选择要使用的 **容器注册表**（如有需要，则创建新的）。

    ![Fill AZML.](../../../../../../translated_images/zh/01-03-fill-AZML.730a5177757bbebb.png)

1. 选择 **审核 + 创建**。

1. 选择 **创建**。

### 在 Azure 订阅中请求 GPU 配额

在此 E2E 示例中，您将使用 *Standard_NC24ads_A100_v4 GPU* 进行微调，它需要配额申请；使用 *Standard_E4s_v3* CPU 进行部署，则不需要配额申请。

> [!NOTE]
>
> 只有按使用量付费订阅（标准订阅类型）有资格申请 GPU；福利订阅当前不支持。
>
> 对于使用福利订阅（例如 Visual Studio 企业订阅）或希望快速测试微调和部署流程的用户，本教程还提供了使用 CPU 和最小数据集微调的指导。但需要注意的是，使用 GPU 和较大数据集微调的效果明显更佳。

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 执行以下操作请求 *Standard NCADSA100v4 Family* 配额：

    - 从左侧标签中选择 **配额**。
    - 选择要使用的 **虚拟机系列**，例如选择包含 *Standard_NC24ads_A100_v4* GPU 的 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**。
    - 从导航菜单中选择 **请求配额**。

        ![Request quota.](../../../../../../translated_images/zh/01-04-request-quota.3d3670c3221ab834.png)

    - 在请求配额页面中，输入您想使用的 **新核心限制**，例如 24。
    - 在请求配额页面中，选择 **提交** 提交 GPU 配额申请。

> [!NOTE]
> 您可以参考文档 [Azure 虚拟机尺寸](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) 选择适合您需求的 GPU 或 CPU。

### 添加角色分配

要微调和部署模型，您必须先创建一个用户分配的托管身份（UAI）并赋予其适当权限。此 UAI 将在部署时用于身份验证。

#### 创建用户分配的托管身份（UAI）

1. 在门户页面顶部的 **搜索栏** 输入 *managed identities*，然后从出现的选项中选择 **托管身份**。

    ![Type managed identities.](../../../../../../translated_images/zh/01-05-type-managed-identities.9297b6039874eff8.png)

1. 选择 **+ 创建**。

    ![Select create.](../../../../../../translated_images/zh/01-06-select-create.936d8d66d7144f9a.png)

1. 执行以下操作：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要，则创建新的）。
    - 选择您想使用的 **区域**。
    - 输入 **名称**。必须是唯一值。

1. 选择 **审核 + 创建**。

1. 选择 **+ 创建**。

#### 向托管身份添加贡献者角色分配

1. 导航到您创建的托管身份资源。

1. 从左侧标签中选择 **Azure 角色分配**。

1. 从导航菜单中选择 **+ 添加角色分配**。

1. 在添加角色分配页面中，执行以下操作：
    - 将 **范围** 设置为 **资源组**。
    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**。
    - 将 **角色** 设置为 **贡献者**。

    ![Fill contributor role.](../../../../../../translated_images/zh/01-07-fill-contributor-role.29ca99b7c9f687e0.png)

1. 选择 **保存**。

#### 向托管身份添加存储 Blob 数据读取者角色分配

1. 在门户页面顶部的 **搜索栏** 输入 *storage accounts*，然后从出现的选项中选择 **存储帐户**。

    ![Type storage accounts.](../../../../../../translated_images/zh/01-08-type-storage-accounts.1186c8e42933e49b.png)

1. 选择与您创建的 Azure 机器学习工作区关联的存储帐户，例如 *finetunephistorage*。

1. 执行以下操作导航到添加角色分配页面：

    - 导航到您创建的 Azure 存储帐户。
    - 从左侧标签中选择 **访问控制（IAM）**。
    - 从导航菜单中选择 **+ 添加**。
    - 选择 **添加角色分配**。

    ![Add role.](../../../../../../translated_images/zh/01-09-add-role.d2db22fec1b187f0.png)

1. 在添加角色分配页面中，执行以下操作：

    - 在角色页面的 **搜索栏** 中输入 *Storage Blob Data Reader* 并从选项中选择 **存储 Blob 数据读取者**。
    - 选择 **下一步**。
    - 在成员页面，选择 **将访问权限分配给** 为 **托管身份**。
    - 选择 **+ 选择成员**。
    - 在选择托管身份页面，选择您的 Azure **订阅**。
    - 选择要指派的 **托管身份**。
    - 选择您创建的托管身份，例如 *finetunephi-managedidentity*。
    - 选择 **选择**。

    ![Select managed identity.](../../../../../../translated_images/zh/01-10-select-managed-identity.5ce5ba181f72a4df.png)

1. 选择 **审核 + 分配**。

#### 向托管身份添加 AcrPull 角色分配

1. 在门户页面顶部的 **搜索栏** 输入 *container registries*，然后从出现的选项中选择 **容器注册表**。

    ![Type container registries.](../../../../../../translated_images/zh/01-11-type-container-registries.ff3b8bdc49dc596c.png)

1. 选择与 Azure 机器学习工作区关联的容器注册表，例如 *finetunephicontainerregistries*。

1. 执行以下操作导航到添加角色分配页面：

    - 选择左侧标签中的 **访问控制（IAM）**。
    - 从导航菜单选择 **+ 添加**。
    - 选择 **添加角色分配**。

1. 在添加角色分配页面，执行以下操作：

    - 在角色页面的 **搜索栏** 中输入 *AcrPull* 并选择 **AcrPull**。
    - 选择 **下一步**。
    - 在成员页面选择 **将访问权限分配给** 为 **托管身份**。
    - 选择 **+ 选择成员**。
    - 在选择托管身份页面选择您的 Azure **订阅**。
    - 选择要指派的 **托管身份**。
    - 选择您创建的托管身份，例如 *finetunephi-managedidentity*。
    - 选择 **选择**。
    - 选择 **审核 + 分配**。

### 设置项目

现在，您将创建一个文件夹用于工作，并设置一个虚拟环境，用于开发一个与用户交互并使用 Azure Cosmos DB 中存储的聊天历史来辅助回答的程序。

#### 创建工作文件夹

1. 打开一个终端窗口，输入以下命令，在默认路径下创建一个名为 *finetune-phi* 的文件夹。

    ```console
    mkdir finetune-phi
    ```

1. 在终端中输入以下命令，进入您创建的 *finetune-phi* 文件夹。

    ```console
    cd finetune-phi
    ```

#### 创建虚拟环境

1. 在终端中输入以下命令，创建名为 *.venv* 的虚拟环境。

    ```console
    python -m venv .venv
    ```

1. 在终端中输入以下命令，激活虚拟环境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> 如果成功，您应在命令提示符前看到 *(.venv)*。

#### 安装所需软件包

1. 在终端中输入以下命令安装所需软件包。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 创建项目文件
在本次练习中，您将为我们的项目创建必要的文件。这些文件包括用于下载数据集、设置 Azure 机器学习环境、微调 Phi-3 模型以及部署微调模型的脚本。您还将创建一个 *conda.yml* 文件来设置微调环境。

在本练习中，您将：

- 创建一个 *download_dataset.py* 文件以下载数据集。
- 创建一个 *setup_ml.py* 文件以设置 Azure 机器学习环境。
- 在 *finetuning_dir* 文件夹中创建一个 *fine_tune.py* 文件，使用数据集微调 Phi-3 模型。
- 创建一个 *conda.yml* 文件来设置微调环境。
- 创建一个 *deploy_model.py* 文件以部署微调模型。
- 创建一个 *integrate_with_promptflow.py* 文件，将微调模型集成并通过 Prompt flow 执行模型。
- 创建一个 flow.dag.yml 文件，设置 Prompt flow 的工作流结构。
- 创建一个 *config.py* 文件以填写 Azure 相关信息。

> [!NOTE]
>
> 完整文件夹结构：
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

1. 在菜单栏中选择 **文件**。

1. 选择 **打开文件夹**。

1. 选择您创建的 *finetune-phi* 文件夹，位于 *C:\Users\yourUserName\finetune-phi*。

    ![打开项目文件夹。](../../../../../../translated_images/zh/01-12-open-project-folder.1fff9c7f41dd1639.png)

1. 在 Visual Studio Code 左侧窗格中右键点击并选择 **新建文件**，创建一个名为 *download_dataset.py* 的新文件。

1. 在 Visual Studio Code 左侧窗格中右键点击并选择 **新建文件**，创建一个名为 *setup_ml.py* 的新文件。

1. 在 Visual Studio Code 左侧窗格中右键点击并选择 **新建文件**，创建一个名为 *deploy_model.py* 的新文件。

    ![创建新文件。](../../../../../../translated_images/zh/01-13-create-new-file.c17c150fff384a39.png)

1. 在 Visual Studio Code 左侧窗格中右键点击并选择 **新建文件夹**，创建一个名为 *finetuning_dir* 的新文件夹。

1. 在 *finetuning_dir* 文件夹内，创建一个名为 *fine_tune.py* 的新文件。

#### 创建并配置 *conda.yml* 文件

1. 在 Visual Studio Code 左侧窗格中右键点击并选择 **新建文件**，创建一个名为 *conda.yml* 的新文件。

1. 将以下代码添加到 *conda.yml* 文件中，以设置 Phi-3 模型的微调环境。

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

1. 在 Visual Studio Code 左侧窗格中右键点击并选择 **新建文件**，创建一个名为 *config.py* 的新文件。

1. 将以下代码添加到 *config.py* 文件中以填写您的 Azure 信息。

    ```python
    # Azure 设置
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure 机器学习设置
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure 托管身份设置
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # 数据集文件路径
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # 微调模型设置
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### 添加 Azure 环境变量

1. 执行以下操作以添加 Azure 订阅 ID：

    - 在门户页面顶部的 **搜索栏** 中输入 *subscriptions*，并从出现的选项中选择 **订阅**。
    - 选择您当前使用的 Azure 订阅。
    - 将您的订阅 ID 复制并粘贴到 *config.py* 文件中。

    ![查找订阅 ID。](../../../../../../translated_images/zh/01-14-find-subscriptionid.4f4ca33555f1e637.png)

1. 执行以下操作以添加 Azure 工作区名称：

    - 进入您创建的 Azure 机器学习资源。
    - 将您的账户名称复制并粘贴到 *config.py* 文件中。

    ![查找 Azure 机器学习名称。](../../../../../../translated_images/zh/01-15-find-AZML-name.1975f0422bca19a7.png)

1. 执行以下操作以添加 Azure 资源组名称：

    - 进入您创建的 Azure 机器学习资源。
    - 将您的 Azure 资源组名称复制并粘贴到 *config.py* 文件中。

    ![查找资源组名称。](../../../../../../translated_images/zh/01-16-find-AZML-resourcegroup.855a349d0af134a3.png)

2. 执行以下操作以添加 Azure 托管身份名称：

    - 进入您创建的托管身份资源。
    - 将您的 Azure 托管身份名称复制并粘贴到 *config.py* 文件中。

    ![查找 UAI。](../../../../../../translated_images/zh/01-17-find-uai.3529464f53499827.png)

### 准备微调数据集

在本练习中，您将运行 *download_dataset.py* 文件，将 *ULTRACHAT_200k* 数据集下载到本地环境。然后，您将使用此数据集在 Azure 机器学习中对 Phi-3 模型进行微调。

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
        # 加载具有指定名称、配置和拆分比例的数据集
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # 将数据集拆分为训练集和测试集（80%训练，20%测试）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 如果目录不存在则创建该目录
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以写入模式打开文件
        with open(filepath, 'w', encoding='utf-8') as f:
            # 遍历数据集中的每条记录
            for record in dataset:
                # 将记录作为JSON对象导出并写入文件
                json.dump(record, f)
                # 写入换行符以分隔记录
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 使用特定配置和拆分比例加载并拆分ULTRACHAT_200k数据集
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 从拆分中提取训练集和测试集
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 将训练集保存为JSONL文件
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # 将测试集保存为单独的JSONL文件
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **使用最小数据集通过 CPU 进行微调的指导**
>
> 如果您想使用 CPU 进行微调，此方法适用于拥有权益订阅（如 Visual Studio 企业订阅）或希望快速测试微调和部署流程的情况。
>
> 将 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` 替换为 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. 在终端中输入以下命令，运行脚本并将数据集下载到本地环境。

    ```console
    python download_data.py
    ```

1. 确认数据集已成功保存至本地的 *finetune-phi/data* 目录。

> [!NOTE]
>
> **数据集大小和微调时间**
>
> 在此端到端示例中，您仅使用了数据集的 1%（`train_sft[:1%]`）。这大幅减少了数据量，加快了上传和微调速度。您可以调整百分比以在训练时间和模型性能之间找到合适的平衡。使用较小的数据集子集缩短了微调所需时间，使端到端示例更易管理。

## 场景 2：在 Azure 机器学习工作室中微调 Phi-3 模型并部署

### 设置 Azure CLI

您需要设置 Azure CLI 来认证您的环境。Azure CLI 允许您直接从命令行管理 Azure 资源，并提供 Azure 机器学习访问这些资源所需的凭据。开始之前，请安装 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)。

1. 打开终端窗口并输入以下命令登录您的 Azure 账户。

    ```console
    az login
    ```

1. 选择您要使用的 Azure 账户。

1. 选择您要使用的 Azure 订阅。

    ![查找资源组名称。](../../../../../../translated_images/zh/02-01-login-using-azure-cli.dfde31cb75e58a87.png)

> [!TIP]
>
> 如果登录 Azure 时遇到困难，尝试使用设备代码。打开终端窗口并输入以下命令登录您的 Azure 账户：
>
> ```console
> az login --use-device-code
> ```
>

### 微调 Phi-3 模型

在本练习中，您将使用提供的数据集对 Phi-3 模型进行微调。首先，在 *fine_tune.py* 文件中定义微调过程。然后，配置 Azure 机器学习环境并通过运行 *setup_ml.py* 文件启动微调过程。该脚本确保微调在 Azure 机器学习环境内进行。

通过运行 *setup_ml.py*，您将在 Azure 机器学习环境中运行微调过程。

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

    # 为避免MLflow中的INVALID_PARAMETER_VALUE错误，禁用MLflow集成
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # 日志设置
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
> 在 *fine_tune.py* 文件中，可以将 `pretrained_model_name` 从 `"microsoft/Phi-3-mini-4k-instruct"` 更改为您想微调的任意模型。例如，如果您将其更改为 `"microsoft/Phi-3.5-mini-instruct"`，就会使用 Phi-3.5-mini-instruct 模型进行微调。要查找并使用您喜欢的模型名称，请访问 [Hugging Face](https://huggingface.co/)，搜索您感兴趣的模型，然后复制其名称粘贴到脚本中的 `pretrained_model_name` 字段。
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="微调 Phi-3.5。">
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

    # 常量

    # 取消注释以下行以使用 CPU 实例进行训练
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # 取消注释以下行以使用 GPU 实例进行训练
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # 替换为你的计算集群位置
    FINETUNING_DIR = "./finetuning_dir" # 微调脚本的路径
    TRAINING_ENV_NAME = "phi-3-training-environment" # 训练环境名称
    MODEL_OUTPUT_DIR = "./model_output" # Azure ML 中模型输出目录的路径

    # 日志设置以跟踪过程
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
            image=DOCKER_IMAGE_NAME,  # 环境的 Docker 镜像
            conda_file=CONDA_FILE,  # Conda 环境文件
            name=TRAINING_ENV_NAME,  # 环境名称
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
                tier="Dedicated",  # 计算集群等级
                min_instances=0,  # 实例最小数量
                max_instances=1  # 实例最大数量
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # 等待集群创建完成
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # fine_tune.py 的路径
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # 训练环境
            compute=compute_name,  # 使用的计算集群
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # 训练数据文件的路径
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # 评估数据文件的路径
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # 初始化 ML 客户端
        ml_client = get_ml_client()

        # 创建环境
        env = create_or_get_environment(ml_client)
        
        # 创建或获取已存在的计算集群
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # 创建并提交微调作业
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # 提交作业
        ml_client.jobs.stream(returned_job.name)  # 流式传输作业日志
        
        # 捕获作业名称
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. 将 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `LOCATION` 替换为您的具体信息。

    ```python
   # 取消注释以下行以使用GPU实例进行训练
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # 替换为您的计算集群的位置
    ```

> [!TIP]
>
> **使用最小数据集通过 CPU 进行微调的指导**
>
> 如果您想使用 CPU 进行微调，此方法适用于拥有权益订阅（如 Visual Studio 企业订阅）或希望快速测试微调和部署流程的情况。
>
> 1. 打开 *setup_ml* 文件。
> 1. 将 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `DOCKER_IMAGE_NAME` 替换为如下内容。如果您无法使用 *Standard_E16s_v3*，可以使用等效的 CPU 实例或申请新额度。
> 1. 将 `LOCATION` 替换为您的具体信息。
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. 输入以下命令运行 *setup_ml.py* 脚本，在 Azure 机器学习中启动微调过程。

    ```python
    python setup_ml.py
    ```

1. 在本练习中，您已成功使用 Azure 机器学习微调了 Phi-3 模型。通过运行 *setup_ml.py* 脚本，您设置了 Azure 机器学习环境并启动了在 *fine_tune.py* 文件中定义的微调过程。请注意，微调过程可能需要较长时间。运行 `python setup_ml.py` 命令后，您需要等待过程完成。您可以在终端中提供的链接进入 Azure 机器学习门户，监控微调作业的状态。

    ![查看微调作业。](../../../../../../translated_images/zh/02-02-see-finetuning-job.59393bc3b143871e.png)

### 部署微调后的模型

为了将微调后的 Phi-3 模型与 Prompt Flow 集成，您需要部署该模型，使其可用于实时推理。此过程包括注册模型、创建在线端点并部署模型。

#### 设置模型名称、端点名称和部署名称以便部署

1. 打开 *config.py* 文件。

1. 将 `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` 替换为您希望的模型名称。

1. 将 `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` 替换为您希望的端点名称。

1. 将 `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` 替换为您希望的部署名称。

#### 向 *deploy_model.py* 文件添加代码

运行 *deploy_model.py* 文件会自动完成整个部署过程。它会根据 *config.py* 文件中指定的模型名称、端点名称和部署名称，完成模型注册、端点创建以及部署。

1. 在 Visual Studio Code 中打开 *deploy_model.py* 文件。

1. 将以下代码添加到 *deploy_model.py* 中。

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # 配置导入
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

    # 常量
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # 日志设置
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
            # 获取当前端点详情
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # 记录当前流量分配以进行调试
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # 设置部署的流量分配
            endpoint.traffic = {deployment_name: 100}
            
            # 使用新的流量分配更新端点
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # 记录更新后的流量分配以进行调试
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # 记录过程中发生的任何错误
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

1. 执行以下操作以获取 `JOB_NAME`：

    - 进入您创建的 Azure 机器学习资源。
    - 选择 **Studio web URL** 以打开 Azure 机器学习工作区。
    - 从左侧标签中选择 **作业**。
    - 选择微调实验，例如 *finetunephi*。
    - 选择您创建的作业。
- 将你的作业名称复制并粘贴到 *deploy_model.py* 文件中的 `JOB_NAME = "your-job-name"`。

1. 将 `COMPUTE_INSTANCE_TYPE` 替换为你的具体信息。

1. 输入以下命令运行 *deploy_model.py* 脚本，并启动 Azure 机器学习中的部署过程。

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> 为避免账户产生额外费用，请确保删除在 Azure 机器学习工作区中创建的终结点。
>

#### 在 Azure 机器学习工作区检查部署状态

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 导航至你创建的 Azure 机器学习工作区。

1. 选择 **Studio web URL** 打开 Azure 机器学习工作区。

1. 从左侧选项卡选择 **Endpoints**。

    ![选择终结点。](../../../../../../translated_images/zh/02-03-select-endpoints.c3136326510baff1.png)

2. 选择你创建的终结点。

    ![选择你创建的终结点。](../../../../../../translated_images/zh/02-04-select-endpoint-created.0363e7dca51dabb4.png)

3. 在此页面上，你可以管理部署过程中创建的终结点。

## 场景 3：与 Prompt flow 集成并与自定义模型聊天

### 将自定义 Phi-3 模型与 Prompt flow 集成

成功部署微调模型后，你现在可以将它与 Prompt flow 集成，以在实时应用中使用你的模型，实现多种交互式任务。

#### 设置微调 Phi-3 模型的 api key 和 endpoint uri

1. 进入你创建的 Azure 机器学习工作区。
1. 从左侧选项卡选择 **Endpoints**。
1. 选择你创建的终结点。
1. 从导航菜单选择 **Consume**。
1. 复制并粘贴你的 **REST endpoint** 到 *config.py* 文件中，替换 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` 为你的 **REST endpoint**。
1. 复制并粘贴你的 **Primary key** 到 *config.py* 文件中，替换 `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` 为你的 **Primary key**。

    ![复制 api key 和 endpoint uri。](../../../../../../translated_images/zh/02-05-copy-apikey-endpoint.88b5a92e6462c53b.png)

#### 向 *flow.dag.yml* 文件添加代码

1. 在 Visual Studio Code 中打开 *flow.dag.yml* 文件。

1. 将以下代码添加到 *flow.dag.yml* 文件中。

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

1. 将以下代码添加到 *integrate_with_promptflow.py* 文件中。

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

    # 日志设置
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

### 与你的自定义模型聊天

1. 输入以下命令运行 *deploy_model.py* 脚本，并启动在 Azure 机器学习中的部署过程。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 这是一个结果示例：现在你可以与你的自定义 Phi-3 模型聊天。建议基于用于微调的数据提问。

    ![Prompt flow 示例。](../../../../../../translated_images/zh/02-06-promptflow-example.89384abaf3ad71f6.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译而成。虽然我们努力确保准确性，但请注意自动翻译可能存在错误或不准确之处。原始文件的原文版本应视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->