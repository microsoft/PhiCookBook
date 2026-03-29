# **בנה את Visual Studio Code GitHub Copilot Chat משלך עם משפחת Microsoft Phi-3**

האם השתמשת בסוכן סביבת העבודה ב-GitHub Copilot Chat? האם תרצה לבנות סוכן קוד לצוות שלך? מעבדה זו מקווה לשלב את המודל בקוד פתוח כדי לבנות סוכן עסקי ליצירת קוד ברמת ארגונית.

## **בסיס**

### **למה לבחור ב-Microsoft Phi-3**

Phi-3 היא סדרת משפחה, הכוללת את phi-3-mini, phi-3-small ו-phi-3-medium המבוססים על פרמטרים שונים לאימון ליצירת טקסט, השלמת דיאלוג ויצירת קוד. יש גם את phi-3-vision המבוסס על Vision. היא מתאימה לארגונים או לצוותים שונים ליצירת פתרונות AI גנרטיביים ללא חיבור לאינטרנט.

מומלץ לקרוא בקישור זה [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

תוסף GitHub Copilot Chat מעניק לך ממשק שיחה שמאפשר לך אינטראקציה עם GitHub Copilot ולקבל תשובות לשאלות הקשורות לתכנות ישירות בתוך VS Code, מבלי שתצטרך לנווט לתיעוד או לחפש בפורומים מקוונים.

Copilot Chat עשוי להשתמש בהדגשת תחביר, הזחה ותכונות עיצוב נוספות כדי להוסיף בהירות לתשובה שנוצרה. בהתאם לסוג השאלה מהמשתמש, התוצאה עשויה לכלול קישורים להקשר בו השתמש Copilot ליצירת התשובה, כגון קבצי קוד מקור או תיעוד, או לחצנים לגישה לפונקציות של VS Code.

- Copilot Chat משתלב בזרימת הפיתוח שלך ומספק לך סיוע במקום שבו אתה צריך אותו:

- התחל שיחת צ'אט מקוונת ישירות מהעורך או מהטרמינל לקבלת עזרה בזמן הקידוד

- השתמש בתצוגת הצ'אט כדי לקבל עוזר AI בצד שיעזור לך בכל זמן

- השקת Quick Chat לשאול שאלה מהירה ולחזור במהירות לפעילות שלך

ניתן להשתמש ב-GitHub Copilot Chat במגוון תרחישים, כגון:

- מענה על שאלות קידוד בנוגע לדרך הטובה ביותר לפתור בעיה

- הסבר של קוד שכתב מישהו אחר והצעת שיפורים

- הצעת תיקוני קוד

- יצירת מקרים של בדיקות יחידה

- יצירת תיעוד קוד

מומלץ לקרוא בקישור זה [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

הפניה ל-**@workspace** ב-Copilot Chat מאפשרת לך לשאול שאלות לגבי כל בסיס הקוד שלך. בהתבסס על השאלה, Copilot מושך באופן אינטיליגנטי קבצים וסמלים רלוונטיים, שהם אז מוזכרים בתשובתו כקישורים ודוגמאות קוד.

כדי לענות על שאלתך, **@workspace** מחפש באותם מקורות שמפתח היה משתמש בהם בעת ניווט בבסיס הקוד ב-VS Code:

- כל הקבצים בסביבת העבודה, למעט קבצים שמדולגים בקובץ .gitignore

- מבנה התיקיות עם שמות תיקיות וקבצים מקוננים

- אינדקס חיפוש הקוד של GitHub, אם סביבת העבודה היא מאגר GitHub ומאונדקסת ע"י חיפוש קוד

- סמלים והגדרות בסביבת העבודה

- טקסט נבחר או טקסט גלוי בעורך הפעיל

הערה: .gitignore מתעלם אם יש לך קובץ פתוח או טקסט שנבחר בתוך קובץ מודלג.

מומלץ לקרוא בקישור זה [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **למידע נוסף על מעבדה זו**

GitHub Copilot שיפר מאוד את יעילות התכנות בארגונים, וכל ארגון מקווה להתאים אישית את הפונקציות הרלוונטיות של GitHub Copilot. ארגונים רבים התאימו תוספים דומים ל-GitHub Copilot בהתבסס על תרחישי העסקים שלהם ומודלים בקוד פתוח. עבור ארגונים, תוספים מותאמים קלים יותר לשליטה, אך הדבר משפיע גם על חוויית המשתמש. אחרי הכל, ל-GitHub Copilot יש פונקציות חזקות יותר בהתמודדות עם תרחישים כלליים ומקצועיים. אם ניתן לשמור על חוויה עקבית, יהיה עדיף להתאים אישית את התוסף של הארגון עצמו. GitHub Copilot Chat מספק APIs רלוונטיים לארגונים להרחבה בחוויית השיחה. שמירת חוויה עקבית וקיום פונקציות מותאמות היא חוויית משתמש טובה יותר.

מעבדה זו משתמשת בעיקר במודל Phi-3 בשילוב עם NPU מקומי והיברידי של Azure כדי לבנות סוכן מותאם אישית ב-GitHub Copilot Chat ***@PHI3*** כדי לסייע למפתחים ארגוניים בהשלמת יצירת קוד***(@PHI3 /gen)*** ויצירת קוד המבוסס על תמונות ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/he/cover.1017ebc9a7c46d09.webp)

### ***הערה:*** 

מעבדה זו מיושמת כרגע ב-AIPC של Intel CPU ו-Apple Silicon. נמשיך לעדכן את גרסת Qualcomm של NPU.

## **מעבדה**

| שם | תיאור | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - התקנות (✅) | הגדר והתקן סביבות וכלי התקנה קשורים | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - הפעלת זרימת פקודות עם Phi-3-mini (✅) | בשילוב עם AIPC / Apple Silicon, שימוש ב-NPU מקומי ליצירת קוד באמצעות Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - פריסת Phi-3-vision בשירות Azure Machine Learning (✅) | יצירת קוד על ידי פריסת קטלוג דגמים של Azure Machine Learning Service – דגם Phi-3-vision לתמונות | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - יצירת סוכן @phi-3 ב-GitHub Copilot Chat (✅)  | יצירת סוכן מותאם אישית Phi-3 ב-GitHub Copilot Chat להשלמת יצירת קוד, יצירת קוד גרפי, RAG וכולי | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| קוד דוגמה (✅)  | הורדת קוד דוגמה | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **משאבים**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. למידה נוספת על GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. למידה נוספת על GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. למידה נוספת על API של GitHub Copilot Chat [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. למידה נוספת על Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. למידה נוספת על קטלוג הדגמים של Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). אף כי אנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית יש להיחשב למקור הסמכותי. למידע קריטי, מומלץ תרגום מקצועי על ידי אדם. אנו לא אחראים לכל אי-הבנה או פרשנות מוטעית הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->