<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-07-16T16:44:37+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "he"
}
-->
# ברוכים הבאים להרחבה שלכם ל-VS Code

## מה יש בתיקייה

* תיקייה זו מכילה את כל הקבצים הדרושים להרחבה שלכם.
* `package.json` - זהו קובץ המניפסט שבו אתם מגדירים את ההרחבה והפקודה שלכם.
  * התוסף לדוגמה רושם פקודה ומגדיר את הכותרת ושם הפקודה שלה. עם המידע הזה VS Code יכול להציג את הפקודה בפלטת הפקודות. עדיין אין צורך לטעון את התוסף.
* `src/extension.ts` - זהו הקובץ הראשי שבו תספקו את מימוש הפקודה שלכם.
  * הקובץ מייצא פונקציה אחת, `activate`, שנקראת בפעם הראשונה שההרחבה מופעלת (במקרה זה על ידי הרצת הפקודה). בתוך פונקציית `activate` אנו קוראים ל-`registerCommand`.
  * אנו מעבירים את הפונקציה שמכילה את מימוש הפקודה כפרמטר השני ל-`registerCommand`.

## התקנה

* התקינו את ההרחבות המומלצות (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, ו-dbaeumer.vscode-eslint)

## התחילו לעבוד מיד

* לחצו על `F5` כדי לפתוח חלון חדש עם ההרחבה שלכם טעונה.
* הריצו את הפקודה שלכם מפלטת הפקודות על ידי לחיצה על (`Ctrl+Shift+P` או `Cmd+Shift+P` במק) והקלדת `Hello World`.
* הגדירו נקודות עצירה בקוד שלכם בתוך `src/extension.ts` כדי לנפות שגיאות בהרחבה.
* מצאו את הפלט מההרחבה שלכם בקונסולת הדיבוג.

## בצעו שינויים

* תוכלו להפעיל מחדש את ההרחבה מסרגל הכלים לדיבוג לאחר שינוי בקוד ב-`src/extension.ts`.
* תוכלו גם לטעון מחדש (`Ctrl+R` או `Cmd+R` במק) את חלון VS Code עם ההרחבה שלכם כדי לטעון את השינויים.

## חקרו את ה-API

* תוכלו לפתוח את כל ה-API שלנו כשאתם פותחים את הקובץ `node_modules/@types/vscode/index.d.ts`.

## הריצו בדיקות

* התקינו את [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* הריצו את המשימה "watch" דרך הפקודה **Tasks: Run Task**. ודאו שהיא רצה, אחרת ייתכן שהבדיקות לא יזוהו.
* פתחו את תצוגת הבדיקות מסרגל הפעילויות ולחצו על כפתור "Run Test", או השתמשו בקיצור המקשים `Ctrl/Cmd + ; A`
* ראו את תוצאות הבדיקה בתצוגת Test Results.
* בצעו שינויים ב-`src/test/extension.test.ts` או צרו קבצי בדיקה חדשים בתוך תיקיית `test`.
  * רץ הבדיקות שסופק יזהה רק קבצים שתואמים לתבנית השם `**.test.ts`.
  * תוכלו ליצור תיקיות בתוך תיקיית `test` כדי לארגן את הבדיקות שלכם כפי שתרצו.

## המשיכו הלאה

* הקטינו את גודל ההרחבה ושפרו את זמן ההפעלה על ידי [אריזת ההרחבה שלכם](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [פרסמו את ההרחבה שלכם](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) בשוק ההרחבות של VS Code.
* אוטומטו בניות על ידי הגדרת [אינטגרציה רציפה](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.