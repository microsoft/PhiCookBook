<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:48:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "sr"
}
-->
# **Fino podešavanje Phi-3 sa Lora**

Fino podešavanje Microsoftovog Phi-3 Mini jezičkog modela korišćenjem [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na prilagođenom skupu podataka za instrukcije za ćaskanje.

LORA pomaže u poboljšanju razumevanja konverzacije i generisanja odgovora.

## Korak po korak vodič za fino podešavanje Phi-3 Mini:

**Uvozi i podešavanje**

Instalacija loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Počni uvozom neophodnih biblioteka kao što su datasets, transformers, peft, trl i torch.  
Podesi logovanje za praćenje procesa treniranja.

Možeš izabrati da prilagodiš neke slojeve zamenjujući ih verzijama iz loralib. Za sada podržavamo samo nn.Linear, nn.Embedding i nn.Conv2d. Takođe podržavamo MergedLinear za slučajeve kada jedan nn.Linear predstavlja više slojeva, kao što je u nekim implementacijama qkv projekcije pažnje (pogledaj Dodatne napomene za više detalja).

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

Pre nego što počne petlja za treniranje, označi samo LoRA parametre kao trenabilne.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Kada se čuva checkpoint, generiši state_dict koji sadrži samo LoRA parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Kada se učitava checkpoint pomoću load_state_dict, obavezno postavi strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sada treniranje može da se nastavi kao i obično.

**Hiparametri**

Definiši dva rečnika: training_config i peft_config. training_config sadrži hiparampetre za treniranje, kao što su stopa učenja, veličina batch-a i podešavanja za logovanje.

peft_config definiše LoRA povezane parametre poput ranga, dropout-a i tipa zadatka.

**Učitavanje modela i tokenizatora**

Navedi putanju do prethodno treniranog Phi-3 modela (npr. "microsoft/Phi-3-mini-4k-instruct"). Konfiguriši podešavanja modela, uključujući korišćenje keša, tip podataka (bfloat16 za mešanu preciznost) i implementaciju pažnje.

**Trening**

Fino podešavanje Phi-3 modela koristeći prilagođeni skup instrukcija za ćaskanje. Iskoristi LoRA podešavanja iz peft_config za efikasnu adaptaciju. Prati napredak treniranja pomoću specificirane strategije logovanja.  
Evaluacija i čuvanje: Proceni fino podešeni model.  
Čuvaj checkpoint-e tokom treniranja za kasniju upotrebu.

**Primeri**
- [Saznaj više sa ovim primerom notebook-a](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Primer Python skripte za fino podešavanje](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Primer fino podešavanja na Hugging Face Hub-u sa LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Primer Hugging Face Model Card - LORA Fine Tuning primer](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Primer fino podešavanja na Hugging Face Hub-u sa QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.