# **Phi-3 peenhäälestamine Lora abil**

Microsofti keelemudeli Phi-3 Mini peenhäälestamine [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) abil, kasutades kohandatud vestlusjuhiste andmekogumit.

LoRA aitab parandada vestluste mõistmist ja vastuste genereerimist.

## Samm-sammuline juhend Phi-3 Mini peenhäälestamiseks:

**Impordid ja seadistamine**

Loralib installimine

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Alustage vajalike teekide importimisega, nagu datasets, transformers, peft, trl ja torch. Seadistage logimine, et jälgida treenimisprotsessi.

Võite valida, et kohandate mõningaid kihte, asendades need loralibis rakendatud vastetega. Praegu toetame ainult nn.Linear, nn.Embedding ja nn.Conv2d. Samuti toetame MergedLinear-i juhtudel, kus üks nn.Linear esindab rohkem kui ühte kihti, näiteks mõnes tähelepanu qkv projektsiooni rakenduses (vt täiendavaid märkusi).

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

Enne treenimistsükli algust märkige ainult LoRA parameetrid treenitavaks.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Kontrollpunkti salvestamisel looge state_dict, mis sisaldab ainult LoRA parameetreid.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Kontrollpunkti laadimisel load_state_dict abil seadke kindlasti strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nüüd saab treenimist jätkata tavapäraselt.

**Hüperparameetrid**

Määratlege kaks sõnastikku: training_config ja peft_config. training_config sisaldab treenimise hüperparameetreid, nagu õppemäär, partii suurus ja logimise seaded.

peft_config määratleb LoRA-ga seotud parameetrid, nagu rank, dropout ja ülesande tüüp.

**Mudeli ja tokeniseerija laadimine**

Määrake eeltreenitud Phi-3 mudeli asukoht (nt "microsoft/Phi-3-mini-4k-instruct"). Konfigureerige mudeli seaded, sealhulgas vahemälu kasutamine, andmetüüp (bfloat16 segatäpsuse jaoks) ja tähelepanu rakendamine.

**Treening**

Peenhäälestage Phi-3 mudel, kasutades kohandatud vestlusjuhiste andmekogumit. Kasutage peft_config-i LoRA seadeid tõhusaks kohandamiseks. Jälgige treenimisprotsessi määratud logimisstrateegia abil.
Hindamine ja salvestamine: Hinnake peenhäälestatud mudelit.
Salvestage treenimise ajal kontrollpunkte hilisemaks kasutamiseks.

**Näited**
- [Lisateave selle näidisnotebooki abil](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Näide Pythonis peenhäälestamise skriptist](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Näide Hugging Face Hubi peenhäälestamisest LORA abil](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Näide Hugging Face mudelikaardist - LORA peenhäälestamise näidis](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Näide Hugging Face Hubi peenhäälestamisest QLORA abil](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.