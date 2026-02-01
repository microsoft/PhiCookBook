# Phi-3.5-vision рецепт за фајнтјунинг

Ово је званична подршка за фајнтјунинг Phi-3.5-vision користећи huggingface библиотеке.  
Молимо вас да пре покретања следећих команди уђете у директоријум са кодом [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) помоћу `cd`.

## Инсталација

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Брзи почетак

Пружају се два примерка скрипти за фајнтјунинг, једна за DocVQA и једна за класификацију мрзитељских мема.

Минимални тестирани хардвер: 4x RTX8000 (48GB RAM по GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision сада званично подржава унос више слика. Ево примера за фајнтјунинг NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Упутство за коришћење

У зависности од хардвера, корисници могу изабрати различите стратегије фајнтјунинга. Подржавамо  
потпуни фајнтјунинг (са Deepspeed Zero-2) са опционално замрзнутим параметрима визије, као и LoRA (укључујући 4bit QLoRA).  
Уопштено, препоручујемо коришћење потпуног фајнтјунинга са flash attention и bf16 кад год је могуће.

### Упутство за конверзију вашег прилагођеног скупа података у потребан формат

Користимо минимални скуп података за класификацију видео записа (подскуп UCF-101) као пример од почетка до краја да покажемо како да конвертујете свој прилагођени скуп података у потребан формат и фајнтјунирате Phi-3.5-vision на њему.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Конвертовани подаци ће изгледати овако:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

За `jsonl` анотацију, сваки ред треба да буде речник као:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Имајте у виду да је `conversations` листа, па је могућа подршка за вишекратне разговоре ако такви подаци постоје.

## Захтев за повећање Azure GPU квоте

### Предуслови

Azure налог са улогом Contributor (или неком другом улогом која укључује приступ Contributor-у).

Ако немате Azure налог, направите [бесплатан налог пре него што почнете](https://azure.microsoft.com).

### Захтев за повећање квоте

Можете поднети захтев за повећање квоте директно из My quotas. Пратите кораке испод да бисте затражили повећање квоте. За овај пример, можете изабрати било коју подесиву квоту у вашој претплати.

Пријавите се на [Azure портал](https://portal.azure.com).

У поље за претрагу унесите "quotas", а затим изаберите Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

На страници Overview изаберите провајдера, као што су Compute или AML.

**Напомена** За све провајдере осим Compute, видећете колону Request increase уместо Adjustable колоне описане испод. Тамо можете затражити повећање за одређену квоту или креирати захтев за подршку за повећање.

На страници My quotas, испод Quota name, изаберите квоту коју желите да повећате. Уверите се да колона Adjustable показује Yes за ову квоту.

При врху странице изаберите New Quota Request, затим изаберите Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

У панелу New Quota Request унесите бројчану вредност за нови лимит квоте, затим изаберите Submit.

Ваш захтев ће бити прегледан, и бићете обавештени да ли је захтев одобрен. Ово обично траје неколико минута.

Ако ваш захтев није одобрен, видећете линк за креирање захтева за подршку. Када користите тај линк, инжењер подршке ће вам помоћи са захтевом за повећање.

## Препоруке за Azure Compute GPU машине

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Ево неколико примера:

### Ако имате A100 или H100 GPU-ове

Потпуни фајнтјунинг обично даје најбоље перформансе. Можете користити следећу команду за фајнтјунинг Phi-3-V на класификацији мрзитељских мема.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ако имате Standard_ND40rs_v2 8x V100-32GB GPU-ове

И даље је могуће у потпуности фајнтјунирати Phi-3-V на класификацији мрзитељских мема. Међутим, очекујте  
знатно мањи проток у односу на A100 или H100 GPU-ове због недостатка подршке за flash attention.  
Тачност може бити утицана због недостатка подршке за bf16 (користи се fp16 мешовита прецизност).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ако немате приступ GPU-овима у дата центру

LoRA може бити једина опција. Можете користити следећу команду за фајнтјунинг Phi-3-V на класификацији мрзитељских мема.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

За Turing+ GPU, QLoRA је подржан

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Препоручени хиперпараметри и очекивана тачност

### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Метод тренинга | Замрзнути визијски модел | тип података | LoRA ранг | LoRA алфа | величина батча | стопа учења | епохе | Тачност  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA резултати ускоро |  |  |  |  |  |  |  |  |

### НАПОМЕНА  
Резултати за DocVQA и Hateful memes испод су засновани на претходној верзији (Phi-3-vision).  
Нови резултати са Phi-3.5-vision ће ускоро бити ажурирани.

### DocVQA (НАПОМЕНА: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Метод тренинга | тип података | LoRA ранг | LoRA алфа | величина батча | стопа учења | епохе | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
замрзнути сликовни модел | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
замрзнути сликовни модел | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (НАПОМЕНА: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Метод тренинга | тип података | LoRA ранг | LoRA алфа | величина батча | стопа учења | епохе | Тачност  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
замрзнути сликовни модел | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
замрзнути сликовни модел | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Тестирање брзине (НАПОМЕНА: Phi-3-vision)

Нови резултати тестирања брзине са Phi-3.5-vision ће ускоро бити ажурирани.

Тестирање брзине је извршено на DocVQA скупу података. Просечна дужина секвенце овог скупа је  
2443.23 токена (користећи `num_crops=16` за сликовни модел).

### 8x A100-80GB (Ampere)

Метод тренинга | \# чворова | GPU-ови | flash attention | Ефективна величина батча | Проток (слика/с) | Убрзање | Максимална меморија GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
замрзнути сликовни модел | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
замрзнути сликовни модел | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Метод тренинга | \# чворова | GPU-ови | flash attention | Ефективна величина батча | Проток (слика/с) | Убрзање | Максимална меморија GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
замрзнути сликовни модел | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Познати проблеми

- Нема могућности покретања flash attention са fp16 (увек се препоручује bf16 кад је доступан, а сви GPU-ови који подржавају flash attention такође подржавају bf16).  
- Још увек није подржано чување интерних чекпоинтова и наставак тренинга.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.