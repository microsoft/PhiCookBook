<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-12-21T18:06:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ml"
}
-->
# **Phi-3 Lora ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്**

Microsoft-ന്റെ Phi-3 Mini ഭാഷാ മോഡൽ ഒരു കസ്റ്റം ചാറ്റ് നിർദ്ദേശ ഡാറ്റാസെറ്റിൽ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ഉപയോഗിച്ച് ഫൈൻ-ട്യൂൺ ചെയ്യുന്നത്.

LoRA സംവാദത്തിന്റെ മനസിലാക്കലും പ്രതികരണ നിർമ്മാണവും മെച്ചപ്പെടുത്താൻ സഹായിക്കും.

## Phi-3 Mini ഫൈൻ-ട്യൂൺ ചെയ്യാൻ ഘട്ടംപ്രതി മാർഗ്ഗനിർദേശം:

**ഇംപോർട്ടുകളും ക്രമീകരണവും** 

Installing loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets, transformers, peft, trl, torch പോലുള്ള ആവശ്യമായ ലൈബ്രററികൾ import ചെയ്യുന്നതോടെ ആരംഭിക്കുക.
ട്രെയിനിംഗ് പ്രക്രിയ ട്രാക്ക് ചെയ്യാൻ ലോഗിംഗ് ക്രമീകരിക്കുക.

നിങ്ങൾക്ക് ചില ലെയറുകൾ loralib-ൽ നടപ്പാക്കിയ സഹപങ്കാളികളാൽ പകരംവെച്ച് അനുയോജ്യമായി മാറ്റാൻ തിരഞ്ഞെടുക്കാം. നിലവിൽ ഞങ്ങൾ പിന്തുണയ്ക്കുന്നത് nn.Linear, nn.Embedding, nn.Conv2d എന്നിവ മാത്രമാണ്. ഒരൊറ്റ nn.Linear ഒന്നിലധികം ലെയറുകളെ പ്രതിനിധീകരിക്കുന്ന കേസുകളിലായി (ഉദാ., ചില attention qkv projection നടപ്പുകളിൽ) ഞങ്ങൾ ഒരു MergedLinear-ഉം പിന്തുണയ്ക്കുന്നു (കൂടുതൽ വിവരങ്ങൾക്ക് Additional Notes കാണുക).

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

ട്രെയിനിംഗ് ലൂപ്പ് തുടങ്ങുന്നതിന് മുമ്പ്, മാത്രം LoRA പാരാമീറ്ററുകൾ പരിശീലനയോഗ്യമാക്കി അടയാൾപ്പെടുത്തുക.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

ചෙක්പോയിന്റ് സേവ് ചെയ്യുമ്പോൾ, മാത്രം LoRA പാരാമീറ്ററുകൾ ഉൾക്കൊള്ളുന്ന ഒരു state_dict രൂപപ്പെടുത്തുക.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ഉപയോഗിച്ച് ചെക്ക്‌പോയിന്റ് ലോഡ് ചെയ്യുമ്പോൾ, strict=False സെറ്റ് ചെയ്യാൻ ശ്രദ്ധിക്കുക.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ഇപ്പോൾ പരിശീലനം സാധാരണപ്രകാരം തുടരാം.

**ഹൈപ്പർപാരാമെടറുകൾ** 

രണ്ട് ഡിക്ഷണറികൾ നിർവചിക്കുക: training_config and peft_config. training_config-ൽ learning rate, batch size, logging സെറ്റിംഗുകൾ എന്നിവയൊക്കെയുള്ള പരിശീലനത്തിന് അനുയോജ്യമായ ഹൈപ്പർപാരാമെടറുകൾ ഉൾക്കൊള്ളുന്നു.

peft_config LoRA-ബന്ധമായ പാരാമീറ്ററുകൾ (ഉദാ., rank, dropout, task type) വ്യക്തമാക്കുന്നു.

**മോഡൽ 및 ടോക്കനൈസർ ലോഡിംഗ്** 

പ്രീ-ട്രെയിൻ ചെയ്ത Phi-3 മോഡലിന്റെ പാത്ത് വ്യക്തമാക്കുക (ഉദാ., "microsoft/Phi-3-mini-4k-instruct"). കാഷെ ഉപയോഗം, ഡാറ്റാ ടൈപ്പ് (മിക്‌സഡ് പ്രിസിഷനിനായി bfloat16), attention നടപ്പാക്കൽ എന്നിവ ഉൾപ്പെടെ മോഡൽ ക്രമീകരണങ്ങൾ ക്രമീകരിക്കുക.

**പരിശീലനം** 

കസ്റ്റം ചാറ്റ് നിർദ്ദേശ ഡാറ്റാസെറ്റ് ഉപയോഗിച്ച് Phi-3 മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യുക. കാര്യക്ഷമമായ അഡാപ്റ്റേഷനിനായി peft_config-ലെ LoRA സെറ്റിങ്ങുകൾ ഉപയോഗിക്കുക. നിർദേശിച്ച ലോഗിംഗ് തന്ത്രം ഉപയോഗിച്ച് പരിശീലന പുരോഗതി നിരീക്ഷിക്കുക.
മൂല്യനിർണ്ണയവും സംരക്ഷണവും: ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ മൂല്യനിർണ്ണയിക്കുക.
പരിശീലനത്തിനിടെ പിന്നീട് ഉപയോഗിക്കാനായി ചെക്‌പോയിന്റുകൾ സേവ് ചെയ്യുക.

**സാമ്പിളുകൾ**
- [ഈ സാമ്പിൾ നോട്ട്ബുക്ക് ഉപയോഗിച്ച് കൂടുതൽ അറിയുക](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ഫൈൻട്യൂണിംഗ് ഉദാഹരണം](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LoRA ഉപയോഗിച്ച് Hugging Face Hub ഫൈൻ-ട്യൂണിംഗ് ഉദാഹരണം](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Card ഉദാഹരണം - LoRA ഫൈൻ-ട്യൂണിംഗ് സാമ്പിൾ](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA ഉപയോഗിച്ച് Hugging Face Hub ഫൈൻ-ട്യൂണിംഗ് ഉദാഹരണം](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ ഡോക്യുമെന്റ് AI പരിഭാഷണ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിച്ചിരുന്നിട്ടും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ അശുദ്ധതകൾ ഉണ്ടായേക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. സ്വദേശഭാഷയിലെ യഥാർത്ഥ രേഖയെ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കുക. പ്രാധാന്യമുള്ള വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യപരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷയുടെ ഉപയോഗത്തെത്തുടർന്നുള്ള ഏതൊരു തെറ്റിദ്ധാരണക്കോ വ്യാഖ്യാനദोषത്തിനോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->