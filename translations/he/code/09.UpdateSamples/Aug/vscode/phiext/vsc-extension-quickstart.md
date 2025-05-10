<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:39:30+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "he"
}
-->
# ברוכים הבאים להרחבה שלכם ל-VS Code

## מה יש בתיקייה

* תיקייה זו מכילה את כל הקבצים הדרושים להרחבה שלכם.
* `package.json` - זהו קובץ המניפסט שבו אתם מגדירים את ההרחבה והפקודה שלכם.
  * התוסף לדוגמה רושם פקודה ומגדיר את הכותרת ושם הפקודה שלה. עם המידע הזה VS Code יכול להציג את הפקודה בפלטת הפקודות. עדיין אין צורך לטעון את התוסף.
* `src/extension.ts` - זהו הקובץ הראשי שבו תספקו את המימוש של הפקודה שלכם.
  * הקובץ מייצא פונקציה אחת, `activate`, שנקראת בפעם הראשונה שההרחבה מופעלת (במקרה זה על ידי ביצוע הפקודה). בתוך הפונקציה `activate` אנו קוראים ל-`registerCommand`.
  * אנו מעבירים את הפונקציה שמכילה את מימוש הפקודה כפרמטר השני ל-`registerCommand`.

## הגדרה

* התקינו את ההרחבות המומלצות (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, ו-dbaeumer.vscode-eslint)


## התחילו מיד לפעול

* לחצו על `F5` כדי לפתוח חלון חדש עם ההרחבה שלכם טעונה.
* הריצו את הפקודה שלכם מפלטת הפקודות על ידי לחיצה על (`Ctrl+Shift+P` או `Cmd+Shift+P` ב-Mac) והקלדת `Hello World`.
* הגדירו נקודות עצירה בקוד שלכם בתוך `src/extension.ts` כדי לבצע דיבוג להרחבה.
* מצאו את הפלט מההרחבה בקונסול הדיבוג.

## עשו שינויים

* תוכלו להפעיל מחדש את ההרחבה מהסרגל דיבוג לאחר שינוי קוד ב-`src/extension.ts`.
* תוכלו גם לטעון מחדש (`Ctrl+R` או `Cmd+R` ב-Mac) את חלון VS Code עם ההרחבה שלכם כדי לטעון את השינויים.


## חקרו את ה-API

* תוכלו לפתוח את כל ה-API שלנו כאשר תפתחו את הקובץ `node_modules/@types/vscode/index.d.ts`.

## הריצו בדיקות

* התקינו את [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* הריצו את המשימה "watch" דרך הפקודה **Tasks: Run Task**. ודאו שהיא רצה, אחרת ייתכן שהבדיקות לא יזוהו.
* פתחו את תצוגת הבדיקות בסרגל הפעילות ולחצו על כפתור "Run Test", או השתמשו בקיצור המקשים `Ctrl/Cmd + ; A`
* ראו את הפלט של תוצאות הבדיקה בתצוגת תוצאות הבדיקות.
* עשו שינויים ב-`src/test/extension.test.ts` או צרו קבצי בדיקה חדשים בתוך תיקיית `test`.
  * רץ הבדיקות המסופק יבחן רק קבצים התואמים לתבנית השם `**.test.ts`.
  * תוכלו ליצור תיקיות בתוך תיקיית `test` כדי לארגן את הבדיקות שלכם כפי שתרצו.

## המשיכו הלאה

* הקטינו את גודל ההרחבה ושפרו את זמן ההפעלה על ידי [אריזת ההרחבה שלכם](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [פרסמו את ההרחבה שלכם](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) בשוק ההרחבות של VS Code.
* אוטומטו בניות על ידי הקמת [אינטגרציה רציפה](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. עבור מידע קריטי, מומלץ להיעזר בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.