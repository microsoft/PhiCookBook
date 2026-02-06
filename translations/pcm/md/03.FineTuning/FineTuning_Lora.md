# **Fine-tuning Phi-3 wit LoRA**

Dis na fine-tuning of Microsoft's Phi-3 Mini language model using [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) on top custom chat instruction dataset. 

LoRA go help improve conversational understanding and response generation. 

## Step-by-step guide wey show how to fine-tune Phi-3 Mini:

**Imports and Setup** 

Installing loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Begin by importing di necessary libraries such as datasets, transformers, peft, trl, and torch.
Set up logging to track di training process.

You fit choose to adapt some layers by replacing dem with counterparts wey loralib implement. We only support nn.Linear, nn.Embedding, and nn.Conv2d for now. We also support a MergedLinear for cases where a single nn.Linear represents more than one layer, such as in some implementations of the attention qkv projection (see Additional Notes for more).

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

Before di training loop start, mark only LoRA parameters as trainable.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

When you dey save checkpoint, generate a state_dict wey only contain LoRA parameters.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

When you dey load checkpoint using load_state_dict, make sure say you set strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Now training fit proceed as usual.

**Hyperparameters** 

Define two dictionaries: training_config and peft_config. training_config get hyperparameters for training, such as learning rate, batch size, and logging settings.

peft_config specify LoRA-related parameters like rank, dropout, and task type.

**Model and Tokenizer Loading** 

Specify di path to di pre-trained Phi-3 model (e.g., "microsoft/Phi-3-mini-4k-instruct"). Configure model settings, including cache usage, data type (bfloat16 for mixed precision), and attention implementation.

**Training** 

Fine-tune di Phi-3 model using di custom chat instruction dataset. Use di LoRA settings from peft_config for efficient adaptation. Monitor di training progress using di specified logging strategy.
Evaluation and Saving: Evaluate di fine-tuned model.
Save checkpoints during training make you fit use am later.

**Samples**
- [Learn more wit dis sample notebook](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning wit LoRA](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example Hugging Face Model Card - LoRA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Example of Hugging Face Hub Fine Tuning wit QLORA](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate with AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make everything correct, abeg note say automated translations fit get mistakes or no too accurate. The original document for im own language na the correct/official source. If na serious matter, better make you use professional human translator. We no go responsible for any misunderstanding or wrong meaning wey fit come from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->