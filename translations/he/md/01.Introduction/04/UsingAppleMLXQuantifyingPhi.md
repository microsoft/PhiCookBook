<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:56:02+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "he"
}
-->
# **כימות Phi-3.5 באמצעות מסגרת Apple MLX**

MLX היא מסגרת מערכים למחקר למידת מכונה על שבבי Apple, מבית מחקר למידת המכונה של Apple.

MLX עוצבה על ידי חוקרי למידת מכונה עבור חוקרי למידת מכונה. המסגרת מיועדת להיות ידידותית למשתמש, אך עדיין יעילה לאימון והפעלת מודלים. העיצוב של המסגרת עצמה גם פשוט מבחינה רעיונית. אנו שואפים להקל על החוקרים להרחיב ולשפר את MLX במטרה לחקור רעיונות חדשים במהירות.

ניתן להאיץ LLMs במכשירי Apple Silicon באמצעות MLX, והמודלים יכולים לפעול מקומית בנוחות רבה.

כעת מסגרת Apple MLX תומכת בהמרת כימות של Phi-3.5-Instruct(**תמיכה במסגרת Apple MLX**), Phi-3.5-Vision(**תמיכה במסגרת MLX-VLM**), ו-Phi-3.5-MoE(**תמיכה במסגרת Apple MLX**). בואו ננסה זאת בהמשך:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 דוגמאות ל-Phi-3.5 עם Apple MLX**

| מעבדות    | הקדמה | מעבר |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | למדו כיצד להשתמש ב-Phi-3.5 Instruct עם מסגרת Apple MLX   |  [מעבר](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (תמונה) | למדו כיצד להשתמש ב-Phi-3.5 Vision לניתוח תמונות עם מסגרת Apple MLX     |  [מעבר](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | למדו כיצד להשתמש ב-Phi-3.5 MoE עם מסגרת Apple MLX  |  [מעבר](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **משאבים**

1. למדו על מסגרת Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. מאגר GitHub של Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. מאגר GitHub של MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.