<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:13:07+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "no"
}
-->
## RAG med PromptFlow og AISearch

I dette eksempelet skal vi implementere en Retrieval Augmented Generation (RAG)-applikasjon som bruker Phi3 som SLM, AI Search som vectorDB og Prompt Flow som lavkode-orchestrator.

## Funksjoner

- Enkel distribusjon med Docker.
- Skalerbar arkitektur for håndtering av AI-arbeidsflyter.
- Lavkode-tilnærming med Prompt Flow.

## Forutsetninger

Før du begynner, sørg for at du har oppfylt følgende krav:

- Docker installert på din lokale maskin.
- En Azure-konto med tillatelser til å opprette og administrere container-ressurser.
- En Azure AI Studio- og Azure AI Search-instans.
- En embedding-modell for å lage indeksen din (kan være enten en Azure OpenAI-embedding eller en OS-modell fra katalogen).
- Python 3.8 eller nyere installert på din lokale maskin.
- Et Azure Container Registry (eller hvilket som helst register du foretrekker).

## Installasjon

1. Opprett en ny flow i ditt Azure AI Studio-prosjekt ved å bruke flow.yaml-filen.
2. Distribuer en Phi3-modell fra Azure AI modellkatalogen din og opprett tilkoblingen til prosjektet ditt. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Opprett vector-indeksen i Azure AI Search ved å bruke et hvilket som helst dokument du ønsker [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Distribuer flowen på en administrert endepunkt og bruk den i prompt-flow-frontend.py-filen. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klon depotet:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bygg Docker-imaget:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Push Docker-imaget til Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Bruk

1. Kjør Docker-containeren:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Åpne applikasjonen i nettleseren på `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Full artikkel: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på det opprinnelige språket bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.