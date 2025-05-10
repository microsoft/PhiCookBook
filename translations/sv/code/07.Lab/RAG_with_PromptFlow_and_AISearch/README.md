<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:12:53+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "sv"
}
-->
## RAG med PromptFlow och AISearch

I detta exempel implementerar vi en Retrieval Augmented Generation (RAG)-applikation som använder Phi3 som SLM, AI Search som vectorDB och Prompt Flow som low-code orchestrator.

## Funktioner

- Enkel distribution med Docker.
- Skalbar arkitektur för hantering av AI-arbetsflöden.
- Low-code metod med Prompt Flow

## Förutsättningar

Innan du börjar, se till att du uppfyller följande krav:

- Docker installerat på din lokala dator.
- Ett Azure-konto med behörighet att skapa och hantera containerresurser.
- Instanser av Azure AI Studio och Azure AI Search
- En embedding-modell för att skapa ditt index (kan vara antingen en Azure OpenAI-embedding eller en OS-modell från katalogen)
- Python 3.8 eller senare installerat på din lokala dator.
- Ett Azure Container Registry (eller valfri annan registry)

## Installation

1. Skapa ett nytt flow i ditt Azure AI Studio-projekt med hjälp av filen flow.yaml.
2. Distribuera en Phi3-modell från din Azure AI model katalog och skapa kopplingen till ditt projekt. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Skapa vector-indexet i Azure AI Search med valfritt dokument. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Distribuera flow på en hanterad endpoint och använd det i prompt-flow-frontend.py-filen. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klona repositoryt:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bygg Docker-imagen:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Skjut upp Docker-imagen till Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Användning

1. Kör Docker-containern:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Öppna applikationen i din webbläsare på `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Fullständig artikel: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.