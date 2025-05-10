<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:46:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "da"
}
-->
# **Finjustering af Phi-3 med Lora**

Finjustering af Microsofts Phi-3 Mini sprogmodel ved hjælp af [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) på et tilpasset chat-instruktionsdatasæt.

LORA hjælper med at forbedre samtaleforståelse og generering af svar.

## Trin-for-trin guide til, hvordan du finjusterer Phi-3 Mini:

**Imports og opsætning**

Installation af loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Start med at importere nødvendige biblioteker som datasets, transformers, peft, trl og torch.  
Opsæt logging for at følge træningsprocessen.

Du kan vælge at tilpasse nogle lag ved at erstatte dem med versioner implementeret i loralib. Vi understøtter lige nu kun nn.Linear, nn.Embedding og nn.Conv2d. Vi understøtter også MergedLinear til tilfælde, hvor et enkelt nn.Linear repræsenterer flere lag, som i nogle implementeringer af attention qkv-projektionen (se Yderligere Bemærkninger for mere info).

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

Før træningssløjfen starter, markeres kun LoRA-parametre som trænbare.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Når du gemmer et checkpoint, genereres en state_dict, der kun indeholder LoRA-parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Når du loader et checkpoint med load_state_dict, skal strict=False sættes.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nu kan træningen fortsætte som normalt.

**Hyperparametre**

Definer to ordbøger: training_config og peft_config. training_config indeholder hyperparametre til træningen, som læringsrate, batch-størrelse og logging-indstillinger.

peft_config specificerer LoRA-relaterede parametre som rank, dropout og opgavetype.

**Model- og Tokenizer-indlæsning**

Angiv stien til den fortrænede Phi-3 model (f.eks. "microsoft/Phi-3-mini-4k-instruct"). Konfigurer modelindstillinger, herunder cache-brug, datatype (bfloat16 til mixed precision) og attention-implementering.

**Træning**

Finjuster Phi-3 modellen med det tilpassede chat-instruktionsdatasæt. Brug LoRA-indstillingerne fra peft_config for effektiv tilpasning. Overvåg træningsforløbet med den angivne logging-strategi.  
Evaluering og gemning: Evaluer den finjusterede model.  
Gem checkpoints under træningen til senere brug.

**Eksempler**
- [Lær mere med denne eksempel-notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Eksempel på Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Eksempel på Hugging Face Hub Fine Tuning med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Eksempel på Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Eksempel på Hugging Face Hub Fine Tuning med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.