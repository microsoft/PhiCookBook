<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-03-27T04:45:53+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "fa"
}
-->
## RAG با PromptFlow و AISearch

در این مثال، یک برنامه تولید افزوده با بازیابی (RAG) را پیاده‌سازی خواهیم کرد که از Phi3 به عنوان SLM، AI Search به عنوان vectorDB و Prompt Flow به عنوان هماهنگ‌کننده کم‌کد استفاده می‌کند.

## ویژگی‌ها

- استقرار آسان با استفاده از Docker.
- معماری مقیاس‌پذیر برای مدیریت جریان‌های کاری هوش مصنوعی.
- رویکرد کم‌کد با استفاده از Prompt Flow.

## پیش‌نیازها

پیش از شروع، اطمینان حاصل کنید که موارد زیر را آماده کرده‌اید:

- Docker بر روی سیستم شما نصب شده باشد.
- یک حساب Azure با دسترسی برای ایجاد و مدیریت منابع کانتینری.
- نمونه‌های Azure AI Studio و Azure AI Search.
- یک مدل embedding برای ایجاد ایندکس (می‌تواند یک embedding از Azure OpenAI یا یک مدل OS از کاتالوگ باشد).
- Python نسخه 3.8 یا بالاتر بر روی سیستم شما نصب شده باشد.
- یک Azure Container Registry (یا هر رجیستری دیگری که انتخاب کرده‌اید).

## نصب

1. یک جریان جدید در پروژه Azure AI Studio خود با استفاده از فایل flow.yaml ایجاد کنید.
2. مدل Phi3 را از کاتالوگ مدل Azure AI استقرار دهید و اتصال آن را به پروژه خود برقرار کنید. [استقرار Phi-3 به عنوان مدل به عنوان سرویس](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. ایندکس برداری را در Azure AI Search با استفاده از هر سندی که انتخاب کرده‌اید ایجاد کنید. [ایجاد ایندکس برداری در Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. جریان را بر روی یک نقطه پایانی مدیریت شده مستقر کنید و از آن در فایل prompt-flow-frontend.py استفاده کنید. [استقرار جریان بر روی نقطه پایانی آنلاین](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. مخزن را کلون کنید:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. تصویر Docker را بسازید:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. تصویر Docker را به Azure Container Registry ارسال کنید:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## استفاده

1. کانتینر Docker را اجرا کنید:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. به برنامه در مرورگر خود در `http://localhost:8501` دسترسی پیدا کنید.

## تماس

والنتینا آلتو - [لینکدین](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مقاله کامل: [RAG با Phi-3-Medium به عنوان مدل به عنوان سرویس از کاتالوگ مدل Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ‌گونه سوءتفاهم یا تفسیر اشتباهی که از استفاده از این ترجمه ناشی شود، نیستیم.