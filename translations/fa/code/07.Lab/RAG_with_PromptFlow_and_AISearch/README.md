## RAG با PromptFlow و AISearch

در این مثال، یک برنامه تولید تقویت‌شده با بازیابی (RAG) را پیاده‌سازی می‌کنیم که از Phi3 به عنوان SLM، AI Search به عنوان vectorDB و Prompt Flow به عنوان هماهنگ‌کننده کم‌کد استفاده می‌کند.

## ویژگی‌ها

- استقرار آسان با استفاده از Docker.
- معماری مقیاس‌پذیر برای مدیریت جریان‌های کاری هوش مصنوعی.
- رویکرد کم‌کد با استفاده از Prompt Flow

## پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر را دارید:

- نصب Docker روی دستگاه محلی شما.
- حساب Azure با دسترسی برای ایجاد و مدیریت منابع کانتینر.
- نمونه‌های Azure AI Studio و Azure AI Search
- یک مدل embedding برای ایجاد ایندکس شما (می‌تواند مدل embedding Azure OpenAI یا مدل OS از کاتالوگ باشد)
- نصب Python 3.8 یا نسخه‌های بالاتر روی دستگاه محلی شما.
- یک Azure Container Registry (یا هر رجیستری دلخواه شما)

## نصب

1. یک جریان جدید در پروژه Azure AI Studio خود با استفاده از فایل flow.yaml ایجاد کنید.
2. یک مدل Phi3 از کاتالوگ مدل Azure AI خود مستقر کنید و اتصال آن را به پروژه خود برقرار کنید. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. ایندکس برداری را در Azure AI Search با استفاده از هر سند دلخواه خود ایجاد کنید [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. جریان را روی یک endpoint مدیریت‌شده مستقر کنید و از آن در فایل prompt-flow-frontend.py استفاده کنید. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
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

2. به برنامه در مرورگر خود در آدرس `http://localhost:8501` دسترسی پیدا کنید.

## تماس

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مقاله کامل: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.