<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:47:32+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "sw"
}
-->
# **Kufinywa kwa Phi-3 kwa kutumia Lora**

Kufinywa kwa mfano wa lugha wa Phi-3 Mini wa Microsoft kwa kutumia [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) kwenye seti ya maelekezo ya mazungumzo iliyobinafsishwa.

LORA itasaidia kuboresha uelewa wa mazungumzo na uzalishaji wa majibu.

## Mwongozo hatua kwa hatua jinsi ya kufinywa Phi-3 Mini:

**Kuagiza na Kuanzisha**

Kusakinisha loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Anza kwa kuagiza maktaba muhimu kama datasets, transformers, peft, trl, na torch. Sanidi ufuatiliaji ili kufuatilia mchakato wa mafunzo.

Unaweza kuchagua kubadilisha baadhi ya tabaka kwa kuzibadilisha na zile zilizotekelezwa katika loralib. Hivi sasa tunasaidia nn.Linear, nn.Embedding, na nn.Conv2d tu. Pia tunasaidia MergedLinear kwa matukio ambapo nn.Linear moja inawakilisha tabaka zaidi ya moja, kama katika baadhi ya utekelezaji wa mradi wa qkv wa umakini (angalia Vidokezo Zaidi kwa maelezo zaidi).

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

Kabla ya mzunguko wa mafunzo kuanza, weka tu vigezo vya LoRA kuwa vinavyoweza kufundishwa.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Unapohifadhi checkpoint, tengeneza state_dict inayojumuisha tu vigezo vya LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Unapopakua checkpoint kwa kutumia load_state_dict, hakikisha umeweka strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sasa mafunzo yanaweza kuendelea kama kawaida.

**Vigezo Vikuu vya Mafunzo**

Taja kamusi mbili: training_config na peft_config. training_config ina vigezo vya mafunzo kama kiwango cha kujifunza, ukubwa wa kundi, na mipangilio ya ufuatiliaji.

peft_config inaeleza vigezo vinavyohusiana na LoRA kama rank, dropout, na aina ya kazi.

**Kupakia Mfano na Tokenizer**

Taja njia ya mfano wa Phi-3 uliopangwa awali (mfano, "microsoft/Phi-3-mini-4k-instruct"). Sanidi mipangilio ya mfano, ikijumuisha matumizi ya cache, aina ya data (bfloat16 kwa usahihi mchanganyiko), na utekelezaji wa umakini.

**Mafunzo**

Finywa mfano wa Phi-3 kwa kutumia seti ya maelekezo ya mazungumzo iliyobinafsishwa. Tumia mipangilio ya LoRA kutoka peft_config kwa ufanisi wa mabadiliko. Fuata maendeleo ya mafunzo kwa kutumia mkakati wa ufuatiliaji uliotajwa.

Tathmini na Kuhifadhi: Tathmini mfano uliobinafsishwa. Hifadhi checkpoint wakati wa mafunzo kwa matumizi ya baadaye.

**Mifano**
- [Jifunze Zaidi na daftari hili la mfano](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Mfano wa FineTuning wa Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Mfano wa Hugging Face Hub Fine Tuning kwa LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Mfano wa Kadi ya Mfano wa Hugging Face - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Mfano wa Hugging Face Hub Fine Tuning kwa QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Kiarifu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatubebei wajibu wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.