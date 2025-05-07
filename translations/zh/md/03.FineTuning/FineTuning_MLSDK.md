<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-07T13:23:32+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "zh"
}
-->
## 如何使用来自 Azure ML 系统注册表的 chat-completion 组件微调模型

在本示例中，我们将对 Phi-3-mini-4k-instruct 模型进行微调，使用 ultrachat_200k 数据集完成两人对话的任务。

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.zh.png)

本示例将展示如何使用 Azure ML SDK 和 Python 进行微调，然后将微调后的模型部署到在线端点，实现实时推理。

### 训练数据

我们将使用 ultrachat_200k 数据集。该数据集是 UltraChat 数据集的精简版本，用于训练 Zephyr-7B-β，这是一个先进的 7b 聊天模型。

### 模型

我们将使用 Phi-3-mini-4k-instruct 模型，演示如何微调模型以完成聊天任务。如果你是从某个特定模型卡打开此笔记本，记得替换为相应的模型名称。

### 任务

- 选择要微调的模型。
- 选择并探索训练数据。
- 配置微调作业。
- 运行微调作业。
- 查看训练和评估指标。
- 注册微调后的模型。
- 部署微调模型，实现实时推理。
- 清理资源。

## 1. 设置前置条件

- 安装依赖
- 连接到 AzureML 工作区。详情见设置 SDK 认证。请替换下面的 <WORKSPACE_NAME>、<RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>。
- 连接到 azureml 系统注册表
- 设置可选的实验名称
- 检查或创建计算资源。

> [!NOTE]
> 要求单个 GPU 节点可以包含多张 GPU 卡。例如，Standard_NC24rs_v3 节点包含 4 张 NVIDIA V100 GPU，而 Standard_NC12s_v3 包含 2 张 NVIDIA V100 GPU。具体信息请参阅文档。每个节点的 GPU 卡数量由下面参数 gpus_per_node 设置，正确设置此值能确保节点中所有 GPU 被充分利用。推荐的 GPU 计算 SKU 可在此处和此处查看。

### Python 库

通过运行下面的单元安装依赖。如果是在新环境中运行，此步骤不可省略。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### 与 Azure ML 交互

1. 该 Python 脚本用于与 Azure 机器学习 (Azure ML) 服务交互。具体步骤如下：

    - 导入 azure.ai.ml、azure.identity 和 azure.ai.ml.entities 包中的必要模块，同时导入 time 模块。

    - 尝试使用 DefaultAzureCredential() 进行认证，该方法简化了认证流程，方便快速开发运行于 Azure 云的应用。如果失败，则退回使用 InteractiveBrowserCredential()，提供交互式登录。

    - 接着尝试使用 from_config 方法创建 MLClient 实例，从默认配置文件（config.json）读取配置。如果失败，则手动提供 subscription_id、resource_group_name 和 workspace_name 创建 MLClient 实例。

    - 创建另一个 MLClient 实例，针对名为 "azureml" 的 Azure ML 注册表。该注册表用于存储模型、微调流水线和环境。

    - 设置实验名称 experiment_name 为 "chat_completion_Phi-3-mini-4k-instruct"。

    - 生成唯一时间戳，通过将当前时间（自纪元以来的秒数，浮点数）转换为整数再转为字符串。该时间戳可用于创建唯一名称和版本。

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. 选择基础模型进行微调

1. Phi-3-mini-4k-instruct 是一个拥有 38 亿参数的轻量级先进开源模型，基于 Phi-2 所用数据集构建。该模型属于 Phi-3 模型家族，Mini 版本有两个变体：4K 和 128K，分别代表支持的上下文长度（以 token 计）。我们需要针对特定用途微调该模型。你可以在 AzureML Studio 的模型目录中浏览这些模型，筛选聊天完成任务。本示例使用 Phi-3-mini-4k-instruct 模型。如果你打开的是其他模型的笔记本，请相应替换模型名称和版本。

    > [!NOTE]
    > 这是模型的 id 属性，会作为微调作业的输入传入。在 AzureML Studio 模型目录的模型详情页中也可见该资产 ID 字段。

2. 该 Python 脚本用于与 Azure 机器学习服务交互，具体操作如下：

    - 将 model_name 设置为 "Phi-3-mini-4k-instruct"。

    - 使用 registry_ml_client 对象的 models 属性的 get 方法，从 Azure ML 注册表中获取指定名称的最新版本模型。get 方法接受两个参数：模型名称和标签，标签指定获取最新版本。

    - 控制台打印即将用于微调的模型名称、版本和 id。字符串的 format 方法用于插入模型的属性值。

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. 创建用于作业的计算资源

微调作业仅支持 GPU 计算资源。计算资源大小取决于模型规模，很多情况下选择合适的计算资源较为复杂。本单元指导用户选择合适的计算资源。

> [!NOTE]
> 以下列出的计算资源均采用最优配置。任何配置更改可能导致 Cuda 内存不足错误。遇到此类问题，请尝试升级到更大规格的计算资源。

> [!NOTE]
> 选择 compute_cluster_size 时，请确保计算资源在你的资源组中可用。如果某个计算资源不可用，可申请访问权限。

### 检查模型是否支持微调

1. 该 Python 脚本用于与 Azure 机器学习模型交互，具体操作如下：

    - 导入 ast 模块，提供处理 Python 抽象语法树的功能。

    - 检查 foundation_model 对象（表示 Azure ML 中的模型）是否包含名为 finetune_compute_allow_list 的标签。Azure ML 中标签是键值对，用于筛选和排序模型。

    - 如果存在该标签，使用 ast.literal_eval 函数安全地将标签值（字符串）解析为 Python 列表，赋值给 computes_allow_list 变量，并打印提示创建计算资源时应从该列表中选择。

    - 如果标签不存在，则将 computes_allow_list 设为 None，并打印提示该标签不在模型标签中。

    - 总结：该脚本检查模型元数据中的特定标签，若存在则将其值转换为列表，并向用户反馈。

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### 检查计算实例

1. 该 Python 脚本用于与 Azure 机器学习服务交互，对计算实例进行多项检查，具体如下：

    - 尝试从 Azure ML 工作区获取名为 compute_cluster 的计算实例。如果该实例的配置状态为 "failed"，则抛出 ValueError。

    - 检查 computes_allow_list 是否不为 None。若不为空，则将列表中的所有计算规格名转为小写，并判断当前计算实例规格是否包含在列表中。若不包含，抛出 ValueError。

    - 若 computes_allow_list 为 None，则检查计算实例规格是否属于不支持的 GPU VM 规格列表。若属于，抛出 ValueError。

    - 获取工作区中所有可用计算规格列表。遍历该列表，找到名称与当前计算实例规格匹配的条目，获取该规格的 GPU 数量，设置 gpu_count_found 为 True。

    - 若 gpu_count_found 为 True，打印计算实例中的 GPU 数量。否则抛出 ValueError。

    - 总结：该脚本对 Azure ML 工作区中的计算实例进行多项检查，包括配置状态、规格合法性及 GPU 数量。

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. 选择用于微调模型的数据集

1. 我们使用 ultrachat_200k 数据集。该数据集分为四个部分，适用于监督微调（sft）和生成排序（gen）。每个部分的样本数量如下：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 接下来的几个单元展示微调的数据预处理：

### 可视化部分数据行

为了让示例快速运行，我们保存了 train_sft 和 test_sft 文件，分别包含已筛选数据的 5%。这意味着微调模型的准确度较低，不适合实际使用。download-dataset.py 脚本用于下载 ultrachat_200k 数据集，并将数据转换为微调流水线组件可用格式。由于数据集较大，此处仅使用部分数据。

1. 运行下面脚本仅下载 5% 的数据。可通过修改 dataset_split_pc 参数调整下载比例。

    > [!NOTE]
    > 部分语言模型使用不同的语言代码，因此数据集中的列名应相应匹配。

1. 以下是数据示例格式

聊天完成数据集以 parquet 格式存储，每条记录遵循以下结构：

    - 这是一个 JSON（JavaScript 对象表示法）文档，是一种流行的数据交换格式。它不是可执行代码，而是存储和传输数据的方式。结构说明：

    - "prompt"：字符串，表示给 AI 助手的任务或问题。

    - "messages"：数组，每个元素是一个对象，表示用户与 AI 助手间的对话消息。每条消息包含两个键：

    - "content"：字符串，消息内容。

    - "role"：字符串，消息发送者身份，可能为 "user" 或 "assistant"。

    - "prompt_id"：字符串，表示该提示的唯一标识符。

1. 该 JSON 示例中，用户请求 AI 助手为反乌托邦故事创建主角，助手做出回应，用户随后请求更多细节，助手同意提供。整个对话关联到特定的 prompt_id。

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### 下载数据

1. 该 Python 脚本用于调用辅助脚本 download-dataset.py 下载数据集，具体操作如下：

    - 导入 os 模块，提供跨平台操作系统功能。

    - 使用 os.system 函数在 shell 中运行 download-dataset.py，传入参数指定下载的数据集（HuggingFaceH4/ultrachat_200k）、下载目录（ultrachat_200k_dataset）和数据集拆分比例（5%）。os.system 返回命令的退出状态，存储在 exit_status 变量。

    - 判断 exit_status 是否不为 0。Unix-like 系统中，0 表示命令成功，非 0 表示错误。若不为 0，则抛出异常，提示下载数据集出错。

    - 总结：该脚本通过辅助脚本下载数据集，若失败则抛出异常。

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### 将数据加载到 DataFrame

1. 该 Python 脚本用于将 JSON Lines 文件加载到 pandas DataFrame 并显示前 5 行，具体操作如下：

    - 导入 pandas 库，强大的数据处理和分析库。

    - 设置 pandas 显示选项中列宽最大值为 0，表示打印时不截断列内容，完整显示。

    - 使用 pd.read_json 函数加载 ultrachat_200k_dataset 目录下的 train_sft.jsonl 文件，lines=True 表示文件为 JSON Lines 格式，每行是独立 JSON 对象。

    - 使用 head 方法显示 DataFrame 的前 5 行（若不足 5 行则显示全部）。

    - 总结：该脚本将 JSON Lines 文件加载为 DataFrame，并完整显示前 5 条数据。

    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. 使用模型和数据提交微调作业

创建使用 chat-completion 流水线组件的作业。了解更多关于微调支持的所有参数。

### 定义微调参数

1. 微调参数可分为两类——训练参数和优化参数。

1. 训练参数定义训练相关内容，如：

    - 使用的优化器、调度器
    - 微调优化的指标
    - 训练步数、批次大小等
    - 优化参数有助于优化 GPU 内存和有效利用计算资源。

1. 以下是部分属于优化参数的示例。优化参数因模型而异，随模型打包处理这些差异。

    - 启用 deepspeed 和 LoRA
    - 启用混合精度训练
    - 启用多节点训练

> [!NOTE]
> 监督微调可能导致模型失去对齐或发生灾难性遗忘。建议检测此问题并在微调后运行对齐阶段。

### 微调参数

1. 该 Python 脚本用于设置机器学习模型微调参数，具体如下：

    - 设置默认训练参数，如训练轮数、训练和评估批次大小、学习率及学习率调度器类型。

    - 设置默认优化参数，如是否启用 LoRa、DeepSpeed 及 DeepSpeed 阶段。

    - 将训练和优化参数合并为 finetune_parameters 字典。

    - 检查 foundation_model 是否有模型特定的默认参数。如果有，打印警告并使用 ast.literal_eval 将其从字符串转换为字典，更新 finetune_parameters。

    - 打印最终用于运行的微调参数。

    - 总结：该脚本设置并显示机器学习模型的微调参数，支持用模型特定参数覆盖默认值。

    ```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### 训练流水线

1. 该 Python 脚本定义了一个函数，用于生成机器学习训练流水线的显示名称，并调用该函数生成并打印名称，具体如下：

    1. 定义 get_pipeline_display_name 函数。该函数根据训练流水线的多个参数生成显示名称。

    2. 函数内部计算总批次大小，方法是将每设备批次大小、梯度累积步数、每节点 GPU 数量和微调节点数相乘。

    3. 获取其他参数，如学习率调度器类型、是否启用 DeepSpeed、DeepSpeed 阶段、是否启用 LoRa、保留模型检查点数量限制以及最大序列长度。

    4. 构造包含上述参数的字符串，参数之间用连字符连接。如果启用了 DeepSpeed 或 LoRa，字符串中分别包含 "ds" 加阶段号，或 "lora"；否则包含 "nods" 或 "nolora"。

    5. 函数返回该字符串，作为训练流水线的显示名称。

    6. 定义函数后调用它生成显示名称，并打印输出。

    7. 总结：该脚本用于生成机器学习训练流水线的显示名称。
基于各种参数的训练管道，然后打印此显示名称。```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### 配置管道

此 Python 脚本使用 Azure Machine Learning SDK 定义并配置一个机器学习管道。具体功能如下：

1. 从 Azure AI ML SDK 导入必要的模块。
2. 从注册表中获取名为 "chat_completion_pipeline" 的管道组件。
3. 使用 `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False` 定义一个管道作业，这意味着如果任何步骤失败，管道将停止运行。
4. 总结来说，此脚本定义并配置了一个用于聊天补全任务的机器学习管道，使用的是 Azure Machine Learning SDK。

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### 提交作业

1. 此 Python 脚本将机器学习管道作业提交到 Azure Machine Learning 工作区，并等待作业完成。具体功能如下：

- 调用 workspace_ml_client 中 jobs 对象的 create_or_update 方法提交管道作业。要运行的管道由 pipeline_object 指定，作业所属的实验由 experiment_name 指定。
- 调用 workspace_ml_client 中 jobs 对象的 stream 方法，等待管道作业完成。等待的作业由 pipeline_job 对象的 name 属性指定。
- 总结来说，此脚本将机器学习管道作业提交到 Azure Machine Learning 工作区，并等待作业完成。

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. 在工作区注册微调模型

我们将从微调作业的输出中注册模型。这将追踪微调模型与微调作业之间的血缘关系。微调作业进一步追踪基础模型、数据和训练代码的血缘。

### 注册机器学习模型

1. 此 Python 脚本注册了在 Azure Machine Learning 管道中训练的机器学习模型。具体功能如下：

- 从 Azure AI ML SDK 导入必要的模块。
- 通过调用 workspace_ml_client 中 jobs 对象的 get 方法并访问其 outputs 属性，检查管道作业是否有 trained_model 输出。
- 通过格式化字符串，使用管道作业名称和输出名称（"trained_model"）构建训练模型的路径。
- 定义微调模型的名称，通过在原模型名称后追加 "-ultrachat-200k" 并将斜杠替换为连字符。
- 准备注册模型，创建一个 Model 对象，包含模型路径、模型类型（MLflow 模型）、模型名称和版本，以及模型描述等参数。
- 通过调用 workspace_ml_client 中 models 对象的 create_or_update 方法并传入 Model 对象来注册模型。
- 打印已注册的模型。
- 总结来说，此脚本注册了在 Azure Machine Learning 管道中训练的机器学习模型。

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. 将微调模型部署到在线端点

在线端点提供持久的 REST API，可用于与需要使用模型的应用程序集成。

### 管理端点

1. 此 Python 脚本在 Azure Machine Learning 中为注册模型创建托管在线端点。具体功能如下：

- 从 Azure AI ML SDK 导入必要的模块。
- 通过在字符串 "ultrachat-completion-" 后追加时间戳，定义唯一的在线端点名称。
- 准备创建在线端点，创建 ManagedOnlineEndpoint 对象，包含端点名称、描述和身份验证模式（"key"）等参数。
- 调用 workspace_ml_client 的 begin_create_or_update 方法创建在线端点，并通过调用 wait 方法等待创建完成。
- 总结来说，此脚本为注册模型在 Azure Machine Learning 中创建了一个托管在线端点。

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> 你可以在这里找到支持部署的 SKU 列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署机器学习模型

1. 此 Python 脚本将注册的机器学习模型部署到 Azure Machine Learning 中的托管在线端点。具体功能如下：

- 导入 ast 模块，该模块提供处理 Python 抽象语法树的函数。
- 将部署实例类型设置为 "Standard_NC6s_v3"。
- 检查 foundation model 中是否存在 inference_compute_allow_list 标签。如果存在，将其字符串值转换为 Python 列表并赋值给 inference_computes_allow_list；如果不存在，则将 inference_computes_allow_list 设为 None。
- 检查指定的实例类型是否在允许列表中。如果不在，打印提示信息，要求用户从允许列表中选择实例类型。
- 准备创建部署，创建 ManagedOnlineDeployment 对象，包含部署名称、端点名称、模型 ID、实例类型和数量、存活探针设置以及请求设置等参数。
- 调用 workspace_ml_client 的 begin_create_or_update 方法创建部署，并通过调用 wait 方法等待创建完成。
- 将端点流量设置为将 100% 流量导向名为 "demo" 的部署。
- 调用 workspace_ml_client 的 begin_create_or_update 方法更新端点，并通过调用 result 方法等待更新完成。
- 总结来说，此脚本将注册的机器学习模型部署到 Azure Machine Learning 的托管在线端点。

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. 使用示例数据测试端点

我们将从测试数据集中获取一些示例数据，提交到在线端点进行推断，然后显示预测标签和真实标签。

### 读取结果

1. 此 Python 脚本将 JSON Lines 文件读取到 pandas DataFrame 中，随机抽取样本，并重置索引。具体功能如下：

- 读取文件 ./ultrachat_200k_dataset/test_gen.jsonl 到 pandas DataFrame。使用 read_json 函数并设置 lines=True，因为文件是 JSON Lines 格式，每行是一个独立的 JSON 对象。
- 从 DataFrame 中随机抽取 1 行。使用 sample 函数并设置 n=1 指定抽取的行数。
- 重置 DataFrame 的索引。使用 reset_index 函数并设置 drop=True 删除原索引，替换为默认整数索引。
- 使用 head 函数显示 DataFrame 的前 2 行。但由于采样后 DataFrame 仅含 1 行，因此只显示该行。
- 总结来说，此脚本将 JSON Lines 文件读取到 pandas DataFrame 中，随机抽取 1 行样本，重置索引，并显示第一行。

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### 创建 JSON 对象

1. 此 Python 脚本创建一个带有特定参数的 JSON 对象并保存到文件。具体功能如下：

- 导入 json 模块，提供处理 JSON 数据的函数。
- 创建一个字典 parameters，包含机器学习模型的参数。键为 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，对应的值分别为 0.6、0.9、True 和 200。
- 创建另一个字典 test_json，包含两个键："input_data" 和 "params"。"input_data" 的值是一个字典，包含 "input_string" 和 "parameters" 两个键。"input_string" 是一个列表，包含 test_df DataFrame 的第一条消息。"parameters" 是前面创建的 parameters 字典。"params" 是一个空字典。
- 打开名为 sample_score.json 的文件。

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### 调用端点

1. 此 Python 脚本调用 Azure Machine Learning 中的在线端点对 JSON 文件进行评分。具体功能如下：

- 调用 workspace_ml_client 对象 online_endpoints 属性的 invoke 方法。该方法用于向在线端点发送请求并获取响应。
- 使用 endpoint_name 和 deployment_name 参数指定端点名称和部署名称。此处端点名称存储在 online_endpoint_name 变量中，部署名称为 "demo"。
- 使用 request_file 参数指定要评分的 JSON 文件路径，此处为 ./ultrachat_200k_dataset/sample_score.json。
- 将端点响应存储在 response 变量中。
- 打印原始响应。
- 总结来说，此脚本调用 Azure Machine Learning 的在线端点对 JSON 文件进行评分，并打印响应。

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. 删除在线端点

1. 不要忘记删除在线端点，否则端点所使用的计算资源将继续计费。此行 Python 代码删除 Azure Machine Learning 中的在线端点。具体功能如下：

- 调用 workspace_ml_client 对象 online_endpoints 属性的 begin_delete 方法，启动在线端点的删除操作。
- 使用 name 参数指定要删除的端点名称，此处端点名称存储在 online_endpoint_name 变量中。
- 调用 wait 方法等待删除操作完成。此为阻塞操作，脚本会暂停直到删除完成。
- 总结来说，此行代码启动了 Azure Machine Learning 中在线端点的删除，并等待操作完成。

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言版本的文件应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。