<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:01:49+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "he"
}
-->
# שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX

המסמך הבא הוא דוגמה לאופן השימוש ב-PromptFlow עם ONNX (Open Neural Network Exchange) לפיתוח יישומי בינה מלאכותית מבוססי מודלים מסוג Phi-3.

PromptFlow היא חבילת כלים לפיתוח שמטרתה לייעל את מחזור הפיתוח המלא של יישומי בינה מלאכותית מבוססי LLM (Large Language Model), החל מרעיונות ופרוטוטייפינג ועד לבדיקות והערכה.

באמצעות שילוב של PromptFlow עם ONNX, מפתחים יכולים:

- לשפר את ביצועי המודל: לנצל את ONNX לאינפרנס ופריסה יעילים של המודל.
- לפשט את הפיתוח: להשתמש ב-PromptFlow לניהול זרימת העבודה ואוטומציה של משימות חוזרות.
- לשפר את שיתוף הפעולה: לאפשר שיתוף פעולה טוב יותר בין חברי הצוות על ידי מתן סביבת פיתוח מאוחדת.

**Prompt flow** היא חבילת כלים לפיתוח שמטרתה לייעל את מחזור הפיתוח המלא של יישומי בינה מלאכותית מבוססי LLM, החל מרעיונות, פרוטוטייפינג, בדיקות, הערכה ועד לפריסה ומעקב בייצור. היא מקלה מאוד על הנדסת הפרומפט ומאפשרת לבנות אפליקציות LLM באיכות ייצור.

Prompt flow יכולה להתחבר ל-OpenAI, Azure OpenAI Service, ולמודלים מותאמים אישית (Huggingface, LLM/SLM מקומי). אנו מקווים לפרוס את מודל ONNX הכמותי של Phi-3.5 באפליקציות מקומיות. Prompt flow יכולה לעזור לנו לתכנן טוב יותר את העסק ולהשלים פתרונות מקומיים מבוססי Phi-3.5. בדוגמה זו, נשלב את ONNX Runtime GenAI Library כדי להשלים את פתרון Prompt flow מבוסס Windows GPU.

## **התקנה**

### **ONNX Runtime GenAI עבור Windows GPU**

קראו את ההנחיות להגדרת ONNX Runtime GenAI עבור Windows GPU [לחצו כאן](./ORTWindowGPUGuideline.md)

### **הגדרת Prompt flow ב-VSCode**

1. התקינו את תוסף Prompt flow ל-VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.he.png)

2. לאחר התקנת התוסף, לחצו עליו ובחרו **Installation dependencies** ופעלו לפי ההנחיות להתקנת Prompt flow SDK בסביבת העבודה שלכם

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.he.png)

3. הורידו את [קוד הדוגמה](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ופתחו אותו ב-VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.he.png)

4. פתחו את הקובץ **flow.dag.yaml** כדי לבחור את סביבת הפייתון שלכם

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.he.png)

   פתחו את **chat_phi3_ort.py** כדי לשנות את מיקום מודל Phi-3.5-instruct ONNX שלכם

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.he.png)

5. הריצו את ה-prompt flow שלכם לבדיקה

פתחו את **flow.dag.yaml** ולחצו על העורך הוויזואלי

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.he.png)

לאחר הלחיצה, הריצו את הפתרון לבדיקה

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.he.png)

1. ניתן להריץ אצווה בטרמינל כדי לבדוק תוצאות נוספות


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

ניתן לבדוק את התוצאות בדפדפן המוגדר כברירת מחדל


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.he.png)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.