<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:35:06+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "fa"
}
-->
# دستورالعمل فاین‌تیونینگ Phi-3.5-vision

این پشتیبانی رسمی فاین‌تیونینگ Phi-3.5-vision با استفاده از کتابخانه‌های huggingface است.  
لطفاً قبل از اجرای دستورات زیر، به دایرکتوری کد [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) بروید (`cd`).

## نصب

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

## شروع سریع

دو اسکریپت نمونه فاین‌تیونینگ ارائه می‌دهیم، یکی برای DocVQA و دیگری برای طبقه‌بندی میم‌های نفرت‌انگیز.

سخت‌افزار حداقلی تست شده: ۴ عدد RTX8000 (هر کارت گرافیک ۴۸ گیگابایت رم)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision اکنون به طور رسمی از ورودی‌های چندتصویری پشتیبانی می‌کند. در اینجا نمونه‌ای برای فاین‌تیونینگ NLVR2 آورده شده است.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## راهنمای استفاده

بسته به سخت‌افزار، کاربران ممکن است استراتژی‌های مختلف فاین‌تیونینگ را انتخاب کنند. ما از  
فاین‌تیونینگ کامل (با Deepspeed Zero-2) با امکان فریز کردن پارامترهای بینایی، و LoRA (شامل QLoRA با دقت ۴بیتی) پشتیبانی می‌کنیم.  
به طور کلی، توصیه می‌کنیم هر زمان ممکن است از فاین‌تیونینگ کامل با flash attention و bf16 استفاده کنید.

### راهنمای تبدیل دیتاست سفارشی شما به فرمت مورد نیاز

ما از یک دیتاست حداقلی طبقه‌بندی ویدیو (زیرمجموعه‌ای از UCF-101) به عنوان مثال انتها به انتها استفاده می‌کنیم تا نشان دهیم چگونه دیتاست سفارشی خود را به فرمت مورد نیاز تبدیل کرده و Phi-3.5-vision را روی آن فاین‌تیون کنیم.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

داده‌های تبدیل شده به این شکل خواهند بود:

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

برای حاشیه‌نویسی `jsonl`، هر خط باید یک دیکشنری مانند زیر باشد:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

توجه داشته باشید که `conversations` یک لیست است، بنابراین مکالمات چندمرحله‌ای در صورت وجود چنین داده‌ای پشتیبانی می‌شود.

## درخواست سهمیه GPU در Azure

### پیش‌نیازها

یک حساب Azure با نقش Contributor (یا نقش دیگری که دسترسی Contributor را شامل شود).

اگر حساب Azure ندارید، [قبل از شروع یک حساب رایگان بسازید](https://azure.microsoft.com).

### درخواست افزایش سهمیه

می‌توانید درخواست افزایش سهمیه را مستقیماً از بخش My quotas ارسال کنید. مراحل زیر را برای درخواست افزایش سهمیه دنبال کنید. در این مثال، می‌توانید هر سهمیه قابل تنظیم در اشتراک خود را انتخاب کنید.

وارد [پورتال Azure](https://portal.azure.com) شوید.

در کادر جستجو "quotas" را وارد کنید و سپس Quotas را انتخاب کنید.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

در صفحه Overview، یک ارائه‌دهنده مانند Compute یا AML را انتخاب کنید.

**توجه** برای همه ارائه‌دهندگان به جز Compute، به جای ستون Adjustable، ستون Request increase را خواهید دید. در آنجا می‌توانید برای سهمیه خاصی درخواست افزایش دهید یا درخواست پشتیبانی برای افزایش ایجاد کنید.

در صفحه My quotas، زیر Quota name، سهمیه‌ای که می‌خواهید افزایش دهید را انتخاب کنید. مطمئن شوید ستون Adjustable برای این سهمیه مقدار Yes را نشان می‌دهد.

نزدیک بالای صفحه، New Quota Request را انتخاب کنید، سپس Enter a new limit را انتخاب کنید.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

در پنل New Quota Request، مقدار عددی برای محدودیت جدید سهمیه خود وارد کنید، سپس Submit را بزنید.

درخواست شما بررسی خواهد شد و در صورت امکان، به شما اطلاع داده می‌شود. این معمولاً ظرف چند دقیقه انجام می‌شود.

اگر درخواست شما پذیرفته نشد، لینکی برای ایجاد درخواست پشتیبانی مشاهده خواهید کرد. با استفاده از این لینک، یک مهندس پشتیبانی به شما در درخواست افزایش کمک خواهد کرد.

## پیشنهادات SKU ماشین‌های GPU محاسباتی Azure

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

چند مثال:

### اگر GPUهای A100 یا H100 دارید

فاین‌تیونینگ کامل معمولاً بهترین عملکرد را ارائه می‌دهد. می‌توانید از دستور زیر برای فاین‌تیونینگ Phi-3-V در طبقه‌بندی میم‌های نفرت‌انگیز استفاده کنید.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### اگر ۸ عدد Standard_ND40rs_v2 با V100-32GB دارید

هنوز امکان فاین‌تیونینگ کامل Phi-3-V روی طبقه‌بندی میم‌های نفرت‌انگیز وجود دارد. با این حال، به دلیل عدم پشتیبانی از flash attention، انتظار عملکرد بسیار پایین‌تر نسبت به GPUهای A100 یا H100 را داشته باشید.  
دقت نیز ممکن است به دلیل عدم پشتیبانی از bf16 تحت تأثیر قرار گیرد (در عوض آموزش با دقت ترکیبی fp16 استفاده می‌شود).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### اگر به GPUهای دیتاسنتر دسترسی ندارید

LoRA ممکن است تنها گزینه شما باشد. می‌توانید از دستور زیر برای فاین‌تیونینگ Phi-3-V روی طبقه‌بندی میم‌های نفرت‌انگیز استفاده کنید.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

برای GPUهای Turing+، QLoRA پشتیبانی می‌شود.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ابرپارامترهای پیشنهادی و دقت مورد انتظار

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

روش آموزش | مدل بینایی فریز شده | نوع داده | رتبه LoRA | آلفای LoRA | اندازه بچ | نرخ یادگیری | اپوک‌ها | دقت  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
نتایج LoRA به زودی می‌آید |  |  |  |  |  |  |  |  |

### توجه  
نتایج زیر برای DocVQA و میم‌های نفرت‌انگیز بر اساس نسخه قبلی (Phi-3-vision) است.  
نتایج جدید با Phi-3.5-vision به زودی به‌روزرسانی خواهد شد.

### DocVQA (توجه: Phi-3-vision)

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

روش آموزش | نوع داده | رتبه LoRA | آلفای LoRA | اندازه بچ | نرخ یادگیری | اپوک‌ها | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
مدل تصویر فریز شده | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
مدل تصویر فریز شده | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### میم‌های نفرت‌انگیز (توجه: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

روش آموزش | نوع داده | رتبه LoRA | آلفای LoRA | اندازه بچ | نرخ یادگیری | اپوک‌ها | دقت  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
مدل تصویر فریز شده | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
مدل تصویر فریز شده | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## بنچمارک سرعت (توجه: Phi-3-vision)

نتایج جدید بنچمارک با Phi-3.5-vision به زودی به‌روزرسانی خواهد شد.

بنچمارک سرعت روی دیتاست DocVQA انجام شده است. طول متوسط توکن‌های این دیتاست  
۲۴۴۳.۲۳ است (با استفاده از `num_crops=16` برای مدل تصویر).

### ۸ عدد A100-80GB (Ampere)

روش آموزش | تعداد نودها | تعداد GPUها | flash attention | اندازه بچ مؤثر | توان عملیاتی (تصویر/ثانیه) | سرعت نسبی | حداکثر حافظه GPU (گیگابایت)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42 |  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 |  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 |  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 |  
مدل تصویر فریز شده | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29 |  
مدل تصویر فریز شده | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 |  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50 |  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 |  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32 |  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 |

### ۸ عدد V100-32GB (Volta)

روش آموزش | تعداد نودها | تعداد GPUها | flash attention | اندازه بچ مؤثر | توان عملیاتی (تصویر/ثانیه) | سرعت نسبی | حداکثر حافظه GPU (گیگابایت)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32 |  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32 |  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32 |  
مدل تصویر فریز شده | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27 |  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30 |

## مشکلات شناخته شده

- امکان اجرای flash attention با fp16 وجود ندارد (همیشه bf16 توصیه می‌شود و تمام GPUهایی که از flash attention پشتیبانی می‌کنند، از bf16 نیز پشتیبانی می‌کنند).  
- هنوز امکان ذخیره چک‌پوینت‌های میانی و ادامه آموزش وجود ندارد.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.