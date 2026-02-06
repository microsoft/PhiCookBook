## 欢迎使用 VS Code 的 AI 工具包

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) 集成了来自 Azure AI Studio 目录及 Hugging Face 等其他目录的多种模型。该工具包简化了使用生成式 AI 工具和模型构建 AI 应用的常见开发任务，功能包括：
- 快速开始模型发现和试玩。
- 使用本地计算资源进行模型微调和推理。
- 使用 Azure 资源进行远程微调和推理。

[安装 AI Toolkit for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/zh-CN/Aitoolkit.7157953df04812dc.webp)

**[Private Preview]** 一键为 Azure Container Apps 配置，支持在云端运行模型微调和推理。

现在，让我们开始你的 AI 应用开发：

- [欢迎使用 VS Code 的 AI 工具包](../../../../md/03.FineTuning)
- [本地开发](../../../../md/03.FineTuning)
  - [准备工作](../../../../md/03.FineTuning)
  - [激活 Conda](../../../../md/03.FineTuning)
  - [仅基础模型微调](../../../../md/03.FineTuning)
  - [模型微调与推理](../../../../md/03.FineTuning)
  - [模型微调](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [微调示例和资源](../../../../md/03.FineTuning)
- [**\[Private Preview\]** 远程开发](../../../../md/03.FineTuning)
  - [前提条件](../../../../md/03.FineTuning)
  - [设置远程开发项目](../../../../md/03.FineTuning)
  - [配置 Azure 资源](../../../../md/03.FineTuning)
  - [\[可选\] 将 Huggingface Token 添加到 Azure Container App Secret](../../../../md/03.FineTuning)
  - [运行微调](../../../../md/03.FineTuning)
  - [配置推理端点](../../../../md/03.FineTuning)
  - [部署推理端点](../../../../md/03.FineTuning)
  - [高级用法](../../../../md/03.FineTuning)

## 本地开发
### 准备工作

1. 确保主机已安装 NVIDIA 驱动。
2. 如果使用 HF 数据集，运行 `huggingface-cli login`。
3. `Olive` 关键设置说明，涉及任何修改内存使用的配置。

### 激活 Conda
由于我们使用的是共享的 WSL 环境，需要手动激活 conda 环境。完成此步骤后即可运行微调或推理。

```bash
conda activate [conda-env-name] 
```

### 仅基础模型微调
如果只想尝试基础模型而不进行微调，激活 conda 后可以运行以下命令。

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### 模型微调与推理

打开开发容器中的工作区后，打开终端（默认路径为项目根目录），运行以下命令对选定数据集进行 LLM 微调。

```bash
python finetuning/invoke_olive.py 
```

检查点和最终模型将保存在 `models` 文件夹中。

接下来，可以通过 `console`、`web browser` 或 `prompt flow` 使用微调后的模型进行聊天推理。

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

要在 VS Code 中使用 `prompt flow`，请参考此[快速入门](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)。

### 模型微调

接下来，根据设备是否有 GPU，下载以下模型。

使用 QLoRA 启动本地微调会话时，从我们的目录中选择要微调的模型。
| 平台 | 是否有 GPU | 模型名称 | 大小 (GB) |
|---------|---------|--------|--------|
| Windows | 是 | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | 是 | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | 否 | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_注意_** 下载模型不需要 Azure 账号。

Phi3-mini (int4) 模型大小约为 2GB-3GB，下载时间取决于网络速度，可能需要几分钟。

首先选择项目名称和位置。
然后从模型目录中选择模型。系统会提示下载项目模板，之后点击“配置项目”调整各种设置。

### Microsoft Olive

我们使用 [Olive](https://microsoft.github.io/Olive/why-olive.html) 在 PyTorch 模型上运行 QLoRA 微调。所有设置均预设为默认值，以优化本地微调过程中的内存使用，但你可以根据实际情况进行调整。

### 微调示例和资源

- [微调入门指南](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [使用 HuggingFace 数据集进行微调](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [使用简单数据集进行微调](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** 远程开发

### 前提条件

1. 要在远程 Azure Container App 环境中运行模型微调，确保订阅有足够的 GPU 容量。可提交[支持工单](https://azure.microsoft.com/support/create-ticket/)申请所需容量。[了解更多 GPU 容量信息](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. 如果使用 HuggingFace 私有数据集，确保拥有[HuggingFace 账号](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo)并[生成访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. 在 AI Toolkit for VS Code 中启用远程微调和推理功能标志
   1. 打开 VS Code 设置，选择 *文件 -> 首选项 -> 设置*。
   2. 导航到 *扩展*，选择 *AI Toolkit*。
   3. 选择 *"Enable Remote Fine-tuning And Inference"* 选项。
   4. 重载 VS Code 使设置生效。

- [远程微调](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### 设置远程开发项目
1. 执行命令面板中的 `AI Toolkit: Focus on Resource View`。
2. 进入 *Model Fine-tuning* 访问模型目录。为项目命名并选择本地存储位置，然后点击 *"Configure Project"*。
3. 项目配置
    1. 避免启用 *"Fine-tune locally"* 选项。
    2. Olive 配置设置将显示预设默认值，请根据需要调整填写。
    3. 继续点击 *Generate Project*。此步骤利用 WSL 并设置新的 Conda 环境，为未来支持 Dev Containers 做准备。
4. 点击 *"Relaunch Window In Workspace"* 打开远程开发项目。

> **注意：** 该项目目前仅支持在 AI Toolkit for VS Code 中本地或远程运行。如果创建项目时选择了 *"Fine-tune locally"*，则仅在 WSL 中运行，不支持远程开发。反之，不启用 *"Fine-tune locally"*，项目将仅限于远程 Azure Container App 环境。

### 配置 Azure 资源
开始前，需要为远程微调配置 Azure 资源。通过命令面板运行 `AI Toolkit: Provision Azure Container Apps job for fine-tuning`。

可通过输出通道显示的链接监控配置进度。

### [可选] 将 Huggingface Token 添加到 Azure Container App Secret
如果使用私有 HuggingFace 数据集，可将 HuggingFace 令牌设置为环境变量，避免在 Hugging Face Hub 手动登录。
使用命令 `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`，将 Secret 名称设置为 [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken)，并使用你的 Hugging Face 令牌作为 Secret 值。

### 运行微调
执行 `AI Toolkit: Run fine-tuning` 命令启动远程微调任务。

查看系统和控制台日志，可通过输出面板中的链接访问 Azure 门户（更多步骤见[在 Azure 上查看和查询日志](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)）。也可以在 VSCode 输出面板直接查看控制台日志，运行命令 `AI Toolkit: Show the running fine-tuning job streaming logs`。
> **注意：** 任务可能因资源不足而排队。如果日志未显示，执行 `AI Toolkit: Show the running fine-tuning job streaming logs` 命令，等待一段时间后再次执行以重新连接日志流。

微调过程中将使用 QLoRA，为模型创建 LoRA 适配器以供推理使用。
微调结果将存储在 Azure Files 中。

### 配置推理端点
适配器训练完成后，使用简单的 Gradio 应用与模型交互。
与微调过程类似，需要通过命令面板执行 `AI Toolkit: Provision Azure Container Apps for inference` 配置远程推理的 Azure 资源。

默认情况下，推理的订阅和资源组应与微调时使用的保持一致。推理将使用相同的 Azure Container App 环境，访问微调步骤中生成并存储在 Azure Files 的模型和模型适配器。

### 部署推理端点
如果需要修改推理代码或重新加载推理模型，请执行 `AI Toolkit: Deploy for inference` 命令。此操作会将最新代码同步到 Azure Container App 并重启副本。

部署成功后，可点击 VSCode 通知中的“*Go to Inference Endpoint*”按钮访问推理 API。或者，在 `./infra/inference.config.json` 文件中的 `ACA_APP_ENDPOINT` 以及输出面板中找到 Web API 端点。现在你可以使用该端点评估模型。

### 高级用法
有关 AI Toolkit 远程开发的更多信息，请参阅[远程微调模型](https://aka.ms/ai-toolkit/remote-provision)和[使用微调模型进行推理](https://aka.ms/ai-toolkit/remote-inference)文档。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。