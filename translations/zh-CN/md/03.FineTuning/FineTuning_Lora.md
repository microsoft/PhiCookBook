# **使用 Lora 微调 Phi-3**

使用 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 在自定义聊天指令数据集上微调微软的 Phi-3 Mini 语言模型。

LORA 有助于提升对话理解和响应生成能力。

## Phi-3 Mini 微调的逐步指南：

**导入和设置**

安装 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先导入所需的库，如 datasets、transformers、peft、trl 和 torch。  
设置日志记录以跟踪训练过程。

你可以选择通过替换为 loralib 实现的对应层来适配部分层。目前仅支持 nn.Linear、nn.Embedding 和 nn.Conv2d。对于某些情况下单个 nn.Linear 表示多层的情况（例如某些注意力 qkv 投影的实现，详见附加说明），我们也支持 MergedLinear。

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

保存检查点时，生成只包含 LoRA 参数的 state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

使用 load_state_dict 加载检查点时，确保设置 strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

现在可以照常进行训练。

**超参数**

定义两个字典：training_config 和 peft_config。training_config 包含训练的超参数，如学习率、批量大小和日志设置。

peft_config 指定与 LoRA 相关的参数，如秩（rank）、dropout 和任务类型。

**模型和分词器加载**

指定预训练 Phi-3 模型的路径（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型设置，包括缓存使用、数据类型（混合精度使用 bfloat16）和注意力实现方式。

**训练**

使用自定义聊天指令数据集微调 Phi-3 模型。利用 peft_config 中的 LoRA 设置实现高效适配。通过指定的日志策略监控训练进度。  
评估和保存：评估微调后的模型。  
训练过程中保存检查点以备后续使用。

**示例**  
- [通过此示例笔记本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python 微调示例](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub 上使用 LORA 微调示例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face 模型卡示例 - LORA 微调](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub 上使用 QLORA 微调示例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。