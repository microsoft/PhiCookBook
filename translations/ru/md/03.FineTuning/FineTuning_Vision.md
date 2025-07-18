<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:33:45+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "ru"
}
-->
# Phi-3.5-vision рецепт дообучения

Это официальная поддержка дообучения Phi-3.5-vision с использованием библиотек huggingface.  
Перед выполнением следующих команд перейдите в каталог с кодом [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Установка

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

## Быстрый старт

Мы предоставляем два примера скриптов дообучения: один для DocVQA и один для классификации оскорбительных мемов.

Минимальное тестовое оборудование — 4x RTX8000 (48 ГБ ОЗУ на каждую GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision теперь официально поддерживает мульти-изображения на входе. Вот пример дообучения на NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Руководство по использованию

В зависимости от оборудования пользователи могут выбирать разные стратегии дообучения. Мы поддерживаем  
полное дообучение (с Deepspeed Zero-2) с возможностью заморозки параметров визуальной части, а также LoRA (включая 4-битный QLoRA).  
В целом, мы рекомендуем использовать полное дообучение с flash attention и bf16, когда это возможно.

### Руководство по конвертации вашего кастомного датасета в требуемый формат

В качестве примера end-to-end мы используем минимальный датасет для классификации видео (подмножество UCF-101), чтобы показать, как преобразовать ваш датасет в нужный формат и дообучить на нем Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Преобразованные данные будут выглядеть так:

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

Для аннотации в формате `jsonl` каждая строка должна быть словарём следующего вида:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Обратите внимание, что `conversations` — это список, поэтому поддерживается мульти-туровое общение, если такие данные доступны.

## Запрос квоты на Azure GPU

### Требования

Аккаунт Azure с ролью Contributor (или другой ролью, включающей доступ Contributor).

Если у вас нет аккаунта Azure, создайте [бесплатный аккаунт перед началом работы](https://azure.microsoft.com).

### Запрос увеличения квоты

Вы можете подать запрос на увеличение квоты напрямую через My quotas. Следуйте инструкциям ниже, чтобы запросить увеличение квоты. Для примера можно выбрать любую регулируемую квоту в вашей подписке.

Войдите в [Azure портал](https://portal.azure.com).

Введите "quotas" в строку поиска и выберите Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

На странице Overview выберите провайдера, например Compute или AML.

**Примечание** Для всех провайдеров, кроме Compute, вы увидите колонку Request increase вместо Adjustable, как описано ниже. Там можно запросить увеличение конкретной квоты или создать запрос в поддержку.

На странице My quotas в столбце Quota name выберите квоту, которую хотите увеличить. Убедитесь, что в столбце Adjustable для этой квоты стоит Yes.

В верхней части страницы выберите New Quota Request, затем Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

В панели New Quota Request введите числовое значение нового лимита и нажмите Submit.

Ваш запрос будет рассмотрен, и вы получите уведомление о возможности его выполнения. Обычно это занимает несколько минут.

Если запрос не будет выполнен, появится ссылка для создания запроса в поддержку. Используя её, вы получите помощь инженера поддержки по вашему запросу.

## Рекомендации по SKU GPU машин Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Примеры:

### Если у вас есть GPU A100 или H100

Полное дообучение обычно даёт наилучшие результаты. Для дообучения Phi-3-V на классификации оскорбительных мемов можно использовать следующую команду.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Если у вас есть Standard_ND40rs_v2 с 8x V100-32GB GPU

Полное дообучение Phi-3-V на классификации оскорбительных мемов также возможно. Однако ожидайте значительно меньшую пропускную способность по сравнению с A100 или H100 из-за отсутствия поддержки flash attention.  
Точность также может пострадать из-за отсутствия поддержки bf16 (используется смешанная точность fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Если у вас нет доступа к GPU дата-центра

LoRA может быть вашим единственным вариантом. Для дообучения Phi-3-V на классификации оскорбительных мемов используйте следующую команду.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Для GPU поколения Turing+ поддерживается QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Рекомендуемые гиперпараметры и ожидаемая точность

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

Метод обучения | Замороженная визуальная модель | тип данных | ранг LoRA | LoRA alpha | размер батча | скорость обучения | эпохи | Точность  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20  
Результаты LoRA скоро будут |  |  |  |  |  |  |  |  |

### ВАЖНО  
Ниже приведены результаты для DocVQA и Hateful memes на основе предыдущей версии (Phi-3-vision).  
Новые результаты с Phi-3.5-vision будут опубликованы в ближайшее время.

### DocVQA (ВАЖНО: Phi-3-vision)

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

Метод обучения | тип данных | ранг LoRA | LoRA alpha | размер батча | скорость обучения | эпохи | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60  
замороженная визуальная модель | bf16 | - | - | 64 | 1e-4 | 2 | 79.19  
замороженная визуальная модель | fp16 | - | - | 64 | 1e-4 | 2 | 78.74  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  

### Hateful memes (ВАЖНО: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Метод обучения | тип данных | ранг LoRA | LoRA alpha | размер батча | скорость обучения | эпохи | Точность  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4  
замороженная визуальная модель | bf16 | - | - | 64 | 1e-4 | 3 | 79.4  
замороженная визуальная модель | fp16 | - | - | 64 | 1e-4 | 3 | 78.6  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8  

## Тестирование скорости (ВАЖНО: Phi-3-vision)

Новые результаты тестирования с Phi-3.5-vision будут опубликованы в ближайшее время.

Тестирование скорости проводилось на датасете DocVQA. Средняя длина последовательности в этом датасете — 2443.23 токена (используется `num_crops=16` для визуальной модели).

### 8x A100-80GB (Ampere)

Метод обучения | \# узлов | GPU | flash attention | Эффективный размер батча | Пропускная способность (изображений/с) | Ускорение | Пиковое использование памяти GPU (ГБ)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
замороженная визуальная модель | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
замороженная визуальная модель | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Метод обучения | \# узлов | GPU | flash attention | Эффективный размер батча | Пропускная способность (изображений/с) | Ускорение | Пиковое использование памяти GPU (ГБ)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
замороженная визуальная модель | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Известные проблемы

- Невозможно использовать flash attention с fp16 (рекомендуется bf16, если доступно, и все GPU с поддержкой flash attention также поддерживают bf16).  
- Пока не поддерживается сохранение промежуточных чекпоинтов и возобновление обучения.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.