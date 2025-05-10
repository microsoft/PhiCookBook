<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:07:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "bg"
}
-->
# Phi-3.5-vision рецепта за фино настройване

Това е официалната поддръжка за фино настройване на Phi-3.5-vision с помощта на huggingface библиотеки.  
Моля, `cd` към директорията с код [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) преди да изпълните следващите команди.

## Инсталация

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

## Бърз старт

Предоставяме два примерни скрипта за фино настройване – един за DocVQA и един за класификация на омразни мемета.

Минималният хардуер, тестван на 4x RTX8000 (48GB RAM на GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision вече официално поддържа вход с множество изображения. Ето пример за фино настройване на NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Ръководство за употреба

В зависимост от хардуера, потребителите могат да изберат различни стратегии за фино настройване. Поддържаме  
full-finetuning (с Deepspeed Zero-2) с опционално замразени визуални параметри, както и LoRA (включително 4bit QLoRA).  
Общо взето, препоръчваме да използвате full finetuning с flash attention и bf16, когато е възможно.

### Ръководство за конвертиране на ваш собствен набор от данни в изисквания формат

Използваме минимален видео класификационен набор от данни (подмножество от UCF-101) като пример от край до край, за да демонстрираме как да конвертирате вашия набор от данни в изисквания формат и да фино настроите Phi-3.5-vision върху него.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Конвертираните данни ще изглеждат така:

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

За `jsonl` анотацията, всеки ред трябва да е речник като:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Обърнете внимание, че `conversations` е списък, затова се поддържа мулти-стъпков разговор, ако такива данни са налични.

## Искане за квота за Azure GPU

### Предварителни изисквания

Необходим е Azure акаунт с роля Contributor (или друга роля, включваща достъп Contributor).

Ако нямате Azure акаунт, създайте [безплатен акаунт преди да започнете](https://azure.microsoft.com).

### Искане за увеличение на квота

Можете да подадете заявка за увеличение на квота директно от My quotas. Следвайте стъпките по-долу, за да поискате увеличение на квота. За този пример можете да изберете всяка регулируема квота във вашия абонамент.

Влезте в [Azure портала](https://portal.azure.com).

Въведете "quotas" в полето за търсене и изберете Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

На страницата Overview изберете доставчик, като Compute или AML.

**Note** За всички доставчици, различни от Compute, ще видите колона Request increase вместо описаната Adjustable колона. Там можете да поискате увеличение за конкретна квота или да създадете заявка за поддръжка.

На страницата My quotas, под Quota name, изберете квотата, която искате да увеличите. Уверете се, че колоната Adjustable показва Yes за тази квота.

Близо до върха на страницата изберете New Quota Request, след това изберете Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

В панела New Quota Request въведете числова стойност за новия лимит на квотата и след това изберете Submit.

Вашата заявка ще бъде прегледана и ще получите уведомление дали може да бъде изпълнена. Обикновено това става в рамките на няколко минути.

Ако заявката не бъде изпълнена, ще видите връзка за създаване на заявка за поддръжка. Когато използвате тази връзка, инженер по поддръжката ще ви помогне с вашето искане за увеличение.

## Препоръчани SKU за Azure Compute GPU машини

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Ето няколко примера:

### Ако имате A100 или H100 GPU-та

Пълното фино настройване обикновено дава най-добра производителност. Можете да използвате следната команда за фино настройване на Phi-3-V за класификация на омразни мемета.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ако имате Standard_ND40rs_v2 с 8x V100-32GB GPU-та

Все още е възможно да се направи пълно фино настройване на Phi-3-V за класификация на омразни мемета. Въпреки това очаквайте  
значително по-нисък пропускателен капацитет в сравнение с A100 или H100 GPU-та поради липсата на поддръжка на flash attention.  
Точността също може да бъде засегната поради липсата на поддръжка на bf16 (използва се fp16 смесена прецизност).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ако нямате достъп до GPU-та в центрове за данни  
LoRA може да е единственият ви избор. Можете да използвате следната команда за фино настройване на Phi-3-V за класификация на омразни мемета.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

За Turing+ GPU е поддържан QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Препоръчани хиперпараметри и очаквана точност

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

Метод на обучение | Замразен визуален модел | тип данни | LoRA ранг | LoRA алфа | размер на партидата | скорост на учене | епохи | Точност
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Резултати за LoRA скоро ще бъдат налични |  |  |  |  |  |  |  |  |

### NOTE  
Долните резултати за DocVQA и Hateful memes са базирани на предишната версия (Phi-3-vision).  
Новите резултати с Phi-3.5-vision ще бъдат актуализирани скоро.

### DocVQA (NOTE: Phi-3-vision)

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

Метод на обучение | тип данни | LoRA ранг | LoRA алфа | размер на партидата | скорост на учене | епохи | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
замразен визуален модел | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
замразен визуален модел | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Метод на обучение | тип данни | LoRA ранг | LoRA алфа | размер на партидата | скорост на учене | епохи | Точност
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
замразен визуален модел | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
замразен визуален модел | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Тестове за скорост (NOTE: Phi-3-vision)

Новите тестове за скорост с Phi-3.5-vision ще бъдат добавени скоро.

Тестовете за скорост са извършени върху набора от данни DocVQA. Средната дължина на последователността в този набор е 2443.23 токена (използвайки `num_crops=16` за визуалния модел).

### 8x A100-80GB (Ampere)

Метод на обучение | \# възли | GPU-та | flash attention | Ефективен размер на партидата | Пропускателна способност (изображения/сек) | Ускорение | Пикова GPU памет (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
замразен визуален модел | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
замразен визуален модел | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Метод на обучение | \# възли | GPU-та | flash attention | Ефективен размер на партидата | Пропускателна способност (изображения/сек) | Ускорение | Пикова GPU памет (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
замразен визуален модел | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Известни проблеми

- Не може да се използва flash attention с fp16 (препоръчва се винаги bf16, когато е наличен, а всички GPU-та, поддържащи flash attention, поддържат и bf16).
- Все още не се поддържа запазване на междинни контролни точки и възобновяване на обучението.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.