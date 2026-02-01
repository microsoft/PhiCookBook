# **Finjustering av Phi-3 med Lora**

Finjustering av Microsofts språkmodell Phi-3 Mini ved hjelp av [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) på et tilpasset chat-instruksjonsdatasett.

LORA vil bidra til å forbedre samtaleforståelse og responsgenerering.

## Trinnvis guide for hvordan du finjusterer Phi-3 Mini:

**Imports og oppsett**

Installere loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Start med å importere nødvendige biblioteker som datasets, transformers, peft, trl og torch.  
Sett opp logging for å følge treningsprosessen.

Du kan velge å tilpasse noen lag ved å erstatte dem med tilsvarende implementert i loralib. Vi støtter foreløpig kun nn.Linear, nn.Embedding og nn.Conv2d. Vi støtter også MergedLinear for tilfeller der en enkelt nn.Linear representerer mer enn ett lag, slik som i noen implementasjoner av attention qkv-projeksjonen (se Tilleggsnotater for mer informasjon).

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

Før treningsløkken starter, merk kun LoRA-parametere som trenbare.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Når du lagrer et sjekkpunkt, generer en state_dict som kun inneholder LoRA-parametere.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Når du laster et sjekkpunkt med load_state_dict, sørg for å sette strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nå kan treningen fortsette som vanlig.

**Hyperparametere**

Definer to ordbøker: training_config og peft_config. training_config inneholder hyperparametere for trening, som læringsrate, batch-størrelse og loggingsinnstillinger.

peft_config spesifiserer LoRA-relaterte parametere som rank, dropout og oppgavetype.

**Modell- og tokenizerlasting**

Spesifiser stien til den forhåndstrente Phi-3-modellen (f.eks. "microsoft/Phi-3-mini-4k-instruct"). Konfigurer modellinnstillinger, inkludert cache-bruk, datatype (bfloat16 for mixed precision) og implementasjon av attention.

**Trening**

Finjuster Phi-3-modellen ved hjelp av det tilpassede chat-instruksjonsdatasettet. Bruk LoRA-innstillingene fra peft_config for effektiv tilpasning. Overvåk treningsfremdriften med den angitte loggestrategien.  
Evaluering og lagring: Evaluer den finjusterte modellen.  
Lagre sjekkpunkter under trening for senere bruk.

**Eksempler**
- [Lær mer med denne eksempelnotatboken](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Eksempel på Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Eksempel på Hugging Face Hub Fine Tuning med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Eksempel på Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Eksempel på Hugging Face Hub Fine Tuning med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.