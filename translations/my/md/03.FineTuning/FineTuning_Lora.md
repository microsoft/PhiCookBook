<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:36:47+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "my"
}
-->
# **Lora ဖြင့် Phi-3 ကို အတိအကျ ပြင်ဆင်ခြင်း**

Microsoft ၏ Phi-3 Mini ဘာသာစကားမော်ဒယ်ကို [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) အသုံးပြု၍ ကိုယ်ပိုင် စကားပြောညွှန်ကြားချက် ဒေတာစုံအပေါ် အတိအကျ ပြင်ဆင်ခြင်း။

LORA သည် စကားပြောနားလည်မှုနှင့် တုံ့ပြန်မှု ဖန်တီးမှုကို တိုးတက်စေပါသည်။

## Phi-3 Mini ကို အတိအကျ ပြင်ဆင်ရန် အဆင့်လိုက် လမ်းညွှန်ချက်

**Imports နှင့် စတင်ပြင်ဆင်ခြင်း**

loralib ကို ထည့်သွင်းခြင်း

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl, torch ကဲ့သို့ လိုအပ်သော 라이ဘရယ်များကို import ပြုလုပ်ပါ။
လေ့ကျင့်မှု လုပ်ငန်းစဉ်ကို မှတ်တမ်းတင်ရန် logging ကို စတင်ပြင်ဆင်ပါ။

loralib တွင် ရှိသော counterparts များဖြင့် အချို့သော အလွှာများကို ပြောင်းလဲအသုံးပြုနိုင်သည်။ ယခုအချိန်တွင် nn.Linear, nn.Embedding, nn.Conv2d များကိုသာ ထောက်ပံ့ပေးပါသည်။ attention qkv projection ၏ အချို့ အကောင်အထည်ဖော်မှုများတွင် nn.Linear တစ်ခုသည် အလွှာများစွာကို ကိုယ်စားပြုသောအခါ MergedLinear ကိုလည်း ထောက်ပံ့ပေးပါသည် (အသေးစိတ် မှတ်ချက်များကို ကြည့်ပါ)။

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

လေ့ကျင့်မှု loop စတင်မီ LoRA ပါရာမီတာများကိုသာ သင်ကြားနိုင်အောင် သတ်မှတ်ပါ။

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

checkpoint သိမ်းဆည်းရာတွင် LoRA ပါရာမီတာများသာ ပါဝင်သော state_dict ကို ဖန်တီးပါ။

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ဖြင့် checkpoint ကို load လုပ်ရာတွင် strict=False ဟု သတ်မှတ်ရန် သတိပြုပါ။

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ယခုလေ့ကျင့်မှုကို ပုံမှန်အတိုင်း ဆက်လက်လုပ်ဆောင်နိုင်ပါပြီ။

**Hyperparameters**

training_config နှင့် peft_config ဆိုသော dictionary နှစ်ခုကို သတ်မှတ်ပါ။ training_config တွင် သင်ကြားမှုအတွက် learning rate, batch size, logging စသည့် hyperparameter များ ပါဝင်သည်။

peft_config တွင် LoRA နှင့်ဆက်စပ်သော rank, dropout, task type စသည့် ပါရာမီတာများ ပါဝင်သည်။

**Model နှင့် Tokenizer ကို Load ပြုလုပ်ခြင်း**

pre-trained Phi-3 မော်ဒယ် (ဥပမာ - "microsoft/Phi-3-mini-4k-instruct") ၏ လမ်းကြောင်းကို သတ်မှတ်ပါ။ မော်ဒယ်ဆက်တင်များတွင် cache အသုံးပြုမှု၊ data type (mixed precision အတွက် bfloat16) နှင့် attention အကောင်အထည်ဖော်မှုများကို ပြင်ဆင်ပါ။

**Training**

ကိုယ်ပိုင် စကားပြောညွှန်ကြားချက် ဒေတာစုံဖြင့် Phi-3 မော်ဒယ်ကို အတိအကျ ပြင်ဆင်ပါ။ peft_config မှ LoRA ဆက်တင်များကို အသုံးပြု၍ ထိရောက်စွာ ပြင်ဆင်နိုင်ပါသည်။ သတ်မှတ်ထားသော logging နည်းလမ်းဖြင့် လေ့ကျင့်မှု တိုးတက်မှုကို စောင့်ကြည့်ပါ။

**အကဲဖြတ်ခြင်းနှင့် သိမ်းဆည်းခြင်း**  
အတိအကျ ပြင်ဆင်ပြီးသော မော်ဒယ်ကို အကဲဖြတ်ပါ။  
နောက်ပိုင်းအသုံးပြုနိုင်ရန် လေ့ကျင့်မှုအတွင်း checkpoint များကို သိမ်းဆည်းပါ။

**နမူနာများ**  
- [ဒီနမူနာ notebook ဖြင့် ပိုမိုလေ့လာရန်](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python FineTuning နမူနာ](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub တွင် LORA ဖြင့် Fine Tuning နမူနာ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face Model Card - LORA Fine Tuning နမူနာ](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub တွင် QLORA ဖြင့် Fine Tuning နမူနာ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။