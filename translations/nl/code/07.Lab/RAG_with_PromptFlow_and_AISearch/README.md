<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-16T17:09:21+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "nl"
}
-->
## RAG met PromptFlow en AISearch

In dit voorbeeld implementeren we een Retrieval Augmented Generation (RAG) applicatie waarbij Phi3 wordt gebruikt als SLM, AI Search als vectorDB en Prompt Flow als low-code orkestrator.

## Kenmerken

- Eenvoudige implementatie met Docker.
- Schaalbare architectuur voor het afhandelen van AI-workflows.
- Low-code aanpak met Prompt Flow.

## Vereisten

Voordat je begint, zorg ervoor dat je aan de volgende voorwaarden voldoet:

- Docker geïnstalleerd op je lokale machine.
- Een Azure-account met rechten om containerresources te maken en beheren.
- Een Azure AI Studio en Azure AI Search instantie.
- Een embeddingmodel om je index te maken (dit kan een Azure OpenAI embedding zijn of een OS-model uit de catalogus).
- Python 3.8 of hoger geïnstalleerd op je lokale machine.
- Een Azure Container Registry (of een andere registry naar keuze).

## Installatie

1. Maak een nieuwe flow aan in je Azure AI Studio-project met behulp van het flow.yaml bestand.
2. Implementeer een Phi3 Model vanuit je Azure AI modelcatalogus en maak de verbinding met je project. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Maak de vectorindex aan in Azure AI Search met een document naar keuze. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Implementeer de flow op een managed endpoint en gebruik deze in het prompt-flow-frontend.py bestand. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone de repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bouw de Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Push de Docker image naar Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Gebruik

1. Start de Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Open de applicatie in je browser via `http://localhost:8501`.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Volledig artikel: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.