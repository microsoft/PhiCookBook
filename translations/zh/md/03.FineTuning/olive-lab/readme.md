<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-05-07T13:40:36+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "zh"
}
-->
# 实验室：优化 AI 模型以实现设备端推理

## 介绍

> [!IMPORTANT]  
> 本实验需要配备 **Nvidia A10 或 A100 GPU**，并安装相应的驱动和 CUDA 工具包（版本 12 及以上）。

> [!NOTE]  
> 这是一个 **35分钟** 的实验，将带你动手了解使用 OLIVE 优化设备端推理模型的核心概念。

## 学习目标

完成本实验后，你将能够使用 OLIVE：

- 使用 AWQ 量化方法对 AI 模型进行量化。
- 针对特定任务对 AI 模型进行微调。
- 生成 LoRA 适配器（微调模型），以便在 ONNX Runtime 上实现高效的设备端推理。

### 什么是 Olive

Olive（*O*NNX *live*）是一个模型优化工具包，配备了命令行界面（CLI），使你能够为 ONNX runtime +++https://onnxruntime.ai+++ 提供高质量和高性能的模型。

![Olive 流程图](../../../../../translated_images/olive-flow.5daf97340275f8b61397e91430ff02724a2547937b352e7fdfc2f669c56dcd35.zh.png)

Olive 的输入通常是 PyTorch 或 Hugging Face 模型，输出是一个经过优化的 ONNX 模型，在运行 ONNX runtime 的设备（部署目标）上执行。Olive 会针对部署目标的 AI 加速器（NPU、GPU、CPU）进行模型优化，这些硬件由 Qualcomm、AMD、Nvidia 或 Intel 等厂商提供。

Olive 执行一个 *工作流*，即一系列有序的模型优化任务，称为 *passes* —— 示例包括：模型压缩、图捕获、量化、图优化。每个 pass 都有一组可调参数，用于达到最佳指标，如准确率和延迟，这些指标由相应的评估器评估。Olive 使用搜索算法的搜索策略，自动逐个或批量调优每个 pass。

#### Olive 的优势

- **减少反复试验的挫败感和时间**，无需手动尝试各种图优化、压缩和量化技术。定义你的质量和性能约束，让 Olive 自动帮你找到最佳模型。
- **内置 40+ 模型优化组件**，涵盖量化、压缩、图优化和微调等前沿技术。
- **易用的 CLI**，支持常见的模型优化任务，如 olive quantize、olive auto-opt、olive finetune。
- 内置模型打包和部署功能。
- 支持生成 **多 LoRA 服务** 的模型。
- 通过 YAML/JSON 构建工作流，实现模型优化和部署任务的编排。
- 与 **Hugging Face** 和 **Azure AI** 集成。
- 内置 **缓存** 机制，帮助 **节省成本**。

## 实验指导
> [!NOTE]  
> 请确保你已根据实验 1 配置好 Azure AI Hub 和项目，并设置好 A100 计算资源。

### 步骤 0：连接到你的 Azure AI 计算资源

你将使用 **VS Code** 的远程功能连接到 Azure AI 计算资源。

1. 打开你的 **VS Code** 桌面应用程序：  
1. 使用 **Shift+Ctrl+P** 打开 **命令面板**  
1. 在命令面板中搜索 **AzureML - remote: Connect to compute instance in New Window**。  
1. 按屏幕提示操作，选择你的 Azure 订阅、资源组、项目和你在实验 1 中设置的计算名称。  
1. 成功连接后，你将在 Visual Studio Code 左下角看到连接状态 `><Azure ML: Compute Name`。

### 步骤 1：克隆仓库

在 VS Code 中，按 **Ctrl+J** 打开一个新的终端，克隆此仓库：

终端中会显示提示：

```
azureuser@computername:~/cloudfiles/code$ 
```  
克隆解决方案

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### 步骤 2：在 VS Code 中打开文件夹

在终端中执行以下命令，将在新窗口打开相关文件夹：

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

或者，你也可以通过选择 **文件** > **打开文件夹** 来打开。

### 步骤 3：安装依赖

在 Azure AI 计算实例的 VS Code 终端中（提示：**Ctrl+J**），执行以下命令安装依赖：

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> 安装所有依赖大约需要 5 分钟。

在本实验中，你将下载并上传模型到 Azure AI 模型目录。为访问模型目录，你需要登录 Azure：

```bash
az login
```

> [!NOTE]  
> 登录时会要求你选择订阅，请确保选择本实验提供的订阅。

### 步骤 4：执行 Olive 命令

在 Azure AI 计算实例的 VS Code 终端中（提示：**Ctrl+J**），确保已激活 `olive-ai` conda 环境：

```bash
conda activate olive-ai
```

接下来，在命令行中执行以下 Olive 命令。

1. **查看数据：** 本例中，你将微调 Phi-3.5-Mini 模型，使其专注于回答旅行相关问题。以下代码显示数据集的前几条记录，格式为 JSON lines：

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **量化模型：** 在训练模型之前，先用以下命令进行量化，采用一种称为主动感知量化（AWQ）的技术 +++https://arxiv.org/abs/2306.00978+++。AWQ 通过考虑推理时产生的激活值对模型权重进行量化。这意味着量化过程会结合激活的实际数据分布，相较传统权重量化方法能更好地保持模型准确性。

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    AWQ 量化大约需要 **8 分钟**，能将模型大小从约 7.5GB 减少到约 2.5GB。

    在本实验中，我们展示如何从 Hugging Face 输入模型（例如：`microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` 命令对量化后的模型进行微调）。先量化再微调比先微调后量化能获得更好的准确率，因为微调过程能部分恢复量化带来的损失。

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    微调（100 步）大约需要 **6 分钟**。

1. **优化：** 模型训练完成后，使用 Olive 的 `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` 参数进行优化——但本实验中我们使用 CPU。

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    优化大约需要 **5 分钟**。

### 步骤 5：模型推理快速测试

为了测试模型推理，在你的文件夹中创建一个名为 **app.py** 的 Python 文件，并复制粘贴以下代码：

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

使用以下命令执行代码：

```bash
python app.py
```

### 步骤 6：上传模型到 Azure AI

将模型上传到 Azure AI 模型库，可以让你的开发团队成员共享模型，并实现模型的版本控制。运行以下命令上传模型：

> [!NOTE]  
> 请更新 `{}` 中的 `resourceGroup` 和 Azure AI 项目名称，然后运行命令。

```
az ml workspace show
```

或者访问 +++ai.azure.com+++，选择 **管理中心** > **项目** > **概览**

将 `{}` 占位符替换为你的资源组名称和 Azure AI 项目名称。

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
你可以在 https://ml.azure.com/model/list 查看上传的模型并进行部署。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。