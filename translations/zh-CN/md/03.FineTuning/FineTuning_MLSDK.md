## 如何使用 Azure ML 系统注册表中的聊天完成组件微调模型

在此示例中，我们将对 Phi-3-mini-4k-instruct 模型进行微调，以使用 ultrachat_200k 数据集完成两人之间的对话。

![MLFineTune](../../../../translated_images/zh-CN/MLFineTune.928d4c6b3767dd35.webp)

该示例将向您展示如何使用 Azure ML SDK 和 Python 进行微调，然后将微调后的模型部署到在线端点以进行实时推理。

### 训练数据

我们将使用 ultrachat_200k 数据集。该数据集是 UltraChat 数据集的经过严格筛选版本，用于训练 Zephyr-7B-β，一款最先进的 7b 聊天模型。

### 模型

我们将使用 Phi-3-mini-4k-instruct 模型，演示用户如何为聊天完成任务微调模型。如果您是从特定模型卡打开此笔记本，请记得替换为相应的模型名称。

### 任务

- 选择要微调的模型。
- 选择并探索训练数据。
- 配置微调作业。
- 运行微调作业。
- 查看训练和评估指标。
- 注册微调后的模型。
- 部署微调后的模型以进行实时推理。
- 清理资源。

## 1. 环境准备

- 安装依赖
- 连接到 AzureML 工作区。详细信息请参阅设置 SDK 认证。下面替换 <WORKSPACE_NAME>、<RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>。
- 连接到 azureml 系统注册表
- 设置可选的实验名称
- 检查或创建计算资源。

> [!NOTE]
> 需要单个 GPU 节点可能拥有多个 GPU 卡。例如，Standard_NC24rs_v3 节点中有 4 个 NVIDIA V100 GPU，而 Standard_NC12s_v3 中有 2 个 NVIDIA V100 GPU。有关详细信息，请参考文档。每个节点的 GPU 卡数量在下方参数 gpus_per_node 中设置。正确设置此值可确保节点内所有 GPU 的利用率。推荐的 GPU 计算 SKU 可查询此处及此处。

### Python 库

运行以下单元安装依赖。如果在新环境中运行，此步骤不可省略。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### 与 Azure ML 交互

1. 该 Python 脚本用于与 Azure 机器学习 (Azure ML) 服务交互。下面是其功能简述：

    - 它从 azure.ai.ml、azure.identity 和 azure.ai.ml.entities 包导入必要模块。同时导入 time 模块。

    - 尝试使用 DefaultAzureCredential() 进行认证，该类提供简化的认证体验，可快速开始开发在 Azure 云中运行的应用程序。如果失败，则回退使用 InteractiveBrowserCredential()，提供交互式登录提示。

    - 尝试使用 from_config 方法创建 MLClient 实例，该方法从默认配置文件(config.json)读取配置。如果失败，则通过手动提供 subscription_id、resource_group_name 和 workspace_name 创建 MLClient 实例。

    - 创建另一个 MLClient 实例，针对名为 "azureml" 的 Azure ML 注册表。该注册表用于存储模型、微调流水线和环境。

    - 将 experiment_name 设置为 "chat_completion_Phi-3-mini-4k-instruct"。

    - 生成唯一时间戳，将当前时间（自纪元以来的秒数，浮点数）转换为整数再转为字符串。此时间戳可用于创建唯一名称和版本。

    ```python
    # 从 Azure ML 和 Azure Identity 导入必要的模块
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # 导入时间模块
    
    # 尝试使用 DefaultAzureCredential 进行身份验证
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # 如果 DefaultAzureCredential 失败，使用 InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # 尝试使用默认配置文件创建 MLClient 实例
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # 如果失败，通过手动提供详细信息创建 MLClient 实例
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # 为名为 "azureml" 的 Azure ML 注册表创建另一个 MLClient 实例
    # 该注册表是存储模型、微调管道和环境的地方
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # 设置实验名称
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # 生成一个唯一的时间戳，可用于需要唯一名称和版本的情况
    timestamp = str(int(time.time()))
    ```

## 2. 选择基础模型进行微调

1. Phi-3-mini-4k-instruct 是一个拥有 38 亿参数的轻量级最先进开源模型，基于 Phi-2 使用的数据集构建。该模型属于 Phi-3 模型家族，Mini 版本有支持上下文长度（以标记计）的两种变体：4K 和 128K。我们需要为特定用途微调该模型。您可以在 AzureML Studio 的模型目录中浏览这些模型，筛选聊天完成任务。本示例使用 Phi-3-mini-4k-instruct 模型。如果您为其它模型打开此笔记本，请相应替换模型名称和版本。

> [!NOTE]
> 这是模型的 id 属性，将作为输入传递到微调作业中。该 id 也可在 AzureML Studio 模型目录的模型详细信息页面中作为资产 ID 查看。

2. 该 Python 脚本用于与 Azure 机器学习 (Azure ML) 服务交互。下面是其操作总结：

    - 将 model_name 设置为 "Phi-3-mini-4k-instruct"。

    - 使用 registry_ml_client 对象的 models 属性的 get 方法，从 Azure ML 注册表中检索指定名称的模型的最新版本。get 方法调用时传入两个参数：模型名称和一个标签，标签指定应检索模型的最新版本。

    - 打印信息到控制台，指明用于微调的模型名称、版本和 id。使用字符串的 format 方法将模型的名称、版本和 id 插入消息。模型的名称、版本和 id 作为 foundation_model 对象的属性访问。

    ```python
    # 设置模型名称
    model_name = "Phi-3-mini-4k-instruct"
    
    # 从 Azure ML 注册表获取模型的最新版本
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # 打印模型名称、版本和 ID
    # 这些信息对于跟踪和调试很有用
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. 创建供作业使用的计算资源

微调作业仅支持 GPU 计算资源。计算规模取决于模型大小，许多情况下难以确定合适的计算资源。本单元引导用户选择合适的计算资源。

> [!NOTE]
> 以下列出的计算资源配置均为最优配置。更改配置可能导致 Cuda 内存溢出错误。若遇此问题，请尝试升级为更大规模的计算资源。

> [!NOTE]
> 选择 compute_cluster_size 时，请确保该计算资源在您的资源组中可用。如计算资源不可用，可提出请求以获得使用权限。

### 检查模型微调支持

1. 该 Python 脚本用于与 Azure 机器学习 (Azure ML) 模型交互。功能说明：

    - 导入 ast 模块，它提供处理 Python 抽象语法树的函数。

    - 检查 foundation_model 对象（代表 Azure ML 中的一个模型）是否有名为 finetune_compute_allow_list 的标签。Azure ML 标签是键值对，用于筛选和排序模型。

    - 如果存在 finetune_compute_allow_list 标签，使用 ast.literal_eval 安全地将标签值（字符串）解析为 Python 列表，将其赋给 computes_allow_list 变量。然后打印提示，说明应从此列表中创建计算资源。

    - 如果不存在该标签，设置 computes_allow_list 为 None，打印消息指出该标签不在模型标签中。

    - 总结，该脚本检查模型元数据中是否有特定标签，若有则转换为列表，并相应反馈给用户。

    ```python
    # 导入 ast 模块，该模块提供处理 Python 抽象语法树的函数
    import ast
    
    # 检查模型的标签中是否存在 'finetune_compute_allow_list' 标签
    if "finetune_compute_allow_list" in foundation_model.tags:
        # 如果标签存在，使用 ast.literal_eval 安全地将标签的值（字符串）解析为 Python 列表
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # 将字符串转换为 Python 列表
        # 打印一条消息，表示应从列表中创建计算
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # 如果标签不存在，将 computes_allow_list 设置为 None
        computes_allow_list = None
        # 打印一条消息，表示 'finetune_compute_allow_list' 标签不属于模型的标签
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### 检查计算实例

1. 该 Python 脚本用于与 Azure 机器学习 (Azure ML) 服务交互，并对计算实例执行多项检查。简要说明：

    - 尝试从 Azure ML 工作区获取名为 compute_cluster 的计算实例。如果该实例的配置状态为 "failed"，则抛出 ValueError。

    - 如果 computes_allow_list 不为 None，将其所有计算大小字符串转换为小写，并检查当前计算实例的规模是否在列表中。如果不在，则抛出 ValueError。

    - 若 computes_allow_list 为 None，则检查当前计算实例规模是否处于不支持的 GPU 虚拟机规模列表内。如果是，则抛出 ValueError。

    - 获取工作区内所有可用计算规模的列表。遍历列表，查找匹配计算实例规模的条目，获取该计算规模的 GPU 数量。若找到，将 gpu_count_found 设为 True。

    - 若 gpu_count_found 为 True，打印计算实例中 GPU 数量。否则抛出 ValueError。

    - 总结，该脚本对 Azure ML 工作区中的计算实例执行多项检查，包括配置状态、规模是否符合允许或拒绝列表，以及 GPU 数量。

    ```python
    # 打印异常信息
    print(e)
    # 如果计算资源大小在工作区中不可用，则引发 ValueError
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # 从 Azure ML 工作区检索计算实例
    compute = workspace_ml_client.compute.get(compute_cluster)
    # 检查计算实例的配置状态是否为“失败”
    if compute.provisioning_state.lower() == "failed":
        # 如果配置状态为“失败”，则引发 ValueError
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # 检查 computes_allow_list 是否不为 None
    if computes_allow_list is not None:
        # 将 computes_allow_list 中的所有计算资源大小转换为小写
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # 检查计算实例的大小是否在 computes_allow_list_lower_case 中
        if compute.size.lower() not in computes_allow_list_lower_case:
            # 如果计算实例的大小不在 computes_allow_list_lower_case 中，则引发 ValueError
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # 定义一份不支持的 GPU 虚拟机大小列表
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # 检查计算实例的大小是否在 unsupported_gpu_vm_list 中
        if compute.size.lower() in unsupported_gpu_vm_list:
            # 如果计算实例的大小在 unsupported_gpu_vm_list 中，则引发 ValueError
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # 初始化一个标志以检查是否已找到计算实例中的 GPU 数量
    gpu_count_found = False
    # 检索工作区中所有可用的计算资源大小列表
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # 遍历可用计算资源大小列表
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # 检查计算资源大小的名称是否与计算实例的大小匹配
        if compute_sku.name.lower() == compute.size.lower():
            # 如果匹配，检索该计算资源大小的 GPU 数量并将 gpu_count_found 设为 True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # 如果 gpu_count_found 为 True，则打印计算实例中的 GPU 数量
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # 如果 gpu_count_found 为 False，则引发 ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. 选择用于模型微调的数据集

1. 我们使用 ultrachat_200k 数据集。该数据集分为四个拆分，适合监督微调 (sft) 和生成排序 (gen) 任务。每个拆分的样本数如下所示：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 接下来的几个单元演示微调的基本数据准备：

### 可视化部分数据行

为了让示例快速运行，保存了包含已裁剪数据 5% 的 train_sft 和 test_sft 文件。这意味着微调模型的准确度较低，因此不建议用于真实场景。
download-dataset.py 脚本用于下载 ultrachat_200k 数据集，并将数据转换为微调流水线组件可消费的格式。由于数据集较大，这里只包含数据集的部分内容。

1. 运行以下脚本仅下载数据集的 5%。可通过修改 dataset_split_pc 参数来设置所需的百分比。

> [!NOTE]
> 一些语言模型具有不同的语言代码，因此数据集中的列名称应相应反映。

1. 以下示例展示了数据的样式
聊天完成数据集存储在 parquet 格式文件中，每条数据按以下模式存储：

    - 这是一个 JSON（JavaScript 对象表示法）文档，是一种流行的数据交换格式。它不是可执行代码，而是存储和传输数据的方式。其结构如下：

    - "prompt"：该键对应的字符串表示向 AI 助手提出的任务或问题。

    - "messages"：该键对应一个对象数组。每个对象代表用户与 AI 助手之间的一条对话消息。每条消息对象包含两个键：

    - "content"：消息内容字符串。
    - "role"：发送者角色字符串，可为 "user" 或 "assistant"。
    - "prompt_id"：对应提示的唯一标识符字符串。

1. 在此 JSON 文档中，用户请求 AI 助手创建一个反乌托邦故事的主角。助手响应后，用户请求更多细节。助手同意提供更多细节。整个对话关联着特定的 prompt_id。

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

1. 该 Python 脚本用于通过名为 download-dataset.py 的辅助脚本下载数据集。功能解释：

    - 导入 os 模块，提供跨操作系统的功能接口。

    - 使用 os.system 函数以 shell 方式执行 download-dataset.py 脚本并传入特定命令行参数。参数指定要下载的数据集（HuggingFaceH4/ultrachat_200k）、下载目录（ultrachat_200k_dataset）和拆分百分比（5）。os.system 函数返回命令的退出状态，该状态存储在 exit_status 变量。

    - 检查 exit_status 是否不为 0。在类 Unix 操作系统中，退出状态为 0 表示命令成功，其他值表示错误。如不为 0，则引发异常，提示下载数据集出错。

    - 总结，该脚本运行辅助脚本以下载数据集，若下载失败则抛出异常。

    ```python
    # 导入os模块，它提供了使用操作系统相关功能的方法
    import os
    
    # 使用os.system函数在shell中运行download-dataset.py脚本，并传递特定的命令行参数
    # 参数指定要下载的数据集（HuggingFaceH4/ultrachat_200k）、下载目录（ultrachat_200k_dataset）和数据集拆分的百分比（5）
    # os.system函数返回它执行的命令的退出状态；该状态存储在exit_status变量中
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # 检查exit_status是否不等于0
    # 在类Unix操作系统中，退出状态0通常表示命令成功，而任何其他数字表示错误
    # 如果exit_status不为0，则抛出异常，提示下载数据集时出错
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### 将数据加载到 DataFrame

1. 该 Python 脚本将 JSON Lines 文件加载到 pandas DataFrame 中，并显示前 5 行。功能说明：

    - 导入 pandas 库，这是一个强大的数据处理和分析库。

    - 设置 pandas 显示选项中的最大列宽为 0，表示打印时将显示列的完整文本，不进行截断。
- 它使用 pd.read_json 函数从 ultrachat_200k_dataset 目录加载 train_sft.jsonl 文件到一个 DataFrame。lines=True 参数表示文件是 JSON Lines 格式，每行是一个独立的 JSON 对象。

- 它使用 head 方法显示 DataFrame 的前 5 行。如果 DataFrame 少于 5 行，则显示所有行。

- 总结来说，该脚本是将一个 JSON Lines 文件加载进 DataFrame 并显示前 5 行且完整展示列文本。

    ```python
    # 导入pandas库，这是一个强大的数据操作和分析库
    import pandas as pd
    
    # 将pandas显示选项的最大列宽设置为0
    # 这意味着当打印DataFrame时，每列的完整文本将不会被截断
    pd.set_option("display.max_colwidth", 0)
    
    # 使用pd.read_json函数从ultrachat_200k_dataset目录加载train_sft.jsonl文件到DataFrame中
    # lines=True参数表示文件是JSON Lines格式，每行都是一个独立的JSON对象
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # 使用head方法显示DataFrame的前5行
    # 如果DataFrame少于5行，则显示所有行
    df.head()
    ```

## 5. 使用模型和数据作为输入提交微调任务

创建使用 chat-completion 管道组件的作业。了解更多关于微调支持的所有参数。

### 定义微调参数

1. 微调参数可以分为两类——训练参数、优化参数

1. 训练参数定义训练相关内容，例如——

    - 使用的优化器、调度器
    - 优化微调的指标
    - 训练步数、批大小等
    - 优化参数帮助优化 GPU 内存，高效利用计算资源。

1. 以下是属于该类别的一些参数。优化参数因模型而异，并与模型捆绑处理这些变化。

    - 启用 deepspeed 和 LoRA
    - 启用混合精度训练
    - 启用多节点训练

> [!NOTE]
> 监督微调可能导致偏离对齐或灾难性遗忘。建议检查此问题并在微调后运行对齐阶段。

### 微调参数

1. 该 Python 脚本设置了微调机器学习模型的参数。分解如下：

    - 设置默认训练参数，如训练周期数、训练与评估批大小、学习率及其调度器类型。

    - 设置默认优化参数，如是否使用层次相关传播 (LoRa)、DeepSpeed 及 DeepSpeed 阶段。

    - 将训练和优化参数合并为一个字典 finetune_parameters。

    - 检查 foundation_model 是否有模型特定的默认参数。若有，打印警告信息并用模型特定默认参数更新 finetune_parameters。使用 ast.literal_eval 将字符串转换为 Python 字典。

    - 打印最终用于运行的微调参数集。

    - 总结：该脚本设置并展示机器学习模型微调参数，可用模型特定参数覆写默认值。

    ```python
    # 设置默认的训练参数，如训练轮数、训练和评估的批次大小、学习率以及学习率调度器类型
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # 设置默认的优化参数，如是否应用分层相关性传播（LoRa）和DeepSpeed，以及DeepSpeed的阶段
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # 将训练参数和优化参数合并到一个名为finetune_parameters的字典中
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # 检查foundation_model是否有任何特定模型的默认参数
    # 如果有，打印警告信息并使用这些特定模型的默认参数更新finetune_parameters字典
    # 使用ast.literal_eval函数将特定模型默认参数从字符串转换为Python字典
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # 将字符串转换为Python字典
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # 打印将用于此次运行的最终微调参数集
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### 训练管道

1. 该 Python 脚本定义了一个函数用来生成机器学习训练管道的显示名称，并调用该函数生成打印显示名。详解如下：

1. 定义了 get_pipeline_display_name 函数。该函数基于训练管道相关参数生成一个显示名称。

1. 函数内部计算总批量大小，通过乘以每设备批次大小、梯度累积步数、每节点 GPU 数量和微调节点数。

1. 获取其他参数，如学习率调度器类型、是否启用 DeepSpeed、DeepSpeed 阶段、是否启用 LoRa、保留的模型检查点数限制和最大序列长度。

1. 构造一个包含所有参数的字符串，用连字符连接。如果启用 DeepSpeed 或 LoRa，字符串包含 "ds" 加阶段号，或 "lora"，否则包含 "nods" 或 "nolora"。

1. 函数返回该字符串，作为训练管道的显示名称。

1. 定义函数后调用生成显示名称并打印。

1. 总结：该脚本基于多种参数生成机器学习训练管道的显示名称并打印。

    ```python
    # 定义一个函数来生成训练管道的显示名称
    def get_pipeline_display_name():
        # 通过将每个设备的批量大小、梯度累积步数、每个节点的GPU数量以及用于微调的节点数量相乘来计算总批量大小
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # 获取学习率调度器的类型
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # 获取是否应用了DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # 获取DeepSpeed的阶段
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # 如果应用了DeepSpeed，在显示名称中包含“ds”后跟DeepSpeed阶段；否则，包含“nods”
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # 获取是否应用了层次相关传播（LoRa）
        lora = finetune_parameters.get("apply_lora", "false")
        # 如果应用了LoRa，在显示名称中包含“lora”；否则，包含“nolora”
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # 获取要保留的模型检查点数量限制
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # 获取最大序列长度
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # 通过连接所有参数并以连字符分隔来构建显示名称
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
    
    # 调用函数生成显示名称
    pipeline_display_name = get_pipeline_display_name()
    # 打印显示名称
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### 配置管道

该 Python 脚本使用 Azure 机器学习 SDK 定义并配置机器学习管道。分解如下：

1. 从 Azure AI ML SDK 导入必要模块。

1. 从注册表获取名为 "chat_completion_pipeline" 的管道组件。

1. 使用 `@pipeline` 装饰器和 `create_pipeline` 函数定义一个管道作业。管道名称设置为 `pipeline_display_name`。

1. 在 `create_pipeline` 函数内，用多种参数初始化获取的管道组件，包括模型路径、不同阶段的计算集群、训练和测试数据集划分、微调使用的 GPU 数量和其他微调参数。

1. 将微调作业的输出映射到管道作业输出，方便将微调模型注册，注册是部署到在线或批处理终端所必需。

1. 调用 `create_pipeline` 函数创建管道实例。

1. 设置管道中的 `force_rerun` 为 `True`，表示不使用先前作业的缓存结果。

1. 设置管道中的 `continue_on_step_failure` 为 `False`，表示如果任一步骤失败管道即停止。

1. 总结：该脚本使用 Azure 机器学习 SDK 定义并配置一个用于聊天完成任务的机器学习管道。

    ```python
    # 从 Azure AI ML SDK 导入必要的模块
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # 从注册表中获取名为 "chat_completion_pipeline" 的管道组件
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # 使用 @pipeline 装饰器和 create_pipeline 函数定义管道作业
    # 管道的名称设置为 pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # 使用各种参数初始化获取的管道组件
        # 这些包括模型路径、不同阶段的计算集群、用于训练和测试的数据集拆分、用于微调的 GPU 数量以及其他微调参数
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # 将数据集拆分映射到参数
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # 训练设置
            number_of_gpu_to_use_finetuning=gpus_per_node,  # 设置为计算资源中可用的 GPU 数量
            **finetune_parameters
        )
        return {
            # 将微调作业的输出映射到管道作业的输出
            # 这样做是为了方便注册微调后的模型
            # 要将模型部署到在线或批处理端点，必须注册模型
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # 通过调用 create_pipeline 函数创建管道实例
    pipeline_object = create_pipeline()
    
    # 不使用之前作业的缓存结果
    pipeline_object.settings.force_rerun = True
    
    # 将步骤失败时的继续设置为 False
    # 这意味着如果任何步骤失败，管道将停止运行
    pipeline_object.settings.continue_on_step_failure = False
    ```

### 提交作业

1. 该 Python 脚本将机器学习管道作业提交到 Azure 机器学习工作区，并等待作业完成。详解如下：

    - 调用 workspace_ml_client 中 jobs 对象的 create_or_update 方法提交管道作业。运行的管道由 pipeline_object 指定，作业所属实验名由 experiment_name 指定。

    - 调用 workspace_ml_client 中 jobs 对象的 stream 方法等待管道作业完成。等待的作业通过 pipeline_job 对象的 name 属性指定。

    - 总结：该脚本将机器学习管道作业提交到 Azure 机器学习工作区，并等待其完成。

    ```python
    # 将管道作业提交到 Azure 机器学习工作区
    # 要运行的管道由 pipeline_object 指定
    # 作业运行所属的实验由 experiment_name 指定
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # 等待管道作业完成
    # 要等待的作业由 pipeline_job 对象的 name 属性指定
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. 在工作区注册微调模型

我们将从微调作业的输出注册模型。这将跟踪微调模型与微调作业间的血缘关系。微调作业进一步跟踪基础模型、数据和训练代码的血缘。

### 注册 ML 模型

1. 该 Python 脚本注册 Azure 机器学习管道中训练的机器学习模型。详解如下：

    - 从 Azure AI ML SDK 导入必要模块。

    - 通过调用 workspace_ml_client 中 jobs 对象的 get 方法并访问其 outputs 属性，检查来自管道作业的 trained_model 输出是否可用。

    - 构造训练模型路径，格式化字符串使用管道作业名称和输出名 "trained_model"。

    - 定义微调模型名称，在原始模型名称后追加 "-ultrachat-200k"，并将斜杠替换为连字符。

    - 准备使用 Model 对象注册模型，设置模型路径、模型类型（MLflow 模型）、模型名称及版本及描述等参数。

    - 调用 workspace_ml_client 中 models 对象的 create_or_update 方法进行模型注册。

    - 打印注册成功的模型信息。

1. 总结：该脚本在 Azure 机器学习管道中注册训练好的机器学习模型。

    ```python
    # 从 Azure AI ML SDK 导入必要的模块
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # 检查管道作业中是否有 `trained_model` 输出
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # 通过格式化字符串构造训练模型的路径，字符串包含管道作业的名称和输出名称（"trained_model"）
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # 通过在原始模型名称后附加 "-ultrachat-200k" 并将所有斜杠替换为连字符来定义微调模型的名称
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # 准备注册模型，通过创建一个包含各种参数的 Model 对象
    # 这些参数包括模型路径、模型类型（MLflow 模型）、模型名称和版本以及模型描述
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # 使用时间戳作为版本以避免版本冲突
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # 通过调用 workspace_ml_client 中 models 对象的 create_or_update 方法并传入 Model 对象来注册模型
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # 打印已注册的模型
    print("registered model: \n", registered_model)
    ```

## 7. 将微调模型部署到在线端点

在线端点提供持久的 REST API，可用于集成需使用模型的应用。

### 管理端点

1. 该 Python 脚本为已注册模型在 Azure 机器学习中创建托管在线端点。详解如下：

    - 从 Azure AI ML SDK 导入必要模块。

    - 定义一个唯一的在线端点名称，在字符串 "ultrachat-completion-" 后追加时间戳。

    - 准备创建在线端点，创建 ManagedOnlineEndpoint 对象，设置端点名称、描述和身份验证模式（"key"）等参数。

    - 调用 workspace_ml_client 的 begin_create_or_update 方法并传入 ManagedOnlineEndpoint 对象创建端点，调用 wait 方法等待创建完成。

1. 总结：该脚本为已注册模型在 Azure 机器学习服务中创建一个托管在线端点。

    ```python
    # 从 Azure AI ML SDK 导入必要的模块
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # 通过在字符串 "ultrachat-completion-" 后附加时间戳来定义在线端点的唯一名称
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # 准备创建在线端点，通过创建具有各种参数的 ManagedOnlineEndpoint 对象
    # 这些参数包括端点的名称、端点的描述以及验证模式（"key"）
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # 通过调用 workspace_ml_client 的 begin_create_or_update 方法并传入 ManagedOnlineEndpoint 对象来创建在线端点
    # 然后通过调用 wait 方法等待创建操作完成
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> 这里是支持部署的 SKU 列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署 ML 模型

1. 该 Python 脚本将已注册机器学习模型部署到 Azure 机器学习的托管在线端点。详解如下：

    - 导入 ast 模块，该模块提供处理 Python 抽象语法树的函数。

    - 将部署实例类型设置为 "Standard_NC6s_v3"。

    - 检查 foundation_model 中是否存在 inference_compute_allow_list 标签。若存在，将其值从字符串转换为 Python 列表并赋值给 inference_computes_allow_list；否则设置为 None。

    - 检查指定实例类型是否在允许列表中。若不在，打印提示请用户选择允许列表中的实例类型。

    - 准备创建部署，创建 ManagedOnlineDeployment 对象，设置部署名称、端点名称、模型 ID、实例类型及数量、存活探针设置和请求设置等参数。

    - 调用 workspace_ml_client 的 begin_create_or_update 方法并传入 ManagedOnlineDeployment 对象创建部署，调用 wait 方法等待创建完成。

    - 将流量设置为将端点 100% 流量导入名为 "demo" 的部署。

    - 通过调用 workspace_ml_client 的 begin_create_or_update 方法更新端点，传入端点对象，调用 result 方法等待更新完成。

1. 总结：该脚本将已注册机器学习模型部署到 Azure 机器学习的托管在线端点。

    ```python
    # 导入 ast 模块，该模块提供处理 Python 抽象语法树的函数
    import ast
    
    # 设置部署的实例类型
    instance_type = "Standard_NC6s_v3"
    
    # 检查基础模型中是否存在 `inference_compute_allow_list` 标签
    if "inference_compute_allow_list" in foundation_model.tags:
        # 如果存在，将标签值从字符串转换为 Python 列表，并赋值给 `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # 如果不存在，将 `inference_computes_allow_list` 设置为 `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # 检查指定的实例类型是否在允许列表中
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # 准备创建部署，通过使用各种参数创建一个 `ManagedOnlineDeployment` 对象
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # 通过调用 `workspace_ml_client` 的 `begin_create_or_update` 方法并传入 `ManagedOnlineDeployment` 对象来创建部署
    # 然后通过调用 `wait` 方法等待创建操作完成
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # 设置端点流量，将 100% 流量导向 "demo" 部署
    endpoint.traffic = {"demo": 100}
    
    # 通过调用 `workspace_ml_client` 的 `begin_create_or_update` 方法并传入 `endpoint` 对象来更新端点
    # 然后通过调用 `result` 方法等待更新操作完成
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. 使用示例数据测试端点

我们将从测试数据集中获取部分示例数据，提交到在线端点进行推理。随后将展示预测标签与真实标签并排。

### 读取结果

1. 该 Python 脚本将 JSON Lines 文件读取到 pandas DataFrame，随机抽样并重置索引。详解如下：

    - 使用 pandas 的 read_json 函数读取文件 ./ultrachat_200k_dataset/test_gen.jsonl，使用 lines=True 参数，因为文件是 JSON Lines 格式，每行是独立 JSON 对象。

    - 从 DataFrame 中随机抽取 1 行。sample 函数使用 n=1 参数指定抽样行数。

    - 重置 DataFrame 索引，reset_index 函数使用 drop=True 参数丢弃原索引用默认整数索引替代。

    - 使用 head 函数展示 DataFrame 前 2 行，但由于采样后只有 1 行，实际只显示这 1 行。

1. 总结：该脚本将 JSON Lines 文件读取为 pandas DataFrame，随机抽取 1 行，重置索引并显示该行。

    ```python
    # 导入 pandas 库
    import pandas as pd
    
    # 将 JSON Lines 文件 './ultrachat_200k_dataset/test_gen.jsonl' 读入 pandas DataFrame
    # 参数 'lines=True' 表示文件是 JSON Lines 格式，每行都是一个独立的 JSON 对象
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # 从 DataFrame 中随机抽取 1 行样本
    # 参数 'n=1' 指定要随机选择的行数
    test_df = test_df.sample(n=1)
    
    # 重置 DataFrame 的索引
    # 参数 'drop=True' 表示丢弃原始索引，替换为默认的整型新索引
    # 参数 'inplace=True' 表示在原地修改 DataFrame（不创建新对象）
    test_df.reset_index(drop=True, inplace=True)
    
    # 显示 DataFrame 的前 2 行
    # 但由于抽样后 DataFrame 只有一行，这将只显示那一行
    test_df.head(2)
    ```

### 创建 JSON 对象

1. 该 Python 脚本创建带特定参数的 JSON 对象并保存到文件。详解如下：

    - 导入 json 模块，提供处理 JSON 数据的函数。
- 它创建了一个名为 parameters 的字典，包含表示机器学习模型参数的键和值。键分别是 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，对应的值分别是 0.6、0.9、True 和 200。

- 它创建了另一个名为 test_json 的字典，包含两个键："input_data" 和 "params"。"input_data" 的值是另一个字典，包含键 "input_string" 和 "parameters"。"input_string" 的值是一个列表，包含 test_df 数据框中的第一条消息。"parameters" 的值是之前创建的 parameters 字典。 "params" 的值是一个空字典。

- 它打开了一个名为 sample_score.json 的文件

    ```python
    # 导入 json 模块，该模块提供操作 JSON 数据的函数
    import json
    
    # 创建一个字典 `parameters`，包含代表机器学习模型参数的键和值
    # 键包括 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，对应的值分别是 0.6、0.9、True 和 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # 创建另一个字典 `test_json`，包含两个键："input_data" 和 "params"
    # "input_data" 的值是另一个字典，包含键 "input_string" 和 "parameters"
    # "input_string" 的值是一个列表，包含 `test_df` 数据框的第一条消息
    # "parameters" 的值是之前创建的 `parameters` 字典
    # "params" 的值是一个空字典
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # 以写模式打开位于 `./ultrachat_200k_dataset` 目录下名为 `sample_score.json` 的文件
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # 使用 `json.dump` 函数将 `test_json` 字典以 JSON 格式写入文件
        json.dump(test_json, f)
    ```

### 调用端点

1. 这个 Python 脚本正在调用 Azure 机器学习中的在线端点来对一个 JSON 文件进行评分。以下是其功能拆解：

    - 它调用 workspace_ml_client 对象的 online_endpoints 属性的 invoke 方法。此方法用于向在线端点发送请求并获取响应。

    - 它通过 endpoint_name 和 deployment_name 参数指定端点名称和部署名称。在此例中，端点名称存储在 online_endpoint_name 变量中，部署名称是 "demo"。

    - 它通过 request_file 参数指定要评分的 JSON 文件路径。此处文件路径为 ./ultrachat_200k_dataset/sample_score.json。

    - 它将端点返回的响应存储在 response 变量中。

    - 它打印了原始响应内容。

1. 总结来说，该脚本调用了 Azure 机器学习中的一个在线端点，对一个 JSON 文件进行评分，并打印了响应结果。

    ```python
    # 调用 Azure 机器学习中的在线端点对 `sample_score.json` 文件进行评分
    # 使用 `workspace_ml_client` 对象的 `online_endpoints` 属性的 `invoke` 方法发送请求到在线端点并获取响应
    # `endpoint_name` 参数指定端点的名称，存储在 `online_endpoint_name` 变量中
    # `deployment_name` 参数指定部署的名称，这里是 "demo"
    # `request_file` 参数指定要评分的 JSON 文件路径，为 `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # 打印来自端点的原始响应
    print("raw response: \n", response, "\n")
    ```

## 9. 删除在线端点

1. 别忘了删除在线端点，否则会因为端点占用的计算资源而持续计费。以下这行 Python 代码用于删除 Azure 机器学习中的一个在线端点。其功能拆解如下：

    - 它调用 workspace_ml_client 对象的 online_endpoints 属性的 begin_delete 方法。此方法用于开始删除一个在线端点。

    - 它通过 name 参数指定要删除的端点名称。在此例中，端点名称存储在 online_endpoint_name 变量中。

    - 它调用 wait 方法，等待删除操作完成。这是一个阻塞操作，会阻止脚本继续执行，直到删除完成。

    - 总结来说，这行代码启动了 Azure 机器学习中在线端点的删除操作，并等待其完成。

    ```python
    # 删除 Azure 机器学习中的在线端点
    # 使用 `workspace_ml_client` 对象的 `online_endpoints` 属性的 `begin_delete` 方法来启动在线端点的删除
    # `name` 参数指定要删除的端点名称，该名称存储在 `online_endpoint_name` 变量中
    # 调用 `wait` 方法以等待删除操作完成。这是一个阻塞操作，意味着在删除完成之前脚本将不会继续执行
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文档的母语版本应视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->