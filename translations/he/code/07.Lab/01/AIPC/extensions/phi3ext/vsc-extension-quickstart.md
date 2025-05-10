<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:57:26+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "he"
}
-->
# ברוכים הבאים להרחבה שלכם ל-VS Code

## מה יש בתיקייה

* תיקייה זו מכילה את כל הקבצים הנדרשים להרחבה שלכם.
* `package.json` - זהו קובץ המניפסט שבו אתם מצהירים על ההרחבה והפקודה שלכם.
  * הפלאגין לדוגמה רושם פקודה ומגדיר את הכותרת ושם הפקודה שלה. עם המידע הזה VS Code יכול להציג את הפקודה בפלטת הפקודות. אין צורך לטעון את הפלאגין בשלב זה.
* `src/extension.ts` - זהו הקובץ הראשי שבו תספקו את מימוש הפקודה שלכם.
  * הקובץ מייצא פונקציה אחת, `activate`, שנקראת בפעם הראשונה שההרחבה מופעלת (במקרה זה על ידי הרצת הפקודה). בתוך פונקציית `activate` אנו קוראים ל-`registerCommand`.
  * אנו מעבירים את הפונקציה שמכילה את מימוש הפקודה כפרמטר השני ל-`registerCommand`.

## הגדרה

* התקינו את ההרחבות המומלצות (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, ו-dbaeumer.vscode-eslint)


## התחילו לעבוד מיד

* לחצו על `F5` כדי לפתוח חלון חדש עם ההרחבה שלכם טעונה.
* הריצו את הפקודה שלכם מפלטת הפקודות על ידי לחיצה על (`Ctrl+Shift+P` או `Cmd+Shift+P` ב-Mac) והקלדת `Hello World`.
* הגדירו נקודות עצירה בקוד שלכם בתוך `src/extension.ts` כדי לנפות את ההרחבה.
* מצאו פלט מההרחבה שלכם בקונסול הדיבוג.

## עשו שינויים

* ניתן להפעיל מחדש את ההרחבה מהסרגל דיבוג אחרי שינוי קוד ב-`src/extension.ts`.
* ניתן גם לטעון מחדש (`Ctrl+R` או `Cmd+R` ב-Mac) את חלון VS Code עם ההרחבה שלכם כדי לטעון את השינויים.


## חקרו את ה-API

* תוכלו לפתוח את כל סט ה-API שלנו כשאתם פותחים את הקובץ `node_modules/@types/vscode/index.d.ts`.

## הריצו בדיקות

* התקינו את [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* הריצו את משימת ה-"watch" דרך הפקודה **Tasks: Run Task**. ודאו שהיא פועלת, אחרת הבדיקות לא יזוהו.
* פתחו את תצוגת הבדיקות בסרגל הפעילויות ולחצו על כפתור "Run Test", או השתמשו בקיצור המקשים `Ctrl/Cmd + ; A`
* צפו בפלט תוצאות הבדיקה בתצוגת תוצאות הבדיקות.
* עשו שינויים ב-`src/test/extension.test.ts` או צרו קבצי בדיקה חדשים בתוך תיקיית `test`.
  * רץ הבדיקות שסופק יבחן רק קבצים שתואמים לדפוס השמות `**.test.ts`.
  * תוכלו ליצור תיקיות בתוך תיקיית `test` כדי לארגן את הבדיקות שלכם כפי שתרצו.

## המשיכו הלאה

* הקטינו את גודל ההרחבה ושפרו את זמן האתחול על ידי [אריזת ההרחבה שלכם](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [פרסמו את ההרחבה שלכם](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) בשוק ההרחבות של VS Code.
* אוטומטו בניות על ידי הגדרת [אינטגרציה רציפה](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.