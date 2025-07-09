<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-09T19:02:20+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "uk"
}
-->
# Phi-3.5-vision рецепт донавчання

Це офіційна підтримка донавчання Phi-3.5-vision з використанням бібліотек huggingface.  
Будь ласка, перейдіть у директорію з кодом [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) перед запуском наступних команд.

## Встановлення

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

## Швидкий старт

Ми надаємо два приклади скриптів для донавчання: один для DocVQA, інший для класифікації образливих мемів.

Мінімальне тестоване обладнання — 4x RTX8000 (48 ГБ ОЗП на кожен GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision тепер офіційно підтримує мультизображення на вході. Ось приклад донавчання для NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Інструкція з використання

Залежно від обладнання, користувачі можуть обирати різні стратегії донавчання. Ми підтримуємо  
повне донавчання (з Deepspeed Zero-2) з опціонально замороженими параметрами візуальної частини, а також LoRA (включно з 4bit QLoRA).  
Загалом, рекомендуємо використовувати повне донавчання з flash attention та bf16, коли це можливо.

### Інструкція з конвертації вашого кастомного датасету у потрібний формат

Ми використовуємо мінімальний датасет для класифікації відео (підмножина UCF-101) як приклад end-to-end, щоб показати, як конвертувати ваш кастомний датасет у потрібний формат і донавчити на ньому Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Конвертовані дані виглядатимуть так:

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

Для анотації у форматі `jsonl` кожен рядок має бути словником такого вигляду:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Зверніть увагу, що `conversations` — це список, тому підтримується багатокрокова розмова, якщо такі дані доступні.

## Запит квоти на GPU в Azure

### Вимоги

Обліковий запис Azure з роллю Contributor (або іншою роллю, що включає доступ Contributor).

Якщо у вас немає облікового запису Azure, створіть [безкоштовний обліковий запис перед початком](https://azure.microsoft.com).

### Запит на збільшення квоти

Ви можете подати запит на збільшення квоти безпосередньо через My quotas. Виконайте наведені нижче кроки, щоб запросити збільшення квоти. Для прикладу можна обрати будь-яку регульовану квоту у вашій підписці.

Увійдіть у [Azure портал](https://portal.azure.com).

Введіть "quotas" у пошуковому полі, потім оберіть Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

На сторінці Overview оберіть провайдера, наприклад Compute або AML.

**Note** Для всіх провайдерів, окрім Compute, ви побачите колонку Request increase замість Adjustable, як описано нижче. Там можна запросити збільшення конкретної квоти або створити запит у службу підтримки.

На сторінці My quotas, у колонці Quota name оберіть квоту, яку хочете збільшити. Переконайтеся, що у колонці Adjustable для цієї квоти стоїть Yes.

Біля верху сторінки натисніть New Quota Request, потім оберіть Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

У панелі New Quota Request введіть числове значення нового ліміту квоти, потім натисніть Submit.

Ваш запит буде розглянутий, і ви отримаєте повідомлення, чи його можна виконати. Зазвичай це відбувається протягом кількох хвилин.

Якщо запит не буде виконано, ви побачите посилання для створення запиту у службу підтримки. Використовуючи це посилання, інженер підтримки допоможе вам із запитом на збільшення.

## Рекомендовані SKU для Azure Compute GPU машин

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Ось кілька прикладів:

### Якщо у вас є GPU A100 або H100

Повне донавчання зазвичай дає найкращу продуктивність. Ви можете використати наступну команду для донавчання Phi-3-V на класифікації образливих мемів.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Якщо у вас є Standard_ND40rs_v2 з 8x V100-32GB GPU

Повне донавчання Phi-3-V на класифікації образливих мемів також можливе. Однак очікуйте значно нижчу пропускну здатність у порівнянні з A100 або H100 через відсутність підтримки flash attention.  
Точність також може постраждати через відсутність підтримки bf16 (замість цього використовується змішана точність fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Якщо у вас немає доступу до GPU дата-центру

LoRA може бути вашим єдиним варіантом. Ви можете використати наступну команду для донавчання Phi-3-V на класифікації образливих мемів.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Для GPU Turing+ підтримується QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Рекомендовані гіперпараметри та очікувана точність

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

Метод навчання | Заморожена візуальна модель | тип даних | ранг LoRA | альфа LoRA | розмір батчу | швидкість навчання | епохи | Точність  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
повне донавчання |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
повне донавчання | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Результати LoRA скоро будуть |  |  |  |  |  |  |  |  |

### NOTE  
Нижченаведені результати для DocVQA та образливих мемів базуються на попередній версії (Phi-3-vision).  
Нові результати з Phi-3.5-vision будуть оновлені найближчим часом.

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

Метод навчання | тип даних | ранг LoRA | альфа LoRA | розмір батчу | швидкість навчання | епохи | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
повне донавчання | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
повне донавчання | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
заморожена візуальна модель | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
заморожена візуальна модель | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Образливі меми (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Метод навчання | тип даних | ранг LoRA | альфа LoRA | розмір батчу | швидкість навчання | епохи | Точність  
--- | --- | --- | --- | --- | --- | --- | --- |  
повне донавчання | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
повне донавчання | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
заморожена візуальна модель | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
заморожена візуальна модель | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Тестування швидкості (NOTE: Phi-3-vision)

Нові результати тестування з Phi-3.5-vision будуть оновлені найближчим часом.

Тестування швидкості виконувалося на датасеті DocVQA. Середня довжина послідовності цього датасету — 2443.23 токенів (з використанням `num_crops=16` для візуальної моделі).

### 8x A100-80GB (Ampere)

Метод навчання | \# вузлів | GPU | flash attention | Ефективний розмір батчу | Пропускна здатність (зобр./с) | Прискорення | Пік пам’яті GPU (ГБ)  
--- | --- | --- | --- | --- | --- | --- | --- |  
повне донавчання | 1 | 8 |  | 64 | 5.041 | 1x | ~42 |  
повне донавчання | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 |  
повне донавчання | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 |  
повне донавчання | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 |  
заморожена візуальна модель | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29 |  
заморожена візуальна модель | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 |  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50 |  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 |  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32 |  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 |

### 8x V100-32GB (Volta)

Метод навчання | \# вузлів | GPU | flash attention | Ефективний розмір батчу | Пропускна здатність (зобр./с) | Прискорення | Пік пам’яті GPU (ГБ)  
--- | --- | --- | --- | --- | --- | --- | --- |  
повне донавчання | 1 | 8 |  | 64 | 2.462 | 1x | ~32 |  
повне донавчання | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32 |  
повне донавчання | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32 |  
заморожена візуальна модель | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27 |  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30 |

## Відомі проблеми

- Неможливо запускати flash attention з fp16 (рекомендується завжди використовувати bf16, і всі GPU, що підтримують flash attention, також підтримують bf16).  
- Поки що не підтримується збереження проміжних чекпойнтів і відновлення навчання.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.