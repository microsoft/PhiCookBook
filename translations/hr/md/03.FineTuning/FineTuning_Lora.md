<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:36:24+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "hr"
}
-->
# **Fino podešavanje Phi-3 s Lora**

Fino podešavanje Microsoftovog jezičnog modela Phi-3 Mini koristeći [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na prilagođenom skupu podataka za chat upute.

LORA pomaže u poboljšanju razumijevanja razgovora i generiranju odgovora.

## Korak-po-korak vodič za fino podešavanje Phi-3 Mini:

**Uvoz i postavljanje**

Instalacija loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Započnite uvozom potrebnih biblioteka kao što su datasets, transformers, peft, trl i torch.  
Postavite logiranje za praćenje procesa treniranja.

Možete odabrati prilagodbu nekih slojeva zamjenom njihovih verzija implementiranih u loralib. Trenutno podržavamo samo nn.Linear, nn.Embedding i nn.Conv2d. Također podržavamo MergedLinear za slučajeve kada jedan nn.Linear predstavlja više slojeva, kao što je u nekim implementacijama projekcije qkv pažnje (pogledajte Dodatne napomene za više informacija).

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

Prije početka petlje treniranja, označite samo LoRA parametre kao trenabilne.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Prilikom spremanja checkpointa, generirajte state_dict koji sadrži samo LoRA parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Prilikom učitavanja checkpointa koristeći load_state_dict, obavezno postavite strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sada treniranje može teći kao i obično.

**Hiperparametri**

Definirajte dva rječnika: training_config i peft_config. training_config sadrži hiperparametre za treniranje, poput stope učenja, veličine batcha i postavki logiranja.

peft_config specificira LoRA povezane parametre kao što su rank, dropout i tip zadatka.

**Učitavanje modela i tokenizatora**

Navedite put do prethodno treniranog Phi-3 modela (npr. "microsoft/Phi-3-mini-4k-instruct"). Konfigurirajte postavke modela, uključujući korištenje cachea, tip podataka (bfloat16 za miješanu preciznost) i implementaciju pažnje.

**Treniranje**

Fino podesite Phi-3 model koristeći prilagođeni skup podataka za chat upute. Iskoristite LoRA postavke iz peft_config za učinkovitu prilagodbu. Pratite napredak treniranja koristeći zadanu strategiju logiranja.  
Evaluacija i spremanje: Procijenite fino podešeni model.  
Spremite checkpointove tijekom treniranja za kasniju upotrebu.

**Primjeri**  
- [Saznajte više s ovim primjerom bilježnice](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Primjer Python skripte za fino podešavanje](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Primjer fino podešavanja na Hugging Face Hubu s LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Primjer Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Primjer fino podešavanja na Hugging Face Hubu s QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.