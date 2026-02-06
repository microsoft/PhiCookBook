## RAG с PromptFlow и AISearch

В този пример ще реализираме приложение за Retrieval Augmented Generation (RAG), използвайки Phi3 като SLM, AI Search като vectorDB и Prompt Flow като low-code оркестратор.

## Характеристики

- Лесно разгръщане с помощта на Docker.
- Скалираща се архитектура за обработка на AI работни потоци.
- Подход с нисък код чрез Prompt Flow.

## Предварителни изисквания

Преди да започнете, уверете се, че сте изпълнили следните условия:

- Инсталиран Docker на локалната ви машина.
- Azure акаунт с права за създаване и управление на контейнерни ресурси.
- Инстанции на Azure AI Studio и Azure AI Search.
- Модел за вграждане (embedding), с който да създадете индекса си (може да е Azure OpenAI embedding или OS модел от каталога).
- Инсталиран Python 3.8 или по-нова версия на локалната машина.
- Azure Container Registry (или друг регистър по ваш избор).

## Инсталация

1. Създайте нов flow в Azure AI Studio проекта си, използвайки файла flow.yaml.
2. Разположете Phi3 модел от Azure AI моделния каталог и създайте връзка към проекта си. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Създайте векторен индекс в Azure AI Search, използвайки произволен документ по ваш избор. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Разположете flow на управляван endpoint и го използвайте във файла prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Клонирайте репозитория:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Създайте Docker образ:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Качете Docker образа в Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Използване

1. Стартирайте Docker контейнера:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Достъпете приложението през браузъра си на адрес `http://localhost:8501`.

## Контакти

Валентина Алто - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Пълен статия: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.