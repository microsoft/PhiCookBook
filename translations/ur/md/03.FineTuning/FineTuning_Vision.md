<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dd1b570422a819b39b14a4c7be06c8fa",
  "translation_date": "2025-04-03T08:21:54+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Vision.md",
  "language_code": "ur"
}
-->
# Phi-3.5-vision فائن ٹیوننگ ترکیب

یہ Phi-3.5-vision کے فائن ٹیوننگ کے لیے huggingface لائبریریوں کا آفیشل سپورٹ ہے۔
براہ کرم کوڈ ڈائریکٹری [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) پر جائیں اور درج ذیل کمانڈز چلانے سے پہلے اسے دیکھیں۔

## انسٹالیشن

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

## جلدی شروع کریں

ہم دو مثالوں کے فائن ٹیوننگ اسکرپٹس فراہم کرتے ہیں، ایک DocVQA کے لیے اور ایک نفرت انگیز میمز کی درجہ بندی کے لیے۔

کم از کم ہارڈویئر: 4x RTX8000 (48GB RAM فی GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision اب باقاعدہ طور پر ملٹی امیج ان پٹس کو سپورٹ کرتا ہے۔ یہاں NLVR2 کے فائن ٹیوننگ کے لیے ایک مثال ہے:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## استعمال کی رہنمائی

ہارڈویئر کے مطابق، صارفین مختلف فائن ٹیوننگ حکمت عملیوں کا انتخاب کر سکتے ہیں۔ ہم مکمل فائن ٹیوننگ (Deepspeed Zero-2 کے ساتھ) کی حمایت کرتے ہیں، جس میں ویژن پیرامیٹرز کو منجمد کرنے کا آپشن شامل ہے، اور LoRA (4bit QLoRA سمیت)۔ عمومی طور پر، ہم bf16 اور فلیش اٹینشن کے ساتھ مکمل فائن ٹیوننگ کی سفارش کرتے ہیں جب بھی ممکن ہو۔

### اپنی مرضی کے ڈیٹاسیٹ کو مطلوبہ فارمیٹ میں تبدیل کرنے کی رہنمائی

ہم ایک کم از کم ویڈیو درجہ بندی ڈیٹاسیٹ (UCF-101 کا سب سیٹ) استعمال کرتے ہیں تاکہ یہ دکھایا جا سکے کہ اپنی مرضی کے ڈیٹاسیٹ کو مطلوبہ فارمیٹ میں کیسے تبدیل کیا جائے اور Phi-3.5-vision پر فائن ٹیون کیسے کریں۔

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

تبدیل شدہ ڈیٹا اس طرح نظر آئے گا:

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

`jsonl` تشریح کے لیے، ہر لائن ایک ڈکشنری ہونی چاہیے جیسے:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

نوٹ کریں کہ `conversations` ایک فہرست ہے، اس طرح ملٹی ٹرن گفتگو کو سپورٹ کیا جا سکتا ہے اگر ایسا ڈیٹا دستیاب ہو۔

## Azure GPU کوٹا کی درخواست 

### شرائط

Contributor رول کے ساتھ ایک Azure اکاؤنٹ (یا کوئی دوسرا رول جس میں Contributor رسائی شامل ہو)۔

اگر آپ کے پاس Azure اکاؤنٹ نہیں ہے، تو [ایک مفت اکاؤنٹ بنائیں](https://azure.microsoft.com)۔

### کوٹا میں اضافے کی درخواست کریں

آپ My quotas سے براہ راست کوٹا میں اضافے کی درخواست کر سکتے ہیں۔ کوٹا میں اضافے کی درخواست کے لیے درج ذیل مراحل پر عمل کریں۔ اس مثال کے لیے، آپ اپنی سبسکرپشن میں کسی بھی ایڈجسٹ کوٹا کا انتخاب کر سکتے ہیں۔

Azure پورٹل میں سائن ان کریں [Azure portal](https://portal.azure.com)۔

سرچ باکس میں "quotas" درج کریں، پھر Quotas کو منتخب کریں۔
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview صفحہ پر، ایک پرووائیڈر منتخب کریں، جیسے Compute یا AML۔

**نوٹ** Compute کے علاوہ تمام پرووائیڈرز کے لیے، آپ کو Request increase کالم نظر آئے گا بجائے Adjustable کالم کے۔ وہاں، آپ کسی مخصوص کوٹا کے لیے اضافے کی درخواست کر سکتے ہیں، یا اضافے کے لیے سپورٹ درخواست بنا سکتے ہیں۔

My quotas صفحہ پر، Quota name کے تحت، اس کوٹا کو منتخب کریں جسے آپ بڑھانا چاہتے ہیں۔ یقینی بنائیں کہ Adjustable کالم اس کوٹا کے لیے Yes دکھاتا ہے۔

صفحے کے اوپری حصے میں، New Quota Request منتخب کریں، پھر Enter a new limit کو منتخب کریں۔

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request پین میں، اپنے نئے کوٹا کی حد کے لیے عددی قدر درج کریں، پھر Submit کو منتخب کریں۔

آپ کی درخواست کا جائزہ لیا جائے گا، اور آپ کو مطلع کیا جائے گا کہ آیا درخواست پوری کی جا سکتی ہے۔ یہ عام طور پر چند منٹوں میں ہوتا ہے۔

اگر آپ کی درخواست پوری نہیں ہوتی، تو آپ کو سپورٹ درخواست بنانے کے لیے ایک لنک نظر آئے گا۔ جب آپ اس لنک کا استعمال کرتے ہیں، تو ایک سپورٹ انجینئر آپ کی اضافے کی درخواست میں مدد کرے گا۔

## Azure Compute GPU مشین SKU تجاویز

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

یہاں کچھ مثالیں ہیں:

### اگر آپ کے پاس A100 یا H100 GPUs ہیں

مکمل فائن ٹیوننگ عام طور پر بہترین کارکردگی فراہم کرتی ہے۔ آپ درج ذیل کمانڈ کا استعمال کرتے ہوئے نفرت انگیز میمز کی درجہ بندی پر Phi-3-V کو فائن ٹیون کر سکتے ہیں۔

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### اگر آپ کے پاس Standard_ND40rs_v2 8x V100-32GB GPUs ہیں

Phi-3-V کو نفرت انگیز میمز کی درجہ بندی پر مکمل فائن ٹیون کرنا اب بھی ممکن ہے۔ تاہم، A100 یا H100 GPUs کے مقابلے میں فلیش اٹینشن کی عدم موجودگی کی وجہ سے بہت کم تھروپٹ کی توقع کریں۔
درستگی بھی متاثر ہو سکتی ہے کیونکہ bf16 کی عدم موجودگی کی وجہ سے fp16 مکسڈ پریسیشن ٹریننگ استعمال کی جاتی ہے۔

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### اگر آپ کے پاس ڈیٹا سینٹر GPUs تک رسائی نہیں ہے
LoRA شاید آپ کا واحد انتخاب ہو۔ آپ درج ذیل کمانڈ کا استعمال کرتے ہوئے نفرت انگیز میمز کی درجہ بندی پر Phi-3-V کو فائن ٹیون کر سکتے ہیں۔

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU کے لیے، QLoRA کی حمایت کی جاتی ہے

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## تجویز کردہ ہائپر پیرامیٹرز اور متوقع درستگی
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

ٹریننگ کا طریقہ | منجمد ویژن ماڈل | ڈیٹا ٹائپ | LoRA رینک | LoRA الفا | بیچ سائز | لرننگ ریٹ | ایپوکز | درستگی
--- | --- | --- | --- | --- | --- | --- | --- | --- |
مکمل فائن ٹیوننگ |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
مکمل فائن ٹیوننگ | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA کے نتائج جلد آئیں گے |  |  |  |  |  |  |  |  |

### نوٹ
ذیل میں DocVQA اور نفرت انگیز میمز کے نتائج پچھلے ورژن (Phi-3-vision) پر مبنی ہیں۔
Phi-3.5-vision کے ساتھ نئے نتائج جلد اپ ڈیٹ کیے جائیں گے۔

### DocVQA (نوٹ: Phi-3-vision)

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

ٹریننگ کا طریقہ | ڈیٹا ٹائپ | LoRA رینک | LoRA الفا | بیچ سائز | لرننگ ریٹ | ایپوکز | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
مکمل فائن ٹیوننگ | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
مکمل فائن ٹیوننگ | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
منجمد امیج ماڈل| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
منجمد امیج ماڈل| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### نفرت انگیز میمز (نوٹ: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

ٹریننگ کا طریقہ | ڈیٹا ٹائپ | LoRA رینک | LoRA الفا | بیچ سائز | لرننگ ریٹ | ایپوکز | درستگی
--- | --- | --- | --- | --- | --- | --- | --- |
مکمل فائن ٹیوننگ | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
مکمل فائن ٹیوننگ | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
منجمد امیج ماڈل| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
منجمد امیج ماڈل| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## رفتار کا بینچ مارکنگ (نوٹ: Phi-3-vision)

Phi-3.5-vision کے ساتھ نئے بینچ مارکنگ نتائج جلد اپ ڈیٹ کیے جائیں گے۔

رفتار کا بینچ مارکنگ DocVQA ڈیٹاسیٹ پر انجام دیا گیا۔ اس ڈیٹاسیٹ کی اوسط سیکوئنس لمبائی 2443.23 ٹوکنز ہے (`num_crops=16` کے ساتھ امیج ماڈل کے لیے)۔

### 8x A100-80GB (Ampere)

ٹریننگ کا طریقہ | \# نوڈز | GPUs | فلیش اٹینشن | مؤثر بیچ سائز | تھروپٹ (img/s) | رفتار | GPU میم کی چوٹی (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
مکمل فائن ٹیوننگ | 1 | 8 |  | 64 | 5.041 |  1x | ~42
مکمل فائن ٹیوننگ | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
مکمل فائن ٹیوننگ | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
مکمل فائن ٹیوننگ | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
منجمد امیج ماڈل | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
منجمد امیج ماڈل | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

ٹریننگ کا طریقہ | \# نوڈز | GPUs | فلیش اٹینشن | مؤثر بیچ سائز | تھروپٹ (img/s) | رفتار | GPU میم کی چوٹی (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
مکمل فائن ٹیوننگ | 1 | 8 | | 64 | 2.462 |  1x | ~32
مکمل فائن ٹیوننگ | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
مکمل فائن ٹیوننگ | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
منجمد امیج ماڈل | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## معلوم مسائل

- فلیش اٹینشن fp16 کے ساتھ نہیں چل سکتا (bf16 ہمیشہ سفارش کی جاتی ہے جب دستیاب ہو، اور تمام GPUs جو فلیش اٹینشن کی حمایت کرتے ہیں وہ bf16 کی بھی حمایت کرتے ہیں)۔
- ابھی تک درمیانی چیک پوائنٹس کو محفوظ کرنے اور ٹریننگ کو دوبارہ شروع کرنے کی حمایت نہیں کرتے۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔