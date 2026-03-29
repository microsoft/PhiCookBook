# כיוונון עדין של Phi-3 עם Microsoft Foundry

בואו נחקור כיצד לכוונן עדין את דגם השפה Phi-3 Mini של Microsoft באמצעות Microsoft Foundry. כיוונון עדין מאפשר לכם להתאים את Phi-3 Mini למשימות ספציפיות, מה שהופך אותו לעוצמתי ומודע להקשר אפילו יותר.

## שיקולים

- **יכולות:** אילו דגמים ניתנים לכוונון עדין? מה ניתן לכוונן בדגם הבסיסי?
- **עלות:** מהו מודל התמחור לכיוונון עדין?
- **התאמה אישית:** עד כמה אפשר לשנות את דגם הבסיס – ובאיזה אופנים?
- **נוחות:** כיצד מתבצע כיוונון עדין בפועל – האם אני צריך לכתוב קוד מותאם? האם עלי לספק את משאבי החישוב שלי?
- **בטיחות:** דגמים מכווננים ידועים כבעלי סיכוני בטיחות – האם קיימים מגני בטיחות כדי למנוע נזק בלתי מכוון?

![AIFoundry Models](../../../../translated_images/he/AIFoundryModels.0e1b16f7d0b09b73.webp)

## הכנה לכיוונון עדין

### דרישות מוקדמות

> [!NOTE]
> עבור דגמי משפחת Phi-3, מודל כיוונון עדין בתשלום לפי שימוש זמין רק עם מרכזיות שנוצרו באזור **East US 2**.

- מנוי Azure. אם אין לכם מנוי Azure, צרו [חשבון Azure בתשלום](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) כדי להתחיל.

- פרויקט [AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- בקרות גישה מבוססות תפקיד (Azure RBAC) משמשות להענקת גישה לפעולות ב-Microsoft Foundry. כדי לבצע את השלבים במאמר זה, על חשבון המשתמש שלכם להיות מוקצה לתפקיד __Azure AI Developer__ בקבוצת המשאבים.

### רישום ספק מנוי

וודאו שהמנוי רשום לספק המשאבים `Microsoft.Network`.

1. התחברו ל[פורטאל Azure](https://portal.azure.com).
1. בחרו **Subscriptions** מהתפריט השמאלי.
1. בחרו את המנוי שברצונכם להשתמש בו.
1. בחרו **AI project settings** > **Resource providers** מהתפריט השמאלי.
1. ודאו ש-**Microsoft.Network** נמצא ברשימת ספקי המשאבים. אם לא, הוסיפו אותו.

### הכנת נתונים

הכינו את נתוני האימון והאימות כדי לכוונן את הדגם שלכם. מערכי הנתונים שלכם לאימון ולאימות מורכבים מדוגמאות קלט ופלט כיצד תרצו שהדגם יתפקד.

ודאו שכל דוגמאות האימון שלכם פועלות לפי הפורמט הצפוי למידול. כדי לכוונן דגמים ביעילות, ודאו שיש סט נתונים מאוזן ומגוון.

זה כולל שמירה על איזון בנתונים, הכללת תרחישים שונים, ועדכון תקופתי של נתוני האימון כדי ליישר ציפיות עם המציאות, מה שמוביל לתגובות מדויקות ומאוזנות יותר של הדגם.

סוגי דגמים שונים דורשים פורמט שונה של נתוני אימון.

### השלמת שיחה (Chat Completion)

נתוני האימון והאימות שאתם משתמשים בהם **חייבים** להיות בפורמט JSON Lines (JSONL). עבור `Phi-3-mini-128k-instruct` מערך הכיוונון העדין חייב להיות בפורמט שיחות שמשמש את ממשק API של השלמות שיחה.

### דוגמה לפורמט קובץ

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```
  
סוג הקובץ הנתמך הוא JSON Lines. הקבצים מועלים למחסן הברירת מחדל ונגישים בפרויקט שלכם.

## כיוונון עדין של Phi-3 עם Microsoft Foundry

Microsoft Foundry מאפשרת לכם להתאים דגמי שפה גדולים לסטים האישיים שלכם באמצעות תהליך הנקרא כיוונון עדין. כיוונון עדין מספק ערך משמעותי על ידי מתן אפשרויות התאמה אישית ואופטימיזציה למשימות וליישומים ספציפיים. הוא מוביל לשיפור ביצועים, יעילות עלות, הפחתת זמן תגובה ותוצאות מותאמות.

![Finetune AI Foundry](../../../../translated_images/he/AIFoundryfinetune.193aaddce48d553c.webp)

### יצירת פרויקט חדש

1. התחברו ל-[Microsoft Foundry](https://ai.azure.com).

1. בחרו **+New project** כדי ליצור פרויקט חדש ב-Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/he/select-new-project.cd31c0404088d7a3.webp)

1. בצעו את המטלות הבאות:

    - שם ה**Hub** של הפרויקט. חייב להיות ערך ייחודי.
    - בחרו את ה**Hub** לשימוש (צרו חדש במידת הצורך).

    ![FineTuneSelect](../../../../translated_images/he/create-project.ca3b71298b90e420.webp)

1. בצעו את המטלות הבאות ליצירת Hub חדש:

    - הזינו **שם Hub**. חייב להיות ערך ייחודי.
    - בחרו את מנוי ה-Azure שלכם.
    - בחרו את **Resource group** לשימוש (צרו חדש במידת הצורך).
    - בחרו את **המיקום** שברצונכם להשתמש בו.
    - בחרו את שירותי Azure AI שברצונכם לחבר (צרו חדש במידת הצורך).
    - בחרו **Connect Azure AI Search** כדי **להדלג על חיבור**.

    ![FineTuneSelect](../../../../translated_images/he/create-hub.49e53d235e80779e.webp)

1. בחרו **Next**.
1. בחרו **Create a project**.

### הכנת הנתונים

לפני הכיוונון, אספו או צרו מערך נתונים שרלוונטי למשימה שלכם, כגון הוראות שיחה, זוגות שאלות-תשובות, או כל סוג טקסט אחר שקשור. נקו ועבדו את הנתונים על ידי הסרת רעשים, טיפול בערכים חסרים וטוקניזציה של הטקסט.

### כיוונון עדין של דגמי Phi-3 ב-Microsoft Foundry

> [!NOTE]
> כיוונון עדין של דגמי Phi-3 נתמך כרגע רק בפרויקטים הממוקמים באזור East US 2.

1. בחרו **Model catalog** מתפריט הצד השמאלי.

1. הקלידו *phi-3* בשורת החיפוש ובחרו את דגם phi-3 שברצונכם להשתמש בו.

    ![FineTuneSelect](../../../../translated_images/he/select-model.60ef2d4a6a3cec57.webp)

1. בחרו **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/he/select-finetune.a976213b543dd9d8.webp)

1. הזינו את שם **הדגם המכוונן**.

    ![FineTuneSelect](../../../../translated_images/he/finetune1.c2b39463f0d34148.webp)

1. בחרו **Next**.

1. בצעו את המטלות הבאות:

    - בחרו **סוג המשימה** ל-**Chat completion**.
    - בחרו את **נתוני האימון** שברצונכם להשתמש בהם. ניתן להעלות אותם דרך מערכת הנתונים של Microsoft Foundry או מהסביבה המקומית שלכם.

    ![FineTuneSelect](../../../../translated_images/he/finetune2.43cb099b1a94442d.webp)

1. בחרו **Next**.

1. העלו את **נתוני האימות** שברצונכם להשתמש בהם, או בחרו **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/he/finetune3.fd96121b67dcdd92.webp)

1. בחרו **Next**.

1. בצעו את המטלות הבאות:

    - בחרו את **מכפיל גודל האצווה** שברצונכם להשתמש בו.
    - בחרו את **קצב הלמידה** שברצונכם להשתמש בו.
    - בחרו את **מספר האפוקים** שברצונכם להשתמש בו.

    ![FineTuneSelect](../../../../translated_images/he/finetune4.e18b80ffccb5834a.webp)

1. בחרו **Submit** כדי להתחיל את תהליך הכיוונון העדין.

    ![FineTuneSelect](../../../../translated_images/he/select-submit.0a3802d581bac271.webp)

1. לאחר שהדגם שלכם מכוונן עדין, הסטטוס יוצג כ-**Completed**, כפי שמוצג בתמונה שלמטה. כעת תוכלו לפרוס את הדגם ולהשתמש בו באפליקציה שלכם, במגרש המשחקים, או ב-Prompt Flow. למידע נוסף, ראו [כיצד לפרוס דגמי משפחת Phi-3 עם Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/he/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> למידע מפורט יותר על כיוונון עדין של Phi-3, בקרו ב-[Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## ניקוי דגמים מכווננים עדין

ניתן למחוק דגם מכוונן עדין מהרשימה ב-[Microsoft Foundry](https://ai.azure.com) או מדף פרטי הדגם. בחרו את הדגם המכוונן למחיקה מדף הכיוונון העדין, ואז לחצו על כפתור המחיקה כדי למחוק את הדגם.

> [!NOTE]
> אי אפשר למחוק דגם מותאם אישית אם יש לו פריסה פעילה. עליכם למחוק קודם את הפריסה לפני שתוכלו למחוק את הדגם המותאם שלכם.

## עלויות ומכסים

### שיקולי עלות ומכסה לדגמי Phi-3 מכווננים כשירות

דגמי Phi המכווננים כשירות מוצעים על ידי Microsoft ומשולבים בתוך Microsoft Foundry לשימוש. תוכלו למצוא את המחיר בעת [פריסה](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) או בעת כיוונון הדגם תחת לשונית המחירים והתנאים במדריך הפריסה.

## סינון תוכן

דגמים המפורסים כשירות בתשלום לפי שימוש מוגנים על ידי Azure AI Content Safety. כאשר מפורסמים לנקודות קצה של זמן-אמת, ניתן לבחור לבטל תכונה זו. עם אפשרות Azure AI Content Safety מופעלת, גם ההנחיה וגם התגובה עוברים דרך מכלול דגמי סיווג שמטרתם לזהות ולמנוע הפקת תוכן מזיק. מערכת הסינון מזהה ונוקטת פעולה במקטעי תוכן מזיקים ספציפיים הן בהנחיות הקלט והן בתגובות הפלט. למידע נוסף על [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**הגדרות כיוונון עדין**

היפרפרמטרים: הגדרת היפרפרמטרים כמו קצב הלמידה, גודל אצווה ומספר אפוקים לאימון.

**פונקציית אובדן**

בחר פונקציית אובדן מתאימה למשימה (למשל, cross-entropy).

**אופטימייזר**

בחר אופטימייזר (למשל, Adam) לעדכוני גרדיאנט במהלך האימון.

**תהליך כיוונון עדין**

- טעינת דגם מאומן מראש: טען את נקודת הבדיקה של Phi-3 Mini.
- הוספת שכבות מותאמות: הוסף שכבות ייעודיות למשימה (למשל, ראש סיווג להוראות שיחה).

**אימון הדגם**  
כוונן את הדגם באמצעות מערך הנתונים שהכנת. עקוב אחר התקדמות האימון והתאם את ההיפרפרמטרים במידת הצורך.

**הערכה ואימות**

מערך אימות: חלק את הנתונים למערך אימון ומערך אימות.

**הערכת ביצועים**

השתמש במדדים כמו דיוק, F1-score או perplexity כדי להעריך את הביצועים.

## שמירת דגם מכוונן עדין

**נקודת בדיקה**  
שמור את נקודת הבדיקה של הדגם המכוונן לשימוש עתידי.

## פריסה

- פריסה כשירות רשת: פרוס את הדגם המכוונן כשירות ווב ב-Microsoft Foundry.
- בדיקת נקודת הקצה: שלח שאילתות בדיקה לנקודת הקצה המופרסמת כדי לאמת את תפקודה.

## חזרה ושיפור

חזור על התהליך: אם הביצועים לא מספקים, חזר על התהליך על ידי כיוונון היפרפרמטרים, הוספת נתונים, או כיוונון לאפוקים נוספים.

## ניטור ושיפור

ניטור מתמיד של התנהגות הדגם וכיוונון מחדש לפי הצורך.

## התאמה והרחבה

משימות מותאמות: Phi-3 Mini ניתן לכוונן למשימות שונות מעבר להוראות שיחה. חקרו שימושים נוספים!  
ניסויים: נסו ארכיטקטורות שונות, שילובי שכבות וטכניקות לשיפור ביצועים.

> [!NOTE]
> כיוונון עדין הוא תהליך איטרטיבי. נסו, למדו, והתאימו את הדגם כדי להשיג את התוצאות הטובות ביותר למשימה הספציפית שלכם!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להכיר כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי, מומלץ לבצע תרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי הבנה או פרשנות שגויה הנובעת מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->