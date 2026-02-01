# **Kurekebisha Phi-3 kwa Lora**

Kurekebisha mfano wa lugha wa Phi-3 Mini wa Microsoft kwa kutumia [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) kwenye seti ya maelekezo ya mazungumzo iliyobinafsishwa.

LORA itasaidia kuboresha uelewa wa mazungumzo na utengenezaji wa majibu.

## Mwongozo wa hatua kwa hatua jinsi ya kurekebisha Phi-3 Mini:

**Kuagiza na Kuandaa**

Kusakinisha loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Anza kwa kuagiza maktaba muhimu kama datasets, transformers, peft, trl, na torch. Weka mfumo wa kufuatilia ili kuangalia mchakato wa mafunzo.

Unaweza kuchagua kubadilisha baadhi ya tabaka kwa kuzibadilisha na zile zilizotekelezwa katika loralib. Kwa sasa tunasaidia nn.Linear, nn.Embedding, na nn.Conv2d tu. Pia tunasaidia MergedLinear kwa matukio ambapo nn.Linear moja inawakilisha tabaka zaidi ya moja, kama katika baadhi ya utekelezaji wa mradi wa umakini wa qkv (angalia Maelezo Zaidi kwa maelezo zaidi).

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

Kabla ya mzunguko wa mafunzo kuanza, weka tu vigezo vya LoRA kama vinavyoweza kufunzwa.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Unapohifadhi alama ya kuangalia (checkpoint), tengeneza state_dict inayojumuisha tu vigezo vya LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Unapopakua alama ya kuangalia kwa kutumia load_state_dict, hakikisha umeweka strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sasa mafunzo yanaweza kuendelea kama kawaida.

**Vigezo Vikuu vya Mafunzo**

Taja kamusi mbili: training_config na peft_config. training_config ina vigezo vya mafunzo kama kiwango cha kujifunza, ukubwa wa kundi, na mipangilio ya kufuatilia.

peft_config inaelezea vigezo vinavyohusiana na LoRA kama rank, dropout, na aina ya kazi.

**Kupakia Mfano na Tokenizer**

Taja njia ya mfano wa Phi-3 uliotanguliwa (mfano, "microsoft/Phi-3-mini-4k-instruct"). Sanidi mipangilio ya mfano, ikiwa ni pamoja na matumizi ya cache, aina ya data (bfloat16 kwa usahihi mchanganyiko), na utekelezaji wa umakini.

**Mafunzo**

Rekebisha mfano wa Phi-3 kwa kutumia seti ya maelekezo ya mazungumzo iliyobinafsishwa. Tumia mipangilio ya LoRA kutoka peft_config kwa ufanisi wa marekebisho. Fuata maendeleo ya mafunzo kwa kutumia mkakati wa kufuatilia uliotajwa.

Tathmini na Kuhifadhi: Tathmini mfano uliorekebishwa. Hifadhi alama za kuangalia wakati wa mafunzo kwa matumizi ya baadaye.

**Mifano**
- [Jifunze Zaidi kwa kutumia daftari hili la mfano](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Mfano wa Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Mfano wa Hugging Face Hub Fine Tuning na LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Mfano wa Kadi ya Mfano wa Hugging Face - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Mfano wa Hugging Face Hub Fine Tuning na QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.