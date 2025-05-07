<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-07T13:30:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "zh"
}
-->
# **使用 Lora 微调 Phi-3**

使用 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 对微软的 Phi-3 Mini 语言模型进行微调，基于自定义的聊天指令数据集。

LORA 有助于提升对话理解和响应生成能力。

## 微调 Phi-3 Mini 的详细步骤：

**导入与设置**

安装 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先导入所需的库，如 datasets、transformers、peft、trl 和 torch。
设置日志记录以跟踪训练过程。

你可以选择用 loralib 实现的对应层替换部分层进行适配。目前仅支持 nn.Linear、nn.Embedding 和 nn.Conv2d。我们还支持 MergedLinear，用于某些实现中一个 nn.Linear 代表多个层的情况，比如注意力机制中的 qkv 投影（详情见附加说明）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

在训练循环开始前，仅将 LoRA 参数标记为可训练。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

保存检查点时，生成仅包含 LoRA 参数的 state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

加载检查点时，使用 load_state_dict 并确保设置 strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

现在可以像平常一样开始训练。

**超参数**

定义两个字典：training_config 和 peft_config。training_config 包含训练的超参数，如学习率、批量大小和日志设置。

peft_config 指定与 LoRA 相关的参数，如秩（rank）、dropout 和任务类型。

**模型和分词器加载**

指定预训练 Phi-3 模型的路径（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型设置，包括缓存使用、数据类型（bfloat16 用于混合精度）和注意力实现方式。

**训练**

使用自定义聊天指令数据集对 Phi-3 模型进行微调。利用 peft_config 中的 LoRA 设置实现高效适配。通过指定的日志策略监控训练进度。
评估与保存：对微调后的模型进行评估。
训练过程中保存检查点以备后续使用。

**示例**
- [通过此示例笔记本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微调示例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub 上使用 LORA 微调示例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡示例 - LORA 微调示例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub 上使用 QLORA 微调示例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或曲解，我们不承担任何责任。