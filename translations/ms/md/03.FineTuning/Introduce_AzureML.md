<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-05-09T22:22:23+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "ms"
}
-->
# **הכרת שירות Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) הוא שירות ענן שמאיץ ומנהל את מחזור החיים של פרויקטים בתחום למידת מכונה (ML).

מקצועני ML, מדעני נתונים ומהנדסים יכולים להשתמש בו בעבודתם היומיומית כדי:

- לאמן ולפרוס מודלים.
- לנהל תהליכי Machine Learning Operations (MLOps).
- ניתן ליצור מודל ב-Azure Machine Learning או להשתמש במודל שנבנה בפלטפורמה בקוד פתוח, כמו PyTorch, TensorFlow או scikit-learn.
- כלי MLOps עוזרים במעקב, אימון מחדש ופריסה חוזרת של מודלים.

## למי מיועד Azure Machine Learning?

**מדעני נתונים ומהנדסי ML**

הם יכולים להשתמש בכלים שמאיצים ומאוטומטים את תהליכי העבודה היומיומיים שלהם.  
Azure ML מספק תכונות להבטחת הוגנות, להסבריות, למעקב ולביקורת.

**מפתחי אפליקציות:**  
יכולים לשלב מודלים באפליקציות או בשירותים בצורה חלקה.

**מפתחי פלטפורמה**

יש להם גישה למערך כלים חזק הנתמך על ידי Azure Resource Manager APIs יציבים.  
כלים אלו מאפשרים בנייה של כלי ML מתקדמים.

**ארגונים**

עובדים בענן Microsoft Azure, ומרוויחים מאבטחה מוכרת ובקרת גישה מבוססת תפקידים.  
ניתן להגדיר פרויקטים לשליטה בגישה לנתונים מוגנים ולפעולות ספציפיות.

## פרודוקטיביות לכל חברי הצוות  
פרויקטי ML לרוב דורשים צוות עם מגוון מיומנויות לבנייה ותחזוקה.

Azure ML מספק כלים שמאפשרים לך:  
- לשתף פעולה עם הצוות דרך פנקסי הערות משותפים, משאבי חישוב, חישוב ללא שרת, נתונים וסביבות.  
- לפתח מודלים עם הוגנות, הסבריות, מעקב וביקורת כדי לעמוד בדרישות שייכות וביקורת.  
- לפרוס מודלי ML במהירות ובקלות בקנה מידה, ולנהל ולפקח עליהם ביעילות באמצעות MLOps.  
- להריץ עומסי עבודה של למידת מכונה בכל מקום עם ממשל, אבטחה וציות מובנים.

## כלים חוצי פלטפורמות

כל חבר צוות ML יכול להשתמש בכלים המועדפים עליו כדי לבצע את העבודה.  
בין אם אתה מריץ ניסויים מהירים, מכוון פרמטרים, בונה צינורות עבודה או מנהל אינפרנסים, ניתן להשתמש בממשקים מוכרים כמו:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST APIs

כשאתה מחדד מודלים ומשתף פעולה לאורך מחזור הפיתוח, תוכל לשתף ולמצוא נכסים, משאבים ומדדים בממשק Azure Machine Learning studio.

## **LLM/SLM ב-Azure ML**

Azure ML הוסיף פונקציות רבות הקשורות ל-LLM/SLM, שמשלבות בין LLMOps ל-SLMOps ליצירת פלטפורמת טכנולוגיית בינה מלאכותית גנרטיבית ארגונית.

### **קטלוג מודלים**

משתמשים ארגוניים יכולים לפרוס מודלים שונים בהתאם לתרחישי עסק שונים דרך קטלוג מודלים, ולספק שירותים כ-Model as Service למפתחים או משתמשים בארגון.

![models](../../../../translated_images/models.2450411eac222e539ffb55785a8f550d01be1030bd8eb67c9c4f9ae4ca5d64be.ms.png)

קטלוג המודלים ב-Azure Machine Learning studio הוא מרכז לגילוי ושימוש במגוון רחב של מודלים שמאפשרים לבנות יישומי Generative AI. קטלוג המודלים כולל מאות מודלים מספקים שונים כמו Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, כולל מודלים שאומנו על ידי Microsoft. מודלים מספקים שאינם Microsoft מוגדרים כמוצרים שאינם של Microsoft, בהתאם לתנאי המוצר של Microsoft, ומותנים בתנאים המסופקים עם המודל.

### **צינור עבודה (Job Pipeline)**

הבסיס של צינור למידת מכונה הוא חלוקה של משימת למידת מכונה מלאה לזרימת עבודה רב-שלבית. כל שלב הוא רכיב ניהולי שניתן לפתח, לאופטימיזציה, להגדיר ולאוטומציה בנפרד. השלבים מחוברים דרך ממשקים מוגדרים היטב. שירות צינור העבודה של Azure Machine Learning מנהל אוטומטית את כל התלות בין השלבים.

בהתאמת SLM / LLM, ניתן לנהל את הנתונים, האימון ותהליכי ההפקה דרך Pipeline.

![finetuning](../../../../translated_images/finetuning.b52e4aa971dfd8d3c668db913a2b419380533bd3a920d227ec19c078b7b3f309.ms.png)

### **Prompt flow**

יתרונות השימוש ב-Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow מציע מגוון יתרונות שעוזרים למשתמשים לעבור מרעיון לניסוי ולבסוף ליישומים מבוססי LLM מוכנים לפרודקשן:

**גמישות בהנדסת פרומפטים**

חוויית כתיבה אינטראקטיבית: Azure Machine Learning prompt flow מספק ייצוג חזותי של מבנה הזרימה, שמאפשר למשתמשים להבין ולנווט בקלות בפרויקטים שלהם. בנוסף, הוא מציע חוויית קידוד בסגנון פנקס הערות לפיתוח ו-debug יעיל של הזרימה.  
גרסאות לכיוונון פרומפט: משתמשים יכולים ליצור ולהשוות בין וריאציות פרומפט שונות, מה שמקל על תהליך שיפור איטרטיבי.

הערכה: זרימות הערכה מובנות מאפשרות למשתמשים להעריך את איכות ויעילות הפרומפטים והזרימות שלהם.

משאבים מקיפים: Azure Machine Learning prompt flow כולל ספריית כלים, דוגמאות ותבניות מובנות שמספקות נקודת התחלה לפיתוח, מעוררות יצירתיות ומאיצות את התהליך.

**מוכנות ארגונית ליישומים מבוססי LLM**

שיתוף פעולה: Azure Machine Learning prompt flow תומך בשיתוף פעולה בצוות, ומאפשר למספר משתמשים לעבוד יחד על פרויקטים של הנדסת פרומפטים, לשתף ידע ולשמור על בקרת גרסאות.

פלטפורמה כוללת: Azure Machine Learning prompt flow מפשט את כל תהליך הנדסת הפרומפטים, מפיתוח והערכה ועד פריסה ומעקב. משתמשים יכולים לפרוס את הזרימות שלהם כנקודות קצה של Azure Machine Learning ולעקוב אחר הביצועים בזמן אמת, להבטיח פעולה מיטבית ושיפור מתמיד.

פתרונות מוכנות ארגונית של Azure Machine Learning: Prompt flow משתמש בפתרונות המוכנות הארגונית החזקים של Azure Machine Learning, ומספק בסיס מאובטח, סקלאבילי ואמין לפיתוח, ניסוי ופריסה של זרימות.

עם Azure Machine Learning prompt flow, משתמשים יכולים לשחרר את הגמישות בהנדסת הפרומפטים, לשתף פעולה ביעילות ולהשתמש בפתרונות ארגוניים מוצקים להצלחה בפיתוח ופריסת יישומים מבוססי LLM.

שילוב כוח המחשוב, הנתונים והרכיבים השונים של Azure ML מאפשר למפתחים ארגוניים לבנות בקלות את יישומי הבינה המלאכותית שלהם.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.