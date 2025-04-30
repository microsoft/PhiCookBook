<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-03-27T04:43:49+00:00",
  "source_file": "code\\07.Lab\\RAG_with_PromptFlow_and_AISearch\\README.md",
  "language_code": "ru"
}
-->
## RAG с PromptFlow и AISearch

В этом примере мы реализуем приложение Retrieval Augmented Generation (RAG), используя Phi3 в качестве SLM, AI Search в качестве vectorDB и Prompt Flow в качестве low-code оркестратора.

## Возможности

- Простое развертывание с использованием Docker.
- Масштабируемая архитектура для работы с AI-процессами.
- Подход с минимальным количеством кода благодаря Prompt Flow.

## Необходимые условия

Перед началом убедитесь, что выполнены следующие требования:

- Установлен Docker на вашем локальном компьютере.
- У вас есть учетная запись Azure с правами на создание и управление контейнерными ресурсами.
- Экземпляры Azure AI Studio и Azure AI Search.
- Модель для создания эмбеддингов для индекса (может быть либо Azure OpenAI embedding, либо модель из каталога OS).
- Установлен Python версии 3.8 или выше на вашем локальном компьютере.
- Azure Container Registry (или любой другой реестр на ваш выбор).

## Установка

1. Создайте новый flow в вашем проекте Azure AI Studio, используя файл flow.yaml.
2. Разверните модель Phi3 из каталога моделей Azure AI и создайте подключение к вашему проекту. [Развернуть Phi-3 как Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Создайте векторный индекс в Azure AI Search, используя любой документ на ваш выбор. [Создать векторный индекс в Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Разверните flow на управляемой конечной точке и используйте его в файле prompt-flow-frontend.py. [Развернуть flow на онлайн-конечной точке](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
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

Валентина Альто - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Полная статья: [RAG с Phi-3-Medium как Model as a Service из каталога моделей Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.