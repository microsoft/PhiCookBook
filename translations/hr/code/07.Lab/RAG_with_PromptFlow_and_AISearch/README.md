## RAG s PromptFlow i AISearch

U ovom primjeru implementirat ćemo Retrieval Augmented Generation (RAG) aplikaciju koristeći Phi3 kao SLM, AI Search kao vectorDB i Prompt Flow kao low-code orkestrator.

## Značajke

- Jednostavna implementacija pomoću Dockera.
- Skalabilna arhitektura za upravljanje AI radnim tokovima.
- Low-code pristup koristeći Prompt Flow

## Preduvjeti

Prije nego što započnete, provjerite jeste li ispunili sljedeće uvjete:

- Docker instaliran na vašem lokalnom računalu.
- Azure račun s dopuštenjima za kreiranje i upravljanje kontejnerskim resursima.
- Azure AI Studio i Azure AI Search instance
- Embedding model za izradu indeksa (može biti Azure OpenAI embedding ili OS model iz kataloga)
- Python 3.8 ili noviji instaliran na vašem lokalnom računalu.
- Azure Container Registry (ili bilo koji registar po vašem izboru)

## Instalacija

1. Kreirajte novi flow u vašem Azure AI Studio projektu koristeći flow.yaml datoteku.
2. Implementirajte Phi3 model iz vašeg Azure AI model kataloga i povežite ga s projektom. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Kreirajte vector indeks na Azure AI Search koristeći bilo koji dokument po vašem izboru [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Implementirajte flow na managed endpoint i koristite ga u datoteci prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonirajte repozitorij:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Izgradite Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Pošaljite Docker image u Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Korištenje

1. Pokrenite Docker kontejner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Pristupite aplikaciji u pregledniku na `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Cijeli članak: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.