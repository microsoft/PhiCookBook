<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:13:33+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "he"
}
-->
## RAG עם PromptFlow ו-AISearch

בדוגמה הזו, נממש אפליקציית Retrieval Augmented Generation (RAG) תוך שימוש ב-Phi3 כ-SLM, AI Search כ-vectorDB ו-Prompt Flow כמנהל תהליכים בקוד נמוך.

## תכונות

- פריסה קלה באמצעות Docker.
- ארכיטקטורה סקלאבילית לטיפול בזרימות עבודה של AI.
- גישה בקוד נמוך באמצעות Prompt Flow.

## דרישות מוקדמות

לפני שמתחילים, ודאו שעומדים בדרישות הבאות:

- Docker מותקן על המחשב המקומי שלכם.
- חשבון Azure עם הרשאות ליצירה וניהול של משאבי מכולות.
- מופעי Azure AI Studio ו-Azure AI Search.
- מודל הטמעה ליצירת האינדקס שלכם (יכול להיות מודל Azure OpenAI embedding או מודל OS מהקטלוג).
- Python 3.8 או גרסה מאוחרת יותר מותקנת על המחשב המקומי.
- Azure Container Registry (או כל רישום שתבחרו).

## התקנה

1. צרו זרימה חדשה בפרויקט Azure AI Studio שלכם באמצעות הקובץ flow.yaml.
2. פרסמו מודל Phi3 מהקטלוג של מודלי Azure AI וצרו את החיבור לפרויקט שלכם. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. צרו את אינדקס הווקטורים ב-Azure AI Search באמצעות כל מסמך שתבחרו. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. פרסמו את הזרימה בנקודת קצה מנוהלת והשתמשו בה בקובץ prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. שכפלו את המאגר:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. בנו את תמונת ה-Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. דחפו את תמונת ה-Docker ל-Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## שימוש

1. הריצו את מכולת ה-Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. גשו לאפליקציה בדפדפן בכתובת `http://localhost:8501`.

## יצירת קשר

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

מאמר מלא: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.