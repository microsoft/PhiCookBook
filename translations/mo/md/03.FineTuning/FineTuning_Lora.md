<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98eb289883c5e181a74e72a59e1ddc6d",
  "translation_date": "2025-04-04T13:12:25+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "mo"
}
-->
# **Phi-3 Mini ကို LoRA နဲ့ Fine-tuning လုပ်ခြင်း**

Microsoft ရဲ့ Phi-3 Mini ဘာသာစကားမော်ဒယ်ကို [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) အသုံးပြုပြီး ကိုယ်ပိုင် Chat Instruction Dataset ပေါ်မှာ Fine-tuning လုပ်ခြင်း။

LoRA က ဆွေးနွေးမှုနားလည်မှုနဲ့ အဖြေထုတ်ပေးမှုကို တိုးတက်စေမှာဖြစ်ပါတယ်။

## Phi-3 Mini ကို Fine-tuning လုပ်ရန် လိုက်နာရမည့်အဆင့်ဆင့်လမ်းညွှန်:

**Imports နဲ့ အစပျိုးခြင်း**

loralib ကို Install လုပ်ခြင်း

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

လိုအပ်သော Library တွေ (datasets, transformers, peft, trl, torch) ကို Import လုပ်ပါ။
Training လုပ်ငန်းစဉ်ကို Monitor လုပ်နိုင်ဖို့ Logging ကို Set up လုပ်ပါ။

บาง Layer တွေကို LoRA နဲ့ ပြောင်းလဲနိုင်ပါတယ်။ လောလတ်တလောမှာ nn.Linear, nn.Embedding, nn.Conv2d ကိုပဲ Support လုပ်ပါတယ်။ nn.Linear တစ်ခုက Layer အများအပြားကို ကိုယ်စားပြုတဲ့အခါ (ဥပမာ Attention qkv projection အတွက်) MergedLinear ကိုလည်း Support လုပ်ပါတယ် (နောက်ထပ် မှတ်ချက်တွေကို ကြည့်ပါ)။

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

Training Loop စမယ့်အခါ LoRA Parameters တွေကိုပဲ Trainable အဖြစ် သတ်မှတ်ပါ။

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Checkpoint ကို Save လုပ်တဲ့အခါ LoRA Parameters တွေပါဝင်တဲ့ state_dict ကိုသာ Generate လုပ်ပါ။

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Checkpoint ကို load_state_dict နဲ့ Load လုပ်တဲ့အခါ strict=False လို့ သတ်မှတ်ပါ။

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

အခုတော့ Training ကို ပုံမှန်အတိုင်း ဆက်လက်လုပ်နိုင်ပါပြီ။

**Hyperparameters**

training_config နဲ့ peft_config ဆိုတဲ့ Dictionary နှစ်ခုကို သတ်မှတ်ပါ။  
training_config မှာ Learning Rate, Batch Size, Logging Setting စတဲ့ Training Hyperparameters တွေ ပါဝင်ပါတယ်။

peft_config မှာ LoRA ဆိုင်ရာ Parameters (Rank, Dropout, Task Type) တွေ ပါပါတယ်။

**Model နဲ့ Tokenizer Loading**

Pre-trained Phi-3 Model (ဥပမာ "microsoft/Phi-3-mini-4k-instruct") ရဲ့ Path ကို သတ်မှတ်ပါ။  
Model Settings တွေ (Cache Usage, Data Type (Mixed Precision အတွက် bfloat16), Attention Implementation) ကို Configure လုပ်ပါ။

**Training**

ကိုယ်ပိုင် Chat Instruction Dataset ကို အသုံးပြုပြီး Phi-3 Model ကို Fine-tune လုပ်ပါ။  
peft_config ရဲ့ LoRA Settings တွေကို အသုံးပြုပြီး အကျိုးရှိစွာ Adapt လုပ်ပါ။  
Training လုပ်စဉ် Progress ကို သတ်မှတ်ထားတဲ့ Logging Strategy နဲ့ Monitor လုပ်ပါ။  
**Evaluation နဲ့ Saving:** Fine-tuned Model ကို သုံးပြီး စမ်းသပ်ပါ။  
Training အတွင်း Checkpoints တွေကို Save လုပ်ထားပြီး နောက်တစ်ခါ အသုံးပြုနိုင်ဖို့ ထိန်းသိမ်းပါ။

**Samples**
- [ဒီ Sample Notebook နဲ့ ပိုမိုလေ့လာပါ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning Sample ဥပမာ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub Fine Tuning with LORA ဥပမာ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub Fine Tuning with QLORA ဥပမာ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

It seems like "mo" might be shorthand for a language or something specific, but it's unclear which language or context you're referring to. Could you clarify what "mo" stands for? For example, is it Maori, Montenegrin, or something else?