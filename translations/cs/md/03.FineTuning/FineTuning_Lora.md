<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:35:20+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "cs"
}
-->
# **Doladění Phi-3 pomocí Lora**

Doladění jazykového modelu Phi-3 Mini od Microsoftu pomocí [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na vlastním datasetu s chatovacími instrukcemi.

LORA pomůže zlepšit porozumění konverzaci a generování odpovědí.

## Podrobný návod, jak doladit Phi-3 Mini:

**Importy a nastavení**

Instalace loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Nejprve naimportujte potřebné knihovny jako datasets, transformers, peft, trl a torch.  
Nastavte logování pro sledování průběhu tréninku.

Můžete se rozhodnout upravit některé vrstvy nahrazením jejich implementací z loralib. Momentálně podporujeme pouze nn.Linear, nn.Embedding a nn.Conv2d. Také podporujeme MergedLinear pro případy, kdy jedna nn.Linear vrstva reprezentuje více vrstev, například v některých implementacích projekce qkv v attention (viz Dodatečné poznámky).

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

Před začátkem tréninkové smyčky označte jako trénovatelné pouze LoRA parametry.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Při ukládání checkpointu vytvořte state_dict, který bude obsahovat pouze LoRA parametry.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Při načítání checkpointu pomocí load_state_dict nezapomeňte nastavit strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nyní může trénink probíhat jako obvykle.

**Hyperparametry**

Definujte dva slovníky: training_config a peft_config. training_config obsahuje hyperparametry tréninku, jako je learning rate, velikost batch a nastavení logování.

peft_config specifikuje parametry související s LoRA, například rank, dropout a typ úkolu.

**Načtení modelu a tokenizeru**

Uveďte cestu k předtrénovanému modelu Phi-3 (např. "microsoft/Phi-3-mini-4k-instruct"). Nakonfigurujte nastavení modelu, včetně použití cache, datového typu (bfloat16 pro smíšenou přesnost) a implementace attention.

**Trénink**

Doladění modelu Phi-3 pomocí vlastního datasetu s chatovacími instrukcemi. Využijte LoRA nastavení z peft_config pro efektivní adaptaci. Sledujte průběh tréninku pomocí zvolené strategie logování.  
Vyhodnocení a ukládání: Vyhodnoťte doladěný model.  
Ukládejte checkpointy během tréninku pro pozdější použití.

**Ukázky**
- [Více informací v tomto ukázkovém notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Příklad Python skriptu pro doladění](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Příklad doladění na Hugging Face Hub pomocí LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Příklad Hugging Face Model Card - ukázka doladění LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Příklad doladění na Hugging Face Hub pomocí QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.