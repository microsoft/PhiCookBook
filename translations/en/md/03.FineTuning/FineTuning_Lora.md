<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-09T19:05:07+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "en"
}
-->
# **Fine-tuning Phi-3 with Lora**

Fine-tuning Microsoft's Phi-3 Mini language model using [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) on a custom chat instruction dataset.

LoRA helps enhance conversational understanding and response generation.

## Step-by-step guide on how to fine-tune Phi-3 Mini:

**Imports and Setup**

Installing loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Start by importing the necessary libraries such as datasets, transformers, peft, trl, and torch.  
Set up logging to monitor the training process.

You can choose to adapt certain layers by replacing them with versions implemented in loralib. Currently, we support nn.Linear, nn.Embedding, and nn.Conv2d. We also support a MergedLinear for cases where a single nn.Linear represents multiple layers, like in some implementations of the attention qkv projection (see Additional Notes for details).

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

Before starting the training loop, mark only the LoRA parameters as trainable.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

When saving a checkpoint, create a state_dict that includes only the LoRA parameters.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

When loading a checkpoint with load_state_dict, make sure to set strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Now you can proceed with training as usual.

**Hyperparameters**

Define two dictionaries: training_config and peft_config. training_config contains training hyperparameters like learning rate, batch size, and logging settings.

peft_config specifies LoRA-related parameters such as rank, dropout, and task type.

**Model and Tokenizer Loading**

Specify the path to the pre-trained Phi-3 model (e.g., "microsoft/Phi-3-mini-4k-instruct"). Configure model settings including cache usage, data type (bfloat16 for mixed precision), and attention implementation.

**Training**

Fine-tune the Phi-3 model using the custom chat instruction dataset. Use the LoRA settings from peft_config for efficient adaptation. Track training progress with the chosen logging strategy.  
Evaluation and Saving: Evaluate the fine-tuned model.  
Save checkpoints during training for future use.

**Samples**  
- [Learn More with this sample notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Example of Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Example of Hugging Face Hub Fine Tuning with LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Example Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.