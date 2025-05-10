<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:53:53+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "he"
}
-->
# שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX

המסמך הבא הוא דוגמה לאופן השימוש ב-PromptFlow עם ONNX (Open Neural Network Exchange) לפיתוח יישומי בינה מלאכותית מבוססי מודלים של Phi-3.

PromptFlow היא חבילת כלי פיתוח שמטרתה לייעל את מחזור הפיתוח המלא של יישומי AI מבוססי LLM (מודל שפה גדול), מהרעיון והפרוטוטייפ ועד לבדיקה והערכה.

באינטגרציה של PromptFlow עם ONNX, מפתחים יכולים:

- לשפר את ביצועי המודל: לנצל את ONNX לאינפרנס והפצה יעילים של המודל.
- לפשט את הפיתוח: להשתמש ב-PromptFlow לניהול זרימת העבודה ואוטומציה של משימות חוזרות.
- לחזק שיתוף פעולה: להקל על שיתוף פעולה בין חברי הצוות באמצעות סביבת פיתוח מאוחדת.

**Prompt flow** היא חבילת כלי פיתוח שמטרתה לייעל את מחזור הפיתוח המלא של יישומי AI מבוססי LLM, מהרעיונות, הפרוטוטייפ, הבדיקות וההערכה ועד לפריסה ומעקב בייצור. היא מפשטת מאוד את הנדסת הפרומפט ומאפשרת לבנות אפליקציות LLM באיכות ייצור.

Prompt flow יכולה להתחבר ל-OpenAI, Azure OpenAI Service, ולמודלים הניתנים להתאמה (Huggingface, LLM/SLM מקומי). אנו מקווים לפרוס את מודל ONNX הכמותי של Phi-3.5 ליישומים מקומיים. Prompt flow יכולה לסייע לנו לתכנן טוב יותר את העסק ולהשלים פתרונות מקומיים מבוססי Phi-3.5. בדוגמה זו, נשלב את ONNX Runtime GenAI Library להשלמת פתרון Prompt flow המבוסס על GPU של Windows.

## **התקנה**

### **ONNX Runtime GenAI עבור Windows GPU**

קראו מדריך זה כדי להגדיר ONNX Runtime GenAI עבור Windows GPU  [click here](./ORTWindowGPUGuideline.md)

### **הגדרת Prompt flow ב-VSCode**

1. התקינו את תוסף Prompt flow ל-VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.he.png)

2. לאחר התקנת התוסף, לחצו עליו ובחרו **Installation dependencies** ופעלו לפי המדריך להתקנת Prompt flow SDK בסביבתכם

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.he.png)

3. הורידו את [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ופתחו את הדוגמה ב-VS Code

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.he.png)

4. פתחו את **flow.dag.yaml** לבחירת סביבת Python שלכם

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.he.png)

   פתחו את **chat_phi3_ort.py** לשינוי מיקום מודל Phi-3.5-instruct ONNX שלכם

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.he.png)

5. הריצו את Prompt flow לבדיקה

פתחו את **flow.dag.yaml** ולחצו על העורך הוויזואלי

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.he.png)

לאחר הלחיצה, הריצו לבדיקה

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.he.png)

1. ניתן להריץ batch בטרמינל כדי לבדוק תוצאות נוספות


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

ניתן לבדוק את התוצאות בדפדפן המוגדר כברירת מחדל


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.he.png)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא אחראים לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.