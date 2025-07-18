<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:33:49+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "he"
}
-->
# **כיוונון עדין של Phi-3 עם Lora**

כיוונון עדין של מודל השפה Phi-3 Mini של מיקרוסופט באמצעות [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) על מערך נתונים מותאם להוראות שיחה.

LORA תסייע בשיפור ההבנה השיחתית ויצירת התגובות.

## מדריך שלב אחר שלב כיצד לכוונן עדין את Phi-3 Mini:

**ייבוא והגדרות**

התקנת loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

התחילו בייבוא הספריות הנחוצות כמו datasets, transformers, peft, trl ו-torch.  
הגדירו רישום לוגים למעקב אחר תהליך האימון.

ניתן לבחור להתאים שכבות מסוימות על ידי החלפתן בגרסאות המיושמות ב-loralib. כרגע אנו תומכים רק ב-nn.Linear, nn.Embedding ו-nn.Conv2d. בנוסף, אנו תומכים ב-MergedLinear למקרים שבהם nn.Linear אחד מייצג יותר משכבה אחת, כמו במימושים מסוימים של פרויקט הקשב qkv (ראו הערות נוספות לפרטים).

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

לפני תחילת לולאת האימון, סמנו רק את פרמטרי LoRA כניתנים לאימון.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

בעת שמירת נקודת בדיקה, צרו state_dict שמכיל רק את פרמטרי LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

בעת טעינת נקודת בדיקה באמצעות load_state_dict, ודאו שהפרמטר strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

כעת ניתן להמשיך באימון כרגיל.

**היפרפרמטרים**

הגדירו שני מילונים: training_config ו-peft_config.  
training_config כולל היפרפרמטרים לאימון, כמו שיעור למידה, גודל אצווה והגדרות רישום לוגים.

peft_config מגדיר פרמטרים הקשורים ל-LoRA כמו דרגה, dropout וסוג המשימה.

**טעינת מודל וטוקנייזר**

ציינו את הנתיב למודל Phi-3 המאומן מראש (למשל, "microsoft/Phi-3-mini-4k-instruct").  
הגדירו את הגדרות המודל, כולל שימוש במטמון, סוג הנתונים (bfloat16 לדיוק מעורב) ומימוש הקשב.

**אימון**

כווננו עדין את מודל Phi-3 באמצעות מערך הנתונים המותאם להוראות שיחה.  
השתמשו בהגדרות LoRA מתוך peft_config להתאמה יעילה.  
עקבו אחר התקדמות האימון באמצעות אסטרטגיית הרישום שהוגדרה.  
הערכה ושמירה: העריכו את המודל המכוונן.  
שמרו נקודות בדיקה במהלך האימון לשימוש עתידי.

**דוגמאות**
- [למידע נוסף עם פנקס דוגמא זה](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [דוגמה לסקריפט כיוונון עדין בפייתון](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [דוגמה לכיוונון עדין עם LORA ב-Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [דוגמה לכרטיס מודל Hugging Face - דוגמת כיוונון עדין עם LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [דוגמה לכיוונון עדין עם QLORA ב-Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.