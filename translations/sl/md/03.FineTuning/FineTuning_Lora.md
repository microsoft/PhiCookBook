<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:36:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "sl"
}
-->
# **Natančno prilagajanje Phi-3 z Loro**

Natančno prilagajanje Microsoftovega jezikovnega modela Phi-3 Mini z uporabo [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na prilagojenem naboru navodil za klepet.

LORA bo pomagala izboljšati razumevanje pogovora in generiranje odgovorov.

## Korak za korakom vodič za natančno prilagajanje Phi-3 Mini:

**Uvozi in nastavitev**

Namestitev loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Začnite z uvozom potrebnih knjižnic, kot so datasets, transformers, peft, trl in torch.  
Nastavite beleženje za spremljanje procesa učenja.

Lahko se odločite, da prilagodite nekatere plasti tako, da jih zamenjate s tistimi, ki so implementirane v loralib. Trenutno podpiramo samo nn.Linear, nn.Embedding in nn.Conv2d. Prav tako podpiramo MergedLinear za primere, kjer ena sama nn.Linear predstavlja več plasti, kot je v nekaterih implementacijah projekcije pozornosti qkv (glejte dodatne opombe za več).

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

Pri nalaganju kontrolne točke z uporabo load_state_dict poskrbite, da bo strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Zdaj lahko učenje poteka kot običajno.

**Hiperparametri**

Določite dva slovarja: training_config in peft_config. training_config vsebuje hiperparametre za učenje, kot so hitrost učenja, velikost serije in nastavitve beleženja.

peft_config določa parametre, povezane z LoRA, kot so rang, dropout in tip naloge.

**Nalaganje modela in tokenizatorja**

Določite pot do vnaprej naučenega modela Phi-3 (npr. "microsoft/Phi-3-mini-4k-instruct"). Konfigurirajte nastavitve modela, vključno z uporabo predpomnilnika, tipom podatkov (bfloat16 za mešano natančnost) in implementacijo pozornosti.

**Učenje**

Natančno prilagodite model Phi-3 z uporabo prilagojenega nabora navodil za klepet. Uporabite nastavitve LoRA iz peft_config za učinkovito prilagoditev. Spremljajte napredek učenja z izbrano strategijo beleženja.  
Evalvacija in shranjevanje: Ocenite natančno prilagojen model.  
Med učenjem shranjujte kontrolne točke za kasnejšo uporabo.

**Primeri**
- [Več o tem v tem vzorčnem zvezku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python skripte za natančno prilagajanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primer natančnega prilagajanja z LORA na Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primer modelne kartice Hugging Face - vzorec natančnega prilagajanja z LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Primer natančnega prilagajanja z QLORA na Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.