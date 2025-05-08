<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-07T15:18:39+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "ur"
}
-->
## RAG with PromptFlow and AISearch

اس مثال میں، ہم Retrieval Augmented Generation (RAG) ایپلیکیشن کو Phi3 کو SLM کے طور پر، AI Search کو vectorDB کے طور پر اور Prompt Flow کو low-code orchestrator کے طور پر استعمال کرتے ہوئے نافذ کریں گے۔

## Features

- Docker کے ذریعے آسان تعیناتی۔
- AI ورک فلو کو سنبھالنے کے لیے قابل توسیع فن تعمیر۔
- Prompt Flow کا استعمال کرتے ہوئے کم کوڈ کا طریقہ۔

## Prerequisites

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ نے درج ذیل ضروریات پوری کر لی ہیں:

- آپ کی مقامی مشین پر Docker انسٹال ہو۔
- Azure اکاؤنٹ جس کے پاس container resources بنانے اور منظم کرنے کی اجازت ہو۔
- Azure AI Studio اور Azure AI Search کی مثالیں۔
- ایک embedding ماڈل تاکہ آپ اپنا انڈیکس بنا سکیں (یہ Azure OpenAI embedding ہو سکتا ہے یا کیٹلاگ کا کوئی OS ماڈل)۔
- Python 3.8 یا اس کے بعد کا ورژن آپ کی مقامی مشین پر انسٹال ہو۔
- Azure Container Registry (یا آپ کی پسند کا کوئی بھی رجسٹری)۔

## Installation

1. اپنے Azure AI Studio پروجیکٹ پر flow.yaml فائل کا استعمال کرتے ہوئے نیا فلو بنائیں۔
2. اپنے Azure AI ماڈل کیٹلاگ سے Phi3 ماڈل تعینات کریں اور اپنے پروجیکٹ سے کنکشن بنائیں۔ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search پر vector انڈیکس بنائیں، کوئی بھی دستاویز استعمال کر سکتے ہیں۔ [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. فلو کو managed endpoint پر تعینات کریں اور اسے prompt-flow-frontend.py فائل میں استعمال کریں۔ [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. repository کلون کریں:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker امیج بنائیں:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker امیج کو Azure Container Registry پر push کریں:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Usage

1. Docker container چلائیں:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. اپنے براؤزر میں `http://localhost:8501` پر ایپلیکیشن تک رسائی حاصل کریں۔

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مکمل مضمون: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم نوٹ کریں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔