# **שימוש ב-Phi-3 ב-Microsoft Foundry**

עם התפתחות ה-AI הגנרטיבי, אנו מקווים להשתמש בפלטפורמה מאוחדת לניהול מודלים גדולים לשפה (LLM) ומודלים ספציפיים לשפה (SLM), אינטגרציה של נתוני ארגונים, פעולות כיוונון עדין/RAG, והערכת עסקים ארגוניים שונים לאחר שילוב LLM ו-SLM, וכן הלאה, כך שניתן יהיה ליישם יישומים חכמים של AI גנרטיבי בצורה טובה יותר. [Microsoft Foundry](https://ai.azure.com) היא פלטפורמת יישומי AI גנרטיבי ברמת ארגון.

![aistudo](../../../../translated_images/he/aifoundry_home.f28a8127c96c7d93.webp)

עם Microsoft Foundry, ניתן להעריך תגובות של מודלים גדולים לשפה (LLM) ולתזמר רכיבי יישום פרומפט עם זרימת פרומפטים לשיפור ביצועים. הפלטפורמה מאפשרת סקלאביליות בהפיכת הוכחות אישור לייצור מלא בקלות. ניטור מתמשך ושיפור תומכים בהצלחה לטווח ארוך.

ניתן לבצע פריסה מהירה של מודל Phi-3 ב-Microsoft Foundry באמצעות צעדים פשוטים, ואז להשתמש ב-Microsoft Foundry להשלמת Playground/Chat, כיוונון עדין, הערכה ועבודות קשורות ל-Phi-3.

## **1. הכנות**

אם כבר מותקן אצלכם [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) במחשב, השימוש בתבנית זו פשוט כמו הרצת הפקודה הזו בספריה חדשה.

## יצירה ידנית

יצירת פרויקט ו-hub ב-Microsoft Foundry היא דרך מצוינת לארגן ולנהל את עבודות ה-AI שלכם. להלן מדריך שלב אחר שלב כדי להתחיל:

### יצירת פרויקט ב-Microsoft Foundry

1. **גש ל-Microsoft Foundry**: היכנס לפורטל של Microsoft Foundry.
2. **צור פרויקט**:
   - אם אתה בתוך פרויקט, בחר ב-"Microsoft Foundry" בפינה השמאלית העליונה כדי לחזור לדף הבית.
   - בחר "+ Create project".
   - הזן שם לפרויקט.
   - אם יש לך hub, הוא ייבחר כברירת מחדל. אם יש לך גישה ליותר מ-hub אחד, תוכל לבחור אחר מהרשימה הנגללת. אם ברצונך ליצור hub חדש, בחר "Create new hub" והזן שם.
   - בחר "Create".

### יצירת Hub ב-Microsoft Foundry

1. **גש ל-Microsoft Foundry**: היכנס עם חשבון Azure שלך.
2. **צור Hub**:
   - בחר במרכז הניהול מהתפריט השמאלי.
   - בחר "All resources", לאחר מכן את החץ למטה לצד "+ New project" ובחר "+ New hub".
   - בדיאלוג "Create a new hub", הזן שם ל-hub שלך (למשל contoso-hub) ושנה שדות נוספים במידת הצורך.
   - בחר "Next", בדוק את המידע ואז בחר "Create".

להוראות מפורטות יותר, ניתן לעיין ב-[התיעוד הרשמי של Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

לאחר יצירה מוצלחת, ניתן לגשת לסטודיו שיצרת דרך [ai.azure.com](https://ai.azure.com/)

יכולים להיות מספר פרויקטים באותו AI Foundry. צור פרויקט ב-AI Foundry כהכנה.

צור Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. פריסה של מודל Phi ב-Microsoft Foundry**

לחץ על אופציית Explore של הפרויקט כדי להיכנס לקטלוג המודלים ובחר ב-Phi-3

בחר Phi-3-mini-4k-instruct

לחץ על 'Deploy' כדי לפרוס את המודל Phi-3-mini-4k-instruct

> [!NOTE]
>
> ניתן לבחור כוח מחשוב בעת הפריסה

## **3. Playground Chat Phi ב-Microsoft Foundry**

גש לדף הפריסה, בחר Playground, וצ'ט עם Phi-3 של Microsoft Foundry

## **4. פריסת המודל מ-Microsoft Foundry**

כדי לפרוס מודל מ-Azure Model Catalog, ניתן לבצע את השלבים הבאים:

- היכנס ל-Microsoft Foundry.
- בחר את המודל שברצונך לפרוס מתוך קטלוג המודלים של Microsoft Foundry.
- בדף הפרטים של המודל, בחר Deploy ואז בחר Serverless API עם Azure AI Content Safety.
- בחר את הפרויקט שבו ברצונך לפרוס את המודלים. כדי להשתמש בהצעת ה-Serverless API, סביבת העבודה שלך חייבת להיות באזור East US 2 או Sweden Central. ניתן להתאים אישית את שם הפריסה.
- באשף הפריסה, בחר את המחירון והתנאים כדי ללמוד על המחירון ותנאי השימוש.
- בחר Deploy. המתן עד שהפריסה תהיה מוכנה ושתהיה מנותב לדף הפריסות.
- בחר Open in playground להתחיל אינטראקציה עם המודל.
- תוכל לחזור לדף הפריסות, לבחור בפריסה, ולרשום את כתובת ה-URL של נקודת הקצה ואת המפתח הסודי, אותם ניתן להשתמש לקריאות אל הפריסה וליצירת השלמות.
- תמיד ניתן למצוא את פרטי נקודת הקצה, URL ומפתחות הגישה על ידי ניווט ללשונית Build ולבחור בפריסות מתוך חלק הרכיבים.

> [!NOTE]
> שים לב שחשבון המשתמש שלך חייב להחזיק בהרשאות Azure AI Developer על קבוצת המשאבים כדי לבצע את השלבים הללו.

## **5. שימוש ב-Phi API ב-Microsoft Foundry**

ניתן לגשת ל-https://{שם הפרויקט שלך}.region.inference.ml.azure.com/swagger.json דרך Postman GET ולשלב זאת עם המפתח כדי להכיר את הממשקים המסופקים

אפשר לקבל פרמטרי בקשה בנוחות רבה, כמו גם פרמטרי תגובה.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי של אדם. אנו לא נושאים באחריות לכל אי-הבנות או פרשנויות שגויות הנובעות מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->