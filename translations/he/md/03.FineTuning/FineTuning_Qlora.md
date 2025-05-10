<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:51+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "he"
}
-->
**כיוונון עדין של Phi-3 עם QLoRA**

כיוונון עדין של מודל השפה Phi-3 Mini של Microsoft באמצעות [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA מסייע בשיפור ההבנה השיחית ויצירת התגובות.

כדי לטעון מודלים ב-4 ביט עם transformers ו-bitsandbytes, יש להתקין את accelerate ו-transformers מהמקור ולוודא שיש לכם את הגרסה העדכנית ביותר של ספריית bitsandbytes.

**דוגמאות**
- [למידע נוסף עם המחברת לדוגמה הזו](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [דוגמה לסקריפט כיוונון עדין בפייתון](../../../../code/03.Finetuning/FineTrainingScript.py)
- [דוגמה לכיוונון עדין ב-Hugging Face Hub עם LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [דוגמה לכיוונון עדין ב-Hugging Face Hub עם QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפת המקור כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי של אדם. אנו לא נישא באחריות לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.