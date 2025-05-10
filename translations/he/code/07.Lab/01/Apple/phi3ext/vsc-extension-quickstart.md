<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:09:00+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "he"
}
-->
# ברוכים הבאים לתוסף ה-VS Code שלכם

## מה יש בתיקייה

* תיקייה זו מכילה את כל הקבצים הדרושים לתוסף שלכם.
* `package.json` - זהו קובץ המניפסט שבו אתם מצהירים על התוסף והפקודה שלכם.
  * הפלאגין לדוגמה רושם פקודה ומגדיר את הכותרת ושם הפקודה שלה. עם המידע הזה VS Code יכול להציג את הפקודה בפלטת הפקודות. אין צורך לטעון את הפלאגין בשלב זה.
* `src/extension.ts` - זהו הקובץ הראשי שבו תספקו את המימוש של הפקודה שלכם.
  * הקובץ מייצא פונקציה אחת, `activate`, שנקראת בפעם הראשונה שהתוסף מופעל (במקרה הזה על ידי הרצת הפקודה). בתוך פונקציית `activate` קוראים ל-`registerCommand`.
  * אנו מעבירים את הפונקציה שמכילה את מימוש הפקודה כפרמטר השני ל-`registerCommand`.

## הגדרות

* התקינו את התוספים המומלצים (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, ו-dbaeumer.vscode-eslint)


## התחילו לעבוד מיד

* לחצו על `F5` כדי לפתוח חלון חדש עם התוסף שלכם טעון.
* הריצו את הפקודה שלכם מפלטת הפקודות על ידי לחיצה על (`Ctrl+Shift+P` או `Cmd+Shift+P` במק) והקלדת `Hello World`.
* הגדירו נקודות עצירה בקוד שלכם בתוך `src/extension.ts` כדי לנפות שגיאות בתוסף.
* מצאו את הפלט של התוסף שלכם בקונסולת הדיבאג.

## עשו שינויים

* תוכלו להפעיל מחדש את התוסף מסרגל הדיבאג לאחר שינוי קוד ב-`src/extension.ts`.
* תוכלו גם לטעון מחדש (`Ctrl+R` או `Cmd+R` במק) את חלון ה-VS Code עם התוסף שלכם כדי לטעון את השינויים.


## חקרו את ה-API

* תוכלו לפתוח את כל סט ה-API שלנו כאשר תפתחו את הקובץ `node_modules/@types/vscode/index.d.ts`.

## הריצו בדיקות

* התקינו את [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* הריצו את המשימה "watch" דרך הפקודה **Tasks: Run Task**. וודאו שהיא פועלת, אחרת ייתכן שהבדיקות לא יזוהו.
* פתחו את תצוגת הבדיקות בסרגל הפעילות ולחצו על כפתור "Run Test", או השתמשו בקיצור המקשים `Ctrl/Cmd + ; A`
* ראו את תוצאות הבדיקות בתצוגת תוצאות הבדיקות.
* עשו שינויים ב-`src/test/extension.test.ts` או צרו קבצי בדיקה חדשים בתוך תיקיית `test`.
  * רץ הבדיקות שסופק יזהה רק קבצים התואמים לתבנית השם `**.test.ts`.
  * תוכלו ליצור תיקיות בתוך תיקיית `test` כדי לארגן את הבדיקות שלכם בכל דרך שתרצו.

## המשיכו הלאה

* הקטינו את גודל התוסף ושפרו את זמן האתחול על ידי [אריזת התוסף](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [פרסמו את התוסף שלכם](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) בשוק התוספים של VS Code.
* אוטומטו בניות על ידי הגדרת [אינטגרציה רציפה](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור המוסמך. למידע קריטי מומלץ להשתמש בתרגום מקצועי של מתרגם אנושי. אנו לא אחראים לכל אי-הבנה או פרשנות שגויה הנובעים מהשימוש בתרגום זה.