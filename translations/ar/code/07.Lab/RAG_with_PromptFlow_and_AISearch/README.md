## RAG مع PromptFlow و AISearch

في هذا المثال، سنقوم بتنفيذ تطبيق استرجاع معزز بالتوليد (RAG) باستخدام Phi3 كنموذج لغة صغيرة (SLM)، و AI Search كقاعدة بيانات متجهات، و Prompt Flow كمنسق منخفض الكود.

## الميزات

- نشر سهل باستخدام Docker.
- بنية قابلة للتوسع لمعالجة تدفقات عمل الذكاء الاصطناعي.
- نهج منخفض الكود باستخدام Prompt Flow.

## المتطلبات الأساسية

قبل أن تبدأ، تأكد من استيفاء المتطلبات التالية:

- تثبيت Docker على جهازك المحلي.
- حساب Azure مع أذونات لإنشاء وإدارة موارد الحاويات.
- وجود Azure AI Studio و Azure AI Search.
- نموذج تضمين لإنشاء الفهرس الخاص بك (يمكن أن يكون إما تضمين Azure OpenAI أو نموذج مفتوح المصدر من الكتالوج).
- تثبيت Python 3.8 أو أحدث على جهازك المحلي.
- سجل حاويات Azure (أو أي سجل تختاره).

## التثبيت

1. أنشئ تدفقًا جديدًا في مشروع Azure AI Studio الخاص بك باستخدام ملف flow.yaml.
2. انشر نموذج Phi3 من كتالوج نماذج Azure AI وأنشئ الاتصال بمشروعك. [نشر Phi-3 كنموذج كخدمة](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. أنشئ فهرس المتجهات على Azure AI Search باستخدام أي مستند تختاره [إنشاء فهرس متجهات على Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. انشر التدفق على نقطة نهاية مُدارة واستخدمه في ملف prompt-flow-frontend.py. [نشر تدفق على نقطة نهاية عبر الإنترنت](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. استنسخ المستودع:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. أنشئ صورة Docker:

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

1. شغّل حاوية Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ادخل إلى التطبيق في متصفحك على العنوان `http://localhost:8501`.

## التواصل

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

المقال الكامل: [RAG مع Phi-3-Medium كنموذج كخدمة من كتالوج نماذج Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.