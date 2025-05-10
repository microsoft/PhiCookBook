<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-05-09T15:18:06+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "ms"
}
-->
# **Introduce Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) הוא כלי אוטומציה ויזואלי המאפשר למשתמשים ליצור תהליכי עבודה אוטומטיים באמצעות תבניות מוכנות ומחברים מותאמים אישית. הוא מיועד לאפשר למפתחים ואנליסטים עסקיים לבנות במהירות תהליכים אוטומטיים למשימות כמו ניהול נתונים, שיתוף פעולה ואופטימיזציה של תהליכים. עם Prompt Flow, המשתמשים יכולים בקלות לחבר שירותים, יישומים ומערכות שונות, ולאוטומט תהליכים עסקיים מורכבים.

Microsoft Prompt Flow תוכנן לייעל את מחזור הפיתוח המלא של יישומי AI המופעלים על ידי מודלים שפתיים גדולים (LLMs). בין אם אתם בשלב הרעיוני, הפיתוח, הבדיקה, ההערכה או הפריסה של יישומים מבוססי LLM, Prompt Flow מפשט את התהליך ומאפשר לכם לבנות אפליקציות LLM באיכות ייצור.

## הנה התכונות והיתרונות המרכזיים של שימוש ב-Microsoft Prompt Flow:

**חווית עריכה אינטראקטיבית**

Prompt Flow מספק ייצוג ויזואלי של מבנה ה-flow שלכם, מה שמקל על הבנת וניהול הפרויקטים.
הוא מציע חווית קידוד בסגנון מחברת (notebook) לפיתוח ו-debug יעיל של ה-flow.

**גרסאות וכיול של הפרומפט**

צרו והשוו בין גרסאות שונות של הפרומפט כדי לאפשר תהליך שיפור הדרגתי. העריכו את ביצועי הפרומפטים השונים ובחרו את היעילים ביותר.

**תהליכי הערכה מובנים**

העריכו את איכות ויעילות הפרומפטים והתהליכים שלכם באמצעות כלי הערכה מובנים.
הבינו עד כמה יישומי ה-LLM שלכם מבצעים טוב.

**משאבים מקיפים**

Prompt Flow כולל ספרייה של כלים, דוגמאות ותבניות מובנות. משאבים אלו משמשים כנקודת התחלה לפיתוח, מעוררים יצירתיות ומאיצים את התהליך.

**שיתוף פעולה ומוכנות ארגונית**

תמכו בשיתוף פעולה צוותי בכך שמאפשרים למספר משתמשים לעבוד יחד על פרויקטים של הנדסת פרומפטים.
שמרו על בקרת גרסאות ושיתוף ידע יעיל. פשטו את כל תהליך הנדסת הפרומפטים, מהפיתוח וההערכה ועד לפריסה ומעקב.

## הערכה ב-Prompt Flow

ב-Microsoft Prompt Flow, הערכה ממלאת תפקיד מרכזי בהערכת ביצועי מודלי ה-AI שלכם. נבחן כיצד ניתן להתאים אישית תהליכי הערכה ומדדים בתוך Prompt Flow:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.ms.png)

**הבנת ההערכה ב-Prompt Flow**

ב-Prompt Flow, flow מייצג רצף של nodes שמעבדים קלט ומייצרים פלט. תהליכי הערכה הם סוג מיוחד של flows שנועדו להעריך את ביצועי הריצה על פי קריטריונים ומטרות ספציפיות.

**תכונות מרכזיות של תהליכי הערכה**

הם בדרך כלל רצים לאחר ה-flow הנבדק, תוך שימוש בפלט שלו. הם מחשבים ציונים או מדדים כדי למדוד את ביצועי ה-flow הנבדק. מדדים יכולים לכלול דיוק, ציון רלוונטיות או כל מדד רלוונטי אחר.

### התאמת תהליכי הערכה

**הגדרת קלטים**

תהליכי הערכה צריכים לקבל את הפלטים של הריצה הנבדקת. הגדירו קלטים בדומה ל-flows רגילים.
לדוגמה, אם אתם מעריכים flow של QnA, קראו לקלט "answer". אם מעריכים flow של סיווג, קראו לקלט "category". ייתכן ויהיו גם קלטים של ground truth (למשל תוויות אמיתיות).

**פלטים ומדדים**

תהליכי הערכה מייצרים תוצאות שמודדות את ביצועי ה-flow הנבדק. מדדים יכולים להיות מחושבים באמצעות Python או LLM. השתמשו בפונקציה log_metric() כדי לתעד מדדים רלוונטיים.

**שימוש בתהליכי הערכה מותאמים אישית**

פיתחו את תהליך ההערכה שלכם המותאם למשימות ולמטרות הספציפיות שלכם.
התאימו את המדדים בהתאם למטרות ההערכה.
החילו תהליך הערכה זה על ריצות בכמויות גדולות לצורך בדיקות רחבות היקף.

## שיטות הערכה מובנות

Prompt Flow מציע גם שיטות הערכה מובנות.
ניתן להגיש ריצות בכמויות גדולות ולהשתמש בשיטות אלו כדי להעריך את ביצועי ה-flow עם מאגרי נתונים גדולים.
צפו בתוצאות ההערכה, השוו מדדים וערכו שיפורים לפי הצורך.
זכרו, הערכה חיונית כדי לוודא שמודלי ה-AI שלכם עומדים בקריטריונים ובמטרות הרצויות. עיינו בתיעוד הרשמי לקבלת הוראות מפורטות לפיתוח ושימוש בתהליכי הערכה ב-Microsoft Prompt Flow.

לסיכום, Microsoft Prompt Flow מעניק למפתחים את היכולת ליצור יישומי LLM איכותיים על ידי פישוט הנדסת הפרומפטים וסיפוק סביבת פיתוח חזקה. אם אתם עובדים עם LLM, Prompt Flow הוא כלי חשוב שכדאי להכיר. עיינו ב-[Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) לקבלת הוראות מפורטות לפיתוח ושימוש בתהליכי הערכה ב-Microsoft Prompt Flow.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.