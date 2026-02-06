## RAG with PromptFlow and AISearch

اس مثال میں، ہم Retrieval Augmented Generation (RAG) ایپلیکیشن کو Phi3 کو SLM کے طور پر، AI Search کو vectorDB کے طور پر اور Prompt Flow کو low-code orchestrator کے طور پر استعمال کرتے ہوئے نافذ کریں گے۔

## خصوصیات

- Docker کے ذریعے آسان تعیناتی۔
- AI ورک فلو کو سنبھالنے کے لیے قابل توسیع فن تعمیر۔
- Prompt Flow کے ذریعے کم کوڈ والا طریقہ۔

## ضروریات

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ نے درج ذیل شرائط پوری کر لی ہیں:

- آپ کے مقامی کمپیوٹر پر Docker انسٹال ہو۔
- Azure اکاؤنٹ جس میں container resources بنانے اور منظم کرنے کی اجازت ہو۔
- Azure AI Studio اور Azure AI Search کے انسٹینسز۔
- ایک embedding ماڈل تاکہ آپ اپنا انڈیکس بنا سکیں (یہ Azure OpenAI embedding ہو سکتا ہے یا کیٹلاگ سے کوئی OS ماڈل)۔
- Python 3.8 یا اس کے بعد کا ورژن آپ کے مقامی کمپیوٹر پر انسٹال ہو۔
- Azure Container Registry (یا آپ کی پسند کا کوئی بھی رجسٹری)۔

## تنصیب

1. اپنے Azure AI Studio پروجیکٹ میں flow.yaml فائل استعمال کرتے ہوئے نیا فلو بنائیں۔
2. اپنے Azure AI ماڈل کیٹلاگ سے Phi3 ماڈل تعینات کریں اور اپنے پروجیکٹ سے کنکشن بنائیں۔ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search پر اپنی پسند کے کسی بھی دستاویز کا استعمال کرتے ہوئے vector انڈیکس بنائیں۔ [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. فلو کو managed endpoint پر تعینات کریں اور اسے prompt-flow-frontend.py فائل میں استعمال کریں۔ [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. ریپوزیٹری کلون کریں:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker امیج بنائیں:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker امیج کو Azure Container Registry میں پش کریں:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## استعمال

1. Docker container چلائیں:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. اپنے براؤزر میں `http://localhost:8501` پر ایپلیکیشن تک رسائی حاصل کریں۔

## رابطہ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مکمل مضمون: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔