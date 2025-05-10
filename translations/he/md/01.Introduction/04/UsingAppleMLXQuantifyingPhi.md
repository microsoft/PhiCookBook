<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:47:04+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "he"
}
-->
# **כימות Phi-3.5 באמצעות Apple MLX Framework**

MLX הוא מסגרת מערכים למחקר למידת מכונה על שבבי Apple, שמובאת לכם על ידי צוות מחקר למידת המכונה של Apple.

MLX נבנתה על ידי חוקרי למידת מכונה עבור חוקרי למידת מכונה. המסגרת מיועדת להיות ידידותית למשתמש, אך עדיין יעילה לאימון ולהפעלת מודלים. העיצוב של המסגרת עצמו גם פשוט מבחינה רעיונית. אנו מתכוונים להקל על החוקרים להרחיב ולשפר את MLX במטרה לחקור במהירות רעיונות חדשים.

ניתן להאיץ מודלים גדולים (LLMs) במכשירי Apple Silicon דרך MLX, ומודלים יכולים לפעול מקומית בנוחות רבה.

כעת Apple MLX Framework תומכת בהמרת כימות של Phi-3.5-Instruct (**Apple MLX Framework support**), Phi-3.5-Vision (**MLX-VLM Framework support**), ו-Phi-3.5-MoE (**Apple MLX Framework support**). בואו ננסה זאת בהמשך:

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
| 🚀 Lab-Introduce Phi-3.5 Instruct  | ללמוד כיצד להשתמש ב-Phi-3.5 Instruct עם מסגרת Apple MLX   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (תמונה) | ללמוד כיצד להשתמש ב-Phi-3.5 Vision לניתוח תמונות עם מסגרת Apple MLX     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | ללמוד כיצד להשתמש ב-Phi-3.5 MoE עם מסגרת Apple MLX  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **משאבים**

1. ללמוד על Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. מאגר GitHub של Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. מאגר GitHub של MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב למקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.