<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-07T15:18:18+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "fa"
}
-->
## RAG با PromptFlow و AISearch

در این مثال، یک برنامه تولید افزوده بازیابی (RAG) را با استفاده از Phi3 به عنوان SLM، AI Search به عنوان vectorDB و Prompt Flow به عنوان هماهنگ‌کننده کم‌کد پیاده‌سازی خواهیم کرد.

## ویژگی‌ها

- استقرار آسان با استفاده از Docker.
- معماری مقیاس‌پذیر برای مدیریت جریان‌های کاری هوش مصنوعی.
- رویکرد کم‌کد با استفاده از Prompt Flow

## پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر را دارید:

- نصب Docker روی دستگاه محلی شما.
- یک حساب Azure با دسترسی برای ایجاد و مدیریت منابع کانتینر.
- نمونه‌های Azure AI Studio و Azure AI Search
- یک مدل embedding برای ایجاد ایندکس خود (می‌تواند embedding Azure OpenAI یا مدل OS از کاتالوگ باشد)
- نصب Python 3.8 یا نسخه‌های جدیدتر روی دستگاه محلی.
- یک Azure Container Registry (یا هر رجیستری دلخواه)

## نصب

1. ایجاد یک فلو جدید در پروژه Azure AI Studio خود با استفاده از فایل flow.yaml.
2. استقرار مدل Phi3 از کاتالوگ مدل Azure AI خود و ایجاد اتصال به پروژه. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. ایجاد ایندکس برداری روی Azure AI Search با استفاده از هر سندی که می‌خواهید [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. استقرار فلو روی یک endpoint مدیریت‌شده و استفاده از آن در فایل prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. کلون کردن مخزن:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. ساخت ایمیج Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. ارسال ایمیج Docker به Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## استفاده

1. اجرای کانتینر Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. دسترسی به برنامه در مرورگر خود در آدرس `http://localhost:8501`.

## تماس

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مقاله کامل: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچگونه سوءتفاهم یا برداشت نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.