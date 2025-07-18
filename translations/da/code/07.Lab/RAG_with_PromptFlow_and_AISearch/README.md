<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:08:58+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "da"
}
-->
## RAG med PromptFlow og AISearch

I dette eksempel implementerer vi en Retrieval Augmented Generation (RAG) applikation, der bruger Phi3 som SLM, AI Search som vectorDB og Prompt Flow som low-code orkestrator.

## Funktioner

- Nem udrulning med Docker.
- Skalerbar arkitektur til håndtering af AI-workflows.
- Low-code tilgang med Prompt Flow.

## Forudsætninger

Før du går i gang, skal du sikre dig, at du opfylder følgende krav:

- Docker installeret på din lokale maskine.
- En Azure-konto med tilladelser til at oprette og administrere container-ressourcer.
- En Azure AI Studio og Azure AI Search instans.
- En embedding-model til at oprette dit indeks (kan være enten en Azure OpenAI embedding eller en OS-model fra kataloget).
- Python 3.8 eller nyere installeret på din lokale maskine.
- Et Azure Container Registry (eller et andet registry efter eget valg).

## Installation

1. Opret et nyt flow i dit Azure AI Studio-projekt ved hjælp af flow.yaml-filen.
2. Udrul en Phi3 Model fra dit Azure AI modelkatalog og opret forbindelsen til dit projekt. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Opret vector-indekset på Azure AI Search ved hjælp af et dokument efter eget valg [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Udrul flowet på en managed endpoint og brug det i prompt-flow-frontend.py-filen. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klon repositoryet:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Byg Docker-billedet:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Push Docker-billedet til Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Brug

1. Kør Docker-containeren:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Åbn applikationen i din browser på `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Fuld artikel: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.