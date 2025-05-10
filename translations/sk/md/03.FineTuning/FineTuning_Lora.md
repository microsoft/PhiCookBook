<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:48:02+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "sk"
}
-->
# **Doladenie Phi-3 pomocou Lora**

Doladenie modelu jazyka Phi-3 Mini od Microsoftu pomocou [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na vlastnej dátovej sade s inštrukciami pre chat.

LORA pomáha zlepšiť pochopenie konverzácie a generovanie odpovedí.

## Podrobný návod, ako doladiť Phi-3 Mini:

**Importy a nastavenie**

Inštalácia loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Najskôr importujte potrebné knižnice ako datasets, transformers, peft, trl a torch.  
Nastavte logovanie na sledovanie priebehu trénovania.

Môžete si zvoliť adaptáciu niektorých vrstiev ich nahradením implementáciami z loralib. Momentálne podporujeme nn.Linear, nn.Embedding a nn.Conv2d. Tiež podporujeme MergedLinear pre prípady, keď jedna nn.Linear reprezentuje viac vrstiev, napríklad pri projekcii qkv v attention (viď Dodatočné poznámky pre viac informácií).

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

Pred začiatkom trénovacej slučky označte ako trénovateľné iba LoRA parametre.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Pri ukladaní checkpointu vytvorte state_dict, ktorý obsahuje len LoRA parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Pri načítaní checkpointu pomocou load_state_dict nastavte strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Teraz môže trénovanie prebiehať štandardným spôsobom.

**Hyperparametre**

Definujte dva slovníky: training_config a peft_config. training_config obsahuje hyperparametre trénovania, ako sú learning rate, veľkosť batchu a nastavenia logovania.

peft_config špecifikuje parametre súvisiace s LoRA, napríklad rank, dropout a typ úlohy.

**Načítanie modelu a tokenizéra**

Zadajte cestu k predtrénovanému modelu Phi-3 (napr. "microsoft/Phi-3-mini-4k-instruct"). Nakonfigurujte nastavenia modelu vrátane použitia cache, dátového typu (bfloat16 pre zmiešanú presnosť) a implementácie attention.

**Trénovanie**

Doladte model Phi-3 pomocou vlastnej dátovej sady s inštrukciami pre chat. Využite LoRA nastavenia z peft_config pre efektívnu adaptáciu. Sledujte priebeh trénovania podľa zvolenej stratégie logovania.  
Vyhodnotenie a ukladanie: Vyhodnoťte doladený model.  
Ukladajte checkpointy počas trénovania pre neskoršie použitie.

**Ukážky**
- [Viac informácií v tomto ukážkovom notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Príklad Python skriptu na doladenie](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Príklad doladenia pomocou Hugging Face Hub a LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Príklad Hugging Face Model Card - LORA doladenie](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Príklad doladenia pomocou Hugging Face Hub a QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.