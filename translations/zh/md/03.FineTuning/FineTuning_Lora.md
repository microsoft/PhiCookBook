<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98eb289883c5e181a74e72a59e1ddc6d",
  "translation_date": "2025-04-03T08:07:25+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "zh"
}
-->
# **使用LoRA微调Phi-3**

利用[LoRA（低秩适应）](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)在自定义聊天指令数据集上微调微软的Phi-3 Mini语言模型。

LoRA可以帮助提升对话理解和响应生成能力。

## 微调Phi-3 Mini的分步指南：

**导入和设置**

安装loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先导入必要的库，例如datasets、transformers、peft、trl和torch。
设置日志记录以跟踪训练过程。

你可以选择通过使用loralib实现的对应模块替换一些层来进行适配。目前我们仅支持nn.Linear、nn.Embedding和nn.Conv2d。同时，对于某些实现中将多个层合并为一个的nn.Linear（例如注意力qkv投影），我们还支持MergedLinear（详见附加说明）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

导入loralib模块：

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

在训练循环开始之前，仅标记LoRA参数为可训练。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

保存检查点时，生成仅包含LoRA参数的state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

加载检查点时使用load_state_dict，并确保设置strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

之后可以按照常规方式进行训练。

**超参数**

定义两个字典：training_config和peft_config。training_config包含训练的超参数，例如学习率、批量大小和日志记录设置。

peft_config指定与LoRA相关的参数，如秩、dropout和任务类型。

**模型和分词器加载**

指定预训练Phi-3模型的路径（例如“microsoft/Phi-3-mini-4k-instruct”）。配置模型设置，包括缓存使用、数据类型（bfloat16用于混合精度）以及注意力实现。

**训练**

使用自定义聊天指令数据集微调Phi-3模型。利用peft_config中的LoRA设置实现高效适配。通过指定的日志策略监控训练进度。
评估和保存：评估微调后的模型。
在训练过程中保存检查点以供后续使用。

**样例**
- [通过这个样例笔记本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微调样例示例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用LoRA进行Hugging Face Hub微调的示例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face模型卡示例 - LoRA微调样例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [使用QLORA进行Hugging Face Hub微调的示例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们尽力确保翻译的准确性，但请注意，自动翻译可能会包含错误或不准确之处。原始语言版本的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而引发的任何误解或误读承担责任。