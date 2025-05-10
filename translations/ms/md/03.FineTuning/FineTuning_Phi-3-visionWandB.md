<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:49:21+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "ms"
}
-->
# Phi-3-Vision-128K-Instruct סקירת פרויקט

## המודל

ה-Phi-3-Vision-128K-Instruct, מודל מולטימודלי קל משקל וחדיש, הוא הליבה של פרויקט זה. הוא חלק ממשפחת המודלים Phi-3 ותומך באורך הקשר של עד 128,000 טוקנים. המודל אומן על מערך נתונים מגוון הכולל נתונים סינתטיים ואתרי אינטרנט ציבוריים שעברו סינון קפדני, עם דגש על תוכן איכותי ומעמיק מבחינת היגיון. תהליך האימון כלל כוונון מפוקח ואופטימיזציה ישירה להעדפות, כדי להבטיח עמידה מדויקת בהוראות, וכן אמצעי בטיחות חזקים.

## יצירת נתוני דוגמה חיונית ממספר סיבות:

1. **בדיקות**: נתוני דוגמה מאפשרים לבדוק את האפליקציה בתרחישים שונים מבלי להשפיע על נתונים אמיתיים. זה חשוב במיוחד בשלבי פיתוח ובדיקות.

2. **כוונון ביצועים**: עם נתוני דוגמה המדמים את היקף ומורכבות הנתונים האמיתיים, ניתן לזהות צווארי בקבוק בביצועים ולשפר את האפליקציה בהתאם.

3. **פרוטוטייפינג**: ניתן להשתמש בנתוני דוגמה ליצירת אבטיפוסים ומוקאפים, שיעזרו להבין את דרישות המשתמש ולקבל משוב.

4. **ניתוח נתונים**: במדעי הנתונים, נתוני דוגמה משמשים לעיתים קרובות לניתוח ראשוני, אימון מודלים ובדיקת אלגוריתמים.

5. **אבטחה**: שימוש בנתוני דוגמה בסביבת פיתוח ובדיקות יכול לסייע למנוע דליפות בלתי מכוונות של נתונים רגישים.

6. **למידה**: אם אתם לומדים טכנולוגיה או כלי חדש, עבודה עם נתוני דוגמה מספקת דרך מעשית ליישם את מה שלמדתם.

זכרו, איכות נתוני הדוגמה משפיעה משמעותית על הפעילויות הללו. הנתונים צריכים להיות קרובים ככל האפשר לנתונים האמיתיים במבנה ובגיוון.

### יצירת נתוני דוגמה
[Generate DataSet Script](./CreatingSampleData.md)

## מערך הנתונים

דוגמה טובה למערך נתונים לדוגמה היא [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (זמין ב-Huggingface).  
מערך הנתונים של מוצרי Burberry כולל מידע על קטגוריית המוצר, מחיר וכותרת, עם סה"כ 3,040 שורות, כל אחת מייצגת מוצר ייחודי. מערך נתונים זה מאפשר לנו לבדוק את יכולת המודל להבין ולפרש נתונים חזותיים, וליצור טקסט תיאורי המתאר פרטים ויזואליים מורכבים ותכונות ספציפיות למותג.

**Note:** ניתן להשתמש בכל מערך נתונים הכולל תמונות.

## חשיבה מורכבת

המודל נדרש להסיק מסקנות לגבי מחירים ושמות בהתבסס אך ורק על התמונה. זה מחייב את המודל לא רק לזהות תכונות חזותיות אלא גם להבין את המשמעויות שלהן מבחינת ערך המוצר ומיתוג. על ידי יצירת תיאורים מדויקים מהתמונות, הפרויקט מדגים את הפוטנציאל בשילוב נתונים חזותיים לשיפור הביצועים והגמישות של מודלים ביישומים בעולם האמיתי.

## ארכיטקטורת Phi-3 Vision

ארכיטקטורת המודל היא גרסה מולטימודלית של Phi-3. הוא מעבד גם טקסט וגם תמונות, ומשלב את הקלטים האלה לרצף אחיד להבנה וליצירה מקיפה. המודל משתמש בשכבות הטמעה נפרדות לטקסט ולתמונות. טוקני הטקסט מומרצים לווקטורים צפופים, בעוד שהתמונות מעובדות דרך מודל ראייה CLIP כדי לחלץ תכונות. הטמעת התמונות מוקרנת למימדים התואמים את הטוקנים הטקסטואליים, כדי לאפשר שילוב חלק.

## שילוב הטמעות טקסט ותמונה

טוקנים מיוחדים בתוך רצף הטקסט מציינים היכן יש להכניס את הטמעות התמונות. במהלך העיבוד, טוקנים אלה מוחלפים בטמעות התמונה המתאימות, מה שמאפשר למודל לטפל בטקסט ותמונות כרצף אחד. הפקודה למערך הנתונים שלנו מעוצבת באמצעות הטוקן המיוחד <|image|> כך:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## דוגמת קוד
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.