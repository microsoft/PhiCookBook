<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-03-27T04:44:52+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "ar"
}
-->
## استخدام RAG مع PromptFlow و AISearch

في هذا المثال، سنقوم بتنفيذ تطبيق استرجاع معزز للتوليد (RAG) باستخدام Phi3 كنموذج لغة دلالي (SLM)، و AI Search كقاعدة بيانات متجهة، و Prompt Flow كمنظم منخفض الكود.

## الميزات

- نشر سهل باستخدام Docker.
- بنية قابلة للتوسع لمعالجة سير العمل الخاص بالذكاء الاصطناعي.
- نهج منخفض الكود باستخدام Prompt Flow.

## المتطلبات الأساسية

قبل البدء، تأكد من تلبية المتطلبات التالية:

- تثبيت Docker على جهازك المحلي.
- حساب Azure مع صلاحيات لإنشاء وإدارة موارد الحاويات.
- وجود Azure AI Studio و Azure AI Search.
- نموذج تضمين لإنشاء الفهرس الخاص بك (يمكن أن يكون نموذج تضمين Azure OpenAI أو نموذج مفتوح المصدر من الكتالوج).
- تثبيت Python 3.8 أو إصدار أحدث على جهازك المحلي.
- سجل حاويات Azure (أو أي سجل من اختيارك).

## التثبيت

1. أنشئ تدفقًا جديدًا في مشروع Azure AI Studio باستخدام ملف flow.yaml.
2. قم بنشر نموذج Phi3 من كتالوج نماذج Azure AI وربط الاتصال بمشروعك. [نشر Phi-3 كنموذج كخدمة](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. أنشئ فهرسًا متجهًا على Azure AI Search باستخدام أي مستند تختاره. [إنشاء فهرس متجه على Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. قم بنشر التدفق على نقطة نهاية مُدارة واستخدمه في ملف prompt-flow-frontend.py. [نشر تدفق على نقطة نهاية عبر الإنترنت](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. استنسخ المستودع:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. قم ببناء صورة Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. ادفع صورة Docker إلى سجل حاويات Azure:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## الاستخدام

1. قم بتشغيل حاوية Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. افتح التطبيق في متصفحك على `http://localhost:8501`.

## التواصل

فالنتينا ألتو - [لينكد إن](https://www.linkedin.com/in/valentina-alto-6a0590148/)

المقال الكامل: [RAG باستخدام Phi-3-Medium كنموذج كخدمة من كتالوج نماذج Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. بالنسبة للمعلومات الحساسة أو الهامة، يُوصى بالاستعانة بخدمات الترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ نتيجة استخدام هذه الترجمة.