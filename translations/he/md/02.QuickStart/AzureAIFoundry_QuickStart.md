# **שימוש ב-Phi-3 ב-Azure AI Foundry**

עם התפתחות ה-AI הגנרטיבי, אנו מקווים להשתמש בפלטפורמה מאוחדת לניהול מודלים גדולים של שפה (LLM) ומודלים קטנים של שפה (SLM), אינטגרציה של נתוני ארגון, פעולות כיוונון עדין/RAG, והערכת עסקים שונים בארגון לאחר שילוב LLM ו-SLM, וכדומה, כדי לאפשר יישום חכם יותר של אפליקציות גנרטיביות. [Azure AI Foundry](https://ai.azure.com) היא פלטפורמת יישומים גנרטיביים ברמת ארגון.

![aistudo](../../../../translated_images/he/aifoundry_home.f28a8127c96c7d93.webp)

באמצעות Azure AI Foundry, ניתן להעריך תגובות של מודלים גדולים של שפה (LLM) ולתזמר רכיבי יישום פרומפט עם prompt flow לשיפור הביצועים. הפלטפורמה מאפשרת גמישות בקנה מידה להמרת הוכחות מושג למוצר מלא בקלות. ניטור מתמשך ושיפור תומכים בהצלחה לטווח ארוך.

ניתן לפרוס במהירות את מודל Phi-3 ב-Azure AI Foundry דרך כמה שלבים פשוטים, ולאחר מכן להשתמש ב-Azure AI Foundry להשלמת Playground/Chat, כיוונון עדין, הערכה ועבודות נוספות הקשורות ל-Phi-3.

## **1. הכנה**

אם כבר התקנת את [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) במחשב שלך, השימוש בתבנית זו פשוט כמו הרצת הפקודה הזו בתיקייה חדשה.

## יצירה ידנית

יצירת פרויקט ו-hub ב-Microsoft Azure AI Foundry היא דרך מצוינת לארגן ולנהל את עבודת ה-AI שלך. הנה מדריך שלב-אחר-שלב שיעזור לך להתחיל:

### יצירת פרויקט ב-Azure AI Foundry

1. **גש ל-Azure AI Foundry**: היכנס לפורטל Azure AI Foundry.
2. **צור פרויקט**:
   - אם אתה בתוך פרויקט, בחר ב-"Azure AI Foundry" בפינה השמאלית העליונה של הדף כדי לחזור לדף הבית.
   - בחר "+ Create project".
   - הזן שם לפרויקט.
   - אם יש לך hub, הוא ייבחר כברירת מחדל. אם יש לך גישה ליותר מ-hub אחד, תוכל לבחור hub אחר מהרשימה הנפתחת. אם ברצונך ליצור hub חדש, בחר "Create new hub" וספק שם.
   - בחר "Create".

### יצירת Hub ב-Azure AI Foundry

1. **גש ל-Azure AI Foundry**: היכנס עם חשבון Azure שלך.
2. **צור Hub**:
   - בחר במרכז הניהול מהתפריט השמאלי.
   - בחר "All resources", לאחר מכן לחץ על החץ למטה ליד "+ New project" ובחר "+ New hub".
   - בחלון "Create a new hub", הזן שם ל-hub שלך (למשל contoso-hub) ושנה שדות נוספים לפי הצורך.
   - בחר "Next", סקור את המידע ואז בחר "Create".

להוראות מפורטות יותר, ניתן לעיין בתיעוד הרשמי של [Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

לאחר יצירה מוצלחת, תוכל לגשת לסטודיו שיצרת דרך [ai.azure.com](https://ai.azure.com/)

ניתן לנהל מספר פרויקטים ב-AI Foundry אחד. צור פרויקט ב-AI Foundry כהכנה.

צור Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. פריסת מודל Phi ב-Azure AI Foundry**

לחץ על אפשרות Explore של הפרויקט כדי להיכנס לקטלוג המודלים ובחר Phi-3

בחר Phi-3-mini-4k-instruct

לחץ על 'Deploy' כדי לפרוס את מודל Phi-3-mini-4k-instruct

> [!NOTE]
>
> ניתן לבחור את עוצמת המחשוב בעת הפריסה

## **3. Playground Chat עם Phi ב-Azure AI Foundry**

גש לדף הפריסה, בחר Playground, וצ'ט עם Phi-3 של Azure AI Foundry

## **4. פריסת המודל מ-Azure AI Foundry**

כדי לפרוס מודל מ-Azure Model Catalog, ניתן לבצע את השלבים הבאים:

- היכנס ל-Azure AI Foundry.
- בחר את המודל שברצונך לפרוס מקטלוג המודלים של Azure AI Foundry.
- בדף הפרטים של המודל, בחר Deploy ואז בחר Serverless API עם Azure AI Content Safety.
- בחר את הפרויקט שבו ברצונך לפרוס את המודלים שלך. כדי להשתמש ב-Serverless API, סביבת העבודה שלך חייבת להיות באזור East US 2 או Sweden Central. ניתן להתאים את שם הפריסה.
- באשף הפריסה, בחר את התמחור והתנאים כדי ללמוד על המחיר ותנאי השימוש.
- בחר Deploy. המתן עד שהפריסה תהיה מוכנה ויועברו אותך לדף הפריסות.
- בחר Open in playground כדי להתחיל באינטראקציה עם המודל.
- תוכל לחזור לדף הפריסות, לבחור בפריסה, ולרשום את כתובת ה-URL של ה-endpoint ואת מפתח הסוד, אותם תוכל להשתמש לקריאה לפריסה וליצירת השלמות.
- תמיד תוכל למצוא את פרטי ה-endpoint, ה-URL ומפתחות הגישה על ידי ניווט ללשונית Build ובחירת Deployments מתוך חלק Components.

> [!NOTE]
> שים לב שחשבון המשתמש שלך חייב לקבל הרשאות תפקיד Azure AI Developer על קבוצת המשאבים כדי לבצע שלבים אלה.

## **5. שימוש ב-Phi API ב-Azure AI Foundry**

ניתן לגשת לכתובת https://{Your project name}.region.inference.ml.azure.com/swagger.json דרך Postman ב-GET ולשלב אותה עם Key כדי ללמוד על הממשקים המסופקים

ניתן לקבל את פרמטרי הבקשה בקלות רבה, כמו גם את פרמטרי התגובה.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.