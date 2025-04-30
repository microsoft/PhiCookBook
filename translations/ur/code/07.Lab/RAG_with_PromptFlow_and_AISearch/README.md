<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "962051ba495487884232e77fda80027f",
  "translation_date": "2025-04-03T06:26:49+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "ur"
}
-->
## RAG کے ساتھ PromptFlow اور AISearch

اس مثال میں، ہم Retrieval Augmented Generation (RAG) ایپلی کیشن کو نافذ کریں گے جو Phi3 کو SLM، AI Search کو vectorDB اور Prompt Flow کو low-code orchestrator کے طور پر استعمال کرے گا۔

## خصوصیات

- Docker کے ذریعے آسان تنصیب۔
- AI ورک فلو کو ہینڈل کرنے کے لیے قابل توسیع آرکیٹیکچر۔
- کم کوڈ اپروچ Prompt Flow کے ذریعے۔

## ضروریات

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ نے درج ذیل ضروریات کو پورا کر لیا ہے:

- آپ کے لوکل مشین پر Docker انسٹال ہو۔
- Azure اکاؤنٹ جس میں کنٹینر وسائل بنانے اور منظم کرنے کی اجازت ہو۔
- Azure AI Studio اور Azure AI Search انسٹینسز۔
- آپ کے انڈیکس بنانے کے لیے ایک embedding ماڈل (یہ Azure OpenAI embedding یا کیٹلاگ سے کوئی OS ماڈل ہو سکتا ہے)۔
- آپ کے لوکل مشین پر Python 3.8 یا اس سے زیادہ انسٹال ہو۔
- Azure Container Registry (یا آپ کے انتخاب کا کوئی بھی رجسٹری)۔

## تنصیب

1. Azure AI Studio پروجیکٹ پر flow.yaml فائل استعمال کرتے ہوئے نیا فلو بنائیں۔
2. Azure AI ماڈل کیٹلاگ سے Phi3 ماڈل کو ڈیپلائے کریں اور اپنے پروجیکٹ کے ساتھ کنکشن بنائیں۔ [Phi-3 کو Model as a Service کے طور پر ڈیپلائے کریں](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search پر اپنی مرضی کے کسی بھی دستاویز کے ذریعے vector index بنائیں۔ [Azure AI Search پر vector index بنائیں](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. فلو کو ایک managed endpoint پر ڈیپلائے کریں اور اسے prompt-flow-frontend.py فائل میں استعمال کریں۔ [فلو کو ایک online endpoint پر ڈیپلائے کریں](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. ریپوزٹری کلون کریں:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker امیج بنائیں:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker امیج کو Azure Container Registry پر پش کریں:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## استعمال

1. Docker کنٹینر چلائیں:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. اپنے براؤزر میں ایپلی کیشن کو `http://localhost:8501` پر ایکسیس کریں۔

## رابطہ

والنٹینا آلٹو - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مکمل مضمون: [Azure Model Catalog سے Phi-3-Medium کو Model as a Service کے طور پر RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے پوری کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔