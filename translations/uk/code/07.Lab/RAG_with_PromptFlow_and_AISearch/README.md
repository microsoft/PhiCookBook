<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:11:31+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "uk"
}
-->
## RAG з PromptFlow та AISearch

У цьому прикладі ми реалізуємо застосунок Retrieval Augmented Generation (RAG), використовуючи Phi3 як SLM, AI Search як vectorDB та Prompt Flow як low-code оркестратор.

## Особливості

- Легке розгортання за допомогою Docker.
- Масштабована архітектура для обробки AI робочих процесів.
- Підхід з низьким рівнем кодування за допомогою Prompt Flow.

## Вимоги

Перед початком переконайтеся, що ви виконали наступні умови:

- Встановлений Docker на вашому локальному комп’ютері.
- Обліковий запис Azure з правами на створення та керування контейнерними ресурсами.
- Екземпляри Azure AI Studio та Azure AI Search.
- Модель для створення векторного індексу (може бути Azure OpenAI embedding або модель з відкритим кодом з каталогу).
- Встановлений Python 3.8 або новіша версія на вашому локальному комп’ютері.
- Azure Container Registry (або будь-який інший реєстр на ваш вибір).

## Встановлення

1. Створіть новий flow у вашому проекті Azure AI Studio, використовуючи файл flow.yaml.
2. Розгорніть модель Phi3 з каталогу моделей Azure AI та створіть підключення до вашого проекту. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Створіть векторний індекс в Azure AI Search, використовуючи будь-який документ на ваш вибір. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Розгорніть flow на керованій кінцевій точці та використовуйте його у файлі prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Клонуйте репозиторій:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Створіть Docker-образ:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Завантажте Docker-образ у Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Використання

1. Запустіть Docker-контейнер:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Відкрийте застосунок у браузері за адресою `http://localhost:8501`.

## Контакти

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Повна стаття: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.