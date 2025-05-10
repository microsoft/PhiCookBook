<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:09:25+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "ms"
}
-->
# ברוכים הבאים לתוסף ה-VS Code שלכם

## מה יש בתיקייה

* תיקייה זו מכילה את כל הקבצים הנדרשים לתוסף שלכם.
* `package.json` - זהו קובץ המניפסט שבו אתם מגדירים את התוסף והפקודה שלכם.
  * התוסף לדוגמה רושם פקודה ומגדיר את הכותרת ושם הפקודה שלה. עם המידע הזה VS Code יכול להציג את הפקודה בפלטת הפקודות. עדיין אין צורך לטעון את התוסף.
* `src/extension.ts` - זהו הקובץ הראשי שבו תספקו את מימוש הפקודה שלכם.
  * הקובץ מייצא פונקציה אחת, `activate`, שנקראת בפעם הראשונה שהתוסף מופעל (במקרה זה בעת ביצוע הפקודה). בתוך פונקציית `activate` אנו קוראים ל-`registerCommand`.
  * אנו מעבירים את הפונקציה שמכילה את מימוש הפקודה כפרמטר השני ל-`registerCommand`.

## התקנה

* התקינו את התוספים המומלצים (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, ו-dbaeumer.vscode-eslint)


## התחילו לעבוד מיד

* לחצו על `F5` כדי לפתוח חלון חדש עם התוסף שלכם טעון.
* הריצו את הפקודה שלכם מפלטת הפקודות על ידי לחיצה על (`Ctrl+Shift+P` או `Cmd+Shift+P` ב-Mac) והקלדת `Hello World`.
* הגדירו נקודות עצירה בקוד שלכם בתוך `src/extension.ts` כדי לנפות באגים בתוסף.
* מצאו את הפלט של התוסף שלכם בקונסולת הניפוי.

## בצעו שינויים

* תוכלו להפעיל מחדש את התוסף מסרגל הכלים לניפוי לאחר שינוי קוד ב-`src/extension.ts`.
* תוכלו גם לטעון מחדש (`Ctrl+R` או `Cmd+R` ב-Mac) את חלון ה-VS Code עם התוסף כדי לטעון את השינויים שלכם.


## חקרו את ה-API

* תוכלו לפתוח את כל מערך ה-API שלנו כשאתם פותחים את הקובץ `node_modules/@types/vscode/index.d.ts`.

## הרצת בדיקות

* התקינו את [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* הריצו את המשימה "watch" דרך הפקודה **Tasks: Run Task**. ודאו שהיא רצה, אחרת ייתכן שהבדיקות לא יזוהו.
* פתחו את תצוגת הבדיקות בסרגל הפעילויות ולחצו על כפתור "Run Test", או השתמשו בקיצור המקשים `Ctrl/Cmd + ; A`
* צפו בפלט תוצאות הבדיקות בתצוגת Test Results.
* בצעו שינויים ב-`src/test/extension.test.ts` או צרו קבצי בדיקה חדשים בתוך תיקיית `test`.
  * רץ הבדיקות שסופק יזהה רק קבצים שתואמים לתבנית השם `**.test.ts`.
  * תוכלו ליצור תיקיות בתוך תיקיית `test` כדי לארגן את הבדיקות שלכם איך שתרצו.

## המשיכו הלאה

* הקטינו את גודל התוסף ושפרו את זמן ההפעלה על ידי [אריזת התוסף שלכם](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [פרסמו את התוסף שלכם](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) בשוק התוספים של VS Code.
* אוטומטו בניות על ידי הגדרת [אינטגרציה רציפה](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.