<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:46:51+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "he"
}
-->
# **כיוונון עדין של Phi-3 עם Lora**

כיוונון עדין של מודל השפה Phi-3 Mini של מיקרוסופט באמצעות [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) על מאגר נתוני הוראות שיחה מותאם אישית.

LORA תעזור לשפר את ההבנה השיחית ואת יצירת התגובות.

## מדריך שלב-אחר-שלב כיצד לכוונן עדין את Phi-3 Mini:

**ייבוא והגדרות**

התקנת loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

התחל בייבוא ספריות נחוצות כמו datasets, transformers, peft, trl ו-torch.
הגדר לוגים למעקב אחרי תהליך האימון.

ניתן לבחור להתאים שכבות מסוימות על ידי החלפתן בגרסאות המיושמות ב-loralib. כרגע אנו תומכים ב-nn.Linear, nn.Embedding ו-nn.Conv2d בלבד. בנוסף, אנו תומכים ב-MergedLinear במקרים בהם nn.Linear אחד מייצג יותר משכבה אחת, כמו בכמה מימושים של ההטלה qkv בתשומת לב (ראו הערות נוספות לפרטים).

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

לפני תחילת לולאת האימון, סמן את פרמטרי LoRA בלבד כניתנים לאימון.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

בעת שמירת נקודת בדיקה, צור state_dict המכיל רק את פרמטרי LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

בעת טעינת נקודת בדיקה עם load_state_dict, הקפד להגדיר strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

כעת ניתן להמשיך באימון כרגיל.

**היפרפרמטרים**

הגדר שני מילונים: training_config ו-peft_config. training_config כולל היפרפרמטרים לאימון, כגון קצב למידה, גודל אצווה והגדרות לוגים.

peft_config מפרט פרמטרים הקשורים ל-LoRA כמו דרגה, dropout וסוג המשימה.

**טעינת מודל וטוקנייזר**

ציין את הנתיב למודל Phi-3 המאומן מראש (למשל "microsoft/Phi-3-mini-4k-instruct"). קבע הגדרות מודל, כולל שימוש במטמון, סוג נתונים (bfloat16 לדיוק מעורב) ומימוש התשומת לב.

**אימון**

כוונן עדין את מודל Phi-3 באמצעות מאגר הנתונים המותאם להוראות שיחה. נצל את הגדרות LoRA מ-peft_config להתאמה יעילה. עקוב אחרי התקדמות האימון באמצעות אסטרטגיית הלוגינג שנקבעה.
הערכה ושמירה: הערך את המודל המכוונן עדין.
שמור נקודות בדיקה במהלך האימון לשימוש עתידי.

**דוגמאות**
- [למידע נוסף עם דף המחברת הזה](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [דוגמה לסקריפט כיוונון עדין בפייתון](../../../../code/03.Finetuning/FineTrainingScript.py)
- [דוגמה לכיוונון עדין עם LORA דרך Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [דוגמת כרטיס מודל Hugging Face - דוגמת כיוונון עדין עם LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [דוגמה לכיוונון עדין עם QLORA דרך Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעים מהשימוש בתרגום זה.