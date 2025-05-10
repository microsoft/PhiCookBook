<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:46:09+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "sv"
}
-->
# **Finjustering av Phi-3 med Lora**

Finjustering av Microsofts språkmodell Phi-3 Mini med hjälp av [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) på en anpassad chattinstruktionsdataset.

LORA hjälper till att förbättra förståelsen i konversationer och generering av svar.

## Steg-för-steg-guide för hur man finjusterar Phi-3 Mini:

**Import och installation**

Installera loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Börja med att importera nödvändiga bibliotek som datasets, transformers, peft, trl och torch.  
Sätt upp loggning för att följa träningsprocessen.

Du kan välja att anpassa vissa lager genom att ersätta dem med motsvarigheter implementerade i loralib. Vi stödjer för närvarande endast nn.Linear, nn.Embedding och nn.Conv2d. Vi stödjer också MergedLinear för fall där ett enda nn.Linear representerar flera lager, som i vissa implementationer av attention qkv-projektionen (se Ytterligare anteckningar för mer information).

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

Innan träningsloopen startar, markera endast LoRA-parametrar som träningsbara.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

När du sparar en checkpoint, skapa en state_dict som endast innehåller LoRA-parametrar.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

När du laddar en checkpoint med load_state_dict, se till att sätta strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nu kan träningen fortsätta som vanligt.

**Hyperparametrar**

Definiera två ordböcker: training_config och peft_config. training_config innehåller hyperparametrar för träningen, som inlärningshastighet, batch-storlek och loggningsinställningar.

peft_config specificerar LoRA-relaterade parametrar som rank, dropout och uppgiftstyp.

**Ladda modell och tokenizer**

Ange sökvägen till den förtränade Phi-3-modellen (t.ex. "microsoft/Phi-3-mini-4k-instruct"). Konfigurera modellinställningar, inklusive cache-användning, datatyp (bfloat16 för mixed precision) och attention-implementation.

**Träning**

Finjustera Phi-3-modellen med den anpassade chattinstruktionsdatan. Använd LoRA-inställningarna från peft_config för effektiv anpassning. Följ träningsförloppet med den angivna loggningsstrategin.  
Utvärdering och sparande: Utvärdera den finjusterade modellen.  
Spara checkpoints under träningen för senare användning.

**Exempel**  
- [Lär dig mer med detta exempel-notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Exempel på Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Exempel på Hugging Face Hub Fine Tuning med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Exempel på Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Exempel på Hugging Face Hub Fine Tuning med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.