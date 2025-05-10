<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:11:44+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "pa"
}
-->
## RAG with PromptFlow and AISearch

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ Retrieval Augmented Generation (RAG) ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਲਾਗੂ ਕਰਾਂਗੇ ਜੋ Phi3 ਨੂੰ SLM ਵਜੋਂ, AI Search ਨੂੰ vectorDB ਵਜੋਂ ਅਤੇ Prompt Flow ਨੂੰ low-code orchestrator ਵਜੋਂ ਵਰਤਦਾ ਹੈ।

## ਫੀਚਰ

- Docker ਦੀ ਵਰਤੋਂ ਨਾਲ ਆਸਾਨ ਤੌਰ 'ਤੇ ਡਿਪਲੋਇਮੈਂਟ।
- AI ਵਰਕਫਲੋਜ਼ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਸਕੇਲਏਬਲ ਆਰਕੀਟੈਕਚਰ।
- Prompt Flow ਦੀ ਵਰਤੋਂ ਨਾਲ ਲੋ ਕੋਡ ਅਪ੍ਰੋਚ।

## ਜਰੂਰੀਆਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਹੇਠ ਲਿਖੀਆਂ ਲੋੜਾਂ ਪੂਰੀਆਂ ਕੀਤੀਆਂ ਹਨ:

- ਤੁਹਾਡੇ ਸਥਾਨਕ ਮਸ਼ੀਨ 'ਤੇ Docker ਇੰਸਟਾਲ ਹੋਇਆ ਹੋਵੇ।
- Azure ਖਾਤਾ ਜਿਸ ਵਿੱਚ ਕੰਟੇਨਰ ਰਿਸੋਰਸ ਬਣਾਉਣ ਅਤੇ ਪ੍ਰਬੰਧਨ ਕਰਨ ਦੀ ਪਰਮੀਸ਼ਨ ਹੋਵੇ।
- Azure AI Studio ਅਤੇ Azure AI Search ਇੰਸਟੈਂਸ।
- ਇੱਕ embedding ਮਾਡਲ ਜੋ ਤੁਹਾਡੇ ਇੰਡੈਕਸ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾਵੇ (ਇਹ Azure OpenAI embedding ਜਾਂ ਕੈਟਾਲੌਗ ਤੋਂ ਕੋਈ OS ਮਾਡਲ ਹੋ ਸਕਦਾ ਹੈ)।
- ਤੁਹਾਡੇ ਸਥਾਨਕ ਮਸ਼ੀਨ 'ਤੇ Python 3.8 ਜਾਂ ਉਸ ਤੋਂ ਬਾਅਦ ਦਾ ਵਰਜਨ ਇੰਸਟਾਲ ਹੋਵੇ।
- ਇੱਕ Azure Container Registry (ਜਾਂ ਤੁਹਾਡੇ ਚੋਣ ਦੇ ਕਿਸੇ ਵੀ ਰਜਿਸਟਰੀ)।

## ਇੰਸਟਾਲੇਸ਼ਨ

1. ਆਪਣੇ Azure AI Studio ਪ੍ਰੋਜੈਕਟ 'ਤੇ flow.yaml ਫਾਈਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਨਵਾਂ ਫਲੋ ਬਣਾਓ।
2. ਆਪਣੇ Azure AI ਮਾਡਲ ਕੈਟਾਲੌਗ ਤੋਂ Phi3 ਮਾਡਲ ਡਿਪਲੋਇ ਕਰੋ ਅਤੇ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਨਾਲ ਕਨੈਕਸ਼ਨ ਬਣਾਓ। [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search 'ਤੇ ਕਿਸੇ ਵੀ ਦਸਤਾਵੇਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ vector index ਬਣਾਓ। [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. ਮੈਨੇਜਡ ਐਂਡਪੌਇੰਟ 'ਤੇ ਫਲੋ ਡਿਪਲੋਇ ਕਰੋ ਅਤੇ ਇਸਨੂੰ prompt-flow-frontend.py ਫਾਈਲ ਵਿੱਚ ਵਰਤੋ। [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰੋ:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker ਇਮੇਜ ਬਣਾਓ:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker ਇਮੇਜ ਨੂੰ Azure Container Registry 'ਤੇ ਪੁਸ਼ ਕਰੋ:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## ਵਰਤੋਂ

1. Docker ਕੰਟੇਨਰ ਚਲਾਓ:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ਆਪਣੇ ਬ੍ਰਾਉਜ਼ਰ ਵਿੱਚ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ `http://localhost:8501` 'ਤੇ ਐਕਸੈੱਸ ਕਰੋ।

## ਸੰਪਰਕ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

ਪੂਰਾ ਲੇਖ: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।