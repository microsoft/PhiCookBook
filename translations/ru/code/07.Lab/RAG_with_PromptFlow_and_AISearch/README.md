<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:05:47+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "ru"
}
-->
## RAG с PromptFlow и AISearch

В этом примере мы реализуем приложение Retrieval Augmented Generation (RAG), используя Phi3 в качестве SLM, AI Search как vectorDB и Prompt Flow в роли low-code оркестратора.

## Особенности

- Простое развертывание с помощью Docker.
- Масштабируемая архитектура для обработки AI-воркфлоу.
- Подход с низким уровнем кода с использованием Prompt Flow.

## Требования

Перед началом убедитесь, что вы выполнили следующие условия:

- Docker установлен на вашем локальном компьютере.
- Аккаунт Azure с правами на создание и управление контейнерными ресурсами.
- Инстансы Azure AI Studio и Azure AI Search.
- Модель эмбеддингов для создания индекса (может быть либо Azure OpenAI embedding, либо OS-модель из каталога).
- Python 3.8 или новее, установленный на вашем локальном компьютере.
- Azure Container Registry (или любой другой реестр по вашему выбору).

## Установка

1. Создайте новый flow в вашем проекте Azure AI Studio, используя файл flow.yaml.
2. Разверните модель Phi3 из каталога моделей Azure AI и создайте подключение к вашему проекту. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Создайте векторный индекс в Azure AI Search, используя любой выбранный вами документ. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Разверните flow на управляемой конечной точке и используйте его в файле prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Клонируйте репозиторий:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Соберите Docker-образ:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Отправьте Docker-образ в Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Использование

1. Запустите Docker-контейнер:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Откройте приложение в браузере по адресу `http://localhost:8501`.

## Контакты

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Полная статья: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.