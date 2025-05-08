<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-07T13:35:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "ru"
}
-->
# Phi-3.5-vision рецепт дообучения

Это официальная поддержка дообучения Phi-3.5-vision с использованием библиотек huggingface.  
Перед выполнением следующих команд перейдите `cd` в каталог с кодом [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

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

Мы предоставляем два примера скриптов дообучения: для DocVQA и для классификации оскорбительных мемов.

Минимальное протестированное оборудование: 4x RTX8000 (48 ГБ ОЗУ на GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision теперь официально поддерживает мульти-изображения на входе. Вот пример дообучения на NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Руководство по использованию

В зависимости от аппаратного обеспечения пользователи могут выбрать разные стратегии дообучения. Мы поддерживаем  
полное дообучение (с Deepspeed Zero-2) с возможностью заморозки параметров vision и LoRA (включая 4bit QLoRA).  
В целом, мы рекомендуем использовать полное дообучение с flash attention и bf16, когда это возможно.

### Руководство по конвертации вашего собственного датасета в нужный формат

Мы используем минимальный датасет для классификации видео (подмножество UCF-101) в качестве примера end-to-end, чтобы показать, как конвертировать ваш датасет в нужный формат и дообучить Phi-3.5-vision на нём.

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

Для аннотаций в формате `jsonl` каждая строка должна быть словарём следующего вида:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Обратите внимание, что `conversations` — это список, поэтому поддерживается многоступенчатый диалог, если такие данные доступны.

## Запрос квоты на Azure GPU

### Требования

Аккаунт Azure с ролью Contributor (или другой ролью с доступом Contributor).

Если у вас нет аккаунта Azure, создайте [бесплатный аккаунт перед началом работы](https://azure.microsoft.com).

### Запрос увеличения квоты

Вы можете отправить запрос на увеличение квоты напрямую через My quotas. Следуйте инструкциям ниже, чтобы запросить увеличение квоты. В этом примере можно выбрать любую регулируемую квоту в вашей подписке.

Войдите в [Azure портал](https://portal.azure.com).

Введите «quotas» в строку поиска и выберите Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

На странице Overview выберите провайдера, например Compute или AML.

**Note** Для всех провайдеров, кроме Compute, вы увидите столбец Request increase вместо Adjustable, как описано ниже. Там можно запросить увеличение конкретной квоты или создать запрос в службу поддержки.

На странице My quotas в столбце Quota name выберите квоту, которую хотите увеличить. Убедитесь, что в столбце Adjustable для этой квоты указано Yes.

В верхней части страницы выберите New Quota Request, затем выберите Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

В панели New Quota Request введите числовое значение нового лимита квоты и нажмите Submit.

Ваш запрос будет рассмотрен, и вы получите уведомление, если запрос будет удовлетворён. Обычно это происходит в течение нескольких минут.

Если запрос не будет удовлетворён, вы увидите ссылку для создания запроса в службу поддержки. При использовании этой ссылки с вами свяжется инженер поддержки для помощи с вашим запросом.

## Рекомендации по SKU GPU машин Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Вот несколько примеров:

### Если у вас есть GPU A100 или H100

Полное дообучение обычно даёт наилучшую производительность. Можно использовать следующую команду для дообучения Phi-3-V на классификации оскорбительных мемов.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Если у вас есть Standard_ND40rs_v2 8x V100-32GB GPUs

Дообучение Phi-3-V на классификации оскорбительных мемов всё ещё возможно. Однако ожидайте  
значительно меньшую пропускную способность по сравнению с A100 или H100 из-за отсутствия поддержки flash attention.  
Точность также может пострадать из-за отсутствия поддержки bf16 (используется смешанная точность fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Если у вас нет доступа к GPU дата-центров

LoRA может быть вашим единственным вариантом. Можно использовать следующую команду для дообучения Phi-3-V на классификации оскорбительных мемов.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Для GPU Turing+ поддерживается QLoRA

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

Метод обучения | Замороженная модель vision | тип данных | ранг LoRA | alpha LoRA | размер батча | скорость обучения | эпохи | Точность  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20  
Результаты LoRA скоро будут |  |  |  |  |  |  |  |  |

### NOTE  
Ниже приведены результаты DocVQA и Hateful memes, основанные на предыдущей версии (Phi-3-vision).  
Новые результаты для Phi-3.5-vision будут обновлены в ближайшее время.

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

Метод обучения | тип данных | ранг LoRA | alpha LoRA | размер батча | скорость обучения | эпохи | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60  
замороженная модель изображения | bf16 | - | - | 64 | 1e-4 | 2 | 79.19  
замороженная модель изображения | fp16 | - | - | 64 | 1e-4 | 2 | 78.74  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  

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

Метод обучения | тип данных | ранг LoRA | alpha LoRA | размер батча | скорость обучения | эпохи | Точность  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4  
замороженная модель изображения | bf16 | - | - | 64 | 1e-4 | 3 | 79.4  
замороженная модель изображения | fp16 | - | - | 64 | 1e-4 | 3 | 78.6  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8  

## Тестирование скорости (NOTE: Phi-3-vision)

Новые результаты тестирования скорости с Phi-3.5-vision будут обновлены в ближайшее время.

Тестирование скорости проведено на датасете DocVQA. Средняя длина последовательности в этом датасете  
составляет 2443.23 токена (используется `num_crops=16` для модели изображения).

### 8x A100-80GB (Ampere)

Метод обучения | \# узлов | GPU | flash attention | Эффективный размер батча | Пропускная способность (изобр./с) | Ускорение | Пиковое потребление памяти GPU (ГБ)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
замороженная модель изображения | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
замороженная модель изображения | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Метод обучения | \# узлов | GPU | flash attention | Эффективный размер батча | Пропускная способность (изобр./с) | Ускорение | Пиковое потребление памяти GPU (ГБ)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
замороженная модель изображения | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Известные проблемы

- Невозможно использовать flash attention с fp16 (рекомендуется всегда использовать bf16, если доступно, и все GPU, поддерживающие flash attention, также поддерживают bf16).  
- Пока не поддерживается сохранение промежуточных чекпоинтов и возобновление обучения.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.