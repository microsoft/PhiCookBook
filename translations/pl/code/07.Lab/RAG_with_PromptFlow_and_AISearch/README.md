<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:08:16+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "pl"
}
-->
## RAG z PromptFlow i AISearch

W tym przykładzie zaimplementujemy aplikację Retrieval Augmented Generation (RAG), wykorzystując Phi3 jako SLM, AI Search jako vectorDB oraz Prompt Flow jako narzędzie do niskokodowej orkiestracji.

## Funkcje

- Łatwa instalacja za pomocą Dockera.
- Skalowalna architektura do obsługi przepływów pracy AI.
- Podejście low-code z użyciem Prompt Flow.

## Wymagania wstępne

Zanim zaczniesz, upewnij się, że spełniasz następujące wymagania:

- Docker zainstalowany na lokalnym komputerze.
- Konto Azure z uprawnieniami do tworzenia i zarządzania zasobami kontenerowymi.
- Instancje Azure AI Studio oraz Azure AI Search.
- Model embeddingowy do stworzenia indeksu (może to być Azure OpenAI embedding lub model OS z katalogu).
- Python 3.8 lub nowszy zainstalowany na lokalnym komputerze.
- Azure Container Registry (lub dowolny inny rejestr kontenerów).

## Instalacja

1. Utwórz nowy flow w swoim projekcie Azure AI Studio, korzystając z pliku flow.yaml.
2. Wdróż model Phi3 z katalogu modeli Azure AI i połącz go ze swoim projektem. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Utwórz indeks wektorowy w Azure AI Search, używając dowolnego dokumentu. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Wdróż flow na zarządzanym endpointzie i użyj go w pliku prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Sklonuj repozytorium:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Zbuduj obraz Dockera:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Wypchnij obraz Dockera do Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Użytkowanie

1. Uruchom kontener Dockera:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Uzyskaj dostęp do aplikacji w przeglądarce pod adresem `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Pełny artykuł: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.