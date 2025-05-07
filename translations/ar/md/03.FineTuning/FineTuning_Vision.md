<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-07T10:26:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "ar"
}
-->
# وصفة ضبط Phi-3.5-vision بدقة

هذا هو الدعم الرسمي لضبط Phi-3.5-vision باستخدام مكتبات huggingface.  
يرجى `cd` إلى مجلد الكود [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) قبل تشغيل الأوامر التالية.

## التثبيت

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

## بداية سريعة

نقدم سكريبتين مثالين للضبط الدقيق، أحدهما لـ DocVQA والآخر لتصنيف الميمات المسيئة.

تم اختبار الحد الأدنى من الأجهزة على 4x RTX8000 (ذاكرة 48GB لكل وحدة معالجة رسومات)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

يدعم Phi-3.5-vision الآن رسميًا إدخال صور متعددة. إليك مثال لضبط NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## دليل الاستخدام

اعتمادًا على الأجهزة، يمكن للمستخدمين اختيار استراتيجيات ضبط مختلفة. نحن ندعم  
الضبط الكامل (مع Deepspeed Zero-2) مع إمكانية تجميد معلمات الرؤية، وLoRA (بما في ذلك 4bit QLoRA).  
بشكل عام، نوصي باستخدام الضبط الكامل مع flash attention وbf16 متى ما أمكن.

### دليل لتحويل مجموعة البيانات المخصصة إلى التنسيق المطلوب

نستخدم مجموعة بيانات تصنيف فيديو بسيطة (جزء من UCF-101) كمثال شامل لشرح كيفية تحويل مجموعة البيانات المخصصة وضبط Phi-3.5-vision عليها.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

سيبدو البيانات المحولة كالتالي:

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

بالنسبة لتعليقات `jsonl`، يجب أن يكون كل سطر قاموسًا مثل:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

لاحظ أن `conversations` هي قائمة، لذا يمكن دعم المحادثات متعددة الأدوار إذا كانت هذه البيانات متوفرة.

## طلب حصة GPU من Azure

### المتطلبات الأساسية

حساب Azure بدور Contributor (أو دور آخر يتضمن صلاحيات Contributor).

إذا لم يكن لديك حساب Azure، قم بإنشاء [حساب مجاني قبل البدء](https://azure.microsoft.com).

### طلب زيادة الحصة

يمكنك تقديم طلب زيادة الحصة مباشرة من صفحة My quotas. اتبع الخطوات أدناه لطلب زيادة حصة. في هذا المثال، يمكنك اختيار أي حصة قابلة للتعديل في اشتراكك.

سجل الدخول إلى [بوابة Azure](https://portal.azure.com).

اكتب "quotas" في مربع البحث، ثم اختر Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

في صفحة Overview، اختر مزودًا مثل Compute أو AML.

**ملاحظة** بالنسبة لجميع المزودين غير Compute، سترى عمود Request increase بدلاً من عمود Adjustable الموضح أدناه. هناك، يمكنك طلب زيادة لحصة محددة أو إنشاء طلب دعم للزيادة.

في صفحة My quotas، ضمن اسم الحصة، اختر الحصة التي تريد زيادتها. تأكد من أن عمود Adjustable يعرض نعم لهذه الحصة.

قرب أعلى الصفحة، اختر New Quota Request، ثم اختر Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

في لوحة New Quota Request، أدخل قيمة رقمية لحد الحصة الجديد، ثم اختر Submit.

سيتم مراجعة طلبك، وسيتم إعلامك إذا كان بالإمكان تلبيته. عادةً ما يحدث ذلك خلال دقائق.

إذا لم يتم تلبية طلبك، سترى رابطًا لإنشاء طلب دعم. عند استخدام هذا الرابط، سيساعدك مهندس الدعم في طلب الزيادة.

## اقتراحات SKU لأجهزة Azure Compute GPU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

إليك بعض الأمثلة:

### إذا كان لديك GPUs من نوع A100 أو H100

عادةً ما يعطي الضبط الكامل أفضل أداء. يمكنك استخدام الأمر التالي لضبط Phi-3-V على تصنيف الميمات المسيئة.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### إذا كان لديك Standard_ND40rs_v2 مع 8x V100-32GB GPUs

لا يزال من الممكن ضبط Phi-3-V بالكامل على تصنيف الميمات المسيئة. مع ذلك، توقع  
معدل تمرير أقل بكثير مقارنة بـ A100 أو H100 بسبب عدم دعم flash attention.  
قد تتأثر الدقة أيضًا بسبب عدم دعم bf16 (يُستخدم تدريب دقة مختلطة fp16 بدلاً من ذلك).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### إذا لم يكن لديك وصول إلى GPUs في مراكز البيانات

قد يكون LoRA خيارك الوحيد. يمكنك استخدام الأمر التالي لضبط Phi-3-V على تصنيف الميمات المسيئة.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

بالنسبة لـ Turing+ GPU، يتم دعم QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## المعلمات المقترحة والدقة المتوقعة  
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

طريقة التدريب | نموذج الرؤية المجمد | نوع البيانات | رتبة LoRA | ألفا LoRA | حجم الدُفعة | معدل التعلم | عدد العصور | الدقة  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA results comming soon |  |  |  |  |  |  |  |  |

### ملاحظة  
النتائج التالية لـ DocVQA وHateful memes مبنية على النسخة السابقة (Phi-3-vision).  
سيتم تحديث النتائج الجديدة مع Phi-3.5-vision قريبًا.

### DocVQA (ملاحظة: Phi-3-vision)

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

طريقة التدريب | نوع البيانات | رتبة LoRA | ألفا LoRA | حجم الدُفعة | معدل التعلم | عدد العصور | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (ملاحظة: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

طريقة التدريب | نوع البيانات | رتبة LoRA | ألفا LoRA | حجم الدُفعة | معدل التعلم | عدد العصور | الدقة  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## قياس سرعة الأداء (ملاحظة: Phi-3-vision)

سيتم تحديث نتائج القياس الجديدة مع Phi-3.5-vision قريبًا.

تم إجراء قياس السرعة على مجموعة بيانات DocVQA. متوسط طول التسلسل في هذه المجموعة  
هو 2443.23 رمزًا (باستخدام `num_crops=16` لنموذج الصورة).

### 8x A100-80GB (Ampere)

طريقة التدريب | \# العقد | وحدات معالجة الرسومات | flash attention | حجم الدُفعة الفعلي | الإنتاجية (صورة/ثانية) | التسريع | أعلى ذاكرة GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

طريقة التدريب | \# العقد | وحدات معالجة الرسومات | flash attention | حجم الدُفعة الفعلي | الإنتاجية (صورة/ثانية) | التسريع | أعلى ذاكرة GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## المشكلات المعروفة

- لا يمكن تشغيل flash attention مع fp16 (يُنصح دائمًا باستخدام bf16 عندما يكون متاحًا، وجميع وحدات معالجة الرسومات التي تدعم flash attention تدعم أيضًا bf16).  
- لا يدعم حفظ نقاط التحقق الوسيطة واستئناف التدريب حتى الآن.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الهامة، يُنصح بالترجمة المهنية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.