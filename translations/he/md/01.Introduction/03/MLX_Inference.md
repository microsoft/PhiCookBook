<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:16:07+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "he"
}
-->
# **אינפרנס Phi-3 עם מסגרת Apple MLX**

## **מהי מסגרת MLX**

MLX היא מסגרת מערכים למחקר למידת מכונה על שבבי Apple, מבית מחקר למידת המכונה של Apple.

MLX עוצבה על ידי חוקרי למידת מכונה עבור חוקרי למידת מכונה. המסגרת מיועדת להיות נוחה לשימוש, אך עדיין יעילה לאימון ופריסת מודלים. העיצוב של המסגרת עצמו גם הוא פשוט במובן הרעיוני. אנו שואפים להקל על החוקרים להרחיב ולשפר את MLX במטרה לחקור רעיונות חדשים במהירות.

ניתן להאיץ מודלים גדולים (LLMs) במכשירי Apple Silicon באמצעות MLX, והפעלת המודלים מקומית נעשית בנוחות רבה.

## **שימוש ב-MLX לאינפרנס Phi-3-mini**

### **1. הגדרת סביבת MLX שלך**

1. Python 3.11.x  
2. התקנת ספריית MLX  


```bash

pip install mlx-lm

```

### **2. הפעלת Phi-3-mini בטרמינל עם MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

התוצאה (הסביבה שלי היא Apple M1 Max, 64GB) היא

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.he.png)

### **3. קוואנטיזציה של Phi-3-mini עם MLX בטרמינל**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** ניתן לבצע קוואנטיזציה למודל באמצעות mlx_lm.convert, והקוואנטיזציה המוגדרת כברירת מחדל היא INT4. בדוגמה זו הקוואנטיזציה היא ל-INT4.

ניתן לבצע קוואנטיזציה למודל באמצעות mlx_lm.convert, והקוואנטיזציה המוגדרת כברירת מחדל היא INT4. בדוגמה זו מתבצעת קוואנטיזציה של Phi-3-mini ל-INT4. לאחר הקוואנטיזציה, המודל יישמר בתיקיית ברירת המחדל ./mlx_model

ניתן לבדוק את המודל המקוואנטז עם MLX מהטרמינל


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

התוצאה היא

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.he.png)


### **4. הפעלת Phi-3-mini עם MLX ב-Jupyter Notebook**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.he.png)

***Note:*** אנא קראו את הדוגמה הזו [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **משאבים**

1. למידה על מסגרת Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. מאגר GitHub של Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור המוסמך. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.