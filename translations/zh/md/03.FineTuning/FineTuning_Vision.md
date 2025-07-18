<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:36:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "zh"
}
-->
# Phi-3.5-vision 微调方案

这是使用 huggingface 库对 Phi-3.5-vision 进行微调的官方支持。  
请在运行以下命令前，`cd` 到代码目录 [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning)。

## 安装

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## 快速开始

我们提供了两个示例微调脚本，一个用于 DocVQA，另一个用于仇恨表情包分类。

最低硬件测试环境为 4x RTX8000（每个 GPU 48GB 内存）

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 现已正式支持多图像输入。以下是微调 NLVR2 的示例

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南

根据硬件情况，用户可以选择不同的微调策略。我们支持  
全量微调（使用 Deepspeed Zero-2），可选择冻结视觉参数，以及 LoRA（包括 4bit QLoRA）。  
一般来说，我们推荐尽可能使用带有 flash attention 和 bf16 的全量微调。

### 自定义数据集转换为所需格式的指南

我们使用一个最小的视频分类数据集（UCF-101 的子集）作为端到端示例，演示如何将自定义数据集转换为所需格式，并在其上微调 Phi-3.5-vision。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

转换后的数据示例如下：

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

对于 `jsonl` 注释文件，每行应为如下字典格式：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

注意 `conversations` 是一个列表，因此如果有多轮对话数据，也能支持多轮对话。

## 申请 Azure GPU 配额

### 前提条件

拥有 Azure 账户且具备 Contributor 角色（或包含 Contributor 权限的其他角色）。

如果没有 Azure 账户，请先[创建免费账户](https://azure.microsoft.com)。

### 申请配额提升

您可以直接在“我的配额”中提交配额提升申请。以下步骤演示如何申请配额提升。示例中，您可以选择订阅中任何可调整的配额。

登录 [Azure 门户](https://portal.azure.com)。

在搜索框输入“quotas”，然后选择 Quotas。  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在概览页，选择一个提供商，如 Compute 或 AML。

**注意** 除 Compute 外，其他提供商会显示“Request increase”列，而非下文所述的“Adjustable”列。您可以在此请求特定配额的提升，或创建支持请求。

在“我的配额”页，找到您想提升的配额，确保“Adjustable”列显示为 Yes。

页面顶部附近，选择“New Quota Request”，然后选择“Enter a new limit”。  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在“New Quota Request”面板中，输入新的配额数值，然后点击“Submit”。

您的申请将被审核，审核结果会通知您，通常几分钟内完成。

如果申请未通过，页面会提供创建支持请求的链接。使用该链接后，支持工程师会协助您完成配额提升申请。

## Azure 计算 GPU 机型建议

[ND A100 v4 系列](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5 系列](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下是一些示例：

### 如果您有 A100 或 H100 GPU

全量微调通常能获得最佳性能。您可以使用以下命令对 Phi-3-V 进行仇恨表情包分类微调。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### 如果您有 Standard_ND40rs_v2 8x V100-32GB GPU

仍然可以对 Phi-3-V 进行仇恨表情包分类的全量微调。但由于不支持 flash attention，吞吐量会远低于 A100 或 H100 GPU。  
同时由于不支持 bf16（改用 fp16 混合精度训练），准确率可能也会受到影响。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果您无法使用数据中心 GPU

LoRA 可能是您的唯一选择。您可以使用以下命令对 Phi-3-V 进行仇恨表情包分类微调。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

对于 Turing+ GPU，支持 QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 建议的超参数及预期准确率

### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

训练方法 | 是否冻结视觉模型 | 数据类型 | LoRA rank | LoRA alpha | 批量大小 | 学习率 | 训练轮数 | 准确率
--- | --- | --- | --- | --- | --- | --- | --- | --- |
全量微调 |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
全量微调 | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 结果即将发布 |  |  |  |  |  |  |  |  |

### 注意  
以下 DocVQA 和仇恨表情包的结果基于之前版本（Phi-3-vision）。  
Phi-3.5-vision 的新结果将尽快更新。

### DocVQA（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

训练方法 | 数据类型 | LoRA rank | LoRA alpha | 批量大小 | 学习率 | 训练轮数 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
全量微调 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
冻结图像模型 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
冻结图像模型 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 仇恨表情包（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

训练方法 | 数据类型 | LoRA rank | LoRA alpha | 批量大小 | 学习率 | 训练轮数 | 准确率
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
全量微调 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
冻结图像模型 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
冻结图像模型 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 速度基准测试（注意：Phi-3-vision）

Phi-3.5-vision 的新基准测试结果将尽快更新。

速度基准测试在 DocVQA 数据集上进行。该数据集的平均序列长度为 2443.23 个 token（图像模型使用 `num_crops=16`）。

### 8x A100-80GB（Ampere）

训练方法 | 节点数 | GPU 数量 | flash attention | 有效批量大小 | 吞吐量（张/秒） | 加速比 | GPU 峰值内存（GB）
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | 1 | 8 |  | 64 | 5.041 | 1x | ~42
全量微调 | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
全量微调 | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
全量微调 | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
冻结图像模型 | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
冻结图像模型 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB（Volta）

训练方法 | 节点数 | GPU 数量 | flash attention | 有效批量大小 | 吞吐量（张/秒） | 加速比 | GPU 峰值内存（GB）
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | 1 | 8 |  | 64 | 2.462 | 1x | ~32
全量微调 | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
全量微调 | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
冻结图像模型 | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 已知问题

- fp16 下无法运行 flash attention（建议有条件时优先使用 bf16，所有支持 flash attention 的 GPU 也都支持 bf16）。
- 目前不支持保存中间检查点和恢复训练。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。