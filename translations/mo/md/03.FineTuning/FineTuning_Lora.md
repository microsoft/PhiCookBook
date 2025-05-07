<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-07T13:30:56+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "mo"
}
-->
# **Fine-tuning Phi-3 with Lora**

Fine-tuning Microsoft's Phi-3 Mini language model using [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) on a custom chat instruction dataset.

LORA will help improve conversational understanding and response generation.

## Step-by-step guide on how to fine-tune Phi-3 Mini:

**Imports and Setup**

Installing loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Start by importing essential libraries such as datasets, transformers, peft, trl, and torch.  
Set up logging to monitor the training progress.

You can choose to adapt certain layers by swapping them with versions implemented in loralib. Currently, we support nn.Linear, nn.Embedding, and nn.Conv2d. Additionally, MergedLinear is supported for cases where a single nn.Linear represents multiple layers, like some attention qkv projection implementations (see Additional Notes for details).

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

Before starting the training loop, make sure only LoRA parameters are marked as trainable.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

When saving a checkpoint, create a state_dict that contains only LoRA parameters.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

When loading a checkpoint with load_state_dict, remember to set strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Now you can proceed with training as usual.

**Hyperparameters**

Define two dictionaries: training_config and peft_config.  
training_config includes training hyperparameters such as learning rate, batch size, and logging options.

peft_config contains LoRA-specific settings like rank, dropout, and task type.

**Model and Tokenizer Loading**

Specify the path to the pre-trained Phi-3 model (e.g., "microsoft/Phi-3-mini-4k-instruct"). Configure model options including cache usage, data type (bfloat16 for mixed precision), and attention implementation.

**Training**

Fine-tune the Phi-3 model using your custom chat instruction dataset. Use the LoRA parameters from peft_config for efficient adaptation. Track training progress with the configured logging strategy.  
Evaluation and Saving: Evaluate the fine-tuned model and save checkpoints during training for future use.

**Samples**  
- [Learn More with this sample notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Example of Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Example of Hugging Face Hub Fine Tuning with LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Example Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
Dis dokument has ben translaited using AI translait service [Co-op Translator](https://github.com/Azure/co-op-translator). Wail wi strive for accuracy, plies be awair dat automated translaits may contain errors or inaccuracies. Di original dokument in its native language shud be considered di authoritative source. For critical information, professional human translait is recommended. Wi ar not liable for any misunderstandings or misinterpretations arising from di use of dis translait.