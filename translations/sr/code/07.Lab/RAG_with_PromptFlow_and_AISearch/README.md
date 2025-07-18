<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:10:57+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "sr"
}
-->
## RAG са PromptFlow и AISearch

У овом примеру ћемо имплементирати апликацију за генерацију уз подршку претраживања (Retrieval Augmented Generation - RAG) користећи Phi3 као SLM, AI Search као vectorDB и Prompt Flow као low-code оркестратор.

## Карактеристике

- Лако постављање помоћу Docker-а.
- Скалирајућа архитектура за руковање AI радним токовима.
- Low code приступ коришћењем Prompt Flow-а.

## Захтеви

Пре него што почнете, уверите се да испуњавате следеће услове:

- Docker инсталиран на вашем локалном рачунару.
- Azure налог са дозволама за креирање и управљање контејнер ресурсима.
- Инстанце Azure AI Studio и Azure AI Search.
- Модел за уграђивање (embedding) за креирање индекса (може бити Azure OpenAI embedding или OS модел из каталога).
- Python 3.8 или новији инсталиран на вашем локалном рачунару.
- Azure Container Registry (или било који регистар по вашем избору).

## Инсталација

1. Креирајте нови flow у вашем Azure AI Studio пројекту користећи flow.yaml фајл.
2. Деплојујте Phi3 модел из вашег Azure AI model каталога и повежите га са пројектом. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Креирајте vector индекс на Azure AI Search користећи било који документ по вашем избору. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Деплојујте flow на managed endpoint и користите га у prompt-flow-frontend.py фајлу. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Клонирајте репозиторијум:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Направите Docker слику:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Пошаљите Docker слику у Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Коришћење

1. Покрените Docker контејнер:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Приступите апликацији у вашем прегледачу на адреси `http://localhost:8501`.

## Контакт

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Цео чланак: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.