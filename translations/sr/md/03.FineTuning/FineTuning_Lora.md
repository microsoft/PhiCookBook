<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:36:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "sr"
}
-->
# **Фајн-тјунинг Phi-3 помоћу Lora**

Фајн-тјунинг Microsoft-овог Phi-3 Mini језичког модела користећи [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) на прилагођеном скупу упутстава за ћаскање.

LORA ће помоћи у побољшању разумевања разговора и генерисања одговора.

## Корак по корак водич како фајн-тјунирати Phi-3 Mini:

**Увоз и подешавање**

Инсталирање loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Почните увозом потребних библиотека као што су datasets, transformers, peft, trl и torch.  
Подесите логовање како бисте пратили процес тренинга.

Можете изабрати да прилагодите неке слојеве заменом њихових имплементација оним из loralib. Тренутно подржавамо само nn.Linear, nn.Embedding и nn.Conv2d. Такође подржавамо MergedLinear за случајеве када један nn.Linear представља више слојева, као што је у неким имплементацијама пројекције qkv у attention-у (погледајте Додатне напомене за више детаља).

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

Пре почетка тренинг петље, означите само LoRA параметре као оне који се могу тренирати.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Када чувате чекпоинт, генеришите state_dict који садржи само LoRA параметре.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Када учитавате чекпоинт користећи load_state_dict, обавезно подесите strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Сада тренинг може да се настави као и обично.

**Хиперпараметри**

Дефинишите два речника: training_config и peft_config. training_config садржи хиперпараметре за тренинг, као што су learning rate, batch size и подешавања логовања.

peft_config одређује LoRA параметре као што су rank, dropout и тип задатка.

**Учитавање модела и токенизера**

Назначите путању до претходно обученог Phi-3 модела (нпр. "microsoft/Phi-3-mini-4k-instruct"). Конфигуришите подешавања модела, укључујући коришћење кеша, тип података (bfloat16 за мешовиту прецизност) и имплементацију attention-а.

**Тренинг**

Фајн-тјунирајте Phi-3 модел користећи прилагођени скуп упутстава за ћаскање. Искористите LoRA подешавања из peft_config за ефикасну адаптацију. Пратите напредак тренинга користећи назначену стратегију логовања.  
Евалуација и чување: Процените фајн-тјунирани модел.  
Чувајте чекпоинтове током тренинга за каснију употребу.

**Примери**  
- [Сазнајте више уз овај пример notebook-а](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Пример Python скрипте за фајн-тјунинг](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Пример фајн-тјунинга на Hugging Face Hub-у са LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Пример Hugging Face Model Card - LORA фајн-тјунинг пример](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Пример фајн-тјунинга на Hugging Face Hub-у са QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.