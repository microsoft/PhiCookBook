<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:48:48+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "sl"
}
-->
# **Fine-tuning Phi-3 with Lora**

Fine-tuning Microsoft's Phi-3 Mini jezikovni model z uporabo [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na prilagojenem naboru podatkov za navodila v klepetu.

LORA bo pomagala izboljšati razumevanje pogovora in generiranje odgovorov.

## Korak za korakom vodič, kako fino nastaviti Phi-3 Mini:

**Uvozi in nastavitev**

Namestitev loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Najprej uvozite potrebne knjižnice, kot so datasets, transformers, peft, trl in torch.  
Nastavite beleženje za spremljanje procesa učenja.

Lahko izberete, da prilagodite nekatere plasti tako, da jih nadomestite s tistimi, ki jih izvaja loralib. Trenutno podpiramo nn.Linear, nn.Embedding in nn.Conv2d. Podpiramo tudi MergedLinear za primere, kjer ena sama nn.Linear predstavlja več plasti, kot je to v nekaterih izvedbah projekcije qkv pozornosti (glejte Dodatne opombe za več).

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

Pred začetkom učne zanke označite kot trenirljive samo LoRA parametre.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Pri shranjevanju kontrolne točke ustvarite state_dict, ki vsebuje samo LoRA parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Pri nalaganju kontrolne točke z load_state_dict poskrbite, da je strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Zdaj se lahko učenje nadaljuje kot običajno.

**Hiperparametri**

Določite dva slovarja: training_config in peft_config. training_config vsebuje hiperparametre za učenje, kot so hitrost učenja, velikost serije in nastavitve beleženja.

peft_config določa parametre povezane z LoRA, kot so rank, dropout in tip naloge.

**Nalaganje modela in tokenizerja**

Določite pot do predhodno naučenega modela Phi-3 (npr. "microsoft/Phi-3-mini-4k-instruct"). Konfigurirajte nastavitve modela, vključno z uporabo predpomnilnika, tipom podatkov (bfloat16 za mešano natančnost) in implementacijo pozornosti.

**Učenje**

Fino nastavite model Phi-3 z uporabo prilagojenega nabora podatkov za navodila v klepetu. Uporabite LoRA nastavitve iz peft_config za učinkovito prilagoditev. Spremljajte napredek učenja z določenim načinom beleženja.  
Evaluacija in shranjevanje: ocenite fino nastavljeni model.  
Shranjujte kontrolne točke med učenjem za kasnejšo uporabo.

**Primeri**
- [Več informacij s tem vzorčnim zvezkom](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Primer Python FineTuning vzorca](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Primer Fine Tuning na Hugging Face Hub z LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Primer model kartice na Hugging Face - LORA Fine Tuning vzorec](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Primer Fine Tuning na Hugging Face Hub z QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.