**כיוונון עדין של Phi-3 עם QLoRA**

כיוונון עדין של מודל השפה Phi-3 Mini של מיקרוסופט באמצעות [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA יסייע בשיפור ההבנה השיחית ויצירת התגובות.

כדי לטעון מודלים ב-4 ביט עם transformers ו-bitsandbytes, יש להתקין את accelerate ו-transformers מהמקור ולוודא שיש ברשותכם את הגרסה העדכנית ביותר של ספריית bitsandbytes.

**דוגמאות**
- [למידע נוסף עם המחברת לדוגמה הזו](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [דוגמה לסקריפט כיוונון עדין בפייתון](../../../../code/03.Finetuning/FineTrainingScript.py)
- [דוגמה לכיוונון עדין ב-Hugging Face Hub עם LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [דוגמה לכיוונון עדין ב-Hugging Face Hub עם QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.