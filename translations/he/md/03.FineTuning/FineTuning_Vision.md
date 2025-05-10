<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:04:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "he"
}
-->
# מתכון לכיול מחדש של Phi-3.5-vision

זוהי התמיכה הרשמית בכיול מחדש של Phi-3.5-vision באמצעות ספריות huggingface.
אנא `cd` לתיקיית הקוד [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) לפני הרצת הפקודות הבאות.

## התקנה

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

## התחלה מהירה

אנו מספקים שני סקריפטים לדוגמה לכיול מחדש, אחד ל-DocVQA ואחד לסיווג ממים שנאה.

נבדק על חומרה מינימלית של 4x RTX8000 (48GB RAM לכל GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision תומך כעת רשמית בקלטים מרובי תמונות. הנה דוגמה לכיול מחדש של NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## מדריך שימוש

בהתאם לחומרה, המשתמשים יכולים לבחור באסטרטגיות כוונון שונות. אנו תומכים
בכוונון מלא (עם Deepspeed Zero-2) עם אפשרות להקפאת פרמטרי הראייה, ו-LoRA (כולל QLoRA ב-4 ביט).
באופן כללי, אנו ממליצים להשתמש בכיול מלא עם flash attention ו-bf16 מתי שניתן.

### מדריך להמרת מערך הנתונים המותאם שלך לפורמט הנדרש

אנו משתמשים במערך נתונים מינימלי לסיווג וידאו (תת-קבוצה של UCF-101) כדוגמה מקצה לקצה כדי להראות כיצד להמיר את מערך הנתונים המותאם שלך לפורמט הנדרש ולכוונן את Phi-3.5-vision עליו.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

הנתונים שהומרו ייראו כך:

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

לגבי התיעוד בפורמט `jsonl`, כל שורה צריכה להיות מילון כמו:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

שים לב ש-`conversations` היא רשימה, ולכן ניתן לתמוך בשיחה מרובת סבבים אם קיימים נתונים כאלו.

## בקשת הקצאת GPU ב-Azure

### דרישות מוקדמות

חשבון Azure עם תפקיד Contributor (או תפקיד אחר הכולל גישת Contributor).

אם אין לך חשבון Azure, צור [חשבון חינמי לפני שתתחיל](https://azure.microsoft.com).

### בקשת הגדלת הקצאה

ניתן להגיש בקשה להגדלת הקצאה ישירות מ-My quotas. עקוב אחר השלבים הבאים כדי לבקש הגדלה עבור הקצאה. בדוגמה זו, תוכל לבחור כל הקצאה שניתנת לשינוי במנוי שלך.

התחבר ל-[פורטל Azure](https://portal.azure.com).

הקלד "quotas" בתיבת החיפוש, ואז בחר Quotas.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

בעמוד Overview, בחר ספק, כמו Compute או AML.

**Note** עבור כל הספקים פרט ל-Compute, תראה עמודת Request increase במקום עמודת Adjustable המתוארת למטה. שם תוכל לבקש הגדלה להקצאה ספציפית, או ליצור בקשת תמיכה להגדלה.

בעמוד My quotas, תחת Quota name, בחר את ההקצאה שברצונך להגדיל. ודא שעמודת Adjustable מציגה Yes עבור הקצאה זו.

למעלה בעמוד, בחר New Quota Request, ואז בחר Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

בלוח New Quota Request, הזן ערך מספרי עבור הגבלת ההקצאה החדשה שלך, ואז בחר Submit.

הבקשה שלך תיבחן, ותקבל הודעה אם ניתן למלא אותה. זה בדרך כלל מתרחש תוך כמה דקות.

אם הבקשה לא תתמלא, תראה קישור ליצירת בקשת תמיכה. כשאתה משתמש בקישור זה, מהנדס תמיכה יסייע לך בבקשת ההגדלה.

## המלצות למכונות GPU של Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

הנה כמה דוגמאות:

### אם יש לך GPUs מדגם A100 או H100

כוונון מלא בדרך כלל נותן את הביצועים הטובים ביותר. תוכל להשתמש בפקודה הבאה לכיול מחדש של Phi-3-V בסיווג ממים שנאה.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### אם יש לך Standard_ND40rs_v2 עם 8x V100-32GB GPUs

עדיין אפשרי לבצע כוונון מלא של Phi-3-V בסיווג ממים שנאה. עם זאת, צפה ל
קצב עיבוד נמוך יותר משמעותית בהשוואה ל-A100 או H100 בגלל חוסר התמיכה ב-flash attention.
הדיוק יכול גם להיות מושפע מחוסר תמיכה ב-bf16 (משתמשים באימון precision מעורב fp16 במקום).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### אם אין לך גישה ל-GPUs במרכזי נתונים
LoRA עשוי להיות הבחירה היחידה שלך. תוכל להשתמש בפקודה הבאה לכיול מחדש של Phi-3-V בסיווג ממים שנאה.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

עבור Turing+ GPU, QLoRA נתמך

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## פרמטרים מומלצים ודיוק צפוי
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

שיטת אימון | מודל ראייה מוקפא | סוג נתונים | דרגת LoRA | אלפא LoRA | גודל אצווה | קצב למידה | אפוקים | דיוק
--- | --- | --- | --- | --- | --- | --- | --- | --- |
כוונון מלא |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
כוונון מלא | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
תוצאות LoRA יגיעו בקרוב |  |  |  |  |  |  |  |  |

### NOTE
התוצאות הבאות של DocVQA וממים שנאה מבוססות על הגרסה הקודמת (Phi-3-vision).
התוצאות החדשות עם Phi-3.5-vision יפורסמו בקרוב.

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

שיטת אימון | סוג נתונים | דרגת LoRA | אלפא LoRA | גודל אצווה | קצב למידה | אפוקים | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
כוונון מלא | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
כוונון מלא | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
מודל תמונה מוקפא| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
מודל תמונה מוקפא| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### ממים שנאה (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

שיטת אימון | סוג נתונים | דרגת LoRA | אלפא LoRA | גודל אצווה | קצב למידה | אפוקים | דיוק
--- | --- | --- | --- | --- | --- | --- | --- |
כוונון מלא | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
כוונון מלא | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
מודל תמונה מוקפא| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
מודל תמונה מוקפא| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## מדדי מהירות (NOTE: Phi-3-vision)

תוצאות מדידה חדשות עם Phi-3.5-vision יפורסמו בקרוב.

מדידת המהירות מתבצעת על מערך הנתונים DocVQA. אורך רצף ממוצע במערך זה
הוא 2443.23 טוקנים (משתמשים ב-`num_crops=16` עבור מודל התמונה).

### 8x A100-80GB (Ampere)

שיטת אימון | \# צמתים | GPUs | flash attention | גודל אצווה אפקטיבי | תפוקה (תמונות/שניה) | מהירות יחסית | זיכרון GPU שיא (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
כוונון מלא | 1 | 8 |  | 64 | 5.041 |  1x | ~42
כוונון מלא | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
כוונון מלא | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
כוונון מלא | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
מודל תמונה מוקפא | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
מודל תמונה מוקפא | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

שיטת אימון | \# צמתים | GPUs | flash attention | גודל אצווה אפקטיבי | תפוקה (תמונות/שניה) | מהירות יחסית | זיכרון GPU שיא (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
כוונון מלא | 1 | 8 | | 64 | 2.462 |  1x | ~32
כוונון מלא | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
כוונון מלא | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
מודל תמונה מוקפא | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## בעיות ידועות

- לא ניתן להריץ flash attention עם fp16 (bf16 מומלץ תמיד כשזמין, וכל GPUs התומכים ב-flash attention גם תומכים ב-bf16).
- עדיין לא תומך בשמירת נקודות בדיקה ביניים והמשך אימון.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לכל אי הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.