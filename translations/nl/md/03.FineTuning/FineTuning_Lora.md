<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:33:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "nl"
}
-->
# **Fine-tunen van Phi-3 met Lora**

Fine-tunen van Microsoft’s Phi-3 Mini taalmodel met behulp van [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) op een aangepaste chatinstructiedataset.

LORA helpt bij het verbeteren van het begrip in gesprekken en het genereren van reacties.

## Stapsgewijze handleiding voor het fine-tunen van Phi-3 Mini:

**Imports en Setup**

Installeren van loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Begin met het importeren van de benodigde libraries zoals datasets, transformers, peft, trl en torch.  
Stel logging in om het trainingsproces te volgen.

Je kunt ervoor kiezen om sommige lagen aan te passen door ze te vervangen door versies die in loralib zijn geïmplementeerd. We ondersteunen momenteel alleen nn.Linear, nn.Embedding en nn.Conv2d. Daarnaast ondersteunen we ook een MergedLinear voor gevallen waarin één enkele nn.Linear meerdere lagen vertegenwoordigt, zoals bij sommige implementaties van de attention qkv-projectie (zie Extra Notities voor meer informatie).

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

Voordat de trainingslus begint, markeer je alleen de LoRA-parameters als trainbaar.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Bij het opslaan van een checkpoint, genereer je een state_dict die alleen de LoRA-parameters bevat.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Bij het laden van een checkpoint met load_state_dict, zorg ervoor dat strict=False is ingesteld.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nu kan de training zoals gebruikelijk worden voortgezet.

**Hyperparameters**

Definieer twee dictionaries: training_config en peft_config. training_config bevat hyperparameters voor de training, zoals learning rate, batchgrootte en logging-instellingen.

peft_config specificeert LoRA-gerelateerde parameters zoals rank, dropout en taaktype.

**Model en Tokenizer Laden**

Geef het pad op naar het voorgetrainde Phi-3 model (bijv. "microsoft/Phi-3-mini-4k-instruct"). Configureer modelinstellingen, waaronder cachegebruik, datatype (bfloat16 voor mixed precision) en implementatie van attention.

**Training**

Fine-tune het Phi-3 model met de aangepaste chatinstructiedataset. Maak gebruik van de LoRA-instellingen uit peft_config voor efficiënte aanpassing. Houd de voortgang van de training in de gaten met de opgegeven loggingstrategie.  
Evaluatie en Opslaan: Evalueer het gefinetunede model.  
Sla checkpoints op tijdens de training voor later gebruik.

**Voorbeelden**  
- [Leer meer met dit voorbeeldnotebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Voorbeeld van Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Voorbeeld van Hugging Face Hub Fine Tuning met LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Voorbeeld Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Voorbeeld van Hugging Face Hub Fine Tuning met QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.